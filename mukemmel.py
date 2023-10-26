# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.
# Mükemmel Sayı => Bazı pozitif tam sayıların pozitif bölenleri toplamı, sayının kendisinin iki katına eşit olması.
# 6 => 1, 2, 3, 6 
# toplam = 1 + 2 + 3 + 6 = 12 

sayi = int(input("pozitif bir sayı giriniz: "))
toplam = 0

for i in range(1,sayi+1):
    if sayi %i == 0:
        toplam += i

print(toplam)

if sayi*2 == toplam:
    print(str(sayi) + " mükemmel sayıdır.")

else:
    print("Mükemmel sayı değildir.")