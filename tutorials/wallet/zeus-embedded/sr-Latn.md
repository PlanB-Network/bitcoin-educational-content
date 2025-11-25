---
name: Zeus Embedded
description: Kako koristiti Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS je u početku mobilna aplikacija za daljinsko upravljanje čvorovima munje, omogućavajući vam da kontrolišete vaš čvor instaliran na udaljenom serveru


Ali aplikacija takođe ima funkciju "Embedded node".



**Ovo je aspekt aplikacije koji ćemo istraživati u ovom vodiču.** Ovo omogućava svakome da ima svoj sopstveni lightning čvor na mobilnom uređaju, bez potrebe za posvećenim serverom, na isti način kao što ACINQ nudi svoj neverovatan Wallet lightning Phoenix.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Podsećamo, Lightning je mreža koja radi paralelno sa Bitcoin, omogućavajući razmenu bitcoina bez potrebe za sistematskim sprovođenjem On-Chain transakcija. Rezultat su gotovo trenutne transakcije, bez potrebe za čekanjem od 10 minuta da se blok validira. Ovo je posebno korisno kada se plaća trgovcu u fizičkom svetu. Štaviše, Lightning pruža izuzetan nivo **poverljivosti** koji Bitcoin mreža nema u svojoj osnovi.*



**Zeus "Integrated "** je namenjen Bitkoin entuzijastima koji žele da maksimalno povećaju svoju privatnost i autonomiju.


Ukratko, to je **potencijalno** Wallet mobil iz snova cypherpunks-a. Čak i ako je još uvek u povojima (alfa verzija) i podložan nekim greškama, njegove karakteristike su brojne, i nema sumnje da će oduševiti najodvažnije među nama, koji žele maksimalnu kontrolu i opcionalnost.



S druge strane, mislim da trenutno nije pogodno za početnike koji nisu upoznati sa Bitcoin i jednostavno žele jednostavan način slanja/primanja satoshija. Iako se to može promeniti u budućnosti, jer se implementira funkcija čuvanja putem Cashu (chaumian Ecash) protokola za početnike...



## Instaliraj aplikaciju



