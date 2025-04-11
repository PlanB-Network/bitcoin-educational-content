---
name: Ledger Nano S

description: Kuidas seadistada oma Ledger Nano S seadet
---

![pilt](assets/cover.webp)

Külm füüsiline rahakott – 60€ – Algaja – Turvamaks 2000€ kuni 50 000€

Ledger on Prantsuse lahendus bitcoinide turvaliseks hoidmiseks lihtsal viisil.

Selles õpetuses arutame ka paroolilauseid, mis on edasijõudnud turvalahendus suurte summade hoidmiseks: 20 000€ – 100 000€.

https://www.youtube.com/watch?v=_vsHNTLi8MQ

# Ühenda Ledger Sparrow Bitcoin Rahakotiga (juhendi kirjutamine)

Veenduge, et olete läbi lugenud teise osa “Kasutades Bitcoin Riistvara Rahakotte” esmalt. Ma jätan mõned sammud vahele ja keskendun peamiselt sellele, mis on spetsiifiline Ledgeri jaoks siin.

## Seadme seadistamine

Ledgeriga tuleb kaasa oma USB kaabel. Veenduge, et kasutate just seda ja mitte suvalist vana kaablit. Mõned USB kaablid on ainult toite jaoks. See siin edastab andmeid JA toidet. Kui olen seadet kasutanud telefonilaadija USB kaabliga, mis juhtus olema käepärast, ei ole seade ühendust saanud.

Ühendage see oma arvutiga ja seade lülitub sisse.

![pilt](assets/1.webp)

Kerige läbi valikute. Näete

1. Seadista kui uus seade
2. Taasta taastefraasist

Põhimõtteliselt küsib see, kas soovite, et seade looks teile seemne või kui teil on juba olemasolev, mida sooviksite kasutada. On parim tava teha oma seeme, kuid seda turvaliselt teha on väga edasijõudnud ja väljaspool selle artikli ulatust. Valige “Seadista kui uus seade”

Seejärel palutakse teil valida PIN-kood. See ei ole osa teie Bitcoin seemnest ja on spetsiifiline ainult sellele seadmele. See lukustab seadme.

Seejärel esitatakse teile 24 sõna, mida peate läbi kerima ja üles kirjutama.

Kummalisel kombel, kui jõuate lõppu, ütleb see “vajuta vasakule, et oma sõnu kontrollida”. See ei kirjelda, kuidas kinnitada jätkamiseks, see lihtsalt tähendab, et saate sõnu uuesti vaadata. Vajutage paremale selle asemel ja kinnitage vajutades vasakule ja paremale korraga.

Järgmine osa on ülimalt tüütu. See segab 24 sõna ja peate kinnitama igaühe, 1 kuni 24, läbides kõik sõnad iga valiku jaoks. Kui olete lõpetanud, lubab see teil kahe nupuvajutusega kinnitada ja jätkata.

![pilt](assets/2.webp)

Teie armatuurlaual näete, et teil on seadete nupp ja plussmärgiga nupp, mis võimaldab teil rakendusi installida. Kuid peate esmalt ühenduma Ledger Live'iga. Teeme seda järgmisena…

## Laadi alla Ledger Live

Võiksite Ledger Live'i alla laadida nende veebilehelt, kuid parem on saada see GitHubist, kus hoitakse lähtekoodi.

Google'i otsing “ledger live GitHub” või klõpsake seda linki https://github.com/LedgerHQ/ledger-live-desktop

![pilt](assets/3.webp)

Kerige alla, kuni näete pealkirja “Allalaadimised”…

![pilt](assets/4.webp)

