---
name: Mullvad Browser
description: Kako koristiti Mullvad Browser za privatnost
---

![cover](assets/cover.webp)



U svetu gde digitalni nadzor postaje sveprisutan, zaštita vaše online privatnosti nikada nije bila važnija. Kompanije koriste sofisticirane tehnike da vas prate:





- Kolačići trećih strana**: mali fajlovi koje postavljaju spoljašnji sajtovi da bi vas pratili sa jednog sajta na drugi
- Otisak prsta**: prikuplja jedinstvene karakteristike vašeg pregledača i uređaja (rezolucija ekrana, instalirani fontovi, dodaci, itd.) kako bi vas identifikovao bez kolačića
- Skripte za praćenje**: nevidljivi JavaScript kodovi koji analiziraju vaše ponašanje pri pretraživanju (klikovi, skrolovanje, vreme provedeno)
- Analiza IP Address**: geografska lokacija i identifikacija vašeg Internet provajdera



Ovi podaci se zatim kombinuju kako bi se kreirali detaljni profili vašeg ponašanja na mreži i unovčavaju se, često bez vašeg znanja. Ova stvarnost postavlja osnovno pitanje: kako možete surfovati Internetom dok čuvate svoju anonimnost i poverljivost?



Odgovor leži uglavnom u vašem izboru web pregledača. Ovaj alat, koji svakodnevno koristimo za pristup informacijama, kupovinu ili komunikaciju, igra odlučujuću ulogu u zaštiti naših ličnih podataka. Nažalost, popularni pregledači kao što je Google Chrome (koji drži oko 65% globalnog tržišta) su dizajnirani oko poslovnih modela zasnovanih na masovnom prikupljanju podataka korisnika.



![MULLVAD BROWSER](assets/fr/01.webp)


*Ističe se Mullvad Browser zbog izuzetno efikasnog blokiranja tragača, daleko nadmašujući potrošačke pretraživače*



Suočeni s ovim izazovom, pojavljuju se novi igrači sa drugačijom filozofijom: stavljanjem privatnosti u srž njihovog dizajna. Među njima, Mullvad Browser se ističe kao inovativno rešenje koje kombinuje najbolje zaštite privatnosti sa fluidnim, pristupačnim iskustvom pretraživanja.



Za razliku od tradicionalnih pregledača koji nastoje personalizovati vaše iskustvo prikupljanjem vaših podataka, Mullvad Browser pristupa suprotno: čini da svi njegovi korisnici izgledaju identično za web stranice, čime individualizovano praćenje postaje praktično nemoguće.



U ovom vodiču ćemo zajedno otkriti kako Mullvad Browser može transformisati način na koji pretražujete Internet, nudeći vam snažnu zaštitu od nadzora bez žrtvovanja jednostavnosti korišćenja.




## Predstavljamo Mullvad Browser



**Mullvad Browser** je veb pregledač fokusiran na privatnost, razvijen u saradnji sa Tor Project-om i distribuiran besplatno od strane švedske kompanije Mullvad VPN. Pokrenut u aprilu 2023. godine, predstavlja se kao **"Tor Browser bez Tor mreže"**, dizajniran da minimizira praćenje i otiske prstiju na mreži, omogućavajući korisnicima da pretražuju putem pouzdanog VPN-a umesto Tor mreže.



Mullvad Browser je besplatan, open-source pregledač zasnovan na Firefox ESR (dugotrajnoj verziji Mozilla Firefox-a) i ojačan od strane stručnjaka Tor projekta. Konkretno, uključuje većinu **zaštitnih funkcija Tor Browser-a**, ali **ne usmerava saobraćaj preko Tor mreže**. Umesto toga, korisnici mogu (i treba) da ga povežu sa pouzdanim šifrovanim VPN-om kako bi anonimizovali svoj IP Address.



