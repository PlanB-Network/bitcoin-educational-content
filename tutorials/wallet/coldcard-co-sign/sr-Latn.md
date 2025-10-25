---
name: COLDCARD - Su-potpisivanje
description: Otkrijte funkciju Co-Sign i koristite je na vašem COLDCARD-u
---

![cover](assets/cover.webp)


*NB: Ovaj vodič je namenjen osobama koje već imaju određeno iskustvo sa multisignature novčanicima, Coinkite uređajima i softverom kao što su Sparrow wallet ili Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Zašto ColdCard Ko-Potpis?



Ova funkcija vam omogućava da dodate **uslove trošenja** na vaš ColdCard (Q ili Mk4) uređaj na način Hardverskog Sigurnosnog Modula (HSM), kako biste zaštitili svoja sredstva dok zadržavate značajnu fleksibilnost i kontrolu nad njima.



Uslovi trošenja mogu biti, na primer:





- Ograničenja na veličinu**: ograničite količinu bitkoina koju možete potrošiti u jednoj transakciji.
- Ograničenja brzine:** odlučite koliko transakcija možete obaviti po jedinici vremena (po satu, danu, nedelji, itd.), zahtevajući minimalan broj blokova između njih.
- Unapred odobrene adrese:** Dozvolite slanje bitkoina samo na unapred odobrene adrese.
- Dvofaktorska autentifikacija:** Zahteva potvrdu iz aplikacije za mobilne uređaje treće strane za 2FA (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) na pametnom telefonu/tabletu sa NFC-om i pristupom internetu.



**Kako funkcioniše



Dodavanjem drugog seed na vaš ColdCard Mk4 ili Q uređaj, nazvanog "Ključ politike trošenja", koji ćemo u ovom vodiču nazivati "C Ključ".


Pored ovog dodatnog seed, bićete zamoljeni da Supply bar još jedan dodatni ključ (XPUB), koji ćemo nazvati "Rezervni Ključ", kako biste kreirali Wallet Multisig 2-na-N.



Ukratko, napravićemo Wallet Multisig, a vaš ColdCard uređaj će sadržati 2 privatna ključa potrebna za trošenje sredstava, seed master uređaja i "Ključ politike trošenja".



Svaki put kada se zatraži potpisivanje "C Key", primeniće se navedeni uslovi potrošnje, i ColdCard će potpisati samo ako transakcija ispunjava te uslove.



Ako želite da se oslobodite ovih uslova trošenja, možete to učiniti:




- potpisivanjem jednim od rezervnih ključeva i seed rukom, ili 2 rezervna ključa u zavisnosti od veličine vašeg Multisig.
- unošenjem "Ključa politike trošenja" ili "C ključa" u meni "Zajedničko potpisivanje". **Ovaj drugi se ne može direktno konsultovati na uređaju, inače bi bilo ko mogao otkazati konfigurisane uslove trošenja.**




## Konfigurisanje ColdCard Ko-Potpisa



