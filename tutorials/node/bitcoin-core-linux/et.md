---
nimi: Bitcoin Core Node (linux)
kirjeldus: Oma sõlme käitamine Bitcoin Core'iga
---

![kaas](assets/cover.webp)

# Oma sõlme käitamine Bitcoin Core'iga

Sissejuhatus Bitcoini ja sõlme kontseptsiooni, millele lisandub põhjalik paigaldusjuhend Linuxile.

Üks Bitcoini kõige põnevamaid ettepanekuid on võimalus programm ise käivitada ja seeläbi osaleda võrgus ning avaliku tehinguregistri kontrollimises granulaarsel tasemel.

Bitcoin, avatud lähtekoodiga projekt, on olnud avalikult levitatav ja tasuta saadaval alates 2009. aastast. Peaaegu 15 aastat pärast selle loomist on Bitcoin nüüdseks vastupidav ja peatamatu digitaalne rahandusvõrk, millest saadav kasu põhineb võimsal orgaanilisel võrguefektil. Nende pingutuste ja visiooni eest väärib Satoshi Nakamoto meie tänu. Muide, me võõrustame Bitcoini valge raamatut siin Agora 256-s (märkus: samuti ülikoolis).

## Saades omaenda pangaks

Oma sõlme käitamine on muutunud hädavajalikuks neile, kes järgivad Bitcoini põhimõtet. Ilma kellegi loata on võimalik alla laadida plokiahel algusest peale ja seeläbi kontrollida kõiki tehinguid A-st Z-ni vastavalt Bitcoini protokollile.

Programm sisaldab ka oma rahakotti. Seega on meil kontroll tehingute üle, mida saadame ülejäänud võrku, ilma vahendaja või kolmanda osapoole sekkumiseta. Te olete omaenda pank.

Ülejäänud artikkel on seega juhend Bitcoin Core'i paigaldamiseks — kõige laialdasemalt kasutatav Bitcoini tarkvaraversioon — eriti Debianiga ühilduvatele Linuxi distributsioonidele, nagu Ubuntu ja Pop!_OS. Järgige seda juhendit, et astuda samm lähemale oma individuaalsele suveräänsusele.

## Bitcoin Core'i paigaldusjuhend Debian/Ubuntu jaoks

> Eeltingimused
>
> - Minimaalselt 6GB andmeruumi (piiratud sõlm) — 1TB andmeruumi (täissõlm)
> - Jätke vähemalt 24 tundi algse ploki allalaadimise (IBD) lõpuleviimiseks. See toiming on kohustuslik isegi piiratud sõlme jaoks.
> - Jätke ~600GB ribalaiust IBD jaoks, isegi piiratud sõlme jaoks.

> 💡 Järgnevad käsud on eeldefineeritud Bitcoin Core versioonile 24.1.

## Failide allalaadimine ja kontrollimine

1. Laadige alla bitcoin-24.1-x86_64-linux-gnu.tar.gz, samuti SHA256SUMS ja SHA256SUMS.asc failid. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Avage terminal kataloogis, kus allalaaditud failid asuvad. Näiteks cd ~/Downloads/.
3. Kontrollige, et versioonifaili kontrollsumma on loetletud kontrollsumma failis, kasutades käsku sha256sum --ignore-missing --check SHA256SUMS.
4. Selle käsu väljund peaks sisaldama allalaaditud versioonifaili nimele järgnevat "OK". Näide: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Installige git, kasutades käsku sudo install git. Seejärel kloonige repositoorium, mis sisaldab Bitcoin Core'i allkirjastajate PGP võtmeid, kasutades käsku git clone https://github.com/bitcoin-core/guix.sigs.
6. Importige kõikide allkirjastajate PGP võtmed, kasutades käsku gpg --import guix.sigs/builder-keys/\*
7. Kontrollige, et kontrollsumma fail on allkirjastatud allkirjastajate PGP võtmetega, kasutades käsku gpg --verify SHA256SUMS.asc.
Iga allkiri tagastab rea, mis algab järgmiselt: gpg: Hea allkiri ja teine rida lõppeb järgmiselt: Esmane võtme sõrmejälg: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (näide Pieter Wuille'i PGP võtme sõrmejäljest).
> 💡 Kõikide allkirjastajate võtmed ei pea tagastama "OK". Tegelikult võib piisata vaid ühest. Kasutaja peab ise määrama oma valideerimisläve PGP kontrollimiseks.
>
> Võite ignoreerida sõnumeid HOIATUS: See võti ei ole usaldusväärse allkirjaga kinnitatud!

> Pole mingit märki, et allkiri kuuluks omanikule.

## Bitcoin Core graafilise liidese paigaldamine

1. Terminalis, endiselt kataloogis, kus asub Bitcoin Core versioonifail, kasutage arhiivis sisalduvate failide ekstraktimiseks käsku tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz.

2. Paigaldage varem ekstraktitud failid käsu sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\* abil.

3. Paigaldage vajalikud sõltuvused käsu sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev abil.

4. Käivitage bitcoin-qt (Bitcoin Core graafiline liides) käsu bitcoin-qt abil.

5. Kärbitud sõlme valimiseks märkige piirake plokiahela salvestusruumi ja seadistage salvestatava andme limiit:

![welcome](assets/1.webp)

## Järeldus 1. osa: Paigaldusjuhend

Kui Bitcoin Core on paigaldatud, on soovitatav hoida seda võimalikult palju töös, et panustada Bitcoin võrku, kontrollides tehinguid ja edastades uusi plokke teistele peeridele.

Siiski, oma sõlme jooksmine ja sünkroniseerimine katkendlikult, isegi ainult vastuvõetud ja saadetud tehingute valideerimiseks, on hea praktika.

![Creation wallet](assets/2.webp)

# Tori seadistamine Bitcoin Core sõlme jaoks

> 💡 See juhend on mõeldud Bitcoin Core 24.0.1 jaoks Ubuntu/Debian ühilduvatel Linuxi distributsioonidel.

## Tori paigaldamine ja seadistamine Bitcoin Core jaoks

Esmalt peame paigaldama Tori teenuse (The Onion Router), võrgu, mida kasutatakse anonüümseks suhtluseks, mis võimaldab meil anonüümida meie interaktsioone Bitcoin võrguga. Online privaatsuskaitse vahendite, sealhulgas Tori, tutvustuseks vaadake meie artiklit sellel teemal.

Tori paigaldamiseks avage terminal ja sisestage sudo apt -y install tor. Paigalduse lõppedes käivitub teenus tavaliselt automaatselt taustal. Kontrollige, et see töötab korrektselt käsu sudo systemctl status tor abil. Vastus peaks näitama Active: active (exited). Selle funktsiooni väljumiseks vajutage Ctrl+C.

> Igaks juhuks võite terminalis kasutada järgmisi käske Tori käivitamiseks, peatamiseks või taaskäivitamiseks:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

Järgmisena käivitame Bitcoin Core graafilise liidese käsu bitcoin-qt abil. Seejärel lubame tarkvara automaatse funktsiooni, et suunata meie ühendused läbi Tori puhverserveri: Seaded > Võrk, ja sealt saame kontrollida Ühenda läbi SOCKS5 puhverserveri (vaikimisi puhverserver) ning kasutada eraldi SOCKS5 puhverserverit, et jõuda peerideni läbi Tori sibulateenuste.

![option](assets/3.webp)

Bitcoin Core tuvastab automaatselt, kas Tor on paigaldatud ja kui jah, siis loob vaikimisi väljaminevad ühendused teiste sõlmedega, mis kasutavad samuti Tori, lisaks ühendustele sõlmedega, mis kasutavad IPv4/IPv6 võrke (clearnet).
💡 Prantsuse keeleks ekraanikeele muutmiseks minge seadete all olevasse vahekaarti Display.

## Täiustatud Tori seadistamine (valikuline)

On võimalik seadistada Bitcoin Core kasutama ühenduste loomiseks ainult Tor võrku, optimeerides nii meie anonüümsust meie sõlme kaudu. Kuna graafilises liideses selleks sisseehitatud funktsionaalsust ei ole, peame käsitsi looma konfiguratsioonifaili. Minge Settings, seejärel Options.

![option 2](assets/4.webp)

Siin klõpsake Open configuration file. Bitcoin.conf tekstifailis lisage lihtsalt rida onlynet=onion ja salvestage fail. Bitcoin Core'i taaskäivitamiseks peate selle käsu jõustumiseks taaskäivitama.
Seejärel seadistame Tori teenuse nii, et Bitcoin Core saaks vastu võtta sissetulevaid ühendusi läbi puhverserveri, võimaldades teistel võrgusõlmedel kasutada meie sõlme blockchaini andmete allalaadimiseks ilma meie masina turvalisust ohustamata.

Terminalis sisestage sudo nano /etc/tor/torrc, et pääseda ligi Tori teenuse konfiguratsioonifailile. Selles failis otsige rida #ControlPort 9051 ja eemaldage # selle lubamiseks. Nüüd lisage faili kaks uut rida: HiddenServiceDir /var/lib/tor/bitcoin-service/ ja HiddenServicePort 8333 127.0.0.1:8334. Failist väljumiseks salvestamisega vajutage Ctrl+X > Y > Enter. Tagasi terminalis taaskäivitage Tor, sisestades käsu sudo systemctl restart tor.

Selle seadistusega saab Bitcoin Core luua sissetulevaid ja väljaminevaid ühendusi teiste võrgusõlmedega ainult Tor võrgu (Onion) kaudu. Selle kinnitamiseks klõpsake vahekaardil Window, seejärel Peers.

![Nodes Window](assets/5.webp)

## Lisamaterjalid

Lõppkokkuvõttes võib ainult Tor võrgu (onlynet=onion) kasutamine muuta teid haavatavaks Sybili rünnaku suhtes. Seetõttu soovitavad mõned säilitada mitmevõrgulise konfiguratsiooni, et leevendada seda tüüpi riski. Peale selle suunatakse kõik IPv4/IPv6 ühendused Tori puhverserveri kaudu, kui see on konfigureeritud, nagu eelnevalt mainitud.

Alternatiivina, et jääda ainult Tor võrku ja leevendada Sybili rünnaku riski, võite oma bitcoin.conf faili lisada teise usaldusväärse sõlme aadressi, lisades rea addnode=trusted_address.onion. Seda rida võite lisada mitu korda, kui soovite ühenduda mitme usaldusväärse sõlmega.

Oma Bitcoin sõlme logide vaatamiseks, mis on spetsiifiliselt seotud selle suhtlusega Toriga, lisage oma bitcoin.conf faili debug=tor. Nüüd on teil debug logis asjakohane Tori teave, mida saate vaadata Information aknas Debug File nupuga. Neid logisid on võimalik vaadata ka otse terminalis käsklusega bitcoind -debug=tor.

> 💡 Mõned huvitavad lingid:
>
> - Wiki lehekülg, mis selgitab Tori ja selle suhet Bitcoiniga
> - Bitcoin Core konfiguratsioonifaili generaator Jameson Loppi poolt
> - Tori seadistamise juhend Jon Atacki poolt

Nagu alati, kui teil on küsimusi, jagage neid vabalt Agora256 kogukonnaga. Õpime koos, et olla homme paremad kui täna!