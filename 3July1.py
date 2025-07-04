qonaqlar = ["Aysel", "Murad", "Samir", "Leyla"]
while True:
    emr = input("Əlavə et / Axtar / Çıx: ").lower()
    if emr == "əlavə et":
        yeni = input("Yeni qonağın adını yaz: ")
        if yeni in qonaqlar:
            print("Bu ad artıq mövcuddur.")
        else:
            qonaqlar.append(yeni)
            print("Əlavə olundu.")
    elif emr == "axtar":
        ad = input("Axtarılan ad: ")
        tapildi = any(ad.lower() in q.lower() for q in qonaqlar)
        if tapildi:
            print("Qonaq siyahıda var.")
        else:
            print("Tapılmadı.")
    elif emr == "çıx":
        break
    else:
        print("Əmr tanınmadı.")