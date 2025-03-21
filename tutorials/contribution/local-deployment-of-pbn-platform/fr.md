---
name: Guide pour l'exécution locale de la plate-forme Plan ₿ Network
description: Comment faire fonctionner le Plan ₿ Network dans un environnement local pour tester ma contribution au contenu ou la relecture/révision du contenu éducatif sur le Plan ₿ Network ?
---
![github](assets/cover.webp)

## En résumé

Ce tutoriel fournit des instructions étape par étape pour configurer le système de gestion de l'apprentissage Bitcoin à partir de Plan ₿ Network sur votre machine locale en utilisant Docker, des clés factices et des configurations de référentiel personnalisées.

Si vous n'avez pas compris la partie ci-dessus, ne vous inquiétez pas, ce tutoriel est fait pour vous !

---
## **Comment faire fonctionner localement le système de gestion de l'apprentissage Bitcoin**

Ce tutoriel fournit des étapes détaillées pour configurer la plateforme, gérer les clés factices et personnaliser les dépôts. Suivez les étapes ci-dessous pour éviter les problèmes courants et configurer correctement votre environnement local.

**1. Conditions préalables**


- Machine Linux avec Docker et Docker Compose installés (il a été rapporté que cela fonctionnait également sous Windows).
- version suffisante de `nodejs` (testé : 22.12.0)
- `pnpm` installé sur votre système.
- Git configuré pour le clonage de dépôts.

**2. Cloner le référentiel**

Clonez le référentiel sur votre machine locale :

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Configurer les variables d'environnement**

1\. Dupliquer le fichier `.env.example` :

```bash
cp .env.example .env
```

1. Editez le fichier `.env`, en supprimant la partie .example du nom, maintenant vous devez inclure des clés factices pour les variables requises. Exemple :

⚠️ Il s'agit d'une étape obligatoire. Si vous la sautez, des erreurs se produiront, telles que le refus de connexion entre certains conteneurs.

N'oubliez pas d'ajouter votre PAT Github dédié dans le fichier

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Installer les dépendances**

assurez-vous d'avoir installé une version appropriée de nodejs. En date du 2024-12, la version 22.12.0 (LTS) a fait ses preuves.

⚠️ La version de nodejs du dépôt Ubuntu 22.04 est 12.22.9 : trop ancienne pour permettre l'installation de pnpm

Pour installer nodejs, vous trouverez des instructions [ici] (https://nodejs.org/en/download/package-manager) ; par exemple, vous pouvez choisir d'utiliser la méthode d'installation `nvm`.

---
Avant de lancer la phase d'installation des paquets nécessaires à pnpm, assurez-vous que toutes les dépendances sont installées, vous pouvez le faire en exécutant la commande suivante :

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Dans votre dossier `../Bitcoin-learning-management-system/`, exécutez la commande suivante pour installer `pnpm`

```bash
pnpm install
```
__TIP:__ N'oubliez pas de mettre à jour de temps en temps les dépendances et pnpm lui-même

**5. Faire fonctionner les conteneurs**

Dans votre dossier `../Bitcoin-learning-management-system/`, démarrez l'environnement de développement avec Docker :

```bash
docker compose up --build -V
```

Si vous exécutez également la commande suivante de cette manière, vous ne verrez pas les journaux dans votre terminal.

```bash
docker compose up -d --build -V
```

Cela construira et démarrera tous les conteneurs nécessaires à partir de dockers.

**6. Accéder à l'application**

Une fois que les conteneurs fonctionnent, accédez au frontend à l'adresse suivante :

\N- [<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Remarque : l'application se rechargera automatiquement si vous modifiez des fichiers sources.

**7.** Configurer votre base de données Schema

Lors de la première exécution, vous devrez exécuter les migrations de la base de données.

Pour ce faire, lancez le script de migration : `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Importer des données du référentiel**

Pour importer des données dans la base de données, faites une demande à l'API :

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Résoudre les problèmes d'accès au volume de synchronisation**

Si vous rencontrez des problèmes d'accès aux volumes `cdn` et `sync`, exécutez :

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

mais encore une fois :

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Personnaliser le référentiel (optionnel)**

Si vous devez utiliser une Fork ou une branche spécifique :

1. Modifiez le fichier `.env` pour mettre à jour les variables suivantes :

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Redémarrer Docker :

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Resynchroniser les données du référentiel :

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Ce tutoriel permet de s'assurer que la plateforme est correctement configurée avec des clés factices, que les dépendances sont installées et que les dépôts sont personnalisés si nécessaire. 🎉 Bonne chance avec votre installation !

**Commandes d'aide supplémentaire**

arrêter tous les conteneurs

```
docker compose down
```

élaguer tous les contenants et volumes existants

```
docker container prune -f
docker volume prune --all
```

recréer les conteneurs avec la même commande que celle utilisée dans le guide officiel et le script de synchronisation du déjeuner :

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