Idite na [veb-sajt projekta](https://zeusln.com/) da preuzmete aplikaciju za operativni sistem vašeg pametnog telefona:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Kreiranje portfolija



Kada se aplikacija pokrene, kliknite na dugme "Quick Start" da biste započeli kreiranje Wallet.



![image](assets/fr/03.webp)





Pojaviće se niz ekrana za inicijalizaciju. Sačekajte nekoliko trenutaka, zatim sačekajte nekoliko minuta dok se čvor 100% ne sinhronizuje putem Neutrino.



Ovo može potrajati nekoliko minuta. Za informaciju, neutrino je način da mobilni novčanici pristupe informacijama Blockchain Bitcoin, bez potrebe za pokretanjem Full node.



![image](assets/fr/04.webp)





Nakon nekoliko trenutaka, spremni ste za polazak.



![image](assets/fr/05.webp)




## Postavljanje aplikacije



Spreman, pa ne baš sasvim, jer se podrazumeva da Zeus korisnik dostojan tog imena upravlja svojim Wallet sa klasom i stilom. Dakle, moraćemo da promenimo njegov avatar.



Kliknite na svoj avatar u gornjem desnom uglu ekrana:



![image](assets/fr/06.webp)





Kliknite na zupčanik, zatim na plus "+" :



![image](assets/fr/07.webp)





Odaberite najlepšu fotografiju Zevsa da predstavlja ovaj Wallet i kliknite na "CHOOSE PICTURE" na dnu ekrana, zatim se vratite klikom na strelicu u gornjem desnom uglu.



![image](assets/fr/08.webp)





Na kraju, dajte svom Wallet nadimak i kliknite na "SAVE Wallet CONFIG" da bi promena stupila na snagu. Na kraju, kliknite na strelicu nazad u gornjem levom uglu da se vratite na početni ekran.



![image](assets/fr/09.webp)





Ovog puta zaista možemo početi.



![image](assets/fr/10.webp)



### Biometrija



Da biste zaštitili pristup svom Wallet, možete dodati PIN/lozinku i aktivirati biometriju.



Da biste to uradili, idite na glavni meni Wallet klikom na horizontalne crte u gornjem levom uglu.



![image](assets/fr/11.webp)





Izaberite "Settings", zatim "Security" i na kraju "Set/Change PIN".



![image](assets/fr/12.webp)





Kreirajte svoj PIN, potvrdite ga i aktivirajte biometriju pritiskom na odgovarajuće dugme "Biometrija". Vratite se u glavni meni koristeći strelicu u gornjem levom uglu.



![image](assets/fr/13.webp)




### Sačuvaj Mnemonic frazu



Kada se vratite u glavni meni, kliknite na "Back up Wallet", zatim pročitajte upozorenje koje vas informiše da je gubitak 24 reči koje ćete dobiti jednak gubitku pristupa vašim sredstvima, i da svako ko ima te reči pored vas može pristupiti vašim sredstvima. Nikada ih ne dajte nikome.



Odaberite "RAZUMEM" na dnu ekrana. Zatim kliknite na svaku od 24 reči da ih prikažete i pažljivo zabeležite.



Možete to napisati na papir, ili možda, radi dodatne sigurnosti, ugravirati na nerđajući čelik kako biste ga zaštitili od požara, poplave ili urušavanja. Izbor medija za vaš Mnemonic zavisiće od vaše sigurnosne strategije, ali ako koristite Zeus kao portfelj troškova koji sadrži umerene iznose, papir bi trebao biti dovoljan.



Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Kada završite, kliknite na "I'VE BACKUP MY 24 WORDS" na dnu ekrana, i vraćamo se na početni ekran, spremni da primimo naše prve bitkoine.




## Opcija 1 - Primite On-Chain bitkoine i otvorite Lightning kanal



**Zeus Embedded** je prvenstveno dizajniran kao ugrađeni čvor za munje, ali se takođe može koristiti kao Wallet On-Chain.



Da biste primili On-Chain bitkoine, kliknite na dugme "On-Chain" i zatim na "Receive".


Na kraju, skenirajte QR kod ili kopirajte Bitcoin Address da biste položili sredstva.



![image](assets/fr/15.webp)





Jednom kada sredstva budu potvrđena i pripisana na vaš Wallet, možete ih koristiti za otvaranje **Lightning kanala**. Vaš Lightning kanal je vaša kapija ka Lightning Network, omogućavajući vam da Exchange bitkoine na mnogo poverljiviji i brži način.





- Da biste to uradili, kliknite na "MOVE On-Chain FUNDS TO LIGHTNING"



Na sledećem ekranu, od vas se traži da otvorite kanal u saradnji sa **"Olympus by Zeus "**, LSP (Lightning Service Provider) koji preferira Wallet.


Za ovaj vodič, izabraćemo ovu opciju radi jednostavnosti, ali je potpuno moguće otvoriti kanale sa bilo kojim čvorom na mreži.


Moguće je otvoriti nekoliko kanala u jednoj transakciji odabirom opcije "OPEN ADDITIONAL CHANNEL". *Ali ćemo to razmotriti u "naprednoj" verziji **Zeus Embedded** tutorijala.*





- Zatim odaberite iznos koji želite posvetiti ovom kanalu. U našem slučaju, sva naša On-Chain sredstva će biti iskorišćena, tako da aktiviramo dugme "Iskoristi sva moguća sredstva".





- Na kraju, izaberite dugme "OPEN CHANNEL" na dnu ekrana.



![image](assets/fr/16.webp)





U roku od nekoliko sekundi, kanal je uspostavljen i spremni smo da izvršimo naše prve Lightning transakcije. Na početnom ekranu, možemo videti mali sat pored našeg Wallet salda. To je zato što ćemo još uvek morati da sačekamo 3 On-Chain potvrde pre nego što kanal zaista postane funkcionalan.



![image](assets/fr/17.webp)





Nakon 3 potvrde, primećujemo da je naš saldo sada pripisan Lightning umetku.



![image](assets/fr/18.webp)



Mala tačka detalja: kada kliknemo na meni na dnu ekrana da bismo videli status naših lightning kanala, vidimo da mali deo našeg balansa nije dostupan za trošenje: možemo potrošiti samo 208253 satoshija umesto 210370 koje zapravo imamo. Ovo je normalno, jer je specifično za lightning protokol.



Konačno, treba napomenuti da naš partner Olympus zadržava pravo da zatvori kanal po sopstvenom nahođenju, ako se, na primer, ne koristi. Da bismo osigurali održavanje našeg kanala, moraćemo da platimo LSP-u (Lightning Service Provider), kao što ćemo videti u sledećem pasusu, kroz 2. način otvaranja kanala.





## Pošalji bitkoine putem Lightning-a



Sada kada smo pokrenuli naš kanal, hajde da vidimo kako ga možemo koristiti za plaćanje Invoice (Invoice) lightning.



Da biste to uradili, kliknite na dugme "Lightning", a zatim na "Send".



![image](assets/fr/19.webp)





Na sledećem ekranu, kopirajte svoj Invoice u predviđeno polje ili ga skenirajte klikom na ikonu u gornjem desnom uglu. Na kraju, prevucite dugme "Slide to Pay" udesno da platite.



![image](assets/fr/20.webp)






Sačekajte nekoliko sekundi i Invoice je isplaćen, a vaši satoshi su putovali brzinom svetlosti.



![image](assets/fr/21.webp)





Zeus vam zatim omogućava da dodate belešku kako biste označili vašu uplatu, ili da pregledate putanju koju su vaši satoshi prešli pre nego što su stigli na odredište (i naknade koje su naplatili svi međučvorovi). Ovo je vrsta funkcionalnosti koju volimo kod Wallet.



![image](assets/fr/22.webp)



Imajte na umu da za razliku od Wallet kao što je [Phoenix]([Plan ₿ Academy - Phoenix](https://planb.academy/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), sa Zeusom se ruta izračunava lokalno i nije delegirana trećoj strani (ACINQ u slučaju Phoenixa). Tako da ste vi jedini koji zna primaoca uplate. Gubimo malo na efikasnosti (uplate traju malo duže da se završe, ali dobijamo mnogo u smislu privatnosti).





Klikom na malu strelicu na dnu početnog ekrana, možete takođe pregledati našu istoriju plaćanja. Ovde vidimo u Green primljenih 212,121 Sats za On-Chain, zatim crvenom bojom označeno 211,756 Sats korišćenih za otvaranje našeg kanala, zatim 121,212 satoshija korišćenih za plaćanje našeg Invoice lightning-a.



![image](assets/fr/23.webp)





## Opcija 2 - Primite bitkoine direktno na Lightning



Umesto ručnog otvaranja kanala, kao što smo upravo videli, moguće je primiti sredstva direktno putem Lightning-a, čak i bez prethodno postojećeg kanala, koristeći Olympus, Zeus LSP.




- Da biste to uradili, kliknite na dugme "Lightning" na početnom ekranu, a zatim na "Receive".
- Zatim izaberite iznos koji želite da primite u polju "Amount" i odaberite dugme "CREATE Invoice" na dnu ekrana.



![image](assets/fr/24.webp)





Sledeći ekran prikazuje Invoice koji treba platiti da bi se primili satoshi. Rečeno nam je da će LSP zadržati 10.000 Sats ako se uplata izvrši putem Lightning-a. Kasnije ćemo videti kako se ove naknade za otvaranje kanala opravdavaju.



Platite Invoice ili neka neko drugi to plati, i kanal će biti automatski otvoren, ali uz odbijanje 10,000 Sats kako je dogovoreno.



![image](assets/fr/25.webp)





Sada smo na čelu 2 kanala munje, čiji status možete proveriti klikom na dugme označeno belom strelicom na dnu početnog ekrana.



Možemo videti da, za razliku od kanala otvorenog sa naše On-Chain skale, onaj otvoren direktno putem munje ne prikazuje upozorenje.


Kako ste platili za postavljanje ovog kanala, Pružalac usluga munje (LSP) se obavezuje da održava kanal 3 meseca i nudi vam "dolaznu likvidnost". Na donjem kanalu, možete videti da je kapacitet prijema 96383 satoshija. LSP je stoga vezao kapital kako bi vam omogućio da primate uplate direktno nakon otvaranja kanala.



Dakle, 10,000 Satoshi u plaćenim naknadama pokrivaju: trošak otvaranja kanala (Bitcoin On-Chain transakcija, garanciju za održavanje kanala tokom 3 meseca, i blokadu kapitala).



![image](assets/fr/26.webp)





Čestitamo, sada ste spremni da koristite Zeus Embedded, Wallet mobilni sistem osvetljenja sa najnaprednijim funkcijama na tržištu.





Da biste saznali više o tehničkom radu Lightning Network, možete pronaći odličnu besplatnu obuku Plan ₿ Academy od Fanisa Michalakisa:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb