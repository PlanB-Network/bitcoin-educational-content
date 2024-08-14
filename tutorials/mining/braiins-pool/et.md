---
name: Braiins Pool

description: Tutvustus Braiins Pool'ile
---

![signup](assets/cover.webp)

Braiins Pool, varem tuntud kui Slush Pool, on esimene Bitcoin'i kaevandamise bassein. Asutatud novembris 2010, kaevandas see oma esimese ploki 16. detsembril 2010, plokk 97834.

Mai 2024 seisuga on Braiins Pool'i arvutusvõimsus 13 EH/s, mis moodustab umbes 1,8% kogu Bitcoin'i hashrate'ist. See on kaevandanud kokku 1 307 188 bitcoin'i, mis on ligikaudu 6% maksimaalsest 21 miljonist bitcoin'ist, mis kunagi eksisteerima hakkavad.

### Kompensatsioonisüsteem

Alates 2023. aasta lõpust on Braiins Pool muutnud oma kompensatsioonisüsteemi, võttes kasutusele FPPS (Full Pay Per Share) süsteemi. See tähendab, et kaevurid saavad iga päev tasu kogu eelmise päeva töö eest, isegi kui bassein ei leidnud plokki. See erineb vanast süsteemist, kus kaevurid said tasu ainult siis, kui bassein leidis ploki.

**On märkimisväärne, [vastavalt Mononaut'i tweetile](https://x.com/mononautical/status/1777686545715089605), kes analüüsib Bitcoin TimeChain'i, et paljud FPPS süsteemi kasutavad kaevandusbasseinid saadavad kaevandatud bitcoin'id AntPool'i aadressile, mis tähendaks, et AntPool kontrollib kõigi nende basseinide hashrate'i, umbes 47% globaalsest Bitcoin'i hashrate'ist. See on väga halb uudis võrgu detsentraliseerituse jaoks.**

### Basseini Tasud

Braiins Pool'i tasud on 2,5%, kuid kui kasutate oma masinatel BraiinsOS'i, on tasud 0%

### Väljamaksed

**Lightning Väljamaksed**
Lightning väljamaksed võimaldavad teil oma tasusid välja võtta ilma minimaalse summata kord päevas Lightning aadressi kaudu.
Selle meetodi kasutamiseks peab teil olema Lightning aadressidega ühilduv rahakott.

**On-Chain Väljamaksed**
On-Chain väljamaksed on piiratud minimaalse summaga ja võivad olla tasulised.
Minimaalne summa: 20 000 satsi
Tasud: 10 000 satsi summade puhul, mis on väiksemad kui 500 000 satsi
Tasuta summade puhul, mis on suuremad kui 500 000 satsi
Väljamakseid saab käivitada ajavahemiku või summa järgi.

## Konto Loomine

Braiins Pool'i kasutamise alustamiseks [minge nende veebilehele](https://braiins.com/pool) ja klõpsake paremal üleval nuppu "SIGN UP"


![signup](assets/3.webp)

Sisestage oma andmed ja kinnitage, seejärel saate e-kirja, milles palutakse kinnitada teie aadress. Kinnitage e-kirjas oleva lingi kaudu ja seejärel logige platvormile sisse

![signup](assets/4.webp)


## "Töötaja" lisamine
Töötaja on kaevur, mille ühendate basseiniga. Uue kaevuri lisamiseks klõpsake vasakul külgmenüüs nuppu "Workers".
![signup](assets/7.webp)

Seejärel klõpsake lillal nupul "Connect Workers +".

Selles aknas valige oma geograafiline piirkond.

Kui soovite ühendada kaevuri, mis kasutab BraiinsOS'i, valige protokoll "Stratum V2". Vastasel juhul valige "Stratum V1".

![signup](assets/8.webp)

Teil on vaja sisestada teave oma kaevuri veebilehel (vaadake oma kaevuri dokumentatsioonist, kuhu see teave sisestada).

Siin, **"stratum+tcp://eu.stratum.braiins.com:3333"** on basseini URL.
**JimZap.workerName** on teie identifikaator ja teie kaevuri nimi, kus JimZap on identifikaator ja .workerName on kaevuri nimi. Kui teil on mitu kaevurit, võite neile kas anda sama nime, sel juhul liidetakse nende arvutusvõimsus armatuurlaual kokku, või anda neile erinevad nimed, et neid individuaalselt jälgida.
Ja parool on alati sama **"anything123"**

Kui olete selle teabe oma kaevuri veebilehel sisestanud ja see on kaevandamist alustanud, näete seda mõne minuti pärast Braiins Pooli armatuurlaual.

## Armatuurlaua Ülevaade

![signup](assets/9.webp)

Ülemises ribas näete kõigi teie kaevurite keskmist kogu hashrate'i viie minuti, ühe tunni ja 24 tunni jooksul. Ja kokkuvõte kaevuritest, mis on võrgus või võrgust väljas.
Allpool olev graafik võimaldab teil jälgida oma arvutusvõimsuse arengut.

![signup](assets/10.webp)

Selle graafiku all on teil mitu teavet oma tasude kohta satsides.

**"Tänased Kaevandamise Tasud"** Näitab satside arvu, mille olete täna kaevandanud. Päeva lõpus lähtestatakse see väärtus 0-le ja satsid saadetakse teie kontole.

**"Eilne Kogutasu"** Satside arv, mille kaevandasite eelmisel päeval

**"Hinnanguline Tulusus (1 TH/s)"** On hinnang satside arvule, mida teenite ühe päeva jooksul 1 TH/s arvutusvõimsusega. Näiteks, kui väärtus on 77 satsi, ja teil on arvutusvõimsust 10 TH/s terve päeva jooksul, siis teoreetiliselt teeniksite 77 x 10 = 770 satsi päevas.

**"Kogu Aja Tasu"** Kogu satside arv, mille olete Braiins Pooliga kaevandanud

**"Tasustamise Skeem"** Basseini poolt rakendatav tasumäär

**"Järgmise Väljamakse ETA"** Hinnang ajale, mis kulub enne, kui saate platvormilt satsid välja võtta. Siin hinnang ei näita midagi, kuna kaevandamine on kestnud vaid mõne minuti.

**"Kontojääk"** Teie kontol olevate satside arv, mille saate seejärel välja võtta.
## Väljamaksete Seadistamine
Võite oma tasud välja võtta kas on-chain või läbi lightningi aadressiga.

Üleval klõpsake "Funds". Vaikimisi on teil "Bitcoin Account". Võite luua teisi, et jagada tasusid. Me pöördume selle juurde järgmises jaotises tagasi.

Praegu klõpsake "Set up".

![signup](assets/17.webp)

Selles uues aknas saate valida "Onchain payout".

Nimetage see rahakott, esitage BTC aadress ja valige soovitud käivituse tüüp. "Threshold" tähendab, et makse käivitatakse, kui olete kogunud määratletud summa BTC-d, ja "Time interval" korral käivitatakse makse regulaarsete intervallidega (päev/nädalad/kuud).

Pange tähele, et minimaalne summa on 0.0002 BTC ja et alla 0.005 BTC puhul rakendatakse tasu 0.0001 BTC.

![signup](assets/18.webp)

Kui soovite kasutada Lightningi väljamakseid, vajate rahakotti, mis pakub Lightningi aadressi. Näiteks võite kasutada getAlby.

Klõpsake akna ülaosas "Lightning payout".

Sisestage oma Lightningi aadress ja märkige ruut "I understand..." seejärel kinnitage.

Selle väljamaksemeetodiga saadetakse teie tasud iga päev teie rahakotti.

![signup](assets/14.webp)
Kui olete oma väljamakse seaded valideerinud, saate kinnituse e-kirja.
![signup](assets/15.webp)

## Jagatud Tasud

Braiins Pool võimaldab samuti jagada teie tasusid mitme rahakoti vahel.

Selleks klõpsake üleval "Mining" ja seejärel vasakul "Settings".

![signup](assets/19.webp)

Sellel lehel saate lisada teise "Financial Account" klõpsates "Add Another Financial Account" ning jaotada oma tasud % määras nende erinevate kontode vahel, millele peate seostama rahakoti. Uue rahakoti seostamiseks Finantskontoga vaadake eelmist jaotist.