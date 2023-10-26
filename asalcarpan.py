#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

sayi = int(input("Bir sayı girin: "))  # Kullanıcıdan bir sayı girildi

carpanlar = [] # Asal çarpanları görmek için
bolen = 2  # İlk böleni 2 olarak başlatın

while bolen <= sayi:
    if sayi % bolen == 0:
        # Eğer sayı bölünebiliyorsa, bu, bir asal çarpanı temsil eder
        carpanlar.append(bolen)
        sayi //= bolen  # Sayıyı bölenin sonucuyla güncelleyin
    else:
        bolen += 1  # Böleni bir sonraki sayıya taşıyın

if len(carpanlar) == 0:
    print("Asal bir sayı girdiniz.")
else:
    print(f"Girilen sayının asal çarpanları: {carpanlar}")



