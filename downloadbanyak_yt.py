
import os
from pytube import YouTube

# Masukkan daftar url disini,
video_urls = [
 'https://www.youtube.com/watch?v=dcQybaUEoKo&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=1',
 'https://www.youtube.com/watch?v=r7ISc8__D28&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=2',
 'https://www.youtube.com/watch?v=CBhCXYE60ro&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=3',
 'https://www.youtube.com/watch?v=NpAmLQnPkCc&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=4',
 'https://www.youtube.com/watch?v=lexLquKmcTI&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=5',
 'https://www.youtube.com/watch?v=L3uPovbd-hk&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=6',
 'https://www.youtube.com/watch?v=YUxZdzzaXQg&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=7',
 'https://www.youtube.com/watch?v=Dq9AE-OkWKw&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=8',
 'https://www.youtube.com/watch?v=HmFnBkNbt7E&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=9',
 'https://www.youtube.com/watch?v=XSkhAm0SzM0&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=10',
 'https://www.youtube.com/watch?v=dQW_SDcXDNg&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=11',
 'https://www.youtube.com/watch?v=kRsq3HxZX_U&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=12',
 'https://www.youtube.com/watch?v=9iRvd0OhH74&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=13',
 'https://www.youtube.com/watch?v=Z5u5vridU6Q&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=14',
 'https://www.youtube.com/watch?v=kTspiE5Vylw&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=15',
 'https://www.youtube.com/watch?v=dWt9EZ2fo2A&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=16',
 'https://www.youtube.com/watch?v=eZS0Nxky9sE&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=17',
 'https://www.youtube.com/watch?v=nY1UfyuBpvU&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=18',
 'https://www.youtube.com/watch?v=sgGPbtYBJ5Q&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=19',
 'https://www.youtube.com/watch?v=WWNH5y_qI_g&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=20',
 'https://www.youtube.com/watch?v=SeNfQDvTZbU&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=21',
 'https://www.youtube.com/watch?v=pQcGSXEb97M&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=22',
 'https://www.youtube.com/watch?v=WeY_q3L9qkc&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=23',
 'https://www.youtube.com/watch?v=-0foEVbZCK4&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=24',
 'https://www.youtube.com/watch?v=qhUpVGgFH4Q&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=25',
 'https://www.youtube.com/watch?v=jmCc0Ese2Vk&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=26',
 'https://www.youtube.com/watch?v=Mm3-gk9bdiE&list=UULFdd9POu1PHwW7k8oiuWPweQ&index=27'
]


# Tentukan nama folder unduhan
download_folder_name = "lagu_anak_anak"
download_folder = os.path.join(os.path.expanduser("~/Downloads"), download_folder_name)

# Buat folder jika belum ada
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Loop melalui setiap URL dalam daftar dan lakukan proses unduhan
for url in video_urls:
    # Dapatkan stream dengan resolusi tertinggi
    stream = YouTube(url).streams.get_highest_resolution()

    # Tentukan nama file untuk unduhan
    video_title = stream.title
    resolution = stream.resolution
    video_file = os.path.join(download_folder, f"{video_title.replace('|', '_')}_{resolution}.mp4")

    # Cek apakah file sudah ada
    if os.path.exists(video_file):
        print(f"File already exists: {video_file}")
        print("Skipping...\n")
        continue

    # Tampilkan informasi video tanpa mengunduh
    print(f"Video Title: {stream.title}")
    print(f"Resolution: {stream.resolution}")
    print(f"Filesize: {stream.filesize / (1024 * 1024):.2f} MB")
    print(f"Video URL: {url}")

    # Hilangkan bagian berikut ini jika Anda tidak ingin mengunduh
    print(f"\nDownloading {url}")
    # Download video
    stream.download(output_path=download_folder, filename=f"{video_title.replace('|', '_')}_{resolution}.mp4")
    print(f"Download complete! Resolution: {resolution}\n")

