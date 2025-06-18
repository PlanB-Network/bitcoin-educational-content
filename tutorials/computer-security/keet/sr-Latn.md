---
name: Keet
description: Čet od osobe do osobe
---
![cover](assets/cover.webp)



Keet je aplikacija za instant poruke dizajnirana da radi bez ikakvih servera. Pokrenuta 2022. godine od strane Holepunch-a (kompanije finansirane od strane Tether-a i Bitfinex-a), aplikacija je u potpunosti zasnovana na peer-to-peer mreži i karakteriše je radikalno decentralizovan pristup: poruke, pozivi i fajlovi se razmenjuju direktno između korisnika, bez posrednika.



Keet šifrira sve komunikacije od kraja do kraja i ne traži lične podatke. Registracija je anonimna, bez potrebe za brojem telefona ili email adresom. Pored razmene tekstualnih poruka, Keet nudi video pozive veoma visokog kvaliteta, kao i neograničeno deljenje fajlova. Aplikacija se stoga može koristiti na hibridan način, kako za ličnu, tako i za profesionalnu upotrebu.



![Image](assets/fr/01.webp)



Trenutno (april 2025), Keet nije u potpunosti open-source. Deo izvornog koda je dostupan na [Holepunch-ovom GitHub repozitorijumu](https://github.com/holepunchto), posebno kriptografske i mrežne komponente, ali klijent Interface još uvek nije. Holepunch je, međutim, najavio svoju nameru da celu aplikaciju učini open-source u budućnosti. U zavisnosti od toga kada otkrijete ovaj vodič, ovo je možda već urađeno.




| Aplikacija           | E2EE 1:1       | E2EE grupe     | Anonimna registracija | Licenca klijenta open-source | Licenca servera open-source | Decentralizovani server      | Godina kreiranja  |
| -------------------- | -------------- | -------------- | --------------------- | ---------------------------- | --------------------------- | ---------------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                     | ❌                            | ❌                           | ❌                            | 2009              |
| WeChat               | ❌              | ❌              | ❌                     | ❌                            | ❌                           | ❌                            | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opcionalno) | ❌                     | ❌                            | ❌                           | ❌                            | 2011              |
| Telegram             | 🟡 (opcionalno) | ❌              | 🟡                    | ✅                            | ❌                           | ❌                            | 2013              |
| LINE                 | ✅              | ✅              | ❌                     | ❌                            | ❌                           | ❌                            | 2011              |
| Signal               | ✅              | ✅              | ❌                     | ✅                            | ✅                           | ❌                            | 2014              |
| Threema              | ✅              | ✅              | ✅                     | ✅                            | ❌                           | ❌                            | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                     | ✅                            | ✅                           | 🟡 (federativni)            | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                     | ✅                            | N/A                         | 🟡 (preko email-a)          | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                     | ✅                            | ✅                           | 🟡 (federativni)            | 2014              |
| Session              | ✅              | ✅              | ✅                     | ✅                            | ✅                           | ✅                            | 2020              |
| SimpleX              | ✅              | ✅              | ✅                     | ✅                            | ✅                           | ✅                            | 2021              |
| Olvid                | ✅              | ✅              | ✅                     | ✅                            | ❌                           | 🟡(nema direktorijuma)      | 2019              |
| Keet                 | ✅              | ✅              | ✅                     | ❌                            | N/A                         | ✅                            | 2022              |
| Jami                 | ✅              | ✅              | ✅                     | ✅                            | N/A                         | ✅                            | 2005              |
| Briar                | ✅              | ✅              | ✅                     | ✅                            | N/A                         | ✅                            | 2018              |
| Tox                  | ✅              | ✅              | ✅                     | ✅                            | N/A                         | ✅                            | 2013              |

*E2EE = Šifrovanje od kraja do kraja*



## Instaliraj Keet



Keet je dostupan na svim platformama. Možete preuzeti aplikaciju direktno iz prodavnice aplikacija na vašem telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



