---
name: BIP-85
description: Kako mogu koristiti BIP-85 za generate više seed fraza iz glavnog seed?
---
![cover](assets/cover.webp)



## 1. Razumevanje BIP-85



### 1.1 Šta je BIP-85?



BIP-85 je napredna funkcija koja vam omogućava da kreirate nekoliko **seed sekundarnih fraza** iz jedne **seed glavne fraze**.



Svaka seed sekundarna rečenica može se koristiti za kreiranje potpuno nezavisnog Bitcoin portfolija. Ovi portfoliji mogu se koristiti za razne svrhe: Hot Wallet na mobilnom, portfolio za rođaka, zaseban portfolio štednje, itd.



Sve podfraze seed su **matematički izvedene**, ali je **nemoguće pratiti nazad do glavne fraze seed** iz podfraze. Ovo osigurava potpunu separaciju između svakog portfolija.



Sve dok imate pristup svojoj seed glavnoj frazi (i pridruženoj passphrase ako je koristite), možete regenerisati bilo koju seed sekundarnu frazu **identično**, bez potrebe da je posebno čuvate.



### 1.2 Zašto koristiti BIP-85?



BIP-85 je koristan ako želite da:





- Kreiraj nekoliko nezavisnih Bitcoin portfolija bez višestrukih rezervnih kopija.
- Upravljajte svojim sredstvima prema različitim namjenama (štednja, troškovi, porodica, projekti)
- Garantovanje zaštite za rođake („Funkcija Ujak Džim“)
- Izbrišite portfolio bez gubitka pristupa vašim sredstvima
- Pojednostavite svoju sigurnost: samo jedna seed ključna fraza za zaštitu



### 1.3 Prednosti u odnosu na BIP-32



Sa BIP-32, jedna seed rečenica može se koristiti za generate kompletnu hijerarhiju Bitcoin naloga i adresa, koristeći putanje derivacije (na primer: `m/44'/0'/0'/0/0`). Svaka putanja može predstavljati poseban nalog, ali **svi ostaju povezani sa istom seed rečenicom**. Dakle, ako je ova seed fraza kompromitovana, **svi izvedeni nalozi postaju dostupni**.



Sa BIP-85, glavna rečenica seed može se koristiti za generate nekoliko potpuno nezavisnih seed sekundarnih rečenica: **ako je jedno od ovih sekundarnih semena ugroženo, napadač nikada neće moći da se vrati na glavnu seed ili pristupi drugim portfeljima**.


Ovo omogućava segmentaciju rizika:





- Možete koristiti sekundarni seed za Hot Wallet ili privremenu upotrebu, prihvatajući veće izlaganje.
- Čak i ako je ovaj Hot Wallet ugrožen, vaša druga sredstva, zaštićena drugim sekundarnim seed-ovima ili čuvana van mreže, **ostaju sigurna**.



S druge strane, za oba BIP-32 i BIP-85, ako je glavni seed kompromitovan, **sva sredstva su ranjiva**. Stoga je ključno zaštititi ga najvišim nivoom sigurnosti.



![image](assets/fr/02.webp)


## 2. Praktične upotrebe za BIP-85



BIP-85 vam omogućava da kreirate više Bitcoin portfolija iz jedne seed osnovne fraze, svaki sa svojom seed sekundarnom frazom. Ovde je pet praktičnih primera korišćenja za organizovanje i obezbeđivanje vaših Bitcoin sredstava. Svaki primer objašnjava zašto je korišćenje BIP-85 praktičnije nego upravljanje višestrukim nalozima sa jednom seed frazom putem BIP-32.



### 2.1 Ograničavanje rizika manje sigurnog portfolija





- Scenario**: Koristite "Hot Wallet" Wallet (instaliran na uređaju povezanom na Internet), za dnevne transakcije.
- Rešenje BIP-85**: Kreirate seed sekundarnu frazu posvećenu ovom portfoliju.
- Prednost nad BIP-32**: Ne morate da uvozite seed primarnu frazu na vaš telefon, smanjujući rizik od hakovanja. Samo je seed sekundarna fraza ugrožena, štiteći vaše druge novčanike. Sa BIP-32, morate koristiti seed glavnu frazu i putanju zaobići, izlažući sva vaša sredstva.



### 2.2 Kreirajte portfolio za člana porodice