![video](https://youtu.be/MjMPDUWWegw)



### 1- Aktiviraj funkcionalnost



Prvo, uverite se da vaš uređaj ima barem najnoviju verziju firmvera:




- Mk4: v5.4.2
- P: v1.3.2P




Na vašem Mk4 ili ColdCardQ, idite na *Advanced Tools > ColdCard Co-Signing*.



![Co-Sign](assets/fr/01.webp)



*U sledećem vodiču, snimci ekrana će biti napravljeni na ColdCardQ radi praktičnosti, ali koraci i meniji su identični između Mk4 i Q.*



Prikazano je rezime funkcionalnosti.


Terminologija koja se koristi za označavanje ključeva, koju ćemo ponovo koristiti u 2-na-3 multi-potpisu Wallet koji ćemo kreirati, je:



Ključ A = Coldcard master seed


Ključ B = Rezervni ključ


Ključ C = Politika trošenja ključ



Kliknite **"ENTER "**.



![Co-Sign](assets/fr/02.webp)



Sledeći korak je odlučiti koji privatni ključ će delovati kao "Ključ politike trošenja" ili "Ključ C".



Možemo videti da imamo nekoliko opcija otvorenih za nas:





- Ili pritisnite **"ENTER "** da generate novu seed rečenicu od 12 reči.





- Ili kliknite na **"(1) "** da uvezete postojeći 12-rečni seed, ili izaberite **"(2) "** da uvezete postojeći 24-rečni seed.





- Ili pritisnite **„(6) “** da uvezete seed iz trezora vašeg uređaja.



Za potrebe ovog tutorijala, odlučili smo da uvezemo postojeći 12-reči seed pritiskom na **"(1) "**. Ovo može biti bilo koji seed BIP39 koji već posedujete i za koji očigledno imate rezervnu kopiju.



Koristite tastaturu da unesete 12 reči vašeg seed. Za ovaj primer, izabraćemo važeću frazu seed beef x 12. Zatim pritisnite **"ENTER "**.


*NB: ako nemate rezervnu kopiju ovog seed, više nećete moći da menjate postavke "Co-Sign" na svom uređaju, kako biste promenili uslove potrošnje*



Funkcija "Co-Sign" je sada aktivirana na uređaju. Zatim ćemo morati odabrati naše uslove potrošnje, a potom završiti kreiranje multi-potpis Wallet.



![Co-Sign](assets/fr/03.webp)



### 2- Izaberite uslove trošenja ili "*politike trošenja*"



Ovde navodimo uslove trošenja koji moraju biti ispunjeni kada **"C Key "** ili **"Spending Policy Key**" potpiše transakciju.



U meniju **"Co-Signing "** kliknite na **"Spending Policy**".



Zatim možete odabrati maksimalnu magnitudu, tj. maksimalan broj satoshija koji se mogu potrošiti u jednoj transakciji.



Za ovaj primer, izabraćemo maksimalnu magnitudu od **21212** satoshija. Kliknite na **"ENTER "** da potvrdite.




![Co-Sign](assets/fr/04.webp)



Zatim biramo da postavimo maksimalnu brzinu, tj. broj transakcija koje uređaj može potpisati po jedinici vremena. Za ovaj vodič, izabraćemo neograničenu brzinu, tj. bez ograničenja na broj transakcija.




![Co-Sign](assets/fr/05.webp)



### 3- Kreiraj Wallet Multisig 2-na-N



Još uvek treba da izaberemo treći ključ za naš Wallet Multisig, tj. **"Rezervni Ključ"** (Ključ B), pored uređaja **glavni seed** (Ključ A) i **"Ključ Politike Trošenja"** (Ključ C).



Naš "B Key" će morati biti uvezen ili putem SD kartice, ili putem QR koda u slučaju ColdCardQ.


Da bismo to uradili, biće nam potreban drugi ColdCard Mk4 ili Q uređaj, na kojem se koristi naš "Key B".



Na ovom drugom uređaju koji sadrži vaš **"Backup Key "**, recimo ColdCard Mk4 za ovaj primer, idite iz glavnog menija na **"Settings "**, zatim, **"Multisig Wallet"**, i na kraju **"Export Xpub "**.


(Ako je vaš drugi uređaj ColdCardQ, imaćete opciju da izvezete svoj Xpub putem QR koda, naravno).





![Co-Sign](assets/fr/06.webp)





Na sledećem ekranu, umetnite SD karticu i kliknite na dugme **"validate "** u donjem desnom uglu. Zatim kliknite na **"(1) "** da sačuvate fajl na SD kartici.



Datoteka će sadržati otisak javnog ključa (*fingerprint*) u svom nazivu i imaće oblik `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Zatim umetnite SD karticu u "initial" ColdCardQ da biste uvezli naš "Backup Key" (ključ B).


U meniju "ColdCard Co-Signing" izaberite "Build 2-of-N", zatim na sledećem ekranu kliknite **"ENTER "**, pa ponovo **"ENTER "** da uvezete "Backup Key" sa SD kartice.



![Co-Sign](assets/fr/08.webp)



Na sledećem ekranu ostavite "Account Number" prazno (osim ako tačno znate šta radite) i kliknite ponovo na **"ENTER "**.



![Co-Sign](assets/fr/09.webp)



Konačno smo spremni da koristimo naš novi Wallet Multisig 2-sur-3, sastavljen na sledeći način:



Ključ A= Coldcard Q master seed


Ključ B= Rezervni ključ (upravo uvezen sa drugog Coldcard uređaja)


Ključ C= Ključ politike trošenja (ako se koristi za potpisivanje, nameće unapred definisane uslove trošenja)



## Potpiši sa Sparrow wallet



Ako je potrebno, pogledajte tutorijale ispod da biste se upoznali sa softverom Sparrow wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.network/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Izvoz Wallet Multisig 2-sur-3 u Sparrow wallet



Sada moramo da izvezemo naš Wallet Multisig u Sparrow kako bismo mogli da postavimo naše prve satoshije tamo.



Sa glavnog menija vašeg ColdCardQ, izaberite **"Settings "**, zatim **"Multisig Wallets "**.


Skup Multisig novčanika poznatih vašem ColdCard-u je sada prikazan, sa brojem ključeva uključenih ovde "2/3" (2-sur3). Izaberite Multisig **"ColdCard Co-Sign "** koji smo upravo kreirali, zatim kliknite na **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Na kraju, izaberite metodu koja će vam omogućiti da izvezete Wallet na Sparrow. U našem slučaju, izabraćemo SD karticu, i zato kliknite na **"(1) "** nakon umetanja SD kartice u slot A uređaja.



![Co-Sign](assets/fr/11.webp)



Zatim u Sparrow wallet, izaberite "Import Wallet".



![Co-Sign](assets/fr/12.webp)



Zatim kliknite na **"Import File "**. Zatim izaberite fajl **"export-Coldcard_Co-sign.txt "** na vašoj SD kartici.



![Co-Sign](assets/fr/13.webp)



Dajte svom Wallet ime kako će se pojaviti u Sparrow, i izaberite lozinku za šifrovanje vašeg Wallet (ili ne).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Sada smo spremni da primimo naše prve satoshije i testiramo uslove potrošnje koje smo primenili na naš Wallet.



![Co-Sign](assets/fr/16.webp)



### 2- Testiranje unapred definisanih politika trošenja



Kao podsetnik, odlučili smo se za maksimalnu magnitudu od 21212 satoshija za naš Wallet Multisig. To je značilo da bi svaki put kada Ključ za Politiku Trošenja (Ključ C) potpiše transakciju, ona bila važeća samo ako je potrošeni iznos manji ili jednak 21212 satoshija.



Hajde da ga testiramo.


Prvo, kliknimo na karticu "Receive" u Sparrow i prebacimo nekoliko Sats na Wallet, koje ćemo koristiti tokom ovog tutorijala.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Onda pokušajmo potrošiti više od dozvoljenih 21212 satoshija simulacijom transakcije od 50,000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Nakon skeniranja QR koda koji predstavlja *nepotpisanu* transakciju sa našim ColdCardQ za uvoz transakcije, ovo je ono što nam se prikazuje na ekranu. Poruka upozorenja nam govori da uslovi potrošnje nisu ispunjeni. Ako ipak potpišemo transakciju, tada će samo jedan od 2 ključa (seed master na uređaju, ali ne i "Ključ C") potpisati.




![Co-Sign](assets/fr/23.webp)



Ovde, nakon uvoza naše transakcije u Sparrow, možemo videti da je samo jedan od potpisa primenjen na transakciju.



![Co-Sign](assets/fr/24.webp)




Sada hajde da ponovimo eksperiment, ali za transakciju od 21,000 satoshija, tj. manje od maksimalne magnitude (21212 Sats) koju smo postavili za ovaj Wallet.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Hajde da pokušamo potpisati ovu transakciju sa našim ColdCardQ.



Ovog puta nema problema, ne pojavljuje se poruka upozorenja, i kada uvezemo potpisanu transakciju u Sparrow wallet, ovog puta su primenjena 2 potpisa, čineći transakciju važećom i spremnom za distribuciju.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Ko-potpiši sa Nunchuk



https://planb.network/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA & Whitelisted adrese



U ovom pasusu, koristićemo naš Wallet Multisig Co-Sign sa Nunchukom, i iskoristićemo priliku da primenimo nove uslove potrošnje da vidimo kako ide.



Idite na *Avanced Tools > ColdCard Co-Signing*.


Od nas se traži da unesemo naš "Ključ politike trošenja", kako bismo pristupili meniju koji nam omogućava da promenimo uslove trošenja. U našem slučaju, unosimo 12 x "beef".



Odlučili smo da zadržimo magnitudu od 21212 Sats, i maksimalnu "Limit Brzinu" iz praktičnih razloga vezanih za ovaj tutorijal. S druge strane, koristićemo meni **"Whitelist Addresses "** da nametnemo adrese na koje se naša sredstva mogu trošiti.




![Co-Sign](assets/fr/31.webp)




Skenirajte QR kodove povezane sa adresama (izabraćemo 2) koje želite da dodate na vašu belu listu, zatim kliknite na **"ENTER "**. Nakon validacije vaših adresa pritiskom na **"ENTER "** sukcesivno, vidimo da su primenjena ograničenja na Magnitude i adrese korisnika.



![Co-Sign](assets/fr/32.webp)



Konačno, da bismo dobili potpunu sliku mogućnosti koje nudi "Co-Sign", hajde da aktiviramo opciju "Web 2FA".


Ova funkcija vam omogućava da koristite aplikaciju koja je u skladu sa TOTP RFC-6238, kao što su Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / ili Aegis Authenticator, kako biste dodali dodatni Layer nivo sigurnosti.



https://planb.network/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.network/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

U konkretnim terminima, pre nego što potpišete transakciju, potrebno je da prinesete svoj NFC-omogućen, internet-povezan uređaj blizu vašeg Coldcard-a. Ovo će vas automatski odvesti na coldcard.com veb stranicu, gde će vam biti zatraženo da unesete 6-cifreni kod za vašu aplikaciju. Ako unesete ispravan kod, veb stranica će vam prikazati ili QR kod za skeniranje za ColdCardQ, ili 8-cifreni kod koji treba da unesete na vaš Mk4, kako biste autorizovali vaš uređaj za potpisivanje.





![Co-Sign](assets/fr/33.webp)



Nakon skeniranja QR koda prikazanog u vašoj aplikaciji za dvostruku autentifikaciju i dodavanja vašeg ColdCard Co-Sign (CCC) naloga, od vas će biti zatraženo da potvrdite da je sve u redu unosom vašeg 2FA koda.



Ukucajte svoj ColdCard na zadnju stranu vašeg NFC uređaja.



![Co-Sign](assets/fr/34.webp)



Na veb stranici koja se otvori, unesite 2FA kod vaše omiljene aplikacije. Zatim skenirajte prikazani QR kod sa vašim ColdCardQ (ili unesite 8-cifreni kod prikazan na vašem Mk4).



![Co-Sign](assets/fr/35.webp)




Sada smo uveli ograničenje na magnitudu (21212 Sats), odredišne adrese i dvostruku autentifikaciju.



![Co-Sign](assets/fr/36.webp)



### 2- Izvoz Wallet Multisig 2-na-3 na Nunchuk



Hajde da izvezemo Wallet Multisig 2-na-3 u Nunchuk ovaj put, kao što smo ranije uradili sa Sparrow.


Idite na *Settings > Multisig Wallets > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Ovog puta izaberite opciju NFC za izvoz klikom na ColdcardQ dugme istog naziva **"NFC "**.



![Co-Sign](assets/fr/37.webp)



U Nunchuk-u, ako prvi put otvarate aplikaciju, kliknite na **"Recover existing Wallet"**.



![Co-Sign](assets/fr/38.webp)



Ako već imate Wallet u aplikaciji, kliknite na **"+"** u gornjem desnom uglu, zatim **"Recover existing Wallet"**.



![Co-Sign](assets/fr/39.webp)




Zatim izaberite **"Recover Wallet from COLDCARD "** zatim **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Na kraju, prislonite zadnji deo vašeg pametnog telefona na ekran vašeg ColdCardQ uređaja kako biste uvezli Wallet putem NFC-a.



![Co-Sign](assets/fr/41.webp)



Naš račun i satoshi prethodno deponovani putem Sparrow wallet su vraćeni.



![Co-Sign](assets/fr/42.webp)



### 3- Testiranje unapred definisanih politika trošenja



Hajde sada da pokušamo da izvršimo transakciju koja krši 2 uslova potrošnje koje smo postavili. **Pokušaćemo da potrošimo više od 21212 Sats na Address koji nije odobren.** Pokušajmo da pošaljemo 22 222 Sats na nasumični Address.



![Co-Sign](assets/fr/43.webp)



Kada je transakcija kreirana, kliknite na 3 male tačke u gornjem desnom uglu da biste je izvezli na vaš ColdCard.



![Co-Sign](assets/fr/44.webp)



Zatim izaberite **"Export via BBQR "** i skenirajte prikazani QR kod sa vašim ColdCardQ.



![Co-Sign](assets/fr/45.webp)



Vaš ColdcardQ zatim prikazuje upozorenje koje, kada skrolujete do dna ekrana, pojašnjava da transakcija krši uslove potrošnje, kao što se i očekivalo.



**Imajte na umu da uređaj ne govori koje su uslove potrošnje uključeni, kako bi se sprečio potencijalni napadač da pokuša zaobići ograničenja.**




![Co-Sign](assets/fr/46.webp)



Ako i dalje potvrđujete pritiskom na **"ENTER "**, pojavljuje se QR kod koji predstavlja potpisanu transakciju. Ako ga uvezete u Nunchuk, možete videti da je primenjen samo jedan potpis.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Hajde da izvedemo potpuno istu operaciju, ali ovaj put sa transakcijom koja poštuje ograničenje magnitude (21212 Sats), i troši satoshije na jednu od 2 adrese koje smo unapred konfigurisali.



Šaljemo Nunchuk 12121 Sats na jednu od naših 2 adrese. Zatim izvozimo transakciju na naš ColdCard kao što je ranije urađeno.



![Co-Sign](assets/fr/49.webp)




Nakon što uvezemo nepotpisanu transakciju u naš ColdCardQ, da vidimo šta nam je prikazano ovaj put.



Upozorenje je uvek prisutno, ali ovog puta, skrolujući do dna ekrana, vidimo da je reč o validaciji transakcije putem 2FA. Uređaj nas pita da prinesemo naš ColdcardQ blizu našeg NFC terminala povezanog na Internet (smartfon ili tablet), što i činimo.



![Co-Sign](assets/fr/50.webp)



Naš pametni telefon otvara veb stranicu koja traži da unesemo naš 2FA kod, što činimo zahvaljujući Proton Authenticator-u.



![Co-Sign](assets/fr/51.webp)





Zatim skenirajte QR kod koji se pojavljuje na veb stranici, da biste autorizovali vaš ColdCard da potpiše transakciju.


Transakcija je sada potpisana sa 2 ključa i stoga je važeća.



Ako je "Push Tx" omogućen na vašem ColdCardQ, možete emitovati transakciju direktno na mrežu jednostavnim dodirom na poleđini vašeg pametnog telefona.



![Co-Sign](assets/fr/52.webp)




Ako nemate aktiviran "Push tx", pritisnite dugme "QR" na vašem ColdCardQ da prikažete potpisanu transakciju kao QR kod, i uvezite je u Nunchuk, na isti način kao u prethodnom primeru.



![Co-Sign](assets/fr/53.webp)



Ovog puta primećujemo da su primenjena 2 potpisa, tako da je transakcija spremna za emitovanje na Bitcoin mreži.



![Co-Sign](assets/fr/54.webp)




Došli smo do kraja ovog vodiča, koji će vam dati pregled mogućnosti koje nudi Co-Sign funkcionalnost integrisana u Coinkite-ove ColdCardQ i Mk4 uređaje, kao i njeno korišćenje putem novčanika kao što su Sparrow i Nunchuk.