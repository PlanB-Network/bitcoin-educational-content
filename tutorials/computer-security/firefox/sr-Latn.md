---
name: Firefox
description: Kako konfigurisati Firefox da zaštiti vašu privatnost?
---

![cover](assets/cover.webp)



## Uvod



Svi provodimo sate na internetu, često ne shvatajući šta naš pretraživač otkriva o nama. Svaki klik, svaka pretraga, svaka poseta sajtu hrani ogromnu industriju prikupljanja ličnih podataka.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Udeo na tržištu web pregledača: Chrome dominira sa 65% tržišta, praćen Safari i Edge. Izvor: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Kao što ovaj grafikon pokazuje, Google Chrome masivno dominira, sa preko 65% globalne upotrebe. Ova hegemonija znači da većina korisnika Interneta poverava svoje podatke o pretraživanju Google-u, kompaniji čiji poslovni model se zasniva na ciljnom oglašavanju. Firefox, sa samo 3% tržišta, predstavlja alternativu koju razvija Mozilla, neprofitna organizacija bez komercijalnog interesa za eksploataciju vaših podataka.



Ali odabir Firefoxa je samo prvi korak. Podrazumevano, čak i Firefox zahteva prilagođavanja kako bi se maksimizirala vaša zaštita. Ovaj vodič vas vodi korak po korak, od najjednostavnijih do najnaprednijih, kako biste transformisali Firefox u pravi štit protiv praćenja, a pritom očuvali prijatno iskustvo pretraživanja.



### Zašto Firefox?





- Besplatan i otvoren izvor** (Gecko engine): proverljiv, transparentan kod
- Neprofitna organizacija**: Mozilla Foundation, misija od opšteg interesa
- Ugrađene izvorne zaštite**: Poboljšana zaštita praćenja (ETP), Potpuna zaštita kolačića (TCP), Particionisanje stanja, Samo HTTPS režim, DNS preko HTTPS (DoH)
- Napredna prilagođavanja**: za razliku od Chrome-a, Firefox vam omogućava da detaljno modifikujete njegovo ponašanje



### Važni principi pre nego što počnete





- Nema univerzalnog recepta**: što više modifikujete, to više rizikujete da se istaknete (otisci prstiju). Cilj je biti bolje zaštićen bez isticanja iz mase.
- Korak-po-korak napredak**: Promenite podešavanje, testirajte vaše uobičajene sajtove, zatim nastavite. Nema potrebe da menjate sve odjednom.
- Lični balans**: Pronađite SVOJ kompromis između privatnosti i jednostavnosti korišćenja.



## Brza instalacija



![Téléchargement Firefox](assets/fr/02.webp)



**Official download:** Go to [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). On this page, select your operating system (Windows, macOS, Linux) to access the appropriate download page with specific installation instructions.





- Windows**: preuzmite `.exe` instalacioni program, dvaput kliknite i pratite čarobnjak za instalaciju
- macOS**: preuzmite `.dmg` datoteku, otvorite je i prevucite Firefox u Applications fasciklu
- Linux**: nekoliko opcija dostupno - paket `.deb`/`.rpm`, Flatpak (Flathub), Snap, ili putem upravitelja paketa (apt, dnf, pacman). Preferirajte zvanične Mozilla izvore.



**Savet:** Kada instalirate, proverite ažuriranja putem Pomoć → **O Firefoxu** (važno za sigurnosne zakrpe).



![Configuration initiale Firefox](assets/fr/03.webp)


*Prvi ekran prilikom pokretanja Firefoxa: postavite Firefox kao vaš podrazumevani pregledač, dodajte ga u prečice, zatim kliknite na "Sačuvaj i nastavi" *



![Création compte Firefox](assets/fr/04.webp)


*Opcioni korak: kreirajte ili se prijavite na Firefox nalog. Možete preskočiti ovaj korak klikom na "Ne sada" u donjem desnom uglu*



![Page d'accueil Firefox](assets/fr/05.webp)


*Firefox početni ekran nakon što je konfiguracija završena. Obratite pažnju na ☰ meni u gornjem desnom uglu, koji omogućava pristup Podešavanjima i Ekstenzijama za prilagođavanje Firefox-a*



## Zaštite već aktivirane po defaultu (umirujuće)





- Izolacija sajtova (Fission)**: u progresivnom uvođenju. Ova funkcija pokreće svaki sajt u zasebnom procesu kako bi sprečila da jedna zlonamerna kartica pristupi podacima druge. Proverite njen status putem `about:support` (pretražite "Fission"). Ako nije omogućena, možete je ručno aktivirati u `about:config` sa `fission.autostart = true`.
- Total Cookie Protection (TCP)**: aktivna po podrazumevanoj vrednosti. Kolačići i druge memorije su ograničeni na sajt prve strane (jedna "tegla" po sajtu), što neutralizuje praćenje između sajtova. Privremeni izuzeci se prave putem Storage Access API kada je to potrebno (integrisani dugmići za prijavu).
- Zaštita od praćenja preusmeravanja/odbijanja**: Firefox automatski detektuje i čisti kolačiće koje ostavljaju sajtovi za preusmeravanje (linkovi koji vas preusmeravaju preko tragača pre odredišta), smanjujući ovaj kanal praćenja bez ikakve vaše akcije.



## Nivo 1 - Osnovno (≤ 10 minuta)



Cilj: veliki dobici u privatnosti bez narušavanja weba. Za 90% korisnika.



Da biste pristupili podešavanjima, kliknite na meni ☰ u gornjem desnom uglu, zatim **"Settings "**:



![Paramètres généraux](assets/fr/07.webp)


*Firefox stranica sa podešavanjima - kartica "Opšte". Ovde podešavate većinu opcija privatnosti*



**Praćenje zaštite (ETP)**




- Prebaci **ETP** na **Strict**. Blokiraš više tragača (kolačići između sajtova, otisak prsta, kriptokopanje, društveni widgeti...).
- Ako sajt ne radi (video, dugme za prijavu...), deaktivirajte zaštitu samo za taj sajt putem 🛡️ štita, zatim osvežite karticu.



Evo su različiti nivoi bezbednosti ETP-a:




- Standard** (uravnotežen, maksimalna kompatibilnost)
  - Blokira: društvene trackere, kolačiće između sajtova (svi prozori), sadržaj za praćenje u privatnom pretraživanju, rudare kriptovaluta, detektore otiska prsta.
  - Uključuje **Total Cookie Protection** (TCP): jedna tegla po sajtu.
- Strogo** (preporučeno za poverljivost)
  - Takođe blokira sadržaj za praćenje u svim prozorima + poznato i sumnjivo otiskivanje prstiju.
  - Možda će pokvariti neke sajtove; koristite 🛡️ štit za lokalni izuzetak.
- Prilagođeno** (napredno)
  - Fino podešavanje: kolačići, praćenje sadržaja, maloletnici, otisak prsta (poznato/osumnjičeno).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Kolačići i podaci sa sajta




- Omogući **"Brisanje kolačića i podataka sa sajta pri zatvaranju"** da bi se svaki put ponovo pokrenulo čisto.
- Dodajte **Izuzetke** za 2-3 ključna sajta po želji (e-mail, banka).


**Automatski unos podataka, sugestije i početna stranica**




- Deaktivirajte **automatsko popunjavanje** (ID-ovi, adrese, kartice). Umesto toga koristite menadžer lozinki.
- Pretraga**: deaktiviraj **"Prikaži predloge pretrage "**.
- Address traka**: izrezati **"Sponzorisani predlozi "** i **"Kontekstualni predlozi "**.
- Početna**: onemogući **Pocket** i **sponzorisani sadržaj**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Samo HTTPS**




- Aktiviraj **"HTTPS režim samo u svim prozorima "**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Telemetrija i merenje oglašavanja




- U "Prikupljanju podataka od strane Firefox-a", **opozovite izbor svega**.
- Deaktiviraj **"Mere za oglašavanje koje poštuju privatnost"** (PPA).
- Sigurno pregledanje**: držite ga omogućenim (preporučeno). Firefox proverava sajtove u odnosu na liste pretnji putem heširanih upita i lokalnih provera, štiteći od fišinga i malvera uz minimalan uticaj na privatnost.



**Global Privacy Control (opciono)**




- Aktivirajte **GPC** da signalizirate vaše odbijanje prodaje/deljenja podataka.



**Pretraživač




- Prebacite se na **DuckDuckGo**, **Startpage**, **Qwant** ili **Brave Search** (Podešavanja → Pretraga).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Privatna navigacija**




- Privatni prozori (Ctrl/Cmd+Shift+P) za jednokratne sesije (pokloni, sekundarni nalozi...). Izbegavajte "uvek privatni" režim: ekstenzije mogu biti neaktivne, a izuzeci za kolačiće manje korisni.



**Osnovne ekstenzije** (instaliraj iz zvaničnog kataloga)




- uBlock Origin**: blokira oglase i trenutno praćenje, lagan.
- Privacy Badger**: uči da blokira ono što vas prati; šalje Do Not Track / GPC.
- ClearURLs** (opciono): Firefox (ETP Strict) i uBO već čiste mnogo; zadržite ga ako i dalje vidite "prljave" URL-ove (utm, fbclid).
- Firefox Multi-Account Containers**: **izoluje kolačiće/sesije i skladište po kontejneru; paralelni multi-nalozi; manje praćenja između sajtova**. Zvanično proširenje: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Lozinke i 2FA**




- Koristite posvećen menadžer lozinki** (Bitwarden, KeePassXC). **Izbegavajte** čuvanje lozinki u pregledaču. **Omogućite 2FA** gde god je moguće.



## Nivo 2 - Ojačano (Kompartmanizacija i Mreža)



Cilj: podeliti aktivnosti i smanjiti curenje mreže.



**DNS preko HTTPS (DoH)**




- Podrazumevani status**: Automatski aktiviran u nekim regionima (SAD, Kanada, Rusija, Ukrajina). Drugde je potrebna ručna aktivacija.
- Konfiguracija**: Postavke → Opšte → Mrežna podešavanja → **Omogući DoH** → **Cloudflare** ili **Quad9** → **Maksimalna zaštita**.
- Maksimalna zaštita = samo TRR** (bez povratka na sistemski DNS). Ako korporativna/hotelska mreža blokira, prebacite se nazad na **Standard** ili onemogućite DoH.
- Redundancy**: Ako već koristite pouzdan VPN sa sopstvenim sigurnim DNS-om, DoH može biti suvišan.
- Test verifikacije**: `https://www.dnsleaktest.com/` treba da prikazuje samo izabranog DoH provajdera.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Kompartmenalizacija sa kontejnerima i profilima




- Multi-Account Containers**: kreirajte prostore (Lični, Posao, Finansije, Društvene mreže, Kupovina, Privremeno). Konfigurišite **"Uvek otvori u ovom kontejneru"** za vaše redovne sajtove. Zvanično proširenje: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Zašto ih koristiti?
  - Snažna izolacija** kolačića/sesija/skladišta po prostoru.
  - Manje praćenja između sajtova**: ograničite gigante (Facebook, Google).
  - Istovremeni multi-nalozi** na istoj usluzi.
  - Manji rizik od CSRF/XSS** između segmentiranih identiteta.
  - Savet: najmanje, posvećeni kontejneri za Društvene mreže/Google, Posao, Finansije.
- Facebook Container** (opciono): pojednostavljena verzija posvećena FB/Instagramu.
- Odvojeni profili**: putem `about:profiles` (glavni profil, minimalni "ultra-sigurni" profil, test profil). Potpuna podela podataka i ekstenzija.



**Napredna proširenja** (da se rezerviše)




- Cookie AutoDelete**: briše kolačiće sajta čim se kartica zatvori (korisno ako je Firefox dugo otvoren).
- LocalCDN**: služi trenutne biblioteke lokalno (smanjuje pozive ka Google/Microsoft). Delimična kompatibilnost.



**Mobilni (Android)**




- Firefox Android + uBlock Origin**: slična zaštita u pokretu.



## Nivo 3 - Ekspert (o:config & Arkenfox)



Cilj: napredno očvršćavanje sa prihvaćenim kompromisima. Preporučeno na **odvojenom profilu**.



Izaberite samo jedan od sledeća dva pristupa:



**Pristup A - Ručne izmene**: Nekoliko ciljanih prilagođavanja putem `about:config` (jednostavnija, preciznija kontrola)


**Pristup B - Arkenfox user.js**: Potpuna automatska konfiguracija (složenije, maksimalna zaštita)



➡️ **Arkenfox već uključuje SVE promene u about:config navedene ispod** + stotine drugih. Ako izaberete Arkenfox, ignorišite odeljak about:config.



### Pristup A: Ručne izmene putem about:config



Ukucajte `about:config` u Address traku → Prihvatite rizik.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Otpornost na otiske prstiju (nasleđeno iz Tor Browser-a)


```text
privacy.resistFingerprinting = true
```


Efekti: UTC vremenska zona, **letterboxing** (standardne veličine prozora), standardizovani User-Agent/politike, ograničenja za Canvas/WebGL/AudioContext. Više uniformnosti, ali nekoliko "čudnosti" (pomereno vreme, ponekad malo engleskog).





- Onemogući WebRTC (izbegava curenje IP adrese; kvari Web visio)


```text
media.peerconnection.enabled = false
```





- Referer plus kompatibilan (podrazumevano)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Stroga opcija (može prekinuti plaćanja/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Ograničavanje brbljivih API-ja i spekulacija


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Zlatno pravilo: ako se nešto pokvari, vratite se na poslednju promenu.



### Pristup B: Arkenfox user.js (Potpuno automatizovana konfiguracija)



Projekat **Arkenfox** obezbeđuje `user.js` datoteku koju održava zajednica i koja automatski primenjuje stotine Firefox podešavanja usmerenih na privatnost i bezbednost. Nakon ponovnog pokretanja, Firefox čita ovu datoteku iz vašeg profila i primenjuje ova podešavanja.





- Koja je poenta? Počnite od **dosledne ojačane osnove** bez "kliktanja svuda"; smanjite previd; uštedite vreme.
- Šta se menja (primeri): telemetrija smanjena, kolačići/keš/referer/HTTPS ojačani, **RFP** + letterboxing, **WebRTC onemogućen**, DoH/TLS podešavanja, ograničeni pričljivi API-ji.
- Kada ga koristiti: ako želite da Firefox bude pojačan za 10 minuta i prihvatate nekoliko izuzetaka (DRM/streaming, Web visio, SSO/plaćanja).
- Prednosti: brzo, dosledno, **ažurirano** (usklađeno sa ESR), veoma dobro **dokumentovano** (wiki + komentari), **prilagodljivo** putem nadjačavanja.
- Ograničenja: kompatibilnost (neke web aplikacije), udobnost (UTC, veličine prozora), i podsetnik: **nije Tor** (nema mrežne anonimnosti).



Instalacija (idealno na **posvećenom profilu**)


1. Sačuvaj profil/omiljene i navedi svoje sajtove sa izuzecima za kolačiće.


2. Preuzmite `user.js` sa `https://github.com/arkenfox/user.js` (ESR/stabilna verzija).


3. Pronađite svoj profilni folder putem `about:profiles`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4. Zatvorite Firefox i premestite `user.js` u koren profilnog foldera.


5. Ponovo pokreni; prilagodi putem `about:config` ili datoteke za nadjačavanje.



Ažuriranja




- Pratite Arkenfox izdanja (usklađena sa ESR), zamenite `user.js`, ponovo pokrenite Firefox; pročitajte beleške o izdanju.



**Prilagođavanje putem nadjačavanja**



Arkenfox je namerno restriktivan po podrazumevanim postavkama. Da biste prilagodili određene postavke svojim potrebama (strimovanje, visio, specifični sajtovi), možete kreirati fajl `user-overrides.js` u istom folderu kao `user.js`. Ovaj fajl vam omogućava da "pregazite" određene Arkenfox preferencije bez modifikovanja glavnog fajla.



Kreirajte `user-overrides.js` i dodajte svoje prilagođavanja:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



Najbolje prakse




- Koristite poseban profil **"Arkenfox"** i zadržite "normalan" profil za udobnost.
- Minimizirajte ekstenzije (uBlock Origin je OK) kako biste ograničili površinu napada i jedinstvenost.
- Dodajte izuzetke po sajtovima (štit 🛡️, uBO, NoScript ako se koristi) kada je potrebno.
- Testiraj nakon svake promene: WebRTC/DNS curenja, Cover Your Tracks, CreepJS.



## Najbolje prakse





- Ažuriranja**: Firefox i ekstenzije su ažurirane.
- Proširenja**: razumna i pouzdana; pazite na "sumnjiva" iskupljenja.
- Preuzimanja**: oprez; testirajte osetljive datoteke na VirusTotal.
- Lozinke**: **posvećeni menadžer** (Bitwarden, KeePassXC); **2FA** omogućeno; izbegavati čuvanje u pregledaču.
- Higijena**: ograničiti Google/Facebook na kontejnere; redovno zatvarati/otvarati da se "resetuje" kontekst.



## Ograničenja i alternative





- Ojačani pregledač ≠ anonimnost na mreži: bez **VPN-a**, vaša IP adresa ostaje vidljiva; čak i sa njim, korelacija je i dalje moguća.
- Previše modifikovanja može vas učiniti **jedinstvenim**. **RFP** standardizuje; alati za randomizaciju (npr. Chameleon) mogu... izdvojiti vas. Testirajte, uporedite, prilagodite.
- Alternative/dopune:
 - Tor Browser: mreža anonimnosti putem Tor-a; sporije. Pogledajte naš kompletan vodič za instalaciju i konfiguraciju**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad Browser: "Tor bez Tor-a", za kombinovanje sa VPN-om; standardizovan otisak. Saznajte kako da ga instalirate u našem posvećenom vodiču**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Preporučene kombinacije: Firefox (Nivo 2) + VPN za svakodnevnu upotrebu; Tor/Mullvad za osetljive aktivnosti; odvojeni profili za kompartmenalizaciju.



## Zaključak



Prateći ovaj vodič korak po korak, pretvorili ste Firefox u pravi bedem protiv digitalnog nadzora. Od osnovnih podešavanja Nivoa 1 do naprednih Arkenfox konfiguracija, svaka promena jača vašu privatnost bez ugrožavanja vašeg iskustva pretraživanja.



**Vaša privatnost je sada bolje zaštićena**: blokirani su tragači oglasa, kolačići su podeljeni, IP Address curenja neutralizovana, telemetrija onemogućena. Firefox više nije samo pretraživač, već alat za digitalni otpor prilagođen vašim potrebama.



**Zapamtite: poverljivost nikada nije zagarantovana. Redovno testirajte svoju zaštitu, ažurirajte postavke i ne oklevajte da prilagodite svoju konfiguraciju kako se vaše navike menjaju. Vaša anonimnost na mreži zavisi koliko od vaših alata, toliko i od vaših praksi.



## Resursi



### Plan ₿ Network




- SCU 202 - Poboljšanje vaše lične digitalne bezbednosti: Da biste saznali više o konceptima digitalne bezbednosti obrađenim u ovom vodiču**



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla dokumentacija




- [Važna zaštita od praćenja](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Zvanični vodič za važnu zaštitu od praćenja
- [State Partitioning](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Tehnička dokumentacija o particionisanju stanja
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): Kompletna referenca o veb bezbednosti



### Arkenfox




- [Viki i vodič za instalaciju](https://github.com/arkenfox/user.js/wiki): Kompletna dokumentacija projekta Arkenfox
- [Depozit i izdanja](https://github.com/arkenfox/user.js): Preuzmite user.js datoteku i pratite ažuriranja



### Vodiči i zajednice




- [PrivacyGuides - Desktop browsers](https://www.privacyguides.org/en/desktop-browsers/): Preporuke i poređenja pregledača
- Reddit**: r/firefox, r/privacy za povratne informacije i podršku
- PrivacyGuides forum**: in-depth technical discussions



### Alati za testiranje




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): Digitalno otiskivanje prstiju i efikasnost protiv praćenja
- [Test curenja DNS-a](https://www.dnsleaktest.com/): Test curenja DNS-a i efikasnost DoH-a
- [BrowserLeaks](https://browserleaks.com/): Kompletan testni paket (WebRTC, Canvas, Fontovi, itd.)
- [BadSSL](https://badssl.com/): SSL/TLS testovi validacije sertifikata
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Napredna analiza 50+ vektora otiska prsta
- [Test Cloudflare DNS](https://1.1.1.1/help): Provera da li Cloudflare DoH radi ispravno
