---
term: VAIGISTATUD MAKSUD
---

Meetod staatiliste Bitcoin aadresside kasutamiseks maksete vastuvõtmiseks ilma aadressi taaskasutuseta, ilma interaktsioonita ja ilma nähtava on-ahela seoseta erinevate maksete ja staatilise aadressi vahel. See tehnika kõrvaldab vajaduse iga tehingu jaoks genereerida uus, kasutamata vastuvõtu aadress, vältides seeläbi tavalisi interaktsioone Bitcoinis, kus saaja peab maksjale andma uue aadressi.

Vaigistatud maksete puhul kasutab maksja saaja avalikke võtmeid (kulutamise avalik võti ja skaneerimise avalik võti) ning oma privaatvõtmete summat sisendina, et genereerida iga makse jaoks värske aadress. Ainult saaja, oma privaatvõtmetega, suudab arvutada selle makseaadressi vastava privaatvõtme. ECDH (*Elliptilise Kõvera Diffie-Hellmani*), krüptograafiline võtmevahetuse algoritm, kasutatakse ühise saladuse loomiseks, mida seejärel kasutatakse vastuvõtu aadressi ja privaatvõtme tuletamiseks (ainult saaja poolel). Selleks, et tuvastada neile mõeldud Vaigistatud Makseid, peavad saajad skaneerima plokiahelat ja uurima iga protokolli kriteeriumidele vastavat tehingut. Erinevalt BIP47-st, mis kasutab teavitustehingut maksekanali loomiseks, kõrvaldavad Vaigistatud Maksed selle sammu, säästes tehingu. Kompromiss on aga see, et saaja peab skaneerima kõik potentsiaalsed tehingud, et määrata ECDH rakendamisega, kas need on adresseeritud neile.

Näiteks Bobi staatiline aadress $B$ esindab tema skaneerimise avaliku võtme ja kulutamise avaliku võtme konkatenatsiooni:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Need võtmed on lihtsalt tuletatud järgmiselt teelt:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Bob avaldab selle staatilise aadressi. Alice taastab selle, et teha Vaigistatud Makse Bobile. Ta arvutab Bobi makseaadressi $P_0$ järgmiselt:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Kus:

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

Koos:
* $B_{\text{scan}}$: Bobi skaneerimise avalik võti (staatiline aadress);
* $B_{\text{spend}}$: Bobi kulutamise avalik võti (staatiline aadress);
* $A$: Sisendis olevate avalike võtmete summa (tweak);
* $a$: Tweaki privaatvõti, st kõigi Alice'i tehingus kasutatud `scriptPubKey` UTXO-de sisenditena tarbitud võtmepaaride summa;
* $\text{outpoint}_L$: Lexikograafiliselt väikseim UTXO, mida kasutatakse sisendina Alice'i tehingus;
* $\text{ ‖ }$: Konkatenatsioon (operandide otsast-otsani ühendamise operatsioon);
* $G$: Elliptilise kõvera `secp256k1` generaatorpunkt;
* $\text{hash}$: SHA256 räsifunktsioon, märgistatud kui `BIP0352/SharedSecret`;
* $P_0$: Esimene avalik võti / unikaalne makseaadress makseks Bobile;
* $0$: Mitme unikaalse makseaadressi genereerimiseks kasutatud täisarv.

Bob skaneerib plokiahelat, et leida oma Vaigistatud Makse järgmiselt:
$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Sellega:
* $b_{\text{scan}}$: Bobi privaatne skaneerimisvõti.

Kui ta leiab $P_0$ aadressina, mis sisaldab talle suunatud Vaikset Makset, arvutab ta $p_0$, privaatvõtme, mis võimaldab tal kulutada Alice'i poolt $P_0$ saadetud vahendeid:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Sellega:
* $b_{\text{spend}}$: Bobi privaatne kulutamisvõti;
* $n$: elliptilise kõvera `secp256k1` järjekord.

Lisaks sellele põhiversioonile saab silte kasutada ka mitme erineva staatilise aadressi genereerimiseks samast põhilisest staatilisest aadressist, eesmärgiga eraldada mitu kasutust ilma skaneerimisel nõutava töö hulka ebamõistlikult suurendamata.