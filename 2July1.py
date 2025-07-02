import time
saniye = 15  # Taymerin müddəti 15 saniyədir.
while saniye > 0:
    print(saniye)
    time.sleep(1) #1 saniyə gözləmə müddətini göstərir. 
    saniye -= 3  # Saniyəni üç-üç azaldır.
print("Vaxt bitdi!")