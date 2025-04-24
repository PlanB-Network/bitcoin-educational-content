---
name: Doprinos - Git vodič (napredni)
description: Vodič za napredne korisnike za pružanje tutorijala o Plan ₿ Network sa Git-om
---
![cover](assets/cover.webp)


Pre nego što pratite ovaj vodič o dodavanju novog vodiča, potrebno je da završite nekoliko preliminarnih koraka. Ako to već niste učinili, molimo vas da prvo pogledate ovaj uvodni vodič, a zatim se vratite ovde :


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Već imate :



- Izaberite temu za vaš vodič;
- Kontaktirao sam Plan ₿ Network tim putem [Telegram grupe](https://t.me/PlanBNetwork_ContentBuilder) ili paolo@planb.network ;
- Izaberite svoje alate za doprinos.


U ovom vodiču za iskusne korisnike Git-a, ukratko ćemo rezimirati ključne korake i osnovne smernice za ponudu novog Plan ₿ Network vodiča. Ako niste upoznati sa Git-om i GitHub-om, preporučujem da umesto toga pratite jedan od ova 2 detaljnija vodiča koji će vas voditi korak po korak :



- Srednji nivo (GitHub Desktop) :


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- Početnici (web Interface) :


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Predloženi alati


Za uređivanje Markdown datoteka :



- Obsidian (Besplatan, nije otvorenog koda)
- Mark Text (Besplatno, otvorenog koda)
- Zettlr (Besplatan, otvorenog koda)
- Typora (komercijalni softver, ~€15, nije otvorenog koda)


Za Git :



- Git (Besplatan, otvorenog koda)
- GitHub Desktop (Besplatno, otvorenog koda)
- Sourcetree (Besplatno, nije otvorenog koda)


Za uređivanje YAML datoteka :



- Visual Studio Code (Besplatan, otvorenog koda)
- Sublime Text (Besplatan sa ograničenjima, nije otvorenog koda)


Da biste kreirali dijagrame i vizuale :



- Canva (Besplatno sa plaćenim opcijama, nije otvorenog koda)
- Inkscape (Besplatan, otvorenog koda)
- Penpot (Besplatan, otvorenog koda)


## Tokovi posla


### 1 - Konfigurišite vaše lokalno okruženje



- Morate imati svoj Fork iz [Plan ₿ Network repozitorijuma na GitHub-u](https://github.com/PlanB-Network/Bitcoin-educational-content).
- Sinhronizujte glavnu granu (`dev`) vašeg Fork sa izvornim repozitorijumom.
- Ažurirajte svoju lokalnu kloniranu verziju.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - Kreiraj novu granu



- Uverite se da ste na `dev` grani.
- Kreiraj novu granu sa opisnim imenom (npr. `tuto-Green-Wallet-loic`).
- Objavi ovu granu na svom online Fork.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - Dodajte dokumente za tutorijal


***Napomena:*** Možete automatizovati korake 3 i 4 koristeći [moj Python GUI skript](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Pokrenite ga direktno iz njegove fascikle u vašoj lokalnoj kloniranoj verziji, zatim popunite potrebna polja na GUI. Za više informacija o tome kako ga instalirati i koristiti, pogledajte [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


Ako više volite da to uradite ručno, pratite ove korake :



- Pronađite odgovarajući folder u lokalnom repozitorijumu (npr. `tutorials/Wallet`).
- Kreirajte direktorijum posvećen vodiču sa jasnim imenom (npr. `gw-14-gw-13`). Ovo ime foldera će takođe odrediti URL putanju vodiča. Trebalo bi da bude u malim slovima, bez specijalnih karaktera (osim crtica) i bez razmaka.
- Dodajte sledeće stavke u ovaj direktorijum:
    - Poddirektorijum pod nazivom `assets` koji sadrži :
        - Dve `.webp` slike:
            - `logo.webp`: Logo za tutorijal (kvadratni format sa pozadinom). Ovaj logo mora predstavljati softver ili alat koji se prezentuje. Ako tutorijal nije specifičan za neki alat (npr.: opšti vodič za generisanje Mnemonic fraze), možete izabrati odgovarajući vizual (npr.: generička ikonica).
            - `cover.webp`: Naslovna slika prikazana na početku tutorijala.
        - Poddirektorijum sa kodom originalnog jezika tutorijala. Na primer, ako je tutorijal napisan na engleskom jeziku, ovaj poddirektorijum treba da se zove `en'. Postavite sve vizuelne elemente tutorijala (dijagrame, slike, snimke ekrana, itd.) u ovaj direktorijum.
    - Datoteka `tutorial.yml` koja sadrži metapodatke (autor, oznake, kategorija, nivo težine, itd.).
    - Datoteka u Markdown formatu koja sadrži vodič, imenovana prema kodu jezika (npr. `fr.md`, `en.md`, itd.).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - Popunite YAML datoteku



- Dovršite datoteku `tutorial.yml` na sledeći način:


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



- id** : A UUID (_Universally Unique Identifier_) koji jedinstveno identifikuje tutorijal. Možete ga generate koristiti pomoću [online alata](https://www.uuidgenerator.net/version4). Jedini zahtev je da ovaj UUID bude nasumičan kako bi se izbegli konflikti sa drugim UUID-om na platformi;



- project_id** : UUID kompanije ili organizacije iza alata predstavljenog u tutorijalu [sa liste projekata](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Na primer, ako kreirate tutorijal o Green Wallet softveru, možete pronaći ovaj `project_id` u sledećoj datoteci: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Ova informacija se dodaje u YAML datoteku vašeg tutorijala jer Plan ₿ Network održava bazu podataka svih kompanija i organizacija koje rade na Bitcoin ili povezanim projektima. Dodavanjem `project_id` entiteta povezanog sa vašim tutorijalom, kreirate vezu između dva Elements;



- tagovi** : 2 ili 3 relevantne ključne reči povezane sa sadržajem tutorijala, isključivo odabrane [sa Plan ₿ Network liste tagova](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- kategorija** : Podkategorija koja odgovara sadržaju tutorijala, prema strukturi sajta Plan ₿ Network (na primer, za novčanike: `desktop`, `hardware`, `mobile`, `backup`);



- nivo** : Nivo težine tutorijala, izabran iz:
    - `početnik`
    - `srednji`
    - `napredan`
    - `stručnjak`



- professor_id** : Vaš `professor_id` (UUID) kako je prikazan na [vašem profesorskom profilu](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors);



- original_language** : Originalni jezik tutorijala (npr. `fr`, `en`, itd.);



- lektura** : Informacije o procesu lekture. Završite prvi deo, jer lektura sopstvenog tutorijala se računa kao prva validacija:
    - jezik** : Jezički kod za lekturu (npr., `fr`, `en`, itd.).
    - last_contribution_date** : Datum dana.
    - hitnost** : 1
    - contributor_names** : Your GitHub ID.
    - nagrada** : 0


Za više detalja o vašem ID-u nastavnika, molimo vas da pogledate odgovarajući vodič :


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


### 5 - Napiši sadržaj



- Dovršite svojstva Markdown datoteke sa:
    - Naslov (`name`).
    - Kratak opis (`description`).
- Dodajte naslovnu sliku na vrh tutorijala koristeći Markdown sintaksu (zamenite "Green" imenom prikazanog alata):

```markdown
![Green](path/to/your/image.jpg)
```


```
![cover-green](assets/cover.webp)
```



- Napišite sadržaj vodiča u Markdown formatu:
    - Koristite dobro strukturirane naslove (`##`), liste i paragrafe.
    - Umetnite vizuale koristeći Markdown sintaksu:


```
![nom-image](assets/en/001.webp)
```




- Postavite dijagrame i slike u odgovarajući podfolder jezika, u `/assets`.


### 6 - Sačuvaj i pošalji tutorijal



- Sačuvaj svoje izmene lokalno kreiranjem commita sa opisnom porukom.
- Pritisni promene na svoj GitHub Fork.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- Kada završite, kreirajte Pull Request (PR) na GitHub-u kako biste predložili integraciju vaših izmena.
- Dodajte naslov i kratak opis PR-u. Navedite odgovarajući broj problema u komentaru.


### 7 - Lektorisanje i spajanje



- Sačekajte validaciju ili povratne informacije od administratora.
- Ako je potrebno, izvrši ispravke i pošalji nove izmene.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- Kada je PR spojen, možete obrisati svoju radnu granu.


## Standardi za kreiranje sadržaja



- Formatiranje podržano na platformi** :
    - Klasični Markdown: liste, linkovi, slike, citati, **bold**, *italik*, itd.
    - LaTeX (blok samo, ne inline): ograničeno sa `$$`.
    - Umetnuti kod: Sintaksa sa jednim obrnutim apostrofom.
    - Blokovi koda: Sintaksa sa tri obrnutih navodnika, na primer :


```
print("Hello, Bitcoin!")
```



- Ilustracije i dijagrami** :
    - Sve slike moraju biti u WebP formatu. Koristite ovaj besplatni alat za konvertovanje ako je potrebno: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Imenujte vizuale sa 2 ili 3 cifre (npr. `001.webp`, `002.webp`).
    - Za mobilne ili Hardware Wallet tutorijale, koristite makete.
    - Koristite samo vizuale koje ste sami kreirali ili one koji su oslobođeni autorskih prava.
    - Uverite se da su relevantni i visokog kvaliteta.
- Grafička povelja** :
    - Font: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Boje Plan ₿ Network :
        - Narandžasta: `#FF5C00`
        - Crna: `#000000`
        - Bela: `#FFFFFF`


Ako imate tehničkih poteškoća prilikom predaje vašeg tutorijala, molimo vas da se ne ustručavate da zatražite pomoć na [našoj posvećenoj Telegram grupi za doprinose](https://t.me/PlanBNetwork_ContentBuilder). Hvala vam puno!