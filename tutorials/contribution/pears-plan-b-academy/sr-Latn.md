---
name: Plan ₿ Academy - Pears App
description: Kako instalirati i koristiti aplikaciju Plan ₿ Academy na Pears?
---

![cover](assets/cover.webp)


Verovatno već znate da je Plan ₿ Academy najveća obrazovna baza podataka posvećena Bitcoin, koja okuplja kurseve, tutorijale i hiljade resursa otvorenog koda. Prvobitno, Plan ₿ Academy je bio vebsajt. Ali šta bi se desilo ako više ne biste mogli da mu pristupite na uobičajen način, na primer u slučaju cenzure?


U ovom vodiču ćemo naučiti kako pokrenuti platformu **Plan ₿ Academy** na zaista otporan način na cenzuru koristeći **Pears**, peer-to-peer (P2P) tehnologiju koju je razvio **Holepunch** i koju podržava **Tether**.


Pears je softver koji nam omogućava da pokrenemo platformu Plan ₿ Academy bez oslanjanja na centralizovani veb-sajt. U ovom vodiču ćemo instalirati Pears na vašem računaru kako bismo pristupili Plan ₿ Academy preko Pears-a.


Cilj Pears-a je jednostavan: omogućiti distribuciju i korišćenje web aplikacija bez oslanjanja na bilo kakvu centralizovanu infrastrukturu (bez servera, bez hostova, bez posrednika). Drugim rečima, čak i ako provajder u oblaku prestane sa radom ili neka država blokira domen, aplikacija nastavlja da živi među mrežnim čvorovima. Ovaj pristup omogućava našoj obrazovnoj platformi, Plan ₿ Academy, da ostane dostupna širom sveta, bez jedne tačke otkaza.


---

**Ukratko:**



- Instalirajte Pears;



- Pokrenite sledeću komandu da biste lansirali aplikaciju Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Šta su kruške?


Pears je istovremeno okruženje za izvršavanje, alat za razvoj i platforma za implementaciju aplikacija od korisnika do korisnika. Ovaj alat otvorenog koda omogućava vam da gradite, delite i pokrećete softver bez servera ili infrastrukture, direktno između korisnika. U praktičnom smislu, to znači da umesto hostovanja aplikacije na centralnom serveru, svaki korisnik postaje čvor u mreži: dele deo aplikacije i podataka sa drugim korisnicima. Ceo sistem formira distribuiranu mrežu gde svaka instanca sarađuje kako bi usluga ostala dostupna.


![Image](assets/fr/01.webp)


Ovaj pristup zasnovan je na skupu modularnih softverskih komponenti koje je razvio Holepunch:



- Hypercore**: distribuirani log koji osigurava doslednost podataka i sigurnost bez centralne baze podataka.
- Hyperbee**: indeks izgrađen na vrhu Hypercore-a koji omogućava da podaci budu organizovani i pretraživani efikasno.
- Hyperdrive**: distribuirani datotečni sistem koji se koristi za skladištenje i sinhronizaciju aplikacionih fajlova među vršnjacima.
- Hyperswarm** i **HyperDHT**: mrežni slojevi koji omogućavaju otkrivanje i povezivanje vršnjaka širom sveta bez centralnog servera.
- Secretstream**: protokol za šifrovanje od kraja do kraja koji osigurava komunikaciju između vršnjaka.


Kombinovanjem ovih komponenti, Pears omogućava kreiranje autonomnih, enkriptovanih i distribuiranih aplikacija, gde svaki korisnik aktivno učestvuje u mreži. Ova decentralizovana arhitektura eliminiše troškove infrastrukture, rizike cenzure i SPOF-ove (*Single Points of Failure*).


Pears razvija Holepunch, kompanija koju su osnovali Mathias Buus i Paolo Ardoino (CEO Tether-a i CTO Bitfinex-a), sa misijom da prošire peer-to-peer logiku izvan Bitcoin. Njihova ambicija je da izgrade "*Internet vršnjaka*", gde svaka aplikacija može da funkcioniše bez dozvole, bez servera i bez posrednika. Holepunch već stoji iza **Keet**, potpuno P2P aplikacije za video konferencije i razmenu poruka.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Ovaj vodič za instalaciju Pears-a podeljen je na više sekcija u zavisnosti od vašeg operativnog sistema. Idite direktno na onaj koji odgovara vašem okruženju kako biste pratili odgovarajuća uputstva:*



