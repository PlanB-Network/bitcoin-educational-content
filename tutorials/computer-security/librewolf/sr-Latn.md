---
name: LibreWolf
description: Kako koristiti LibreWolf pregledač za privatnost
---

![cover](assets/cover.webp)



Svaki klik, svaka pretraga, svaka posećena stranica: vaš web pregledač je postao sofisticirani doušnik koji hrani globalni komercijalni nadzorni sistem. Google Chrome, koji koristi preko 3 milijarde ljudi, pretvara vaše svakodnevno pretraživanje u unosne podatke za reklamne gigante. Čak i Firefox, uprkos svojoj reputaciji "etičkog" pregledača, po defaultu aktivira telemetrijske mehanizme koji prenose vaše navike pretraživanja Mozilli.



Ova stvarnost postavlja suštinsko pitanje: da li je još uvek moguće slobodno pretraživati Internet bez stalnog nadzora i profilisanja? Srećom, odgovor je da, zahvaljujući projektima zajednice koji korisnika ponovo stavljaju u središte svojih briga.



LibreWolf oličava ovu filozofiju digitalnog otpora. Plod rada zajednice nezavisnih programera, ovaj pregledač pretvara Firefox u pravi štit protiv online nadzora. Dok komercijalni pregledači nastoje unovčiti vašu pažnju, LibreWolf čini suprotno: čini vas nevidljivim za trackere dok očuvava fluidno, moderno iskustvo pretraživanja.



U ovom vodiču, otkrićemo kako LibreWolf može transformisati način na koji surfujete internetom, nudeći snažnu zaštitu protiv praćenja bez žrtvovanja performansi ili kompatibilnosti sa webom.



![LIBREWOLF](assets/fr/01.webp)


*Udeo tržište web pregledača: Chrome dominira sa 65% tržišta, praćen Safari i Edge. Ova dominacija postavlja pitanja o raznolikosti weba i privatnosti*



## Predstavljamo LibreWolf



**FreeWolf** je veb pregledač otvorenog koda izveden iz Mozilla Firefox-a, razvijen i održavan od strane nezavisne zajednice entuzijasta slobodnog softvera. Njegov glavni cilj je da ponudi pregledanje fokusirano na privatnost, sigurnost i slobodu korisnika.



U konkretnom smislu, LibreWolf koristi Firefox-ov Gecko engine, ali sa radikalno drugačijom filozofijom: gde Firefox mora balansirati između privatnosti i jednostavnosti korišćenja, LibreWolf se opredeljuje za privatnost po default-u. Projekat uklanja sve što bi moglo narušiti vašu privatnost (telemetrija, prikupljanje podataka, sponzorisani moduli) dok integriše poboljšana sigurnosna podešavanja.



### Ciljevi: privatnost i sloboda



LibreWolf ima za cilj maksimiziranje zaštite protiv praćenja i otiska prsta, dok poboljšava sigurnost pretraživača. Njegovi glavni ciljevi uključuju:





- Eliminišite svu telemetriju i prikupljanje podataka** u Firefoxu
- Onemogući funkcije koje su u suprotnosti sa slobodom korisnika**, kao što su vlasnički DRM moduli
- Primeni postavke privatnosti/bezbednosti** i specifične zakrpe od samog početka
- Razvoj zajednice garantuje transparentnost i nezavisnost** od komercijalnih interesa



Ukratko, LibreWolf se predstavlja kao "Firefox kakav bi bio da je privatnost na prvom mestu" - pregledač koji vas poštuje po defaultu, bez potrebe za dodatnom konfiguracijom.



### Glavne karakteristike



Od samog početka, LibreWolf nudi niz funkcija usmerenih na privatnost:



**Bez telemetrije ili prikupljanja podataka:** Za razliku od Chrome-a ili Firefox-a, koji šalju određene statistike korišćenja, LibreWolf apsolutno ništa ne prikuplja iz vašeg pretraživanja. Nema izveštaja o greškama, nema korisničkih studija, nema sponzorisanih sugestija.



**LibreWolf** nativno integriše ekstenziju uBlock Origin, jedan od najboljih blokatora reklama i tragača na tržištu. Podrazumevano, LibreWolf agresivno filtrira sve što bi moglo da vas prati na mreži (nametljive reklame, skripte za praćenje, kriptovalute Mining).



**Privatni pretraživač po defaultu:** LibreWolf po defaultu koristi DuckDuckGo kao početni pretraživač, koji ne čuva istoriju vaših upita. Druge alternative orijentisane na privatnost (Searx, Qwant, Whoogle) su takođe dostupne.



