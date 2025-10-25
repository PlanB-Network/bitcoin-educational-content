---
name: Alias Vault
description: Võimas tööriist paroolide, kahefaktorilise autentimise ja varjunimede haldamiseks (koos sisseehitatud e-posti serveriga) - ka ise hostitud!
---

![cover](assets/cover.webp)



Privaatsus ja turvalisus internetis on teema, millele igaüks, sõltumata tema ettevõttest, peaks pöörama suurt tähelepanu.



Need küsimused on pealegi osa pidevas segaduses olevast maailmast: üha rohkem arendajaid osaleb selles teemas, tuues rakendusi väljakujunenud lahendustele ja uutele toodetele.



See on nii **Leendert de Borst** ja tema `Alias Vault`, revolutsiooniline tööriist (esimene omataoline), mis võimaldab teil hallata ja salvestada paroole, kasutada paroolide kirjeid veebiteenuste autentimiseks, hallata kahefaktorilist autentimist, kuid mis kõige tähtsam, generate tõelisi _aliase_, kõik ühes Interface-s.



**Alias Vault ei peatu siinkohal**.



## Peamised omadused



Alias Vault töötab pilves arendaja serverites või isehostituna oma infrastruktuuris, mille jaoks on saadaval Dockeri failid ja image, mida saab paigaldada koos sciptiga. Lisaks veebi Interface-le on saadaval laiendused kõigile populaarsetele brauseritele, samuti mobiilirakendused iOSile ja Androidile; viimast saab alla laadida ka F-Droidist, möödudes ametlikust Google'i poest.



Ühes Interface Alias Vault on:




- Tasuta ja avatud lähtekoodiga**
- Password Manager**, et salvestada kõik keerulised paroolid. Brauseri laiendust kasutades täidab paroolihaldur veebisaitidele sisselogimise
- 2FA**, et toetada kahefaktorilist autentimist
- Pseudonimede haldur koos sisseehitatud e-posti serveriga**: Pigem loob see tegelikke alter-egosid koos eesnime, perekonnanime, soo, kasutajanime, parooli ja sünnipäevaga (kui see teave on nõutav).



Paketti kuulub ulatuslik ja põhjalik dokumentatsioon, mis aitab uustulnukatel seda võimsat tööriista avastada.



## Ei mingeid isikuandmeid!



See algab, nagu alati, [aliasvault.net](aliasvault.net) veebisaidilt. Nagu mainitud, saab Alias Vault'i kasutada oma serveris või arendaja pilvest, et sellega tutvuda enne isehostitavale lahendusele üleminekut.



Saidil on tõesti pilkupüüdev ja hästi hooldatud graafika, kuid hea asi tuleb siis, kui hakkate käed rüpes käima: **loo oma konto**.



![img](assets/en/01.webp)



Teie suureks üllatuseks leiate, et Alias Vault ei küsi isiklikke andmeid: kõik, mida vajate konto loomiseks, on ükskõik milline hüüdnimi, teile tuttav sõna, kui see on olemas. Nõustuge kasutustingimustega, valige sõna ja jätkake.



![img](assets/en/02.webp)



Määrake nüüd **`peaparool`**, mis on kogu teie uue süsteemi kõige tähtsam teave. Selle ühe parooliga olete tegelikult ainus, kes saab kontole juurde pääseda/taastada, sest see hoiab teie `vault` krüpteerituna serveris, mis hakkab teie andmeid majutama.



![img](assets/en/03.webp)



Fakt: Te olete loonud oma paroolihalduri ja alias-halduri, kuid ilma oma töötavat, privaatset e-posti Address andmata.



![img](assets/en/04.webp)



Alias Vault tervitab teid turvalises, uues, isiklikus, kuid samas ka tühjas ruumis. Ja nüüd hakkame seda veidi rahvastama.



Kui teil on juba olemas paroolihaldur, saate importida faili sellest, mida kasutate, et hinnata erinevusi teiste pakkujatega või ehk kõrvaldada alias-haldur, et saaksite kõike hallata ühes rakenduses.



![img](assets/en/05.webp)



Alias Vault on äärmiselt lihtne: teil on üks põhileht, mis on `Koduleht`, millel on kaks menüüd:




- `Credentials`: võimaldab luua ja hallata identiteete ja varjunimesid
- `Email`: postkast, kus saate kontrollida sissetulevaid sõnumeid teie loodud varjunimede kohta.



![img](assets/en/06.webp)



Meid huvitab just esimese `alias` loomine, seega minge lehe paremasse ülaossa ja klõpsake _+Uue Alias_.



![img](assets/en/07.webp)



Esialgu näeb menüü välja minimaalne, nagu Alias Vault'i filosoofia. Selle funktsiooni funktsioonide avastamiseks klõpsake lingil _Create via advanced mode_.



![img](assets/en/08.webp)



Esimese ekraani ülemises osas saate selle abil importida salasõnade volitusi, mida te juba kasutate teenuste puhul, millega teil on tellimus või mida te kasutate kõige sagedamini internetis.



Kui olete aktiveerinud kahefaktorilise autentimise mõnes (või kõigis) ülaltoodud teenustes, saate Alias Vaultiga hallata ka seda täiendavat Layer turvalisust, importides "salajase võtme". Alias Vault loob juurdepääsu jaoks vajaliku `TOTP`.



![img](assets/en/09.webp)



**Ohutus**: Selleks, et kasutada õiget Address, millega olete varem kontosid loonud, klõpsake _Enter custom domain_, et saaksite pärast `@` määrata õige domeeni.



![img](assets/en/14.webp)



Selle ekraani alumine osa on kõige lõbusam. Klõpsake _Generate Random Alias_ ja Alias Vault loob teile erinevate vajaduste jaoks eraldi identiteedid, millest igaühel on oma postkast, väga tugeva taseme paroolid, mida täiendavad muud andmed nagu sugu, sünnikuupäev ja sobiv hüüdnimi.



![img](assets/en/10.webp)



Rakendatavast menüüst saate muuta seadistusi, mis mõjutavad paroolide genereerimist, näiteks valida ainult väiketähed ja kõrvaldada mitmetähelised tähed.



![img](assets/en/11.webp)



Saate kasutada Alias Vault'i poolt soovitatud alias e-posti aadressi või muuta domeene, kui klõpsate vastavat rippmenüüd.



![img](assets/en/12.webp)



Enne selle e-posti kasutamist sisselogimisteenuse jaoks saate selle funktsionaalsust testida, saates oma Address-st sõnumi äsja loodud postkasti.



![img](assets/en/13.webp)



**⚠️ HOIATUS**: E-kirjade vastuvõtmine on võimalik tänu Alias Vault'i sisseehitatud serverile, kuid see võimaldab teil ainult e-kirju vastu võtta, kuid mitte vastata või kasutada e-posti kasti `alias` teenuse "tavaliste" funktsioonidega. Seega erineb see suuresti Simple Loginist, Addyst ja teistest platvormidest, mis on pühendatud ainult seda tüüpi teenusele. Simple Login'i näitel saate vaadata spetsiaalset õpetust:



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Testina loodud aliase kustutamiseks tuleb teil vaid logida sisse oma "Kodu", seejärel "Volitused" ja klõpsata identiteedil, mida soovite kustutada. Paremasse ülanurka ilmub käsk _Delete_, et saaksite jätkata.



![img](assets/en/16.webp)



## Brauseri laiendus



Sõltuvalt sellest, millised on teie vajadused, võite kasutada brauseripikendust, mis on leitav kõige levinumates brauserites.



![img](assets/en/15.webp)



See installeerub nii, nagu te juba tegite kõigi teiste laiendustega, nii et ma ei hakka selle detailiga pikemalt tegelema.



Brauseripikendus on selleks, et lihtsustada veebiteenustesse sisselogimist või vajaduse korral uute varjunimede loomist: kui teenus on salvestatud teie Alias Vault'i kirjete hulka, teeb automaatne täitmine seda, mida on vaja.



![img](assets/en/17.webp)



