---
termi: MAKSUKANAVA
---

Lightning Networkin puitteissa maksukanava on kaksisuuntainen yhteys kahden Lightning-solmun välillä, joka mahdollistaa bitcoinien vaihdon off-chain. On-chain, maksukanava edustetaan 2/2 multisignature-osoitteella, jota molemmat osapuolet hallitsevat. Maksukanavan avaaminen ja sulkeminen vaativat kumpikin on-chain transaktion. Näiden kahden tapahtuman välillä kanavan käyttäjät voivat suorittaa hyvin suuren määrän bitcoinien vaihtoja off-chain Lightning Networkissa, ilman että tarvitaan on-chain toimintaa. Lightningissa on mahdollista reitittää maksu useiden kanavien ja solmujen kautta, jotta bitcoineja voidaan lähettää ilman, että tarvitsee avata suoraa kanavaa vastaanottajan kanssa.