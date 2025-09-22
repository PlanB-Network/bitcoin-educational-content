---
name: Boltzmann Calculator
description: Razumeti koncept entropije i kako koristiti Boltzmannovu formulu
---
![cover](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, vebsajt KYCP.org trenutno nije dostupan. Gitlab koji je hostovao Python Boltzmann Calculator kod je takođe zaplenjen. Trenutno nije moguće preuzeti ovaj alat. Međutim, moguće je da će kod biti ponovo objavljen od strane drugih u narednim nedeljama. U međuvremenu, možete i dalje koristiti ovaj vodič da biste razumeli kako funkcioniše Boltzmann kalkulator. Pokazatelji koje pruža ovaj alat primenljivi su na bilo koju Bitcoin transakciju i mogu se takođe izračunati ručno. Obezbediću sve potrebne proračune u ovom vodiču. Ako ste već preuzeli Python alat na svoj uređaj ili ako koristite RoninDojo, možete nastaviti da koristite alat i pratite ovaj vodič kao i obično, i dalje funkcioniše.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

Boltzmann kalkulator je alat za analizu Bitcoin transakcije merenjem njenog nivoa entropije zajedno sa drugim naprednim metrikama. Pruža uvide u veze između ulaza i izlaza transakcije. Ovi indikatori nude kvantifikovanu procenu privatnosti transakcije i pomažu u identifikaciji potencijalnih grešaka.


Ovaj Python alat razvili su timovi Samourai novčanika i OXT, ali se može koristiti na bilo kojoj Bitcoin transakciji.


## Kako koristiti Boltzmann kalkulator?

Da biste koristili Boltzmann kalkulator, dostupne su vam dve opcije. Prva je da instalirate Python alat direktno na vaš uređaj. Alternativno, možete se odlučiti za KYCP.org (_Know Your Coin Privacy_) vebsajt, koji nudi platformu za pojednostavljeno korišćenje. Za korisnike RoninDojo-a, imajte na umu da je ovaj alat već integrisan u vaš čvor.


Korišćenje KYCP sajta je prilično jednostavno: samo unesite identifikator transakcije (txid) koji želite da analizirate u traku za pretragu i pritisnite `ENTER`.

![KYCP](assets/1.webp)

Zatim ćete pronaći različite informacije o transakciji, uključujući veze između ulaza i izlaza. Kliknite na `deterministic links`.

![KYCP](assets/2.webp)

Stići ćete na stranicu posvećenu pokazateljima Boltzmann kalkulatora.

![KYCP](assets/3.webp)

Za one koji preferiraju da koriste alat direktno sa svog RoninDojo čvora, dostupan je putem `RoninCLI > Samourai Toolkit > Boltzmann Calculator`.


Kao i sa sajtom KYCP.org, kada je Python alat instaliran, jednostavno ćete morati da nalepite txid transakcije koju želite da analizirate.


![KYCP](assets/7.webp)


Zatim pritisnite taster `ENTER` da biste dobili rezultate.


![KYCP](assets/8.webp)


## Koji su indikatori Boltzmann kalkulatora?

### Kombinacije / Interpretacije:

Prvi indikator koji softver izračunava je ukupan broj mogućih kombinacija, označen pod `nb combinations` ili `interpretations` u alatu.


Uzimajući u obzir vrednosti UTXO-a uključenih u transakciju, ovaj indikator izračunava broj načina na koje se ulazi mogu povezati sa izlazima. Drugim rečima, određuje broj mogućih interpretacija koje transakcija može izazvati iz perspektive spoljnog posmatrača koji je analizira.

Na primer, CoinJoin strukturiran prema Whirlpool 5x5 modelu predstavlja `1,496` mogućih kombinacija: ![KYCP](assets/4.webp)

Whirlpool Surge Cycle 8x8 CoinJoin, s druge strane, predstavlja `9,934,563` mogućih interpretacija: ![KYCP](assets/5.webp)

Nasuprot tome, tradicionalnija transakcija sa 1 ulazom i 2 izlaza će predstaviti samo jedno tumačenje: ![KYCP](assets/6.webp)


### Entropija:

Drugi indikator koji se izračunava je entropija transakcije, označena sa `Entropy`.


U opštem kontekstu kriptografije i informacija, entropija je kvantitativna mera nesigurnosti ili nepredvidljivosti povezane sa izvorom podataka ili slučajnim procesom. Drugim rečima, entropija kvantifikuje koliko je teško predvideti ili pogoditi informacije.


U specifičnom kontekstu analize lanaca, entropija je takođe naziv indikatora, izvedenog iz Shannonove entropije i [izumljenog od strane LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), koji se izračunava pomoću Boltzmann alata.


Kada transakcija pokazuje veliki broj mogućih kombinacija, često je relevantnije pozvati se na njenu entropiju. Ovaj indikator omogućava merenje nedostatka znanja analitičara o tačnoj konfiguraciji transakcije. Drugim rečima, što je veća entropija, to je analitičarima teži zadatak identifikacije Bitcoin kretanja između ulaza i izlaza.


U praksi, entropija otkriva da li, iz perspektive spoljnog posmatrača, transakcija predstavlja više mogućih interpretacija, zasnovanih isključivo na iznosima ulaza i izlaza, bez razmatranja drugih spoljašnjih ili unutrašnjih obrazaca i heuristika. Visoka entropija je tada sinonim za bolju poverljivost transakcije.


Entropija je definisana kao binarni logaritam broja mogućih kombinacija. Ovde je korišćena formula:

```plaintext
E: entropija transakcije
C: broj mogućih kombinacija za transakciju

E = log2(C)
```


U matematici, binarni logaritam (logaritam sa bazom 2) odgovara inverznoj operaciji eksponenciranja broja 2. Drugim rečima, binarni logaritam od `x` je eksponent na koji se `2` mora podići da bi se dobilo `x`. Ovaj pokazatelj se stoga izražava u bitovima.


Hajde da uzmemo primer izračunavanja entropije za CoinJoin transakciju strukturisanu prema Whirlpool 5x5 modelu, koji, kao što je ranije pomenuto, nudi broj mogućih kombinacija od `1,496`:

```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```

Dakle, ova CoinJoin transakcija pokazuje entropiju od `10.5469 bita`, što se smatra veoma zadovoljavajućim. Što je ova vrednost viša, to transakcija dopušta više različitih interpretacija, čime se jača njen nivo privatnosti.

Za CoinJoin transakciju 8x8 koja predstavlja `9,934,563` interpretacija, entropija bi bila:

```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```


Hajde da uzmemo još jedan primer sa konvencionalnijom transakcijom, koja sadrži jedan ulaz i dva izlaza: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) U slučaju ove transakcije, jedina moguća interpretacija je: `(In.0) > (Out.0 ; Out.1)`. Shodno tome, njena entropija je utvrđena na `0`:

```plaintext
C = 1
E = log2(1)
E = 0 bits
```


### Efikasnost:

Treći indikator koji pruža Boltzmann kalkulator naziva se `Wallet Efficiency`. Ovaj indikator procenjuje efikasnost transakcije poredeći je sa optimalnom transakcijom zamislivom u identičnoj konfiguraciji.


Ovo nas vodi do rasprave o konceptu maksimalne entropije, koja odgovara najvećoj entropiji koju bi određena struktura transakcije teoretski mogla postići. Efikasnost transakcije se zatim izračunava suočavanjem ove maksimalne entropije sa stvarnom entropijom analizirane transakcije.


Formula koja se koristi je sledeća:

```plaintext
ER: stvarna entropija transakcije izražena u bitovima
EM: maksimalna moguća entropija za zadatu strukturu transakcije izražena u bitovima
Ef: efikasnost transakcije izražena u bitovima

Ef = ER - EM
```


Na primer, za Whirlpool coinjoin strukturu tipa 5x5, maksimalna entropija iznosi 10,5469:

```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```


Ovaj indikator je takođe izražen kao procenat, njegova formula je zatim:

```plaintext
CR: stvarni broj mogućih kombinacija
CM: maksimalan broj mogućih kombinacija sa istom strukturom
Ef:  efikasnost izražena u procentima

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```


Efikasnost od 100% ukazuje na to da transakcija u potpunosti koristi svoj potencijal za privatnost u okviru date strukture.


### Gustina entropije:

