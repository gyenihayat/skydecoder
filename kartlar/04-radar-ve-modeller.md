---
kategori: "Radar ve Modeller"
seviye: "orta"
etiketler: ["radar", "dBZ", "GFS", "ECMWF", "ICON", "ensemble", "Windy"]
guncelleme: "2026-09-08"
---

## Radar Görüntüsü Nasıl Okunur?

**Kısa tanım:** Hava radarı bir mikrodalga sinyal gönderir ve yağış taneciklerinden geri yansıyan gücü ölçer. Bu güç "yansıtıcılık" (dBZ) olarak renklendirilir; renk yağışın türünü değil şiddetini gösterir.

**Eşik / Formül:**

| dBZ | Renk (yaygın palet) | Anlamı | Yaklaşık yağış şiddeti |
|---|---|---|---|
| < 15 | Açık mavi / gri | Çisenti, bulut, kuş, böcek | < 0,3 mm/sa |
| 15–30 | Mavi–yeşil | Hafif yağmur, kar | 0,3–3 mm/sa |
| 30–40 | Yeşil–sarı | Orta yağmur | 3–12 mm/sa |
| 40–50 | Sarı–turuncu | Kuvvetli sağanak | 12–50 mm/sa |
| 50–60 | Kırmızı | Şiddetli sağanak, küçük dolu olası | 50–100 mm/sa |
| > 60 | Mor / beyaz | Büyük dolu neredeyse kesin | — |

- Kar için değerler 5–10 dBZ daha düşük okunur (kar zayıf yansıtır; 25 dBZ kar zaten yoğundur).
- **Parlak bant (bright band):** Erime seviyesinde eriyen kar, ıslak yüzeyi nedeniyle aşırı yansıtır; radarda halka şeklinde sahte "kuvvetli yağış" şeridi görülür.
- **Yer yankısı (ground clutter):** Radar çevresindeki dağlar ve binalar sabit lekeler yapar.
- **Anormal yayılım:** İnversiyon gecelerinde demet yere kırılır, olmayan "yağış" görünür (özellikle sakin, açık gecelerde).
- Demet yüksekliği: 100 km'de ~1 km, 200 km'de ~3 km, 250 km'de ~4,5 km üstünden bakar.

**Nasıl çalışır:** Radar 360° tarar, her turda anteni biraz kaldırır (0,5°, 1,5°, 2,5° …). En düşük açı yere en yakın yağışı gösterir. Yansıyan güç tanecik çapının 6. kuvvetiyle orantılıdır; bu yüzden birkaç iri dolu tanesi binlerce küçük damladan daha parlak görünür. Doppler modunda ayrıca taneciklerin radara yaklaşma/uzaklaşma hızı ölçülür (rüzgâr, dönme).

**Günlük hayattan örnek:** MGM radar mozaiğinde Ankara üzerine gelen 45–50 dBZ'lik hücre: 20–30 dakika içinde kuvvetli sağanak, muhtemelen küçük dolu. Aynı hücrenin 60 dBZ'ye çıkması ve tepeden "üç gövde saçılımı" (three-body scatter spike) görünmesi iri dolu işaretidir.

**Sık yapılan hata:** Radarda kırmızı görüp "sel geliyor" demek. 50 dBZ, dakikalar süren bir sağanak da olabilir; süre ve hücrenin hareket hızı belirleyicidir. Ayrıca radarın 200 km ötesindeki zayıf yağış (kış karı gibi) demetin altında kaldığı için hiç görünmeyebilir.

**Kaynaklar:**
1. NWS Radar Reflectivity FAQ — dBZ tablosu ve yankı türleri
2. MGM Radar Ürünleri sayfası — Türkiye radar ağı ve palet
3. Rinehart, *Radar for Meteorologists* — Z–R ilişkisi (Marshall–Palmer)

> **Tutarlılık:** 🟢 Yüksek (3/3 kaynak hemfikir) · Son doğrulama: 2026-09-08
> Çelişki: — (dBZ→mm/sa dönüşümü yağış tipine göre 2 kata kadar değişir; aralık verildi)

---

## Hava Durumu Modelleri Nedir?

**Kısa tanım:** Sayısal hava tahmin modeli, atmosferi bir grid'e böler ve fizik denklemlerini (hareket, termodinamik, nem) ileri doğru çözerek gelecek saatler ve günler için tahmin üretir. Farklı kurumların modelleri farklı çözünürlük, fizik ve başlangıç verisi kullanır; bu yüzden aynı gün için farklı sonuç verirler.

