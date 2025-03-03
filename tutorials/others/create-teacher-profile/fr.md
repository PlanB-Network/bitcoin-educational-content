---
name: Professeur Plan ₿ Network
description: Comment ajouter ou modifier son profil de professeur sur Plan ₿ Network ?
---
![cover](assets/cover.webp)

Si vous souhaitez contribuer sur Plan ₿ Network en écrivant un nouveau tutoriel ou bien un nouveau cours, vous allez avoir besoin d'un profil de professeur. Cela vous permettra d'être correctement crédité pour le contenu que vous produisez sur la plateforme.

Si vous avez déjà contribué sur Plan ₿ Network dans de la production de contenu éducatif, vous avez sûrement déjà un profil de professeur. Vous pouvez le retrouver dans le dossier `/professors` [sur notre dépôt GitHub](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors). Si vous avez déjà un profil, vous pouvez récupérer votre identifiant dans le fichier `professor.yml`. Si vous voulez modifier votre profil, vous pouvez aller directement dans la section "Modifier son profil de professeur" à la fin de ce tutoriel.

## Ajouter un nouveau professeur avec notre logiciel

La manière la plus simple de créer votre profil de professeur sur Plan ₿ Network est d'utiliser notre outil python intégré au dépôt. Voici comment faire.

### 1 - Configurez votre environnement local

- Vous devez avoir votre propre fork du [dépôt Plan ₿ Network sur GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Synchronisez la branche principale (`dev`) de votre fork avec le dépôt source.
- Mettez à jour votre clone local.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
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

### 2 - Créez une nouvelle branche

- Assurez-vous d’être sur la branche `dev`.
- Créez une nouvelle branche avec un nom descriptif (par exemple : `add-professor-loic-morel`).
- Publiez cette branche sur votre fork en ligne.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev

# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel

# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```

### 3 - Créez votre profil de professeur

- Sur votre clone local, rendez-vous dans le dossier `scripts/tutorial-related/data-creator/`.
- Installez les dépendances nécessaires pour le logiciel (il faut également avoir installé Python) :

```bash
pip install -r requirements.txt
```

- Puis lancez le logiciel avec la commande :

```bash
python3 main.py
```

- Vous arrivez ensuite sur l'accueil. Renseignez le chemin local vers votre clone du dépôt, la langue dans laquelle vous rédigez et votre identifiant GitHub. Si vous créez ce professeur pour une autre personne et que vous avez déjà votre propre profil de professeur, entrez le dans la case "PBN Professor's ID". Si vous créez votre profil de professeur pour vous-même, vous n'avez pas encore d'identifiant de professeur puisque vous êtes en train de le créer. Laissez donc cette case vide.
- Puis, cliquez sur le bouton "New Professor".

01

- Renseignez les informations demandées, puis une fois terminé, cliquez sur le bouton "Create Professor". Cela va automatiquement créer tous les fichiers nécessaire pour votre profil.

02

- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.

```bash
# Créez un commit avec un message descriptif
git commit -m "new professor Loïc Morel"

# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```

- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR.

### 4 - Relecture et fusion

- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.

```bash
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"

# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```

- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.

## Modifier votre profil de professeur

Si vous êtes à l'aise avec l'utilisation de Git, vous pouvez modifier votre profil de professeur en créant une nouvelle branche et en modifiant directement le fichier concerné sur dans votre dossier de professeur existant. Cel peut être soit dans le fichier `professor.yml` soit dans le fichier markdown en fonciton de l'informaiton que vous souhaitez rectifier. Une fois vos modifications réalisées en local, pooussez-les vers votre fork puis faites une PR.

Si vous êtes débutant, je vous conseille de faire la modification directement sur l'interface web de GitHub. Pour ce faire, vous devez simplement avoir un compte GitHub. Si vous ne savez pas comment en créer un, suivez 


















