import urequests
import network
import time
from machine import Pin, ADC
import dht

# Koneksi WiFi
WIFI_SSID = "YEFTA"
WIFI_PASSWORD = "085705652088"

# Token Ubidots
UBIDOTS_TOKEN = "BBUS-5nqw3d0di3rtPT3fW2MrkYFpRMEAow"
DEVICE_LABEL = "sic"
UBIDOTS_URL = f"http://industrial.api.ubidots.com/api/v1.6/devices/sic"

# URL Local API
LOCAL_API_URL = "http://192.168.1.3:5000/api/sensor"

# Koneksi WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print("Menghubungkan ke WiFi...")
        time.sleep(1)
    print("Terhubung ke WiFi!")

# Inisialisasi Sensor
dht_sensor = dht.DHT11(Pin(4))
ldr_sensor = ADC(Pin(32))
ldr_sensor.atten(ADC.ATTN_11DB)

# Kirim data ke Ubidots
def send_data(temp, hum, light):
    data = {
        "temperature": temp,
        "humidity": hum,
        "light_intensity": light
    }
    headers = {
        "X-Auth-Token": UBIDOTS_TOKEN,
        "Content-Type": "application/json"
    }
    response = urequests.post(UBIDOTS_URL, json=data, headers=headers)
    print("Ubidots Response:", response.text)
    response.close()

# Kirim data ke API lokal
def send_to_local_api(temp, hum, light):
    data = {
        "temperature": temp,
        "humidity": hum,
        "light_intensity": light
    }
    response = urequests.post(LOCAL_API_URL, json=data)
    print("Local API Response:", response.text)

# Loop Utama
connect_wifi()
while True:
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        light_intensity = ldr_sensor.read() / 4095 * 100  # Convert ke persentase
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Light: {light_intensity}%")
        send_data(temperature, humidity, light_intensity)
        send_to_local_api(temperature, humidity, light_intensity)
        time.sleep(10)
    except Exception as e:
        print("Error:", e)
