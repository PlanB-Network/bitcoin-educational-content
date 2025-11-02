---
name: SwapMarket
description: Bitcoin i agregator usluga za zamenu Lightning-a
---

![cover](assets/cover.webp)



Prenos sredstava između Bitcoin On-Chain i Lightning Network obično zahteva ili ručno otvaranje Lightning kanala (tehnički i skupo), ili korišćenje centralizovanih platformi za zamenu sa KYC. SwapMarket nudi alternativu: Trustless atomske zamene putem konkurentnih provajdera, bez KYC.



Inovacija: iako su provajderi posrednici, HTLC (*Hash Vremenski Zaključani Ugovori*) matematički garantuju da vaša sredstva ostaju pod vašom kontrolom. Agregacija nekoliko provajdera (Boltz, ZEUS Swaps, Eldamar, Middle Way) stvara cenovnu konkurenciju. Interface veb otvorenog koda, moguće ga je samostalno hostovati.



## Šta je SwapMarket?



Otvoreni agregator pokrenut 2024. godine, SwapMarket funkcioniše kao komparator Bitcoin/Lightning provajdera za zamenu. Korisnik trenutno upoređuje uslove (naknade, likvidnost, ograničenja) i bira optimalnog provajdera.



### Tehnička arhitektura



**Frontend client-side**: 100% klijentska aplikacija (Fork Boltz Web App) hostovana na GitHub Pages. Kod se izvršava u pregledaču bez serverske podrške. Istorija se čuva lokalno (kolačići/keš). Javni i proverljiv izvorni kod.



**Provider discovery** : Hard-kodirana lista u `src/configs/Mainnet.ts`. Novi provajderi dodati putem Pull Request-a ili email-a.



**Nezavisni bekendi**: Svaki provajder upravlja sopstvenim Boltz bekendom. Interface u realnom vremenu pretražuje API-je kako bi odmah uporedio ponude.



**HTLC Atomske Zamene**: Hash Vremenski Zaključani Ugovori garantuju atomskost: ili se zamena izvršava, ili svaka strana povrati svoja sredstva. Rizik druge strane matematički eliminisan.



### Filozofija



SwapMarket smanjuje centralizaciju stvaranjem konkurencije između provajdera za naknade i likvidnost. Nema KYC, otvoreni kod koji se može samostalno hostovati, množenje nezavisnih operatera kako bi se izbegle tačke pojedinačnog kvara.



## Glavne karakteristike



### Tržište provajdera



Interface prikazuje sve aktivne provajdere: ime provajdera, primenjene naknade (procenat i/ili fiksne), minimalne/maksimalne dostupne iznose i podržane tipove zamena. Aplikacija direktno upituje API-je svakog provajdera navedenog u konfiguracionoj datoteci kako bi u realnom vremenu dobila ponude. Konkurencija između provajdera garantuje optimalne stope, generalno oko 0,5% za standardne zamene.



### Dvosmerne zamene



**Swap-in (On-Chain → Lightning)**: Konvertuj On-Chain BTC u Lightning satoshije. Upotreba: napajanje mobilnog Wallet Lightning, dobijanje dolaznog kapaciteta na čvoru, ili imati trenutnu likvidnost.



**Swap-out (Lightning → On-Chain)**: Konvertujte Lightning satoshije u On-Chain BTC. Upotreba: prebacite Wallet Lightning u Cold skladište ili balansirajte likvidnost između slojeva.



### Bezbednost i oporavak



**Trustless Atomske zamene: HTLC garantuje da će ili Exchange biti u potpunosti završen, ili će svaka strana povratiti svoj ulog. Rizik druge strane je matematički eliminisan.



**Mehanizam otkupa**: Svaka zamena ima datum isteka (TIMELOCK). Ako zamena ne uspe, sredstva su automatski povratna nakon isteka. Korisnik uvek zadržava opciju da povrati svoje bitkoine.



**Recovery keys**: SwapMarket vam omogućava da izvezete ključeve za oporavak za zamene koje su u toku. U slučaju problema, ovi ključevi se mogu koristiti za finalizaciju ili otkazivanje zamene sa bilo kog uređaja.



## Instalacija i pristup



### Interface veb



SwapMarket ne zahteva instalaciju. Pristup je putem pregledača posetom https://swapmarket.github.io. Za maksimalnu poverljivost, koristite Brave, Firefox sa ekstenzijama za zaštitu od praćenja, ili LibreWolf. Tor Browser se preporučuje za anonimnost na mreži.



Nije potrebna registracija, e-mail ili verifikacija identiteta.



### Samostalno hostovanje (opciono)



Za tehničke korisnike koji žele eliminisati bilo kakvu zavisnost od zvaničnog GitHub Pages domena, SwapMarket se može pokrenuti lokalno :



**Preko npm-a** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Preko Dockera** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Aplikacija će biti dostupna na `http://localhost:3000`. Samostalno hostovanje garantuje potpunu kontrolu nad Interface, eliminiše rizik od cenzure zvaničnog domena i omogućava da se izvorni kod pregleda pre izvršavanja.



### Početna konfiguracija



**Wallet Lightning**: Uverite se da imate operativni Wallet Lightning (Phoenix, Zeus, BlueWallet, itd.). Za swap-ins, koristićete generate za Lightning Invoice. Za swap-outs, platićete Lightning Invoice.



**Wallet On-Chain**: Za zamene, biće vam potreban Wallet Bitcoin On-Chain za slanje sredstava. Za zamene, pripremite Bitcoin prijemni Address.



**Opciona konfiguracija**: SwapMarket čuva istoriju zamena i preferencije u kolačićima pregledača. Nije potrebno kreiranje naloga.



## Pristup podešavanjima i ključ za oporavak



Pre nego što napravite svoje prve zamene, toplo preporučujemo da preuzmete svoj **Rescue Key**. Ovaj ključ za hitne slučajeve omogućava vam da povratite svoja sredstva u slučaju tehničkog problema ili gubitka pristupa vašem uređaju.



### Parametri pristupa



Sa glavne stranice SwapMarket-a, kliknite na ikonu zupčanika (⚙️) u gornjem desnom uglu Interface, pored obrasca za zamenu.



![Accès aux paramètres](assets/fr/01.webp)



### Postavke stranice



Stranica sa postavkama se otvara, prikazujući nekoliko opcija za konfiguraciju:





- Denominacija**: Izbor između BTC ili Sats
- Decimal Separator**: Decimal separator (, or .)
- Audio/Browser Notifications**: Audio i obaveštenja pregledača
- Rescue Key** : Preuzmi ključ za oporavak
- Logovi**: Pregledaj, preuzmi ili izbriši logove



![Page Settings](assets/fr/02.webp)



### Preuzmi Ključ za Spašavanje



Kliknite na dugme **Download** pored "Rescue Key".



**Važne tačke** :




- Rescue Key je **jedinstveni ključ za hitne slučajeve** koji radi za sve vaše buduće zamene.
- Čuvajte ovaj ključ na **sigurnom i trajnom** mestu (menadžer lozinki, digitalni sef)
- U slučaju problema sa zamjenom (istek vremena, tehnički kvar), ovaj ključ vam omogućava da povratite svoja sredstva



## Kreiranje zamene korak po korak



### Zamena: Lightning → Bitcoin



Ovaj prvi primer pokazuje kako konvertovati Lightning satoshije u On-Chain bitkoine.



**Korak 1: Zamena konfiguracije



Sa glavne stranice, izaberite obrazac za zamenu :




- LIGHTNING** (gornje polje): Unesite iznos koji želite poslati u Sats Lightning (primer: 30,000 Sats)
- Bitcoin** (bottom field): Iznos koji ćete primiti automatski se prikazuje nakon što se odbiju naknade (primer: Sats 29,320)



U donje polje zalepite svoj **prijemni Bitcoin Address** gde želite da primite sredstva. Pažljivo proverite ovaj Address.



Podrazumevani provajder je obično Boltz Exchange. Mrežne naknade i naknade provajdera su jasno prikazane.



![Configuration swap-out](assets/fr/03.webp)



**Korak 2: Izbor provajdera**



