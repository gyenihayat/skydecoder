#!/usr/bin/env python3
"""Ziyaretçilerin 'Merak ettikleriniz' bölümüne yazdığı talepleri indirir ve talepler.txt'ye yazar.

Kullanım:  python3 talepler.py
Sonra talepler.txt dosyasını açıp kart üretilecek konuları seçin.
"""
import urllib.request
from pathlib import Path

SITE = "https://skydecoder.vercel.app"
PANEL_KODU = "cbe9k1"  # gizli panel ile aynı kod (#stat-cbe9k1)
HEDEF = Path(__file__).parent / "talepler.txt"

with urllib.request.urlopen(f"{SITE}/api/talep?kod={PANEL_KODU}&format=txt", timeout=30) as r:
    metin = r.read().decode("utf-8")
HEDEF.write_text(metin, encoding="utf-8")
adet = sum(1 for line in metin.splitlines() if line[:1].isdigit())
print(f"{adet} talep -> {HEDEF}")
