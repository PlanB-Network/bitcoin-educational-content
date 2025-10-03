---
name: Threema
description: Sigurno, anonimno dopisivanje u realnom vremenu
---
![cover](assets/cover.webp)



Osnovan 2012. godine u Švajcarskoj, Threema je aplikacija za instant poruke dizajnirana da garantuje privatnost i sigurnost. Za razliku od WhatsApp-a, Telegram-a ili Signal-a, Threema ne zahteva broj telefona ili e-mail adresu za kreiranje naloga. Svaki korisnik ima jedinstveni identifikator, omogućavajući potpuno anonimnu registraciju.



Sa tehničke strane, komunikacije preko Threema su end-to-end šifrovane. Kod mobilne aplikacije je otvorenog koda od 2020. godine, ali serverska infrastruktura ostaje vlasnička i centralizovana. Serveri su hostovani isključivo u Švajcarskoj (zemlji poznatoj po svom pravnom okviru za zaštitu podataka).



![Image](assets/fr/01.webp)



Threema ima osnovne klijente za Android i iOS. Postoji i veb aplikacija, kao i softver dostupan za Windows, Linux i macOS. Međutim, da biste ih koristili, prvo se morate registrovati na mobilnom uređaju.



Aplikacija Threema nije besplatna. Radi po modelu jednokratne kupovine: 5,99 € za korišćenje aplikacije doživotno (ili 4,99 € ako je kupite direktno). Da biste zaista koristili Threema anonimno, plaćanje takođe mora biti anonimno. Zato možete kupiti aktivacioni ključ u bitkoinima ili gotovini na "*Threema Shop*" kako biste aktivirali Android verziju. Na iOS-u, s druge strane, kupovina mora proći kroz App Store, zbog Apple-ovih ograničenja na monetizaciju aplikacija.



Postoji i posebna poslovna verzija pod nazivom "*Threema Work*". U ovom vodiču, fokusiraćemo se na kućnu verziju.



| Aplikacija          | E2EE 1:1       | E2EE grupe   | Anonimna prijava | Licenca otvorenog koda klijenta | Licenca otvorenog koda servera | Decentralizovan server | Godina kreiranja |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opciono) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (opciono) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| **Threema**          | **✅**              | **✅**              | **✅**                   | **✅**                          | **❌**                           | **❌**                    | **2012**              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (federativni)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (preko emaila)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (federativni)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅          | ✅          | ✅               | ✅                      | ❌                       |🟡(nema direktorijuma)                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |


*E2EE = Šifrovanje od kraja do kraja*



## Instalirajte Threema aplikaciju



Threema je dostupna na svim platformama. Aplikaciju možete preuzeti direktno iz prodavnice aplikacija na vašem telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



Na Androidu je takođe moguće [instalirati putem APK-a](https://shop.threema.ch/en/download).



Postoje i [računarske verzije](https://threema.ch/download) (MacOS, Linux i Windows). Ovaj vodič će vam pokazati kako da ih sinhronizujete.



## Kupi Threema licencu



Jednom kada instalirate aplikaciju, ako ste išli direktno preko prodavnice aplikacija, već ste platili licencu i trebali biste imati trenutni pristup. Ako ste išli preko F-Droid ili APK-a, sada morate kupiti licencu na zvaničnom sajtu.



[Idite na "*Threema Shop*"](https://shop.threema.ch/) i kliknite na dugme "*Buy Threema for Android*".



![Image](assets/fr/02.webp)



Odaberite broj licenci koje želite da kupite (samo jednu ako je samo za vas), izaberite valutu i odaberite način isporuke licence. Možete izabrati da primite licencu putem e-pošte ili direktno na sajtu ako želite da ostanete anonimni. Zatim kliknite na "*Proceed to payment (prevod: Nastavi na plaćanje)*".



![Image](assets/fr/03.webp)



Izaberite svoj način plaćanja. U mom slučaju, platiću u bitkoinima, što vam takođe preporučujem, jer vam omogućava da ostanete anonimni (pod uslovom da pravilno koristite Bitcoin) i mnogo je pogodnije od plaćanja gotovinom na daljinu. Zatim kliknite na "*Next*".



![Image](assets/fr/04.webp)



Ako vam nije potrebna faktura, kliknite na "*Next*" ponovo bez unosa bilo kakvih ličnih podataka.



Zatim potvrdite kupovinu klikom na "*Confirm payment (Potvrdi plaćanje)*".



![Image](assets/fr/05.webp)



Zatim ćete morati poslati naznačeni iznos na datu Bitcoin adresu (nažalost, Lightning još nije podržan). Kada transakcija bude potvrđena na Blockchain-u, kliknite na "*Close*" pored fakture.



Zatim ćete imati pristup svom licencnom ključu. Napomena: ako niste uneli e-mail, ovaj ključ će biti prikazan samo ovde. Zapamtite da sačuvate URL stranice kako biste joj kasnije mogli pristupiti ako bude potrebno.



![Image](assets/fr/06.webp)



## Kreiraj nalog na Threema



Sada kada imate svoj licencni ključ, konačno možete pokrenuti aplikaciju. Prilikom prvog pokretanja, ako niste kupili Threema putem prodavnice aplikacija, bićete zamoljeni da unesete svoj licencni ključ, kupljen na sajtu.



![Image](assets/fr/07.webp)



Zatim kliknite na dugme "*Set up now*".



![Image](assets/fr/08.webp)



Pomerajte prst po ekranu kako biste generisali izvor entropije, neophodan za kreiranje vašeg "*Threema ID-a*".



![Image](assets/fr/09.webp)



Vaš "*Threema ID*" će tada biti prikazan. Omogućiće vam da kontaktirate druge korisnike. Kliknite na "*Next*".



![Image](assets/fr/10.webp)



Izaberite lozinku. Omogućiće vam da povratite pristup svom nalogu ukoliko se ukaže potreba. Neka vaša lozinka bude što duža i nasumična, i sačuvajte njenu sigurnu kopiju, na primer u menadžeru lozinki.



![Image](assets/fr/11.webp)



Zatim izaberite korisničko ime, koje može biti vaše pravo ime ili pseudonim.



![Image](assets/fr/12.webp)



Zatim možete povezati svoj Threema ID sa svojim brojem telefona. Ovo vam olakšava pretragu kroz kontakte, ali ako koristite Threema, to je takođe da biste sačuvali svoju anonimnost: stoga je najbolje da ga ne povezujete. Kliknite na "*Next*".



![Image](assets/fr/13.webp)



Kada završite ovaj korak, kliknite na "*Finish*".



![Image](assets/fr/14.webp)



Sada ste povezani sa Threema i možete početi komunicirati.



![Image](assets/fr/15.webp)



## Postavite Threema



Prvo pristupite podešavanjima klikom na tri male tačke u gornjem desnom uglu, zatim izaberite "*Settings*".



![Image](assets/fr/16.webp)



Na kartici "*Privacy*", pronaći ćete nekoliko opcija koje možete prilagoditi svojim potrebama:




- Sinhronizacija kontakata na vašem telefonu ;
- Prihvatanje poruka od nepoznatih osoba;
- Indikator pisanja tokom unosa podataka ;
- Obaveštenje o prijemu poruka..



![Image](assets/fr/17.webp)



Na kartici "*Security*", preporučujem aktiviranje opcije "*Locking mechanism*" kako biste zaštitili pristup aplikaciji. Takođe je preporučljivo aktivirati passphrase kako biste osigurali svoje lokalne rezervne kopije.



![Image](assets/fr/18.webp)



Slobodno istražite ostale delove podešavanja kako biste prilagodili aplikaciju svojim preferencijama.



![Image](assets/fr/19.webp)



## Pravljenje rezervne kopije vašeg Threema naloga



Pre nego što počnete da razmenjujete poruke, važno je da isplanirate način oporavka svog naloga, posebno ako promenite ili izgubite telefon. Da biste to uradili, kliknite na tri tačke u gornjem desnom uglu interfesja, zatim pristupite meniju "*Backups*".



![Image](assets/fr/20.webp)



Ovde ćete pronaći dve opcije za pravljenje rezervne kopije vaših podataka:




- "*Threema Safe*";
- "*Bekap Podataka*".



"*Threema Safe*" čuva sve informacije o vašem nalogu, osim vaših razgovora, na Threema serverima. Ovi podaci su šifrovani lozinkom koju ste odabrali prilikom kreiranja naloga, osiguravajući da Threema nema pristup njima. Bekapi se prave automatski i redovno.



Sa "*Threema Safe*", da biste povratili svoj nalog na novom uređaju, sve što treba da uradite je da unesete svoj "*Threema ID*" i svoju lozinku. Ako bilo koja od ove dve informacije nedostaje, biće nemoguće obnoviti vaš nalog.



Ova opcija vam omogućava samo da preuzmete svoj ID, profil, kontakte, grupe i određena podešavanja, ali **ne i istoriju razgovora**.



Da biste aktivirali "*Threema Safe*", jednostavno označite opciju u meniju "*Backups*".



![Image](assets/fr/21.webp)



Ako takođe želite da napravite rezervnu kopiju i vratite istoriju razgovora, moraćete da koristite opciju "*Data Backup*". Ovo generiše punu rezervnu kopiju vašeg naloga, koja se čuva lokalno na vašem telefonu. Moraćete da prenesete ovu rezervnu kopiju na vaš novi uređaj i koristite vašu lozinku (i moguće vaš passphrase) da biste vratili ceo nalog.



Pošto je ova rezervna kopija samo lokalna, potrebno je redovno kopirati je na eksterni medij. U suprotnom, ako vaš uređaj bude izgubljen, oporavak će biti nemoguć. Ova metoda je stoga najprikladnija za planirani prenos sa jednog uređaja na drugi, a ne za hitne situacije.



Imajte na umu: "*Data Backup*" funkcioniše samo ako koristite isti operativni sistem. Nećete ga moći koristiti, na primer, za migraciju sa Samsunga na iPhone.



## Prilagodite svoj Threema profil



U gornjem levom uglu interfejsa, kliknite na svoju profilnu sliku, a zatim izaberite "*My Profile*".



![Image](assets/fr/22.webp)



Ovde možete prilagoditi svoj profil: dodajte fotografiju, izaberite ko može da je vidi ili pogledajte svoje Threema prijavljivanje.



![Image](assets/fr/23.webp)



## Sinhronizujte softver sa PC-ijem



Ako želite da pristupite svojim razgovorima na računaru, možete da sinhronizujete svoj Threema nalog sa namenskim softverom. Preuzmite softver za vaš operativni sistem [sa zvanične veb stranice](https://threema.ch/en/download).



![Image](assets/fr/24.webp)



Na vašem telefonu kliknite na tri tačke u gornjem desnom uglu, zatim otvorite meni "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Kliknite na "*Add device*", zatim koristite svoj telefon da skenirate QR kod prikazan od strane softvera na vašem računaru.



![Image](assets/fr/26.webp)



Da biste potvrdili sinhronizaciju, kliknite na grupu emotikona prikazanu u softveru.



![Image](assets/fr/27.webp)



Na vašem računaru, prijavite se koristeći vašu lozinku.



![Image](assets/fr/28.webp)



Pored mobilne aplikacije, sada možete pristupiti svom Threema nalogu direktno sa računara.



![Image](assets/fr/29.webp)



## Slanje poruka putem Threema



Sada kada je sve ispravno postavljeno, možete početi sa komunikacijom. Kliknite na dugme "*Start chat*".



![Image](assets/fr/30.webp)



Izaberite "*New contact*".



![Image](assets/fr/31.webp)



Unesite ili skenirajte "*Threema ID*" vašeg dopisnika.



![Image](assets/fr/32.webp)



Kliknite na ikonu poruke.



![Image](assets/fr/33.webp)



Pošalji prvu poruku svom dopisniku.



![Image](assets/fr/34.webp)



Kada vaš dopisnik odgovori, veza će biti uspostavljena i moći ćete da vidite njegovo ili njeno ime i profilnu fotografiju. Zatim možete razmenjivati poruke, multimedijalne datoteke, pa čak i obavljati pozive.



![Image](assets/fr/35.webp)



Čestitamo, sada ste u toku sa korišćenjem Threema poruka, odlične alternative za WathsApp! Ako ste smatrali da je ovaj vodič koristan, bio bih veoma zahvalan ako biste kliknuli na zeleni palac ispod. Slobodno podelite ovaj vodič na vašim društvenim mrežama. Hvala vam puno!



Takođe preporučujem ovaj drugi vodič, u kojem vas upoznajem sa Proton Mail-om, mnogo privatnijom alternativom Gmail-u:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
