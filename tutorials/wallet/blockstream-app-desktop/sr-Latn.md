---
name: Blockstream App - Desktop
description: Kako koristiti svoj Hardware Wallet sa Blockstream aplikacijom na računaru?
---
![cover](assets/cover.webp)



## 1. Uvod



### 1.1 Cilj tutorijala





- Ovaj vodič objašnjava kako koristiti **Blockstream App** na računaru za upravljanje Bitcoin **onchain** Wallet sa **Hardware Wallet**, omogućavajući sigurne transakcije zabeležene na glavnom Blockchain Bitcoin.
- Obuhvata instalaciju, početnu konfiguraciju, povezivanje Hardware Wallet i primanje i slanje onchain bitcoina.
- Napomena: Ostali tutorijali u Dodacima pokrivaju Liquid, Samo-za-gledanje i mobilnu aplikaciju.



### 1.2 Ciljna publika





- **Početnici**: Korisnici koji žele da upravljaju svojim bitkoinima pomoću sigurnog desktop softvera i Hardware Wallet.
- **Srednji korisnici**: Ljudi koji žele da razumeju kako da koriste Hardware Wallet za transakcije na lancu i opcije privatnosti kao što su Tor ili SPV.



### 1.3. Pozadina o hardverskim novčanicima





- **Hardware Wallet**, **Cold Wallet**: Fizički uređaj koji čuva privatne ključeve van mreže, nudeći visok nivo sigurnosti protiv sajber napada, za razliku od **Hot novčanika** (softverski novčanici na povezanim uređajima).
- **Preporučena upotreba**:
    - Idealno za osiguranje velikih iznosa ili dugoročnu štednju.
    - Pogodan za korisnike fokusirane na sigurnost koji žele zaštititi svoja sredstva od rizika povezanih sa povezanim uređajima.
- **Ograničenja**: Zahteva softver kao što je Blockstream App za pregled stanja, generate adresa i emitovanje Hardware Wallet-potpisanih transakcija.



## 2. Predstavljanje Blockstream aplikacije





- **Blockstream App** je mobilna (iOS, Android) i desktop aplikacija za upravljanje Bitcoin novčanicima i sredstvima na Liquid Network. Kupljena od strane Blockstream-a 2016. godine, zvala se *GreenAddress*, preimenovana je u *Blockstream Green* (2019), a sada se zove *Blockstream app* (2025).
- **Ključne karakteristike**:
- **Onchain** transakcije na Blockchain Bitcoin.
    - Transakcije na mreži **Liquid** (Sidechain za brze, poverljive razmene).
- **Portfelji samo za gledanje** za praćenje fondova bez pristupa ključevima.
    - Opcije privatnosti: povezivanje putem **Tor**-a, povezivanje na **lični čvor** putem Electrum-a, ili **SPV** verifikacija za smanjenje zavisnosti od čvorova trećih strana.
    - Funkcije **Replace-by-fee (RBF)** za ubrzavanje nepotvrđenih transakcija.
- **Kompatibilnost**: Integrira hardverske novčanike kao što je **Blockstream Jade**.
- **Interface**: Intuitivan za početnike, sa naprednim opcijama za stručnjake.
- **Napomena**: Ovaj vodič se fokusira na korišćenje na lancu sa Hardware Wallet na desktop verziji. Drugi priloženi tutorijali pokrivaju korišćenje na mobilnoj aplikaciji, za na lancu, Liquid i funkcije samo za gledanje.



## 3. Instaliranje i podešavanje Blockstream App Desktop



### 3.1. preuzimanje





