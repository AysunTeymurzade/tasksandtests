from datetime import datetime
gunler = {
    0: "Bazar ertəsi: başlanğıclar üçün əla gündür!",
    1: "Çərşənbə axşamı: sabitlik gətirər.",
    2: "Çərşənbə: ruhdan düşmə!",
    3: "Cümə axşamı: sona bir addım var!",
    4: "Cümə: zəhmətini qiymətləndirmə vaxtı!",
    5: "Şənbə: özün üçün nələrsə et.",
    6: "Bazar: dincəl və ruhunu bəslə."
}
bugun = datetime.now().weekday()
print("Motivasiya: ", gunler[bugun])
