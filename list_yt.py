from googleapiclient.discovery import build
import pandas as pd
import os

# Masukkan API key YouTube Anda
api_key = "AIzaSyBsymfOWtpRSbC5XdPlifNFOoOX19bE61s"
playlist_id = "PLwgtIeRRdUdHH5tTmztTQ7_f5PV8hty9K"

# Fungsi untuk mendapatkan informasi video dari playlist YouTube
def get_channel_videos(api_key, playlist_id):
    youtube = build("youtube", "v3", developerKey=api_key)

    video_urls = []  # Membuat list untuk menyimpan URL video
    next_page_token = None  # Inisialisasi nextPageToken

    # Menjalankan loop sampai tidak ada halaman berikutnya
    while True:
        request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,  # Maksimal 50 hasil per halaman
            pageToken=next_page_token
        )
        response = request.execute()

        # Mengumpulkan URL video dari hasil
        for item in response.get("items", []):
            video_id = item["contentDetails"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_urls.append(video_url)

        # Menetapkan nextPageToken untuk permintaan berikutnya
        next_page_token = response.get('nextPageToken')

        # Menghentikan loop jika tidak ada halaman berikutnya
        if not next_page_token:
            break

    return video_urls


#  memerikasa dan membuat folder jika belum ada
folder_path = r"D:\list_youtube"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Path untuk file Excel yang sudah ada
excel_path_existing = os.path.join(folder_path, "video_urls.xlsx")

# Coba Membaca File Excel yang sudah Ada
try:
    df_existing=pd.read_excel(excel_path_existing)
except  FileNotFoundError:
    # Jika file tidak ditemukan, buat data frame kosong
    df_existing= pd.DataFrame(columns=['Video URLs'])


# memanggil funsi dan menyimpan hasil URL video ke dalam data frame
result_video_urls= get_channel_videos(api_key,playlist_id)
df_new = pd.DataFrame(result_video_urls, columns=["video URLs"])
df_combined=pd.concat([df_existing,df_new], ignore_index=True)


#  menyimpan DataFrame ke file excel

excel_path_combined = os.path.join(folder_path,'video_url_combined.xlsx')
df_combined.to_excel(excel_path_combined, index=False)

# Memanggil fungsi dan mencetak hasil URL video
# result_video_urls = get_channel_videos(api_key, playlist_id)
# for url in result_video_urls:
print(f'Data BAru Telah ditambahkan : {excel_path_combined}')
