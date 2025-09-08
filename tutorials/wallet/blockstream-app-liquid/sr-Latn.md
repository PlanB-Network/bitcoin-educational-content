---
name: Blockstream Aplikacija - Liquid
description: Kako konfigurisati Blockstream aplikaciju i koristiti Liquid Network
---
![cover](assets/cover.webp)


## 1. Uvod


### 1.1 Cilj tutorijala





- Ovaj vodič objašnjava kako koristiti mobilnu aplikaciju **Blockstream App** za upravljanje portfoliom **Bitcoin Liquid**, tj. transakcijama zabeleženim direktno na Bitcoin "Liquid" bočnom lancu.
- Obuhvata instalaciju, početnu konfiguraciju, kreiranje Software Wallet i operacije za primanje i slanje bitkoina na Liquid.
- Napomena: Ostali tutorijali u Dodacima pokrivaju Onchain, Samo-za-gledanje i desktop verziju.



### 1.2 Ciljna publika





- Početnici**: Korisnici koji žele da upravljaju svojim bitkoinima putem intuitivne mobilne aplikacije, integrišući Liquid Network.
- Korisnici srednjeg nivoa**: Ljudi koji žele da razumeju funkcionalnosti na lancu i opcije privatnosti kao što su Tor ili SPV.



### 1.3 Uvođenje Liquid



**Liquid** je **Sidechain** od Bitcoin, razvijen od strane **[Blockstream](https://blockstream.com/Liquid/)**, dizajniran da ponudi bržu, više Confidential Transactions i naprednu funkcionalnost, dok ostaje povezan sa glavnim Blockchain Bitcoin.



Sidechain je nezavisni Blockchain koji radi paralelno sa Bitcoin, koristeći mehanizam poznat kao **two-way peg**. Ovaj sistem zaključava bitkoine na glavnom Blockchain kako bi kreirao **Liquid-Bitkoine (L-BTC)**, tokene koji cirkulišu na Liquid Network dok zadržavaju paritet vrednosti sa originalnim bitkoinima. Sredstva se mogu vratiti na Blockchain Bitcoin u bilo kom trenutku.



![image](assets/fr/17.webp)






- (1) Peg-in**: Bitcoini (BTC) su zaključani na glavnom Blockchain od strane Liquid federacije. Zauzvrat, ekvivalentna količina Liquid-Bitcoina (L-BTC), koja osigurava paritet između dva lanca, se izdaje na Blockchain Liquid i šalje korisniku.





- (2) Nezavisne transakcije** : Transakcije mogu da se odvijaju istovremeno i nezavisno na glavnom Blockchain (BTC) i Sidechain Liquid (L-BTC), u zavisnosti od zahteva korisnika.





- (3) Peg-out**: Korisnik šalje Liquid-Bitcoine (L-BTC) nazad federaciji Liquid. Federacija zatim otključava ekvivalentnu količinu bitcoina (BTC) na glavnom Blockchain i prenosi ih korisniku.



Liquid se oslanja na **federaciju** pouzdanih učesnika (berze, priznate Bitcoin kompanije) koji upravljaju validacijom blokova i bilateralnim sidrenjem. Za razliku od Blockchain Bitcoin, koji je decentralizovan i oslanja se na rudare, Liquid je **federativna** mreža, što znači da njena sigurnost i upravljanje zavise od ovih učesnika. Iako to podrazumeva kompromis u decentralizaciji, omogućava optimizovane performanse i naprednu funkcionalnost.



![image](assets/fr/18.webp)



##### Zašto koristiti Liquid?





- Brzina**: Transakcije na Liquid su potvrđene za oko **1 minut**, u poređenju sa 10 minuta ili više za onchain transakcije, zahvaljujući blokovima koje generiše federacija validatora svake minute.
- Poboljšana poverljivost**: Liquid koristi **Confidential Transactions**, koji skriva količinu i tip prenetog sredstva, čineći transakcije privatnijim (iako adrese ostaju vidljive).
- Niske naknade** : Transakcije na Liquid su generalno jeftinije, što ih čini idealnim za česte prenose ili male iznose.
- Više sredstava**: Pored L-BTC-a, Liquid podržava izdavanje drugih digitalnih sredstava, kao što su stabilni novčići ili tokeni, za upotrebu u specifičnim aplikacijama.
- Use cases**: Liquid je posebno pogodan za razmene između različitih platformi, brza plaćanja ili aplikacije koje zahtevaju pametne ugovore, dok ostaje povezan sa sigurnošću Bitcoin.



**Napomena: Ovaj vodič se fokusira na korišćenje Liquid putem Blockstream aplikacije. Za detaljno razumevanje Liquid Network, pronaći ćete resurse u dodatku.



### 1.4. Hot Wallet podsetnik





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: svi nazivi za aplikaciju instaliranu na pametnom telefonu, računaru ili bilo kojem uređaju povezanom na Internet, omogućavajući upravljanje i osiguranje privatnih ključeva sa Bitcoin Wallet.
- Za razliku od **hardverskih novčanika**, takođe poznatih kao **Cold novčanici**, koji izoluju ključeve van mreže, softverski novčanici rade u povezanom okruženju, što ih čini podložnijim sajber napadima.





- Preporučena upotreba** :
    - Idealno za upravljanje umerenim količinama Bitcoin, posebno za dnevne transakcije.
    - Pogodan za početnike ili korisnike sa ograničenim sredstvima, za koje Hardware Wallet može izgledati suvišno.





- Ograničenja**: Manje siguran za čuvanje velikih sredstava ili dugoročnu štednju. U ovom slučaju, izaberite Hardware Wallet.




## 2. Predstavljanje Blockstream aplikacije





- Blockstream App** je mobilna (iOS, Android) i desktop aplikacija za upravljanje Bitcoin novčanicima i sredstvima na Liquid Network. Kupljena od strane [Blockstream](https://blockstream.com/) 2016. godine, ranije je bila nazvana *Green Address* a zatim *Blockstream Green*.
- Ključne karakteristike** :
    - Onchain** transakcije na Blockchain Bitcoin.
    - Transakcije na mreži **Liquid** (Sidechain za brze, poverljive razmene).
    - Portfelji samo za gledanje** za praćenje fondova bez pristupa ključevima.
    - Opcije privatnosti: povezivanje putem **Tor**-a, povezivanje na **lični čvor** putem Electrum-a, ili **SPV** verifikacija za smanjenje zavisnosti od čvorova trećih strana.
    - Funkcije **Replace-by-fee (RBF)** za ubrzavanje nepotvrđenih transakcija.
- Kompatibilnost**: Integrira hardverske novčanike kao što je **Blockstream Jade**.
- Interface**: Intuitivan za početnike, sa naprednim opcijama za stručnjake.
- Napomena**: Ovaj vodič se fokusira na upotrebu na lancu. Drugi tutorijali u dodacima pokrivaju Onchain, Samo za gledanje i desktop verziju.




## 3. Instaliranje i konfiguracija Blockstream aplikacije



### 3.1. preuzimanje





- Za Android** :
    - Preuzmite [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) sa Google Play Store-a.
    - Alternativa: Instalirajte putem APK datoteke dostupne na [Blockstream-ovom zvaničnom GitHub-u](https://github.com/Blockstream/green_android).
- Za iOS** :
    - Preuzmite [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) iz App Store-a.
- Napomena**: Obavezno preuzmite sa zvaničnih izvora kako biste izbegli lažne aplikacije.



### 3.2. početna konfiguracija





- Početni ekran**: Kada se prvi put otvori, aplikacija prikazuje ekran bez konfigurisanog Wallet. Kreirani ili uvezeni portfoliji će se ovde pojaviti kasnije.



![image](assets/fr/02.webp)





- Prilagodite postavke**: Kliknite na "Postavke aplikacije", prilagodite opcije ispod, kliknite na "Sačuvaj", restartujte aplikaciju i kreirajte svoj portfolio.



![image](assets/fr/03.webp)



#### 3.2.1. Poboljšana privatnost (samo Android)





- Funkcija**: Onemogućava snimke ekrana, skriva preglede aplikacija u upravitelju zadataka i zaključava pristup kada je telefon zaključan.
- Zašto?** : Štiti vaše podatke od neovlašćenog fizičkog pristupa ili zlonamernog softvera za snimanje ekrana.



#### 3.2.2. Povezivanje putem Tor-a





- Funkcija**: Usmeravanje mrežnog saobraćaja putem **Tor**-a, anonimne mreže koja šifrira vaše veze.
- Zašto?**: Sakrijte svoj IP Address i zaštitite svoju privatnost, idealno ako ne verujete svojoj mreži (na primer, javni Wi-Fi).
- Nedostatak**: Može usporiti aplikaciju zbog enkripcije.
- Preporuka**: Aktivirajte Tor ako je poverljivost prioritet, ali testirajte brzinu veze.



#### 3.2.3. Povezivanje na lični čvor





- Funkcija**: Povezuje aplikaciju sa vašim sopstvenim **kompletnim Bitcoin čvorom** putem **Electrum servera**.
- Zašto?**: Pruža potpunu kontrolu nad Blockchain podacima, eliminišući zavisnost od Blockstream servera.
- Preduslov**: Konfigurisani Bitcoin čvor.
- Preporuka**: Napredni korisnici koji žele maksimalni suverenitet.



#### 3.2.4. SPV verifikacija





- Funkcija**: Koristi **Pojednostavljenu verifikaciju plaćanja (SPV)** za direktnu verifikaciju određenih Blockchain podataka bez preuzimanja celog lanca.
- Zašto?**: Smanjuje zavisnost od podrazumevanog čvora Blockstream-a, dok ostaje lagan za mobilne uređaje.
- Nedostatak**: Manje siguran od Full node, jer se oslanja na čvorove trećih strana za neke informacije.
- Preporuka**: Aktivirajte SPV ako ne možete koristiti lični čvor, ali preferirajte Full node za optimalnu sigurnost.





## 4. Kreiranje Bitcoin onchain portfolija



### 4.1. Početak kreacije





- Upozorenje**: Postavite svoj portfolio u privatnom okruženju, bez kamera ili posmatrača.
- Sa početnog ekrana, kliknite na "Get Started" :



![image](assets/fr/04.webp)





- Ako želite da upravljate **Cold Wallet** (offline Wallet): kliknite na **"Connect Jade "** da biste koristili Hardware Wallet Blockstream Jade ili druge kompatibilne Cold novčanike.



![image](assets/fr/05.webp)






- Sledeći ekran se pojavljuje:



![image](assets/fr/06.webp)






- (1) **"Postavljanje mobilnog Wallet"** : Kreirajte novi Hot Wallet (Hot Wallet).
- (2) **"Restore from Backup "**: Importujte postojeći portfelj koristeći Mnemonic frazu (12 ili 24 reči). Upozorenje: Nemojte uvoziti frazu sa Cold Wallet, jer će biti izložena na povezanom uređaju, čime se poništava njena sigurnost.
- (3) **"Watch-Only "**: Uvezite postojeći portfelj samo za čitanje, da biste videli stanje (npr. vašeg Cold Wallet) bez izlaganja Mnemonic fraze. Pogledajte "Watch Only" vodič u dodatku.



**U ovom vodiču**: Kliknite na **"Setup Mobile Wallet"** da biste kreirali Hot Wallet.


Vaš Wallet je automatski kreiran i početna stranica Wallet, ovde nazvana "Moj Wallet 5", je prikazana:



![image](assets/fr/07.webp)



**Važno**: Blockstream App je pojednostavio kreiranje Wallet tako što automatski ne prikazuje seed frazu od 12 reči. *Iako se portfolio sada kreira jednim klikom, rizikujete da izgubite pristup svojim sredstvima ako ne sačuvate svoju seed frazu*.



### 4.2. Sačuvaj seed frazu





- Na početnom ekranu Wallet, kliknite na karticu "Security", zatim na prompt "Back Up" ili na meni "Recovery Phrase":



![image](assets/fr/08.webp)



seed 12-rečeni izraz će biti prikazan da ga sačuvate.





- Zapišite svoju frazu za oporavak s najvećom pažnjom. Zapišite je na papir ili metal i čuvajte na sigurnom mestu (sigurno, vanmrežno mesto). Ova fraza je vaš jedini način pristupa vašim bitcoinima u slučaju gubitka uređaja ili brisanja aplikacije.
- Takođe je važno napomenuti da svako ko ima ovu frazu može ukrasti sve vaše bitkoine. Nikada je ne čuvajte digitalno:
 - Nema snimka ekrana
 - Nema rezervnih kopija oblaka, e-pošte ili poruka
 - Bez kopiranja/lepljenja (rizik od čuvanja u međumemoriji)



**! Ova tačka je kritična**. Za više informacija o rezervnoj kopiji :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Proveri seed rečenicu



Pre nego što pošaljete sredstva na Address povezanu sa ovom seed frazom, morate testirati rezervnu kopiju svojih 12 reči.


Da bismo to uradili, napisaćemo referencu, obrisati Wallet, vratiti je pomoću rezervne kopije i proveriti da li je referenca nepromenjena.





- Na početnom ekranu Wallet, kliknite na karticu "Settings", zatim na "Wallet Details", i kopirajte zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Napomena: zpub Address može se uvesti u vašu Blockstream aplikaciju za funkciju "Samo za gledanje" (pogledajte Dodatak).





- Izbrišite aplikaciju, zatim obnovite Wallet putem **"Restore from Backup "** unosom Mnemonic fraze, i proverite da li je zpub nepromenjen. Ako jeste, vaš bekap je ispravan i možete poslati sredstva na Wallet.





- Da biste saznali više o tome kako izvesti test oporavka, ovde je posvećen vodič :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Obezbeđivanje pristupa aplikaciji



Zaključajte pristup aplikaciji jakim PIN kodom:




- Sa početnog ekrana Wallet, idite na **"Security "** zatim kliknite na **"PIN "**
- Unesite i potvrdite **nasumični 6-cifreni PIN kod**.



**Biometrijska opcija**: Dostupna za dodatnu pogodnost, ali manje sigurna od robusnog PIN koda (rizik od neovlašćenog pristupa, npr. otisak prsta ili skeniranje lica tokom spavanja).



**Napomena**: PIN osigurava uređaj, ali samo seed fraza može se koristiti za povrat sredstava.





## 5. Korišćenje Liquid Wallet



### 5.1. Primi "L-BTC" bitkoine



Da biste primili Liquid-Bitcoins (L-BTC), dostupno je nekoliko opcija. Možete zamoliti nekoga da vam ih pošalje direktno tako što ćete podeliti Liquid primanje Address, što je detaljno opisano u nastavku.



Alternativno, Exchange vaše bitkoine onchain ili putem Lightning Network za L-BTC koristeći [most kao što je Boltz](https://boltz.Exchange/): unesite vaš Liquid primajući Address, izvršite uplatu kako želite i primite vaš L-BTC.





- Sa početnog ekrana portfolija, kliknite na '"**Transact**" zatim **"Receive "**.



![image](assets/fr/19.webp)





- Podrazumevano, aplikacija prikazuje prazan **receipt Address, onchain** (SegWit v0 format, počinje sa `bc1q...`). Kliknite na "Bitcoin" da biste izabrali **Liquid Bitcoin** :



![image](assets/fr/20.webp)





- Opcije** :
 - (1) Kliknite na strelice da biste izabrali drugi novi Address povezan sa ovom seed rečenicom.
    - (2) Takođe možete izabrati Address iz već korišćenih/prikazanih, klikom na tri tačke u gornjem desnom uglu, a zatim na "Lista adresa"
    - (3) Da biste zatražili određeni iznos, kliknite na tri tačke u gornjem desnom uglu, izaberite "Zatraži iznos" i unesite željeni iznos. QR će biti ažuriran, a Address će biti zamenjen Bitcoin URI-jem za plaćanje.



![image](assets/fr/21.webp)





- Podelite Address/URI klikom na "**Share**", kopiranjem teksta ili skeniranjem QR koda.
- Verifikacija**: Proverite Address podeljen sa primaocem koliko god je moguće kako biste izbegli greške ili napade (npr. malver koji menja sadržaj međumemorije).



### 5.2. pošalji bitkoine





- Sa početnog ekrana portfolija, kliknite na "**Transact**" zatim **"Send "** :



![image](assets/fr/22.webp)





- Unesite detalje** :
    - (1) Unesite **Address primaoca** tako što ćete ga zalepiti ili skenirati QR kod.
    - (2) Proverite imovinu i račun sa kojeg se sredstva šalju.
    - (3) Naznačite **iznos** koji treba poslati. Možete izabrati jedinicu: L-BTC, L-satoši, USD, ...



![image](assets/fr/23.webp)





- Proveri** :
    - Proveri Address, iznos i troškove na ekranu sažetka.
    - Greška Address može rezultirati nepovratnim gubitkom sredstava. Pazite na zlonamerni softver koji menja sadržaj u međuspremniku.



![image](assets/fr/24.webp)





- Potvrda**: Prevucite dugme „Pošalji“ da potpišete i distribuirate transakciju.
- Praćenje**: U Wallet kartici "Transact", transakcija se pojavljuje kao "Nepotvrđeno", zatim "Potvrđeno", pa "Završeno":



![image](assets/fr/25.webp)





- Vreme između 2 bloka je 1 minut na Liquid, tako da je transakcija brzo potvrđena i završena.




## Aneksi



### A1. Ostali vodiči za Blockstream aplikaciju



Korišćenje Onchain mreže



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Uvoz i praćenje Wallet u režimu "Samo za gledanje"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Desktop verzija



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Najbolje prakse



Da biste koristili **Blockstream App** sigurno i efikasno, pratite ove preporuke. One će vam pomoći da zaštitite svoja sredstva, optimizujete svoje transakcije i sačuvate svoju poverljivost na mrežama **Bitcoin (onchain)**, **Liquid** i **Lightning**.





- Osigurajte svoju frazu za oporavak** :
 - Uputstvo: Čuvanje vaše Mnemonic fraze



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Koristite sigurnu autentifikaciju** :
 - Aktivirajte **jak PIN** ili **biometrijsku autentifikaciju** (otisak prsta ili prepoznavanje lica) kako biste zaštitili pristup aplikaciji.
 - Nikada ne delite svoj PIN ili biometrijske podatke.





- Zaštitite svoju privatnost** :
 - generate novi Address za svaku onchain prijem ili Liquid za ograničavanje praćenja na Blockchain.
 - Aktiviraj funkcije "Enhanced Privacy", "Tor" i "SPV".
 - Za maksimalnu poverljivost, povežite svoj Wallet sa sopstvenim Bitcoin čvorom putem Electrum servera umesto korišćenja javnog čvora.





- Izaberite mrežu koja najbolje odgovara vašim potrebama** :
 - Onchain**: Preferirano za dugoročno čuvanje ili transakcije velike vrednosti (naknade zanemarljive u odnosu na iznos).
 - Liquid**: Koristite za brze, niskobudžetne transfere sa poboljšanom poverljivošću.
 - Lightning**: Odaberite trenutne, niskotarifne transfere za male iznose.





- Uvek proveravajte adrese za dostavu** :
 - Pre nego što pošaljete sredstva, pažljivo proverite Address. Sredstva poslana na pogrešan Address su zauvek izgubljena. Koristite kopiranje/lepljenje ili skeniranje QR koda, nikada ne kopirajte/modifikujte Address ručno.





- Optimizujte troškove** :
 - Za transakcije na lancu, odaberite odgovarajuće naknade (sporo, srednje, brzo) u skladu sa hitnošću i zagušenošću mreže.
 - Koristite Liquid, ili Lightning za male količine.





- Ažurirajte aplikaciju redovno




### A3. Dodatni resursi





- Zvanični linkovi:**
 - [Zvanična veb stranica](https://blockstream.com/)**
 - [Podrška za mobilnu aplikaciju](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokumentacija i ćaskanje
 - [GitHub](https://github.com/Blockstream/green_android)**





- Block Explorers :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Munja: **[1ML (Lightning Network)](https://1ml.com/)**





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
