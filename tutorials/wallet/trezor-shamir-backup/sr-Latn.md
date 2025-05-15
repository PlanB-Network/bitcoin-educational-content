---
name: Trezor Shamir Backup
description: Jedno-deonične i više-deonične Mnemonic fraze na Trezoru
---
![cover](assets/cover.webp)



*Image credit: [Trezor.io](https://trezor.io/)*



## Nove opcije bekapa na Trezoru



Od 2023. godine, Trezor nudi novi format bekapa pod nazivom ***Single-share Backup***, koji postepeno zamenjuje klasični pristup zasnovan na BIP39 koji se nalazi na većini portfolija. Za razliku od tradicionalnih Mnemonic fraza od 12 ili 24 reči, ovaj novi format se zasniva na jednoj frazi od 20 reči izvedenoj iz standarda koji je razvio SatoshiLabs: **SLIP39**. Cilj je poboljšanje robusnosti i čitljivosti bekapa, uz omogućavanje glatke migracije ka modelu distribuiranog bekapa.



Ovaj distribuirani model se zove ***Multi-share Backup***. Zasniva se na istom principu, ali umesto generisanja jedne Mnemonic fraze, deli je na nekoliko fragmenata nazvanih ***shares***, od kojih je svaki Mnemonic fraza za sebe. Da bi se obnovio portfolio, određen broj ovih *shares* (definisan *threshold*-om) mora biti ponovo spojen. Na primer, u 3-od-5 šemi, bilo koje 3 *shares* od 5 će obnoviti portfolio. Imajte na umu da je Trezorov distribuirani sistem bekapa drugačiji od Multisig novčanika. Da biste potrošili svoje bitkoine, potreban vam je samo vaš Hardware Wallet Trezor. Potrebna je samo jedna potpis. Distribucija se primenjuje samo na nivou Mnemonic fraze, tj. bekapa.



![Image](assets/fr/01.webp)



Ovaj sistem rešava problem jedne tačke otkaza Mnemonic fraze bez nedostataka povezanih sa upravljanjem Multisig ili passphrase BIP39. Proces oporavka više se ne zasniva na jednom delu informacija, već na nekoliko, sa dodatnom prednošću tolerancije gubitka zahvaljujući pragu.



Korisnici koji su kreirali portfolio sa *Single-share Backup* mogu preći na *Multi-share Backup* u bilo kom trenutku bez potrebe za migracijom svog portfolija. Adrese za primanje i nalozi će ostati identični. Sistem *Multi-share* utiče samo na rezervnu kopiju, dok ostatak portfolija ostaje nepromenjen.



Multi-share Backup* je dostupan na Trezor Model T, Safe 3 i Safe 5. Ova funkcija nije podržana od strane Trezor Model One.



**Važna napomena:** Trezorov *Multi-share* sistem je kriptografski siguran, jer koristi *Shamir's Secret Sharing* šemu za distribuciju. Snažno savetujemo da ne primenjujete sličan sistem ručno, tako što ćete sami podeliti klasičnu Mnemonic frazu. To je loša praksa koja značajno povećava rizik od krađe i gubitka vaših bitkoina, stoga to nemojte raditi. Klasična Mnemonic fraza se čuva u celosti.



## Shamirovo deljenje tajni u SLIP39



Kriptografski mehanizam koji je osnova *Multi-share* rezervnih kopija na Trezoru je *Shamir's Secret Sharing Scheme* (SSSS). Njegov princip je sledeći: tajna informacija (u ovom slučaju, seed portfolija) se transformiše u matematički polinom. Zatim se izračunava nekoliko tačaka ovog polinoma, od kojih svaka postaje deonica. Originalna tajna se rekonstruiše interpolacijom polinoma, prikupljanjem minimalnog broja tačaka (prag).



Nijedna tajna informacija ne može se zaključiti iz broja deonica ispod praga, što garantuje savršenu teorijsku sigurnost tajne informacije. Drugim rečima, čak ni napadač sa neograničenom računalnom snagom ne može pogoditi seed ako prag nije dostignut.



SLIP39 koristi ovu šemu za distribuciju seed portfolija. Svaki deo je rečenica od 20 reči, sastavljena sa liste od 1024 reči (različite od BIP39 liste).



## Postavljanje Multi-share Backup-a na Trezor



Kada kreirate svoj portfolio na Trezoru, imate tri različite opcije:




- Koristite klasičnu BIP39 Mnemonic frazu od 12 ili 24 reči;
- Koristite Mnemonic frazu sa jednim deljenjem (SLIP39);
- Konfigurišite više Mnemonic fraza u Multi-share (SLIP39).



Ako se odlučite za SLIP39 Mnemonic frazu sa jednim deljenjem, moći ćete da unapredite na Multi-share kasnije bez potrebe za resetovanjem portfolija. S druge strane, ako započnete sa klasičnim BIP39 portfoliom (fraza od 12 ili 24 reči), nećete moći direktno da ga konvertujete u Multi-share. Moraćete da kreirate novi Multi-share portfolio od nule i prenesete svoja sredstva sa starog portfolija na novi putem jedne ili više Bitcoin transakcija. Ovo je složenija i skuplja operacija. Ako želite da izvršite ovu migraciju, preporučujem da kupite novi Hardware Wallet Trezor kako biste izbegli unos vašeg seed na softveru za portfolio.



U ovom vodiču ćemo prvo pogledati kako postaviti Multi-share prilikom kreiranja portfolija, a zatim ćemo u narednom delu videti kako konvertovati Single-share u Multi-share na postojećem portfoliju.



Ako vam je potrebna pomoć pri početnom podešavanju vašeg uređaja, imamo detaljan vodič za svaki Trezor model:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Na novom portfoliju



Sada ste završili početnu konfiguraciju vašeg Trezora i spremni ste da kreirate portfolio. U Trezor Suite, kliknite na dugme "*Create new Wallet*".



![Image](assets/fr/02.webp)



Izaberite opciju "*Multi-share Backup*", zatim kliknite na "*Create Wallet*".



![Image](assets/fr/03.webp)



Prihvatite uslove korišćenja na vašem Trezoru i potvrdite kreiranje portfolija.



![Image](assets/fr/04.webp)



U Trezor Suite, kliknite na "*Continue to backup*".



![Image](assets/fr/05.webp)



Pročitajte uputstva pažljivo, potvrdite ih, zatim kliknite na "*Create Wallet backup*".



![Image](assets/fr/06.webp)



Za više informacija o pravilnom načinu čuvanja i upravljanja vašim Mnemonic frazama, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Na Trezoru, izaberite ukupan broj deonica koje želite da konfigurišete. Najčešće konfiguracije su 2-od-3 i 3-od-5. Za ovaj primer, kreiraću 2-od-3, tako da ću izabrati 3 deonice. Svaka deonica će predstavljati Mnemonic frazu od 20 reči.



*Za korisnike Safe 5, iako će ekran prikazati "*Tap to continue*", zapravo ćete morati prevući nagore da biste potvrdili



![Image](assets/fr/07.webp)



Zatim potvrdite prag, tj. broj akcija potrebnih za ponovno sticanje pristupa Wallet i bitkoinima koje sadrži.



![Image](assets/fr/08.webp)



Trezor će kreirati vaše različite delove (Mnemonic fraze) koristeći svoj generator slučajnih brojeva. Uverite se da vas niko ne posmatra tokom ove operacije. Zapišite reči prikazane na ekranu na fizički medij po vašem izboru. Važno je da reči budu numerisane i u sekvencijalnom redosledu.



Preporučujem da zabeležite svaki deo na posebnom medijumu i pažljivo upravljate njihovim skladištenjem kako biste izbegli da nekoliko njih bude dostupno na istom mestu. Na primer, za konfiguraciju 2-od-3 kao što je moja, jedna opcija bi bila da jedan deo držite kod kuće, drugi kod poverljivog prijatelja, a poslednji u sefu banke. Izbor lokacija za skladištenje zavisiće od vaše lične strategije bezbednosti.



Na vrhu ekrana možete videti koju akciju trenutno gledate.



naravno, nikada ne smete deliti ove reči na Internetu, kao što to radim u ovom vodiču. Ovaj primer Wallet će biti korišćen samo na Testnet i biće obrisan na kraju vodiča.**_



![Image](assets/fr/09.webp)



Da biste prešli na sledeće reči, kliknite na dno ekrana. Možete se vratiti unazad klizanjem nadole. Kada zapišete sve reči, držite prst na ekranu da biste prešli na sledeći deo i ponovite operaciju.



![Image](assets/fr/10.webp)



Na kraju svakog snimanja deonice, od vas će se tražiti da izaberete reči u vašoj Mnemonic frazi kako biste potvrdili da ste ih ispravno zapisali.



![Image](assets/fr/11.webp)



I to je to, uspešno ste napravili rezervnu kopiju svog portfolija koristeći opciju Multi-share. Sada možete nastaviti sa ostatkom uputstava za konfiguraciju.



### Na postojećem portfoliju sa jednom akcijom



Ako već imate Trezor Wallet sa rezervnom kopijom sa jednim delom (SLIP39 Mnemonic fraza, ne klasična BIP39 fraza), i želite da poboljšate dostupnost i sigurnost vaše Wallet rezervne kopije, možete postaviti sistem sa više delova bez potrebe za prenosom vaših bitkoina.



Da biste to uradili, povežite i otključajte svoj Hardware Wallet. U Trezor Suite idite na Podešavanja.



![Image](assets/fr/12.webp)



Idite na karticu "*Device*".



![Image](assets/fr/13.webp)



Zatim kliknite na "*Create Multi-share Backup*".



![Image](assets/fr/14.webp)



Pročitajte uputstva, zatim kliknite na "*Create Multi-share Backup*".



![Image](assets/fr/15.webp)



Zatim ćete morati uneti vašu trenutnu Mnemonic frazu (jedan deo) na vašem Trezor ekranu. Izaberite broj reči (podrazumevano je 20).



![Image](assets/fr/16.webp)



Zatim koristite Trezorovu tastaturu na ekranu da unesete svaku reč vaše trenutne Mnemonic fraze.



![Image](assets/fr/17.webp)



Zatim možete odabrati konfiguraciju vašeg Multi-share Backup-a prateći uputstva navedena u prethodnom odeljku.



![Image](assets/fr/18.webp)



Kada kreirate svoj Multi-share Backup, moraćete da odlučite šta da uradite sa vašom originalnom Single-share Mnemonic frazom. Kako Bitcoin portfolio ostaje isti, ova pojedinačna fraza će uvek omogućiti pristup njemu. Ovo će zavisiti od vaše sigurnosne strategije, ali generalno, preporučljivo je uništiti ovu frazu kako biste eliminisali ovu jedinstvenu tačku kvara, što je upravo cilj Multi-share Backup-a. Ako odlučite da je uništite, pobrinite se da to uradite na siguran način, jer **ona i dalje omogućava pristup vašim bitcoinima**.



Čestitamo, sada ste upoznati sa korišćenjem Single-share i Multi-share rezervnih kopija na Trezor hardverskim novčanicima. Ako želite da unapredite svoju Wallet sigurnost, pogledajte ovaj vodič o BIP39 lozinkama:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Ako ste našli ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!



## Dodatni resursi





- [SLIP-0039: Shamir's Secret-Sharing za Mnemonic Kodove](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup on Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamir-ovo deljenje tajni](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).