---
name: GrapheneOS

description: Grafen OS vodič
---

> [GrapheneOS](https://grapheneos.org/) je mobilni operativni sistem fokusiran na privatnost i sigurnost sa kompatibilnošću za Android aplikacije, razvijen kao neprofitni open source projekat.

GrapheneOS, originally founded in 2014 as 'CopperheadOS' is based on the traditional Android Code (AOSP), but with many changes and improvements aimed at improving user privacy and security. GrapheneOS puts the user in control of their phone, not the big tech companies.


### Rezime:



- Uvod
- Priprema
- Instaliraj
- Alternativne aplikacije
- Nedostaci
- Korisne informacije


Vodič na https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md


## Zašto koristiti GrapheneOS?


Moderni telefoni su uređaji za praćenje i prikupljanje podataka u vrednosti od $500-$1000. Svaki aspekt našeg života prolazi kroz njih, i nažalost, veliki deo tih podataka se deli sa trećim stranama na neki način.

GrapheneOS je napravljen specifično da smanji deljenje podataka i poboljša bezbednost vašeg uređaja od potencijalnih vektora napada. Ne postoji nešto kao GrapheneOS nalog. Nije vam potreban da biste preuzeli aplikacije ili komunicirali sa OS-om. Jednostavno rečeno, vi niste proizvod.


GrapheneOS pruža dodatnu sigurnost vašem Android iskustvu kroz neke jednostavne osnovne principe.


1. **Smanjenje površine napada** - Uklonite nepotreban kod (ili bloatware).

2. **Prevencija izloženosti ranjivostima** - Omogućite korisniku dovoljno granularnosti da izabere kompromise sa kojima je zadovoljan.

3. **Sandbox containment** - GrapheneOS dodatno učvršćuje postojeće Android sandbox okruženje, dodatno ograničavajući sposobnost svake aplikacije da komunicira sa ostatkom vašeg telefona.


Saznajte više o tehničkim detaljima skupa funkcija GrapheneOS [ovde](https://grapheneos.org/features).


### Olakšavanje tranzicije


Ako ste godinama bili ukorenjeni u ekosistem Google-a ili Apple-a, pomisao da preko noći izgubite svu tu pogodnost može biti zastrašujuća. Ali uz pažljivo razmotrene odluke o instalaciji aplikacija (o čemu će biti reči kasnije), veliki deo ove očekivane teškoće može biti smanjen ili uklonjen.


Koliko god da alternative postaju dobre, pomisao na takvu promenu i dalje može biti odbojna. Ako se nađete u ovoj situaciji, moj najbolji savet je da koristite svoj novi GrapheneOS uređaj zajedno sa postojećim telefonom neko vreme. Odatle možete polako smanjivati upotrebu 2-3 aplikacije nedeljno dok ne dođete do toga da koristite samo svoj GrapheneOS uređaj.


Ako se odlučiš za ovaj pristup, budi strog prema sebi i prekini oslanjanje na nadzirane alternative što je brže moguće. Mi ljudi smo lenji i često biramo put najmanjeg otpora. Seti se zašto si uopšte napravio promenu.


**Umesto da plaćate svojim ličnim podacima, odlučili ste da plaćate svojim vremenom, a ponekad i svojim Hard zarađenim novcem (u zavisnosti od alternativnih aplikacija koje instalirate).**


## Početak


GrapheneOS je trenutno u proizvodnji samo za _(prilično ironično)_ [Google Pixel](https://grapheneos.org/faq#supported-devices) liniju telefona. Ovo nije bez dobrog razloga. Pixel nudi najbolju hardversku sigurnost koja dopunjuje rad na očvršćavanju OS-a. Ovo uključuje stvari kao što su specifične izolacije komponenti i verifikovano pokretanje.


### Odabir uređaja


Kada birate Pixel na koji želite instalirati GrapheneOS, osigurajte da proverite koliko dugo će uređaj nastaviti da prima podrazumevane [bezbednosne ažuriranja](https://support.google.com/pixelphone/answer/4457705?hl=en#zippy=%2Cpixel-xl-a-a-g-a-g).


U vreme pisanja, Pixel 6a je najjeftiniji dostupni model sa dobrom dugoročnom podrškom, garantovanom do jula 2027. Ako se odlučite za ovaj model, otključavanje OEM-a neće raditi sa verzijom fabričkog OS-a. Potrebno je da ga ažurirate na izdanje iz juna 2022. ili kasnije putem ažuriranja preko mreže. Nakon što ga ažurirate, takođe ćete morati da vratite uređaj na fabrička podešavanja da biste popravili otključavanje OEM-a. Svi ostali modeli koji su otključani od strane operatera biće spremni za GrapheneOS odmah iz kutije.


Kada birate uređaj, takođe ćete želeti da osigurate da kupite otključanu verziju. Određeni operateri kao što je Verizon isporučuju svoje jedinice sa zaključanim bootloader-om, što potpuno sprečava sledeći proces.


### Instaliranje GrapheneOS-a


GrapheneOS [web installer](https://grapheneos.org/install/web) čini ceo proces jednostavnim, i može ga završiti bilo ko za manje od 10 minuta.

Sledeća uputstva su skraćena verzija preuzeta sa gornjeg linka.


Sve što vam treba pri ruci je:



- Piksel
- USB kabl za povezivanje telefona sa računarom
- Računar za pokretanje veb pregledača (bilo koji pregledač zasnovan na Chromium-u: Chrome, Edge, Brave, itd.)


Hajde da zaronimo u to:


1. Prvi korak je da odete na **Podešavanja** > **O telefonu** i više puta dodirnete broj verzije dok ne vidite da je **'Režim za programere'** aktiviran.

2. Zatim idite na **Podešavanja** > **Sistem** > **Opcije za programere** i omogućite **'OEM otključavanje'**.

3. Sada ponovo pokrenite uređaj i držite dugme za smanjenje jačine zvuka dok se telefon ponovo uključuje.

4. Povežite telefon sa svojim laptopom i ako se zatraži autorizacija, dozvolite povezivanje.

5. Na stranici web instalatera, kliknite na 'Otključaj bootloader'.

6. Videćete da se opcije telefona menjaju. Koristite dugme za jačinu zvuka da promenite izbor na `otključaj` i koristite dugme za napajanje da prihvatite.

7. Zatim kliknite na preuzimanje izdanja na stranici web instalatera.

8. Kada se preuzimanje završi, pređite na sledeći korak i kliknite na 'Flash release'. Ovo će trajati minut ili dva i ne morate uopšte da dirate telefon.

9. Na kraju, pređite na sledeći korak veb instalatera i kliknite na **Lock Bootloader**. Moraćete da promenite izbor i potvrdite pomoću dugmeta za napajanje na isti način kao što ste to uradili ranije u procesu.

10. Kada vidite reč `Start`, potvrdite to dugmetom za napajanje i uređaj će se pokrenuti u vaš novi operativni sistem bez Google-a.


![image](assets/2.webp)

Ekran za pokretanje GrapheneOS-a



_Nakon inicijalnog pokretanja i podešavanja, dobra je praksa onemogućiti OEM otključavanje u Podešavanja > Sistem > Opcije za programere._


_Takođe možete razmotriti dodatni, opcioni ali preporučeni korak verifikacije instalacije putem Auditor aplikacije. Biće vam potreban poseban Android telefon sa instaliranom aplikacijom da biste završili ovaj korak. Uputstva za ovo možete pronaći [ovde](https://attestation.app/tutorial)._



![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Video koji detaljno prikazuje jednostavne korake navedene iznad



Ako ti jednostavni koraci deluju kao previše, možete razmisliti o kupovini Pixel telefona sa GrapheneOS softverom [pre-instaliranim](https://ronindojo.io/en/roninmobile). Samo budite svesni da time ukazujete malu količinu poverenja dobavljaču.


### Pre Installed Apps


Sada kada ste postavili, možda ćete primetiti koliko GrapheneOS izgleda osnovno pri prvoj instalaciji. Podrazumevano ćete imati instalirane ove aplikacije:


![image](assets/3.webp)


Podrazumevane aplikacije


Jedina dva sa kojima možda niste upoznati su 'Auditor' i 'Vanadium'.



- [Auditor aplikacija](https://play.google.com/store/apps/details?id=app.attestation.auditor) koristi sigurnosne funkcije zasnovane na hardveru za verifikaciju identiteta uređaja zajedno sa autentičnošću i integritetom operativnog sistema. Ona će proveriti da li uređaj koristi fabrički operativni sistem sa zaključanim bootloader-om i da li nije došlo do neovlašćenog menjanja operativnog sistema.
- [Vanadium](https://github.com/GrapheneOS/Vanadium) je varijanta Chromium veb pregledača sa pojačanom privatnošću i sigurnošću.


## Prilagođavanje


Postavke telefona su lična stvar, ali evo nekih od prvih stavki koje menjam kada instaliram GrapheneOS da bih se osećao više kao kod kuće.


### Postavljanje pozadine i ažuriranje teme


Idite na Podešavanja > Pozadina i stil. Odavde:



- Ažurirajte pozadine početnog i zaključanog ekrana za slike preuzete sa weba.
- Biranje boja akcenta korišćenih kroz korisnički interfejs.
- Omogući tamnu temu.


### Prikaži procenat baterije


Idite na **Podešavanja** > **Baterija**, zatim omogućite **Prikaži procenat baterije** u statusnoj traci.


### Uvezi kontakte


**Sa drugog Android telefona** - Idite na aplikaciju Kontakti i potražite opciju Izvezi u VCF.


**Sa iOS-a** - Koristite aplikaciju kao što je Export Contact i koristite opciju izvoza 'vCard' da biste izvezli VCF datoteku.

Kada imate VCF datoteku, možete je preneti na svoj GrapheneOS uređaj pomoću opcije spoljašnje memorije kao što je microSD kartica ili USB drajv. Ako nemate nijednu od tih opcija pri ruci, možete se odlučiti za deljenje putem jedne od mnogih aplikacija navedenih ispod.


![image](assets/4.webp)


Personalizovani početni ekran



## Alternativne Aplikacije


Da bi vaš telefon bio koristan, želećete da instalirate neke aplikacije! Opcije koje slede su uključene jer sam ih sve lično koristio ili zato što dobijaju snažne preporuke od šire zajednice koja se bavi privatnošću. Postoje mnoge druge sjajne alternative koje nisu pomenute, a [Awesome Privacy](https://awesome-privacy.xyz) nudi neverovatno opsežnu listu aplikacija koje čuvaju privatnost za sve vrste uređaja.


Samo zato što je aplikacija besplatni softver otvorenog koda (FOSS) ne znači da je slobodna od potencijalnih curenja privatnosti. Koristite [Exodus](https://reports.exodus-privacy.eu.org/en/) da vidite kako vaše omiljene aplikacije prolaze na njihovim proverama privatnosti.


### F-Droid


[F-Droid](https://f-droid.org/) je instalabilni katalog FOSS aplikacija za Android. Klijent olakšava pregledanje, instalaciju i ažuriranje aplikacija na vašem uređaju. Vredi napomenuti da ažuriranja putem F-Droid-a ponekad mogu biti sporija nego kod drugih prodavnica aplikacija. Ovo uglavnom zavisi od toga da li se aplikacija nalazi putem glavnog F-Droid repozitorijuma ili prilagođenog.


Da biste instalirali F-Droid, jednostavno idite na njihovu veb stranicu putem pregledača na vašem GrapheneOS telefonu i dodirnite preuzimanje. Ovo će preuzeti `.apk` datoteku. Zatim će vam biti postavljeno pitanje da li želite da instalirate aplikaciju.


Kao i aplikacije koje se nalaze u podrazumevanom repozitorijumu u F-Droid-u, mnogi Open Source projekti će takođe hostovati sopstveni repozitorijum koji se može dodati u podešavanjima F-Droid aplikacije. Ako je to slučaj, projekat o kojem je reč će vas provesti kroz veoma jednostavne korake potrebne da to postignete na njihovoj veb stranici.


![image](assets/5.webp)


Početni ekran F-Droid


### Aurora Store


[Aurora Store](https://auroraoss.com/) je FOSS verzija Google Play prodavnice. Aurora izgleda i deluje veoma slično tradicionalnoj Play prodavnici i omogućava vam da preuzmete i ažurirate bilo koju aplikaciju koju biste inače pronašli putem Google opcije.


Ubistvena funkcija Aurore je anonimno prijavljivanje. To znači da možete preuzeti bilo koju od vaših omiljenih aplikacija koje nisu dostupne putem F-Droid-a ili direktnog APK-a, bez potrebe da budete prijavljeni na vaš Google nalog.


Pre nego što požurite da ovo postavite kao svoju podrazumevanu opciju instalacije, setite se da su mnoge aplikacije od kojih pokušavamo da pobegnemo instalirane sa Play Store-a. Samo zato što su dostupne preko Aurore ne menja činjenicu da neke mogu imati ugrađene funkcije praćenja. Neće uvek biti moguće, ali kad god možete, potražite alternativu na F-Droid pre nego što preuzmete putem Aurore.


Da biste instalirali Auroru, jednostavno potražite 'Aurora Store' u F-Droidu.


Aurora takođe ima neke potencijalne vektore napada, jer "anonimni nalozi" su zapravo kreirani i kontrolisani od strane Aurore. U teoriji, oni bi mogli da serviraju zlonamerna ažuriranja ili da guraju aplikacije na vaš telefon, iako biste i dalje morali da prihvatite instalacioni prompt na uređaju. Aurora takođe ponekad ima problema sa aplikacijama koje se ne prikazuju zbog pogrešnog očitavanja regiona i uređaja. Ovo se obično može zaobići sledećim koracima.


**Top tip** - Sometimes the Aurora Store will experience rate limiting which limits your ability to search and install apps. To get around this go to **Settings** > **Apps** > **Aurora** > **Open by default**, then add the domain `play.google.com`. Now, whenever navigate to a product or service's website that has the 'Download via Play Store' link, tapping on it will open that app within Aurora for you to download.



![image](assets/6.webp)


Početni ekran Aurora Store


### Preuzimanje APK


Aplikacije na Androidu mogu se preuzeti i instalirati putem `.apk` fajla. Ovo je odlična alternativa koja ne zahteva prodavnice aplikacija trećih strana, jednostavno preuzmite fajl direktno sa sajta projekta ili usluge ili GitHub repozitorijuma.


Nedostatak ovog pristupa je što ne dobijate automatska ažuriranja, pa ćete morati pratiti komunikacione kanale te usluge kako biste saznali o novim izdanjima. Međutim, postoji sjajan projekat pod nazivom Obtanium koji ima za cilj da to reši. [Obtainium](https://github.com/ImranR98/Obtainium) vam omogućava da instalirate i ažurirate aplikacije otvorenog koda direktno sa njihovih stranica izdanja, i primate obaveštenja kada su nova izdanja dostupna.


![image](assets/7.webp)


Obtanium pregled


### Veb aplikacije


Za situacije kada možda želite retko koristiti neku uslugu i ne želite da preuzimate nativnu aplikaciju, možete jednostavno pristupiti veb verziji. Mnogi sajtovi danas takođe nude podršku za Progressive Web App (PWA). Ovo je slučaj kada možete obeležiti određeni sajt (npr. Twitter.com) na početnom ekranu vašeg telefona. Zatim, kada dodirnete ikonu, otvara se kao aplikacija preko celog ekrana bez uobičajenih ometanja koja dolaze sa tipičnim iskustvom pretraživača. Primer kako ovo izgleda možete videti ispod.


Da biste to postigli u Vanadiumu, izvornom pregledaču GrapheneOS-a, jednostavno idite na željenu web stranicu, dodirnite tri vertikalne tačke u gornjem desnom uglu ekrana, a zatim dodirnite **'Dodaj na početni ekran'**.


Jedina mana ovog pristupa je što, pošto je ovo samo obeležena veb stranica, nećete dobiti nikakve obaveštenja. Iako bi neki to mogli videti kao pozitivnu stvar!


![image](assets/8.webp)


Twitter PWA


### Web Pregledači


Ne možete stvarno pogrešiti sa unapred upakovanom opcijom, Vanadium. Aplikacija se ponaša identično kao bilo koji drugi mobilni pregledač koji sam probao i nikada nisam imao problema sa kompatibilnošću.


Za slučajeve kada treba da pristupite Tor nativnim `.onion` sajtovima, možete preuzeti Tor Browser APK direktno sa njihove [veb stranice](https://www.torproject.org/download/#android) ili putem F-Droid-a.


### VPN-ovi


Da biste zaštitili svoju online aktivnost od vašeg znatiželjnog internet provajdera (ISP), aplikacija za Virtuelnu Privatnu Mrežu (VPN) je dobra opcija. VPN šalje vaš internet saobraćaj kroz šifrovani tunel do deljene IP Address koju kontroliše provajder VPN usluge kako bi se osiguralo da aktivnost vašeg uređaja ne može biti povezana sa vama.


Sledeće su 3 dobro poštovane opcije koje vam omogućavaju da platite za uslugu u Bitcoin i bez pružanja bilo kakvih ličnih informacija. Sve 3 opcije su dostupne putem F-Droid.



- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)


### Poruke


U poslednjih godina rešenja za enkriptovane poruke postala su brojna. Problem ipak ostaje, možete imati najbolju i najprivatniju opciju instaliranu na svom telefonu, ali ako nemate kontakte koji je koriste, koja je svrha?


Većina ljudi koji nisu zainteresovani za privatnost verovatno koristi WhatsApp ili iMessage. Prvi se može preuzeti putem Aurora Store-a, ali drugi neće raditi na GrapheneOS-u (očigledno!).



- [Signal](https://signal.org/) je jedan od popularnijih end-to-end enkriptovanih (E2EE) mesindžera koji ima dobar dosadašnji učinak i bogat skup funkcija. Signal zahteva broj telefona za registraciju, tako da ako planirate da ćaskate sa ljudima za koje biste radije da ne znaju vaš broj telefona, možda bi trebalo da razmotrite neke od alternativa. Signal mora biti preuzet putem Aurora Store-a.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) je prilično nov E2EE mesindžer. Nema korisnički ID, ne zahteva broj telefona ili lične informacije. Ljudi vas pronalaze skeniranjem vašeg ličnog QR koda ili posetom vašeg jedinstvenog linka. Simplex takođe omogućava naprednim korisnicima da pokrenu sopstveni server kako bi dodatno smanjili oslanjanje na bilo koji centralizovani entitet. Simplex nema desktop klijent, pa možda nije pogodan ako vam je multi-uređaj na listi prioriteta. Simplex za Android je dostupan putem F-Droid.
- [Threema](https://threema.ch/en/faq/libre_installation) nudi slično iskustvo kao Simplex, ali postoji duže vreme i kao rezultat toga, deluje malo uglađenije. Threema nije besplatan, doživotna licenca košta $4.99 i može se kupiti sa Bitcoin. Threema nudi web klijent i izvorne desktop aplikacije. Android aplikacija je dostupna putem F-Droid.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) je nezvanični FOSS Fork zvanične Telegram aplikacije za Android. Telegram ima E2EE 'tajne četove', ali podrazumevana opcija nije privatna. Telegram FOSS se može preuzeti sa F-Droid.


![image](assets/9.webp)

Levo: Threema, Desno: Simplex


### Mediji



- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) je višeplatformski Spotify klijent koji ne zahteva Premium nalog. Spotube je dostupan putem F-Droid-a.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) je fantastična aplikacija za strimovanje bilo koje muzike sa YouTube Music, besplatno. ViMusic je dostupan na F-Droid.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) nudi YouTube iskustvo bez dosadnih reklama i sumnjivih dozvola. Sa NewPipe možete se pretplatiti na kanale, slušati u pozadini, pa čak i preuzeti za gledanje van mreže. NewPipe je dostupan putem F-Droid.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) je plejer za podkaste koji vam omogućava da se pretplatite i upravljate svim vašim omiljenim emisijama. AntennaPod je dostupan putem F-Droid-a.


![image](assets/11.webp)

Levo: Spotube, Desno: ViMusic


### Mape


Ako želite glasovnu pomoć dok vozite i koristite aplikaciju za mape u GrapheneOS-u, potrebno je da instalirate [RHVoice](https://rhvoice.org/installation/) i [konfigurišete](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available) ga.



- [Magic Earth](https://www.magicearth.com/) je alternativa za mape koja podržava navigaciju korak-po-korak, 3D i offline mape. Magic Earth se može preuzeti iz Aurora Store-a.
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) je alternativna mapa za putnike, turiste, planinare i bicikliste zasnovana na podacima OpenStreetMap-a prikupljenim od strane zajednice. Fokusirana je na privatnost, otvorenog je koda i predstavlja Fork aplikacije Maps.me (ranije poznate kao MapsWithMe). Podržava 100% funkcionalnosti bez aktivne internet veze i može se preuzeti sa F-Droid-a.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) je još jedna odlična alternativa za mape koja podržava sve gore navedene funkcije.


![image](assets/13.webp)

Levo: Magic Earth, Desno: Organic Maps


### Email



- [Proton Mail](https://proton.me/mail) nudi besplatnu privatnu email uslugu koja podržava revidirani E2EE. Proton takođe nudi plaćenu verziju koja podržava prilagođene domene i [aliasing](https://proton.me/support/creating-aliases). Proton Mail se može preuzeti kao direktan APK ili putem Aurore.
- [Tutanota](https://tutanota.com/) nudi iste funkcije kao Proton Mail, uključujući opcione plaćene usluge i može se preuzeti kao direktan APK ili putem F-Droid-a.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) je klijent za e-poštu otvorenog koda koji radi sa gotovo svim provajderima e-pošte. Podržava više naloga, objedinjeni prijemni sandučić i OpenPGP standard enkripcije.


![image](assets/15.webp)

Levo: Proton Mail, Desno: Tutanota


### Produktivnost



- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) je program za sinhronizaciju fajlova. Sinhronizuje fajlove između dva ili više uređaja u realnom vremenu, sigurno zaštićeno od znatiželjnih očiju. Vaši podaci su samo vaši i zaslužujete da izaberete gde će biti uskladišteni, da li će biti podeljeni sa nekom trećom stranom i kako će biti preneti preko interneta. Syncthing je dostupan putem F-Droid-a.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) povezuje sve vaše uređaje kako bi lako komunicirali jedni s drugima kada su povezani na vašu kućnu mrežu. Jednostavno šaljite datoteke, fotografije, podatke iz međuspremnika na sve vaše uređaje (čak i na iOS!). KDE Connect se može preuzeti sa F-Droid.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) je E2EE aplikacija za beleške koja omogućava sinhronizaciju vaših misli i lista zadataka na svim vašim uređajima. Njihov besplatni plan bi trebalo da pokrije većinu ličnih potreba. Notesnook je dostupan na F-Droid.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) je veoma sličan Notesnook-u, ali zahteva plaćeni plan da bi se podudaralo sa skupom funkcija. Standard Notes je dostupan putem F-Droid-a.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) je aplikacija za tastaturu koja vam omogućava da prilagodite gotovo sve što možete zamisliti kada je u pitanju iskustvo kucanja na vašem telefonu. Može se preuzeti putem F-Droid-a.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) je podrazumevana Google tastatura aplikacija. Po mom iskustvu, nudi ubedljivo najbolje iskustvo kucanja i prevlačenja. Ako preuzmete ovu aplikaciju, obavezno potpuno onemogućite sve dozvole vezane za mrežu. Može se preuzeti putem Aurore.


![image](assets/17.webp)

Levo: Notesnook, Desno: KDE Connect


### Lifestyle



- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) je prelepo dizajnirana aplikacija za vremensku prognozu otvorenog koda dostupna putem F-Droid-a. Takođe podržava mnogo različitih veličina widgeta, tako da možete videti vremensku prognozu za izabranu lokaciju direktno sa vašeg početnog ekrana.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) je aplikacija otvorenog koda koja čuva privatnost i podržava više od 200 jezika. Translate You je dostupan putem F-Droid-a.
- [Proton Calendar](https://proton.me/calendar/download) je jednostavan za korišćenje E2EE koji besprekorno komunicira sa vašim Proton email nalozima. Proton Calendar se može preuzeti kao APK ili putem Aurora prodavnice.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) je aplikacija za prikazivanje i čuvanje boarding karata, kupona, karata za filmove i članskih kartica itd. Jednostavno preuzmite odgovarajući `pkpass` ili `espass` fajl i otvorite ga pomoću aplikacije. PassAndroid je dostupan putem F-Droid-a.


![image](assets/19.webp)

Levo: Geometrijsko vreme, Desno: Proton kalendar


### Bezbednost/Privatnost



- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) nudi besplatno i E2EE rešenje za upravljanje lozinkama na više platformi za sve vaše uređaje. Njihova plaćena usluga omogućava integraciju 2FA kodova u aplikaciju. Serverska strana Bitwardena može se samostalno hostovati, a Android aplikacija je dostupna putem F-Droida.
- [Proton Pass](https://proton.me/pass/download) nudi sličnu besplatnu uslugu kao Bitwarden, ali korisnici [Proton Unlimited](https://proton.me/pricing) mogu pristupiti dodatnim naprednim funkcijama. Proton Pass je dostupan putem APK ili Aurora.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) je aplikacija za dvofaktorsku autentifikaciju za sisteme koji koriste protokole jednokratnih lozinki. Tokeni se mogu lako dodati skeniranjem QR koda. FreeOTP je dostupan putem F-Droid-a.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) je besplatna, sigurna i otvorenog koda aplikacija za Android za upravljanje vašim tokenima za dvostepenu verifikaciju za vaše onlajn usluge. Aegis je dostupan putem F-Droid-a.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) je plaćena, višeplatformska usluga koja šifrira vaše podatke lokalno kako biste ih mogli sigurno otpremiti na vašu omiljenu uslugu u oblaku. Cryptomator se može preuzeti putem F-Droid-a.


![image](assets/21.webp)

Levo: Proton Pass, Desno: Bitwarden


### Cloud Solutions



- [Proton Drive](https://proton.me/drive/download) je plaćeno E2EE cloud rešenje za bekapovanje i skladištenje svih vaših fajlova. U trenutku pisanja, upravo su najavili Windows desktop klijent, ali korisnici Mac i Linux sistema moraju nastaviti da koriste veb verziju za sinhronizaciju sa svojih računara (za sada). Android klijent je dostupan kao APK ili preko Aurore.
- [Skiff](https://skiff.com/download) takođe nudi plaćeno E2EE skladištenje u oblaku i alate za saradnju na fajlovima. Nude klijent za desktop za Mac i Windows (kao i veb aplikaciju), a njihovi Android klijenti moraju biti preuzeti sa Aurore.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) nudi potpuno opremljeno rešenje zasnovano na oblaku za saradnju, sinhronizaciju između uređaja i skladištenje fajlova. Napredniji korisnici mogu izabrati da sami hostuju svoj besplatni i open source softver na bilo kojem hardveru koji žele. Android klijenti se mogu preuzeti putem F-Droid-a.
- [Cryptpad](https://cryptpad.fr/) nudi besplatnu, web baziranu, E2EE alternativu za Google Docs.


![image](assets/23.webp)

Proton Drive


## Nedostaci


Otvoreni kod i alternative koje čuvaju privatnost za aplikacije tehnoloških konglomerata na koje ste navikli su brojne, a neke od njih su često bolje od zatvorenog koda, špijunskih alternativa.


Međutim, kada prelazite na GrapheneOS, postoje određene pogodnosti kojih se morate odreći zbog nedostatka alternativa. To uključuje:



- Apple CarPlay/Android Auto** - Moraćete da se držite dobrog starog Bluetooth-a, USB-a ili Aux-a.
- Apple/Google Pay** - Gotovo svi ionako nose svoj Wallet sa sobom!
- Banking apps** - Nije da ove aplikacije uopšte ne rade. Neke rade savršeno. Druge rade samo kada su omogućene Google Play usluge (pročitajte više o tome ispod), a neke jednostavno ne rade uopšte. Pročitajte izveštaj o vašoj banci [ovde](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) da biste videli trenutno stanje. Ne brinite ako je vaša banka na listi onih koje ne rade, zapamtite da jednostavno možete sačuvati URL kao veb aplikaciju na vašem početnom ekranu.
- Push Notifications** - Većina aplikacija koje vam šalju obaveštenja kada ne koristite određenu aplikaciju to će učiniti putem Google Play Services. Ove usluge nisu instalirane po defaultu sa GrapheneOS, tako da ako ne dobijate obaveštenja odmah kada vam prijatelj pošalje email, verovatno je to razlog. Dobra vest je da su neke od gore pomenutih aplikacija implementirale sopstvenu pozadinsku vezu kako bi periodično proveravale za ažuriranja i zatim vam dale obaveštenje kada je to potrebno.


### Sandboxed Google Play


**Imajte na umu da:** GrapheneOS ima kompatibilnost Layer koja pruža opciju za instalaciju i korišćenje zvaničnih izdanja Google Play-a u standardnom peskovniku aplikacija. Google Play ne dobija apsolutno nikakav poseban pristup ili privilegije na GrapheneOS-u za razliku od zaobilaženja peskovnika aplikacija i dobijanja ogromne količine visoko privilegovanog pristupa.


Ako otkrijete da jednostavno ne možete živeti bez tih push obaveštenja za vašu omiljenu aplikaciju ili je određena aplikacija 'neophodna' beskorisna bez Play Services, GrapheneOS vam omogućava da [instalirate](https://grapheneos.org/usage#sandboxed-google-play-installation) ove servise u potpuno izolovanom okruženju. Kada se instaliraju, ovi servisi ne zahtevaju Google nalog za rad, a dozvole svakog od njih mogu biti strogo kontrolisane.


Pre nego što požurite da ih instalirate prvog dana, pozivam vas da vidite koliko daleko možete stići bez njih. Verovatno ćete biti iznenađeni koliko mnogo aplikacija funkcioniše savršeno normalno bez njih.


Ako želite da ih instalirate, jednostavno dodirnite unapred instaliranu aplikaciju 'Apps', a zatim 'Google Play Services'. Razmislite o njihovoj instalaciji zajedno sa onim manje privatnim aplikacijama bez kojih ne možete da živite, unutar potpuno odvojenog korisničkog profila kako biste obezbedili dodatni Layer nivo razdvajanja od ostatka vašeg telefona.


![image](assets/24.webp)

Ekran za instalaciju Play usluga


### Profili


GrapheneOS vam omogućava da imate odvojeno telefonsko iskustvo, unutar vašeg telefona. Dodatni profili mogu instalirati svoje aplikacije i usluge i ne mogu pristupiti bilo kojim fajlovima ili podacima sa naloga vlasnika.

Ako imate samo jednu ili dve od tih aplikacija koje zahtevaju Play Services, ali ih koristite vrlo retko, instaliranje tih aplikacija zajedno sa Play Services u zasebnom profilu može biti odlična ideja da dodatno ojačate bilo kakve male implikacije na privatnost koje ostaju kada ih pokrećete u vlasničkom profilu.


Više o ovom slučaju upotrebe možete pročitati [ovde](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).


Ako odlučite da dodate poseban profil koji odgovara vašem slučaju upotrebe, aplikacija [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) može vam biti korisna. Insular vam omogućava da lako klonirate bilo koju od vaših postojećih aplikacija na novi profil bez potrebe da prolazite kroz bilo koji od tradicionalnih puteva instalacije pokrivenih ranije u ovom vodiču. Insular takođe omogućava da brzo 'zamrznete' bilo koju od tih aplikacija kako biste potpuno onemogućili sve pozadinske servise te aplikacije da se pokreću.


![image](assets/24.webp)

Ekran za upravljanje korisničkim profilom


### e-Sims


Ako želite da podignete privatnost svog telefona na viši nivo i imate mobilnu uslugu koja je odvojena od vašeg stvarnog identiteta, eSIM bi mogao biti za vas. eSIM je virtuelna SIM kartica koju možete kupiti online i dodati na svoj telefon putem QR koda. Kompanije koje nude takve usluge i koje se mogu platiti anonimno sa Bitcoin uključuju [Silent.Link](https://silent.link/) i [Bitrefill](https://www.bitrefill.com/gb/en/esims/).


eSIM-ovi ne treba da se posmatraju kao potpuni lek za privatnost telefona. Oni mogu biti koristan alat kada su u pravim rukama, ali molimo vas da istražite [kompromise](https://grapheneos.org/faq#cellular-tracking) korišćenja bilo koje vrste mobilne usluge ako vam je namera da budete potpuno 'van mreže'.


Sandboxed Play Services mora biti instaliran za eSIM provisioning u GrapheneOS.


## Bekapovi


Nakon što postavite svoj novi Pixel telefon bez Google-a, dobra je ideja da napravite rezervnu kopiju. Ova rezervna kopija će vam omogućiti da vratite telefon u identično stanje u slučaju da izgubite telefon ili da bude izgubljen/ukraden.


Možete izabrati da sačuvate rezervnu kopiju na bilo koji eksterni medijum za skladištenje, ili na samostalno hostovano cloud rešenje kao što je Nextcloud, iako neki korisnici prijavljuju različite nivoe uspeha sa ovom opcijom.


Da biste kreirali svoju prvu rezervnu kopiju:


1. Idite na **Settings** > **System** > **Backup**, zatim zapišite svoj 12-reči kod za oporavak. Ovaj kod je potreban za dešifrovanje rezervne kopije datoteke kasnije. Izgubite kod, izgubite pristup rezervnoj kopiji telefona.

2. Zatim izaberite lokaciju za skladištenje. Preporučio bih eksterni USB disk ili industrijski microSD karticu.

3. Izaberite podatke za bekapovanje. Ako imate prostora na odabranom mediju za skladištenje, savetovao bih da odaberete sve.

4. Dodirnite tri tačke u gornjem desnom uglu i izaberite **Backup now**.


![image](assets/26.webp)


Rezervna kopija ekrana


Zapamtite da, ako pravite offline rezervne kopije na eksternim medijima za skladištenje, ima smisla redovno završavati ovaj korak kako biste osigurali da se nedavne važne ažuriranja na vašem telefonu ne izgube ako se dogodi najgore.


![video](https://www.youtube.com/embed/eyWmcItzisk)


Video koji detaljno opisuje proces pravljenja rezervne kopije


## Zaključak


U poslednjih nekoliko godina, GrapheneOS softver je značajno sazreo. Stabilniji je i kompatibilniji nego ikada. Povezivanje ovoga sa procvatom Open Source i ekosistema aplikacija koje čuvaju privatnost, čini GrapheneOS zaista održivom alternativom za standardni Android ili iOS, čak i za 'obične' ljude baš poput vas!


Kompromitovanje podataka i masovni nadzor su toliko uobičajeni u današnjem svetu da jedva dospevaju na naslovne strane. Na vama je da se zaštitite. Biće potrebno prilagođavanje i žrtvovanje, ali smanjenje vaše izloženosti takvim povredama nije ni približno teško kao što mislite da će biti.


Nadam se da će vam ovaj vodič pomoći na vašem putovanju. Ako ste smatrali da je ovaj vodič koristan i želite da podržite moj rad, molim vas razmislite o slanju [donacije](/tips).


Ako ste postojeći korisnik GrapheneOS-a ili to postanete kao rezultat ovog vodiča, razmislite o [doniranju](https://grapheneos.org/donate) kako biste podržali njihov važan rad.


### Saznajte više


GrapheneOS je zečja rupa kojom bi svako mogao lako provesti nedelje istražujući. Postoji toliko toga što možete naučiti i prilagoditi kako biste iskustvo prilagodili svojim zahtevima i modelima pretnji. Ispod su neki linkovi gde možete nastaviti svoje putovanje:



- [Službeni vodič za korišćenje GrapheneOS-a](https://grapheneos.org/usage) - Službena veb stranica
- [GrapheneOS Forum](https://discuss.grapheneos.org/) - Zvanična veb stranica
- [GrapheneOS Settings Masterclass](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video by 'The Privacy Wayfinder'
- [GrapheneOS General Podcast](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast od 'Watchman Privacy'


puna zasluga: https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md