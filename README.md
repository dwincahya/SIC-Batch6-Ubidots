# IoT Project: Menghubungkan Sensor LDR dan DHT11 ke Ubidots dan MongoDB menggunakan ESP8266

Proyek ini merupakan contoh implementasi IoT yang menghubungkan sensor LDR (Light Dependent Resistor) dan DHT11 (sensor suhu dan kelembaban) ke platform Ubidots dan database MongoDB menggunakan modul ESP8266. Data dari sensor dikirim ke Ubidots untuk visualisasi dan ke MongoDB untuk penyimpanan jangka panjang.

## Daftar Isi
- [Komponen yang Dibutuhkan](#komponen-yang-dibutuhkan)
- [Instalasi dan Setup](#instalasi-dan-setup)
- [Skema Rangkaian](#skema-rangkaian)
- [Konfigurasi Ubidots](#konfigurasi-ubidots)
- [Konfigurasi MongoDB](#konfigurasi-mongodb)
- [Cara Menggunakan](#cara-menggunakan)
- [Lisensi](#lisensi)

## Komponen yang Dibutuhkan
1. Modul ESP8266 (NodeMCU atau Wemos D1 Mini)
2. Sensor DHT11
3. Sensor LDR
4. Resistor 10kΩ (untuk LDR)
5. Kabel jumper
6. Breadboard
7. Micro USB cable

## Instalasi dan Setup
1. **Instal Arduino IDE**: Pastikan Arduino IDE sudah terinstal di komputer Anda. Jika belum, unduh dari [situs resmi Arduino](https://www.arduino.cc/en/software).
2. **Tambahkan Board ESP8266**: Buka `File > Preferences` dan tambahkan URL berikut ke `Additional Boards Manager URLs`:
   http://arduino.esp8266.com/stable/package_esp8266com_index.json
Kemudian, buka `Tools > Board > Boards Manager`, cari `esp8266`, dan instal.
3. **Instal Library yang Dibutuhkan**:
- Library DHT: `DHT sensor library` oleh Adafruit
- Library Ubidots: `Ubidots ESP8266` oleh Ubidots
- Library ArduinoJson: `ArduinoJson` oleh Benoit Blanchon
- Library MongoDB: `MongoDB` (gunakan library yang sesuai untuk koneksi ke MongoDB, atau gunakan HTTP client untuk mengirim data ke backend)

## Konfigurasi Ubidots
1. Buat akun di [Ubidots](https://ubidots.com/) jika belum memiliki.
2. Buat device baru di Ubidots dan tambahkan dua variabel:
- `temperature` (untuk data suhu)
- `light_intensity` (untuk data intensitas cahaya)
3. Dapatkan token API dari Ubidots untuk mengirim data.

## Konfigurasi MongoDB
1. Buat database MongoDB (gunakan MongoDB Atlas untuk cloud atau instal MongoDB lokal).
2. Buat collection untuk menyimpan data sensor.
3. Buat API endpoint (misalnya menggunakan Node.js atau Python) untuk menerima data dari ESP8266 dan menyimpannya ke MongoDB.

## Cara Menggunakan
1. Sambungkan perangkat sesuai skema rangkaian.
2. Upload kode ke ESP8266 (lihat file terpisah untuk kode pemrograman).
3. Buka dashboard Ubidots untuk memantau data sensor.
4. Periksa database MongoDB untuk melihat data yang tersimpan.