Što se tiče korisničkog iskustva, Mullvad Browser podseća na klasični pregledač, nudeći fluidnu navigaciju. Dostupan je besplatno na Windows, macOS i Linux (nema mobilnu verziju). Ne morate biti pretplatnik Mullvad VPN-a da biste ga koristili; međutim, **korišćenje Mullvad Browser-a bez maskiranja vašeg IP-a ne pruža potpunu anonimnost** - stoga se toplo preporučuje da ga koristite u kombinaciji sa pouzdanim VPN-om.



### Ciljevi: privatnost i zaštita od praćenja



Mullvad pregledač je dizajniran sa jednim glavnim ciljem: **zaštita privatnosti korisnika** na mreži i suprotstavljanje uobičajenim tehnikama praćenja i profilisanja. Njegovi glavni ciljevi uključuju:





- Drastično smanjite praćenje oglasa i praćenje** od strane veb-sajtova i oglašivačkih agencija. Po defaultu, Mullvad Browser blokira treće strane koje prate, kolačiće za praćenje i skripte za otiske prstiju koje bi vas mogle identifikovati.





- Standardizujte otisak prsta vašeg pregledača** kako biste se **"stopili s masom"**. Otisak prsta je poput jedinstvene "lične karte" kreirane kombinovanjem svih karakteristika vašeg pregledača. Mullvad Browser osigurava da svi njegovi korisnici imaju potpuno istu "ličnu kartu", čineći ih nemogućim za individualno razlikovanje.





- Nudi trenutnu zaštitu bez dodatnih ekstenzija**. Mullvad Browser dolazi u konfiguraciji "spreman za korišćenje": korisnik ne mora da instalira niz ekstenzija ili menja bilo kakva podešavanja da bi bio zaštićen.





- Ne žrtvujte performanse ili ergonomiju** više nego što je potrebno. U odsustvu Tor rutiranja, Mullvad Browser nudi mnogo brže pretraživanje nego Tor Browser, približavajući se performansama standardnog pretraživača u kombinaciji sa VPN-om.



### Ključne funkcije Mullvad Browser-a



Mullvad Browser uključuje niz **sigurnosnih i privatnih funkcija** direktno inspirisanih Tor Browser-om:





- Privatno pregledanje u svakom trenutku:** Privatni režim pregledanja je podrazumevano aktiviran i ne može se deaktivirati. **Nema istorije, kolačića ili keša koji se čuvaju iz jedne sesije u drugu**. Čim zatvorite Mullvad Browser, svi podaci o pregledanju se brišu.





- Poboljšana zaštita protiv otiska prsta:** Pregledač primenjuje stroga podešavanja kako bi osujetio digitalno otiskivanje prsta. Ovo uključuje:
 - Standardizacija korisničkog agenta** i verzije pregledača
 - Vremenska zona postavljena na UTC** za sve korisnike
 - Letterboxing**: tehnika koja automatski dodaje sive margine oko veb stranica kako bi standardizovala veličinu prikaza i sprečila identifikaciju prema dimenzijama vašeg ekrana
 - Blokiraj API-je za otisak prsta**: Canvas (2D crtanje), WebGL (3D grafika) i AudioContext (audio obrada) tehnologije su onemogućene jer mogu otkriti jedinstvene detalje o vašem hardveru
 - Standardizovani sistemski fontovi** kako bi se izbegla identifikacija putem instaliranih fontova





- Blokiranje tragača i oglašavanja:** Mullvad Browser nativno integriše ekstenziju **uBlock Origin** (pre-instalirana) sa dodatnim listama zaštite za blokiranje **tragača trećih strana, oglašivačkih skripti i drugog zlonamernog sadržaja**. Ova zaštita je praćena tehnikom **First-Party Isolation**: tehnikom koja skladišti kolačiće u odvojene "posude" za svaki sajt, sprečavajući jedan sajt da čita kolačiće koje je ostavio drugi.





- Dugme za resetovanje sesije:** Kao dugme "New Identity" u Tor pretraživaču, Mullvad pretraživač nudi dugme za **brzo restartovanje pretraživača sa novom, praznom sesijom**.





- Podesiti nivoe bezbednosti:** Možete podesiti nivo bezbednosti (*Normalno*, *Bezbednije*, *Najbezbednije*) u podešavanjima, baš kao u Tor pretraživaču.



## Ugrađene ekstenzije po defaultu



Mullvad Browser uključuje **tri unapred instalirana ekstenzije** koje čine srž njegove zaštite protiv praćenja. **Ključno je nikada ih ne uklanjati ili menjati njihove konfiguracije**, jer bi vas to učinilo jedinstvenim među korisnicima Mullvad Browser-a:



### **uBlock Origin**


Ovo proširenje za blokiranje oglasa i praćenja dolazi unapred konfigurisano sa **optimizovanim listama filtera** za blokiranje:




- Nametljivo oglašavanje
- Treće strane koje prate i prikupljaju vaše podatke
- Zlonamerni skripti
- Praćenje ponašanja Elements



uBlock Origin u Mullvad Browser koristi standardizovane parametre kako bi osigurao da svi korisnici blokiraju tačno iste Elements, čime se očuva uniformnost digitalnih otisaka.



### **NoScript**


NoScript radi u pozadini kako bi upravljao **nivoima bezbednosti** pregledača. Ovo:




- Kontroliše izvršavanje JavaScript-a** prema izabranom nivou (Normalno/Najsigurnije/Najsigurnije)
- Automatski filtrira XSS** (Cross-Site Scripting) napade
- Blokira opasan** aktivni sadržaj na sajtovima koji nisu HTTPS
- Njegova ikona je podrazumevano skrivena, ali se može prikazati putem "Prilagodi traku sa alatkama"



### **Mullvad Browser** ekstenzija


Ovo Mullvad-specifično proširenje nudi različite funkcionalnosti u zavisnosti od toga da li ste korisnik Mullvad VPN-a ili ne:



#### **Bez Mullvad VPN pretplate:**




- Osnovna provera veze**: prikazuje vašu trenutnu javnu IP adresu i neke informacije o vezi
- Preporuke za privatnost**: saveti za poboljšanje vaših sigurnosnih postavki (DNS, samo HTTPS, pretraživač)
- WebRTC** kontrola: omogućiti/onemogućiti kako bi se sprečilo curenje IP Address
- Može se izbrisati bez uticaja** na vaš digitalni otisak ako ne koristite Mullvad VPN



#### **Sa Mullvad VPN pretplatom:**


Proširenje otkriva svoj puni potencijal sa naprednim funkcijama:





- Integrisani SOCKS5 proxy**: povezivanje jednim klikom na Mullvad VPN server proxy
 - Fiksna IP Address**: za razliku od VPN-a, koji može promeniti svoj IP Address, proxy uvek garantuje isti izlazni Address
 - Automatski prekidač**: ako se VPN prekine, saobraćaj u pregledaču je odmah blokiran
 - IPv6 podrška**: IPv6 povezivanje čak i ako vaša VPN veza to nema omogućeno





- Multihop (dupli VPN)**: sposobnost promene lokacije proxy-ja kako bi se kreirao tunel unutar tunela
 - Vaš saobraćaj prvo prolazi kroz vaš VPN server, a zatim "skače" na drugi Mullvad server.
 - Koristite drugačiju lokalizaciju samo za pregledač.





- Napredno praćenje veze**: praćenje statusa vašeg VPN-a u realnom vremenu, povezanog servera i detekcija curenja DNS-a





- Pristup Mullvad Leta**: privatni pretraživač rezervisan za pretplatnike (iako ga Mullvad ne preporučuje zbog razloga korelacije sa vašim nalogom)



Ova tri proširenja rade zajedno kako bi stvorila koherentan ekosistem zaštite, gde svaki korisnik ima koristi od potpuno istih odbrana bez mogućnosti prilagođavanja koje bi ugrozilo kolektivnu anonimnost.



## Prednosti i nedostaci Mullvad Browser-a



### Pogodnosti





- Izvrsna zaštita privatnosti po defaultu:** Mullvad Browser primenjuje veoma stroga podešavanja privatnosti od samog početka, bez potrebe za ručnom konfiguracijom.





- Bolje performanse od Tor Browser-a:** U nedostatku onion rutiranja, Mullvad Browser je **znatno brži i responzivniji** od Tor Browser-a za klasično pretraživanje interneta.





- Poznata jednostavnost Interface:** Mullvad Browser je zasnovan na Firefox-ovom Interface. Ako ste navikli na Firefox ili čak Tor Browser, nećete se osećati izgubljeno.





- Pouzdana saradnja i revidirani kod:** Mullvad Browser koristi stručnost Tor Project-a, a sav izvorni kod je dostupan za eksterno revidiranje.



### Nedostaci





- Nema anonimnosti na mreži bez VPN-a:** Najvažnija stvar je da **Mullvad Browser sam po sebi ne skriva vaš IP Address** (kao i svi drugi pretraživači, osim Tor Browser-a). Vaš IP Address je kao vaša "poštanska Address" na Internetu: otkriva vašu lokaciju i vašeg ISP-a. Stoga **u velikoj meri zavisi od VPN-a** (virtuelne privatne mreže) da sakrije ove ključne informacije.





- Nema mobilne verzije:** Do danas je Mullvad Browser dostupan samo na PC-ju (Windows, Mac, Linux).





- Nekompatibilno sa određenim navikama:** **stalni privatni režim** znači da ne možete zadržati sesiju od jedne upotrebe do sledeće. Nemoguće je ostati prijavljen na veb nalog iz jedne sesije u drugu.





- Ograničene funkcije:** Da bi se očuvala uniformnost otiska prsta, Mullvad Browser je **onemogućio nekoliko funkcija** prisutnih u Firefox-u i nije namenjen za prilagođavanje.



## Instaliranje Mullvad Browser



