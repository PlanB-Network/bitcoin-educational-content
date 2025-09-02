---
name: Orion Browser
description: Kako koristiti Orion Browser za zaštitu privatnosti na Mac-u i iPhone-u?
---

![cover](assets/cover.webp)



## Uvod



U kontekstu gde većina pregledača masovno prikuplja naše lične podatke, izbor pregledača koji poštuje privatnost postaje ključan. Chrome dominira sa 65% globalnog tržišta, ali njegov poslovni model se zasniva na eksploataciji vaših podataka o pretraživanju. Safari, iako integrisan u Apple ekosistem, nema napredne funkcije zaštite i ne podržava fleksibilno ekstenzije trećih strana.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Raspodela tržišta web pregledača: Chrome dominira sa preko 65% tržišnog udela, a slede ga Safari, Edge i Firefox*



**Orion Browser** predstavlja se kao inovativna alternativa za korisnike Apple-a. Razvijen od strane Kagi-ja, ovaj pregledač kombinuje brzinu WebKit motora sa filozofijom nulte telemetrije. Za razliku od svojih konkurenata, Orion ne šalje podatke na udaljene servere i prirodno blokira 99,9% reklama i tragača, uključujući YouTube.



Njegova jedinstvena karakteristika? Orion je **jedini WebKit** pregledač koji nativno instalira ekstenzije za Chrome **i** Firefox, nudeći najbolje od oba sveta. Ova kompatibilnost, u kombinaciji sa potrošnjom memorije 2 do 3 puta nižom od drugih pregledača i besprekornom integracijom sa Apple ekosistemom (iCloud, Keychain), čini ga idealnim izborom za korisnike Mac-a i iPhone-a koji brinu o privatnosti.



## Zašto odabrati Orion Browser?



### Ključne prednosti



**Maksimalna zaštita odmah po otvaranju**: Orion blokira 99,9% oglasa (uključujući YouTube) i sve prve i treće strane trackere po defaultu. Njegova tehnologija kombinuje WebKitovu Inteligentnu Prevenciju Praćenja sa EasyPrivacy listama za maksimalnu efikasnost. Jedinstvena karakteristika: Orion blokira skripte za otisak prsta **pre nego što se izvrše**, čineći praćenje doslovno nemogućim - radikalniji pristup od drugih pretraživača koji samo pokušavaju da "maskiraju" podatke.



**Nula proverljive telemetrije**: Orion pristupa privatnosti na radikalan način, sa nultom telemetrijom po dizajnu. Za razliku od drugih pregledača, koji prave stotine mrežnih zahteva pri pokretanju (IP eksponent, otisak pregledača, lične informacije), Orion nikada ne "zove kući". Ova fundamentalna razlika potpuno eliminiše rizik od nenamernog curenja podataka.



**Izuzetne performanse**: Na osnovu optimizovane verzije WebKit-a, Orion je jednak ili čak nadmašuje Safari po brzini na Mac-u. Testovi Speedometer 2.0/2.1 ga dosledno postavljaju na prvo mesto na Apple Silicon procesorima. Blokiranje reklama u izvornom obliku dodatno ubrzava učitavanje stranica za 20 do 40%.



**Univerzalna podrška za ekstenzije**: Velika inovacija, Orion vam omogućava da instalirate ekstenzije iz Chrome Web Store-a **i** Mozilla Add-ons. Podrška za WebExtensions je trenutno eksperimentalna, sa ciljem 100% kompatibilnosti pri beta izdanju. Možete koristiti mnoge popularne ekstenzije kao što su uBlock Origin, Bitwarden, čak i na iPhone-u - što je svetski presedan na iOS-u, iako neke možda neće raditi savršeno.



### Ograničenja kojih treba biti svestan





- Ograničena dostupnost**: Trenutno rezervisano za macOS i iOS/iPadOS. Verzija za Linux dostiže razvojne prekretnice (Prekretnica 2 u 2025. godini), ali javna verzija nije dostupna. Windows i Android nisu u razvoju zbog nedostatka resursa.
- Zatvoreni izvorni kod**: Iako su neki delovi otvorenog koda, Orion ostaje pretežno vlasnički, što je tačka debate u zajednici za privatnost.
- Eksperimentalna proširenja**: Podrška za proširenja je i dalje u beta fazi, sa čestim nekompatibilnostima. Proširenja mogu uticati na performanse, a neka uopšte ne rade.
- WebKit bezbednost**: Za razliku od Chromium-a, WebKit ne nudi tako robusnu izolaciju procesa po sajtu, što može predstavljati bezbednosne rizike u određenim scenarijima.
- Blokiranje testova**: Orion namerno loše prolazi u testovima online oglašavanja (26-35%), jer Kagi smatra da su ovi testovi "fundamentalno pogrešni". Stvarna efikasnost u svakodnevnoj upotrebi je daleko superiornija.



## Instalacija Orion Browser-a



### Na macOS



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*Početna stranica Kagi predstavlja Orion Browser kao "pregledač bez reklama sa potpunom zaštitom privatnosti i univerzalnom podrškom za ekstenzije"*





