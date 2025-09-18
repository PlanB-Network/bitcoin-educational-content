---
name: Bitcoin Core (Linux)
description: Oma sõlme käivitamine Bitcoin core-ga Linuxis
---

![cover](assets/cover.webp)


## Oma sõlme käivitamine Bitcoin core abil


Bitcoin ja sõlme mõiste tutvustus, mida täiendab põhjalik paigaldusjuhend Linuxi kohta.


Bitcoin üks põnevamaid aspekte on võimalus ise programmi käivitada ja seega osaleda võrgustiku ja avaliku tehingu Ledger kontrollimisel.


Bitcoin on avatud lähtekoodiga projektina olnud vabalt kättesaadav ja avalikult levitatav alates 2009. aastast. Peaaegu 17 aastat pärast selle loomist on Bitcoin nüüd tugev ja peatamatu digitaalne rahavõrk, mis saab kasu võimsast orgaanilisest võrguefektist. Satoshi Nakamoto väärib oma jõupingutuste ja visiooni eest meie tänu. Muide, me võõrustame Bitcoin whitepaperit siin Agora 256-s (märkus: ka ülikoolis).


### Oma pangaks saamine


Bitcoin eetose järgijate jaoks on oma sõlme pidamine muutunud oluliseks. Kelleltki luba küsimata on võimalik Blockchain algusest peale alla laadida ja seega kontrollida kõiki tehinguid A-st Z-ni vastavalt Bitcoin protokollile.


Programm sisaldab ka oma Wallet. Seega on meil kontroll tehingute üle, mida me ülejäänud võrku saadame, ilma vahendajate või kolmandate isikuteta. Te olete ise oma pank.


Selle artikli ülejäänud osa on seega juhend Bitcoin core - kõige laialdasemalt kasutatava Bitcoin tarkvaraversiooni - paigaldamiseks spetsiaalselt Debianiga ühilduvatele Linuxi distributsioonidele, nagu Ubuntu ja Pop!OS. Järgige seda juhendit, et astuda üks samm lähemale oma individuaalsele suveräänsusele.


## Bitcoin core paigaldusjuhend Debian/Ubuntu jaoks


**Eeldused**


- Minimaalselt 6 GB andmemahtu (pruned sõlme) - 1 TB andmemahtu (Full node)
- Eeldage, et *Initial Block Download* (IBD) võtab vähemalt 24 tundi. See toiming on kohustuslik isegi pruned sõlme puhul.
- Lubage IBD jaoks ~600 GB ribalaiust, isegi pruned sõlme puhul.


** Märkus:💡** järgmised käsud on Bitcoin core versiooni 24.1 jaoks etteantud.


### Failide allalaadimine ja kontrollimine



