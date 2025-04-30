---
name: GitHub Desktop
description: Kako postaviti lokalno radno okruženje?
---
![github](assets/cover.webp)


Misija PlanB-a je da obezbedi vrhunske obrazovne resurse o Bitcoin na što više jezika. Sav sadržaj objavljen na sajtu je otvorenog koda i hostovan na GitHub-u, što omogućava svakome da učestvuje u obogaćivanju platforme. Doprinosi mogu biti u različitim oblicima: ispravljanje i lektura postojećih tekstova, prevođenje na druge jezike, ažuriranje informacija ili kreiranje novih tutorijala koji još nisu dostupni na našem sajtu.


Ako želite da doprinesete PlanB mreži, biće potrebno da koristite GitHub za predlaganje izmena. Da biste to uradili, imate dve opcije:


- Doprinesite direktno putem GitHub-ovog web Interface**: Ovo je najjednostavnija metoda. Ako ste početnik ili planirate da napravite samo nekoliko manjih doprinosa, ova opcija je verovatno najbolja za vas;
- Doprinosite lokalno koristeći Git**: Ova metoda je pogodnija ako planirate da redovno ili značajno doprinosite PlanB mreži. Iako postavljanje vašeg lokalnog Git okruženja na računaru može delovati složeno na početku, ovaj pristup je efikasniji na duže staze. Omogućava fleksibilnije upravljanje promenama. Ako ste novi u ovome, ne brinite, **objašnjavamo ceo proces postavljanja vašeg okruženja u ovom vodiču** (obećavamo, nećete morati da kucate bilo kakve komandne linije ^^).


Ako nemate pojma šta je GitHub, ili ako želite da saznate više o tehničkim terminima vezanim za Git i GitHub, preporučujem da pročitate naš uvodni članak kako biste se upoznali sa ovim konceptima.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c




- Da biste započeli, očigledno će vam biti potreban GitHub nalog. Ako ga već imate, možete se prijaviti, u suprotnom, možete koristiti naš vodič za kreiranje novog.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



## Korak 1: Instalirajte GitHub Desktop



- Idite na https://desktop.github.com/ da preuzmete GitHub Desktop softver. Ovaj softver vam omogućava da lako komunicirate sa GitHub-om, bez potrebe za korišćenjem terminala:

![github-desktop](assets/1.webp)


- Kada prvi put pokrenete softver, od vas će biti zatraženo da povežete svoj GitHub nalog. Da biste to uradili, kliknite na `Sign in to GitHub.com`:

![github-desktop](assets/2.webp)


- Stranica za autentifikaciju će se otvoriti u vašem pregledaču. Unesite svoj email Address i lozinku odabranu prilikom kreiranja naloga, zatim kliknite na dugme `Sign in`:

![github-desktop](assets/3.webp)


- Kliknite na `Authorize desktop` da potvrdite vezu između vašeg naloga i softvera:

![github-desktop](assets/4.webp)


- Automatski ćete biti preusmereni na GitHub Desktop softver. Kliknite na `Finish`: ![github-desktop](assets/5.webp)
- Ako ste upravo kreirali svoj GitHub nalog, bićete preusmereni na stranicu koja pokazuje da još niste kreirali nijedan repozitorijum. U ovom trenutku, ostavite GitHub Desktop softver po strani; vratićemo mu se kasnije: ![github-desktop](assets/6.webp)


## Korak 2: Instalirajte Obsidian


Hajde da pređemo na instaliranje softvera za pisanje. Ovde imate nekoliko opcija. Biće vam potreban softver koji podržava uređivanje Markdown fajlova, jer PlanB Network koristi ovaj format za tekstualne fajlove u svom repozitorijumu.


Postoji mnoštvo softvera specijalizovanih za uređivanje Markdown fajlova, kao što je Typora, dizajniran specifično za pisanje. Iako nije idealno, moguće je izabrati i uređivač koda, kao što su Visual Studio Code (VSC) ili Sublime Text. Međutim, kao pisac, preferiram da koristim Obsidian softver. Hajde da zajedno vidimo kako da ga instaliramo i počnemo sa korišćenjem.



- Idite na https://obsidian.md/download i preuzmite softver: ![github-desktop](assets/7.webp)
- Instalirajte Obsidian, pokrenite softver, izaberite svoj jezik, a zatim kliknite na `Quick Start`: ![github-desktop](assets/8.webp)
- Stići ćete do Obsidian softvera. Za sada nemate otvorenih fajlova: ![github-desktop](assets/9.webp)


## Korak 3: Fork PlanB Network repozitorijum



- Idite u PlanB Network repozitorijum podataka na sledećem Address: [https://github.com/PlanB-Network/Bitcoin-educational-content](https://github.com/PlanB-Network/Bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Sa ove stranice, kliknite na dugme `Fork` u gornjem desnom uglu prozora: ![github-desktop](assets/11.webp)
- U meniju za kreiranje, možete ostaviti podrazumevana podešavanja. Uverite se da je polje `Copy the dev branch only` označeno, zatim kliknite na dugme `Create Fork`: ![github-desktop](assets/12.webp)
- Stići ćete zatim do sopstvenog Fork repozitorijuma PlanB mreže: ![github-desktop](assets/13.webp)

Ovaj Fork predstavlja poseban repozitorijum od originalnog, iako trenutno sadrži iste podatke. Sada ćete raditi na ovom novom repozitorijumu.


Na neki način, napravili smo kopiju izvornog repozitorijuma PlanB Network. Vaš Fork (kopija) i originalni repozitorijum će sada evoluirati nezavisno jedan od drugog. Na originalnom repozitorijumu, drugi saradnici mogu dodavati nove podatke, dok ćete vi, na vašem Fork, nastaviti sa sopstvenim izmenama.

Da bi se održala doslednost između ova dva repozitorijuma, biće neophodno da ih periodično sinhronizujete kako bi preuzimali iste informacije. Da biste poslali svoje izmene u izvorni repozitorijum, koristićete ono što se zove **Pull Request**. A da biste integrisali izmene iz izvornog repozitorijuma u vaš Fork, koristićete komandu **Sync Fork** dostupnu na GitHub web Interface.

![github-desktop](assets/14.webp)


## Korak 4: Kloniraj Fork



- Vratite se na GitHub Desktop softver. Do sada bi vaš Fork trebao da se pojavi u sekciji `Your repositories`. Ako ga ne vidite odmah, koristite dugme sa dvostrukom strelicom da osvežite listu. Kada se vaš Fork pojavi, kliknite na njega da ga izaberete:

![github-desktop](assets/15.webp)


- Zatim kliknite na plavo dugme: `Clone [username]/Bitcoin-educational-content`:

![github-desktop](assets/16.webp)


- Zadržite podrazumevanu putanju. Da potvrdite, kliknite na plavo dugme `Clone`:

![github-desktop](assets/17.webp)


- Sačekajte dok GitHub Desktop klonira vaš Fork lokalno:

![github-desktop](assets/18.webp)


- Nakon kloniranja repozitorijuma, softver vam nudi dve opcije. Morate izabrati prvu: `To contribute to the parent project`. Ovaj izbor će vam omogućiti da predstavite svoj budući rad kao doprinos glavnom projektu (`PlanB-Network/Bitcoin-educational-content`), a ne isključivo kao modifikaciju vašeg ličnog Fork (`[username]/Bitcoin-educational-content`). Kada izaberete opciju, kliknite na `Continue`:

![github-desktop](assets/19.webp)


- Vaš GitHub Desktop je sada ispravno konfigurisan. Sada možete ostaviti softver otvorenim u pozadini kako biste pratili izmene koje ćemo napraviti.

![github-desktop](assets/20.webp)

Ono što smo postigli u ovoj fazi je kreiranje lokalne kopije vašeg repozitorijuma, koji je hostovan na GitHub-u. Kao podsetnik, ovaj repozitorijum je Fork izvornog repozitorijuma PlanB Network-a. Moći ćete da izvršite izmene na ovoj lokalnoj kopiji, kao što su dodavanje tutorijala, prevoda ili ispravki. Kada te izmene budu napravljene, koristićete komandu **Push origin** da pošaljete svoje lokalne izmene na vaš Fork hostovan na GitHub-u.


Možete takođe preuzeti izmene sa Fork, na primer, tokom sinhronizacije sa PlanB Network repozitorijumom. Za ovo ćete koristiti komandu **Fetch origin** da preuzmete izmene na vašu lokalnu kopiju (vaš klon), a zatim komandu **Pull origin** da ih spojite sa vašim radom. Ovo vam omogućava da budete u toku sa najnovijim razvojem projekta dok efektivno doprinosite.


![github-desktop](assets/21.webp)

## Korak 5: Kreirajte novi Obsidian trezor



- Otvorite Obsidian softver i kliknite na malu ikonu trezora u donjem levom uglu prozora:

![github-desktop](assets/22.webp)


- Kliknite na dugme `Open` da otvorite postojeću fasciklu kao trezor: ![github-desktop](assets/23.webp)
- Vaš istraživač datoteka će se otvoriti. Treba da pronađete i izaberete folder pod nazivom `GitHub`, koji bi trebalo da se nalazi u vašem direktorijumu `Documents` među vašim datotekama. Ova putanja odgovara onoj koju ste uspostavili tokom koraka 4. Nakon što izaberete folder, potvrdite njegov izbor. Kreiranje vašeg trezora na Obsidian-u će se zatim pokrenuti na novoj stranici softvera:


![github-desktop](assets/24.webp)

-> **Pažnja**, važno je ne birati fasciklu `Bitcoin-educational-content` prilikom kreiranja novog trezora u Obsidian-u. Umesto toga, izaberite nadređenu fasciklu, `GitHub`. Ako izaberete fasciklu `Bitcoin-educational-content`, konfiguraciona fascikla `.obsidian`, koja sadrži vaša lokalna Obsidian podešavanja, automatski će biti integrisana u repozitorijum. Želimo da to izbegnemo, jer nije potrebno prenositi vaša Obsidian podešavanja u PlanB Network repozitorijum. Alternativa je dodavanje fascikle `.obsidian` u `.gitignore` fajl, ali bi ovaj metod takođe izmenio `.gitignore` fajl izvornog repozitorijuma, što nije poželjno.



- Na levoj strani prozora možete videti stablo fajlova sa vašim različitim GitHub repozitorijumima koji su lokalno klonirani.
- Klikom na strelice pored imena fascikli, možete ih proširiti kako biste pristupili podfasciklama repozitorijuma i njihovim dokumentima:

![github-desktop](assets/25.webp)


- Ne zaboravi da podesiš Obsidian na tamni režim: "Svetlost privlači bube" ;)


