---
kategori: "Kategori adı"
seviye: "temel | orta | ileri"
etiketler: []
guncelleme: "YYYY-AA-GG"
---

## Kart Başlığı

**Kısa tanım:** Tek cümlede ne olduğu.

**Eşik / Formül:**
- Sayısal kural veya formül burada.

**Nasıl çalışır:** Fiziksel mekanizma, 3–5 cümle.

**Günlük hayattan örnek:** Somut, yerel bir örnek.

**Sık yapılan hata:** Yanlış bilinen nokta ve doğrusu.

**Kaynaklar:**
1. Kaynak adı — kısa not (hangi değeri verdiği)
2. Kaynak adı — kısa not
3. Kaynak adı — kısa not

> **Tutarlılık:** 🟢 Yüksek (3/3 kaynak hemfikir) · Son doğrulama: YYYY-AA-GG
> Çelişki: — *(varsa buraya yazılır)*

---

### AI agent için üretim talimatı (prompt özeti)

1. Konu için en az 3 bağımsız kaynak topla (tercih sırası: MGM, NOAA/NWS, ECMWF, Met Office, DWD, üniversite ders notu, Wikipedia).
2. Her kaynaktan sayısal eşiği ve tanımı ayrı ayrı çıkar.
3. Eşikler karşılaştır: tümü aynıysa 🟢, ±%20 içindeyse 🟡 ve aralık ver, dışındaysa 🔴 ve `Çelişki:` satırını doldur.
4. Yukarıdaki şablonu **birebir** doldur; alan atlama, sıra değiştirme.
5. 🔴 olan kartı `taslak/` klasörüne yaz, `kartlar/` altına yazma.
