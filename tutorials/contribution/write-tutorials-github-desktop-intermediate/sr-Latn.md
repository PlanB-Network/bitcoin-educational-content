---
name: Doprinos - Tutorijal sa GitHub Desktop (Srednji nivo)
description: Kompletan vodič za predlaganje tutorijala o Plan ₿ Network korišćenjem GitHub Desktop-a
---
![cover](assets/cover.webp)


Pre nego što pratite ovaj vodič o dodavanju novog vodiča, morate završiti neke preliminarne korake. Ako to još niste učinili, pozivam vas da prvo pogledate ovaj uvodni vodič, a zatim se vratite ovde:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Već imate:


- Izabrana tema vašeg tutorijala;
- Kontaktirao sam Plan ₿ Network tim putem [Telegram grupe](https://t.me/PlanBNetwork_ContentBuilder) ili paolo@planb.network;
- Izabrali ste alate za doprinos.


U ovom vodiču ćemo videti kako da dodate svoj vodič na Plan ₿ Network podešavanjem vašeg lokalnog okruženja sa GitHub Desktop. Ako već dobro poznajete Git, ovaj veoma detaljan vodič možda neće biti potreban za vas. Preporučio bih da pogledate ovaj drugi vodič gde predstavljam samo glavne smernice, bez detaljnog korak-po-korak vođenja:



- Iskusni korisnici**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Ako ne želite da postavljate lokalno okruženje, pratite ovaj drugi vodič namenjen početnicima, gde pravimo izmene direktno putem GitHub-ovog web Interface:



- Početnici (web Interface)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Preduslovi


Softver potreban za praćenje ovog tutorijala:



- [GitHub Desktop](https://desktop.github.com/);
- Uređivač markdown datoteka kao što je [Obsidian](https://obsidian.md/);
- Uređivač koda ([VSC](https://code.visualstudio.com/) ili [Sublime Text](https://www.sublimetext.com/)).


![TUTO](assets/fr/01.webp)


Preduslovi pre početka tutorijala:



- Imate [GitHub nalog](https://github.com/signup);
- Imate Fork iz [Plan ₿ Network izvornog repozitorijuma](https://github.com/PlanB-Network/Bitcoin-educational-content);
- Imajte [profil profesora na Plan ₿ Network](https://planb.network/professors) (samo ako predlažete kompletan tutorijal).


Ako vam je potrebna pomoć u pribavljanju ovih preduslova, moji drugi tutorijali će vam pomoći:



Kada je sve na svom mestu i vaše lokalno okruženje je pravilno postavljeno sa vašim sopstvenim Fork od Plan ₿ Network, možete početi sa dodavanjem tutorijala.


## 1 - Kreiraj novu granu


Otvorite svoj pregledač i idite na stranicu vašeg Fork u repozitorijumu Plan ₿ Network. Ovo je Fork koji ste uspostavili na GitHub-u. URL vašeg Fork bi trebalo da izgleda ovako: `https://github.com/[vaše-korisničko-ime]/Bitcoin-educational-content`:


![TUTO](assets/fr/03.webp)


Uverite se da ste na glavnoj grani `dev`, zatim kliknite na dugme `Sync Fork`. Ako vaš Fork nije ažuriran, GitHub će ponuditi da ažurira vašu granu. Nastavite sa ovim ažuriranjem. Ako je, naprotiv, vaša grana već ažurirana, GitHub će vas obavestiti:


![TUTO](assets/fr/04.webp)


Otvorite GitHub Desktop softver i proverite da li je vaš Fork pravilno izabran u gornjem levom uglu prozora:


![TUTO](assets/fr/05.webp)


Kliknite na dugme `Fetch origin`. Ako je vaš lokalni repozitorijum već ažuriran, GitHub Desktop neće predložiti dodatne akcije. U suprotnom, pojaviće se opcija `Pull origin`. Kliknite na ovo dugme da ažurirate vaš lokalni repozitorijum:


![TUTO](assets/fr/06.webp)


Proverite da ste zaista na glavnoj grani `dev`:


![TUTO](assets/fr/07.webp)


Kliknite na ovu granu, zatim kliknite na dugme `New Branch`:


![TUTO](assets/fr/08.webp)


Osigurajte da je nova grana zasnovana na izvornom repozitorijumu, naime `PlanB-Network/Bitcoin-educational-content`.


Nazovite svoju granu na način da naslov jasno ukazuje na njenu svrhu, koristeći crtice za razdvajanje svake reči. Na primer, recimo da je naš cilj napisati vodič za korišćenje Sparrow Wallet softvera. U ovom slučaju, radna grana posvećena pisanju ovog vodiča mogla bi se nazvati: `tuto-sparrow-Wallet-loic`. Kada unesete odgovarajući naziv, kliknite na `Create branch` da potvrdite kreiranje grane:


![TUTO](assets/fr/09.webp)


Sada kliknite na dugme `Publish branch` da biste sačuvali svoju novu radnu granu na vašem online Fork na GitHub-u:

![TUTORIAL](assets/fr/10.webp)

Sada, na GitHub Desktop-u, trebali biste se naći na vašoj novoj grani. To znači da će sve promene napravljene lokalno na vašem računaru biti isključivo sačuvane na ovoj specifičnoj grani. Takođe, sve dok je ova grana izabrana na GitHub Desktop-u, fajlovi vidljivi lokalno na vašoj mašini odgovaraju onima sa ove grane (`tuto-sparrow-Wallet-loic`), a ne onima sa glavne grane (`dev`).


![TUTORIAL](assets/fr/11.webp)


Za svaki novi članak koji želite objaviti, potrebno je kreirati novu granu iz `dev`. Grana u Gitu je paralelna verzija projekta, koja vam omogućava da pravite izmene bez uticaja na glavnu granu, sve dok rad ne bude spreman za spajanje.


## 2 - Dodavanje datoteka za tutorijal


Sada kada je radna grana kreirana, vreme je da integrišete vaš novi tutorijal. Imate dve opcije: koristiti moj Python skript, koji automatizuje kreiranje neophodnih dokumenata, ili ručno kreirati svaki fajl. Pogledaćemo korake koje treba pratiti za svaku opciju.


### Sa mojim Python skriptom


Treba da instalirate na vašem računaru:


- Python 3.8 ili noviji.


Da biste koristili skriptu, idite do fascikle u kojoj je smeštena. Skripta se nalazi u Plan ₿ Network skladištu podataka na putanji: `Bitcoin-educational-content/scripts/tutorial-related/data-creator`.


Jednom kada ste u fascikli, instalirajte zavisnosti:


```
pip install -r requirements.txt
```


Zatim pokrenite softver komandom:


```
python3 main.py
```


Grafički korisnički interfejs Interface (GUI) će se otvoriti. Prvi put ćete morati uneti sve potrebne informacije, ali pri narednim korišćenjima, skripta će pamtiti vaše lične podatke, tako da ih nećete morati ponovo unositi.


![DATA-CREATOR-PY](assets/fr/37.webp)


Počnite unosom lokalne putanje do fascikle `/tutorials` u vašem kloniranom repozitorijumu (`.../Bitcoin-educational-content/tutorials/`). Putanju možete uneti ručno ili kliknuti na dugme "Browse" da biste navigirali pomoću vašeg istraživača fajlova.


![DATA-CREATOR-PY](assets/fr/38.webp)


Odaberite jezik na kojem ćete pisati svoj vodič.


![DATA-CREATOR-PY](assets/fr/39.webp)


U polju "Contributor's GitHub ID" unesite svoje GitHub korisničko ime.


![DATA-CREATOR-PY](assets/fr/40.webp)


Zatim, treba da popunite profil profesora. Dostupno vam je nekoliko opcija:


- Unesite prva slova vašeg imena u polje "Ime profesora". Vaše ime će se zatim pojaviti na padajućoj listi "Predlozi prof.". Izaberite ga klikom na njega;
- Alternativno, možete direktno kliknuti na padajuću listu "Prof. Suggestions" i odabrati ime vašeg profesora.


Ova akcija će automatski popuniti UUID vašeg profesora u odgovarajuće polje.



![DATA-CREATOR-PY](assets/fr/41.webp)


Ako još uvek nemate profil profesora, pogledajte ovaj vodič:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Zatim kliknite na dugme „Novi tutorijal“.


![DATA-CREATOR-PY](assets/fr/42.webp)


Izaberite glavnu kategoriju za vaš vodič. Zatim, odaberite odgovarajuću potkategoriju na osnovu izabrane glavne kategorije.


![DATA-CREATOR-PY](assets/fr/43.webp)


Odredite nivo težine tutorijala.


![DATA-CREATOR-PY](assets/fr/44.webp)


Izaberite ime za direktorijum kreiran specifično za vaš vodič. Ime ove fascikle treba da odražava softver koji je pokriven u vodiču, koristeći crtice za razdvajanje reči. Na primer, fascikla bi mogla biti nazvana `red-Wallet`:


![DATA-CREATOR-PY](assets/fr/45.webp)


`project_id` je UUID kompanije ili organizacije iza alata pokrivenog u vodiču, dostupan [u listi projekata](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Na primer, za vodič o Sparrow Wallet, možete pronaći njegov `project_id` u fajlu: `Bitcoin-educational-content/resources/projects/sparrow/project.yml`. Ova informacija se dodaje u vaš YAML fajl vodiča jer Plan ₿ Network održava bazu podataka kompanija i organizacija aktivnih u Bitcoin ili povezanim projektima. Dodavanjem povezanog `project_id`, povezujete vaš sadržaj sa relevantnim entitetom.


***Ažuriranje:*** U novoj verziji skripte više nije potrebno ručno unositi `project_id`. Dodata je funkcija pretrage koja pronalazi projekat po imenu i automatski preuzima odgovarajući `project_id`. Upišite početak imena projekta u polje "Project Name" da biste ga pretražili, a zatim izaberite željenu kompaniju iz padajućeg menija. `project_id` će biti automatski popunjen u polju ispod. Takođe ga možete uneti ručno ako je potrebno.


![DATA-CREATOR-PY](assets/fr/46.webp)


Za oznake, izaberite 2 ili 3 relevantne ključne reči povezane sa sadržajem vašeg tutorijala, birajući isključivo sa [liste oznaka Plan ₿ Network](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Softver takođe pruža funkciju pretrage ključnih reči sa padajućom listom.


![DATA-CREATOR-PY](assets/fr/47.webp)


Kada su svi podaci uneti i verifikovani, kliknite na "Create Tutorial" da potvrdite kreiranje vaših datoteka za tutorijal. Ovo će generate vaš folder za tutorijal i sve potrebne datoteke u izabranoj kategoriji lokalno.


![DATA-CREATOR-PY](assets/fr/48.webp)


Sada možete preskočiti pododeljak "Bez mog Python skripta" kao i korak 3, "Popunite YAML datoteku," jer je skript već izvršio ove radnje za vas. Pređite direktno na korak 4 i počnite pisati svoj vodič.


Za više informacija o ovom Python skriptu, možete pogledati i [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


### Bez mog Python skripta


Otvorite upravitelj datoteka i idite do fascikle `Bitcoin-educational-content`, koja predstavlja lokalnu kloniranu verziju vašeg repozitorijuma. Obično biste je trebali pronaći pod `Documents\GitHub\Bitcoin-educational-content`.


U ovom direktorijumu, potrebno je da pronađete odgovarajući podfolder za postavljanje vašeg tutorijala. Organizacija foldera odražava različite sekcije Plan ₿ Network vebsajta. U našem primeru, pošto želimo da dodamo tutorijal o Sparrow Wallet, trebali bismo da navigiramo do sledeće putanje: `Bitcoin-educational-content\tutorials\Wallet`, što odgovara `Wallet` sekciji na vebsajtu:


![TUTO](assets/fr/12.webp)


U okviru fascikle `Wallet`, potrebno je da kreirate novi direktorijum posebno posvećen vašem tutorijalu. Ime ovog direktorijuma treba da dočara softver koji je pokriven u tutorijalu, povezujući reči crticama. Za moj primer, fascikla će biti nazvana `sparrow-Wallet`:


![TUTO](assets/fr/13.webp)


U ovoj novoj podmapi posvećenoj vašem vodiču, potrebno je dodati nekoliko Elements:


- Kreirajte fasciklu `assets`, namenjenu za primanje svih ilustracija potrebnih za vaš vodič;
- U okviru ove fascikle `assets`, potrebno je da kreirate podfasciklu nazvanu prema kodu originalnog jezika tutorijala. Na primer, ako je tutorijal napisan na engleskom, ova podfascikla mora biti nazvana `en`. Postavite sve vizuelne elemente tutorijala tamo (dijagrami, slike, snimci ekrana, itd.).
- Datoteka `tutorial.yml` mora biti kreirana kako bi se zabeležili detalji vezani za vaš vodič;
- Datoteka u markdown formatu treba da bude kreirana za pisanje stvarnog sadržaja vašeg tutorijala. Ova datoteka mora biti naslovljena prema kodu jezika pisanja. Na primer, za tutorijal napisan na francuskom, datoteka mora biti nazvana `fr.md`.


![TUTO](assets/fr/14.webp)


Da rezimiramo, evo hijerarhije fajlova koje treba kreirati:


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```


## 3 - Popunite YAML datoteku


Popunite datoteku `tutorial.yml` kopiranjem sledećeg šablona:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


Evo potrebna polja:



- id**: A UUID (_Universally Unique Identifier_) koji jedinstveno identifikuje tutorijal. Možete ga generate koristiti [online alat](https://www.uuidgenerator.net/version4). Jedini zahtev je da ovaj UUID bude nasumičan kako bi se izbegli konflikti sa drugim UUID-om na platformi;



- project_id**: UUID kompanije ili organizacije iza alata predstavljenog u vodiču [sa liste projekata](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Na primer, ako kreirate vodič o Green Wallet softveru, možete pronaći ovaj `project_id` u sledećem fajlu: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Ova informacija se dodaje u vaš YAML fajl vodiča jer Plan ₿ Network održava bazu podataka svih kompanija i organizacija koje rade na Bitcoin ili povezanim projektima. Dodavanjem `project_id` entiteta povezanog sa vašim vodičem, kreirate vezu između dva Elements;



- tagovi**: 2 ili 3 relevantne ključne reči povezane sa sadržajem tutorijala, isključivo odabrane [iz Plan ₿ Network liste tagova](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- kategorija**: Podkategorija koja odgovara sadržaju tutorijala, prema strukturi vebsajta Plan ₿ Network (na primer, za novčanike: `desktop`, `hardware`, `mobile`, `backup`);



- nivo**: Nivo težine tutorijala, izabran iz:
    - `početnik`
    - `srednji`
    - `napredno`
    - `stručnjak`



- professor_id**: Vaš `professor_id` (UUID) kako je prikazan na [vašem profesorskom profilu](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors);



- original_language**: Originalni jezik tutorijala (npr. `fr`, `en`, itd.);



- lektura**: Informacije o procesu lekture. Završite prvi deo, jer lektura sopstvenog tutorijala se računa kao prva validacija:
    - jezik**: Jezički kod za lekturu (npr., `fr`, `en`, itd.).
    - last_contribution_date**: Datum dana.
    - hitnost**: 1
    - contributor_names**: Vaš GitHub ID.
    - nagrada**: 0


Za više detalja o vašem ID-u nastavnika, pogledajte odgovarajući vodič:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


Kada završite sa izmenama vašeg `tutorial.yml` fajla, sačuvajte dokument klikom na `File > Save`:


![TUTO](assets/fr/16.webp)


Sada možete zatvoriti svoj uređivač koda.


## 4 - Popunite Markdown datoteku


Sada možete otvoriti svoju datoteku koja će sadržati vaš vodič, imenovanu sa kodom vašeg jezika, kao što je `fr.md`. Idite u Obsidian, na levoj strani prozora, skrolujte kroz stablo fascikli dok ne pronađete fasciklu vašeg vodiča i datoteku koju tražite:


![TUTO](assets/fr/18.webp)


Kliknite na datoteku da biste je otvorili:


![TUTO](assets/fr/19.webp)


Počećemo popunjavanjem odeljka `Properties` na vrhu dokumenta.


![TUTO](assets/fr/20.webp)


Ručno dodajte i popunite sledeći blok koda:


```
---
name: [Title]
description: [Description]
---
```


![TUTO](assets/fr/21.webp)


Popunite naziv vašeg tutorijala i kratak opis njega:


![TUTO](assets/fr/22.webp)


Zatim, dodajte putanju slike naslovnice na početku vašeg vodiča. Da biste to uradili, zabeležite:


```
![cover-sparrow](assets/cover.webp)
```


Ova sintaksa će biti korisna kad god je potrebno dodati sliku u vaš vodič. Uzvičnik označava da je u pitanju slika, dok je alternativni tekst (alt) naveden između zagrada. Putanja do slike je navedena između okruglih zagrada:


![TUTO](assets/fr/23.webp)


## 5 - Dodajte logo i naslovnu stranu


U okviru fascikle `assets`, morate dodati datoteku pod nazivom `logo.webp`, koja će služiti kao sličica za vaš članak. Ova slika mora biti u `.webp` formatu i mora poštovati kvadratne dimenzije kako bi se uskladila sa korisnikom Interface. Slobodni ste da izaberete logo softvera koji je pokriven u tutorijalu ili bilo koju drugu relevantnu sliku, pod uslovom da je oslobođena prava. Pored toga, dodajte i sliku pod nazivom `cover.webp` na istom mestu. Ova slika će biti prikazana na vrhu vašeg tutorijala. Osigurajte da ova slika, kao i logo, poštuje prava korišćenja i da je pogodna za kontekst vašeg tutorijala:

## 6 - Pisanje tutorijala i dodavanje vizuala


Nastavite pisanje svog vodiča pisanjem sadržaja. Kada želite da uključite podnaslov, primenite odgovarajuće markdown formatiranje tako što ćete prefiksirati tekst sa `##`:


![TUTO](assets/fr/24.webp)


Podfolder jezika u folderu `assets` koristi se za čuvanje dijagrama i vizuala koji će pratiti vaš vodič. Koliko god je to moguće, izbegavajte uključivanje teksta u vaše slike kako biste učinili vaš sadržaj dostupnim međunarodnoj publici. Naravno, softver koji se predstavlja će sadržati tekst, ali ako dodajete dijagrame ili dodatne indikacije na snimcima ekrana softvera, učinite to bez teksta ili, ako je neophodno, koristite engleski.


![TUTO](assets/fr/25.webp)


Da biste imenovali svoje slike, jednostavno koristite brojeve koji odgovaraju njihovom redosledu pojavljivanja u tutorijalu, formatirane sa dve cifre (ili tri cifre ako vaš tutorijal sadrži više od 99 slika). Na primer, nazovite svoju prvu sliku `01.webp`, drugu `02.webp`, i tako dalje.


Vaše slike moraju biti isključivo u formatu `.webp`. Ako je potrebno, možete koristiti [moj softver za konverziju slika](https://github.com/LoicPandul/ImagesConverter).


![TUTO](assets/fr/26.webp)


Da biste umetnuli dijagram u svoj dokument, koristite sledeću Markdown komandu, vodeći računa da navedete odgovarajući alternativni tekst kao i tačan put do slike:


```
![sparrow](assets/fr/01.webp)
```


Uzvičnik na početku označava da je to slika. Alternativni tekst, koji pomaže u pristupačnosti i SEO, nalazi se između zagrada. Na kraju, putanja do slike je navedena između zagrada.


Ako želite da kreirate sopstvene dijagrame, obavezno se pridržavajte grafičke povelje Plan ₿ Network kako biste osigurali vizuelnu doslednost:


- Font**: Koristite [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- Boje**:
 - Narandžasta: #FF5C00
 - Crna: #000000
 - Bela: #FFFFFF


**Važno je da svi vizuelni elementi integrisani u vaše tutorijale budu bez prava ili da poštuju licencu izvornog fajla**. Takođe, svi dijagrami objavljeni na Plan ₿ Network dostupni su pod CC-BY-SA licencom, na isti način kao i tekst.

**-> Savet:** Kada delite datoteke javno, kao što su slike, važno je ukloniti sav nepotreban metapodatak. Ovo može sadržati osetljive informacije, kao što su podaci o lokaciji, datumi kreiranja ili detalji o autoru. Da biste zaštitili svoju privatnost, preporučljivo je obrisati ove metapodatke. Da biste pojednostavili ovaj proces, možete koristiti specijalizovane alate kao što je [Exif Cleaner](https://exifcleaner.com/), koji omogućava čišćenje metapodataka dokumenta jednostavnim prevlačenjem i ispuštanjem.

## 7 - Sačuvaj i pošalji tutorijal


Kada završite pisanje svog tutorijala na jeziku po vašem izboru, sledeći korak je da podnesete **Pull Request**. Administrator će se zatim pobrinuti za dodavanje svih nedostajućih prevoda vašeg tutorijala, zahvaljujući našem automatizovanom metodu prevođenja uz ljudsku reviziju.


Da biste nastavili sa Pull Request-om, otvorite GitHub Desktop softver. Softver bi automatski trebalo da detektuje promene koje ste napravili lokalno na vašoj grani u poređenju sa originalnim repozitorijumom. Pre nego što nastavite, pažljivo proverite na levoj strani Interface da li ove promene odgovaraju onome što ste očekivali:


![TUTO](assets/fr/28.webp)


Dodajte naslov za vašu izmenu, zatim kliknite na plavo dugme `Commit to [vaša grana]` da potvrdite ove promene:


![TUTO](assets/fr/29.webp)


Commit je čuvanje promena napravljenih na grani, praćeno opisnom porukom, što omogućava praćenje evolucije projekta tokom vremena. To je neka vrsta međuprovere.


Zatim kliknite na dugme `Push origin`. Ovo će poslati vaš commit na vaš Fork:


![TUTO](assets/fr/30.webp)


Ako niste završili svoj tutorijal, možete mu se vratiti kasnije i napraviti nove izmene. Ako ste završili sa izmenama za ovu granu, kliknite sada na dugme `Preview Pull Request`:


![TUTO](assets/fr/31.webp)


Možete poslednji put proveriti da li su vaše izmene tačne, a zatim kliknite na dugme `Create pull request`:


![TUTO](assets/fr/32.webp)


Zahtev za povlačenje je zahtev napravljen za integraciju izmena iz vaše grane u glavnu granu repozitorijuma Plan ₿ Network, što omogućava pregled i diskusiju o izmenama pre njihovog spajanja.


Bićete automatski preusmereni na vaš pregledač na GitHub-u na stranicu za pripremu vašeg Zahteva za Povlačenje:


![TUTO](assets/fr/33.webp)

Navedite naslov koji ukratko rezimira promene koje želite da spojite sa izvornim repozitorijumom. Dodajte kratak komentar koji opisuje ove promene (ako imate broj problema povezan sa kreiranjem vašeg tutorijala, zapamtite da navedete u komentaru `Closes #{broj problema}`), zatim kliknite na dugme Green `Create pull request` da potvrdite zahtev za spajanje:

![TUTO](assets/fr/34.webp)


Vaš PR će tada biti vidljiv na kartici `Pull Request` glavnog repozitorijuma Plan ₿ Network. Sve što treba da uradite je da sačekate da vas administrator kontaktira kako bi potvrdio spajanje vašeg doprinosa ili zatražio bilo kakve dodatne izmene.


![TUTO](assets/fr/35.webp)


Nakon što je vaš PR spojen sa glavnom granom, preporučuje se brisanje vaše radne grane (`tuto-sparrow-Wallet`) kako biste održali čistu istoriju na vašem Fork. GitHub će vam automatski ponuditi ovu opciju na vašoj PR stranici:


![TUTO](assets/fr/36.webp)


Na softveru GitHub Desktop, možete se vratiti na glavnu granu vašeg Fork (`dev`).


![TUTO](assets/fr/07.webp)


Ako želite da izvršite izmene u svom doprinosu nakon što ste već poslali svoj PR, procedura zavisi od trenutnog stanja vašeg PR-a:


- Ako je vaš PR još uvek otvoren i nije spojen, napravite izmene lokalno dok ostajete na istoj grani. Kada su izmene završene, koristite dugme `Push origin` da dodate novi commit vašem još uvek otvorenom PR-u;
- Ako je vaš PR već spojen sa glavnom granom, moraćete da započnete proces iznova kreiranjem nove grane, a zatim podnošenjem novog PR-a. Osigurajte da je vaš lokalni repozitorijum sinhronizovan sa Plan ₿ Network izvornim repozitorijumom pre nego što nastavite.


Ako naiđete na tehničke poteškoće prilikom predaje svog tutorijala, ne ustručavajte se da zatražite pomoć na [našoj posvećenoj Telegram grupi za doprinose](https://t.me/PlanBNetwork_ContentBuilder). Hvala!