---
name: SimpleX Chat
description: Prvo poštansko sanduče bez korisničkog ID-a
---
![cover](assets/cover.webp)



Pokrenut 2021. godine, SimpleX je besplatna aplikacija za instant poruke sa radikalno drugačijim pristupom privatnosti. Za razliku od WhatsApp-a, Signala i drugih centralizovanih servisa za razmenu poruka, SimpleX se ističe po upravljanju korisnicima: nema korisničkih identifikatora, pseudonima, brojeva ili vidljivih javnih ključeva. Ovaj potpuni izostanak identifikatora čini gotovo nemogućim povezivanje korisnika, garantujući visok nivo privatnosti.



Za razliku od većine aplikacija koje zahtevaju nalog ili broj telefona, SimpleX vam omogućava da započnete razgovore deljenjem linka ili efemernog QR koda. Svaki link kreira jedinstveni enkriptovani kanal, a kontakti ne mogu pronaći ili ponovo kontaktirati pošiljaoca bez eksplicitnog Exchange. Poruke su enkriptovane od kraja do kraja i prolaze kroz relej servere koji ih brišu nakon slanja, i ne vide ni pošiljaoca ni primaoca, niti njihove ključeve.



![Image](assets/fr/01.webp)



Mreža je potpuno decentralizovana i nefederisana: serveri ne poznaju jedni druge, ne čuvaju globalni direktorijum i ne hostuju korisničke profile. Još bolje, svaki korisnik može postaviti i koristiti svoj sopstveni relejni server, dok ostaje interoperabilan sa onima na javnoj mreži.



SimpleX je potpuno otvorenog koda (klijenti, protokoli i serveri), dostupan na Androidu, iOS-u, Linuxu, Windowsu i macOS-u. Njegova lokalna memorija je šifrovana i prenosiva, tako da možete preneti profil sa jednog uređaja na drugi bez oslanjanja na centralizovani server.



SimpleX integriše sve klasične funkcije aplikacija za razmenu poruka. Međutim, njegova ergonomija ostaje manje fluidna u poređenju sa WhatsApp-om ili Signal-om. Takođe može biti restriktivniji za korišćenje, posebno prilikom dodavanja kontakata. Dakle, po mom mišljenju, to je relevantna alternativa za WhatsApp ili Signal za korisnike koji stavljaju poverljivost u srž svojih prioriteta i koji su spremni, iz tog razloga, da naprave nekoliko ustupaka u svakodnevnom korisničkom komforu.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| **SimpleX**          | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Šifrovanje od kraja do kraja*



## Instalirajte aplikaciju SimpleX Chat



SimpleX Chat je dostupan na svim platformama. Možete preuzeti aplikaciju direktno iz prodavnice aplikacija na vašem telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



