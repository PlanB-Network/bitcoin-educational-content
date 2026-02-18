---
name: Delta Chat
description: Praktični vodič za decentralizovani alat za razmenu poruka
---

![image](assets/cover.webp)




## Uvod - Kontrola Četa i Privatnost



U poslednjih nekoliko godina sve se više govori o Chat Control-u, regulatornom predlogu koji ima za cilj uvođenje automatskog skeniranja privatnih poruka na glavnim komunikacionim platformama. Deklarisani cilj je borba protiv ilegalnog sadržaja, problem je što bi ovaj mehanizam zapravo uključivao masovni nadzor, čime bi se potkopala end-to-end enkripcija i tako ugrozila privatnost svih korisnika, ne samo prestupnika.



Prava opasnost je da razgovori postanu kontrolisana okruženja, gde svaka poruka, slika ili prilog mogu biti pregledani pre nego što stignu do primaoca. I ovde dolazi jedno moguće rešenje: udaljiti se od centralizovanih platformi i preći na decentralizovane sisteme za razmenu poruka, koji ne zavise od jednog provajdera i ne mogu lako biti podvrgnuti ovakvoj vrsti nadzora.



Jedno takvo rešenje biće predstavljeno u ovom vodiču: Delta Chat. Zreo i već upotrebljiv alat.




## Zašto Delta Chat i kako funkcioniše



Delta Chat je već veoma dobro rešenje za svakodnevno dopisivanje: veoma korisno za razgovor sa prijateljima, porodicom i drugim ljudima, baš kao pravi ekvivalent WhatsApp-a.



To je decentralizovani sistem za razmenu poruka zasnovan isključivo na e-pošti. U suštini koristi infrastrukturu tradicionalne e-pošte, ali gradi moderni interfejs i iskustvo instant mesindžera na njoj. Na prvi pogled ovo može delovati pomalo improvizovano, ali zapravo funkcioniše veoma dobro i iznenađujuće je robusno. Možete koristiti posvećene mejl servere zvane ChatMail, ali takođe može besprekorno raditi sa regularnim mejl serverima. To znači da se možete prijaviti sa postojećim nalogom ako želite, bez potrebe da kreirate nešto novo.



Još jedan vrhunac je podrška za WebXDC-ove, koji su male Web aplikacije koje se mogu koristiti direktno unutar ćaskanja, slično mini-aplikacijama u Telegram. Važna razlika je što ove aplikacije nemaju pristup Internetu, tako da ne mogu pratiti korisnika ili slati podatke eksterno.



Sa bezbednosnog aspekta, Delta Chat koristi verifikovanu end-to-end enkripciju, zasnovanu na PGP ali sa modernim ekstenzijama koje je čine uporedivom po nivou zaštite sa Signal. Jedini trenutni nedostatak je Perfect Forward Secrecy, ali to je aspekt koji se razvija.



Budući da se zasniva isključivo na e-pošti, Delta Chat to u potpunosti izbegava:




- obavezni brojevi telefona
- Centralizovani ID-ovi
- registracije povezane sa jednom uslugom



I to je ono što čini ovaj alat veoma otpornim na invazivne regulative kao što je Kontrola Četa.




## Instalacija



Sa zvanične veb stranice [Delta Chat](https://delta.chat/download) možete otići u odeljak za preuzimanje. Na Linux-u je zgodno dostupan putem Flathub-a, ali postoje i paketi za Arch, NixOS, Snap i samostalne verzije.



![image](assets/it/01.webp)



Dostupno je i za:




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- i druge prodavnice...



Ako tražite vodič za instalaciju F-Droid, ovaj tutorijal bi vam mogao pomoći:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Jedna veoma važna stvar: desktop verzije ne zahtevaju telefon. Za razliku od WhatsApp-a ili SimpleX Chat, ne morate se prvo registrovati putem mobilnog. Možete kreirati svoj profil direktno na računaru ili ga preneti sa drugog uređaja.




## Kreiranje profila



Kada se aplikacija otvori, Delta Chat pita da li želite da kreirate novi profil ili da koristite postojeći.



![image](assets/it/02.webp)



Kreiranjem novog profila možete uneti:




- ime
- slika (opciono)



Podrazumevano je predložen ChatMail server, ali je moguće:




- izaberite drugi ChatMail server
- koristi klasičan email nalog
- ručno konfigurišite IMAP i SMTP
- registrujte se koristeći pozivni kod drugog korisnika



Nakon nekoliko sekundi, profil je spreman i možete početi koristiti aplikaciju.



![image](assets/it/03.webp)




## Interface i chat



Interfejs je veoma jednostavan i direktan:




- Poruke uređaja, koje su lokalne komunikacije
- Sačuvane poruke, slične onima u Telegram i sinhronizovane između uređaja



![image](assets/it/04.webp)



Da biste dodali kontakt jednostavno:




- Prikazivanje vašeg QR koda
- Skeniraj drugu osobu
- Pozovi putem linka (podeli link za poziv).



![image](assets/it/05.webp)



Jednom kada je veza uspostavljena, end-to-end enkripcija se automatski konfiguriše. Korisnički interfejs za ćaskanje je veoma sličan onom na WhatsApp-u:




- tekstualne i glasovne poruke
- fotografije, video zapisi i datoteke
- odgovori na poruke
- reakcije
- iskakajući prozori
- prilagodljiva obaveštenja.



![image](assets/it/06.webp)



## WebXDC: aplikacije u ćaskanjima:



Delta Chat omogućava korišćenje WebXDC, tj. malih aplikacija ugrađenih u razgovore. Ovde je kratak spisak najkorisnijih identifikovanih:




- ankete
- crtaće table
- privatni privremeni čatovi
- igre sa deljenim rezultatima u ćaskanju



Složenije igre se takođe mogu započeti, što pokazuje fleksibilnost ovog alata.



![image](assets/it/07.webp)



## Grupe, kanali i napredne funkcije



Možete kreirati grupe, koristiti stikere (posebno na desktop računarima) i, aktiviranjem eksperimentalnih opcija, čak i kanale, slične onima u Telegram.



U naprednim podešavanjima možete uključiti:




- glasovni pozivi (još uvek eksperimentalno)
- napredno upravljanje profilom e-pošte
- pune sigurnosne kopije.



![image](assets/it/08.webp)



## Multidevice i backup



Delta Chat u potpunosti podržava više uređaja:




- možete dodati drugi uređaj putem QR koda
- možete izvršiti potpuni prenos putem rezervne kopije.



Za nekoliko sekundi ponovo ćete pronaći svoje četove, grupe i kompletnu istoriju, bez oslanjanja na centralni server.



![image](assets/it/09.webp)




## Zaključak



U vreme kada se sve više govori o kontroli privatnih komunikacija, Delta Chat predstavlja konkretan odgovor: decentralizovano, šifrovano dopisivanje koje je zaista upotrebljivo svakog dana.



To je rešenje koje me je, od svih koje sam probao, najviše ubedilo zbog jednostavnosti, privatnosti i slobode. Ako želite, možete me kontaktirati i na Delta Chat putem sledećeg [pozivnog linka](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Ako vam se dopao ovaj vodič, možete me podržati donacijom i ostavljanjem palca gore. I zapamtite: samo korišćenjem i istraživanjem Delta Chat-a sa mobilnog i desktop uređaja zaista ćete otkriti njegovu punu funkcionalnost.



Do sledećeg puta.