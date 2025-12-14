---
name: LN Markets
description: Bitcoin platforma za trgovanje na Lightning Network
---

![cover](assets/cover.webp)



LN Markets je prva prava Lightning-native Bitcoin platforma za trgovanje, koja vam omogućava da trgujete sa leveridžovanim Bitcoin derivatima direktno sa vašeg wallet Lightning-a, bez KYC-a, sa trenutnim poravnanjem i minimalnim starateljstvom. Pokrenuta 2020. godine, eliminiše trenja tradicionalnih berzi: nema verifikacije identiteta, nema blokiranih depozita, nema čekanja na potvrde blockchain-a. Vaš wallet Lightning postaje vaš trgovački račun.



## Šta je LN Markets?



LN Markets nudi **Futures** (perpetualne ugovore sa leverage-om do 100×) i **Options** (Call/Put sa rizikom ograničenim na plaćenu premiju). Platforma funkcioniše kao sloj za agregaciju likvidnosti koji konsoliduje više trgovačkih mesta za optimalno izvršenje bez proklizavanja. Vaša sredstva su zaključana samo za tačno trajanje vaših aktivnih pozicija, a ne danima ili nedeljama kao kod tradicionalnog skrbničkog računa.



### Dostupni proizvodi za trgovanje



**Futures (Perpetualni ugovori)**



Perpetualni ugovori su fjučersi bez datuma isteka, omogućavajući vam da spekulišete o cenovnom trendu Bitcoin sa leveridžom. LN Markets nudi dva režima upravljanja marginom:



**Izolovani režim**: Svaka pozicija ima svoju posvećenu marginu. Samo sredstva dodeljena ovoj specifičnoj poziciji su u riziku. Ako pozicija dostigne cenu likvidacije, **samo ova pozicija je likvidirana**, vaše druge pozicije i preostali saldo nisu pogođeni. Idealno za strogo ograničavanje rizika po trgovini.



**Cross Mode (Cross Margin)** : Marža se deli između svih vaših otvorenih pozicija. Vaš ukupni saldo na računu služi kao kolateral za sve vaše pozicije. Ako neka pozicija krene loše, sistem koristi vaš celokupni raspoloživi saldo kako bi izbegao likvidaciju. **Rizik**: ako vaš ukupni saldo nestane, sve vaše pozicije mogu biti likvidirane istovremeno. Preporučuje se samo iskusnim trgovcima koji žele da maksimiziraju efikasnost kapitala.



**Upravljanje pozicijama** :





- Long pozicija**: kladite se na rast BTC/USD. Ako cena poraste, dobijate; ako padne, gubite. **Primer**: Bitcoin na $100,000, otvarate Long sa 10,000 sats i 10× polugom. Ako Bitcoin poraste na $105,000 (+5%), vaša pozicija dobija 50% (5% × 10), tj. ~5,000 sats profita. Ako Bitcoin padne na $95,000 (-5%), gubite 50%, tj. gubitak od ~5,000 sats.





- Kratka pozicija**: kladite se na pad BTC/USD. Ako cena padne, dobijate; ako poraste, gubite. **Primer**: Bitcoin na $100,000, otvarate kratku poziciju sa 10,000 sats i 10× polugom. Ako Bitcoin padne na $95,000 (-5%), dobijate 50%, tj. ~5,000 sats. Ako Bitcoin poraste na $105,000 (+5%), gubite 50%.



Leverage (do 100×) proporcionalno pojačava dobitke i gubitke. Mehanizam **stope finansiranja** (periodične naknade svakih 8 sati) balansira duge i kratke pozicije. Možete upravljati sa do 100 fjučers pozicija istovremeno.



**Opcije**



Opcija je kao **lutrijska karta sa datumom isteka**. Plaćate premiju da biste se kladili na pravac cene Bitcoin. **Glavna prednost**: nikada ne možete izgubiti više od plaćene premije, likvidacija nije moguća.





- Call opcija (bikovska opklada)**: Kladite se da će Bitcoin porasti iznad udarne cene pre isteka. Pobeđujete ako cena poraste, gubitak je ograničen na premiju ako cena padne.