- Scenario**: Postavili ste Bitcoin Wallet za nekoga bliskog vama (npr. vašu majku), dok ste u mogućnosti da ga povratite ako ga izgube.
- Rešenje BIP-85**: Kreirate posvećenu seed sekundarnu rečenicu i delite samo ovu.
- Prednost nad BIP-32**: Sa BIP-32, kreiranje naloga za voljenu osobu zahteva ili deljenje vaše glavne seed fraze, rizikujući sva vaša sredstva i komplikujući upravljanje za vašu voljenu osobu (upravljanje granajućim putanjama), ili kreiranje nove seed fraze koju treba sačuvati pored vaše glavne seed fraze.



### 2.3 Olakšavanje upravljanja odvojenim portfeljima





- Scenario**: Razdvajate svoje bitkoine za različite svrhe (npr. dugoročna štednja, sredstva bez KYC).
- Rešenje BIP-85**: Kreirate seed sekundarne fraze posvećene svakom cilju.
- Prednost nad BIP-32**: Sa BIP-32, svi nalozi dele istu seed frazu, što komplikuje upravljanje u portfeljima trećih strana zahtevajući da se upravlja derivacionim putanjama kao što je `m/44'/0'/0'`. Pored toga, nije moguće dodeliti poseban nalog po uređaju (npr. "štednja na Coldcard", "dnevno na mobilnom", "odmor na Trezor"). BIP-85 dodeljuje jedinstvenu sekundarnu seed frazu po cilju, što je lako identifikovati i uvesti zasebno na svakom uređaju.



### 2.4 Korišćenje privremenog Wallet za transakcije





- Scenario**: Trebate privremeni portfolio za jednokratnu transakciju ili za očuvanje poverljivosti (npr.: mešanje sredstava, interakcija sa Exchange KYC, itd.).
- Rešenje BIP-85**: Kreirate seed sekundarnu rečenicu, koristite je za transakciju, a zatim je uništite ako je potrebno, znajući da se može regenerisati.
- Prednost nad BIP-32**: Sa BIP-32, privremeni račun zavisi od seed glavne rečenice, izlažući sva vaša sredstva ako bude ugrožena.





## 3. Pre nego što počneš





- Hardware** (opciono)
 - Coldcard Mk4 ili Q1
 - MicroSD kartica





- Osnovno znanje
 - Razumevanje Mnemonic fraza (BIP-39): lista od 12 do 24 reči za čuvanje portfolija.
 - Znajte šta je Bitcoin Wallet: softver ili uređaj za upravljanje vašim bitcoinima, i kako ga obnoviti pomoću Mnemonic fraze.
 - Više resursa u Aneksima.





- Kompatibilan** softver
 - Sparrow wallet (računar, samo za gledanje ili napredno upravljanje)
 - Nunchuck (mobilni, za više potpisa)
 - BlueWallet (mobilni)
 - ...





- 3.4 Coldcard** konfiguracija
 - Inicijalizujte seed rečenicu od 24 reči na Coldcard-u.
 - Opcionalno: Dodajte passphrase za osiguranje pristupa BIP-85 granama.
 - Aktiviraj korisne opcije: NFC (za izvoz), onemogući USB na bateriji (sigurnost).




## 4. Uputstvo korak po korak



Pratite ove korake da biste kreirali, koristili i preuzeli sekundarni Mnemonic sa BIP-85 na vašem Coldcard-u.



### 4.1 generate a seed sekundarna rečenica



Kreiraćete seed sekundarnu frazu iz vaše seed glavne fraze.


Uključite svoj Coldcard, unesite svoj PIN kod.





- 1. Ako ste primenili passphrase na vaš glavni seed:**
 - Sa početnog ekrana idite na `passphrase`.
    - Izaberite `Add Word` i unesite svoju lozinku.
    - Pritisnite `Apply`.
    - Proverite identitet Wallet: Idite na `Advanced > View Identity` da zabeležite otisak prsta Wallet.





- 2. Idi na BIP-85** meni
 - Sa početnog ekrana idite na `Napredno > Izvedi seed B85`
 - Pročitajte upozorenje i potvrdite.



ColdCard vas obaveštava da su semena generisana matematički izvedena iz vašeg glavnog seed, ali kriptografski potpuno nezavisna.


![image](assets/fr/03.webp)





- 3. Izaberite format


Odaberite format fraze seed: 12, 18 ili 24 reči. Proverite broj reči prihvaćenih od strane Wallet u koji želite da uvezete vašu seed frazu.


![image](assets/fr/04.webp)





- 4. Odaberi indeks
 - Unesite indeks između 0 i 9999.
 - Ovaj indeks je ključan za regeneraciju sekundarnog seed u kasnijem periodu. Čuvajte ga pažljivo sa etiketom kao što je: "Index 1 = Wallet mobile", "Index 2 = family project", "Index 4 = test mix", ...
 - Ako ga izgubite, nećete izgubiti pristup svojim sredstvima, ali ćete morati testirati kombinacije od 0 do 9999 da biste ih pronašli.


![image](assets/fr/05.webp)





- 5. Zabeleži ili izvezi seed sekundarnu rečenicu**


ColdCard sada prikazuje novu seed sekundarnu rečenicu. Možete :




 - **Beleška ručno**.
 - Pritisnite :
     - 1` da biste ga sačuvali na SD kartici
     - `2` za **ulazak u "use this seed"** režim na ColdCard-u (korisno za izvoz ili potpisivanje transakcije)
     - 3` da prikaže **QR kod** (za skeniranje pomoću mobilne aplikacije kao što je BlueWallet ili Nunchuck)
     - 4` da ga pošaljete putem **NFC**



💡 U ovom trenutku, imate nezavisnu seed frazu, koja se može koristiti u bilo kom Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Korišćenje sekundarnog seed



Sada možete koristiti ovaj izvedeni seed za kreiranje novog portfolija u :




- mobilna aplikacija
- još jedan Hardware Wallet
- Multisig portfolio



### 4.3 Oporavak izgubljene sekundarne fraze seed



Da biste u bilo kom trenutku preuzeli sekundarni seed, ponovite proces:


1. Ponovo pokreni svoj ColdCard


2. Unesite svoj PIN


3. Unesite svoj passphrase, ako je definisan


4. Idite na `Advanced > Derive seed B85`


5. Izaberite format (12/18/24 reči)


6. Unesite isti indeks (npr. `1`)


7. Dobijaćete tačno isti sekundarni seed




## 5. Ograničenja, rizici i najbolje prakse



### 5.1 Zavisnost od seed glavna rečenica + passphrase



Korišćenje BIP85 u potpunosti se oslanja na glavnu rečenicu od 24 reči seed, kao i na passphrase ako ste je primenili.




- Iz ova dva Elements, sve seed sekundarne fraze mogu biti regenerisane.
- Bez jednog od ovih 2 Elements, gubite pristup svim izvedenim portfeljima.



### 5.2 Rizici u konfiguraciji sa više potpisa



Snažno savetujemo protiv korišćenja sekundarnih seed fraza generisanih iz iste primarne seed fraze u multi-sig konfiguraciji: ako su uređaj ili primarna seed fraza kompromitovani, napadač bi mogao regenerisati sve multi-sig ključeve.



### 5.3 Kompatibilnost softvera



Nisu sve aplikacije direktno podržane derivacijom BIP85. Međutim, seed-ovi generisani putem BIP85 su standardni BIP39 seed-ovi (12, 18 ili 24 reči), i stoga se mogu koristiti u bilo kojem portfoliju kompatibilnom sa BIP39.



### 5.4 BIP85 account register



Preporučuje se da vodite ažurirani lični registar seed sekundarnih fraza.




- Omogućava vam da brzo saznate koji BIP85 indeks odgovara kojem portfoliju, bez potrebe da čuvate seed sekundarne fraze.
- Ovaj registar treba da ostane minimalistički, bez eksplicitnog pominjanja Bitcoin, i treba da bude čuvan odvojeno od glavnog seed. Ne zaboravite da ga pomenete u svom planu nasledstva.



Registar može sadržati :




- bIP85 indeks korišćen (broj od 0 do 9999)
- ime za upotrebu ili referencu (npr. Hot Wallet, lična štednja, Wallet od mame)
- ako je potrebno, Wallet otisak prsta za verifikaciju u ColdCard



### 5.5 Bekap



Bekapovi moraju uključivati :




- glavni seed
- gW-76 (ako se koristi)



Nikada ne skladištiti zajedno:




- glavni seed i passphrase
- glavni seed i registar računa BIP85



Više resursa u dodacima.




## DODACI



## A.1 Rečnik





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed fraza](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Sačuvaj svoju frazu za oporavak



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Razumevanje passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Kako funkcionišu Bitcoin portfoliji



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f