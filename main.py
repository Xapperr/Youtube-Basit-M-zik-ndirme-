import os
from pytube import YouTube
link = input("Lütfen bir link girin: ")

print("Girilen Link:", link)

klasor = "Indirilenler"
if not os.path.exists(klasor):
    os.mkdir(klasor)
    print(f"{klasor} klasörü oluşturuldu...")
else:
    print(f"{klasor} klasörü zaten mevcut...")
print(f"{klasor} klasörü bulundu...")


try:
    yt = YouTube(link)
except:
    print("Bir şeyler ters gitti...")
    exit()
music=yt.streams.filter(only_audio=True).first()



print("İndiriliyor")
cikis=music.download(klasor)
baslangicyolu, _ =os.path.splitext(cikis)
print(baslangicyolu)
donustur=baslangicyolu+".mp3"
os.rename(cikis,donustur)
print("İndirme tamamlandı...")
