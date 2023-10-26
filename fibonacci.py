# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
#Fibonacci dizisi => her sayının kendinden önceki ile toplanması sonucu oluşan bir sayı dizisidir. 
#Fibonacci dizisi => 1,1,2,3,5,8,13....

a = 1
b = 1

fibonacci = [a ,b]

for i in range(21):
    a, b = b , a+b
    fibonacci.append(b)

print(fibonacci)


    
