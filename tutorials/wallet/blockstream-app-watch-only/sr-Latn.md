---
name: Blockstream App - Watch-Only
description: Kako da konfigurišem Watch-only wallet na Blockstream aplikaciji?
---

![cover](assets/cover.webp)


## 1. Uvod


### 1.1 Cilj tutorijala





- Ovaj vodič objašnjava kako postaviti i koristiti funkciju **Samo za gledanje** mobilne aplikacije **Blockstream App** za praćenje Bitcoin Wallet bez pristupa njegovim privatnim ključevima.
- Obuhvata instalaciju, početnu konfiguraciju, uvoz proširenog javnog ključa i njegovo korišćenje za praćenje stanja i generate adresa za primanje.
- Napomena: Drugi tutorijali, navedeni u dodatku, pokrivaju Onchain, Liquid i desktop verziju.



### 1.2. Ciljna publika





- **Početnici**: Korisnici koji žele da prate Bitcoin portfolio (često povezan sa Hardware Wallet) putem intuitivne mobilne aplikacije.
- **Srednji korisnici**: Ljudi koji žele da upravljaju portfolijima samo za čitanje dok koriste opcije privatnosti kao što su Tor ili SPV.
- **Vlasnici Hardware Wallet**: Da provere svoje stanje i generate adrese bez povezivanja svog uređaja.
- **Preduzeća i prodavnice**:
 - Pratite svoje transakcije za računovodstvene svrhe bez izlaganja svojih privatnih ključeva.
 - Verifikujte transakcije primljene bez unosa njihovih privatnih ključeva u sisteme za online plaćanje.
 - Omogućite zaposlenima da generate nove adrese za prijem bez pristupa privatnim ključevima.
- **Organizacije i crowdfunding**: Prikazati stanje transparentno donatorima bez omogućavanja pristupa sredstvima.



### 1.3. Uvođenje Samo-za-gledanje



A **Watch-Only** Wallet omogućava vam da pratite transakcije i stanje Bitcoin Wallet bez pristupa privatnim ključevima. Za razliku od konvencionalnog Wallet, on skladišti samo javne podatke, kao što je **prošireni javni ključ** (koji je doveo do **xpub**, zatim "zpub", "ypub", itd.), što mu omogućava da dobije adrese za primanje i prati istoriju transakcija na Blockchain Bitcoin. Odsustvo privatnih ključeva onemogućava isplatu sredstava iz aplikacije, garantujući poboljšanu sigurnost.



![image](assets/fr/10.webp)



**Zašto koristiti Watch-only wallet?**





- **Bezbednost**: Idealno za praćenje portfolija osiguranog pomoću **Hardware Wallet** bez izlaganja privatnih ključeva na povezanom uređaju.
- **Pogodnost**: Omogućava vam da proverite stanje i generate nove adrese primalaca bez povezivanja sa Hardware Wallet.
- **Poverljivost**: Kompatibilno sa opcijama kao što su **Tor** ili **SPV** za ograničavanje zavisnosti od servera trećih strana.
- **Use cases**: Praćenje sredstava u pokretu, generisanje adresa za primanje uplata, ili verifikacija transakcija bez rizikovanja privatnih ključeva.



![image](assets/fr/01.webp)



### 1.4. Prošireni javni ključevi



**Prošireni javni ključ** (xpub, ypub, zpub, itd.) je deo podataka izveden iz Bitcoin Wallet koji generiše sve podređene javne ključeve i njihove povezane adrese za primanje, bez davanja pristupa privatnim ključevima.





- Kako funkcioniše: Prošireni javni ključ se generiše iz seed fraze putem determinističkog procesa (BIP-32). On kreira hijerarhijsko stablo podređenih javnih ključeva, od kojih svaki može biti konvertovan u primanje Address. Koristeći isti put derivacije (npr. `m/44'/0'/0'`) kao i posmatrani Wallet, Watch-only wallet generiše iste adrese, omogućavajući praćenje sredstava i kreiranje novih adresa za primanje.



![image](assets/fr/11.webp)





- Prošireni tipovi javnih ključeva
- **xpub**: Koristi se za Legacy portfolije (adrese koje počinju sa "1", BIP-44) i Taproot portfolije (adrese koje počinju sa "bc1p", BIP-86).
- **ypub**: Dizajniran za kompatibilne SegWit novčanike (adrese koje počinju sa "3", BIP-49).
- **zpub**: Povezano sa native SegWit portfolijima (adrese koje počinju sa "bc1q", BIP-84).
- **Drugi (tpub, upub, vpub, itd.)**: Koriste se za alternativne mreže (kao što je Testnet) ili specifične standarde. Na primer, tpub je za Testnet mrežu.





