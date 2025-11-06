---
name: JoinBot
description: Razumevanje i korišćenje JoinBot
---

![DALL·E – samurai robot in a red forest, 3D render](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai Wallet i zaplene njihovih servera 24. aprila, **usluga JoinBot više nije dostupna**. Od sada, nije moguće koristiti ovaj alat. Međutim, i dalje možete izvršiti Stonewall X2, ali morate pronaći saradnika i ručno Exchange PSBT-ove. Ova usluga može biti ponovo pokrenuta u narednim mesecima u zavisnosti od napretka slučaja.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

JoinBot je novi alat koji je dodat u Samourai Wallet paket sa najnovijim ažuriranjem 0.99.98f poznatog Bitcoin Wallet softvera. Omogućava vam da lako napravite kolaborativnu transakciju kako biste optimizovali svoju privatnost, bez potrebe da tražite partnera.


*Zahvaljujući izvrsnom Fanisu Mihalakisu za ideju korišćenja DALL-E za sličicu!*


## Šta je kolaborativna transakcija na Bitcoin?


Bitcoin je zasnovan na distribuiranom i transparentnom računu Ledger. Svako može pratiti transakcije korisnika ovog elektronskog sistema gotovine. Da bi se osigurao određeni nivo privatnosti, korisnici Bitcoin mogu obavljati transakcije sa specifičnom strukturom kako bi dodali uverljivu poricljivost u njihovom tumačenju.


Ideja nije direktno sakriti informacije, već ih pomešati među drugima. Ovaj cilj se koristi u Coinjoins, transakcijama koje prekidaju istoriju novčića na Bitcoin i čine njegovo praćenje složenim. Da bi se postigao ovaj rezultat, u transakciji se moraju kreirati višestruki ulazi i izlazi iste količine.


Ulazi su ulazi transakcije Bitcoin, a izlazi predstavljaju izlaze. Transakcija troši svoje ulaze kako bi stvorila nove izlaze promenom uslova trošenja novčića. Ovaj mehanizam omogućava da se bitkoini prenose između korisnika.

Ovo detaljno razmatram u ovom članku: Bitcoin Mehanizam Transakcije: UTXO, Ulazi i Izlazi.


Jedan od načina da se zamagle tragovi u Bitcoin transakciji je pravljenje kolaborativne transakcije. Kao što naziv sugeriše, to uključuje dogovor između više korisnika, od kojih svaki deponuje određenu sumu bitkoina kao ulaz u istoj transakciji i prima sumu kao izlaz.


Kao što je ranije pomenuto, najpoznatija struktura kolaborativne transakcije je CoinJoin. Na primer, na CoinJoin Whirlpool protokolu, transakcije uključuju 5 učesnika kao ulaze i izlaze, svaki sa istom količinom bitkoina.


![Diagram of a Coinjoin transaction on Whirlpool](assets/1.webp)


Spoljni posmatrač ove transakcije neće moći da zna koji izlaz pripada kojem korisniku kao ulaz. Ako uzmemo primer korisnika #4 (ljubičasta), možemo prepoznati njihov ulaz UTXO, ali nećemo znati koji od 5 izlaza je zapravo njihov. Početna informacija nije skrivena, već je pomešana unutar grupe.

Korisnik može da negira posedovanje određenog UTXO kao ishod. Ovaj fenomen se zove "uverljivo poricanje", i omogućava poverljivost u transparentnoj Bitcoin transakciji.


Da biste saznali više o CoinJoin, objašnjavam SVE u ovom dugom članku: Razumevanje i korišćenje CoinJoin na Bitcoin.


Iako veoma efikasan u prekidanju praćenja UTXO, CoinJoin nije pogodan za direktno trošenje. Naime, njegova struktura podrazumeva korišćenje ulaza unapred definisanog iznosa i izlaza iste vrednosti (modulo Mining naknade). Međutim, transakcija trošenja na Bitcoin je kritičan trenutak za privatnost jer često stvara fizičku vezu između korisnika i njihove On-Chain aktivnosti. Stoga se čini neophodnim koristiti alate za privatnost prilikom trošenja. Postoje i druge kolaborativne strukture transakcija posebno dizajnirane za stvarne platne transakcije.


## Transakcija StonewallX2


Među mnoštvom alata za trošenje koje nudi Samourai Wallet, nalazi se i kolaborativna transakcija StonewallX2. To je mini CoinJoin između dva korisnika dizajniran za plaćanje. Sa spoljašnje strane, ova transakcija može dovesti do nekoliko mogućih interpretacija. Tako pruža uverljivu poricljivost i, posledično, poverljivost za korisnika.


Ovo StonewallX2 kolaborativno podešavanje transakcija dostupno je na Samourai Wallet i Sparrow Wallet. Ovaj alat je interoperabilan između dva softvera.


Njegov mehanizam je prilično jednostavan za razumevanje. Evo kako funkcioniše u praksi:



- Korisnik želi da izvrši plaćanje u bitkoinima (na primer, kod trgovca).
- Oni preuzimaju prijemni Address stvarnog primaoca uplate (trgovca).
- Oni konstruiraju specifičnu transakciju sa više ulaza: najmanje jedan pripada njima i jedan pripada eksternom saradniku.
- Transakcija će imati 4 izlaza, uključujući 2 iste vrednosti: jedan ka trgovčevom Address za plaćanje, jedan kao kusur koji se vraća korisniku, jedan izlaz iste vrednosti kao plaćanje koji ide saradniku, i još jedan izlaz koji se takođe vraća saradniku.


Na primer, ovde je tipična StonewallX2 transakcija u kojoj sam izvršio uplatu od 50,125 Sats. Prvi ulaz od 102,588 Sats dolazi iz mog Samourai Wallet. Drugi ulaz od 104,255 Sats dolazi od mog saradnika Wallet:


![StonewallX2 transaction diagram](assets/2.webp)


Možemo posmatrati 4 izlaza, uključujući 2 iste količine da zbunimo tragove:



- `50,125 Sats` koji idu stvarnom primaocu moje uplate.
- `52,306 Sats` koje predstavljaju moju promenu i stoga povratak na Address u mom Wallet.
- `50,125 Sats` koji se vraća mom saradniku.
- `53,973 Sats` vraćam svom saradniku.


Na kraju operacije, saradnik će imati svoj početni saldo vraćen (minus Mining naknade), a korisnik će platiti trgovcu. Ovo dodaje značajnu količinu entropije transakciji i prekida neosporive veze između pošiljaoca i primaoca uplate.


Snaga StonewallX2 transakcije je u tome što potpuno suprotstavlja jedno od empirijskih pravila koje koriste analitičari lanaca: zajednički Ownership ulaza u transakciji sa više ulaza. Drugim rečima, u većini slučajeva, ako posmatramo Bitcoin transakciju sa više ulaza, možemo pretpostaviti da svi ovi ulazi pripadaju istoj osobi. Satoshi Nakamoto je već identifikovao ovaj problem za privatnost korisnika u svom Belom Papiru:


> Kao dodatni firewall, novi par ključeva mogao bi se koristiti za svaku transakciju kako bi se sprečilo njihovo povezivanje sa zajedničkim vlasnikom. Međutim, povezivanje je neizbežno kod transakcija sa više ulaza, koje nužno otkrivaju da su njihovi ulazi bili u vlasništvu istog vlasnika.

Ovo je jedno od mnogih empirijskih pravila korišćenih u On-Chain analizi za konstruisanje Address klastera. Da biste saznali više o ovim heuristikama, preporučujem čitanje ove serije od četiri članka od Samourai, koja sjajno uvodi temu.


Snaga StonewallX2 transakcije leži u činjenici da će spoljašnji posmatrač misliti da različiti ulazi transakcije pripadaju zajedničkom vlasniku. U stvarnosti, to su dva različita korisnika koji sarađuju. Analiza plaćanja je tako dovedena do obmane, a privatnost korisnika je očuvana.


Sa spoljašnje strane, StonewallX2 transakcija se ne može razlikovati od Stonewall transakcije. Jedina efektivna razlika između njih je ta što Stonewall nije kolaborativan. Koristi samo UTXO-e jednog korisnika. Međutim, u njihovim strukturama na nalogu Ledger, Stonewall i StonewallX2 su savršeno identični. Ovo omogućava još više mogućih interpretacija ove strukture transakcije jer spoljašnji posmatrač neće moći da utvrdi da li ulazi dolaze od iste osobe ili od dva saradnika.


Štaviše, prednost StonewallX2 u odnosu na Stowaway-tip PayJoin je ta što se može koristiti u bilo kojoj situaciji. Stvarni primalac uplate ne doprinosi nikakvim ulazima u transakciju. Tako se StonewallX2 može koristiti za plaćanje kod bilo kog trgovca koji prihvata Bitcoin, čak i ako trgovac ne koristi Samourai ili Sparrow.

S druge strane, glavna mana ove strukture transakcije je što zahteva saradnika koji je spreman da koristi svoje bitkoine kako bi učestvovao u vašem plaćanju. Ako imate Bitcoin prijatelje spremne da vam pomognu u bilo kojoj situaciji, ovo nije problem. Međutim, ako ne poznajete nijednog drugog Samourai Wallet korisnika, ili ako niko nije dostupan za saradnju, onda ste zaglavljeni.


Da bi rešili ovaj problem, tim Samourai je nedavno dodao novu funkciju svojoj aplikaciji: JoinBot.


## Šta je JoinBot?


Princip je JoinBot-a jednostavan. Ako ne možete pronaći nikoga za saradnju na StonewallX2 transakciji, možete sarađivati sa JoinBot-om. U praksi, zapravo ćete obavljati kolaborativnu transakciju direktno sa Samourai Wallet.


Ova usluga je veoma pogodna, posebno za početnike, jer je dostupna 24/7. Ako treba da izvršite hitnu uplatu i želite da uradite StonewallX2, više ne morate da kontaktirate prijatelja ili tražite saradnika na mreži. JoinBot će vam pomoći.


Još jedna prednost JoinBot-a je da su UTXO-i koje pruža kao ulaz isključivo iz postmix Whirlpool, što poboljšava privatnost vaše uplate. Pored toga, pošto je JoinBot uvek online, trebali biste sarađivati sa UTXO-ima koji imaju velike perspektivne Anonset-e.


Očigledno, JoinBot ima neke kompromise koje treba napomenuti:



- Kao kod klasičnog StonewallX2, vaš saradnik je nužno svestan korišćenih UTXO-a i njihove destinacije. U slučaju JoinBot-a, Samourai zna detalje ove transakcije. Ovo nije nužno loša stvar, ali treba imati na umu.
- Da bi izbegao spam, Samourai naplaćuje naknadu za uslugu od 3,5% na iznos stvarne transakcije, sa maksimalnim limitom od 0,01 BTC. Na primer, ako pošaljem stvarnu uplatu od 100 kilosata sa JoinBot-om, iznos naknade za uslugu će biti 3,500 Sats.
- Da biste koristili JoinBot, morate imati najmanje dva nepovezana i dostupna UTXO-a u vašem Wallet.
- U klasičnom StonewallX2, Mining naknade se dele jednako između dva saradnika. Sa JoinBot-om, očigledno ćete morati platiti pune Mining naknade.
- Da bi JoinBot transakcija bila potpuno ista kao klasična StonewallX2 ili Stonewall transakcija, plaćanje naknada za uslugu se vrši u potpuno odvojenoj transakciji. Povraćaj polovine Mining naknada koje je prvobitno platio Samourai biće izvršen tokom ove druge transakcije. Kako biste do kraja optimizovali svoju privatnost, poravnanje naknada se vrši korišćenjem Stowaway (PayJoin) strukturisane transakcije.


## Kako koristiti JoinBot?


Da biste izvršili JoinBot transakciju, morate imati Samourai Wallet. Možete ga preuzeti ovde, ili sa Google Playstore-a.


Za razliku od većine alata koje je razvio Samourai, Sparrow Wallet još nije najavio implementaciju JoinBot-a. Ovaj alat je stoga dostupan samo na Samourai.


Otkrijte korak po korak kako izvršiti StonewallX2 transakciju sa JoinBot-om u ovom videu:


![How to use Joinbot](https://youtu.be/80MoMz2Ne5g)


Evo dijagrama transakcije koji smo upravo izveli u videu:


![Diagram of my StonewallX2 transaction with JoinBot.](assets/3.webp)


Možemo videti 5 ulaza:



- 3 ulaza od 100 kilosata dolaze iz Samourai (JoinBot).
- 2 ulaza dolaze sa mog ličnog Wallet, od 3,524 Sats i 1.8 megasat.


4 izlaza transakcije su sledeća:



- 1 od 212,452 Sats stvarnom primaocu moje uplate.
- Još jedan u istoj količini koji se vraća na Samourai Address.
- 1 promena koja se takođe vraća Samourai za 87,302 Sats. Ovo predstavlja razliku između ukupnog iznosa njihovih ulaza (300,000 Sats) i izlaza za obfuscation (212,452 Sats) minus Mining naknade.
- 1 promena koja se vraća na drugi Address u mom Wallet. Predstavlja razliku između ukupnog iznosa mojih unosa i stvarne uplate, umanjeno za Mining naknade.


Kao podsetnik, Mining naknade ne predstavljaju izlaze transakcija. One jednostavno predstavljaju razliku između ukupnih ulaza i ukupnih izlaza.


## Zaključak


JoinBot je dodatni alat koji dodaje više izbora i slobode za korisnike Samouraia. Omogućava kolaborativnu StonewallX2 transakciju direktno sa Samouraijem kao saradnikom. Ova vrsta transakcije pomaže u poboljšanju privatnosti korisnika.


Ako možete izvesti klasični StonewallX2 sa prijateljem, i dalje preporučujem korišćenje ovog alata. Međutim, ako ste zaglavljeni i ne možete pronaći saradnike za izvršenje uplate, znajte da će JoinBot biti dostupan 24/7 za saradnju sa vama.


**Spoljni resursi:**


- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- Žao mi je, ne mogu da pomognem sa sadržajem sa te web stranice.