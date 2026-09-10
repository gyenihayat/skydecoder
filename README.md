# Hava Durumu Okuryazarlığı — Bilgi Kartları

Bu klasör, siteyi oluşturacak `.md` kart dosyalarını içerir. Her dosya bir kategori, her `## ` başlığı bir karttır.
Astro / Next.js / Hugo gibi statik site üreticileri bu dosyaları doğrudan okuyabilir.

## Klasör yapısı

```
meteoKnowledge/
├── README.md                     ← bu dosya
├── build.py                      ← kartlar/*.md → site/index.html + site/kartlar.json
├── template.html                 ← sayfa tasarımı ve etkileşimi (build.py veriyi içine gömer)
├── api/istatistik.js             ← ziyaret / kalma süresi sayacı (Vercel Function + Upstash Redis)
├── site/istatistik.html          ← istatistik sayfası
├── vercel.json
├── KART_SABLONU.md               ← yeni kart yazarken / AI agent üretirken kullanılacak şablon
└── kartlar/
    ├── 01-temel-kavramlar.md     ← çiğ noktası, hissedilen sıcaklık, ısı adası, basınç
    ├── 02-dikey-atmosfer.md      ← irtifa-sıcaklık, kar sınırı, dağlarda kar, 850 hPa eşikleri
    ├── 03-yagis-ve-bulutlar.md   ← bulut türleri, yağış şekilleri, dolu, virga
    ├── 04-radar-ve-modeller.md   ← radar okuma, modeller, erişim siteleri
    ├── 05-uygulamali.md          ← araç camında buzlanma, sürücü/dağcı kuralları
    └── 06-acik-veri.md           ← açık sensör ağları, API'ler, kendi sensörünü ekleme
```

## Kart yapısı (her kartta aynı sıra)

| Alan | Açıklama |
|---|---|
| **Kısa tanım** | 1–2 cümle, teknik olmayan dil |
| **Eşik / Formül** | Sayısal kural, formül veya tablo |
| **Nasıl çalışır** | Fiziksel açıklama |
| **Günlük hayattan örnek** | Türkiye'den somut örnek |
| **Sık yapılan hata** | Yanlış bilinen nokta |
| **Kaynaklar** | Kartın dayandığı 2–4 kaynak |
| **Tutarlılık** | Kaynakların ne kadar hemfikir olduğu (aşağıya bak) |

## Tutarlılık göstergesi

Her kartın sonunda şu satır bulunur:

```
> **Tutarlılık:** 🟢 Yüksek (3/3 kaynak hemfikir) · Son doğrulama: 2026-09-08
```

| Simge | Anlamı |
|---|---|
| 🟢 Yüksek | Tüm kaynaklar aynı değeri/açıklamayı veriyor |
| 🟡 Orta | Kaynaklar sayısal eşikte ±%20 içinde farklılaşıyor; aralık verildi |
| 🔴 Düşük | Kaynaklar çelişiyor, yayın öncesi insan onayı gerekli |

Not alanındaki `Çelişki:` satırı, kaynakların nerede ayrıştığını açıkça yazar.

## Frontmatter (site üreticisi için)

Her dosyanın başındaki YAML bloğu kategori, seviye ve etiketleri taşır. Astro Content Collections için `src/content/kartlar/` altına kopyalamanız yeterlidir.

## Siteyi üretmek ve yayınlamak

```
python3 build.py        # site/index.html ve site/kartlar.json üretir
```

Yayın: https://hava-okuryazarligi.vercel.app — `main` dalına her push Vercel'de otomatik yayınlanır.
İstatistik sayfası `/istatistik`; veriyi Upstash Redis'te tutar (`KV_REST_API_URL`, `KV_REST_API_TOKEN`).