Allpool näete linki: Juhised installipakettide räsi ja allkirjade kontrollimiseks on saadaval sellel lehel. Klõpsake seda linki.(https://live.ledger.tools/lld-signatures)

![pilt](assets/5.webp)

Üleval on linkide valikud tarkvarapaketi jaoks, mida vajate, sõltuvalt teie operatsioonisüsteemist. Klõpsake sobivat, et alla laadida.

Järgmisena soovime alla laaditud faili räsi kontrollida, lisaturvalisuse tagamiseks.
Ledger avaldab iga selle lehel saadaoleva faili räsi. Nüüd räsime allalaaditud faili ja võrdleme väljundit. See peab olema identne, et veenduda faili mittemanipuleerituses.

Ava terminal Macis või CMD Windowsis. Järgi neid käsklusi...

cd Downloads

<Enter>

```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- Macile
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- Windowsile
```

<Enter>

Loodetavasti on ilmne, et käsud algavad noolte järel. Veendu, et kui see artikkel on aegunud, muudad käskudes failinime täpselt selleks failinimeks, mille alla laadisid. Peale iga käsku pead vajutama <Enter> klahvi. Siin näidatud käsud ei pruugi sinu veebibrauseris ühele reale mahtuda. Pane tähele, et kõik on kirjutatud ühele reale.

Vaata räsi väljundit ja veendu, et see on identne GitHubis avaldatuga.

Ideaaljuhul tahad sa olla veelgi ettevaatlikum ja veenduda, et avaldatud räsud ei ole võltsitud. Seda teeme gpg allkirjadega, kuid see on selle artikli ulatusest väljas. Kui soovid selle kohta rohkem teada saada (ja ma soovitan, et sa seda lõpuks teeksid), siis loe seda artiklit.

## Ühendu Ledger Live'iga

Enne Ledger Live'i käivitamist aitab privaatsust veidi parandada VPN-i sisselülitamine. Ledger saab endiselt kõik su aadressid kätte, kuid nad ei tea sinu IP-aadressi, mis reedab sinu koduaadressi. Mullvad VPN on suurepärane VPN-teenus ja see ei ole väga kallis (ma ei reklaami, lihtsalt kasutan seda).

Paigalda tarkvara oma arvutisse ja käivita see.

![image](assets/6.webp)

Vali oma seade ja vali “Esimene kord kasutades…”

![image](assets/7.webp)

Seejärel viiakse sind läbi viisardi, kuid me oleme kõik need sammud juba teinud, nii et saad edasi liikuda.

![image](assets/8.webp)

Pärast paljusid samme ja viktoriini kontrollitakse, kas seade on ehtne. Peate veenduma, et olete ühendatud ja sisestanud PIN-koodi, seejärel küsib seade, kas lubate Ledger Live'il ühenduda. Peate selle kinnitama, muidugi.

![image](assets/9.webp)

Järgmises hüpikaknas oli mõningane shitcoin reklaam, mis oli maskeeritud kui “väljalaske märkmed”. Lükka see tagasi ja siis peaksid jõudma sellele ekraanile.

![image](assets/10.webp)

Peate klõpsama “Lisa konto”, et saada Bitcoin Wallet.

![image](assets/11.webp)

Veendu, et valiksid Bitcoin, mitte Bitcoin Cash või mõne muu shitcoini. See kontrollib seadet ja peate kinnitama, et jätkata SEADMES. See arvutab aadresse paar minutit. Seejärel klõpsa VALMIS.

![image](assets/12.webp)
![image](assets/13.webp)

Suurepärane. Nüüd on sul arvutis shitcoin rahakoti haldur, mis sisaldab Bitcoin rahakotti. Tegelikult sa ei vaja seda enam ja võid sellest lahti saada. Tegelik eesmärk oli saada Bitcoin App seadmesse endasse ja see oli ainus viis, välja arvatud mõningate ekstreemsete tarkvarainseneri tehnikate kasutamine.

Mäleta, et varem, seadmes, oli meil seadete nupp ja plussmärgi nupp. Nüüd on meil lisaks Bitcoin App nupp.

Võid nüüd Ledger Live'i sulgeda.

## Lisa paroolilause
Nüüd, kui meil on Bitcoin App, saame oma seemnefraasile lisada paroolilause. Me ei saanud seda teha varem, kui seeme esimest korda loodi, sest alguses meil ei olnud Bitcoin Appi ja me pidime ühenduma Ledger Live'iga, et seda saada.

Mine seadme "settings" menüüsse, seejärel alammenüüsse "security". Seejärel vali passphrase. Näed "Advanced feature". Klõpsa paremat nuppu, näed "read manuel…" ja seejärel pärast parema nupu klõpsamist näed "back". Kuid see pole veel kõik. Intuitiivselt võiksid arvata, et see on kõik, kuid klõpsa paremat nuppu uuesti. Näed "set up passphrase".

Võid otsustada "attach to PIN" või "Set temporarily". Soovitan "attach to the PIN". Nii saad sõltuvalt sellest, millist PIN-koodi sisestad seadme esmakordsel sisselülitamisel, juurdepääsu erinevatele rahakottidele. Kui valiksid "set temporarily", pead iga kord, kui soovid sellele rahakotile juurde pääseda, paroolilause sisestama, kuid see on alati vaikimisi PIN-koodiga.

Sisesta paroolilause ja kinnita see.

See küsib sinult "Current PIN". See ei ole PIN, mida seostad uue paroolilausega. See on PIN, mille sisestasid seadme selle sessiooni jaoks sisselülitamisel.

Nüüd saad peamenüüsse tagasi minna, valides mõned korrad tagasi valiku.

## Rahakoti Jälgimine

Eelmistes artiklites selgitasin, kuidas alla laadida ja kontrollida Sparrow rahakotti ning kuidas seda ühendada omaenda noodiga või avaliku noodiga. Peaksid järgima neid juhiseid:

- Installi Bitcoin Core (https://armantheparman.com/bitcoincore/)

- Installi Sparrow Bitcoin Wallet (https://armantheparman.com/download-sparrow/)

- Ühenda Sparrow Bitcoin Wallet Bitcoin Core'iga (https://armantheparman.com/sparrowcore/)

Sparrow Bitcoin Walleti alternatiivina võib kasutada Electrum Desktop Walletit, kuid ma jätkan Sparrow Bitcoin Walleti selgitamist, kuna pean seda enamiku inimeste jaoks parimaks. Edasijõudnud kasutajad võivad eelistada kasutada alternatiivina Electrumit.

Nüüd laeme selle üles ja ühendame Ledgeri, rahakotiga, mis sisaldab paroolilauset. See rahakott ei ole kunagi olnud avatud Ledger Live'is, kuna see loodi PÄRAST seadme ühendamist Ledger Live'iga. Veendu, et sa ei ühenda seda kunagi uuesti Ledger Live'iga, et mitte paljastada oma uut privaatset rahakotti.

Loo uus rahakott:

![image](assets/14.webp)

Pane sellele ilus nimi

![image](assets/15.webp)

Pane tähele märkeruutu "Has existing transaction". Kui see on rahakott, mida oled varem kasutanud, siis märgi see ruut, vastasel juhul kuvatakse saldo valesti nullina. Selle ruudu märkimine palub Sparrow'l uurida Bitcoin Core'i andmebaasi (blockchain) varasemate tehingute kohta. Selle juhendi jaoks kasutame täiesti uut rahakotti, nii et võid ruudu märkimata jätta.

![image](assets/16.webp)

Klõpsa "Connected Hardware Wallet" ja veendu, et seade on tegelikult ühendatud, sisse lülitatud, PIN sisestatud ja oled sisestanud Bitcoin Appi.

![image](assets/17.webp)

Klõpsa "Scan" ja seejärel järgmisel ekraanil "Import Keystore".

![image](assets/18.webp)

Järgmisel ekraanil pole midagi muuta, Ledger on selle sinu eest täitnud. Klõpsa "Apply"

![image](assets/19.webp)
Järgmine ekraan võimaldab teil lisada parooli. Ärge ajage seda segamini "paroolilausega"; paljud inimesed teevad seda. Nimetus on kahjuks eksitav. Parool võimaldab teil seda rahakotti oma arvutis lukustada. See on spetsiifiline ainult sellele tarkvarale selles arvutis. See ei ole osa teie Bitcoini privaatvõtmest.
![image](assets/20.webp)

Pärast pausi, kui arvuti mõtleb, näete, kuidas vasakul olevad nupud muutuvad hallist siniseks. Palju õnne, teie rahakott on nüüd kasutamiseks valmis. Tehke ja saatke tehinguid nii palju kui süda lustib.

![image](assets/21.webp)

## Vastuvõtmine

Bitcoini vastuvõtmiseks minge vasakul olevale aadresside vahelehele ja valige üks aadressidest, millele soovite vastu võtta. Lihtsalt paremklõpsake soovitud aadressil ja valige "kopeeri aadress". Seejärel minge oma vahetusplatvormile, kust raha saadetakse, ja kleepige see sinna. Või võite aadressi anda kliendile, kes saab seda kasutada teile maksmiseks.

Kui kasutate rahakotti esimest korda, peaksite vastu võtma väga väikese summa, harjutama selle saatmist teisele aadressile, kas rahakoti sees või tagasi vahetusplatvormile, et tõestada, et rahakott toimib nagu oodatud.

Kui olete seda teinud, peate varundama sõnad, mille üles kirjutasite. Ühest koopiast ei piisa. Tehke vähemalt kaks paberkoopiat (metall on parem) ja hoidke neid kahes erinevas, hästi turvatud kohas. See vähendab loodusõnnetuse riski, mis hävitab teie HWW ja paberist varukoopia ühe sündmuse käigus. Vaadake täieliku arutelu jaoks "Bitcoini riistvararahakottide kasutamine".

## Saatmine

![image](assets/22.webp)

Makse tegemisel peate "Maksa" väljale kleepima aadressi, millele maksate. Tegelikult ei saa te sildi välja tühjaks jätta, see on lihtsalt teie enda rahakottide kirjete jaoks, kuid Sparrow ei luba seda – lihtsalt sisestage midagi (ainult teie näete seda). Sisestage summa ja saate käsitsi kohandada ka soovitud tasu.

Rahakott ei saa tehingut allkirjastada, kui HWW pole ühendatud. See on HWW ülesanne – vastu võtta tehing, see allkirjastada ja tagastada allkirjastatuna. Veenduge, kui allkirjastate seadmel, et visuaalselt kontrollite, kas maksate sama aadressi, mis on seadmel ja arvuti ekraanil, ning arve, mille saate (nt võite olla saanud e-kirja teatud aadressile maksmiseks).

Pöörake tähelepanu ka sellele, et kui valite maksesummast suurema mündi, siis ülejääk saadetakse tagasi ühele teie rahakottide vahetus aadressidest. Mõned inimesed ei ole seda teadnud ja on oma tehingut avalikul plokiahelal üles otsides arvanud, et mõned bitcoini saadeti ründaja aadressile, kuid tegelikult oli see nende enda vahetus aadress.

## Püsivara

Püsivara uuendamiseks peate ühenduma Ledger Live'iga. Kui soovite seda teha, peaksite seadme esmalt pühkima ja veenduma, et teil on olemas oma varundussõnad ja paroolilause seadme taastamiseks. Eelistan seadme esmalt pühkida, sest peate oma seadme Ledger Live'iga ühendama püsivara uuendamiseks ja eelistan mitte kunagi oma uut rahakotti (see, millel on paroolilause) Ledger Live'ile paljastada. Lihtsalt ei usalda, et Ledger ei ekstrakti minu avaliku võtme teavet seadmest, kui ühendan selle Ledger Live'iga. Nad väidavad, et nad ei tee seda, kuid ma ei saa seda ise kontrollida, kui ma ei loe koodi ja mõista sisemist riistvara.

## Järeldus
See artikkel näitas teile, kuidas kasutada Ledger HWW-d turvalisemal ja privaatsemal viisil, kui reklaamitud – kuid ainult see artikkel ei ole piisav. Nagu ma alguses ütlesin, peaksite seda kombineerima teabega, mis on esitatud teoses „Bitcoin'i riistvarakottide kasutamine“. Nõuanded:

Staatiline Lightning aadress: dandysack84@walletofsatoshi.com
https://armantheparman.com/ledgersparrow/

Selle teema süvendamiseks ja oma rahakoti turvalisuse tugevdamiseks Ledger Nano'ga koos BIP39 passphrase'iga kutsun teid tutvuma selle põhjaliku õpetusega:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

