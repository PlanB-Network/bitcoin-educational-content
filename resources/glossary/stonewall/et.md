---
term: STONEWALL

---
Bitcoini tehingu erivorm, mille eesmärk on suurendada kasutaja privaatsust kulutamise ajal, jäljendades kahe inimese vahelist mündiühendust, ilma et see tegelikult oleks üks. Tõepoolest, see tehing ei ole koostöövõimalus. Kasutaja võib selle konstrueerida üksi, kasutades sisendina ainult oma UTXOsid. Seega saate luua Stonewall-tehingu mis tahes korral, ilma et peaksite teise kasutajaga sünkroonima.

Stonewall-tehingu toimimine on järgmine: tehingu sisestamisel kasutab saatja 2 talle kuuluvat UTXO-d. Seejärel toodab tehing 4 väljundit, millest 2 on täpselt sama summa. Ülejäänud 2 moodustavad muutuse. Neist 2 väljundist, mille summa on sama, läheb tegelikult ainult üks makse saajale.

Seega on Stonewalli tehingus ainult 2 rolli:


- Saatja, kes teeb tegeliku makse;
- Vastuvõtja, kes ei pruugi olla teadlik tehingu eripärast ja ootab lihtsalt saatjalt makset.

![](../../dictionnaire/assets/33.webp)

Stonewall-tehingud on saadaval nii Samourai Wallet'i rakenduses kui ka Sparrow Wallet'i tarkvaras.

Stonewalli struktuur lisab tehingule palju entroopiat ja varjab ahelanalüüsi jälgi. Väljastpoolt võib sellist tehingut tõlgendada kui kahe inimese vahelist väikest mündiühendust. Tegelikkuses on see aga, nagu Stonewall x2 tehing, makse. Selline meetod tekitab seega ebakindlust ahelaanalüüsis või viib isegi valede jälgede tekkimiseni. Isegi kui välise vaatleja suudab Stonewalli tehingu mustri tuvastada, ei ole tal kogu teave olemas. Ta ei suuda kindlaks teha, milline kahest samade summade UTXOst vastab maksele. Lisaks sellele ei suuda ta kindlaks teha, kas kaks UTXO-d on pärit kahelt erinevalt inimeselt või kuuluvad nad ühele isikule, kes neid ühendas. Viimane punkt tuleneb asjaolust, et Stonewall x2 tehingud järgivad täpselt sama mustrit kui Stonewall tehingud. Väljastpoolt ja ilma täiendava kontekstiteabeta on võimatu eristada Stonewall-tehingut Stonewall x2-tehingust. Siiski ei ole esimesed tehingud koostöövõimalused, samas kui viimased on. See lisab selle kulu suhtes veelgi rohkem kahtlusi.