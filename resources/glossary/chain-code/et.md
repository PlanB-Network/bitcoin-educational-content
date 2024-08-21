---
term: AHETEKETI KOOD
---

Hierarhilise deterministliku (HD) tuletamise kontekstis Bitcoin'i rahakottide puhul on ahelakood 256-bitine krüptograafiline soolaväärtus, mida kasutatakse lapsevõtmete genereerimiseks vanemvõtmest vastavalt BIP32 standardile. Ahelakoodi kasutatakse koos vanemvõtmega ja lapse indeksiga, et deterministlikult genereerida uus võtmepaar (privaatvõti ja avalik võti) ilma vanemvõtit või muid tuletatud lapsevõtmeid paljastamata.

Seega on igal võtmepaaril unikaalne ahelakood. Ahelakood saadakse kas rahakoti seemne räsimisel ja bitide parema poole võtmisel. Sellisel juhul nimetatakse seda meistri ahelakoodiks, mis on seotud meistri privaatvõtmega. Alternatiivselt võib selle saada vanemvõtme ja selle vanema ahelakoodi ning indeksi räsimisel, seejärel paremate bitide hoidmisel. Siis nimetatakse seda lapse ahelakoodiks.

Ilma iga vanemapaari seotud ahelakoodi teadmata on võtmete tuletamine võimatu. See toob tuletamisprotsessi pseudojuhuslikke andmeid, et tagada krüptograafiliste võtmete genereerimine ründajate jaoks ettearvamatuks, samal ajal kui rahakoti omaniku jaoks jääb see deterministlikuks.

> ► *Inglise keeles nimetatakse "code de chaîne" "ahelakoodiks" ja "code de chaîne maître" "meistri ahelakoodiks".*