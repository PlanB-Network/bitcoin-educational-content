---
name: Wallet od Satoshi
description: Najjednostavniji skrbnički Wallet za početak
---
![cover](assets/cover.webp)

_Ovaj vodič je napisao_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Preuzimanje, Postavljanje i Korišćenje Wallet od Satoshi


Wallet od Satoshi je Lightning Network Wallet, čuvarski, i veoma jednostavan za korišćenje.

Za potrebe kursa [BTC105 - Finding Now](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5), koriste se Redeem Lightning Network vaučeri.


**Uvek zapamti**: _nemaš ključeve, nemaš novčiće_


Skrbnički novčanici ne omogućavaju korisnicima potpunu kontrolu nad njihovim sredstvima. Obično se ne preporučuju, osim za početnike. WoS bi trebalo koristiti kao prelazni Wallet ili za držanje džeparca, a ne za dugoročno akumuliranje sredstava.


---

Wallet of Satoshi (WoS) je kustodijalni proizvod, ali ima određenu reputaciju. Razumno je da se obratimo alatu kao što je WoS, na primer, da bismo povećali našu sposobnost primanja likvidnosti. Privremeno delegiramo WoS-u "prljav posao" upravljanja likvidnošću kanala za nas. Kada se dostigne određeni iznos, ispraznićemo WoS On-Chain na naš nekustodijalni Wallet.


**UPOZORENJE⚠️: Preporučuje se da pročitate ceo vodič pre nego što nastavite**


### Preuzimanje Wallet od Satoshi


Idite na Play Store i preuzmite WoS


![image](assets/it/01.webp)


**Napomena:** WoS se preuzima samo iz zvaničnih prodavnica. Ako je operativni sistem uređaja programiran, pre otvaranja WoS-a postoji deo za verifikaciju od strane samog OS-a. Nakon faze verifikacije, izaberite _Otvori_.


![image](assets/it/02.webp)


Wallet od Satoshi otvara se sa sledećim ekranom, i potrebno je kliknuti na _Start_


![image](assets/it/03.webp)


### Registracija naloga za WoS


U ovom trenutku, Wallet je već operativan, ali radi veće sigurnosti, nastavljamo sa postavljanjem prijave: biće potrebna za povrat sredstava u slučaju kvara uređaja ili gubitka. Stoga, izaberite meni u gornjem levom uglu.


![image](assets/it/04.webp)


Ceo prozor menija se otvara, u kojem morate isključivo postaviti valutu (Wallet ili Satoshi po defaultu prikazuje američki dolar kao referentnu valutu) i boju teme (svetla/tamna), prema ukusu. Ne koristite druge komande.


Pošto je WoS alat za čuvanje, ne možemo napraviti rezervnu kopiju Wallet pomoću Mnemonic fraze, ali možemo omogućiti WoS-u da povrati naša sredstva, u slučaju gubitka ili nekorišćenja mobilnog uređaja, klikom na _Login/Register_

Pojavljuje se prozor koji nas pita da unesemo email Address. Može biti **Proton mail** (preporučeno), ali mora biti funkcionalan, jer će nam omogućiti da povratimo sredstva u Wallet u slučaju gubitka/kradje ili oštećenja mobilnog telefona.


![image](assets/it/08.webp)


Wallet od Satoshi je poslao poruku na navedeni email inbox.


![image](assets/it/09.webp)


U poštanskom sandučetu ćemo pronaći dve reči, koje treba da unesemo, prepisujući ih, u prostor koji je obezbedila aplikacija.


- ne aktivirajte prevodioca: reči su na engleskom i moraju ostati na engleskom**
- ponovo napiši


![image](assets/it/10.webp)


Nakon prepisivanja dve reči, kliknite _OK_.


![image](assets/it/11.webp)


Rezultat bi trebalo da bude slika koja se pojavljuje na vrhu, sa simbolom kvačice za verifikaciju.


![image](assets/it/12.webp)


dok je u odeljku sa podešavanjima, crvena traka _Prijava/Registracija_ sada prikazuje korisnikov email Address.


![image](assets/it/13.webp)


### Primanje uplata


