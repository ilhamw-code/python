import pywhatkit as py
import datetime
import time
import pyautogui as klik

# py.sendwhatmsg(f"+6282323066956", "hello testing ke ke 3", datetime.datetime.now().hour,datetime.datetime.now().minute+1)
# time.sleep(1)
# klik.click()
# time.sleep(2)
# klik.press('enter')

# import pywhatkit as py
# import datetime
# import time
# import pyautogui as klik

nomor_telepon = [
    "+6282323066956", 
    "+6285363321614",
    "+6282190218108" 
    ]

def kirim_pesan(nomor, pesan, jam, menit):
    py.sendwhatmsg(nomor, pesan, jam, menit)
    klik.click()
    time.sleep(2)
    klik.press('enter')

for nomor in nomor_telepon:
    kirim_pesan(nomor, """Assalamualaikum bpk/ibu. Mohon perhatian untuk jdwal ujian wawancara dan praktek ibadah sebagai berikut: 
Jalur prestasi  : 6-7 Maret 2024 
Jalur reguler, asrama/ non asrama sesuai dengan nomor ujian yang tertera di kartu pendaftaran. 
001-200 : 5-10 maret 2024
201 - 400 : 12 - 17 Maret 2024
401 - 600 : 19 - 24 Maret 2024
601 - 800 : 26 - 28 Maret 2024.
                """, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
    time.sleep(5)


# # Buat daftar nomor tujuan, pisahkan dengan koma
# nomor_tujuan = "+628363321614"

# # Buat pesan yang ingin Anda kirim
# pesan = "Halo, ini pesan otomatis dari Copilot"

# # Tentukan waktu pengiriman, dalam format jam dan menit
# waktu_jam = 11 # Jam 10 pagi
# waktu_menit = 26 # Menit ke 15

# # Gunakan fungsi sendwhatmsg_bulk untuk mengirim pesan ke banyak nomor
# pywhatkit.sendwhatmsg(nomor_tujuan, pesan, waktu_jam,
#  waktu_menit)