- Put opcija (medveđa opklada)**: Kladite se da će Bitcoin pasti ispod udarne cene. Dobijate ako cena padne, gubitak je ograničen na premiju ako cena poraste.





- Straddle (opklada na volatilnost)**: Kupujete Call I Put istovremeno. Dobijate ako Bitcoin napravi veliki pomak u bilo kom pravcu, gubite obe premije ako cena ostane stabilna.



Ograničenje: 50 istovremenih pozicija. Idealno za početak trgovanja s polugom bez straha od likvidacije.



**sats ↔ sUSD**: Trenutno konvertujte svoje satoshije u sintetičke dolare (sUSD) kako biste se zaštitili od volatilnosti, ili obrnuto da biste povratili izloženost Bitcoin.



## Pristup platformi i kreiranje naloga



### Idi na LN Markets



Idite na [lnmarkets.com](https://lnmarkets.com) i kliknite na "Open App".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Kreiraj svoj nalog



Ekran dobrodošlice nudi nekoliko metoda povezivanja:



![Méthodes de connexion](assets/fr/02.webp)



**Opcije dostupne** :


1. **Registrujte se sa Lightning wallet** (preporučeno) : LNURL-auth sa Phoenix, Breez, Zeus ili BlueWallet


2. **Registrujte se putem e-pošte**: klasični nalog (ograničava Lightning iskustvo)


3. **Alby** ili **Ledger**: ekstenzije za pregledač



### Povezivanje putem Lightning-a (LNURL-auth)



Kliknite na "Registrujte se sa Lightning wallet". Skenirajte QR kod sa vašim wallet Lightning :



![QR code LNURL-auth](assets/fr/03.webp)



Vaš wallet automatski potpisuje kriptografski zahtev i vaš nalog se kreira trenutno, bez emaila ili lozinke. Snažna sigurnost i potpuna anonimnost.



### Početna konfiguracija



![Configuration post-connexion](assets/fr/04.webp)



**Dostupni parametri** :




- Korisničko ime**: personalizujte svoje korisničko ime
- Automatska povlačenja**: aktivirajte automatska povlačenja na vaš wallet nakon zatvaranja trgovine
- Dvofaktorska autentifikacija**: poboljšana sigurnost sa 2FA
- Dokumentacija**: pristupite zvaničnim resursima



## Interface turneja



LN Markets interfejs je organizovan u nekoliko sekcija dostupnih iz bočnog menija:



### Kontrolna tabla



![Dashboard](assets/fr/06.webp)



Prikazuje vašu izvedbu po tipu proizvoda (Futures Cross, Futures Isolated, Options) sa P&L, trgovanim volumenima i vašim ličnim Address Lightning (npr. `pivi@lnmarkets.com`).



### Profil



![Profil trader](assets/fr/07.webp)



Detaljna statistika: broj trgovina, tip trgovca (SCALPER, itd.), medijana trajanja pozicije, raspodela Long/Short, procenat uspešnosti, proseci (količina, margina, leverage), i progresivna struktura naknada prema obimu.



### Trgovine



![Historique des trades](assets/fr/08.webp)



Kartica Trgovine prikazuje kompletnu istoriju vaših pozicija, sa svim važnim metrima: datum kreiranja, pravac (Duga/Kratka), veličina pozicije (količina), angažovana margina, ulazna i izlazna cena, ostvareni profit/gubitak (P&L) i troškovi trgovanja. Možete filtrirati po tipu proizvoda (fjučersi/opcije) i izvesti vaše podatke za eksternu analizu ili računovodstvo.



### Postavke



![Paramètres de la plateforme](assets/fr/05.webp)



Kartica Podešavanja nudi dve kartice: **Account** i **Interface**.



**Nalog** kartica:



Upravljanje nalogom sa poljima koja se mogu uređivati :




- Korisničko ime**: promenite svoje korisničko ime (npr. "pivi") pomoću dugmeta "Ažuriraj"
- Email**: dodaj/uredi svoju email adresu
- Depozitna bitcoin adresa**: bitcoin adresa koju možete koristiti za uplatu on-chain sredstava.



**Tri prekidača konfiguracije** :




- Pojavi se na tabelama lidera**: izaberi da li želiš da se pojaviš na javnim tabelama lidera
- Koristite Taproot adrese**: koristite Bitcoin adrese Taproot za on-chain depozite/isplate
- Omogući automatska povlačenja**: aktiviraj automatska povlačenja na svoj wallet Lightning nakon zatvaranja trgovine



**Migracija naloga**: Sekcija koja vam omogućava da migrirate vaš Lightning nalog na klasičnu autentifikaciju putem email-a/lozinke.



**Session upravljanje**: Dugme "Obriši sesiju i lokalne podatke" za prekid veze i čišćenje lokalnih podataka pretraživača.



**Interface** kartica:



Prilagodite korisničko iskustvo sa sedam prekidača:




- Preskoči potvrdu narudžbine**: deaktiviraj modal za potvrdu pre izvršenja trgovine (brzo trgovanje)
- Prikaži opise alata**: prikaži opise alata kada se zadrži pokazivač iznad elemenata
- Privatni režim (maskira osetljive podatke)**: maskira iznose i osetljive podatke u interfejsu (režim privatnosti)
- Prikaži neto PL u profilu**: prikaži neto profit/gubitak u vašem javnom profilu
- Koristite ikone jedinica**: prikažite ikone za valute (sats, $)
- Omogući zvučna obaveštenja**: aktiviraj zvučna obaveštenja za trgovačke događaje
- Omogući obaveštenja na radnoj površini**: aktiviraj obaveštenja operativnog sistema na radnoj površini



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin i sintetički USD salda sa istorijom depozita, povlačenja, međusobnih transfera, zamena, finansiranja i upravljanja adresama on chain.



### API



![API V3](assets/fr/10.webp)



LN Markets nudi kompletan API REST (V2 i V3) za potpunu automatizaciju vašeg trgovanja putem skripti ili botova. Možete kreirati API ključeve sa prilagodljivim dozvolama (samo za čitanje, trgovanje, povlačenja) direktno iz interfejsa. Zvanični TypeScript i Python SDK-ovi su dostupni za laku integraciju. Kompletna API V3 dokumentacija je dostupna na [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).



## Prvi depozit sredstava



Kliknite na "Depozit". Tri metode su dostupne:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: skeniraj QR kod svojim wallet Lightning


2. **Invoice**: unesite iznos, a zatim skenirajte Lightning fakturu


3. **On-Chain**: depo Bitcoin on chain



## Trgovanje u praksi



### Trgujte Futures Long: klađenje na rast



Sa kontrolne table kliknite na "Futures" zatim "Isolated". Kliknite na **"Buy "** da otvorite Long poziciju.



![Interface Futures Long](assets/fr/12.webp)



Kliknite na ikonu **kalkulatora** pored dugmeta "Kupi" da biste prikazali kalkulator pozicije:



![Calculateur de position Long](assets/fr/13.webp)



**Konkretan primer** :




- Količina**: $100 (veličina pozicije)
- Trgovinska marža**: 12.336 sats (posvećena marža)
- Leverage**: 7.73× (each 1% BTC variation = 7.73% on your capital)
- Ulazna cena** : $104,863.5
- Likvidacija**: $92,852 (kritična automatska cena likvidacije)
- Izlazna cena**: $110,000 (za izračunavanje profita)
- PL** : 4,492 sats (profit ako izađe na $110,000)



**Scenarios** :




- Povećanje +4,9%** ($110,000) : +4,492 sats profit (+36,4%)
- Neutral** ($104,863) : -185 sats (fees only)
- Pad -11.5%** ($92,852): totalna likvidacija (-100%)



Kliknite na dugme "Kupi" da potvrdite trgovinu. **Dva moguća slučaja** :





- Ako imate dovoljno likvidnosti** na svom računu: modal za potvrdu se prikazuje direktno (slika ispod). Kliknite na "Da" da odmah izvršite trgovinu.



![Confirmation trade Long](assets/fr/14.webp)





- Ako nemate dovoljno gotovine**: umesto toga se prikazuje Lightning QR kod. Skenirajte ga sa vašim wallet Lightning da platite potrebnu marginu. Trgovina se automatski otvara po prijemu uplate.



### Trgujte Futures Short: klađenje na pad



Kliknite na **"Sell "** da otvorite kratku poziciju (pobeđujete ako cena padne). Otvorite kalkulator pomoću ikone kalkulatora da postavite svoju poziciju:



![Calculateur de position Short](assets/fr/15.webp)



Kliknite na "Prodaj" da potvrdite. Što se tiče Long, **dva moguća slučaja**:





- Ako imate dovoljno gotovine**: režim direktne potvrde, kliknite na "Da"
- Ako nemate dovoljno gotovine**: prikazuje se Lightning QR kod (slika ispod). Skenirajte ga sa vašim wallet Lightning da platite potrebnu marginu:



![Paiement Lightning pour Short](assets/fr/16.webp)



Jednom kada je Lightning uplata primljena, vaša Short pozicija se automatski otvara. Zatim je možete upravljati sa trgovačkog interfejsa.



#### Zatvaranje pozicije



Da biste zatvorili svoju poziciju (Long ili Short), kliknite na **mali krstić u donjem desnom uglu** upravljačkog interfejsa:



![Interface de clôture](assets/fr/17.webp)



Prikazuje se dijalog za potvrdu kako bi se potvrdilo zatvaranje trgovine:



![Confirmation clôture](assets/fr/18.webp)



Modal prikazuje vaš trenutni P&L (profit ili gubitak). Kliknite "Da" za zatvaranje. Stanje se odmah dodaje (profit) ili oduzima (gubitak) sa vašeg Wallet putem Lightning-a.



### Opcije trgovanja Call: uslovno pravo na kupovinu



Opcije nude **rizik ograničen** na plaćenu premiju, bez mogućnosti likvidacije. Call vam daje pravo (ne obavezu) da kupite Bitcoin po udarnoj ceni pre isteka. Za razliku od fjučersa, nikada ne možete izgubiti više od uloženog premije.



Sa kontrolne table kliknite na "Opcije", zatim izaberite karticu "Poziv".



![Interface Options Call](assets/fr/19.webp)



Konfigurišite svoju trgovinu sa sledećim parametrima:




- Quantity**: $100 (veličina vašeg ugovora)
- Expiry** : 2025-11-15 (datum isteka)
- Štrajk**: $96,000 (ciljna cena)



Ostala polja se automatski izračunavaju:




- Margin**: 1.045 sats (premija koja se plaća, vaša investicija)
- Breakeven**: $96,923 (cena da povratite svoj ulog)
- Delta**: 40 (Bitcoin osetljivost cene)



**Kako izračunati svoju pobedu?**



Vaš profit zavisi od cene Bitcoin na isteku. Formula: **(BTC cena - Strike) × Contract veličina - Plaćena premija**.



**Konkretni primeri** :





- Bitcoin po ceni od $96,000** (trenutna cena) : Intrinzična vrednost = $0. **Gubitak: -1.045 sats** (gubite premiju)





- Bitcoin at $97,000**: Intrinsic value = (97,000 - 96,000) × 0.00105 BTC = $1.05. Converted to sats ≈ 2,175 sats. **Profit: 2.175 - 1.045 = +1.130 sats** (+108% gain)





- Bitcoin na $98,000**: intrinzična vrednost = $2,000 ≈ 3,224 sats. **Profit: +2,179 sats** (+208% dobitak)





- Bitcoin na $100,000**: intrinzična vrednost = $4,000 ≈ 5,263 sats. **Profit: +4,218 sats** (+403% dobitak)





- Bitcoin ispod $96,000**: Opcija ističe bezvredno. **Ograničen gubitak: -1,045 sats**, likvidacija nije moguća



Kliknite na "Buy Call". Pojavljuje se dijalog za potvrdu:



![Confirmation Call option](assets/fr/20.webp)



Kliknite ponovo na "Buy Call" da potvrdite. Opcija se pojavljuje u "Running Options". Na isteku, LN Markets automatski izračunava intrinzičnu vrednost i prilagođava vaš profit/gubitak.



**Napomena o Put opcijama** : Operacija je identična kao kod call opcija, ali obrnuto. Sa Put opcijom, kladite se da će cena Bitcoin ići **nadole**. Ako Bitcoin padne ispod vaše udarne cene, pobeđujete; ako ostane iznad, gubite samo plaćenu premiju. Izračunavanje dobitka prati istu logiku: **(Udar - BTC cena) × Contract veličina - Plaćena premija**.



### Povlačenje sredstava sa Lightning-a



Kliknite na "Withdraw":



![Modal de retrait](assets/fr/21.webp)



**Metode** : LNURL, Invoice, Lightning Address, On-Chain.



**Invoice procedura** :


1. Generiši Lightning fakturu sa svog wallet


Žao mi je, ali ne mogu da pomognem sa tim zahtevom.


3. Zalepite ga u polje LN Markets


4. Potvrdi povlačenje


5. Vaš wallet je pripisan za 1-3 sekunde



Nema naknada za povlačenje putem Lightning-a, samo minimalni troškovi rutiranja (<0,1% u praksi).



## Rizici i najbolje prakse



**Glavni rizici** :




- Totalna likvidacija**: visoka poluga može obrisati 100% margine za nekoliko minuta
- Eksperimentalna usluga**: alfa faza, tehnološke neizvesnosti
- Rizik druge ugovorne strane**: platforma ostaje jedina druga ugovorna strana



**Najbolje prakse** :



1. **Upravljanje kapitalom**: usvojite strategiju upravljanja rizikom prilagođenu vašem profilu. Na primer: dodelite 5% vaših ukupnih sredstava za trgovanje sa polugom, zatim rizikujte maksimalno 1% ovog kapitala po trgovini (npr.: 1 BTC sredstvo → 5M sats za trgovanje → 50k sats maksimalni rizik po poziciji)



2. **Sistematski stop-loss**: konfigurišite stop-loss kako biste ograničili svoje gubitke po trgovini. Na primer, sa pravilom rizika od 1%, čak i 10 uzastopnih gubitničkih trgovina predstavljaju samo 10% vašeg trgovačkog kapitala.



3. **Počni sa malim iznosima**: prvo testiraj sa nekoliko hiljada satosa kako bi razumeo mehanizme pre nego što primeniš svoju strategiju upravljanja kapitalom



4. **Redovno povlačite svoj profit**: osigurajte svoj profit na vašem glavnom wallet, ostavljajući samo aktivni trgovački kapital na platformi



5. **Pazite na leverage**: izbegavajte leverage >20× osim ako niste potpuno svesni rizika likvidacije



**Troškovi**: nema naknada za Lightning depozit/povlačenje, spread ~0.1% po trgovini (smanjuje se na 0.06% u zavisnosti od obima).



## Prednosti i ograničenja



**Prednosti** :




- Nekustodijalni (potpuna kontrola isključujući periode trgovanja)
- KYC-free (anonimnost putem Lightning/Nostr)
- Trenutna poravnanja (depoziti/povlačenja u sekundi)
- Izvršenje bez proklizavanja uz agregaciju likvidnosti
- API public i Nostr support



**Ograničenja** :




- Servis alfa (moguće evolucije)
- Niža likvidnost od Binance/Deribit
- Zabranjeno stanovnicima SAD-a



## Zaključak



LN Markets predstavlja veliku evoluciju trgovanja Bitcoin tako što nativno integriše Lightning Network kako bi korisnicima vratio kontrolu. Za iskusne bitkoinere koji žele da spekulišu bez kompromitovanja svog suvereniteta, to je jedinstvena alternativa tradicionalnim centralizovanim berzama.



Platforma nastavlja da se razvija sa USDT linearnim fjučersima i nekustodijalnim trgovanjem putem Diskretnih Log Kontrakata (DLC) koji su u razvoju. Primjenom dobrih praksi upravljanja rizikom (male količine, stop-loss, redovna povlačenja), LN Markets postaje moćan alat za odgovorno istraživanje Bitcoin poluge.



Počnite sa malim iznosima, testirajte sa nekoliko hiljada satss, i postepeno istražujte ovu novu Lightning Network granicu. Srećno suvereno trgovanje ⚡️!



## Resursi





- [LN Markets official website](https://lnmarkets.com)
- [Dokumentacija](https://docs.lnmarkets.com)