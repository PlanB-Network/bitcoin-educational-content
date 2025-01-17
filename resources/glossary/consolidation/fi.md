---
term: CONSOLIDATION

---
Erikoistapahtuma, jossa useita pieniä UTXO:ita yhdistetään yhteen syötteeseen, jolloin tuloksena on yksi suurempi UTXO. Tämä operaatio on omaan lompakkoon tehty transaktio. Yhdistämisen tavoitteena on hyödyntää aikoja, jolloin Bitcoin-verkon maksut ovat alhaiset, ja yhdistää useita pieniä UTXO:ita yhdeksi arvoltaan suuremmaksi. Näin se ennakoi pakollisia kuluja maksujen noustessa, mikä mahdollistaa säästöt tulevissa transaktiomaksuissa.

Paljon panoksia sisältävät maksutapahtumat ovatkin raskaampia ja näin ollen kalliimpia. Transaktiomaksuissa saavutettavien säästöjen lisäksi konsolidointi on myös pitkän aikavälin suunnittelua. Jos lompakossasi on hyvin pieniä UTXO:ita, niistä voi tulla käyttökelvottomia, jos Bitcoin-verkko joutuu pitkäksi aikaa korkeiden maksujen kauteen. Jos esimerkiksi tarvitset 10 000 satsin UTXO:n, mutta kaivostoiminnan vähimmäismaksut ovat 15 000 satsia, kulut ylittäisivät itse UTXO:n arvon. Näiden pienten UTXO:iden käytöstä tulee silloin taloudellisesti järjetöntä, ja ne pysyvät käyttökelvottomina niin kauan kuin maksut eivät laske. Näitä UTXO:ita kutsutaan yleisesti "pölyksi" Yhdistämällä säännöllisesti pieniä UTXO:itasi vähennät tätä maksujen korotuksiin liittyvää riskiä.

On kuitenkin tärkeää huomata, että konsolidointitapahtumat ovat tunnistettavissa ketjuanalyysin aikana. Tällainen liiketoimi osoittaa Common Input Ownership Heuristic (CIOH), mikä tarkoittaa, että konsolidointitapahtuman panokset omistaa yksi yksikkö. Tällä voi olla vaikutuksia käyttäjän yksityisyyteen.

![](../../dictionnaire/assets/7.webp)