---
name: Zeus Embedded
description: Kuidas kasutada Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS on esialgu mobiilirakendus välgumihkete kaugjuhtimiseks, mis võimaldab teil juhtida oma kaugserverisse paigaldatud sõlme


Kuid rakenduses on ka "Embedded node".



**Es on see rakenduse tahk, mida me selles õpetuses uurime.** See võimaldab igaühel omada oma välgussõlme mobiilis, ilma et oleks vaja spetsiaalset serverit, samamoodi nagu ACINQ pakub oma uskumatut Wallet välgussõlme Phoenix.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Tuletame meelde, et Lightning on võrk, mis töötab paralleelselt Bitcoin-ga, võimaldades bitcoinide vahetamist ilma On-Chain tehinguid süstemaatiliselt sooritamata. Tulemuseks on peaaegu kohesed tehingud, ilma et oleks vaja oodata 10 minutit ploki kinnitamist. See on eriti kasulik, kui maksta kaupmehe eest füüsilises maailmas. Veelgi enam, Lightning pakub märkimisväärset **konfidentsiaalsuse taset**, mida Bitcoin võrk ei oma*.



**Zeus "Integreeritud "** on suunatud Bitcoiners, kes soovivad maksimeerida oma privaatsust ja autonoomiat.


Ühesõnaga, see on **potentsiaalselt** Wallet mobiiltelefoni cypherpunks unistuste. Isegi kui see on veel lapsekingades (alfaversioon) ja selle puhul on veel mõned vead, on selle funktsioone palju ja pole kahtlustki, et see rõõmustab kõige kartmatumaid meist, kes tahavad maksimaalset kontrolli ja valikuvõimalusi.



Teisest küljest ei usu ma, et see on praegu sobiv algajatele, kes ei tunne Bitcoin ja tahavad lihtsalt lihtsat viisi satoshide saatmiseks/vastuvõtmiseks. Kuigi see võib tulevikus muutuda, kuna Cashu (chaumian Ecash) protokolli kaudu on algajatele mõeldud custody funktsioon kasutusel...



## Installige rakendus



Minge [projekti veebisait](https://zeusln.com/), et laadida alla rakendus oma nutitelefoni operatsioonisüsteemi jaoks:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Portfelli loomine



Kui rakendus on käivitunud, klõpsake nupule "Quick Start", et alustada Wallet loomist.



![image](assets/fr/03.webp)





Seejärel ilmub rida initsialiseerimisekraane. Oodake mõned hetked, seejärel oodake paar minutit, kuni sõlme on Neutrino kaudu 100% sünkroonitud.



See võib võtta paar minutit. Informatsiooniks neutrino on viis, kuidas mobiilsed rahakotid pääsevad ligi Blockchain Bitcoin teabele, ilma et oleks vaja käivitada Full node.



![image](assets/fr/04.webp)





Mõne hetke pärast olete valmis minema.



![image](assets/fr/05.webp)




## Rakenduse seadistamine



Valmis, noh, mitte päris, sest on ütlematagi selge, et selle nime vääriline Zeuse kasutaja navigeerib oma Wallet klassiliselt ja stiilselt. Nii et me peame tema avatari muutma.



Klõpsake oma avataril ekraani paremas ülanurgas:



![image](assets/fr/06.webp)





Klõpsake hammasratta ja seejärel pluss "+" :



![image](assets/fr/07.webp)





Valige kõige ilusam foto Zeusest, mis esindab seda Wallet, ja klõpsake ekraani allosas "VÄLJA PILTUUR", seejärel minge tagasi, klõpsates üleval paremal asuval noolega.



![image](assets/fr/08.webp)





Lõpuks andke oma Wallet-le hüüdnimi ja klõpsake "SAVE Wallet CONFIG", et muudatus jõustuks. Lõpuks klõpsake vasakus ülanurgas oleval tagasiminekunoolil, et naasta avakuvale.



![image](assets/fr/09.webp)





Seekord saame tõesti alustada.



![image](assets/fr/10.webp)



### Biomeetria



Wallet-le juurdepääsu kaitsmiseks saate lisada PIN-koodi/parooli ja aktiveerida biomeetria.



Selleks minge Wallet peamenüüsse, klõpsates vasakul üleval horisontaalsetel kriipsudel.



![image](assets/fr/11.webp)





Valige "Seaded", seejärel "Turvalisus" ja lõpuks "PIN-koodi määramine/muutmine".



![image](assets/fr/12.webp)





Looge oma PIN-kood, kinnitage see ja aktiveerige biomeetria, vajutades vastavat nuppu "Biomeetria".  Pöörduge tagasi peamenüüsse, kasutades vasakus ülaosas asuvat noolt.



![image](assets/fr/13.webp)




### Salvesta Mnemonic fraas



Kui oled tagasi peamenüüs, klõpsa "Back up Wallet", seejärel loe hoiatusteksti, mis teavitab sind, et 24 sõna kaotamine, mida sa kohe saad, tähendab juurdepääsu kaotamist sinu rahalistele vahenditele ja et igaüks, kellel on need sõnad lisaks sulle, saab ligipääsu sinu rahalistele vahenditele. Ärge kunagi andke neid kellelegi.



Valige ekraani allosas "I UNDERSTAND". Seejärel klõpsake iga 24 sõnale, et need esile tuua, ja märkige need hoolikalt üles.



Võite selle kirjutada paberile või ehk täiendava turvalisuse tagamiseks graveerida selle roostevabast terasest, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest. Teie Mnemonic kandja valik sõltub teie turvastrateegiast, kuid kui kasutate Zeust mõõdukaid summasid sisaldava kuluportfellina, peaks paberist piisama.



Lisateavet selle kohta, kuidas oma Mnemonic fraasi õigesti salvestada ja hallata, soovitan kindlasti jälgida seda teist õpetust, eriti kui olete algaja:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Kui olete lõpetanud, klõpsake ekraani allosas nuppu "I'VE BACKUP MY 24 WORDS" ja oleme tagasi avalehel, valmis oma esimesi bitcoine vastu võtma.




## Võimalus 1 - saada On-Chain bitcoin'e ja avada Lightning-kanal



**Zeus Embedded** on mõeldud eelkõige sisseehitatud välgussõlmena, kuid seda saab kasutada ka Wallet On-Chain-na.



On-Chain bitcoinide vastuvõtmiseks klõpsake nupul "On-Chain" ja seejärel nupul "Saada".


Lõpuks skaneerige QR-koodi või kopeerige Bitcoin Address, et raha sisse maksta.



![image](assets/fr/15.webp)





Kui raha on kinnitatud ja teie Wallet-le krediteeritud, saate seda kasutada **Valguskanali** avamiseks. Teie Lightning-kanal on teie värav Lightning Network-le, mis võimaldab teil Exchange bitcoin'id palju konfidentsiaalsemalt ja kiiremini kätte saada.





- Selleks klõpsake nuppu "LIIKUMINE On-Chain FUNDS TO LIGHTNING"



Järgmisel ekraanil palutakse teil avada kanal koostöös **"Olympus by Zeus "**, Wallet poolt eelistatud LSP-ga (Lightning Service Provider).


Selles õpetuses valime lihtsuse huvides selle võimaluse, kuid on täiesti võimalik avada kanaleid mis tahes võrgusõlme kaudu.


On isegi võimalik avada mitu kanalit ühe tehinguga, valides "OPEN ADDITIONAL CHANNEL" (LISAKANALI AVAMINE). *Aga seda vaatame **Zeus Embedded** õpetuse "edasijõudnute" versioonis.*





- Seejärel valige summa, mille soovite sellele kanalile eraldada. Meie puhul kasutatakse kõik meie On-Chain vahendid, seega aktiveerime nupu "Kasuta kõiki võimalikke vahendeid".





- Lõpuks valige ekraani allosas olev nupp "OPEN CHANNEL".



![image](assets/fr/16.webp)





Mõne sekundiga on kanal loodud ja me oleme valmis tegema oma esimesi Lightning-tehinguid. Avakuval näeme meie Wallet saldo kõrval väikest kella. See tuleneb sellest, et peame veel ootama 3 On-Chain kinnitust, enne kui kanal on tõeliselt toimiv.



![image](assets/fr/17.webp)





Pärast 3 kinnitust märkame, et meie saldo on nüüd krediteeritud välklambile.



![image](assets/fr/18.webp)



Üks väike detail: kui me klõpsame ekraani allosas olevas menüüs, et vaadata meie välgukanalite seisu, näeme, et väike osa meie saldost ei ole kulutamiseks saadaval: me saame kulutada ainult 208253 satoshi selle 210370 asemel, mis meil tegelikult on. See on normaalne, sest see on välkprotokollile omane.



Lõpetuseks tuleb märkida, et meie partner Olympus jätab endale õiguse sulgeda kanal oma äranägemise järgi, kui seda näiteks ei kasutata. Selleks, et tagada meie kanali säilimine, peame maksma LSP-le (Lightning Service Provider), nagu näeme järgmises lõigus, kanali avamise 2. viisi kaudu.





## Bitcoinide saatmine Lightning'i kaudu



Nüüd, kui me oleme saanud oma kanali üles ja tööle, vaatame, kuidas me saame seda kasutada, et maksta Invoice (Invoice) välk.



Selleks klõpsake nupule "Välk" ja seejärel nupule "Saada".



![image](assets/fr/19.webp)





Järgmisel ekraanil kopeerige oma Invoice selleks ettenähtud väljale või skannige see, klõpsates üleval paremal asuval ikoonil. Lõpuks libistage maksmiseks nuppu "Slide to Pay" paremale.



![image](assets/fr/20.webp)






Oodake paar sekundit ja Invoice on tasutud ning teie satoshid on liikunud valguse kiirusega.



![image](assets/fr/21.webp)





Zeus võimaldab teil seejärel lisada märkuse oma makse tähistamiseks või vaadata marsruuti, mille teie satoshid läbisid enne sihtkohta jõudmist (ja kõigi vahepealsete sõlmpunktide poolt kogutud tasusid). See on just selline funktsionaalsus, mis meile Wallet puhul meeldib.



![image](assets/fr/22.webp)



Pange tähele, et erinevalt Wallet-st nagu [Phoenix]([Plan ₿ Academy - Phoenix](https://planb.academy/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), arvutatakse Zeuse puhul marsruut kohalikult ja seda ei delegeerita kolmandale osapoolele (Phoenixi puhul ACINQ). Seega olete ainus, kes teab makse saajat. Me kaotame veidi tõhusust (maksete tegemine võtab veidi kauem aega, kuid me võidame palju privaatsuse osas).





Kui klõpsate koduekraani allosas oleval väikesel noolega, saate vaadata ka meie makseajalugu. Siin näeme Green-s 212,121 Sats, mis saime On-Chain eest, siis punasega vastavalt 211,756 Sats, mida kasutasime meie kanali avamiseks, siis 121,212 satoshi, mida kasutasime Invoice välguse eest maksmiseks.



![image](assets/fr/23.webp)





## Võimalus 2 - bitcoinide vastuvõtmine otse Lightningi kaudu



Selle asemel, et avada kanal käsitsi, nagu me just nägime, on võimalik saada raha otse Lightning'i kaudu, isegi ilma eelnevalt olemasoleva kanalita, kasutades Olympus, Zeus LSP-d.




- Selleks klõpsake avakuval nupule "Välk" ja seejärel nupule "Vastuvõtmine".
- Seejärel valige summa, mida soovite saada, lahtrisse "Summa" ja valige ekraani allosas olev nupp "LOOMA Invoice".



![image](assets/fr/24.webp)





Järgmisel ekraanil kuvatakse Invoice, mida tuleb maksta, et saada satoshi. Meile öeldakse, et LSP peab kinni 10 000 Sats, kui makse tehakse välguga. Hiljem näeme, kuidas need kanali avamise tasud on õigustatud.



Makske Invoice või laske kellelgi teisel maksta, ja kanal avatakse automaatselt, kuid sellest lahutatakse 10 000 Sats, nagu kokku lepitud.



![image](assets/fr/25.webp)





Oleme nüüd 2 välgukanali eesotsas, mille staatust saab kontrollida, kui klõpsata nupule, mida tähistab valge nool ekraani allosas.



Me näeme, et erinevalt meie On-Chain skaala kaudu avatud kanalist ei näita see, mis avatakse otse välgu kaudu, mingit hoiatust.


Kuna olete selle kanali loomise eest maksnud, kohustub välkteenuse pakkuja (Lightning Service Provider, LSP) hoidma kanalit 3 kuud ja pakub teile "sissetulevat likviidsust". Alumisel kanalil näete, et vastuvõtuvõimsus on 96383 satoshi. LSP on seega sidunud kapitali, et võimaldada teil saada makseid vahetult pärast kanali avamist.



Seega 10 000 Satoshi makstud tasud katavad: kanali avamise kulud (Bitcoin On-Chain tehing, garantii kanali hooldamiseks 3 kuu jooksul ja kapitali lukustamine).



![image](assets/fr/26.webp)





Palju õnne, olete nüüd valmis kasutama Zeus Embedded'i, Wallet mobiilse valgustussüsteemi, millel on kõige arenenumad funktsioonid turul.





Kui soovite rohkem teada saada Lightning Network tehnilise toimimise kohta, leiate Fanis Michalakise suurepärase tasuta Plan ₿ Academy koolituse:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb