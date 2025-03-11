---
name: Příspěvek - Výukový program Git (pro pokročilé)
description: Průvodce pro pokročilé uživatele, který nabízí výukový program pro plánování ₿ Síť s Gitem
---
![cover](assets/cover.webp)

Než se pustíte do tohoto návodu na přidání nového tutoriálu, musíte provést několik předběžných kroků. Pokud jste tak ještě neučinili, podívejte se nejprve na tento úvodní návod a pak se vraťte sem :

https://planb.network/tutorials/contribution/tutorial/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Již máte :


- Vyberte si téma výukového programu;
- Kontaktoval tým sítě Plan ₿ prostřednictvím [skupiny Telegram](https://t.me/PlanBNetwork_ContentBuilder) nebo paolo@planb.network ;
- Vyberte si nástroje pro přispívání.

V tomto tutoriálu pro zkušené uživatele systému Git stručně shrneme klíčové kroky a základní pokyny pro nabídku nového tutoriálu Plan ₿ Network. Pokud se v systému Git a GitHub nevyznáte, doporučuji vám raději sledovat jeden z těchto dalších 2 podrobnějších tutoriálů, které vás provedou krok za krokem :


- Středně pokročilý (GitHub Desktop)** :

https://planb.network/tutorials/contribution/tutorial/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Začátečníci (webové rozhraní)** :

https://planb.network/tutorials/contribution/tutorial/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Navrhované nástroje

Pro úpravu souborů Markdown :


- Obsidian** (zdarma, ne open-source)
- Mark Text** (zdarma, open-source)
- Zettlr** (zdarma, open-source)
- Typora** (Payware, ~15 EUR, není open-source)

Pro Git :


- Git** (zdarma, open-source)
- GitHub Desktop** (zdarma, open-source)
- Sourcetree** (zdarma, ne open-source)

Pro úpravu souborů YAML :


- Visual Studio Code** (zdarma, open-source)
- Sublime Text** (zdarma s omezeními, není open-source)

Vytváření diagramů a vizualizací :


- Canva** (zdarma s placenými možnostmi, ne open-source)
- Inkscape** (zdarma, open-source)
- Penpot** (zdarma, open-source)

## Pracovní postupy

### 1 - Konfigurace místního prostředí


- Musíte mít vlastní fork repozitáře [Plan ₿ Network na GitHubu](https://github.com/PlanB-Network/bitcoin-educational-content).
- Synchronizujte hlavní větev (`dev`) svého forku se zdrojovým úložištěm.
- Aktualizujte svůj místní klon.

```
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - Vytvoření nové pobočky


- Ujistěte se, že jste ve větvi `dev`.
- Vytvořte novou větev s popisným názvem (např. `tuto-green-wallet-loic`).
- Zveřejněte tuto větev na svém online forku.

```
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Přidání výukových dokumentů

***Poznámka:*** Kroky 3 a 4 můžete automatizovat pomocí [mého skriptu pro grafické uživatelské rozhraní Pythonu](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Spusťte jej přímo z jeho složky v místním klonu a poté vyplňte požadovaná pole v grafickém uživatelském rozhraní. Další informace o tom, jak jej nainstalovat a používat, najdete v [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Pokud to chcete provést ručně, postupujte podle následujících kroků :


- Vyhledejte příslušnou složku v místním úložišti (např. `tutorials/wallet`).
- Vytvořte adresář určený pro výukový program s jasným názvem (např. `zelená peněženka`). Tento název adresáře bude také určovat cestu URL k výukovému kurzu. Měl by být psán malými písmeny, bez speciálních znaků (kromě pomlček) a bez mezer.
- Do tohoto adresáře přidejte následující položky:
    - Podsložka s názvem `assets` obsahující :
        - Dva obrázky `.webp`:
            - `logo.webp`: Logo výukového programu (čtvercový formát s pozadím). Toto logo musí reprezentovat prezentovaný software nebo nástroj. Pokud se tutoriál netýká konkrétního nástroje (např.: obecný návod na generování mnemotechnické fráze), můžete zvolit vhodný vizuál (např.: obecnou ikonu).
            - `cover.webp`: Obrázek obálky zobrazený na začátku výukového programu.
        - Podsložka s kódem původního jazyka výukového programu. Pokud je například výukový program napsán v angličtině, měla by se tato podsložka jmenovat `en'. Do této složky umístěte všechny vizuální materiály výukového programu (diagramy, obrázky, snímky obrazovky atd.).
    - Soubor `tutorial.yml` obsahující metadata (autor, značky, kategorie, úroveň obtížnosti atd.).
    - Soubor Markdown obsahující výukový program, pojmenovaný podle kódu jazyka (např. `fr.md`, `en.md` atd.).

```
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - Vyplnění souboru YAML


- Soubor `tutorial.yml` vyplňte následujícím způsobem:

```
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
```

Zde jsou povinná pole:


- id**: UUID (_Universally Unique Identifier_), který jednoznačně identifikuje výukový program. Můžete jej vygenerovat pomocí [online nástroje](https://www.uuidgenerator.net/version4). Jediným omezením je, že tento UUID musí být náhodný, aby nedošlo ke konfliktu s jiným UUID na platformě;
- project_id** : UUID společnosti nebo organizace, která stojí za nástrojem prezentovaným v tutoriálu [ze seznamu projektů](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Pokud například zpracováváte výukový program o softwaru Green Wallet, najdete toto `project_id` v následujícím souboru: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Tato informace je přidána do souboru YAML vašeho výukového programu, protože síť Plan ₿ udržuje databázi všech společností a organizací působících na Bitcoinu nebo souvisejících projektech. Přidáním `project_id` propojené entity do svého tutoriálu vytvoříte vazbu mezi těmito dvěma prvky;
- tagy**: 2 nebo 3 relevantní klíčová slova související s obsahem výukového programu, vybraná výhradně [ze seznamu tagů sítě Plan ₿](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- kategorie** : Podkategorie odpovídající obsahu výuky podle struktury sítě Plan ₿ (např. pro peněženky: `desktop`, `hardware`, `mobil`, `zálohování`) ;
- úroveň** : Úroveň obtížnosti výuky, od :
    - začátečník`
    - `intermediate`
    - `pokročilý`
    - `expert`
- profesor**: (slova BIP39), jak je zobrazeno na [profilu učitele](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- original_language** : Původní jazyk výukového programu (např. `fr`, `en` atd.) ;
- korektury**: Informace o procesu korektury. Vyplňte první část, protože korektura vlastního výukového programu se počítá jako první ověření:
    - jazyk**: (např. `fr`, `en` atd.).
    - last_contribution_date**: Dnešní datum.
    - naléhavost** : Nechte prázdné.
    - přispěvatelé_id** : Vaše GitHub ID.
    - odměna** : Nechte prázdné.

Další podrobnosti o ID učitele naleznete v příslušném výukovém kurzu :

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
```

### 5 - Napište obsah


- Doplňte vlastnosti souboru Markdown pomocí :
    - Název (`name`).
    - Krátký popis (`description`).
- Přidejte obrázek na obálku v horní části tutoriálu pomocí syntaxe Markdown (nahraďte slovo "green" názvem zobrazeného nástroje):

```
![cover-green](assets/cover.webp)
```


- Napište obsah výukového programu v jazyce Markdown :
    - Používejte dobře strukturované nadpisy (`##`), seznamy a odstavce.
    - Vkládání vizualizací pomocí syntaxe Markdown :

```
![nom-image](assets/en/001.webp)
```


- Diagramy a obrázky umístěte do podsložky příslušného jazyka v adresáři `/assets`.

### 6 - Uložte a odešlete výukový program


- Uložte své změny lokálně vytvořením revize s popisnou zprávou.
- Uložte změny do své vidlice GitHubu.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Po dokončení vytvořte na GitHubu žádost o stažení (PR) a navrhněte začlenění svých úprav.
- Přidejte název a stručný popis PR. V komentáři uveďte odpovídající číslo problému.

### 7 - Korektury a slučování


- Vyčkejte na potvrzení nebo zpětnou vazbu od správce.
- V případě potřeby proveďte opravy a odešlete nové revize.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Po sloučení PR můžete pracovní větev odstranit.

## Standardy pro tvorbu obsahu


- Formátování podporované platformou** :
    - Klasický Markdown: seznamy, odkazy, obrázky, citace, tučné písmo, kurzíva atd.
    - LaTeX (pouze blokově, ne inline): ohraničeno `$$`.
    - Řádkový kód: Syntaxe s jedním zpětným zaškrtnutím.
    - Bloky kódu: Syntaxe se třemi zpětnými háčky, například :

```
print("Hello, Bitcoin!")
```


- Ilustrace a schémata** :
    - Všechny obrázky musí být ve formátu WebP. V případě potřeby použijte tento bezplatný nástroj pro jejich konverzi: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Pojmenujte vizuály pomocí 2 nebo 3 číslic (např. `001.webp`, `002.webp`).
    - Pro výukové programy pro mobilní nebo hardwarové peněženky používejte makety.
    - Používejte pouze vizuály vytvořené vlastními silami nebo bez nároku na honorář.
    - Ujistěte se, že jsou relevantní a kvalitní.
- Grafická karta** :
    - Písmo: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Barvy Plán ₿ Síť :
        - Oranžová: `#FF5C00`
        - Černá: `#000000`
        - Bílá: `#FFFFFF`

Pokud máte technické potíže s odesláním návodu, neváhejte požádat o pomoc na [naší speciální skupině pro příspěvky na Telegramu](https://t.me/PlanBNetwork_ContentBuilder). Moc vám děkujeme!