- Idite na [zvaničnu veb stranicu](https://blockstream.com/app/) i kliknite na "_Download Now_". Preuzmite verziju koja odgovara vašem operativnom sistemu (Windows, macOS, Linux).
- **Napomena**: Obavezno preuzmite sa zvaničnog izvora kako biste izbegli lažni softver.



### 3.2. početna konfiguracija





- **Početni ekran**: Kada se prvi put otvori, aplikacija prikazuje ekran bez konfigurisanog Wallet. Kreirani ili uvezeni portfoliji će se kasnije pojaviti ovde.



![image](assets/fr/02.webp)





- **Prilagodite postavke**: Kliknite na ikonu postavki u donjem levom uglu, prilagodite opcije ispod, a zatim izađite iz Interface da nastavite.



![image](assets/fr/03.webp)



#### 3.2.1. Opšti parametri





- U meniju Podešavanja, kliknite na "**Opšte**".
- **Funkcija**: Promenite jezik softvera i aktivirajte eksperimentalne funkcije ako je potrebno.



![image](assets/fr/04.webp)



#### 3.2.2. Konekcija putem Tor-a





- U meniju Podešavanja, kliknite na "**Mreža**".
- **Funkcija**: Usmeravanje mrežnog saobraćaja putem **Tor**-a, anonimne mreže koja šifruje vaše veze.
- **Zašto?**: Sakrijte svoj IP Address i zaštitite svoju privatnost, idealno ako ne verujete svojoj mreži (na primer, javni Wi-Fi).
- **Nedostatak**: Može usporiti aplikaciju zbog enkripcije.
- **Preporuka**: Aktivirajte Tor ako je poverljivost prioritet, ali testirajte brzinu veze.



![image](assets/fr/05.webp)



#### 3.2.3. Povezivanje na lični čvor





- U meniju Podešavanja, kliknite na "**Prilagođeni serveri i validacija**".
- **Funkcija**: Povezuje aplikaciju sa vašim **kompletnim Bitcoin čvorom** putem **Electrum servera**.
- **Zašto?**: Pruža potpunu kontrolu nad Blockchain podacima, eliminišući zavisnost od Blockstream servera.
- **Preduslov**: Konfigurisani Bitcoin čvor.
- **Preporuka**: Napredni korisnici koji žele maksimalni suverenitet.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. SPV verifikacija





- U meniju Podešavanja, kliknite na "**Prilagođeni serveri i validacija**".
- **Funkcija**: Koristi **Simplified Payment Verification (SPV)** koji preuzima zaglavlja blokova i verifikuje vaše transakcije putem dokaza o uključivanju (Merkle), bez čuvanja kompletnog Blockchain.
- **Zašto?**: Smanjuje zavisnost od podrazumevanog čvora Blockstream-a, dok ostaje lagan za uređaje.
- **Nedostatak**: Manje siguran od Full node, jer se oslanja na čvorove trećih strana za neke informacije.
- **Preporuka**: Aktivirajte SPV ako ne možete koristiti lični čvor, ali preferirajte Full node za optimalnu sigurnost.



![image](assets/fr/07.webp)



## 4. Povezivanje Hardware Wallet sa Blockstream aplikacijom



### 4.1. Preliminarna razmatranja



#### 4.1.1. Za korisnike Ledger





- Blockstream Green podržava samo aplikaciju **Bitcoin Legacy** na Ledger uređajima (Nano S, Nano X).
- Koraci koje treba pratiti u **Ledger Live** pre povezivanja vašeg uređaja :


1. Idite na **"Settings "** → **"Experimental features "** i aktivirajte **developer mode**.


2. Idite na **"My Ledger"** → **"App Catalogue "**, zatim instalirajte aplikaciju **Bitcoin Legacy**


3. Otvorite aplikaciju **Bitcoin Legacy** na vašem Ledger pre pokretanja Blockstream Green kako biste uspostavili vezu.




- **Napomena**: Uverite se da je vaš Ledger otključan pomoću vašeg PIN koda i da je aplikacija Bitcoin Legacy aktivna kada se povežete.



#### 4.1.2 Inicijalizacija Hardware Wallet





- Ako vaš Hardware Wallet (Ledger, Trezor, ili Blockstream Jade) nikada nije korišćen (bilo sa Blockstream Green, ili sa drugim softverom kao što je Ledger Live), prvo ćete ga morati inicijalizovati. Ovaj korak uključuje, u sigurnom okruženju, bez kamera ili posmatrača:


1. **seed generisanje fraza / Mnemonic fraza** (12, 18 ili 24 reči): Pažljivo je zapišite na papir.


2. **seed verifikacija fraze**: Testirajte uvoz Wallet iz navedenih reči, npr. verifikacijom proširenog javnog ključa. Da se izvrši pre slanja sredstava na Wallet i trajnog obezbeđivanja seed fraze.


3. **Osiguranje seed fraze**: Sačuvajte frazu na fizičkom mediju (papir ili metal) i na sigurnom mestu. Nikada je ne čuvajte digitalno (bez snimaka ekrana, oblaka ili e-pošte).




- **Važno**: Fraza seed je vaš jedini način da povratite svoja sredstva ako se uređaj izgubi ili pokvari. Svako ko ima pristup može ukrasti vaše bitkoine.
- **Resursi** za pravljenje rezervne kopije i proveru rečenice seed :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Konfiguracija za ovaj vodič :





- Pretpostavićemo da je Hardware Wallet već inicijalizovan sa seed frazom i PIN kodom za zaključavanje.
- Pretpostavljamo da Hardware Wallet nikada nije bio povezan sa Blockstream App, što zahteva kreiranje novog naloga. Ako je Hardware Wallet već korišćen sa Blockstream App, nalog će se automatski pojaviti kada se aplikacija otvori.



### 4.2. Pokreni povezivanje





- Sa početnog ekrana, kliknite na "**Postavi novi Wallet**", zatim potvrdite uslove korišćenja i kliknite na "**Započni**" :



![image](assets/fr/08.webp)





- Odaberite opciju "**On Hardware Wallet**":



![image](assets/fr/09.webp)





- Ako koristite **Blockstream Jade**, kliknite na odgovarajuće dugme. U suprotnom, izaberite "**Poveži drugi hardverski uređaj**" :



![image](assets/fr/10.webp)





- Povežite svoj Hardware Wallet sa računarom putem USB-a i izaberite ga u Blockstream aplikaciji :



![image](assets/fr/22.webp)





- Molimo sačekajte dok Blockstream aplikacija uvozi informacije o vašem portfoliju:



![image](assets/fr/23.webp)



### 4.3. Kreiraj nalog





- Ako je vaš Hardware Wallet već korišćen sa Blockstream App, vaš nalog će se automatski pojaviti u Interface nakon uvoza. U suprotnom, kreirajte nalog klikom na "**Create Account**" :



![image](assets/fr/24.webp)





- Izaberite "**Standard**" za konfiguraciju klasičnog Bitcoin portfolija:



![image](assets/fr/25.webp)





- Kada vaš nalog bude kreiran, možete pristupiti svom glavnom Interface portfoliju:



![image](assets/fr/26.webp)





## 5. Korišćenje onchain Wallet sa Hardware Wallet



### 5.1. Primite bitkoine





- Sa glavnog ekrana portfolija, kliknite na "**Primi**" :



![image](assets/fr/27.webp)





- Aplikacija prikazuje **prazan prijem Address**. Korišćenje novog Address za svaki prijem poboljšava vašu poverljivost. Kliknite na "**Kopiraj Address**" da kopirate Address, ili neka pošiljalac skenira prikazani QR kod:



![image](assets/fr/12.webp)



**Opcije** :




- (1) Kliknite na strelice da generate novi Address povezan sa vašim portfoliom.
- (2) Da biste zatražili određeni iznos, kliknite na "**Više opcija**" a zatim na "**Zatraži iznos**". QR će biti ažuriran, a Address će biti zamenjen sa Bitcoin URI za plaćanje kao što je: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Da biste ponovo koristili prethodni Address, kliknite na "**Više opcija**" zatim na "**Lista adresa**" :



![image](assets/fr/14.webp)





- **Verifikacija**: Pažljivo proverite podeljeni Address kako biste izbegli greške ili napade (npr. zlonamerni softver koji menja sadržaj međuspremnika).
- Jednom kada transakcija bude emitovana na mreži, pojaviće se u vašem Wallet. Sačekajte od 1 do 6 potvrda da biste smatrali transakciju nepromenljivom.



![image](assets/fr/28.webp)



### 5.2. pošalji bitkoine





- Sa glavnog ekrana portfolija, kliknite na "**Pošalji**".



![image](assets/fr/29.webp)





- Unesite **detalje**:
    - (1) Proverite da je odabrana imovina **Bitcoin** (onchain).
    - (2) Unesite **Address primaoca** tako što ćete ga zalepiti ili skenirati QR kod pomoću veb kamere.
    - (3) Naznačite **iznos** koji treba poslati (u BTC, satoshima ili drugim jedinicama).




![image](assets/fr/16.webp)





- Izaberite **naknade za transakciju** (opciono) :
 - Izaberite jednu od predloženih opcija (brzo, srednje, sporo) prema hitnosti, sa procenjenim vremenom potvrde.
 - Za prilagođene naknade, ručno podesite broj satoshija po vbyte-u. Oni su prikazani na početnom ekranu. Pogledajte i [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Ručno biranje UTXO-a** (opciono): Kliknite na "**Ručno biranje Coin**" da biste odabrali specifične UTXO-e koji će se koristiti u transakciji.



![image](assets/fr/18.webp)





- **Preliminarna verifikacija**: Proverite Address, iznos i naknade na ekranu sažetka, zatim kliknite na "**Potvrdi transakciju**". U stvarnosti, transakcija neće biti puštena u mrežu dok je ne potpišete sa svojim Hardware Wallet, koji jedini ima tajne ključeve povezane sa adresama sa kojih će UTXO-ovi (satoši) biti zaduženi.



![image](assets/fr/19.webp)





- **Završna provera i potpis**: Uverite se da su svi parametri transakcije tačni **na vašem Hardware Wallet** ekranu, zatim potpišite transakciju koristeći ga. Greška Address može rezultirati nepovratnim gubitkom sredstava.





- **Emitovanje**: Kada se potpiše, Blockstream App automatski emituje transakciju na Bitcoin mreži.



![image](assets/fr/20.webp)





- **Praćenje**:
 - Transakcija se pojavljuje na početnom ekranu Wallet kao "na čekanju" dok se ne potvrdi.
 - Sve dok transakcija nije potvrđena, funkcija **Replace-by-fee (RBF)** može se koristiti za ubrzavanje potvrde povećanjem naknade (pogledajte Dodatak).



![image](assets/fr/21.webp)



## Aneksi



### A1. Ostali Blockstream tutorijali





- Korišćenje Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Uvezi i prati portfelj u "Samo za gledanje" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Korišćenje Blockstream aplikacije na mobilnim telefonima (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Objašnjenje Replace-by-fee (RBF)





- **Definicija**: Replace-by-fee (RBF) je funkcija mreže Bitcoin koja omogućava pošiljaocu da ubrza potvrdu **onchain** transakcije povećanjem naknade.
- **Ograničenja**:
    - RBF nije dostupan za Liquid ili Lightning transakcije.
    - Početna transakcija mora biti označena kao RBF-kompatibilna, što Blockstream App radi automatski.
- Za više informacija, pogledajte [naš rečnik](https://planb.network/resources/glossary/RBF-replacebyfee).



### A3. Najbolje prakse





- **Osigurajte svoju frazu za oporavak**:
    - Sačuvajte Hardware Wallet-ovu Mnemonic frazu na fizičkom mediju (papir, metal) na sigurnom mestu.
    - Nikada ga ne čuvajte digitalno (oblak, email, snimak ekrana).
    - Uputstvo : Sačuvajte svoju Mnemonic frazu :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Zaštitite svoju privatnost**:





    - generate novi Address za svaki onchain prijem.
    - Aktiviraj **Tor** ili **SPV** da ograničiš praćenje.
    - Povežite se sa sopstvenim Bitcoin čvorom putem Electrum-a za maksimalni suverenitet.
- **Uvek proveravajte adrese za dostavu**:





    - Proveri Address na svom Hardware Wallet ekranu pre potpisivanja.
    - Koristite kopiranje/lepljenje ili QR kod da biste izbegli ručne greške.
- **Optimizujte troškove**:





    - Prilagodite naknade prema hitnosti i zagušenju mreže (pogledajte [Mempool.space](https://Mempool.space/)).
    - Koristite Liquid ili Lightning za brze, niskotroškovne transakcije koje ne zahtevaju sigurnost na lancu.
- **Ažuriraj softver**:





    - Ažurirajte svoju Blockstream aplikaciju i Hardware Wallet firmware sa najnovijim funkcijama i sigurnosnim zakrpama.



### A4. Dodatni resursi





- **Zvanični linkovi**:
    - [Službena veb stranica](https://blockstream.com/)
    - [Podrška za Blockstream aplikaciju](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentacija i ćaskanje
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Block Explorers**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/Liquid)
    - Lightning : [1ML (Lightning Network)](https://1ml.com/)





- **Osiguravanje vaše fraze za oporavak:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Rečnik](https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Rečnik](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb