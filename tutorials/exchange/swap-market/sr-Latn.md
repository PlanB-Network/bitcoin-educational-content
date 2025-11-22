---
name: SwapMarket
description: Bitcoin i agregator usluga za zamenu Lightning-a
---

![cover](assets/cover.webp)



Prenos sredstava između Bitcoin, on-chain i Lightning Network obično zahteva ili ručno otvaranje Lightning kanala (tehnički i skupo), ili korišćenje centralizovanih platformi za zamenu sa KYC. SwapMarket nudi alternativu: zamene bez poverenja putem konkurentnih provajdera, bez KYC.



Inovacija: iako su provajderi posrednici, HTLC (*Hash Time Locked Contracts*) matematički garantuje da vaša sredstva ostaju pod vašom kontrolom. Agregacija nekoliko provajdera (Boltz, ZEUS Swaps, Eldamar, Middle Way) stvara cenovnu konkurenciju. Interface web otvorenog koda, moguće ga je samostalno hostovati.



## Šta je SwapMarket?



Otvoreni agregator pokrenut 2024. godine, SwapMarket funkcioniše kao upoređivač Bitcoin/Lightning provajdera za zamenu. Korisnik trenutno upoređuje uslove (naknade, likvidnost, ograničenja) i bira optimalnog provajdera.



### Tehnička arhitektura



**Frontend client-side**: 100% klijentska aplikacija (fork Boltz Web App) hostovana na GitHub Pages. Kod se izvršava u pregledaču bez serverske pozadine. Istorija se čuva lokalno (kolačići/keš). Javni i proverljiv izvorni kod.



**Provider discovery** : Hardkodirana lista u `src/configs/mainnet.ts`. Novi provajderi se dodaju putem Pull Request-a ili email-a.



**Nezavisni bekendi**: Svaki provajder upravlja sopstvenim Boltz bekendom. Interfejs u realnom vremenu upituje API-je kako bi trenutno uporedio ponude.



**HTLC Atomske Zamene**: Hash Vremenski Zaključani Ugovori garantuju atomskost: ili se zamena izvršava, ili svaka strana povrati svoja sredstva. Rizik druge strane matematički eliminisan.



### Filozofija



SwapMarket smanjuje centralizaciju stvaranjem konkurencije između provajdera za naknade i likvidnost. Nema KYC, otvoreni kod koji se može samostalno hostovati, umnožavanje nezavisnih operatera kako bi se izbegle tačke pojedinačnog kvara.



## Glavne karakteristike



### Tržište provajdera



Interfejs prikazuje sve aktivne provajdere: ime provajdera, primenjene naknade (procenat i/ili fiksne), dostupne minimalne/maksimalne iznose i podržane tipove zamene. Aplikacija direktno upituje API-je svakog provajdera navedenog u konfiguracionoj datoteci kako bi preuzela ponude u realnom vremenu. Konkurencija između provajdera garantuje optimalne stope, generalno oko 0,5% za standardne zamene.



### Dvosmerne zamene



**Swap-in (on-chain → Lightning)**: Konvertujte on-chain BTC u Lightning satoshije. Upotreba: napajanje mobilnog wallet Lightning, dobijanje dolaznog kapaciteta na čvoru ili trenutna likvidnost.



**Swap-out (Lightning → on-chain)**: Konvertujte Lightning satoshije u on-chain BTC. Upotreba: ispraznite wallet Lightning u hladno skladište ili balansirajte likvidnost između slojeva.



### Sigurnost i oporavak



**Trustless atomic swaps**: HTLC-ovi garantuju da će ili razmena biti u potpunosti završena, ili će svaka strana povratiti svoj ulog. Rizik druge strane je matematički eliminisan.



**Mehanizam otplate**: Svaki swap ima vremensko zaključavanje. Ako swap ne uspe, sredstva su automatski povratna nakon isteka. Korisnik uvek zadržava opciju da povrati svoje bitkoine.



**Ključevi za oporavak**: SwapMarket vam omogućava da izvezete ključeve za oporavak za zamene koje su u toku. U slučaju problema, ovi ključevi se mogu koristiti za finalizaciju ili otkazivanje zamene sa bilo kog uređaja.



## Instalacija i pristup



### Interface web



SwapMarket ne zahteva instalaciju. Pristup je putem pregledača posetom https://swapmarket.github.io. Za maksimalnu poverljivost, koristite Brave, Firefox sa ekstenzijama za zaštitu od praćenja, ili LibreWolf. Tor Browser se preporučuje za anonimnost na mreži.



Nije potrebna registracija, e-pošta ili verifikacija identiteta.



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



Aplikacija će biti dostupna na `http://localhost:3000`. Samostalno hostovanje garantuje potpunu kontrolu nad interfejsom, eliminiše rizik od cenzure zvaničnog domena i omogućava da se izvorni kod proveri pre izvršavanja.



### Početna konfiguracija



**Wallet Lightning**: Uverite se da imate operativni wallet Lightning (Phoenix, Zeus, BlueWallet, itd.). Za swap-ins, generate ćete Lightning fakturu. Za swap-outs, platićete Lightning fakturu.



**Wallet on-chain**: Za zamene, biće vam potreban wallet Bitcoin on-chain za slanje sredstava. Za zamene, pripremite Bitcoin adresu za primanje.



**Opciona konfiguracija**: SwapMarket čuva istoriju zamena i preferencije u kolačićima pregledača. Nije potrebno kreiranje naloga.



## Pristup podešavanjima i ključ za spasavanje



Pre nego što napravite svoje prve zamene, toplo preporučujemo da preuzmete svoj **Rescue Key**. Ovaj ključ za hitne slučajeve omogućava vam da povratite svoja sredstva u slučaju tehničkog problema ili gubitka pristupa vašem uređaju.



### Parametri pristupa



Sa glavne stranice SwapMarket-a, kliknite na ikonu zupčanika (⚙️) u gornjem desnom uglu interfejsa, pored forme za zamenu.



![Accès aux paramètres](assets/fr/01.webp)



### Postavke stranice



Stranica sa postavkama se otvara, prikazujući nekoliko opcija konfiguracije:





- Denominacija**: Izbor BTC ili sats
- Decimal Separator**: Decimal separator (, or .)
- Audio/Obaveštenja Pregledača**: Audio i obaveštenja pregledača
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



Ovaj prvi primer pokazuje kako konvertovati Lightning satoshije u on-chain bitkoine.



**Korak 1: Zamena konfiguracije



Sa glavne stranice, odaberite obrazac za zamenu :




- LIGHTNING** (gornje polje): Unesite iznos koji želite poslati u sats Lightning (primer: 30,000 sats)
- BITCOIN** (donje polje): Iznos koji ćete primiti automatski se prikazuje nakon što su naknade oduzete (primer: 29,320 sats)



U donje polje nalepite svoju **Bitcoin adresu za primanje** na koju želite da primite sredstva. Pažljivo proverite ovu adresu.



Podrazumevani provajder je obično Boltz Exchange. Mrežne naknade i naknade provajdera su jasno prikazane.



![Configuration swap-out](assets/fr/03.webp)



**Korak 2: Izbor provajdera**



Kliknite na padajući meni provajdera (podrazumevano: "Boltz Exchange") da prikažete sve dostupne provajdere likvidnosti.



Otvara se modalni prozor koji prikazuje tabelu za poređenje:




