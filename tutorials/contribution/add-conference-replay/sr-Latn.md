---
name: Dodavanje snimka konferencije
description: Kako dodati reprizu konferencije na PlanB Network?
---
![conference](assets/cover.webp)


Misija PlanB-a je da obezbedi vrhunske obrazovne resurse o Bitcoin na što više jezika. Sav sadržaj objavljen na sajtu je otvorenog koda i hostovan na GitHub-u, omogućavajući svakome da doprinese obogaćivanju platforme.


Želite li dodati snimak vaše Bitcoin konferencije na PlanB Network sajt i dati vidljivost ovom događaju, ali ne znate kako? Ovaj vodič je za vas!


Međutim, ako želite da dodate konferenciju koja će se održati u budućnosti, savetujem vam da pročitate ovaj drugi vodič u kojem objašnjavamo kako da dodate novi događaj na sajt.


https://planb.network/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- Prvo, potrebno je da imate nalog na GitHub-u. Ako ne znate kako da kreirate nalog, napravili smo detaljan vodič da vas uputimo.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Idite na [GitHub repozitorijum PlanB posvećen podacima](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) u sekciji `resources/conference/`:

![conference](assets/02.webp)


- Kliknite u gornjem desnom uglu na dugme `Add file`, zatim na `Create new file`:

![conference](assets/03.webp)


- Ako nikada ranije niste doprineli sadržaju PlanB mreže, biće potrebno da kreirate svoj Fork originalnog repozitorijuma. Forkovanje repozitorijuma znači kreiranje kopije tog repozitorijuma na vašem GitHub nalogu, što vam omogućava da radite na projektu bez uticaja na originalni repozitorijum. Kliknite na dugme `Fork this repository`:

![conference](assets/04.webp)


- Zatim ćete stići na GitHub stranicu za uređivanje:

![conference](assets/05.webp)


- Kreirajte fasciklu za vašu konferenciju. Da biste to uradili, u polje `Name your file...` upišite naziv vaše konferencije malim slovima sa crticama umesto razmaka. Na primer, ako se vaša konferencija zove "Paris Bitcoin Conference", treba da zabeležite `paris-Bitcoin-conference`. Takođe dodajte godinu vaše konferencije, na primer: `paris-Bitcoin-conference-2024`:

![conference](assets/06.webp)


- Da biste potvrdili kreiranje fascikle, jednostavno zabeležite kosu crtu nakon vašeg imena u istom polju, na primer: `paris-Bitcoin-conference-2024/`. Dodavanje kose crte automatski kreira fasciklu umesto fajla:

![conference](assets/07.webp)


- U ovom folderu, kreiraćete prvi YAML fajl pod nazivom `conference.yml`:

![conference](assets/08.webp)

Popunite ovaj fajl informacijama vezanim za vašu konferenciju koristeći ovaj šablon:

```yaml
year:
name:
builder:
location:
language:
-
links:
website:
twitter:
tags:
-
-
```


Na primer, vaš YAML fajl može izgledati ovako:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


Ako još nemate "*builder*" identifikator za vašu organizaciju, možete ga dodati prateći ovaj drugi vodič.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Kada završite sa izmenama u ovoj datoteci, sačuvajte ih klikom na dugme `Commit changes...`:

![conference](assets/10.webp)


- Dodajte naslov za vaše izmene, kao i kratak opis:

![conference](assets/11.webp)


- Kliknite na dugme Green `Predloži izmene`:

![conference](assets/12.webp)


- Zatim ćete stići na stranicu koja sumira sve vaše promene:

![conference](assets/13.webp)


- Kliknite na svoju GitHub profilnu sliku u gornjem desnom uglu, zatim na `Your Repositories`:

![conference](assets/14.webp)


- Odaberite svoj Fork iz PlanB Network repozitorijuma:

![conference](assets/15.webp)


- Trebalo bi da vidite obaveštenje na vrhu prozora sa vašom novom granom. Verovatno se zove `patch-1`. Kliknite na nju:

![conference](assets/16.webp)


- Sada ste na svojoj radnoj grani:

![conference](assets/17.webp)


- Vratite se u folder `resources/conference/` i izaberite folder vaše konferencije koji ste upravo kreirali u prethodnom commitu:

![conference](assets/18.webp)


- U fascikli vaše konferencije, kliknite na dugme `Add file`, zatim na `Create new file`:

![conference](assets/19.webp)


- Nazovi ovu novu fasciklu `assets` i potvrdi njeno kreiranje stavljanjem kosa crta `/` na kraj:

![conference](assets/20.webp)


- U ovom folderu `assets`, kreiraj fajl pod nazivom `.gitkeep`:

![conference](assets/21.webp)


- Kliknite na dugme `Commit changes...`:

![conference](assets/22.webp)


- Ostavite naslov commita kao podrazumevani, i proverite da je opcija `Commit directly to the patch-1 branch` označena, zatim kliknite na `Commit changes`:

![conference](assets/23.webp)


- Vratite se u fasciklu `assets`:

![conference](assets/24.webp)