**Pojačana zaštita protiv otisaka prstiju:** Otisak prsta omogućava da se pregledač jedinstveno identifikuje putem njegove konfiguracije, čak i bez kolačića. Da bi se to sprečilo, LibreWolf aktivira RFP (Resist Fingerprinting) tehnologiju iz Tor projekta, kako bi vaš pregledač bio što generičniji. Testovi pokazuju da je standardni Firefox ~90% jedinstven na alatima kao što je coveryourtracks.eff.org, u poređenju sa samo ~10-20% za LibreWolf (ovi podaci su indikativni i mogu varirati u zavisnosti od softverske i hardverske konfiguracije i instaliranih ekstenzija).



![LIBREWOLF](assets/fr/07.webp)


*EFF test stranica [Cover Your Tracks](https://coveryourtracks.eff.org/) sa dugmetom TEST YOUR BROWSER. Ova stranica se koristi za procenu zaštite protiv praćenja i otiska prsta.



![LIBREWOLF](assets/fr/08.webp)


*Rezultat testa Cover Your Tracks. Poruka "imate snažnu zaštitu protiv praćenja na Webu" je prikazana, pokazujući efikasnost LibreWolf-a.* zaštita



**LibreWolf aktivira stroga sigurnosna podešavanja po podrazumevanoj vrednosti. Firefoxova Poboljšana zaštita od praćenja je postavljena na Strogi nivo kako bi blokirala hiljade tragača, kolačića trećih strana i zlonamerni sadržaj. Takođe aktivira izolaciju sajtova i kolačića (*Total Cookie Protection*) kako bi particionisala podatke za svaku domenu, i ograničava WebRTC (ograničavajući *ICE kandidate* i rutiranje preko proxy-ja kada je proxy prisutan) kako bi smanjila rizik od curenja IP Address.



**Brza ažuriranja pretraživača:** Projekat pomno prati razvoj Firefox-a: LibreWolf je uvek zasnovan na najnovijoj stabilnoj verziji Firefox-a, a održavaoci se trude da izdaju novu verziju u roku od 24 do 72 sata nakon svakog zvaničnog izdanja Firefox-a.



## Prednosti i nedostaci



### Pogodnosti





- Nema telemetrije ili neželjenih veza:** LibreWolf ne prenosi podatke o korišćenju, osiguravajući potpunu zaštitu vaše privatnosti.





- Otvoreni kod i zasnovan na zajednici:** Projekat je 100% otvorenog koda i održavaju ga volonteri. Ova nezavisnost garantuje da nijedan reklamni model neće uticati na razvoj.





- Pre-konfigurisano za privatnost:** LibreWolf vam štedi dragoceno vreme: nema potrebe da provodite sate podešavajući Firefox postavke, sve je već urađeno.





- Izvorni blokator oglasa/tragača:** uBlock Origin je integrisan kao standard, tako da ne morate ništa da radite kako biste se zaštitili od oglasa i grešaka.





- Izvrsna zaštita od otisaka prstiju:** Zahvaljujući RFP-u i brojnim postavkama privatnosti, LibreWolf drastično smanjuje vaš jedinstveni digitalni otisak na internetu.





- Poboljšane performanse i mala težina:** Uklanjanjem telemetrije i određenih neesencijalnih funkcija, LibreWolf može biti nešto brži i manje zahtevati energiju od standardnog Firefoxa.



### Nedostaci i ograničenja





- Nema ugrađenih automatskih ažuriranja:** LibreWolf se ne ažurira sam. Na vama je da instalirate nove verzije čim budu objavljene, kako biste ostali bezbedni.





- Smanjena kompatibilnost sa određenim uslugama:** Zbog veoma strogih podešavanja, LibreWolf može naići na probleme na određenim veb-sajtovima. Streaming platforme kao što su Netflix i Disney+ neće raditi, jer LibreWolf podrazumevano onemogućava Widevine DRM.





- Nema ugrađenu anonimnu mrežu:** Za razliku od Tor Browser-a, LibreWolf ne usmerava saobraćaj putem Tor-a ili VPN-a samostalno. Ako vam je potrebna mrežna anonimnost, moraćete ručno da konfigurišete proxy/VPN.





- Kolačići koji nisu trajni i sesije (podrazumevano):** Iz razloga poverljivosti, LibreWolf briše kolačiće, istoriju i podatke sa sajtova svaki put kada zatvorite svoj pregledač. Moraćete ponovo da se prijavite na svoje naloge svaki put kada se prijavite.





- Nema mobilne verzije ili sinhronizacije sa oblakom:** LibreWolf je dostupan samo na desktopu (Windows, Linux, macOS). Ne postoji mobilna aplikacija, i stoga nema sinhronizacije naloga ili obeleživača putem oblaka.



## Instaliranje LibreWolf-a



**Official website:** [librewolf.net](https://librewolf.net)



LibreWolf je dostupan za sve glavne desktop operativne sisteme: Linux, Windows i macOS. Da biste preuzeli LibreWolf, posetite zvaničnu veb stranicu:



![LIBREWOLF](assets/fr/02.webp)


*Početna stranica LibreWolf-a (librewolf.net) prikazuje logo pregledača, plavo dugme Instaliraj, i linkove Izvorni kod i Dokumentacija. Velika plava strelica pokazuje na dugme Instaliraj*



Kliknite na dugme „Instalacija“ da biste pristupili detaljnim uputstvima za vaš operativni sistem:



![LIBREWOLF](assets/fr/03.webp)


*Stranica za odabir operativnog sistema za LibreWolf.* preuzimanje



Instalacija se razlikuje u zavisnosti od vašeg OS-a:



### Na Linuxu


LibreWolf nudi verzije za mnoge distribucije. Na Debian/Ubuntu i derivatima, dostupan je zvanični APT repozitorijum. Alternativno, LibreWolf je objavljen kao Flatpak na Flathub:


```
flatpak install flathub io.gitlab.librewolf-community
```



### Na Windowsu


Preuzmite instalacioni program (.exe) sa zvaničnog sajta ili koristite:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`



### Na macOS


LibreWolf je dostupan kao .dmg paket za Mac. Preuzmite sliku diska sa zvaničnog sajta i prevucite LibreWolf aplikaciju u vaš folder Applications. Alternativno, možete ga instalirati putem Homebrew-a.




## Konfiguracija i prva upotreba



Prilikom prvog pokretanja, primetićete poznati Firefox Interface, osim što je više pojednostavljen: početna stranica sadrži samo traku za pretragu i nema sponzorisanih sugestija. Videćete ikonu uBlock Origin u traci sa alatkama - znak da je blokator aktivan.



![LIBREWOLF](assets/fr/04.webp)


*Početna stranica LibreWolf-a sa ekstenzijama i menijem. Plava strelica u gornjem desnom uglu označava ikonu menija (tri horizontalne linije)



LibreWolf automatski učitava vaše stranice u "strogi" (anti-tracking) režim, a podrazumevani pretraživač će biti DuckDuckGo. Možete pokušati da posetite sajt za testiranje praćenja (npr. amiunique.org) kako biste uočili izloženi otisak - trebalo bi da bude mnogo generičkiji nego sa standardnim pregledačem.



### Postavke privatnosti



LibreWolf je već optimalno konfigurisan za privatnost. U Meni → Opcije → Privatnost i sigurnost, videćete da je LibreWolf postavljen na režim Poboljšane zaštite od praćenja: Strogo. Ovaj režim blokira:




- Međusajtni tragači
- Kolačići treće strane
- Poznati sadržaj za praćenje
- Kryptomajning
- Detektori digitalnih otisaka prstiju



![LIBREWOLF](assets/fr/05.webp)


*Stranica sa karticama za sigurnost i privatnost prikazuje LibreWolf.* sigurnosne postavke



WebRTC je onemogućen (sprečavanje curenja IP adresa), a Total Cookie Protection je na snazi. Telemetrija i Firefox ankete su potpuno onemogućene.



### Upravljanje kolačićima i istorijom



Podrazumevano, LibreWolf briše kolačiće i lokalnu memoriju svaki put kada se zatvori. Ako vam ovo ponašanje smeta, možete ga prilagoditi u Privatnost i bezbednost → Kolačići i podaci sa sajtova tako što ćete poništiti izbor "Obriši kolačiće i podatke sa sajtova kada se zatvori LibreWolf".



![LIBREWOLF](assets/fr/06.webp)


*Na istoj stranici malo niže, prikazuje opciju za brisanje kolačića kada se pregledač zatvori*



### Dodavanje korisnih ekstenzija



U principu, LibreWolf obeshrabruje dodavanje nepotrebnih ekstenzija, jer svaka ekstenzija može biti vektor praćenja. Ipak, neke renomirane ekstenzije mogu poboljšati vaše iskustvo:




- Firefox Multi-Account Containers** (by Mozilla) za pregledanje u odvojenim kontejnerima
- Decentraleyes** ili **LocalCDN** za lokalno posluživanje uobičajenih biblioteka



Posebno izbegavajte ekstenzije "besplatni VPN" ili sumnjive proxy-je - uBlock Origin već pokriva 99% vaših potreba.



## Svakodnevna upotreba



### Svakodnevno pretraživanje interneta


Koristite LibreWolf za vaše svakodnevne aktivnosti na Internetu. Glavna razlika u odnosu na druge pretraživače je što ostavljate mnogo manje tragova za oglašavanje. Baneri "Prihvati kolačiće" nestaju na mnogim sajtovima, zahvaljujući uBlock-ovim listama filtera.



### Koristite privatne kartice za kompartmenalizaciju


Iako LibreWolf briše sve na kraju sesije, može biti korisno otvoriti prozor privatnog pretraživača (Ctrl+Shift+P) za određene zadatke tokom sesije, kako bi se odvojio specifičan identitet.



### Iskoristite kontejnere za više naloga


Instaliranje ekstenzije Multi-Account Containers može vam značajno pomoći da segmentirate svoje aktivnosti u vodonepropusne silose. Na primer, možete definisati kontejner "Banking" za vaše bankarske sajtove, kontejner "Social Networks" za Facebook/Twitter, itd. Svaki kontejner ima svoje kolačiće, sesije i izolovanu memoriju. Svaki kontejner ima svoje kolačiće, sesije i izolovanu memoriju.



### Fino podešeno upravljanje dozvolama po lokaciji


LibreWolf vam omogućava da kontrolišete dozvole koje dajete sajtovima (Lokacija, Kamera, Mikrofon, Obaveštenja) pojedinačno. Dajte dozvole samo sajtovima kojima verujete i gde je to neophodno.



## Najbolje prakse sa LibreWolf



1. **Ažurirajte LibreWolf:** Redovno proveravajte sajt za nove verzije, posebno nakon stabilnog izdanja Firefox-a.



2. **Izbegavajte mešanje ličnog identiteta i privatnog pretraživanja:** Idealno bi bilo da se ne prijavljujete sa ličnim nalozima u istoj sesiji u kojoj obavljate osetljivo istraživanje.



3. **Nemojte preopteretiti LibreWolf suvišnim ekstenzijama:** Svaka ekstenzija koju instalirate može uneti sigurnosne rizike ili rizike otiska prsta.



4. **Koristite VPN ili Tor proxy dodatno:** LibreWolf vas ne čini anonimnim za vašeg ISP-a. Za mrežnu anonimnost, možete koristiti LibreWolf iza pouzdanog VPN-a.



5. **Sačuvajte važne podatke:** Zabeleške, lozinke ako su sačuvane lokalno. Razmislite o eksternom menadžeru lozinki (KeePassXC, Bitwarden) umesto osnovnog menadžera lozinki u pregledaču.



## Poređenje sa drugim pregledačima



LibreWolf je deo "alatke" pregledača usmerenih na privatnost:



**LibreWolf vs. Firefox:** LibreWolf dolazi već ojačan i bez ikakve telemetrije. Firefox zadržava prednost sinhronizacije na više uređaja i veoma veliku bazu korisnika, ali zahteva ručnu konfiguraciju da bi postigao nivo poverljivosti kao LibreWolf.



**Brave koristi Chrome/Chromium kod i integriše poslovni model putem svog opcionalnog reklamnog programa. LibreWolf, kao zajednica Fork za Firefox, zadržava Mozillin slobodan ekosistem i nema veze sa Google-om.



**LibreWolf vs Tor Browser:** Tor Browser je nezamenljiv za anonimnost u suočavanju sa moćnim nadzorom, ali je spor i neudoban za svakodnevnu upotrebu. LibreWolf, za svakodnevno pretraživanje klasičnog weba, je mnogo brži i praktičniji.



**LibreWolf vs Mullvad Browser:** Mullvad Browser ide još dalje u standardizaciji, ali na račun smanjene upotrebljivosti (nemoguće je zadržati kolačić za prijavu). LibreWolf postiže ravnotežu: veoma privatan, ali upotrebljiv na dnevnoj bazi.



## Zaključak



LibreWolf predstavlja odlično rešenje za one koji traže ultra-privatni "svakodnevni" pregledač, a da ne idu do ekstremne anonimnosti kao kod Tor-a. To je idealan izbor za aktiviste, novinare, programere ili napredne korisnike koji žele klasično pretraživanje interneta (brzo, kompatibilno sa modernim sajtovima) dok izbegavaju praćenje oglasa i Veliku Tehnologiju.



Iako ima određena ograničenja (nema automatskih ažuriranja, smanjena kompatibilnost sa određenim uslugama), LibreWolf je vredan alat u arsenalu svakoga ko želi da povrati kontrolu nad svojom digitalnom privatnošću. Njegova jednostavnost korišćenja i podrazumevana konfiguracija čine ga mudrim izborom za korisnike koji su svesni važnosti privatnosti.



## Resursi



### Zvanična dokumentacija




- [LibreWolf zvanična veb stranica](https://librewolf.net)
- [Izvorni kod na Codeberg-u](https://codeberg.org/librewolf)
- [Službena FAQ](https://librewolf.net/docs/faq)



### Vodiči i poređenja




- [Privacy Guides](https://www.privacyguides.org/en/desktop-browsers/)
- [Uporedni testovi privatnosti](https://privacytests.org)



### Podrška zajednice




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)