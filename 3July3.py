bio = input("İnstagram bio yaz: ")
xasiyyet = []
if any(emoji in bio for emoji in ":sparkles::cherry_blossom::black_heart::sunglasses:"):
    xasiyyet.append("emosional və vizual yönümlü")
if "kitab" in bio or "yazar" in bio:
    xasiyyet.append("ədəbi maraqlı")
if "ALLAH" in bio.upper():
    xasiyyet.append("dini bağlılığı var")
if len(bio) < 30:
    xasiyyet.append("qısa və konkret")
print("Bu bioya əsasən şəxs: ", ", ".join(xasiyyet))