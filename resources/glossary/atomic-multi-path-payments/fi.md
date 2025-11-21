---
term: ATOMISET MONIPOLKUMAKSUT
---

Parannettu versio MPP:stä (*Multi-Path Payments*), jossa kullakin maksupätkällä on erillinen osittainen salaisuus, jolla varmistetaan, että maksutapahtuma selvitetään atomisesti eli joko kokonaan tai ei ollenkaan.


MPP:t ovat Lightningin maksutapoja, joiden avulla maksutapahtuma voidaan jakaa useisiin pienempiin osiin ja reitittää eri reittejä pitkin. Toisin sanoen kukin maksun osa kulkee eri solmupolkua pitkin. Näin kierretään likviditeettirajoitukset, jotka kohdistuvat reitin yhteen kanavaan. Perus-MPP:ssä jokainen maksun murto-osa jakaa saman salaisuuden ja siten saman Hash:n HTLC:ssä. Tämä voi tehdä tapahtumasta jäljitettävissä olevan, jos tarkkailija on läsnä useilla reiteillä, koska hän voi yhdistää kaikki nämä identtiset salaisuudet toisiinsa. Lisäksi koska salaisuus on ainutlaatuinen kaikille maksun osille, se ei ole atominen. Tämä tarkoittaa, että jotkin maksun osat voidaan suorittaa onnistuneesti, kun taas toiset voivat epäonnistua.


AMP:ssä käytetään yksilöllisiä osasalaisuuksia kutakin fraktiota varten. Kun kaikki fragmentit on vastaanotettu, vastaanottaja voi niiden avulla rekonstruoida alkuperäisen yleisen salaisuuden ja vaatia täyden maksun. Tämä menetelmä tekee maksun osittaisen suorittamisen mahdottomaksi, koska koko maksun avaaminen edellyttää kaikkien osasalaisuuksien hallintaa. Näin varmistetaan, että maksu on täysin onnistunut tai täysin epäonnistunut (eli atominen). AMP parantaa myös luottamuksellisuutta, koska eri reittien välillä ei ole enää näkyviä yhteyksiä.


Yksi AMP:n eduista on se, että se toimii, vaikka vain vastaanottaja ja lähettäjä olisivat toteuttaneet tämän menetelmän. Välittäjäsolmut käsittelevät näitä maksuja tavanomaisina tapahtumina HTLC:tä käyttäen, eivätkä ne tiedä, että ne käsittelevät suuremman maksun murto-osia.