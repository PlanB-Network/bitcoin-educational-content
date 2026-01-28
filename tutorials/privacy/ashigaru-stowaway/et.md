---
name: Ashigaru - Stowaway
description: Kuidas teha Payjoin tehingut Ashigaru's?
---
![cover](assets/cover.webp)



> *Sundida plokiahela spioonid ümber mõtlema kõike, mida nad arvavad teadvat.*

Payjoin on Bitcoin tehingustruktuur, mis on loodud kasutajate konfidentsiaalsuse suurendamiseks, hõlmates otsest koostööd makse saajaga. Selle rakendamise hõlbustamiseks ja protsessi automatiseerimiseks on olemas mitu rakendust. Neist tuntuim on kahtlemata Stowaway, mille algselt töötas välja Samurai Wallet meeskond ja mis on nüüdseks integreeritud fork Ashigarusse.



## Kuidas Stowaway töötab?



Nagu varem mainitud, on Ashigaru integreeritud PayJoin tööriist nimega "Stowaway". See on saadaval Ashigaru rakenduses Androidis. Payjoini teostamiseks peab saaja (kes võtab ka koostööpartneri rolli) kasutama Stowaway'ga ühilduvat tarkvara, st hetkel ainult Ashigaru.



Stowaway põhineb tehingukategoorial, mida Samurai nimetas "Cahoots". Cahoot on mitme kasutaja vaheline ühistehing, mis hõlmab teabevahetust väljaspool Bitcoin plokiahelat. Ashigaru pakub praegu kahte Cahooti vahendit: Stowaway (Payjoins) ja StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots-tehingud nõuavad osaliselt allkirjastatud tehingute vahetamist kasutajate vahel. See protsess võib olla pikk ja tüütu, eriti kui see toimub eemalt. Siiski on seda võimalik teha ka käsitsi, kui koostööpartnerid asuvad samas kohas. Konkreetselt tähendab see viie järjestikuse QR-koodi skaneerimist, mida kaks osalejat vahetavad.



Kaugemal muutub see meetod liiga keeruliseks. Selle probleemi lahendamiseks on Samourai välja töötanud Toril põhineva krüpteeritud suhtlusprotokolli nimega "*Soroban*". Tänu Sorobanile on Payjoini jaoks vajalikud andmevahetused automatiseeritud ja toimuvad taustal.



Selline krüpteeritud side nõuab Cahooti osalejate vahelist ühendust ja autentimist. Seetõttu tugineb Soroban kasutajate Paynymidele. Kui te ei ole veel kursis, kuidas Paynyms töötab, vaadake seda spetsiaalset õpetust, et rohkem teada saada:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Lühidalt öeldes on Paynym teie wallet-ga seotud unikaalne identifikaator, mis võimaldab teil aktiveerida erinevaid funktsioone, sealhulgas krüpteeritud vahetusi. See on identifikaatori kujul, millele on lisatud illustratsioon. Siin on näiteks see, mida ma kasutan Testnet puhul:



![Image](assets/fr/01.webp)



**Kokkuvõtteks:**





- payjoin" = Konkreetne ühistehingu struktuur;





- `Stowaway` = Ashigaru's saadaval olev Payjoin rakendamine;





- `Cahoots` = nimi, mille Samourai on andnud kõigile oma koostöövõimalustele, eelkõige Payjoin `Stowaway`, mis on tänapäeval Ashigarul üle võetud;





- soroban = Toril loodud krüpteeritud suhtlusprotokoll, mis võimaldab koostööd teiste kasutajatega "Cahoots" tehingus;





- paynym" = Unikaalne wallet identifikaator, mida kasutatakse teise kasutajaga "Soroban" suhtlemiseks, et teostada "Chahoots" tehingut.



Kui soovite põhjalikumalt uurida, kuidas Payjoins töötab ja nende kasulikkust onchain privaatsuses, siis soovitan seda teist õpetust:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Kuidas luua ühendus Paynymide vahel?



Alustamiseks peate muidugi installima Ashigaru ja looma :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Cahootsi kaugtehingute, sealhulgas PayJoin (*Stowaway*) sooritamiseks Ashigaru kaudu peate esmalt "jälgima" kasutajat, kellega soovite koostööd teha, kasutades tema Paynym'i. Stowaway puhul tähendab see, et te järgite isikut, kellele soovite bitcoine saata. Kui te ei tea veel, kuidas teisele Paynymile järgneda, leiate üksikasjaliku protseduuri sellest õpetusest :



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Kuidas ma teen Ashigaru's Payjoin'i?



Stowaway-tehingute tegemiseks klõpsake ekraani vasakus ülanurgas oleval Paynym'i pildil, seejärel avage menüü "Koostöö". Teiega koos tehingus osalev isik peab tegema sama, välja arvatud juhul, kui te vahetate QR-koode isiklikult.



![Image](assets/fr/02.webp)



Teil on kaks võimalust: valige "Algatada", kui olete makse saatja, või "Osaleda", kui olete makse saaja.



![Image](assets/fr/03.webp)



Kui te olete saaja, on menetlus väga lihtne. Sorobani võrgu kaudu tehtava kaugkoostöö puhul klõpsake nupule "Osalemine", valige konto, mida soovite kasutada, seejärel vajutage nuppu "OOTA KAHJUTAVAID NÕUDED", et oodata maksja poolt saadetud taotlust.



![Image](assets/fr/04.webp)



Teisest küljest, kui soovite QR-koodi skaneerimise teel isiklikult koostööd teha, minge oma wallet avalehele, vajutage ekraani ülaosas olevale QR-koodi ikoonile ja skaneerige seejärel tehingu algatanud maksja poolt antud QR-koodi.



![Image](assets/fr/05.webp)



Kui olete maksja rollis, st tehingu algatajaks, minge menüüsse "Koostöö" ja valige "Algatada".



![Image](assets/fr/06.webp)



Tehingu tüübiks, kuna soovime teha Payjoin Stowaway, valige see valik.



![Image](assets/fr/07.webp)



Seejärel saate valida, kas teha koostööd veebis (*Cahoots* läbi *Sorobani*) või teha koostööd silmast-silma, kasutades QR-koodi vahetamist.



![Image](assets/fr/08.webp)



### Cahoots online



Kui olete valinud võimaluse "Online", siis valige saaja Paynymsist, mida te jälgite.



![Image](assets/fr/09.webp)



Klõpsake nupule "Tehingu seadistamine" ja valige seejärel konto, millelt soovite kulutusi teha.



![Image](assets/fr/10.webp)



Järgmisel lehel sisestage tehingu üksikasjad: saajale saadetav summa ja tasumäär. Vastuvõtja aadressi ei ole vaja sisestada, sest vastuvõtja edastab selle ise PSBT vahetuse ajal.



Seejärel klõpsake nuppu "Tehingu seadistuste läbivaatamine".



![Image](assets/fr/11.webp)



Kontrollige hoolikalt teavet, veenduge, et teie koostööpartner kuulab *Cahoots* päringuid, seejärel klõpsake rohelist nuppu "BEGIN TRANSACTION", et algatada PSBT-de vahetamine Sorobani kaudu.



![Image](assets/fr/12.webp)



Oodake, kuni mõlemad osalejad on tehingu allkirjastanud, seejärel edastage see Bitcoin võrgus.



![Image](assets/fr/13.webp)



### Suhtelised arutelud



Kui soovite vahetust isiklikult teostada, valige tehingu tüüp "STONEWALL X2" ja seejärel valik "Isiklikult / käsitsi".



![Image](assets/fr/14.webp)



Klõpsake nupule "Tehingu seadistamine" ja valige seejärel konto, millelt soovite kulutusi teha.



![Image](assets/fr/15.webp)



Järgmisel lehel sisestage tehingu üksikasjad: saajale saadetav summa ja tasumäär. Vastuvõtja aadressi ei ole vaja sisestada, sest vastuvõtja edastab selle ise PSBT vahetuse ajal.



Seejärel klõpsake nuppu "Tehingu seadistuste läbivaatamine".



![Image](assets/fr/16.webp)



Kontrollige üksikasju ja vajutage seejärel rohelist nuppu "ALUSTA TRANSAKTSIOON", et alustada PSBTide vahetamist QR-koodi skaneerimise teel.



![Image](assets/fr/17.webp)



Vahetamine toimub vaheldumisi skaneerimise ja koostööpartneri vahel: klõpsake nuppu `NÄITA QR-KOODI`, et näidata oma QR-koodi oma koostööpartnerile, kes skaneerib selle. Seejärel klõpsab ta `SHOW QR CODE`, et näidata oma koodi, ja teie skaneerite selle `LAUNCH QR Scanner` abil. Korrake seda protsessi, kuni kõik viis vahetusetappi on läbitud.



![Image](assets/fr/18.webp)



Kui kõik vahetused on lõpetatud, kontrollige tehingu üksikasju ja vabastage see, lohistades ekraani allosas olevat rohelist noolt.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Selle struktuur on järgmine:



![Image](assets/fr/20.webp)



*Credit: [mempool.space](https://mempool.space/)*



Kui me analüüsime seda tehingut, näeme minu UTXO summas "164 211 sats" sisendi poolel, samuti UTXO summas "190 002 sats", mis kuulub makse tegelikule saajale. Väljundi poolel saan ma UTXO summas "63,995 sats", samas kui saaja saab UTXO summas "290,002 sats". Võrreldes sisendeid ja väljundeid, näeme, et saaja on tõepoolest teeninud 100 000 sats, mis vastab minu tegelikule maksele, ja et mina olen kaotanud 100 000 sats, millele olen lisanud mining kulud.



Ilmselt võin ma seda struktuuri kirjeldada, sest ma ehitasin selle tehingu ise. Kuid välise vaatleja jaoks on üldiselt võimatu kindlaks teha, millised UTXO-d kuuluvad millisele osalejale, kas sisendites või väljundites.



Selleks, et süvendada oma teadmisi onchain privaatsuse haldamise kohta Bitcoin, soovitan teil osaleda minu BTC 204 koolitusel Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c