- Status**: Green indikator ako je provajder aktivan
- Alias**: Ime provajdera (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Naknada**: Naknade koje naplaćuje pružalac usluga (uglavnom između 0.49% i 0.5%)
- Max Swap**: Maksimalni iznos prihvaćen za zamenu



Uporedite naknade i maksimalne iznose, a zatim izaberite provajdera po vašem izboru.



**Imajte na umu**: Interfejs za izbor provajdera ne prikazuje **minimalne iznose** za svakog provajdera. Ove informacije se pojavljuju samo u interfejsu za kreiranje zamene, nakon što je provajder izabran. Minimalni i maksimalni iznosi mogu varirati od provajdera do provajdera i mogu se menjati tokom vremena. **Uvek proverite ove limite u trenutku vaše zamene**: ako iznos koji želite da zamenite nije u okviru limita provajdera, možete izabrati drugog koji je pogodniji za vašu transakciju.



![Sélection du provider](assets/fr/04.webp)



**Korak 3: Kreiranje zamene i Lightning** plaćanje



Kliknite na žuto dugme **"CREATE ATOMIC SWAP "**. SwapMarket će generate generisati **Lightning fakturu** (BOLT11) koju ćete platiti sa vašeg wallet Lightning.



Stranica prikazuje :




- Swap ID**: Jedinstveni identifikator zamene (primer: J4ymFIMVR6Hm)
- Status**: "swap.created" (swap kreiran, čeka se uplata)
- QR kod**: Skenirajte ga sa vašim wallet Lightning
- Invoice Lightning**: Karakterna niska koja počinje sa "lnbc" (primer: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Platite ovaj račun sa vašeg wallet Lightning (Phoenix, Zeus, BlueWallet, itd.). Tačan iznos za plaćanje je prikazan (primer: 30,000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Korak 4: Potvrda i prihvatanje**



Jednom kada je Lightning uplata potvrđena, SwapMarket odmah prima vašu uplatu i provajder emituje Bitcoin transakciju na vašu adresu.



Status se menja u **"invoice.settled "** (faktura plaćena), i prikazuje se poruka o potvrdi.



Vaši on-chain bitkoini će biti dostupni čim transakcija bude potvrđena (obično od nekoliko minuta do nekoliko sati, u zavisnosti od mining naknada koje je odabrao provajder).



![Confirmation swap-out](assets/fr/06.webp)



Možete kliknuti na **"OPEN CLAIM TRANSACTION "** da biste pogledali Bitcoin transakciju na blockchain pretraživaču.



### Zamena: Bitcoin → Lightning



Ovaj drugi primer pokazuje kako konvertovati on-chain bitkoina u Lightning satošije.



**Korak 1: Zamena konfiguracije



Sa glavne stranice, odaberite obrazac za zamenu :




- BITCOIN** (gornje polje): Unesite iznos koji želite poslati u sats Bitcoin (primer: 63,400 sats)
- LIGHTNING** (donje polje): Iznos koji ćete primiti automatski se prikazuje nakon odbitka naknada (primer: 62 884 sats)



U donje polje nalepite Lightning** fakturu (BOLT11) generisanu sa vašeg wallet Lightning, ili koristite vašu LNURL adresu ako vaš wallet to podržava.



![Configuration swap-in](assets/fr/07.webp)



**Korak 2: Provera Rescue Key-a**



Nakon što kliknete na **"CREATE ATOMIC SWAP "**, pojavljuje se modalni prozor koji traži da verifikujete vaš Rescue Key.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Pošto ste već otpremili svoj ključ za oporavak tokom početne konfiguracije (pogledajte prethodni odeljak), kliknite na dugme **"VERIFY EXISTING KEY "** da biste uvezli ključ koji ste sačuvali.



Izaberite prethodno preuzetu Rescue Key datoteku. Nakon uspešne verifikacije, interfejs se automatski prebacuje na sledeći korak.



**Korak 3: Bitcoin** adresa za depozit



SwapMarket sada generiše **jedinstvenu Bitcoin adresu** koja sadrži HTLC ugovor povezan sa vašom Lightning fakturom.



Stranica prikazuje :




- Swap ID**: Jedinstveni identifikator (primer: 1kGmB6JyGqU4)
- Status**: "invoice.set" (faktura postavljena, čeka se uplata Bitcoin)
- QR kod**: Bitcoin adresa skladišta
- Bitcoin** adresa: Obično počinje sa "bc1p..." (primer: bc1p5mvtwxapjkds...9d4n9f)
- Upozorenje u žutom** : "Uverite se da vaša transakcija bude potvrđena unutar ~24 sata nakon kreiranja ove zamene!"



Ovaj period od ~24 sata je **timeout** HTLC ugovora. Ako vaša Bitcoin transakcija nije potvrđena u ovom vremenskom okviru, zamena će propasti i moraćete da koristite svoj Rescue Key da povratite svoja sredstva.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Možete kopirati adresu klikom na dugme **"ADDRESS "**, ili skenirati QR kod direktno sa vašeg wallet on-chain.



**Korak 4: Slanje bitkoina**



Iz vašeg wallet Bitcoin on-chain, pošaljite **tačno** naznačeni iznos (npr. 63,400 sats) na generisanu adresu.



**Važno**: Koristite odgovarajuće mining naknade kako biste osigurali brzo potvrđivanje. Ako je naknada preniska i transakcija ostane u mempool-u duže od vremenskog ograničenja (~24h), zamena će propasti.



Jednom kada je transakcija poslana, SwapMarket detektuje da je u mempool-u i prikazuje:




- Status** : "transaction.mempool
- Poruka**: "Transakcija je u mempool-u - Čeka se potvrda za završetak zamene"



![Transaction en mempool](assets/fr/10.webp)



**Korak 5: Potvrda i Munja** prijem



Čim transakcija Bitcoin dobije svoju prvu potvrdu, provajder automatski plaća vaš Lightning račun. Odmah dobijate satoshije na vašem wallet Lightning.



Status se menja u **"transaction.claim.pending "**, zatim se prikazuje poruka o potvrdi:



![Confirmation swap-in](assets/fr/11.webp)



Vaši Lightning satoshi su odmah dostupni u vašem wallet.



## Prednosti i ograničenja



### Pogodnosti



**Takmičenje u cenama**: Agregacija provajdera stvara prirodno takmičenje koje povlači naknade nadole (0,49% do 0,5%).



**Poverljivost**: Bez KYC, 100% klijentski interfejs (bez prenosa ličnih podataka), kompatibilan sa Tor Browser-om.



**Non-custodial**: HTLC matematički garantuje isključivu kontrolu nad vašim sredstvima. Ili zamena uspeva, ili dobijate svoje bitkoine nazad.



**Otvoreni kod koji se može samostalno hostovati**: javni kod koji se može proveriti, može se lokalno implementirati za maksimalnu otpornost na cenzuru.



### Ograničenja



**Ograničena likvidnost**: Ograničen broj aktivnih provajdera (Boltz, Eldamar, MiddleWay u zavisnosti od perioda). Maksimalni iznosi mogu biti ograničeni.



**Vreme isteka**: Vreme čekanja od 24h do 48h. Ako transakcija on-chain nije potvrđena pre isteka, potrebna je ručna obnova.



**Interface centralizacija**: Iako se može samostalno hostovati, zvanični interfejs je hostovan na GitHub Pages. Ako GitHub cenzuriše repo, pristup preko swapmarket.github.io će biti blokiran (rešenje: samostalno hostovanje).



**on-chain Traces**: HTLC skripte su potencijalno prepoznatljive naprednom analizom blockchaina.



## Najbolje prakse



### Sigurna konfiguracija



**Preuzmite svoj Rescue Key**: Pre nego što obavite prve zamene, preuzmite svoj Rescue Key iz Podešavanja (pogledajte posvećeni odeljak iznad). Ovaj jedinstveni ključ će raditi za sve vaše buduće zamene, omogućavajući vam da povratite svoja sredstva u slučaju problema.



**Koristite Tor Pregledač**: Za maksimalnu poverljivost, pristupite SwapMarket-u putem Tor Pregledača kako biste sakrili svoju IP adresu.



**Razmislite o samostalnom hostovanju**: Za tehničke korisnike, pokretanje sopstvene instance SwapMarket-a eliminiše zavisnost od zvaničnog GitHub Pages domena.



### Optimizacija zamene



**Pratite mempool**: Proverite mempool.space pre zamene. Birajte periode niske aktivnosti kako biste minimizirali mining troškove.



**Proverite adrese**: Za zamene, pažljivo proverite vašu adresu za primanje. Koristite kopiranje i lepljenje i proverite prvih 5 i poslednjih 5 karaktera.



**Testirajte sa malim količinama**: Počnite sa minimalno dozvoljenim (25.000 do 50.000 sats). Postepeno povećavajte kada savladate proces.



**Dokumentujte svoje zamene**: Zabeležite ID svake zamene, adresu za otkup i datum isteka. Ove informacije olakšavaju praćenje i oporavak u slučaju tehničkog problema.



### Strategija korišćenja



**Uravnotežite svoj novčani tok**: Koristite SwapMarket da prilagodite svoju alokaciju između on-chain (štednja, dugoročna sigurnost) i Lightning (dnevni troškovi, trenutna plaćanja) prema vašim stvarnim potrebama.



**Izračunajte profitabilnost**: Za trajne potrebe Lightning likvidnosti, uporedite kumulativni trošak ponovljenih zamena sa otvaranjem Lightning kanala direktno. SwapMarket je odličan za jednokratna prilagođavanja, ne nužno za velike redovne tokove.



## SwapMarket vs Boltz: Koja je razlika?



### Boltz: Tehnologija vs. Usluga



**Boltz je tehnologija otvorenog koda** (`boltz-backend` na GitHub-u) koja implementira atomske zamene putem HTLC između Bitcoin, Lightning i Liquid.



**Kritična tačka**: Svi SwapMarket provajderi (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) implementiraju svoju instancu Boltz backend-a. Osnovna tehnologija je stoga identična. Ranljivost u Boltz backend-u bi potencijalno uticala na sve provajdere, ali otvorena priroda sistema omogućava reviziju od strane zajednice.



**Boltz Exchange** je usluga koju pruža isključivo tim Boltz, dok **SwapMarket** okuplja nekoliko provajdera koji svi koriste Boltz tehnologiju, stvarajući konkurentno okruženje za cene.



Pogledajte naše Boltz i Zeus Swap tutorijale za više detalja:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Ključne razlike



| Aspekt       | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Priroda       | Jedinstvena usluga   | Agregator više provajdera            |
| Provajderi    | Samo Boltz           | Boltz, ZEUS, Eldamar, Middle Way     |
| Konkurencija  | Fiksne tarife         | Slobodna konkurencija                |
| Interfejs     | boltz.exchange       | swapmarket.github.io (samohostujuće) |
| Bezbednost    | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

**Prednosti SwapMarket-a**: Cenovna konkurencija, diverzifikacija backend instanci, poređenje u realnom vremenu.



**Tehnološke alternative** (nije kompatibilno sa SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Ova rešenja koriste sopstvene implementacije podmorskih zamena.



**Preporuka**: Koristite Boltz Exchange za jednostavnost ili SwapMarket za optimizaciju troškova kroz konkurenciju. Obe opcije su ekvivalentne po bezbednosti (HTLC ne-kustodijalan).



## Zaključak



SwapMarket omogućava Bitcoin/Lightning razmene agregiranjem više provajdera u jedan interfejs. HTLC arhitektura garantuje ne-kustodijalnu prirodu zamena, odsustvo KYC-a čuva poverljivost, a samohostujući open-source kod pojačava otpornost na cenzuru.



Konkurencija između provajdera poboljšava stope i umnožava izvore likvidnosti. Da bi se optimizovalo upravljanje u dva sloja (on-chain štednja, Lightning troškovi), SwapMarket je praktičan alat koji čuva finansijski suverenitet i poverljivost.



## Resursi



### Zvanična dokumentacija




- [SwapMarket - Web aplikacija](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Tehnička dokumentacija](https://docs.boltz.exchange/)
- [Vodič za samostalno hostovanje](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Povezani projekti




- [Boltz Exchange](https://boltz.exchange) - Originalna usluga atomskih zamena
- [ZEUS Swaps](https://zeusln.com) - Provajder Lightning zamena