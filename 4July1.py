from datetime import datetime
bugun = datetime.now()
aylar = {
    1: "Başlanğıc", 2: "Səbir", 3: "Yenilənmə",
    4: "Çiçəkləmə", 5: "İrəliləyiş", 6: "Həyəcan",
    7: "Istilik", 8: "Dincəlmə", 9: "Dəyişiklik",
    10: "Sakitlik", 11: "Sükut", 12: "Son"
}
gun = bugun.day
ay = bugun.month
print(f"Bu gün {gun}-ci gündür, ayın adı: {aylar[ay]}")
