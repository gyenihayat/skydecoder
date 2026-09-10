---
kategori: "Açık Veri ve Sensörler"
seviye: "ileri"
etiketler: ["API", "sensör", "ESP32", "Netatmo", "open-meteo", "MQTT", "harita"]
guncelleme: "2026-09-08"
---

## Açık Sensör Ağları ve Ücretsiz API'ler

**Kısa tanım:** Binlerce amatör ve resmî sensör, anlık sıcaklık, nem ve basınç verisini açık olarak paylaşır. Sitenize canlı bir veri katmanı eklemek için bu kaynaklar yeterlidir; çoğu ücretsiz ve JSON döner.

**Eşik / Formül:**

| Kaynak | Veri | Erişim | Kapsam / Not |
|---|---|---|---|
| **Open-Meteo API** | Model tahmini + geçmiş + anlık (ECMWF, GFS, ICON…) | Ücretsiz, anahtar gerekmez, 10.000 istek/gün | `api.open-meteo.com/v1/forecast?latitude=39.9&longitude=32.8&current=temperature_2m,dew_point_2m` — en kolay başlangıç |
| **Netatmo Weathermap** | Amatör istasyon anlık sıcaklık/nem/basınç | Ücretsiz API (OAuth), `getpublicdata` | Türkiye'de büyük şehirlerde yüzlerce istasyon; yerleşim hatası olabilir |
| **Weather Underground PWS** | Kişisel istasyon ağı | Ücretsiz anahtar yalnız istasyon sahiplerine | Yaygın; yalnızca kendi istasyonunuz varsa API |
| **Sensor.Community** (eski Luftdaten) | Açık donanım sıcaklık/nem/PM2.5 | Tamamen açık, `data.sensor.community` | Hava kalitesi odaklı; Türkiye'de sınırlı |
| **OpenWeatherMap** | Anlık + tahmin | Ücretsiz seviye 1.000 istek/gün | Kolay, ama kaynak şeffaf değil |
| **NOAA / Synoptic (MesoWest)** | Resmî ve mesonet istasyonlar | Ücretsiz akademik seviye | Türkiye için MGM SYNOP istasyonları dahil |
| **MGM** | Resmî istasyon anlık verisi | Resmî API yok; web sayfası gösterir | Kurumsal başvuru ile veri alınabilir |
| **OGIMET** | Dünya SYNOP/METAR arşivi | Ücretsiz web | Türkiye istasyonlarının 3 saatlik geçmişi |
| **METAR (havalimanları)** | Anlık gözlem | `aviationweather.gov/data/api` — ücretsiz | LTAC Esenboğa, LTFM İstanbul vb. — en güvenilir kalibre veri |

**Nasıl çalışır:** Amatör ağlar veriyi kullanıcının cihazından buluta, oradan API'ye taşır. Resmî istasyonlar WMO standartlarında (2 m yükseklik, gölgede, çimen üstünde) ölçer; amatör sensörler balkonda güneş görebilir, duvara yakın olabilir. Bu yüzden sitenizde **kaynak tipini** (resmî / amatör) her sensör noktasında gösterin.

**Günlük hayattan örnek:** Ankara için Open-Meteo'dan model sıcaklığı, Esenboğa METAR'dan resmî ölçüm, Netatmo'dan Çankaya'daki 30 amatör istasyonun ortalamasını aynı haritada gösterin: aradaki 2–3°C fark, kentsel ısı adası kartını canlı olarak doğrular.

**Sık yapılan hata:** Amatör istasyon verisini filtrelemeden ortalamaya katmak. Güneş gören sensör öğlen 5–8°C yüksek gösterir; komşularından 3°C'den fazla sapan istasyonu dışarıda bırakın (medyan filtre).

**Kaynaklar:**
1. Open-Meteo dokümantasyonu — API parametreleri ve limitler
2. Netatmo Developer Portal — `getpublicdata` uç noktası
3. WMO Guide No. 8 — istasyon yerleşim standartları

> **Tutarlılık:** 🟡 Orta (kaynak listesi güncel; limitler ve ücretler değişken) · Son doğrulama: 2026-09-08
> Çelişki: — API limitleri ve ücretsiz seviyeler sık değişir; **bu kart 3 ayda bir yeniden doğrulanmalıdır.**

---

## Kendi Sensörünüzü Siteye Bağlama

**Kısa tanım:** 15 dolarlık bir ESP32 kartı ve BME280 sensörü ile 5 dakikada bir sıcaklık, nem ve basınç ölçüp sitenize gönderebilirsiniz. Veri MQTT veya basit bir HTTP POST ile bir veritabanına yazılır, site oradan okur.

**Eşik / Formül:**
- Donanım: ESP32 (Wi-Fi) + BME280 (sıcaklık ±1°C, nem ±3 %, basınç ±1 hPa) + radyasyon kalkanı (güneş koruması, şart)
- Ölçüm aralığı: 5–10 dakika; daha sık gereksiz, pil ve API yükü artar
- Veri akışı: `ESP32 → MQTT broker (Mosquitto) veya HTTP POST → Supabase / InfluxDB / basit JSON dosyası → site`
- Kalite kontrol: 1 saatte > 5°C sıçrama → "şüpheli" işaretle; nem > %100 → kırp; 3 ölçüm arka arkaya eksik → "çevrimdışı"
- Deniz seviyesine indirgenmiş basınç: `P₀ = P × (1 − 0,0065·h / (T + 0,0065·h + 273,15))^(−5,257)` (h: metre, T: °C)

**Nasıl çalışır:** Sensör I²C üzerinden ESP32'ye bağlanır. ESP32 Wi-Fi ile ölçümü JSON olarak gönderir: `{"id":"ank-cankaya-01","t":18.4,"rh":42,"p":907.1,"ts":"2026-09-08T14:05:00Z"}`. Sunucu tarafında bir Supabase tablosu veya statik site için GitHub Actions ile her 10 dakikada güncellenen bir `data.json` yeterlidir. Site, Leaflet haritasına nokta olarak çizer ve son 24 saat grafiğini gösterir.

**Günlük hayattan örnek:** Balkona kurduğunuz sensör sabah 07:00'de 4°C ve çiğ noktası 3,5°C gösteriyor; site otomatik olarak "Sis riski yüksek" rozeti ve "Çiğ noktası" kartına bağlantı verir. Bu, sitenin eğitim ve canlı veri katmanını birleştiren en değerli özelliktir.

**Sık yapılan hata:** Sensörü duvara veya güneş gören yere asmak. Radyasyon kalkanı olmadan ölçülen sıcaklık gündüz 5–10°C yüksek çıkar; verinin tamamı anlamsız olur. Kalkanı 3D yazıcı ile basabilir ya da iç içe geçmiş beyaz plastik tabaklarla yapabilirsiniz.

**Kaynaklar:**
1. Bosch BME280 datasheet — doğruluk değerleri
2. WMO Guide No. 8 — radyasyon kalkanı ve 2 m yükseklik standardı
3. Espressif ESP32 + Arduino MQTT örnekleri — bağlantı kodu

> **Tutarlılık:** 🟢 Yüksek (3/3 kaynak hemfikir) · Son doğrulama: 2026-09-08
> Çelişki: —
