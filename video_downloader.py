import os
import yt_dlp

def create_videos_folder():
    if not os.path.exists('videos'):
        os.makedirs('videos')
        print("'videos' klasörü oluşturuldu.")

def download_video(url, platform):
    create_videos_folder()
    
    ydl_opts = {
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'format': 'best',
        'quiet': True,  # Çıktıyı gizler
        'no_warnings': True  # Uyarıları gizler
    }
    
    # X (Twitter) için özel ayarlar
    if platform == "x":
        ydl_opts['format'] = 'best'
    
    # Instagram için özel ayarlar
    elif platform == "instagram":
        ydl_opts['format'] = 'best'
        
    # YouTube için özel ayarlar
    elif platform == "youtube":
        ydl_opts['format'] = 'best'
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video başarıyla indirildi!")
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")

def main():
    while True:
        print("\n1 - X (Twitter) Video İndir")
        print("2 - Instagram Reels İndir")
        print("3 - YouTube Shorts İndir")
        print("4 - Çıkış")
        
        secim = input("Seçiminiz (1-4): ")
        
        if secim == "1":
            url = input("X (Twitter) video URL'sini girin: ")
            download_video(url, "x")
        elif secim == "2":
            url = input("Instagram Reels URL'sini girin: ")
            download_video(url, "instagram")
        elif secim == "3":
            url = input("YouTube Shorts URL'sini girin: ")
            download_video(url, "youtube")
        elif secim == "4":
            print("Program kapatılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main() 