- Idi na [kagi.com/orion](https://kagi.com/orion/)
- Kliknite na "**Preuzmi Orion za macOS**"



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*Orion Browser stranica za preuzimanje prikazuje dostupnost za macOS i iOS, sa linkovima ka App Store-u*





- Otvorite preuzetu `.dmg` datoteku
- Prevucite Orion aplikaciju u fasciklu Applications
- Prilikom prvog pokretanja, macOS će tražiti da potvrdite otvaranje



**Alternativni Homebrew**:


```bash
brew install --cask orion
```



### Na iPhone/iPad





- Otvorite **App Store**
- Pretraži "**Orion Browser by Kagi**"
- Instalirajte besplatnu aplikaciju (kompatibilna sa iOS 15+)



### Početna konfiguracija



Prilikom prvog pokretanja, Orion vas vodi kroz nekoliko koraka:



**1. Ekran dobrodošlice


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Orion Browser početni ekran ističe ključne karakteristike: brže pretraživanje, nulta telemetrija, blokiranje oglasa i podrška za ekstenzije*



**2. Interface** prilagođavanje


![Options de personnalisation](assets/fr/05.webp)


*Ekran za prilagođavanje vam omogućava da konfigurišete izgled kartica i Interface prema vašim preferencijama*





- Uvoz podataka**: Lako prenesite favorite i lozinke iz Safarija, Chrome-a ili Firefoxa
- ICloud sinhronizacija**: Aktivirajte da pronađete svoje favorite i kartice na svim vašim Apple uređajima



**3. Instalacija na mobilnim uređajima**


![Installation sur iOS](assets/fr/06.webp)


*Ekran za instalaciju na iOS-u prikazuje QR kod za brzo preuzimanje Orion Browser-a iz App Store-a*



**4. Interface dobrodošlica i osnovni alati



![Page d'accueil Orion](assets/fr/07.webp)


*Orion Browser Interface početna stranica: strelica označava tri ključna alata dostupna direktno sa Address trake*



Kada je konfiguracija završena, otkrićete Orionov pojednostavljeni Interface sa **tri osnovna alata** (označena strelicom):





- Štit 🛡️**: Prikazuje Izveštaj o privatnosti sa brojem stavki blokiranih na trenutnoj stranici
- Četkica 🖌️**: Prilagodite prikaz stranice (tema, font, uklonite ometajući Elements)
- Gear ⚙️**: Konfiguriši parametre specifične za veb-sajt (dozvole, blokiranje, itd.)



Ovi alati su uvek dostupni i omogućavaju vam da kontrolišete svoje iskustvo pretraživanja na osnovu sajta.



**Važno**: Orion je besplatan i ne zahteva registraciju ili kreiranje naloga za rad.



![Orion+ dans les préférences](assets/fr/08.webp)


*Ekran za pretplatu Orion+ u postavkama, nudi opcionalnu pretplatu za podršku razvoju*



**Orion+ (opciono)**: Da podrži razvoj projekta, Kagi nudi Orion+ (5$ mesečno, 50$ godišnje, ili 150$ doživotno). Ova dobrovoljna pretplata omogućava:




- Komunicirajte direktno sa razvojnim timom
- Uticati na evoluciju pregledača prema vašim potrebama
- Pristupite Nightly verzijama sa najnovijim eksperimentalnim funkcijama
- Iskoristite prednosti najnovijeg WebKit engine-a
- Dobijte prepoznatljivu značku na forumu za povratne informacije



Orion+ garantuje nezavisnost projekta: "Vaš finansijski doprinos pomaže nam da ostanemo nezavisni i održimo obećanje da postanemo najbolji pregledač za naše korisnike". Upravo ovaj model finansiranja od strane korisnika održava Orion bez reklama i telemetrije.



## Konfiguracija za maksimalnu poverljivost



### Osnovni parametri



Pristupite preferencama putem **Orion → Preferences** (ili ⌘,):



**1. Pretraga - Privatni pretraživač**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Podrazumevana konfiguracija pretraživača: DuckDuckGo je izabran za maksimalnu privatnost*





- Podrazumevani pretraživač**: Izaberite **DuckDuckGo**, **Startpage** ili **Kagi** za optimalnu privatnost (izbegavajte Google/Bing)
- Preporuke pretrage**: Onemogućite ih kako biste sprečili da pritisci tastera budu poslati serverima pretraživača



**2. Privatnost - Opšta** zaštita



![Content Blocker dans les préférences](assets/fr/12.webp)


*Orion podešavanja privatnosti prikazuju Blokator sadržaja sa 119.156 aktivnih pravila, opcije za uklanjanje tragača i prilagođeni korisnički agent*



**Blokator sadržaja aktivan po defaultu**:




- EasyList**: 119k+ pravila za blokiranje oglasa
- EasyPrivacy**: Zaštita protiv praćenja
- Upravljaj listama filtera**: Dodaj dodatne liste (Hagezi preporučeno)



**Opcije privatnosti**:




- Ukloni pratioce iz URL-ova**: "Samo za privatno pretraživanje" čisti kopirane linkove
- Delite izveštaje o padu**: "Nakon traženja odobrenja" poštuje vaš pristanak
- Prilagođeni korisnički agent**: Može se modifikovati da zaobiđe određene blokade



![YouTube avec Privacy Report](assets/fr/10.webp)


*Primer YouTube primer sa Orionom: bez vidljivih reklama i Izveštaj o privatnosti prikazuje mnogo blokiranih Elements*



**3. Postavke veb-sajta - Kontrola po sajtu**



![Website Settings pour YouTube](assets/fr/11.webp)


*Postavke veb-sajta za YouTube prikazuju opcije kompatibilnosti, blokiranje sadržaja i dozvole specifične za sajt*



**Brzi pristup**: Kliknite na zupčanik ⚙️ u Address traci da biste podesili:




- Režim kompatibilnosti**: Rešava probleme sa prikazom obustavljanjem ekstenzija
- Blokatori sadržaja**: Deaktivirajte blokiranje za određeni sajt ako je potrebno
- JavaScript/Kolačići**: Granularna kontrola po sajtu
- Dozvole**: Kamera, mikrofon, lokacija pojedinačno konfigurisane



**4. Napredni Prilagođeni Filteri** (vidi dole)



**Kreiraj prilagođene filtere** (Privatnost → Upravljanje listama filtera → Prilagođeni filteri):



**Pojednostavljena sintaksa** (kompatibilna sa Adblock Plus):




- `reddit.com##.promotedlink`: Sakriva sponzorisane objave na Redditu
- `||ads.example.com^`: Potpuno blokira domen za oglašavanje
- `@@||site-utile.com^`: Kreira izuzetak za sajt



**Savet:** Posetite [FilterLists.com](https://filterlists.com) za hiljade gotovih specijalizovanih lista.



### Preporučene ekstenzije



Orion prirodno podržava ekstenzije za Chrome i Firefox. Instalirajte ih direktno iz zvaničnih prodavnica:



**Osnovne stvari**:




- uBlock Origin**: Dodaje granularnu kontrolu nad ugrađenim blokatorom
- Bitwarden**: Menadžer lozinki otvorenog koda
- ClearURLs**: Briše parametre za praćenje u URL-ovima



**Opcionalno**:




- LocalCDN**: Služi zajedničke biblioteke lokalno
- Cookie AutoDelete**: Automatski briše kolačiće nakon zatvaranja kartica
- NoScript**: Totalna kontrola nad izvršavanjem JavaScript-a (napredni korisnici)



Da instalirate:




- Posetite [chrome.google.com/webstore](https://chrome.google.com/webstore) ili [addons.mozilla.org](https://addons.mozilla.org)
- Kliknite na "Dodaj u Chrome/Firefox"
- Orion će presresti i automatski instalirati ekstenziju



**Upozorenje**: Pošto je podrška za ekstenzije eksperimentalna, mnoge ekstenzije možda neće raditi ispravno ili mogu uticati na performanse. U slučaju problema (sajt više ne radi, usporenost), onemogućite ekstenzije jednu po jednu kako biste identifikovali izvor.



## Svakodnevna upotreba



### Interface i jedinstvene karakteristike




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Orion meni za četkice za prilagođavanje prikaza: veličina fonta, tema (svetla/tamna), deaktivacija lepljivih zaglavlja i uklanjanje ometajućeg Elements*



**Alatka za četkanje: napredna prilagođavanja**



Orionova **četkica** je jedinstvena funkcija koja vam omogućava prilagođavanje prikaza svake veb stranice:



**Opcije teme**:




- Prebacivanje između svetle i tamne teme za svaki sajt
- Automatsko prilagođavanje vašim sistemskim preferencijama



**Tipografska kontrola**:




- Veličina fonta**: Podesite čitljivost pomoću dugmadi A- i A+
- Stil fonta**: Promeni porodicu fonta (podrazumevana ili prilagođena)



**Interface čišćenje**:




- Onemogući lepljive zaglavlja**: Uklanja zaglavlja koja ostaju zalepljena na vrhu prilikom skrolovanja
- Izbriši Elements**: Trajno ukloni dosadne Elements (reklame, iskačuće prozore, banere sa kolačićima)
  - Kliknite na "+ Izbriši" zatim odaberite stavku koju želite sakriti
  - Veoma korisno za sajtove sa upornim reklamama ili vizuelnim praćenjem Elements



**Upornost**: Sva ova podešavanja se čuvaju po domenu i automatski se ponovo primenjuju sledeći put kada posetite.



**Napredno upravljanje karticama**:




- Vertikalne kartice**: Aktivirajte putem trake menija (funkcija Kartice sa strane)
- Kompaktne kartice**: U Podešavanjima → Kartice → Raspored "Kompaktno" za uštedu prostora
- Grupe kartica**: Organizujte svoje sesije po temama
- Više profila**: Kreirajte odvojene identitete putem trake menija (funkcija Profili) sa potpuno izolovanim podacima



**Režim niske potrošnje**: Inspirisan iPhone-om, ovaj režim automatski suspenduje neaktivne kartice nakon 5 minuta i može smanjiti potrošnju energije do 90%. Aktivirajte ga putem Orion-ove trake menija na Mac-u, ili u podešavanjima na iOS-u.



**Ugrađeni alati** (Meni za uređivanje i drugi):




- Izmeni Tekst na Stranici**: privremeno izmeni bilo koji tekst (Izmeni meni)
- Dozvoli Kopiranje i Lepljenje**: Zaobilazi ograničenja kopiranja (Meni za uređivanje)
- Kopiraj Čistu Vezu**: Desni klik na vezu da ukloniš parametre praćenja
- Fokus Mod**: navigacija bez ometanja, preko celog ekrana
- Picture-in-Picture**: Gledajte video zapise u plutajućem prozoru
- Otvorite u Internet arhivi**: Direktan pristup arhiviranim verzijama
- Izveštaj o privatnosti**: Kliknite na štit 🛡️ da vidite stavke blokirane od strane stranice



### Upravljanje privatnim pregledanjem



Orionova privatna navigacija (⌘⇧N) nudi:




- Potpuna izolacija kolačića i sesija
- Automatsko brisanje pri zatvaranju
- Istorija i deaktivacija keša
- Poboljšana zaštita protiv otiska prsta



**Savjet**: Za naprednu kompartimentalizaciju, kreirajte **odvojene profile** putem trake menija (funkcija Profili). Svaki profil se pojavljuje kao zasebna aplikacija u Dock-u, sa sopstvenim podešavanjima, ekstenzijama i potpuno izolovanim podacima.



### Optimizacija performansi i privatnost



Da bi Orion ostao brz i privatan:




- Ekstenzije**: Ograničiti na strogi minimum (može smanjiti performanse)
- Režim niske potrošnje**: Aktivirajte za duge sesije (moguća ušteda od 90%)
- Izveštaj o privatnosti**: Kliknite na štit 🛡️ da biste videli blokade u realnom vremenu
- Vizuelno prilagođavanje**: Koristite 🖌️ četkicu da prilagodite prikaz i uklonite ometajući Elements
- Kopiraj Čistu Vezu**: Desni klik za kopiranje veza bez pratilaca
- Odvojeni profili**: Koristite posvećene profile za razdvajanje svojih aktivnosti
- Postavke veb-sajta**: Kliknite na zupčanik ⚙️ da prilagodite dozvole po sajtu
- Redovno čišćenje**: Očistite keš putem Orion → Očisti podatke pretraživanja



## Poređenje sa alternativama



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Versus Safari**: Orion nudi superiornu zaštitu sa svojim naprednim blokatorom i podrškom za ekstenzije, dok održava WebKit performanse.



**Versus Chrome**: nenadmašena privatnost bez kompromisa po pitanju kompatibilnosti, zahvaljujući podršci za Chrome ekstenzije.



**Versus Firefox**: Brži na Mac-u, Interface intuitivniji, ali manje granularna kontrola i nije otvorenog koda.



**Versus Brave**: Slična filozofija, ali Orion izbegava kripto/BAT kontroverze i nudi bolju integraciju sa Apple-om.



## Preporučeni slučajevi upotrebe



**Idealno za**:




- Korisnici Apple-a koji traže više privatnosti od Safarija
- Ljudi koji žele da blokiraju sve reklame (uključujući YouTube) bez ekstenzija
- Programeri kojima su potrebni WebKit devtools sa integrisanom zaštitom privatnosti
- Korisnici iPhone-a koji žele desktop ekstenzije na mobilnom (jedinstvena inovacija)
- Profesionalci koji treba da razdvoje svoje aktivnosti (višestruki profili)
- Korisnici mobilnih uređaja koji traže bolje upravljanje baterijom (Režim niske potrošnje)



**Izbegavajte ako**:




- Uglavnom koristite Windows/Linux (verzija nije dostupna)
- Potpuni open-source je ključan za vaš model pretnji
- Oslanjate se na određene ekstenzije koje možda neće raditi
- Treba vam sinhronizacija između platformi izvan Apple ekosistema
- Vi preferirate provereno, stabilno rešenje (stalni beta status od 2021)



## Tačke pažnje i bezbednosti



### Jedinstvene sigurnosne karakteristike



**Revolucionarna zaštita protiv otiska prsta**: Orion je jedini pregledač koji potpuno blokira izvršavanje skripti za otisak prsta pre nego što mogu da skeniraju vaš sistem. Ovaj pristup "nema pokretanja skripti = nema mogućeg otiska prsta" nadmašuje tradicionalne metode maskiranja koje koriste drugi pregledači.



**Transparent Whitelist**: Orion održava malu javnu listu sajtova (browserbench.org, wizzair.com) gde je blokiranje automatski onemogućeno kako bi se izbegle neispravnosti. Ova transparentnost omogućava korisnicima da tačno razumeju kada i zašto je blokiranje ublaženo.



**Nerevidirane ekstenzije**: Podrška za ekstenzije za Chrome/Firefox uvodi dodatne rizike, jer ove ekstenzije nisu dizajnirane za WebKit i nisu specifično revidirane za ovo okruženje.



### Održavanje i ažuriranja





- Automatska ažuriranja**: Orion se automatski ažurira na macOS putem Sparkle
- Praćenje ranjivosti**: Redovno proveravajte beleške o izdanju za sigurnosne zakrpe
- Prijavljivanje grešaka**: Koristite [orionfeedback.org](https://orionfeedback.org) za prijavljivanje problema




## Zaključak



Orion Browser predstavlja značajan korak napred za privatnost na macOS i iOS. Njegov pristup bez telemetrije, u kombinaciji sa ultra-efikasnim native blokatorom i jedinstvenom podrškom za univerzalne ekstenzije, čini ga odličnim izborom za korisnike Apple-a koji su svesni važnosti privatnosti.



**Važno**: Orion ostaje u trajnoj beta verziji od 2021. godine, sa ograničenjima kompatibilnosti ekstenzija i inherentnim rizicima WebKit-a. Procijenite ove kompromise u skladu sa vašim modelom pretnji.



Za svakodnevnu upotrebu na Mac-u ili iPhone-u, verovatno je najbolji kompromis između poverljivosti, performansi i jednostavnosti korišćenja dostupan u Apple ekosistemu, pod uslovom da prihvatite njegova ograničenja.



Zapamtite: zaštita vaše privatnosti ne zavisi samo od vašeg pregledača. Kombinujte Orion sa najboljim praksama (jake lozinke, 2FA, VPN ako je potrebno) za optimalnu online sigurnost.



## Resursi i podrška



### Zvanična dokumentacija




- Zvanična veb stranica**: [kagi.com/orion](https://kagi.com/orion/)
- Full FAQ**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- Zajednički forum**: [community.kagi.com](https://community.kagi.com)
- Praćenje grešaka**: [orionfeedback.org](https://orionfeedback.org)
- GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Komponente otvorenog koda
- Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - Vesti i ažuriranja



### Preporučeni verifikacioni testovi



Nakon konfiguracije, testirajte vašu postavku:




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Test otiska prsta
- [DNS Leak Test](https://www.dnsleaktest.com/) - Proverite curenje DNS-a
- [BrowserLeaks](https://browserleaks.com/) - Kompletan skup testova privatnosti



### Alternative na Plan ₿ Network


Za maksimalnu zaštitu, pogledajte naše druge vodiče:




- [Firefox hardened](https://planb.network/tutorials/computer-security/firefox) - Napredna konfiguracija za više platformi
- [Tor Browser](https://planb.network/tutorials/computer-security/tor-browser) - Potpuna mrežna anonimnost
- [Mullvad Browser](https://planb.network/tutorials/computer-security/mullvad-browser) - Maksimalna zaštita od otiska prsta



Ako želite da saznate više o istoriji i funkcionisanju pregledača, kao i o glavnim digitalnim objektima u vašem svakodnevnom životu, pozivam vas da otkrijete naš novi besplatni kurs obuke SCU 202, dostupan na Plan ₿ Network:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1