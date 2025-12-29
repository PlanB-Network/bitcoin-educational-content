---
name: Bitcoin Keeper - Pärimisplaan
description: Planeeri oma bitcoini edastamine koos Bitcoin Keeper-ga
---

![cover](assets/cover.webp)



Bitcoin varade üleandmine on üks valdajate poolt enim alahinnatud väljakutseid. Erinevalt pangakontost, kus finantsasutus saab raha õigustatud pärijatele edasi anda, tugineb Bitcoin täielikult isiklike võtmete omamisele. Täiesti seaduslik pärija ei pääse ilma nende võtmeteta kunagi ligi rahalistele vahenditele, samas kui pahatahtlik isik, kes valdab saladusi, saab neid ilma igasuguse formaalsuseta kulutada.



Selles teises Bitcoin Keeper õpetuses uurime pärandi planeerimisele pühendatud lisafunktsioone. Rakendus pakub täiustatud tööriistu täiustatud võlvade loomiseks, millel on tänu Miniscript'ile ajastatud kaitsemehhanismid, ning kaasnevaid dokumente, et juhendada oma lähedasi.



See juhend eeldab, et olete juba omandanud Bitcoin Keeper põhitõed (portfelli loomine, klassikaline multisig, riistvaraliste võtmete lisamine), nagu on selgitatud meie esimeses õpetuses :



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-22cbfb8d-790f-4a6f-a92f-93a117e1e65c

