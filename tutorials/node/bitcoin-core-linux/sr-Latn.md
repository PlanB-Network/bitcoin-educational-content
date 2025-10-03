---
name: Bitcoin Core (Linux)
description: Pokretanje sopstvenog čvora sa Bitcoin core na Linuxu
---

![cover](assets/cover.webp)


## Pokretanje sopstvenog čvora sa Bitcoin core


Uvod u Bitcoin i koncept čvora, dopunjen sveobuhvatnim vodičem za instalaciju na Linuxu.


Jedan od najuzbudljivijih aspekata Bitcoin je mogućnost da sami pokrenete program i tako učestvujete na detaljnom nivou u mreži i verifikaciji javne transakcije Ledger.


Bitcoin, kao projekat otvorenog koda, slobodno je dostupan i javno distribuiran od 2009. godine. Skoro 17 godina nakon svog nastanka, Bitcoin je sada robustna i nezaustavljiva digitalna monetarna mreža, koja koristi snažan organski mrežni efekat. Za njihove napore i viziju, Satoshi Nakamoto zaslužuje našu zahvalnost. Usput, mi hostujemo Bitcoin beli papir ovde na Agora 256 (napomena: takođe na univerzitetu).


### Postajanje sopstvene banke


Pokretanje sopstvenog čvora postalo je ključno za pristalice Bitcoin etosa. Bez traženja ičijeg dopuštenja, moguće je preuzeti Blockchain od početka i tako verifikovati sve transakcije od A do Z prema Bitcoin protokolu.


Program takođe uključuje sopstveni Wallet. Tako imamo kontrolu nad transakcijama koje šaljemo ostatku mreže, bez posrednika ili treće strane. Vi ste svoja banka.


Ostatak ovog članka je stoga vodič za instalaciju Bitcoin core — najčešće korišćene verzije softvera Bitcoin — posebno na Linux distribucijama kompatibilnim sa Debianom kao što su Ubuntu i Pop!OS. Pratite ovaj vodič kako biste se približili svojoj individualnoj suverenosti.


## Vodič za instalaciju Bitcoin core za Debian/Ubuntu


**Preduslovi**


- Minimum 6GB of data storage (pruned node) — 1TB of data storage (Full node)
- Očekujte da će *Početno Preuzimanje Bloka* (IBD) trajati najmanje 24 sata. Ova operacija je obavezna čak i za pruned čvor.
- Dozvoli ~600GB protoka za IBD, čak i za pruned čvor.


**Napomena:💡** sledeće komande su unapred definisane za Bitcoin core verziju 24.1.


### Preuzimanje i verifikacija fajlova