Da biste primili na WoS, kliknite _Receive_ i pojaviće se niz komandi.


![image](assets/it/14.webp)


Možete primiti


- via LN-Address **a**
- putem LN, podešavanjem Invoice **b**
- on chain (WoS podržava Bitcoin mrežu, ali uz plaćene zamene podmornica) **c**
- skeniranjem QR koda LNurl-p **d**


![image](assets/it/15.webp)


### Kreiranje Invoice


Kliknite na _Receive_ i izaberite komandu sa simbolom Lightning Network.


![image](assets/it/16.webp)


Meni za kreiranje Invoice se pojavljuje, gde kliknemo na _Dodaj iznos_ da bismo uneli tačan iznos i dodali opis, u ovom primeru, «Moj prvi Invoice».


![image](assets/it/17.webp)


Sa tastaturom postavljamo iznos.


![image](assets/it/18.webp)


da zatim dobijete isplatu Invoice. Primljena uplata izgleda ovako:


![image](assets/it/19.webp)


### Sakupljanje sa POS-a


Wallet od Satoshi ima podrazumevanu funkciju, koja ga čini posebno pogodnim za trgovce: POS. Hajde da vidimo kako da je aktiviramo.


Sa glavnog ekrana, izaberite meni u gornjem desnom uglu.


![image](assets/it/20.webp)


Zatim izaberite _Point of Sale_.


![image](assets/it/21.webp)


Sa najnovijim izdanjem WoS-a, obavezno izaberite _Keypad_.


![image](assets/it/22.webp)

i zatim unesite iznos na tastaturi, u primeru koji sledi jednak 10 centi / 118 Sats. Dodajte opis za kolekciju, u ovom slučaju "moj drugi sa POS". Veliko dugme Green se osvetli, i treba ga kliknuti.

![image](assets/it/23.webp)


do generate Invoice i pokaži ga - na primer - kupcu.


![image](assets/it/24.webp)


Ova uplata je takođe prikupljena!


![image](assets/it/25.webp)


### Slanje uplata


Jednostavnost je snaga glavnog ekrana WoS-a. Da biste platili Invoice, kliknite na _Send_


![image](assets/it/26.webp)


Prilikom prve upotrebe, WoS traži dozvolu za pristup kameri


![image](assets/it/27.webp)


Od ovog trenutka kamera se aktivira


![image](assets/it/28.webp)


Uokvirujući Invoice, vidimo da je zatraženo plaćanje od 210 Sats. Takođe se čita opis, ako ga je podnosilac zahteva postavio. Ovaj ekran je rezime i takođe zahtev za potvrdom: WoS "traži autorizaciju" za slanje plaćanja, koja se odobrava klikom na Green dugme _Pošalji_


![image](assets/it/29.webp)


Kada uplata stigne na odredište, WoS obaveštava ovim ekranom


![image](assets/it/30.webp)


Sa glavnog ekrana, klikom na _History_ (odmah ispod stanja) pojavljuje se lista transakcija


![image](assets/it/31.webp)


#### Oporavak WoS naloga


Sada ćemo videti kako instalirati WoS na novi uređaj; ovo će takođe biti korisno u slučajevima krađe, gubitka ili nemogućnosti korišćenja mobilnog telefona na kojem je Wallet prethodno bio instaliran. Nakon ponovne instalacije, morate ponovo izvršiti postupak registracije naloga koji je upravo objašnjen, sa jednom varijantom: na kraju zahteva za prijavu sa prethodno postavljenim email-om, WoS će se pojaviti ovako:


![image](assets/it/33.webp)


Poruka nas upozorava da je poslat email sa procedurom za ponovnu aktivaciju naloga. Morate otvoriti svoj email inbox.


**VAŽNO**: otvorite email sa računara ili, u svakom slučaju, sa uređaja koji je različit od onog na kojem planirate da povratite WoS nalog. U prijemnom sandučetu pronađite poruku koja vam prikazuje QR kod za skeniranje.


![image](assets/it/34.webp)


Kada je QR kod uokviren, na glavnoj stranici WoS-a će se pojaviti oporavljeni nalog, sa stanjem i istorijom.