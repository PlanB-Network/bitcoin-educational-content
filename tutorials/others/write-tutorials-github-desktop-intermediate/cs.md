---
name: Příspěvek - Výukový kurz s GitHub Desktop (pro středně pokročilé)
description: Kompletní průvodce návrhem výukového programu na síti Plan ₿ pomocí GitHub Desktop
---
![cover](assets/cover.webp)

Než se pustíte do tohoto návodu na přidání nového tutoriálu, musíte provést několik předběžných kroků. Pokud jste tak ještě neučinili, vyzývám vás, abyste se nejprve seznámili s tímto úvodním tutoriálem a poté se sem vrátili:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Už jste to udělali:


- Vybrané téma výukového programu;
- Kontaktoval tým sítě Plan ₿ prostřednictvím [skupiny Telegram](https://t.me/PlanBNetwork_ContentBuilder) nebo paolo@planb.network;
- Vybrané nástroje pro příspěvek.

V tomto tutoriálu se podíváme, jak přidat svůj tutoriál do sítě Plan ₿ nastavením místního prostředí pomocí aplikace GitHub Desktop. Pokud jste již zběhlí v práci se systémem Git, tento velmi podrobný návod pro vás nemusí být nutný. Doporučuji spíše konzultaci tohoto jiného tutoriálu, kde uvádím pouze hlavní pokyny, bez podrobného návodu krok za krokem:


- Zkušení uživatelé**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Pokud nechcete nastavovat místní prostředí, postupujte podle tohoto dalšího návodu určeného pro začátečníky, kde změny provedeme přímo přes webové rozhraní GitHubu:


- Pro začátečníky (webové rozhraní)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Předpoklady

Software potřebný pro tento výukový program:


- [GitHub Desktop](https://desktop.github.com/);
- Editor souborů markdown, jako je [Obsidian](https://obsidian.md/);
- Editor kódu ([VSC](https://code.visualstudio.com/) nebo [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Předpoklady před zahájením výuky:


- Mít účet [GitHub](https://github.com/signup);
- Mít fork zdrojového úložiště [Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content);
- Mít [profil profesora v síti Plan ₿](https://planb.network/professors) (pouze pokud navrhujete kompletní výukový program).

Pokud potřebujete pomoci se získáním těchto předpokladů, pomohou vám mé další výukové programy:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
Jakmile je vše na svém místě a vaše místní prostředí je správně nastaveno s vlastní odnoží sítě Plan ₿, můžete začít přidávat výukový program.

## 1 - Vytvoření nové pobočky

Otevřete prohlížeč a přejděte na stránku svého úložiště sítě Plan ₿. Jedná se o fork, který jste založili na GitHubu. Adresa URL vašeho forku by měla vypadat takto: `https://github.com/[vaše uživatelské jméno]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Ujistěte se, že se nacházíte v hlavní větvi `dev`, a poté klikněte na tlačítko `Sync fork`. Pokud váš fork není aktuální, GitHub vám nabídne aktualizaci vaší větve. Pokračujte v této aktualizaci. Pokud je naopak vaše větev již aktuální, GitHub vás o tom bude informovat:

![TUTO](assets/fr/04.webp)

Otevřete program GitHub Desktop a ujistěte se, že je v levém horním rohu okna správně vybrán váš fork:

![TUTO](assets/fr/05.webp)

Klikněte na tlačítko `Přinést původ`. Pokud je váš místní repozitář již aktualizován, aplikace GitHub Desktop nenavrhne žádné další kroky. V opačném případě se zobrazí možnost `Pull origin`. Kliknutím na toto tlačítko aktualizujete svůj místní repozitář:

![TUTO](assets/fr/06.webp)

Ověřte, zda jste skutečně v hlavní větvi `dev`:

![TUTO](assets/fr/07.webp)

Klikněte na tuto větev a potom klikněte na tlačítko `Nová větev`:

![TUTO](assets/fr/08.webp)

Ujistěte se, že nová větev je založena na zdrojovém úložišti, konkrétně `PlanB-Network/bitcoin-educational-content`.

Pojmenujte svou pobočku tak, aby byl z názvu zřejmý její účel, a oddělujte jednotlivá slova pomlčkami. Řekněme například, že naším cílem je napsat návod na používání softwaru Sparrow Wallet. V tomto případě by se pracovní větev určená k napsání tohoto návodu mohla jmenovat: `tuto-sparrow-wallet-loic`. Po zadání vhodného názvu klikněte na tlačítko `Vytvořit větev` a potvrďte vytvoření větve:

![TUTO](assets/fr/09.webp)

Nyní klikněte na tlačítko `Publikovat větev` a uložte novou pracovní větev do své online větve na GitHubu:

![TUTORIAL](assets/fr/10.webp)

Nyní byste se měli na ploše GitHubu ocitnout v nové větvi. To znamená, že všechny změny provedené lokálně na vašem počítači budou uloženy výhradně v této konkrétní větvi. Dokud bude na ploše GitHub Desktop tato větev vybrána, budou soubory viditelné lokálně na vašem počítači odpovídat souborům této větve (`tuto-sparrow-wallet-loic`), a nikoli souborům hlavní větve (`dev`).

![TUTORIAL](assets/fr/11.webp)

Pro každý nový článek, který chcete publikovat, musíte vytvořit novou větev z `dev`. Větev v systému Git je paralelní verze projektu, která umožňuje provádět změny, aniž by ovlivnila hlavní větev, dokud není práce připravena ke sloučení.

## 2 - Přidání výukových souborů

Nyní, když je vytvořena pracovní větev, je čas integrovat nový výukový program. Máte dvě možnosti: použít můj skript Python, který automatizuje vytvoření potřebných dokumentů, nebo vytvořit každý soubor ručně. Podíváme se na kroky, které je třeba dodržet u každé z těchto možností.

### Pomocí mého skriptu Python

Musíte jej nainstalovat do počítače:


- Python 3.8 nebo vyšší;
- Nezbytné závislosti pro skript. Spustit:

```bash
pip install customtkinter appdirs
```

Chcete-li skript použít, přejděte do složky, kde je uložen. Skript se nachází v úložišti dat sítě Plan ₿ pod cestou: `bitcoin-educational-content/scripts/tutorial-related/new-tutorial-creation/`.

Po vstupu do složky spusťte příkaz:

```bash
python new-tutorial-creation.py
```

Otevře se grafické uživatelské rozhraní (GUI). Poprvé budete muset zadat všechny potřebné informace, ale při dalších použitích skriptu se vaše osobní údaje zapamatují, takže je nebudete muset zadávat znovu.

![TUTORIAL](assets/fr/37.webp)

Začněte uvedením místní cesty vedoucí ke složce `/tutorials` na vašem klonu úložiště (`.../bitcoin-educational-content/tutorials/`). Můžete si ji poznamenat ručně nebo kliknutím na tlačítko "Procházet" přejít přes průzkumníka souborů.

![TUTORIAL](assets/fr/38.webp)

Vyberte jazyk, ve kterém budete psát výukový program.

![TUTORIAL](assets/fr/39.webp)

Zvolte si hlavní kategorii výukového programu.

![TUTORIAL](assets/fr/40.webp)

Poté vyberte vhodnou podkategorii v závislosti na zvolené hlavní kategorii.

![TUTORIAL](assets/fr/41.webp)

Určete úroveň obtížnosti výukového programu.

![TUTORIAL](assets/fr/42.webp)

Zvolte název adresáře vytvořeného speciálně pro váš výukový program. Název tohoto adresáře by měl odrážet software, který je předmětem výukového kurzu, a slova by měl spojovat pomlčkami. Složka by se například mohla jmenovat `red-wallet`:

![TUTO](assets/fr/43.webp)

`project_id` je UUID společnosti nebo organizace, která stojí za nástrojem prezentovaným v tutoriálu a je k dispozici [v seznamu projektů](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Například pro výukový program o softwaru Sparrow Wallet byste v souboru našli toto `project_id`: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Tato informace je přidána do souboru YAML vašeho výukového kurzu, protože síť Plan ₿ Network spravuje databázi společností a organizací aktivních v oblasti Bitcoinu nebo souvisejících projektů. Přidáním `project_id` spojeného s vaším tutoriálem vytvoříte vazbu mezi vaším obsahem a dotyčným subjektem.

***Aktualizace:*** V nové verzi skriptu již nemusíte ručně zadávat `project_id`. Byla přidána funkce vyhledávání, která vyhledá projekt podle jeho názvu a automaticky načte odpovídající `project_id`. Pro vyhledání zadejte do pole "Název projektu" začátek názvu projektu a poté vyberte požadovanou společnost z rozbalovací nabídky. V následujícím poli se automaticky vyplní `project_id`. V případě potřeby máte také možnost zapsat jej ručně.

![TUTO](assets/fr/44.webp)

U značek vyberte 2 nebo 3 relevantní klíčová slova související s obsahem vašeho výukového programu a vyberte je výhradně [ze seznamu značek sítě Plan ₿](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).

![TUTO](assets/fr/45.webp)

Do pole "ID GitHubu přispěvatele" zadejte své ID GitHubu.

![TUTO](assets/fr/46.webp)

Do pole "ID profesora PBN" zadejte své ID pomocí slov ze seznamu BIP39, jak je uvedeno na [profilu profesora](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).

![TUTO](assets/fr/47.webp)

Další podrobnosti o ID profesora naleznete v následujícím návodu:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Po zadání a ověření všech informací klikněte na tlačítko "Vytvořit výukový program" a potvrďte vytvoření výukových souborů. Tím se lokálně vygeneruje složka vašeho tutoriálu a všechny potřebné soubory ve složce vybrané kategorie.

![TUTO](assets/fr/48.webp)

Nyní můžete přeskočit podkapitolu "Bez mého skriptu Python", stejně jako krok 3 "Vyplnění souboru YAML", protože skript již tyto činnosti provedl automaticky za vás. Přejděte přímo ke kroku 4 a začněte psát svůj výukový program.

Další informace o tomto skriptu v jazyce Python naleznete také [v jeho README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Bez mého skriptu Python

Otevřete správce souborů a přejděte do složky `bitcoin-educational-content`, která představuje místní klon vašeho úložiště. Obvykle byste ji měli najít ve složce `Documents\GitHub\bitcoin-educational-content`.

V tomto adresáři je třeba najít příslušný podsložku pro umístění výukového programu. Uspořádání složek odráží různé sekce webových stránek sítě Plan ₿. V našem příkladu, protože chceme přidat výukový program o peněžence Sparrow, je vhodné přejít do následující cesty: `bitcoin-educational-content\tutorials\wallet`, což odpovídá sekci `WALLET` na webových stránkách:

![TUTO](assets/fr/12.webp)

Ve složce `peněženka` musíte vytvořit nový adresář určený speciálně pro váš výukový program. Název této složky by měl evokovat software, který je v tutoriálu popsán, a dbejte na to, abyste slova spojovali pomlčkami. V mém případě se složka bude jmenovat `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

Do této nové podsložky určené pro váš výukový program je třeba přidat několik prvků:


- Vytvořte složku `assets`, do které vložíte všechny ilustrace potřebné pro výukový program;
- V této složce `assets` je třeba vytvořit podsložku pojmenovanou podle původního kódu jazyka výukového programu. Pokud je například výukový program napsán v angličtině, musí být tato podsložka pojmenována `en`. Umístěte do ní všechny vizuální materiály výukového programu (schémata, obrázky, snímky obrazovky atd.).
- Je třeba vytvořit soubor `tutorial.yml`, do kterého budou zaznamenány podrobnosti týkající se vašeho výukového programu;
- Pro zápis skutečného obsahu výukového programu je třeba vytvořit soubor ve formátu markdown. Tento soubor musí mít název podle kódu jazyka zápisu. Například pro výukový program psaný ve francouzštině se soubor musí jmenovat `fr.md`.

![TUTO](assets/fr/14.webp)

Stručně shrnuto, zde je hierarchie souborů, které je třeba vytvořit:

```plaintext
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Vyplnění souboru YAML

Vyplňte soubor `tutorial.yml` zkopírováním následující šablony:

```yaml
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

credits:
  professor: 

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributors_id:
      - 
    reward:
````

Zde jsou uvedeny podrobnosti o povinných polích:


- **id**: UUID (_Universally Unique Identifier_), který slouží k jednoznačné identifikaci výukového programu. Můžete jej vygenerovat pomocí [online nástroje](https://www.uuidgenerator.net/version4). Jediným požadavkem je, aby tento UUID byl náhodný, aby nedošlo ke konfliktu s jiným UUID na platformě;
- **project_id**: UUID společnosti nebo organizace, která stojí za nástrojem prezentovaným v tutoriálu [ze seznamu projektů](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Pokud například vytváříte výukový program o softwaru Sparrow Wallet, najdete toto `project_id` v následujícím souboru: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Tato informace je přidána do souboru YAML vašeho výukového programu, protože síť Plan ₿ udržuje databázi všech společností a organizací působících v oblasti Bitcoinu nebo souvisejících projektů. Přidáním `project_id` subjektu souvisejícího s vaším tutoriálem vytvoříte spojení mezi těmito dvěma prvky;
- **tags**: 2 nebo 3 relevantní klíčová slova související s obsahem výukového programu, vybraná výhradně [ze seznamu značek sítě Plan ₿](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- **category**: Podkategorie odpovídající obsahu výukového programu podle struktury webu sítě Plan ₿ (například pro peněženky: `desktop`, `hardware`, `mobil`, `zálohování`);
- **level**: Úroveň obtížnosti výukového programu, mezi:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: (slova BIP39), jak je zobrazeno na [vašem profilu profesora](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- **original_language**: Původní jazyk výukového programu (například `fr`, `en` atd.);
- **proofreading**: Informace o procesu korektury. Vyplňte první část, protože korektura vlastního výukového materiálu se počítá jako první ověření:
    - **language**: Kód jazyka korektury (například `fr`, `en` atd.).
    - **last_contribution_date**: Dnešní datum.
    - **urgency**: Nevyplňujte.
    - **contributors_id**: Vaše GitHub ID.
    - **reward**: Nevyplňujte.

Další podrobnosti o identifikátoru profesora naleznete v příslušném výukovém kurzu:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Zde je příklad vyplněného souboru `tutorial.yml` pro výukový program o peněžence Blockstream Green:

```yaml
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [Název]
description: [Popis]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```