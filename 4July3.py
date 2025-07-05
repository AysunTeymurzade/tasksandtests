insanlar = [
    {"ad": "Sona", "yas": 19},
    {"ad": "Aysun", "yas": 22},
    {"ad": "Kamil", "yas": 27},
    {"ad": "Zəhra", "yas": 17}
]
filtr = int(input("Neçə yaşdan yuxarıları göstərək? "))
for insan in insanlar:
    if insan["yas"] >= filtr:
        print(f"{insan['ad']} - {insan['yas']} yaş")
uygunlar = [i for i in insanlar if i["yas"] >= filtr]
if not uygunlar:
    print("Bu yaşdan yuxarı heç kim tapılmadı.")
else:
    for insan in uygunlar:
        print(f"{insan['ad']} - {insan['yas']} yaş")