Mullvad Browser je dostupan besplatno za Windows, macOS i Linux. Da biste ga instalirali, idite na [zvaničnu Mullvad veb stranicu](https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Zvanična početna stranica Mullvad Browser-a sa istaknutim dugmetom za preuzimanje.*



![MULLVAD BROWSER](assets/fr/03.webp)



*Odaberite svoj operativni sistem na stranici za preuzimanje Mullvad Browser-a.*



Kliknite na dugme **"Download "** koje odgovara vašem operativnom sistemu.



Za Linux, možete birati između različitih formata u zavisnosti od vaše distribucije. Kada se preuzimanje završi:



### Na Windowsu


Pokrenite preuzetu datoteku `.exe` i pratite uputstva za instalaciju.



### Na macOS-u


Otvorite preuzetu datoteku `.dmg` i prevucite aplikaciju Mullvad Browser u vaš folder Applications.



### Na Linuxu


Otpakujte arhivu `.tar.xz` u direktorijum po vašem izboru i pokrenite datoteku `start-mullvad-browser.desktop`.



## Konfiguracija i prva upotreba



Kada prvi put pokrenete Mullvad Browser, videćete Interface vrlo sličan onom u Tor Browser-u. Pregledač je unapred konfigurisan za privatnost i ne zahteva posebne izmene.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Mullvad Browser početna stranica sa ekstenzijama, ikona metle do generate novi identitet i meni aplikacije u gornjem desnom uglu.*



**Važno:** Mullvad Browser ne maskira vašu IP adresu Address po defaultu. Za potpunu zaštitu, toplo preporučujemo korišćenje VPN-a paralelno. Možete koristiti Mullvad VPN ili bilo koju drugu pouzdanu VPN uslugu.



Pregledač takođe uključuje **DNS-over-HTTPS (DoH)** koristeći Mullvad-ovu DNS uslugu: ova tehnologija šifrira vaše DNS zahteve (prevođenje imena sajtova u IP adrese) kako bi sprečila vašeg ISP-a da prati sajtove koje posećujete.



### Postavke bezbednosti



Možete podesiti nivo bezbednosti klikom na **meni aplikacije** (tri horizontalne linije) u gornjem desnom uglu, zatim na **"Podešavanja "**, pa na karticu **"Privatnost i bezbednost "**. Skrolujte dole do odeljka **"Bezbednost "**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Izbor nivoa bezbednosti: strelice pokazuju putanju od menija aplikacije do kartice "Privatnost i bezbednost" do opcija bezbednosti*



Mullvad Browser nudi tri nivoa sigurnosti:





- Normalno** (trenutni podrazumevani nivo): Sve funkcije pregledača i vebsajta su omogućene





- Safer**: Onemogućava često opasne funkcije veb-sajtova, što može dovesti do gubitka funkcionalnosti na nekim veb-sajtovima:
 - JavaScript je onemogućen za sajtove koji nisu HTTPS
 - Neki fontovi i matematički simboli su onemogućeni
 - Zvuk i video (HTML5 mediji) kao i WebGL su "klikni za reprodukciju"





- Najbezbednije**: Dozvoljava samo funkcije veb-sajta potrebne za statične sajtove i osnovne usluge:
 - JavaScript je podrazumevano onemogućen za sve sajtove
 - Neki fontovi, ikone, slike i matematički simboli su onemogućeni.
 - Zvuk i video (HTML5 mediji) kao i WebGL su "klikni za reprodukciju"



### Dugme za novu sesiju



Da biste ponovo pokrenuli sa praznom sesijom bez zatvaranja pregledača, kliknite na ikonu metle ili koristite meni aplikacije > **"Nova sesija "**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Funkcija "Resetuj svoj identitet" za ponovno pokretanje pregledača sa potpuno novom sesijom*



## Svakodnevna upotreba



### Normalna navigacija



Mullvad Browser se ponaša kao klasični pregledač za svakodnevno pretraživanje. Sve web stranice su dostupne kao i obično, uz dodatnu prednost poboljšane zaštite protiv praćenja.



### Upravljanje kolačićima i prijava



Zbog stalnog privatnog režima, moraćete da se ponovo prijavite na svoje naloge svaki put kada se prijavite. Ovo je cena koju plaćate za maksimalnu poverljivost.



### Ekstenzije



Mullvad Browser tehnički omogućava instalaciju dodatnih ekstenzija iz Firefox kataloga, ali **važno je razumeti posledice**. Svaka dodata ekstenzija menja vaš digitalni otisak i razlikuje vas od drugih korisnika Mullvad Browser-a, što je suprotno osnovnom principu pretraživača: da svi korisnici izgledaju identično.



Kako Mullvad objašnjava: *"Ponekad je bolje nemati specifičnu odbranu nego imati jednu. Želeći da povećate privatnost na mreži, instalirate ekstenzije koje vas na kraju čine još vidljivijim."*



Ako ipak odlučite da instalirate ekstenzije, budite svesni da time kreirate jedinstveni otisak koji može biti korišćen za praćenje vašeg kretanja sa sajta na sajt. Za maksimalnu zaštitu, najbolje je držati se tri unapred instalirane ekstenzije, koje su identične za sve korisnike.



## Najbolje prakse sa Mullvad Browser



1. **Uvek koristite VPN: Mullvad Browser ne maskira vašu IP adresu. VPN je neophodan za potpunu anonimnost.



2. **Nemojte prilagođavati pregledač**: Izbegavajte promenu postavki ili dodavanje ekstenzija, jer vas to može učiniti prepoznatljivim.



3. **Koristite dugme za novu sesiju**: Između različitih aktivnosti, koristite funkciju resetovanja da podelite svoje sesije.



4. **Izaberite nivo bezbednosti koji najbolje odgovara vašim potrebama**:




   - Normalno (preporučeno)**: Za svakodnevno pretraživanje. Već nudi odličnu zaštitu uz održavanje funkcionalnosti veb-sajtova. Ovo je najbolji balans za 95% korisnika.
   - Safer**: Ako posećujete nepoznate ili potencijalno opasne sajtove, ili za dodatnu zaštitu na javnim Wi-Fi mrežama. Neki sajtovi mogu nefunkcionisati ispravno.
   - Najsigurnije**: Rezervisano za situacije visokog rizika (istraživačko novinarstvo, osetljive komunikacije, neprijateljska okruženja). Većina modernih sajtova neće raditi, ali to je cena maksimalne sigurnosti.



5. **Redovno proveravajte ažuriranja**: Održavajte svoj pregledač ažuriranim sa najnovijim sigurnosnim zakrpama.



6. **Koristite pretraživače koji poštuju privatnost**: Izaberite DuckDuckGo, Startpage ili Searx umesto Google-a.



7. **Omogući samo HTTPS režim**: U podešavanjima, proveri da je omogućen režim "samo HTTPS" kako bi se forsirale sigurne veze.



8. **NE MENJAJTE napredna podešavanja**: Za razliku od drugih pregledača, Mullvad Browser je dizajniran tako da SVI korisnici imaju potpuno istu konfiguraciju. Menjanje podešavanja u `about:config` ili menjanje uBlock Origin/NoScript podešavanja učinilo bi vas jedinstvenim i potpuno poništilo anonimnost pregledača.



## Preporučena DNS konfiguracija



Mullvad Browser automatski integriše Mullvad DNS-over-HTTPS. Ako koristite Mullvad VPN, ekstenzija će preporučiti da **onemogućite Mullvad DoH** jer je brže koristiti DNS server vašeg VPN servera. Ako ne koristite Mullvad VPN, držite Mullvad DoH omogućenim kako biste izbegli nadgledanje DNS-a od strane vašeg ISP-a.



## Zaključak



Mullvad Browser je odlično rešenje za one koji traže privatnosti naklonjeno pretraživanje interneta bez ograničenja performansi Tor mreže. U kombinaciji sa kvalitetnim VPN-om, nudi snažnu zaštitu protiv praćenja i nadzora na mreži.



Iako ima određena ograničenja (nema mobilnu verziju, nepostojane sesije), Mullvad Browser je vredan alat u arsenalu svakoga ko želi da povrati kontrolu nad svojom digitalnom privatnošću. Njegova jednostavnost korišćenja i podrazumevana konfiguracija čine ga mudrim izborom za korisnike koji su svesni privatnosti, bilo da su početnici ili iskusni.



## Resursi



### Zvanična dokumentacija




- [Official Mullvad Browser website](https://mullvad.net/fr/browser)
- [Stranica za preuzimanje Mullvad pretraživača](https://mullvad.net/en/download/browser)
- [Detaljne tehničke specifikacije](https://mullvad.net/en/browser/Hard-facts)
- [Mullvad Browser Extension](https://mullvad.net/en/help/mullvad-browser-extension)



### Vodiči i objašnjenja




- [Zašto je privatnost važna](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor bez Tor-a: Mullvad Browser koncept](https://mullvad.net/en/browser/tor-without-tor)
- [Kako odabrati pregledač koji poštuje privatnost](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Understanding browser fingerprinting](https://mullvad.net/en/browser/browser-fingerprinting)



### Podrška i pomoć




- [Mullvad Browser Help Center](https://mullvad.net/en/help/tag/mullvad-browser)
- [Prvi koraci ka privatnosti na mreži](https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Resursi zajednice




- [Vodič za Mullvad Browser - Vodiči za privatnost](https://www.privacyguides.org/en/desktop-browsers/)
- [Diskusije zajednice](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)