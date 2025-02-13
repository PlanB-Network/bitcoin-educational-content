---
name: Liana
description: Rahakoti seadistamine ja kasutamine Liana's
---
![cover](assets/cover.webp)

Selles õpetuses selgitame samm-sammult, kuidas Liana rakendust arvutis kasutada. Muuhulgas saate teada, kuidas luua automatiseeritud päringukava, saada ja saata bitcoin'e tavalistes olukordades ning saada raha olemasolevast portfellist teatud aja möödudes tagasi.

Jaanuaris 2025 olid Liana'ga ühilduvad riistvaralised rahakotid: Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.

Kui soovite olemasolevast Liana rahakotist raha tagasi saada, lugege allpool olevat esitlust ja minge otse jaotisse "Bitcoinide tagasisaamine".

## Liana tarkvara tutvustamine

Liana on avatud lähtekoodiga tarkvarapakett, mis on mõeldud täiustatud portfellide loomiseks ja haldamiseks, eelkõige osana automatiseeritud pärimissüsteemist või jõulisest varundusmehhanismist. Projekti on alates 2022. aastast arendanud Wizardsardine, mis on Kévin Loaeci ja Antoine Poinsot' asutatud ettevõte. Ametlikul veebisaidil esitatakse Liana kui "lihtne portfoolio isiklikuks kureerimiseks koos taastamis- ja pärimisfunktsioonidega". Tarkvara töötab arvutites -- Linux, MacOS, Windows -- ja selle (avatud) lähtekood on kättesaadav [GitHubis](https://github.com/wizardsardine/liana).

Liana tugineb Bitcoini programmeeritavusele, et luua täiustatud rahakott. Eelkõige kasutab see ära ajalukustusi (*timelocks*), mis võimaldavad raha kulutada alles pärast teatud aja möödumist ja mis on seotud Bitcoini taastamisega. Liana rahakott koosneb seega mitmest kulutamisviisist:


- Peamine kulutuste tee, mis on alati kättesaadav;
- Vähemalt üks taastamisrada, mis muutub kättesaadavaks teatud aja möödudes.

Allpool olev skeem illustreerib kahe kulureaga portfelli toimimist:

![Schéma explicatif](assets/fr/01.webp)

See toiming võimaldab seadistada erinevaid konfiguratsioone, sealhulgas :


- Pärimis- (või pärimis-) plaan, mis võimaldab pärijatel kasutaja surma korral raha tagasi saada. Lisateavet selle teema kohta soovitame lugeda [4. osa] (https://planb.network/courses/btc102/233c88d3-2e8e-5eba-ac06-efe67a209038) kursusest BTC102.
- Tugevdatud varukoopia koos taastamisajaga, mis annab kasutajale võimaluse kasutada oma rahakotti, ilma et ta peaks hoidma vastavat salajast lauset ja riskima selle vargusega, näiteks sissemurdmise ajal.
- Turvavõrk inimestele, kes alustavad Bitcoiniga: nad haldavad oma rahakotti ise ja nende "eestkostja" (näiteks sugulane) jätab endale õiguse oma raha teatud aja möödudes tagasi saada.
- Mitme osapoolega allkirjastamise skeem (*multisig*), mille nõuded vähenevad aja jooksul, et tulla toime ühe või mitme osaleja, näiteks ettevõtte partnerite kadumisega.

Liana suur tugevus seisneb selles, et sellega võetakse kasutusele standardiseeritud viis, kuidas tagada vahendite tagasinõudmine jooksvateks kuludeks kasutatava põhivõtme kaotamise korral. See kujutab endast suurt uuendust vahendite puhta hoidmise jaoks, mis on täis riske, eriti kui te ei ole selles valdkonnas hästi informeeritud. Liana võib seega julgustada isegi kõige riskikartlikumaid kasutajaid lõpetama oma vahendite hoidmise eest vastutava depositooriumi (näiteks vahetusplatvormi) kasutamise ja taastama oma raha omandiõiguse, mis on kooskõlas Bitcoini cypherpunk'i eetosega.

Loomulikult on Liana'l ka omad puudused. Esimene neist on see, et peate oma rahakotti regulaarselt uuendama, tehes tehingu Bitcoini plokiahelas. See võib olla tüütu (sõltuvalt sellest, kui tihti te tarkvara kasutate) ja kulukas (sõltuvalt tasude tasemest sel ajal), kuid see on hind, mida te maksate lisaturvalisuse eest.

Teine negatiivne punkt võib olla konfidentsiaalsus. Kui te kaasate teise isiku konfiguratsiooni, saab ta teada kõik teie aadressid ja võib seega teie tegevust jälgida. See ei ole aga probleemiks, kui valite tugevdatud varukoopia või pärimiskava, mille puhul teie pärija ei saa portfelli üksikasjadest kohe teada.

## Ettevalmistus

Selles õppematerjalis koostame järeltuleku plaani. Me kasutame :


- Ledger Nano S Plus, igapäevaste kulutuste jaoks;

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- Blockstream Jade, mida kasutatakse rahaliste vahendite tagasisaamiseks;

https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- Kaks andmekandjat (USB-pulgad) portfoolio kirjelduse salvestamiseks;
- Pärimiskiri, mis sisaldab juhiseid rahaliste vahendite sissenõudmiseks;
- Nummerdatud pitseeritud kott, mis tagab, et taaskasutusvahendit (Jade) ei ole kasutatud.

## Paigaldamine ja konfigureerimine

Külastage ametlikku Wizardsardine'i veebisaiti ja laadige Liana alla aadressil https://wizardsardine.com/liana/. Võite alla laadida ka uusima versiooni [GitHubi repositooriumist](https://github.com/wizardsardine/liana/releases), kus saate kontrollida tarkvara autentsust. Selles õpetuses kasutatav versioon on 0.9.

![Télécharger Liana](assets/fr/02.webp)

Selleks, et teada saada, kuidas käsitsi kontrollida tarkvara autentsust ja terviklikkust enne installimist, soovitame tutvuda selle õpetusega :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Paigaldage tarkvara oma masinasse ja käivitage see. Valige oma rahakoti konfigureerimiseks valik "*Loo uus Liana rahakott*".

![Accueil Liana](assets/fr/03.webp)

Valige oma portfelli tüüp. Kui soovite luua täiustatud varukoopia koos taastamisajaga, võite valida "*Koosta oma*" ja valida vaikimisi skeemi. See töötab peaaegu samamoodi, välja arvatud see, et te ei pea säilitama riistvara rahakoti taastamise lauset.

Me ignoreerime siinkohal *Suurendav multisig*, mis loob keerulisema konfiguratsiooni.

Selle õpetuse jaoks kasutame lihtsat pärimist.

![Choisir type de portefeuille](assets/fr/04.webp)

Järgneb kiire selgitus.

![Rapide explication](assets/fr/05.webp)

Kui olete selgituse läbi lugenud, saate oma Liana rahakoti võtmed seadistada. See on oluline samm, sest see määrab teie konto kulutamisomadused.

![Configurer clés](assets/fr/06.webp)

Kõigepealt saate menüüs "Täpsemad seaded" otsustada "kirjelduse tüübi", st viisi, kuidas leping ahelasse kirjutatakse. Saate valida kahe tüübi vahel: P2WSH (SegWit) või Taproot. Mõlemal juhul on kulutingimuste semantika sama. Kui P2WSH muudab lepingu lihtsamini arusaadavaks, siis Taproot on parem, sest see peidab kasutamata tingimused ja säästab kulusid väljavõtete hankimisel.

See valik on vabatahtlik: kui kahtled, jäta vaikimisi valik (versiooni 0.9 puhul P2WSH, kuid see võib muutuda).

![Choisir le type de descripteur](assets/fr/07.webp)

Järgmisena konfigureerige oma esmane võti (*primaarne võti*). Seda võtit (või õigemini seda võtmekogumit) kasutatakse vahendite jooksvate kulutuste jaoks, mille suhtes ei kehti mingid ajastamise tingimused. Vajutades nupule "*Set*", saate valida vastava *allkirjastamise seadme*. Meie puhul oleme valinud Ledger Nano S Plus riistvaralise rahakoti.

Lubage seadme laiendatud avaliku võtme jagamine. Andke sellele võtmele tähendusrikas nimi (antud juhul "Nano S+"). Pange tähele, et kõik seadmesse paigaldatud rakendused jätkavad normaalset toimimist.

![Configurer clé principale](assets/fr/08.webp)

Seejärel määrake tagasimakseviivitus, st aeg, mille möödudes saab raha kulutada *pärimisvõtme* abil. See viivitus määratakse plokkidena, kusjuures iga ploki vahel on keskmiselt 10 minutit. See võib ulatuda 10 minutist (1 plokk) kuni umbes 15 kuuni (65,535 plokki). See ülemine piir on Bitcoini protokolli piirang, kuna lukustusaja on kodeeritud 16 bitti.

Kui ei ole erilisi asjaolusid, valige pikim tarneaeg: 15 kuud või 65,535 plokki. See aitab teil kulusid kokku hoida. Soovitame siiski teostada uuendamise protseduuri (mida on kirjeldatud jaotises "Portfelli uuendamine") kord aastas, alati samal aastaajal, et "ritualiseerida" seda praktikat ja vältida unustamist.

Siinkohal oleme määranud testide läbiviimiseks ühe tunni (6 plokki) taastumisaja.

![Configurer temps de verrouillage](assets/fr/09.webp)

Lõpuks seadistage oma pärandvara võti. Seda võtit (või õigemini võtmekomplekti) kasutatakse teie kadumise korral rahaliste vahendite tagasisaamiseks. Klõpsake nupule "*Set*", valige allkirjastamise seade ja kinnitage sellel laiendatud avaliku võtme jagamine.

Selle õpetuse jaoks valisime Jade'i. Andke võtmele kõnekas nimi (siin "Jade"). Nagu ka esimese seadme puhul, toimivad tavapärased kontod edasi.

![Configurer clé de succession](assets/fr/10.webp)

Kui kõik need toimingud on lõpetatud, kontrollige, et kõik on korras, ja klõpsake "*Jätka*", et oma valikuid kinnitada.

![Confirmer clés](assets/fr/11.webp)

Järgmine samm on portfelli kirjelduse salvestamine. See on teave, mida vajate oma kontol olevate vahendite leidmiseks. Vastupidiselt mnemoonilisele fraasile ei võimalda deskriptor teil raha kulutada, seega tekitab selle avalikustamine ainult konfidentsiaalsusprobleemi (isik teab kõiki teie tehinguid).

Salvestage kaks koopiat kirjeldusest elektroonilisel andmekandjal, näiteks USB-pulgal. Trükkige kindlasti ka kaks koopiat paberil välja, et elektroonilise andmekandja kahjustumise korral oleks teil võimalik neile ligi pääseda. Iga varukoopia peab olema seotud allkirja andva seadmega.

![Sauvegarder descripteur](assets/fr/12.webp)

Meie kirjeldus (mida analüüsitakse õpetuse lõpus) on järgmine:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Viimane samm esialgse portfellikonfiguratsiooni juures on allkirja seadmetena kasutatavate riistvaraportfellide kirjelduse kontrollimine.

![Enregistrer descripteur](assets/fr/13.webp)

Tehke sama iga allkirjastamise seadme puhul. Peate kontrollima ja kinnitama, et kirjeldaja on lisatud igale riistvaraportfellile.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

Teie rahakoti andmed on nüüd registreeritud ja kõik, mis on jäänud, on konfigureerida, kuidas soovite Bitcoini võrguga ühenduda. Saate valida, kas kasutada oma sõlme (kohalikku või kaugkasutatavat) või WizardSardine'i infrastruktuuri. Viimasel juhul peate oma rahakotiga siduma e-posti aadressi, mis võimaldab teil kirjelduse kätte saada. WizardSardine'il on juurdepääs kõikidele teie tehingutele. Seetõttu soovitatakse esimest varianti.

![Sélectionner connexion réseau](assets/fr/15.webp)

Me oleme otsustanud kasutada oma sõlme. Te võite kasutada olemasolevat sõlme või paigaldada oma masinasse *kärbitud sõlme*. Kui teil ei ole ligipääsu mõnele teisele sõlmpunktile, installige oma masinasse oma sõlmpunkt, mis peaks võtma aega (umbes mitu päeva).

![Choisir type de nœud](assets/fr/16.webp)

Selle õpetuse jaoks kasutasime olemasolevat (avalikku) Electrumi serverit. Kuid olge ettevaatlik! Sellel oli juurdepääs kogu meie tegevusele Liana rahakotiga. Seega kasutage oma sõlme, kui soovite oma privaatsust kaitsta.

![Connexion serveur Electrum public](assets/fr/17.webp)

Kui sõlme konfigureerimine on lõpetatud, peaks avanema peamine ekraan, kus kuvatakse teie värskelt loodud Liana rahakott.

Kasutage võimalust hoida taastamisüksus turvalises kohas. Seda tuleks hoida strateegilises kohas, et teie surma korral saaksid teie pärijad selle üles leida.

Lisaturvalisuse tagamiseks võite panna taastamiseks kasutatavad komponendid pitseeritud kotti (*tõkestatud kott*) ja kirjutada selle seerianumber kuhugi. See tagab, et keegi ei ole sellele ligi pääsenud ja et teie seade jääb kehtima.

Meie näites oleme kokku pannud järgmised elemendid:


- Blockstream Jade allkirja seadmena pärandvara jaoks;
- USB-kaabel seadme ühendamiseks ja laadimiseks;
- Paberkandjal varukoopia lausest, kui seade ei tööta või kahjustub (arvestage, et andmekandja võib olla ka metallist ja seega ilmastikust kaitstud, nagu näiteks Cryptosteel kapslite puhul);
- Portfelli kirjeldust sisaldav USB-klahv ;
- Kirjelduse paberkandjal varukoopia, juhul kui USB-mäluseade ei tööta või on kahjustatud (seda varukoopiat ei ole siin pildistatud);
- Pärimiskiri, milles kirjeldatakse rahaliste vahendite tagasinõudmiseks võetavaid meetmeid.

![Éléments de récupération](assets/fr/18.webp)

Ja me paneme need esemed pitseri alla!

![Sachet scellé récupération](assets/fr/19.webp)

## Raha laekumine

Liana põhiekraanil kuvatakse teie saldo ja teie portfelliga seotud tehingud (varasemad ja praegused). Meie puhul on saldo null, mis on normaalne.

![Écran principal](assets/fr/20.webp)

Raha saamiseks minge vahekaardile "*Võta*" ja klõpsake "*Loo aadress*". Teie ekraanile peaks ilmuma uus aadress. See on pikem kui tavaportfellis: see on aadress, mis on seotud eraldiseisva lepinguga (P2WSH või Taproot).

![Générer nouvelle adresse](assets/fr/21.webp)

Te peate selle aadressi oma riistvaraportfellis kontrollima, klõpsates "*Kontrollige riistvaraseadmes*".

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Kui raha on saadetud, ilmub tehing põhiekraanile (esmalt kinnitamata, seejärel kinnitatud). Siin oleme selle testi jaoks saatnud 50 000 satoshit (ülekande ajal veidi üle 50 dollari). On ütlematagi selge, et teie puhul peab ülekantav summa olema tehingutasude tõttu sellest väärtusest suurusjärgu võrra suurem.

![Vérifier solde](assets/fr/23.webp)

Saate kontrollida oma vahendite aegumise staatust, kui lähete vahekaardile "*Mündid*". Sellel vahekaardil kuvatakse sinu rahakotis olevad erinevad mündid (UTXO). Siin näeme, et meie tehinguga loodud 50,000 satoshise münt aegub samal päeval (ühe tunni pärast).

![Obtenir informations pièce](assets/fr/24.webp)

Bitcoinis kasutatava UTXO esindusmudeli paremaks mõistmiseks võite tutvuda Loïc Moreli kirjutatud Bitcoini konfidentsiaalsuse kursuse esimese osaga:

https://planb.network/courses/btc204
## Jooksvad kulud

Praegused kulutused on Liana kasutamise normaalne olukord. Bitcoinide saatmine põhivõtmega toimib nagu kõigis klassikalistes Bitcoini rahakottides, näiteks Electrum või Sparrow.

Tasu tegemiseks minge vahekaardile "*Saatmine*" ja sisestage olulised andmed: saaja BTC-aadress, saadetav summa ja soovitud tasumäär. Samuti saab lisada (kohapeal salvestatud) kirjelduse, mis on teie isiklikuks mugavuseks. Meie näites saatsime 10 000 satoshit teatavale Bobile, maksumääraga 4 sat/ov ehk 0,67 dollarit tehingu toimumise ajal.

Liana pakub ka "mündikontrolli": te annate, millist münti (UTXO) soovite kulutada. Siin oleme valinud eelnevalt loodud 50 000 satoshi suuruse mündi.

![Envoyer fonds clé principale](assets/fr/25.webp)

Seejärel allkirjastage tehing oma allkirja seadmega, mis on seotud üldvõtmega, klõpsates "*allkirjastada*". Te peate tehingu oma riistvaralise rahakoti kaudu kontrollima ja kinnitama. Siin kasutasime tehingu allkirjastamiseks Nano S Plus'i.

![Signer transaction clé principale](assets/fr/26.webp)

Lõpuks edastage tehing üle võrgu, klõpsates "*Broadcast*". Pange tähele, et raha saatmine nullib kasutatud müntide taastumisaja.

![Diffuser transaction clé principale](assets/fr/27.webp)

Tehing ilmub põhiekraanile ja teie saldo ajakohastatakse.

![Solde après dépense](assets/fr/28.webp)

## Portfelli ajakohastamine

Nagu eespool selgitatud, nõuab Liana rahakott, et uuendaksite oma raha regulaarselt, tehes tehingu plokiahelas. Kui te seda ei tee, võib teie rahalisi vahendeid taastada teie pärija (või täiustatud varundamise korral teie teine seade). Selline olukord ei ole äärmiselt ohtlik, kuid see lükkab ümber selle mehhanismi loomise eesmärgi: säilitada kontroll oma bitcoinide üle ilma usaldusväärse kolmanda isiku poole pöördumata, saades samal ajal kasu turvavõrgustikust.

Enne raha (või selle osa) aegumist kuvatakse hoiatus, mida saab kasutada taastamisvõtme abil. See näitab, et teie "taastumisvõti" (*recovery path*) on varsti saadaval. Arvestades meie taastamisaja lühidust (üks tund), kuvatakse see teade otse meie puhul.

![Avertissement chemin récupération](assets/fr/29.webp)

Kui tähtaeg läheneb, ilmub nupp, mis kutsub teid üles asjaomaseid vahendeid ajakohastama.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

Müntide uuendamiseks minge vahekaardile "*Mündid*" ja klõpsake vastaval mündi lahtril "*Uuenda münt*". Kui teil on mitu münti, peaksite neid konfidentsiaalsuse huvides värskendama ükshaaval ja suhteliselt lühikese intervalliga. Kulude vähendamiseks võite oma raha konsolideerida, saates kogu portfelli uuele vastuvõtuaadressile, kuid see mõjutab teie konfidentsiaalsust.

![Actualiser pièce](assets/fr/31.webp)

Märkige tehingu soovitud tasumäär. Kuna tegemist on ülekandega iseendale, saate määrata üsna madala tasu määra, eriti kui teete seda mitu päeva enne aegumist.

![Transfert à soi-même](assets/fr/32.webp)

Tehing (tähisega "*Sefi ülekanne*") on nähtav ainult vahekaardil "*Tehingud*".

![Transactions après auto-transfert](assets/fr/33.webp)

Kui see on kinnitatud, on teie münt turvaline! Võite rahulikult puhata kuni järgmise aegumiskuupäevani.

## Bitcoini taastamine

Liana portfellist vahendite tagasinõudmisel võib teil olla üks kahest olukorrast. Teil võib olla juurdepääs arvutile, kuhu tarkvara on paigaldatud, sellisel juhul tuleb teil vaid avada see (mis juhtub täiustatud varundusmudeli puhul). Teil ei pruugi aga olla juurdepääsu sellele arvutile, seega alustame siinkohal nullist. Pange tähele, et taastamisprotseduur on mõlemal juhul sama.

Alustamiseks laadige Liana alla [Wizardsardine'i ametlikult veebilehelt](https://wizardsardine.com/liana/) või [GitHubi repositooriumist](https://github.com/wizardsardine/liana/releases), kus saate kontrollida tarkvara autentsust. Installige tarkvara ja käivitage see. Meie puhul kasutatud versioon on 0.9, nii et visuaalid võivad olla muutunud. Valige tervitusekraanil valik "Add an existing Liana wallet" (Lisa olemasolev Liana rahakott).

![Ajouter portefeuille existant](assets/fr/34.webp)

Konfigureerige, kuidas soovite võrku ühenduda. Saate valida, kas kasutada oma sõlme (kohalikku või kaugkasutatavat) või WizardSardine'i infrastruktuuri. Viimasel juhul vajate portfelli looja kasutatavat e-posti aadressi, et fondid saaksid automaatselt leida. Kui teil seda teavet ei ole, valige esimene variant.

![Sélectionner connexion réseau](assets/fr/35.webp)

Kui kasutate oma sõlme, importige portfoolio kirjeldus. See on konto tehniline kirjeldus, mis võimaldab teil välja otsida selles hoitavaid vahendeid. Meie puhul on see järgmine teave:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

Seejärel palub Liana teil sisestada mälulause. Kui teil on toimiv allkirja seade (riistvaraline rahakott), jätke see osa vahele. Kui teie seade on puudu või kahjustatud, kuid teil on vastavad 12 või 24 sõna, saate seda võimalust siiski kasutada. Kindluse mõttes (kui taastatav summa on suur) soovitame siiski hankida uue riistvaralise rahakoti ja kasutada sellel olevate võtmete taastamiseks mnemoonikat.

Meie puhul kasutame Blockstream Jade'i riistvaralist rahakotti taastamise seadmena ja valime selle sammu vahelejätmise ("*Skip*").

![Passer phrase mnémotechnique](assets/fr/37.webp)

Kontrollige ja salvestage kirjeldust oma allkirja seadmesse, valides selle ekraanil. Kui teie riistvaraline rahakott ei ilmu, kontrollige, et see on ühendatud ja lukustamata. Kontrollige ja kinnitage, et see teave on teie seadmesse lisatud.

![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Konfigureerige oma sõlme. Saate kasutada olemasolevat sõlme või paigaldada oma masinasse *kärbitud sõlme*. Meie puhul kasutasime olemasolevat sõlme.

![Choisir type de nœud](assets/fr/39.webp)

Selle õpetuse jaoks kasutasime avalikku Electrumi serverit. Siiski oli sellel juurdepääs kogu meie tegevusele Liana rahakotiga. Kui soovite oma privaatsust kaitsta, kasutage parem oma sõlme.

![Connexion serveur Electrum public](assets/fr/17.webp)

Kui olete oma sõlme seadistanud, jõuate rahakoti põhiekraanile, kus saate vaadata kontoga seotud saldot ja varasemaid tehinguid. Samuti saate vaadata, kas raha on võimalik kätte saada. Siin näeme, et mündi saab välja võtta.

![Accueil Liana récupération](assets/fr/40.webp)

Portfellis olevate vahendite taastamiseks minge vasakus allosas olevasse jaotisse Seaded ("*Settings*") ja klõpsake nupul "*Recovery*".

![Récupération dans paramètres](assets/fr/41.webp)

Kuluta rahakotis olev münt, märgistades vastava kasti. Märkige BTC-aadress, kuhu soovite raha saata, ning tehingutasu määr. Seejärel klõpsake nuppu "*Järgmine*".

![Récupération des pièces](assets/fr/42.webp)

Allkirjastage tehing, klõpsates "*allkirjastada*" ja kinnitades tehingu oma riistvara rahakotis.

![Signer transaction clé de récupération](assets/fr/43.webp)

Seejärel edastage see üle võrgu, klõpsates nupule "*Broadcast*".

![Diffuser transaction clé de récupération](assets/fr/44.webp)

Tehing peaks ilmuma põhiekraanile. Pärast kinnitamist on taastamine lõpule viidud!

![Écran principal après récupération](assets/fr/45.webp)

## Videod

Kui soovid Liana kohta rohkem teada saada, on siin mõned videod, mis annavad sulle selgema ettekujutuse selle toimimisest. Siin on Liana video esitlus koos Kévin Loaec'i ja Antoine Poinsot'ga :

![Vidéo de présentation avec Kévin Loaec et Antoine Poinsot](https://youtu.be/siuLmQo1lM8)

Ja siin on õpetus, kuidas kasutada Liana't, koos Antoine Poinsot'ga :

![Vidéo-tutoriel avec Antoine Poinsot](https://youtu.be/JrG4WMVPZDQ)

Viimases näidatud manipulatsioonid on sarnased käesolevas õpetuses esitatud manipulatsioonidega.

## Boonus: deskriptorite analüüs

Deskriptor on inimesele loetav tähemärgijada, mis kirjeldab ammendavalt aadresside kogumit. See ühendab endas mitmeid olulisi andmeid täiustatud portfelli osade (UTXO) leidmiseks. Deskriptori kirjutamise viis põhineb Andrew Poelstra, Pieter Wuille ja Sanket Kanjalkari poolt 2019. aastal välja töötatud skriptimiskeelel [Miniscript syntax] (https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/).

Et paremini mõista, miks see märgijada on oluline, analüüsime meie näite kirjeldajat, mis on :

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Sellest kirjeldusest saab välja võtta järgmise teabe:


- `wsh` (lühend *tunnistusskripti hash*): See on loodud tehinguväljundi tüüp. Kui me oleksime otsustanud kasutada Taproot'i, oleks identifikaator olnud `tr`.
- `või_d`: See on loogiline operaator, mis näitab, et kulu aktsepteerimiseks peab olema täidetud *üks kahest järgmisest* tingimusest (`_d` tähistab konkreetset süntaksit).
- "pk" (lühend *avalik võti*): See operaator kontrollib antud allkirja järgmise avaliku võtme suhtes ja annab vastuse boolaarselt (TRUE või FALSE).
- `[3689a8e7/48'/0'/0'/2']`: See element sisaldab peamise riistvaralise rahakoti (antud juhul Nano S Plus) põhivõtme *jälge* ja seotud laiendatud privaatvõtme tuletamise teed (millest kõik teised privaatvõtmed tuletatakse).
- `xpub6FKY ... WQa`: See on laiendatud avalik võti, mis on seotud peamise riistvaraportfelliga (siin Nano S Plus)
- `/<0;1>/*`: Need on tuletamise teed lihtsate võtmete ja aadresside saamiseks: `0` vastuvõtmiseks, `1` sisemisteks operatsioonideks (*muutus*), koos "jokkeriga" (`*`), mis võimaldab mitme aadressi järjestikust tuletamist konfigureeritaval viisil, sarnaselt klassikalise portfoolio tarkvara "lünga piiride" juhtimisega.
- ja_v`: See on loogiline operaator, mis näitab, et *kaks järgmist* tingimust peavad olema täidetud, et kulu oleks aktsepteeritud (`_v` tähistab konkreetset süntaksit).
- `v:pkh` (lühend *verify: public key hash*): See operaator kontrollib antud allkirja ja avalikku võtit järgneva avaliku võtme hashi (*hash*) suhtes. See on sisuliselt sama kontroll nagu P2PKH ja P2WPKH skriptide puhul.
- `[42e629dd/48'/0'/0'/2']`: See on sama element nagu eespool (mis koosneb jälgimisest ja tuletamise teest), kuid siin on märgitud riistvara taastamisportfelli (antud juhul Jade) peavõti jälgimine.
- `xpub6DpQ ... WQd`: See on laiendatud avalik võti, mis on seotud riistvara taastamise rahakotiga (siin Jade).
- `older(6)` : See operaator kontrollib, et loodud tehingu väljund peab olema vanusega, mis on rangelt suurem kui 6 plokki, et seda saaks kulutada.

Viimane andmeelement (`8alrve5h`) on kirjelduse kontrollsumma ja vastab portfelli identifikaatorile.

Selle portfoolio abil loodud skriptid võtavad järgmise kuju:

```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```

Kuna teie Bitcoini rahakoti turvalisus sõltub ka teie arusaamisest selle toimimisest, soovitan teil uurida põhjalikult deterministlike ja hierarhiliste rahakottide mehhanisme, võttes selle tasuta koolituskursuse Plan ₿ Network :

https://planb.network/courses/cyp201