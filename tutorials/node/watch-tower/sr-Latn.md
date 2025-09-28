---
name: Lightning Watchtower
description: Razumevanje i korišćenje Watchtower na vašem Lightning čvoru
---
![cover](assets/cover.webp)



## Kako funkcionišu osmatračnice?



Suštinski deo Lightning Network ekosistema, _Watchtowers_ pružaju dodatni nivo zaštite za korisničke Lightning kanale. Njihova glavna uloga je da prate status kanala i intervenišu ako jedna strana kanala pokuša da prevari drugu.



Kako Watchtower može utvrditi da li je kanal kompromitovan? Prima od korisnika (jedne od strana u kanalu) informacije potrebne za pravilno identifikovanje i rešavanje bilo kakvog kršenja. Ove informacije uključuju detalje o najnovijoj transakciji, trenutnom statusu kanala i Elements potrebnom za kreiranje kaznenih transakcija. Pre nego što prenese ove podatke na Watchtower, korisnik ih može enkriptovati kako bi sačuvao poverljivost. Dakle, čak i ako Watchtower primi podatke, neće moći da ih dekriptuje dok se kršenje zaista ne dogodi. Ovaj mehanizam enkripcije štiti privatnost korisnika i sprečava Watchtower da dobije neovlašćen pristup osetljivim informacijama.



U ovom vodiču ćemo pogledati 3 načina korišćenja **Watchtower** :




- prvo, klasična sirova metoda preko LND,
- onda još jedan pristup sa Eye of Satoshi,
- i konačno, pojednostavljena konfiguracija Watchtower na vašem Lightning čvoru hostovanom sa Umbrel.



## 1 - Konfigurisanje Watchtower ili klijenta putem LND



