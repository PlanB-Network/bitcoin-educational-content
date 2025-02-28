---
name: Contribuição - Tutorial Git (avançado)
description: Guia para utilizadores avançados para oferecer um tutorial sobre o Plano ₿ Rede com o Git
---
![cover](assets/cover.webp)

Antes de seguir este tutorial sobre como adicionar um novo tutorial, é necessário ter concluído algumas etapas preliminares. Se ainda não o fez, consulte primeiro este tutorial introdutório e depois volte aqui:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Já tem :


- Escolha um tema para o seu tutorial;
- Contactou a equipa do Plano ₿ Network através do [grupo Telegram] (https://t.me/PlanBNetwork_ContentBuilder) ou paolo@planb.network ;
- Escolha as suas ferramentas de contribuição.

Neste tutorial para usuários experientes do Git, vamos resumir brevemente as principais etapas e diretrizes essenciais para oferecer um novo tutorial Plan ₿ Network. Se você não estiver familiarizado com o Git e o GitHub, recomendo que você siga um desses dois outros tutoriais mais detalhados que o levarão passo a passo:


- Intermediário (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Iniciantes (interface web)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Ferramentas sugeridas

Para editar ficheiros Markdown :


- Obsidian** (Gratuito, não de código aberto)
- Mark Text** (gratuito, de fonte aberta)
- Zettlr** (gratuito, de código aberto)
- Typora** (Payware, ~15€, não é de código aberto)

Para Git :


- Git** (gratuito, de código aberto)
- GitHub Desktop** (gratuito, de código aberto)
- Sourcetree** (Gratuito, não de fonte aberta)

Para editar ficheiros YAML :


- Visual Studio Code** (gratuito, de fonte aberta)
- Sublime Text** (gratuito com limitações, não é de código aberto)

Para criar diagramas e imagens :


- Canva** (gratuito com opções pagas, não é de código aberto)
- Inkscape** (gratuito, de código aberto)
- Penpot** (gratuito, de código aberto)

## Fluxos de trabalho

### 1 - Configurar o seu ambiente local


- Tem de ter a sua própria bifurcação do repositório [Plan ₿ Network no GitHub] (https://github.com/PlanB-Network/bitcoin-educational-content).
- Sincroniza o ramo principal (`dev`) da sua bifurcação com o repositório de código fonte.
- Actualize o seu clone local.

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

### 2 - Criar uma nova sucursal


- Certifique-se de que está no ramo `dev`.
- Crie um novo ramo com um nome descritivo (por exemplo, `tuto-green-wallet-loic`).
- Publique este ramo na sua bifurcação em linha.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Adicionar os documentos do tutorial

***Nota:*** Pode automatizar os passos 3 e 4 utilizando [o meu script Python GUI](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Execute-o diretamente a partir da sua pasta no seu clone local e, em seguida, preencha os campos necessários na GUI. Para mais informações sobre como o instalar e utilizar, consulte o [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Se preferir fazê-lo manualmente, siga estes passos :


- Localize a pasta apropriada no repositório local (por exemplo, `tutorials/wallet`).
- Crie um diretório dedicado ao tutorial com um nome claro (por exemplo, `green-wallet`). Este nome de pasta também determinará o caminho URL do tutorial. Deve estar em minúsculas, sem caracteres especiais (exceto hífenes) e sem espaços.
- Adicione os seguintes itens a este diretório:
    - Uma subpasta chamada `assets` contendo :
        - Duas imagens `.webp`:
            - `logo.webp`: O logótipo do tutorial (formato quadrado com fundo). Este logótipo deve representar o software ou a ferramenta apresentada. Se o tutorial não for específico de uma ferramenta (por exemplo: um guia geral para gerar uma frase mnemónica), pode escolher um visual adequado (por exemplo: um ícone genérico).
            - `cover.webp`: Uma imagem de capa exibida no início do tutorial.
        - Uma subpasta com o código do idioma original do tutorial. Por exemplo, se o tutorial for escrito em inglês, esta subpasta deve ser nomeada `en'. Coloque todos os elementos visuais do tutorial (diagramas, imagens, screenshots, etc.) nesta pasta.
    - Um ficheiro `tutorial.yml` contendo metadados (autor, etiquetas, categoria, nível de dificuldade, etc.).
    - Um ficheiro Markdown contendo o tutorial, nomeado de acordo com o código da língua (por exemplo, `fr.md`, `en.md`, etc.).

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

### 4 - Preencher o ficheiro YAML


- Complete o ficheiro `tutorial.yml` da seguinte forma:

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

tags:


  - carteiras
  - software
  - chaves

categoria: telemóvel

nível: principiante

créditos:

professor: pretty-private

# Revisão de metadados

língua_original: fr

revisão de provas:


  - língua: fr

last_contribution_date: 2024-11-20

urgência:

contribuintes_id:


      - LoicPandul

recompensa:

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

# Criar um commit com uma mensagem descritiva

git commit -m "Adicionar tutorial de carteira verde"

# Empurrar as modificações para o garfo

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Criar um commit descrevendo as correcções efectuadas

git commit -m "Correcções após a revisão do tutorial da carteira verde"

# Correcções no garfo

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

print("Olá, Bitcoin!")

```