---
name: Braiins Pool

description: Uvod u Braiins Pool
---

![signup](assets/cover.webp)


Braiins Pool, formerly known as Slush Pool, je prvi Bitcoin Mining pool. Osnovan u novembru 2010, iskopao je svoj prvi blok 16. decembra 2010, blok 97834.


Od maja 2024. godine, Braiins Pool ima računarsku snagu od 13 EH/s, što predstavlja oko 1,8% od ukupnih Bitcoin Hashrate. Iskopao je ukupno 1.307.188 bitkoina, što je približno 6% od maksimalnih 21 milion bitkoina koji će ikada postojati.


### Sistem kompenzacije


Od kraja 2023. godine, Braiins Pool je promenio svoj sistem kompenzacije kako bi usvojio FPPS (Full Pay Per Share) sistem. To znači da rudari svakodnevno dobijaju nagrade za sav svoj rad od prethodnog dana, čak i ako bazen nije pronašao blok. Ovo se razlikuje od starog sistema gde su rudari dobijali nagradu samo kada bi bazen pronašao blok.


**Vredi napomenuti, [prema tvitu Mononauta](https://x.com/mononautical/status/1777686545715089605) koji analizira Bitcoin TimeChain, da mnogi Mining bazeni koristeći FPPS sistem šalju iskopane bitkoine na Address AntPool-a, što bi značilo da AntPool kontroliše Hashrate svih tih bazena, oko 47% globalnog Bitcoin Hashrate. Ovo su veoma loše vesti za decentralizaciju mreže.**


### Naknade za bazen


Naknade za Braiins Pool su 2.5%, međutim, ako koristite BraiinsOS na vašim mašinama, naknade će biti 0%


### Povlačenja


**Lightning Povlačenja**

Povlačenja putem Lightning-a omogućavaju vam da povučete svoje nagrade bez minimalnog iznosa jednom dnevno putem Lightning Address.

Da biste koristili ovu metodu, morate imati Wallet kompatibilan sa Lightning adresama.


**On-Chain Isplate**

Povlačenja On-Chain su ograničena na minimalni iznos i mogu biti podložna naknadama.

Minimalni iznos: 20,000 Sats

Naknade: 10,000 Sats za iznose manje od 500,000 Sats

Besplatno za iznose preko 500,000 Sats

Povlačenja se mogu pokrenuti vremenskim intervalom ili iznosom.


## Kreiranje Naloga


Da biste počeli koristiti Braiins Pool [idite na njihovu web stranicu](https://braiins.com/pool) i kliknite na "SIGN UP" u gornjem desnom uglu.



![signup](assets/3.webp)


Unesite svoje informacije i potvrdite, zatim ćete dobiti email sa zahtevom za potvrdu vašeg Address. Potvrdite putem linka u emailu koji ste primili i zatim se prijavite na platformu.


![signup](assets/4.webp)



## Dodavanje "radnika"

Radnik je Miner koji ćete povezati na bazen. Da biste dodali novi Miner, kliknite na "Workers" u levom bočnom meniju.

![signup](assets/7.webp)


Zatim kliknite na ljubičasto dugme "Connect Workers +".


U ovom prozoru izaberite svoju geografsku oblast.


Ako Miner koji želite da povežete koristi BraiinsOS, izaberite protokol "Stratum V2". U suprotnom, izaberite "Stratum V1".


![signup](assets/8.webp)


Imaćete informacije za unos na vašu Miner veb stranicu (pogledajte dokumentaciju vašeg Miner da biste znali gde da unesete ove informacije).


Ovde, **"stratum+tcp://eu.stratum.braiins.com:3333"** je URL bazena.


**JimZap.workerName** je vaš identifikator i ime vašeg Miner, gde je JimZap identifikator a .workerName je ime Miner. Ako imate više rudara, možete im dati isto ime, u kom slučaju će se njihova računarska snaga sabrati na kontrolnoj tabli, ili im dati različita imena kako biste ih pratili pojedinačno.


A lozinka je uvek ista **"anything123"**


Kada unesete ove informacije na veb stranicu vašeg Miner i pokrenete Mining, videćete da se pojavljuje nakon nekoliko minuta na Braiins Pool kontrolnoj tabli.


## Pregled kontrolne table


![signup](assets/9.webp)


U gornjem baneru možete videti prosečan ukupni Hashrate svih vaših rudara tokom 5 minuta, 1 sata i 24 sata. I sažetak broja rudara koji su online ili offline.

Ispod, grafikon vam omogućava da pratite evoluciju vaše računarske snage.


![signup](assets/10.webp)


Ispod ovog grafikona imate nekoliko informacija o vašim nagradama u Sats.


**"Današnje Mining Nagrade"** Označava broj Sats koje ste danas iskopali. Na kraju dana, ova vrednost će biti resetovana na 0 i Sats će biti poslati na vaš račun.


**"Jučešnja ukupna nagrada"** Broj Sats koji ste iskopali dan ranije


**"Proc. profitabilnost (1 TH/s)"** Je procena broja Sats koje zaradite u jednom danu za računarsku snagu od 1 TH/s. Na primer, ako je vrednost 77 Sats, a vi imate računarsku snagu od 10 TH/s kontinuirano tokom dana, tada biste teoretski zaradili 77 x 10 = 770 Sats dnevno.


**"All Time Reward"** Ukupno Sats koje ste iskopali sa Braiins Pool


**"Šema Nagrada"** Stopa naknade koju primenjuje bazen


**"Sledeća procena isplate"** Procena vremena koje će biti potrebno pre nego što budete mogli da povučete Sats sa platforme. Ovde procena ne pokazuje ništa jer je Mining tek započet pre nekoliko minuta.


**"Stanje na računu"** Broj Sats dostupnih na vašem računu, koji zatim možete podići.

## Postavljanje Isplata

Možete povući svoje nagrade ili On-Chain ili putem lightning sa Address.


Na vrhu, kliknite na "Funds". Podrazumevano, imate "Bitcoin Account". Možete kreirati druge kako biste delili nagrade. Vratićemo se na ovo u sledećem odeljku.


Za sada, kliknite na "Set up".


![signup](assets/17.webp)


U ovom novom prozoru, možete izabrati "Onchain payout".


Nazovite ovo Wallet, obezbedite BTC Address, i izaberite tip okidača koji želite. "Threshold" znači da će uplata biti pokrenuta kada akumulirate definisanu količinu BTC-a, a sa "Time interval", uplata će biti pokrenuta u redovnim intervalima (dan/nedelje/meseci).


Imajte na umu da je minimalni iznos 0.0002 BTC i da će ispod 0.005 BTC biti primenjena naknada od 0.0001 BTC.


![signup](assets/18.webp)


Ako želite da koristite Lightning isplate, biće vam potreban Wallet koji obezbeđuje Lightning Address. Na primer, možete koristiti getAlby.


Kliknite na vrh prozora na "Lightning payout".


Unesite svoj Lightning Address i označite polje "Razumem..." zatim potvrdite.


Sa ovom metodom povlačenja, vaše nagrade će biti poslate na vaš Wallet svaki dan.


![signup](assets/14.webp)


Kada potvrdite postavke isplate, dobićete e-poruku sa potvrdom.


![signup](assets/15.webp)


## Deljenje nagrada


Braiins Pool takođe vam omogućava da delite svoje nagrade na više novčanika.


Da biste to uradili, kliknite na vrhu na "Mining" zatim levo na "Settings".


![signup](assets/19.webp)


Na ovoj stranici, moći ćete da dodate drugi "Finansijski Račun" klikom na "Dodaj Drugi Finansijski Račun" i raspodelite svoje nagrade u % preko ovih različitih računa sa kojima morate povezati Wallet. Da biste povezali novi Wallet sa Finansijskim Računom, pogledajte prethodni odeljak.