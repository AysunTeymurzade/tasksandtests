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
