---
name: JoinMarket

description: Vodič i uputstvo kako koristiti JoinMarket za CoinJoin preko Bitcoin putem komandne linije
---

![cover](assets/cover.webp)



---

Ako ste pronašli ovu stranicu pretraživanjem interneta za "JoinTmarket", imate moju iskrenu zahvalnost. Međutim, naišli ste na vodič koji se bavi potpuno drugačijom, ali izuzetno zanimljivom temom! 🚬🍁



Cilj ovog tutorijala je da ilustruje teorijski i praktični rad JoinMarket-a, putem komandne linije. 🐢 💚



## JoinMarket Teorijska Definicija



Možemo definisati JoinMarket kao alat, ili Wallet, koji omogućava CoinJoin sa drugim korisnicima na potpuno Trustless način i bez ikakvog centralnog koordinatora.



Pošto je ceo teorijski deo ovog alata izuzetno širok, odlučio sam da ga Address u specifičnoj epizodi mog podkasta. Za one koji razumeju italijanski, toplo preporučujem da nastavite sa čitanjem nakon slušanja epizode, kako biste bolje usvojili osnovne koncepte za pravilno korišćenje ovog programa.



Možete nadoknaditi epizodu na ovim direktnim linkovima:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (ovde možete slušati direktno iz pregledača).
- [Antenna pod](https://antennapod.org/) je besplatan i otvorenog koda menadžer za podkaste koji ne zahteva registraciju. Da biste pronašli epizodu, preuzmite aplikaciju, ručno dodajte moj podkast lepljenjem [ovog linka](https://Anchor.fm/s/bd5d5b20/podcast/rss) u odeljak _feed rss_, zatim potražite epizodu posvećenu JoinMarket-u.



## Instalacija



Operativni sistemi:





- Raspiblitz
- Umbrel
- MyNode
- Raspibolt



## Konfiguracione Datoteke



JoinMarket je prilagodljiv softver sa beskonačnim brojem podešavanja; ova podešavanja su specificirana u konfiguracionoj datoteci koja se nalazi u glavnom direktorijumu programa pod nazivom `Joinmarket.cfg`.



U ovom odeljku ćemo pregledati neka polja koja bi vam mogla biti zanimljiva za istraživanje i/ili modifikaciju, u zavisnosti od vaših potreba. Želeo bih da naglasim da su sve promene navedene u nastavku korisne za poznavanje kako bi se rad softvera prilagodio ličnim potrebama, ali nisu obavezne.



Prvo idemo u folder `joinmarket/scripts` i pokrenimo komandu:



```bash
python wallet-tool.py generate
```


U ovom trenutku bismo trebali dobiti grešku, ali to će uzrokovati da softver generate unapred postavljenu datoteku sa podešavanjima za nas. Možemo otići i urediti datoteku sa podešavanjima iz terminala sa:



```bash
nano joinmarket.cfg
```



ili:



```bash
vim joinmarket.cfg
```



jednom kada otvorimo, primetićemo brojne linije sa različitim podešavanjima i njihovim objašnjenjima na engleskom jeziku. Konkretno, analiziraćemo ispod najzanimljivije varijable:





- `merge_algorithm` u slučaju da radimo kao kreator, ovo polje podešava koliko agresivno će softver konsolidovati nepotrošene Izlaze. U slučaju da imamo mnogo UTXO-a za konsolidaciju, može imati smisla prebaciti se sa _postepenog_ na _pohlepni_
- `tx_fees` podešava kao taker naknade sa kojima se plaća transakcija, veoma je korisno promeniti ovo podešavanje u slučaju da često koristite tumbler (o tome ćemo kasnije govoriti) jer ako dođe do skoka u naknadama tokom izvršenja istog, ako ne postavimo ovo polje ispravno, rizikujemo da potrošimo mnogo Sats za CoinJoin. Postavljanjem vrednosti u hiljadama (kao što je 2000) ovo će biti jednako 2 Sats/vBytes, 3500 za 3.5 Sats/vBytes, i tako dalje. Preporučio bih broj u rasponu od 1500 do 6000 u zavisnosti od vaših potreba.
- `max_cj_fee_abs` se koristi da se odredi koliko smo spremni da platimo u apsolutnim iznosima za proizvođače koje izaberemo tokom CoinJoin. Podrazumevano, ovo polje za proizvođače je 200 Sats, dobra opcija bi mogla biti broj u rasponu od 200 do 1000 Sats po partneru (ovo se zasniva na tome koliko želite da potrošite i koliko anon-set tražite za vaše CoinJoin-e)
- `max_cj_fee_rel` ima istu funkciju kao i polje iznad, ali specificira relativne naknade (procenat) koje smo spremni da platimo svakoj drugoj strani. Pošto je ovo vrednost u `procentima`, budite pažljivi da ne postavite visoke vrednosti kako biste izbegli visoke troškove u CoinJoins sa velikim iznosima. Podrazumevana vrednost za kreatore je _0.00002_, preporučujem sličnu ili malo višu vrednost.
- `minimum_makers` je polje koje određuje sa koliko drugih suprotnih strana radimo CoinJoin, po defaultu joinMarket uvek bira od 4 do 9 suprotnih strana, ako želimo, za veću privatnost, možemo povećati ovu vrednost na 5 ili 6 (to će ipak učiniti transakcije skupljim).
- `cjfee_a` specificira, u slučaju da delujemo kao maker, koliko Sats u apsolutnim terminima želimo da prikupimo za iznajmljivanje naše likvidnosti. Ovo polje je potpuno subjektivno, podrazumevana vrednost je već veoma dobra (tako ćemo imati bolju privatnost kao maker) možemo razmotriti da ga postavimo na 0 ako želimo da napravimo više CoinJoin za manje vremena.
- `cjfee_r` isto kao gore navedeno polje, ali u procentima, a ne apsolutno. Opet preporučujem da ostavite podrazumevanu vrednost ili je smanjite kako biste privukli više korisnika.
- `ordertype` sa ovim poljem biramo od proizvođača da li da naplati apsolutno (absoffer) ili procentualno (reloffer). Obično primaoci preferiraju apsolutne ponude zbog ekonomskih razloga.
- `minsize` ako ne želimo da UTXO bude previše mali kao proizvođači, možemo odrediti minimalni CoinJoin za učešće. Ovo polje je izraženo u Satoshi i potpuno je subjektivno. Možemo ostaviti ovo polje na 0 ili povećati na 500000 (Sats), 1000000 (Sats), i tako dalje.



Budite veoma pažljivi da ne menjate pogrešna polja, neka od varijabli u joinmarket.cfg fajlu ako su pogrešno postavljena mogu ugroziti funkcionalnost softvera ili potpuno uništiti vašu privatnost, oči širom otvorene i maksimalan oprez!



## Postavka Radnog Okruženja



Neki čvorovi automatski postavljaju ispravne vrednosti za ova polja unutar joinmarket.cfg datoteke. Preporučujem da ručno ponovo proverite:





- `rpc_user = yourusername-as-in-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #podrazumevano obično ispravno`
- `rpc_port = 8332 # default za Mainnet`



U ovom trenutku možemo nastaviti sa kreiranjem našeg Wallet unutar JoinMarket:



```bash
python wallet-tool.py generate
```



Ova komanda će nas uvesti u unos lozinke kojom ćemo šifrovati Wallet i ime koje želimo da mu damo, kada vas pita da li želite da podržite fidelity bonds preporučujem korišćenje opcije _yes_, izlaz koji će biti vraćen izgledaće ovako:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


u slučaju da se pojavi greška, najverovatnije smo pogrešno postavili 4 RPC polja navedena iznad. U slučaju da može pomoći, pratite [ovaj vodič](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) koji se nalazi u originalnoj JoinMarket dokumentaciji.



Postavili smo radno okruženje i možemo početi istraživati komande koje će nam biti najkorisnije. Svi skripti o kojima ćemo diskutovati mogu se pokrenuti u konzoli sa dodatkom `--help` za detaljno objašnjenje.



Sada možemo pokušati da pokrenemo:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



ova komanda će vam prikazati sve različite Wallet dubine mešanja sa različitim adresama kategorizovanim kao:




- Novo (Address nikad korišćen)
- Zamena (ostatak prethodne transakcije)
- Cj-out (izlaz iz CoinJoin)



evo praktičan primer rezultata:



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


Sada možemo nastaviti sa deponovanjem naših prvih Satošija na jednu ili više adresa, sećajući se da bez obzira na to da li smo maker ili taker, softver nikada neće direktno konsolidovati UTXO u različite mixdepth-ove, na ovaj način možemo držati Satse sa različitim nivoima privatnosti odvojeno unutar Wallet.



## Slanje Bitcoin sa CoinJoin Single



Sada možemo premestiti naše Satošije. Jedna od glavnih komandi u ovom softveru je skripta:



```bash
pyhton sendpayment.py
```


što će nam omogućiti slanje transakcija na druge adrese sa ili bez CoinJoin. Hajde da pređemo na to kako funkcioniše i neke praktične primere. Podrazumevano formatiranje komande je (zapamtite da zamenite tekst obuhvaćen simbolima < i >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



osnovni primer upotrebe može biti:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


u ovom slučaju ćemo poslati na Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc tj. 5000000 Satoshi iz našeg mixdepth 0 (podrazumevani) tako što ćemo izabrati od 4 do 9 suprotnih strana za CoinJoin (podrazumevana opcija).



Da bismo imali veću kontrolu nad time kako i koje UTXO-e trošiti, možemo pregledati dodatne opcije za ovu komandu:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


u ovom primeru dodali smo dve specifikacije: -N označava sa koliko ćemo se protivstrana mešati, -m dubinu mešanja iz koje ćemo povući sredstva. U stvari, poslali smo 100,000,000 Sats (1 btc) na Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c sa sredstvima u dubini mešanja 1 i mešanjem sa 5 protivstrana.



Ako stavimo 0 kao vrednost slanja specificirajući mixdepth, joinMarket će izvršiti takozvani `sweep`, to jest, poslaće sva sredstva u tom mixdepth-u konsolidujući ih međusobno:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



ovde smo poslali sva sredstva iz mixdepth 0 (mogli smo da ga ne navedemo jer je to podrazumevano) mešajući sa 7 suprotnih strana.



Komanda sendpayment koristi se za prebacivanje sredstava iz joinMarket-a na eksterni Wallet ili za slanje Satoshi osobi dodavanjem Layer nivoa privatnosti između nas i njega. Da bismo postigli dovoljan nivo privatnosti na našim UTXO-ima, prikladnije je koristiti komandu tumbler.py koju ćemo objasniti kasnije u ovom vodiču.



## Biti Maker



Skripta koju ćemo obraditi u ovom delu je:



```bash
yg-privacyenhanced.py
```



Ovaj program se koristi za delovanje kao maker u joinMarket-u. Softver će se povezati sa našim Bitcoin čvorom i sa internim tržištem platforme na kojoj se maker-i predstavljaju kao ponuđači likvidnosti, a takeri traže protivstrane. U slučaju da želite koristiti fiducijarnu obveznicu, možete je kreirati sa ovim formatiranjem:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



na primer:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



izlaz koji će nam biti vraćen biće Bitcoin Address (tj. onaj na koji ćete morati da položite sredstva koja želite da dodelite vernosti).



**Upozorenje**: Postoje dve stvari na koje treba obratiti posebnu pažnju ako planirate da kreirate Fidelity Bond (poznat i kao FB);





- jednom kada sredstva budu uložena, ne mogu se ponovo premestiti dok ne isteknu. Obratite pažnju na to koliko Satss šaljete na Address i kako formatirate datum. Greške nisu dozvoljene!
- Fidelity bond je lako prepoznatljiv na lancu, pa je preporučljivo deponovati sredstva putem CoinJoin i sa poreklom koje nije povezano sa vašim identitetom. Isto je preporučljivo uraditi kada želite da premestite istekli fidelity bond iz JoinMarket-a.



Važno je zapamtiti da je moguće ponovo napuniti fiducijarni bond samo jednom transakcijom, u slučaju UTXO višestrukih samo će najveći biti smatran validnim za FB.



Sada ćemo se pozabaviti skriptom pomenutim na početku ovog pasusa, kada smo kreirali fiducijarni bond (koji je, podsećamo, opcionalan) spremni smo da pokrenemo izvršni fajl kako bismo delovali kao maker na joinMarket-u. Kada su Satss deponovani na različite adrese i mixdepth možemo pokrenuti komandu:



```bash
python yg-privacyenhanced.py <wallet name>
```



Od ovog trenutka (nakon nekoliko minuta povezivanja na mrežu) i dok ne zaustavimo skriptu, naš JoinMarket klijent će se pojaviti na listi aktivnih makera na protokolu i ponuditi našu likvidnost raznim suprotnim stranama za pravljenje CoinJoin. Ne očekujte desetine CoinJoin-ova dnevno (osim ako nemate ogromnu fiducijarnost i veliku likvidnost deponovanu na Wallet), takođe zapamtite da faktori kao što su potrebne naknade i deponovani Satoshiji utiču na to koliko često ćete biti maker.



Pokretanjem komande ispod moći ćete da vidite istoriju svih transakcija napravljenih na Wallet i bilo koji dobitak (ako ste kreator) ili trošak naknade (ako ste primalac) koji ste imali tokom trajanja Wallet.



```bash
python wallet-tool.py <wallet name> history
```



Jednom kada vaši Satoshiji naprave CoinJoins, oni će se kretati iz mixdepth-a u mixdepth dok ne stignu do poslednjeg. Kada prođu četvrti, vratiće se u mixdepth 0, na vama je koliko privatnosti želite pre nego što ih premestite na Cold Wallet, preporučljivo je završiti ceo Wallet ciklus.



## Tumbler



Evo nas konačno na najsočnijem delu JoinMarket-a, tumbleru! Ako ste slušali podcast, već znate o čemu se radi. Jedna preporuka pre nego što počnemo: **Pazite na naknade!** Ne zaboravite da postavite limite u joinmarket.cfg fajlu (kao što je objašnjeno na početku) i razmislite o pokretanju programa samo kada su onchain naknade relativno niske (ispod 10 Sats/vB).



Da biste pokrenuli tumbler, potrebno je zaustaviti skriptu iz maker-a (ako je bila aktivna), nakon toga možemo pokrenuti komandu:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Neophodno je uneti **najmanje** 3 izlazne adrese za tumbler: ovo je da bi se osigurala dobra privatnost i da se ne bi stvorile očigledne veze između UTXO-a tokom procesa. Kao i obično, dodavanjem `--help` komandi možete videti sve dodatne detalje. Hajde da pogledamo složeniji primer sa naprednim pravilima:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



U ovom slučaju pokrenuli smo skriptu za tumbler koja neće koristiti podrazumevani broj partnera (parametar -N označava da zahtevamo 7 partnera sa maksimalnom varijansom od 2, tako da je nasumičan broj kreatora od 5 do 9) i sa većim brojem CoinJoin po mixdepth-u (po defaultu ova skripta pravi nasumičan broj CoinJoin po sekciji Wallet u rasponu od 1 do 3, koristeći komandu -c 3 1 umesto toga će biti od 2 DO 4). Na ovaj način ćemo potrošiti više Sats na naknade, ali ćemo imati veći set anonimnosti.



Možete dodati onoliko izlaznih adresa koliko želite (minimum 3, nema maksimalnog broja osim zdravog razuma). Međutim, nije moguće, zbog problema privatnosti, odlučiti kako će Satoshi biti raspoređen među adresama navedenim kao izlaz.



Tumbler je namerno dugotrajan proces, povremeno se može desiti da nešto prestane da radi, u većini slučajeva ovo će se rešiti samo od sebe u roku od nekoliko sati. U slučaju potpunog pada možemo pokušati da ga ponovo pokrenemo komandom:



```bash
python tumbler.py --restart
```



Ili jednostavno ponovo pokrenite novu komandu za mešanje. Ovo neće pokrenuti zakazivanje prethodnog mešača, već će pokrenuti novi ciklus mešanja. U slučaju da zatvaranje SSH terminala ka vašem čvoru takođe zaustavi skriptu, možete iskoristiti program `TMUX` koji se može instalirati komandom:



```bash
sudo apt install tmux
```



Pokretanjem iz ljuske kucanjem `tmux` otvoriće vam terminal koji će ostati aktivan u pozadini čak i ako zatvorite udaljenu vezu. Kada se ponovo povežete na vaš čvor sa komandom: `tmux attach` ponovo ćete otvoriti ljusku koja je ostala aktivna u pozadini.



## Zaključak



JoinMarket je beskonačan i prilagodljiv softver. U ovom vodiču smo otkrili glavne funkcije kako bi bilo moguće da ga bilo ko koristi (ili sam barem pokušao, shvatam da korišćenje ovog softvera nije jednostavno). Jedan od najvećih problema sa JoinMarket-om je upravo to: broj ljudi koji ga koriste i koji su tvorci. Ako malo korisnika koristi ovaj softver, ukupna privatnost (anon-set) je smanjena. Zato se nadam da će ovaj vodič podstaći korišćenje i ubediti vas da preuzmete i instalirate moj omiljeni softver za pravljenje CoinJoin. U slučaju da želite da se još dublje upustite u neke aspekte, preporučujem da pročitate razne detaljne dokumente na github-u, oni su stvarno dobro urađeni i možete ih pronaći ovde.



Srećno mešanje kornjača!🐢 💚



[Ovde](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) možete podržati Turtlecute