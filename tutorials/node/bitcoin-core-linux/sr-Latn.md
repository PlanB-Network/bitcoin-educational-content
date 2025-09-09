---
name: Bitcoin Core (Linux)
description: Pokretanje sopstvenog čvora sa Bitcoin Core-om
---

![cover](assets/cover.webp)


# Pokretanje sopstvenog Bitcoin Core čvora 


Uvod u Bitcoin i koncept čvora, dopunjen sveobuhvatnim vodičem za instalaciju na Linuxu.


Jedna od najuzbudljivijih mogućnosti koje Bitcoin nudi jeste mogućnost da sami pokrenete program i na taj način učestvujete na detaljnom nivou u mreži i verifikaciji javne knjige transakcija.


Bitcoin, projekat otvorenog koda, javno je distribuiran i dostupan besplatno od 2009. godine. Skoro 15 godina nakon svog nastanka, Bitcoin je danas snažna i nezaustavljiva digitalna monetarna mreža, koja koristi moćan organski mrežni efekat. Za svoju viziju i trud, Satoshi Nakamoto zaslužuje našu zahvalnost.
Usput, Bitcoin whitepaper hostujemo ovde na Agora 256 (napomena: nalazi se i na sajtu univerziteta).


## Postati sopstvena banka


Pokretanje sopstvenog čvora postalo je ključno za pristalice Bitcoin aksioma. Bez traženja dozvole od bilo koga, moguće je preuzeti Blockchain od početka i tako verifikovati sve transakcije od A do Š prema Bitcoin protokolu.


Program takođe uključuje sopstveni novčanik. Tako, dobijamo kontrolu nad transakcijama koje šaljemo ostatku mreže, bez ikakvog posrednika ili treće strane. Vi ste vaša sopstvena banka.


Ostatak ovog članka je stoga vodič za instalaciju Bitcoin Core-a — najčešće korišćene verzije Bitcoin softvera — posebno na Linux distribucijama kompatibilnim sa Debianom kao što su Ubuntu i Pop!/_OS. Pratite ovaj vodič kako biste se približili svojoj individualnoj suverenosti.


## Vodič za instalaciju Bitcoin Core za Debian/Ubuntu


**Preduslovi**


- Minimum 6 GB prostora za skladištenje podataka ([pruned čvor](https://planb.network/resources/glossary/pruned-node)) — 1 TB prostora za skladištenje podataka (puni čvor)
- Dozvolite najmanje 24 sata za završetak početnog preuzimanja blokova (IBD). Ova operacija je obavezna čak i za pruned čvor.
- Dozvoli ~600GB protoka za IBD, čak i za pruned čvor.


**Napomena:💡** sledeće komande su unapred definisane za Bitcoin Core verziju 24.1.


## Preuzimanje i verifikacija fajlova


1. Preuzmite Bitcoin-24.1-x86_64-linux-gnu.tar.gz, kao i SHA256SUMS i SHA256SUMS.asc datoteke. (https://bitcoincore.org/bin/Bitcoin-core-24.1/Bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Otvorite terminal u direktorijumu gde se nalaze preuzeti fajlovi. Npr., cd ~/Downloads/.

3. Verifikujte da je kontrolni zbir datoteke verzije naveden u datoteci sa kontrolnim zbirovima koristeći komandu sha256sum --ignore-missing --check SHA256SUMS.

4. Izlaz ove komande treba da uključuje ime preuzete verzije fajla praćeno sa "OK". Primer: Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Instalirajte git koristeći komandu sudo install git. Zatim, klonirajte repozitorijum koji sadrži PGP ključeve potpisnika Bitcoin Core-a koristeći komandu git clone https://github.com/Bitcoin-core/guix.sigs.

6. Uvezite PGP ključeve svih potpisnika koristeći komandu gpg --import guix.sigs/builder-keys//\*

7. Verifikujte da je datoteka kontrolnog zbira potpisana PGP ključevima potpisnika koristeći komandu gpg --verify SHA256SUMS.asc.


Svaki potpis će vratiti liniju koja počinje sa: gpg: Good signature i drugu liniju koja se završava sa Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (primer jedinstvenog identifikatora PGP ključa Pietera Wuillea).


**Napomena💡:** nije neophodno da svi ključevi potpisnika vrate "OK". Zapravo, možda je dovoljan samo jedan. Na korisniku je da odredi svoj prag validacije za PGP verifikaciju.


Možete ignorisati poruke WARNING:


- `Ovaj ključ nije sertifikovan pouzdanim potpisom!`, na engleskom `This key is not certified with a trusted signature!`
- `Nema naznaka da potpis pripada vlasniku.`, na engleskom `There is no indication that the signature belongs to the owner.`


## Instalacija Bitcoin Core grafičkog interfejsa


1. U terminalu, i dalje u direktorijumu gde se nalazi Bitcoin Core verzija fajla, koristite komandu tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz da biste raspakovali fajlove sadržane u arhivi.


2. Instalirajte prethodno izdvojene fajlove koristeći komandu sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin//\*


3. Instalirajte neophodne zavisnosti, na engleskom "dependencies", koristeći komandu sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev


4. Pokrenite Bitcoin-qt (Bitcoin Core grafički interfejs) koristeći komandu Bitcoin-qt.


5. Da biste izabrali pruned čvor, označite "Limit Blockchain storage" i konfigurišite ograničenje podataka koje će biti uskladišteno:


![welcome](assets/1.webp)


## Zaključak dela 1: Vodič za instalaciju


Kada je Bitcoin Core instaliran, preporučuje se da ga držite uključenim što je više moguće kako biste doprineli Bitcoin mreži verifikovanjem transakcija i prenošenjem novih blokova drugim čvorovima.


Međutim, povremeno pokretanje i sinhronizacija vašeg čvora, čak i samo za validaciju primljenih i poslatih transakcija, ostaje dobra praksa.


![Creation wallet](assets/2.webp)


# Konfigurisanje Tor-a za Bitcoin Core čvor


**Napomena💡:** ovaj vodič je dizajniran za Bitcoin Core 24.0.1 na Linux distribucijama kompatibilnim sa Ubuntu/Debian.


## Instaliranje i konfiguracija Tor-a za Bitcoin Core


Prvo, treba da instaliramo Tor servis (The Onion Router), mrežu koja se koristi za anonimnu komunikaciju, što će nam omogućiti da anonimizujemo naše interakcije sa Bitcoin mrežom. Za uvod u alate za zaštitu privatnosti na mreži, uključujući Tor, pogledajte naš članak na ovu temu.


Da biste instalirali Tor, otvorite terminal i unesite sudo apt -y install tor. Kada se instalacija završi, usluga će se obično automatski pokrenuti u pozadini. Proverite da li ispravno radi pomoću komande sudo systemctl status tor. Odgovor bi trebalo da pokaže Active: active (exited). Pritisnite Ctrl+C da izađete iz ove funkcije.


**Savet:** u svakom slučaju, možete koristiti sledeće komande u terminalu za pokretanje, zaustavljanje ili ponovno pokretanje Tor-a:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Zatim, pokrenimo Bitcoin Core grafički interfejs sa komandom Bitcoin-qt. Zatim, omogućimo automatsku funkciju softvera da usmeri naše konekcije kroz Tor proxy: Settings > Network, i odatle možemo označiti "Connect through SOCKS5 proxy (default proxy)" kao i "Use a separate SOCKS5 proxy to reach peers via Tor onion services".


![option](assets/3.webp)


Bitcoin Core automatski detektuje da li je Tor instaliran i, ako jeste, po defaultu će kreirati odlazne konekcije ka drugim čvorovima koji takođe koriste Tor, pored konekcija ka čvorovima koji koriste IPv4/IPv6 mreže (clearnet).


**Napomena💡:** da biste promenili jezik prikaza na francuski, idite na karticu Prikaz, engleski "Display" u Podešavanjima (engleski "Settings").


## Napredna Tor konfiguracija (opciono)


Moguće je konfigurisati Bitcoin Core da koristi samo Tor mrežu za povezivanje sa peer-ovima, čime se optimizuje naša anonimnost putem našeg čvora. Pošto ne postoji ugrađena funkcionalnost za ovo u grafičkom interfejsu, potrebno je ručno kreirati konfiguracioni fajl. Idite na "Settings", zatim "Options".


![option 2](assets/4.webp)


Ovde, kliknite na "Open configuration file". Kada ste u Bitcoin.conf tekstualnom fajlu, jednostavno dodajte liniju onlynet=onion i sačuvajte fajl. Potrebno je da restartujete Bitcoin Core da bi ova komanda stupila na snagu.

Zatim ćemo konfigurisati Tor servis tako da Bitcoin Core može primati dolazne konekcije putem proxy-ja, omogućavajući drugim čvorovima na mreži da koriste naš čvor za preuzimanje Blockchain podataka bez ugrožavanja sigurnosti naše mašine.


U terminalu unesite sudo nano /etc/tor/torrc da pristupite konfiguracionom fajlu Tor servisa. U ovom fajlu pronađite liniju #ControlPort 9051 i uklonite # da biste je omogućili. Sada dodajte dve nove linije u fajl: _HiddenServiceDir /var/lib/tor/Bitcoin-service/_ i _HiddenServicePort 8333 127.0.0.1:8334_. Da biste izašli iz fajla i sačuvali ga, pritisnite Ctrl+X > Y > Enter. Nazad u terminalu, restartujte Tor unosom komande _sudo systemctl restart tor_.


Sa ovom konfiguracijom, Bitcoin Core će moći da uspostavi dolazne i odlazne konekcije sa drugim čvorovima na mreži samo preko Tor mreže (Onion). Da biste to potvrdili, kliknite na karticu "Window", zatim "Peers".


![Nodes Window](assets/5.webp)


## Dodatni resursi


Na kraju, korišćenje samo Tor mreže (onlynet=onion) moglo bi vas učiniti ranjivim na Sybil napad. Zato neki preporučuju održavanje konfiguracije sa više mreža kako bi se ublažila ova vrsta rizika. Štaviše, sve IPv4/IPv6 konekcije će biti usmerene kroz Tor proxy kada se konfiguriše, kao što je ranije navedeno.


Alternativno, da biste ostali isključivo na Tor mreži i smanjili rizik od Sybil napada, možete dodati adresu drugog pouzdanog čvora u vaš Bitcoin.conf fajl dodavanjem linije _addnode=trusted_address.onion_. Ovu liniju možete dodati više puta ako želite da se povežete sa više pouzdanih čvorova.


Da biste pregledali logove vašeg Bitcoin čvora koji su posebno povezani s njegovom interakcijom s Tor-om, dodajte _debug=tor_ u vašu Bitcoin.conf datoteku. Sada ćete imati relevantne informacije o Tor-u u vašem debug logu, koje možete pregledati u prozoru "Information" pomoću dugmeta "Debug File". Takođe je moguće pregledati ove logove direktno u terminalu pomoću komande _bitcoind -debug=tor_.


**Savet💡:** ovde su neki zanimljivi linkovi:


- Wiki stranica koja objašnjava Tor i njegovu vezu sa Bitcoin-om
- Bitcoin Core generator konfiguracione datoteke autora Jameson Lopp-a
- Vodič za konfiguraciju Tor-a autora Jon Atack


Kao i uvek, ako imate bilo kakva pitanja, slobodno ih podelite sa zajednicom Agora256. Učimo zajedno da bismo sutra bili bolji nego što smo danas!
