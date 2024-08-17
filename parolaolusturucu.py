import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Şifre uzunluğunu giriniz: "))
parola = ""

if uzunluk < 5:
    print("Şifreniz çok kısa")
elif uzunluk > 25:
    print("Şifreniz çok uzun")
else:
    for i in range(uzunluk):
        parola = parola + random.choice(karakterler)
    print("oluşturulan parola", parola)
