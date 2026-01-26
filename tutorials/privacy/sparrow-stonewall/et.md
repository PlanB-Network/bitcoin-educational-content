---
name: Sparrow Wallet - Stonewall
description: Stonewall-tehingute mõistmine ja kasutamine Sparrows
---

![cover](assets/cover.webp)




> *Murda plokiahela analüüsi eeldused matemaatiliselt tõestatava kahtlusega sinu tehingute saatja ja saaja vahel.*

## Mis on Stonewall-tehing?



Stonewall on Bitcoin tehingu erivorm, mille eesmärk on suurendada kasutajate konfidentsiaalsust kulutuste tegemisel, imiteerides kahe inimese vahelist mündiühendust, ilma et see tegelikult oleks üks. Tegelikult ei ole see tehing koostööpõhine. Kasutaja võib seda ise ehitada, kasutades sisendina ainult talle kuuluvaid UTXOsid. Seega saate luua Stonewall-tehingu ükskõik millisel juhul, ilma et peaksite teise kasutajaga sünkroonima.



Stonewall-tehing toimib järgmiselt: tehingu sisendina kasutab emitent 2 UTXO, mis kuuluvad talle. Väljundi poolel toodab tehing 4 väljundit, millest 2 on täpselt sama suured. Ülejäänud 2 on välisvaluuta. Neist kahest sama suurusest väljundist läheb tegelikult ainult üks makse saajale.



Seega on Stonewalli tehingus ainult 2 rolli:




- Emitent, kes teeb tegeliku makse ;
- Saaja, kes ei pruugi olla teadlik tehingu eripärast ja lihtsalt ootab saatjalt makset.



Võtame selle tehingustruktuuri mõistmiseks näite. Alice on pagariäris, et osta oma baguette'i, mis maksab 4000 eurot sats". Ta soovib maksta bitcoinides, säilitades samal ajal mingi konfidentsiaalsuse oma makse kohta. Seega otsustab ta makse jaoks luua Stonewall-tehingu.



![image](assets/fr/01.webp)



Analüüsides seda tehingut, näeme, et pagar on tõepoolest saanud baguette'i eest 4000 sats. Alice kasutas sisendina 2 UTXOd: üks 10 000 sats ja teine 15 000 sats. Väljundiks on ta saanud 3 UTXO: üks 4 000 sats, üks 6 000 sats ja üks 11 000 sats. Alice netosaldo on seega 4 000 sats, mis vastab hästi baguette'i hinnale.



Selles näites olen mining tasud tahtlikult kõrvale jätnud, et muuta see arusaadavamaks. Tegelikkuses kannab tehingukulud täielikult emitent.



## Mis vahe on Stonewalli ja Stonewall x2 vahel?



Stonewall-tehing toimib samamoodi nagu StonewallX2-tehing, kuid viimane nõuab erinevalt klassilisest Stonewall-tehingust koostööd, millest tuleneb ka nimetus "x2". See on tingitud sellest, et Stonewall-tehingu täitmine ei vaja välist koostööd: saatja saab selle teostada ilma teise isiku abita. Seevastu Stonewall x2 tehingu puhul liitub protsessiga täiendav osaleja, keda nimetatakse "koostööpartneriks". Ta panustab tehingusse lisaks saatja bitcoinidele ka oma bitcoinid ja võtab lõpus üle kogu summa (miinus mining kulud).



Tuleme tagasi meie näite juurde Alice pagariäris. Kui ta oleks tahtnud teha Stonewall x2 tehingu, oleks Alice pidanud tehingu tegemisel tegema koostööd Bob-ga (kolmas osapool). Mõlemad oleksid toonud UTXO. Bob oleks siis väljumisel saanud oma panuse täies ulatuses kätte. Pagar oleks saanud oma baguette'i eest tasu samamoodi nagu Stonewalli tehingu puhul, samas kui Alice oleks saanud tagasi oma esialgse saldo, millest oleks maha arvatud baguette'i maksumus.



![image](assets/fr/02.webp)



Väljastpoolt vaadatuna oleks tehing jäänud täpselt samaks.



![image](assets/fr/03.webp)



Kokkuvõttes on Stonewalli ja Stonewall x2 tehingute struktuur identne. Nende kahe erinevus seisneb nende koostöölises või mittekoostöödelises olemuses. Stonewall-tehingut arendatakse individuaalselt, ilma koostööta. Stonewall x2 tehing seevastu tugineb kahe üksikisiku vahelisele koostööle.



[**-> Lisateave Stonewall-tehingute kohta x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Mis on Stonewalli tehingu mõte?



Stonewalli struktuur lisab tehingule tohutult entroopiat, mis hägustab ahelanalüüsi piire. Väljastpoolt vaadatuna võib sellist tehingut tõlgendada kui väikest mündiühendust kahe inimese vahel. Kuid tegelikult on see, nagu ka Stonewall x2 tehing, makse. Seetõttu tekitab see meetod ahelanalüüsis ebakindlust või isegi viib valede juhtnöörideni.



Võtame näiteks Alice pagariäri juures. Tehing plokiahelas näeks välja nii:



![image](assets/fr/04.webp)



Väline vaatleja, kes tugineb tavalisele ahelaanalüüsi heuristikale, võib ekslikult järeldada, et "*kaks inimest on teinud väikese coinjoini, mille sisendiks on kummalgi üks UTXO ja väljundiks kaks UTXOd*".



![image](assets/fr/05.webp)



See tõlgendus on ebatäpne, sest, nagu te teate, üks UTXO saadeti pagarile, 2 sissetulevat UTXOd tulid Alicelt ja ta sai tagasi 3 vahetusväljundit.



![image](assets/fr/01.webp)



Isegi kui välisvaatlejal õnnestub Stonewalli tehingu paterne tuvastada, ei ole tal kogu teavet. Ta ei suuda kindlaks teha, milline kahest samade summade UTXOst vastab maksele. Lisaks ei saa ta kindlaks teha, kas kaks UTXO-kannet pärinevad kahelt erinevalt inimeselt või kuuluvad nad ühele isikule, kes on need omavahel ühendanud. Viimane punkt tuleneb asjaolust, et eespool nimetatud Stonewall x2 tehingud järgivad täpselt sama mustrit kui Stonewall tehingud. Väljastpoolt vaadatuna ja ilma täiendava kontekstilise teabeta on võimatu eristada Stonewall-tehingut ja Stonewall x2-tehingut. Esimesed ei ole koostööga seotud tehingud, samas kui viimased on koostööga seotud tehingud. See lisab kulule veelgi rohkem kahtlusi.



![image](assets/fr/03.webp)



## Kuidas teha Stonewall-tehing Sparrow-s?



Algselt välja töötatud Samurai Wallet meeskond, Stonewall tehingute võeti üle Ashigaru taotluse, fork algse portfelli loodud pärast arreteerimist Samurai arendajad, ja ka Sparrow Wallet.



Teil on vaja paigaldada Sparrow ja luua :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Erinevalt Stowaway või Stonewall x2 (*cahoots*) tehingutest ei nõua Stonewall tehingud Paynyms'i kasutamist. Neid saab teostada otse, ilma erilise ettevalmistuseta või koostööta teise kasutajaga.



Stonewall-tehingu tegemiseks Sparrow-l on protseduur väga lihtne: alustage tehingu loomisega nagu tavaliselt, kas menüüst `Send` või menüüst `UTXOs`, kui soovite teha *Coin Control*.



![Image](assets/fr/06.webp)



Seejärel sisestage tehingu üksikasjad: saaja aadress, etikett, saadetav summa ja tasu suurus või määr, sõltuvalt turutingimustest.



![Image](assets/fr/07.webp)



Enne kinnitamist saate siin valida Stonewalli struktuuri. Kasutajaliidese allosas asendage `Efektiivsus` sõnaga `Privaatsus`. Kui see valik ei ilmu, tähendab see, et teie portfellis ei ole piisavalt palju UTXOsid, et seda tüüpi tehingut ehitada.



![Image](assets/fr/08.webp)



Pärast valiku "Privaatsus" valimist märkate, et tehingu struktuur muutub täielikult: see muutub Stonewall-tehinguks, mis tarbib sisendina mitu teie UTXO-d ja annab kaks identsete summadega väljundit, millest üks vastab tegelikule maksele "100 000 sats", lisaks vahetusväljunditele.



![Image](assets/fr/09.webp)



Kui kõik on õige, klõpsake nuppu "Loo tehing".



Seejärel saate veelkord kontrollida oma tehingu üksikasju ja klõpsata nuppu "Tehingu allkirjastamiseks lõpuleviimine".



![Image](assets/fr/10.webp)



Seejärel allkirjastage tehing vastavalt teie portfellile iseloomulikule meetodile ja klõpsake "Tehingu edastamine", et edastada see Bitcoin võrgus, oodates kinnitust.



![Image](assets/fr/11.webp)



Te teate nüüd, kuidas Stonewall-tehing töötab Sparrow Wallet-s ja kuidas seda luua. Et süvendada nende tööriistade valdamist, mis on mõeldud teie onchaini konfidentsiaalsuse tugevdamiseks, kutsun teid üles jälgima minu BTC 204 koolitust Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c