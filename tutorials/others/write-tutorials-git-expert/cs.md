---
name: Příspěvek - Výukový program Git (pro pokročilé)
description: Průvodce pro pokročilé uživatele, který nabízí výukový program pro plánování ₿ Síť s Gitem
---
![cover](assets/cover.webp)

Než se pustíte do tohoto návodu na přidání nového tutoriálu, musíte provést několik předběžných kroků. Pokud jste tak ještě neučinili, podívejte se nejprve na tento úvodní návod a pak se vraťte sem :

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Již máte :


- Vyberte si téma výukového programu;
- Kontaktoval tým sítě Plan ₿ prostřednictvím [skupiny Telegram](https://t.me/PlanBNetwork_ContentBuilder) nebo paolo@planb.network ;
- Vyberte si nástroje pro přispívání.

V tomto tutoriálu pro zkušené uživatele systému Git stručně shrneme klíčové kroky a základní pokyny pro nabídku nového tutoriálu Plan ₿ Network. Pokud se v systému Git a GitHub nevyznáte, doporučuji vám raději sledovat jeden z těchto 2 dalších, podrobnějších tutoriálů, které vás provedou krok za krokem :


- Středně pokročilý (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Začátečníci (webové rozhraní)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
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

```bash
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

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Přidání výukových dokumentů

***Poznámka:*** Kroky 3 a 4 můžete automatizovat pomocí [mého skriptu pro grafické uživatelské rozhraní Pythonu](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Spusťte jej přímo z jeho složky v místním klonu a poté vyplňte požadovaná pole v grafickém uživatelském rozhraní. Další informace o tom, jak jej nainstalovat a používat, najdete v [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Pokud to raději uděláte ručně, postupujte podle následujících kroků :


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

```bash
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
Voici le détail des champs obligatoires :
- **id** : Un UUID (_Universally Unique Identifier_) permettant d’identifier de manière unique le tutoriel. Vous pouvez le générer avec [un outil en ligne](https://www.uuidgenerator.net/version4). La seule contrainte est que cet UUID soit aléatoire pour ne pas avoir de conflit avec un autre UUID sur la plateforme ;
- **project_id** : L'UUID de l’entreprise ou de l’organisation derrière l’outil présenté dans le tutoriel [depuis la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, si vous réalisez un tutoriel sur le logiciel Green Wallet, vous pouvez trouver ce `project_id` dans le fichier suivant : `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Cette information est ajoutée dans le fichier YAML de votre tutoriel parce que Plan ₿ Network maintient une base de données de toutes les entreprises et organisations opérant sur Bitcoin ou des projets connexes. En ajoutant le `project_id` de l'entité liée à votre tutoriel, vous créez un lien entre les deux éléments ;
- **tags** : 2 ou 3 mots-clés pertinents liés au contenu du tutoriel, choisis exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ;
- **category** : La sous-catégorie correspondant au contenu du tutoriel, selon la structure du site Plan ₿ Network (par exemple pour les wallets : `desktop`, `hardware`, `mobile`, `backup`) ;
- **level** : Le niveau de difficulté du tutoriel, parmi :
- `beginner`
- `intermediate`
- `advanced`
- `expert`
- **professor** : Votre `contributor_id` (mots BIP39) tel qu'affiché sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) ;
- **original_language** : La langue d’origine du tutoriel (par exemple `fr`, `en`, etc.) ;
- **proofreading** : Informations sur le processus de relecture. Remplissez la première partie, car la relecture de votre propre tutoriel compte comme une première validation :
- **language** : Code de langue de la relecture (par exemple `fr`, `en`, etc.).
- **last_contribution_date** : Date du jour.
- **urgency** : Laissez vide.
- **contributors_id** : Votre ID GitHub.
- **reward** : Laissez vide.
Pour davantage de détails sur votre identifiant de professeur, reportez-vous au tutoriel correspondant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
```

id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tagy:


  - peněženky
  - software
  - klíče

kategorie: mobilní zařízení

úroveň: začátečník

úvěry:

profesor: pretty-private

# Korektury metadat

original_language: fr

korektury:


  - jazyk: fr

last_contribution_date: 2024-11-20

naléhavost:

přispěvatelé_id:


      - LoicPandul

odměna:

```
### 5 - Rédigez le contenu
- Complétez les propriétés du fichier Markdown avec :
- Le titre (`name`).
- Une courte description (`description`).
- Ajoutez l’image de couverture en haut du tutoriel avec la syntaxe Markdown (remplacez "green" par le nom de l’outil présenté) :
```

![cover-green](assets/cover.webp)

```
- Rédigez le contenu du tutoriel en Markdown :
- Utilisez des titres bien structurés (`##`), des listes et des paragraphes.
- Insérez des visuels avec la syntaxe Markdown :
```

![nom-image](assets/en/001.webp)

```
- Placez les schémas et images dans le sous-dossier de langue correspondant, dans `/assets`.
### 6 - Enregistrez et soumettez le tutoriel
- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.
```

# Vytvoření revize s popisnou zprávou

git commit -m "Add green-wallet tutorial"

# Přetlačte úpravy na vidličku

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Vytvoření revize s popisem provedených oprav

git commit -m "Opravy po revizi návodu pro zelenou peněženku"

# Tlakové korekce na vidlici

git push origin tuto-green-wallet-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("Hello, Bitcoin!")

```