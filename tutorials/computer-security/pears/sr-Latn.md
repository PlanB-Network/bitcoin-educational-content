---
name: Pears
description: Kako da instaliram i koristim aplikacije na Pears?
---

![cover](assets/cover.webp)



U ovom vodiču ćemo naučiti kako pokrenuti aplikacije na **Pears**, peer-to-peer (P2P) tehnologiji koju je razvila **Holepunch** i podržava **Tether**. Cilj je jednostavan: omogućiti distribuciju i korišćenje web aplikacija bez oslanjanja na bilo kakvu centralizovanu infrastrukturu (bez servera, bez hostova, bez posrednika). Drugim rečima, čak i ako provajder oblaka prestane sa radom ili neka zemlja blokira domen, aplikacija nastavlja da živi među mrežnim vršnjacima.



## 1. Šta su kruške?



Pears je okruženje za izvršavanje, alat za razvoj i platforma za implementaciju aplikacija od korisnika do korisnika. Ovaj alat otvorenog koda omogućava izgradnju, deljenje i pokretanje softvera bez servera ili infrastrukture, direktno između korisnika. Konkretno, to znači da umesto hostovanja aplikacije na centralnom serveru, svaki korisnik postaje čvor mreže, deleći deo aplikacije i podataka sa drugim korisnicima. Ceo sistem formira distribuiranu mrežu, pri čemu svaka instanca sarađuje kako bi usluga ostala dostupna.



![Image](assets/fr/01.webp)



Ovaj pristup zasnovan je na skupu modularnih softverskih blokova koje je razvio Holepunch:




- Hypercore**: distribuirani log koji garantuje konzistentnost podataka i sigurnost bez centralne baze podataka.
- Hyperbee**: indeksator na vrhu Hypercore-a, za efikasnu organizaciju i pregledavanje podataka.
- Hyperdrive**: distribuirani fajl sistem koji se koristi za skladištenje i sinhronizaciju aplikacionih fajlova između vršnjaka.
- Hyperswarm** i **HyperDHT**: mrežni slojevi koji omogućavaju otkrivanje i povezivanje između vršnjaka širom sveta, bez centralnog servera.
- Secretstream**: E2E enkripcioni protokol za obezbeđivanje razmene između dva korisnika.



Kombinovanjem ovih komponenti, Pears omogućava kreiranje autonomnih, enkriptovanih i distribuiranih aplikacija, gde svaki korisnik aktivno učestvuje u mreži. Ova decentralizovana arhitektura eliminiše troškove infrastrukture, rizike cenzure i SPOF-ove (*Single Point of Failure*).



## 2. Poreklo i filozofija projekta



Pears razvija Holepunch, kompanija koju su osnovali Mathias Buus i Paolo Ardoino (CEO Tether-a i CTO Bitfinex-a), sa misijom da prošire peer-to-peer logiku izvan Bitcoin. Njihova ambicija je da izgrade "Peer-to-Peer Internet", gde svaka aplikacija može da radi bez autorizacije, bez servera i bez posrednika. Holepunch već stoji iza **Keet**, potpuno P2P aplikacije za video konferencije i razmenu poruka.



*Ovaj vodič za instalaciju Pears-a podeljen je na nekoliko sekcija u zavisnosti od vašeg operativnog sistema. Idite direktno na deo koji odgovara vašem okruženju kako biste pratili odgovarajuća uputstva :*




- Linux (Debian)** → Deo **3**
- Windows** → Part **4**
- macOS** → Deo **5**



## 3. Kako instalirati Pears na Linux (Debian)



Instaliranje Pears na Debian sistemu je relativno jednostavno, ali zahteva nekoliko preduslova, koje ćemo detaljno opisati u ovom odeljku.



### 3.1. ažurirati sistem



Prvo i najvažnije, važno je osigurati da je vaš sistem ažuriran.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. instaliraj zavisnosti



Pears se oslanja na određene sistemske biblioteke, posebno `libatomic1`, koju koristi Bare JavaScript runtime. Instalirajte je sledećom komandom:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. instaliraj Node.js i npm putem NVM



Pears se distribuira putem *npm*, menadžera paketa za *Node.js*. Iako Pears ne zavisi direktno od *Node.js* za funkcionisanje, neophodan je za instalaciju. Preporučeni metod za instalaciju *Node.js* na Linuxu je *NVM* (*Node Version Manager*), koji vam omogućava da upravljate sa nekoliko verzija Node-a paralelno.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Zatim ponovo učitajte svoj terminal da aktivirate *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Proverite da je *NVM* instaliran:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Zatim instalirajte stabilnu verziju *Node.js* (npr. trenutni LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Proveri instalacije *Node.js* i *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Instaliranje Pears sa npm



Kada *npm* bude dostupan, možete instalirati Pears CLI globalno na vašem sistemu. Ovo će vam omogućiti da pokrenete komandu `pear` iz bilo kog direktorijuma.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Inicijalizuj Kruške



Nakon instalacije, jednostavno pokrenite sledeću komandu u vašem terminalu:



```bash
pear
```



Prilikom prvog pokretanja, Pears će se povezati na peer-to-peer mrežu kako bi preuzeo potrebne komponente. Ovaj proces ne zahteva centralni server: fajlovi se dobijaju direktno od drugih korisnika.



![Image](assets/fr/10.webp)



Kada se preuzimanje završi, ponovo pokrenite komandu da proverite da li sve radi:



```bash
pear
```



![Image](assets/fr/11.webp)



Ako je sve ispravno instalirano, biće prikazana pomoć za Pears sa listom dostupnih komandi.



### 3.6. Testiranje krušaka sa Keet



Da biste proverili da li je Pears potpuno operativan, možete pokrenuti P2P aplikaciju koja je već dostupna na mreži, kao što je Keet, Holepunch-ov softver otvorenog koda za razmenu poruka i video konferencije.



```bash
pear run pear://keet
```



Ova komanda učitava Keet aplikaciju direktno sa Pears mreže, bez prolaska kroz centralni server. Ako se Keet pokrene ispravno, vaša Pears instalacija je potpuno funkcionalna.



![Image](assets/fr/12.webp)



Vaš Linux sistem je sada spreman za pokretanje i hostovanje peer-to-peer aplikacija sa Pears.



## 4. Kako instalirati Pears na Windows



Instaliranje Pears-a na Windows je jednako lako kao i na Linux-u, ali zahteva nekoliko posebnih alata.



*Ako koristite Linux, možete preskočiti na korak 6.*



### 4.1. otvorite PowerShell u administratorskom režimu



Prvo pokrenite PowerShell sa administratorskim pravima :




- Kliknite na Start meni;
- Upiši PowerShell ;
- Desni klik na "*Windows PowerShell*" ;
- Izaberite "*Pokreni kao administrator*".



![Image](assets/fr/15.webp)



### 4.2. preuzmi NVS



Pears se instalira putem *npm*, *Node.js* menadžera paketa. Na Windows-u, metoda koju preporučuje Holepunch je korišćenje *NVS* (*Node Version Switcher*), koji je stabilniji od *NVM* na ovom sistemu.



U PowerShell-u, pokrenite sledeću komandu da instalirate najnoviju verziju *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. instaliraj Node.js



Nakon instalacije, ponovo pokrenite PowerShell i unesite sledeću komandu:



```powershell
nvs
```



Trebalo bi da vidite listu dostupnih verzija *Node.js*. Izaberite prvu pritiskom na taster `a` na vašoj tastaturi.



![Image](assets/fr/17.webp)



*Node.js* je instaliran.



![Image](assets/fr/18.webp)



### 4.4. Proveri instalacije



Uverite se da su *Node.js* i *npm* dostupni:



```powershell
node -v
npm -v
```



Obe komande moraju vratiti broj verzije.



![Image](assets/fr/19.webp)



### 4.5. Instaliranje Pears sa npm



Jednom kada su *Node.js* i *npm* dostupni, instalirajte **Pears CLI** globalno na vašem sistemu:



```powershell
npm install -g pear
```



Ovo će instalirati `pear` binarni fajl u vaš globalni *npm* direktorijum.



![Image](assets/fr/20.webp)



### 4.6. Proveri i inicijalizuj Kruške



Kada je instalacija završena, pokrenite :



```powershell
pear
```



Prilikom prvog pokretanja, Pears će automatski preuzeti potrebne komponente sa peer-to-peer mreže. Ovaj proces može potrajati nekoliko trenutaka.



![Image](assets/fr/21.webp)



Ako je sve prošlo dobro, trebalo bi da vidite CLI Pears ekran za pomoć sa listom dostupnih pod-komandi (run, seed, info...).



### 4.7. Testiranje krušaka sa Keetom



Da biste proverili da li je Pears potpuno operativan, možete pokrenuti P2P aplikaciju koja je već dostupna na mreži, kao što je Keet, Holepunch-ov softver otvorenog koda za razmenu poruka i video konferencije.



```bash
pear run pear://keet
```



Ova komanda učitava Keet aplikaciju direktno sa Pears mreže, bez prolaska kroz centralni server. Ako se Keet pokrene ispravno, vaša Pears instalacija je potpuno funkcionalna.



![Image](assets/fr/22.webp)



Vaš Windows sistem je sada spreman za pokretanje i hostovanje peer-to-peer aplikacija sa Pears.



## 5. Kako da instaliram Pears na macOS?



Instaliranje Pears-a na macOS je slično instaliranju na Linux, ali zahteva nekoliko prilagođavanja specifičnih za Apple okruženje. Hajde da zajedno otkrijemo ove korake.



*Ako koristite Linux ili Windows i već ste instalirali Pears, možete preći direktno na **korak 6**.*



### 5.1. Proverite sistemske zahteve



Pre nego što instalirate, molimo vas da se uverite da je *Xcode Command Line Tools* prisutan na vašem sistemu. Ovaj paket obezbeđuje neophodne alate za kompilaciju za _Node.js_ i njegove zavisnosti.



Da biste to uradili, otvorite terminal pomoću prečice na tastaturi `Cmd + Space bar`, zatim otkucajte `Terminal` i pritisnite taster `Enter`. Zatim možete uneti ovu komandu u terminal da pokrenete instalaciju:



```bash
xcode-select --install
```



Ako su alati već instalirani na vašem sistemu, macOS će vas obavestiti.



### 5.2. instaliraj NVM



Pears se distribuira putem *npm*-a, menadžera paketa za *Node.js*. Iako Pears ne zavisi direktno od *Node.js*-a za funkcionisanje, neophodan je za instalaciju. Preporučeni metod za instaliranje *Node.js*-a na macOS je *NVM* (*Node Version Manager*), koji vam omogućava upravljanje sa nekoliko verzija Node-a paralelno.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Zatim ponovo učitajte svoj terminal da aktivirate *NVM* :



```bash
source ~/.zshrc
```



Ako koristite *bash* umesto *zsh*, pokrenite :



```bash
source ~/.bashrc
```



Zatim proverite da li je *NVM* instaliran:



```bash
nvm --version
```



Terminal bi trebalo da vrati verziju *NVM* instaliranu na vašem sistemu.



### 5.3. instaliraj Node.js i npm



Zatim instalirajte stabilnu verziju *Node.js* (npr. trenutni LTS):



```bash
nvm install --lts
```



Kada je instalacija završena, proverite instalirane verzije:



```bash
node -v
npm -v
```



Obe komande moraju vratiti broj verzije.



### 5.4 Instaliranje Pears sa npm



Kada *npm* bude dostupan, možete instalirati Pears CLI globalno na vašem sistemu. Ovo će vam omogućiti da pokrenete komandu `pear` iz bilo kog direktorijuma.



```bash
npm install -g pear
```



### 5.5. Inicijalizujte Kruške



Nakon instalacije, jednostavno pokrenite sledeću komandu u vašem terminalu:



```bash
pear
```



Prilikom prvog pokretanja, Pears će se povezati na peer-to-peer mrežu kako bi preuzeo potrebne komponente. Ovaj proces ne zahteva centralni server: fajlovi se dobijaju direktno od drugih korisnika.



Kada se preuzimanje završi, ponovo pokrenite komandu da proverite da li sve radi:



```bash
pear
```



Ako je sve ispravno instalirano, biće prikazana pomoć za Pears sa listom dostupnih komandi.



### 5.6. Testiranje krušaka sa Keetom



Da biste proverili da li je Pears potpuno operativan, možete pokrenuti P2P aplikaciju koja je već dostupna na mreži, kao što je Keet, Holepunch-ov softver otvorenog koda za razmenu poruka i video konferencije.



```bash
pear run pear://keet
```



Ova komanda učitava Keet aplikaciju direktno sa Pears mreže, bez prolaska kroz centralni server. Ako se Keet pokrene ispravno, vaša Pears instalacija je potpuno funkcionalna.



Vaš macOS sistem je sada spreman za pokretanje i hostovanje peer-to-peer aplikacija sa Pears.



## 6. Kako da koristim aplikaciju na Pears?



Kada Pears bude pokrenut, možete pokrenuti aplikaciju po vašem izboru direktno sledećom komandom:



```bash
pear run pear://[KEY]
```



Jednostavno zamenite `[KEY]` sa ključem aplikacije koji želite da koristite.



![Image](assets/fr/13.webp)



Da biste naučili kako da pokrenete našu Plan ₿ Academy platformu na Pears, pogledajte ovaj sveobuhvatni vodič :



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

A da biste saznali kako da koristite Keet aplikaciju za razmenu poruka koju ste upravo pokrenuli na Pears, pogledajte ovaj vodič :



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b