---
name: Ashigaru - Stonewall x2
description: Stonewall x2 tehingute mõistmine ja kasutamine Ashigarul
---
![cover stonewall x2](assets/cover.webp)



> *Tehke iga kulutamine mündiühenduseks

## Mis on Stonewall x2 tehing?



Stonewall x2 on Bitcoin tehingu erivorm, mille eesmärk on suurendada kasutaja konfidentsiaalsust kulutuste tegemisel, tehes koostööd kolmanda osapoolega, kes ei ole kulutustega seotud. See meetod simuleerib kahe osaleja vahelist minimündiühendust, tehes samal ajal makse kolmandale osapoolele. Stonewall x2-tehingud on saadaval Ashigaru rakenduses, mis on Samourai Wallet (selle tehinguliigi loomise taga olev meeskond) fork.



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Kuidas see toimib, on suhteliselt lihtne: te kasutate makse tegemiseks enda valduses olevat UTXO ja võtate appi kolmanda osapoole, kes samuti panustab oma UTXO-ga. Tehingu tulemuseks on neli väljundit: kaks võrdset summat, millest üks on mõeldud makse saaja aadressile, teine aga koostööpartnerile kuuluvale aadressile. Kolmas UTXO saadetakse tagasi teisele, koostööpartnerile kuuluvale aadressile, mis võimaldab tal esialgset summat tagasi saada (neutraalne tegevus tema jaoks, moduleerides mining kulusid), ja viimane UTXO saadetakse tagasi meile kuuluvale aadressile, mis moodustab makse vahetuse.



Stonewall x2 tehingutes on seega määratletud kolm erinevat rolli:




- Emitent, kes teeb tegeliku makse ;
- Koostööpartner, kes teeb bitcoinid kättesaadavaks, et parandada tehingu anonüümsust, saades samal ajal oma raha lõpus täies ulatuses tagasi (tema jaoks neutraalne tegevus, moduleeritud mining kulud);
- Saaja, kes ei pruugi olla teadlik tehingu eripärast ja lihtsalt ootab saatjalt makset.



Võtame ühe näite. Alice on pagariäris, et osta oma baguette'i, mis maksab 4000 sats". Ta soovib maksta bitcoinides, säilitades samal ajal oma makse kohta konfidentsiaalsuse. Seega kutsub ta oma sõbra Bob, kes teda selles aitab.



![image](assets/fr/01.webp)



Analüüsides seda tehingut, näeme, et pagar sai tegelikult 4000 sats baguette'i eest. Alice kasutas sisendina 10 000 sats ja sai väljundina tagasi 6 000 sats, mis annab netosaldo 4 000 sats, mis vastab baguette'i hinnale. Bob kasutas sisendina 15 000 sats ja sai kaks väljundit: üks 4 000 sats ja teine 11 000 sats, mis teeb saldoks 0.



Selles näites olen mining tasud tahtlikult kõrvale jätnud, et muuta see arusaadavamaks. Tegelikkuses jagunevad tehingutasud võrdselt makse väljastaja ja koostööpartneri vahel.



## Mis vahe on Stonewalli ja Stonewall x2 vahel?



StonewallX2-tehing toimib täpselt samamoodi nagu Stonewall-tehing, ainult et esimene on koostööl põhinev, teine aga mitte. Nagu me nägime, osaleb StonewallX2-tehingus kolmas osapool, kes on makse suhtes väline ja kes teeb oma bitcoinid kättesaadavaks, et suurendada tehingu konfidentsiaalsust. Klassikalise Stonewall-tehingu puhul võtab koostööpartneri rolli üle saatja.



Tuleme tagasi meie näite Alice juurde pagariäris. Kui ta ei oleks suutnud leida kedagi nagu Bob, kes oleks temaga oma kulutuskäigul kaasas käinud, oleks ta võinud teha Stonewalli üksi. Nii oleks kaks UTXOd teel sissepoole olnud tema omad ja ta oleks teel välja võtnud kolm.



![image](assets/fr/02.webp)




Väljastpoolt vaadatuna oleks tehing jäänud samaks.



![image](assets/fr/05.webp)



Seega peaks loogika olema järgmine, kui soovite kasutada Ashigaru kulutamisvahendit:




- Kui kaupmees ei toeta Payjoin Stowaway't, saate tänu Stonewall x2 teha ühise tehingu teise isikuga väljaspool makset;
- Kui te ei leia kedagi Stonewall x2 tehingu tegemiseks, võite teha ainult Stonewall tehingu, mis imiteerib Stonewall x2 tehingu käitumist.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Mis on Stonewall x2 tehingu mõte?



Stonewall x2 struktuur lisab tehingule tohutult entroopiat, mis segab ahela analüüsi. Väljastpoolt vaadatuna võib sellist tehingut tõlgendada kui väikest Coinjoini kahe inimese vahel. Kuid tegelikkuses on see makse. Seetõttu tekitab see meetod ahelaanalüüsis ebakindlust või viib isegi valede juhtnöörideni.



Võtame näiteks Alice, Bob ja Boulanger. Tehing plokiahelas näeks välja järgmiselt:



![image](assets/fr/03.webp)



Väline vaatleja, kes tugineb tavalisele ahelaanalüüsi heuristikale, võib ekslikult järeldada, et "*Alice ja Bob on teinud väikese ühisliidu, kusjuures üks UTXO on sisse ja kaks UTXOd on välja*".



![image](assets/fr/04.webp)



See tõlgendus on vale, sest nagu te teate, saadeti Boulangerisse UTXO, Alice-l on ainult üks vahetusväljund ja Bob-l on kaks vahetusväljundit.



![image](assets/fr/01.webp)



Isegi kui välisvaatlejal õnnestub Stonewall x2 tehingu paterne tuvastada, ei ole tal kogu teavet. Ta ei suuda kindlaks teha, milline kahest samade summade UTXOst vastab maksele. Samuti ei saa ta kindlaks teha, kas makse tegi Alice või Bob. Lõpuks ei saa ta ka kindlaks teha, kas kaks sisestatud UTXOd on pärit kahelt erinevalt inimeselt või kuuluvad nad ühele isikule, kes on need ühendanud. See viimane punkt tuleneb asjaolust, et eespool käsitletud klassikalised Stonewall-tehingud järgivad täpselt sama paterne nagu Stonewall x2-tehingud. Väljastpoolt vaadatuna ja ilma täiendava kontekstilise teabeta on võimatu eristada Stonewall-tehingut Stonewall x2-tehingust. Esimesed ei ole koostööga seotud tehingud, samas kui viimased on koostööga seotud tehingud. See lisab kulule veelgi rohkem kahtlusi.



![image](assets/fr/05.webp)




## Kuidas luua ühendus Paynymide vahel?



Nagu muud Ashigaru (*Cahoots*) ühistehingud, hõlmab ka Stonewall x2 osaliselt allkirjastatud tehingute vahetamist saatja ja koostööpartneri vahel. Seda vahetust saab teha käsitsi, kui olete füüsiliselt koos oma koostööpartneriga, või automaatselt, kasutades Sorobani kommunikatsiooniprotokolli.



Kui valite teise võimaluse, peate enne Stonewall x2 sooritamist looma ühenduse Paynymide vahel. Selleks peab teie Paynym "*jälgima*" oma koostööpartneri Paynym'i ja vastupidi. Kuidas seda teha, saate teada selle teise õpetuse algusest:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Kuidas ma teen Ashigarul Stonewall x2 tehingu?



Stonewall x2 tehingu tegemiseks klõpsake ekraani vasakus ülanurgas oleval Paynym'i pildil, seejärel avage menüü "Koostöö". Teiega koos tehingus osalev isik peab tegema sama, välja arvatud juhul, kui te vahetate QR-koode isiklikult.



![Image](assets/fr/06.webp)



Teil on kaks võimalust: valige "Algatada", kui olete makse saatja, või "Osaleda", kui olete tehingus osalev isik, kuid ei ole ei maksja ega tegelik saaja.



![Image](assets/fr/07.webp)



Kui teil on koostööpartneri roll, on menetlus väga lihtne. Sorobani võrgu kaudu tehtava kaugkoostöö puhul klõpsake nuppu `Osalemine`, valige konto, mida soovite kasutada, seejärel vajutage `OTA KAHJUTAVAID NÕUDEID`, et oodata maksja poolt saadetud taotlust.



![Image](assets/fr/08.webp)



Teisest küljest, kui soovite QR-koodi skaneerimise teel isiklikult koostööd teha, minge oma wallet avalehele, vajutage ekraani ülaosas olevale QR-koodi ikoonile ja skannige seejärel tehingu algatanud maksja antud QR-koodi.



![Image](assets/fr/09.webp)



Kui olete maksja rollis, st tehingu algatajaks, minge menüüsse "Koostöö" ja valige "Algatada".



![Image](assets/fr/10.webp)



Kuna me soovime teostada Stonewall x2, valige tehingu tüübiks see valik.



![Image](assets/fr/11.webp)



Seejärel saate valida, kas teha koostööd veebis (*Cahoots* läbi *Sorobani*) või teha koostööd silmast-silma, kasutades QR-koodi vahetamist.



![Image](assets/fr/12.webp)



### Cahoots online



Kui olete valinud võimaluse "Online", siis valige oma koostööpartner Paynymsist, mida te jälgite.



![Image](assets/fr/13.webp)



Klõpsake nupule "Tehingu seadistamine" ja valige seejärel konto, millelt soovite kulutusi teha.



![Image](assets/fr/14.webp)



Järgmisel lehel sisestage tehingu andmed: makse tegeliku saaja aadress, saadetav summa ja tasumäär. Seejärel klõpsake nuppu `Tehingu seadistamise läbivaatamine`.



![Image](assets/fr/15.webp)



Kontrollige hoolikalt teavet, veenduge, et teie koostööpartner kuulab *Cahoots* päringuid, seejärel klõpsake rohelist nuppu "BEGIN TRANSACTION", et algatada PSBT-de vahetamine Sorobani kaudu.



![Image](assets/fr/16.webp)



Oodake, kuni mõlemad osalejad on tehingu allkirjastanud, seejärel edastage see Bitcoin võrgus.



![Image](assets/fr/17.webp)



### Suhtelised arutelud



Kui soovite vahetust isiklikult teostada, valige tehingu tüüp "STONEWALL X2" ja seejärel valik "Isiklikult / käsitsi".



![Image](assets/fr/18.webp)



Klõpsake nupule "Tehingu seadistamine" ja valige seejärel konto, millelt soovite kulutusi teha.



![Image](assets/fr/19.webp)



Järgmisel lehel sisestage tehingu andmed: makse tegeliku saaja aadress, saadetav summa ja tasumäär. Seejärel klõpsake nuppu `Tehingu seadistamise läbivaatamine`.



![Image](assets/fr/20.webp)



Kontrollige üksikasju ja vajutage seejärel rohelist nuppu "ALUSTA TRANSAKTSIOON", et alustada PSBTide vahetamist QR-koodi skaneerimise teel.



![Image](assets/fr/21.webp)



Vahetamine toimub vaheldumisi skaneerimise ja koostööpartneri vahel: klõpsake nuppu `NÄITA QR-KOODI`, et näidata oma QR-koodi oma koostööpartnerile, kes skaneerib selle. Seejärel klõpsab ta `SHOW QR CODE`, et näidata oma koodi, ja teie skaneerite selle `LAUNCH QR Scanner` abil. Korrake seda protsessi, kuni kõik viis vahetusetappi on läbitud.



![Image](assets/fr/22.webp)



Kui kõik vahetused on lõpetatud, kontrollige tehingu üksikasju ja vabastage see, lohistades ekraani allosas olevat rohelist noolt.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Selle struktuur on järgmine:



![Image](assets/fr/24.webp)



*Credit: [mempool.space](https://mempool.space/)*



Me võime täheldada kahte sisendit minu portfellist, vastavalt `91,869 sats` ja `64,823 sats`, samas kui teised kaks sisendit pärinevad minu koostööpartneri wallet-st. Väljundi poolel saadetakse üks UTXO summas `100,000 sats` tegelikule makse saajale ning kaks UTXO-d summas `100,000 sats` ja `159,578 sats` naasevad minu koostööpartneri portfelli. Tema jaoks on operatsioon neutraalne, sest ta saab tagasi kogu summa, mille ta oli investeerinud sisendiks (välja arvatud mining kulud, millesse ta panustas). Lõpuks, ma saan UTXO vahetusena 56 270 sats, mis vastab minu kogu sisendi ja saajale saadetud 100 000 sats vahele.



Ilmselt võin ma seda struktuuri kirjeldada, sest ma ehitasin selle tehingu ise. Kuid välise vaatleja jaoks on üldiselt võimatu kindlaks teha, millised UTXO-d kuuluvad millisele osalejale, kas sisendites või väljundites.



Selleks, et süvendada oma teadmisi onchain privaatsuse haldamisest Bitcoin-s, soovitan teil osaleda minu BTC 204 koolitusel Plan ₿ Akadeemias :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c