Na Androidu je takođe moguće [instalirati putem APK](https://github.com/holepunchto/keet-mobile-releases/releases).



U ovom vodiču ćemo se koncentrisati na mobilnu verziju, ali imajte na umu da su [verzije za računare takođe dostupne](https://keet.io/) (MacOS, Linux i Windows). Takođe je moguće sinhronizovati vaš nalog na više uređaja.



## Kreiraj nalog na Keet



Prilikom prvog pokretanja, možete zanemariti ekrane prezentacije.



![Image](assets/fr/02.webp)



Kliknite na dugme "*I'm a new user*".



![Image](assets/fr/03.webp)



Prihvatite uslove korišćenja, zatim kliknite na "*Quick setup*".



![Image](assets/fr/04.webp)



Izaberite ime ili nadimak, zatim kliknite na "*Završi podešavanje*".



![Image](assets/fr/05.webp)



Vaš profil je sada kreiran. Kliknite na "*Finish setup*" ponovo da završite.



![Image](assets/fr/06.webp)



Profil možete prilagoditi u bilo kom trenutku iz kartice "*Profil*".



## Sačuvaj svoj Keet nalog



Prva stvar koju treba da uradite sa svojim novim Keet nalogom je da sačuvate svoju frazu za oporavak. Ovo je niz od 24 reči koji će vam omogućiti da povratite pristup svom nalogu u slučaju gubitka ili promene uređaja. Ova fraza daje pun pristup vašem nalogu svakome ko je zna, tako da je važno napraviti pouzdanu rezervnu kopiju i nikada je ne otkrivati.



Da biste to uradili, kliknite na karticu "*Profil*" u donjem desnom uglu Interface.



![Image](assets/fr/07.webp)



Zatim pristupite meniju "*Settings*".



![Image](assets/fr/08.webp)



Odaberite "*Privacy and Security*".



![Image](assets/fr/09.webp)



Zatim kliknite na "*Recovery phrase*".



![Image](assets/fr/10.webp)



Pritisnite dugme "*View phrase*" da biste prikazali svoju frazu za oporavak. Pažljivo je kopirajte i čuvajte na sigurnom mestu.



![Image](assets/fr/11.webp)



## Slanje poruka sa Keet



Da biste komunicirali na Keet-u, potrebno je da kreirate "*Rooms*". Da biste to uradili, kliknite na ikonu olovke u gornjem desnom uglu Interface.



![Image](assets/fr/12.webp)



Odaberite "*Nova grupna ćaskanja*".



![Image](assets/fr/13.webp)



Izaberite ime i opis za vašu "*Sobu*", zatim kliknite na "*Kreiraj grupni čet*".



![Image](assets/fr/14.webp)



Vaša "*Soba*" je sada kreirana. Kliknite na ikonu "*+*" u gornjem desnom uglu da pozovete učesnike.



![Image](assets/fr/15.webp)



Definišite prava koja dodeljujete novim članovima putem pozivnog linka, kao i trajanje važenja linka. Zatim kliknite na "*generate invite*".



![Image](assets/fr/16.webp)



Keet će generate link za pridruživanje vašoj "*Sobi*". Možete ga kopirati i podeliti, ili omogućiti ljudima koje želite da pozovete da skeniraju njegov QR kod.



![Image](assets/fr/17.webp)



Sada možete početi razmenjivati poruke i multimedijalne datoteke. Da biste pokrenuli poziv, kliknite na ikonu telefona u gornjem desnom uglu.



![Image](assets/fr/18.webp)



Iz ove grupe možete slati privatne poruke određenom članu. Kliknite na profilnu sliku grupe, a zatim izaberite željenog člana u odeljku "*Članovi*".



![Image](assets/fr/19.webp)



Kliknite na dugme "*Pošalji zahtev za DM*" i unesite svoju poruku.



![Image](assets/fr/20.webp)



Kada zahtev za DM bude prihvaćen, naći ćete ovaj kontakt na početnoj stranici, gde možete razgovarati s njim privatno.



![Image](assets/fr/21.webp)



## Sinhronizujte svoj nalog na više uređaja



Sada kada znate kako da koristite Keet i imate nalog, možete ga sinhronizovati i na drugom uređaju, kao što je računar. Da biste to uradili, otvorite aplikaciju na svom mobilnom telefonu, zatim kliknite na "*Profil*" i pristupite "*Podešavanjima*".



![Image](assets/fr/22.webp)



Zatim idite na meni "*Moji uređaji*".



![Image](assets/fr/23.webp)



Kliknite na "*Add device*". Keet će generate link za sinhronizaciju novog uređaja. Kopirajte ovaj link.



![Image](assets/fr/24.webp)



Na vašem drugom uređaju, instalirajte Keet. Na početnom ekranu, odaberite opciju "*I'm a current user*".



![Image](assets/fr/25.webp)



Zatim kliknite na "*Link device*".



![Image](assets/fr/26.webp)



Nalepite vezu koju je obezbedio vaš prvi uređaj, a zatim kliknite na "*Start syncing*".



![Image](assets/fr/27.webp)



Na svom prvom uređaju kliknite na "*Potvrdi povezivanje uređaja*" da biste autorizovali vezu.



![Image](assets/fr/28.webp)



Na drugom uređaju, dovršite proces klikom na "*Link devices*".



![Image](assets/fr/29.webp)



Sada možete pristupiti svim svojim "*Room*" i razgovorima sa ovog novog uređaja.



![Image](assets/fr/30.webp)



Čestitamo, sada ste u toku sa korišćenjem Keet poruka, odlične alternative za WathsApp! Ako vam je ovaj vodič bio koristan, bio bih veoma zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj vodič na vašim društvenim mrežama. Hvala vam puno!



Takođe preporučujem ovaj drugi vodič, u kojem vas upoznajem sa Proton Mail-om, mnogo privatnijom alternativom Gmail-u :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2