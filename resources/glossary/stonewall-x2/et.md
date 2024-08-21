---
term: STONEWALL X2
---

Konkreetne Bitcoin'i tehingu vorm, mille eesmärk on suurendada kasutaja privaatsust kulutamise ajal, tehes koostööd kolmanda osapoolega, kes ei ole kulutusega seotud. See meetod simuleerib mini-coinjoin'i kahe osaleja vahel, tehes samal ajal makse kolmandale osapoolele. Stonewall x2 tehingud on saadaval nii Samourai Wallet rakenduses kui ka Sparrow Wallet tarkvaras (mõlemad on omavahel ühilduvad).

Selle toimimine on suhteliselt lihtne: see kasutab meie valduses olevat UTXO-d makse tegemiseks ja otsib kolmanda osapoole abi, kes samuti panustab oma valduses oleva UTXO-ga. Tehing lõppeb nelja väljundiga: kaks neist võrdsetes summas, üks mõeldud makse saaja aadressile, teine koostööpartneri aadressile. Kolmas UTXO saadetakse tagasi teisele koostööpartneri aadressile, võimaldades neil algsumma taastada (neile neutraalne tegevus, miinus kaevandamistasud), ja viimane UTXO naaseb aadressile, mis kuulub meile, mis kujutab endast maksest üle jäänud raha. Seega on Stonewall x2 tehingutes määratletud kolm erinevat rolli:
* Saatja, kes teeb tegeliku makse;
* Koostööpartner, kes annab bitcoine, et parandada tehingu üldist anonüümsust, taastades lõpuks täielikult oma vahendid;
* Saaja, kes võib olla tehingu konkreetsest olemusest teadmata ja lihtsalt ootab saatjalt makset.

![](../../dictionnaire/assets/3.png)

Stonewall x2 struktuur lisab tehingule palju entroopiat ja segab ahelanalüüsi jälgi. Väljastpoolt vaadates võib sellist tehingut tõlgendada kui väikest coinjoin'i kahe inimese vahel. Kuid tegelikkuses on see makse. See meetod tekitab seega ahelanalüüsis ebakindlust või isegi viib valejälgedeni. Isegi kui väline vaatleja suudab tuvastada Stonewall x2 tehingu mustri, ei oma nad kogu teavet. Nad ei suuda kindlaks teha, kumb kahest võrdsest summas UTXO-st vastab maksele. Lisaks ei saa nad teada, kes tegi makse. Lõpuks ei suuda nad kindlaks teha, kas kaks sisend-UTXO-d pärinevad kahest erinevast inimesest või kuuluvad need ühele inimesele, kes need ühendas. Viimane punkt tuleneb asjaolust, et klassikalised Stonewall tehingud järgivad täpselt sama mustrit kui Stonewall x2 tehingud. Väljastpoolt ja ilma konteksti lisateabeta on võimatu eristada Stonewall tehingut Stonewall x2 tehingust. Siiski, esimesed ei ole koostöö tehingud, samas kui viimased on. See lisab veelgi kahtlust kulutuse üle.