Kliknite na padajući meni provajdera (podrazumevano: "Boltz Exchange") da prikažete sve dostupne provajdere likvidnosti.



Otvara se modalni prozor koji prikazuje tabelu za poređenje:




- Status**: Green indikator da li je provajder aktivan
- Alias**: Ime provajdera (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Naknada**: Naknade koje naplaćuje pružalac usluga (uglavnom između 0.49% i 0.5%)
- Max Swap**: Maksimalni iznos prihvaćen za zamenu



Uporedite naknade i maksimalne iznose, a zatim izaberite provajdera po vašem izboru.



**Imajte na umu**: Izbor provajdera Interface ne prikazuje **minimalne iznose** za svakog provajdera. Ove informacije se pojavljuju samo u kreiranju zamene Interface, nakon što je provajder izabran. Minimalni i maksimalni iznosi mogu varirati od provajdera do provajdera i mogu se menjati tokom vremena. **Uvek proverite ove limite u trenutku vaše zamene**: ako je iznos koji želite da zamenite van limita provajdera, možete izabrati drugog koji je pogodniji za vašu transakciju.



![Sélection du provider](assets/fr/04.webp)



**Korak 3: Kreiranje zamene i Lightning** plaćanje



Kliknite na žuto dugme **"CREATE ATOMIC SWAP "**. SwapMarket će generate kreirati **Lightning Invoice** (BOLT11) za vas da platite sa vašeg Wallet Lightning.



Stranica prikazuje :




- Swap ID**: Jedinstveni identifikator zamene (primer: J4ymFIMVR6Hm)
- Status**: "swap.created" (swap kreiran, čeka se uplata)
- QR kod**: Skenirajte ga sa vašim Wallet Lightning
- Invoice Lightning**: Niz karaktera koji počinje sa "lnbc" (primer: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Platite ovaj Invoice sa vašeg Wallet Lightning (Phoenix, Zeus, BlueWallet, itd.). Tačan iznos za plaćanje je prikazan (primer: 30,000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Korak 4: Potvrda i prihvatanje**



Jednom kada je Lightning uplata potvrđena, SwapMarket odmah prima vašu uplatu i provajder emituje Bitcoin transakciju na vaš Address.



Status se menja u **"Invoice.settled "** (Invoice plaćeno), i pojavljuje se poruka o potvrdi.



Vaši On-Chain bitkoini će biti dostupni čim transakcija bude potvrđena (obično u roku od nekoliko minuta do nekoliko sati, u zavisnosti od Mining naknada koje je odabrao provajder).



![Confirmation swap-out](assets/fr/06.webp)



Možete kliknuti na **"OPEN CLAIM TRANSACTION "** da biste pogledali Bitcoin transakciju na Blockchain exploreru.



### Zamena: Bitcoin → Lightning



Ovaj drugi primer pokazuje kako konvertovati On-Chain bitkoine u Lightning satoshije.



**Korak 1: Zamena konfiguracije



Sa glavne stranice, odaberite obrazac za zamenu :




- Bitcoin** (gornje polje): Unesite iznos koji želite poslati u Sats Bitcoin (primer: 63,400 Sats)
- LIGHTNING** (donje polje): Iznos koji ćete primiti automatski se prikazuje nakon odbitka naknada (primer: 62 884 Sats)



U donje polje nalepite Lightning** Invoice (BOLT11) generisan iz vašeg Wallet Lightning, ili koristite vaš LNURL Address ako vaš Wallet to podržava.



![Configuration swap-in](assets/fr/07.webp)



**Korak 2: Provera Rescue Key-a**



Nakon što kliknete na **"CREATE ATOMIC SWAP "**, pojavljuje se modalni prozor koji traži da verifikujete vaš Rescue Key.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Pošto ste već otpremili svoj ključ za oporavak tokom početne konfiguracije (pogledajte prethodni odeljak), kliknite na dugme **"VERIFY EXISTING KEY "** da biste uvezli ključ koji ste sačuvali.



Izaberite prethodno preuzetu datoteku sa spasilačkim ključem. Nakon uspešne verifikacije, Interface automatski prelazi na sledeći korak.



**Korak 3: Bitcoin** depozit Address



SwapMarket sada generiše **jedinstveni Bitcoin Address** koji sadrži HTLC Contract povezan sa vašim Lightning Invoice.



Stranica prikazuje :




- Swap ID**: Jedinstveni identifikator (primer: 1kGmB6JyGqU4)
- Status** : "Invoice.set" (Invoice set, čeka se uplata Bitcoin)
- QR kod**: Bitcoin depo Address
- Bitcoin** Address: Obično počinje sa "bc1p..." (primer: bc1p5mvtwxapjkds...9d4n9f)
- Upozorenje u žutom** : "Uverite se da vaša transakcija bude potvrđena unutar ~24 sata nakon kreiranja ove zamene!"



Ovaj period od ~24 sata je **timeout** za HTLC Contract. Ako vaša Bitcoin transakcija nije potvrđena u ovom vremenskom okviru, zamena će propasti i moraćete da koristite svoj Rescue Key da povratite svoja sredstva.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Možete kopirati Address klikom na dugme **"Address"**, ili skenirati QR kod direktno sa vašeg Wallet On-Chain.



**Korak 4: Slanje bitkoina**



Sa vašeg Wallet Bitcoin On-Chain, pošaljite **tačno** naznačeni iznos (npr. 63,400 Sats) na generisani Address.



**Važno**: Koristite odgovarajuće Mining naknade kako biste osigurali brzo potvrđivanje. Ako je naknada preniska i transakcija ostane u Mempool duže od vremenskog ograničenja (~24h), zamena će propasti.



Jednom kada je transakcija poslana, SwapMarket detektuje da je u Mempool i prikazuje:




- Status** : "transaction.Mempool"
- Poruka**: "Transakcija je u Mempool - Čeka se potvrda za završetak zamene"



![Transaction en mempool](assets/fr/10.webp)



**Korak 5: Potvrda i Munja** prijem



Čim transakcija Bitcoin dobije svoju prvu potvrdu, provajder automatski plaća vaš Lightning Invoice. Odmah dobijate satoshije na vašem Wallet Lightning.



Status se menja u **"transaction.claim.pending "**, zatim se prikazuje poruka o potvrdi:



![Confirmation swap-in](assets/fr/11.webp)



Vaši Lightning satoshi su odmah dostupni u vašem Wallet.



## Prednosti i ograničenja



### Pogodnosti



**Takmičenje u cenama**: Agregacija provajdera stvara prirodno takmičenje koje povlači naknade nadole (0,49% do 0,5%).



**Poverljivost**: Nema KYC, Interface 100% na strani klijenta (bez prenosa ličnih podataka), kompatibilno sa Tor Browser-om.



**Non-custodial**: HTLC matematički garantuje isključivu kontrolu nad vašim sredstvima. Ili zamena uspeva, ili dobijate svoje bitkoine nazad.



**Otvoreni kod koji se može samostalno hostovati**: javni kod koji se može revidirati, moguće ga je lokalno implementirati za maksimalnu otpornost na cenzuru.



### Ograničenja



**Ograničena likvidnost**: Ograničen broj aktivnih provajdera (Boltz, Eldamar, MiddleWay u zavisnosti od perioda). Maksimalni iznosi mogu biti ograničeni.



**Vreme isteka**: Vreme čekanja od 24h do 48h. Ako transakcija On-Chain nije potvrđena pre isteka, potrebna je ručna obnova.



**Interface centralizacija**: Iako se može samostalno hostovati, zvanični Interface je hostovan na GitHub Pages. Ako GitHub cenzuriše repo, pristup preko swapmarket.github.io će biti blokiran (rešenje: samostalno hostovanje).



**On-Chain tragovi**: HTLC skripte su potencijalno prepoznatljive naprednom Blockchain analizom.



## Najbolje prakse



### Sigurna konfiguracija



**Preuzmite svoj Rescue Key**: Pre nego što obavite prve zamene, preuzmite svoj Rescue Key iz Podešavanja (pogledajte posvećeni odeljak iznad). Ovaj jedinstveni ključ će raditi za sve vaše buduće zamene, omogućavajući vam da povratite svoja sredstva u slučaju problema.



**Koristite Tor Pregledač**: Za maksimalnu poverljivost, pristupite SwapMarket-u putem Tor Pregledača kako biste sakrili svoj IP Address.



**Razmislite o samostalnom hostovanju**: Za tehničke korisnike, pokretanje sopstvene instance SwapMarket-a eliminiše zavisnost od zvaničnog GitHub Pages domena.



### Optimizacija zamene



**Pratite Mempool**: Proverite Mempool.space pre zamene. Birajte vreme niske aktivnosti kako biste minimizirali troškove Mining.



**Proverite adrese**: Za zamene, pažljivo proverite vaš prijemni Address. Koristite kopiranje i lepljenje i proverite prvih 5 i poslednjih 5 karaktera.



**Testirajte sa malim količinama**: Počnite sa minimalno dozvoljenim (25.000 do 50.000 Sats). Postepeno povećavajte kada savladate proces.



**Dokumentujte svoje zamene**: Zabeležite ID svake zamene, otkupni Address i datum isteka. Ove informacije olakšavaju praćenje i oporavak u slučaju tehničkog problema.



### Strategija korišćenja



**Uravnotežite svoj novčani tok**: Koristite SwapMarket da prilagodite svoju alokaciju između On-Chain (štednja, dugoročna sigurnost) i Lightning (dnevni troškovi, trenutna plaćanja) prema vašim stvarnim potrebama.



**Izračunajte profitabilnost**: Za trajne potrebe Lightning likvidnosti, uporedite kumulativni trošak ponovljenih zamena sa otvaranjem Lightning kanala direktno. SwapMarket je odličan za jednokratna podešavanja, ne nužno za velike redovne tokove.



## SwapMarket vs Boltz: Koja je razlika?



### Boltz: Tehnologija vs. Usluga



**Boltz je open-source tehnologija** (`boltz-backend` na GitHubu) koja implementira atomske zamene putem HTLC između Bitcoin, Lightning i Liquid.



**Kritična tačka**: Svi SwapMarket provajderi (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) koriste svoju instancu Boltz backend-a. Osnovna tehnologija je stoga identična. Ranljivost u Boltz backend-u bi potencijalno uticala na sve provajdere, ali otvoreni kod sistema omogućava reviziju od strane zajednice.



**Boltz Exchange** je usluga koju pruža isključivo tim Boltz, dok **SwapMarket** okuplja nekoliko provajdera koji svi koriste Boltz tehnologiju, stvarajući konkurentno cenovno okruženje.



Pogledajte naše Boltz i Zeus Swap tutorijale za više detalja:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Ključne razlike



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarket prednosti**: Cenovna konkurencija, diverzifikacija backend instanci, poređenje u realnom vremenu.



**Tehnološke alternative** (nisu kompatibilne sa SwapMarket-om): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Ova rešenja koriste sopstvene implementacije podmorskih zamena.



**Preporuka**: Koristite Boltz Exchange za jednostavnost ili SwapMarket za optimizaciju troškova kroz konkurenciju. Obe opcije su jednake po bezbednosti (HTLC ne-kustodijalni).



## Zaključak



SwapMarket olakšava Bitcoin/Lightning razmene agregiranjem više provajdera u jedan Interface. Arhitektura HTLC garantuje ne-kustodijalnu prirodu zamena, odsustvo KYC-a čuva poverljivost, a open-source kod koji se može samostalno hostovati pojačava otpornost na cenzuru.



Konkurencija između provajdera poboljšava stope i umnožava izvore likvidnosti. Da bi se optimizovalo upravljanje dva-Layer (On-Chain štednja, Lightning troškovi), SwapMarket je praktičan alat koji čuva finansijski suverenitet i poverljivost.



## Resursi



### Zvanična dokumentacija




- [SwapMarket - Web aplikacija](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Tehnička dokumentacija](https://docs.boltz.Exchange/)
- [Vodič za samostalno hostovanje](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Povezani projekti




- [Boltz Exchange](https://boltz.Exchange) - Originalna usluga atomskih zamena
- [ZEUS Swaps](https://zeusln.com) - Pružalac Lightning zamena