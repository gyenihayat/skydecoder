// Ziyaret ve sitede kalma süresi sayacı. Upstash Redis (REST) üzerinde tutulur.
// GET  /api/istatistik            -> özet JSON
// POST /api/istatistik {tip:...}  -> kayıt (giris | sure | kart)

const URL_ = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
const TOKEN = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
const GUN_SAYISI = 30;
const MAX_SURE_SN = 4 * 60 * 60;

async function redis(commands) {
  const r = await fetch(`${URL_}/pipeline`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${TOKEN}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(commands),
  });
  if (!r.ok) throw new Error(`Redis ${r.status}: ${await r.text()}`);
  const out = await r.json();
  return out.map((x) => x.result);
}

function bugunISO() {
  return new Date().toISOString().slice(0, 10);
}
function gunler(n) {
  const list = [];
  const t = new Date();
  for (let i = 0; i < n; i++) {
    list.push(new Date(t.getTime() - i * 86400000).toISOString().slice(0, 10));
  }
  return list;
}
function govde(req) {
  if (!req.body) return {};
  if (typeof req.body === 'string') {
    try { return JSON.parse(req.body); } catch { return {}; }
  }
  return req.body;
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') {
    const anahtar = (req.query && req.query.anahtar) || '';
    if (!process.env.ISTATISTIK_ANAHTAR || anahtar !== process.env.ISTATISTIK_ANAHTAR) {
      res.status(404).json({ hata: 'Bulunamadı.' });
      return;
    }
  }
  if (!URL_ || !TOKEN) {
    res.status(503).json({ hata: 'Depolama ayarlı değil. Vercel projesine Upstash Redis bağlayın (KV_REST_API_URL / KV_REST_API_TOKEN).' });
    return;
  }
  try {
    if (req.method === 'POST') {
      const b = govde(req);
      const gun = bugunISO();
      const cmds = [];
      if (b.tip === 'giris') {
        cmds.push(['INCR', 'ziyaret:toplam'], ['INCR', `ziyaret:gun:${gun}`], ['SET', 'ist:baslangic', gun, 'NX']);
        if (b.yeni) cmds.push(['INCR', 'ziyaretci:tekil']);
      } else if (b.tip === 'sure') {
        const sn = Math.min(MAX_SURE_SN, Math.max(0, Math.round(Number(b.sn) || 0)));
        if (sn > 0) cmds.push(['INCRBY', 'sure:toplam', sn], ['INCRBY', `sure:gun:${gun}`, sn]);
      } else if (b.tip === 'kart' && typeof b.id === 'string' && b.id.length < 120) {
        cmds.push(['ZINCRBY', 'kart:acilis', 1, b.id]);
      }
      if (cmds.length) await redis(cmds);
      res.status(204).end();
      return;
    }

    const gs = gunler(GUN_SAYISI);
    const cmds = [
      ['GET', 'ziyaret:toplam'], ['GET', 'ziyaretci:tekil'], ['GET', 'sure:toplam'], ['GET', 'ist:baslangic'],
      ['ZREVRANGE', 'kart:acilis', 0, 9, 'WITHSCORES'],
      ...gs.map((g) => ['GET', `ziyaret:gun:${g}`]),
      ...gs.map((g) => ['GET', `sure:gun:${g}`]),
    ];
    const r = await redis(cmds);
    const toplam = Number(r[0] || 0);
    const sureToplam = Number(r[2] || 0);
    const z = r[4] || [];
    const kartlar = [];
    for (let i = 0; i < z.length; i += 2) kartlar.push({ id: z[i], adet: Number(z[i + 1]) });
    const gunluk = gs.map((g, i) => {
      const ziyaret = Number(r[5 + i] || 0);
      const sure = Number(r[5 + GUN_SAYISI + i] || 0);
      return { gun: g, ziyaret, sure_ort_sn: ziyaret ? Math.round(sure / ziyaret) : 0 };
    });
    res.status(200).json({
      toplam_ziyaret: toplam,
      tekil_ziyaretci: Number(r[1] || 0),
      sure_toplam_sn: sureToplam,
      sure_ort_sn: toplam ? Math.round(sureToplam / toplam) : 0,
      baslangic: r[3] || null,
      bugun: gunluk[0],
      gunluk,
      kartlar,
    });
  } catch (e) {
    res.status(500).json({ hata: String(e.message || e) });
  }
};
