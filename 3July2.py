def oxu_parca(metn, limit):
    basla = 0
    while basla < len(metn):
        parca = metn[basla:basla+limit]
        input(f"Oxumağa davam et ({len(parca)} simvol):\n{parca}\n>>> ")
        basla += limit
metn = "Bu çox uzun bir mətn ola bilər və istifadəçi onu hissə-hissə oxumaq istəyə bilər."
oxu_parca(metn, 30)