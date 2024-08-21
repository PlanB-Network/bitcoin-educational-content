---
term: SILD (VAIKSED MAKSUD)
---

Vaiksete Maksete protokollis kasutatakse silte kui täisarve, et muuta algset staatilist aadressi, luues nii mitmeid teisi staatilisi aadresse. Nende siltide kasutamine võimaldab eristada Vaiksete Maksete kaudu saadetud makseid, kasutades iga kasutuskorra jaoks erinevaid staatilisi aadresse, ilma et see suurendaks oluliselt operatiivset koormust nende maksete tuvastamiseks (skaneerimiseks). Bob kasutab staatilist aadressi $B$, mis koosneb kahest avalikust võtmest: $B_{\text{scan}}$ skaneerimiseks ja $B_{\text{spend}}$ kulutamiseks. Avaliku võtme $B_{\text{spend}}$ juurde lisatakse $b_{\text{scan}}$ räsi ja täisarv $m$, mis on skalaarselt korrutatud generaatorpunkti $G$-ga, luues nii uut tüüpi kulutamise avaliku võtme $B_m$:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Näiteks esimene võti $B_1$ saadakse sel viisil:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

Bob'i poolt avaldatud staatiline aadress koosneb nüüd $B_{\text{scan}}$-st ja $B_m$-st. Näiteks esimene staatiline aadress sildiga $1$ on:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Alustame sildist $1$, kuna silt $0$ on reserveeritud vahetusrahaks. Alice, kes soovib saata bitcoine Bob'i poolt pakutud sildistatud staatilisele aadressile, tuletatakse unikaalne makseaadress $P_0$, kasutades uut $B_1$ asemel $B_{\text{spend}}$:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Tegelikkuses ei pruugi Alice isegi teada, et Bob'il on sildistatud aadress, kuna ta lihtsalt kasutab staatilise aadressi teist osa, mida antud juhul on väärtus $B_1$ mitte $B_{\text{spend}}$. Maksete skaneerimiseks kasutab Bob alati oma algse staatilise aadressi väärtust koos $B_{\text{spend}}$-ga sel viisil:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Seejärel lihtsalt lahutab ta leitud väärtuse $P_0$ iga väljundi puhul ükshaaval. Seejärel kontrollib ta, kas ühe nende lahutuste tulemustest vastab ühele tema rahakotis kasutatavatest siltidest. Kui see vastab, näiteks väljundi #4 puhul sildiga $1$, tähendab see, et see väljund on Vaikne Makse, mis on seotud tema staatilise aadressiga sildiga $B_1$:
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

See töötab, sest:
$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$
Tänu sellele meetodile saab Bob kasutada mitmeid staatilisi aadresse (nagu $B_1$, $B_2$, $B_3$...), mis kõik on tuletatud tema baasstaatilisest aadressist ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), et korrektselt eristada erinevaid kasutusviise.

Siiski, see staatiliste aadresside eraldamine kehtib ainult isikliku rahakoti haldamise vaatenurgast, kuid ei võimalda identiteetide eraldamist. Kuna neil kõigil on sama $B_{\text{scan}}$, on väga lihtne kõik staatilised aadressid omavahel seostada ja järeldada, et need kuuluvad ühele entiteedile.