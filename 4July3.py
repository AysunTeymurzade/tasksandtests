insanlar = [
    {"ad": "Sona", "yas": 22},
    {"ad": "Aysun", "yas": 24},
    {"ad": "Kamran", "yas": 27},
    {"ad": "Zəhra", "yas": 19}
]
filtr = int(input("Neçə yaşdan yuxarıları göstərək? "))
for insan in insanlar:
    if insan["yas"] >= filtr:
        print(f"{insan['ad']} - {insan['yas']} yaş")