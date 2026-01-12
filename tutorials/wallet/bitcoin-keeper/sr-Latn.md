---
name: Bitcoin Keeper
description: Bitcoin mobilni wallet za bezbednost i multi-sig
---

![cover](assets/cover.webp)



Sigurno upravljanje bitcoinima predstavlja veliki izazov za svakog vlasnika koji je svestan uloga uključenih u finansijski suverenitet. Između jednostavnosti mobilnog wallet i robusnosti multi-sig rešenja, tehnička razlika može izgledati zastrašujuće za mnoge korisnike. Bitcoin Keeper je pozicioniran upravo na ovom preseku, nudeći progresivan pristup sigurnosti koji prati korisnike dok se razvijaju.



Bitcoin Keeper je aplikacija otvorenog koda za mobilne uređaje, isključivo posvećena Bitcoin, koju je razvila ekipa BitHyve. Njena ambicija je da napredni menadžment portfolija učini dostupnim, posebno multisignature konfiguracije, uz održavanje intuitivnog interfejsa za početnike. Aplikacija usvaja slogan "Osiguraj danas, Planiraj za sutra", što odražava njenu filozofiju dugoročne podrške.



Za razliku od generalističkih novčanika koji upravljaju sa više kriptovaluta, Bitcoin Keeper održava strogi fokus na Bitcoin. Ovaj pristup isključivo za bitcoin smanjuje potencijalnu površinu napada i uveliko pojednostavljuje korisničko iskustvo. Aplikacija se takođe ističe svojom nativnom integracijom najrasprostranjenijih hardverskih novčanika i naprednim funkcijama upravljanja UTXO.



## Šta je Bitcoin Keeper?



### Filozofija i ciljevi



Bitcoin Keeper je dizajniran da zadovolji specifične potrebe bitkoinera koji žele da zadrže punu kontrolu nad svojim privatnim ključevima. Projekat u potpunosti prihvata fundamentalne principe Bitcoin: otvoren i proverljiv izvorni kod, poštovanje privatnosti i suverenitet korisnika. Nije potrebna registracija niti lične informacije za korišćenje aplikacije, a može čak raditi i offline za operacije potpisivanja.



Centralni cilj je ponuditi fleksibilan, budućnosti otporan alat za čuvanje BTC tokom nekoliko godina, pa čak i nekoliko generacija, zahvaljujući funkcionalnostima nasleđivanja. Aplikacija omogućava korisnicima da započnu jednostavno sa mobilnim wallet, a zatim postepeno evoluiraju ka sigurnijim rešenjima sa više potpisa.



### Arhitektura aplikacije



Bitcoin Keeper organizuje upravljanje fondovima oko dva različita koncepta. **Hot Wallet** je jednostavan jednoključni wallet, pohranjen na telefonu, dizajniran za svakodnevnu potrošnju i skromne iznose. Trezori** su sefovi sa više potpisa (više ključeva) koji zahtevaju nekoliko ključeva za autorizaciju troška, dizajnirani za dugoročno sigurno skladištenje.



### Glavne karakteristike



Bitcoin Keeper podržava skoro sve hardverske novčanike na tržištu: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport i Coinkiteov Tapsigner. Integracija se odvija putem različitih metoda u zavisnosti od uređaja: skeniranje QR koda, NFC povezivanje ili uvoz datoteka.



Aplikacija takođe nudi napredno upravljanje UTXO sa označavanjem transakcija, kontrolom novčića za ručno biranje ulaza prilikom slanja i podrškom za PSBT format za delimično potpisane transakcije.



## Instalacija i početna konfiguracija



Bitcoin Keeper je dostupan besplatno na Androidu putem Google Play Store-a i na iOS-u putem App Store-a. Izdavač je naveden kao BitHyve. Pre instalacije, uverite se da vaš uređaj nema malver, da je ažuriran i da nije root-ovan ili jailbreak-ovan.



Prilikom prvog pokretanja, aplikacija vas pita da kreirate sigurnosni PIN kod. Ovaj kod štiti pristup vašem wallet i šifrira osetljive podatke lokalno. Izaberite jak kod i zapamtite ga. Zatim možete aktivirati biometrijsku autentifikaciju (otisak prsta ili Face ID) za brže otključavanje.



![Installation et configuration du PIN](assets/fr/01.webp)



Aplikacija zatim prikazuje nekoliko uvodnih ekrana koji objašnjavaju njena tri stuba: kreiranje wallet za slanje i primanje bitkoina, upravljanje ključevima sa kompatibilnošću za wallet hardver, i planiranje nasleđa za prenos bitkoina. Pritisnite "Get Started", zatim izaberite "Start New" za kreiranje nove konfiguracije.



![Écrans d'introduction](assets/fr/02.webp)



## Otkrivanje interfejsa



Interfejs Bitcoin Keeper organizovan je oko četiri glavne kartice dostupne iz donje navigacione trake:



![Les quatre onglets de l'application](assets/fr/03.webp)



Kartica **Wallets** prikazuje vaše novčanike i njihove bilanse. Ovde pristupate svojim novčanicima da biste slali i primali bitkoine. Oznake "Hot Wallet" i "Single-Key" ili "Multi-Key" omogućavaju vam da brzo identifikujete tip svakog wallet.



Kartica **Keys** centralizuje upravljanje vašim potpisnim ključevima. Ovde ćete pronaći Mobilni Ključ generisan od strane aplikacije, kao i sve ključeve uvezene iz hardverskih novčanika. Takođe, ovde dodajete nove uređaje za potpisivanje.



Kartica **Concierge** nudi usluge podrške: postavite pitanja timu za podršku i povežite se sa Bitcoin savetnicima za personalizovanu pomoć.



Kartica **Više** (Više opcija) omogućava pristup podešavanjima kao što su lična veza sa serverom, rezervna kopija ključa, dokumenti o nasleđivanju, preferencije prikaza i upravljanje wallet.



## Povezivanje na sopstveni server



Da biste ojačali svoju poverljivost, Bitcoin Keeper vam omogućava da povežete aplikaciju sa sopstvenim Electrum serverom, umesto da koristite podrazumevane javne servere.



![Configuration du serveur Electrum](assets/fr/04.webp)



Sa kartice Više, skrolujte nadole da pronađete podešavanja servera. Pritisnite "Dodaj Server" da konfigurišete novu konekciju. Možete birati između "Javni Server" (pre-konfigurisani javni serveri) i "Privatni Electrum" (vaš sopstveni server).



Za privatni server, unesite URL (npr. umbrel.local za Umbrel čvor) i broj porta (obično 50001). Aktivirajte SSL ako vaš server to podržava. Takođe možete skenirati QR kod konfiguracije. Kada unesete parametre, pritisnite "Poveži se na server".



Ako još uvek nemate svoj Bitcoin čvor, pogledajte naš vodič za Umbrel, jednostavan i pristupačan način da sami napravite čvor:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Primite bitkoine



Sa kartice Novčanici, odaberite wallet sa kojeg želite primiti sredstva pritiskom na njega. Ekran wallet prikazuje stanje i tri dugmeta za radnje: Pošalji Bitcoin, Primi Bitcoin i Prikaži sve kovanice.



![Réception de bitcoins](assets/fr/05.webp)



Pritisnite "Receive Bitcoin". Bitcoin Keeper generiše novu adresu za prijem u Bech32 formatu (počinje sa bc1...), zajedno sa njenim QR kodom. Možete dodati oznaku ovoj adresi kako biste identifikovali izvor sredstava. Podelite adresu sa pošiljaocem prikazivanjem QR koda ili kopiranjem tekstualne adrese.



Aplikacija automatski generiše novu adresu za svaki prijem, čuvajući vašu privatnost. Koristite "Get New Address" da dobijete praznu adresu ako je potrebno.



## UTXO upravljanje



Bitcoin Keeper nudi potpunu vidljivost UTXO (Neutrošeni Izlazi Transakcija) koji čine vaš saldo. Sa ekrana wallet, pritisnite "View All Coins" za pristup menadžeru ćoškova.



![Gestion des UTXO](assets/fr/06.webp)



Ekran "Upravljanje Kovanicama" prikazuje svaki UTXO pojedinačno sa njegovim iznosom i oznakom. Ovaj prikaz vam omogućava da pratite poreklo vaših kovanica i organizujete ih. Možete odabrati specifične UTXO-e putem "Odaberi za Slanje" kako biste slali sa kontrolom kovanica, čime izbegavate mešanje kovanica različitog porekla.



## Pošalji bitkoine



Da biste poslali, izaberite izvorni portfolio i pritisnite "Pošalji Bitcoin". Unesite adresu odredišta (nalepite ili skenirajte putem QR koda) i opcionalno dodajte oznaku za identifikaciju primaoca.



![Envoi de bitcoins](assets/fr/07.webp)



Sledeći ekran vam omogućava da unesete iznos koji želite poslati. Interfejs prikazuje vaš raspoloživi saldo i konverziju u fiat valutu. Izaberite prioritet naplate: Nizak (ekonomičan, ~60 minuta), Srednji, ili Visok (prioritetan). Procijenjene naknade u sats/vbyte prikazuju se u realnom vremenu. Pritisnite "Pošalji" da nastavite.



![Confirmation et envoi](assets/fr/08.webp)



Ekran sažetka prikazuje sve detalje: wallet izvor, odredišnu adresu, prioritet transakcije, mrežne troškove, poslati iznos i ukupno. Molimo pažljivo proverite ove informacije, jer su Bitcoin transakcije nepovratne. Pritisnite "Potvrdi i Pošalji" da biste poslali transakciju.



Pojavljuje se potvrda "Slanje uspešno" sa kompletnim rezimeom. Transakcija je vidljiva u istoriji "Nedavne transakcije" sa svojom oznakom.



## Sačuvaj svoje ključeve



Pravljenje rezervne kopije vašeg Ključa za oporavak je kritičan korak. Sa kartice Više, idite na odeljak "Rezervna kopija i oporavak" i kliknite na "Ključ za oporavak".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Ekran prikazuje status vaših rezervnih kopija. Da biste verifikovali vašu rezervnu kopiju, aplikacija traži da potvrdite određenu reč u vašoj frazi (npr. 7. reč). Ova verifikacija osigurava da ste ispravno zapisali vašu frazu za oporavak.



Iz "Postavke ključa za oporavak", možete videti vašu kompletnu frazu putem "Prikaži ključ za oporavak" i videti Otisak prsta potpisnika vašeg ključa. Čuvajte vašu frazu od 12 reči na papiru, na sigurnom mestu, daleko od vlage i vatre. Nikada je ne čuvajte na povezanom uređaju.



## Dodajte eksterni ključ (wallet hardver)



Jedna od glavnih prednosti Bitcoin Keeper je integracija hardverskih novčanika. Na kartici Keys pritisnite "Add key" da dodate novi uređaj za potpisivanje.



![Ajout d'une clé hardware](assets/fr/10.webp)



Odaberite "Dodaj ključ sa hardvera" da povežete hardverski wallet. Aplikacija podržava širok spektar uređaja: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner i Specter Solutions.



### Tapsigner konfiguracija



Tapsigner je NFC kartica od Coinkite-a posebno pogodna za mobilnu upotrebu. Ako želite da saznate više, imamo posvećen vodič :



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Da biste dodali Tapsigner, izaberite ga sa liste hardverskih novčanika.



![Configuration du Tapsigner](assets/fr/11.webp)



Prvo unesite PIN kod od 6-32 cifre odštampan na poleđini vaše kartice (podrazumevano na novim karticama), ili vaš PIN ako je već konfigurisan. Pritisnite "Nastavi", zatim prinesite vaš Tapsigner blizu poleđine vašeg telefona kada se prikaže "Spremno za skeniranje". NFC komunikacija automatski uvozi javni ključ. Zatim možete dodati opis (npr. "Métro Card") da identifikujete ovaj ključ.



## Kreiraj multisig portfolio



Jednom kada postavite svoje ključeve, možete kreirati višepotpisni wallet kombinovanjem nekoliko uređaja. Na kartici Novčanici, kliknite na "Dodaj Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Imate tri opcije: "Create Wallet" za novi portfolio, "Import Wallet" za vraćanje postojećeg wallet, ili "Collaborative Wallet" za deljeni trezor. Izaberite "Create Wallet" zatim "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



Sledeći ekran nudi različite konfiguracije: "Jedan ključ", "2 od 3 više ključeva", ili "3 od 5 više ključeva". Za prilagođeni multi-sig, pritisnite "Izaberi prilagođeno podešavanje". Na primer, izaberite "1 od 2": potreban je jedan potpis od dva moguća ključa.



Zatim izaberite ključeve koji će činiti vaš Vault. U našem primeru, kombinujemo "Mobilni Ključ" (softverski ključ telefona) sa "TAPSIGNER" (Metro kartica). Ova konfiguracija nudi redundanciju: ako jedan od ključeva postane nedostupan, uvek možete trošiti svoja sredstva sa drugim.



![Finalisation du wallet multisig](assets/fr/14.webp)



Imenujte svoj wallet (npr. "Test PlanB"), dodajte opcioni opis i proverite izabrane ključeve. Pritisnite "Kreiraj svoj Wallet". Pojaviće se poruka "Wallet uspešno kreiran", podsećajući vas da sačuvate wallet fajl za oporavak.



Vaš novi multisig wallet sada se pojavljuje na kartici Novčanici sa oznakom "Multi-key" i naznakom "1 od 2".



### Sačuvaj konfiguracionu datoteku



**Za razliku od jednostavnog wallet, gde je fraza za oporavak dovoljna za vraćanje pristupa, wallet multisig takođe zahteva konfiguracioni fajl koji opisuje strukturu sefa (koji ključevi učestvuju, koliko potpisa je potrebno). Bez ovog fajla, čak i sa svim frazama za oporavak, nećete moći da obnovite svoj wallet.



![Export du fichier de configuration](assets/fr/15.webp)



Da biste izvezli ovu datoteku, izaberite svoj wallet multisig u kartici Novčanici, zatim pritisnite ikonu Postavke (zupčanik) u gornjem desnom uglu. U "Wallet Postavke", kliknite na "Wallet konfiguraciona datoteka". Dostupno je nekoliko opcija izvoza:





- Izvoz PDF**: generiše PDF dokument koji sadrži sve informacije o wallet
- Prikaži QR**: prikazuje QR kod koji se može skenirati za uvoz konfiguracije na drugi uređaj
- Airdrop / Izvoz datoteke**: izvozi datoteku putem opcija za deljenje na vašem telefonu
- NFC**: podeli putem NFC-a sa kompatibilnim uređajem



Držite ovu konfiguracionu datoteku odvojeno od vaših fraza za oporavak, idealno na šifrovanom ili odštampanom medijumu. Ako izgubite telefon, ova datoteka u kombinaciji sa frazama za oporavak za svaki učesnički ključ omogućiće vam da obnovite vaš wallet multisig na Bitcoin Keeper ili bilo kojem drugom kompatibilnom softveru.



## Najbolje prakse



### Organizacija fonda



Strukturirajte svoje bitkoine prema njihovoj upotrebi: vrući wallet Single-Key za tekuće troškove sa ograničenim iznosima, i jedan ili više Vaults Multi-Key za dugoročne uštede. Sistematsko UTXO označavanje će vam pomoći da pratite odakle dolaze vaša sredstva, što je posebno korisno za upravljanje poverljivošću i izbegavanje mešanja novčića različitog porekla.



Čuvajte svoj telefon: aktivirajte biometrijsku zaštitu, redovno ažurirajte sistem i budite oprezni sa instaliranim aplikacijama. I održavajte Bitcoin Keeper ažuriranim sa sigurnosnim zakrpama.



### Sigurnost rezervne kopije



Čuvajte najmanje dve kopije svake fraze za oporavak na papiru, smeštene na geografski odvojenim lokacijama. Za veće sume, razmislite o ugraviranom, na katastrofe otpornom metalu. Nikada ne čuvajte ove fraze na uređaju povezanom na Internet i nikada ih ne fotografišite.



Za multi-sig trezore, takođe sačuvajte konfiguracioni fajl (Wallet Recovery File), koji sadrži učesničke javne ključeve i strukturu trezora. Ovaj fajl, u kombinaciji sa frazama za oporavak ključeva, omogućava da se wallet rekonstruiše na bilo kojem kompatibilnom softveru kao što su Sparrow ili Specter.



## Prednosti i ograničenja



### Istaknuto





- Aplikacija samo za Bitcoin smanjuje složenost i rizik
- Izvorna integracija multisig trezora sa uputstvom korak po korak
- Proširena podrška za hardver wallet (Tapsigner, Coldcard, Ledger, Jade, itd.)
- Napredno upravljanje UTXO i kontrola novčića
- Može se povezati sa ličnim Electrum serverom
- Otvoren, proverljiv izvorni kod



### Ograničenja koja treba razmotriti





- Interface uglavnom na engleskom
- Neke premium funkcije (Cloud Backup, Assisted Server) zahtevaju nadogradnju.
- Multisig konfiguracija zahteva početnu obuku



## Zaključak



Bitcoin Keeper se ističe kao skalabilno rešenje za upravljanje vašim bitkoinima. Njegov progresivni pristup, od jednostavnog hot wallet do multi-potpisnih Vaults, znači da se sigurnost može unaprediti kako se potrebe menjaju. Mogućnost jednostavne integracije hardverskih novčanika kao što je Tapsigner otvara put za robusne konfiguracije bez prekomerne složenosti.



Bitcoin-samo orijentacija, otvoreni izvorni kod i poštovanje privatnosti čine ga izborom koji je usklađen sa osnovnim vrednostima Bitcoin ekosistema.



Ovaj vodič pokriva osnovne funkcije Bitcoin Keeper u njegovoj besplatnoj verziji. Aplikacija takođe nudi premium funkcije (Cloud Backup, Assisted Server Backup, Canary Wallets) koje će biti tema posebnog vodiča. U narednom vodiču, takođe ćemo istraživati funkciju Planiranja Nasleđa, koja vam omogućava da pripremite prenos vaših bitcoina vašim voljenima, zahvaljujući Poboljšanim Trezorima i pratećim dokumentima integrisanim u aplikaciju.



## Resursi





- Zvanična veb stranica: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Help Center: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Izvorni kod: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)