Ainus ettevaatus on kontrollida, et Alias Vault on aktiivne. Tegelikult on rakendusel vaikimisi seadistus, mille kohaselt see peatub pärast teatud aja möödumist. See on väga kasulik funktsioon, **kui peate näiteks oma arvutist eemale astuma, et keegi teine ei pääseks teie kontodele ligi**. Lihtsustatud protseduur võimaldab teil uuesti sisse logida, sisestades "peaparooli", kui eelmine seanss on veel vahemälus. Väljalogimise aeg on üks parameetritest, mida saate kohandada, lühendades või pikendades seda vastavalt oma eelistustele.



## Mobiilirakendus



Nagu kõik sedalaadi rakendused, on ka Alias Vaultil olemas mobiilseadmete versioon nii Androidi kui ka iOSi keskkonnas. Androidi jaoks saate rakenduse alla laadida [F-Droid](https://f-droid.org/packages/net.aliasvault.app/).



Selle artikli kirjutamise ajal (2025. aasta augusti lõpus) on mobiilirakenduse arvates "automaatne täitmine" eksperimentaalne funktsioon, mis ei tööta, välja arvatud väga vähestel saitidel. Kuni selle täieliku rakendamiseni nõuab Alias Vault'i kasutamine mobiilis andmete kopeerimist ja kleepimist.



Kui olete rakenduse poest alla laadinud, sisestate sisselogimiseks lihtsalt veebirakenduses loodud kasutaja ja "peaparooli".



![img](assets/en/18.webp)



Vault'i avamisel küsitakse, kas soovite lubada biomeetriliselt kontrollitud juurdepääsu, mis on täiendav Layer turvameede, et keegi teine ei saaks teie paroolidele ligi, kui tal juhtub olema teie telefon käes.



![img](assets/en/19.webp)



Kui otsustate biomeetrilise kontrolli sisse seada, siis tehke seda. Kui jätate selle sammu vahele ja muudate meelt, saate selle ka hiljem menüüst _Settings_ seadistada.



Kui olete sisselogimise lõpetanud, leiate juba loodud andmed uuesti sünkroniseeritud.



![img](assets/en/20.webp)



Mobiilirakendust saab suunata oma serveris asuva `vault` lingile.



![img](assets/en/22.webp)



Ja just seda isehostitud versiooni me Address lühidalt ka järgmises osas käsitleme.



## Self-Hosting: täielik kontroll oma andmete üle



Alias Vault, kui aus olla, ei ole esimene "paroolihaldur", mis võimaldab teil teenust oma infrastruktuuris kasutusele võtta. On ka teisi, kuid mõnel neist on kas piirangud või on osaliselt suletud lähtekoodiga.



Võimalus on ainulaadne: **Lõpetage sõltuvus välistest teenusepakkujatest või pilvedest, kuid kasutage omaenda kohalikku serverit, et valvata ja hallata paroole, varjunimesid ja äärmiselt tundlikku teavet, mis on sellega seotud**. Alias Vault'i abil saate lasta meiliteenusel viidata ka oma e-posti serverile, et tagada täiendav konfidentsiaalsus.



On aeg pöörduda [dokumentatsiooni](https://docs.aliasvault.net/installation/) poole, et teada saada, kuidas jätkata Alias Vault'i isehostimist.



![img](assets/en/23.webp)



Alias Vault töötab Docker Compose'il, seega on vaja minimaalset kogemust Linuxi ja Dockeriga. Võite alustada põhiinstallatsiooniga ja seejärel täiendada edasijõudnute lahendustega.



Teie server peab töötama 64-bitisel masinal, millel on Linuxi distributsioon, 1 GB RAM ja vähemalt 16 GB mälu; Dockeri (CE) versioon peab olema vähemalt 20.10 või uuem, Docker Compose'i jaoks on vaja versiooni 2.0 või uuem.



Otsustasin proovida Alias Vault'i õhukese kliendiga, millele on paigaldatud DietPi distributsioonina, Debian Bookwormi baasil, mis on optimeeritud põhiliste asjadeni ja kus juba jooksevad `Docker` ja `Docker Compose`.



Kõigepealt looge oma kodukataloogi mingi korra loomiseks kataloog, avage `terminal` ja kleepige käsk paigaldusskripti käivitamiseks.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Kui paigaldus on lõpetatud, leiate oma juurdepääsutunnused:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Kontrollige kataloogi sisu pärast paigaldamist.



![img](assets/en/29.webp)



Alias Vault käivitamiseks kasutage käsku:



"Launch-Alias-Vault"


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Krüpteerimise ja turvalisusega seotud kaalutlused



![img](assets/en/32.webp)



Vastavalt sellele, mida Lanedirt väidab veebilehel, dokumentatsioonis ja Githubis, jääb Alias Vaultiga **kõik milline teave (komponendid), mille paigutate Alias Vaulti, tihedalt seadmega seotud, krüpteeritud ja kättesaamatuks kõigile, kes ei tea "peaparooli "**.



Seega on "peaparool" kogu "võlviku" põhielement. Pärast selle sisestamist töödeldakse seda algoritmiga `Argon2id`, mis on Hard-mälu võtme tuletamise funktsioon, et takistada saladuse väljaviimist seadmest.



Kõik jääb isegi pilve- või hostinguteenuse halduri eest varjatud. Tegelikult ei pääse administraatoripaneelist ligi kasutaja andmetele, te saate teada vaid seda, kas nad on loonud aliase, saanud e-kirju ja vähe muud.



Kogu salvestatud sisu krüpteeritakse ja dekrüpteeritakse krüptograafiliste võtmetega, mis on tuletatud "peaparoolist". **Serveris salvestatakse ainult krüpteeritud andmeid, midagi ei ilmu tavatekstina**. Kui kasutaja unustab või kaotab oma "peaparooli", on sellega seotud konto pöördumatult kadunud, sest server ei pääse ligi lihtkirjas olevale sisule.



Isehostitava versiooni puhul on olemas skript, millega saab `master password` tagasi seadistada, kuid see ei takista andmete kadumist.



![img](assets/en/33.webp)



Kuna Alias Vault on _Beta_-staadiumis, võib teil olla raskusi juurdepääsuga, kui muudate/uuendate peaparooli. Soovitan valida see algusest peale robustne ja keeruline, et saaksite teenusega eksperimenteerida ja lõpuks otsustada, kas kasutada seda. Kui teil on pärast parooli uuendamist raskusi pilvele juurdepääsuga, võtke ühendust Alias Vault'i klienditoega.



Alias Vault'i arhitektuuri ja turvalisuse täielikuks mõistmiseks soovitan tungivalt tutvuda [selle lehekülje](https://docs.aliasvault.net/architecture/), mis sisaldab üksikasju selle toimimise aluseks oleva krüptograafia kohta.



## Teekaart


Arendajate eesmärk on muuta Alias Vault 2025. aasta lõpuks küpseks ja stabiilseks, et määratleda selle tulevased kasutusomadused.



Alias Vault on ja jääb alati avatud lähtekoodiga ja tasuta, kuid tõenäoliselt mitte piiramatult nagu beeta-versioonis. Mõned tasulised funktsioonid on rakendamisel, nagu on juba teatatud.



On olemas meeskonna/perekonna plaanid ja toetus riistvara võtmetele, viimane FIDO2 või WebAuthiga autentimiseks.



## Kellele on vaja Alias Vault



**Selline tööriist on ideaalne kõigile, kes seavad privaatsuse veebis esikohale**.



Teie identiteet on suure tõenäosusega teie veebipõhise äritegevuse keskmes ja seda tuleb kaitsta kõigi vahenditega, et hoida **see** andmed eemal teenustest, ettevõtetest ja vahendajatest, kes on valmis tegema kõike, et teie veebikäitumist kätte saada.



Alias Vault annab teile tagasi täieliku kontrolli oma volituste üle, vähendades või kõrvaldades täielikult vajaduse toetuda kolmandatele osapooltele teie kõige tundlikumate andmete kaitsmisel ja krüpteerimisel.



Alias Vault'i arhitektuur ja krüptograafiline võimalus on ideaalne suveräänsetele üksikisikutele, väikestele ja keskmise suurusega ettevõtetele, arendusmeeskondadele ja kõigile **ava lähtekoodiga** rakenduste entusiastidele. Kui kuulute mõnda neist kategooriatest: nautige Alias Vault'i avastamist.