- [Download](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, samuti `SHA256SUMS` ja `SHA256SUMS.asc` failid (ilmselgelt peate alla laadima tarkvara uusima versiooni).



- Avage terminal kataloogis, kus allalaaditud failid asuvad. Näide: `cd ~/Downloads/`.



- Kontrollige, et versioonifaili kontrollsumma on kontrollsummafailis loetletud, kasutades käsku `sha256sum --ignore-missing --check SHA256SUMS`.



- Selle käsu väljund peaks sisaldama allalaaditud versioonifaili nime, millele järgneb "OK". Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Installige git käsuga `sudo apt install git`. Seejärel kloonige Bitcoin core allkirjastajate PGP-võtmeid sisaldav repositoorium käsuga `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Impordi kõigi allkirjastajate PGP-võtmed käsuga `gpg --import guix.sigs/builder-keys/*`



- Kontrollige, et kontrollsummafail on allkirjastatud allkirjastajate PGP-võtmetega, kasutades käsku `gpg --verify SHA256SUMS.asc`.



Iga kehtiva allkirja puhul kuvatakse rida, mis algab järgmiselt: `gpg: Hea allkiri` ja teine rida, mis lõpeb sõnaga: `Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (näide Pieter Wuille'i PGP-võtme sõrmejäljest).


**Märkus💡:** ei ole vaja, et kõik allkirjastamisvõtmed tagastaksid "OK". Tegelikult võib olla vajalik ainult üks. Kasutaja peab ise määrama oma PGP kinnitamise lävendi.


Te võite hoiatusi ignoreerida:



- "See võti ei ole sertifitseeritud usaldusväärse allkirjaga!



- "Puudub märge, et allkiri kuulub omanikule


### Bitcoin core graafilise Interface paigaldamine



- Kasutage terminalis, endiselt kataloogis, kus asub Bitcoin core versiooni fail, käsku `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, et ekstraheerida arhiivis olevad failid.



- Paigaldage eelnevalt ekstraheeritud failid käsuga `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Paigaldage vajalikud sõltuvused käsuga `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Käivitage _bitcoin-qt_ (Bitcoin core graafiline Interface), kasutades käsku `Bitcoin-qt`.



- pruned sõlme valimiseks märgistage _Limit Blockchain storage_ ja konfigureerige salvestatavate andmete piirang:


![welcome](assets/fr/02.webp)


### 1. osa kokkuvõte: paigaldusjuhend


Kui Bitcoin core on paigaldatud, on soovitatav seda võimalikult palju töös hoida, et aidata kaasa Bitcoin võrgule, kontrollides tehinguid ja edastades uusi plokke teistele eakaaslastele.


Siiski on endiselt hea tava oma sõlme aeg-ajalt käivitada ja sünkroniseerida, isegi kui see on vajalik vastuvõetud ja saadetud tehingute valideerimiseks.


![Creation wallet](assets/fr/03.webp)


## Tori konfigureerimine Bitcoin core sõlme jaoks


**Märkus💡:** See juhend on mõeldud Bitcoin core 24.0.1 jaoks Ubuntu/Debianiga ühilduvates Linuxi distributsioonides.


### Tor'i paigaldamine ja konfigureerimine Bitcoin core jaoks


Kõigepealt peame installima Tor-teenuse (The Onion Router), anonüümse suhtluse jaoks kasutatava võrgu, mis võimaldab meil anonüümseks muuta meie suhtlust Bitcoin võrguga. Sissejuhatus veebipõhiste privaatsuskaitsevahendite, sealhulgas Tor'i kohta on esitatud meie sellekohases artiklis.


Tor'i installimiseks avage terminal ja sisestage `sudo apt -y install tor`. Kui paigaldus on lõpetatud, käivitub teenus tavaliselt automaatselt taustal. Kontrollige, et see töötab õigesti käsuga `sudo systemctl status tor`. Vastus peaks näitama `Active: active (exited)`. Funktsioonist väljumiseks vajutage klahvi `Ctrl+C`.


**Nipp:** igal juhul saate kasutada järgmisi käske terminalis, et käivitada, peatada või taaskäivitada Tor:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Järgmisena käivitame Bitcoin core graafilise Interface käsuga `Bitcoin-qt`. Seejärel aktiveerime tarkvara automaatse funktsiooni, et suunata meie ühendused läbi Tor-proxy: _Settings > Network_ ja sealt valige _Connect through SOCKS5 proxy (default proxy)_ ning _Use a separate SOCKS5 proxy to reach peers via Tor onion services_.


![option](assets/fr/04.webp)


Bitcoin core tuvastab automaatselt, kas Tor on paigaldatud, ja kui see on nii, loob vaikimisi väljaminevad ühendused teiste sõlmedega, mis samuti kasutavad Tor'i, lisaks ühendustele IPv4/IPv6-võrke (clearnet) kasutavate sõlmedega.


**Märkus💡:** Et muuta kuvamiskeel prantsuse keeleks, minge seadete vahekaardile Kuvamine.


### Täiustatud Tori konfiguratsioon (valikuline)


Bitcoin core on võimalik konfigureerida nii, et ta kasutaks ainult Tor-võrku, et luua ühendust eakaaslastega, optimeerides seega meie anonüümsust meie sõlme kaudu. Kuna graafilises Interface ei ole selleks sisseehitatud funktsionaalsust, tuleb meil käsitsi luua konfiguratsioonifail. Minge Settings (Seaded) ja seejärel Options (Valikud).


![option 2](assets/fr/05.webp)


Siin klõpsake nuppu _Open configuration file_ (konfiguratsioonifaili avamine). Kui olete tekstifailis `Bitcoin.conf`, lisage lihtsalt rida `onlynet=onion` ja salvestage fail. Selleks, et see käsk jõustuks, tuleb Bitcoin core uuesti käivitada.


Seejärel konfigureerime Tori teenuse nii, et Bitcoin core saab sissetulevaid ühendusi proxy kaudu, mis võimaldab teistel võrgusõlmedel kasutada meie sõlme Blockchain andmete allalaadimiseks, ilma et see ohustaks meie masina turvalisust.


Terminali sisestage `sudo nano /etc/tor/torrc`, et pääseda ligi Tori teenuse konfiguratsioonifailile. Otsige selles failis rida `#ControlPort 9051` ja eemaldage `#`, et seda lubada. Nüüd lisage faili kaks uut rida:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Failist väljumiseks selle salvestamise ajal vajutage klahvi `Ctrl+X > Y > Enter`. Tagasi terminalis, taaskäivitage Tor, sisestades käsu `sudo systemctl restart tor`.


Sellise konfiguratsiooni korral saab Bitcoin core luua sissetulevaid ja väljaminevaid ühendusi teiste võrgusõlmedega ainult Tor-võrgu (Onion) kaudu. Selle kinnitamiseks klõpsake vahekaardil _Window_, seejärel _Peers_.


![Nodes Window](assets/fr/06.webp)


### Täiendavad ressursid


Lõppkokkuvõttes võib ainult Tori võrgu (`onlynet=onion`) kasutamine muuta teid Sybil Attack suhtes haavatavaks. Seepärast soovitavad mõned sellise riski vähendamiseks säilitada mitme võrgu konfiguratsiooni. Lisaks suunatakse kõik IPv4/IPv6 ühendused läbi Tor-proxy, kui see on konfigureeritud, nagu eelnevalt märgitud.


Alternatiivina, et jääda ainult Tori võrku ja vähendada Sybil Attack ohtu, võite lisada oma `Bitcoin.conf` faili teise usaldusväärse sõlme Address, lisades rea `addnode=trusted_address.onion`. Seda rida võite lisada mitu korda, kui soovite luua ühenduse mitme usaldusväärse sõlme juurde.


Kui soovite vaadata oma Bitcoin sõlme logisid, mis on konkreetselt seotud selle suhtlusega Toriga, lisage faili `Bitcoin.conf` faili `debug=tor`. Nüüd on teie tõrjelogis asjakohane Toriga seotud teave, mida saate vaadata aknas _Information_ nupu _Debug File_ abil. Neid logisid on võimalik vaadata ka otse terminalis käsuga `bitcoind -debug=tor`.


**Tipp💡:** siin on mõned huvitavad lingid:


- [Wiki lehekülg, mis selgitab Tori ja selle seost Bitcoin-ga](https://en.Bitcoin.it/wiki/Tor)
- [Bitcoin core konfiguratsioonifaili generaator Jameson Loppi poolt](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Jon Atacki koostatud Tor'i konfiguratsiooni juhend](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Nagu alati, kui teil on küsimusi, jagage neid julgelt Agora256 kogukonnaga. Me õpime koos, et olla homme paremad kui täna!