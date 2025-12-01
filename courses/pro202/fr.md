---
name: Programmation Bitcoin
goal: Construire une bibliothèque Bitcoin complète à partir de zéro et comprendre les fondements cryptographiques de Bitcoin
objectives: 

 - Mettre en œuvre l'arithmétique des corps finis et les opérations sur les courbes elliptiques en Python
 - Construire et analyser les transactions Bitcoin de manière programmatique
 - Créer des adresses Testnet et diffuser des transactions sur le réseau
 - Maîtriser les fondements mathématiques du modèle de sécurité Bitcoin

---
# Un voyage dans les scripts et les programmes de Bitcoin


Ce cours intensif de deux jours, enseigné par Jimmy Song, vous plonge dans les fondements techniques de Bitcoin en construisant une bibliothèque Bitcoin complète à partir de la base. En commençant par les mathématiques essentielles des champs finis et des courbes elliptiques, vous progresserez dans l'analyse des transactions, l'exécution des scripts et la communication réseau. Grâce à des exercices de codage pratiques dans des carnets Jupyter, vous créerez votre propre Testnet Address, construirez des transactions manuellement et les diffuserez directement sur le réseau, tout en acquérant une compréhension profonde des principes cryptographiques qui rendent le Bitcoin sûr et le Trustless.


Bonne découverte !


+++


# Introduction

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Aperçu du cours

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>




Bienvenue dans le cours PRO 202 _**Programming Bitcoin**_, un parcours intensif qui vous emmène de l’arithmétique des corps finis jusqu’à la création et la diffusion de transactions réelles sur le réseau de test de Bitcoin.

Dans ce cours, vous construirez progressivement une bibliothèque Bitcoin en Python tout en acquérant les bases cryptographiques, protocolaires et logicielles nécessaires pour raisonner avec précision sur la sécurité et le fonctionnement interne de Bitcoin. L’approche PRO 202 est résolument pratique : chaque concept est immédiatement implémenté dans des notebooks Jupyter, garantissant que la théorie et le code se renforcent mutuellement.

### Concepts mathématiques essentiels pour Bitcoin

Cette première section établit le socle mathématique indispensable. Vous implémenterez l’arithmétique des corps finis et les opérations sur les courbes elliptiques (loi de groupe, addition, doublement, multiplication scalaire...) — les prérequis pour ECDSA. L’objectif est double : comprendre la structure algébrique qui rend possibles les signatures cryptographiques et construire des outils Python fiables pour les manipuler.

Vous formaliserez ensuite les composants de l’ECDSA : génération de clé, formatage de point, hachage, création et vérification de signature. Cette section relie directement la théorie à la pratique, en insistant sur les détails d’implémentation et la robustesse du modèle de sécurité sous-jacent.

### Fonctionnement interne d’une transaction Bitcoin

Dans la deuxième section, vous analyserez la structure d’une transaction Bitcoin : UTXO, entrées/sorties, séquences, scripts, encodages, et plus encore. Vous écrirez du code pour construire, signer et vérifier des transactions, acquérant ainsi une compréhension précise de ce que le hachage engage et pourquoi.

Ensuite, vous mettrez en œuvre un exécuteur _Script_ minimal, passerez en revue les principaux opcodes et validerez les chemins de dépense. L’objectif est de vous rendre capable d’auditer le comportement des transactions, de diagnostiquer les échecs de validation et de raisonner sur la sécurité des politiques de dépense.

### Fonctionnement interne du réseau Bitcoin

Dans la troisième section, vous replacerez la transaction dans le système global : structure des blocs, en-têtes, difficulté et mécanisme de preuve de travail (Proof-of-Work). Vous manipulerez les messages du protocole, les en-têtes de blocs et les arbres de Merkle.

Enfin, vous étudierez la communication entre nœuds pair à pair, l’optimisation des messages et l’introduction de SegWit.

Comme pour chaque cours de la Plan ₿ Academy, la section finale comprend une évaluation conçue pour consolider votre compréhension. Prêt à découvrir le fonctionnement interne de Bitcoin et à écrire le code qui le fait tourner ? Commençons !

# Concepts mathématiques essentiels pour Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Mathématiques pour la mise en œuvre de Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Cryptographie à courbe elliptique

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transaction Innerworkings

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Analyse des transactions et signatures ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Validation des scripts et des transactions

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Construction de transactions et Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Les rouages du réseau Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Blocs Bitcoin et Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Communication en réseau et arbres de Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Communication avancée entre nœuds et témoins séparés

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Section finale


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Critiques et évaluations


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Conclusion


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
