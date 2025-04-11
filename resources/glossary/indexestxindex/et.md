---
term: INDEKSID/TXINDEX/

---
Failid Bitcoin Core'is, mis on pühendatud kõigi tehingute indekseerimisele plokiahelas. See indekseerimine võimaldab tehingu kohta üksikasjalikku teavet kiiresti otsida, kasutades selle identifikaatorit (TXID), ilma et peaks kogu plokiahelat läbi käima. Nende indekseerimisfailide loomine on võimalus, mis ei ole Bitcoin Core'is vaikimisi lubatud. Kui see funktsioon ei ole lubatud, indekseerib teie sõlme ainult need tehingud, mis on seotud teie sõlmega seotud rahakottidega. Kõigi tehingute indekseerimise lubamiseks peate seadma parameetri `-txindex=1` failis `bitcoin.conf`. See valik on eriti kasulik rakenduste ja teenuste jaoks, mis otsivad sageli Bitcoini tehingulugu.