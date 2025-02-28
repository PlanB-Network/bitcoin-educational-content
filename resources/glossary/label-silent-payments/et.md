---
term: (VAIKIVAD MAKSED)

---
Silent Payments'i protokollis on märgised täisarvud, mida kasutatakse esialgse staatilise aadressi muutmiseks, et luua palju teisi staatilisi aadresse. Nende märgiste kasutamine võimaldab eraldada vaikivate maksete kaudu saadetavad maksed, kasutades iga kasutuse jaoks erinevaid staatilisi aadresse, ilma et see suurendaks liigselt nende maksete tuvastamise (skaneerimise) koormust. Bob kasutab staatilist aadressi $B$, mis koosneb kahest avalikust võtmest: $B_{\text{scan}}$ skaneerimiseks ja $B_{\text{spend}}$ kulutamiseks. Kulutuste avalikule võtmele $B_{\text{scan}}$ lisatakse $b_{\text{scan}}$ ja täisarv $m$, mis on skalaarselt korrutatud generaatorpunktiga $G$, et luua mingi uus kulutuste avalik võti $B_m$:

$$ B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $ $$

Näiteks esimene võti $B_1$ saadakse sel viisil:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Bobi avaldatud staatiline aadress koosneb nüüd $B_{\text{scan}}$ ja $B_m$. Näiteks esimene staatiline aadress märgisega $1$ on järgmine:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Alustame ainult sildist $1$, sest silt $0$ on reserveeritud muutuste jaoks. Alice, kes soovib saata bitcoin'e Bobi poolt antud märgistatud staatilisele aadressile, tuletab unikaalse makseaadressi $P_0$, kasutades uut $B_1$ asemel $B_{\text{spend}}$:

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Tegelikkuses ei pruugi Alice isegi teada, et Bobil on märgistatud aadress, sest ta kasutab lihtsalt tema esitatud staatilise aadressi teist osa, mis antud juhul on väärtus $B_1$, mitte $B_{\text{spend}}$. Maksete otsimiseks kasutab Bob alati oma esialgse staatilise aadressi väärtust koos $B_{\text{spend}}$ sellisel viisil:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Seejärel ta lihtsalt lahutab igast väljundist ükshaaval leitud väärtuse $P_0$. Seejärel kontrollib ta, kas üks nende lahutamise tulemustest vastab ühe tema rahakotis kasutatava sildi väärtusele. Kui see vastab näiteks väljundi #4 puhul, millel on silt $1$, tähendab see, et see väljund on tema staatilise aadressiga $B_1$ seotud vaikiv makse:

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

See toimib, sest:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Tänu sellele meetodile saab Bob kasutada mitmeid staatilisi aadresse (koos $B_1$, $B_2$, $B_3$...), mis kõik on tuletatud tema põhilisest staatilisest aadressist ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}}$), et kasutusi korralikult eraldada.

Selline staatiliste aadresside eraldamine kehtib siiski ainult isikliku rahakoti haldamise seisukohast, kuid ei võimalda identiteedi eraldamist. Kuna neil kõigil on sama $B_{\text{scan}}$, on väga lihtne seostada kõik staatilised aadressid omavahel ja järeldada, et nad kuuluvad ühele isikule.