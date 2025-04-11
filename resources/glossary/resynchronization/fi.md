---
term: RESYNKRONOINTI

---
Viittaa ilmiöön, jossa lohkoketjun rakenne muuttuu, koska samalla korkeudella olevat kilpailevat lohkot ovat olemassa. Tämä tapahtuu, kun osa lohkoketjusta korvataan toisella ketjulla, jossa on enemmän kertynyttä työtä.

Nämä uudelleensynkronoinnit ovat osa Bitcoinin luonnollista toimintaa, jossa eri louhijat voivat löytää uusia lohkoja lähes samanaikaisesti, jolloin Bitcoin-verkko jakautuu kahtia. Tällaisissa tapauksissa verkko voi jakautua väliaikaisesti kilpaileviin ketjuihin. Lopulta, kun yhteen näistä ketjuista kertyy enemmän työtä, solmut hylkäävät muut ketjut, ja niiden lohkoista tulee niin sanottuja "vanhentuneita lohkoja" tai "orpoja lohkoja" Tämä prosessi, jossa yksi ketju korvataan toisella, on uudelleensynkronointia.

![](../../dictionnaire/assets/9.webp)

Uudelleen synkronoinnilla voi olla erilaisia seurauksia. Ensinnäkin, jos käyttäjän transaktio on vahvistettu lohkossa, joka osoittautuu hylätyksi, mutta tätä transaktiota ei löydy lopullisesti voimassa olevasta ketjusta, hänen transaktiostaan tulee jälleen vahvistamaton. Tämän vuoksi on suositeltavaa odottaa aina vähintään 6 vahvistusta, jotta transaktio voidaan katsoa todella muuttumattomaksi. Kuuden lohkon jälkeen uudelleen synkronoinnit ovat niin epätodennäköisiä, että niiden todennäköisyyttä voidaan pitää lähes olemattomana.

Lisäksi maailmanlaajuisen järjestelmän tasolla uudelleensynkronoinnit merkitsevät louhijoiden laskentatehon tuhlausta. Kun jako tapahtuu, jotkut louhijat ovat ketjussa A ja toiset ketjussa B. Jos ketju `B` lopulta hylätään uudelleensynkronoinnin aikana, kaikki louhijoiden käyttämä laskentateho tässä ketjussa on määritelmän mukaan hukkaan heitettyä. Jos Bitcoin-verkossa on liikaa uudelleensynkronointeja, verkon yleinen turvallisuus heikkenee. Osittain tästä syystä lohkokoon kasvattaminen tai lohkojen välisen ajan (10 minuuttia) lyhentäminen voi olla vaarallista.

> ► *Jotkut bitcoin-asiakkaat käyttävät mieluummin termiä "orpo lohko" viittaamaan vanhentuneeseen lohkoon. Lisäksi, vaikka se on anglikaaninen ilmaus, yleiskielessä "reorganisaatio" tai "reorg" on usein parempi kuin "resynkronisaatio" *