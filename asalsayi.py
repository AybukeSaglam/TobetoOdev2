# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız. 
# Asal sayı => Kendisinden ve 1’den başka böleni olmayan sayılar.
# 2, 3, 5, 7, 11........



sayi = int(input("Bir sayi giriniz: "))

if sayi > 1:
    for i in range (2,sayi):
        if sayi % i == 0 :
            print("Asal sayı değil")
            break
        else:
            print("Sayı asaldır.")
            break

else:
    print("geçerli sayı giriniz")