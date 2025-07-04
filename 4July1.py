from datetime import datetime
bugun = datetime.now()
aylar = {
    1: "Qışın başlanğıcı", 2: "Səbr ayı", 3: "Yenilənmə",
    4: "Çiçəkləmə", 5: "İrəliləyiş", 6: "Yay həyəcanı",
    7: "Günəşli çağ", 8: "Dincəlmə", 9: "Dəyişiklik",
    10: "Sakitlik", 11: "Kədərli sükut", 12: "Qapanış"
}
gun = bugun.day
ay = bugun.month
print(f"Bu gün {gun}-ci gündür, ayın adı: {aylar[ay]}")