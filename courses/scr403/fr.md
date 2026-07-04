---
name: Plonger dans Simplicity
goal: Maîtriser la philosophie de conception, le système de types et le cycle de vie complet de Simplicity
objectives:
  - Comprendre les trois méthodes fondamentales de composition et les neuf combinateurs qui forment un langage complet
  - Construire la logique booléenne, l'arithmétique et SHA-256 à partir du système de types minimal de Simplicity
  - Saisir comment les effets de bord Failure et Reader permettent une véritable interaction avec la blockchain
  - Apprendre comment les programmes Simplicity deviennent des adresses Taproot et sont rachetés avec des données de témoin
---

# Plonger dans Simplicity

Une plongée en profondeur dans la théorie et les décisions de conception derrière le langage Simplicity, basée sur la série complète en cinq parties ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) par [Dr. Russell O'Connor](https://r6.ca/), le créateur de Simplicity chez Blockstream Research. Ce cours explique *pourquoi* Simplicity a été conçu de cette façon, pas comment l'écrire.

Le cours suit les articles du Dr. O'Connor à travers les trois façons fondamentales de combiner des calculs, le système de types minimal et son théorème de complétude, la construction de types de données pratiques et d'arithmétique à partir de premiers principes, l'introduction soigneuse d'effets de bord pour l'interaction avec la blockchain, et enfin comment les programmes sont engagés dans des adresses et rachetés on-chain.

+++

# Introduction

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Aperçu du cours

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Bienvenue dans SCR403 — Plonger dans Simplicity !

Ce cours est basé sur la série d'articles **"Delving Simplicity"** écrite par [Dr. Russell O'Connor](https://r6.ca/), un développeur en technologies d'infrastructure chez [Blockstream](https://blockstream.com/) et le créateur de Simplicity. Les articles originaux ont été publiés sur le forum [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) et constituent la source principale de ce cours. Nous lui sommes reconnaissants de son travail pionnier, qui a rendu possible ce contenu éducatif.

### Ce que vous allez apprendre

Ce cours explore la philosophie de conception et les fondements mathématiques de Simplicity, le langage de script de nouvelle génération activé sur le [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) en juillet 2025. Il suit la série complète de cinq articles et est structuré en deux sections de contenu principales :

1. **Les fondations de Simplicity** — Pourquoi le calcul sur blockchain exige un langage fondamentalement différent, les trois façons de combiner des opérations (séquentielle, parallèle, conditionnelle), et les neuf combinateurs de base qui forment un langage mathématiquement complet
2. **Des types de données aux programmes** — Construire la logique booléenne, l'arithmétique et SHA-256 à partir de premiers principes ; comprendre les effets de bord Failure et Reader qui permettent l'interaction avec la blockchain ; et apprendre comment les programmes sont engagés dans des adresses Taproot via des racines de Merkle d'engagement et rachetés avec des données de témoin

### Prérequis

Il s'agit d'un cours de **niveau expert** (environ 10 heures). Vous devriez être à l'aise avec :
- Les concepts de base du scripting Bitcoin (ce que fait la validation de transaction)
- Les concepts fondamentaux de programmation (types, fonctions, composition)
- Une certaine familiarité avec la notation mathématique est utile mais pas requise. Nous introduisons tout au fur et à mesure

### Ressources clés

- **Articles originaux** : ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) par Dr. Russell O'Connor sur Delving Bitcoin
- **Dépôt Simplicity** : [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — code source et preuves formelles Rocq
- **Site officiel** : [simplicity-lang.org](https://simplicity-lang.org/) — documentation et référence SimplicityHL
- **Blog Blockstream** : [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — aperçu technique

Prêt à plonger dans l'une des pièces d'ingénierie Bitcoin les plus élégantes ? C'est parti !

## Qu'est-ce que Simplicity ?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Si vous arrivez à ce cours sans connaissance préalable de Simplicity, ce chapitre vous orientera avant de plonger dans le grand bain.

### Simplicity en bref

Simplicity est un **langage de contrats intelligents natif de Bitcoin**, en production sur le Liquid Network aujourd'hui. Envisagé pour la première fois par le Dr. Russell O'Connor vers 2012 et détaillé dans son article de 2017 *Simplicity: A New Language for Blockchains*, il a été activé sur le Liquid Network en juillet 2025 après des années de vérification formelle et de développement.

Contrairement à Solidity d'Ethereum, qui est un langage de contrats de haut niveau Turing-complet, Simplicity est intentionnellement minimal. Il possède :
- **Trois constructeurs de types** (unité, somme, produit)
- **Neuf combinateurs** (opérations de base et règles de composition)
- **Aucune boucle, aucune récursion, aucune mémoire dynamique**

À partir de ces seules primitives, vous pouvez construire n'importe quel calcul nécessaire à la validation de transaction, de la logique booléenne au hachage SHA-256 complet.

### Que pouvez-vous faire avec Simplicity aujourd'hui ?

Simplicity alimente déjà de vraies applications sur le Liquid Network. La plus notable est le [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), une place de marché d'options sans oracle où les utilisateurs échangent des options d'achat sur du L-BTC en utilisant de l'USDt comme collatéral (le contrat sous-jacent prend aussi en charge les options de vente). Parmi les autres projets Simplicity en production figurent [Swaption](https://swaption.io/) par SideSwap (options) et le projet open source [Deadcat](https://github.com/Resolvr-io/deadcat) par Resolvr (marchés de prédiction). Au-delà de la DeFi, Simplicity permet des conditions de dépense avancées telles que des coffres-forts (vaults), des covenants et des schémas multisig complexes qui seraient impossibles ou dangereux en Bitcoin Script.

### Ce que ce cours est — et n'est pas

Ce n'est **pas** un tutoriel de codage pratique. Vous n'écrirez pas de programmes Simplicity ici. Si c'est ce que vous cherchez, consultez :
- [simplicity-lang.org](https://simplicity-lang.org/) — documentation officielle et le langage de haut niveau SimplicityHL
- Le [dépôt GitHub de Simplicity](https://github.com/BlockstreamResearch/simplicity) — implémentation de référence, exemples et preuves Rocq
- Le [billet de blog Blockstream](https://blog.blockstream.com/en-simplicity-github/) sur les premiers pas

Ce qu'est ce cours : les **choix philosophiques et techniques** derrière la conception de Simplicity. Pourquoi ce langage a-t-il été créé de cette façon ? Pourquoi seulement neuf combinateurs ? Pourquoi pas de récursion ? Pourquoi est-il important que le système de types se rattache au calcul des séquents de Gentzen ?

Pensez-y comme comprendre **pourquoi le moteur a été construit ainsi** plutôt qu'apprendre à conduire la voiture.

### À qui s'adresse ce cours ?

Ce cours est idéal pour :
- Les **développeurs de protocole** qui veulent comprendre les fondations de Simplicity avant d'écrire du code
- Les **chercheurs Bitcoin** intéressés par la vérification formelle et l'approche fondée sur la théorie des types
- Les **informaticiens** curieux du lien entre le calcul des séquents et le calcul sur blockchain
- Les **bitcoiners avancés** qui veulent aller au-delà d'une compréhension superficielle des capacités de scripting de Liquid

Si des termes comme « types somme », « combinateurs » ou « calcul des séquents » vous sont totalement inconnus, ne vous inquiétez pas, nous expliquons tout depuis le début. Mais préparez-vous à un voyage dense et mathématique.

### Des articles au cours

La série originale « Delving Simplicity » du Dr. O'Connor est structurée en cinq articles techniques. Ce cours réorganise et annote ce matériel en un parcours d'apprentissage progressif avec des quiz pour tester votre compréhension en chemin. Les idées, définitions et preuves sont les siennes, et nous avons adapté le format pour un enseignement structuré.

# Les fondations de Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Façons fondamentales de combiner des calculs

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Maintenant que Simplicity a été activé sur le Liquid Network, j'aimerais faire une plongée en profondeur dans la philosophie et la conception du langage Simplicity.

La validation de transaction de Bitcoin est une application significativement différente de la conception habituelle de langages de programmation. L'espace de bloc est une ressource rare, donc les programmes doivent être compacts. Les programmes dans les transactions Bitcoin ne sont exécutés que sur une seule entrée, et tout le monde exécute le programme sur la même entrée. De plus, l'agent qui autorise la transaction connaît déjà à l'avance le résultat du calcul : que la transaction est valide.

En général, l'agent qui autorise la transaction exécutera des calculs bien plus coûteux pour dériver des données de témoin attestant de la validité de la transaction, tandis que les programmes exécutés sur la blockchain doivent seulement vérifier la validité de ces données. Vérifier la validité est souvent bien moins coûteux que la prouver.

Nous avons conçu Simplicity en tenant compte de ce type de défis particuliers de conception de langage. Par exemple, Simplicity exige que les branches non exécutées soient élaguées afin qu'elles n'apparaissent pas sur la blockchain. Les étapes de prétraitement sont soigneusement conçues pour présenter une complexité temporelle (quasi-)linéaire dans la taille du programme Simplicity. L'analyse statique est utilisée à la place du « gas », qui ne peut pas être calculé sans exécuter le code d'une manière prescrite, afin que les détails du modèle d'exécution ne deviennent pas critiques pour le consensus. Aucune allocation dynamique de mémoire pendant l'exécution. Et ainsi de suite.

Avant de plonger dans les détails de conception de Simplicity, je veux commencer cette série par un peu de philosophie de programmation sur les façons générales de combiner des blocs de construction de base pour créer de nouvelles fonctionnalités.

### Composition

Supposons que l'on conçoive un langage pour des transactions programmables pour une blockchain comme Bitcoin. En particulier, les programmes n'ont accès qu'aux données de la transaction et aux données UTXO des entrées, et l'exécution ne fait que déterminer la validité de la transaction (ce qui permet de mettre en cache le résultat de l'exécution). Disons que l'on part d'un ensemble d'opérations de base capables d'effectuer diverses tâches telles que des calculs de base, la lecture et/ou le traitement de données de la transaction, et la vérification de signature. Chaque opération consomme un type d'entrée (éventuellement vide) et retourne un type de sortie. Quelles sont les façons de combiner ces opérations de base en opérations plus complexes ?

### Composition séquentielle

![Composition séquentielle](assets/en/001.webp)

La méthode de composition la plus fondamentale est la composition séquentielle. Si nous avons deux opérations de base, dont le type de données de sortie de l'une correspond au type de données d'entrée de l'autre, alors nous pouvons combiner ces deux opérations en une nouvelle opération composite. Cette nouvelle opération exécute ces deux opérations de base en séquence, prenant en entrée l'entrée de la première opération, transmettant la sortie de cette première opération à l'entrée de la seconde opération, et retournant finalement la sortie de cette seconde opération.

Bien sûr, nous n'avons pas besoin de nous restreindre à combiner uniquement des opérations de base. Maintenant que nous avons des opérations composites, nous pouvons également les combiner en utilisant la composition fonctionnelle.

En mathématiques, cette composition séquentielle est souvent simplement appelée « composition », et l'on pourrait penser que c'est la seule façon de composer des choses. Cependant, nous avons d'autres façons de composer des opérations.

### Composition parallèle

![Composition parallèle](assets/en/002.webp)

Supposons que nous ayons deux opérations, qui pourraient être des opérations de base ou complexes, et qu'elles prennent toutes deux le même type d'entrée. Une deuxième façon fondamentale de composer ces deux opérations est de les exécuter toutes deux sur la même entrée. C'est ce qu'on appelle la composition parallèle, et le type de sortie est le « produit » des types de sortie des opérations d'origine, et contient la paire des deux sorties.

Bien que cela s'appelle composition « parallèle », et que les deux opérations puissent en principe être exécutées en parallèle, l'exécution parallèle n'est pas une exigence opérationnelle. Nous pouvons implémenter la composition parallèle « séquentiellement » en exécutant d'abord une opération, puis la seconde. Peu nous importe la façon dont la composition parallèle est implémentée, tant que le résultat est le même.

### Composition conditionnelle

![Composition conditionnelle](assets/en/003.webp)

La composition conditionnelle est le dual de la composition parallèle. Dans ce cas, nous avons deux opérations qui produisent la même sortie, et nous les composons en choisissant celle des deux à exécuter. L'entrée de cette opération composite est la « somme » ou « union étiquetée » des types d'entrée des opérations d'origine. Dans ce cas, l'étiquette, « Left » ou « Right », est un seul bit dans les données de l'entrée qui détermine quel type de données est transporté, et donc laquelle des deux opérations peut être exécutée.

La composition conditionnelle fonctionne de la même manière même lorsque l'entrée est la somme de deux types identiques. Le type somme contient toujours une étiquette, et la valeur de cette étiquette détermine laquelle des deux opérations doit être exécutée.

### Composition en Bitcoin Script

Il existe de nombreuses façons de réaliser ces trois types de composition dans divers langages de programmation. En Bitcoin Script, la composition séquentielle est réalisée (approximativement) par la concaténation de deux routines (c'est pourquoi Bitcoin Script est appelé un langage de programmation concaténatif), puisque la sortie d'une routine est laissée sur la pile pour être consommée par la routine suivante. La composition parallèle est obtenue en utilisant des opérations de duplication et d'échange pour manipuler la pile afin que deux routines puissent s'exécuter sur la même entrée. Les choses ne sont pas entièrement simples, car ce que nous appelons le « produit » des types est généralement réalisé en utilisant plusieurs éléments de pile. Espérons que vous saisissez l'idée générale.

La composition conditionnelle est, bien sûr, réalisée par `OP_IF`, qui branche selon la valeur présente sur la pile. Dans ce cas, l'élément situé au sommet de la pile joue le rôle d'étiquette, et généralement l'élément ou les éléments suivants sur la pile sont de « types » différents selon la valeur de l'étiquette. Pour chaque cas, les types des éléments de pile ne peuvent convenir qu'à l'une des branches du `OP_IF`. Cependant, une fois arrivé à `OP_ENDIF`, les éléments de la pile doivent être de « type » cohérent, de sorte que le reste du script puisse continuer indépendamment de la branche empruntée précédemment.

### Composition en Simplicity

Nous avons conçu Simplicity avec des combinateurs qui implémentent directement ces trois formes de composition. Ajoutés à quelques combinateurs supplémentaires pour prendre en charge d'autres opérations de base liées aux types produit et somme, le langage Simplicity de base finit par comprendre neuf combinateurs suffisants pour exprimer tout calcul fini. Nous en discuterons plus en détail dans le prochain chapitre.

### Une quatrième forme de composition

Avant de terminer, il convient de mentionner qu'il existe au moins une autre forme de composition en informatique, la « composition récursive ». Dans la composition récursive, une opération est itérée plusieurs fois.

Notez que Bitcoin Script ne prend pas en charge la composition récursive, et de la même façon, nous avons explicitement exclu la récursion non bornée de la conception de Simplicity. Notre thèse est que le calcul itératif non borné est mieux implémenté en utilisant des covenants récursifs qui calculent sur plusieurs transactions. Cela permet aux utilisateurs d'éviter les contraintes d'espace de bloc et de standardité, et de mieux prédire les coûts de transaction.

Cela dit, il existe des façons de détourner la fonctionnalité de délégation de Simplicity pour fournir quelque chose ressemblant à une composition récursive non bornée, ce dont nous pourrons discuter plus tard dans cette série.

### Conclusion

Nous avons passé en revue les trois formes majeures de composition permettant de transformer des opérations de base en opérations complexes :

- la composition séquentielle
- la composition parallèle
- la composition conditionnelle

Nous avons discuté de la façon dont ces formes de composition sont réalisées en Bitcoin Script, et suggéré comment elles ont influencé la conception du langage Simplicity. Nous avons noté que la quatrième forme de composition, la composition récursive, est explicitement exclue à la fois de Simplicity et de Bitcoin Script.

Dans le prochain chapitre, nous décrirons les neuf combinateurs qui composent le cœur du langage Simplicity, comment ils permettent de réaliser directement ces trois formes de composition, et comment cela forme un langage complet pour décrire tout calcul fini.

## Complétude combinatoire de Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

Dans ce chapitre, nous présentons le langage Simplicity de base et montrons que le langage est complet, c'est-à-dire que tout calcul fini peut y être exprimé.

### Types de Simplicity

Simplicity prend en charge trois constructeurs de types fondamentaux. Le type produit `A × B` représente les sorties de la composition parallèle, tandis que le type somme `A + B` (union étiquetée) gère les entrées de la composition conditionnelle. Le troisième type est le type unité.

### Type unité

Le type unité, noté `𝟙` ou `ONE`, contient exactement une valeur : le tuple vide `⟨⟩` ou `()`. Ce type de donnée à zéro bit ne transporte aucune information.

### Type somme

Un type somme `A + B` combine deux types avec des étiquettes indiquant « gauche » ou « droite ». Les valeurs s'écrivent `σᴸ(a)` ou `inl(a)` pour les valeurs étiquetées à gauche, et `σᴿ(b)` ou `inr(b)` pour les valeurs étiquetées à droite. Les étiquettes restent distinctes même en combinant des types identiques.

#### Type booléen

Le type `𝟙 + 𝟙`, noté `𝟚` ou `TWO`, représente un type à un bit avec deux valeurs. Par convention, `σᴸ⟨⟩` représente faux/zéro, tandis que `σᴿ⟨⟩` représente vrai/un.

### Type produit

Les types produit `A × B` contiennent des paires de valeurs écrites `⟨a, b⟩` ou `(a, b)`. Le type `𝟚 × 𝟚` a quatre valeurs, distinctes des quatre valeurs de `𝟚 + 𝟚`.

### Expressions Simplicity de base

Les opérations sont notées `f : A ⊢ B`, ce qui signifie type d'entrée `A` et type de sortie `B`. Simplicity est « du premier ordre » — il n'a pas de types fonction.

### Deux opérations de base

Le langage de base fournit deux opérations de base :

**Identité (`iden`).** L'opération identité transmet son entrée sans la modifier :

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unité (`unit`).** L'opération unité rejette son entrée et retourne le tuple vide :

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Ces opérations forment des familles avec une opération par type.

### Trois combinateurs de composition

La composition séquentielle utilise `comp f g` (écrit `f ⨾ g` ou `f >>> g`) :

```
Si f : A ⊢ B et g : B ⊢ C, alors
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

La composition parallèle utilise `pair f g` (écrit `f ▵ g` ou `f &&& g`) :

```
Si f : A ⊢ B et g : A ⊢ C, alors
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

La composition conditionnelle utilise `case f g : (A + B) × C ⊢ D`, donnant aux branches accès à l'environnement partagé `C` :

```
Si f : A × C ⊢ D et g : B × C ⊢ D, alors
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Pourquoi la composition conditionnelle prend-elle cette forme — une somme associée à un environnement partagé `C` — plutôt qu'un simple `copair f g : A + B ⊢ C` qui se contenterait de choisir une branche ? Parce qu'un `copair` nu ne peut pas exprimer la **distribution** : la fonction `dist : (A + B) × C ⊢ A × C + B × C` qui pousse une entrée partagée dans la branche choisie. En intégrant directement l'environnement `C` dans `case`, Simplicity obtient à la fois la composition conditionnelle *et* la distribution à partir d'un seul combinateur — l'une des décisions de conception clés qui permettent de limiter le langage de base à neuf combinateurs.

### Quatre combinateurs supplémentaires

La consommation de produits utilise `take` et `drop` :

**take** extrait l'élément de gauche :

```
Si f : A ⊢ C, alors
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extrait l'élément de droite :

```
Si f : B ⊢ C, alors
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

La production de sommes utilise `injl` et `injr` :

**injl** enveloppe avec une étiquette gauche :

```
Si f : A ⊢ B, alors
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** enveloppe avec une étiquette droite :

```
Si f : A ⊢ C, alors
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Les neuf combinateurs de base

Au total, Simplicity possède exactement neuf combinateurs de base :

| Combinateur | Rôle |
|---|---|
| `iden` | Transmet l'entrée |
| `unit` | Rejette l'entrée |
| `comp` | Composition séquentielle |
| `pair` | Composition parallèle |
| `case` | Composition conditionnelle |
| `take` | Extrait la gauche du produit |
| `drop` | Extrait la droite du produit |
| `injl` | Injecte dans la gauche de la somme |
| `injr` | Injecte dans la droite de la somme |

### Simplicity et le calcul des séquents

La conception de Simplicity dérive du fragment conjonctif-disjonctif du calcul des séquents de Gentzen. Plus précisément, il s'agit d'une variante de l'*interprétation fonctionnelle* du calcul des séquents, elle-même analogue à la correspondance de Curry-Howard entre déduction naturelle et calcul lambda. Les règles des combinateurs présentent des « types plus petits dans les prémisses que dans les conclusions », ce qui permet à la Bit Machine — l'interpréteur abstrait à pile de Simplicity — de minimiser la copie de données pendant l'exécution.

### Les valeurs ne sont pas des expressions

Les expressions Simplicity dénotent des opérations, pas des valeurs. La notation `scribe b : A ⊢ B` représente une expression unique qui retourne toujours la valeur `b`, servant de commodité de notation plutôt que de combinateur. Cela reflète le fonctionnement de Bitcoin Script, où des opérations comme `OP_1` empilent des valeurs plutôt que de les exprimer directement.

### Le théorème de complétude de Simplicity

Avec les neuf combinateurs en main, comment savoir qu'il ne nous manque rien — que ces neuf-là suffisent réellement ? Le théorème de complétude de Simplicity répond à cette question : pour toute fonction entre types Simplicity (finis), une expression Simplicity la dénote. La preuve est constructive — elle montre comment construire l'expression :

1. **Décomposer l'entrée** : à l'aide d'expressions `case` imbriquées, décomposer entièrement toute entrée de tout type en ses bits constitutifs
2. **Construire une table de correspondance** : pour chaque entrée possible, utiliser `scribe` pour produire la sortie correspondante
3. **Assembler** : les `case` imbriqués et les `scribe` forment ensemble une immense table de correspondance qui implémente la fonction

Ce théorème est formellement vérifié dans l'assistant de preuve Rocq (anciennement Coq). La preuve fait partie du dépôt officiel de Simplicity et a été vérifiée automatiquement.

Bien que le théorème de complétude garantisse que les neuf combinateurs de Simplicity peuvent exprimer toute fonction entre types Simplicity (finis), les expressions résultant de la construction par table de correspondance sont d'une taille impraticable. Une fonction sur des entrées de 256 bits nécessiterait une table de correspondance avec 2²⁵⁶ entrées. C'est pourquoi les chapitres suivants se concentrent sur la construction d'expressions efficaces qui exploitent la structure des calculs, plutôt que de tout résoudre en force brute via des tables de correspondance.

### Conclusion

Le langage de base de Simplicity comprend un système de types et des combinateurs permettant tout calcul fini. Bien que le théorème de complétude garantisse l'expressivité, les expressions résultant de la construction générique sont d'une taille impraticable. Le développement pratique en Simplicity consiste à exploiter la structure computationnelle pour produire des expressions concises. Les chapitres suivants explorent les structures de données, les interactions avec les transactions et des combinateurs supplémentaires.

# Des types de données aux programmes

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Construire des types de données

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

Dans les chapitres précédents, nous avons montré comment l'ensemble de combinateurs de base de Simplicity suffit à implémenter tout calcul pur fini. Ce chapitre montre comment construire des structures de données et des calculs pratiques à partir de ces primitives — de la même façon que les ordinateurs sont construits à partir de portes logiques.

### Logique booléenne

Le type booléen, noté `𝟚`, égal à `𝟙 + 𝟙`, a deux valeurs : `σᴸ⟨⟩` (faux) et `σᴿ⟨⟩` (vrai). En utilisant les combinateurs de base, les opérateurs de logique booléenne peuvent être construits.

#### Opération And

L'opération logique `and : 𝟚 × 𝟚 ⊢ 𝟚` prend deux bits et retourne un bit. L'implémentation branche sur le premier bit : s'il est faux, retourne faux ; sinon, retourne le second bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Test avec `⟨false, false⟩` :

```
⟦and⟧⟨false, false⟩
 = {développer la notation pour false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {développer la définition de and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {évaluer case pour σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {évaluer injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {évaluer unit}
σᴸ⟨⟩
 = {par la notation pour false}
false
```

Test avec `⟨true, true⟩` :

```
⟦and⟧⟨true, true⟩
 = {développer la notation pour true et la définition de and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {évaluer case pour σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {évaluer drop}
⟦iden⟧(σᴿ⟨⟩)
 = {évaluer iden}
σᴿ⟨⟩
 = {par la notation pour true}
true
```

#### Autres opérations logiques

L'opération `not` nécessite un combinateur auxiliaire :

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Le `iden ▵ unit : A ⊢ A × 𝟙` initial ajoute un « environnement » vide à l'entrée, permettant l'application du combinateur `case`. L'utilisation de `take` dans les deux branches rejette cet environnement vide pour exécuter `f` ou `g`.

Autres opérations logiques booléennes :

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Additionneurs de bits

Un « demi-additionneur » prend deux bits et les additionne, produisant une sortie de deux bits : un bit de retenue et un bit de somme.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Un « additionneur complet » additionne trois bits, produisant une sortie de deux bits. L'entrée utilise le tuple imbriqué `(𝟚 × 𝟚) × 𝟚`.

Pour les tuples imbriqués, une notation compacte est utilisée :

- `O f` désigne `take f`
- `I f` désigne `drop f`
- `H` désigne `iden`

Par exemple, `I O H` signifie `drop (take iden) : A × (B × C) ⊢ B`, extrayant la valeur du milieu. La notation évoque les chiffres binaires : en pensant aux tuples imbriqués comme des arbres binaires, la notation représente les chiffres binaires inversés des positions dans l'arbre. Ces expressions forment des indices de De Bruijn pour Simplicity.

**Note :** la notation `I`, `O` et `H` ne s'applique qu'aux sous-expressions constituées uniquement de `take`, `drop` et `iden`.

L'additionneur complet compose deux demi-additionneurs, en prenant le `or` logique des bits de retenue :

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

Dans la première ligne, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` exécute le demi-additionneur sur les deux premiers bits, en conservant le dernier bit.

Dans la deuxième ligne, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` conserve le premier bit (la retenue sortante du premier demi-additionneur) et exécute le demi-additionneur sur les deux derniers bits.

Dans la dernière ligne, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` prend le OR logique des deux premiers bits (retenues sortantes des deux demi-additionneurs) et retourne le bit de somme sortante du second demi-additionneur.

Ceci illustre la programmation en Simplicity : utiliser la notation `I`, `O` et `H` pour référencer des bits de données, formant des « environnements » adaptés pour appeler d'autres fonctions via composition séquentielle.

Les utilisateurs ne définissent pas directement les opérations de bas niveau. Plus loin dans cette série, nous aborderons les jets de la bibliothèque standard qui implémentent les fonctions courantes. Les utilisateurs finaux ne sont pas censés programmer directement en Simplicity, à l'instar de Bitcoin Script. À la place, des langages de plus haut niveau comme SimplicityHL génèrent du code Simplicity, gérant les « environnements » des sous-expressions et traduisant les variables nommées en séquences appropriées de `take` et `drop`.

### Vecteurs

Les vecteurs de longueur fixe sont définis en formant des produits itérés du type `A` :

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Ils peuvent aussi s'écrire `A^2`, `A^4`, `A^8`, etc.

Les vecteurs ne sont définis que pour des longueurs qui sont des puissances de deux. Les autres longueurs nécessitent de choisir des conventions de parenthésage.

Étant donné une expression `f : A ⊢ B`, l'associer par paires répétées la « mappe » sur des vecteurs de longueur fixe :

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Étant donné une fonction `f : A × B ⊢ B`, l'itération ou le « repliement » (folding) sur des vecteurs de longueur fixe :

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

De nombreuses variantes existent. Étant donné `f : A × B ⊢ C`, on peut « zipper » sur des vecteurs appariés avec `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Étant donné `f : (A × B) × C ⊢ C`, on peut replier sur des vecteurs appariés avec `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Combiner `map` et `fold-right` crée des combinateurs accumulateurs : `f : A × C ⊢ C × B` produit `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Bien d'autres variantes sont possibles.

#### Mots multi-bits

Un vecteur de bits produit des entiers multi-bits. Par exemple, `𝟚³²` est un type mot de 32 bits. `𝟚²⁵⁶` est un type mot de 256 bits, adapté aux hachages et opérations cryptographiques.

En utilisant l'additionneur complet, une variante des opérations sur vecteurs définit un « additionneur à propagation de retenue » sur des mots multi-bits :

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` prend deux nombres binaires de n bits et une retenue entrante d'un bit, et retourne un drapeau de retenue sortante d'un bit et une somme de n bits.

#### SHA-256

En définissant récursivement des opérations arithmétiques sur les mots multi-bits — soustraction, multiplication, division — et des opérations logiques bit à bit telles que AND, OR, XOR logiques, et en combinant celles-ci de façon répétée, on peut même construire la fonction de compression de bloc de SHA-256 :

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

La compression SHA-256 est formellement définie en Simplicity au sein de l'assistant de preuve Rocq (anciennement Coq), avec une preuve formelle que l'implémentation `sha256-hash-block` est correcte.

La compression s'exécute trop lentement en Simplicity brut. Les jets exécutent nativement des fonctions courantes comme la compression SHA-256. Les implémentations Simplicity pures servent de spécifications formelles pour les jets.

### Types optionnels

Les types optionnels résultent d'une somme avec le type unité :

```
Option A ≔ 𝟙 + A
```

Le type `Option A` peut s'écrire `A?` ou `𝕊 A` (où `𝕊` signifie « successeur »). Les fonctions se mappent sur les types optionnels :

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Des combinateurs monadiques tels que bind peuvent être définis :

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Tampons de longueur variable

Les « tampons » (buffers) sont des types pour les vecteurs partiellement remplis :

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Le type `Xᑉ⁸` se développe en `(1 + X⁴) × ((1 + X²) × (1 + X))`. En traitant cela comme un polynôme et en le développant, on obtient `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Interprété comme un type, cela représente la somme de tous les tuples possibles de X jusqu'à 7, y compris le tuple vide. C'est exactement le type des listes de longueur strictement inférieure à 8.

Comme pour les vecteurs, des opérations de mappage et de repliement peuvent être définies sur les tampons. Les opérations de pile incluent `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` et `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` ajoute un élément au tampon, retournant un vecteur complet en cas de débordement. `pop-<n` retire un élément, retournant le tampon plus petit et l'élément retiré, ou éventuellement rien si le tampon d'origine était vide.

La définition de `push-<n`, de façon récursive :

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Simplicity brut devient difficile à suivre au-delà d'un certain niveau de complexité. Les utilisateurs finaux utilisent des langages de plus haut niveau comme SimplicityHL qui génèrent ces expressions idiomatiques.

### Conclusion

Ce chapitre a montré comment construire des opérations logiques à partir de bits. À partir de là, l'arithmétique au niveau des bits a émergé, permettant de raisonner sur l'exécution. Des types vecteurs ont été développés, démontrant l'itération sur des mots multi-bits pour la définition de l'arithmétique. En poursuivant, des opérations cryptographiques comme SHA-256 et la validation de signature Schnorr peuvent être définies en utilisant uniquement des combinateurs Simplicity — toutes effectivement définies avec Simplicity.

Ce chapitre n'est pas un guide exhaustif de tous les types de données et opérations constructibles en Simplicity, mais illustre la réalisation de fonctionnalités pratiques dans les contraintes de Simplicity. Malgré des types finis et bornés, des vecteurs utiles, des types tampon et des opérations itérant sur ces structures peuvent être définis.

Les spécifications réelles des opérations de la bibliothèque standard diffèrent légèrement des définitions données ici. Par exemple, l'additionneur complet utilise un XOR à 3 entrées et une fonction logique « majorité » plutôt que deux demi-additionneurs.

En pratique, les programmes Simplicity utilisent des jets pour les opérations arithmétiques et cryptographiques. Cependant, les jets ne remplacent que des expressions. Les combinateurs itérant sur des tampons et des vecteurs ne peuvent pas être remplacés par des jets, et apparaissent dans les programmes Simplicity réels. Bien que plutôt que de les utiliser directement, les utilisateurs finaux emploient des langages de plus haut niveau comme SimplicityHL qui génèrent de telles expressions.

Les combinateurs définis récursivement semblent croître de façon exponentielle en taille d'expression. Ce n'est pas problématique. Lors de la sérialisation, les expressions sont encodées sous forme de DAG (graphes orientés acycliques) plutôt que d'arbres. La représentation réelle ne croît que linéairement.

Jusqu'à présent, seuls des calculs purs ont été considérés. L'interaction avec les données de transaction pour des tâches comme la signature de transactions nécessite un moyen pour les programmes d'échouer si les signatures sont invalides. Le prochain chapitre aborde les effets de bord en Simplicity.

## Deux effets de bord

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

Dans les chapitres précédents, nous avons montré comment construire certaines structures de données et calculs en utilisant l'ensemble de combinateurs de base de Simplicity. Comme nous l'avons noté, les combinateurs de base suffisent à implémenter tout calcul pur fini. Cela soulève une question : que peut-on obtenir de plus ? Nous pouvons ajouter des effets de bord supplémentaires à nos expressions.

Il existe divers types d'effets de bord possibles pour les expressions : mise à jour d'état, écriture dans un journal, levée d'exception, lecture depuis un environnement, appel d'une continuation, etc. Les effets de bord disponibles en Simplicity dépendent de l'application.

Pour les applications Bitcoin et Liquid, nous disposons actuellement de deux effets de bord : l'effet Failure, qui est un effet d'exception dont l'exception est de type `𝟙`, et l'effet Reader, qui permet d'accéder aux données de l'environnement de la transaction. Nos combinateurs de base sont « purs » ; ils n'ont aucun effet de bord. Cependant, les jets peuvent introduire de nouvelles primitives qui, elles, ont des effets de bord.

### Jets avec effets

Nous parlerons davantage des jets plus loin dans ce cours, mais nous présentons ici quelques jets d'exemple pour illustrer leurs effets de bord.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` est un jet pour une expression qui prend une clé publique x-only, un message de 256 bits et une signature Schnorr, et ne retourne rien ! D'après son type, il devrait se comporter comme un `unit`. La différence réside dans l'effet de bord du jet : si la validation de la signature échoue, alors tout le calcul est interrompu en levant une exception (de type unité). C'est l'effet Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` est un jet minimaliste pour exprimer l'effet Failure. Si l'entrée de `verify` est `false`, tout le calcul est interrompu en levant une exception. Si l'entrée est `true`, rien n'est retourné, mais le calcul peut continuer.

#### Hachages de transaction

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` semble être une fonction constante, puisqu'il n'existe qu'une seule valeur d'entrée possible : le tuple vide. Cependant, ce jet lit dans l'environnement de la transaction et produit un hachage des données de la transaction analogue au condensé de message `SIGHASH_ALL` utilisé dans la vérification de signature de Bitcoin Script. C'est un exemple de l'effet Reader : la valeur retournée dépend de l'environnement de transaction dans lequel le jet est exécuté. Il existe plusieurs autres jets de hachage qui hachent divers sous-ensembles des données de l'environnement de transaction pour aider à construire des condensés de message personnalisés pour les signatures.

#### Jets d'introspection

`input-sequence : 𝟚³² ⊢ 𝟚³²?` est une fonction qui prend un index d'entrée et retourne le numéro de séquence de la transaction pour cette entrée, retournant éventuellement rien si l'index est hors limites. Là encore, la valeur de sortie n'est pas une fonction pure de l'index d'entrée, mais l'opération utilise plutôt l'effet Reader pour accéder à l'environnement de transaction afin de déterminer la valeur de sortie. Il existe plusieurs autres jets d'introspection qui retournent divers fragments des données de l'environnement de transaction.

### Classer les effets

Tous les effets de bord ne sont pas égaux. Certains effets de bord se comportent mieux que d'autres. Nous pouvons classer les effets selon leur aptitude aux transformations de programme.

#### Effets commutatifs

Un effet commutatif est un effet tel que, si vous échangez les sorties de deux expressions, vous pouvez échanger sans risque les expressions elles-mêmes sans changer l'effet de l'expression. Considérons `swap = I H ▵ O H : A × B ⊢ B × A`. Si `f ▵ g ⨾ swap = g ▵ f` pour toute expression `f` et `g` avec effets de bord, alors les effets sont commutatifs.

Lire des données de transaction depuis l'environnement est un effet commutatif, car le résultat de la lecture dans l'environnement est le même, quel que soit l'ordre dans lequel nous exécutons la lecture.

En général, lever une exception n'est pas un effet commutatif. Si `f` lève une exception `e₁` et `g` lève une autre exception `e₂`, alors l'exception levée par la paire de `f` et `g` dépend de l'ordre dans lequel ils sont exécutés.

Cependant, dans le cas particulier de l'effet Failure, où seule une exception de type unité peut être levée, l'effet est commutatif. Peu importe lequel de `f` ou `g` lève une exception, l'exception résultante sera la même, car il n'existe qu'une seule valeur d'exception possible.

#### Effets idempotents

Un effet idempotent est un effet tel que, si vous dupliquez la sortie d'une expression, vous pouvez dupliquer sans risque l'expression elle-même sans changer l'effet de l'expression. Considérons `dup = iden ▵ iden : A ⊢ A × A`. Si `f ⨾ dup = dup ⨾ f ▵ f` pour tout `f` avec effets de bord, alors les effets sont idempotents.

Lire des données de transaction depuis l'environnement est un effet idempotent. Lever une exception est également un effet idempotent. Même si une seule des deux expressions dupliquées sera exécutée, toute exception levée par `dup ⨾ f ▵ f` sera la même que l'exception levée par `f ⨾ dup`.

Cependant, écrire dans un journal peut ne pas être idempotent, car dupliquer l'effet ferait apparaître le message de journal deux fois. Toutefois, si le journal consiste en un *ensemble* de messages plutôt qu'une *liste* de messages, alors l'effet serait idempotent (et commutatif), car l'insertion dans un ensemble est elle-même une opération idempotente.

#### Effets unitaires

Un effet unitaire est un effet tel que, si vous rejetez la sortie d'une expression, vous pouvez rejeter sans risque l'expression elle-même sans changer ses effets. Si l'on a toujours `f ⨾ unit = unit` pour tout `f` avec effets de bord, alors vos effets sont unitaires.

Lire des données depuis l'environnement est l'un des rares types d'effets unitaires. Si le résultat de la lecture des données de transaction depuis l'environnement est rejeté, l'ensemble de l'expression effectuant la lecture peut être rejeté.

L'effet Failure n'est pas unitaire. Si `f` lève une exception, alors `f ⨾ unit` en lèvera une aussi ; l'exécution n'atteindra même pas le combinateur `unit` avant que le calcul ne soit interrompu. En revanche, `unit` ne lèverait évidemment aucune exception, donc les effets de `f ⨾ unit` et de `unit` seraient différents.

Pour résumer, voici comment les effets discutés ci-dessus se situent par rapport à ces trois propriétés :

| Effet | Commutatif | Idempotent | Unitaire |
| --- | :---: | :---: | :---: |
| Reader (environnement de transaction) | ✓ | ✓ | ✓ |
| Failure (exception de type unité) | ✓ | ✓ | ✗ |
| Writer (journal comme ensemble) | ✓ | ✓ | ✗ |
| Exceptions générales (type arbitraire) | ✗ | ✓ | ✗ |

### Effets autorisés en Simplicity

Plus un type d'effet a de propriétés bien comportées, plus un optimiseur Simplicity dispose de marge pour transformer les programmes qui utilisent ces effets. Idéalement, nous n'autoriserions que des effets possédant les trois propriétés : commutatif, idempotent et unitaire. Cela permettrait à un optimiseur d'effectuer n'importe quel type de transformation de programme qu'il souhaite. Cependant, la lecture depuis un environnement est le seul effet qui satisfait aux trois propriétés.

Nous exigeons plutôt que les effets de Simplicity soient commutatifs et idempotents. Les deux effets que nous utilisons en Simplicity, l'effet Failure et l'effet Reader, sont commutatifs et idempotents. Cela permet d'effectuer une large classe d'optimisations sur le code Simplicity.

Cependant, la transformation « rejet » décrite ci-dessus, qui tente de remplacer `f ⨾ unit` par `unit`, ou toute transformation similaire, n'est pas autorisée si `f` peut produire un effet Failure. En effet, imaginez que `f` contienne une assertion `bip0340-verify`. Il serait désastreux de tenter d'optimiser cette vérification en la supprimant.

### Pourquoi autoriser des effets de bord ?

Pourquoi Simplicity autorise-t-il même des effets de bord ? Ne serait-il pas préférable que chaque programme prenne la transaction entière en entrée et retourne une sortie booléenne décidant si une transaction est valide ou non ?

#### Vérification par lots

L'une des raisons pour lesquelles nous avons l'effet Failure est de prendre en charge la [vérification par lots](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) des signatures Schnorr. Dans la vérification par lots, de nombreuses vérifications individuelles de signatures Schnorr sont regroupées de telle sorte que si une seule vérification de signature échoue, alors le lot entier échoue.

Cette procédure de regroupement améliore l'efficacité par rapport à la vérification individuelle de chaque signature. L'inconvénient est que si la vérification par lots échoue, nous ne savons pas quelle vérification de signature spécifique a échoué.

En utilisant l'effet de bord Failure, `bip0340-verify` garantit que si une vérification de signature échoue, la transaction entière échoue. Si `bip0340-verify` retournait plutôt `𝟚`, un type booléen, pour indiquer le succès ou l'échec, alors une vérification de signature en échec pourrait quand même mener à une branche où le script réussit. Dans un tel cas, nous aurions besoin de savoir si la signature particulière est valide ou non, et nous ne pourrions donc pas tirer parti de la vérification par lots.

#### Données de transaction précalculées

Un problème du Bitcoin Script des débuts était que la fonction de hachage utilisée pour créer les condensés de message pour les signatures était linéaire dans la taille de la transaction. En général, chaque entrée crée au moins un condensé de message pour la vérification de signature, donc la quantité totale de hachage était quadratique dans la taille de la transaction.

Ce problème a été résolu par Segwit et les itérations ultérieures de Bitcoin Script en redéfinissant les condensés de message de sorte qu'ils puissent être calculés en temps constant par vérification de signature. Cela repose sur `PrecomputedTransactionData`, qui précalcule les hachages des données de transaction une seule fois, puis les partage entre les calculs de sighash de chaque entrée. Les jets de hachage de transaction de Simplicity reposent sur le même type de données de transaction précalculées pour garantir que les jets s'exécutent en temps constant.

Supposons que `sig-all-hash` n'utilise pas l'effet Reader. Supposons que nous ayons réussi à construire un type Simplicity pour l'environnement de transaction. Appelons-le `TxEnv`, de sorte que `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` soit le type du jet. Une telle définition exigerait que le jet `sig-all-hash` puisse calculer le hachage de n'importe quelle transaction, pas seulement celle à laquelle il est associé. Les programmes Simplicity pourraient copier le `TxEnv` donné et passer une copie modifiée de celui-ci à `sig-all-hash`. Dans un tel cas, `sig-all-hash` ne pourrait pas s'appuyer sur `PrecomputedTransactionData`, et nous nous retrouverions à exiger un temps linéaire dans quelque donnée de transaction que ce soit passée à cette version de `sig-all-hash`.

Parce que `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` utilise l'effet Reader pour accéder aux données de transaction, il n'a *que* accès à un environnement de transaction fixe. Pour cette raison, l'implémentation du jet peut utiliser en toute sécurité `PrecomputedTransactionData` et fonctionner en temps constant.

### Agrégation de signatures inter-entrées

Bien que ni Liquid ni Bitcoin ne prennent en charge l'[agrégation de signatures inter-entrées](https://hrf.org/latest/cisa-research-paper/) (cross-input signature aggregation) à l'heure actuelle, nous aimerions vérifier que Simplicity puisse être compatible avec cette fonctionnalité le moment venu.

Bien que les détails n'aient pas été finalisés, nous imaginons une demi-agrégation implémentée en utilisant un effet Writer. C'est-à-dire qu'un nouveau jet avec un type tel que `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` prendrait une clé publique, un condensé de message et la composante `r` d'une signature Schnorr (une signature Schnorr est constituée d'une composante `r` et d'une composante `s`) et l'écrirait dans un journal de transaction avant de poursuivre l'exécution. Ensuite, ailleurs dans la transaction ou avec celle-ci, une composante `s` agrégée pour toutes les signatures Schnorr demi-agrégées serait fournie. La transaction ne serait valide que si une telle composante `s` agrégée est fournie pour toutes les clés, messages et composantes `r` journalisés.

Pour répondre aux exigences de Simplicity, cet effet Writer doit être idempotent et commutatif. Cela peut être garanti en traitant le journal du writer comme un ensemble de tuples clé, message, composante `r`. Cela fonctionne parce que les opérations d'ensemble sont idempotentes et commutatives. Traiter le journal comme un ensemble de valeurs serait compatible avec l'algorithme de vérification de demi-agrégation.

### Conclusion

Dans ce chapitre, nous avons examiné l'ajout d'effets de bord aux calculs que Simplicity peut effectuer. Nous avons classé divers types d'effets selon leur comportement vis-à-vis de différents types de transformation de programme. Nous avons décidé de restreindre les effets de Simplicity à ceux qui sont commutatifs et idempotents.

Les deux effets que nous utilisons pour les applications Bitcoin et Liquid sont l'effet Reader, pour accéder à l'environnement de transaction, et l'effet Failure, pour interrompre et faire échouer le programme. Certains jets utilisent des opérations primitives où ces types d'effets de bord peuvent se produire.

L'effet Failure détermine la sortie d'un programme Simplicity : le programme échoue, invalidant la transaction, ou le programme réussit. L'effet Reader fournit un type d'entrée à un programme Simplicity : l'environnement contenant les données de transaction. Mais nous devons également fournir d'autres entrées, comme des signatures numériques, aux programmes Simplicity.

Dans le prochain chapitre, nous verrons ce que sont les programmes Simplicity, comment ils deviennent des adresses, et comment nous ajoutons d'autres entrées, comme des signatures, aux programmes Simplicity.

## Programmes et adresses

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

Dans le chapitre précédent, nous avons décrit deux effets de bord utilisés en Simplicity : l'effet Failure, qui détermine le succès ou l'échec d'un programme, et l'effet Reader, qui donne accès à l'environnement de transaction. Nous nous tournons maintenant vers la question pratique : qu'est-ce exactement qu'un programme Simplicity, et comment devient-il une adresse sur la blockchain ?

### Programmes Simplicity

Un programme Simplicity est défini comme une expression Simplicity de type `𝟙 ⊢ 𝟙`. Cette signature de type signifie que le programme ne prend aucune entrée significative (juste la valeur unité) et ne produit aucune sortie significative (juste la valeur unité). L'effet Reader capture l'entrée de l'environnement de transaction, tandis que l'effet Failure indique le succès ou l'échec. Ces effets gèrent les entrées/sorties plutôt que les types Simplicity eux-mêmes.

### Racine de Merkle d'engagement

Plutôt que de stocker des programmes complets on-chain, Bitcoin emploie des engagements — une pratique héritée de Pay-to-Script-Hash (P2SH). Simplicity utilise une racine de Merkle d'engagement (Commitment Merkle Root, CMR).

Chaque combinateur reçoit une étiquette SHA-256 dérivée du modèle : `Simplicity␟Commitment␟[identifiant]`, où `␟` représente le code ASCII 31 (le séparateur d'unité).

Chaque étiquette est le hachage SHA-256 de la chaîne pré-image correspondante listée ci-dessous :

| Combinateur | Pré-image de l'étiquette (chaîne ASCII) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Une expression Simplicity est ensuite hachée récursivement en un CMR de 256 bits en calculant un état intermédiaire (midstate) SHA-256 étiqueté pour chaque combinateur, ainsi que les CMR de ses arguments (notons `#ᶜ(e)` le CMR de l'expression `e`, et `∥` la concaténation d'octets) :

| Combinateur | Règle du CMR |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Les combinateurs binaires (`comp`, `pair`, `case`) concatènent les CMR des deux enfants ; les combinateurs unaires (`take`, `drop`, `injl`, `injr`) concatènent le CMR de leur unique enfant après un remplissage (padding) de 32 octets à `0x00` ; et les feuilles nullaires (`iden`, `unit`) hachent leur étiquette seule. Deux conventions permettent de garder ce calcul peu coûteux : des midstates SHA-256 sont utilisés de sorte que **chaque expression nécessite au plus un appel à la fonction de compression SHA-256** (en supposant que le midstate jusqu'aux étiquettes constantes est précalculé), et les constructeurs à un argument préfixent leur argument avec 32 octets de remplissage `0x00`, ce qui permet un peu de précalcul supplémentaire pour les implémentations qui le souhaitent.

Pour le combinateur `unit` — un constructeur nullaire sans sous-expression argument — cette règle se spécialise en `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, où `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (l'étiquette est fournie deux fois). Le CMR résultant pour le programme trivial `unit` est :

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

De façon cruciale, le CMR ne s'engage pas sur les types des expressions Simplicity, s'appuyant à la place sur l'inférence de type lors du rachat.

### Adresses

Les adresses emploient le mécanisme Taproot du BIP-0341, avec les CMR engagés sous la version de TapLeaf `0xbe`. Le processus comprend :

1. Le calcul d'un hachage étiqueté TapLeaf combinant l'octet de version, la longueur du CMR et le CMR lui-même
2. L'ajustement (tweak) d'une clé publique interne (en utilisant un point NUMS lorsqu'aucun chemin de dépense par clé n'est souhaité)
3. La conversion au format bech32m
4. L'ajout des sommes de contrôle appropriées

Lorsqu'aucun chemin de dépense par clé n'est souhaité, la clé publique interne est fixée à un point **NUMS** (« Nothing-Up-My-Sleeve », rien dans la manche) : un point de courbe délibérément choisi de sorte que personne ne connaît son logarithme discret — en d'autres termes, un point sans clé privée correspondante. Comme personne ne peut jamais produire de signature pour lui, le chemin de dépense par clé est prouvablement inutilisable, et la sortie ne peut être dépensée *que* via le chemin de script Simplicity engagé. Dans une application réelle, ce point NUMS devrait être randomisé, comme le recommande le BIP-0341, afin que les sorties sans chemin de dépense par clé soient indistinguables des sorties Taproot ordinaires (un avantage en matière de confidentialité).

#### De Simplicity à l'adresse

Parcourons ensemble toute la dérivation pour le programme le plus simple possible : `unit : 𝟙 ⊢ 𝟙`, un no-op qui réussit toujours.

**1. Étiquette du combinateur.** Calculer d'abord l'étiquette de `unit` :

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Fournir l'étiquette deux fois pour obtenir le CMR du programme :

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. Hachage TapLeaf.** Préfixer le CMR avec la version de TapLeaf de Simplicity `0xbe` et la longueur du CMR `0x20` (32 octets), puis calculer le hachage étiqueté TapLeaf d'Elements (un hachage étiqueté est `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`) :

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Avec cette seule feuille, il n'y a pas de TapBranch, donc ce hachage est déjà la racine du TapTree.

**4. TapTweak.** Puisque nous ne voulons aucun chemin de dépense par clé, nous utilisons le point NUMS du BIP-0341 comme clé interne et l'ajustons avec la racine du TapTree :

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Clé de sortie.** Ajuster la clé interne sur la courbe, `output_pk = lift_x(internal_pk) ⊕ t·G` (l'arithmétique sur courbe elliptique est résumée ici), donnant la clé de sortie x-only `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Adresse Bech32m.** Encoder la clé de sortie x-only, préfixer un `p` (le caractère de version de témoin SegWit v1), ajouter le préfixe lisible par un humain du testnet Liquid `tex1`, et ajouter la somme de contrôle Bech32m. L'adresse finale est :

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Cela représentait beaucoup de travail — mais l'essentiel en est imposé par Taproot lui-même, pas par Simplicity.

### Expressions de témoin

Un nouveau type de combinateur répond à l'absence d'entrée aux programmes Simplicity : l'expression de témoin. Le combinateur `witness` permet d'intégrer aux programmes des données de signature et d'autres éléments de témoin.

```
      w : B
-----------------
witness w : A ⊢ B
```

La sémantique de l'expression de témoin est directe : elle ignore son entrée et retourne simplement la valeur `w` (qui peut être de tout type Simplicity), c'est-à-dire `⟦witness w⟧(a) = w`. Cela n'ajoute **aucune expressivité nouvelle** — par le théorème de complétude, Simplicity peut déjà construire une telle fonction constante (rappelez-vous la macro `scribe` des chapitres précédents). L'intérêt du combinateur `witness` réside entièrement dans son **CMR** : la valeur `w` est **exclue** du CMR de l'expression, de sorte que l'adresse peut être calculée avant que `w` soit connue, et `w` est fournie au moment du rachat.

Ce choix de conception favorise l'élagage — les branches conditionnelles non exécutées n'ont pas besoin d'être révélées on-chain, y compris leurs expressions de témoin associées. Lorsqu'une branche est élaguée, le vérificateur n'a besoin que du CMR du sous-arbre élagué, pas de son contenu réel.

### Valeurs de témoin

Il peut sembler limitant qu'une expression de témoin ne puisse contenir qu'une *valeur*, et non une expression Simplicity plus générale. Mais les programmes des blockchains fondées sur les UTXO ne s'exécutent qu'une seule fois. Il n'est pas nécessaire de passer une sous-expression entière dans un nœud de témoin : l'utilisateur peut simplement exécuter lui-même cette sous-expression, hors chaîne, et transcrire sa sortie dans la valeur de témoin pour obtenir exactement le même résultat.

(Plus loin dans ce cours, nous rencontrerons le combinateur `disconnect`, qui se comporte un peu comme une expression de témoin mais qui *prend* effectivement une expression Simplicity entière comme argument.)

Une conception alternative consisterait à fournir toutes les données de témoin en argument au programme Simplicity de niveau supérieur. Les expressions de témoin sont préférées pour deux raisons. Premièrement, l'**élagage** : les branches non exécutées des expressions `case` ne sont jamais révélées on-chain, et toute expression de témoin à l'intérieur de ces branches est élaguée avec elles. Deuxièmement, la **localité** : les expressions de témoin permettent de placer chaque valeur de témoin exactement là où elle est utilisée, au lieu de la faire remonter depuis l'entrée de niveau supérieur du programme.

### Inférence de type

Puisque les CMR ne s'engagent pas sur les types, le système de types est reconstruit lors du rachat. L'algorithme d'inférence de type de Simplicity détermine les types minimaux pour chaque sous-expression en fonction de la structure des combinateurs. Plus précisément, l'inférence calcule le type *principal* (le plus général) de chaque sous-expression ; toute variable de type qui reste libre est ensuite instanciée au type unité `𝟙`, ce qui donne un type unique et minimal pour le programme.

### Conclusion

Dans ce chapitre, nous avons établi que les programmes Simplicity sont des expressions de type `𝟙 ⊢ 𝟙`, expliqué comment les racines de Merkle d'engagement sont construites à partir de hachages SHA-256 étiquetés de chaque combinateur, et montré comment les CMR sont transformés en adresses on-chain via le mécanisme Taproot du BIP-0341. Nous avons présenté les expressions de témoin comme le mécanisme permettant de fournir des données de signature et d'autres entrées au moment de la dépense, sans s'engager sur leurs valeurs au moment de la création de l'adresse.

# Section finale

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Avis et évaluations

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Examen final

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusion

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