- Kliknite na dugme `Add file`, zatim na `Upload files`:

![conference](assets/25.webp)


- Otvara se nova stranica. Prevucite i otpustite sliku koja predstavlja vašu konferenciju i biće prikazana na PlanB Network sajtu: ![conference](assets/26.webp)
- Može biti logo, sličica ili čak poster:

![conference](assets/27.webp)


- Kada se slika otpremi, proverite da li je polje `Commit directly to the patch-1 branch` označeno, zatim kliknite na `Commit changes`:

![conference](assets/28.webp)


- Budite pažljivi, vaša slika mora biti nazvana `thumbnail` i mora biti u `.webp` formatu. Puno ime fajla treba da bude: `thumbnail.webp`:

![conference](assets/29.webp)


- Vratite se u svoj folder `assets` i kliknite na posrednički fajl `.gitkeep`:

![conference](assets/30.webp)


- Kada otvorite datoteku, kliknite na 3 male tačke u gornjem desnom uglu, a zatim na `Delete file`:

![conference](assets/31.webp)


- Potvrdite da ste i dalje na istoj radnoj grani, zatim kliknite na dugme `Commit changes`:

![conference](assets/32.webp)


- Dodajte naslov i opis vašoj izmeni, zatim kliknite na `Commit changes`:

![conference](assets/33.webp)


- Vrati se u svoj konferencijski folder:

![conference](assets/34.webp)


- Kliknite na dugme `Add file`, zatim na `Create new file`:

![conference](assets/35.webp)


- Napravite novu markdown (.md) datoteku tako što ćete je imenovati indikatorom vašeg maternjeg jezika. Ova datoteka će se koristiti za reprize vaše konferencije. Na primer, ako želim da napišem opise konferencija na engleskom, nazvaću ovu datoteku en.md:

![conference](assets/36.webp)


- Ispunite ovu markdown datoteku koristeći ovaj šablon koji možete prilagoditi konfiguraciji vaše konferencije:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- Na početku vašeg dokumenta, u "front matter," popunite polje `name:` imenom vaše konferencije i godinom repriza. U polju `description:` napišite kratak opis vašeg događaja na jeziku datoteke. Na primer, za datoteku pod nazivom `en.md`, opis treba da bude na engleskom. Tim PlanB Network će se pobrinuti za prevođenje vašeg opisa koristeći njihov model.
- Naslovi prvog nivoa, označeni sa `#`, koriste se za organizaciju konferencije po scenama. Na primer, `# Glavna scena` za glavnu scenu i `# Radionica` za scenu posvećenu radionicama.



- Drugi nivo naslova, označen dvostrukim `##`, koristi se za razdvajanje različitih video snimaka repriza. Ako su konferencije snimane kontinuirano tokom pola dana, navedite, na primer, `## Petak ujutru`. Ako su konferencije snimane i emitovane pojedinačno, imenujte konferenciju direktno sa naslovom drugog nivoa.



- Pod svaki naslov drugog nivoa, umetnite link ka odgovarajućem video snimku. Sintaksa treba da bude: `![video](https://youtu.be/XXXXXXXXXXXX)`, zamenjujući `XXXXXXXXXXXX` stvarnim linkom video snimka.



- Ako format dozvoljava (pojedinačne konferencije), možete dodati imena govornika. Da biste to uradili, dodajte polje `Govornik:` praćeno imenom ili pseudonimom govornika ispod linka za video. U slučaju više govornika, odvojite svako ime zarezom, na primer ovako: `Govornik: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- Kada završite sa izmenama ovog fajla, sačuvajte ih klikom na dugme `Commit changes...`:

![conference](assets/38.webp)


- Dodajte naslov za vaše izmene, kao i kratak opis:

![conference](assets/39.webp)


- Kliknite na `Commit changes`:

![conference](assets/40.webp)


- Vaša konferencijska fascikla sada bi trebala izgledati ovako:

![conference](assets/41.webp)


- Ako vam sve odgovara, vratite se na koren vašeg Fork:

![conference](assets/42.webp)


- Trebalo bi da vidite poruku koja ukazuje da je vaša grana pretrpela izmene. Kliknite na dugme `Compare & pull request`:

![conference](assets/43.webp)


- Dodajte jasan naslov i opis za vaš PR:

![conference](assets/44.webp)


- Kliknite na dugme `Create pull request`:

![conference](assets/45.webp)

Čestitamo! Vaš PR je uspešno kreiran. Administrator će ga sada pregledati i, ako je sve u redu, spojiti ga u glavni repozitorijum PlanB Network-a. Trebalo bi da vidite reprize vaše konferencije na sajtu nekoliko dana kasnije.


Molimo vas da pratite napredak vašeg PR-a. Moguće je da administrator ostavi komentar tražeći dodatne informacije. Sve dok vaš PR nije validiran, možete ga videti pod karticom `Pull requests` na GitHub repozitorijumu PlanB Network-a:

![conference](assets/46.webp)


Hvala vam puno na vašem dragocenom doprinosu! :)