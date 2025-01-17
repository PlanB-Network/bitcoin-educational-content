---
term: AKTSIAD

---
Kaevandamisbasseinide kontekstis on aktsia näitaja, mida kasutatakse üksiku kaevuri panuse mõõtmiseks basseinis. See näitaja on aluseks tasu arvutamisel, mida koondis igale kaevandajale ümber jaotab. Iga aktsia vastab hashile, mis vastab Bitcoini võrgustiku raskusastme eesmärgist madalamale raskusastmele.

Selgitamaks seda analoogia abil, vaadelge 20-suunalist täringut. Oletame, et Bitcoini puhul tuleb ploki valideerimiseks (st 1 või 2 tulemuse saavutamiseks) veeretada number, mis on väiksem kui 3. See tähendab, et töö tõestamiseks tuleb veeretada number, mis on väiksem kui 3. Nüüd kujutage ette, et kaevandamisbasseinis on raskuse sihtarvuks seatud 10. Seega loeb üksiku kaevandaja jaoks iga täringuviskamine, mille tulemus on väiksem kui 10, kehtivaks osaks. Seejärel edastab kaevandaja need aktsiad basseinile, et nõuda oma tasu, isegi kui need ei vasta Bitcoini ploki jaoks kehtivale tulemusele.

Iga arvutatud hash-i puhul võib üks kaevandaja basseinis kokku puutuda kolme erineva stsenaariumiga:


- Kui hash-väärtus on suurem või võrdne basseini seatud raskuse sihtmääraga, siis ei ole sellest hash-väärtusest kasu. Seejärel muudab kaevandaja oma nonce'i, et proovida uut hash'i: `hash > share > block`.
- Kui hash on madalam kui aktsia raskusastme eesmärk, kuid suurem või võrdne Bitcoini raskusastme eesmärgiga, siis see hash kujutab endast kehtivat aktsiat, mis ei ole aga piisav ploki valideerimiseks. Kaevandaja võib selle hashi saata oma basseini, et nõuda aktsia juurde kuuluvat tasu: "share > hash > block".
- Kui hash on madalam kui Bitcoini võrgustiku raskusastme eesmärk, loetakse see nii kehtivaks osaks kui ka kehtivaks plokiks. Kaevandaja edastab selle hashi oma poolile, kes kiirustab selle edastamist Bitcoini võrgus. See hash loetakse kaevandaja jaoks samuti kehtivaks share'iks: "share > bloc > hash".

![](../../dictionnaire/assets/32.webp)

Seda aktsiasüsteemi kasutatakse iga üksiku kaevuri poolt tehtud töö hindamiseks basseinis, ilma et oleks vaja eraldi ümber arvutada kõiki kaevuri poolt genereeritud hash'e, mis oleks basseini jaoks täiesti ebaefektiivne.

Kaevandamisbasseinid kohandavad aktsiate raskusastet, et tasakaalustada kontrollkoormust ja tagada, et iga kaevandaja, olgu ta siis väike või suur, esitab aktsiaid umbes iga paari sekundi tagant. See võimaldab iga kaevuri hashrate'i täpset arvutamist ja tasu jaotamist vastavalt valitud hüvitise arvutamise meetodile (PPS, PPLNS, TIDES...).

> ► *Fransi keeles võib "shares" tõlkida kui "osa".*