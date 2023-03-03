import requests
import random
import string


print("Tnitro kod üreteciye hoş geldin ben M...... E....  Bu, nitro kodları üretecek ve kodun geçerli olup olmadığını kontrol edecektir. Kod geçerliyse, kodu 2 satır bırakarak yazdırır ve geçerli değilse yazdırır '*'.\n\n\n")
num = int(input('Oluşturulacak ve Kontrol Edilecek  Kod sayısını girin Girin:\n'))


with open("Nitro Kod.txt", "w", encoding='utf-8') as file:
    print("Nitro kodlarınız oluşturuluyor, sabırlı olun!")

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"oluşturuldu {num} Kodlar\n")

with open("Nitro Kod.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\n Geçerli | {nitro}\n\n") 
        else:
            print(f"*", end = "")  

print("\n\n\nKodları oluşturdunuz ve başarıyla kontrol ettiniz, umarım bazı geçerli kodlarınız vardır.")
