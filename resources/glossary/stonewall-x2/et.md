---
term: STONEWALL X2

---
Bitcoini tehingu erivorm, mille eesmärk on suurendada kasutaja privaatsust kulutuste ajal, tehes koostööd kolmanda osapoolega, kes ei ole kulutustega seotud. See meetod simuleerib kahe osaleja vahelist mini-mündiühendust, tehes samal ajal makse kolmandale osapoolele. Stonewall x2 tehingud on saadaval nii Samourai Wallet'i rakenduses kui ka Sparrow Wallet'i tarkvaras (mõlemad on koostalitlusvõimelised).

Selle toimimine on suhteliselt lihtne: makse tegemiseks kasutatakse meie valduses olevat UTXO-d ja palutakse kolmanda isiku abi, kes samuti panustab oma UTXO-ga. Tehing lõpeb nelja väljundiga: kaks võrdset summat, millest üks on mõeldud makse saaja aadressile, teine aga koostööpartnerile kuuluvale aadressile. Kolmas UTXO saadetakse tagasi teisele koostööpartneri aadressile, mis võimaldab tal saada tagasi esialgse summa (tema jaoks neutraalne tegevus, millest on maha arvatud kaevandamistasud), ja viimane UTXO läheb tagasi meile kuuluvale aadressile, mis kujutab endast makse muutust. Seega on Stonewall x2 tehingutes määratletud kolm erinevat rolli:


- Saatja, kes teeb tegeliku makse;
- Koostööpartner, kes annab bitcoinid, et parandada tehingu üldist anonüümsust, saades samal ajal oma vahendid lõpus täielikult tagasi;
- Vastuvõtja, kes ei pruugi olla teadlik tehingu eripärast ja ootab lihtsalt saatjalt makset.

![](../../dictionnaire/assets/3.webp)

Stonewall x2 struktuur lisab tehingule palju entroopiat ja segab ahelanalüüsi jälgi. Väljastpoolt võib sellist tehingut tõlgendada kui kahe inimese vahelist väikest mündiühendust. Kuid tegelikkuses on see makse. Seega tekitab see meetod ahelaanalüüsis ebakindlust või viib isegi valede jälgedeni. Isegi kui välise vaatleja suudab tuvastada Stonewall x2 tehingu mustri, ei ole tal kogu teave olemas. Ta ei suuda kindlaks teha, milline kahest võrdse suurusega UTXOst vastab maksele. Peale selle ei saa ta teada, kes makse tegi. Lõpuks ei saa nad ka kindlaks teha, kas kaks sisestatud UTXOd pärinevad kahelt erinevalt inimeselt või kuuluvad nad ühele isikule, kes neid ühendas. Viimane punkt tuleneb asjaolust, et klassikalised Stonewall-tehingud järgivad täpselt sama mustrit kui Stonewall x2-tehingud. Väljastpoolt ja ilma lisateabeta konteksti kohta on võimatu eristada Stonewall-tehingut Stonewall x2-tehingust. Esimesed ei ole siiski koostöötehingud, samas kui viimased on koostöötehingud. See lisab kulude suhtes veelgi rohkem kahtlusi.