- **Distinction**: The choice between xpub, ypub, or zpub depends on the Address type (legacy, SegWit, Taproot or nested SegWit) and the BIP standard used by the Wallet. Check the format required by your source portfolio to ensure compatibility with Blockstream App.





- **Bezbednost i poverljivost**: Prošireni javni ključ nije osetljiv u smislu bezbednosti, jer ne omogućava trošenje sredstava (nema pristup privatnim ključevima). Međutim, osetljiv je u smislu poverljivosti, jer otkriva sve javne adrese i povezanu istoriju transakcija.



**Preporuka**: Zaštitite svoj prošireni javni ključ kao poverljive informacije.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet podsetnik





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: svi nazivi za aplikaciju instaliranu na pametnom telefonu, računaru ili bilo kojem uređaju povezanom na Internet, omogućavajući upravljanje i osiguranje privatnih ključeva sa Bitcoin Wallet.
- Za razliku od **hardverskih novčanika**, takođe poznatih kao **Cold novčanici**, koji izoluju ključeve van mreže, softverski novčanici rade u povezanom okruženju, što ih čini podložnijim sajber napadima.





- **Preporučena upotreba**:
    - Idealno za upravljanje umerenim količinama Bitcoin, posebno za dnevne transakcije.
    - Pogodan za početnike ili korisnike sa ograničenim sredstvima, za koje Hardware Wallet može izgledati suvišno.





- **Ograničenja**: Manje siguran za čuvanje velikih sredstava ili dugoročnu štednju. U ovom slučaju, izaberite Hardware Wallet.




## 2. Uvođenje Blockstream aplikacije





- **Blockstream App** je mobilna (iOS, Android) i desktop aplikacija za upravljanje Bitcoin portfolijima i sredstvima na Liquid Network. Kupljena od strane [Blockstream](https://blockstream.com/) 2016. godine, ranije je bila nazvana *Green Address* a zatim *Blockstream Green*.
- **Ključne karakteristike**:
- **Onchain** transakcije na Blockchain Bitcoin.
    - Transakcije na mreži **Liquid** (Sidechain za brze, poverljive razmene).
- **Portfelji samo za gledanje** za praćenje fondova bez pristupa ključevima.
    - Opcije privatnosti: povezivanje putem **Tor**-a, povezivanje na **lični čvor** putem Electrum-a, ili **SPV** verifikacija za smanjenje zavisnosti od čvorova trećih strana.
    - Funkcije **Replace-by-fee (RBF)** za ubrzavanje nepotvrđenih transakcija.
- **Kompatibilnost**: Integrira hardverske novčanike kao što je **Blockstream Jade**.
- **Interface**: Intuitivan za početnike, sa naprednim opcijama za stručnjake.
- **Napomena**: Ovaj vodič se fokusira na upotrebu na lancu. Drugi tutorijali u Dodacima pokrivaju Onchain, Samo za gledanje i desktop verziju.




## 3. Instaliranje i konfiguracija Blockstream aplikacije



### 3.1. preuzimanje





- **Za Android**:
    - Preuzmite [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) sa Google Play Store-a.
    - Alternativa: Instalirajte putem APK datoteke dostupne na [Blockstream-ovom zvaničnom GitHub-u](https://github.com/Blockstream/green_android).
- Za **iOS**:
    - Preuzmite [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) iz App Store-a.
- **Napomena**: Obavezno preuzmite sa zvaničnih izvora kako biste izbegli lažne aplikacije.



### 3.2. početna konfiguracija





- **Početni ekran**: Kada se prvi put otvori, aplikacija prikazuje ekran bez konfigurisanog Wallet. Kreirani ili uvezeni portfoliji će se ovde pojaviti kasnije.



![image](assets/fr/02.webp)





- **Prilagodite postavke**: Kliknite na "Postavke aplikacije", prilagodite opcije ispod, kliknite na "Sačuvaj", restartujte aplikaciju i kreirajte svoj portfolio.



![image](assets/fr/03.webp)



#### 3.2.1. Poboljšana privatnost (samo Android)





- **Funkcija**: Onemogućava snimke ekrana, skriva preglede aplikacija u upravitelju zadataka i zaključava pristup kada je telefon zaključan.
- **Zašto?**: Štiti vaše podatke od neovlašćenog fizičkog pristupa ili zlonamernog softvera za snimanje ekrana.



#### 3.2.2. Povezivanje putem Tor-a





- **Funkcija**: Usmeravanje mrežnog saobraćaja putem **Tor**-a, anonimne mreže koja šifruje vaše veze.
- **Zašto?**: Sakrijte svoj IP Address i zaštitite svoju privatnost, idealno ako ne verujete svojoj mreži (javni Wi-Fi, na primer).
- **Nedostatak**: Može usporiti aplikaciju zbog enkripcije.
- **Preporuka**: Aktivirajte Tor ako je poverljivost prioritet, ali testirajte brzinu veze.



#### 3.2.3. Povezivanje na lični čvor





- **Funkcija**: Povezuje aplikaciju sa vašim sopstvenim **kompletnim Bitcoin čvorom** putem **Electrum servera**.
- **Zašto?**: Pruža potpunu kontrolu nad Blockchain podacima, eliminišući zavisnost od Blockstream servera.
- **Preduslov**: Konfigurisani Bitcoin čvor.
- **Preporuka**: Napredni korisnici koji žele maksimalni suverenitet.



#### 3.2.4. SPV verifikacija





- **Funkcija**: Koristi **Simplified Payment Verification (SPV)** za direktnu verifikaciju određenih Blockchain podataka bez preuzimanja celog lanca.
- **Zašto?**: Smanjuje zavisnost od podrazumevanog čvora Blockstream-a, dok ostaje lagan za mobilne uređaje.
- **Nedostatak**: Manje siguran od Full node, jer se oslanja na čvorove trećih strana za neke informacije.
- **Preporuka**: Aktivirajte SPV ako ne možete koristiti lični čvor, ali preferirajte Full node za optimalnu sigurnost.





## 4. Kreiranje Bitcoin portfolija "Samo za gledanje"



### 4.1. Oporavi prošireni javni ključ



Da biste postavili Watch-only wallet, prvo morate dobiti prošireni javni ključ (xpub, ypub, zpub, itd.) Wallet koji će se pratiti. Ove informacije su obično dostupne u postavkama ili u odeljku "Wallet informacije" vašeg softvera ili Hardware Wallet.





- Primer sa aplikacijom Blockstream: Sa početnog ekrana Wallet idite na "Settings", zatim "Wallet Details", i kopirajte zpub :



![image](assets/fr/09.webp)





- Alternativa 1: generate QR kod koji sadrži prošireni javni ključ za skeniranje u sledećem koraku.
- Alternativa 2: Koristite output descriptor ako vaš Wallet to omogućava.



### 4.2. uvoz Wallet Samo za gledanje





- **Upozorenje**: Postavite svoj portfolio u privatnom okruženju, bez kamera ili posmatrača.
- Sa početnog ekrana, kliknite na "Set up a new portfolio" a zatim na "Get Started" :



![image](assets/fr/04.webp)





- Sledeći ekran se pojavljuje:



![image](assets/fr/06.webp)






- (1) **"Postavljanje Mobilnog Wallet"** : Kreirajte novi Hot Wallet. Pogledajte tutorijal "Blockstream App - Onchain" u dodatku.
- (2) **"Obnovi iz rezervne kopije "**: Uvezi postojeći portfolio koristeći Mnemonic frazu (12 ili 24 reči). Oprez: Nemoj uvoziti frazu sa Cold Wallet, jer će biti izložena na povezanom uređaju, čime se poništava njena sigurnost.
- (3) **"Watch-Only "**: opcija koja nas zanima za ovaj vodič.





- Zatim izaberite "**Single signature**" i mrežu "**Bitcoin**":



![image](assets/fr/12.webp)





- Nalepite prošireni javni ključ (xpub, ypub, zpub, itd.), skenirajte odgovarajući QR kod ili unesite output descriptor. Čak i ako aplikacija navodi "xpub", ključevi ypub, zpub, itd. su takođe ovlašćeni. Zatim kliknite na "Poveži":



![image](assets/fr/13.webp)




### 4.3. Korišćenje Wallet samo za gledanje



Nakon uvoza, Watch-only wallet prikazuje ukupan saldo i istoriju transakcija adresa izvedenih iz proširenog javnog ključa. Vidljive su samo onchain transakcije (transakcije Liquid se ignorišu). Da biste pratili Liquid Wallet, ponovite uvoz odabirom "Liquid" u prethodnom koraku.





- **Pogledaj stanje i istoriju**: sa početnog ekrana, pogledaj ukupno stanje i istoriju transakcija na lancu:



![image](assets/fr/14.webp)





- generate prima Address**: Kliknite na "Transact", zatim "Receive", da kreirate novi onchain Address. Podelite ga putem QR koda ili kopirajte da primite sredstva:



![image](assets/fr/15.webp)





- **Pošalji sredstva**: Kliknite na **"Transakcija"**, zatim **"Pošalji"**. Možete uneti:
 - Primalacov Address.
 - Iznos transakcije.
 - Naknade za transakciju.



Međutim, pošto Watch-only wallet ne drži privatne ključeve, ne možete direktno slati sredstva. Da biste potpisali transakciju, povežite svoje Hardware Wallet ili Exchange PSBT-ove skeniranjem QR kodova (opcija dostupna na Coldcard Q, na primer).



![image](assets/fr/16.webp)





- **Napomena**: Uvek proverite prijemni Address i detalje transakcije kako biste izbegli greške. Sredstva poslana na pogrešan Address ne mogu se povratiti.




## Aneksi



### A1. Ostali Blockstream App tutorijali





- Korišćenje Onchain mreže :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Korišćenje Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Desktop verzija :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Prošireni javni ključevi





- Rečnik :
 - [Prošireni javni ključevi](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Kurs :
 - [Prošireni javni ključevi](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Najbolje prakse



Da biste koristili **Blockstream App** sigurno i efikasno, pratite ove preporuke. One će vam pomoći da zaštitite svoja sredstva, optimizujete svoje transakcije i sačuvate svoju poverljivost na mrežama **Bitcoin (onchain)**, **Liquid** i **Lightning**.





- **Osigurajte svoju frazu za oporavak**:
 - Uputstvo: Čuvanje vaše Mnemonic fraze



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Koristite sigurnu autentifikaciju**:
 - Aktivirajte **jak PIN** ili **biometrijsku autentifikaciju** (otisak prsta ili prepoznavanje lica) kako biste zaštitili pristup aplikaciji.
 - Nikada ne delite svoj PIN ili biometrijske podatke.





- **Zaštitite svoju privatnost**:
 - generate novi Address za svaki onchain ili Liquid prijem kako bi se ograničilo praćenje na Blockchain.
 - Aktiviraj funkcije "Enhanced Privacy", "Tor" i "SPV".
 - Za maksimalnu poverljivost, povežite svoj Wallet sa sopstvenim Bitcoin čvorom preko Electrum servera umesto korišćenja javnog čvora.





- **Izaberite mrežu koja najbolje odgovara vašim potrebama**:
- **Onchain**: Preferirano za dugoročno čuvanje ili transakcije velike vrednosti (naknade zanemarljive u odnosu na iznos).
- **Liquid**: Koristite za brze, niskobudžetne transfere sa poboljšanom poverljivošću.
- **Lightning**: Odaberite trenutne, niskotarifne transfere za male iznose.





- **Uvek proveravajte adrese za dostavu**:
 - Pre nego što pošaljete sredstva, pažljivo proverite Address. Sredstva poslana na pogrešan Address su zauvek izgubljena. Koristite kopiranje/lepljenje ili skeniranje QR koda, nikada ne kopirajte/modifikujte Address ručno.





- **Optimizujte troškove**:
 - Za transakcije na lancu, odaberite odgovarajuće naknade (sporo, srednje, brzo) u zavisnosti od hitnosti i zagušenja mreže.
 - Koristite Liquid, ili Lightning za male količine.





- Ažurirajte aplikaciju redovno




### A4. Dodatni resursi





- **Zvanični Blockstream linkovi:**
- [Zvanična veb stranica](https://blockstream.com/)
- [Podrška za mobilnu aplikaciju](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentacija i ćaskanje
- [GitHub](https://github.com/Blockstream/green_android)





- **Block Explorers:**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Lightning: **[1ML (Lightning Network)](https://1ml.com/)**





- **Učenje i tutorijali:** **[Plan ₿ Network](https://planb.network/)**
  - Osiguravanje vaše fraze za oporavak



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Glosar](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Rečnik](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb