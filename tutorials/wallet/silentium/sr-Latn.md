---
name: Silentium
description: Progresivni web wallet sa podrškom za Silent Payments (BIP-352)
---

![cover](assets/cover.webp)



Ponovna upotreba Bitcoin adresa je jedna od najdirektnijih pretnji korisničkoj poverljivosti. Kada primalac deli jednu adresu za primanje više uplata, bilo koji posmatrač može pratiti sve povezane transakcije i rekonstruisati njihovu finansijsku istoriju. Ovaj problem posebno pogađa kreatore sadržaja, dobrotvorne organizacije ili aktiviste koji žele javno prikazati adresu za donacije bez ugrožavanja svoje privatnosti.



Silentium odgovara na ovaj problem elegantnim rešenjem dostupnim direktno iz vašeg pregledača. Ova aplikacija otvorenog koda, progresivna veb aplikacija (PWA), pokrenuta u maju 2024. godine od strane Louisa Singera, implementira Silent Payments (BIP-352): višekratno upotrebljivu statičku adresu gde svaka uplata završava na zasebnoj adresi na blokčejnu, bez prethodne interakcije ili vidljive veze između transakcija.



**Važno upozorenje**: Silentium je eksperimentalni projekat koji služi kao *proof-of-concept* za Silent Payments lagane novčanike. Ne bi trebalo da se koristi kao dnevni wallet ili za čuvanje značajnih iznosa. Programeri izričito navode:



> Koristite na sopstveni rizik.

Imajte na umu da se ovaj wallet može koristiti kao testnet ili regtest.



## Šta je Silentium?



### Filozofija i ciljevi



Silentium služi kao tehnička demonstracija za implementaciju Silent Payments u laganom wallet pregledaču. Iako takođe podržava konvencionalne Bitcoin adrese, naglasak je na Silent Payments kako bi korisnicima omogućio da eksperimentišu sa ovom tehnologijom privatnosti na jednostavan način.



### Kako funkcionišu Silent Payments?



Silent Payments (BIP-352) koriste Elliptic Curve Diffie-Hellman Key Exchange (ECDH). Primalac generiše statičku adresu (`sp1...` na mainnet, `tsp1...` na testnetu) koja se sastoji od dva javna ključa: ključa za skeniranje radi detekcije uplata i ključa za trošenje radi korišćenja istih.



Pošiljalac kombinuje svoje privatne ulazne ključeve sa sken ključem primaoca kako bi izračunao zajedničku tajnu koja generiše kriptografski "tweak". Ovaj tweak, dodat ključu za trošenje, stvara jedinstvenu Taproot adresu za svaku transakciju. Primalac ponavlja ovaj proračun sa svojim privatnim sken ključem kako bi detektovao i potrošio sredstva bez ikakve prethodne interakcije.



Prednosti: poboljšana poverljivost za pošiljaoca i primaoca, nije potreban server treće strane, transakcije se ne razlikuju od konvencionalnih Taproot plaćanja. Glavni nedostatak: intenzivno skeniranje blockchain-a za otkrivanje plaćanja.



Da biste saznali više o teorijskom funkcionisanju Silent Payments, pogledajte poslednji deo BTC,204 kursa na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Podržane platforme



Silentium je Progressive Web App (PWA) dostupan iz bilo kog modernog pregledača (mobilnog ili desktop). Koristite ga direktno na `app.silentium.dev`, instalirajte ga kao native aplikaciju putem vašeg pregledača, ili ga postavite lokalno. Instalacija se vrši direktno iz pregledača, bez prolaska kroz zvanične prodavnice.



## Korišćenje Web aplikacije



### Pristup i instalacija



[Idite na `https://app.silentium.dev/` iz vašeg pregledača](https://app.silentium.dev/). Aplikacija se učitava trenutno i prikazuje početni ekran.



Da biste ga instalirali kao izvornu aplikaciju na iOS-u, pritisnite dugme za deljenje (kvadrat sa strelicom nagore), a zatim izaberite "Na početni ekran". Na Androidu, pregledač obično direktno nudi obaveštenje "Dodaj na početni ekran". Kada se instalira, Silentium se pojavljuje sa svojom posebnom ikonom i radi kao izvorna aplikacija, ali zahteva internet vezu za sinhronizaciju transakcija.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Kreiranje portfolija



Prilikom prvog pokretanja, izaberite "Create Wallet" da generate novi portfolio, ili "Restore Wallet" da obnovite iz postojeće fraze za oporavak.



Odaberite "Create Wallet". Aplikacija generiše frazu od 12 reči koju morate pažljivo zapisati. Ova fraza je jedini način da povratite svoja sredstva. Čak i na testnetu, usvojite dobre prakse pravljenja rezervnih kopija. Pritisnite "Continue" nakon što sačuvate svoju frazu.



Aplikacija zatim traži da postavite lozinku kako biste osigurali pristup wallet. Izaberite jaku lozinku i potvrdite je.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Kada je fraza potvrđena i lozinka postavljena, bićete preusmereni na glavni interfejs.



### Interface glavni i parametri



Glavni interfejs prikazuje vaš saldo u satoshijima (u početku 0 sats), sa tri dugmeta na dnu:




- Sync**: sinhronizuje wallet sa blokčejnom
- Primiti**: primiti sredstva
- Pošalji**: poslati bitkoine



Pristupite podešavanjima putem ikone u gornjem desnom uglu (tri horizontalne linije). Meni Podešavanja nudi nekoliko opcija:





- O**: informacije o aplikaciji
- Backup**: backup fraze za oporavak
- Explorer**: izaberite blockchain explorer (Mempool po podrazumevano) i Silentiumd server
- Mreža**: izbor mreže (mainnet/testnet)
- Lozinka**: promeni lozinku
- Ponovno učitavanje**: ponovo učitavanje wallet
- Reset**: kompletno resetovanje
- Tema**: promeni temu



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Deo **Explorer** je posebno važan: omogućava vam da izaberete blockchain explorer koji se koristi (Mempool po defaultu) i takođe prikazuje URL Silentiumd servera (`https://bitcoin.silentium.dev/v1` za mainnet). Ako hostujete sopstveni Silentiumd server ili želite da koristite testnet, ovde konfigurišete ove parametre.



### Primanje sredstava



Sa glavnog interfejsa, pritisnite dugme "Receive". Podrazumevano, Silentium prikazuje adresu za Silent Payment sa njenim QR kodom. Adresa počinje sa `sp1...` na mainnet ili `tsp1...` na testnetu.



Možete se prebacivati između Silent Payment i klasičnih Bitcoin adresa koristeći dugme "Prebaci na klasičnu adresu" / "Prebaci na tihu adresu" na dnu ekrana.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Jednom kada je transakcija emitovana, molimo sačekajte nekoliko minuta. Za tihe uplate, Silentium automatski skenira blockchain za transakcije namenjene vama. Transakcije se pojavljuju sa statusom "Nepotvrđeno" pre nego što budu postepeno potvrđene.



### Pošalji uplatu



Sa glavnog interfejsa, pritisnite dugme "Pošalji". Ekran za slanje će vas pitati :



1. **Address**: nalepite adresu za Tiho Plaćanje (`sp1...` ili `tsp1...`) ili klasičnu Bitcoin adresu. Možete koristiti ikonu za skeniranje QR koda da skenirate adresu.


2. **Amount**: unesite iznos u satoshijima koji želite poslati. Prikazuje se numerička tastatura za jednostavan unos. Vaše dostupno stanje je prikazano na vrhu za referencu.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Kada unesete adresu i iznos, pritisnite "Nastavi" da biste nastavili. Aplikacija će vas zamoliti da izaberete željeni nivo naknade pre nego što potvrdite transakciju.



## wallet samostalno hostovanje



### Zašto samostalno hostovati?



Silentiumovo lokalno hostovanje nudi potpunu suverenost, verifikaciju koda, razvojno okruženje i otpornost u slučaju neuspeha zvanične lokacije.



### Preduslovi



Node.js (verzija 14+), npm ili yarn, Git, i oko 500 MB prostora na disku.



### Lokalna instalacija



Klonirajte repozitorijum i instalirajte :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Pokreni i koristi



Pokrenite aplikaciju u režimu razvoja:



```bash
yarn start
```



Idite na `http://localhost:3000` u vašem pregledaču. Za optimizovanu produkcijsku verziju :



```bash
yarn build
```



Datoteke generisane u `build/` mogu biti poslužene pomoću nginx, Apache ili bilo kog web servera. Podrazumevano, Silentium se povezuje na javni server `bitcoin.silentium.dev`. Izmenite ovo podešavanje u parametrima da biste koristili testnet ili svoj sopstveni server.



## Silentiumd server



### Uloga i rad



Silentium koristi **Silentiumd** indeksirajući server za optimizaciju detekcije plaćanja. Skeniranje svih Taproot transakcija bilo bi previše nezgrapno za pretraživač ili mobilni telefon.



Silentiumd unapred izračunava međupodatke (podešavanja) za svaku Taproot transakciju. Vaš wallet preuzima ova podešavanja (nekoliko bajtova po transakciji) i vrši konačni proračun lokalno, verifikujući vlasništvo nad uplatom. Server nikada ne zna vaše ključeve niti može identifikovati vaše transakcije, za razliku od konvencionalnih Electrum servera.



Kompaktni BIP158 filteri omogućavaju vašem wallet da odredi koje blokove da skenira bez otkrivanja vaših adresa, čime se čuva vaša poverljivost.



### Javni server



Javni server `bitcoin.silentium.dev` (mainnet), sponzorisan od strane Vulpem Ventures, nudi jednostavno i trenutno iskustvo. Iako je poverljivost očuvana, ovaj pristup podrazumeva relativno poverenje u infrastrukturu treće strane.



### Hostujte sopstveni Silentiumd server



Za potpunu suverenost, hostujte svoj sopstveni Silentiumd server. Preduslovi: Bitcoin Core non-elagged čvor sa `txindex=1` i `blockfilterindex=1`, Go 1.21+, 10-20 GB prostora na disku, veštine sistemske administracije.



**Instalacija:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Konfigurišite putem promenljivih okruženja (pogledajte `config.md` repozitorijuma za detalje). Server indeksira blokčejn i izlaže API koji može biti upitan od strane vašeg wallet.



Trenutno ne postoje pakovana rešenja za Umbrel ili Start9, što ograničava pristupačnost za netehničke korisnike.



## Prednosti i ograničenja



### Istaknuto





- Maksimalna pristupačnost**: koristite iz bilo kog pregledača, nije potrebna teška instalacija
- Više platformi**: radi na mobilnim uređajima (Android/iOS) i desktopu zahvaljujući PWA tehnologiji
- Jednostavno samostalno hostovanje**: lokalna instalacija moguća sa nekoliko komandi
- Open-source**: potpuno proverljiv kod na GitHub-u
- Privatnost u fokusu**: bez praćenja, bez analitike, lokalne kriptografske kalkulacije
- Odvojena arhitektura**: jasno razdvajanje između wallet (klijent) i indeksirajućeg servera
- Bez naloga**: nije potrebna registracija ili lični podaci



### Ograničenja koja treba razmotriti





- Eksperimentalni projekat**: samo dokaz koncepta, nije namenjen za svakodnevnu upotrebu ili proizvodnju
- Bez garancija**: rizik od grešaka, ranjivosti, mogući gubitak sredstava
- Ograničena podrška**: malo korisničke dokumentacije, mala zajednica, nema zvanične podrške
- Zavisnost servera**: zahteva funkcionalan Silentiumd server (javni ili samostalno hostovan)
- Intenzivno skeniranje**: Detekcija tihih plaćanja troši propusni opseg
- Smanjena funkcionalnost**: nema kontrole nad novčićima, nema Lightning-a, nema višestrukih potpisa



## Najbolje prakse



### seed bezbednost



Čak i na testnetu, tretirajte svoju frazu za oporavak ozbiljno. Zapišite je i čuvajte na sigurnom mestu. Držite odvojene novčanike za testnet i mainnet: nikada ne koristite testni seed na wallet namenjenom za stvarna sredstva.



### Verifikacija izvornog koda



Jedna od prednosti samostalnog hostovanja je mogućnost provere izvornog koda pre nego što ga pokrenete. Ako planirate da koristite Silentium sa pravim sredstvima, odvojite vreme da pregledate kod ili angažujte pouzdanog programera da to uradi. Takođe, uporedite hash koda postavljenog na `app.silentium.dev` sa onim iz GitHub repozitorijuma kako biste osigurali autentičnost.



### Bekap i obnova



Oporavak sredstava putem Silent Payments zahteva wallet kompatibilan sa BIP-352 protokolom. Standardni wallet ne može skenirati blockchain da bi povratio vaše UTXO Silent Payments. Držite Silentium instaliranim ili se pobrinite da imate pristup drugom kompatibilnom wallet (kao što je Cake Wallet ili druge buduće implementacije) kako biste po potrebi vratili svoja sredstva.



## Zaključak



Silentium pruža pristupačno okruženje za testiranje i razumevanje Silent Payments bez tehničkih prepreka. Kao dokaz koncepta, pokazuje kako se ova tehnologija privatnosti može integrisati u wallet pregledač uz očuvanje samostalnog čuvanja sredstava. Eksperimentišite na testnetu kako biste otkrili ovo obećavajuće otkriće za on-chain privatnost.



## Resursi



### Zvanična dokumentacija




- Silentium GitHub repository (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub repository (server): https://github.com/louisinger/silentiumd
- Veb aplikacija: https://app.silentium.dev/
- Silent Payments zajednica: https://silentpayments.xyz
- Specifikacija BIP-352: https://bips.dev/352



### Članci i resursi




- Zvanično saopštenje (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Silent Payments: https://bitcoinops.org/en/topics/silent-payments/



### Testnet alati




- Testnet slavina: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet