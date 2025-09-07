---
name: Doprinos - GitHub Web vodič (početnik)
description: Potpuni vodič za Plan ₿ Network tutorijale sa GitHub Web
---
![cover](assets/cover.webp)


Pre nego što pratite ovaj vodič o dodavanju novog vodiča, potrebno je da završite nekoliko preliminarnih koraka. Ako to već niste učinili, molimo vas da prvo pogledate ovaj uvodni vodič, a zatim se vratite ovde:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Već imate:




- Izaberite temu za vaš vodič;
- Kontaktirao sam Plan ₿ Network tim putem [Telegram grupe](https://t.me/PlanBNetwork_ContentBuilder) ili paolo@planb.network ;
- Izaberite alate za doprinos.


U ovom vodiču ćemo pogledati kako da dodate svoj vodič u Plan ₿ Network koristeći web verziju GitHub-a. Ako ste već savladali Git, ovaj veoma detaljan vodič možda neće biti potreban za vas. Umesto toga, preporučujem da pogledate jedan od ova druga 2 vodiča, gde detaljno opisujem smernice koje treba pratiti i korake za pravljenje izmena sa lokalnog:




- Iskusni korisnici**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410


- Srednji nivo (GitHub Desktop)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Preduslovi


Preduslovi pre početka tutorijala:




- Imate [GitHub nalog](https://github.com/signup);
- Imate Fork iz [Plan ₿ Network izvornog repozitorijuma](https://github.com/PlanB-Network/Bitcoin-educational-content);
- Imajte [profil nastavnika na Plan ₿ Network](https://planb.network/professors) (samo ako nudite kompletan tutorijal).


Ako vam treba pomoć oko dobijanja ovih preduslova, moji drugi tutorijali će pomoći:



https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Kada je sve na svom mestu i imate svoj Fork iz Plan ₿ Network repozitorijuma, možete početi sa dodavanjem tutorijala.


## 1 - Kreiraj novu granu


Otvorite svoj pregledač i idite na svoju Fork stranicu u Plan ₿ Network repozitorijumu. Ovo je Fork koji ste uspostavili na GitHub-u. URL vaše Fork stranice treba da izgleda ovako: `https://github.com/[vaše-korisničko-ime]/Bitcoin-educational-content`:


![GITHUB](assets/fr/01.webp)


Uverite se da ste na glavnoj grani `dev`, zatim kliknite na dugme "*Sync Fork*". Ako vaš Fork nije ažuriran, GitHub će vas zamoliti da ažurirate vašu granu. Nastavite sa ovim ažuriranjem:


![GITHUB](assets/fr/02.webp)


Kliknite na granu `dev`, zatim imenujte svoju radnu granu tako da njen naslov jasno odražava njenu svrhu, koristeći crtice za razdvajanje reči. Na primer, ako je naš cilj da napišemo tutorijal o korišćenju Green Wallet, grana bi mogla biti nazvana: `tuto-Green-Wallet-loic`. Nakon što unesete odgovarajuće ime, kliknite na "*Create branch*" da potvrdite kreiranje vaše nove grane na osnovu `dev`:


![GITHUB](assets/fr/03.webp)


Trebalo bi da sada budete na svojoj novoj grani posla:


![GITHUB](assets/fr/04.webp)


To znači da će sve promene koje napravite biti sačuvane samo na toj specifičnoj grani.


Za svaki novi članak koji planirate objaviti, kreirajte novu granu iz `dev`.


Grana u Gitu predstavlja paralelnu verziju projekta, omogućavajući vam da radite na izmenama bez uticaja na glavnu granu, sve dok vaš rad ne bude spreman za integraciju.


## 2 - Dodaj datoteke za tutorijal


Sada kada je radna grana kreirana, vreme je da integrišete vaš novi tutorijal.


U okviru vaših datoteka grane, potrebno je pronaći odgovarajući podfolder za postavljanje vašeg tutorijala. Organizacija foldera odražava različite sekcije Plan ₿ Network vebsajta. U našem primeru, pošto dodajemo tutorijal na Green Wallet, idite na sledeću putanju: `Bitcoin-educational-content\tutorials\Wallet` koja odgovara `Wallet` sekciji vebsajta:


![GITHUB](assets/fr/05.webp)


U fascikli `Wallet`, kreiraj novi direktorijum specifično posvećen tvom tutorijalu. Ime ovog fascikla treba jasno da označava softver koji se pokriva u tutorijalu, koristeći crtice za povezivanje reči. Za moj primer, fascikl će se zvati `Green-Wallet`. Klikni na "*Add File*" zatim na "*Create new file*":


![GITHUB](assets/fr/06.webp)


Unesite naziv fascikle praćen kosom crtom `/` da biste potvrdili njeno kreiranje kao fascikle.


![GITHUB](assets/fr/07.webp)


U ovom novom podfolderu posvećenom vašem vodiču, potrebno je dodati nekoliko stavki:




- Kreirajte fasciklu `assets` za sve ilustracije potrebne za vaš vodič;
- U okviru ove fascikle `assets`, kreirajte podfasciklu nazvanu prema kodu originalnog jezika tutorijala. Na primer, ako je tutorijal napisan na engleskom, ova podfascikla treba da se zove `en`. Postavite sve vizuale tutorijala (dijagrame, slike, snimke ekrana, itd.) u ovu fasciklu.
- Datoteka `tutorial.yml` mora biti kreirana da zabeleži detalje vašeg tutorijala;
- Datoteka u markdown formatu mora biti kreirana za pisanje stvarnog sadržaja vašeg tutorijala. Ova datoteka mora biti imenovana prema kodu jezika na kojem je napisana. Na primer, za tutorijal napisan na francuskom, datoteka bi trebalo da se zove `fr.md`.


Da rezimiramo, evo hijerarhije datoteka (nastavićemo da ih kreiramo u sledećem odeljku):


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```


## 3 - Popunite YAML datoteku


Hajde da počnemo sa YAML fajlom. U polje za kreiranje novog fajla unesite `tutorial.yml`:


![GITHUB](assets/fr/08.webp)


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



- id**: A UUID (_Universally Unique Identifier_) koji jedinstveno identifikuje tutorijal. Možete ga generate koristiti pomoću [online alata](https://www.uuidgenerator.net/version4). Jedini zahtev je da ovaj UUID bude nasumičan kako bi se izbegli konflikti sa drugim UUID-om na platformi;



- project_id**: The UUID kompanije ili organizacije iza alata predstavljenog u vodiču [sa liste projekata](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Na primer, ako kreirate vodič o Green Wallet softveru, možete pronaći ovaj `project_id` u sledećem fajlu: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Ova informacija se dodaje u vaš YAML fajl vodiča jer Plan ₿ Network održava bazu podataka svih kompanija i organizacija koje rade na Bitcoin ili povezanim projektima. Dodavanjem `project_id` entiteta povezanog sa vašim vodičem, kreirate vezu između dva Elements;



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
    - contributor_names**: Your GitHub ID.
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


Kada završite sa izmenama vašeg `tutorial.yml` fajla, sačuvajte dokument klikom na dugme "*Commit changes...*":


![GITHUB](assets/fr/09.webp)


Dodajte naslov i opis, i osigurajte da je commit napravljen na grani koju ste kreirali na početku ovog tutorijala. Zatim potvrdite klikom na "*Commit changes*".


![GITHUB](assets/fr/10.webp)


## 4 - Kreiranje podfoldera za slike


Kliknite na "*Add File*" ponovo, a zatim na "*Create new file*":


![GITHUB](assets/fr/11.webp)


Unesite `assets` praćeno kosom crtom `/` da biste kreirali fasciklu:


![GITHUB](assets/fr/12.webp)


Ponovite ovaj korak u fascikli `/assets` da biste kreirali podfasciklu za jezik, na primer `fr` ako je vaš vodič na francuskom:


![GITHUB](assets/fr/13.webp)


U ovom folderu, kreiraj lažnu datoteku kako bi naterao GitHub da zadrži tvoj folder (koji bi inače bio prazan). Nazovi ovu datoteku `.gitkeep`. Zatim klikni na "*Commit changes...*".


![GITHUB](assets/fr/14.webp)


Proverite ponovo da ste na ispravnoj grani, zatim kliknite na "*Commit changes*".


![GITHUB](assets/fr/15.webp)


## 5 - Kreiranje Markdown datoteke


Sada ćemo kreirati datoteku koja će sadržati vaš vodič, imenovanu prema vašem jezičkom kodu, na primer `fr.md` ako pišemo na francuskom. Idite u vaš folder za vodiče:


![GITHUB](assets/fr/16.webp)


Kliknite na "Dodaj datoteku*", zatim na "Kreiraj novu datoteku*".


![GITHUB](assets/fr/17.webp)


Nazovite datoteku koristeći kod vašeg jezika. U mom slučaju, pošto je tutorijal napisan na francuskom, nazivam svoju datoteku `fr.md`. Ekstenzija `.md` označava da je datoteka u Markdown formatu.


![GITHUB](assets/fr/18.webp)


Počinjemo popunjavanjem odeljka `Properties` na vrhu dokumenta. Ručno dodajte i popunite sledeći blok koda (ključevi `name:` i `description:` moraju ostati na engleskom, ali njihove vrednosti moraju biti napisane na jeziku koji se koristi za vaš vodič):


```
---
name: [Titre]
description: [Description]
---
```


![GITHUB](assets/fr/19.webp)


Unesite naziv vašeg tutorijala i kratak opis:


![GITHUB](assets/fr/20.webp)


Zatim dodajte putanju do naslovne slike na početku vašeg vodiča. Da biste to uradili, zabeležite:


```
![cover-green](assets/cover.webp)
```


Ova sintaksa će vam biti korisna kad god treba da dodate sliku u vaš vodič. Uzvičnik označava sliku, čiji je alternativni tekst (alt) naveden između uglastih zagrada. Putanja do slike je navedena između zagrada:


![GITHUB](assets/fr/21.webp)


Kliknite na dugme "*Commit changes...*" da biste sačuvali ovu datoteku.


![GITHUB](assets/fr/22.webp)


Proverite da ste na pravoj grani, zatim potvrdite commit.


![GITHUB](assets/fr/23.webp)


Vaš folder za tutorijale sada bi trebao izgledati ovako, prema vašem kodu jezika:


![GITHUB](assets/fr/24.webp)


## 6 - Dodaj logo i naslovnu stranu


U okviru fascikle `assets`, potrebno je dodati datoteku pod nazivom `logo.webp`, koja će služiti kao sličica za vaš članak. Ova slika mora biti u formatu `.webp` i mora biti kvadratnog oblika kako bi odgovarala korisniku Interface.


Slobodno izaberite logo softvera koji se koristi u tutorijalu, ili bilo koju drugu relevantnu sliku, sve dok je bez autorskih prava. Pored toga, dodajte sliku pod nazivom `cover.webp` na isto mesto. Ova slika će biti prikazana na vrhu vašeg tutorijala. Uverite se da ova slika, kao i logo, poštuje prava korišćenja i da je prikladna za kontekst vašeg tutorijala.


Da biste dodali slike u folder `/assets`, možete ih prevući i ispustiti iz svojih lokalnih fajlova. Uverite se da ste u folderu `/assets` i na pravoj grani, zatim kliknite na "*Commit changes*".


![GITHUB](assets/fr/26.webp)


Sada biste trebali videti slike u fascikli.


![GITHUB](assets/fr/27.webp)


## 7 - Pisanje tutorijala


Nastavite pisanje svog vodiča beleženjem sadržaja u Markdown datoteku sa kodom jezika (u mom primeru, na francuskom, to je `fr.md` datoteka). Idite na datoteku i kliknite na ikonu olovke:


![GITHUB](assets/fr/28.webp)


Počnite pisati svoj vodič. Kada dodajete podnaslov, koristite odgovarajuće Markdown formatiranje tako što ćete tekstu dodati prefiks `##`.


![GITHUB](assets/fr/29.webp)


Naizmenično koristite "*Edit*" i "*Preview*" prikaze kako biste bolje vizualizovali renderovanje.


![GITHUB](assets/fr/30.webp)


Da biste sačuvali svoj rad, kliknite na "*Commit Changes...*", uverite se da ste na pravoj grani, zatim potvrdite klikom na "*Commit Changes*" ponovo.


![GITHUB](assets/fr/31.webp)


## 8 - Dodajte vizuale


Jezički podfolder u folderu `/assets` (u mom primeru: `/assets/en`) koristi se za čuvanje dijagrama i vizuala koji će pratiti vaš tutorijal. Koliko god je moguće, izbegavajte uključivanje teksta u vaše slike kako biste učinili sadržaj dostupnim međunarodnoj publici. Naravno, softver koji se prikazuje će sadržati tekst, ali ako dodajete šeme ili dodatne indikacije na snimcima ekrana softvera, učinite to bez teksta ili, ako je neophodno, koristite engleski.


Da biste imenovali svoje slike, jednostavno koristite brojeve koji odgovaraju njihovom redosledu pojavljivanja u vodiču, formatirane kao dve cifre (ili tri cifre ako vaš vodič sadrži više od 99 slika). Na primer, imenujte svoju prvu sliku `01.webp`, drugu `02.webp`, i tako dalje.


Vaše slike moraju biti samo u formatu `.webp`. Ako je potrebno, možete koristiti [moj softver za konverziju slika](https://github.com/LoicPandul/ImagesConverter).


![GITHUB](assets/fr/32.webp)


Sada kada ste dodali svoje slike u podfolder, možete obrisati lažnu datoteku `.gitkeep`. Otvorite ovu datoteku, kliknite na tri mala tačkice u gornjem desnom uglu, zatim na "*Delete file*".


![GITHUB](assets/fr/33.webp)


Sačuvajte svoje izmene klikom na "*Commit changes...*".


![GITHUB](assets/fr/34.webp)


Da biste umetnuli dijagram iz vaše podmape u vaš urednički dokument, koristite sledeću Markdown komandu, vodeći računa da navedete odgovarajući alternativni tekst i tačan put do slike za vaš jezik:


```
![green](assets/fr/01.webp)
```


Uzvičnik na početku označava sliku. Alternativni tekst, koji pomaže pristupačnosti i referenciranju, stavlja se između uglastih zagrada. Na kraju, putanja do slike je naznačena između zagrada.


![GITHUB](assets/fr/35.webp)


Ako želite da kreirate sopstvene šeme, obavezno pratite Plan ₿ Network grafičke smernice kako biste osigurali vizuelnu doslednost:




- Font**: Koristite [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- Boje**:
 - Narandžasta: #FF5C00
 - Crna: #000000
 - Bela: #FFFFFF


**Važno je da svi vizuali integrisani u vaše tutorijale budu bez autorskih prava ili da poštuju licencu izvornog fajla**. Stoga su svi dijagrami objavljeni na Plan ₿ Network dostupni pod CC-BY-SA licencom, na isti način kao i tekst.


**-> Savet:** Kada delite datoteke javno, kao što su slike, važno je ukloniti suvišne metapodatke. Oni mogu sadržati osetljive informacije, kao što su podaci o lokaciji, datumi kreiranja i detalji o autoru. Da biste zaštitili svoju privatnost, dobra je ideja ukloniti ove metapodatke. Da biste pojednostavili ovu operaciju, možete koristiti specijalizovane alate kao što je [Exif Cleaner](https://exifcleaner.com/), koji vam omogućava da očistite metapodatke dokumenta jednostavnim prevlačenjem i ispuštanjem.


## 9 - Predložite vodič


Kada završite pisanje svog tutorijala na jeziku po vašem izboru, sledeći korak je da podnesete **Pull Request**. Administrator će zatim dodati nedostajuće prevode vašem tutorijalu, koristeći našu automatizovanu metodu prevođenja uz ljudsku proveru.


Da biste nastavili sa Pull Request-om, nakon što sačuvate sve svoje izmene, kliknite na dugme "*Contribute*", zatim na "*Open pull request*":


![GITHUB](assets/fr/36.webp)


Zahtev za povlačenje je zahtev za integraciju izmena iz vaše grane u glavnu granu repozitorijuma Plan ₿ Network, što omogućava pregled i diskusiju o izmenama pre nego što budu spojene.


Pre nego što nastavite, pažljivo proverite na dnu Interface da li su ove promene ono što ste očekivali:


![GITHUB](assets/fr/37.webp)


Uverite se da je, na vrhu Interface, vaša radna grana spojena na `dev` granu repozitorijuma Plan ₿ Network (koja je glavna grana).


Unesite naslov koji ukratko rezimira izmene koje želite da spojite sa izvornim repozitorijumom. Dodajte kratak komentar koji opisuje ove izmene (ako imate broj problema povezan sa kreiranjem vašeg tutorijala, ne zaboravite da navedete `Closes #{issue number}` kao komentar), zatim kliknite na Green dugme "*Create pull request*" da potvrdite zahtev za spajanje:


![GITHUB](assets/fr/38.webp)


Vaš PR će tada biti vidljiv na kartici "*Pull Request*" glavnog repozitorijuma Plan ₿ Network. Sve što sada treba da uradite je da sačekate da vas administrator kontaktira kako bi potvrdio da je vaš doprinos spojen, ili da zatraži bilo kakve dodatne izmene.


![GITHUB](assets/fr/39.webp)


Nakon spajanja vašeg PR-a sa glavnom granom, preporučujemo brisanje vaše radne grane (u mom primeru: `tuto-Green-Wallet`) kako biste održali čistu istoriju vašeg Fork. GitHub će vam automatski ponuditi ovu opciju na vašoj PR stranici:


![GITHUB](assets/fr/40.webp)


Ako želite da izvršite izmene u svom doprinosu nakon što ste već poslali svoj PR, koraci koje treba slediti zavise od trenutnog statusa vašeg PR-a:




- Ako je vaš PR još uvek otvoren i nije spojen, napravite izmene na istoj radnoj grani. Izmene u commitu će biti dodate vašem još uvek otvorenom PR-u;
- U slučaju da je vaš PR već spojen sa glavnom granom, moraćete da ponovite proces od početka kreiranjem nove grane, a zatim podnošenjem novog PR-a. Uverite se da je vaš Fork sinhronizovan sa Plan ₿ Network izvornim repozitorijumom na `dev` grani pre nego što nastavite.


Ako imate tehničkih poteškoća sa slanjem vašeg tutorijala, slobodno zatražite pomoć na [našoj posvećenoj Telegram grupi za doprinose](https://t.me/PlanBNetwork_ContentBuilder). Hvala vam puno!