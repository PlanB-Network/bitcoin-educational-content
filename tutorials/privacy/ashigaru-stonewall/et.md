---
name: Ashigaru - Stonewall
description: Stonewall-tehingute mõistmine ja kasutamine Ashigaru's
---
![cover stonewall](assets/cover.webp)



> *Murda plokiahela analüüsi eeldused matemaatiliselt tõestatava kahtlusega sinu tehingute saatja ja saaja vahel.*

## Mis on Stonewall-tehing?



Stonewall on Bitcoin tehingu erivorm, mille eesmärk on suurendada kasutajate konfidentsiaalsust kulutuste tegemisel, imiteerides kahe inimese vahelist mündiühendust, ilma et see tegelikult oleks üks. Tegelikult ei ole see tehing koostööpõhine. Kasutaja võib selle ise ehitada, kasutades sisendina ainult talle kuuluvaid UTXOsid. Seega saate luua Stonewall-tehingu mis tahes korral, ilma et peaksite teise kasutajaga sünkroonima.



Stonewall-tehing toimib järgmiselt: tehingu sisendina kasutab emitent 2 UTXO, mis kuuluvad talle. Väljundi poolel annab tehing 4 väljundit, millest 2 on täpselt sama suured. Ülejäänud 2 on välisvaluuta. Neist kahest sama suurusest väljundist läheb tegelikult ainult üks makse saajale.



Seega on Stonewalli tehingus ainult 2 rolli:




- Emitent, kes teeb tegeliku makse ;
- Saaja, kes ei pruugi olla teadlik tehingu eripärast ja lihtsalt ootab saatjalt makset.



Võtame selle tehingustruktuuri mõistmiseks näite. Alice on pagariäris, et osta oma baguette'i, mis maksab 4000 eurot sats`. Ta soovib maksta bitcoin'idega, säilitades samal ajal mingi konfidentsiaalsuse oma makse kohta. Seega otsustab ta makse jaoks luua Stonewall-tehingu.



![image](assets/fr/01.webp)



Analüüsides seda tehingut, näeme, et pagar on tõepoolest saanud baguette'i eest 4000 sats. Alice kasutas sisendina 2 UTXO: üks "10 000 sats" ja üks "15 000 sats". Väljundipoolel on ta saanud tagasi 3 UTXO: üks summas 4 000 sats, üks summas 6 000 sats ja üks summas 11 000 sats. Alice netosaldo on seega 4 000 sats, mis vastab hästi baguette'i hinnale.



Selles näites olen mining tasud tahtlikult kõrvale jätnud, et muuta see arusaadavamaks. Tegelikkuses kannab tehingukulud täielikult emitent.



## Mis vahe on Stonewalli ja Stonewall x2 vahel?



Stonewall-tehing toimib samamoodi nagu StonewallX2-tehing, kuid viimane nõuab erinevalt klassilisest Stonewall-tehingust koostööd, millest tuleneb ka nimetus "x2". See on tingitud sellest, et Stonewall-tehingu täitmine ei vaja välist koostööd: saatja saab selle teostada ilma teise isiku abita. Seevastu Stonewall x2 tehingu puhul liitub protsessiga täiendav osaleja, keda nimetatakse "koostööpartneriks". Ta panustab tehingusse lisaks saatja bitcoinidele ka oma bitcoinid ja võtab lõpus üle kogu summa (modulo mining kulud).



Tuleme tagasi meie näite juurde Alice pagariäris. Kui ta oleks tahtnud teha Stonewall x2 tehingu, oleks Alice pidanud tehingu tegemisel tegema koostööd Bob-ga (kolmas isik). Mõlemad oleksid toonud UTXO. Bob oleks siis saanud kogu oma panuse tagasi. Pagar oleks saanud oma baguette'i eest tasu samamoodi nagu Stonewalli tehingu puhul, samas kui Alice oleks saanud tagasi oma esialgse saldo, millest oleks maha arvatud baguette'i maksumus.



![image](assets/fr/02.webp)



Väljastpoolt vaadatuna oleks tehing jäänud täpselt samaks.



![image](assets/fr/03.webp)



Kokkuvõttes on Stonewalli ja Stonewall x2 tehingute struktuur identne. Nende kahe erinevus seisneb nende koostöölises või mittekoostöödelises olemuses. Stonewall-tehingut arendatakse individuaalselt, ilma koostööta. Stonewall x2 tehing seevastu tugineb kahe üksikisiku vahelisele koostööle.



[**-> Lisateave Stonewall-tehingute kohta x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Mis on Stonewalli tehingu mõte?



Stonewalli struktuur lisab tehingule tohutult entroopiat, mis hägustab ahelanalüüsi piire. Väljastpoolt vaadatuna võib sellist tehingut tõlgendada kui väikest mündiühendust kahe inimese vahel. Kuid tegelikkuses on see, nagu Stonewall x2 tehing, makse. Seega tekitab see meetod ahelaanalüüsis ebakindlust või viib isegi valede juhtnöörideni.



Võtame näiteks Alice pagariäri juures. Tehing plokiahelas näeks välja nii:



![image](assets/fr/04.webp)



Väline vaatleja, kes tugineb tavalisele ahelaanalüüsi heuristikale, võib ekslikult järeldada, et "**kaks inimest on teinud väikese coinjoini, mille sisendiks on kummalgi üks UTXO ja väljundiks kaks UTXOd**".



![image](assets/fr/05.webp)



See tõlgendus on ebatäpne, sest, nagu te teate, üks UTXO saadeti pagarile, 2 sissetulevat UTXO-d tulid Alicelt ja ta sai tagasi 3 vahetuskursi väljundit.



![image](assets/fr/01.webp)



Isegi kui välisvaatlejal õnnestub Stonewalli tehingu paterne tuvastada, ei ole tal kogu teavet. Ta ei suuda kindlaks teha, milline kahest samade summade UTXOst vastab maksele. Lisaks ei saa ta kindlaks teha, kas kaks sisestatud UTXOd on pärit kahelt erinevalt inimeselt või kuuluvad need ühele isikule, kes on need kokku viinud. Viimane punkt tuleneb asjaolust, et eespool nimetatud Stonewall x2 tehingud järgivad täpselt sama mustrit kui Stonewall tehingud. Väljastpoolt vaadatuna ja ilma täiendava kontekstilise teabeta on võimatu eristada Stonewall-tehingut ja Stonewall x2-tehingut. Esimesed ei ole koostööga seotud tehingud, samas kui viimased on koostööga seotud tehingud. See lisab kulule veelgi rohkem kahtlusi.



![image](assets/fr/03.webp)



## Kuidas ma teen Ashigarul Stonewall tehingu?



Algselt Samourai Wallet meeskonna poolt välja töötatud Stonewall-tehingud on üle võetud Ashigaru rakenduse poolt, mis on pärast Samourai arendajate arreteerimist loodud fork algse wallet. Sa pead installima Ashigaru ja looma wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Erinevalt Stowaway või Stonewall x2 (*cahoots*) tehingutest ei nõua Stonewall tehingud Paynyms'i kasutamist. Neid saab teostada otse, ilma eelneva ettevalmistuseta või koostööta teise kasutajaga.



Tegelikult ei ole teil tegelikult Stonewall-tehingute tegemiseks õpetust vaja, sest Ashigaru genereerib neid automaatselt iga kord, kui te kulutate, niipea kui teie wallet sisaldab piisavalt UTXO-d.



Klõpsake ekraani paremas allservas nupule "+" ja valige seejärel "Saada".



![Image](assets/fr/06.webp)



Valige konto, millelt soovite kulutusi teha.



![Image](assets/fr/07.webp)



Seejärel sisestage tehingu andmed: saaja aadress ja saadetav summa ning vajutage kinnitamiseks noolt.



![Image](assets/fr/08.webp)



Siin saate loomulikult kohandada vaikimisi tehingutasusid vastavalt turutingimustele. Kõige huvitavam element sellel lehel on siiski tehingu tüüp. Märkate, et Ashigaru on automaatselt valinud `STONEWALL`. Vajutage nupule `PREVIEW`, et rohkem teada saada.



![Image](assets/fr/09.webp)



Näete, et tehing on tõepoolest Stonewall-tüüpi: see koosneb 2 sama summa suurusest sisendist, 2 sama summa suurusest väljundist, samuti vahetusväljunditest ja minu puhul täiendavast sisendist, et rahuldada maksesumma.



![Image](assets/fr/10.webp)



Kui te ei soovi teha Stonewall-tehingut, vaid eelistate tavalist makset, klõpsake ekraani paremas ülaosas oleval pliiatsi ikoonil ja valige "STONEWALL" asemel "Lihtne".



![Image](assets/fr/11.webp)



Kui olete kõik üksikasjad kontrollinud, lohistage rohelist noolt ekraani allosas, et allkirjastada ja vabastada tehing.



![Image](assets/fr/12.webp)



Te teate nüüd, kuidas teostada Stonewall-tehingut, ja mis veelgi tähtsam, kuidas see toimib. Kui soovite rohkem teada saada, vaadake minu õpetust Ashigaru terminalist, kus selgitatakse, kuidas teha mündiühendusi Whirlpool kaudu.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add