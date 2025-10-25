---
name: Remix - Whirlpool
description: Koliko remiksa treba uraditi na Whirlpool-u?
---
![cover remix- wp](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, Whirlpool Stats Tool više nije dostupan za preuzimanje, jer je bio hostovan na Samourai-ovom Gitlab-u. Čak i ako ste prethodno preuzeli ovaj alat lokalno na svoj računar, ili je bio instaliran na vašem RoninDojo čvoru, WST trenutno neće funkcionisati. Oslanjao se na podatke koje je pružao OXT.me za svoje funkcionisanje, a ovaj sajt više nije dostupan. Trenutno, WST nije naročito koristan jer je Whirlpool protokol neaktivan. Međutim, ostaje mogućnost da bi ovi softveri mogli biti vraćeni u narednim nedeljama. Štaviše, teorijski deo ovog članka ostaje relevantan za razumevanje principa i ciljeva coinjoin-a uopšte (ne samo Whirlpool-a), kao i za razumevanje efikasnosti Whirlpool modela. Takođe možete naučiti kako kvantifikovati privatnost koju pružaju CoinJoin ciklusi.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo upotrebu ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> *Prekinite vezu koju vaši novčići ostavljaju*

Ovo je pitanje koje mi često postavljaju. **Kada radite coinjoins sa Whirlpool-om, koliko remiksa treba uraditi da bi se postigli zadovoljavajući rezultati?**


Svrha CoinJoin-a je da ponudi uverljivu poricljivost mešanjem vašeg novčića sa grupom neprepoznatljivih novčića. Cilj ove akcije je da prekine veze praćenja, kako od prošlosti ka sadašnjosti, tako i od sadašnjosti ka prošlosti. Drugim rečima, analitičar koji zna vašu početnu transakciju na ulazu u CoinJoin cikluse ne bi trebalo da može definitivno da identifikuje vaš UTXO na izlazu iz ciklusa remiksa (analiza od ulaznih ciklusa do izlaznih ciklusa).

![past-present links diagram](assets/en/1.webp)


Nasuprot tome, analitičar koji zna vaš UTXO na izlazu iz CoinJoin ciklusa ne bi trebalo da bude u mogućnosti da odredi originalnu transakciju na ulazu u cikluse (analiza od izlaznih ciklusa ka ulaznim ciklusima).

![present-past links diagram](assets/en/2.webp)

Međutim, broj remiksa nije pouzdan kriterijum za procenu poteškoća sa kojima bi se analitičar suočio prilikom uspostavljanja veza između prošlosti i sadašnjosti, ili obrnuto. Relevantniji pokazatelj bi bila veličina grupa u kojima se vaš novčić skriva. Ovi pokazatelji se nazivaju "anonsetovi". U slučaju Whirlpool-a, postoje dve vrste anonsetova.


Prvo, možemo odrediti veličinu grupe gde je vaš UTXO skriven na izlazu iz ciklusa CoinJoin, tj. broj neodredivih novčića prisutnih unutar te grupe.

![probable UTXOs at exit](assets/en/3.webp)

Ovaj indikator, nazvan "prospective anonset" na francuskom, "forward anonset" na engleskom, ili "forward-looking metrics" (prevod na srpski bi bio "Metrike orijentisane na budućnost"), omogućava nam da procenimo otpornost vašeg novčića na analize koje prate put novčića od ulaza do izlaza iz CoinJoin ciklusa. Ova metrika procenjuje u kojoj meri je vaš UTXO zaštićen od pokušaja rekonstrukcije njegove istorije od ulazne tačke do izlazne tačke u CoinJoin procesu. Na primer, ako je vaša transakcija učestvovala u svom prvom CoinJoin ciklusu i dodatno su izvedena dva nizvodna ciklusa, prospective anonset vašeg novčića bi bio `13`:

![forward anonset](assets/en/4.webp)

Drugo, može se izračunati još jedan indikator za procenu otpornosti vašeg dela na analizu od sadašnjosti ka prošlosti. Poznavanjem vašeg UTXO na kraju ciklusa, ovaj indikator određuje broj potencijalnih Tx0 transakcija koje su mogle činiti vaš ulaz u CoinJoin ciklusima (analiza od kraja ka početku ciklusa). Ovaj indikator meri koliko je analitičaru teško da prati poreklo vašeg novčića nakon što je prošao kroz coinjoinse.![Verovatni izvori na ulazu](assets/en/5.webp)

Naziv ovog indikatora je "backward anonset" ili "backward-looking metrics" (u prevodu na srpski "Metrike orijentisane na prošlost"). Na francuskom, volim da ga zovem "anonset rétrospectif". Na dijagramu ispod, ovo odgovara svim narandžastim Tx0 mehurićima:

![backward anonset](assets/en/6.webp)

Da biste saznali više o metodi izračunavanja ovih indikatora, preporučujem da pročitate [moj Twitter niz](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) na ovu temu. Takođe pripremamo opširniji članak na PlanB mreži.


Svjestan sam da dati odgovor može izgledati nezadovoljavajuće jer ste se nadali specifičnom broju remiksa, a ja vas upućujem na dokumentaciju. Razlog za to je što je broj remiksa nepouzdan pokazatelj za procjenu anonimnosti stečene u CoinJoin ciklusima. Stoga nije moguće definirati fiksni broj remiksa kao apsolutni i univerzalni sigurnosni prag.


Istina je da svaki dodatni remiks vašeg dela povećava njegove anonimne skupove. Međutim, važno je razumeti da su prvenstveno remiksi koje izvode vaši vršnjaci ti koji doprinose rastu vašeg potencijalnog anonimnog skupa. Sa Whirlpool modelom, vaša transakcija može postići značajne nivoe potencijalnog anonimnog skupa sa samo dva ili tri CoinJoin ciklusa, isključivo kroz aktivnost vršnjaka uključenih u prethodne coinjoin-e.


S druge strane, retrospektivni anonset nije problem u našem slučaju. Zapravo, od vašeg početnog CoinJoin-a, imate koristi od nasleđa prethodnih transakcija u bazenu, što odmah daje vašem delu visok retrospektivni anonset, uz marginalno povećanje u svakom narednom ciklusu.

Takođe je važno razumeti da stvaranje uverljive poricljivosti nikada nije potpuno. Ono se oslanja na verovatnoću praćenja vašeg novčića. Ova verovatnoća opada kako se veličina grupa koje ga skrivaju povećava. Stoga bi trebalo da prilagodite svoje ciljeve u smislu anonsetova prema vašim ličnim očekivanjima. Zapitajte se o razlozima koji vas navode da koristite coinjoin-e i nivoima anonimnosti potrebnim za postizanje tih ciljeva. Na primer, ako je korišćenje coinjoin-a jednostavno usmereno na očuvanje privatnosti vašeg novčanika prilikom slanja nekoliko satošija vašem kumčetu za rođendan, veoma visoki nivoi anonimnosti nisu neophodni. Vaše kumče verovatno nije u stanju da izvrši dubinsku analizu lanca, a čak i da jeste, posledice po vaš život ne bi bile katastrofalne. Međutim, ako ste meta autoritarnog režima gde i najmanji komad informacija može rezultirati zatvorom, vaše akcije će morati biti vođene mnogo strožim kriterijumima.


Da biste odredili ove poznate anonset indikatore, možete koristiti Python alat pod nazivom **WST** (Whirlpool Stats Tool).


Međutim, nije uvek neophodno izračunavati anonsete svakog od vaših coinjoinovanih novčića. Sam dizajn Whirlpool-a već vam pruža garancije. Kao što je ranije pomenuto, retrospektivni anonset retko predstavlja problem. Od vašeg početnog mešanja, već dobijate posebno visok retrospektivni rezultat. Što se tiče prospektivnog anonseta, samo treba da držite svoj novčić na post-mix računu dovoljno dugo. Na primer, ovde su anonset rezultati jedne od mojih kovanica od `100,000 satošija` nakon što je provela dva meseca u coinjoin bazenu: 

![WST anonsets](assets/en/7.webp)

Prikazuje retrospektivni rezultat od `34,593` i perspektivni rezultat od `45,202`. U konkretnim terminima, ovo znači dve stvari:


- Ako analitičar zna moj novčić na kraju ciklusa i pokuša da prati njegovo poreklo, naići će na `34,593` potencijalnih izvora, od kojih svaki ima jednaku verovatnoću da bude moj.
- Ako analitičar zna moj novčić na početku ciklusa i pokuša da odredi njegovu korespondenciju na kraju, suočiće se sa `45,202` mogućih UTXO-a, od kojih svaki ima istu verovatnoću da bude moj.

Zato smatram da je upotreba Whirlpool-a posebno relevantna u strategiji `HODL -> Mix -> Spend -> Replace`. Po mom mišljenju, najlogičniji pristup je držati većinu svojih ušteda u bitkoinima u [hladnom novčaniku, eng. Cold Wallet](https://planb.network/resources/glossary/cold-wallet), dok se stalno održava određeni broj novčića u CoinJoin-i na Samourai za pokrivanje dnevnih troškova. Nakon što se bitkoini iz CoinJoin-a potroše, menjaju se novim kako bi se održao željeni nivo mešanih novčića. Ova metoda nam omogućava da se oslobodimo brige o anonsetima naših UTXO-a, dok vreme potrebno za coinjoin postaje mnogo manje restriktivno.


Nadam se da je ovaj odgovor rasvetlio Whirlpool model. Ako želite da saznate više o tome kako coinjoins funkcionišu na Bitcoin-u, preporučujem da pročitate moj obuhvatan članak na ovu temu:




**Spoljni resursi:**


- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://estudiobitcoin.com/como-instalar-y-utilizar-whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/
- https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7.