*Ovaj vodič je preuzet iz [zvanične LND dokumentacije](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Moguće je da su napravljene neke izmene u originalnoj verziji.



Od verzije v0.7.0, `LND` podržava izvršavanje privatnog altruističkog Watchtower kao potpuno integrisanog podsistema `LND`. Posmatrački tornjevi pružaju drugu liniju odbrane protiv zlonamernih ili slučajnih scenarija narušavanja kada je čvor korisnika van mreže ili nije u mogućnosti da odgovori u trenutku narušavanja, nudeći povećan stepen sigurnosti za sredstva kanala.



Za razliku od _nagradnog osmatračkog tornja_, koji zahteva deo sredstava kanala u zamenu za svoju uslugu, _altruistički osmatrački toranj_ vraća sva sredstva žrtve (umanjena za On-Chain naknade) bez naplate provizije. Nagradni osmatrački tornjevi će biti aktivirani u kasnijoj verziji; oni su još u fazi testiranja i poboljšanja.



Pored toga, `LND` sada može biti konfigurisan da funkcioniše kao _watchtower klijent_, čuvajući enkriptovane transakcije za sanaciju povreda (tzv. "justice transactions") od drugih altruističkih watchtower-a. Watchtower skladišti enkriptovane blokove fiksne veličine i može dekriptovati i objaviti transakciju pravde tek nakon što strana koja krši pravila emituje opozvano Commitment stanje. Komunikacija između korisnika i Watchtower je enkriptovana i autentifikovana korišćenjem efemernih parova ključeva, što ograničava sposobnost Watchtower da prati svoje korisnike putem dugoročnih kredencijala.



Imajte na umu da smo odlučili da u ovom izdanju implementiramo ograničen skup funkcija koje već pružaju značajnu sigurnost za korisnike `LND`. Mnoge druge funkcije povezane sa Watchtower su ili blizu završetka ili su u poodmakloj fazi; nastavićemo da ih isporučujemo kako ih budemo testirali i čim budu smatrane bezbednim.



napomena: za sada, osmatračnice čuvaju samo `to_local` i `to_remote` izlaze opozvanih obaveza; čuvanje HTLC izlaza će biti implementirano u budućoj verziji, jer se protokol može proširiti da uključi dodatne podatke o potpisu u šifrovane blokove._



### Konfigurisanje Watchtower



Da biste postavili Watchtower, korisnici komandne linije treba da kompajliraju opcioni `watchtowerrpc` pod-server, koji omogućava interakciju sa Watchtower putem gRPC ili `lncli`. Objavljeni binarni fajlovi uključuju `watchtowerrpc` pod-server po defaultu.



Minimalna konfiguracija za aktivaciju Watchtower je `Watchtower.active=1`.



Možete preuzeti informacije o vašoj Watchtower konfiguraciji pomoću `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Ceo skup opcija konfiguracije Watchtower dostupan je putem `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Interfejsi za slušanje



Podrazumevano, Watchtower sluša na `:9911`, što odgovara portu `9911` na svim dostupnim interfejsima. Korisnici mogu definisati svoje interfejse za slušanje putem opcije `--Watchtower.listen=`. Možete proveriti svoju konfiguraciju u polju `"listeners"` u `lncli tower info`. Ako imate problema sa povezivanjem na vaš Watchtower, uverite se da je `<port>` otvoren ili da je vaš proxy ispravno konfigurisan na aktivni Interface.



#### Eksterne IP adrese



Korisnici takođe mogu da navedu eksternu IP adresu Watchtower uređaja Address(es) sa `Watchtower.externalip=`, što otkriva pun URI Watchtower uređaja (pubkey@host:port) putem RPC ili `lncli tower info` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URI-jevi se mogu komunicirati sa korisnicima za povezivanje i korišćenje sa sledećom komandom:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Ako Watchtower korisnici treba da mu pristupe daljinski, obavezno:




- Otvorite port 9911 (ili port definisan putem `Watchtower.listen`).
- Koristite proxy za preusmeravanje saobraćaja sa otvorenog porta na Watchtower koji sluša Address.



#### Tor skrivene usluge



Stražarnice podržavaju skrivene usluge Tor-a i mogu automatski generate jednu pri pokretanju sa sledećim opcijama:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



.onion Address se zatim pojavljuje u polju `"uris"` tokom `lncli tower info` upita:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



napomena: javni ključ Watchtower razlikuje se od javnog ključa čvora `LND`. Za sada, on deluje kao "Soft lista dozvoljenih", jer korisnici moraju znati javni ključ Watchtower da bi ga koristili kao rezervnu opciju, dok se ne razviju napredniji mehanizmi za liste dozvoljenih. Preporučujemo da NE otkrivate ovaj javni ključ javno, osim ako niste spremni da izložite svoj Watchtower celom Internetu._



#### Watchtower direktorijum baze podataka



Bazu Watchtower može se premestiti korišćenjem opcije `Watchtower.towerdir=`. Imajte na umu da će sufiks `/Bitcoin/Mainnet/Watchtower.db` biti dodat izabranoj putanji kako bi se baze podataka izolovale po stringu. Dakle, postavljanje `Watchtower.towerdir=/path/to/towerdir` će proizvesti bazu podataka na `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Pod Linux-om, na primer, podrazumevana baza podataka za Watchtower se nalazi na :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Konfigurisanje Watchtower klijenta



Da biste konfigurisali Watchtower klijenta, potrebne su vam dve stavke:





- Aktivirajte Watchtower klijenta sa opcijom `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI aktivnog Watchtower.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Možete konfigurisati nekoliko osmatračnica na ovaj način.



#### Naknade za pravne transakcije



Korisnici mogu opcionalno postaviti stopu naknade za transakcije pravde putem opcije `wtclient.sweep-fee-rate`, koja prihvata vrednosti u sat/bajt. Podrazumevana vrednost je 10 sat/bajt, ali je moguće ciljati na više stope kako bi se postigao veći prioritet tokom vršnih opterećenja. Promena `sweep-fee-rate` se primenjuje na sva nova ažuriranja nakon ponovnog pokretanja daemon.



#### Nadzor



Pomoću komande `lncli wtclient`, korisnici sada mogu direktno komunicirati sa Watchtower klijentom kako bi dobili ili izmenili informacije o svim registrovanim osmatračnicama.



Na primer, sa `lncli wtclient tower`, možete saznati broj sesija trenutno pregovaranih sa Watchtower dodanim iznad i utvrditi da li se koristi za bekapove zahvaljujući polju `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Da biste dobili informacije o Watchtower sesijama, koristite opciju `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Sve opcije konfiguracije klijenta Watchtower dostupne su putem `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Instaliranje vašeg sopstvenog Eye of Satoshi



*Ovaj vodič je delimično preuzet iz članka na [Summer of Bitcoin Blogu](https://blog.summerofbitcoin.org/). Izmene su izvršene u originalnoj verziji*



The Eye of Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) je ne-depozitni Watchtower Lightning, u skladu sa [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Sastoji se od dve glavne komponente:





- teos**: uključuje komandnu liniju Interface (CLI) i osnovne serverske funkcije Watchtower. Dve binarne datoteke - **teosd** i **teos-CLI** - se proizvode kada se ovaj _crate_ kompajlira.





- teos-common**: uključuje zajedničku funkcionalnost za server i klijenta (korisno za kreiranje klijenta).



Da biste ispravno pokrenuli Watchtower, potrebno je pokrenuti **bitcoind** pre pokretanja Watchtower sa komandom **teosd**. Pre pokretanja ove dve komande, potrebno je da konfigurišete vaš **Bitcoin.conf** fajl. Evo kako to da uradite:





- Instalirajte Bitcoin core iz izvora ili ga preuzmite. Nakon preuzimanja, postavite datoteku **Bitcoin.conf** u korisnički direktorijum Bitcoin core. Pogledajte ovaj link za više informacija o tome gde postaviti datoteku, jer to zavisi od korišćenog operativnog sistema.





- Kada je lokacija identifikovana, dodajte sledeće opcije:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: za RPC zahteve





- rpcuser** i **rpcpassword**: autentifikacija RPC klijenata na server





- regtest**: nije obavezno, ali korisno ako planirate razvoj.



Vrednosti za **rpcuser** i **rpcpassword** treba da izaberete vi. Moraju biti napisane bez navodnika. Na primer:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Sada, ako pokrenete **bitcoind**, čvor bi trebalo da se pokrene.





- Za deo Watchtower, prvo morate instalirati **teos** iz izvornog koda. Pratite uputstva data na ovom linku.





- Kada uspešno instalirate **teos** na vaš sistem i pokrenete testove, možete preći na poslednji korak: podešavanje **teos.toml** fajla u teos korisničkom direktorijumu. Fajl treba da bude smešten u folderu nazvanom **.teos** (obratite pažnju na tačku) u vašem home direktorijumu. Na primer, **/home//.teos** na Linux-u. Kada pronađete lokaciju, kreirajte **teos.toml** fajl i postavite ove opcije u skladu sa promenama napravljenim na **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Imajte na umu da ovde korisničko ime i lozinka moraju biti napisani **unutar navodnika**. Koristeći prethodni primer :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Jednom kada je ovo urađeno, trebali biste biti spremni da pokrenete Watchtower. Pošto radimo na **regtest**, verovatno je da nijedan blok nije iskopan na našoj Bitcoin test mreži kada se Watchtower prvi put povezao (ako jesu, nešto nije u redu). Watchtower gradi internu keš memoriju poslednjih 100 blokova **bitcoind**; tako da, pri prvom pokretanju, možete dobiti sledeću grešku:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Pošto koristimo **regtest**, možemo Miner blokove izdavanjem RPC komande, bez potrebe da čekamo prosečno 10-minutno kašnjenje koje se viđa na drugim mrežama (kao što su Mainnet ili Testnet). Pogledajte **bitcoin-cli** pomoć za detalje o tome kako Miner blokove.



![Image](assets/fr/01.webp)



To je sve: uspešno ste pokrenuli Watchtower. Čestitamo. 🎉




## 3 - Konfigurisanje Watchtower na Umbrel



Na Umbrelu, povezivanje sa Watchtower radi zaštite vašeg Lightning čvora je izuzetno jednostavno, jer se sve obavlja putem grafičkog Interface. Nakon daljinskog povezivanja sa vašim čvorom, otvorite aplikaciju "**Lightning Node**".



![Image](assets/fr/02.webp)



Kliknite na tri male tačke u gornjem desnom uglu Interface, zatim izaberite "**Napredna podešavanja**".



![Image](assets/fr/03.webp)



U meniju "**Watchtower**" dostupne su dve opcije:





- Watchtower Service**: ova opcija vam omogućava da upravljate Watchtower, tj. servisom koji nadgleda kanale drugih čvorova kako bi otkrio bilo kakav pokušaj prevare. U slučaju proboja, vaš Watchtower objavljuje transakciju na Blockchain, omogućavajući korisnicima da povrate svoja zaključana sredstva. Kada se aktivira, URI vašeg Watchtower se pojavljuje i može se preneti drugim čvorovima kako bi ga mogli dodati svom Watchtower klijentu;





- Watchtower Klijent**: ova opcija vam omogućava povezivanje sa spoljnim osmatračnicama kako biste zaštitili svoje kanale. Kada se aktivira, možete dodati Watchtower usluge kojima će vaš čvor prenositi neophodne informacije o svojim kanalima. Ove osmatračnice će zatim pratiti njihov status i intervenisati u slučaju pokušaja prevare.



Prioritet za vas je naravno da aktivirate *Watchtower Client* kako biste zaštitili svoj čvor, ali takođe preporučujem da aktivirate *Watchtower Service* kako biste zauzvrat doprineli bezbednosti drugih korisnika.



![Image](assets/fr/04.webp)



Zatim kliknite na dugme Green "**Save and Restart Node**". Vaš LND će se restartovati.



U istom meniju, takođe ćete pronaći URI vaše Watchtower usluge ako ste je aktivirali. Takođe možete dodati URI spoljnog Watchtower da zaštitite svoje kanale. Kliknite na "**ADD**" da potvrdite.



![Image](assets/fr/05.webp)



Dostupno je nekoliko Kula stražara na mreži. Na primer, [LN+ i Voltage nude altruistički Watchtower](https://lightningnetwork.plus/Watchtower) na koji se možete povezati:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Još jedna opcija je da Exchange svoj Watchtower URI sa svojim kolegama bitkoinerima, tako da svaki štiti čvor onog drugog.



Takođe preporučujem da postavite nekoliko Stražara kako biste smanjili rizike u slučaju da jedan od njih postane nedostupan.



Konačno, možete podesiti parametar "**Watchtower Client Sweep Fee Rate**". Ovo definiše maksimalnu stopu naknade koju ste spremni da platite za Watchtower transakciju kazne emitovanja da bi bila uključena u blok. Uverite se da ste postavili dovoljno visoku vrednost, prilagođenu iznosima zaključanim u vašim kanalima.