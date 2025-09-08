---
name: Blockstream Aplikacija - Onchain
description: Postavite Blockstream aplikaciju na mobilni uređaj i upravljajte onchain transakcijama
---
![cover](assets/cover.webp)


## 1. Uvod


### 1.1 Cilj tutorijala





- Ovaj vodič objašnjava kako koristiti mobilnu aplikaciju **Blockstream App** za upravljanje Bitcoin **onchain** Wallet, tj. transakcijama zabeleženim direktno na glavnom Blockchain Bitcoin.
- Obuhvata instalaciju, početnu konfiguraciju, kreiranje Software Wallet i operacije za primanje i slanje bitkoina.
- Napomena: Ostali tutorijali u Dodacima pokrivaju Liquid, Samo za gledanje i desktop verziju.



![image](assets/fr/01.webp)



### 1.2 Ciljna publika





- Početnici**: Korisnici koji žele da upravljaju svojim bitkoinima putem intuitivne mobilne aplikacije.
- Korisnici srednjeg nivoa**: Ljudi koji žele da razumeju funkcionalnosti na lancu i opcije privatnosti kao što su Tor ili SPV.



### 1.3. Podsetnici o Hot novčanicima





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: svi nazivi za aplikaciju instaliranu na pametnom telefonu, računaru ili bilo kojem uređaju povezanom na Internet, omogućavajući upravljanje i osiguranje privatnih ključeva sa Bitcoin Wallet.
- Za razliku od **hardverskih novčanika**, poznatih i kao **Cold novčanici**, koji izoluju ključeve van mreže, softverski novčanici rade u povezanom okruženju, što ih čini podložnijim sajber napadima.





- Preporučena upotreba** :
    - Idealno za upravljanje umerenim količinama Bitcoin, posebno za dnevne transakcije.
    - Pogodan za početnike ili korisnike sa ograničenim sredstvima, za koje Hardware Wallet može delovati suvišno.





- Ograničenja**: Manje siguran za čuvanje velikih sredstava ili dugoročnu štednju. U tom slučaju, izaberite Hardware Wallet.




## 2. Predstavljanje Blockstream aplikacije





- Blockstream App** je mobilna (iOS, Android) i desktop aplikacija za upravljanje Bitcoin portfolijima i imovinom na Liquid Network. Kupljena od strane [Blockstream](https://blockstream.com/) 2016. godine, ranije je bila nazvana *Green Address* a zatim *Blockstream Green*.
- Ključne karakteristike** :
    - Onchain** transakcije na Blockchain Bitcoin.
    - Mrežne transakcije **Liquid** (Sidechain za brze, poverljive razmene).
    - Portfelji samo za gledanje** za praćenje fondova bez pristupa ključevima.
    - Opcije privatnosti: povezivanje putem **Tor**-a, povezivanje na **lični čvor** putem Electrum-a, ili **SPV** verifikacija za smanjenje zavisnosti od čvorova trećih strana.
    - Funkcije **Replace-by-fee (RBF)** za ubrzavanje nepotvrđenih transakcija.
- Kompatibilnost**: Integrira hardverske novčanike kao što je **Blockstream Jade**.
- Interface**: Intuitivan za početnike, sa naprednim opcijama za stručnjake.
- Napomena**: Ovaj vodič se fokusira na upotrebu na lancu. Drugi tutorijali u dodacima pokrivaju Liquid, samo za gledanje i desktop verziju.



## 3. Instaliranje i konfiguracija Blockstream aplikacije



### 3.1. preuzimanje





- Za Android** :
    - Preuzmite [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) sa Google Play Store-a.
    - Alternativa: Instalirajte putem APK datoteke dostupne na [Blockstream-ovom zvaničnom GitHub-u](https://github.com/Blockstream/green_android).
- Za iOS** :
    - Preuzmite [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) iz App Store-a.
- Napomena**: Obavezno preuzmite sa zvaničnih izvora kako biste izbegli lažne aplikacije.



### 3.2. početna konfiguracija





- Početni ekran**: Kada se prvi put otvori, aplikacija prikazuje ekran bez konfigurisanog Wallet. Kreirani ili uvezeni portfoliji će se kasnije pojaviti ovde.



![image](assets/fr/02.webp)





- Prilagodite postavke**: Kliknite na "Postavke aplikacije", prilagodite opcije ispod, kliknite na "Sačuvaj", restartujte aplikaciju i kreirajte svoj portfolio.



![image](assets/fr/03.webp)



#### 3.2.1. Poboljšana privatnost (samo za Android)





- Funkcija**: Onemogućava snimke ekrana, skriva preglede aplikacija u upravitelju zadataka i zaključava pristup kada je telefon zaključan.
- Zašto?** : Štiti vaše podatke od neovlašćenog fizičkog pristupa ili zlonamernog softvera za snimanje ekrana.


#### 3.2.2. Povezivanje putem Tor-a





- Funkcija**: Usmeravanje mrežnog saobraćaja putem **Tor**-a, anonimne mreže koja šifrira vaše veze.
- Zašto?**: Sakrijte svoj IP Address i zaštitite svoju privatnost, idealno ako ne verujete svojoj mreži (na primer, javni Wi-Fi).
- Nedostatak**: Može usporiti aplikaciju zbog enkripcije.
- Preporuka**: Aktivirajte Tor ako je poverljivost prioritet, ali testirajte brzinu veze.


#### 3.2.3. Povezivanje na lični čvor





- Funkcija**: Povezuje aplikaciju sa vašim sopstvenim **kompletnim Bitcoin čvorom** putem **Electrum** servera.
- Zašto?**: Pruža potpunu kontrolu nad Blockchain podacima, eliminišući zavisnost od Blockstream servera.
- Preduslov**: Konfigurisani Bitcoin čvor.
- Preporuka**: Napredni korisnici koji traže maksimalni suverenitet.


#### 3.2.4. SPV verifikacija





- Funkcija**: Koristi **Simplified Payment Verification (SPV)** za direktnu verifikaciju određenih Blockchain podataka bez preuzimanja celog lanca.
- Zašto?**: Smanjuje zavisnost od podrazumevanog čvora Blockstream-a, dok ostaje lagan za mobilne uređaje.
- Nedostatak**: Manje siguran od Full node, jer se oslanja na čvorove trećih strana za neke informacije.
- Preporuka**: Aktivirajte SPV ako ne možete koristiti lični čvor, ali preferirajte Full node za optimalnu sigurnost.





## 4. Kreiranje Bitcoin onchain portfolija



### 4.1. Počni kreaciju





- Upozorenje**: Postavite svoj portfolio u privatnom okruženju, bez kamera ili posmatrača.
- Sa početnog ekrana, kliknite na "Get Started" :



![image](assets/fr/04.webp)





- Ako želite da upravljate **Cold Wallet** (offline Wallet): kliknite na **"Connect Jade "** da biste koristili Hardware Wallet Blockstream Jade ili druge kompatibilne Cold novčanike.



![image](assets/fr/05.webp)





- Sledeći ekran se pojavljuje:



![image](assets/fr/06.webp)





- (1) **"Postavljanje mobilnog Wallet"** : Kreiraj novi Hot Wallet (Hot Wallet).
- (2) **"Obnovi iz rezervne kopije "**: Uvezi postojeći portfelj koristeći Mnemonic frazu (12 ili 24 reči). Oprez: Ne uvoziti Cold Wallet frazu, jer će biti izložena na povezanom uređaju, čime se poništava njena sigurnost.
- (3) **"Watch-Only "**: Uvezite postojeći portfelj samo za čitanje, da biste videli saldo (npr. vašeg Cold Wallet) bez izlaganja Mnemonic fraze. Pogledajte Watch Only vodič u dodatku.



**U ovom vodiču**: Kliknite na **"Setup Mobile Wallet"** da biste kreirali Hot Wallet.


Vaš Wallet je automatski kreiran i početna stranica Wallet, ovde nazvana "Moj Wallet 5", je prikazana:



![image](assets/fr/07.webp)



**Važno**: Blockstream aplikacija je pojednostavila kreiranje Wallet tako što ne prikazuje automatski 12 reči seed fraze. *Iako se portfolio sada kreira jednim klikom, rizikujete da izgubite pristup svojim sredstvima ako ne sačuvate svoju seed frazu*.



### 4.2. Sačuvaj seed rečenicu





- Na početnom ekranu Wallet, kliknite na karticu "Security", zatim na opciju "Back Up" ili na meni "Recovery Phrase":



![image](assets/fr/08.webp)



seed 12-rečeni izraz će biti prikazan da ga sačuvate.





- Zapišite svoju frazu za oporavak s najvećom pažnjom. Zapišite je na papir ili metal i čuvajte na sigurnom mestu (sigurna, vanmrežna lokacija). Ova fraza je vaše jedino sredstvo za pristup vašim bitcoinima u slučaju gubitka uređaja ili brisanja aplikacije.
- Takođe je važno napomenuti da svako ko ima ovu frazu može ukrasti sve vaše bitkoine. Nikada je ne čuvajte digitalno:
 - Nema snimka ekrana
 - Nema rezervnih kopija oblaka, e-pošte ili poruka
 - Nema kopiranja/lepljenja (rizik od čuvanja u međuspremniku)



**! Ova tačka je kritična**. Za više informacija o rezervnoj kopiji :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Potvrdi seed rečenicu



Pre nego što pošaljete sredstva na Address povezano sa ovom seed rečenicom, morate testirati rezervnu kopiju svojih 12 reči.



Da bismo to uradili, napisaćemo referencu, obrisati Wallet, vratiti ga pomoću rezervne kopije i proveriti da li je referenca nepromenjena.





- Na početnom ekranu Wallet, kliknite na karticu "Settings", zatim na "Wallet Details", i kopirajte zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Napomena: zpub Address može biti uvezen u vašu Blockstream aplikaciju za funkciju "Samo za gledanje" (pogledajte Dodatak).





- Izbrišite aplikaciju, zatim obnovite Wallet putem **"Restore from Backup "** unosom Mnemonic fraze, i proverite da li je zpub nepromenjen. Ako jeste, vaš bekap je ispravan i možete poslati sredstva na Wallet.





- Da biste saznali više o tome kako izvesti test oporavka, ovde je posvećen vodič :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Obezbeđivanje pristupa aplikaciji



Zaključajte pristup aplikaciji jakim PIN kodom:




- Sa početnog ekrana Wallet idite na **"Security "** zatim kliknite na **"PIN "**
- Unesite i potvrdite **nasumičan 6-cifreni PIN kod**.



**Biometrijska opcija**: Dostupna za dodatnu pogodnost, ali manje sigurna od robusnog PIN koda (rizik od neovlašćenog pristupa, npr. otisak prsta ili skeniranje lica tokom spavanja).



**Napomena**: PIN osigurava uređaj, ali samo seed fraza može se koristiti za povrat sredstava.





## 5. Korišćenje onchain Wallet



### 5.1. Primite bitkoine





- Sa početnog ekrana portfolija, kliknite na '"**Transact**" zatim **"Receive "**.



![image](assets/fr/10.webp)





- Aplikacija prikazuje **prazan prijem Address** (SegWit v0 format, počinje sa `bc1q...`). Korišćenje novog Address svaki put kada primite Bitcoin poboljšava vašu poverljivost.





- Opcije** :
    - (1) "Bitcoin": kliknite da izaberete onchain ili Liquid pošiljku, i izaberite sredstvo.
    - (2) Kliknite na strelice da biste izabrali drugi novi Address povezan sa ovom seed rečenicom.
    - (3) Takođe možete izabrati Address među već korišćenim/prikazanim, klikom na tri tačke u gornjem desnom uglu, a zatim na "Lista adresa".
    - (4) Da biste zatražili određeni iznos, kliknite na tri tačke u gornjem desnom uglu, izaberite "Zatraži iznos" i unesite željeni iznos. QR će biti ažuriran, a Address će biti zamenjen Bitcoin URI-jem za plaćanje.




![image](assets/fr/11.webp)





- Podelite Address/URI klikom na "**Share**", kopiranjem teksta ili skeniranjem QR koda.
- Verifikacija**: Proverite Address podeljen sa primaocem koliko god je moguće kako biste izbegli greške ili napade (npr. zlonamerni softver koji menja sadržaj međuspremnika).



### 5.2. pošalji bitkoine





- Sa početnog ekrana portfolija, kliknite na "**Transact**" zatim **"Send "** :



![image](assets/fr/12.webp)





- Unesite detalje** :
    - (1) Unesite **Address primaoca** lepljenjem ili skeniranjem QR koda.
    - (2) Proverite imovinu i račun sa kojeg se sredstva šalju.
    - (3) Naznačite **iznos** koji treba poslati. Možete izabrati jedinicu: BTC, satoshis, USD, ...


Minimalni iznos (dush limit) dana 03/08/2025 je 546 Sats.




    - (4) Odaberite **naknade za transakciju** :
        - Izaberite jednu od predloženih opcija (npr. brzo, srednje, sporo) u zavisnosti od hitnosti, i prikazaće se približno vreme prenosa.
        - Za prilagođene naknade, ručno podesite broj Satoshi po vbytes (pogledajte [Mempool.space](https://Mempool.space/) za tržišne stope).




![image](assets/fr/13.webp)





- Proveri** :
    - Proveri Address, iznos i troškove na ekranu sažetka.
    - Greška Address može rezultirati nepovratnim gubitkom sredstava. Pazite na zlonamerni softver koji menja sadržaj u međuspremniku.



![image](assets/fr/14.webp)





- Potvrda**: Prevucite dugme "Pošalji" da potpišete i distribuirate transakciju.
- Praćenje**: U Wallet kartici "Transact", transakcija se pojavljuje kao "na čekanju" dok se ne potvrdi (1 do 6 potvrda):



![image](assets/fr/15.webp)





- Sve dok transakcija nije potvrđena, funkcija "Replace by fee" (pogledajte Dodatak) omogućava vam da ubrzate njeno procesuiranje povećanjem naknada za transakciju:



![image](assets/fr/16.webp)




## Dodaci



### A1. Ostali Blockstream tutorijali



Korišćenje Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Uvoz i praćenje Wallet u režimu "Samo za gledanje"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Desktop verzija



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Objašnjenje Replace-by-fee (RBF)



**Definicija**: Replace-by-fee (RBF) je funkcija Bitcoin mreže koja omogućava pošiljaocu da ubrza potvrdu **onchain** transakcije pristankom da plati višu naknadu.



**Ograničenja** :




- RBF nije dostupan za Liquid ili Lightning transakcije.
- Početna transakcija mora biti označena kao RBF-kompatibilna kada se kreira, što Blockstream App radi automatski.



**Više informacija:**




- [Rečnik](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Najbolje prakse



Da biste koristili **Blockstream App** sigurno i efikasno, pratite ove preporuke. One će vam pomoći da zaštitite svoja sredstva, optimizujete svoje transakcije i sačuvate svoju poverljivost na mrežama **Bitcoin (onchain)**, **Liquid** i **Lightning**.





- Osigurajte svoju frazu za oporavak** :
 - Uputstvo: Čuvanje vaše Mnemonic fraze



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Koristite sigurnu autentifikaciju** :
 - Aktivirajte **jak PIN** ili **biometrijsku autentifikaciju** (otisak prsta ili prepoznavanje lica) kako biste zaštitili pristup aplikaciji.
 - Nikada ne delite svoj PIN ili biometrijske podatke.





- Zaštitite svoju privatnost** :
 - generate novi Address za svaki onchain ili Liquid prijem kako bi se ograničilo praćenje na Blockchain.
 - Aktiviraj funkcije "Enhanced Privacy", "Tor" i "SPV".
 - Za maksimalnu poverljivost, povežite svoj Wallet sa sopstvenim Bitcoin čvorom preko Electrum servera umesto korišćenja javnog čvora.





- Izaberite mrežu koja najbolje odgovara vašim potrebama** :
 - Onchain**: Preferirano za dugoročno čuvanje ili transakcije velike vrednosti (naknade zanemarljive u odnosu na iznos).
 - Liquid**: Koristite za brze, niskobudžetne transfere sa poboljšanom poverljivošću.
 - Lightning**: Odaberite trenutne, niskotarifne transfere za male iznose.





- Uvek proveravajte adrese za dostavu** :
 - Pre nego što pošaljete sredstva, pažljivo proverite Address. Sredstva poslana na pogrešan Address su zauvek izgubljena. Koristite kopiranje/lepljenje ili skeniranje QR koda, nikada ne kopirajte/modifikujte Address ručno.





- Optimizujte troškove** :
 - Za transakcije na lancu, izaberite odgovarajuće naknade (sporo, srednje, brzo) u skladu sa hitnošću i zagušenošću mreže.
 - Koristite Liquid, ili Lightning za male količine.





- Ažurirajte aplikaciju redovno




### A4. Dodatni resursi





- Službeni linkovi:**
 - [Official website](https://blockstream.com/)**
 - [Podrška za mobilnu aplikaciju](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokumentacija i ćaskanje
 - [GitHub](https://github.com/Blockstream/green_android)**





- Blok istraživači :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Lightning: **[1ML (Lightning Network)](https://1ml.com/)**





- Učenje i tutorijali:** **[Plan ₿ Network](https://planb.network/)** :
 - Osiguravanje vaše fraze za oporavak



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Rečnik](https://planb.network/fr/resources/glossary/liquid-network)**



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Rečnik](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb