---
term: VAIKIVAD MAKSED

---
Meetod staatiliste Bitcoini aadresside kasutamiseks maksete vastuvõtmiseks ilma aadressi korduvkasutamiseta, ilma interaktsioonita ja ilma nähtava seoseta erinevate maksete ja staatilise aadressi vahel. See meetod välistab vajaduse luua iga tehingu jaoks uued, kasutamata vastuvõtuaadressid, vältides seega Bitcoinis tavapäraseid interaktsioone, kus saaja peab maksjale andma uue aadressi.

Silent Payments'i puhul kasutab maksja iga makse jaoks uue aadressi genereerimiseks sisendina saaja avalikke võtmeid (spend public key ja scan public key) ja oma isiklike võtmete summat. Ainult saaja saab oma isiklike võtmetega arvutada sellele makseaadressile vastava isikliku võtme. ECDH (*Elliptic-Curve Diffie-Hellman*) on krüptograafiline võtmevahetusalgoritm, mida kasutatakse jagatud saladuse loomiseks, mida seejärel kasutatakse vastuvõtva aadressi ja privaatvõtme tuletamiseks (ainult saaja poolel). Et tuvastada neile mõeldud vaikimisi makseid, peavad vastuvõtjad skaneerima plokiahelat ja uurima iga protokolli kriteeriumidele vastavat tehingut. Erinevalt BIP47, mis kasutab maksekanali loomiseks teavitustehingut, jätab Silent Payments selle sammu ära, salvestades tehingu. Kompromiss seisneb siiski selles, et saaja peab skaneerima kõik võimalikud tehingud, et ECDH-i kohaldades kindlaks teha, kas need on adresseeritud talle.

Näiteks Bobi staatiline aadress $B$ kujutab endast tema skaneerimise avaliku võtme ja tema avaliku võtme kulutamise kombinatsiooni:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Need võtmed on lihtsalt tuletatud järgmisest teest:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Selle staatilise aadressi on avaldanud Bob. Alice küsib selle välja, et teha Bobile vaikne makse. Ta arvutab Bobi makseaadressi $P_0$ järgmiselt:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Kus:

$$ \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A) $$

Koos:


- $B_{\text{scan}}$: Bobi skaneerimise avalik võti (staatiline aadress);
- $B_{\text{spend}}$: Bobi kulutatud avalik võti (staatiline aadress);
- $A$: Avalike võtmete summa sisendis (tweak);
- $a$: Tweak'i privaatne võti, st kõigi võtmepaaride summa, mida kasutatakse `scriptPubKey` UTXOs, mida kasutatakse Alice'i tehingu sisendina;
- $\text{outpoint}_L$: Väikseim UTXO (leksikograafiliselt), mida kasutatakse Alice'i tehingus sisendina;
- $\text{ ‖ }$: Konkatenatsioon (operandide liitmine otsast lõpuni);
- $G$: Elliptilise kõvera `secp256k1` generaatorpunkt;
- $\text{hash}$: SHA256 hash-funktsioon, mis on märgistatud `BIP0352/SharedSecret`;
- $P_0$: Esimene avalik võti / unikaalne aadress Bobile maksmiseks;
- $0$: Täisarv, mida kasutatakse mitme unikaalse makseaadressi genereerimiseks.

Bob skaneerib plokiahelat, et leida oma Silent Payment sellisel viisil:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Koos:


- $b_{\text{scan}}$: Bobi privaatne skaneerimisvõti.

Kui ta leiab $P_0$ aadressi, mis sisaldab talle adresseeritud vaikivat makset, arvutab ta $p_0$, mis on privaatne võti, mis võimaldab tal kulutada Alice'i poolt $P_0$-le saadetud raha:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Koos:


- $b_{\text{spend}}$: Bobi privaatne kulutuste võti;
- $n$: elliptilise kõvera "secp256k1" järjekord.

Lisaks sellele põhiversioonile saab siltide abil samast põhilisest staatilisest aadressist genereerida ka mitu erinevat staatilist aadressi, eesmärgiga eraldada mitu kasutust, ilma et skaneerimise käigus nõutav töö põhjendamatult mitmekordistuks.