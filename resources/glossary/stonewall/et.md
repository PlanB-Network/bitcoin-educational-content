---
term: STONEWALL
---

Konkreetne Bitcoin'i tehingu vorm, mille eesmärk on suurendada kasutaja privaatsust kulutamise ajal, jäljendades kahe inimese vahelist coinjoin'i, ilma et see tegelikult oleks. Tegelikult ei ole see tehing koostööpõhine. Kasutaja saab selle ise koostada, kasutades sisenditena ainult oma UTXO-sid. Seega, saate luua Stonewall tehingu igaks juhuks, ilma et peaksite teise kasutajaga sünkroniseerima.

Stonewall tehingu toimimine on järgmine: tehingu sisendis kasutab saatja 2 endale kuuluvat UTXO-d. Tehing toodab seejärel 4 väljundit, millest 2 on täpselt sama summa. Ülejäänud 2 on vahetusraha. Kahest samas summas väljundist läheb tegelikult ainult üks makse saajale.

Seega on Stonewall tehingus ainult 2 rolli:
* Saatja, kes teeb tegeliku makse;
* Saaja, kes võib olla tehingu eripärast teadmata ja lihtsalt ootab saatjalt makset.

![](../../dictionnaire/assets/33.png)
Stonewall tehingud on saadaval nii Samourai Wallet rakenduses kui ka Sparrow Wallet tarkvaras.

Stonewall struktuur lisab tehingule palju entroopiat ja varjab jälge ahela analüüsi jaoks. Väljastpoolt vaadates võib sellist tehingut tõlgendada kui väikest coinjoin'i kahe inimese vahel. Kuid tegelikkuses, nagu ka Stonewall x2 tehingu puhul, on see makse. See meetod tekitab seega ahela analüüsis ebakindlust või isegi viib valedeni. Isegi kui väline vaatleja suudab tuvastada Stonewall tehingu mustrit, ei oma nad kogu teavet. Nad ei suuda kindlaks teha, kumb kahest samas summas UTXO-st vastab maksele. Lisaks ei suuda nad kindlaks teha, kas kaks sisendis olevat UTXO-d pärinevad kahest erinevast inimesest või kuuluvad need ühele inimesele, kes need ühendas. Viimane punkt tuleneb asjaolust, et Stonewall x2 tehingud järgivad täpselt sama mustrit kui Stonewall tehingud. Väljastpoolt ja ilma lisakontekstita on võimatu eristada Stonewall tehingut Stonewall x2 tehingust. Siiski, esimesed ei ole koostööpõhised tehingud, samas kui viimased on. See lisab veelgi kahtlust selle kulutuse üle.