- Linux (Debian)** → Sekcija **2**
- Windows** → Sekcija **3**
- macOS** → Sekcija **4**


## 2. Kako instalirati Pears na Linux (Debian)?


Instaliranje Pears na Debian je relativno jednostavno, ali zahteva nekoliko preduslova, koje ćemo detaljno opisati u ovom odeljku.


### 2.1. Ažuriraj sistem


Pre nego što bilo šta drugo uradite, važno je da se uverite da je vaš sistem ažuriran.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Instaliraj zavisnosti


Pears se oslanja na neke sistemske biblioteke, uključujući `libatomic1`, koju koristi Bare JavaScript runtime engine. Instalirajte je sledećom komandom:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Instalirajte Node.js i npm putem NVM-a


Pears se distribuira putem *npm*, menadžera paketa za *Node.js*. Iako Pears ne zavisi direktno od *Node.js* za rad, potreban je za instalaciju. Preporučeni način za instalaciju *Node.js* na Linuxu je putem *NVM* (*Node Version Manager*), koji vam omogućava upravljanje više verzija Node-a istovremeno.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Zatim, ponovo učitajte svoj terminal da biste aktivirali *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Proverite da je *NVM* ispravno instaliran:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Zatim instalirajte stabilnu verziju *Node.js* (na primer, trenutnu LTS verziju):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Potvrdite da su *Node.js* i *npm* ispravno instalirani:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Instalirajte Pears pomoću npm-a


Kada je *npm* dostupan, možete globalno instalirati Pears CLI na vaš sistem. Ovo vam omogućava da pokrenete komandu `pear` iz bilo kog direktorijuma.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Inicijalizuj Kruške


Nakon instalacije, jednostavno pokrenite sledeću komandu u vašem terminalu:


```bash
pear
```


Prilikom prvog pokretanja, Pears će se povezati na peer-to-peer mrežu kako bi preuzeo potrebne komponente. Ovaj proces ne zavisi od bilo kog centralnog servera — fajlovi se preuzimaju direktno od drugih korisnika.


![Image](assets/fr/10.webp)


Kada se preuzimanje završi, ponovo pokrenite komandu da potvrdite da sve radi:


```bash
pear
```


![Image](assets/fr/11.webp)


Ako je sve ispravno instalirano, meni za pomoć Pears će se pojaviti sa listom dostupnih komandi.


### 2.6. Testirajte kruške sa Keetom


Da biste potvrdili da Pears radi u potpunosti, možete pokrenuti postojeću P2P aplikaciju dostupnu na mreži, kao što je Keet, softver otvorenog koda za razmenu poruka i video konferencije koji je razvio Holepunch.


```bash
pear run pear://keet
```


Ova komanda učitava Keet aplikaciju direktno sa Pears mreže, bez korišćenja centralnog servera. Ako se Keet pokrene ispravno, to znači da je vaša Pears instalacija potpuno funkcionalna.


![Image](assets/fr/12.webp)


Vaš Linux sistem je sada spreman za pokretanje i hostovanje peer-to-peer aplikacija sa Pears.


## 3. Kako instalirati Pears na Windows


Instaliranje Pears na Windows je jednako jednostavno kao i na Linuxu, ali zahteva nekoliko specifičnih alata.


*Ako koristite Linux i već ste instalirali Pears, možete odmah preći na **Korak 5**.*


### 3.1. Otvorite PowerShell kao Administrator


Prvo, pokrenite PowerShell sa administratorskim privilegijama:



- Kliknite na Start meni;
- Ukucaj „PowerShell“;
- Desni klik na "*Windows PowerShell*";
- Odaberite "*Pokreni kao administrator*".


![Image](assets/fr/15.webp)


### 3.2. Preuzimanje NVS


Pears se instalira putem *npm*-a, menadžera paketa za *Node.js*. Na Windows-u, metoda koju preporučuje Holepunch je korišćenje *NVS* (*Node Version Switcher*), koji je stabilniji od *NVM*-a na ovom sistemu.


U PowerShell-u, pokrenite sledeću komandu da instalirate najnoviju verziju *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Instaliraj Node.js


Nakon instalacije, ponovo pokrenite PowerShell, a zatim unesite sledeću komandu:


```powershell
nvs
```


Trebalo bi da vidite listu dostupnih verzija *Node.js*. Izaberite prvu pritiskom na taster `a` na vašoj tastaturi.


![Image](assets/fr/17.webp)


*Node.js* je sada instaliran.


![Image](assets/fr/18.webp)


### 3.4. Verifikuj Instalacije


Uverite se da su *Node.js* i *npm* dostupni:


```powershell
node -v
npm -v
```


Obe komande treba da vrate broj verzije.


![Image](assets/fr/19.webp)


### 3.5. Instalirajte Pears pomoću npm-a


Jednom kada su *Node.js* i *npm* dostupni, instalirajte **Pears CLI** globalno na vašem sistemu:


```powershell
npm install -g pear
```


Ovo instalira binarnu datoteku `pear` u vaš globalni *npm* direktorijum.


![Image](assets/fr/20.webp)


### 3.6. Verifikuj i Inicijalizuj Kruške


Kada je instalacija završena, pokrenite:


```powershell
pear
```


Prilikom prvog pokretanja, Pears će automatski preuzeti potrebne komponente sa peer-to-peer mreže. Ovaj proces može potrajati nekoliko trenutaka.


![Image](assets/fr/21.webp)


Ako je sve prošlo dobro, trebalo bi da vidite Pears CLI meni pomoći sa listom dostupnih podkomandi (run, seed, info...).


### 3.7. Test Pears with Keet


Da biste verifikovali da Pears radi potpuno operativno, možete pokrenuti postojeću P2P aplikaciju dostupnu na mreži, kao što je Keet — softver otvorenog koda za razmenu poruka i video konferencije koji je razvio Holepunch.


```bash
pear run pear://keet
```


Ova komanda učitava Keet aplikaciju direktno sa Pears mreže, bez korišćenja bilo kog centralnog servera. Ako se Keet uspešno pokrene, to znači da je vaša Pears instalacija potpuno funkcionalna.


![Image](assets/fr/22.webp)


Vaš Windows sistem je sada spreman za pokretanje i hostovanje peer-to-peer aplikacija sa Pears.


## 4. Kako instalirati Pears na macOS


Instaliranje Pears na macOS je slično kao na Linuxu, ali zahteva nekoliko prilagođavanja specifičnih za Apple-ovo okruženje. Hajde da prođemo kroz ove korake zajedno.


*Ako koristite Linux ili Windows i već ste instalirali Pears, možete odmah preći na **Korak 5**.*


### 4.1. Proveri sistemske preduslove


Pre instalacije, uverite se da su *Xcode Command Line Tools* instalirani na vašem sistemu. Ovaj paket obezbeđuje neophodne alate za izgradnju za *Node.js* i njegove zavisnosti.


Da biste to uradili, otvorite terminal koristeći prečicu `Cmd + Space bar`, otkucajte `Terminal`, i pritisnite `Enter`. Zatim, pokrenite sledeću komandu u terminalu da biste ga instalirali:


```bash
xcode-select --install
```


Ako su alati već instalirani na vašem sistemu, macOS će vas obavestiti.


### 4.2. Instaliraj NVM


Pears se distribuira putem *npm*, menadžera paketa za *Node.js*. Iako Pears ne zavisi direktno od *Node.js* za funkcionisanje, potreban je za instalaciju. Preporučeni metod za instaliranje *Node.js* na macOS je *NVM* (*Node Version Manager*), koji vam omogućava upravljanje sa više verzija Node-a istovremeno.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Zatim ponovo učitajte svoj terminal da aktivirate *NVM*:


```bash
source ~/.zshrc
```


Ako koristiš *bash* umesto *zsh*, pokreni:


```bash
source ~/.bashrc
```


Zatim, proverite da li je *NVM* ispravno instaliran:


```bash
nvm --version
```


Vaš terminal bi trebalo da prikaže instaliranu verziju *NVM*-a.


### 4.3. Instalirajte Node.js i npm


Zatim instalirajte stabilnu verziju *Node.js* (na primer, trenutnu LTS verziju):


```bash
nvm install --lts
```


Kada je instalacija završena, proverite instalirane verzije:


```bash
node -v
npm -v
```


Obe komande treba da vrate broj verzije.


### 4.4. Instalirajte Pears pomoću npm-a


Kada *npm* bude dostupan, možete globalno instalirati Pears CLI na vaš sistem. Ovo će vam omogućiti da izvršavate `pear` komandu iz bilo kog direktorijuma.


```bash
npm install -g pear
```


### 4.5. Inicijalizuj Kruške


Nakon instalacije, jednostavno pokrenite sledeću komandu u vašem terminalu:


```bash
pear
```


Prilikom prvog pokretanja, Pears se povezuje na peer-to-peer mrežu kako bi preuzeo potrebne komponente. Ovaj proces ne zahteva nikakav centralni server — fajlovi se preuzimaju direktno od drugih korisnika.


Kada se preuzimanje završi, ponovo pokrenite komandu da proverite da li sve radi:


```bash
pear
```


Ako je sve ispravno instalirano, meni za pomoć Pears će se pojaviti sa listom dostupnih komandi.


### 4.6. Testirajte kruške sa Keetom


Da biste proverili da li je Pears potpuno operativan, možete pokrenuti P2P aplikaciju koja je već dostupna na mreži, kao što je Keet, softver otvorenog koda za razmenu poruka i video konferencije od Holepunch-a.


```bash
pear run pear://keet
```


Ova komanda učitava Keet aplikaciju direktno sa Pears mreže, bez korišćenja centralnog servera. Ako se Keet uspešno pokrene, to znači da je vaša Pears instalacija potpuno funkcionalna.


Vaš macOS sistem je sada spreman za pokretanje i hostovanje peer-to-peer aplikacija sa Pears.


## 5. Kako koristiti Plan ₿ Akademiju na Pears


Kada je Pears instaliran i pokrenut, možete direktno pokrenuti platformu **Plan ₿ Academy** putem P2P mreže. Jednostavno pokrenite sledeću komandu u vašem terminalu (ista komanda radi na Linux, Windows i macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Kada se učitavanje završi, Plan ₿ Academy će se otvoriti unutar vašeg Pears okruženja, spreman za korišćenje baš kao originalni vebsajt — ali bez ikakve zavisnosti od centralnog servera.


![Image](assets/fr/14.webp)


## 6. Kako posaditi Plan ₿ Akademiju na kruške


U Pears mreži, *seed* aplikaciju znači redistribuirati je drugim peer-ovima sa sopstvene mašine. U praksi, kada seed Plan ₿ Academy, vaš računar postaje izvor podataka koji omogućava drugim korisnicima da preuzmu aplikaciju bez oslanjanja na centralni server.


Ovaj mehanizam jača otpornost i otpornost na cenzuru naše aplikacije na Pears mreži. Što više vršnjaka seed ima aplikacija, to postaje dostupnija i decentralizovanija, čak i ako neki originalni čvorovi postanu nedostupni.


Da biste pomogli u distribuciji Plan ₿ Akademije, jednostavno pokrenite sledeću komandu:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Sve dok je ova komanda aktivna, vaš uređaj će učestvovati u distribuciji datoteka aplikacije. Ako zatvorite terminal, proces deljenja se zaustavlja.


Da biste nastavili sa sejanjem nakon ponovnog pokretanja, možete pokrenuti komandu u pozadini ili kreirati sistemsku uslugu — na primer, systemd uslugu na Linuxu, LaunchAgent na macOS-u, ili zakazani zadatak na Windowsu. Ove metode osiguravaju da aplikacija Plan ₿ Academy automatski nastavi sa sejanjem pri pokretanju sistema.


Hvala vam što doprinosite decentralizovanoj distribuciji Plan ₿ Akademije na Pears i pomažete da Bitcoin obrazovanje zaista bude otporno na cenzuru!