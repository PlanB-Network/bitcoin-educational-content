---
name: Sparrow Wallet
description: Instaliranje, konfigurisanje i korišćenje Sparrow Wallet
---
![cover](assets/cover.webp)


Sparrow Wallet je softver za upravljanje Bitcoin Wallet sa samostalnim čuvanjem koji je razvio Craig Raw. Ovaj softver otvorenog koda cenjen je među bitkoin entuzijastima zbog svojih brojnih funkcija i intuitivnog Interface.


Postoje dva načina za korišćenje Sparrow-a:




- Kao Hot Wallet, gde su vaši privatni ključevi pohranjeni na vašem računaru.
- Kao menadžer Cold Wallet, gde se privatni ključevi čuvaju na Hardware Wallet. U ovom režimu, Sparrow samo manipuliše javnim Wallet informacijama, prati sredstva, generiše adrese i kreira transakcije, ali je potreban Hardware Wallet potpis da bi ove transakcije bile validne. Stoga može zameniti aplikacije kao što su Ledger Live ili Trezor Suite.


Sparrow podržava novčanike sa jednim potpisom i sa više potpisa, i omogućava fluidno upravljanje više novčanika. Na primer, možete istovremeno kontrolisati jedan Wallet povezan sa Ledger, drugi sa Trezorom, i takođe imati Hot Wallet.


Softver takođe nudi napredne funkcije kontrole novčića, omogućavajući vam da precizno odaberete koje UTXO-e ćete koristiti u svojim transakcijama kako biste optimizovali svoju poverljivost.


Što se tiče povezivanja, Sparrow vam omogućava da se povežete na svoj Bitcoin čvor, bilo daljinski putem Electrum Servera, ili sa Bitcoin Core. Takođe je moguće koristiti javni čvor ako još nemate svoj. Daljinske veze se ostvaruju putem Tor-a.


## Instaliraj Sparrow Wallet