Četvrti indikator je gustina entropije, označen na alatu `Entropy Density`. On pruža perspektivu o entropiji u odnosu na svaki ulaz ili izlaz transakcije. Ovaj indikator je koristan za procenu i poređenje efikasnosti transakcija različitih veličina. Da biste ga izračunali, jednostavno podelite ukupnu entropiju transakcije sa ukupnim brojem uključenih ulaza i izlaza:

```plaintext
ED: gustina entropije izražena u bitovima
E: entropija transakcije izražena u bitovima
T: ukupan broj ulaza i izlaza u transakciji

ED = E / T
```


Uzmimo primer Whirlpool 5x5 CoinJoin:

```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```


Hajde da izračunamo i gustinu entropije za Whirlpool 8x8 CoinJoin:

```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```


### Boltzmann rezultat:

Peti deo informacija koje pruža Boltzmann kalkulator je tabela verovatnoća podudaranja između ulaza i izlaza. Ova tabela pokazuje, kroz Boltzmann rezultat, uslovnu verovatnoću da je određeni ulaz povezan sa datim izlazom.


To je, dakle, kvantitativna mera uslovne verovatnoće da se asocijacija između ulaza i izlaza u transakciji dogodi, na osnovu odnosa broja povoljnih pojava ovog događaja prema ukupnom broju mogućih pojava, u skupu interpretacija.


Uzimajući ponovo primer Whirlpool CoinJoin, tabela uslovnih verovatnoća bi istakla šanse za povezivanje između svakog ulaza i izlaza, pružajući kvantitativnu meru nejasnoće asocijacija u transakciji:


| %       | Izlaz 0  |  Izlaz 1 |  Izlaz 2 |  Izlaz 3 |  Izlaz 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Ulaz  0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Ulaz 1  | 34%      | 34%      | 34%      | 34%      | 34%      |
| Ulaz 2  | 34%      | 34%      | 34%      | 34%      | 34%      |
| Ulaz 3  | 34%      | 34%      | 34%      | 34%      | 34%      |
| Ulaz 4  | 34%      | 34%      | 34%      | 34%      | 34%      |

Ovde jasno možemo videti da svaki ulaz ima jednake šanse da bude povezan sa bilo kojim izlazom, što poboljšava poverljivost transakcije.

Izračunavanje Boltzmann-ovog rezultata uključuje deljenje broja interpretacija u kojima se određeni događaj dešava sa ukupnim brojem dostupnih interpretacija. Dakle, da bi se odredio rezultat koji povezuje ulaz br. 0 sa izlazom br. 3 (`512` interpretacija), koristi se sledeća procedura:

```plaintext
Interpretacije (IN.0 > OUT.3) = 512
Ukupan broj interpretacija = 1496
Rezultat = 512 / 1496 = 34%
```


Uzimajući primer Whirlpool 8x8 CoinJoin (ciklus naleta eng. surge cycle), Boltzmannova tabela bi izgledala ovako:


|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Međutim, u slučaju jednostavne transakcije sa jednim ulazom i dva izlaza, situacija je drugačija:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Ovde se primećuje da je verovatnoća da svaki izlaz potiče iz ulaza br. 0 `100%`. Niža verovatnoća stoga znači veću privatnost razblaživanjem direktnih veza između ulaza i izlaza.


### Determinističke veze:

Šesti podatak koji se pruža je broj determinističkih veza, dopunjen odnosom ovih veza. Ovaj pokazatelj otkriva koliko je veza između ulaza i izlaza u analiziranoj transakciji neosporna, sa verovatnoćom od `100%`. Odnos, s druge strane, nudi perspektivu o težini ovih determinističkih veza unutar celokupnog skupa veza transakcije.

Na primer, Whirlpool tip coinjoin transakcije nema determinističke veze, te zato pokazuje indikator i odnos od 0%. Suprotno tome, u našoj drugoj jednostavnoj transakciji koja je ispitana (sa jednim ulazom i dva izlaza), indikator je postavljen na `2` i odnos dostiže `100%`. Dakle, nulti indikator signalizira odličnu poverljivost zbog odsustva direktnih i neospornih veza između ulaza i izlaza.


**Spoljni resursi:**



- Boltzmann kod na Samourai
- [Bitcoin transakcije i privatnost (Deo I) od Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin transakcije i privatnost (Deo II) od Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin transakcije i privatnost (Deo III) od Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- KYCP Vebsajt
- [Medium članak o uvodu u boltzmann skriptu autora Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
