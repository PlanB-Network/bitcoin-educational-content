---
term: ..

---
Bitcoin Core'i failide nimi, mis salvestavad teavet, mis on vajalik eelnevalt lisatud plokkide poolt UTXO-sse tehtud muudatuste võimalikuks tagasipööramiseks. Iga fail on identifitseeritud unikaalse numbriga, mis on sama, mis failil blk*.dat, millele see vastab. Rev*.dat-failid sisaldavad blk*.dat-failides salvestatud plokkidele vastavaid pöördandmeid. Need andmed on sisuliselt loetelu kõikidest UTXOdest, mis on kasutatud ploki sisendina. Need pöördfailid võimaldavad sõlmpunktil pöörduda tagasi eelmisse olekusse, kui plokiahelas toimub ümberkorraldus, mille tagajärjel varem valideeritud plokid visatakse kõrvale.