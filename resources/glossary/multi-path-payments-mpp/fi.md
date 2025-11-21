---
term: MONIPOLKUMAKSUT (MPP)
---

Yleisnimitys kaikille Lightningin maksutekniikoille, joiden avulla maksutapahtuma voidaan jakaa useisiin pienempiin osiin ja reitittää eri reittejä pitkin. Toisin sanoen kukin maksun osuus kulkee eri solmupolkua pitkin. Näin voidaan kiertää likviditeettirajoitukset yhden kanavan reitillä.


Monipolkuiset maksut tarjoavat myös pieniä etuja luottamuksellisuuden kannalta, koska tarkkailijan on vaikeampi yhdistää kukin maksun osa koko maksutapahtumaan. Perusversiossaan kaikki fragmentit jakavat kuitenkin saman HTLC-salaisuuden, mikä voi tehdä tapahtumasta jäljitettävissä olevan, jos tarkkailija on läsnä useilla reiteillä. Lisäksi koska salaisuus on yksilöllinen kaikille maksun fraktioille, se ei ole atominen. Tämä tarkoittaa, että jotkin maksun osat voidaan suorittaa onnistuneesti, kun taas toiset voivat epäonnistua. Nämä puutteet korjataan "Atomic Multi-Path Payment" -menetelmällä.