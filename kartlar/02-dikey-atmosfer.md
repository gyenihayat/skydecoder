---
kategori: "Dikey Atmosfer"
seviye: "orta"
etiketler: ["irtifa", "lapse rate", "kar sınırı", "850 hPa", "dağ", "orografik"]
guncelleme: "2026-09-08"
---

## İrtifa ile Sıcaklık Nasıl Düşer?

**Kısa tanım:** Troposferde yükseldikçe sıcaklık ortalama her 1000 metrede yaklaşık 6,5°C düşer. Buna "sıcaklık düşme oranı" (lapse rate) denir; günün ve nemin durumuna göre 4 ile 10°C/km arasında değişir.

**Eşik / Formül:**

| Oran | Değer | Ne zaman geçerli |
|---|---|---|
| Standart atmosfer (ICAO) | 6,5°C / 1000 m | Uzun dönem ortalama |
| Kuru adyabatik | 9,8°C / 1000 m | Doymamış hava yükselirken |
| Nemli (doygun) adyabatik | 4–7°C / 1000 m (ort. ~6) | Bulut içinde yükselen hava |
| İnversiyon | Sıcaklık artar | Sakin kış geceleri, vadiler |

- Pratik kural: **100 m'de ≈ 0,65°C**, yani 1500 m'lik bir dağ tabandan ~10°C soğuk olur.

**Nasıl çalışır:** Yükseldikçe basınç düşer, hava genleşir; genleşme iş yapar ve hava soğur (adyabatik soğuma). Kuru hava 9,8°C/km soğur. Hava doyunca yoğuşma ısısı açığa çıkar ve soğuma yavaşlar (nemli oran). Gerçek atmosferde ölçülen ortalama 6,5°C/km, bu ikisinin karışımıdır. Yeryüzü geceleri ışınımla soğuduğunda yere yakın hava yukarıdakinden soğuk kalır: inversiyon.

**Günlük hayattan örnek:** Bursa'da (100 m) 12°C ölçülürken Uludağ Oteller Bölgesi'nde (1900 m) yaklaşık 0°C beklenir. Antalya'da (10 m) 30°C iken Saklıkent'te (1850 m) 18°C dolayında olur.

**Sık yapılan hata:** 6,5°C/km'yi her zaman geçerli sanmak. Kış sabahlarında Ankara'da (900 m) −12°C, Elmadağ zirvesinde (1850 m) −4°C olabilir; inversiyon oranı tersine çevirir.

**Kaynaklar:**
1. ICAO Standard Atmosphere (1993) — 6,5 K/km
2. Wallace & Hobbs, *Atmospheric Science* (2006) — kuru ve nemli adyabatik oranlar
3. NWS JetStream "Lapse rate" — pratik değerler

> **Tutarlılık:** 🟢 Yüksek (3/3 kaynak hemfikir) · Son doğrulama: 2026-09-08
> Çelişki: — (nemli adyabatik oran sıcaklığa bağlı olduğu için aralık verildi)

---

## Kar Sınırı Nedir?

**Kısa tanım:** Yağışın yağmur olarak değil kar olarak düştüğü en alçak yükseklik seviyesidir. Genellikle donma seviyesinin (0°C izotermi) 200–400 m altındadır.

**Eşik / Formül:**
- **Donma seviyesi (freezing level):** Atmosferde sıcaklığın 0°C olduğu yükseklik. Model haritalarında "0°C isotherm / freezing level" olarak verilir.
- **Kar sınırı ≈ Donma seviyesi − 300 m** (aralık: 200–400 m)
- Yoğun yağışta kar sınırı 500–600 m'ye kadar aşağı iner (kar taneleri erirken havayı soğutur).
- Kar tanesi yere ulaşırken sıcaklık +2°C'ye kadar kar olarak kalabilir; belirleyici olan **ıslak termometre sıcaklığı ≤ 0,5–1°C** olmasıdır.
- Türkçe kaynaklarda "kar yağış sınırı" veya "kar seviyesi" olarak da geçer.

**Nasıl çalışır:** Kar taneleri bulutta oluşur ve düşerken 0°C'nin üstündeki tabakada erimeye başlar. Erime anında değil, birkaç yüz metre boyunca sürer; bu yüzden kar, donma seviyesinin altında bir süre daha kar olarak kalır. Hava kuruysa tanenin yüzeyinden buharlaşma ek soğutma sağlar; kar sınırı daha da aşağı iner.

**Günlük hayattan örnek:** Model 1200 m'de donma seviyesi gösteriyorsa Bolu şehir merkezi (725 m) yağmur, Kartalkaya (1900 m) kar, Abant (1300 m) sulu kar–kar sınırındadır. Yoğun ve uzun süreli yağışta Bolu merkeze de kar düşebilir.

**Sık yapılan hata:** Kar sınırını donma seviyesiyle aynı sanmak. Donma seviyesinin tam altında hava +1°C'dir ama kar hâlâ yağar.

**Kaynaklar:**
1. MeteoSwiss "Schneefallgrenze" açıklaması — donma seviyesi −300 m kuralı
2. NWS "Snow level vs freezing level" — 500–1000 ft (150–300 m) farkı
3. Steinacker (1983), *Arch. Met. Geoph. Biocl.* — yoğun yağışta kar sınırının inişi

> **Tutarlılık:** 🟡 Orta (3/3 mekanizmada hemfikir, mesafede farklı) · Son doğrulama: 2026-09-08
> Çelişki: NWS 150–300 m, MeteoSwiss 300 m, Steinacker yoğun yağışta 600 m'ye kadar verir. Kart 200–400 m'yi standart, 600 m'yi uç değer olarak sunar.

---

## Dağlarda Kar Yağması Nasıl Açıklanır?

**Kısa tanım:** Dağa çarpan hava yükselmeye zorlanır, yükselirken soğur, nemi yoğuşur ve yağış oluşur (orografik yükselme). Dağ hem yeterince soğuk hem de daha fazla yağışlı olduğu için kar, dağlarda hem daha sık hem daha çok yağar.

**Eşik / Formül:**
- Rüzgâra bakan yamaç (rüzgâr üstü): yağış artar, tipik olarak her 100 m'de %5–10
- Rüzgâr altı yamaç: föhn etkisi, hava alçalırken 9,8°C/km ısınır ve kurur; yağış azalır ("yağmur gölgesi")
- Kar için gerekli: 850 hPa sıcaklığı ≤ −2/−5°C **ve** yamaç seviyesinde ıslak termometre ≤ 0°C

**Nasıl çalışır:** Nemli hava dağa yaklaştığında yatay hareketi dikey harekete dönüşür. Yükselen hava kuru adyabatik oranla soğur; çiğ noktasına ulaşınca bulut oluşur (bu yükseklik "yoğuşma seviyesi"dir, dağ zirvelerine takılan bulutun tabanı buradadır). Bulut içinde yükselmeye devam eden hava nemli oranla soğur ve yağış bırakır. Zirveyi aşan hava rüzgâr altı yamaçta alçalır, sıkışır, ısınır ve kurur.

**Günlük hayattan örnek:** Karadeniz'den gelen nemli kuzey rüzgârı Kaçkarlar'ın kuzey yamacına metrelerce kar bırakırken, Erzurum tarafında (rüzgâr altı) yağış çok azdır. Toroslar'ın Akdeniz'e bakan yamacı Konya Ovası'ndan 3–4 kat fazla yağış alır.

**Sık yapılan hata:** "Dağ soğuk olduğu için kar yağar" demek. Soğuk gereklidir ama yeterli değildir; nem taşıyan bir rüzgâr yönü olmadan dağ ne kadar soğuk olursa olsun kar yağmaz (örnek: kış boyunca açık, kuru ve −20°C olan Ağrı).

**Kaynaklar:**
1. Roe, G.H. (2005) "Orographic Precipitation", *Annu. Rev. Earth Planet. Sci.* — mekanizma ve yamaç oranları
2. Met Office "Orographic rainfall" — föhn ve yağmur gölgesi
3. MGM Türkiye yağış atlası — Karadeniz/Toros yamaç farkları

> **Tutarlılık:** 🟢 Yüksek (3/3 kaynak hemfikir) · Son doğrulama: 2026-09-08
> Çelişki: —

---

## Kar Yağması İçin Hangi İrtifada Hava Kaç Derece Olmalı?

**Kısa tanım:** Meteorologlar yerdeki sıcaklığa değil, yaklaşık 1500 m'deki (850 hPa) ve 3000 m'deki (700 hPa) sıcaklığa bakar. Alçak kesimlerde kar için 850 hPa'nın −3 ile −5°C'nin altına inmesi gerekir.

**Eşik / Formül:**

| Seviye | Yaklaşık yükseklik | Kar için eşik | Not |
|---|---|---|---|
| 2 m (yüzey) | 0 m | ≤ +1/+2°C (ıslak termometre ≤ 0,5°C) | Tek başına yetersiz |
| 925 hPa | ~750 m | ≤ −1°C | Kıyı şehirleri için iyi gösterge |
| **850 hPa** | **~1500 m** | **≤ −3°C (güvenli: ≤ −5°C)** | En çok kullanılan eşik |
| 700 hPa | ~3000 m | ≤ −10°C | Ek kontrol |
| 1000–500 hPa kalınlık | — | ≤ 5280 m ("528 çizgisi") | Klasik Avrupa kuralı |

- Türkiye için pratik kural: 850 hPa sıcaklığı **−5°C** olduğunda İç Anadolu'da (900–1000 m) kar; **−8°C** ve altında İstanbul, İzmir gibi kıyı şehirlerinde kar mümkündür.
- Deniz üzerinden gelen hava (Karadeniz, Marmara) yerde 1–2°C ekstra ısınma yapar; kıyıda eşik daha sıkı tutulur.

**Nasıl çalışır:** Yerdeki sıcaklık günlük döngü, deniz etkisi ve şehir ısı adasından etkilenir; 850 hPa ise bu gürültüden arınmış "hava kütlesi" sıcaklığını gösterir. Eğer 850 hPa −5°C ise standart oranla yer seviyesinde (0 m) yaklaşık +5°C, 1000 m'de −1,5°C beklenir; yoğun yağışta eriyen kar havayı ek soğutur ve eşik gevşer.

**Günlük hayattan örnek:** Ankara için forecast'ta 850 hPa −6°C ve yağış görülüyorsa kar kesinleşmiştir. İstanbul için 850 hPa −4°C ise Kartal, Sarıyer gibi yüksek ilçelerde kar, Kadıköy sahilde yağmur–sulu kar olur; −8°C'de tüm şehirde kar tutar.

**Sık yapılan hata:** Sadece yer sıcaklığına bakmak. Yerde +3°C iken 850 hPa −7°C ise kar başlayınca yer sıcaklığı hızla düşer ve kar tutar; tersi durumda (yerde 0°C, 850 hPa 0°C) sulu kar ve yağmur olur.

**Kaynaklar:**
1. UK Met Office / wetterzentrale forum "528 line" geleneği — kalınlık kuralı
2. NWS Forecaster's Guide — 850 hPa ve ıslak termometre eşikleri
3. MGM tahmincileri ve Türk hava tahmin forumları (uyarı: resmî değil) — Türkiye için −5/−8°C pratik eşikleri

> **Tutarlılık:** 🟡 Orta (mekanizmada hemfikir, sayısal eşik kaynağa göre değişiyor) · Son doğrulama: 2026-09-08
> Çelişki: 850 hPa eşiği kaynaklarda −2, −3, −5 ve −6°C olarak geçer; bölgeye ve yüksekliğe bağlıdır. Kart, aralığı tablo hâlinde verir ve Türkiye için yerel pratik değerleri "resmî olmayan" olarak işaretler.
