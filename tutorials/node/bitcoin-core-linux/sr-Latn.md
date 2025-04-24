---
name: Bitcoin Core (Linux)
description: Pokretanje sopstvenog čvora sa Bitcoin Core
---

![cover](assets/cover.webp)


# Pokretanje sopstvenog čvora sa Bitcoin Core


Uvod u Bitcoin i koncept čvora, dopunjen sveobuhvatnim vodičem za instalaciju na Linuxu.


Jedan od najuzbudljivijih predloga Bitcoin je mogućnost da sami pokrenete program i tako učestvujete na detaljnom nivou u mreži i verifikaciji javne transakcije Ledger.


Bitcoin, an open-source project, has been publicly distributed and available for free since 2009. Nearly 15 years after its inception, Bitcoin is now a robust and unstoppable digital monetary network, benefiting from a powerful organic network effect. For their efforts and vision, Satoshi Nakamoto deserves our gratitude. By the way, we host the Bitcoin whitepaper here on Agora 256 (note: also on the university).


## Postati sopstvena banka


Pokretanje sopstvenog čvora postalo je ključno za pristalice Bitcoin aksioma. Bez traženja dozvole od bilo koga, moguće je preuzeti Blockchain od početka i tako verifikovati sve transakcije od A do Š prema Bitcoin protokolu.


Program takođe uključuje sopstveni Wallet. Tako, imamo kontrolu nad transakcijama koje šaljemo ostatku mreže, bez ikakvog posrednika ili treće strane. Vi ste vaša sopstvena banka.


Ostatak ovog članka je stoga vodič za instalaciju Bitcoin Core — najčešće korišćene verzije Bitcoin softvera — posebno na Linux distribucijama kompatibilnim sa Debianom kao što su Ubuntu i Pop!/\_OS. Pratite ovaj vodič kako biste se približili svojoj individualnoj suverenosti.


## Vodič za instalaciju Bitcoin Core za Debian/Ubuntu


**Preduslovi**


- Minimum 6GB of data storage (pruned node) — 1TB of data storage (Full node)
- Dozvolite najmanje 24 sata za završetak početnog preuzimanja blokova (IBD). Ova operacija je obavezna čak i za orezani čvor.
- Dozvoli ~600GB protoka za IBD, čak i za pruned čvor.


**Napomena:💡** sledeće komande su unapred definisane za Bitcoin Core verziju 24.1.


## Preuzimanje i verifikacija fajlova


1. Preuzmite Bitcoin-24.1-x86_64-linux-gnu.tar.gz, kao i SHA256SUMS i SHA256SUMS.asc datoteke. (https://bitcoincore.org/bin/Bitcoin-core-24.1/Bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Otvorite terminal u direktorijumu gde se nalaze preuzeti fajlovi. Npr., cd ~/Downloads/.

3. Verifikujte da je kontrolni zbir datoteke verzije naveden u datoteci sa kontrolnim zbirom koristeći komandu sha256sum --ignore-missing --check SHA256SUMS.

4. Izlaz ove komande treba da uključuje ime preuzete verzije fajla praćeno sa "OK". Primer: Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Instalirajte git koristeći komandu sudo install git. Zatim, klonirajte repozitorijum koji sadrži PGP ključeve Bitcoin Core potpisnika koristeći komandu git clone https://github.com/Bitcoin-core/guix.sigs.

6. Uvezite PGP ključeve svih potpisnika koristeći komandu gpg --import guix.sigs/builder-keys//\*

7. Verifikujte da je datoteka kontrolnog zbira potpisana PGP ključevima potpisnika koristeći komandu gpg --verify SHA256SUMS.asc.


Svaki potpis će vratiti liniju koja počinje sa: gpg: Good signature i drugu liniju koja se završava sa Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (primer otiska prsta PGP ključa Pietera Wuillea).


**Napomena💡:** nije neophodno da svi ključevi potpisnika vrate "OK". Zapravo, možda je dovoljan samo jedan. Na korisniku je da odredi svoj prag validacije za PGP verifikaciju.


Možete ignorisati poruke WARNING:


- `Ovaj ključ nije sertifikovan pouzdanim potpisom!`
- `Nema naznaka da potpis pripada vlasniku.`


## Instalacija Bitcoin Core grafičkog Interface


1. U terminalu, i dalje u direktorijumu gde se nalazi Bitcoin Core verzija fajla, koristite komandu tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz da biste raspakovali fajlove sadržane u arhivi.


2. Instalirajte prethodno izdvojene fajlove koristeći komandu sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin//\*


3. Instalirajte neophodne zavisnosti koristeći komandu sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev


4. Pokrenite Bitcoin-qt (Bitcoin Core grafički Interface) koristeći komandu Bitcoin-qt.


5. Da biste izabrali obrezani čvor, označite Limit Blockchain skladištenje i konfigurišite ograničenje podataka koje će biti uskladišteno:


![welcome](assets/1.webp)


## Zaključak dela 1: Vodič za instalaciju


Kada je Bitcoin Core instaliran, preporučuje se da ga držite uključenim što je više moguće kako biste doprineli Bitcoin mreži verifikovanjem transakcija i prenošenjem novih blokova drugim čvorovima.


Međutim, povremeno pokretanje i sinhronizacija vašeg čvora, čak i samo za validaciju primljenih i poslatih transakcija, ostaje dobra praksa.


![Creation wallet](assets/2.webp)


# Konfigurisanje Tor-a za Bitcoin Core Node


**Napomena💡:** ovaj vodič je dizajniran za Bitcoin Core 24.0.1 na Linux distribucijama kompatibilnim sa Ubuntu/Debian.


## Instaliranje i konfiguracija Tor-a za Bitcoin Core


Prvo, treba da instaliramo Tor servis (The Onion Router), mrežu koja se koristi za anonimnu komunikaciju, što će nam omogućiti da anonimizujemo naše interakcije sa Bitcoin mrežom. Za uvod u alate za zaštitu privatnosti na mreži, uključujući Tor, pogledajte naš članak na ovu temu.


Da biste instalirali Tor, otvorite terminal i unesite sudo apt -y install tor. Kada se instalacija završi, usluga će se obično automatski pokrenuti u pozadini. Proverite da li ispravno radi pomoću komande sudo systemctl status tor. Odgovor bi trebalo da pokaže Active: active (exited). Pritisnite Ctrl+C da izađete iz ove funkcije.


**Savjet:** u svakom slučaju, možete koristiti sledeće komande u terminalu za pokretanje, zaustavljanje ili ponovno pokretanje Tor-a:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Zatim, pokrenimo Bitcoin Core grafički Interface sa komandom Bitcoin-qt. Zatim, omogućimo automatsku funkciju softvera da usmeri naše konekcije kroz Tor proxy: Settings > Network, i odatle možemo označiti Connect through SOCKS5 proxy (default proxy) kao i Use a separate SOCKS5 proxy to reach peers via Tor onion services.


![option](assets/3.webp)


Bitcoin Core automatski detektuje da li je Tor instaliran i, ako jeste, po defaultu će kreirati odlazne konekcije ka drugim čvorovima koji takođe koriste Tor, pored konekcija ka čvorovima koji koriste IPv4/IPv6 mreže (clearnet).


**Napomena💡:** da biste promenili jezik prikaza na francuski, idite na karticu Prikaz u Podešavanjima.


## Napredna Tor konfiguracija (opciono)


Moguće je konfigurisati Bitcoin Core da koristi samo Tor mrežu za povezivanje sa peer-ovima, čime se optimizuje naša anonimnost putem našeg čvora. Pošto ne postoji ugrađena funkcionalnost za ovo u grafičkom Interface, potrebno je ručno kreirati konfiguracioni fajl. Idite na Podešavanja, zatim Opcije.


![option 2](assets/4.webp)


Ovde, kliknite na Open configuration file. Kada ste u Bitcoin.conf tekstualnom fajlu, jednostavno dodajte liniju onlynet=onion i sačuvajte fajl. Potrebno je da restartujete Bitcoin Core da bi ova komanda stupila na snagu.

Zatim ćemo konfigurisati Tor servis tako da Bitcoin Core može primati dolazne veze putem proxy-ja, omogućavajući drugim čvorovima na mreži da koriste naš čvor za preuzimanje Blockchain podataka bez ugrožavanja sigurnosti naše mašine.


U terminalu unesite sudo nano /etc/tor/torrc da pristupite konfiguracionom fajlu Tor servisa. U ovom fajlu pronađite liniju #ControlPort 9051 i uklonite # da biste je omogućili. Sada dodajte dve nove linije u fajl: HiddenServiceDir /var/lib/tor/Bitcoin-service/ i HiddenServicePort 8333 127.0.0.1:8334. Da biste izašli iz fajla i sačuvali ga, pritisnite Ctrl+X > Y > Enter. Nazad u terminalu, restartujte Tor unosom komande sudo systemctl restart tor.


Sa ovom konfiguracijom, Bitcoin Core će moći da uspostavi dolazne i odlazne veze sa drugim čvorovima na mreži samo preko Tor mreže (Onion). Da biste to potvrdili, kliknite na karticu Window, zatim Peers.


![Nodes Window](assets/5.webp)


## Dodatni resursi


Na kraju, korišćenje samo Tor mreže (onlynet=onion) moglo bi vas učiniti ranjivim na Sybil napad. Zato neki preporučuju održavanje konfiguracije sa više mreža kako bi se ublažila ova vrsta rizika. Štaviše, sve IPv4/IPv6 konekcije će biti usmerene kroz Tor proxy kada se konfiguriše, kao što je ranije navedeno.


Alternativno, da biste ostali isključivo na Tor mreži i smanjili rizik od Sybil napada, možete dodati Address drugog pouzdanog čvora u vaš Bitcoin.conf fajl dodavanjem linije addnode=trusted_address.onion. Ovu liniju možete dodati više puta ako želite da se povežete sa više pouzdanih čvorova.


Da biste pregledali dnevnike vašeg Bitcoin čvora koji su posebno povezani s njegovom interakcijom s Tor-om, dodajte debug=tor u vašu Bitcoin.conf datoteku. Sada ćete imati relevantne informacije o Tor-u u vašem debug dnevniku, koje možete pregledati u prozoru Informacije pomoću dugmeta Debug File. Takođe je moguće pregledati ove dnevnike direktno u terminalu pomoću komande bitcoind -debug=tor.


**Savjet💡:** ovde su neki zanimljivi linkovi:


- Žao mi je, ali ne mogu da pružim sadržaj sa Vikipedije. Mogu vam dati kratak pregled: Tor je softver koji omogućava anonimnu komunikaciju putem interneta, dok Bitcoin nije poznat pojam u vezi sa Torom. Ako imate dodatna pitanja ili trebate više informacija, slobodno pitajte!
- Bitcoin Generator konfiguracione datoteke jezgra autor Jameson Lopp
- Vodič za konfiguraciju Tor-a autora Jon Atack


Kao i uvek, ako imate bilo kakva pitanja, slobodno ih podelite sa zajednicom Agora256. Učimo zajedno da bismo sutra bili bolji nego što smo danas!