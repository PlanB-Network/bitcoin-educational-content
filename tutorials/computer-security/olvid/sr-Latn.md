---
name: Olvid
description: Privatno dopisivanje za sve
---
![cover](assets/cover.webp)



Olvid je francuska aplikacija za instant poruke pokrenuta 2019. godine, dizajnirana da ponudi visok nivo sigurnosti, bez kompromitovanja privatnosti. Za razliku od WhatsApp-a ili Signal-a, Olvid ne traži nikakve lične podatke prilikom registracije: ni broj telefona, ni email, ništa. Identifikacija između korisnika zasniva se na razmeni ključeva, bez serverskog imenika ili deljene knjige adresa.



Sve poruke su šifrovane od kraja do kraja koristeći originalni kriptografski protokol, dizajniran da zaštiti i metapodatke: niko ne zna s kim razgovarate, niti kada. Klijentski kod je otvorenog koda, ali centralni server koji se koristi za usmeravanje šifrovanih poruka ostaje vlasnički i hostovan na AWS-u.

Bezbednosni model Olvida zasniva se na važnom principu: potpunom odsustvu poverenja u treću stranu pri uspostavljanju digitalnih identiteta. Za razliku od većine aplikacija za šifrovanu komunikaciju koje koriste centralizovani imenik za upravljanje identitetima korisnika, Olvid ne zavisi ni od jedne centralne infrastrukture kako bi obezbedio integritet komunikacije. Ova arhitektura eliminiše rizike povezane sa kompromitacijom imenika.

Ipak, Olvid koristi centralni server za distribuciju poruka, ali on je strogo ograničen na logističku ulogu: obezbeđuje asinhrono slanje šifrovanih poruka. Ovaj server ne učestvuje u šifrovanju, ne zna stvarne identitete korisnika, niti sadržaj ili metapodatke poruka (osim javnog ključa primaoca, koji je neophodan za rutiranje). Stoga se može smatrati neprijateljskim po definiciji, bez ugrožavanja celokupne bezbednosti. Čak i ako bi bio kompromitovan, ne bi omogućio pristup sadržaju komunikacije. Olvid prihvata centralizaciju isporuke poruka (iz razloga efikasnosti i kvaliteta usluge), uz garanciju bezbednosti nezavisne od te infrastrukture.


Olvid nudi besplatnu verziju i verziju sa pretplatom po ceni od €4.99 mesečno. Besplatna verzija nudi punu funkcionalnost, osim mogućnosti upućivanja audio i video poziva (iako je moguće primati ih), i ne dozvoljava sinhronizaciju naloga na više uređaja. Dakle, ako planirate da koristite isključivo svoj pametni telefon i ne trebate da upućujete pozive, Olvid je odlično rešenje.



Olvid je sertifikovan od strane ANSSI (francuske agencije za sajber bezbednost). Ova aplikacija je odlična alternativa tradicionalnim servisima za razmenu poruka (WhatsApp, Facebook Messenger, WeChat...) za one koji traže privatnost uz zadržavanje jednostavnosti korišćenja.



| Aplikacija           | E2EE 1:1       | E2EE grupe     | Anonimna prijava | Licencirani klijent otvorenog koda | Licencirani server otvorenog koda | Decentralizovani server | Godina kreiranja |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opciono) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (opciono) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (federativni)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (preko emaila)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (federativni)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| **Olvid**            | **✅**          | **✅**          | **✅**               | **✅**                       **❌**                       | 🟡(nema direktorijuma)  | **2019**              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Šifrovanje od kraja do kraja*



## Instalirajte Olvid aplikaciju



Olvid je dostupan na svim platformama. Možete preuzeti aplikaciju direktno iz prodavnice aplikacija na vašem telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



