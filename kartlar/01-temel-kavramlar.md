---
kategori: "Temel Kavramlar"
seviye: "temel"
etiketler: ["çiğ noktası", "nem", "hissedilen sıcaklık", "ısı adası", "basınç"]
guncelleme: "2026-09-08"
---

## Çiğ Noktası (Çiğ Sıcaklığı) Nedir?

**Kısa tanım:** Havanın, içindeki su buharı miktarı değişmeden soğutulduğunda doyuma ulaşıp yoğuşmanın (çiğ, sis, bulut) başladığı sıcaklıktır. Havadaki gerçek nem miktarının en dürüst göstergesidir.

**Eşik / Formül:**
- Çiğ noktası ≤ hava sıcaklığı her zaman geçerlidir; ikisi eşitse bağıl nem %100'dür.
- Yaklaşık hesap (Magnus formülü): `Td ≈ T − ((100 − RH) / 5)` (RH > %50 için ±1°C hata)
- Konfor eşikleri:

| Çiğ noktası | His |
|---|---|
| < 10°C | Kuru, ferah |
| 10–15°C | Rahat |
| 16–20°C | Nemli, yapışkan |
| 21–24°C | Bunaltıcı |
| > 24°C | Aşırı bunaltıcı, sağlık riski |

**Nasıl çalışır:** Hava belirli bir sıcaklıkta belirli miktarda su buharı taşıyabilir. Sıcaklık düştükçe bu kapasite azalır; çiğ noktasına inildiğinde hava "dolar" ve fazla buhar sıvıya dönüşür. Bağıl nem sıcaklıkla değişir ama çiğ noktası, havaya nem eklenmedikçe veya çıkarılmadıkça sabit kalır — bu yüzden "gerçek nem" ölçüsüdür.

**Günlük hayattan örnek:** Antalya'da yaz gecesi 26°C'de çiğ noktası 23°C ise gece bunaltıcıdır. Ankara'da aynı 26°C'de çiğ noktası 8°C ise akşam serinler ve terleme kolayca buharlaşır. Sabah araba camındaki çiğ, gece sıcaklığının çiğ noktasına ulaştığını gösterir.

**Sık yapılan hata:** "Bağıl nem %90, çok nemli" demek. Ocak ayında 2°C'de %90 nem, havada çok az su olduğu anlamına gelir; aynı %90 nem Ağustos'ta 30°C'de bunaltıcıdır. Karşılaştırma için çiğ noktasına bakın.

**Kaynaklar:**
1. NOAA / NWS Glossary — çiğ noktası tanımı ve konfor tablosu
2. MGM Meteoroloji Sözlüğü — "çiy noktası sıcaklığı" tanımı
3. Lawrence (2005), *Bull. Amer. Meteor. Soc.* — Magnus yaklaşık formülü ve hata payı

> **Tutarlılık:** 🟢 Yüksek (3/3 kaynak hemfikir) · Son doğrulama: 2026-09-08
> Çelişki: — (konfor tablosu sınırları kaynaklar arasında ±1°C oynar, önemsiz)

---

## Hissedilen Sıcaklık Nasıl Hesaplanır?

**Kısa tanım:** Termometrenin gösterdiği değil, rüzgâr ve nemin etkisiyle insan vücudunun algıladığı sıcaklıktır. Soğukta rüzgâr soğutma (wind chill), sıcakta ısı indeksi (heat index) kullanılır.

**Eşik / Formül:**
- **Rüzgâr soğutma** (T ≤ 10°C ve rüzgâr ≥ 4,8 km/sa iken):
  `Twc = 13,12 + 0,6215·T − 11,37·V^0,16 + 0,3965·T·V^0,16`
  (T: °C, V: 10 m yükseklikteki rüzgâr hızı, km/sa)
- **Isı indeksi** (T ≥ 27°C ve RH ≥ %40 iken): Rothfusz regresyonu; pratikte NWS tablosu kullanılır.
- **Humidex** (Kanada): `H = T + 0,5555·(e − 10)`, e: buhar basıncı (hPa)
- Örnek değerler:

| Sıcaklık | Rüzgâr / Nem | Hissedilen |
|---|---|---|
| 0°C | 30 km/sa rüzgâr | −6°C |
| −10°C | 40 km/sa rüzgâr | −21°C |
| 32°C | %60 nem | 38°C |
| 35°C | %70 nem | 47°C |

**Nasıl çalışır:** Rüzgâr, vücudu saran ince ılık hava tabakasını süpürerek ısı kaybını hızlandırır. Nem ise terin buharlaşmasını yavaşlatır; vücut kendini soğutamaz. Her iki formül de deneysel olarak insan denekler üzerinde kalibre edilmiştir; fiziksel bir ölçüm değil, bir "eşdeğer sıcaklık"tır.

**Günlük hayattan örnek:** Erzurum'da −8°C ve 35 km/sa rüzgârda hissedilen −18°C'dir; açıkta kalan deri 30 dakikada donma riski taşır. Adana'da 36°C ve %55 nemde hissedilen 45°C'dir; bu, ısı çarpması eşiğidir.

**Sık yapılan hata:** Rüzgâr soğutmanın nesneleri de daha soğuk yaptığını sanmak. Rüzgâr, arabanın radyatörünü hava sıcaklığının altına soğutamaz; sadece o sıcaklığa daha hızlı ulaştırır.

**Kaynaklar:**
1. Environment Canada / NWS ortak Wind Chill formülü (2001) — katsayılar
2. NWS Heat Index tablosu (Rothfusz 1990) — ısı indeksi
3. MGM "Hissedilen Sıcaklık" açıklama sayfası — Türkiye'de kullanılan yöntem

> **Tutarlılık:** 🟡 Orta (3/3 tanımda hemfikir, formülde 2 farklı yaklaşım) · Son doğrulama: 2026-09-08
> Çelişki: Sıcak taraf için ABD "heat index", Kanada "humidex", bazı Avrupa ülkeleri "apparent temperature" (Steadman) kullanır; aynı koşulda 2–3°C fark çıkabilir. Kart, en yaygın olan NWS yöntemini esas alır.

---

## Şehir Isı Adası (Kentsel Isı Adası) Nedir?

**Kısa tanım:** Şehir merkezinin, çevresindeki kırsal alandan belirgin biçimde daha sıcak olması olayıdır. En güçlü etki gece görülür.

**Eşik / Formül:**
- Tipik fark: gündüz 1–3°C, açık ve sakin gecelerde 5–10°C
- Etki, rüzgâr hızı 5 m/s'yi aştığında büyük ölçüde silinir
- Şehir büyüklüğü ile logaritmik artar (Oke, 1973): `ΔT ≈ 2,01·log₁₀(nüfus) − 4,06` (Avrupa şehirleri için, sakin açık gecelerde)

**Nasıl çalışır:** Beton ve asfalt gündüz güneş ısısını depolar, gece yavaş bırakır. Binalar yüzey alanını artırır ve rüzgârı keser; yeşil alan azlığı buharlaşma soğutmasını ortadan kaldırır. Araç ve klima atık ısısı eklenir. Sonuç: şehir gece soğuyamaz.

**Günlük hayattan örnek:** İstanbul'da Temmuz gecesi Şişli'de 27°C ölçülürken Şile'de 20°C olabilir. Ankara Kızılay'da kar yağmazken Gölbaşı'nda kar tutması, kış ısı adasının etkisidir.

**Sık yapılan hata:** Isı adasını "küresel ısınma kanıtı" ya da "kanıt değil" diye tartışmaya sokmak. Isı adası yerel bir etkidir; küresel sıcaklık serileri bu etki için düzeltilir.

**Kaynaklar:**
1. Oke, T.R. (1982) *Q. J. R. Meteorol. Soc.* — tanım, gece maksimumu, nüfus ilişkisi
2. US EPA "Heat Island Effect" — 1–3°C gündüz, 12°C'ye kadar gece değerleri
3. İTÜ / TÜBİTAK İstanbul kentsel ısı adası çalışmaları — Türkiye örnekleri

> **Tutarlılık:** 🟢 Yüksek (3/3 kaynak hemfikir) · Son doğrulama: 2026-09-08
> Çelişki: — (maksimum gece farkı EPA'da 12°C, Oke'de 10°C; aralık olarak verildi)

---

## Alçak ve Yüksek Basınç Ne Yapar?

**Kısa tanım:** Alçak basınç merkezi (L / A) yükselen hava, bulut ve yağış getirir; yüksek basınç merkezi (H / Y) alçalan hava, açık gökyüzü ve durgunluk getirir.

**Eşik / Formül:**
- Deniz seviyesi standart basınç: 1013,25 hPa
- Pratik eşikler: < 1000 hPa belirgin alçak, > 1025 hPa belirgin yüksek
- 3 saatte ≥ 3 hPa düşüş: yaklaşan cephe/fırtına işareti
- Kuzey yarımkürede rüzgâr: alçak etrafında saat yönünün tersine ve içe, yüksek etrafında saat yönünde ve dışa

**Nasıl çalışır:** Yüzeyde hava alçak basınca doğru akar, merkezde birleşip yükselir; yükselen hava soğur, nem yoğuşur, bulut ve yağış oluşur. Yüksek basınçta hava yukarıdan çöker, çökerken ısınır ve kurur; bulut dağılır. Kışın yüksek basınç altında hava sakin kaldığı için yerde sis, don ve inversiyon (yerde soğuk, yukarıda ılık hava) görülür — hava kirliliği de bu yüzden birikir.

**Günlük hayattan örnek:** Kasım'da Balkanlar üzerinden gelen alçak basınç Marmara'ya yağış getirir. Ocak'ta Sibirya yüksek basıncı İç Anadolu'ya açık, çok soğuk ve sisli sabahlar getirir; Ankara'da −15°C ve aynı anda Uludağ zirvesinde −5°C ölçülmesi inversiyondur.

**Sık yapılan hata:** "Yüksek basınç = güzel hava" sanmak. Kışın yüksek basınç, en soğuk geceleri, en yoğun sisi ve en kirli havayı getirir.

**Kaynaklar:**
1. Met Office "High and low pressure" — mekanizma ve rüzgâr yönü
2. NWS JetStream — basınç sistemleri dersi
3. MGM Sinoptik Haritalar sayfası — sembol ve eşik kullanımı

> **Tutarlılık:** 🟢 Yüksek (3/3 kaynak hemfikir) · Son doğrulama: 2026-09-08
> Çelişki: —
