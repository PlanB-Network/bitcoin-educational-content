---
nimi: Bitcoin Core Noeud (mac & windows)
kirjeldus: Paigalda Bitcoin Core Macile või Windowsile
---

Bitcoin Core paigaldamine tavakasutaja arvutisse on võimalik, kuid see pole ideaalne. Kui sul pole midagi selle vastu, et jätta oma arvuti tööle 24/7, siis see töötab hästi. Kui on vaja arvutit välja lülitada, muutub tüütuks oodata tarkvara sünkroniseerimist iga kord, kui selle uuesti sisse lülitad.

Juhised on mõeldud Maci või Windowsi kasutajatele. Linuxi kasutajad tõenäoliselt ei vaja minu abi, kuid Linuxi juhised on Maciga väga sarnased.

## Alusta puhtalt

Ideaaljuhul soovid kasutada puhast arvutit, üht ilma pahavarata. Isegi kui kasutad riistvara rahakotti, võib pahavara sind sinu müntidest ilma jätta.

Sa kas võid puhastada vana arvuti ja kasutada seda pühendatud Bitcoin arvutina või osta pühendatud arvuti/sülearvuti.

## Kõvaketas

Bitcoin Core võtab sinu draivil umbes 400 gigabaiti andmeid ja see maht jätkab kasvamist. Sa võid kasutada oma sisemist draivi, kuid võid ka ühendada välist kõvaketast. Ma selgitan mõlemat võimalust. Ideaalis peaksid kasutama tahkis-draivi. Kui sul on vana arvuti, siis tõenäoliselt ei ole sellist sees. Lihtsalt osta 1 või 2 terabaidine väline SSD ja kasuta seda. Tavaline draiv tõenäoliselt töötab, kuid võid kohata probleeme ja see on palju aeglasem.

![pilt](assets/1.webp)

## Laadi alla Bitcoin Core

Mine lehele bitcoin.org (veendu, et sa ei läheks bitcoin.com, mis on shitcoin sait, mida omab Roger Ver, pettes inimesi ostma Bitcoin Cashi Bitcoini asemel)

Kui oled seal, ei ole imelikul kombel ilmne, kust tarkvara saada. Mine ressursside menüüsse ja klõpsa "Bitcoin Core", nagu allpool näidatud:

![pilt](assets/2.webp)

See viib sind allalaadimise lehele:

![pilt](assets/3.webp)

Klõpsa oranžil nupul Laadi alla Bitcoin Core:

![pilt](assets/4.webp)

Valikuid on mitu, sõltuvalt sinu arvutist. Esimesed kaks on selle juhendi jaoks asjakohased; vali vasakul ribal Windows või Mac. Pärast klõpsamist algab allalaadimine, tõenäoliselt sinu Allalaadimiste kausta.

## Kontrolli allalaadimist (osa 1)

Vajad faili, mis sisaldab erinevate väljalasete räsiväärtusi. See fail oli varem bitcoin.org allalaadimislehel, kuid on nüüd liikunud lehele bitcoincore.org/en/download:

![pilt](assets/5.webp)

Vajad SHA256 binaarseid räsiväärtusi sisaldavat faili. See fail sisaldab Bitcoin Core'i erinevate allalaadimispakettide SHA256 räsiväärtusi.

Järgmisena peame räsima Bitcoin Core'i allalaadimise ja võrdlema seda sellega, mida fail ütleb, et räsi peaks olema. Siis teame, et allalaadimine on identne sellega, mida bitcoincore.org ootab.

Liigu uuesti Allalaadimiste kausta ja täida see käsk (asenda X-id täpselt täisnoodi bitcoin allalaadimisfaili nimega):

```bash
shasum -a 256 XXXXXXXXXXXX # <--- MACILE
certutil -hashfile XXXXXXXXXXX SHA256 # <--- WINDOWSILE
```

Saad räsi väljundi. Pane see kirja ja võrdle seda SHA256SUMS failis sisalduva räsiga.

Kui väljundid on identsed, siis oled kontrollinud, et ühtegi andmebitti ei ole muudetud... peaaegu. Meil on vaja veel veenduda, et SHA256SUMS fail ei ole pahatahtlik.

Järgmise sammu jätkamiseks peab meie arvutis olema paigaldatud gpg.
Selleks vaadake minu SHA256/gpg juhendit ja kerige umbes poole peale jaotiseni "Download gpg" ning otsige oma operatsioonisüsteemi alapealkirja. Seejärel tulge siia tagasi.
## Hankige Avalik Võti

Tagasi allalaadimislehel, hankige SHA256 räsi allkirjade fail

![image](assets/6.webp)

Klõpsake seda ja salvestage fail kettale, eelistatavalt Kaustadesse Allalaadimised.

See fail sisaldab erinevate inimeste allkirju SHA256SUMS failile.

Me soovime peaarhitekti avalikku võtit, Wladimir J. van der Laani oma arvuti võtmehoidlas. Tema avaliku võtme ID on:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Kopeerige see tekst järgmisesse käsklusesse:

```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Huvipärast, igal ajal, võite näha, millised võtmed on arvuti võtmehoidlas selle käsklusega:

```bash
gpg --list-keys
```

## Kontrollige allalaadimist (osa 2)

Meil on avalik võti, nii et nüüd saame kontrollida SHA256SUMS faili, mis sisaldab Bitcoin Core allalaadimise räsiväärtusi ja nende räside allkirju.

Avage uuesti Terminal või CMD ja veenduge, et olete Kaustades Allalaadimised. Sealt täitke see käsk:

```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```

Esimene loetletud fail on allkirjafaili täpne kirjapilt. Teine loetletud fail peaks olema tekstifaili, mis sisaldab räsiväärtusi, täpne kirjapilt. Mõlemad failid peaksid olema samas kaustas ja te peate olema failide kaustas, vastasel juhul peate iga faili jaoks välja kirjutama täieliku tee.

See on väljund, mida peaksite saama

![image](assets/7.webp)

HOIATUSE sõnumit on ohutu ignoreerida – see lihtsalt meenutab teile, et te pole Wladimiriga võtmepoolel isiklikult kohtunud ega küsinud temalt, mis on tema avalik võti, ning seejärel öelnud oma arvutile, et usaldab seda võtit täielikult.

Kui saite selle sõnumi, teate nüüd, et SHA256SUMS.asc faili ei ole pärast Wladimiri allkirjastamist muudetud.

## Installige Bitcoin Core

Te ei tohiks vajada detailseid juhiseid programmi installimiseks.

![image](assets/8.webp)

## Käivitage Bitcoin Core

Macis võite saada hoiatuse (Apple on endiselt Bitcoinile vastu)

![image](assets/9.webp)

Klõpsake OK ja seejärel avage oma Süsteemieelistused

![image](assets/10.webp)

Klõpsake Turvalisuse ja Privaatsuse ikoonil:

![image](assets/11.webp)

Seejärel klõpsake "ava igal juhul":

![image](assets/12.webp)

Viga ilmub uuesti, kuid seekord on teil saadaval AVA nupp. Klõpsake seda.

![image](assets/13.webp)

Bitcoin Core peaks laadima ja teile kuvatakse mõned valikud:

![image](assets/14.webp)

Siin saate valida, kas kasutada vaikimisi teed, kuhu plokiahel alla laaditakse, või võite valida oma välist draivi. Kui kavatsete kasutada sisemist draivi, soovitan vaikimisi teed mitte muuta, see teeb asjade seadistamise lihtsamaks, kui installite teisi tarkvarasid, mis suhtlevad Bitcoin Core'iga.
Võite valida kärbitud sõlme käitamise, see säästab ruumi, kuid piirab, mida oma sõlmega teha saate. Igatahes laadite alla terve plokiahela ja kontrollite seda niikuinii, nii et kui teil on ruumi, hoidke alla laaditud andmeid ja ärge kärpige, kui vähegi võimalik.

Kui olete kinnitanud, hakkab plokiahel alla laadima. See võtab mitu päeva.

![image](assets/15.webp)

Võite arvuti välja lülitada ja hiljem allalaadimise juurde tagasi tulla, see ei tee midagi halba.