**Eşik / Formül:**

| Model | Kurum | Çözünürlük | Ufuk | Güncelleme | Güçlü yanı |
|---|---|---|---|---|---|
| **ECMWF IFS (HRES)** | Avrupa (ECMWF) | ~9 km | 10–15 gün | 4×/gün | 3–10 gün arası genel doğrulukta lider |
| **GFS** | ABD (NOAA) | ~13 km | 16 gün | 4×/gün | Ücretsiz, açık, en yaygın |
| **ICON** | Almanya (DWD) | 13 km (global), ICON-EU 6,5 km, ICON-D2 2,2 km | 7,5 gün / 5 gün / 2 gün | 4×–8×/gün | Avrupa ve Türkiye batısı için iyi detay |
| **UKMO (UM)** | İngiltere (Met Office) | ~10 km | 7 gün | 4×/gün | Fırtına takibi |
| **AROME / HARMONIE** | Fransa / İskandinavya | 1,3–2,5 km | 2 gün | Saatlik–8×/gün | Kısa vadeli sağanak, dağ etkisi |
| **HRRR** | ABD | 3 km | 18–48 saat | Saatlik | Yalnız ABD |
| **WRF (MGM)** | Türkiye (MGM) | 4 km | 3 gün | 2×–4×/gün | MGM'nin kendi yüksek çözünürlüklü tahmini |
| **Ensemble (ENS, GEFS)** | ECMWF, NOAA | Daha kaba, 30–51 üye | 15–45 gün | 2×–4×/gün | Belirsizliği ölçer |

- **Çözünürlük:** Grid aralığı; 9 km'lik model Uludağ'ı tek bir kutu olarak görür, dağın kar sınırını ayırt edemez. 2 km altı modeller ("konvektif izinli") sağanak hücrelerini tek tek çözer.
- **Ensemble:** Aynı model, başlangıç koşulları biraz oynatılarak 30–50 kez çalıştırılır. Üyeler hemfikirse tahmin güvenilir, dağılıyorsa belirsiz. 5 gün ötesi için tek modele değil ensemble ortalamasına ve yayılımına bakın.
- Pratik doğruluk: 1–3 gün yüksek, 4–7 gün orta, 7–10 gün yalnızca eğilim, 10+ gün klimatoloji seviyesine yakın.

**Nasıl çalışır:** Model, tüm dünyadan gelen gözlemleri (uydu, radyosonde, uçak, istasyon) alır ve "veri özümseme" ile en tutarlı başlangıç durumunu kurar. Ardından Navier–Stokes, termodinamik ve sürekli denklemleri dakikalık adımlarla ileri çözer. Grid'den küçük süreçler (bulut, türbülans, yağış) "parametrizasyon" ile yaklaşık temsil edilir; modellerin en çok ayrıştığı yer burasıdır.

**Günlük hayattan örnek:** Kış fırtınası 6 gün ötede: ECMWF Marmara'ya kar, GFS yağmur veriyor. Doğru yaklaşım: ECMWF ensemble'ının 51 üyesinin kaçının kar verdiğine bakmak. %70 üye kar diyorsa kar olasılığı yüksek, %30 ise "izle" demektir.

**Sık yapılan hata:** Tek bir model çalışmasının 10 gün sonrası için verdiği kar haritasını haber yapmak. Model her 6 saatte değişir; 10 gün ötede tek çalışma neredeyse rastgeledir.

**Kaynaklar:**
1. ECMWF "Forecast user guide" — IFS özellikleri ve ensemble yorumu
2. NOAA NCEP "GFS/GEFS documentation" — GFS özellikleri
3. DWD "ICON model description" — ICON çözünürlükleri
4. MGM "Sayısal Hava Tahmini" sayfası — WRF ayarları

> **Tutarlılık:** 🟡 Orta (4/4 tanımda hemfikir; çözünürlük ve güncelleme sıklıkları zamanla değişiyor) · Son doğrulama: 2026-09-08
> Çelişki: Model çözünürlükleri yıl içinde güncellenebilir (örn. GFS 13 km'den daha ince gride geçiş planları). Tablo, doğrulama tarihindeki durumu yansıtır; **bu kart 6 ayda bir yeniden doğrulanmalıdır.**

---

## Modellere Erişim Sağlayan Web Siteleri

**Kısa tanım:** Ham model çıktıları büyük dosyalardır; aşağıdaki siteler bunları harita, meteogram ve grafik hâlinde ücretsiz sunar. Her sitenin gösterdiği model listesi ve gecikmesi farklıdır.

**Eşik / Formül:**

| Site | Modeller | Güçlü yanı | Not |
|---|---|---|---|
| **Windy.com** | ECMWF, GFS, ICON, ICON-EU, ICON-D2, AROME, UKMO, NAM | Modelleri tek tıkla karşılaştırma, 850 hPa sıcaklık, donma seviyesi, radar katmanı | En pratik başlangıç; ücretsiz sürüm 3 saatlik adım |
| **Meteoblue.com** | Kendi NEMS modelleri + ECMWF, GFS, ICON | "Multimodel" karşılaştırma tablosu, hava kalitesi | Tahmin güvenilirlik göstergesi (predictability) var |
| **Ventusky.com** | GFS, ICON, ECMWF, HRRR | Kar yüksekliği, dalga, akıcı animasyon | Görsel olarak en anlaşılır |
| **Wetterzentrale.de** | ECMWF, GFS, ICON, UKMO, GEM, ensemble | Klasik 850 hPa ve 500 hPa haritaları, ensemble "spagetti" grafikleri | Tahminciler tarafından en çok kullanılan; arayüz eski |
| **Tropicaltidbits.com** | GFS, ECMWF, ICON, CMC, ensembles | Her parametre için haritalar, sondaj (skew-T) | İngilizce, ileri seviye |
| **Pivotalweather.com** | GFS, ECMWF, HRRR, NAM ve daha fazlası | Yüksek kaliteli haritalar, yağış tipi ürünleri | Bazı ürünler ücretli |
| **Open-Meteo.com** | ECMWF, GFS, ICON, MeteoFrance, JMA ve daha fazlası | **Ücretsiz API**, saatlik JSON, geçmiş veri | Kendi sitenize veri çekmek için ideal |
| **ECMWF Open Charts** (charts.ecmwf.int) | ECMWF HRES, ENS | Resmî ECMWF haritaları, ensemble meteogram | 2022'den beri ücretsiz |
| **MGM (mgm.gov.tr)** | MGM WRF, ECMWF (yorumlanmış) | Türkiye il/ilçe resmî tahmin, radar, uyarılar | Resmî uyarılar yalnız buradan |
| **Windguru.cz** | GFS, ICON, AROME, HARMONIE | Rüzgâr odaklı tablo, sörf/yelken için | Tablo formatı sayısal karşılaştırmaya uygun |
| **Meteociel.fr** | ARPEGE, AROME, GFS, ECMWF | Avrupa'nın en detaylı model arşivi | Fransızca |

**Nasıl çalışır:** Kurumlar (NOAA, DWD, ECMWF) model çıktısını GRIB formatında açık olarak yayınlar; bu siteler dosyaları indirip görselleştirir. ECMWF 2022'den itibaren tam açık veriye geçmiştir. Gecikme genellikle model çalışmasının bitiminden 1–3 saat sonradır.

**Günlük hayattan örnek:** Hafta sonu Kartalkaya'ya kayak planı: Windy'de "ICON-D2" seç, 850 hPa sıcaklığına ve "Kar yağışı" katmanına bak; ardından wetterzentrale'de ECMWF ensemble Bolu meteogramını aç, üyelerin dağılımına bak. İkisi uyuşuyorsa git.

**Sık yapılan hata:** Bir sitenin "hava durumu" ekranını kurumun resmî tahmini sanmak. Windy'nin gösterdiği doğrudan model çıktısıdır; tahminci yorumu yoktur. Resmî uyarı için MGM'ye bakın.

**Kaynaklar:**
1. Her sitenin kendi "About / Models" sayfası — model listeleri
2. ECMWF "Open data" duyurusu (2022) — açık veri politikası
3. Open-Meteo API dokümantasyonu — desteklenen modeller

> **Tutarlılık:** 🟡 Orta (site listeleri güncel; model listeleri değişken) · Son doğrulama: 2026-09-08
> Çelişki: — Sitelerin sunduğu modeller sık değişir; **bu kart 3 ayda bir yeniden doğrulanmalıdır.** Ücretli/ücretsiz durumu da değişebilir.
