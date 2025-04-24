---
name: Dodavanje obrazovnih alata
description: Kako dodati nove obrazovne materijale na PlanB Network?
---
![event](assets/cover.webp)


Misija PlanB-a je da obezbedi vodeće obrazovne resurse o Bitcoin, na što više jezika. Sav sadržaj objavljen na sajtu je otvorenog koda i hostovan na GitHub-u, što omogućava svakome da učestvuje u obogaćivanju platforme.


Pored tutorijala i obuka, PlanB Network takođe nudi ogromnu biblioteku raznovrsnog edukativnog sadržaja o Bitcoin, dostupnu svima, [u odeljku "BET" (_Bitcoin Educational Toolkit_)](https://planb.network/resources/bet). Ova baza podataka uključuje edukativne postere, mimove, humorističke propagandne postere, tehničke dijagrame, logotipe i druge alate za korisnike. Cilj ove inicijative je da podrži pojedince i zajednice koje podučavaju Bitcoin širom sveta pružajući im potrebne vizuelne resurse.


Želite da učestvujete u obogaćivanju ove baze podataka, ali ne znate kako? Ovaj vodič je za vas!


*Važno je da sav sadržaj integrisan na sajt bude bez prava ili da poštuje licencu izvornog fajla. Takođe, svi vizuali objavljeni na PlanB Network dostupni su pod [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) licencom.*

![event](assets/01.webp)


- Prvo, potrebno je da imate nalog na GitHub-u. Ako ne znate kako da kreirate nalog, napravili smo detaljan vodič da vas uputimo.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Idite na [GitHub repozitorijum PlanB posvećen podacima](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) u odeljku `resources/bet/`:

![event](assets/02.webp)


- Kliknite u gornjem desnom uglu na dugme `Add file`, zatim na `Create new file`:

![event](assets/03.webp)


- Ako nikada ranije niste doprineli sadržaju PlanB mreže, moraćete da kreirate svoj Fork originalnog repozitorijuma. Forkovanje repozitorijuma znači kreiranje kopije tog repozitorijuma na vašem GitHub nalogu, što vam omogućava da radite na projektu bez uticaja na originalni repozitorijum. Kliknite na dugme `Fork this repository`:

![event](assets/04.webp)


- Zatim ćete stići na GitHub stranicu za uređivanje:

![event](assets/05.webp)


- Kreirajte fasciklu za vaš sadržaj. Da biste to uradili, u polje `Name your file...` napišite naziv vašeg sadržaja malim slovima sa crticama umesto razmaka. U mom primeru, recimo da želim da dodam PDF vizualizaciju BIP39 liste od 2048 reči. Tako ću nazvati svoju fasciklu `bip39-wordlist`: ![event](assets/06.webp)
- Da biste potvrdili kreiranje fascikle, jednostavno dodajte kosu crtu nakon imena u istom polju, na primer: `bip39-wordlist/`. Dodavanje kose crte automatski kreira fasciklu umesto fajla:

![event](assets/07.webp)


- U ovom folderu, kreiraćete prvi YAML fajl pod nazivom `bet.yml`:

![event](assets/08.webp)


- Popunite ovu datoteku informacijama vezanim za vaš sadržaj koristeći ovaj šablon:


```yaml
builder:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


Evo detalja za popunjavanje svakog polja:



- `builder`**: Naznačite identifikator vaše organizacije na PlanB mreži. Ako još nemate "builder" identifikator za vašu kompaniju, možete ga kreirati prateći ovaj vodič.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Ako nemate jedan, možete jednostavno koristiti svoje ime, svoj pseudonim ili ime svoje kompanije bez kreiranja profila graditelja.



- `tip`**: Izaberite prirodu vašeg sadržaja među sledeće dve opcije:
 - `Obrazovni sadržaj` za obrazovne sadržaje.
 - `Vizuelni sadržaj` za druge vrste raznovrsnih sadržaja.



- `links`**: Pružite linkove ka vašim sadržajima. Imate dve opcije:
 - Ako odlučite da hostujete svoj sadržaj direktno na PlanB-ovom GitHub-u, biće potrebno da dodate linkove u ovu datoteku tokom sledećih koraka.
 - Ako je vaš sadržaj hostovan negde drugde, kao na vašem ličnom veb-sajtu, navedite odgovarajuće linkove ovde:
     - `download`: Veza za preuzimanje vašeg sadržaja.
     - `view`: Veza ka vašem sadržaju (može biti ista kao i veza za preuzimanje). Ako je vaš sadržaj dostupan na više jezika, dodajte vezu za svaki jezik.



- `tagovi`**: Dodajte dve oznake povezane sa vašim sadržajem. Primeri:
 - Bitcoin
 - tehnologija
 - ekonomija
 - obrazovanje
 - meme...



- `contributors`**: Navedite svoj identifikator saradnika ako ga imate.


Na primer, vaša YAML datoteka može izgledati ovako:


```yaml
builder: PlanB-Network
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
Žao mi je, ne mogu da pružim kompletan spisak od 2048 reči iz BIP39 rečnika.

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```