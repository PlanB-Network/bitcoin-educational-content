---
name: Heritage
description: Bitcoin portfell koos integreeritud pärimismehhanismiga Taproot skriptide kaudu
---

![cover](assets/cover.webp)



Bitcoinide edasiandmine surma või töövõimetuse korral on iga krüptovarade omaniku jaoks suur väljakutse. Ilma sobiva pärimiskavata muutuvad need varad teie lähedastele kättesaamatuks.



Heritage pakub elegantset vastust, rakendades otse Bitcoin plokiahelas surnud mehe vahetamise mehhanismi. See avatud lähtekoodiga wallet võimaldab konfigureerida on-chain järeltulekutingimusi: kui omanik ei tee kindlaksmääratud aja jooksul enam ühtegi tehingut, võivad eelnevalt määratud alternatiivsed võtmed raha vabastada.



## Mis on pärand?



Heritage on Bitcoin portfell, mis integreerib Taproot skriptide kaudu pärimismehhanismi. Jérémie Rodoni poolt MIT litsentsi alusel välja töötatud avatud lähtekoodiga tarkvara tagab läbipaistvuse ja kestvuse.



Heritage kasutab Taproot skripte, mis on kodeeritud Bitcoin aadressidega. Iga UTXO integreerib kahte tüüpi kulutingimusi:





- Esmane tee** : Omanik saab igal ajal oma bitcoine kulutada oma primaarse võtmega
- Alternatiivsed teed**: Iga määratud pärija puhul kombineerib skript tema avaliku võtme ja ajaluku vahel



Iga omanikutehing lükkab automaatselt edasi pärimisklauslite aktiveerimise kuupäeva. Pikaajalise tegevusetuse korral (surm, töövõimetus) käivituvad tingimused automaatselt.



## Muinsuskaitse teenus (vabatahtlik)



Heritage pakub kahte kasutusvõimalust:



**Tegi seda ise (tasuta)**: Avatud lähtekoodiga rakendus üksi. Te haldate kõike iseseisvalt oma sõlme abil. See valik pakub sisseehitatud varundust, sisseehitatud pärimist ja ainukontrolli oma bitcoinide üle. Siiski peate ise looma oma hoiatused (kalender, meeldetuletused), et te ei unustaks oma ajamäärasid uuendada, ning automaatseid teateid oma pärijatele ei ole.



**Kasutage teenust (0,05% aastas)** : Btc-heritage.com teenus lisab funktsioone, mis lihtsustavad haldamist:




- Automaatsed meeldetuletused enne tähtaegade lõppemist
- Automaatsed teated pärijatele, et juhendada neid taastamisprotsessi kaudu
- Prioriteetne toetus
- Lihtsustatud kirjeldusjuhtimine



Tasu: 0,05% hallatavast summast aastas, minimaalselt 0,5 miljonit BTC aastas. Esimene aasta tasuta.



Teenus jääb mittekaitstavaks: teie isiklikud võtmed ei lahku kunagi teie seadmest. Heritage ei pääse teie rahalistele vahenditele ligi.



## Heritage CLI



Edasijõudnud kasutajatele, kes eelistavad terminali, pakub Heritage käsurea tööriista (CLI) granuleeritud kontrolliks ja masina õhupiiretega töötamiseks.



![Page Heritage CLI](assets/fr/03.webp)



Täielik CLI dokumentatsioon on saadaval aadressil [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Siit leiate juhised allalaadimiseks, teenusega ühendamiseks, rahakottide loomiseks (Ledger või kohalike võtmetega), pärijate ja tehingute haldamiseks.



See õpetus keskendub töölauarakendusele, mis on enamikule kasutajatele kättesaadavam.



## Heritage Desktop



Heritage Desktop on intuitiivse kasutajaliidesega graafiline rakendus, mis juhatab kasutajat seadistamisprotsessi igas etapis.



### Lae alla



Mine aadressile [btc-heritage.com](https://btc-heritage.com) ja klõpsa "Download application".



![Page d'accueil Heritage](assets/fr/01.webp)



Valige oma operatsioonisüsteemile vastav versioon (Linux 64bits või Windows 64bits). Binaarsed failid ei ole digitaalselt allkirjastatud, mis võib vallandada turvahoiatusi.



![Page de téléchargement](assets/fr/02.webp)



### Paigaldamine Linuxile



Linuxis levitatakse rakendust AppImage'i vormingus. Enne selle käivitamist tuleb paigaldada sõltuvus `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Seejärel tehke fail käivitatavaks ja käivitage see:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Esimene käivitamine



Esimesel käivitamisel pakub sisseelamisviisard teile kolm valikut:



![Onboarding initial](assets/fr/05.webp)





- Seadistage Heritage Wallet**: Looge uus wallet koos pärandkultuuri plaaniga
- Pärandada bitcoinid**: Taasta bitcoins kui pärija
- Avasta ise**: Avasta funktsioone ilma abita



Valige "Setup an Heritage Wallet", et luua oma esimene wallet.



### Bitcoin võrguühendus



Valige, kuidas ühendada Bitcoin võrku:



![Choix connexion](assets/fr/06.webp)





- Päranditeenuse kasutamine**: Haldatud infrastruktuur, lihtsam pärijate jaoks
- Kasutades oma sõlme**: Ühendage oma Bitcoin Core või Electrum sõlme



Selle õpetuse jaoks kasutame oma sõlme.



### Privaatvõtmete haldamine



Valige, kuidas hallata oma isiklikke võtmeid:



![Gestion des clés](assets/fr/07.webp)





- Ledger riistvaraseadmega** : Maksimaalne ohutus wallet riistvaraga (soovitatav)
- Kohalik salvestusruum koos parooliga**: Kohalikult salvestatud võtmed koos parooliga
- Olemasoleva wallet taastamine** : Taastamine olemasolevast seed-st



### Sõlme konfiguratsioon



Kui kasutate oma sõlme, juhendab rakendus teid selle konfigureerimisel. Veenduge, et teie Bitcoin või Electrum sõlm on :




- Paigaldatud ja töötab
- Sünkroonitud Bitcoin võrguga
- Konfigureeritud RPC ühenduste vastuvõtmiseks (Bitcoin Core jaoks)



![Configuration nœud](assets/fr/08.webp)



Kui teie sõlmpunkt on valmis, klõpsake nuppu "Minu Bitcoin sõlmpunkt on käivitatud ja töötab".



### Staatus paneel



Klõpsake üleval paremas nurgas oleval nupul "Status" ja seejärel "Open Configuration", et pääseda juurde ühenduse parameetritele.



![Panneau Status](assets/fr/09.webp)



Määra oma Electrum serveri URL (nt `umbrel.local:50001`, kui kasutad Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### wallet loomine



Kui ühendus on loodud, klõpsake WALLETSi vahekaardil "Create Wallet" (Loo Wallet).



![Créer wallet](assets/fr/11.webp)



Avakuva selgitab Heritage'i jagatud arhitektuuri:



![Architecture split](assets/fr/12.webp)



1. **Key Provider (Offline)**: Haldab teie isiklikke võtmeid ja allkirjastab tehinguid. Võib olla Ledger või wallet tarkvara.


2. **Online Wallet**: Käsitleb sünkroniseerimist Bitcoin võrguga, aadresside loomist ja tehingute edastamist.



Täitke loomevorm :



![Formulaire création wallet](assets/fr/13.webp)





- Wallet nimi**: Unikaalne nimi teie wallet identifitseerimiseks
- Võtmepakkuja**: Valige selle õpetuse jaoks kohalik võtmehoidla
- Uus/taastatud**: Valige "Uus", et luua uus generate seed
- Sõnade arv**: 24 sõna soovitatav maksimaalse turvalisuse tagamiseks



Sisestage tugev salasõna ja valige Online Wallet valikud:



![Options Online Wallet](assets/fr/14.webp)





- Kohalik sõlm**: Kasutab oma Electrum või Bitcoin tuumasõlme
- Muinsuskaitse**: Kasutab Heritage teenust (soovitatav teavitamisfunktsioonide jaoks)



Klõpsake "Create Wallet", et lõpetada loomine.



### Interface alates wallet



Teie wallet on nüüd loodud. Kasutajaliideses kuvatakse :



![Interface wallet](assets/fr/15.webp)





- Saldo
- SEND ja RECEIVE nupud
- Tehingute ajalugu
- Pärandkonfiguratsiooni ajalugu
- wallet aadressid



### Pärijate loomine



Pärijate loomiseks minge vahekaardile "PÄRISTE".



![Page Heirs](assets/fr/16.webp)



Teabe hüpikaken selgitab:




- Pärandajad on Bitcoin avalikud võtmed, mis on seotud üksikisikutega
- Igal pärijal on oma mnemooniline fraas
- Esimene pärija peaks olema "varukoopia" enda jaoks (juhul, kui teie peamine wallet peaks kaduma)



#### Varukoopia pärija loomine



Klõpsake nupule "Create Heir" ja nimetage see "Backup".



![Création héritier Backup](assets/fr/17.webp)



Pikakuva selgitab, miks 12-sõnaline lause ilma passphrase on pärijatele ohutu:


1. **Kohene juurdepääs puudub**: Pärija võtmed ei saa juurdepääsu rahalistele vahenditele enne, kui ajalukk on lõppenud


2. **Kompromissi tuvastamine**: Kui keegi pääseb fraasile ligi, saate uuendada pärandi konfiguratsiooni


3. **Pikaajaline kättesaadavus**: passphrase võib aastate pärast ununeda



Seadistage pärija :



![Configuration héritier](assets/fr/18.webp)





- Peamine teenusepakkuja** : Kohaliku võtme säilitamine
- Uus**: Uue seed genereerimine
- Sõnade arv**: 12 sõna



Lõpetage loomine :



![Finalisation héritier](assets/fr/19.webp)





- Pärija tüüp**: Laiendatud avalik võti
- Ekspordi teenusesse**: Valikuline, võimaldab automaatset teavitamist pärijatele



Nüüd on loodud varukoopia pärija:



![Héritier créé](assets/fr/20.webp)



#### Pärija mälusõna salvestamine



Klõpsake varukoopia pärale ja seejärel "Näita Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**TÄHELEPANU: märkige need 12 sõna üles ja hoidke neid turvalises kohas. See on raha tagasisaamise võti.



![Phrase mnémotechnique](assets/fr/22.webp)



#### seed eemaldamine taotlusest



Kui olete fraasi üles kirjutanud, avage pärimusparameetrid (hammasratta ikoon):



![Paramètres héritier](assets/fr/23.webp)



Kasutage "Strip Heir Seed", et eemaldada privaatne võti rakendusest. Kinnitage, et olete fraasi salvestanud.



![Strip Heir Seed](assets/fr/24.webp)



See on turvameede: rakendusse jääb ainult avalik võti, millest piisab pärimise konfigureerimiseks.



#### Teise pärija loomine



Korrake protsessi, et luua teine pärija (nt "Satoshi"). Nüüd on teil kaks pärijat:



![Deux héritiers](assets/fr/25.webp)





- Varukoopia**: Teie isiklik hädaolukorra võti
- Satoshi**: Määratud pärija



### Pärandkonfiguratsioon



Pöörduge tagasi oma wallet juurde ja klõpsake seadete ikoonil:



![Paramètres wallet](assets/fr/26.webp)



Klõpsake jaotises "Heritage Configuration" (pärandi konfiguratsioon) nupule "Create" (luua):



![Heritage Configuration](assets/fr/27.webp)



Seadke igale pärijale ajalised piirangud:



![Configuration délais](assets/fr/28.webp)





- Varukoopia**: 180 päeva (6 kuud) - Lõpptähtaeg: 2026-06-18
- Satoshi**: 455 päeva (15 kuud) - Lõpptähtaeg: 2027-03-20



**Tähtis**: Iga pärija peab olema pikema viivitusega kui eelmine. Esimene pärija (varukoopia) saab esimesena juurdepääsu rahalistele vahenditele.



Samuti konfigureerida :



![Configuration finale](assets/fr/29.webp)





- Vaatluskuupäev**: Läbiviimise aja arvutamise alguskuupäev
- Minimaalne tähtajaline viivitus**: Minimaalne viivitus pärast tehingu sooritamist (soovitatav 10 päeva)



Klõpsake konfiguratsiooni kinnitamiseks nuppu "Create".



Nüüd on pärandi konfiguratsioon aktiivne:



![Configuration active](assets/fr/30.webp)



See kuvab mõlemad pärijad koos nende vastavate tähtaegade ja aegumiskuupäevadega.



### Deskriptorite salvestamine



**Tähtis**: Salvestage oma wallet kirjeldused. Ilma nendeta, isegi mnemoonilise fraasi abil, on fondide taastamine võimatu.



Klõpsake nuppu "Backup Descriptors" :



![Bouton Backup](assets/fr/31.webp)



Salvestage JSON-fail, mis sisaldab teie Bitcoin kirjeldusi:



![Backup descripteurs](assets/fr/32.webp)



See fail tuleks pärandada teie pärijatele koos vastavate mnemooniliste fraasidega.



### Bitcoinide vastuvõtmine



Klõpsake "RECEIVE", et generate vastuvõtu aadressi saada:



![Recevoir bitcoins](assets/fr/33.webp)



Palju õnne! Teie Heritage Wallet on valmis bitcoinide vastuvõtmiseks. Iga genereeritud aadress sisaldab automaatselt teie Heritage'i tingimusi.



Pärast tehingu saamist uuendatakse teie saldot:



![Solde mis à jour](assets/fr/34.webp)



Ajalugu kuvab tehingu ja sellega seotud pärandvara konfiguratsiooni.



---

## Pärandaja tagasisaamine



Kui määratud aeg on möödunud, võib pärija raha tagasi nõuda.



### Eeltingimused



Pärija vajab :


1. Tema 12-sõnaline mnemooniline lause


2. wallet originaalkirjelduse varukoopiafail (JSON)



### Pärandaja loomine Wallet



Vahekaardil "PÄRIMUSED" tuletab hüpikaken teile neid eeldusi meelde:



![Page Heir Wallets](assets/fr/35.webp)



**Pöörake tähelepanu**: Ilma deskriptori varifailita on juurdepääs fondidele võimatu, isegi õige mnemoonilise fraasi abil.



Klõpsake nuppu "Loo pärija Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Palun täitke vorm:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Pärandaja Wallet nimi**: Nimi selle pärija identifitseerimiseks wallet
- Peamine teenusepakkuja** : Kohaliku võtme säilitamine
- Taastada**: Valige see valik, et sisestada olemasolev fraas



Sisestage 12 sõna pärandaja mnemofraasi ja seadistage pärandaja teenusepakkuja:



![Entrée mnemonic](assets/fr/38.webp)





- Pärandihoidja**: "Kohalik", et kasutada oma sõlme koos varundusfailiga



Laadige JSON varukoopiafail ja klõpsake nuppu "Create Heir Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface pärija Wallet



Luuakse pärija Wallet. Esialgu, kui ajalukk ei ole veel lõppenud, ei ole pärimine võimalik:



![Pas d'héritage disponible](assets/fr/40.webp)



Kui viivitus on möödunud ja vahendid on Bitcoin võrguga sünkroniseeritud, ilmuvad need pärandite loetellu:



![Héritage disponible](assets/fr/41.webp)



Kasutajaliides kuvab :




- Võtme tüüp ja sõrmejälg
- Pärandatavad vahendid kokku
- Praegune kulutatav summa (0 istus, kui ajapiirang ei ole veel lõppenud)
- Tähtaeg ja aegumiskuupäevad



Kui lunastustähtaeg on saabunud, kantakse bitcoinid nupu "Spend" abil üle isiklikule wallet-le.



---

## Parimad tavad



### Deskriptorite salvestamine



wallet kirjeldused on olulised teie pärandiaadresside rekonstrueerimiseks. ** Ilma deskriptoriteta ei suuda te isegi oma mnemoonilise fraasi abil oma vahendeid üles leida.



### Võtmeturvalisus





- Võimaluse korral kasutage Ledger põhivõti jaoks
- Ärge kunagi hoidke pärijate lauseid samas kohas, kus teie enda oma
- Levitada teavet mitmel meediumil ja mitmes kohas



### Dokumentatsioon teie lähedastele



Kirjutage selged juhised, mis selgitavad iga taastamisprotsessi sammu. Teie pärijad ei pruugi kriitilisel hetkel Bitcoin tundma õppida.



## Alternatiivid



Teie bitcoinide edastamise haldamiseks on olemas ka muid lahendusi, sealhulgas Liana ja Bitcoin Keeper. Allpool leiate meie õpetused:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Kokkuvõte



Heritage võimaldab teil planeerida oma Bitcoin pärandit suveräänselt töölauarakenduse kaudu. Rakendamine nõuab läbimõeldud kaalumist sobiva ajakava ja saladuste tagamise osas. Ärge unustage oma pärijatele edasi anda:




- Nende 12-sõnaline mnemooniline fraas
- Deskriptori varundusfail
- Taastamisjuhised



## Ressursid





- [Heritage ametlik kodulehekülg](https://btc-heritage.com)
- [Dokumentatsioon CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)