Idite na [zvaničnu stranicu za preuzimanje Sparrow Wallet](https://sparrowwallet.com/download/) i izaberite verziju softvera koja odgovara vašem operativnom sistemu.


![Image](assets/fr/01.webp)


Važno je proveriti integritet i autentičnost softvera pre nego što ga instalirate. Ako ne znate kako to da uradite, ovde ćete pronaći kompletan vodič:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Jednom kada je Sparrow instaliran, možete preskočiti početne ekrane sa objašnjenjima i preći direktno na ekran za upravljanje vezama.


![Image](assets/fr/02.webp)


![video](https://www.youtube.com/watch?v=MyDMvjGFdDE)



![video](https://youtu.be/IThaolnDgSo)


## Povezivanje na Bitcoin mrežu


Da biste komunicirali sa Bitcoin mrežom i emitovali svoje transakcije, Sparrow mora biti povezan sa Bitcoin čvorom. Postoje tri glavna načina za uspostavljanje ove veze:



- 🟡 Korišćenje javnog čvora, tj. povezivanje sa čvorom treće strane koji omogućava takve veze. Ako nemate svoj Bitcoin čvor, ova opcija vam omogućava da brzo počnete sa Sparrow. Međutim, čvor na koji se povezujete će videti sve vaše transakcije, što bi moglo ugroziti vašu poverljivost. Kontrola nad vašim ključevima je ključna, ali imati svoj čvor je još bolje. Zato koristite ovu opciju samo ako ste tek počeli, uz svest o rizicima po vašu privatnost.
- 🟢 Povezivanje na Bitcoin Core čvor. Ako imate svoj Bitcoin Core čvor, možete ga povezati sa Sparrow Wallet, bilo lokalno ako je Bitcoin Core instaliran na istom računaru, ili na daljinu.
- 🔵 Povezivanje putem Electrum servera. Ako je vaš Bitcoin čvor opremljen sa Electrs, kao što je slučaj sa rešenjima "čvor-u-kutiji" kao što su Umbrel ili Start9, možete se povezati sa njim na daljinu iz Sparrow-a.


**Poželjno je koristiti vezu putem Electrs ili Bitcoin Core na sopstvenom čvoru kako biste smanjili potrebu za poverenjem trećoj strani i optimizovali svoju poverljivost**


### Poveži se na javni čvor 🟡


Povezivanje na javni čvor je veoma jednostavno. Kliknite na karticu "*Public Server*".


![Image](assets/fr/03.webp)


Izaberite čvor sa padajuće liste.


![Image](assets/fr/04.webp)


Zatim kliknite na "*Test Connection*".


![Image](assets/fr/05.webp)


Kada se poveže, Sparrow Wallet će prikazati žutu kvačicu u donjem desnom uglu Interface kako bi naznačio da ste povezani na javni čvor.


![Image](assets/fr/06.webp)


### Povezivanje na Bitcoin Core 🟢


Drugi metod povezivanja sa Bitcoin čvorom je povezivanje Sparrow-a sa Bitcoin Core. Ako je Bitcoin Core instaliran na istoj mašini, autentifikacija će biti putem cookie fajla. Ako je Bitcoin Core na udaljenoj mašini, potrebno je koristiti lozinku definisanu u `Bitcoin.conf` fajlu.


Imajte na umu da ako koristite obrezani Bitcoin Core čvor, nećete moći da obnovite Wallet koji sadrži transakcije pre datuma lokalno sačuvanih blokova. Međutim, za novi Wallet kreiran na Sparrow-u, ovo neće biti problem: vaše nove transakcije će biti vidljive, čak i sa obrezanim čvorom.


Da biste konfigurisali Bitcoin Core čvor, možete se posavetovati sa jednim od sledećih tutorijala, u zavisnosti od vašeg operativnog sistema:


https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Na Sparrow-u, idite na karticu "*Bitcoin Core*".


![Image](assets/fr/07.webp)


**Sa Bitcoin Core lokalno:**


Ako je Bitcoin Core instaliran na vašem računaru, pronađite datoteku `Bitcoin.conf` među softverskim datotekama. Ako ova datoteka ne postoji, možete je kreirati. Otvorite je pomoću uređivača teksta i umetnite sledeći red:


```ini
server=1
```


Zatim sačuvaj svoje izmene.


To možete učiniti i putem Bitcoin-QT-ove Interface grafike tako što ćete otići na "*Settings*" > "*Options...*" i aktivirati opciju "*Enable RPC server*".


Ne zaboravite da restartujete softver nakon što napravite ove promene.


![Image](assets/fr/08.webp)


Zatim se vratite na Sparrow Wallet i unesite putanju do vaše datoteke kolačića, koja se obično nalazi u istoj fascikli kao i `Bitcoin.conf`, u zavisnosti od vašeg operativnog sistema:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)


Ostavite ostale parametre kao podrazumevane, URL `127.0.0.1` i port `8332`, zatim kliknite na "*Test Connection*".


![Image](assets/fr/10.webp)


Veza je uspostavljena. Green oznaka će se pojaviti u donjem desnom uglu da označi da ste povezani na Bitcoin Core čvor.


![Image](assets/fr/11.webp)


**Sa Bitcoin Core daljinskim:**


Ako je Bitcoin Core instaliran na drugoj mašini povezanoj na istu mrežu, prvo pronađite datoteku `Bitcoin.conf` među softverskim datotekama. Ako ova datoteka još ne postoji, možete je kreirati. Otvorite ovu datoteku pomoću uređivača teksta i dodajte sledeći red:


```ini
server=1
```


Nakon uređivanja datoteke, obavezno je sačuvajte u odgovarajućem folderu za vaš operativni sistem:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

Ova operacija se takođe može izvesti putem Bitcoin-QT Interface grafičkog Interface. Idite na meni "*Settings*", zatim "*Options...*", i aktivirajte opciju "*Enable RPC server*" označavanjem odgovarajućeg polja. Ako `Bitcoin.conf` fajl ne postoji, možete ga kreirati direktno iz ovog Interface klikom na "*Open Configuration File*".


![Image](assets/fr/12.webp)


Pronađite IP Address mašine koja hostuje Bitcoin Core na vašoj lokalnoj mreži. Da biste to uradili, možete koristiti alat kao što je [Angry IP Scanner](https://angryip.org/). Pretpostavimo, radi argumentacije, da je IP Address vašeg čvora `192.168.1.18`.


U datoteku `Bitcoin.conf` dodajte sledeće linije, postavljajući `rpcbind=192.168.1.18` da odgovara IP adresi Address vašeg čvora.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/13.webp)


U datoteku `Bitcoin.conf` dodajte korisničko ime i lozinku za daljinske veze. Obavezno zamenite `loic` sa vašim korisničkim imenom i `my_password` sa jakom lozinkom:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/14.webp)


Nakon izmene i čuvanja datoteke, ponovo pokrenite Bitcoin-QT softver.


Sada se možete vratiti na Sparrow Wallet. Idite na karticu "*User / Pass*". Unesite korisničko ime i lozinku koje ste konfigurisali u datoteci `Bitcoin.conf`. Ostavite ostale parametre kao podrazumevane, tj. URL `127.0.0.1` i port `8332`. Zatim kliknite na "*Test Connection*".


![Image](assets/fr/15.webp)


Veza je uspostavljena. Green oznaka će se pojaviti u donjem desnom uglu da označi da ste povezani na Bitcoin Core čvor.


![Image](assets/fr/16.webp)


![video](https://www.youtube.com/watch?v=9Aw6OAXxE_Y)


### Povezivanje na Electrum server 🔵


Konačna opcija za povezivanje je korišćenje udaljenog Electrum servera. Ova metoda vam omogućava da se povežete sa svojim čvorom putem Tor-a sa drugog uređaja, i koristi prednosti indeksatora za brže pregledanje vaših novčanika na Sparrow-u. Posebno je pogodna ako imate rešenje čvor-u-kutiji kao što su Umbrel ili Start9, koji vam omogućavaju da instalirate Electrs jednim klikom.


Da biste to uradili, nabavite Tor `.onion' Address vašeg Electrum servera. Sa Umbrel-om, na primer, naći ćete ga u Electrs aplikaciji.


![Image](assets/fr/17.webp)


Na Sparrow Wallet, pristupite kartici "*Private Electrum*".


![Image](assets/fr/18.webp)


Unesite svoj Tor Address u predviđeni prostor. Ostale postavke mogu ostati podrazumevane. Zatim kliknite na "*Test Connection*".


![Image](assets/fr/19.webp)


Veza je potvrđena. Ako zatvorite ovaj prozor, plava kvačica će se pojaviti u donjem desnom uglu, što ukazuje da ste povezani sa Electrum serverom.


![Image](assets/fr/20.webp)


## Kreiraj Hot Wallet


Sada kada je Sparrow Wallet konfigurisan za komunikaciju sa Bitcoin mrežom, spremni ste da kreirate svoj prvi Wallet. Ovaj deo vas vodi kroz kreiranje Hot Wallet, tj. Wallet čiji su privatni ključevi smešteni na vašem računaru. Pošto je vaš računar složena mašina povezana na Internet, predstavlja veoma veliku površinu za napad. Shodno tome, Hot Wallet treba koristiti samo za ograničene količine bitkoina. Za čuvanje većih količina, odlučite se za sigurni Wallet sa Hardware Wallet. Ako je to ono što tražite, možete preskočiti na sledeći deo.


Da biste kreirali Hot Wallet, sa početnog ekrana Sparrow Wallet, kliknite na karticu "*File*" a zatim na "*New Wallet*".


![Image](assets/fr/21.webp)


Unesite ime za vaš Wallet i kliknite na "*Create Wallet*".


![Image](assets/fr/22.webp)


Na vrhu Interface, možete izabrati da li želite kreirati "*Single Signature*" ili "*Multi Signature*" Wallet. Odmah ispod, odaberite tip skripte za zaključavanje vaših UTXO-a. Preporučujem da koristite najnoviji standard: "*Taproot (P2TR)*".


![Image](assets/fr/23.webp)


Zatim kliknite na "*Novi ili Uvezeni Software Wallet*".


![Image](assets/fr/24.webp)


Izaberite BIP39 standard, jer ga podržava gotovo sav Bitcoin Wallet softver. Zatim, izaberite dužinu vaše fraze za oporavak. Trenutno, fraza od 12 reči je dovoljna, jer obe nude sličnu sigurnost, ali fraza od 12 reči je jednostavnija za čuvanje.


![Image](assets/fr/25.webp)


Kliknite na dugme "*generate New*" da biste generate svoju Wallet-ovu Mnemonic frazu. Ova fraza omogućava potpuni, neograničeni pristup svim vašim bitkoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem računaru.


Fraza od 12 reči vraća pristup vašim bitcoinima u slučaju gubitka, krađe ili kvara vašeg računara. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.


Možete ga ispisati na papir ili, radi dodatne sigurnosti, ugravirati na nerđajući čelik kako biste ga zaštitili od požara, poplave ili urušavanja. Izbor medija za vaš Mnemonic zavisiće od vaše sigurnosne strategije, ali ako koristite Sparrow kao Wallet za tople troškove koji sadrži umerene iznose, papir bi trebao biti dovoljan.


Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)


**Očigledno, nikada ne smete deliti ove reči na Internetu, kao što ja činim u ovom uputstvu. Ovaj primer Wallet će biti korišćen samo na Testnet i biće obrisan na kraju uputstva.**


Takođe možete odabrati da dodate passphrase BIP39 klikom na polje "*Use passphrase*". Upozorenje: korišćenje passphrase može biti veoma korisno, ali ako ne razumete kako funkcioniše, može biti veoma rizično. Zato vam toplo preporučujem da pročitate ovaj kratki teorijski članak na tu temu:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jednom kada sačuvate svoj Mnemonic i bilo koji passphrase na fizički medijum, kliknite na "*Confirm Backup*".


![Image](assets/fr/27.webp)


Ponovo unesite svojih 12 reči da potvrdite da su ispravno sačuvane, zatim kliknite na "*Create Keystore*".


![Image](assets/fr/28.webp)


Zatim kliknite na "*Import Keystore*" da generate vaše Wallet ključeve iz Mnemonic fraze.


![Image](assets/fr/29.webp)


Kliknite na "*Apply*" da biste završili kreiranje Wallet.


![Image](assets/fr/30.webp)


Postavite jaku lozinku kako biste osigurali pristup vašem Sparrow Wallet. Preporučuje se da ovu lozinku čuvate u menadžeru lozinki, kako je ne biste zaboravili. Imajte na umu da ova lozinka ne igra ulogu u derivaciji vaših ključeva. Koristi se samo za pristup vašem Wallet putem Sparrow Wallet. Dakle, čak i bez ove lozinke, vaša Mnemonic fraza će biti dovoljna za pristup vašim bitcoinima iz bilo koje BIP39-kompatibilne aplikacije.


![Image](assets/fr/31.webp)


Vaš Hot Wallet je sada kreiran. Možete preskočiti na odeljak *Primanje Bitcoina* u ovom uputstvu ako ne planirate da koristite Hardware Wallet sa Sparrow.


## Upravljanje Cold Wallet


Drugi način korišćenja Sparrow Wallet je da ga postavite kao Wallet menadžer sa Hardware Wallet. U ovoj konfiguraciji, privatni ključevi vaših Bitcoin Wallet ostaju isključivo na Hardware Wallet, dok Sparrow pristupa samo javnim informacijama. Ovaj pristup nudi viši nivo sigurnosti od gore pomenutih Hot novčanika, jer se privatni ključevi čuvaju na specijalizovanom uređaju, često sa sigurnosnim čipom, koji nije povezan na Internet i stoga predstavlja mnogo manju površinu za napad od tradicionalnog računara.


Postoje dva glavna načina za povezivanje vašeg Hardware Wallet sa Sparrow:




- Kablom, koji se obično koristi sa početnim modelima kao što su Trezor Safe 3 ili Ledger Nano S Plus ;
- U Air-Gap režimu, tj. bez direktne žičane veze, putem MicroSD kartice ili QR koda Exchange.


Sparrow podržava sve ove metode komunikacije i kompatibilan je sa većinom hardverskih novčanika na tržištu.


Za ovaj vodič, koristiću Ledger Nano S sa kablom, ali procedura je slična u Air-Gap režimu. Detalje specifične za vaš Hardware Wallet pronaći ćete u njegovom posvećenom vodiču na Plan ₿ Network.


Pre nego što počnete, uverite se da je Wallet već konfigurisan na vašem Hardware Wallet. Ako koristite žičanu vezu, povežite ga sa vašim računarom putem kabla.


Da biste uvezli takozvani "*Keystore*" (javne informacije potrebne za upravljanje Wallet) u Sparrow Wallet, kliknite na karticu "*File*", zatim na "*New Wallet*".


![Image](assets/fr/32.webp)


Nazovite svoj Wallet i kliknite na "*Create Wallet*". Savetujem vam da unesete ime vašeg Hardware Wallet kako biste ga kasnije lako identifikovali.


![Image](assets/fr/33.webp)


Na vrhu Interface, izaberite između "*Single Signature*" ili "*Multi Signature*" Wallet. Za naš primer, konfigurišemo single-sig Wallet.


Odmah ispod, izaberite tip skripte za zaključavanje vaših UTXO-a. Ako vaš Hardware Wallet to podržava, predlažem da izaberete "*Taproot (P2TR)*".


![Image](assets/fr/34.webp)


Zatim se procedura razlikuje u zavisnosti od vašeg načina povezivanja. Ako koristite Air-Gap metodu, izaberite "*Airgapped Hardware Wallet*". Zatim pratite uputstva specifična za vaš uređaj.


![Image](assets/fr/35.webp)


Ako koristite kablovsku vezu, kao u mom slučaju, izaberite "*Connected Hardware Wallet*".


![Image](assets/fr/36.webp)


Kliknite na "*Scan*" da bi Sparrow detektovao vaš uređaj. Uverite se da je priključen i otključan. Za neke modele, kao što je Ledger, potrebno je otvoriti aplikaciju "*Bitcoin*" da biste omogućili detekciju.


![Image](assets/fr/37.webp)


Odaberite "*Import Keystore*".


![Image](assets/fr/38.webp)


Kliknite na "*Apply*" da završite kreiranje Wallet.


![Image](assets/fr/39.webp)


Postavite jaku lozinku kako biste osigurali pristup vašem Sparrow Wallet. Ova lozinka će zaštititi vaše javne ključeve, adrese i istoriju transakcija. Preporučujemo da je sačuvate u menadžeru lozinki. Imajte na umu da ova lozinka ne igra ulogu u izvođenju vaših ključeva. Čak i bez nje, možete povratiti pristup vašim bitcoinima sa vašim Mnemonic putem bilo kojeg softvera kompatibilnog sa BIP39.


![Image](assets/fr/40.webp)


Vaše upravljanje Wallet je sada konfigurisano na Sparrow.


![Image](assets/fr/41.webp)


## Primite bitkoine


Sada kada je vaš Wallet postavljen na Sparrow, možete primati bitkoine. Jednostavno pristupite meniju "*Receive*".


![Image](assets/fr/42.webp)


Sparrow će prikazati prvi neiskorišćeni Address u vašem Wallet. Možete dodati "*Label*" ovom Address da vas podseća na poreklo ovih satoshija u budućnosti.


![Image](assets/fr/43.webp)


Ako koristite Hot Wallet, prikazani Address može se odmah koristiti, bilo kopiranjem ili skeniranjem pridruženog QR koda.


Ako koristite Hardware Wallet, veoma je važno proveriti Address na ekranu uređaja pre nego što ga upotrebite. Za uređaje sa kablom, povežite i otključajte vaš Hardware Wallet, zatim u Sparrow-u kliknite na "*Prikaži Address*". Uverite se da Address prikazan na vašem Hardware Wallet odgovara onom prikazanom u Sparrow-u.


![Image](assets/fr/44.webp)


Za korisnike Hardware Wallet Air-Gap, verifikacija Address varira u zavisnosti od modela uređaja. Pogledajte posvećeni Plan ₿ Network vodič za precizna uputstva.


Jednom kada je transakcija emitovana od strane platioca, videćete je u kartici "*Transakcije*". Možete kliknuti na nju za više detalja, kao što je txid.


![Image](assets/fr/45.webp)


U kartici "*Addresses*" pronaći ćete listu svih adresa vašeg inboxa. Možete videti da li su već korišćene i da li je dodat label. "*Receive*" adrese su one koje Sparrow prikazuje kada kliknete na "*Receive*" i namenjene su za dolazne uplate. "*Change*" adrese se koriste za Exchange u vašim transakcijama, tj. za povrat neiskorišćenog dela vaših UTXO-a u ulazima.


![Image](assets/fr/46.webp)


Kartica "*UTXOs*" prikazuje sve vaše UTXO-e, tj. fragmente Bitcoin koje posedujete. Možete videti iznos svakog UTXO i pridruženu oznaku.


![Image](assets/fr/47.webp)


## Pošalji bitkoine


Sada kada imate nekoliko satoshija u vašem Wallet, takođe imate opciju da pošaljete neke. Iako postoji nekoliko načina da to uradite, preporučujem da koristite meni "*UTXOs*" za precizniju kontrolu nad novčićima koje trošite (*kontrola novčića*), umesto da idete direktno na meni "*Pošalji*" (iako ovo drugo može biti dovoljno ako ste početnik).


![Image](assets/fr/48.webp)


Izaberite UTXO-ove koje želite koristiti kao ulaze za ovu transakciju, zatim kliknite na "*Pošalji odabrano*". Ovaj pristup vam omogućava da izaberete najprikladnije izvore među vašim UTXO-ovima, u skladu sa vašim troškovima i oznakama primenjenim kada su primljeni, kako biste optimizovali poverljivost vaših plaćanja. Uverite se da je zbir odabranih UTXO-ova veći od iznosa koji želite poslati.


![Image](assets/fr/49.webp)


Unesite Address primaoca u polje "*Pay to*". Takođe možete skenirati Address pomoću vaše veb kamere klikom na ikonu kamere. Dugme "*+Add*" vam omogućava da platite na više adresa u jednoj transakciji.


![Image](assets/fr/50.webp)


Dodajte oznaku svojoj transakciji kako biste se podsetili njene svrhe. Ova oznaka će takođe biti povezana sa vašim budućim Exchange.


![Image](assets/fr/51.webp)


Unesite iznos koji treba poslati na ovaj Address.


![Image](assets/fr/52.webp)


Prilagodite stopu naknade prema trenutnim tržišnim uslovima. To možete učiniti unosom apsolutne vrednosti naknade ili podešavanjem stope naknade pomoću klizača.


![Image](assets/fr/53.webp)


Na dnu Interface, možete birati između "*Efficiency*" i "*Privacy*". U mom slučaju, opcija "*Privacy*" nije dostupna, jer imam samo jedan UTXO u ovom Wallet. "*Efficiency*" odgovara klasičnoj transakciji, dok je "*Privacy*" transakcija tipa Stonewall, struktura transakcije koja pojačava vašu poverljivost simulacijom mini-CoinJoin, što analizu lanca čini složenijom.


![Image](assets/fr/54.webp)


Sparrow prikazuje dijagram sažetka koji pokazuje vaše ulaze, izlaze i naknade za transakciju (imajte na umu da naknade zapravo nisu izlaz, suprotno onome što ovaj dijagram sugeriše). Ako ste zadovoljni sa svime, kliknite na "*Create Transaction*".


![Image](assets/fr/55.webp)


Ovo vas vodi na stranicu sa detaljima Elements vaše transakcije. Proverite da su sve informacije tačne, a zatim kliknite na "*Finalize Transaction for Signing*".


![Image](assets/fr/56.webp)


Važno je zadržati podrazumevani Sighash. Da biste razumeli zašto, pogledajte ovaj kurs obuke, u kojem objašnjavam sve što treba da znate o Sighash:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Na sledećem ekranu, opcije se razlikuju u zavisnosti od tipa Wallet koji koristite:




- Za Hardware Wallet Air-Gap, kliknite na "*Show QR*" da prikažete PSBT koji možete potpisati svojim uređajem, zatim učitajte potpisani PSBT u Sparrow koristeći "*Scan QR*". Opcija "*Save Transaction*" radi na sličan način, ali sa razmenama na microSD;
- Za Hot Wallet, jednostavno kliknite na "*Sign*" i unesite Wallet lozinku da potpišete ;
- Za ožičeni Hardware Wallet, takođe kliknite na "*Sign*" da pošaljete nepotpisanu transakciju na vaš uređaj.


![Image](assets/fr/57.webp)


Na vašem Hardware Wallet, proverite primaoca Address, poslati iznos i naknade. Ako je sve tačno, nastavite sa potpisivanjem.


Jednom kada transakcija bude potpisana, ponovo će se pojaviti u Sparrow, spremna za emitovanje na Bitcoin mreži za naknadno uključivanje u blok. Ako je sve ispravno, kliknite na "*Broadcast Transaction*".


![Image](assets/fr/58.webp)


Vaša transakcija je sada emitovana i čeka potvrdu.


![Image](assets/fr/59.webp)


![video](https://youtu.be/7QCKSPIq0Ac)


## Upravljanje i konfiguracija novčanika na Sparrow


U kartici "*Settings*" pronaći ćete detaljne informacije o vašem Wallet, kao što su :



- Tip portfolija (single-sig ili multi-sig) ;
- Tip skripte korišćen;
- Ime koje ste dodelili Wallet ;
- Otisak glavnog ključa;
- Putanja zaobilaska ;
- Prošireni javni ključ naloga.


![Image](assets/fr/60.webp)


Dugme "*Export*" omogućava vam da izvezete informacije o Wallet kako biste ih mogli koristiti u drugom softveru, a da pritom zadržite informacije postavljene u Sparrow.


Dugme "*Add Account*" omogućava vam da dodate dodatni nalog na vaš Wallet. Nalog odgovara posebnom skupu adresa prijemnog sandučeta. Ova funkcija može biti korisna, na primer, ako želite da razdvojite lični i poslovni nalog, sa jednom Mnemonic frazom.


Dugme "*Advanced*" omogućava pristup naprednim podešavanjima, kao što su prilagođavanje pretrage Sparrow's Address i promena lozinke Wallet.


![Image](assets/fr/61.webp)


Kada zatvorite Sparrow Wallet, vaš Wallet se automatski zaključava. Sledeći put kada otvorite softver, prozor će vas podsetiti da otključate vaš Wallet pomoću njegove lozinke.


![Image](assets/fr/62.webp)


Ako se ovaj prozor ne otvori, ili ako želite da otvorite drugi Wallet na Sparrow, kliknite na karticu "*File*" i izaberite "*Open Wallet*".


![Image](assets/fr/63.webp)


Ovo će otvoriti vaš Upravitelj datoteka u fasciklu gde Sparrow čuva vaše novčanike. Jednostavno izaberite Wallet koji želite da otvorite i unesite lozinku da ga otključate.


![Image](assets/fr/64.webp)


U meniju "*File*" pod "*Settings*", pronaći ćete parametre mrežne veze Bitcoin koji su već istraženi u prethodnim odeljcima. Takođe možete prilagoditi različite parametre kao što su korišćena jedinica, fiat valuta za konverzije i izvori informacija.


![Image](assets/fr/65.webp)


Kartica "*View*" nudi opcije prilagođavanja i pristup nekim korisnim komandama, kao što je "*Refresh Wallet*", koja osvežava pretragu transakcija za vaš Wallet.


![Image](assets/fr/66.webp)


Kartica "*Alati*" grupiše nekoliko naprednih alata, uključujući:



- "*Potpiši/Verifikuj Poruku*" omogućava vam da dokažete posedovanje prijemnog Address ili verifikujete potpis.
- "*Send To Many*" nudi pojednostavljeni Interface za obavljanje transakcija na više adresa primatelja odjednom, što je pogodno za grupno trošenje.
- "*Sweep Private Key*" omogućava vam da preuzmete bitkoine osigurane jednostavnim privatnim ključem i prenesete ih na vaš Sparrow Wallet. Ovo može biti posebno korisno za one sa bitkoinima koji datiraju iz ranih 2010-ih, pre ere HD novčanika.
- "Verify Download" verifikuje integritet i autentičnost preuzetog softvera pre nego što ga instalirate na svoj uređaj.
- "*Restart In*" omogućava vam da se prebacite na svoje novčanike na Testnet ili Signet mrežama. Ovo može biti korisno ako želite pristupiti testnim mrežama sa novčićima bez stvarne vrednosti.


![Image](assets/fr/67.webp)


Sada znate sve o softveru Sparrow Wallet, odličnom alatu za svakodnevno upravljanje vašim Bitcoin novčanicima.


Ako ste našli ovaj vodič korisnim, bio bih veoma zahvalan ako biste ostavili Green palac ispod. Slobodno ga podelite na vašim društvenim mrežama. Hvala vam puno!


Takođe preporučujem ovaj drugi vodič u kojem objašnjavam kako konfigurisati Hardware Wallet COLDCARD Q sa Sparrow Wallet :


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3