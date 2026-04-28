---
name: Wallet of Satoshi - Iseseisev hoidmine
description: Uurige, kuidas konfigureerida Wallet of Satoshi portfelli isehoidmisrežiimi
---

![cover](assets/cover.webp)



***Ne sinu võtmed, mitte sinu mündid* on rohkem kui ütlus, see on Bitcoin põhiprintsiip, mis tähendab, et kui sa ei kontrolli **privaatvõtmeid**, mis su bitcoinid lahti lukustavad, siis sa tegelikult ei oma neid ka.



Paljud kasutajad alustavad tavaliselt **sõltumatu wallet**-ga, seejärel lähevad üle **sõltumatule wallet-le**, kus nad kontrollivad oma isiklikke võtmeid ise.


Selles õppematerjalis ei tutvusta me teile uut enesekohustuslikku wallet. Selle asemel tutvustame teile ***Wallet of Satoshi*** wallet uut funktsiooni: **iseseisev režiim**.



Selle uue integratsiooni eesmärk on võimaldada kasutajatel säilitada kontroll oma isiklike võtmete üle, kasutades samal ajal lihtsust ja sujuvat kasutajakogemust.



Enne kui me jõuame asja tuumani, võtame hetkeks aega, et uurida Wallet of Satoshi (WoS) poolt pakutavat erilist isehooldusrežiimi.



## Omavalvurežiimi eripära



WoSi isehalduse režiimi lihtsus ja sujuvus välistab Lightning-kanalite avamise, sõlmede haldamise keerukuse... Aga kuidas see võimalik on?



Wallet of Satoshi enesekontrollirežiimi toidab **Spark**. See on Layer 2 lahendus Bitcoin jaoks, mille on loonud Lightspark, kasutades **statechains** tehnoloogiat.



Selle tulemusena ei tee te oma tehinguid otse Lightning Network-l. LN** võrgu ja **Spark** vaheline suhtlus toimub **atomaarsete vahetuste** kaudu.



Näiteks soovib Bob tasuda Lightning-arve WoSi abil. Ta edastab oma satoshi, kuid taustal suunatakse need Sparki **Sparki teenusepakkujale (SSP)**, kes omakorda teostab makse Lightning-võrgus.



Alice soovib seevastu saada vahendeid otse oma WoSi portfellist. Sellisel juhul saab **SSP** sats LN kaudu sats ja krediteerib kohe Alice portfelli.



Seega on oluline märkida, et WoSi lihtsusest ja sujuvusest kasu saamiseks peate sõltuma Sparki serveritest. Turvalisuse mõttes on teil aga, kui SSP muutub pahatahtlikuks või kättesaamatuks, olemas **ükspoolse väljumise** mehhanism, turvameede, mis võimaldab teil taastada oma vahendid Bitcoin on-chain (isegi kui see võib olla aeglane ja kulukas) , mis tagab erasektori Lightning-sõlmega võrreldava enesekindluse.



Kõiki neid parameetreid arvesse võttes saate seejärel otsustada, kui palju sats te soovite oma WoSi isehoidmises hoida.



Kui olete Wallet of Satoshi uus kasutaja, peate loomulikult alla laadima wallet mobiilirakenduse. Kui te aga juba kasutate seda ja soovite teada, kuidas kasutada **Iseseisva hoidmise režiimi**, siis minge otse selle õpetuse jaotise **Iseseisva hoidmise režiimi seadistamine** juurde.



## Wallet of Satoshi kasutamise alustamine



Mine oma rakenduste poodi ja lae alla WoS.



![screen](assets/fr/03.webp)



Avage rakendus pärast allalaadimist ja vajutage **Start**.



![screen](assets/fr/04.webp)



Teid suunatakse ümber rakenduse põhiliidesesse. Tegelikult on WoSi esmakordsel kasutamisel portfell juba toimiv ja avaneb vaikimisi süstemaatiliselt hoolduse režiimis.



![screen](assets/fr/05.webp)



Isegi kui te ei soovi WoSi kasutada hoolduse režiimis, soovitame selle esmalt konfigureerida. Selleks vaadake seda õpetust.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Liigume edasi meie WoSi konfiguratsiooni juurde isehoidmises.



## Omavahetusrežiimi konfiguratsioon



Klõpsake põhiliidese paremas ülemises nurgas oleval hamburgeri menüüs (3-riba ikoon).



![screen](assets/fr/06.webp)



Seejärel klõpsake ilmuvas menüüs allmenüüs **Open Self Custody Wallet**.



![screen](assets/fr/07.webp)



WoS ütleb sulle kohe, et *iseseisvumisrežiimiga kaasneb taastumisfraas. Samuti oled sa ainuisikuliselt vastutav oma rahaliste vahendite turvalisuse eest*.



![screen](assets/fr/08.webp)



Märkige nuppu "**Mina saan aru**" (1), seejärel vajutage nuppu **Open Self Custody Wallet** (2), mis kuvatakse helekollase värviga.



![screen](assets/fr/09.webp)



### Iseseisva portfelli loomine



Pärast klõpsamist nupul **Open Self Custody Wallet**, klõpsake nupul **Create a New Wallet**.



![screen](assets/fr/10.webp)



WoS loob seejärel teie jaoks isehooldusportfelli, jällegi samas rakenduses. Teil on võimalik igal ajal ja igal ajal ümber lülituda **hooldus** režiimi (saadaval teatud piirkondades) ja **isehooldus** režiimi vahel.



![screen](assets/fr/11.webp)



Kui see on loodud, suunatakse teid edasi WoSi peamisesse iseteenindusliidesesse. Te märkate, et WoSi hoidmisportfelli ja WoSi iseteenindusportfelli üldülevaate ja liideste vahel ei ole erinevusi.



### Mnemoonilise fraasi salvestamine



Puudutage ekraani ülaosas Wallet of Satoshi nime ja hamburgerimenüü vahel asuvat ikooni **Keychain + Backup Wallet**.



![screen](assets/fr/12.webp)



WoS pakub kahte erinevat võimalust oma 12 sõna (mnemooniline fraas) salvestamiseks: **varundamine Google Drive'i kaudu** ja **manuaalne varundamine**.



Kuigi soovitame teha varukoopia käsitsi, mis on kõige turvalisem, näitame ka, kuidas varundada Google Drive'i kaudu.



#### Varundamine Google Drive'i kaudu



Vajutage nupule **Google Drive Backup**.



![screen](assets/fr/13.webp)



Kui valite Google Drive'i varundamise, on suur oht, et teie Google'i konto satub ohtu. Pahatahtlik isik saaks juurdepääsu teie 12 sõna sisaldavale failile ja saaks seega juurdepääsu teie wallet-le.



Parooli lisamine, et krüpteerida oma 12 sõna sisaldav fail, on kindlasti hea viis lisaturvalisuse lisamiseks.



Aktiveerige seega täiustatud valikutes nupp **Krüpteeri parooliga**.



![screen](assets/fr/14.webp)



Määrake uues ilmuvas liideses tugev parool ja kinnitage see uuesti.



![screen](assets/fr/15.webp)



Oluline on meeles pidada, et kui olete valinud parooli, ei tohi te seda unustada ega kaotada andmekandjat, millele olete selle kirjutanud. Kui unustate või kaotate selle, ei pääse te enam kunagi ligi oma 12 sõnale ja seega ka oma rahalistele vahenditele.



Pärast parooli valimist valige Google'i konto varundamiseks, seejärel andke WoSi poolt nõutavad juurdepääsud.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Oodake paar sekundit. Bingo! Teie varundamine on edukalt lõpetatud.



![screen](assets/fr/18.webp)



Teil on alati võimalus teha täiendav varundus, valides teise varundusmeetodi: manuaalne varundus.


#### Käsitsi varundamine



Kui valite käsitsi varundamise, soovitame tungivalt tutvuda selle õpetusega, milles uuritakse parimaid tavasid oma mnemofraasi turvaliseks varundamiseks, et te ei kaotaks juurdepääsu oma bitcoinidele.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Vajutage nuppu **Manuaalne varundamine**.



![screen](assets/fr/19.webp)



Järgneval kasutajaliidesel tuletab WoS teile meelde mõningaid ettevaatusabinõusid, mida tuleb enne käsitsi varundamise alustamist arvesse võtta.



Aktiveerige nupp **Mina saan aru** ja vajutage nuppu **Järgmine**.



![screen](assets/fr/20.webp)



Seejärel esitatakse teile 12 sõna. Salvestage need, seejärel klõpsake nupule **Järgmine**.



![screen](assets/fr/21.webp)



Sellel uuel kasutajaliidesel vajutage sõnu õiges järjekorras.



![screen](assets/fr/22.webp)



Lõpuks klõpsake nupule **Järgmine**. Palju õnne! Teie varundamine on nüüd lõpule viidud.



![screen](assets/fr/23.webp)



## Iseseisev portfelli taastamine



Kui soovite taastada või taastada oma WoS-i isehaldatava wallet pärast telefoni vahetust või muul põhjusel, on järgmised sammud.



WoSi portfelli avamiseks klõpsake põhiliidese paremas ülemises nurgas oleval hamburgeri menüüs.


Ilmuvas menüüs klõpsake alammenüüs **Avadus Wallet**.


Vajutage uues ilmuvas liideses nuppu **Restore Existing Wallet**.



![screen](assets/fr/24.webp)



Valige taastamismeetod ja jätkake järgmise sammuga.



![screen](assets/fr/25.webp)



### Taastamine Google Drive'i kaudu



1. Vajutage nuppu **Restore From Google Drive**.


2. Valige Google'i konto ja laske WoSil Google Drive'ile salvestatud taastamisandmed kätte saada.


3. Seejärel sisestage oma krüpteerimisparool (kui olete selle muidugi eelnevalt kindlaks määranud) failist, mis sisaldab teie 12 sõna.


4. Oodake mõne hetke, kuni taastamine jõustub, ja te saate oma portfellile uuesti juurdepääsu.



### Käsitsi taastamine



1. Vajutage nuppu **Restore Manually**.


2. Seejärel sisestage oma mnemoonilise fraasi 12 sõna, kirjutades iga sõna oma alguse numbri ette.


3. Oodake mõne hetke, kuni taastamine jõustub, ja te saate oma portfellile uuesti juurdepääsu.




### Bitcoinide ülekandmine WoSi hoiustamise ja WoSi isehoidmise vahel



Kui teil on bitcoinid (sats) oma WoSi hoiul wallet ja loote WoSi enda hoiul wallet, siis te ei kaota oma raha. Veelgi parem on see, et saate need üle kanda oma isehaldatavasse portfelli ja vastupidi.



Selleks :


Saate kopeerida oma välk WoSi iseteeninduse aadressi või enda loodud arve.



![screen](assets/fr/26.webp)



Nüüd avage oma hoidja wallet ja vajutage nuppu **Envoyer**.



Seejärel kleepige aadress või arve. Vajutage teist korda **Envoyer**.



Minge tagasi oma isehoidmisportfelli ja te näete, et te tõepoolest saite raha kätte.



![screen](assets/fr/27.webp)



## Bitcoinide saatmine ja vastuvõtmine



Mis puutub bitcoinide saatmisse ja vastuvõtmisse isehoidmisrežiimis, siis nagu ka üldine ülevaade ja liidesed, ei erine need bitcoinide saatmisest ja vastuvõtmisest WoS custody wallet kaudu.



Palun lugege Wallet of Satoshi kasutamise põhiõpetust Plan₿ võrgus.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Nüüd saate Wallet of Satoshi-i ise konfigureerida ja kasutada isehooldusrežiimis.



Kui leidsid selle õpetuse kasulikuks, palun jäta mulle allpool roheline pöial. Tänan teid väga!