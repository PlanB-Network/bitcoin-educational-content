---
term: ADDRV2

---
Bitcoin-verkon `addr`-viestin ehdotettu kehitys BIP155:n kanssa. `addr`-viestiä käytettiin lähettämään solmujen osoitteita, jotka hyväksyvät saapuvat yhteydet, mutta se oli rajoitettu 128-bittisiin osoitteisiin. Tämä koko oli riittävä IPv6-, IPv4- ja Tor V2 -osoitteille, mutta riittämätön muille protokollille. Päivitetty versio `addrv2` on suunniteltu tukemaan pidempiä osoitteita, mukaan lukien 256-bittiset Tor v3 -piilopalvelut, sekä muita verkkoprotokollia, kuten I2P:tä tai tulevia protokollia.