- [Download](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, kao i datoteke `SHA256SUMS` i `SHA256SUMS.asc` (očigledno je da treba da preuzmete najnoviju verziju softvera).



- Otvorite terminal u direktorijumu gde se nalaze preuzeti fajlovi. Primer: `cd ~/Downloads/`.



- Potvrdite da je kontrolni zbir datoteke verzije naveden u datoteci sa kontrolnim zbirom koristeći komandu `sha256sum --ignore-missing --check SHA256SUMS`.



- Izlaz ove komande treba da uključuje ime preuzete verzije fajla praćeno sa `OK`. Primer: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Instalirajte git koristeći komandu `sudo apt install git`. Zatim, klonirajte repozitorijum koji sadrži PGP ključeve potpisnika Bitcoin core koristeći komandu `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Uvezite PGP ključeve svih potpisnika koristeći komandu `gpg --import guix.sigs/builder-keys/*`



- Proverite da je datoteka sa kontrolnim zbirom potpisana PGP ključevima potpisnika koristeći komandu `gpg --verify SHA256SUMS.asc`.



Svaki važeći potpis će prikazati liniju koja počinje sa: `gpg: Good signature` i drugu liniju koja se završava sa: `Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (primer otiska prsta PGP ključa Pietera Wuillea).


**Napomena💡:** nije neophodno da svi ključevi potpisnika vrate "OK". Zapravo, možda je dovoljan samo jedan. Na korisniku je da odredi svoj prag validacije za PGP verifikaciju.


Možete ignorisati upozorenja:



- `Ovaj ključ nije sertifikovan pouzdanim potpisom!`



- `Nema naznaka da potpis pripada vlasniku.`


### Instalacija Bitcoin core grafičkog Interface



- U terminalu, i dalje u direktorijumu gde se nalazi Bitcoin core verzija datoteke, koristite komandu `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` da ekstrahujete datoteke sadržane u arhivi.



- Instalirajte prethodno izdvojene fajlove koristeći komandu `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Instalirajte potrebne zavisnosti koristeći komandu `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Pokreni _bitcoin-qt_ (Bitcoin core grafički Interface) koristeći komandu `Bitcoin-qt`.



- Da biste izabrali pruned čvor, označite _Limitiraj Blockchain skladište_ i konfigurišite ograničenje podataka za skladištenje:


![welcome](assets/fr/02.webp)


### Zaključak dela 1: Vodič za instalaciju


Kada je Bitcoin core instaliran, preporučuje se da ga držite uključenim što je više moguće kako biste doprineli Bitcoin mreži verifikovanjem transakcija i prenosom novih blokova drugim čvorovima.


Međutim, povremeno pokretanje i sinhronizacija vašeg čvora, čak i samo za validaciju primljenih i poslatih transakcija, ostaje dobra praksa.


![Creation wallet](assets/fr/03.webp)


## Konfigurisanje Tor-a za Bitcoin core čvor


**Napomena💡:** ovaj vodič je dizajniran za Bitcoin core 24.0.1 na Linux distribucijama kompatibilnim sa Ubuntu/Debian.


### Instaliranje i konfiguracija Tor-a za Bitcoin core


Prvo, treba da instaliramo Tor servis (The Onion Router), mrežu koja se koristi za anonimnu komunikaciju, što će nam omogućiti da anonimizujemo naše interakcije sa Bitcoin mrežom. Za uvod u alate za zaštitu privatnosti na mreži, uključujući Tor, pogledajte naš članak na ovu temu.


Da biste instalirali Tor, otvorite terminal i unesite `sudo apt -y install tor`. Kada se instalacija završi, usluga će se obično automatski pokrenuti u pozadini. Proverite da li radi ispravno pomoću komande `sudo systemctl status tor`. Odgovor bi trebalo da pokaže `Active: active (exited)`. Pritisnite `Ctrl+C` da izađete iz ove funkcije.


**Savjet:** u svakom slučaju, možete koristiti sledeće komande u terminalu za pokretanje, zaustavljanje ili ponovno pokretanje Tor-a:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Zatim, pokrenimo grafički Bitcoin core Interface sa komandom `Bitcoin-qt`. Zatim, omogućite automatsku funkciju softvera da usmeri naše konekcije kroz Tor proxy: _Settings > Network_, i odatle označite _Connect through SOCKS5 proxy (default proxy)_ kao i _Use a separate SOCKS5 proxy to reach peers via Tor onion services_.


![option](assets/fr/04.webp)


Bitcoin core automatski detektuje da li je Tor instaliran i, ako jeste, po defaultu će kreirati odlazne veze ka drugim čvorovima koji takođe koriste Tor, pored veza ka čvorovima koji koriste IPv4/IPv6 mreže (clearnet).


**Napomena💡:** da biste promenili jezik prikaza na francuski, idite na karticu Prikaz u Podešavanjima.


### Napredna Tor konfiguracija (opciono)


Moguće je konfigurisati Bitcoin core da koristi samo Tor mrežu za povezivanje sa vršnjacima, čime se optimizuje naša anonimnost preko našeg čvora. Pošto ne postoji ugrađena funkcionalnost za ovo u grafičkom Interface, biće potrebno ručno kreirati konfiguracioni fajl. Idite na Podešavanja, zatim Opcije.


![option 2](assets/fr/05.webp)


Ovde, kliknite na _Open configuration file_. Kada ste u `Bitcoin.conf` tekstualnom fajlu, jednostavno dodajte liniju `onlynet=onion` i sačuvajte fajl. Potrebno je da restartujete Bitcoin core da bi ova komanda stupila na snagu.


Zatim ćemo konfigurisati Tor servis tako da Bitcoin core može primati dolazne veze putem proxy-ja, omogućavajući drugim čvorovima na mreži da koriste naš čvor za preuzimanje podataka sa Blockchain bez ugrožavanja bezbednosti naše mašine.


U terminalu unesite `sudo nano /etc/tor/torrc` da pristupite konfiguracionoj datoteci Tor servisa. U ovoj datoteci pronađite liniju `#ControlPort 9051` i uklonite `#` da biste je omogućili. Sada dodajte dve nove linije u datoteku:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Da biste izašli iz datoteke i sačuvali je, pritisnite `Ctrl+X > Y > Enter`. Nazad u terminalu, ponovo pokrenite Tor unosom komande `sudo systemctl restart tor`.


Sa ovom konfiguracijom, Bitcoin core će moći da uspostavi dolazne i odlazne veze sa drugim čvorovima na mreži samo putem Tor mreže (Onion). Da biste to potvrdili, kliknite na karticu _Window_, zatim _Peers_.


![Nodes Window](assets/fr/06.webp)


### Dodatni resursi


Na kraju, korišćenje samo Tor mreže (`onlynet=onion`) moglo bi vas učiniti ranjivim na Sybil Attack. Zato neki preporučuju održavanje konfiguracije sa više mreža kako bi se ublažila ova vrsta rizika. Štaviše, sve IPv4/IPv6 veze će biti usmerene kroz Tor proxy kada se konfiguriše, kao što je ranije navedeno.


Alternativno, da biste ostali isključivo na Tor mreži i smanjili rizik od Sybil Attack, možete dodati Address drugog pouzdanog čvora u vašu `Bitcoin.conf` datoteku dodavanjem linije `addnode=trusted_address.onion`. Ovu liniju možete dodati više puta ako želite da se povežete sa više pouzdanih čvorova.


Da biste pregledali dnevnike vašeg Bitcoin čvora koji su posebno povezani s njegovom interakcijom s Tor-om, dodajte `debug=tor` u vašu `Bitcoin.conf` datoteku. Sada ćete imati relevantne informacije o Tor-u u vašem debug dnevniku, koje možete pregledati u prozoru _Information_ pomoću dugmeta _Debug File_. Takođe je moguće pregledati ove dnevnike direktno u terminalu pomoću komande `bitcoind -debug=tor`.


**Saveti💡:** ovde su neki zanimljivi linkovi:


- [Wiki page explaining Tor and its relationship with Bitcoin](https://en.Bitcoin.it/wiki/Tor)
- [Bitcoin core configuration file generator by Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Vodič za konfiguraciju Tor-a od Jon Atack](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Kao i uvek, ako imate bilo kakva pitanja, slobodno ih podelite sa zajednicom Agora256. Učimo zajedno da bismo sutra bili bolji nego što smo danas!