Na Androidu je takođe moguće [instalirati putem APK](https://github.com/simplex-chat/simplex-chat/releases).



U ovom vodiču, fokusiraćemo se na mobilnu verziju, ali imajte na umu da su [desktop verzije takođe dostupne](https://simplex.chat/downloads/) (MacOS, Linux i Windows). Moguće je povezati desktop verziju sa postojećim korisničkim profilom na mobilnom uređaju, ali da bi ova sinhronizacija funkcionisala, oba uređaja moraju biti povezana na istu lokalnu mrežu.



![Image](assets/fr/02.webp)



## Kreiraj nalog na SimpleX Chat



Kada prvi put pokrenete aplikaciju, kliknite na dugme "*Create your profile*".



![Image](assets/fr/03.webp)



Izaberite korisničko ime, koje može biti vaše pravo ime ili pseudonim, zatim kliknite na "*Create*".



![Image](assets/fr/04.webp)



Zatim, postavite učestalost kojom će aplikacija proveravati nove poruke. Ako trajanje baterije vašeg telefona nije problem, izaberite "*Instant*" da biste primali poruke u realnom vremenu. Ako želite da uštedite bateriju i sprečite aplikaciju da radi u pozadini, izaberite "*Kada je aplikacija pokrenuta*": tada ćete primati poruke samo kada je aplikacija otvorena. Mogući kompromis je da se odlučite za periodičnu proveru svakih 10 minuta.



Jednom kada napravite svoj izbor, kliknite na "*Use chat*".



![Image](assets/fr/05.webp)



Sada ste povezani na SimpleX Chat i spremni za početak ćaskanja.



![Image](assets/fr/06.webp)



## Postavljanje SimpleX Chat-a



Prvo pristupite podešavanjima klikom na svoju profilnu fotografiju u donjem desnom uglu, zatim na "*Settings*".



![Image](assets/fr/07.webp)



Podrazumevana podešavanja su generalno pogodna za većinu korisnika. Međutim, preporučujem da odete na meni "*Database passphrase & export*". Ovde možete izvesti bazu podataka vašeg SimpleX naloga za potrebe bekapa.



Takođe možete modifikovati passphrase koji se koristi za šifrovanje ove baze podataka. Po defaultu, on se nasumično generiše i čuva lokalno na vašem uređaju. Ako želite, možete definisati svoj sopstveni passphrase i obrisati lokalnu passphrase rezervnu kopiju: tada ćete morati ručno unositi passphrase svaki put kada otvorite aplikaciju, kao i kada prelazite na drugi uređaj.



**Imajte na umu**: ako izaberete ovu opciju, gubitak passphrase će rezultirati trajnim gubitkom svih vaših SimpleX profila i poruka.



![Image](assets/fr/08.webp)



Takođe preporučujem da odete u meni "*Privatnost i bezbednost*", gde možete aktivirati opciju "*SimpleX Lock*". Ovo štiti pristup aplikaciji pomoću koda za zaključavanje.



![Image](assets/fr/09.webp)



Konačno, meniji "*Notifications*" i "*Appearance*" vam omogućavaju da prilagodite SimpleX Chat prema vašim preferencijama.



![Image](assets/fr/10.webp)



## Šaljite poruke pomoću SimpleX Chat



Da biste se povezali sa drugom osobom na SimpleX-u, imate dve opcije:




- Koristite jednokratni link;
- Koristite višekratni statički Address.



Statični Address omogućava svakome ko ga zna da vas kontaktira na SimpleX-u. To je postojani Address, koji može biti korišćen više puta, od strane različitih ljudi, bez vremenskog ograničenja. Upravo ta postojanost ga čini podložnijim spamu. Međutim, za razliku od drugih aplikacija za razmenu poruka, brisanje vašeg SimpleX Address je dovoljno da zaustavi sav spam, bez uticaja na postojeće razgovore. Zapravo, ovaj Address se koristi samo za uspostavljanje početne veze, i više nije potreban kada Exchange započne.



Linkovi za jednokratnu upotrebu, s druge strane, mogu se koristiti samo jednom, od strane bilo kog korisnika. Kada ga kontakt iskoristi, link postaje nevažeći. Moraćete da generate novi za svaku novu vezu.



### Sa statičkim Address



Ako želite da koristite Address, kliknite na svoju profilnu sliku u donjem levom uglu Interface, zatim izaberite "*Create SimpleX Address*". Zatim ponovo kliknite na "*Create SimpleX Address*".



![Image](assets/fr/11.webp)



Vaš višekratni Address je sada kreiran. Možete ga podeliti sa ljudima koji žele da stupe u kontakt sa vama, bilo prikazivanjem QR koda ili slanjem linka.



![Image](assets/fr/12.webp)



Kliknite na dugme "*Address settings*". Ovde možete konfigurisati dozvole povezane sa vašim Address. Opcija "*Share with contacts*" čini vaš Address vidljivim na vašem SimpleX profilu. Vaši kontakti će tada moći da ga pregledaju i proslede drugim osobama koje žele da vas kontaktiraju.



Opcija "*Auto-accept*" automatski prihvata dolazne veze putem vašeg Address. To znači da će svako ko ima vaš Address moći da vidi vaš profil i pošalje vam poruku, osim ako ne aktivirate opciju "*Accept incognito*". Ovo sakriva vaše ime i profilnu fotografiju kada se uspostavi nova veza, zamenjujući ih nasumičnim pseudonimom, različitim za svakog sagovornika.



![Image](assets/fr/13.webp)



### Sa ponovljivim linkom



Drugi način povezivanja sa osobom je kreiranje jednokratnog linka. Da biste to uradili, kliknite na ikonu olovke u donjem desnom uglu Interface, zatim izaberite "*Create 1-time link*".



Ako vam je kontakt poslao link, kliknite na "*Skeniraj / Zalepi link*" da biste ga skenirali ili zalepili.



![Image](assets/fr/14.webp)



SimpleX zatim generiše jednokratni link. Možete ga proslediti svom kontaktu na bilo koji način: fizički Exchange, druge poruke, itd.



![Image](assets/fr/15.webp)



Takođe možete izabrati koji profil želite da povežete sa ovim linkom za poziv. Da biste to uradili, kliknite na svoj profil odmah ispod QR koda. Zatim ćete moći da:




- izaberite jedan od vaših postojećih profila (videćemo kako da kreiramo nekoliko profila u sledećem odeljku);
- ili odaberite režim "*Incognito*", koji skriva vaše ime i profilnu fotografiju nasumično generisanim pseudonimom za vašeg sagovornika.



Ovde biram režim "*Incognito*".



![Image](assets/fr/16.webp)



Moj kontakt je koristio link. Sa svoje strane, nije aktivirao "*Incognito*" režim, zbog čega vidim njegovo profilno ime, "*Bob*". S druge strane, Bob ne vidi moje pravo ime "*Loïc Morel*", već nasumični pseudonim, u ovom slučaju "*RealSynergy*".



![Image](assets/fr/17.webp)



Mogao bih odmah početi razgovor, ali prvo bih želeo da proverim da li razgovaram sa Bobom, a ne sa nekom zlonamernom osobom koja je možda presrela vezu ili izvršila MITM napad.



Da bismo to uradili, proverićemo naš sigurnosni link **van aplikacije**. Ovo je važno, jer bi u slučaju MITM napada interna verifikacija bila kompromitovana. Zato koristite drugi siguran sistem za razmenu poruka, ili još bolje, proverite kodove lično.



U ćaskanju, klikni na Bobovu fotografiju, zatim na "*Verifikuj sigurnosni kod*". Bob treba da uradi isto sa svoje strane.



![Image](assets/fr/18.webp)



Ako radite na daljinu, uporedite kodove na drugom sigurnom sistemu za razmenu poruka (moraju biti identični). Ili još bolje, ako možete da se sretnete lično, skenirajte QR kod vašeg kontakta klikom na "*Skeniraj kod*".



![Image](assets/fr/19.webp)



Ako je verifikacija uspešna, ikonica štita sa oznakom za proveru će se pojaviti pored imena vašeg kontakta. Ovo je vaša garancija da razmenjujete sa Bobom. Ako verifikacija nije uspešna, pojaviće se upozorenje "*Pogrešan sigurnosni kod!*".



![Image](assets/fr/20.webp)



Sada možete slobodno Exchange poruke, pozive i datoteke sa Bobom, u zavisnosti od dozvola koje ste postavili za ovaj razgovor.



## Prilagodite svoje SimpleX Chat profile



Jedna od najmoćnijih karakteristika SimpleX-a je mogućnost upravljanja sa nekoliko potpuno odvojenih korisničkih profila, koji su svi dostupni sa istog lokalnog naloga. Ovo vam omogućava da uredno razdvojite svoje različite identitete, bez komplikovanja upravljanja porukama.



Na primer, možete kreirati :




- Profil sa vašim pravim imenom i pravom fotografijom za vaše profesionalne razmene;
- Profil sa tvojim pravim imenom i smešnom fotografijom za porodične razmene;
- Profil sa lažnom fotografijom i pseudonimom za vaše lične razgovore;
- Još jedan pseudonimni profil za ćaskanje sa strancima.



To ćemo ovde uraditi. Počinjem tako što konfigurišem svoj glavni profil, onaj povezan sa mojim pravim identitetom. Da bih to uradio, kliknem na svoju profilnu fotografiju u donjem desnom uglu, a zatim na svoje korisničko ime.



![Image](assets/fr/21.webp)



Zatim kliknem na svoju profilnu fotografiju da je promenim i dodam novu.



![Image](assets/fr/22.webp)



Da biste dodali druge profile, kliknite na meni "*Profili vaših ćaskanja*".



![Image](assets/fr/23.webp)



Ovde ćete videti sve vaše profile. Kliknite na "*Dodaj profil*" da kreirate novi.



![Image](assets/fr/24.webp)



Zatim izaberite informacije za svoj novi profil: ime, fotografiju, itd. Ovde koristim pseudonim i drugačiju sliku da sakrijem svoj pravi identitet u određenim razmenama.



![Image](assets/fr/25.webp)



Držanjem prsta na profilu možete ga sakriti. Ovo će ga učiniti nevidljivim u aplikaciji, zajedno sa svim povezanim razgovorima. Takođe možete odabrati opciju "*Utišaj*" da prestanete primati obaveštenja.



![Image](assets/fr/26.webp)



Jednom kada kreirate svoje profile, možete ih upravljati nezavisno. Sa početne stranice, jednostavno izaberite aktivni profil za prikaz.



![Image](assets/fr/27.webp)



Kada kreirate pozivni link ili statički Address, sada možete izabrati koji profil želite da povežete sa njim. Na primer, ako izaberem profil "*Satoshi Nakamoto*" da generate link i pošaljem ga Alisi, ona će videti samo moj pseudonimni identitet "*Satoshi Nakamoto*", bez ikakvog saznanja o mom pravom identitetu "*Loïc Morel*". Obrnuto, ako joj dam link sa mog pravog profila, neće imati način da ga poveže sa mojim pseudonimnim profilom.



![Image](assets/fr/28.webp)



Čestitamo, sada ste u toku sa SimpleX porukama, odličnom alternativom za WathsApp!



Takođe preporučujem ovaj drugi vodič, u kojem predstavljam Threema, još jednu zanimljivu alternativu za vašu aplikaciju za razmenu poruka:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74