Na Androidu je takođe moguće [instalirati putem APK-a](https://www.olvid.io/download/).



U ovom vodiču, fokusiraćemo se na mobilnu verziju, ali imajte na umu da su [verzije za računare takođe dostupne](https://www.olvid.io/download/) (MacOS, Linux i Windows). Ako odaberete plaćenu verziju, moći ćete da sinhronizujete svoj nalog na više uređaja.



![Image](assets/fr/01.webp)



## Kreiraj Olvid nalog 



Kada pokrenete aplikaciju prvi put, kliknite na dugme "*I am a new user*".



![Image](assets/fr/02.webp)



Izaberite nadimak ili unesite svoje ime i prezime.



![Image](assets/fr/03.webp)



Dodajte profilnu fotografiju.



![Image](assets/fr/04.webp)



Vaš nalog je sada kreiran.



![Image](assets/fr/05.webp)



Da biste sprečili gubitak pristupa vašem Olvid nalogu, preporučujemo podešavanje automatskih rezervnih kopija. Da biste to uradili, otvorite podešavanja klikom na tri tačke u gornjem desnom uglu prozora, zatim izaberite "*Settings*".

⚠️ **Pažnja**: od verzije 3.7 Olvid-a, procedura za čuvanje rezervnih kopija vaših profila i kontakata je zamenjena novom. Ovaj tutorijal još uvek prikazuje staru verziju. Možete da otkrijete novu verziju u njihovim FAQ: [💾 Čuvanje rezervnih kopija vaših profila](https://www.olvid.io/faq/sauvegarder-vos-profils/)

![Image](assets/fr/06.webp)



Idite na meni "*Save keys and contacts*".



![Image](assets/fr/07.webp)



Zatim kliknite na "*Generate a backup key*". Ovaj ključ će šifrovati vaše rezervne kopije. Ako trebate da povratite svoj nalog na drugom uređaju i više nemate pristup njemu, biće vam potrebni i rezervna kopija i ovaj ključ da biste ga dešifrovali.



![Image](assets/fr/08.webp)



Čuvajte ovaj ključ na sigurnom mestu. Takođe možete napraviti papirnu kopiju.



![Image](assets/fr/09.webp)



Zatim možete odabrati da kreirate lokalnu rezervnu kopiju ili automatsku rezervnu kopiju na cloud servisu. Ova druga opcija se toplo preporučuje kako biste osigurali pristup vašem Olvid nalogu u svim okolnostima, čak i ako izgubite telefon.



![Image](assets/fr/10.webp)



Proverite da je opcija "*Enable automatic backup*" označena.



![Image](assets/fr/11.webp)



Takođe možete istražiti i ostala podešavanja dostupna za prilagođavanje aplikacije vašim potrebama.



![Image](assets/fr/12.webp)



## Slanje poruka sa Olvid-a



Da biste mogli slati poruke, prvo morate dodati kontakte. Na početnoj stranici kliknite na plavo dugme "*+*".



![Image](assets/fr/13.webp)



Olvid zatim prikazuje vaš korisnički ID. Možete ga zatim proslediti osobama sa kojima želite da komunicirate, kako bi vas mogli dodati kao kontakt.



Da biste dodali osobu, skenirajte njen ID kamerom ili ga ručno unesite klikom na tri male tačke u gornjem desnom uglu.



![Image](assets/fr/14.webp)



Kada se ID skenira, možete ili da vaš kontakt skenira prikazani QR kod, ili da im pošaljete zahtev za daljinsko povezivanje klikom na "*Remote contact*".



![Image](assets/fr/15.webp)



Veza je sada uspostavljena.



![Image](assets/fr/16.webp)



Sada možete početi razmenjivati poruke i drugi sadržaj sa svojim dopisnikom!



![Image](assets/fr/17.webp)



Sa početne stranice, pronaći ćete sve svoje razgovore.



![Image](assets/fr/18.webp)



Druga kartica sadrži sve vaše kontakte.



![Image](assets/fr/19.webp)



Takođe možete kreirati grupne diskusije.



![Image](assets/fr/20.webp)



Čestitamo, sada ste u toku sa korišćenjem Olvid poruka, odlične alternative za WathsApp! Ako vam je ovaj vodič bio koristan, bio bih veoma zahvalan ako biste pritisnuli zeleni palac ispod. Slobodno podelite ovaj vodič na vašim društvenim mrežama. Hvala vam puno!



Takođe preporučujem ovaj drugi vodič, u kojem vas upoznajem sa Proton Mail-om, mnogo privatnijom alternativom Gmail-u:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
