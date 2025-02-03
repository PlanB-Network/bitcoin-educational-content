---
term: UUDELLEENJÄRJESTELY

---
Viittaa ilmiöön, jossa lohkoketjun rakenne muuttuu, koska samalla korkeudella olevat kilpailevat lohkot ovat olemassa. Tämä tapahtuu, kun osa lohkoketjusta korvataan toisella ketjulla, jossa on enemmän kertynyttä työtä.

Nämä uudelleenjärjestelyt ovat osa Bitcoinin luonnollista toimintaa, jossa eri louhijat voivat löytää uusia lohkoja lähes samanaikaisesti, jolloin Bitcoin-verkko jakautuu kahtia. Tällaisissa tapauksissa verkko voi jakautua väliaikaisesti kilpaileviin ketjuihin. Lopulta, kun yhteen näistä ketjuista kertyy enemmän työtä, solmut hylkäävät muut ketjut, ja niiden lohkoista tulee niin sanottuja "vanhentuneita lohkoja" tai "orpoja lohkoja" Tämä prosessi, jossa yksi ketju korvataan toisella, on uudelleenjärjestelyä.

![](../../dictionnaire/assets/9.webp)

Uudelleenjärjestelyillä voi olla erilaisia seurauksia. Ensinnäkin, jos käyttäjän transaktio on vahvistettu lohkossa, joka osoittautuu hylätyksi, mutta tämä transaktio ei näy lopullisessa ketjussa, hänen transaktiostaan tulee jälleen vahvistamaton. Tämän vuoksi on suositeltavaa odottaa aina vähintään kuusi vahvistusta, jotta transaktio voidaan katsoa todella muuttumattomaksi. Kuuden lohkon jälkeen uudelleenjärjestelyt ovat niin epätodennäköisiä, että niiden mahdollisuutta voidaan pitää lähes olemattomana.

Lisäksi globaalilla järjestelmätasolla uudelleenjärjestelyt merkitsevät louhijoiden laskentatehon tuhlaamista. Kun jako tapahtuu, osa louhijoista on ketjussa "A" ja osa ketjussa "B". Jos ketju "B" lopulta hylätään uudelleenjärjestelyn aikana, kaikki louhijoiden käyttämä laskentateho tässä ketjussa on määritelmän mukaan hukkaan heitettyä. Jos Bitcoin-verkossa on liikaa uudelleenjärjestelyjä, sen yleinen turvallisuus heikkenee. Osittain tästä syystä lohkokoon kasvattaminen tai lohkojen välisen ajan (10 minuuttia) lyhentäminen voi olla vaarallista.

> ► *Jotkut bitcoin-asiakkaat käyttävät mieluummin termiä "orpo lohko" viittaamaan vanhentuneeseen lohkoon. Yleisessä kielenkäytössä "reorg" tarkoittaa myös "uudelleenjärjestelyä" Termi "reorganisaatio" on anglismi. Tarkemmin sanottuna voitaisiin puhua "uudelleensynkronoinnista "*