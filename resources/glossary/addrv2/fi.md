---
termi: ADDRV2
---

Ehdotettu kehitys BIP155:n myötä Bitcoin-verkon `addr`-viestille. `addr`-viestiä käytettiin solmujen osoitteiden lähettämiseen, jotka hyväksyvät saapuvat yhteydet, mutta se oli rajoittunut 128-bittisiin osoitteisiin. Tämä koko oli riittävä IPv6:lle, IPv4:lle ja Tor V2 -osoitteille, mutta se ei riittänyt muihin protokolliin. Päivitetty versio `addrv2` on suunniteltu tukemaan pidempiä osoitteita, mukaan lukien 256-bittiset Tor v3 piilotetut palvelut, sekä muita verkko-protokollia kuten I2P tai tulevaisuuden protokollat.