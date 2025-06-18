---
name: Signal
description: Izrazi se slobodno
---
![cover](assets/cover.webp)



Signal je aplikacija za razmenu poruka sa end-to-end enkripcijom, dizajnirana da po defaultu nudi dobru poverljivost. Svaka poruka, poziv i fajl su zaštićeni Signal protokolom, koji je prepoznat kao jedan od najrobustnijih protokola za razmenu poruka. Koriste ga mnoge druge aplikacije, uključujući WathsApp, Facebook Messenger, Skype i Google Messages za RCS komunikacije.



Signal je pokrenut 2014. godine od strane Moxie Marlinspike (pseudonim) i razvijan od 2018. godine od strane Signal Foundation, neprofitne organizacije stvorene uz podršku Briana Actona (suosnivača WhatsApp-a).



![Image](assets/fr/01.webp)



U poređenju sa WhatsApp-om, Signal se ističe svojom transparentnošću: kod aplikacije, kako klijentski tako i serverski, je potpuno otvorenog koda. Ovo omogućava svakome da ga pregleda, a posebno da proveri da li je enkripcija primenjena kako je oglašeno.



Međutim, Signal se oslanja na korišćenje telefonskog broja, što je njegova glavna slabost kada je u pitanju anonimnost u poređenju sa drugim rešenjima. Uprkos tome, aplikacija je, po mom mišljenju, jedna od najpouzdanijih u smislu sigurnosti i poverljivosti, zahvaljujući svojoj potpuno otvorenoj arhitekturi i široko prihvaćenom enkripcijskom protokolu, te je stoga testirana i revidirana, za razliku od drugih, marginalnijih aplikacija.



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




## Instalirajte aplikaciju Signal



Signal je dostupan na svim platformama. Aplikaciju možete preuzeti direktno iz prodavnice aplikacija na vašem telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



Na Androidu je takođe moguće [instalirati putem APK-a](https://github.com/signalapp/Signal-Android/releases).



U ovom vodiču ćemo se koncentrisati na mobilnu verziju, ali imajte na umu da su [desktop verzije takođe dostupne](https://signal.org/fr/download/) (MacOS, Linux i Windows). Ipak, prvo ćete morati da postavite mobilnu aplikaciju pre nego što možete da sinhronizujete svoj nalog sa desktop verzijom.



## Kreiraj nalog na Signal



Kada pokrenete aplikaciju prvi put, kliknite na dugme "*Nastavi*".



![Image](assets/fr/02.webp)



Unesite svoj broj telefona, a zatim kliknite na "*Next*".



![Image](assets/fr/03.webp)



Verifikacioni kod će vam biti poslat putem SMS-a. Unesite ovaj kod u aplikaciju Signal.



![Image](assets/fr/04.webp)



Izaberite PIN kod da zaštitite svoj Signal nalog. Ovaj kod šifrira vaše podatke i može se koristiti za vraćanje pristupa vašem nalogu ako izgubite uređaj. Zato je važno izabrati jak PIN kod koji je što duži i nasumičniji, i da ga pouzdano zabeležite.



![Image](assets/fr/05.webp)



Potvrdite ovaj PIN kod još jednom.



![Image](assets/fr/06.webp)



Sada možete personalizovati svoj korisnički profil. Izaberite fotografiju, unesite svoje ime ili nadimak. U ovoj fazi, možete takođe definisati ko može da vas pronađe na Signalu putem vašeg broja. Izaberite "*Svi*" ako želite da budete vidljivi, ili "*Niko*" da ostanete nepronađeni putem broja telefona (tada možete biti dodati samo sa vašim "*Korisničkim imenom*"). Kada završite sa izborom, kliknite na "*Dalje*".



![Image](assets/fr/07.webp)



Sada ste povezani na Signal i spremni za Exchange poruke.



![Image](assets/fr/08.webp)



## Podešavanje vašeg Signal naloga



Kliknite na svoju profilnu fotografiju u gornjem levom uglu da biste pristupili postavkama aplikacije.



![Image](assets/fr/09.webp)



Meni "*Account*" vam omogućava da upravljate postavkama profila. Savetujem vam da zadržite podrazumevane postavke. Takođe možete aktivirati opciju "*Registration Lock*", koja štiti vaš nalog od određenih vrsta napada. Ovaj meni takođe sadrži opcije koje su vam potrebne za prenos naloga na novi uređaj.



![Image](assets/fr/10.webp)



Klikom ponovo na svoju profilnu sliku u podešavanjima, doći ćete do opcija za personalizaciju vašeg profila. Preporučujem da postavite "*Korisničko ime*": ovo će vam omogućiti da stupite u kontakt sa drugim ljudima bez otkrivanja vašeg broja telefona.



![Image](assets/fr/11.webp)



Odabirom "*QR code ili link*", dobićete informacije koje su vam potrebne da ih podelite sa nekim ko želi da vas doda na Signal.



![Image](assets/fr/12.webp)



Meni "*Privacy*" je posebno važan. Ovde ćete pronaći opcije za kontrolu vidljivosti vašeg broja, upravljanje vašim porukama sa vašim kontaktima, kao i razne dozvole dodeljene na aplikaciji.



![Image](assets/fr/13.webp)



I slobodno istražite menije "*Appearance*", "*Chats*" i "*Notifications*" kako biste prilagodili Interface i rad aplikacije vašim ličnim potrebama.



## Poveži desktop aplikaciju



Da biste povezali desktop aplikaciju, počnite instaliranjem softvera na vašem računaru (pogledajte prvi deo ovog tutorijala). Zatim, na vašem telefonu, idite na Podešavanja i otvorite sekciju "*Povezani uređaji*".



![Image](assets/fr/14.webp)



Kliknite na dugme "*Poveži novi uređaj*".



![Image](assets/fr/15.webp)



Na vašem računaru, pokrenite softver, zatim skenirajte QR kod prikazan na ekranu koristeći vaš telefon. Ako želite da uvezete vaše razgovore, izaberite opciju "*Transfer message history*".



![Image](assets/fr/16.webp)



Vaši uređaji su sada potpuno sinhronizovani.



![Image](assets/fr/17.webp)



## Slanje poruka putem Signala



Da biste komunicirali sa nekim na Signalu, prvo ih morate dodati kao kontakt. Postoji nekoliko opcija: možete ih dodati putem njihovog broja telefona (ako je osoba aktivirala opciju da bude pronađena na ovaj način), ili koristiti njihov Signal ID.



Kliknite na ikonu olovke u donjem desnom uglu Interface.



![Image](assets/fr/18.webp)



U mom slučaju, želim da dodam osobu po korisničkom imenu. Zato kliknem na "*Pronađi po korisničkom imenu*".



![Image](assets/fr/19.webp)



Možete zatim ili nalepiti njegov login ili skenirati njegov QR kod.



![Image](assets/fr/20.webp)



Pošalji mu poruku da uspostaviš kontakt.



![Image](assets/fr/21.webp)



Razgovor će se zatim pojaviti na početnoj stranici. Ako osoba prihvati vaš zahtev za kontakt, videćete njeno ime i profilnu fotografiju.



![Image](assets/fr/22.webp)



Čestitamo, sada ste upoznati sa korišćenjem Signal poruka, odličnom alternativom za WathsApp! Ako ste smatrali da je ovaj vodič koristan, bio bih veoma zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj vodič na vašim društvenim mrežama. Hvala vam puno!



Takođe preporučujem ovaj drugi vodič, u kojem vas upoznajem sa Proton Mail-om, mnogo privatnijom alternativom Gmail-u :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2