---
name: COLDCARD - kaasallkiri
description: Avastage kaasallkirja funktsioon ja kasutage seda oma COLDCARDi puhul
---

![cover](assets/cover.webp)


*NB: See õpetus on mõeldud inimestele, kellel on juba mõningane kogemus mitme allkirjaga rahakottide, Coinkite seadmete ja tarkvaraga nagu Sparrow wallet või Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Miks ColdCard Co-Sign?



See funktsioon võimaldab teil lisada oma ColdCard (Q või Mk4) seadmele **kulutustingimused** riistvaralise turvamooduli (HSM) laadis, et kaitsta oma raha, säilitades samal ajal märkimisväärse paindlikkuse ja kontrolli selle üle.



Kulutustingimused võivad olla näiteks:





- Suuruse piirangud**: piirab bitcoinide summa, mida saad ühe tehingu jooksul kulutada.
- Kiiruse piirangud:** otsustage, kui palju tehinguid saate teha ajaühikus (tunnis, päevas, nädalas jne), nõudes nende vahel minimaalset arvu plokke.
- Eelnevalt heakskiidetud aadressid:** Luba ainult bitcoinide saatmist eelnevalt heakskiidetud aadressidele.
- Kahefaktoriline autentimine:** Nõuab kinnitust kolmanda osapoole 2FA mobiilirakendusest (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) NFC-toega nutitelefonis/tahvelarvutis, millel on internetiühendus.



**Kuidas see toimib



Lisades oma ColdCard Mk4 või Q seadmele teise seed, mida nimetatakse "kulupoliitika võtmeks" ja millele me käesolevas õpetuses viitame kui "C võtmele".


Lisaks sellele täiendavale seed-le palutakse teil Supply vähemalt üks täiendav võti (XPUB), mida me nimetame "varivõtmeks", et luua Wallet Multisig 2-on-N.



Kokkuvõttes loome Wallet Multisig ja teie ColdCard-seade sisaldab 2 raha kulutamiseks vajalikku privaatvõtit: seadme seed master ja "kulutamispoliitika võti".



Iga kord, kui "C-võtmele" palutakse allkirja anda, kohaldatakse kindlaksmääratud kulutustingimusi ja ColdCard allkirjastab ainult siis, kui tehing vastab neile.



Kui soovite neist kulutustingimustest loobuda, võite seda teha:




- allkirjastades ühe varuklahvi ja seed käega või 2 varuklahvi, sõltuvalt teie Multisig suurusest.
- sisestades menüüs "Kaasallkiri" "Kulutuskava võti" või "C võti". **Võimalusi ei saa otse seadmes vaadata, sest muidu võiks igaüks seadistatud kulutustingimusi tühistada.**




## ColdCard kaasallkirja seadistamine



![video](https://youtu.be/MjMPDUWWegw)



### 1- Aktiveeri funktsionaalsus



Kõigepealt veenduge, et teie seadmel on vähemalt uusim püsivara versioon:




- Mk4: v5.4.2
- Q: v1.3.2Q




Mine oma Mk4 või ColdCardQs valikusse *Advanced Tools > ColdCard Co-Signing* (Täiustatud tööriistad > ColdCard Co-Signing).



![Co-Sign](assets/fr/01.webp)



*Järgnevas õpetuses on mugavuse huvides tehtud ekraanipildid ColdCardQ-l, kuid sammud ja menüüd on Mk4 ja Q puhul identsed*



Kuvatakse funktsionaalsuse kokkuvõte.


Võtmete tähistamiseks kasutatav terminoloogia, mida me kasutame taas 2-on-3 mitme allkirjaga Wallet puhul, mida me peagi loome, on järgmine:



Võti A = Coldcard master seed


Võti B = varuklahv


Võti C = kulupoliitika võti



Vajutage **"ENTER "**.



![Co-Sign](assets/fr/02.webp)



Järgmine samm on otsustada, milline privaatne võti on "Kulutamispoliitika võti" või "Võti C".



Me näeme, et meil on mitmeid võimalusi:





- Või vajutage **"ENTER "**, et luua uus 12 sõnaga generate lause seed.





- Vajutage kas **"(1) "**, et importida olemasolev 12-sõnaline seed, või valige **"(2) "**, et importida olemasolev 24-sõnaline seed.





- Või vajutage **"(6) "**, et importida seed seadme võlvist.



Selle õpetuse jaoks otsustasime importida olemasoleva 12-sõnalise seed, vajutades **"(1) "**. See võib olla mis tahes seed BIP39, mis teil juba olemas on ja mille kohta teil on ilmselt varukoopia.



Kasutage oma seed 12 sõna sisestamiseks klaviatuuri. Selle näite jaoks valime seed kehtiva fraasi beef x 12. Seejärel vajutage **"ENTER "**.


*NB: kui teil ei ole selle seed varukoopiat, ei saa te enam oma seadme "Co-Sign" seadeid muuta, et muuta oma kulutustingimusi*



Seadmes on nüüd aktiveeritud funktsioon "Kaasallkiri". Järgmisena peame valima oma kulutustingimused, seejärel lõpetame mitme allkirjaga Wallet loomise.



![Co-Sign](assets/fr/03.webp)



### 2- Valige kulutustingimused või "*kulutamispoliitika*"



Siin täpsustatakse kulutamistingimused, mis peavad olema täidetud, kui **"C-võti "** või **"Kulutamispoliitika võti**" allkirjastab tehingu.



Klõpsake menüüs **"Kaasallkirjastamine "** valikut **"Kulutamispoliitika**".



Seejärel saate valida maksimaalse suuruse, st maksimaalse arvu satoshi, mida saab ühe tehinguga kulutada.



Selle näite jaoks valime maksimaalseks suuruseks **21212** satoshi. Kinnitamiseks vajutage **"ENTER "**.




![Co-Sign](assets/fr/04.webp)



Seejärel valime maksimaalse kiiruse, st tehingute arvu, mida seade suudab ajaühikus allkirjastada. Selle õpetuse jaoks valime piiramatu kiiruse, st tehingute arvu ei ole piiratud.




![Co-Sign](assets/fr/05.webp)



### 3- Loo Wallet Multisig 2-on-N



Me peame veel valima kolmanda võtme meie Wallet Multisig jaoks, st **"Backup Key "** (võti B), lisaks seadme **master seed** (võti A) ja **"Spending Policy Key "** (võti C).



Meie "B-võti" tuleb importida kas SD-kaardi kaudu või ColdCardQ puhul QR-koodi kaudu.


Selleks vajame teist ColdCard Mk4 või Q seadet, millel meie "Key B" on kasutusel.



Sellel teisel seadmel, mis sisaldab teie **"Backup Key "**, näiteks ColdCard Mk4, minge peamenüüst **"Settings "**, seejärel **"Multisig Wallet"** ja lõpuks **"Export Xpub "**.


(Kui teie teine seade on ColdCardQ, on teil muidugi võimalus eksportida oma Xpubi QR-koodi kaudu).





![Co-Sign](assets/fr/06.webp)





Järgmisel ekraanil sisestage SD-kaart ja klõpsake paremal allosas oleval nupul **"valideeri "**. Seejärel klõpsake faili salvestamiseks SD-kaardile **"(1) "**.



Faili nimes on avaliku võtme sõrmejälg (*fingerprint*) ja see on kujul `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Seejärel sisestage SD-kaart "esialgsesse" ColdCardQ-sse, et importida meie "varukoopia võti" (võti B).


Valige menüüst "ColdCard Co-Signing" "Build 2-of-N", seejärel klõpsake järgmisel ekraanil **"ENTER "**, seejärel uuesti **"ENTER "**, et importida "Backup Key" SD-kaardilt.



![Co-Sign](assets/fr/08.webp)



Järgmisel ekraanil jätke "Konto number" tühjaks (kui te ei tea täpselt, mida teete) ja vajutage uuesti **"ENTER "**.



![Co-Sign](assets/fr/09.webp)



Lõpuks oleme valmis kasutama meie uut Wallet Multisig 2-sur-3, mis koosneb järgmiselt:



Võti A= Coldcard Q master seed


Võti B = varavõttevõti (just imporditud teisest Coldcard-seadmest)


Võti C= Kulutamispoliitika võti (kui seda kasutatakse allkirjastamiseks, siis määrab eelnevalt kindlaks kulutamistingimused)



## Kaasallkiri koos Sparrow wallet-ga



Vajadusel vaadake allpool olevaid õpetusi, et tutvuda Sparrow wallet tarkvaraga:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.network/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Eksport Wallet Multisig 2-sur-3 kuni Sparrow wallet



Nüüd peame eksportima meie Wallet Multisig Sparrow-sse, et saaksime sinna paigutada oma esimesed satoshid.



Valige oma ColdCardQ peamenüüst **"Seaded "**, seejärel **"Multisig rahakotid "**.


Nüüd kuvatakse teie ColdCard'ile teadaolevate Multisig rahakottide komplekt, kus on märgitud võtmete arv "2/3" (2-sur3). Valige Multisig **"ColdCard Co-Sign "**, mille me just lõime, seejärel klõpsake **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Lõpuks valige meetod, mis võimaldab teil eksportida Wallet Sparrow-sse. Meie puhul valime SD-kaardi ja klõpsame seega **"(1) "** pärast SD-kaardi sisestamist seadme pessa A.



![Co-Sign](assets/fr/11.webp)



Seejärel valige jaotises Sparrow wallet "Import Wallet".



![Co-Sign](assets/fr/12.webp)



Seejärel klõpsake **"Import File "**. Seejärel valige SD-kaardil olev fail **"export-Coldcard_Co-sign.txt "**.



![Co-Sign](assets/fr/13.webp)



Andke oma Wallet-le nimi, nagu see ilmub Sparrow-s, ja valige Wallet krüpteerimiseks (või mitte) salasõna.



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Nüüd oleme valmis saama oma esimesed satoshid ja katsetama kulutingimusi, mida oleme Wallet suhtes kohaldanud.



![Co-Sign](assets/fr/16.webp)



### 2- Eelnevalt määratletud kulupoliitika testimine



Meeldetuletuseks: me otsustasime, et meie Wallet Multisig maksimaalne suurus on 21212 satoshi. See tähendas, et iga kord, kui kulupoliitika võti (võti C) allkirjastas tehingu, oli viimane kehtiv ainult siis, kui kulutatud summa oli väiksem või võrdne 21212 satoshi.



Katsetame seda.


Kõigepealt klõpsame Sparrow-s vahekaardil "Receive" ja laseme paar Satsi Wallet-le, mida me kasutame kogu selle õpetuse jooksul.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Proovime siis kulutada rohkem kui 21212 lubatud satoshi, simuleerides 50 000 Sats tehingut.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Pärast *allkirjastamata* tehingut kujutava QR-koodi skaneerimist meie ColdCardQ-ga, et importida tehing, kuvatakse ekraanil järgmist. Hoiatusteade ütleb meile, et kulutustingimused ei ole täidetud. Kui allkirjastame tehingu ikkagi, siis allkirjastab ainult üks 2 võtmest (seadmes olev seed master, kuid mitte "Key C").




![Co-Sign](assets/fr/23.webp)



Pärast meie tehingu importimist Sparrow-sse näeme, et tehingule on rakendatud ainult üks allkiri.



![Co-Sign](assets/fr/24.webp)




Kordame nüüd katset, kuid tehinguga 21 000 satoshi, st vähem kui maksimaalne suurus (21212 Sats), mille me selle Wallet jaoks seadsime.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Proovime seda tehingut allkirjastada meie ColdCardQ-ga.



Seekord pole probleemi, hoiatusteadet ei ilmu ja kui me impordime allkirjastatud tehingu Sparrow wallet-sse, on seekord 2 allkirja rakendatud, mistõttu tehing on kehtiv ja valmis levitamiseks.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Nunchuki kaasallkiri



https://planb.network/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA ja valges nimekirjas olevad aadressid



Selles lõigus kasutame meie Wallet Multisig Co-Sign koos Nunchukiga ja kasutame võimalust rakendada uusi kulutingimusi, et näha, kuidas see läheb.



Mine *Täiendatud tööriistad > ColdCard Co-Signing*.


Meilt palutakse sisestada meie "kulupoliitika võti", et pääseda menüüsse, mis võimaldab meil muuta kulutustingimusi. Meie puhul sisestame 12 x "veiseliha".



Me otsustasime hoida suurusjärku 21212 Sats ja maksimaalset "piirkiirust" praktilistel põhjustel, mis on seotud selle õpetusega. Teisest küljest kasutame **"Whitelist Addresses "** menüüd, et kehtestada aadressid, millele meie raha võib kulutada.




![Co-Sign](assets/fr/31.webp)




Skaneerige QR-koodid, mis on seotud aadressidega (me valime 2), mida soovite lisada oma valgelistasse, ja vajutage seejärel **"ENTER "**. Pärast aadresside valideerimist, vajutades järjestikku **"ENTER "**, näeme, et piirangud Magnitude ja soodustatud aadressidele on rakendatud.



![Co-Sign](assets/fr/32.webp)



Lõpuks, et saada täielik ülevaade "Co-Sign" pakutavatest võimalustest, aktiveerime võimaluse "Web 2FA".


See funktsioon võimaldab teil kasutada TOTP RFC-6238-konformset rakendust, näiteks Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / või Aegis Authenticator, et lisada täiendav Layer turvalisus.



https://planb.network/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.network/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Konkreetselt öeldes peate enne tehingu allkirjastamist viima oma NFC-funktsiooniga ja internetiga ühendatud seadme Coldcard'i lähedusse. See viib teid automaatselt coldcard.com veebilehele, kus teil palutakse sisestada oma taotluse 6-kohaline kood. Kui sisestate õige koodi, näitab veebileht teile kas QR-koodi, mida saate skaneerida ColdCardQ jaoks, või 8-kohalist koodi, mille peate sisestama oma Mk4-ga, et volitada seade allkirjastama.





![Co-Sign](assets/fr/33.webp)



Pärast topeltautentimisrakenduses kuvatava QR-koodi skannimist ja ColdCard Co-Sign (CCC) konto lisamist palutakse teil 2FA-koodi sisestamisega kontrollida, et kõik on korras.



Sisestage oma ColdCard oma NFC-seadme tagaküljele.



![Co-Sign](assets/fr/34.webp)



Sisestage avaneval veebilehel oma lemmikrakenduse 2FA-kood. Seejärel skaneerige oma ColdCardQ-ga kuvatavat QR-koodi (või sisestage oma Mk4-s kuvatav 8-kohaline kood).



![Co-Sign](assets/fr/35.webp)




Oleme nüüd kehtestanud piirangu suurusjärgu (21212 Sats), sihtaadresside ja kahekordse autentimise suhtes.



![Co-Sign](assets/fr/36.webp)



### 2- Ekspordi Wallet Multisig 2-on-3 Nunchukile



Ekspordime Wallet Multisig 2-on-3 seekord Nunchukisse, nagu me tegime varem Sparrow puhul.


Minge *Settings > Multisig Wallets > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Seekord valige ekspordiks NFC-variant, klõpsates ColdcardQ samanimelisel nupul **"NFC "**.



![Co-Sign](assets/fr/37.webp)



Kui avate rakenduse Nunchukis esimest korda, klõpsake **"Recover existing Wallet"**.



![Co-Sign](assets/fr/38.webp)



Kui teil on juba Wallet rakenduses, klõpsake paremal üleval **"+"**, seejärel **"Recover existing Wallet"**.



![Co-Sign](assets/fr/39.webp)




Seejärel valige **"Recover Wallet from COLDCARD "** ja seejärel **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Lõpuks koputage oma nutitelefoni tagaküljega ColdCardQ ekraanile, et importida Wallet NFC kaudu.



![Co-Sign](assets/fr/41.webp)



Meie konto ja varem Sparrow wallet kaudu hoiustatud satoshid on tagasi.



![Co-Sign](assets/fr/42.webp)



### 3- Eelnevalt määratletud kulupoliitika testimine



Proovime nüüd teha tehingu, mis rikub 2 seatud kulutustingimust. **Katsume kulutada rohkem kui 21212 Sats Address-le, mida ei ole heaks kiidetud.** Proovime saata 22 222 Sats juhuslikule Address-le.



![Co-Sign](assets/fr/43.webp)



Kui tehing on loodud, klõpsake selle eksportimiseks oma ColdCard'i 3 väikesele punktile üleval paremas nurgas.



![Co-Sign](assets/fr/44.webp)



Seejärel valige **"Export via BBQR "** ja skaneerige oma ColdCardQ-ga kuvatavat QR-koodi.



![Co-Sign](assets/fr/45.webp)



Seejärel kuvatakse ColdcardQ ekraanil hoiatus, milles selgitatakse ekraani allserva kerides, et tehing rikub ootuspäraselt kulutustingimusi.



**Märkige, et seade ei ütle meile, millised kulutustingimused on seotud, et vältida võimalikku ründajat, kes üritab piirangutest kõrvale hoida.**




![Co-Sign](assets/fr/46.webp)



Kui kinnitate ikkagi, vajutades **"ENTER "**, ilmub allkirjastatud tehingut kujutav QR-kood. Kui impordite selle Nunchukile, näete, et on rakendatud ainult üks allkiri.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Teostame täpselt sama operatsiooni, kuid seekord tehinguga, mis järgib suuruspiirangut (21212 Sats) ja kulutab satoshid ühele meie poolt eelkonfigureeritud 2 aadressist.



Me saadame Nunchuk 12121 Sats ühele meie 2 aadressist. Seejärel ekspordime tehingu meie ColdCardile, nagu eelnevalt tehtud.



![Co-Sign](assets/fr/49.webp)




Pärast allkirjastamata tehingu importimist meie ColdCardQ-sse, vaatame, mida meile seekord näidatakse.



Hoiatus on alati olemas, kuid seekord näeme ekraani alla kerides, et tegemist on tehingu kinnitamisega 2FA kaudu. Seade palub meil viia oma ColdcardQ internetiga ühendatud NFC-terminali (nutitelefoni või tahvelarvuti) lähedale, mida me ka teeme.



![Co-Sign](assets/fr/50.webp)



Meie nutitelefonis avaneb veebileht, mis palub meil sisestada oma 2FA-kood, mida me tänu Proton Authenticatorile ka teeme.



![Co-Sign](assets/fr/51.webp)





Seejärel skaneerige veebilehele ilmuvat QR-koodi, et volitada oma ColdCard tehingu allkirjastamiseks.


Tehing on nüüd kahe võtmega allkirjastatud ja seega kehtiv.



Kui teie ColdCardQ-s on aktiveeritud "Push Tx", saate tehingu otse võrku edastada lihtsa puudutusega nutitelefoni tagaküljel.



![Co-Sign](assets/fr/52.webp)




Kui teil ei ole "Push tx" aktiveeritud, vajutage ColdCardQ-l nuppu "QR", et kuvada allkirjastatud tehing QR-koodina ja importida see Nunchukisse samamoodi nagu eelmises näites.



![Co-Sign](assets/fr/53.webp)



Seekord märkame, et 2 allkirja on rakendatud, seega on tehing valmis Bitcoin võrgus edastamiseks.



![Co-Sign](assets/fr/54.webp)




Oleme jõudnud selle õpetuse lõpuni, mis annab teile ülevaate Coinkite ColdCardQ ja Mk4 seadmetesse integreeritud Co-Sign funktsionaalsuse pakutavatest võimalustest, samuti selle kasutamisest selliste rahakottide kaudu nagu Sparrow ja Nunchuk.