## Korak 6: Instalirajte uređivač koda


Većina vaših izmena će biti na fajlovima u Markdown formatu (`.md`). Da biste uredili ove dokumente, možete koristiti Obsidian, softver o kojem smo ranije razgovarali. Međutim, PlanB Network koristi druge formate fajlova, i biće potrebno da neke od njih modifikujete.


Na primer, kada kreirate novi tutorijal, biće potrebno da kreirate YAML (`.yml`) fajl kako biste uneli oznake za vaš tutorijal, njegov naslov i vaš ID predavača. Obsidian ne nudi mogućnost modifikacije ove vrste fajlova, tako da će vam biti potreban uređivač koda.


Za ovo vam je dostupno nekoliko opcija. Iako se standardni notepad vašeg računara može koristiti za ove izmene, ovo rešenje nije idealno za uredan rad. Preporučujem da izaberete softver posebno dizajniran za ovu svrhu, kao što su [VS Code](https://code.visualstudio.com/download) ili [Sublime Text](https://www.sublimetext.com/download). Sublime Text, budući da je posebno lagan, biće više nego dovoljan za naše potrebe.


- Instalirajte jedan od ovih softverskih programa i ostavite ga po strani za vaše buduće izmene. ![github-desktop](assets/26.webp)

Čestitamo! Vaše radno okruženje je sada postavljeno za doprinos PlanB mreži. Sada možete istražiti naše druge specifične vodiče za svaku vrstu doprinosa (prevođenje, lektura, pisanje).


https://planb.network/tutorials/others

..).