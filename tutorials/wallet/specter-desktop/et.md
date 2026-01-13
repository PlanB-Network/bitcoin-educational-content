---
name: Specter Desktop
description: Haldage oma mitme allkirjaga Bitcoin portfelli täiesti suveräänselt oma sõlme abil
---

![cover](assets/cover.webp)



Specter Desktop on Cryptoadvance'i poolt alates 2019. aastast välja töötatud avatud lähtekoodiga rakendus (MIT litsents), mis hõlbustab Bitcoin rahakottide haldamist koos teie riistvaraliste rahakottidega (Ledger, Trezor, Coldcard, BitBox02, Passport jne) ja teie enda Bitcoin infrastruktuuriga (Bitcoin Core node või Electrum server). Rakendus paistab silma eelkõige mitme allkirjastamisega konfiguratsioonides, võimaldades teil kindlustada suuri summasid, jaotades allkirjastamisvõimsuse mitme sõltumatu riistvaralise rahakoti vahel.



**Selles õpetuses saate teada, kuidas:**




- Installige ja konfigureerige Specter Desktop oma arvutisse (Windows, macOS või Linux)
- Ühendage Specter Electrum serveriga (selles näites kasutame Umbrel'i)
- Looge lihtne wallet riistvaraga wallet (Coldcard)
- Võtta vastu ja saata bitcoine täiesti suveräänselt
- 2-on-3 multisignatuuriga wallet seadistamine mitme riistvaralise rahakotiga
- Installige Specter Umbreli serverile (edasijõudnute boonus)



Kõik teie tehingud valideeritakse kohapeal teie enda infrastruktuuri kaudu, edastamata mingit teavet välisserveritesse, mis tagab teie konfidentsiaalsuse ja finantssuveräänsuse. Enne allkirjastamist kontrollige tehinguid alati oma wallet riistvara ekraanil.



## Allalaadimine ja paigaldamine



Rakenduse allalaadimiseks külastage Specter Desktopi ametlikku veebisaiti.



![Page d'accueil Specter](assets/fr/01.webp)



Valige allalaadimislehel oma operatsioonisüsteemile vastav versioon: macOS, Windows või Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Pärast allalaadimist installige rakendus vastavalt oma operatsioonisüsteemi tavapärastele juhistele. MacOS-i puhul lohistage ikoon rakendustesse. Windowsi puhul käivitage installija. Linuxi puhul järgige paketi juhiseid.



## Esialgne konfiguratsioon



Esimesel käivitamisel palub Specter Desktop teil valida ühenduse tüüp. Saate luua ühenduse Electrum serveriga või oma Bitcoin Core sõlme.



![Choix du type de connexion](assets/fr/03.webp)



Selles näites kasutame ühendust Electrum serveriga, mis töötab Umbrelil.



Lisateavet leiate meie Umbreli juhendmaterjalist:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

See valik pakub kiiremat sünkroniseerimist kui Bitcoin Core. Kui soovite, võite valida "Bitcoin Core" ja konfigureerida ühenduse oma kohaliku sõlme. Järgmised sammud jäävad sõltumata teie valikust samaks.



Valige "Electrum ühendus", seejärel valige "Sisestage oma", et konfigureerida oma Electrum server.



![Configuration Electrum](assets/fr/04.webp)



Sisestage oma Electrum serveri aadress. Umbreli puhul on aadress `umbrel.local` ja port `50001`. Klõpsake ühenduse loomiseks nupule "Connect".



Pärast ühendamist ilmub tervitusekraan koos kontrollnimekirjaga, mis aitab teil alustada. Nüüd peate lisama oma riistvara rahakotid.



![Écran d'accueil](assets/fr/05.webp)



## wallet riistvara lisamine



Vasakpoolses menüüs klõpsake "Lisa seade", et lisada oma wallet riistvara.



Specter Desktop toetab mitmeid riistvara rahakotte: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault ja paljud teised.



Kui soovite rohkem teada saada, vaadake meie riistvara wallet õpetusi.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Valige oma wallet riistvara. Selles näites kasutame Coldcard MK4.



Allpool leiate meie õpetuse selle wallet riistvara kohta:



https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Coldcard'i puhul tuleb avalikud võtmed eksportida wallet riistvarast kas USB-ühenduse või microSD-kaardi kaudu.



![Import des clés du Coldcard](assets/fr/07.webp)



Järgige kuvatavaid juhiseid, et eksportida võtmed oma Coldcardilt. Andke oma wallet riistvarale nimi (siin "MK4 Tuto"). Kui võtmed on imporditud, saate luua wallet ühe võtmega või lisada teisi riistvara rahakotte mitme allkirjaga wallet jaoks.



![Dispositif ajouté](assets/fr/08.webp)



## Portfelli loomine



Pärast wallet riistvara lisamist klõpsake "Create single key wallet", et luua ühe allkirjaga wallet.



Andke oma portfooliole nimi (nt "Wallet for tuto") ja valige aadressi tüüp. Valige "Segwit", et kasutada emakeelseid bech32-aadresse, mis optimeerivad tehingukulusid.



![Configuration du portefeuille](assets/fr/09.webp)



Kui teie portfell on loodud, pakub Specter võimalust salvestada varukoopia PDF-faili, mis sisaldab kogu portfelli taastamiseks vajalikku avalikku teavet (kirjeldused, laiendatud avalikud võtmed). See fail ei sisalda teie isiklikke võtmeid.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Bitcoinide vastuvõtmine



Bitcoinide vastuvõtmiseks valige vasakpoolses menüüs oma wallet, seejärel klõpsake vahekaardil "Receive".



Specter genereerib automaatselt uue vastuvõtu aadressi koos QR-koodiga.



![Génération d'une adresse de réception](assets/fr/11.webp)



Saate aadressi kopeerida või skaneerida QR-koodi. Kontrollige alati aadressi oma wallet riistvara ekraanil, enne kui seda kellelegi edasi annate.



## Vaata ajalugu ja aadressid



Kui olete bitcoinid saanud, saate oma tehinguid vaadata vahekaardil "Tehingud".



![Historique des transactions](assets/fr/12.webp)



Vahekaardil "Aadressid" saate vaadata kõiki teie portfelli loodud aadresse koos nende kasutamisstaatuse ja nendega seotud summadega.



![Liste des adresses](assets/fr/13.webp)



## Bitcoinide saatmine



Bitcoinide saatmiseks klõpsake vahekaardil "Saada". Sisestage saaja aadress, saadetav summa ja kontrollige lisavalikuid, kui soovite käsitsi valida UTXOs (mündi kontroll).



![Création d'une transaction](assets/fr/14.webp)



Tehingu loomiseks klõpsake nupule "Create Unsigned Transaction". Seejärel palub Specter teil tehingu oma wallet riistvaraga allkirjastada.



![Signature de la transaction](assets/fr/15.webp)



Kui kasutate Coldcard'i, saate valida, kas allkirjastada USB-kaardi või microSD-kaardi abil (õhu abil). Kinnitage tehing oma wallet riistvara ekraanil, kontrollides hoolikalt sihtkoha aadressi ja summat.



Kui tehing on allkirjastatud, saate seda Bitcoin võrgus edastada.



![Options de diffusion](assets/fr/16.webp)



Tehingu saatmiseks klõpsake nuppu "Saada tehing". Specter kinnitab, et teie tehing on saadetud, ja te saate jälgida selle staatust vahekaardil Tehingud.



![Diffusion de la transaction](assets/fr/17.webp)



## Mitme allkirjaga portfelli loomine ja kasutamine



Üks Specter Desktopi peamisi eeliseid on selle võime lihtsustada mitme allkirjaga portfellide haldamist. Mitme allkirjaga wallet nõuab tehingu autoriseerimiseks mitut allkirja, kõrvaldades seega ühe veapunkti. Näiteks 2-on-3-konfiguratsioon nõuab iga kulutuse kinnitamiseks kaks allkirja kolmest erinevast riistvara rahakotist.



Multisig wallet loomiseks lisage kõigepealt kõik allkirjastavad riistvara rahakotid "Lisa seade" abil. Selles näites kasutame kolme erinevat riistvaralist rahakotti: Coldcard MK4 (juba varem lisatud), Passport ja Ledger. Selline tootjate mitmekesistamine tugevdab turvalisust, vältides sõltuvust ühest tarneahelast või firmavarast.



Siin on lingid Ledger ja Passport õpetustele:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Lisage Passport, andes wallet riistvarale nime (nt "Passport multi") ja importides selle võtmed microSD-kaardi või QR-koodi abil. Seejärel klõpsake jätkamiseks nuppu "Continue" (Jätka).



![Ajout du Passport](assets/fr/23.webp)



Seejärel lisage Ledger, ühendades selle USB kaudu ja avades Bitcoin rakenduse wallet riistvaral. Andke sellele nimi (nt "ledger multi") ja klõpsake "Get via USB" ning seejärel "Continue", et importida selle avalikud võtmed.



![Ajout du Ledger](assets/fr/24.webp)



Kui olete oma kolm riistvaralist rahakotti Specteris registreerinud, klõpsake "Lisa wallet" ja valige valik "Mitme allkirjaga", et luua mitme allkirjaga wallet.



![Choix du type de wallet](assets/fr/25.webp)



Valige kolm riistvaralist rahakotti, mida soovite lisada oma mitme allkirja kvoorumisse: MK4 Tuto, Passport multi ja ledger multi. Järgmise sammu jätkamiseks klõpsake nuppu "Jätka".



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Valige oma mitme allkirja konfiguratsioon. Valige aadressitüübiks "Segwit", et saada kasu optimeeritud tasudest. Parameetriga "Tehingute autoriseerimiseks vajalikud allkirjad (m 3-st)" saate määrata künnise: 2-kolmese konfiguratsiooni puhul on vaja 2 allkirja. Iga wallet riistvara kuvab vastava multisig võtme. Loomise lõpuleviimiseks klõpsake nuppu "Create wallet" (Loo wallet).



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Teie "Multi tuto" multisignatuurne portfoolio on nüüd loodud. Specter soovitab teil kohe salvestada varukoopia PDF-faili, mis sisaldab portfoolio kirjeldust. Selle kriitilise tähtsusega faili allalaadimiseks klõpsake nuppu "Save Backup PDF".



![Wallet multisig créé](assets/fr/28.webp)



Specter võimaldab teil ka eksportida wallet teavet igasse oma riistvara rahakotti QR-koodi või faili kaudu. See võimaldab teatavatel riistvaralistel rahakottidel (näiteks Coldcard või Passport) salvestada multisig-konfiguratsiooni otse oma mällu.



Passi jaoks avage oma seade, seejärel minge jaotisse "Konto haldamine" > "Connect Wallet" > "Specter" > "Multisig" > "QR-kood", seejärel skannige Specteri poolt genereeritud QR-kood. Seejärel palub teie Passport teil skannida vastuvõtuaadressi oma wallet-st, et kinnitada multisig-konfiguratsioon.



MK4 puhul ühendage see arvutisse ja avage see. Seejärel klõpsake nupule "Save MK4 Tuto file" ja salvestage fail oma MK4-i. Järgmine kord, kui te oma wallet riistvara allkirjastate, kasutab MK4 seda faili, et lõpetada multisegi konfigureerimine.



![Export vers les hardware wallets](assets/fr/29.webp)



Teavitamiseks saate igal ajal juurdepääsu varukoopiatele oma portfelli vahekaardilt "Seaded" ja seejärel "Eksport":



![Accès au backup PDF](assets/fr/30.webp)



Igapäevane kasutamine jääb sarnaseks lihtsa wallet-ga: te generate saate aadressid nagu tavaliselt. Bitcoinide saatmiseks minge vahekaardile "Saada", sisestage saaja aadress ja summa ning klõpsake seejärel "Loo allkirjastamata tehing".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter ehitab PSBT (Partially Signed Bitcoin Transaction) ja kuvab "Acquired 0 of 2 signatures". Nüüd peate allkirjastama vähemalt kahega oma kolmest riistvaralisest rahakotist. Klõpsake esimesel wallet riistvaral (nt "MK4 Tuto"), et allkirjastada oma Coldcardiga, seejärel teisel (nt "Passport multi"), et saada teine nõutav allkiri.



![Signature de la transaction](assets/fr/32.webp)



Kui olete saanud 2 nõutavat allkirja (liides näitab "Acquired 2 of 2 signatures" ja "Transaction is ready to send"), klõpsake "Send Transaction", et edastada tehing Bitcoin võrgus.



![Transaction prête à être diffusée](assets/fr/33.webp)



Selline mitme allkirjaga lähenemisviis sobib eriti hästi ettevõtetele (mitu juhti peab kulutused heaks kiitma), perekondadele (mitme põlvkonna pärandi kaitse) või üksikisikutele, kes haldavad suuri summasid (riistvara rahakottide geograafiline jaotamine, et taluda kohalikke katastroofe).



### Mitme allkirjaga varukoopiate kriitiline tähtsus



**Pöörake tähelepanu**: mitmemääralise portfelli varundamine erineb põhimõtteliselt ühe portfelli varundamisest. Teie taastamislausetest (seed lausetest) üksi ei piisa multisig portfelli taastamiseks. Te peate varundama ka **output descriptor** (output descriptor), mis sisaldab teie multisig portfelli konfiguratsiooniteavet.



output descriptor sisaldab olulisi andmeid: iga kaasallkirjastaja laiendatud avalikud võtmed (xpubs), allkirja lävi (meie näites 2 kohta 3), kasutatud skripti tüüp (native, nested või legacy Segwit) ja iga wallet riistvara ümbersõiduteed. Ilma selle kirjelduseta ei saa te isegi siis, kui teil on kaks teie kolmest taastamislausest, oma wallet ümber ehitada ega oma bitcoinidele ligi pääseda. Deskriptor võimaldab teie tarkvaral teada, kuidas kombineerida avalikke võtmeid generate teie rahalistele vahenditele vastavate Bitcoin aadresside jaoks.



Specter Desktop genereerib automaatselt varukoopia PDF-faili, kui loote oma multisig portfelli. See PDF sisaldab täielikku kirjeldust, iga wallet riistvara sõrmejälgi ja kogu taastamiseks vajalikku avalikku teavet. **See fail ei sisalda teie isiklikke võtmeid** ja seetõttu ei võimalda teil iseenesest oma bitcoin'e kulutada, kuid võimaldab kõigil, kes sellele ligi pääsevad, näha teie täielikku tehingulugu ja saldot.



Oma mitme allkirja konfiguratsiooni õigeks varundamiseks järgige järgmist protseduuri: pärast portfelli loomist klõpsake vahekaardil "Settings", seejärel "Export" ja valige "Save Backup PDF". Looge sellest PDF-st mitu koopiat: printige vähemalt kaks koopiat paberile ja säilitage ka krüpteeritud digitaalne koopia. Hoidke üks PDF-i koopia koos iga oma taastamislausega geograafiliselt eraldi asuvas kohas.



Graveerige oma taastamise fraasid tulekindlatele ja veekindlatele metallplaatidele, et tagada nende pikaealisus. Ärge kunagi alahinnake nende varukoopiate tähtsust: kui kaotate arvutist kausta `~/.specter` JA kaotate ühe oma riistvaralise rahakoti ilma kirjelduse varukoopiata, on kõik teie vahendid pöördumatult kadunud, isegi 2-kordse konfiguratsiooni korral. Mitme allkirja redundants kaitseb wallet riistvara kadumise eest, kuid ainult siis, kui olete oma wallet kirjelduse korrektselt varundanud.



## Specter Desktopi eelised ja piirangud



**Eelised**: Optimaalne konfidentsiaalsus koos täieliku kohaliku valideerimisega ilma kolmanda osapoole serveriteta. Mitme allkirja paindlikkus täiustatud konfiguratsioonide jaoks (ettevõtte, perekonna, üksikisiku). Laialdane wallet riistvara tugi koos täieliku koostalitlusvõimega (USB ja õhu kaudu ühendatud).



**Piirangud**: Märkimisväärne õppimine Bitcoin edasijõudnud mõistete (UTXOd, deskriptorid, tuletamise teed) osas.



## Parimad tavad



Kontrollige alati enne valideerimist oma riistvara wallet ekraanil olevaid aadresse ja summasid, et kaitsta end pahavara eest.



Hoidke PDF-väljavõtteid oma seemnetest eraldi. Neid avalikke kirjeldusi saab hoida pangakapis või krüpteeritud pilves, mis hõlbustab taastamist ilma teie isiklikke võtmeid paljastamata.



Enne suurte fondidega portfellide kasutamist testige token summade taastamist. Looge, testige, kustutage ja taastage oma protseduuride valideerimiseks.



Hoidke Specter ja oma püsivara ajakohasena. Jaotage oma mitme allkirja kaasallkirjastajad geograafiliselt (kodus/kontoris/läheduses), et taluda kohalikke katastroofe. Kasutage kirjeldavaid silte, et hõlbustada raamatupidamist ja maksudeklaratsioone.



## Boonus: paigaldus Bitcoin serverile (Umbrel, RaspiBlitz, Start9)



Kui teil on juba Bitcoin server, näiteks Umbrel, RaspiBlitz, MyNode või Start9, saate installida Specter Desktopi otse nende rakenduste poest. Selline lähenemine pakub mitmeid olulisi eeliseid: rakendus konfigureerib end automaatselt teie kohaliku Bitcoin Core-sõlme jaoks, see on veebiliidese kaudu 24/7 kättesaadav mis tahes seadmest teie võrgus ja te saate sellele isegi turvaliselt Tor'i kaudu eemalt ligi pääseda. Kogu teie Bitcoin infrastruktuur on tsentraliseeritud ühte spetsiaalsesse serverisse, mis lihtsustab haldamist ja tugevdab teie suveräänsust.



### Installeerimine Umbrel App Store'ist



Mine oma Umbreli kasutajaliidesest App Store'i ja otsi Specter Desktop. Paigaldamise käivitamiseks klõpsake nupule "Install".



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Kui paigaldus on lõpetatud, avage Specter Desktop oma Umbrelil. Tervitusekraanil palutakse teil valida ühenduse tüüp. Kui kasutate Specterit oma Umbrelil, klõpsake ühenduse konfigureerimiseks "Update settings".



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Valige "Remote Specter USB connection", et võimaldada kohaliku arvutiga ühendatud USB-riistvara rahakottide kasutamist, kui kasutate Specterit kauges Umbreli serveris.



![Configuration Remote Specter USB](assets/fr/20.webp)



Järgige kuvatavaid juhiseid HWI-silla konfigureerimiseks. Peate sisenema seadme silla seadistustesse ja lisama domeeni `http://umbrel.local:25441` valgelistile. Klõpsake konfiguratsiooni salvestamiseks nupule "Update".



![HWI Bridge Settings](assets/fr/21.webp)



Kui soovite kasutada oma USB-riistvara rahakotte ka kohalikust arvutist, laadige oma masinasse alla rakendus Specter Desktop ja seadistage see "Jah, ma kasutan Specterit eemalt". Klõpsake konfiguratsiooni lõpetamiseks nupule "Save" (Salvesta).



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Kokkuvõte



Specter Desktop demokratiseerib Bitcoin täiustatud konfiguratsioonid, muutes mitme allkirja kasutamise kättesaadavaks, ilma et see ohustaks teie suveräänsust või konfidentsiaalsust. Märkimisväärseid rahasummasid haldavate kasutajate jaoks muudab see institutsionaalsed tavad lahendusteks, mida saavad kasutada eraisikud.



Kuigi rakendus nõuab esialgset investeeringut infrastruktuuri ja õppimisse, pakub see täielikku suveräänsust: kontrolli valideerimisinfrastruktuuri üle, võtmete füüsilist omandiõigust ja kolmandate isikute järelevalvest vabu tehinguid. Olenemata sellest, kas olete üksikisik, kes kindlustab oma sääste, perekond, kes loob mitme põlvkonna hoiukasti, või ettevõte, kes haldab rahavooge, Specter Desktop on võrdlusvahend maksimaalse turvalisuse ja absoluutse suveräänsuse ühitamiseks.



## Ressursid



### Ametlikud dokumendid




- [Specter Desktop ametlik kodulehekülg](https://specter.solutions/desktop/)
- [GitHubi lähtekood](https://github.com/cryptoadvance/specter-desktop)
- [Täielik dokumentatsioon](https://docs.specter.solutions/)



### Ühendus ja toetus




- [Telegram Specter Community Group](https://t.me/spectersupport)
- [Redditi arutelufoorum](https://reddit.com/r/specterdesktop/)
- [GitHubi veateated](https://github.com/cryptoadvance/specter-desktop/issues)