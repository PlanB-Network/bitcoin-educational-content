---
term: INDEXES/TXINDEX/
---

Bitcoin Core'is olevad failid, mis on pühendatud kõigi plokiahelas esinevate tehingute indekseerimisele. See indekseerimine võimaldab kiiresti otsida tehingu kohta üksikasjalikku teavet kasutades selle identifikaatorit (TXID), ilma et peaks läbi käima terve plokiahela. Nende indekseerimisfailide loomine ei ole Bitcoin Core'is vaikimisi lubatud valik. Kui see funktsioon ei ole lubatud, indekseerib teie sõlm ainult teie sõlmele lisatud rahakottidega seotud tehinguid. Kõigi tehingute indekseerimise lubamiseks peate seadistama parameetri `-txindex=1` failis `bitcoin.conf`. See valik on eriti kasulik rakendustele ja teenustele, mis sageli otsivad läbi Bitcoin'i tehingute ajaloo.