---
term: Addrv2

definition: Uus võrgusõnumi vorming (BIP155), mis võimaldab Bitcoin sõlmede aadresside levitamist. Toetab pikemaid aadresse, nagu Tor v3 või I2P.
---
Bitcoini võrgu "adr" sõnumi kavandatav areng koos BIP155-ga. Sõnumit `addr` kasutati sõlmeaadresside edastamiseks, mis võtavad vastu sissetulevaid ühendusi, kuid see oli piiratud 128-bitiste aadressidega. See suurus oli piisav IPv6, IPv4 ja Tor V2 aadresside jaoks, kuid ebapiisav teiste protokollide jaoks. Uuendatud versioon `addrv2` on mõeldud toetama pikemaid aadresse, sealhulgas 256-bitiseid Tor v3 varjatud teenuseid, samuti teisi võrguprotokolle nagu I2P või tulevasi protokolle.