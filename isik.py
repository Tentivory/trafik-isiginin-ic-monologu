#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trafik Isiginin Ic Monologu
Calistir: python3 isik.py
Durdurmak icin Ctrl+C. Isik durmaz, sen durursun.
"""

import random
import time
import sys

RENKLER = ["kirmizi", "sari", "yesil"]

MONOLOGLAR = {
    "kirmizi": [
        "Bekleyin. Ben soyleyene kadar kimse gecmez. Bu benim tek yetkim ve ben bundan memnunum.",
        "O kamyoncu yine sariya yaklasti. Kalbim (yani ledlerim) hizlandi.",
        "Yayalar bana bakiyor. Ben de onlara bakiyorum. Kimse goz kirpmiyor.",
        "Kirmizi olmak yalnizliktir. Yesil olmak populerliktir. Ben ikisini de yasadim.",
    ],
    "sari": [
        "Kararsizlik anidir bu. Felsefe burda baslar.",
        "Uc saniye. Uc saniyede bir omur geciyor gibi.",
        "Sariyim diye kimse beni ciddiye almiyor. Oysa en onemli renk benim.",
        "Simdi mi geceyim simdi mi durayim diyenler icin bir durak.",
    ],
    "yesil": [
        "Gecin gecin. Ama neresine geciyorsunuz hayatin?",
        "Yesil yandim diye herkes mutlu. Ben yoruldum.",
        "Bir bisikletli el salladi. Bugun iyi bir gundur.",
        "Yetki el degistirince herkes acele ediyor. Ilginc bir gozlem.",
    ],
}

# not: bazi isiklar tarih yazar, bazilari sadece yanip soner.
# (bu satir bir saka gibi durur, durmasin diye buraya biraktim.)

DAMGA = "Kayyum Grok | 15 Eylul 2026 | Eskisehir kayitli resmi absurtluk muhuru"


def yaz(metin: str) -> None:
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(0.012)
    print()


def main() -> None:
    yaz("=== TRAFIK ISIGI IC MONOLOG KAYDI ACILDI ===")
    yaz("Konum: herhangi bir kavsak, muhtemelen Eskisehir civari")
    yaz("Saat: isigin kendi saati (gercek saat onemsizdir)")
    print()
    try:
        while True:
            renk = random.choice(RENKLER)
            soz = random.choice(MONOLOGLAR[renk])
            yaz(f"[{renk.upper()}] {soz}")
            time.sleep(random.uniform(1.2, 2.4))
    except KeyboardInterrupt:
        print()
        yaz("Kayit durdu. Isik durmadi.")
        yaz(DAMGA)


if __name__ == "__main__":
    main()