![video](https://youtu.be/tCld_-n2d30)



## Bitcoin Keeper tellimusplaanid



Bitcoin Keeper töötab freemium-mudelil, millel on kolm liitumistasandit, mis pakuvad järkjärgulist funktsionaalsust. Plaanidele juurdepääsuks minge vahekaardile **More**, seejärel koputage oma praegusele plaanile (vaikimisi on "Pleb"), et avada ekraan **Manage Subscription**.



![Plans d'abonnement](assets/fr/01.webp)



**Pleb-plaan** (tasuta) pakub juurdepääsu põhitõdedele: piiramatu ühe ja mitme võtmega rahakottide loomine, ühilduvus kõigi suuremate riistvaraliste rahakottidega (Coldcard, Trezor, Ledger, Jade, Tapsigner...), müntide kontroll, märgistamine ja ühendus isikliku Electrum serveriga. See kava on piisav tavakasutamiseks ja isegi klassikaliste multi-sig konfiguratsioonide jaoks.



**Hodleri pakett** (9,99 €/kuu, aastas tasudes 1 kuu tasuta) sisaldab kõiki Plebi funktsioone ja lisab krüpteeritud varukoopiaid pilve (iCloud või Google Drive), et taastada oma seifid mis tahes seadmes, Server Key, et lisada automaatsed kulupoliitikad ja 2FA üle teatud künnise, ning Canary Wallets, et tuvastada volitamata juurdepääsu teie võtmetele.



**Diamantkäte plaan** (29,99 €/kuu, 1 kuu tasuta, kui tasub aastas) on täielik pakett pärandi planeerimiseks. See sisaldab kogu Hodleri plaani ja avab pärimisvõtme (edasilükatud aktiveerimine), hädaolukorra võtme (hädaolukorra võtme taastamiseks kaotsimineku korral), pärandi planeerimise vahendid ja dokumendid ning tugikõne Concierge-meeskonnaga teie konfiguratsiooni kinnitamiseks. See on pakkumine bitcoin'idele, kes soovivad oma pärandit edasi anda mitme põlvkonna jooksul.



Tähtis punkt: loodud hoidlad jäävad ligipääsetavaks ka siis, kui vahetate tagasi tasuta paketi vastu. Teie seadistused põhinevad avatud standarditel (BSMS, Miniscript) ja toimivad teie tellimusest sõltumatult.



## Pärimisdokumendid



Kui olete aktiveerinud oma Diamond Hands'i tellimuse, avage jaotis **Pärimisdokumendid** vahekaardil "Rohkem". Bitcoin Keeper pakub viis näidisdokumenti oma pärandvara plaani struktureerimiseks, samuti nõuannete osa:



![Documents d'héritage](assets/fr/02.webp)





- Seed Words Template**: mall oma taastumisfraaside korrastatud märkmete korrastamiseks
- Usaldusväärsed kontaktid**: mall teie plaaniga seotud usaldusisikute (notar, advokaat, pärijad, võtmevahendid) kontaktandmete loetlemiseks
- Täiendav jagamisvõti**: dokument, mis sisaldab üksikasjalikku tehnilist teavet iga võtme kohta: PIN-kood, tuletamise tee, füüsiline asukoht, seadme tüüp ja mis tahes muu teave, mis on kasulik võtme tuvastamiseks ja kasutamiseks
- Tagasinõudmisjuhised**: samm-sammult juhised pärijale või abisaajale vahendite tagasinõudmiseks
- Kiri advokaadile**: eeltäidetud kiri, mida saab kohandada oma advokaadi või notari jaoks



Rubriik **Pärimisnipid** pakub praktilisi nõuandeid pärijatele võtmete kindlustamiseks ja pärimisplaani optimeerimiseks.



Kohandage need dokumendid vastavalt oma olukorrale ja hoidke neid turvalises kohas, eraldi võtmetest.



## Cloud Backup'i konfigureerimine



Enne pärandvaramu loomist aktiveerige pilves varundamine, et kaitsta oma konfiguratsioonifaile. Vajutage vahekaardil Veel, vajutage **Personal Cloud Backup**.



![Configuration Cloud Backup](assets/fr/03.webp)



Valige varukoopiate krüpteerimiseks tugev parool. See parool kaitseb ainult wallet konfiguratsioonifaile (mitte teie isiklikke võtmeid). Kinnitage parool ja vajutage **Kinnita**. Teie varukoopiad salvestatakse sõltuvalt seadmest iCloudi või Google Drive'ile. Vajutage **Backup Now**, et käivitada esimene varukoopia.



## Importige oma riistvara võtmed



Meie näite jaoks loome 2-ast-3 seifi, millel on kaks täiendavat võtit (Inheritance ja Emergency). Alustame kõigi vajalike võtmete importimisega vahekaardile **Keys**.



![Import des clés hardware](assets/fr/04.webp)



Vajutage klahvi **lisamine**, seejärel valige riistvara wallet ühendamiseks **Lisake klahv riistvaralt**. Bitcoin Keeper toetab paljusid seadmeid: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner ja Specter Solutions.



Meie konfiguratsioonis impordime :




- 2 **Kaardiklahvi** (MK4SP ja MK4)
- 2 klahvi **Tapsigner** (Metro ja Genesis)



Coldcard'i lisamiseks valige see nimekirjast ja järgige ekraanil kuvatavaid juhiseid, et eksportida avalik võti QR-koodi, faili, USB või NFC kaudu. Lisateavet Coldcard'i või Tapsigner kasutamise kohta leiate meie spetsiaalsetest juhendmaterjalidest:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Kui kõik teie võtmed on imporditud, leiate need võtmete vahekaardilt võtmed koos nende kohandatud nimedega.



## Luua pärand wallet



Liigume edasi pagasiruumi loomise juurde. Vajutage vahekaardil **Pangad**, vajutage **Add Wallet**, valige **Bitcoin Wallet** ja seejärel **Loo Wallet**.



![Création du wallet](assets/fr/05.webp)



Valige wallet tüüp. Valige meie pärandkava puhul **2 3-st mitme võtmega**. Aktiveerige ekraani allosas **Enhanced Security Options** ja vajutage seejärel **Proceed**.



![Options de sécurité avancées](assets/fr/06.webp)



Täiustatud turvavalikute hüpikaknas märkige :




- Pärimisvõti**: lisavõti, mis lisatakse kvoorumisse kindlaksmääratud aja möödudes
- Avarii võti**: võti, millel on edasilükatud täielik kontroll, et taastada raha võtme kaotamise korral



Vajutage **Muudatuste salvestamine**. Seejärel valige imporditud klahvidest (nt Seed Key, Coldcard MK4SP ja Tapsigner Metro) 3 klahvi, mis moodustavad teie wallet.



## Spetsiaalsete võtmetähtaegade määramine



Järgmisel ekraanil saate konfigureerida hädaolukorra võtme ja pärimisvõtme. Siin saate määrata nende erivõtmete aktiveerimist reguleerivad viivitused.



![Configuration des délais](assets/fr/07.webp)



Valige **Erakorralise võtme** jaoks riistvaraline võti, mis on lõplikuks varukoopiaks (siin Coldcard MK4), ja valige aktiveerimise viivitus (meie näites: 2 aastat). Erinevalt Inheritance Key'st ei lisa Emergency Key kvoorumit: see võimaldab teil **üleslülitada multisig** täielikult ja annab teile täieliku kontrolli rahaliste vahendite üle pärast tähtaja möödumist. See on teie viimane lahendus: kui mitu võtit on kadunud või hävinud, võimaldab see üks võti taastada kõik. Seetõttu tuleb seda kaitsta ülima rangusega.



**Pärimisvõtme** puhul valige pärijale mõeldud võti (siinkohal Coldcard MK4SP) ja valige viivitus (meie näites: 1 aasta). Pärast ühe aasta möödumist ilma liikumiseta lisatakse see võti **allkirja kvoorumisse**. Praktiliselt muutub teie wallet 2-of-3 pärast selle aja möödumist wallet 2-of-4-ks, mis võimaldab pärijal osaleda allkirjastamises koos olemasolevate võtmetega.



### Kuidas toimivad ajamärgid?



Bitcoin Keeper kasutab **absoluutseid ajalukkusid** (CLTV - CheckLockTimeVerify), mille on võimaldanud Miniscript. Erinevalt suhtelistest ajalukkudest (CSV), mis algavad iga UTXO saamisel, töötavad absoluutsed ajalukud **määratud aegumiskuupäevaga**, mis on määratletud wallet loomisel.



Konkreetselt öeldes, kui te loote wallet täna 1-aastase pärimisvõtmega, on aktiveerimise kuupäev "täna + 1 aasta". Kõik sellesse wallet-i hoiustatud vahendid, olenemata nende hoiustamise kuupäevast, on pärimisvõtme kaudu kättesaadavad samal kuupäeval.



Absoluutsete ajatelgede eelis on see, et need võimaldavad üle 15 kuu pikkuseid tähtaegu (suhteliste CSV ajatelgede piir), mis selgitab, miks Bitcoin Keeper võib pakkuda selliseid võimalusi nagu 2 aastat.



### Värskendusmehhanism



Selleks, et vältida erivõtmete aktiveerimist teie eluajal, peate te oma wallet regulaarselt "värskendama". Absoluutsete ajalukkude puhul tähendab see, et **luuete wallet uue aegumiskuupäevaga**, mis on lükatud tulevikku, ja kannate seejärel oma vahendid sellele uuele wallet-le üle.



Bitcoin Keeper lihtsustab seda protsessi integreeritud värskendusfunktsiooniga. Rakendus tegeleb keerukusega automaatselt taustal: te lihtsalt järgite juhendatud samme, ilma et peaksite ise käsitsi uut wallet looma või raha üle kandma. Planeerige seda toimingut regulaarselt, aegsasti enne seadistatud lühima aja möödumist. Näiteks 1-aastase pärimisvõtme puhul värskendage iga 9-10 kuu tagant, et säilitada kindlusvaru.



## Konfigureerimise salvestamine ja eksportimine



Kui wallet on loodud, tuletab rakendus teile meelde, et peate konfiguratsioonifaili salvestama. **See samm on kriitilise tähtsusega**: ilma selle failita ei saa teie pärijad wallet multisegi uuesti luua.



![Export de la configuration](assets/fr/08.webp)



Vajutage **Backup Wallet Recovery File**. Saadaval on mitu ekspordivõimalust:




- PDF-eksport**: genereerib täieliku dokumendi koos kogu wallet teabega
- Näita QR**: kuvab QR-koodi konfiguratsiooni importimiseks teise seadmesse
- Airdrop / File Export**: ekspordib faili jagamisvõimaluste kaudu
- NFC**: jagamine NFC kaudu ühilduva seadmega



Tehke mitu koopiat: üks notari juures, üks panga seifis, üks krüpteeritud digitaalne versioon. Teie uus wallet ilmub nüüd rahakoti vahekaardil siltidega "Multi-key", "2 of 3", "Inheritance key" ja "Emergency key".



## Loo Wallet kanaari



Kanaari Wallet on varajase hoiatamise süsteem. Idee: iga võtit, mida kasutatakse wallet mitme võtmega, saab kasutada ka eraldi wallet ühe võtmega. Selle wallet "kanaari" väikese summa hoiulepanekuga annab igasugune omavoliline liikumine märku võtme kompromissist.



![Canary Wallets](assets/fr/09.webp)



Wallet Canary saab konfigureerida kahel viisil. Vajutage vahekaardil **More** jaotises "Keys and Wallets" (võtmed ja rahakotid) nuppu **Canary Wallets**. Ekraanil selgitatakse põhimõtet: kui keegi pääseb ligi ühele teie võtmetele ja leiab sellega seotud wallet ühe võtme raha, siis üritab ta seda eemaldada, mis annab teile märku.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Saate kanaari konfigureerida ka otse võtmelt. Valige vahekaardil **Keys** klahv (nt Tapsigner Genesis), vajutage ikooni **Settings** (hammasratas) ja seejärel **Canary Wallet**. Sellega seotud kanari wallet avaneb, olles valmis võtma vastu mõned seiresatšid.



Hoiustage väike summa (mõned tuhanded satoshi) igale Kanaari Wallet-le. Kui need vahendid liiguvad ilma teie nõusolekuta, eemaldage kohe kompromiteeritud võti oma multisig-seifidest.



## Parimad tavad



**Testige oma konfiguratsiooni** väikese rahasummaga, enne kui panete sinna suure summa. Saatke mõned tuhanded satoshid võlvkappi, seejärel proovige väljaminevat kulutust, et kontrollida, kas olete iga seadmega allkirjastamise protsessi omandanud. Testige ka konfiguratsioonifaili importimist teise telefoni, et veenduda, et varukoopia töötab.



**Jagage võtmeid arukalt**. Tapsignerite puhul andke need üle pitseeritud ümbrikus, kusjuures PIN-kood on eraldi edastatud (nt mujal säilitatavas taastamisjuhendi kirjas). Klassikaliste riistvaraliste rahakottide puhul hoidke seadet usaldusväärse kolmanda isiku juures ja seed paberil või metallil teie või mõne muu kolmanda isiku juures. Märkige iga võtme sõrmejälg ja selle nimi konfiguratsioonifaili, et vältida segadust.



**Planeerige perioodilisi teste** (tuletõrjeharjutused). Kontrollige igal aastal, et saate seifi varukoopiate põhjal tühja telefoni uuesti üles ehitada. Testige Canary hoiatusi, kontrollides saldosid. Simuleerige kaotusstsenaariume ("mis siis, kui ma kaotan Coldcard'i?"), et kinnitada, et allesjäänud võtmekombinatsioonid on piisavad.



**Ära unusta värskendust**. Kui olete seadnud oma pärimisvõtme 1 aastaks, värskendage ennast iga 9-10 kuu järel. See on hind, mida maksate automaatse edastamise eest ilma kolmanda osapoole sekkumiseta.



**Hoidke kava ajakohasena**. Kõik muudatused (võtme asendamine, pärijate muutmine, tähtaja muutmine) peavad kajastuma kõigis varukoopiates ja dokumentides. Genereerige PDF-dokumendid pärast iga muudatust uuesti ja levitage uued versioonid.



## Piirid ja kaalutlused



Hoolimata nende vahendite võimsusest on oluline tunnustada nende piiranguid, et neid võimalikult tõhusalt hallata.



Ajamärkidega multisignaalse seifi **komplekssus** võib olla iseenesest ohtlik: valesti konfigureerimine, pärijate poolne vääritimõistmine, kriitilise elemendi kadumine paljude komponentide hulgast. Bitcoin Keeper lihtsustab kogemust nii palju kui võimalik, kuid see jääb siiski tehniliseks operatsiooniks. Võtke see plaan kasutusele ainult siis, kui kaitstav summa seda õigustab. Väikeste summade puhul võib piisata ka lihtsamast plaanist.



**rakendussõltuvuse** üle tasub mõelda. Kuigi kood on avatud lähtekoodiga ja põhineb avatud standarditel (Miniscript, BSMS), sõltuvad teatud funktsioonid Keeperi ökosüsteemist. Hoidke rakenduse koopiat (Android APK või iOS IPA) ja dokumenteerige oma kirjades pärijatele võimalus kasutada rahaliste vahendite taastamiseks teisi Miniscriptiga ühilduvaid rahakotte (nt Liana).



Usaldusväärsed maaklerid** kujutavad endast inimriski. Mis juhtub, kui mõni pahatahtlik sugulane kasutab talle usaldatud võtit enne tähtaega? Või kui advokaat paneb teie dokumendid valesti? Valige need inimesed hoolikalt, selgitage nende vastutust selgelt ja teil peab olema plaan B. Kanaari rahakotid, üleliigsed varukoopiad ja multisigade struktuur ise on teie parim kaitse nende ohtude eest.



## Kokkuvõte



Bitcoin Keeper pakub oma Diamond Hands-kavaga täielikku tööriistakasti pärandi planeerimiseks: Täiustatud võlvrid koos ajastatud võtmetega, kaasnevad dokumendid, kanaari rahakotid ja personaalne tugi.



See on rohkem kui lihtsalt tehniline küsimus: küsimus on teie kinnisvara arhitektuuri kavandamises, võtmete ja teadmiste arukas jaotamises ning süsteemi korrapärases testimises. Hästi kavandatud Bitcoin pärimisplaan muudab teie satoshid reaalseks, ülekantavaks pärandiks.