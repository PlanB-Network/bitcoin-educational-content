---
name: Apprendre Rust avec Bitcoin
goal: Améliorez vos compétences en matière de développement Rust grâce au codage Bitcoin
objectives: 

  - S'habituer à la langue Rust
  - Comprendre pourquoi utiliser Rust pour développer Bitcoin
  - Obtenir la base du SDK Lightning

---

# Une expédition Rust pour les constructeurs Bitcoin



Dans ce cours pratique, qui a été filmé lors d'un séminaire organisé par Fulgur' Ventures en octobre 2023, vous développerez vos compétences en Rust en construisant de véritables composants et mini-projets axés sur le Bitcoin. Nous aborderons les principes fondamentaux du Rust, les raisons pour lesquelles le Rust est utilisé pour le développement du Bitcoin (sécurité de la mémoire, performance et concurrence sûre), et comment commencer à utiliser le SDK Lightning pour créer des fonctionnalités de paiement.


Au fil des chapitres, vous pratiquerez les principaux modèles Rust (propriété, durée de vie, traits, async), travaillerez avec les primitives Bitcoin (clés, transactions, scripting) et intégrerez progressivement les concepts Lightning (nœuds, canaux, factures).


Aucun développement préalable en Rust ou Bitcoin n'est strictement requis, bien qu'une familiarité avec la programmation de base soit utile. Le cours s'adresse aux débutants, mais il est suffisamment pratique pour les ingénieurs qui passent au Bitcoin.


+++

# Introduction

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Aperçu du cours

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Introduction**


Bienvenue dans ce cours de programmation pour débutants sur les SDK. Dans cette formation, vous apprendrez les bases de Rust, puis vous vous concentrerez sur l'application de Rust à la programmation de Bitcoin, et vous terminerez par quelques cas d'utilisation des SDK.


Les vidéos de la formation ne seront disponibles qu'en anglais pour l'instant et faisaient partie d'un séminaire organisé en octobre dernier en Toscane par Fulgure Venture. Cette formation se concentre uniquement sur la première semaine. La seconde moitié était destinée à RGB et peut être trouvée dans le cours RGB.


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Cette formation vous donne l'opportunité de développer vos compétences en programmation sur le Lightning Network en utilisant le Rust et divers SDK. Elle est conçue pour les développeurs ayant une solide expérience de la programmation et souhaitant se plonger dans le développement spécifique au Lightning Network. Vous apprendrez les bases du Rust, pourquoi il est adapté au développement du Bitcoin, puis vous passerez à la mise en œuvre pratique à l'aide de SDK spécialisés.


**Section 2 : Apprendre à coder avec Rust**

Dans cette section, vous découvrirez les principes fondamentaux du Rust à travers une série de chapitres progressifs. Vous apprendrez à écrire du code Rust, à comprendre ses spécificités et à maîtriser ses fonctionnalités essentielles à travers sept parties détaillées. Ce module est essentiel pour comprendre pourquoi le Rust est un langage privilégié pour le développement du Bitcoin.


**Section 3 : Rust & Bitcoin**

Ici, nous allons explorer en profondeur pourquoi le Rust est un choix pertinent pour le développement du Bitcoin. Vous découvrirez son modèle d'erreur, l'outil UniFFI et les caractéristiques asynchrones - autant d'éléments clés dans la construction de logiciels robustes et sûrs.


**Section 4 : Développement du LNP/BP avec les SDK**

Vous apprendrez à développer des nœuds LN à l'aide de divers SDK comme le SDK Breez et Greenlight pour Lipa. Vous verrez comment mettre en œuvre des applications Lightning Network en utilisant des bibliothèques conçues pour simplifier le développement Bitcoin et Lightning.


Prêt à développer vos compétences en Lightning Network avec Rust ? C'est parti !

# Apprendre à coder avec le rust book

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Introduction à la Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Installation et gestion de Rust avec Rustup


Lorsque vous commencez votre voyage avec Rust, la première étape consiste à mettre en place un environnement de développement approprié. L'approche la plus largement recommandée pour installer Rust est Rustup, un système de gestion de la chaîne d'outils qui gère l'installation et les mises à jour à travers différents projets et plates-formes.


Rustup est plus qu'un simple installateur, c'est un outil de gestion complet pour votre environnement de développement Rust. Avec Rustup, vous pouvez facilement installer des cibles de compilation supplémentaires pour différentes plateformes, telles que ARM64 pour le développement d'Android ou d'autres architectures que vous pourriez avoir besoin de prendre en charge. L'outil gère également les mises à jour de Rust de manière transparente, ce qui est particulièrement utile étant donné que Rust publie une nouvelle version stable toutes les six semaines environ. Lorsque vous devez mettre à jour vers la dernière version, une simple commande `rustup update` gère tout automatiquement.


Lors de l'installation de Rustup, il est utile de comprendre le modèle de sécurité impliqué. Le processus d'installation télécharge et exécute un script depuis le site officiel de Rust via HTTPS, ce qui fournit une sécurité cryptographique au niveau du transport. Les paquets téléchargés par Rustup et Cargo proviennent de sources fiables (crates.io et l'infrastructure officielle de Rust) et bénéficient du chiffrement HTTPS. Bien que cette approche soit sûre pour la plupart des scénarios de développement, certaines organisations ayant des politiques de sécurité strictes peuvent préférer installer Rust via le gestionnaire de paquets de leur distribution Linux, qui fournit une couche de confiance supplémentaire grâce à l'infrastructure de signature des paquets de la distribution. Pour l'apprentissage et le développement général, Rustup est un outil bien établi et largement reconnu dans l'écosystème Rust.


Pour la plupart des scénarios de développement, vous pouvez installer Rustup en exécutant le script d'installation fourni sur le site officiel de Rust. Le programme d'installation vous demandera de choisir entre différentes options de chaîne d'outils, la chaîne d'outils stable étant le choix recommandé pour la plupart des utilisateurs. L'installation se fait dans votre répertoire personnel, sans nécessiter de privilèges d'administrateur, et met en place toutes les variables d'environnement nécessaires pour une utilisation immédiate.


### Comprendre les chaînes d'outils et les composants Rust


L'écosystème de développement de Rust se compose de plusieurs éléments clés qui fonctionnent ensemble pour fournir un environnement de programmation complet. La compréhension de ces composants vous permet de naviguer plus efficacement dans le processus de développement de Rust et de résoudre les problèmes lorsqu'ils surviennent.


Le compilateur Rust, connu sous le nom de `rustc`, forme le coeur de la chaîne d'outils Rust. Bien que vous puissiez théoriquement utiliser `rustc` directement pour compiler les programmes Rust, la plupart des travaux de développement s'appuient sur Cargo, le gestionnaire de paquets et le système de construction de Rust. Cargo fonctionne de manière similaire à npm dans l'écosystème JavaScript, en gérant les dépendances, en coordonnant les builds, et en fournissant des commandes pratiques pour les tâches de développement courantes. Lorsque vous exécutez des commandes comme `cargo build` ou `cargo run`, Cargo orchestre le processus de compilation, s'occupe de la résolution des dépendances et gère la structure globale du projet.


Clippy est un linter qui analyse votre code et vous propose des suggestions d'amélioration. Contrairement aux vérificateurs de syntaxe de base, Clippy comprend les idiomes Rust et peut recommander des façons plus idiomatiques d'accomplir des tâches spécifiques. Cet outil permet d'apprendre les meilleures pratiques Rust et d'écrire un code plus facile à maintenir.


La chaîne d'outils Rust comprend également des outils de documentation complets et la documentation de la bibliothèque standard, accessible via le site web officiel de documentation Rust. Cette documentation sert de référence indispensable pendant le développement, en fournissant des informations détaillées sur les fonctions, les types et les modules de la bibliothèque standard. La documentation comprend des exemples et des explications détaillés qui vous aident à comprendre non seulement ce que font les fonctions, mais aussi comment les utiliser efficacement dans vos programmes.


Rust supporte plusieurs canaux de publication : stable, beta et nightly. Le canal stable fournit des versions testées de manière approfondie et adaptées à une utilisation en production. Le canal beta offre un aperçu de la prochaine version stable, principalement utilisé pour les tests finaux avant la sortie officielle. Le canal nightly comprend des fonctionnalités expérimentales en cours de développement, qui peuvent être utiles pour essayer de nouvelles fonctionnalités de Rust, bien que ces fonctionnalités puissent changer ou être supprimées dans les versions futures.


### Création et gestion de projets Rust avec Cargo


Le développement moderne de Rust est centré sur Cargo, qui rationalise la création de projets, la gestion des dépendances et le processus de construction. Plutôt que de créer manuellement des répertoires et des fichiers, Cargo fournit la commande `cargo new` pour generate créer une structure de projet complète avec des valeurs par défaut raisonnables.


Lorsque vous créez un nouveau projet avec `cargo new project_name`, Cargo établit une structure de répertoire standard, crée un fichier `main.rs` de base avec un programme "Hello, world !", initialise un dépôt Git, et génère un fichier `Cargo.toml` pour la configuration du projet. Le fichier `Cargo.toml` sert de point central de configuration pour votre projet, contenant des métadonnées sur votre projet et listant toutes les dépendances dont votre code a besoin.


Cargo fournit plusieurs commandes essentielles pour le travail de développement quotidien. La commande `cargo build` compile votre projet et ses dépendances, créant des fichiers exécutables dans le répertoire `target`. Pour une itération rapide pendant le développement, `cargo run` combine la compilation et l'exécution en une seule étape. La commande `cargo check` effectue toutes les vérifications de compilation sans générer l'exécutable final, ce qui la rend significativement plus rapide qu'une compilation complète lorsque vous voulez simplement vérifier que votre code se compile correctement.


Lors de la préparation du code pour le déploiement en production, le drapeau `--release` active les optimisations et supprime les assertions de débogage. Les versions release s'exécutent plus rapidement et produisent des exécutables plus petits, mais elles prennent plus de temps à compiler et suppriment des informations de débogage utiles. Le compilateur applique diverses optimisations pendant les versions release et désactive les contrôles d'exécution tels que la détection de débordement d'entier, ce qui améliore les performances mais supprime certaines garanties de sécurité présentes dans les versions debug.


### Variables, mutabilité et philosophie de sécurité de Rust


Rust adopte une approche de la gestion des variables différente de celle de la plupart des langages. Par défaut, toutes les variables de Rust sont immuables, ce qui signifie que leur valeur ne peut pas être modifiée après leur affectation initiale. Cette décision de conception vise à prévenir les erreurs de programmation courantes qui surviennent à la suite de changements d'état inattendus.


Lorsque vous déclarez une variable en utilisant `let x = 5`, cette variable devient immuable par défaut. Toute tentative de modification ultérieure de sa valeur entraînera une erreur de compilation. Cette exigence d'immuabilité oblige les développeurs à réfléchir soigneusement au moment où les changements d'état sont vraiment nécessaires et rend le comportement du code plus prévisible. De nombreux bogues de programmation proviennent de variables qui changent de manière inattendue, et l'immutabilité par défaut de Rust aide à prévenir ces problèmes.


Lorsque vous avez réellement besoin de modifier la valeur d'une variable, Rust exige une déclaration explicite de mutabilité en utilisant le mot-clé `mut` : `let mut x = 5`. Cette déclaration explicite indique clairement au compilateur et aux autres développeurs que la valeur de cette variable peut changer pendant l'exécution du programme. L'obligation de déclarer explicitement la mutabilité encourage à se demander si la mutabilité est vraiment nécessaire pour chaque variable.


Rust prend également en charge le shadowing, qui permet de déclarer une nouvelle variable portant le même nom qu'une variable précédente. Contrairement à la mutation, le shadowing crée une variable entièrement nouvelle qui porte le même nom, cachant ainsi la variable précédente. Cette technique s'avère particulièrement utile lors de la transformation de données en plusieurs étapes, comme l'analyse d'une chaîne de caractères en un nombre, puis le traitement ultérieur de ce nombre. Grâce au shadowing, vous pouvez conserver un nom de variable cohérent tout au long du processus de transformation, tout en modifiant le type de la variable à chaque étape.


La distinction entre le shadowing et la mutation devient importante lorsque l'on considère les changements de type. Avec le shadowing, vous pouvez changer à la fois la valeur et le type d'une variable parce que vous créez une nouvelle variable. Avec la mutation, vous ne pouvez changer que la valeur tout en conservant le même type, puisque vous modifiez une variable existante au lieu d'en créer une nouvelle.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Types de données et principes de base des systèmes de types


Rust met en œuvre un système de types statique et fort où chaque valeur doit avoir un type bien défini connu au moment de la compilation. Bien que cela puisse sembler restrictif par rapport aux langages à typage dynamique, les capacités d'inférence de type de Rust signifient qu'il est rarement nécessaire de spécifier les types de manière explicite. Le compilateur peut généralement déterminer le type approprié en fonction de l'utilisation que vous faites de la valeur.


Cependant, certaines situations nécessitent des annotations de type explicites. Lorsque vous utilisez des fonctions génériques comme `parse()`, qui peuvent convertir des chaînes de caractères en différents types numériques, le compilateur a besoin de savoir quel type spécifique vous voulez. Dans ce cas, vous devez fournir des annotations de type en utilisant la syntaxe des deux points : ``Pensons que : u32 = "42".parse().expect("Pas un nombre !")`.


Les types scalaires de Rust comprennent les entiers, les nombres à virgule flottante, les booléens et les caractères. Le système de types entiers permet un contrôle précis de l'utilisation de la mémoire et des caractéristiques de performance. Les types entiers sont nommés systématiquement : `i8`, `i16`, `i32`, `i64`, et `i128` pour les entiers signés, et `u8`, `u16`, `u32`, `u64`, et `u128` pour les entiers non signés. Les nombres indiquent la largeur des bits, ce qui rend l'utilisation de la mémoire et les plages de valeurs immédiatement claires.


Les types `isize` et `usize` méritent une attention particulière car ils s'adaptent à votre architecture cible. Sur les systèmes 64 bits, ces types ont une largeur de 64 bits, alors que sur les systèmes 32 bits, ils ont une largeur de 32 bits. Ces types sont couramment utilisés pour l'indexation des tableaux et les décalages de mémoire, car ils correspondent à la taille naturelle des mots de l'architecture cible, ce qui permet une arithmétique de pointeur et des opérations de mémoire efficaces.


Rust fournit plusieurs façons d'écrire les littéraux entiers, y compris les formats décimal, hexadécimal (`0x`), octal (`0o`), et binaire (`0b`). Vous pouvez également utiliser des traits de soulignement n'importe où dans les littéraux numériques pour améliorer la lisibilité, comme écrire `1_000_000` au lieu de `1000000`. Les traits de soulignement n'ont aucun effet sur la valeur, mais ils peuvent rendre les grands nombres plus lisibles.


Les types de nombres à virgule flottante dans Rust sont simples : `f32` pour les nombres à virgule flottante en simple précision et `f64` pour les nombres à virgule flottante en double précision. Le type `f64` est généralement préféré en raison de sa plus grande précision et du fait que les processeurs modernes peuvent souvent traiter les opérations en virgule flottante sur 64 bits aussi efficacement que les opérations sur 32 bits.


### Types composés et organisation des données


Outre les types scalaires, Rust propose des types composés qui regroupent plusieurs valeurs. Les tuples vous permettent de combiner des valeurs de différents types en une seule valeur composée. Vous créez des tuples en utilisant des parenthèses et vous pouvez spécifier le type de chaque élément : `let tup : (i32, f64, u8) = (500, 6.4, 1)`.


Les tuples supportent la déstructuration, qui vous permet d'extraire des valeurs individuelles : `let (x, y, z) = tup`. Cette syntaxe crée trois variables distinctes à partir des composants du tuple. Alternativement, vous pouvez accéder aux éléments du tuple directement en utilisant la notation par points avec l'index de l'élément : `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Les tableaux en Rust diffèrent considérablement des tableaux ou des listes dans de nombreux autres langages car ils ont une taille fixe qui fait partie de leur type. Un tableau de cinq entiers a le type `[i32 ; 5]`, où le point-virgule sépare le type d'élément de la longueur du tableau. Ces informations sur la taille au niveau du type permettent au compilateur d'effectuer un contrôle des limites et garantissent que les fonctions recevant des tableaux savent exactement à combien d'éléments elles doivent s'attendre.


Vous pouvez initialiser les tableaux en listant explicitement tous les éléments : `[1, 2, 3, 4, 5]`, ou en utilisant une syntaxe abrégée pour les tableaux avec des valeurs répétées : `[3 ; 5]` crée un tableau de cinq éléments, tous avec la valeur 3. Cette syntaxe abrégée est utile pour initialiser les tampons ou créer des tableaux avec des valeurs par défaut.


L'accès aux tableaux utilise la notation entre crochets comme la plupart des langages, mais Rust fournit une vérification des limites à la fois à la compilation et à l'exécution. Lorsque vous accédez à un tableau avec un index constant que le compilateur peut vérifier, il détectera les accès hors limites au moment de la compilation. Pour les indices dynamiques déterminés à l'exécution, Rust insère des contrôles de limites qui feront paniquer le programme si vous tentez d'accéder à un indice invalide, évitant ainsi les violations de la sécurité de la mémoire.



## Ownership et sécurité de la mémoire dans Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Comprendre l'approche unique de Rust en matière de gestion de la mémoire


Ce chapitre couvre l'un des concepts les plus importants de Rust. Alors que les concepts précédents ont pu sembler familiers aux programmeurs venant d'autres langages, la propriété est l'approche de Rust pour résoudre le problème de la sécurité de la mémoire sans le ramassage des ordures.


Le Rust a été conçu dans le but fondamental de prévenir les bogues liés à la mémoire qui affectent les langages de bas niveau comme le C et le C++. Ces problèmes comprennent les bogues de type "use-after-free", où l'on accède à la mémoire après qu'elle a été libérée, et les débordements de mémoire tampon, où les programmes écrivent en dehors des limites de la mémoire allouée. Les solutions traditionnelles à ces problèmes ont impliqué des compromis que le Rust cherche à éliminer. Les langages de haut niveau comme Java et Go résolvent le problème de la sécurité de la mémoire grâce au ramasse-miettes, un processus automatique identifiant et libérant périodiquement la mémoire inutilisée. Cependant, les garbage collectors introduisent une surcharge de performance et peuvent provoquer des pauses imprévisibles pendant l'exécution du programme, ce qui les rend inadaptés à la programmation de systèmes où la constance de la performance est cruciale.


Le Rust assure la sécurité de la mémoire principalement grâce à l'analyse statique effectuée au moment de la compilation. Le compilateur examine le code source et peut déterminer si la plupart des opérations de mémoire sont sûres sans nécessiter le ramassage des ordures. Pour les cas qui ne peuvent pas être vérifiés statiquement, comme l'accès à un tableau avec des indices calculés au moment de l'exécution, Rust insère des vérifications de limites qui provoquent une panique plutôt que d'autoriser un comportement indéfini. Cette approche diffère fondamentalement des analyseurs statiques disponibles pour C et C++, qui ont été adaptés à des langages qui n'avaient pas été conçus à l'origine pour une analyse statique complète. La syntaxe et les règles de langage de Rust ont été conçues dès le départ pour permettre une vérification approfondie au moment de la compilation, ce qui garantit qu'une fois qu'un programme a été compilé avec succès, il s'exécutera en toute sécurité ou paniquera de manière prévisible au lieu de présenter un comportement indéfini.


### Le système Ownership : Règles et principes


La pierre angulaire des garanties de sécurité de la mémoire de Rust est le système de propriété, qui régit la gestion de la mémoire tout au long de l'exécution d'un programme. Le Ownership fonctionne sur la base de trois règles fondamentales que le compilateur applique à tout moment :


1. Chaque valeur dans Rust a un propriétaire (une variable qui contient la valeur)

2. Il ne peut y avoir qu'un seul propriétaire à la fois

3. Lorsque le propriétaire sort du champ d'application, la valeur est abandonnée


Dans Rust, les portées sont généralement définies par des accolades, que ce soit dans des corps de fonction, des blocs conditionnels ou des blocs de portée créés explicitement. Lorsqu'une variable est déclarée dans une portée, cette portée devient propriétaire de la valeur de la variable. La variable reste accessible et valide pendant toute la durée de vie de la portée, mais dès que l'exécution quitte la portée, toutes les variables possédées sont automatiquement nettoyées par un processus appelé dropping.


Ce nettoyage automatique est mis en œuvre par le mécanisme d'abandon de Rust, où le langage appelle implicitement une fonction d'abandon sur les variables qui sortent du champ d'application. Pour les types de base, cela signifie simplement que la mémoire est marquée comme disponible pour la réutilisation. Pour les types plus complexes qui gèrent des ressources, les implémentations drop personnalisées peuvent effectuer des opérations de nettoyage supplémentaires, telles que la fermeture des handles de fichiers ou la libération des connexions réseau. Ce modèle, emprunté au RAII (Resource Acquisition Is Initialization) de C++, garantit que les ressources sont toujours correctement libérées sans que le programmeur n'ait besoin d'un code de nettoyage explicite.


### Déplacement du Ownership et disposition de la mémoire


Pour comprendre comment la propriété est transférée entre les variables, il faut examiner la différence entre les types simples et les types complexes en termes de disposition de la mémoire et de comportement de copie. Les types simples comme les entiers, les booléens et les nombres à virgule flottante ont une taille fixe et connue au moment de la compilation et peuvent être copiés efficacement. Lorsque vous affectez une variable entière à une autre, Rust crée une copie complète et indépendante de la valeur, ce qui permet aux deux variables d'exister simultanément sans aucun problème de propriété.


Les types complexes tels que les chaînes de caractères présentent un défi différent car ils gèrent une mémoire allouée dynamiquement. Une chaîne de caractères dans Rust se compose de trois éléments stockés sur la pile : un pointeur sur les données de caractères allouées au tas, la longueur actuelle de la chaîne et la capacité totale de la mémoire tampon allouée. Cette structure permet aux chaînes de croître et de décroître efficacement tout en conservant la connaissance de leurs limites. Lorsque vous assignez une variable String à une autre, Rust est confronté à un choix : il peut copier uniquement la structure basée sur la pile (en créant deux pointeurs vers les mêmes données du tas) ou effectuer une copie profonde de toutes les données du tas.


Le comportement par défaut de Rust est de déplacer la propriété plutôt que de copier, en transférant les données du tas de la variable source à la variable de destination et en invalidant la source. Cette approche permet d'éviter le scénario dangereux selon lequel plusieurs variables pourraient modifier la même mémoire du tas ou la même mémoire pourrait être libérée plusieurs fois lorsque les variables sortent du champ d'application. L'opération de déplacement est efficace car elle ne copie que la petite structure basée sur la pile, et non les données potentiellement volumineuses du tas, tout en maintenant la sécurité de la mémoire en garantissant une propriété unique.


### Références et emprunts


Bien que les déplacements de propriété offrent une certaine sécurité, ils peuvent être restrictifs lorsque vous avez besoin d'utiliser une valeur à plusieurs endroits sans en transférer la propriété. Rust résout ce problème grâce à l'emprunt, qui permet aux fonctions et aux variables d'accéder temporairement aux données sans en prendre la propriété. Une référence, créée à l'aide de l'opérateur esperluette, permet d'accéder en lecture seule à une valeur tout en laissant la propriété à la variable d'origine.


Les références permettent aux fonctions d'opérer sur les données sans les consommer, ce qui permet d'utiliser la même valeur plusieurs fois dans un programme. Lorsque vous passez une référence à une fonction, vous prêtez temporairement les données, et la fonction doit renvoyer la référence avant que le propriétaire initial ne puisse reprendre le contrôle total. Cette métaphore de l'emprunt reflète la nature temporaire de l'accès : tout comme vous pouvez prêter un livre à un ami tout en en conservant la propriété, les références permettent un accès temporaire tout en préservant la relation de propriété initiale.


Les références mutables étendent ce concept pour permettre la modification de données empruntées, mais avec des restrictions strictes pour maintenir la sécurité. La Rust n'autorise qu'une seule référence mutable à un élément de données à un moment donné, ce qui permet d'éviter les courses aux données lorsque plusieurs parties d'un programme peuvent modifier simultanément la même mémoire. En outre, il n'est pas possible d'avoir simultanément des références mutables et immuables aux mêmes données, car cela pourrait conduire à des situations où le code suppose que les données sont stables alors que d'autres codes les modifient activement. Ces règles sont appliquées au moment de la compilation, ce qui permet d'éliminer des classes entières de bogues de concurrence qui affectent d'autres langages de programmation de systèmes.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Types de chaînes et tranches


Le Rust fait la distinction entre les chaînes littérales et le type Chaîne, ce qui reflète des stratégies de gestion de la mémoire et des cas d'utilisation différents. Les littéraux de chaîne sont intégrés directement dans le binaire compilé et ont le type &str (string slice), représentant une vue sur des données de chaîne immuables. Ces littéraux sont efficaces parce qu'ils ne nécessitent pas d'allocation au moment de l'exécution, mais ils ne peuvent pas être modifiés puisqu'ils font partie du code du programme.


Le type Chaîne, en revanche, gère la mémoire allouée dynamiquement et peut croître, décroître et être modifié au moment de l'exécution. Vous pouvez créer une chaîne à partir d'un littéral en utilisant String::from() ou des méthodes similaires, qui allouent la mémoire du tas et copient le contenu du littéral. Cette distinction permet à Rust d'optimiser les performances (en utilisant des littéraux lorsque c'est possible) et la flexibilité (en utilisant des chaînes de caractères lorsque des modifications sont nécessaires).


Les tranches de chaînes (&str) constituent une abstraction puissante permettant de travailler avec des portions de chaînes sans copier les données. Une tranche contient un pointeur sur le début des données de la chaîne et une longueur, ce qui permet de référencer efficacement les sous-chaînes. La syntaxe des tranches utilise des plages (par exemple, &s[0..5]) pour spécifier la partie de la chaîne à référencer. Les tranches étant des références, elles sont soumises à des règles d'emprunt qui empêchent la modification de la chaîne sous-jacente tant que les tranches existent. Cette application au moment de la compilation permet d'éviter des bogues courants tels que l'accès à une mémoire invalide après que la chaîne de caractères originale a été libérée ou modifiée.


### Tableaux, vecteurs et tranches génériques


Le concept de tranche s'étend au-delà des chaînes de caractères à toute séquence d'éléments, fournissant un moyen unifié de travailler avec des tableaux de taille fixe et des vecteurs dynamiques. Les tableaux de Rust ont leur longueur encodée dans leur type (par exemple, [i32 ; 5] pour un tableau de cinq entiers de 32 bits), ce qui les rend appropriés pour les situations nécessitant des garanties de taille à la compilation. Les fonctions qui acceptent les tableaux peuvent imposer des exigences de longueur exacte, ce qui est utile pour des opérations telles que les fonctions cryptographiques qui nécessitent des entrées de taille précise.


Les tranches (&[T]) constituent une alternative plus souple, représentant une vue de toute séquence contiguë d'éléments, quel que soit le stockage sous-jacent. Vous pouvez créer des tranches à partir de tableaux, de vecteurs ou d'autres tranches, et la même tranche peut référencer différentes portions de données tout au long de sa durée de vie. Cette flexibilité rend les tranches idéales pour les fonctions qui doivent traiter des séquences sans se soucier du mécanisme de stockage spécifique ou de la taille exacte.


La relation entre les types possédés (String, Vec<T>) et leurs équivalents en tranches empruntés (&str, &[T]) suit un modèle cohérent dans l'ensemble de la Rust. Les types propres gèrent leur mémoire et peuvent être modifiés, tandis que les tranches fournissent un accès efficace, en lecture seule, à des parties de ces données. Cette conception permet d'obtenir des API à la fois flexibles (en acceptant différents types d'entrée par le biais des tranches) et efficaces (en évitant les copies inutiles), tout en maintenant les garanties de sécurité de Rust grâce au système d'emprunt.



## Structures, construction de types de données complexes

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Les structures de Rust servent de base à la création de types de données complexes, similaires aux classes d'autres langages de programmation. Elles vous permettent de regrouper des données connexes en une seule unité cohérente qui peut contenir plusieurs champs de types différents. La syntaxe de définition d'une structure suit un modèle simple : vous utilisez le mot-clé `struct` suivi du nom de la structure, puis vous définissez les champs entre accolades en utilisant la syntaxe des deux points pour spécifier le type de chaque champ.


Rust suit des conventions de nommage spécifiques pour les structures que le compilateur appliquera par le biais d'avertissements. Les noms de structures doivent utiliser la CamelCase (également connue sous le nom de PascalCase), tandis que les noms de champs à l'intérieur de la structure doivent utiliser la snake_case avec des underscores. Cette convention permet de maintenir la cohérence entre les bases de code Rust et rend le code plus lisible pour les autres développeurs.


Pour créer des instances de structures, vous devez spécifier les valeurs de tous les champs en utilisant le nom de la structure suivi d'accolades contenant les affectations des champs. Une fois que vous avez une instance de structure, vous pouvez accéder et modifier les champs individuels en utilisant la notation par points, à condition que l'instance soit déclarée comme mutable. Cette notation par points fonctionne de manière cohérente dans Rust, contrairement à des langages comme le C++ où vous pouvez utiliser des opérateurs différents pour les pointeurs et les objets directs.


### Fonctions des constructeurs et raccourcis des champs


Rust n'a pas de constructeurs intégrés comme certains langages orientés objet, mais vous pouvez créer des fonctions qui renvoient des instances de structure dans le même but. Ces fonctions de construction prennent généralement des paramètres pour certains ou tous les champs et peuvent définir des valeurs par défaut pour d'autres. Lors de l'écriture de telles fonctions, Rust fournit un raccourci pratique : si un paramètre a le même nom qu'un champ de structure, vous pouvez simplement écrire le nom du champ une seule fois au lieu de le répéter dans le format `champ : valeur`.


Les instances de structure peuvent également être créées en copiant les valeurs d'instances existantes à l'aide de la syntaxe struct update. Cette fonctionnalité vous permet de créer une nouvelle instance en spécifiant uniquement les champs que vous souhaitez modifier, tous les autres champs étant copiés à partir d'une instance existante. Cependant, cette opération suit les règles de propriété de Rust, ce qui signifie que les types non copiés seront déplacés de l'instance source, rendant potentiellement des parties de l'instance originale inutilisables par la suite. Le compilateur suit intelligemment ces déplacements partiels, vous permettant de continuer à utiliser les champs qui n'ont pas été déplacés tout en empêchant l'accès aux champs déplacés.


### Structures de n-uplets et structures d'unités


Rust prend en charge les structures tuple, qui sont des structures dont les champs non nommés sont accessibles par index plutôt que par nom. Ces structures sont utiles pour les types enveloppants simples ou lorsque vous avez besoin d'une structure mais pas de champs nommés. Vous accédez aux champs des structures tuple en utilisant la notation point suivie de l'index du champ, comme `.0` pour le premier champ, `.1` pour le second, et ainsi de suite. Cette approche fonctionne bien pour les structures qui contiennent une seule valeur ou seulement quelques valeurs étroitement liées où les noms peuvent être redondants.


Les structures unitaires représentent la forme la plus simple de structures - elles ne contiennent aucune donnée. Bien que cela puisse sembler inutile au départ, les structures unitaires deviennent précieuses lorsque l'on travaille avec le système de traits de Rust, car elles peuvent mettre en œuvre des comportements sans stocker de données. Ces structures vides servent de marqueurs ou d'espaces réservés dans les modèles Rust plus avancés.


### Méthodes et fonctions associées


Les structures acquièrent des fonctionnalités supplémentaires lorsque vous ajoutez des comportements par le biais de blocs d'implémentation. En utilisant le mot-clé `impl` suivi du nom de la structure, vous pouvez définir des méthodes qui opèrent sur les instances de votre structure. Les méthodes sont des fonctions qui prennent `self` comme premier paramètre, qui peut être une valeur propre (`self`), une référence immuable (`&self`), ou une référence mutable (`&mut self`), en fonction de ce que la méthode doit faire avec l'instance.


Le choix du type de paramètre `self` détermine le comportement de la méthode en ce qui concerne la propriété. Les méthodes prenant `&self` peuvent lire l'instance sans en prendre la propriété, ce qui les rend adaptées aux opérations qui ne modifient pas la structure. Les méthodes prenant `&mut self` peuvent modifier l'instance tout en permettant à l'appelant de conserver la propriété. Les méthodes prenant `self` comme valeur consomment l'instance, ce qui est approprié pour les opérations qui transforment la structure en quelque chose d'autre ou lorsque la méthode représente l'opération finale sur cette instance.


Les fonctions associées sont des fonctions définies dans un bloc d'implémentation qui ne prennent pas `self` comme paramètre. Elles sont similaires aux méthodes statiques dans d'autres langages et sont généralement utilisées comme constructeurs ou fonctions utilitaires liées au type. Vous appelez les fonctions associées en utilisant la syntaxe des deux points (`Type::nom_de_la_fonction()`), ce qui les distingue clairement des méthodes appelées sur les instances.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Énumérations : Modélisation des choix et des variantes


Les énumérations de Rust ont plus de possibilités que les énumérations de nombreux autres langages. Alors qu'elles peuvent représenter de simples ensembles de constantes nommées, les énumérations de Rust peuvent également contenir des données dans chaque variante, ce qui les rend adaptées à la modélisation de situations dans lesquelles une valeur peut être l'un de plusieurs types ou états différents. Chaque variante d'enum peut contenir différents types et quantités de données, de l'absence totale de données à des structures complexes avec des champs nommés.


La possibilité d'attacher des données aux variantes des enums permet d'éliminer de nombreuses erreurs de programmation courantes dans d'autres langages. Au lieu de maintenir des variables distinctes pour un indicateur de type et les données associées - ce qui peut facilement devenir incohérent - les enums Rust regroupent les informations sur le type avec les données elles-mêmes. Cette conception garantit que les données correspondent toujours à la variante, ce qui permet d'éviter les incohérences susceptibles d'entraîner des erreurs d'exécution.


Les variantes d'énumération peuvent contenir des données sous plusieurs formes : aucune donnée pour les indicateurs simples, des données de type tuple pour les champs non nommés ou des données de type struct avec des champs nommés. Vous pouvez même mélanger ces styles au sein d'une même énumération, en choisissant la forme la plus appropriée pour chaque variante. Grâce à cette flexibilité, les enums conviennent à la modélisation de concepts de domaines complexes dans lesquels différents cas requièrent des informations différentes.


#### Le type d'option : Gérer les absences en toute sécurité


L'un des enums les plus importants de Rust est `Option<T>`, qui représente des valeurs qui peuvent être présentes ou non. Cet enum a deux variantes : `Some(T)` contenant une valeur de type T, et `None` représentant l'absence de valeur. Le type Option est la solution de Rust aux problèmes de pointeurs nuls qui affectent de nombreux autres langages, obligeant les développeurs à gérer explicitement les cas où des valeurs peuvent être manquantes.


L'utilisation des types Option rend votre code plus robuste car le compilateur vous demande de gérer à la fois la présence et l'absence de valeurs. Vous ne pouvez pas utiliser accidentellement une valeur potentiellement manquante sans vérifier au préalable si elle existe. Cette gestion explicite permet d'éviter les exceptions de pointeur nul et les erreurs d'exécution similaires qui sont des sources courantes de bogues dans d'autres langages de programmation.


Le type Option s'intègre au système de filtrage de Rust, vous permettant de gérer les deux cas. Des méthodes comme `unwrap_or()` fournissent des moyens pratiques d'extraire des valeurs avec des valeurs par défaut, tandis que des méthodes comme `map()` et `and_then()` permettent d'utiliser des modèles de programmation fonctionnelle pour travailler avec des valeurs optionnelles.


### Correspondance de motifs avec des expressions de correspondance


La recherche de motifs à l'aide d'expressions "match" permet de travailler avec des enums et d'autres types de données. Une expression de correspondance examine une valeur et exécute un code différent en fonction du motif auquel la valeur correspond. Chaque motif peut déstructurer la valeur correspondante, en liant des parties de celle-ci à des variables qui peuvent être utilisées dans le bloc de code correspondant.


Les expressions de correspondance doivent être exhaustives, c'est-à-dire qu'elles doivent traiter tous les cas possibles pour le type faisant l'objet de la correspondance. Cette exigence permet d'éviter les bogues qui pourraient survenir si certains cas n'étaient accidentellement pas traités. Si vous ne souhaitez pas traiter tous les cas de manière explicite, vous pouvez utiliser le caractère générique (`_`) pour traiter tous les cas restants, ou lier les cas non traités à une variable si vous avez besoin d'accéder à la valeur.


La construction `if let` fournit une alternative plus concise à match lorsque vous ne vous intéressez qu'à un motif spécifique. Cette syntaxe est particulièrement utile lorsque l'on travaille avec des types Option ou lorsque l'on veut exécuter du code uniquement si une valeur correspond à une variante particulière de l'enum. La construction `if let` peut inclure une clause `else` pour les cas où le motif ne correspond pas, ce qui en fait une manière simplifiée de gérer des scénarios simples de correspondance de motifs.


#### Collections : Gérer des groupes de données


La bibliothèque standard de Rust fournit plusieurs types de collections pour gérer des groupes de données connexes. Ces collections sont génériques, ce qui signifie qu'elles peuvent stocker des éléments de n'importe quel type et qu'elles gèrent automatiquement la mémoire. Les collections les plus couramment utilisées sont les vecteurs pour les listes ordonnées, les cartes de hachage pour les associations clé-valeur et les chaînes pour les données textuelles.


#### Vecteurs : Matrices dynamiques


Les vecteurs représentent des tableaux évolutifs dont la taille peut changer au cours de l'exécution du programme. Contrairement aux tableaux de taille fixe, les vecteurs allouent de la mémoire sur le tas et peuvent s'étendre ou se réduire en fonction des besoins. La création d'un vecteur nécessite souvent une annotation de type explicite lorsque l'on commence avec un vecteur vide, car le compilateur doit savoir quel type d'éléments le vecteur contiendra.


Les vecteurs offrent plusieurs façons d'accéder aux éléments, chacune avec des caractéristiques de sécurité différentes. La notation de l'index (`vec[0]`) fournit un accès direct mais déclenche une panique si l'index est hors limites. La méthode `get()` renvoie une `Option`, vous permettant de gérer gracieusement les accès hors limites. Le choix entre ces deux approches dépend de votre capacité à garantir la validité de l'index ou de votre besoin de gérer des échecs potentiels.


Les règles d'emprunt de Rust s'appliquent aux vecteurs, ce qui permet d'éviter les problèmes courants de sécurité de la mémoire. Si vous détenez une référence à un élément de vecteur, vous ne pouvez pas modifier le vecteur tant que cette référence n'est pas sortie du champ d'application. Cela permet d'éviter les situations où les références peuvent pointer vers de la mémoire désallouée après des opérations vectorielles telles que l'ajout de nouveaux éléments ou l'effacement du vecteur.


#### Cartes Hash : Stockage clé-valeur


Les cartes Hash offrent un stockage clé-valeur efficace qui permet de rechercher rapidement des valeurs en fonction des clés qui leur sont associées. Les clés et les valeurs peuvent être de n'importe quel type, mais les clés doivent implémenter les traits nécessaires au hachage et à la comparaison d'égalité. Les cartes Hash sont propriétaires des valeurs insérées, à moins que celles-ci n'implémentent l'attribut Copy.


Les cartes Hash offrent plusieurs méthodes pour insérer et mettre à jour des valeurs. La méthode de base `insert()` écrase les valeurs existantes, tandis que `entry()` fournit une logique d'insertion plus flexible. L'entrée API vous permet d'insérer des valeurs uniquement si elles n'existent pas déjà, ou de mettre à jour des valeurs existantes en fonction de leur état actuel. Cette API est utile pour les modèles tels que le comptage des occurrences ou le maintien des totaux en cours.


Lors de la récupération de valeurs dans les cartes de hachage, la méthode `get()` renvoie une `Option` puisque la clé demandée peut ne pas exister. Vous pouvez utiliser des méthodes comme `copied()` pour convertir `Option<&T>` en `Option<T>` pour les types Copy, et `unwrap_or()` pour fournir des valeurs par défaut lorsque des clés sont manquantes.


### Traitement des chaînes de caractères et Unicode


Les chaînes de Rust sont encodées en UTF-8, ce qui permet un support complet de l'Unicode mais introduit une certaine complexité par rapport aux chaînes simples de ASCII. Le type `String` représente des données textuelles propres et évolutives, tandis que les tranches de chaînes (`&str`) fournissent des vues empruntées dans les données de chaînes. Vous pouvez convertir ces types selon vos besoins, les tranches de chaînes étant souvent utilisées pour les paramètres de fonction afin d'accepter à la fois les chaînes possédées et les chaînes littérales.


La manipulation des chaînes de caractères comprend des méthodes permettant d'ajouter du texte, de formater plusieurs valeurs ensemble et d'extraire des sous-chaînes. La méthode `push_str()` ajoute des tranches de chaînes sans en prendre possession, tandis que la macro `format!` fournit un moyen flexible de construire des chaînes à partir de plusieurs composants. Lorsque vous travaillez avec des indices de chaînes, vous devez veiller à respecter les limites des caractères UTF-8 afin d'éviter les paniques à l'exécution.


Pour un traitement sûr caractère par caractère, les chaînes fournissent des méthodes d'itérateur comme `chars()` pour les valeurs scalaires Unicode et `bytes()` pour l'accès aux octets bruts. Ces itérateurs gèrent correctement l'encodage UTF-8, en s'assurant que vous ne divisez pas accidentellement des caractères multi-octets. Cette approche est plus sûre et plus fiable que l'indexation manuelle, en particulier lorsque vous travaillez avec du texte international qui peut contenir des caractères Unicode complexes.



## Le système de traitement des erreurs à deux catégories de Rust

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust adopte une approche fondamentalement différente de la plupart des langages de programmation en ce qui concerne la gestion des erreurs. Alors que de nombreux langages s'appuient principalement sur des exceptions, Rust distingue deux catégories distinctes d'erreurs et fournit des mécanismes spécifiques pour gérer chaque type d'erreur. Ce chapitre explore le système complet de gestion des erreurs de Rust, couvrant à la fois les erreurs irrécupérables qui mettent fin à l'exécution du programme et les erreurs récupérables qui permettent aux programmes de continuer à fonctionner de manière gracieuse.


### Erreurs irrécupérables et panique


Les erreurs irrécupérables représentent des situations dans lesquelles le programme est entré dans un état incohérent ou inattendu dont il ne peut pas sortir en toute sécurité. Il s'agit notamment de scénarios tels que l'accès à un tableau hors limites, la tentative d'opérations qui violent la sécurité de la mémoire ou la rencontre de conditions qui indiquent des erreurs fondamentales dans la logique du programme. Lorsque de telles erreurs se produisent, la réponse appropriée est de terminer le programme immédiatement plutôt que de risquer une corruption supplémentaire ou un comportement indéfini.


Dans Rust, les erreurs irrécupérables déclenchent une panique, qui provoque le plantage du programme de manière contrôlée. Avant de se terminer, Rust exécute un processus appelé déroulement, au cours duquel il remonte la pile d'appels pour fournir une trace détaillée de la pile indiquant exactement où la panique s'est produite. Ce processus de déroulement aide les développeurs à identifier la source du problème lors du débogage. Pour les applications critiques en termes de performances ou les systèmes embarqués, vous pouvez désactiver le déroulement et configurer Rust pour qu'il abandonne immédiatement lorsqu'une panique se produit, bien que cela sacrifie les informations de débogage au profit d'un arrêt plus rapide.


Vous pouvez déclencher une panique explicitement en utilisant la macro `panic!` avec un message personnalisé. Lorsqu'une panique se produit, vous verrez une sortie indiquant quel thread a paniqué et le message associé. La définition de la variable d'environnement `RUST_BACKTRACE` fournit des informations de débogage supplémentaires, en montrant la pile d'appels complète qui a conduit à la panique. Par exemple, une tentative d'accès à l'élément 99 d'un vecteur contenant seulement trois éléments provoquera une panique avec un message "index out of bounds" (index hors limites), ainsi qu'un backtrace montrant la séquence exacte des appels de fonction qui ont conduit à l'erreur.


### Erreurs récupérables avec résultat


Les erreurs récupérables représentent des conditions d'échec attendues que les programmes peuvent traiter avec élégance sans se terminer. Les exemples incluent la tentative d'ouverture d'un fichier qui n'existe pas, les échecs de connexion au réseau, ou une entrée utilisateur invalide. Pour ces situations, Rust fournit l'enum `Result`, qui représente explicitement les opérations susceptibles d'échouer et oblige les développeurs à gérer à la fois les cas de réussite et d'échec.


L'enum `Result` est défini avec deux variantes : `Ok(T)` pour les opérations réussies contenant une valeur de type `T`, et `Err(E)` pour les échecs contenant une erreur de type `E`. Cette conception utilise le système de type de Rust pour s'assurer que les échecs potentiels ne peuvent pas être ignorés. Les fonctions susceptibles d'échouer renvoient un `Result`, et le code appelant doit explicitement gérer les cas de succès et d'erreur, typiquement en utilisant la correspondance de motifs avec les expressions `match`.


Considérons la fonction `File::open`, qui retourne un `Result<File, std::io::Error>`. Lors de l'ouverture d'un fichier, vous recevez soit un objet `File` en cas de succès, soit un objet `std::io::Error` en cas d'échec de l'opération. Vous pouvez faire correspondre ce résultat pour traiter chaque cas de manière appropriée. Dans le cas d'un succès, vous pouvez continuer les opérations sur le fichier, alors que dans le cas d'une erreur, vous pouvez essayer de créer le fichier, essayer une autre approche, ou propager l'erreur au code appelant. Cette gestion explicite garantit que votre programme prend des décisions conscientes concernant la récupération des erreurs plutôt que de se bloquer de manière inattendue.


### Modèles et raccourcis de gestion des erreurs


Alors que le pattern matching explicite fournit un contrôle complet sur la gestion des erreurs, Rust offre plusieurs méthodes de commodité pour les patterns de gestion d'erreurs les plus courants. La méthode `unwrap` extrait la valeur de succès d'un `Result` mais panique si une erreur survient, ce qui la rend utile pour le prototypage rapide ou les situations où vous êtes confiant dans la réussite d'une opération. La méthode `expect` fonctionne de manière similaire mais vous permet de fournir un message de panique personnalisé, facilitant le débogage lorsque les choses tournent mal.


Pour une gestion plus souple des erreurs, des méthodes comme `unwrap_or_else` vous permettent de fournir une fermeture qui s'exécute lorsqu'une erreur se produit, permettant une logique de récupération personnalisée. Vous pouvez enchaîner ces opérations pour gérer des scénarios complexes, tels que la tentative d'ouverture d'un fichier et sa création s'il n'existe pas, avec différentes stratégies de gestion des erreurs pour chaque étape.


L'opérateur point d'interrogation (`?`) fournit une syntaxe concise pour la propagation des erreurs, ce qui est courant dans les programmes Rust. Lorsque vous ajoutez `?` à un `Result`, il décompresse automatiquement les valeurs réussies et renvoie les erreurs immédiatement depuis la fonction courante. Cet opérateur ne peut être utilisé que dans les fonctions qui renvoient des types `Result`, ce qui permet de s'assurer que les erreurs peuvent être correctement propagées sur la pile d'appels. L'opérateur `?` rend le code de gestion des erreurs beaucoup plus lisible en éliminant les expressions de correspondance verbeuses tout en maintenant une sémantique explicite de propagation des erreurs.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Propagation des erreurs et conception des fonctions


La propagation des erreurs est un concept fondamental dans la gestion des erreurs Rust, permettant aux fonctions de transmettre les erreurs à la pile d'appels plutôt que de les gérer localement. Lorsque vous concevez des fonctions susceptibles d'échouer, vous devez renvoyer des types `Résultat` pour donner aux appelants la flexibilité de décider comment gérer les erreurs. Cette approche favorise une gestion composable des erreurs où chaque fonction de la chaîne d'appel peut soit gérer les erreurs localement, soit les transmettre à un code de plus haut niveau qui dispose de plus de contexte pour prendre des décisions de récupération.


L'opérateur point d'interrogation simplifie la propagation des erreurs. Au lieu d'écrire des expressions de correspondance verbeuses pour chaque opération susceptible d'échouer, vous pouvez enchaîner les opérations avec les opérateurs `?`, en créant un code lisible qui gère le chemin de la réussite tout en propageant automatiquement toutes les erreurs qui se produisent. Ce modèle est si courant que de nombreuses fonctions Rust sont conçues spécifiquement pour fonctionner avec l'opérateur `?`, ce qui permet une gestion fluide des erreurs dans votre base de code.


Lorsqu'il s'agit de choisir entre la panique et le renvoi d'erreurs, il faut se demander si le code appelant peut raisonnablement se remettre de la défaillance. Si un échec représente une erreur de programmation ou un état du système irrécupérable, paniquer est approprié. Cependant, si l'échec est une condition attendue que le code appelant peut gérer différemment en fonction du contexte, retourner un `Result` fournit une meilleure flexibilité et une meilleure composabilité.


### Bonnes pratiques et considérations en matière de conception


Une gestion efficace des erreurs dans Rust nécessite de bien réfléchir au moment où il faut paniquer et au moment où il faut renvoyer les erreurs. Utilisez les paniques pour les situations qui représentent des erreurs de programmation ou des états qui ne devraient jamais se produire dans des programmes corrects, comme l'accès à des données codées en dur dont vous savez qu'elles sont valides. Par exemple, l'analyse d'une chaîne d'adresse IP codée en dur dont vous avez vérifié la validité peut utiliser `expect` en toute sécurité avec un message descriptif expliquant pourquoi l'opération ne devrait jamais échouer.


Pour les entrées contrôlées par l'utilisateur ou les interactions avec le système externe, préférez toujours renvoyer des types `Result` plutôt que de paniquer. Les utilisateurs font des erreurs, les fichiers sont supprimés et les connexions réseau échouent - ce sont des conditions normales que les programmes bien conçus doivent gérer avec élégance. En renvoyant des erreurs dans ces situations, vous permettez au code appelant de mettre en œuvre des stratégies de récupération appropriées, qu'il s'agisse d'inviter l'utilisateur à saisir d'autres données, de revenir aux valeurs par défaut ou d'afficher des messages d'erreur utiles.


Envisagez de créer des types personnalisés qui appliquent la validation au moment de la construction afin d'empêcher les états non valides de se propager dans votre programme. Par exemple, si votre programme requiert des nombres compris dans un intervalle spécifique, créez un type enveloppant qui valide les entrées lors de la construction et ne permet pas de créer des instances non valides. Cette approche utilise le système de types de Rust pour éliminer des classes entières d'erreurs en rendant les états non valides irreprésentables, réduisant ainsi la nécessité de vérifier les erreurs au moment de l'exécution dans l'ensemble de votre base de code.


## Fonctionnalités de la programmation fonctionnelle, fermetures et pointeurs intelligents


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Bien que le Rust ne soit pas un langage de programmation fonctionnel pur, il intègre des caractéristiques inspirées des paradigmes de programmation fonctionnelle. Ces caractéristiques permettent aux développeurs d'écrire un code concis en exploitant des concepts tels que les fermetures et les itérateurs. Rust inclut ces éléments fonctionnels afin de fournir des outils flexibles pour le traitement des données et les mécanismes de rappel.


Les fonctions de programmation fonctionnelle de Rust conservent les principes fondamentaux du langage, à savoir la sécurité de la mémoire et les abstractions à coût nul. Lorsque vous utilisez des fermetures et des itérateurs, vous ne sacrifiez pas la performance à l'expressivité - le compilateur Rust optimise ces constructions pour produire un code machine efficace comparable aux approches traditionnelles basées sur les boucles.


### Comprendre les fermetures


En Rust, les fermetures sont des fonctions anonymes qui peuvent capturer des variables de leur environnement. Dans d'autres langages de programmation, elles sont souvent appelées fonctions lambda. La principale caractéristique des fermetures est leur capacité à "fermer" leur environnement, ce qui signifie qu'elles peuvent accéder et utiliser des variables qui existent dans la portée où la fermeture est définie.


La syntaxe des fermetures utilise des caractères pipe (`|`) à la place des parenthèses pour définir les paramètres. Pour une fermeture sans paramètres, vous écrivez `||`, et pour les fermetures avec paramètres, vous les listez entre les pipes comme `|x, y|`. Si le corps de la fermeture consiste en une seule expression, vous pouvez omettre les accolades, ce qui rend la syntaxe très concise.


Prenons l'exemple pratique d'une entreprise de t-shirts qui distribue des chemises exclusives en fonction des préférences de ses clients. Si un client a spécifié une couleur préférée, il reçoit cette couleur ; sinon, il reçoit par défaut la couleur la plus stockée. En utilisant les fermetures, cette logique devient : `user_preference.unwrap_or_else(|| self.most_stocked())`. La fermeture `|| self.most_stocked()` fournit la valeur par défaut seulement quand c'est nécessaire, et elle peut accéder à `self` depuis son environnement.


### Inférence de type de fermeture et flexibilité


L'une des fonctionnalités les plus pratiques de Rust avec les fermetures est l'inférence automatique des types. Contrairement aux fonctions classiques pour lesquelles vous devez explicitement spécifier les types de paramètres et les types de retour, les fermetures peuvent souvent déduire ces types à partir du contexte. Le compilateur analyse la façon dont la fermeture est utilisée et détermine automatiquement les types appropriés. Cependant, une fois qu'une fermeture est appelée avec des types spécifiques, ces types deviennent fixes pour cette instance de fermeture.


Vous pouvez stocker les fermetures dans des variables comme n'importe quelle autre valeur, ce qui en fait des citoyens de première classe dans le langage. Lorsque vous assignez une fermeture à une variable, vous pouvez l'appeler plus tard en utilisant des parenthèses : `let ma_fermeture = |x| x + 1 ; let result = ma_fermeture(5);`. Cette flexibilité vous permet de passer des fermetures comme arguments à des fonctions, de les retourner à partir de fonctions et de les utiliser dans des structures de données.


Si le compilateur ne peut pas déduire les types ou si vous voulez être explicite, vous pouvez annoter les paramètres de fermeture et les types de retour en utilisant une syntaxe similaire à celle des fonctions : `|x : i32| -> i32 { x + 1 }`. Ce typage explicite est parfois nécessaire dans des scénarios complexes où le compilateur a besoin d'informations supplémentaires pour résoudre les types correctement.


### Capturer les variables d'environnement


Les fermetures peuvent capturer des variables de leur environnement de trois manières différentes : par référence immuable, par référence mutable, ou en prenant la propriété. Le compilateur Rust détermine automatiquement la méthode de capture la plus restrictive qui répond aux besoins de votre fermeture, en suivant le principe du moindre privilège.


Lorsqu'une fermeture ne doit lire qu'une valeur, elle la capture par une référence immuable. Cela permet à la variable originale de rester accessible après la définition et l'appel de la fermeture. Par exemple, une fermeture qui imprime une liste empruntera la liste de manière immuable, ce qui vous permettra de continuer à utiliser la liste après l'exécution de la fermeture.


Si une fermeture doit modifier une variable capturée, elle doit capturer par référence mutable. Dans ce cas, la variable capturée et la fermeture elle-même doivent être déclarées comme mutables. La fermeture peut alors modifier la variable capturée, mais les règles d'emprunt s'appliquent toujours - vous ne pouvez pas avoir d'autres références à cette variable tant que la fermeture mutable existe.


La méthode de capture la plus restrictive est la prise de propriété, qui déplace les variables capturées dans la fermeture. Ceci est nécessaire lorsque la fermeture peut dépasser la portée où les variables ont été définies à l'origine, comme lors de la création de threads. Vous pouvez forcer la capture de propriété en utilisant le mot-clé `move` devant les paramètres de la fermeture : `move |x| { /* corps de la fermeture */ }`. Ceci est essentiel pour la sécurité des threads, car les threads ne peuvent pas emprunter en toute sécurité à d'autres threads qui pourraient se terminer et abandonner leurs variables.


### Traits de fermeture et types de fonctions


Rust représente les fermetures à travers un système de traits avec trois traits clés : `FnOnce`, `FnMut`, et `Fn`. Ces traits forment une hiérarchie qui décrit comment les fermetures peuvent être appelées et ce qu'elles peuvent faire avec les variables capturées.


`FnOnce` est le trait le plus basique que toutes les fermetures implémentent. Elle représente les fermetures qui peuvent être appelées au moins une fois. Certaines fermetures, en particulier celles qui déplacent les valeurs capturées ou les consomment d'une manière ou d'une autre, ne peuvent être appelées qu'une seule fois parce qu'elles détruisent ou déplacent les données capturées pendant l'exécution.


`FnMut` représente les fermetures qui peuvent être appelées plusieurs fois et qui peuvent modifier l'environnement capturé. Ces fermetures capturent des variables par référence mutable et peuvent les modifier à travers de multiples appels. Les règles d'emprunt garantissent que lorsqu'une fermeture `FnMut` est active, elle a un accès mutable exclusif à ses variables capturées.


`Fn` est le trait le plus restrictif, représentant les fermetures qui peuvent être appelées plusieurs fois sans modifier leur environnement capturé. Ces fermetures capturent uniquement par référence immuable et peuvent être appelées simultanément sans violer les garanties de sécurité de Rust. Si une fermeture implémente `Fn`, elle implémente automatiquement `FnMut` et `FnOnce`, puisque être appelable plusieurs fois sans mutation implique d'être appelable avec mutation et d'être appelable une fois.


### Travailler avec des itérateurs


Les itérateurs de Rust permettent de traiter des séquences de données. Ils sont paresseux, ce qui signifie qu'ils n'effectuent aucun travail jusqu'à ce que vous les consommiez en appelant des méthodes qui itèrent réellement à travers les données. Cette évaluation paresseuse permet d'enchaîner efficacement les opérations sans créer de collections intermédiaires.


Le trait `Iterator` définit la fonctionnalité de base avec un type associé `Item` qui représente ce que l'itérateur produit, et une méthode `next` qui retourne `Option<Self::Item>`. Lorsque `next` renvoie `None`, l'itérateur est épuisé. Cette conception permet aux itérateurs de représenter en toute sécurité des séquences finies et potentiellement infinies.


Vous pouvez créer des itérateurs à partir de collections en utilisant des méthodes comme `iter()` pour emprunter l'itération, `iter_mut()` pour emprunter l'itération mutable, et `into_iter()` pour consommer l'itération. Le choix entre ces méthodes dépend de la nécessité de modifier des éléments ou de consommer la collection d'origine.


### Adaptateurs et consommateurs d'itérateurs


Les adaptateurs d'itérateurs sont des méthodes qui transforment un itérateur en un autre, ce qui permet d'enchaîner les opérations. Les adaptateurs les plus courants sont `map` pour transformer chaque élément, `filter` pour sélectionner des éléments en fonction d'un prédicat, et `enumerate` pour ajouter des indices. Ces adaptateurs sont paresseux - ils ne font aucun travail jusqu'à ce qu'ils soient consommés.


La méthode `map` applique une fermeture à chaque élément, le transformant en quelque chose d'autre. Par exemple, `numbers.iter().map(|x| x * 2)` crée un itérateur qui double chaque nombre. La méthode `filter` ne conserve que les éléments pour lesquels la fermeture du prédicat retourne vrai : `numbers.iter().filter(|&x| x > 10)` ne conserve que les nombres supérieurs à dix.


Les méthodes de consommation itèrent à travers les données et produisent un résultat final. La méthode `collect` consomme un itérateur et crée une collection à partir de celui-ci. Vous devez souvent spécifier le type de collection : `let vec : Vec<_> = iterator.collect()`. D'autres consommateurs incluent `sum` pour ajouter des éléments numériques, `fold` pour accumuler des valeurs avec une opération personnalisée, et `for_each` pour exécuter des effets de bord sur chaque élément.


### Modèles d'itérateurs avancés


Les opérations supplémentaires sur les itérateurs incluent `zip` pour combiner deux itérateurs par élément, `chain` pour concaténer les itérateurs, et `filter_map` pour combiner le filtrage et le mappage en une seule opération. La méthode `zip` crée des paires à partir des éléments correspondants de deux itérateurs : `a.iter().zip(b.iter())` produit des tuples `(a[0], b[0]), (a[1], b[1]), ...`.


La méthode `fold` est utile pour accumuler des valeurs. Elle prend une valeur initiale et une fermeture qui combine l'accumulateur avec chaque élément : `numbers.iter().fold(0, |acc, x| acc + x)` additionne tous les nombres. Ce modèle peut mettre en œuvre de nombreuses autres opérations telles que la recherche de valeurs maximales, la construction de chaînes de caractères ou la création de structures de données complexes.


Les chaînes d'itérateurs permettent d'exprimer de manière concise des transformations de données complexes. Par exemple, le traitement de données audio peut impliquer : `coefficients.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Cela multiplie les coefficients correspondants et les valeurs du tampon, additionne les résultats et décale la valeur finale, le tout dans une seule expression lisible.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Introduction aux pointeurs intelligents


Les pointeurs intelligents sont des structures de données qui agissent comme des pointeurs traditionnels, mais qui offrent des capacités supplémentaires et une gestion automatique de la mémoire. Contrairement aux références simples, les pointeurs intelligents sont propriétaires des données vers lesquelles ils pointent et peuvent mettre en œuvre un comportement personnalisé pour l'allocation, la désallocation et les schémas d'accès à la mémoire. Ce sont des outils essentiels pour gérer les données allouées au tas et mettre en œuvre des modèles de propriété complexes qui vont au-delà du système de propriété de base de Rust.


L'aspect "intelligent" vient de leur capacité à gérer automatiquement des tâches de gestion de la mémoire qui nécessiteraient autrement une intervention manuelle. Lorsqu'un pointeur intelligent sort de son champ d'application, il peut automatiquement libérer la mémoire associée, décrémenter le nombre de références ou effectuer d'autres opérations de nettoyage. Cette automatisation permet d'éviter les fuites de mémoire et les erreurs d'utilisation après libération, tout en offrant une plus grande souplesse que l'allocation par pile uniquement.


Les pointeurs intelligents implémentent généralement deux traits clés : `Deref` et `Drop`. Le trait `Deref` permet d'utiliser le pointeur intelligent comme s'il s'agissait d'une référence aux données qu'il contient. Le trait `Drop` permet une logique de nettoyage personnalisée lorsque le pointeur intelligent est détruit. Ensemble, ces traits permettent aux pointeurs intelligents de gérer la mémoire automatiquement.


### La boîte Smart Pointer


`Box<T>` est le pointeur intelligent le plus simple, permettant l'allocation du tas pour tout type `T`. Quand vous créez une `Box`, la valeur contenue est stockée sur le tas plutôt que sur la pile, et la `Box` elle-même (qui n'est qu'un pointeur) est stockée sur la pile. Cette indirection est utile lorsque vous avez besoin de stocker de grandes quantités de données sans les déplacer, lorsque vous avez besoin d'un type dont la taille est inconnue à la compilation, ou lorsque vous voulez transférer la propriété des données du tas de manière efficace.


La création d'une `Box` est simple : `let boxed_value = Box::new(42);` alloue un entier sur le tas. La `Box` gère automatiquement cette mémoire - quand la `Box` sort du champ d'application, elle désalloue automatiquement la mémoire du tas. Ce nettoyage automatique permet d'éviter les fuites de mémoire sans nécessiter de gestion manuelle de la mémoire.


L'un des cas d'utilisation les plus importants de `Box` est l'activation de structures de données récursives. Considérons une liste chaînée où chaque noeud contient une valeur et un pointeur vers le noeud suivant. Sans `Box`, vous ne pouvez pas définir une telle structure car le compilateur ne peut pas déterminer la taille d'un type qui se contient lui-même. En utilisant `Box<Node>` pour le pointeur suivant, vous vous affranchissez du problème de taille récursive car `Box` a une taille fixe et connue, indépendamment de ce qu'elle contient.


### Mise en œuvre de l'attribut Deref


Le trait `Deref` permet à un type d'être déréférencé en utilisant l'opérateur `*`, ce qui permet aux pointeurs intelligents de se comporter comme des références aux données qu'ils contiennent. Lorsque vous implémentez `Deref` pour un pointeur intelligent, vous activez le déréférencement automatique qui rend le pointeur intelligent transparent à utiliser. Cela signifie que vous pouvez appeler des méthodes sur le type contenu directement à travers le pointeur intelligent sans déréférencement explicite.


Le trait `Deref` définit un type associé `Target` qui spécifie le type de référence que l'opération de déréférence doit produire. Le trait requiert l'implémentation d'une méthode `deref` qui renvoie une référence au type cible. Pour `Box<T>`, l'implémentation renvoie une référence à la valeur `T` contenue.


Rust effectue une coercion automatique des déréférences, ce qui signifie que le compilateur peut automatiquement insérer des appels à `deref` lorsque cela est nécessaire pour rendre les types compatibles. C'est pourquoi vous pouvez passer une `String` à une fonction qui attend un `&str` - le compilateur déréférence automatiquement la `String` pour obtenir une tranche de chaîne. Cette coercition peut s'enchaîner à plusieurs niveaux, de sorte qu'une `Box<String>` peut être automatiquement convertie en une `&str` par de multiples opérations de déréférencement.


### Mise en œuvre d'une goutte d'eau personnalisée


Le trait `Drop` vous permet de spécifier un code de nettoyage personnalisé qui s'exécute lorsqu'une valeur sort du champ d'application. Ceci est particulièrement important pour les pointeurs intelligents qui gèrent des ressources au-delà de la simple mémoire, comme les handles de fichiers, les connexions réseau ou les comptes de références. Le trait `Drop` a une seule méthode, `drop`, qui prend une référence mutable à `self` et effectue le nettoyage.


La plupart des types n'ont pas besoin d'implémentations personnalisées de `Drop` car Rust gère automatiquement l'abandon de leurs champs. Cependant, les pointeurs intelligents ont souvent besoin d'une logique personnalisée pour nettoyer correctement les ressources qu'ils gèrent. Par exemple, un pointeur intelligent à comptage de références doit décrémenter le comptage de références et potentiellement désallouer les données partagées lorsque la dernière référence est abandonnée.


Vous pouvez aussi explicitement abandonner une valeur avant qu'elle ne sorte de la portée en utilisant `std::mem::drop()`. Cette fonction prend la propriété d'une valeur et l'abandonne immédiatement, ce qui peut être utile pour libérer des ressources plus tôt ou pour s'assurer que le nettoyage a lieu à un moment précis de votre programme. La fonction drop explicite est juste une fonction d'identité qui prend la propriété - le vrai travail se fait quand la valeur est abandonnée à la fin de la fonction.


Cette base de fermetures, d'itérateurs et de pointeurs intelligents donne aux développeurs de Rust des outils pour écrire un code expressif, sûr et efficace. Ces caractéristiques s'associent pour permettre des schémas de programmation communs tout en maintenant les garanties fondamentales de Rust en matière de sécurité de la mémoire et de performances.



## Comptage de références et mutabilité intérieure

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Comptage de référence avec RC


Le comptage de références représente un autre type fondamental de pointeur intelligent dans Rust, conçu spécifiquement pour permettre des scénarios de propriété multiple. Contrairement à Box, qui suit les règles traditionnelles de propriété unique où une seule entité possède les données, RC (Reference Counter) permet à plusieurs parties de votre code de partager simultanément la propriété des mêmes données. Ce modèle de propriété partagée fonctionne grâce à un mécanisme de comptage qui permet de savoir combien de références existent pour un élément de données particulier.


Le système de comptage de références fonctionne en maintenant un compteur interne qui s'incrémente chaque fois que vous clonez une RC et se décrémente lorsqu'une RC est abandonnée. La mémoire n'est libérée que lorsque ce compteur atteint zéro, ce qui garantit que les données restent valides tant qu'une référence existe. Cette approche empêche la désallocation prématurée tout en permettant des schémas de partage de données flexibles qui seraient impossibles avec la simple propriété d'une boîte.


Un exemple pratique de l'utilité du RC concerne la création de structures de données partagées telles que les listes chaînées, où plusieurs listes peuvent faire référence à la même partie de la queue. Imaginons que l'on tente de créer deux listes distinctes faisant toutes deux référence à une sous-séquence commune. Avec la propriété de Box, cela devient impossible parce que le déplacement de la partie partagée dans la première liste transfère la propriété, empêchant son utilisation dans la seconde liste. RC résout ce problème en vous permettant de cloner la référence plutôt que les données sous-jacentes, ce qui rend la structure partagée possible tout en maintenant la sécurité de la mémoire.


Lorsque vous clonez un CR, vous ne dupliquez pas les données internes, quelle que soit leur taille ou leur complexité. Au lieu de cela, vous créez une autre référence au même emplacement mémoire et vous incrémentez le compteur de référence. Le clonage d'instances de CR est donc efficace, même pour les structures de données volumineuses, car seule la référence est copiée, tandis que les données sous-jacentes restent en place.


### Mutabilité intérieure avec RefCell


RefCell introduit la mutabilité intérieure, qui vous permet de modifier des données même si vous ne disposez que d'une référence immuable. Cette capacité modifie fondamentalement la manière dont les règles d'emprunt de Rust sont appliquées en déplaçant les vérifications du moment de la compilation au moment de l'exécution. Alors que les références normales dépendent du compilateur pour vérifier la sécurité de l'emprunt, RefCell effectue ces vérifications pendant l'exécution du programme, offrant ainsi une plus grande flexibilité au prix de paniques potentielles au moment de l'exécution.


Le principe de base de RefCell consiste à maintenir les mêmes règles d'emprunt que Rust applique normalement au moment de la compilation, mais en les vérifiant dynamiquement. À tout moment, vous pouvez avoir soit une référence mutable, soit un nombre quelconque de références immuables aux données à l'intérieur d'une cellule RefCell. Si votre code tente de violer ces règles en créant simultanément des emprunts conflictuels, le programme paniquera plutôt que de produire un comportement indéfini.


Cette vérification au moment de l'exécution permet certains modèles de programmation que le compilateur pourrait rejeter même s'ils sont en fait sûrs. L'analyse statique du compilateur ne peut pas toujours prouver que les modèles d'emprunt complexes sont corrects, ce qui l'amène à privilégier la prudence. RefCell vous permet d'ignorer ces restrictions conservatrices lorsque vous êtes convaincu de la justesse de votre code, mais cette confiance s'accompagne de la responsabilité de garantir une utilisation correcte afin d'éviter les pannes d'exécution.


Un cas d'utilisation courant de RefCell implique des objets fictifs dans les scénarios de test. Lorsque vous mettez en œuvre un trait qui ne fournit qu'un accès immuable au soi, mais que votre implémentation fictive doit suivre les changements d'état en interne, RefCell permet d'appliquer ce modèle. Vous pouvez envelopper l'état interne dans un RefCell, ce qui permet à l'objet fantaisie de modifier ses données de suivi, même par le biais d'une interface immuable.


### Combinaison de RC et de RefCell pour un état mutable partagé


La combinaison de RC et de RefCell crée un modèle d'état mutable partagé, où plusieurs propriétaires peuvent tous potentiellement modifier les mêmes données. RC fournit la capacité de propriété partagée, tandis que RefCell permet la mutation par le biais de références immuables. Cette combinaison est utile dans des scénarios tels que les structures de graphe, les caches ou toute situation où plusieurs parties de votre programme ont besoin d'un accès en lecture et en écriture à des données partagées.


Lorsque vous intégrez une RefCell dans un RC, vous créez une structure qui peut être clonée et distribuée dans votre programme, chaque clone ayant accès aux mêmes données mutables sous-jacentes. Tous les propriétaires peuvent potentiellement modifier les données à l'aide de la méthode borrow_mut de RefCell, mais ils doivent toujours respecter les règles d'emprunt au moment de l'exécution. Ce modèle permet des scénarios de partage de données complexes tout en maintenant les garanties de sécurité de Rust grâce à des vérifications au moment de l'exécution.


Toutefois, cette flexibilité s'accompagne d'importantes mises en garde concernant les fuites de mémoire et les cycles de référence. Lorsque l'on utilise RC avec RefCell, il devient possible de créer accidentellement des références circulaires dans lesquelles les structures de données se référencent elles-mêmes, soit directement, soit par le biais d'une chaîne de références. Ces cycles empêchent le nombre de références d'atteindre zéro, ce qui provoque des fuites de mémoire car les données semblent toujours avoir des références actives, même si elles ne sont plus accessibles depuis le reste du programme.


La solution aux cycles de référence consiste à utiliser des références faibles, qui ne contribuent pas au nombre de références utilisé pour les décisions de gestion de la mémoire. Les références faibles permettent de maintenir les connexions entre les structures de données sans les garder vivantes, ce qui rompt les cycles potentiels tout en préservant la possibilité d'accéder aux données connexes lorsqu'elles existent encore.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### Principes de base de la sécurité des threads et de la simultanéité


L'approche de Rust en matière de concurrence est centrée sur la prévention des courses de données et des problèmes de sécurité de la mémoire au moment de la compilation. Le système de types renforce la sécurité des threads grâce à des traits comme `Send` et `Sync`, qui marquent les types comme sûrs pour le transfert entre les threads ou sûrs pour l'accès concurrent, respectivement. Cette vérification à la compilation permet de détecter de nombreux bogues de concurrence qui n'apparaîtraient qu'à l'exécution dans d'autres langages de programmation de systèmes.


La création de threads dans Rust suit un modèle simple en utilisant thread::spawn, qui prend une fermeture à exécuter dans le nouveau thread et renvoie un handle pour gérer le cycle de vie du thread. Le thread créé s'exécute en même temps que le thread principal, et vous pouvez utiliser la méthode join sur le handle pour attendre la fin de l'exécution. Sans jointure explicite, les threads créés peuvent être interrompus lorsque le thread principal se termine, ce qui risque d'interrompre un travail incomplet.


Le mot-clé move devient crucial lorsque l'on travaille avec des threads, car les fermetures transmises à des threads engendrés doivent souvent posséder leurs données plutôt que de les emprunter. Comme les threads engendrés peuvent survivre à la portée qui les a créés, l'emprunt à la portée parentale crée des violations potentielles de la durée de vie. En déplaçant les données dans la fermeture du thread, on en transfère la propriété, ce qui garantit que les données resteront valables pendant toute la durée de vie du thread, tout en empêchant l'accès à partir de la portée d'origine.


Le passage de messages offre une alternative à la concurrence par état partagé grâce à des canaux qui permettent aux threads de communiquer en envoyant des données plutôt qu'en partageant la mémoire. La bibliothèque standard de Rust fournit des canaux MPSC (Multiple Producer Single Consumer), où plusieurs threads peuvent envoyer des messages à un seul thread récepteur. Ce modèle élimine de nombreux problèmes de synchronisation en évitant totalement le partage d'états mutables et en s'appuyant sur l'échange de messages pour la coordination.


### Concurrence d'états partagés avec Mutex et Arc


Lorsque le passage de messages n'est pas approprié, Rust fournit une concurrence traditionnelle d'état partagé grâce à Mutex (exclusion mutuelle) combiné à Arc (Atomic Reference Counter). Mutex garantit qu'un seul thread peut accéder à des données protégées à la fois en exigeant que les threads acquièrent un verrou avant d'accéder aux données. Le verrou est automatiquement libéré lorsque l'objet de garde renvoyé par l'opération de verrouillage sort du champ d'application, ce qui permet d'éviter les scénarios de blocage courants causés par des déverrouillages oubliés.


Arc est l'équivalent thread-safe de RC, utilisant des opérations atomiques pour gérer le nombre de références en toute sécurité à travers plusieurs threads. Alors que le RC fonctionne parfaitement pour les scénarios à un seul thread, son comptage de référence non atomique crée des conditions de course lorsqu'on y accède à partir de plusieurs threads. Les compteurs atomiques d'Arc garantissent que les modifications du nombre de références sont effectuées en toute sécurité, même en cas d'accès simultané, ce qui permet de partager des données entre plusieurs threads.


La combinaison de l'Arc et du Mutex crée un modèle d'état mutable partagé dans les programmes concurrents. En enveloppant un Mutex dans un Arc, vous pouvez cloner l'Arc pour distribuer l'accès au même Mutex entre plusieurs threads, chaque thread pouvant acquérir le verrou et modifier les données protégées en toute sécurité. Ce modèle offre la flexibilité d'un état partagé tout en maintenant les garanties de sécurité de Rust grâce à la vérification à la compilation et au verrouillage à l'exécution.


Les traits Send et Sync fonctionnent en coulisses pour assurer la sécurité des threads au moment de la compilation. Send indique qu'un type peut être transféré en toute sécurité à un autre thread, tandis que Sync indique que les références à un type peuvent être partagées en toute sécurité entre les threads. La plupart des types implémentent automatiquement ces traits lorsque leurs composants sont thread-safe, mais certains types comme RC et RefCell ne les implémentent pas explicitement car ils ne sont pas conçus pour un accès concurrent. Cette implémentation automatique des traits empêche l'introduction accidentelle de violations de la sécurité des threads tout en permettant aux types sûrs de fonctionner de manière transparente dans des contextes concurrents.


## Comprendre les macros Rust

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Introduction aux macros dans Rust


Les macros dans Rust sont une fonction de métaprogrammation qui permet aux développeurs d'écrire du code qui génère d'autres codes au moment de la compilation. Contrairement aux fonctions, qui sont appelées au moment de l'exécution, les macros sont développées au début du processus de compilation, avant la vérification du type et les étapes ultérieures. Cette distinction fondamentale rend les macros particulièrement utiles pour réduire la répétition du code et créer des langages spécifiques à un domaine dans les programmes Rust.


L'indicateur le plus reconnaissable d'un appel de macro est le point d'exclamation ( !) qui suit le nom de la macro. Par exemple, lorsque vous utilisez `println !("Hello, world !")`, vous n'appelez pas une fonction mais une macro. Cette macro se développe en un code plus complexe qui gère les opérations de formatage et de sortie. Le point d'exclamation sert de repère visuel aux développeurs pour leur indiquer qu'il s'agit d'une génération de code à la compilation plutôt que d'un appel de fonction standard.


Rust propose trois types de macros distincts, chacun servant des objectifs différents dans l'écosystème du langage :



- Macros de type fonction** : Ressemblent à des appels de fonction mais opèrent au moment de la compilation (par exemple, `vec!`, `println!`)
- Macros de dérivation** : Implémentation automatique des traits pour les types (par exemple, `#[derive(Debug, Clone)]`)
- Macros de type attribut** : Modifient le comportement des éléments de code auxquels elles s'appliquent (par exemple, `#[test]`, `#[tokio::main]`)


La compréhension de ces différents types de macros est essentielle pour une programmation Rust efficace, car chacun d'entre eux répond à des cas d'utilisation et à des schémas de programmation spécifiques.


### Types de macros et leurs applications


Les macros de type fonction représentent le type de macro le plus fréquemment rencontré dans la programmation Rust. Ces macros utilisent une syntaxe similaire à celle des appels de fonction, mais elles effectuent une recherche de motifs sur leur entrée afin d'obtenir le code approprié. La macro `vec!` est un exemple courant de cette catégorie, permettant aux développeurs de créer et d'initialiser des vecteurs avec une syntaxe concise. Lorsque vous écrivez `vec ![1, 2, 3, 4]`, la macro l'interprète comme un code qui crée un nouveau vecteur, pousse chaque élément individuellement et renvoie le vecteur complet.


Les macros derive fournissent des implémentations automatiques de traits pour les types personnalisés, réduisant ainsi de manière significative le code de substitution. Lorsque vous ajoutez `#[derive(Debug)]` à une définition de structure ou d'enum, vous demandez au compilateur de generate une implémentation complète du trait Debug pour ce type. Cette implémentation générée gère la logique de formatage nécessaire pour afficher le contenu du type dans un format lisible par l'homme. Le mécanisme derive prend en charge de nombreux traits de la bibliothèque standard, notamment Clone, PartialEq, ce qui en fait un outil couramment utilisé pour réduire la "boilerplate".


Les macros de type attribut modifient le comportement des éléments de code qu'elles annotent, ce qui permet d'ajouter des métadonnées ou de modifier le comportement de la compilation. Ces macros apparaissent comme des attributs placés au-dessus des définitions de type, des fonctions ou d'autres constructions de code. Par exemple, l'attribut `#[non_exhaustive]` sur une énumération indique que des variantes supplémentaires pourraient être ajoutées dans les versions futures, exigeant que les expressions de correspondance incluent un cas par défaut. Ce mécanisme garantit la compatibilité avec les versions ultérieures tout en fournissant une documentation claire sur le potentiel d'évolution du type.


### Création de macros personnalisées ressemblant à des fonctions


Pour écrire des macros personnalisées de type fonction, il faut comprendre la syntaxe de filtrage de Rust pour les définitions de macros. La définition de la macro utilise une approche déclarative dans laquelle vous spécifiez des modèles qui correspondent à différentes formes d'entrée et à des modèles de génération de code correspondants. Chaque macro peut contenir plusieurs branches, ce qui lui permet de traiter différents modèles d'entrée et de générer le code approprié dans chaque cas.


Considérez la création d'une macro vectorielle personnalisée qui démontre les principes fondamentaux de la construction d'une macro. La définition de la macro commence par `macro_rules!` suivi du nom de la macro et d'une série de branches de recherche de motifs. Chaque branche consiste en un motif qui correspond à une syntaxe d'entrée spécifique et un modèle de code qui génère le code Rust correspondant. Par exemple, une branche simple peut correspondre aux crochets vides `[]` et au code generate pour créer un vecteur vide, tandis qu'une autre branche correspond à une expression unique et génère du code pour créer un vecteur avec un seul élément.


Les macros sont particulièrement utiles lorsqu'il s'agit d'implémenter des modèles d'arguments variables à l'aide de la syntaxe de répétition. Le motif `$($x:expr),*` correspond à zéro ou plusieurs expressions séparées par des virgules, ce qui permet à la macro de gérer un nombre arbitraire d'arguments. Le modèle de génération de code correspondant utilise `$(vec.push($x) ;)*` pour itérer sur toutes les expressions correspondantes et generate instructions push individuelles pour chacune d'entre elles. Ce mécanisme de répétition permet aux macros de generate générer du code qu'il serait impossible ou extrêmement verbeux d'écrire manuellement.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


Le processus de compilation transforme les appels de macros en code développé avant la vérification du type et l'optimisation. Lorsque le compilateur rencontre une invocation de macro, il compare l'entrée aux modèles définis et remplace l'appel de macro par le code généré. Ce code étendu subit ensuite les processus de compilation normaux, y compris la vérification des types et l'optimisation. Des outils tels que `cargo expand` permettent aux développeurs d'inspecter le code généré, offrant ainsi de précieuses possibilités de débogage lors du développement de macros complexes.


### Concepts avancés des macros et débogage


Le développement de macros nécessite de comprendre la distinction entre l'exécution au moment de la compilation et l'exécution au moment de l'exécution. Les macros s'exécutent pendant la compilation, générant un code qui sera exécuté au moment de l'exécution. Cette séparation temporelle signifie que la logique de la macro ne peut pas dépendre des valeurs d'exécution, mais elle permet également des optimisations lorsque des calculs complexes peuvent être effectués une seule fois pendant la compilation plutôt que plusieurs fois pendant l'exécution.


Le système de recherche de motifs dans les macros prend en charge divers spécificateurs de fragments qui définissent le type d'éléments de code pouvant être recherchés. Le spécificateur `expr` correspond aux expressions, `ty` correspond aux types, `ident` correspond aux identificateurs, et plusieurs autres fournissent un contrôle fin sur la validation des entrées. Ces spécificateurs assurent que les macros reçoivent des entrées syntaxiquement valides et fournissent des messages d'erreur clairs lorsqu'une syntaxe invalide est rencontrée.


Le débogage des macros présente des défis uniques en raison de leur nature à l'heure de la compilation. La commande `cargo expand` est utile pour le développement des macros, car elle affiche le code entièrement développé généré par les invocations de macros. Cet outil permet aux développeurs de vérifier que leurs macros generate produisent le code voulu et d'identifier les problèmes dans la logique d'expansion. Lorsque le code généré par la macro contient des erreurs, la sortie développée permet de déterminer si le problème se situe au niveau de la définition de la macro ou de la structure du code généré.


Les macros complexes peuvent mettre en œuvre des schémas récursifs, dans lesquels une macro s'appelle elle-même avec des arguments modifiés pour gérer la génération de code imbriqué ou itératif. Toutefois, les macros récursives doivent être conçues avec soin pour éviter l'expansion infinie et les problèmes de performance lors de la compilation. La nature compilatoire de l'expansion des macros signifie que même les implémentations de macros inefficaces n'affectent que la vitesse de compilation, et non les performances d'exécution, mais les macros excessivement complexes peuvent ralentir de manière significative le processus de construction.



# Rust & Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Pourquoi Rust pour le développement de Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


Le choix de Rust pour le développement de Bitcoin et de Lightning n'est pas une coïncidence. Le développement de Bitcoin comporte des responsabilités uniques qui le distinguent du développement logiciel classique. Lorsqu'ils travaillent avec Bitcoin, les développeurs manipulent souvent des fonds d'utilisateurs dans un environnement où les erreurs peuvent être irréversibles. Contrairement aux systèmes financiers traditionnels dotés de protections réglementaires et de mécanismes de rétrofacturation, la nature décentralisée de Bitcoin signifie qu'une fois qu'une transaction est diffusée, il n'y a pas d'autorité à laquelle faire appel pour récupérer les fonds. Cette réalité exige un niveau plus élevé de responsabilité et de précision dans le développement des logiciels.


La philosophie "aller vite et tout casser" qui fonctionne dans de nombreux secteurs technologiques ne s'applique tout simplement pas au développement de Bitcoin. Au contraire, l'écosystème requiert des langages et des outils qui aident les développeurs à créer des logiciels robustes et sécurisés où les défaillances sont soit évitées, soit gérées de manière gracieuse. C'est la raison pour laquelle de nombreux projets Bitcoin de premier plan se sont tournés vers le Rust, notamment le kit de développement Bitcoin (BDK), le kit de développement Lightning (LDK) et le BreezSDK.


Le Rust offre trois propriétés essentielles qui le rendent particulièrement adapté au développement du Bitcoin : un système de types statiques forts, un outillage moderne riche et une compatibilité multiplateforme. Chacune de ces caractéristiques contribue à la capacité du langage à aider les développeurs à écrire un code plus sûr et plus fiable pour traiter les opérations de crypto-monnaie.


### Le système de type statique fort de Rust


Le système de type de Rust offre des caractéristiques de typage statique et fort qui permettent de détecter les erreurs avant qu'elles n'affectent les utilisateurs. La nature statique signifie que la vérification des types a lieu au moment de la compilation, ce qui oblige les développeurs à résoudre les erreurs de type avant même que le programme ne puisse être construit. En revanche, dans les langages à typage dynamique, les erreurs de typage n'apparaissent qu'au cours de l'exécution, potentiellement après que le logiciel a été déployé et qu'il gère des fonds d'utilisateurs réels.


La force du système de types de Rust réside dans son expressivité et sa rigueur dans la modélisation des problèmes. Contrairement aux langages dotés de systèmes de types plus faibles, comme le C, où les développeurs sont limités à des types de base tels que les nombres et les structures, le Rust permet une modélisation riche des types qui peut représenter avec précision des concepts de domaine complexes. Par exemple, vous pouvez créer des types qui font la distinction entre différents types de listes ou qui imposent que certaines opérations ne soient effectuées que sur des types d'objets spécifiques.


Ce qui rend le système de types de Rust pertinent pour le développement de Bitcoin, c'est son approche de la sécurité de la mémoire. Le même système de types qui modélise la logique commerciale gère également la propriété de la mémoire et le contrôle de l'accès partagé. Cette double responsabilité signifie que les classes communes de vulnérabilités, telles que les fuites de mémoire, les erreurs de double absence et les conditions de course, sont entièrement éliminées par le compilateur. Le système de types applique ces garanties de sécurité grâce à des concepts tels que la propriété, l'emprunt et le comptage de références, ce qui rend extrêmement difficile l'introduction de bogues liés à la mémoire qui pourraient compromettre la sécurité ou la stabilité.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Outils modernes et support multiplateforme


L'écosystème d'outils de Rust fournit aux développeurs des outils qui contribuent à la productivité et à la qualité du code. Le compilateur Rust lui-même est conçu non seulement pour traduire le code sous forme binaire, mais aussi pour servir d'outil pédagogique qui aide les développeurs à apprendre et à s'améliorer. Lorsque des erreurs de compilation se produisent, le compilateur fournit des explications détaillées sur ce qui n'a pas fonctionné et suggère souvent des solutions spécifiques. Cette approche est particulièrement précieuse pour les développeurs qui découvrent Rust, car le compilateur enseigne efficacement les bonnes pratiques et aide à éviter les erreurs courantes.


Le langage inclut Cargo, un gestionnaire de paquets unifié qui prend en charge la gestion des dépendances, la construction, les tests et la génération de la documentation. Cette standardisation élimine la fragmentation observée dans les langages plus anciens comme le C++, où de multiples outils concurrents créent des incohérences entre les projets. Cargo prend également en charge des extensions telles que rustfmt pour le formatage du code et Clippy pour l'analyse statique, ce qui permet de s'assurer que le code respecte des règles de style cohérentes et de détecter les problèmes potentiels avant qu'ils ne se transforment en problèmes.


Les capacités multiplateformes de Rust vont au-delà des systèmes d'exploitation traditionnels pour inclure des plateformes mobiles comme Android et iOS, ainsi que WebAssembly pour les applications basées sur des navigateurs. Cette prise en charge multiplateforme est utile pour les applications Bitcoin qui doivent fonctionner dans divers environnements. Par exemple, des projets comme Mutiny Wallet exploitent la compilation WebAssembly de Rust pour créer des portefeuilles Lightning qui s'exécutent directement dans les navigateurs web, ce qui serait irréalisable avec les seules technologies web traditionnelles.


### Comprendre les types d'erreurs et leurs implications


Pour gérer efficacement les erreurs, il faut d'abord comprendre les différentes catégories d'erreurs qui peuvent survenir au cours de l'exécution du programme. Prenons l'exemple d'une simple application de routage qui calcule les chemins entre des points géographiques. Cet exemple illustre trois types fondamentaux d'erreurs que les développeurs doivent traiter : les erreurs d'entrée non valides, les erreurs de ressources d'exécution et les erreurs de logique.


Les erreurs d'entrée non valide se produisent lorsqu'une fonction reçoit des paramètres qui ne répondent pas à ses exigences. Par exemple, si un système de coordonnées géographiques utilise des entiers signés pour la longitude mais reçoit une valeur négative alors que seules les valeurs positives sont valides, la fonction ne peut pas continuer de manière significative. Ces erreurs représentent une violation du contrat entre l'appelant et la fonction, et la réponse appropriée consiste généralement à rejeter l'entrée et à renvoyer une indication d'erreur.


Les erreurs de ressources d'exécution se produisent lorsque les dépendances externes sont indisponibles ou inaccessibles. La lecture d'un fichier de carte peut échouer parce que le fichier n'existe pas, que l'application ne dispose pas des autorisations nécessaires ou que le périphérique de stockage n'est pas disponible. Ces erreurs sont extérieures à la logique du programme et nécessitent souvent des correctifs environnementaux plutôt que des modifications du code. Cependant, les applications robustes doivent anticiper et gérer ces scénarios avec élégance.


Les erreurs logiques représentent des bogues dans l'implémentation du programme ou des incompréhensions sur la façon dont les composants interagissent. Si un algorithme de routage renvoie un chemin vide alors qu'il dispose de points de départ et d'arrivée valides, cela indique un défaut logique qui doit être corrigé dans le code lui-même. Contrairement aux autres types d'erreurs, les erreurs logiques nécessitent généralement un débogage et une modification du code pour être résolues.


### Stratégies pour une gestion robuste des erreurs


La création de logiciels fiables nécessite des stratégies proactives qui minimisent les possibilités d'erreur et traitent les erreurs inévitables avec élégance. La première stratégie consiste à limiter les erreurs possibles grâce à une conception minutieuse des types. En choisissant des types qui ne peuvent représenter que des valeurs valides, les développeurs peuvent éliminer des catégories entières d'erreurs d'entrée non valides. Par exemple, l'utilisation d'entiers non signés pour les valeurs qui ne peuvent pas être négatives permet d'éviter les erreurs de valeur négative au moment de la compilation.


Les assertions fournissent une autre couche de protection en vérifiant explicitement que les conditions attendues se vérifient pendant l'exécution du programme. Ces vérifications ont plusieurs objectifs : elles détectent les bogues pendant les tests, provoquent l'échec des programmes lorsque des problèmes surviennent (ce qui facilite le débogage) et servent de documentation exécutable décrivant les hypothèses du programmeur. Lorsqu'une assertion échoue, cela signifie qu'une hypothèse fondamentale sur l'état du programme a été violée, ce qui indique généralement une erreur de logique qui doit être examinée.


Le principe des abstractions en couches permet de gérer la complexité en garantissant que les erreurs sont traitées aux niveaux appropriés du système. Les détails de l'implémentation interne, y compris les types d'erreurs spécifiques provenant des bibliothèques de niveau inférieur, ne doivent pas se propager au-delà des limites du sous-système. Au contraire, chaque couche doit traduire les erreurs en termes significatifs à ce niveau d'abstraction. Par exemple, une application wallet utilisant une bibliothèque Bitcoin doit traduire les erreurs d'analyse des descripteurs de bas niveau en messages de plus haut niveau tels que "configuration wallet non valide" qui fournissent des informations exploitables aux utilisateurs ou au code appelant.


Cette approche de la gestion des erreurs, combinée au système de types et à l'outillage de Rust, permet de détecter les problèmes potentiels à un stade précoce du processus de développement, avant qu'ils n'affectent les utilisateurs ou ne compromettent la sécurité des applications Bitcoin.



## Modèle d'erreur

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust propose une approche globale de la gestion des erreurs qui concilie sécurité et praticité. Alors que les concepts généraux du modèle d'erreur s'appliquent à tous les langages de programmation, Rust propose des outils et des modèles spécifiques qui rendent la gestion des erreurs à la fois explicite et gérable. La compréhension de ces mécanismes est cruciale pour l'écriture d'applications Rust robustes, capables de gérer gracieusement des situations inattendues tout en maintenant les performances et la sécurité.


### La panique et son utilisation appropriée


Le mécanisme de panique de Rust représente la manière la plus directe de gérer les erreurs irrécupérables. Lorsque vous appelez la macro `panic!`, le programme arrête immédiatement son exécution, soit en l'interrompant, soit en le déroulant, selon votre configuration. La macro panic accepte un message sous forme de chaîne qui décrit ce qui s'est passé, fournissant ainsi un contexte pour le débogage. De plus, des méthodes comme `unwrap()` et `expect()` sur les types Resultat et Option servent de raccourcis pour paniquer lorsque ces types contiennent des valeurs d'erreur ou None respectivement. La méthode `expect()` vous permet de fournir un message personnalisé, ce qui la rend légèrement plus informative que `unwrap()` lors du débogage des échecs.


Malgré sa simplicité, la panique doit être utilisée judicieusement dans le code de production. Il existe plusieurs scénarios dans lesquels l'utilisation de panic est non seulement acceptable, mais aussi recommandée. Lors de l'écriture d'exemples ou de prototypes, panic fournit un moyen propre de se concentrer sur la fonctionnalité principale sans encombrer le code avec une gestion complète des erreurs. Dans les environnements de test, la panique est souvent le comportement souhaité lorsque les assertions échouent, car elle indique clairement que quelque chose d'inattendu s'est produit. La communauté Rust reconnaît également les situations où les développeurs ont plus de connaissances que le compilateur, comme lors de l'analyse d'adresses IP codées en dur dont on sait qu'elles sont valides.


Cependant, l'apparente sécurité des paniques "vérifiées par le compilateur" peut être trompeuse. Considérons un scénario dans lequel vous codez en dur une adresse IP et utilisez `expect()` parce que vous savez qu'elle est valide. Au fil du temps, avec l'évolution du code, cette valeur codée en dur peut être transformée en une constante, et plus tard cette constante peut être changée en quelque chose comme "localhost" pour améliorer l'expérience de l'utilisateur. Soudain, votre panique "sûre" devient un échec d'exécution. Cette évolution montre pourquoi il est généralement préférable d'éviter les paniques dans le code de production et de renvoyer plutôt des types d'erreur appropriés qui peuvent être gérés avec élégance.


Une exception notable à la règle "éviter la panique" concerne les opérations sur les mutex. Lorsque vous appelez `lock()` sur un mutex, il renvoie un Resultat parce que le verrou peut échouer si un autre thread a paniqué pendant qu'il détenait le mutex. Cela crée une situation confuse où votre code local reçoit une erreur pour quelque chose qui s'est produit dans un contexte complètement différent. Puisque vous ne pouvez pas raisonnablement gérer une erreur provenant de la panique d'un autre thread, de nombreux développeurs considèrent qu'il est acceptable de débloquer les verrous mutex, en particulier si vous maintenez une base de code exempte de panique ailleurs.


### Utilisation des types de résultats et d'options


Le type Result constitue l'épine dorsale du système de gestion des erreurs de Rust. En tant qu'enum pouvant contenir soit un `Ok(valeur)` soit un `Err(erreur)`, Result vous force à reconnaître explicitement que les opérations peuvent échouer. Le type Option a un but similaire pour les cas où une valeur peut simplement être absente, contenant soit `Some(value)` soit `None`. Bien que Option ne fournisse pas d'informations détaillées sur les erreurs, il est parfait pour les situations où l'absence d'une valeur est significative et attendue.


Result et Option fournissent plusieurs méthodes utilitaires qui rendent la gestion des erreurs plus ergonomique. La méthode `unwrap_or()` retourne la valeur contenue si elle est présente, ou une valeur par défaut s'il y a une erreur ou None. Cette méthode est particulièrement utile lorsque vous disposez d'une solution de repli raisonnable, comme l'analyse d'une entrée utilisateur avec une valeur par défaut raisonnable en cas d'échec de l'analyse. La méthode `unwrap_or_default()` fonctionne de manière similaire mais utilise la valeur par défaut du type au lieu de vous demander d'en spécifier une. Bien que ces méthodes ne gèrent pas techniquement les erreurs dans le sens traditionnel du terme, elles fournissent un moyen de dégrader gracieusement les fonctionnalités lorsque des problèmes surviennent.


L'opérateur point d'interrogation (`?`) est une syntaxe concise pour la propagation des erreurs. Lorsqu'il est appliqué à un résultat ou à une option, il extrait la valeur de succès si elle est présente, ou renvoie immédiatement l'erreur de la fonction courante s'il y a un problème. Cet opérateur élimine les modèles de vérification d'erreur verbeux communs dans des langages comme Go, où vous devez manuellement vérifier et renvoyer les erreurs à chaque étape. L'opérateur point d'interrogation fournit essentiellement du sucre syntaxique pour les retours anticipés, ce qui vous permet d'écrire un code propre et linéaire qui se concentre sur le chemin heureux tout en gérant automatiquement la propagation des erreurs.


### Modèles avancés de gestion des erreurs


La méthode `map()` sur les types Result et Option permet une gestion des erreurs de type fonctionnel qui peut rendre le code plus expressif et composable. Lorsque vous appelez `map()` sur un Resultat, la fonction fournie est appliquée à la valeur de succès si elle est présente, alors que les erreurs sont automatiquement propagées sans modification. Ce modèle est utile lors de l'enchaînement d'opérations, car il permet de se concentrer sur la transformation des valeurs sans avoir à gérer les cas d'erreur de manière répétée. La méthode `map_err()` fournit la fonctionnalité inverse, vous permettant de transformer les types d'erreurs tout en laissant les valeurs de succès inchangées.


La transformation des erreurs devient cruciale lors de la construction d'applications en couches où différents composants ont besoin de différents types d'erreurs. Prenons l'exemple d'une fonction qui analyse les entrées de l'utilisateur et qui doit convertir les erreurs d'analyse de bas niveau en erreurs spécifiques au domaine. En utilisant `map_err()`, vous pouvez facilement traduire une erreur générique de type "format de nombre invalide" en une erreur plus contextuelle de type "âge invalide" qui a du sens dans le domaine de votre application. Cette transformation a lieu au moment où l'erreur se produit, ce qui rend le code plus lisible et plus facile à maintenir que les blocs try-catch traditionnels où la gestion des erreurs est séparée des opérations qui peuvent échouer.


La combinaison de l'opérateur point d'interrogation et de la cartographie des erreurs permet de créer des modèles concis de gestion des erreurs. Vous pouvez enchaîner les opérations, transformer les erreurs si nécessaire et les propager dans la pile d'appels avec un minimum d'informations. Cette approche permet de maintenir la gestion des erreurs à proximité des opérations susceptibles d'échouer, tout en conservant une séparation nette entre les chemins de réussite et d'erreur.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Bibliothèques externes et écosystèmes de gestion des erreurs


L'écosystème Rust comprend plusieurs bibliothèques populaires qui étendent les capacités de gestion des erreurs de la bibliothèque standard. La bibliothèque `anyhow` propose une approche simplifiée de la gestion des erreurs en offrant un type d'erreur universel qui peut être converti automatiquement à partir de n'importe quel type d'erreur qui implémente le trait Error standard. Cette conversion automatique vous permet d'utiliser l'opérateur point d'interrogation avec différents types d'erreur sans conversion manuelle, ce qui la rend particulièrement utile pour les applications où vous n'avez pas besoin de faire une distinction programmatique entre les différents types d'erreur.


Bien que `anyhow` soit excellent pour simplifier la gestion des erreurs dans les applications où les erreurs sont principalement affichées aux utilisateurs, il a des limites dans le développement de bibliothèques. Puisque `anyhow` convertit essentiellement toutes les erreurs en messages de type chaîne de caractères, les utilisateurs de votre bibliothèque ne peuvent pas facilement répondre de manière programmatique aux différentes conditions d'erreur. Cette limitation rend `anyhow` plus adapté aux applications des utilisateurs finaux qu'aux bibliothèques qui ont besoin de fournir des informations d'erreur structurées à leurs utilisateurs.


Des approches plus avancées de gestion des erreurs impliquent la création de types d'erreurs personnalisés qui modélisent les modes d'échec spécifiques de votre application ou de votre bibliothèque. Un modèle d'erreur bien conçu peut faire la distinction entre les entrées non valides (que l'appelant peut corriger), les erreurs d'exécution (qui peuvent être tentées à nouveau) et les défaillances permanentes (qui indiquent des bogues ou des conditions irrécupérables). Cette approche structurée permet aux utilisateurs de votre code de prendre des décisions intelligentes sur la manière de répondre aux différents types d'erreurs, qu'il s'agisse de réessayer des opérations, d'inviter les utilisateurs à saisir d'autres données ou de signaler des bogues aux développeurs.


## UniFFI, une passerelle entre les bibliothèques Rust et plusieurs langues


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Introduction à l'interface utilisateur et au développement multiplateforme


UniFFI est un outil permettant de rendre les bibliothèques Rust accessibles à travers de multiples langages de programmation et plateformes. Développé par Mozilla, cet outil répond à un défi fondamental dans le développement de logiciels modernes : comment tirer parti des avantages de Rust en termes de performance et de sécurité tout en maintenant la compatibilité avec divers écosystèmes de développement. L'outil génère automatiquement des liaisons linguistiques pour les bibliothèques Rust, ce qui évite aux développeurs de créer manuellement un code d'interface pour chaque langue cible.


Le problème central résolu par UniFFI provient de la nature de Rust en tant que langage compilé. Lorsque le code Rust est compilé, il produit une sortie binaire avec une fonction étrangère Interface (FFI) qui présente une interface de bas niveau qui peut être difficile à utiliser directement à partir de langages de plus haut niveau comme Python, Swift ou Kotlin. Traditionnellement, chaque développeur de bibliothèque devrait écrire un code de liaison personnalisé pour chaque langage cible, ce qui crée un obstacle important à l'adoption multiplateforme. UniFFI élimine cette redondance en fournissant une approche standardisée pour générer ces bindings automatiquement.


La philosophie de conception de l'outil est centrée sur le fait de permettre aux développeurs Rust de se concentrer sur leur logique commerciale de base tout en rendant leurs bibliothèques accessibles aux développeurs travaillant dans d'autres langages. Un développeur iOS utilisant Swift, par exemple, peut consommer une bibliothèque Rust par le biais de bindings générés par UniFFI qui présentent une interface Swift entièrement native, sans aucune indication que l'implémentation sous-jacente est écrite en Rust. Cette intégration transparente permet aux équipes de tirer parti des avantages de Rust en termes de performances sans que tous les membres de l'équipe soient obligés d'apprendre Rust.


### Comprendre l'architecture et le flux de travail de l'interface utilisateur unique


L'interface utilisateur unifiée fonctionne selon un processus bien défini qui transforme les bibliothèques Rust en paquets compatibles avec plusieurs langues. Le processus commence par la création d'un fichier UDL (Unified Definition Language), qui sert de spécification d'interface décrivant les parties de votre bibliothèque Rust qui doivent être exposées à d'autres langues. Ce fichier UDL fait office de contrat entre votre implémentation Rust et les liaisons linguistiques générées.


L'architecture suit une séparation claire des préoccupations. Les développeurs maintiennent leur bibliothèque Rust avec les idiomes et les modèles Rust standard, puis créent un fichier UDL séparé qui fait correspondre l'interface publique au système de types de l'UniFFI. Le générateur de liens UniFFI traite à la fois la bibliothèque Rust et la spécification UDL afin de produire des liens en langage natif pour les plates-formes cibles demandées. Les liaisons générées gèrent toutes les opérations complexes d'échange de données entre le système d'exécution en langue étrangère et le code Rust.


Au moment de l'exécution, l'architecture crée une approche en couches où le code d'application écrit dans le langage cible (tel que Kotlin pour Android) interagit avec le code de liaison généré qui semble entièrement natif de ce langage. Cette couche de liaison gère la traduction entre les types spécifiques à la langue et les types Rust, gère la mémoire en toute sécurité à travers les frontières linguistiques et fournit une gestion des erreurs qui suit les conventions de la langue cible. La logique commerciale sous-jacente de Rust reste inchangée et n'est pas consciente des multiples interfaces linguistiques construites au-dessus d'elle.


### Travailler avec l'UDL : Interface Définition et correspondance des types


Le langage de définition unifié (UDL) est la pierre angulaire de la fonctionnalité de l'interface utilisateur unifiée. Il fournit un moyen déclaratif de spécifier les parties d'une bibliothèque Rust qui doivent être exposées et la manière dont elles doivent être présentées dans les langues cibles. Les fichiers UDL doivent contenir au moins un espace de noms, qui sert de conteneur pour les fonctions qui peuvent être appelées directement sans nécessiter l'instanciation d'un objet. Ces fonctions de l'espace de noms gèrent généralement des opérations simples qui prennent des valeurs en paramètre et renvoient des résultats.


L'UDL prend en charge un ensemble complet de types intégrés qui correspondent naturellement aux types Rust. Les types de base comprennent des primitives standard comme les booléens, différentes tailles d'entiers (u8, u32, etc.), des nombres à virgule flottante et des chaînes de caractères. Les types plus complexes comprennent les vecteurs, les cartes de hachage et les concepts spécifiques à Rust comme les types Option (représentés avec une syntaxe de point d'interrogation) et les types Result pour la gestion des erreurs. Le système de types prend également en charge les énumérations, qu'il s'agisse d'énumérations simples basées sur des valeurs ou d'énumérations complexes contenant des données associées, ce qui permet de modéliser les données au-delà des frontières linguistiques.


Les structures dans Rust se traduisent par des dictionnaires dans UDL, en maintenant une correspondance quasi univoque tout en s'adaptant aux conventions syntaxiques d'UDL. Lorsque les structs Rust ont des méthodes associées, elles peuvent être exposées en tant qu'interfaces en UDL, qui generate sont des classes avec des méthodes dans les langages cibles orientés objet comme Kotlin ou Swift. Ce mappage préserve les modèles de conception orientés objet que les développeurs attendent dans ces langages tout en conservant la structure et le comportement de l'implémentation Rust sous-jacente.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


L'implémentation Rust correspondante définirait ces types et implémenterait l'attribut `uniffi::export` dans les bindings generate pour Kotlin, Swift, Python, et les autres langages supportés.


### Gestion des erreurs et fonctionnalités avancées


L'interface UniFFI propose une gestion des erreurs qui préserve le modèle d'erreur basé sur les résultats de Rust tout en le traduisant de manière appropriée pour les langues cibles. Les fonctions qui renvoient des types Result dans Rust peuvent être marquées avec le mot-clé "throws" dans UDL, en spécifiant les types d'erreurs qu'elles peuvent produire. Ces erreurs doivent être définies comme des enums d'erreurs dans le fichier UDL et doivent implémenter le trait Error standard de Rust dans le code Rust sous-jacent. La classe thiserror fournit une macro pratique pour implémenter ce trait, ce qui réduit considérablement le code de base.


La traduction de la gestion des erreurs démontre l'approche de l'UniFFI qui tient compte du langage. En Kotlin, les fonctions marquées comme "throwing" dans l'UDL generate sont des méthodes qui lancent des exceptions selon les conventions Java/Kotlin. Les bindings Python utilisent de la même manière le modèle d'exception de Python. Cette traduction garantit que la gestion des erreurs est naturelle et idiomatique dans chaque langue cible, tout en préservant la signification sémantique des types d'erreur Rust originaux.


Les interfaces de rappel représentent une autre caractéristique avancée qui permet une communication bidirectionnelle entre les bibliothèques Rust et les applications consommatrices. Lorsqu'une bibliothèque Rust doit rappeler le code d'une application, les développeurs peuvent définir des traits dans la Rust et les marquer comme interfaces de rappel dans l'UDL. L'application consommatrice implémente ces interfaces dans son langage natif, et l'interface UniFFI gère le marshaling complexe nécessaire pour invoquer ces rappels à partir du code Rust. Ce modèle nécessite une attention particulière à la sécurité des threads, car les callbacks peuvent traverser les frontières des threads, ce qui nécessite des limites Send et Sync du côté de la Rust.


### Applications réelles et limites actuelles


L'interface utilisateur unique a été adoptée par la communauté de développement des crypto-monnaies et des blockchains, avec des projets majeurs tels que BDK (kit de développement Bitcoin), LDK (kit de développement Lightning), et diverses implémentations wallet qui l'utilisent pour fournir des SDK mobiles. Ces projets démontrent l'utilisation de l'UniFFI dans des environnements de production.


L'examen des fichiers UDL réels de ces projets révèle des modèles et des meilleures pratiques issus de l'utilisation pratique. Le fichier UDL de BDK, par exemple, montre comment des modèles de domaine complexes avec de multiples enums, structures et interfaces peuvent être efficacement mappés pour créer des SDK mobiles complets. La cohérence de la syntaxe UDL entre les différents projets signifie que les développeurs familiarisés avec une bibliothèque compatible UniFFI peuvent rapidement comprendre et travailler avec d'autres, créant ainsi un effet de réseau qui profite à l'ensemble de l'écosystème.


Cependant, l'interface UniFFI présente des limites notables que les développeurs doivent prendre en compte. La plus importante est l'absence de prise en charge des interfaces asynchrones. Toutes les liaisons générées sont synchrones, ce qui oblige les développeurs à gérer les opérations asynchrones dans leur code Rust et à présenter des interfaces synchrones aux applications consommatrices. En outre, le placement de la documentation pose un problème : la documentation écrite dans le code Rust n'est pas transférée aux liaisons générées, tandis que la documentation contenue dans les fichiers UDL n'est pas disponible pour les consommateurs directs de la bibliothèque Rust. Bien que des efforts soient actuellement déployés pour remédier à ces limitations par le biais de l'analyse et de la génération automatiques, elles restent des aspects à prendre en compte dans les implémentations actuelles. Enfin, UniFFI génère des liaisons linguistiques mais ne s'occupe pas de l'emballage et de la distribution spécifiques à la plate-forme, laissant les développeurs gérer les étapes finales de la création de paquets distribuables pour chaque plate-forme cible.


# Développement de LNP/BP avec SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## Nœud LN sur le SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### Comprendre l'architecture modulaire de LDK


Le kit de développement Lightning (LDK) adopte une approche différente de la mise en œuvre Lightning Network par rapport aux logiciels de nœuds traditionnels tels que CLightning ou LND. Alors que les nœuds Lightning conventionnels fonctionnent comme des applications daemon complètes s'exécutant en continu sur une machine, le LDK fonctionne comme une bibliothèque Rust modulaire qui fournit des composants primitifs pour construire des solutions Lightning personnalisées. Cette distinction architecturale rend LDK flexible, permettant aux développeurs d'assembler les fonctionnalités de Lightning de manière à répondre aux exigences spécifiques de leur projet.


La philosophie de base de LDK est axée sur la modularité et l'adaptabilité. Plutôt que de fournir une solution monolithique, LDK propose des composants individuels qui peuvent être combinés, personnalisés ou remplacés entièrement. Chaque composant est livré avec des implémentations par défaut qui fonctionnent dans la boîte, mais les développeurs conservent la liberté de substituer leurs propres implémentations lorsque cela est nécessaire. Par exemple, LDK inclut des implémentations par défaut pour la surveillance de la blockchain, la signature des transactions et la communication réseau, mais chacune d'entre elles peut être remplacée par des solutions personnalisées adaptées à des cas d'utilisation ou à des environnements spécifiques.


Cette conception modulaire permet au LDK de fonctionner sur diverses plates-formes et dans des scénarios qui seraient difficiles pour les nœuds Lightning traditionnels. Les applications mobiles, les navigateurs web, les appareils embarqués et le matériel spécialisé peuvent tous exploiter les composants de LDK en fonction de leurs contraintes et exigences particulières. L'architecture de la bibliothèque garantit que les développeurs peuvent créer des applications compatibles avec Lightning sans être enfermés dans des modèles opérationnels prédéterminés ou des dépendances de système.


### Cas d'utilisation du LDK et flexibilité de la plateforme


La flexibilité architecturale de LDK ouvre la voie à de nombreux cas d'utilisation qui vont bien au-delà des déploiements traditionnels de nœuds Lightning. Le développement du wallet mobile représente l'une des applications les plus convaincantes, où LDK permet la création de portefeuilles Lightning non conservateurs similaires au Phoenix wallet. Ces implémentations mobiles peuvent maintenir le contrôle de l'utilisateur sur les clés privées tout en se synchronisant avec les fournisseurs de services Lightning (LSP) lors de la mise en ligne, ce qui permet une réception des paiements et une gestion des canaux transparentes, même en cas de connectivité intermittente.


L'intégration du module de sécurité matériel (HSM) illustre un autre cas d'utilisation puissant pour LDK. En extrayant uniquement les composants de signature et de vérification des transactions, les développeurs peuvent créer des dispositifs de signature conscients de Lightning qui comprennent le contexte et les implications des transactions Lightning. Cette capacité va au-delà de la simple signature de transaction pour inclure une analyse intelligente de la transmission des paiements, des opérations de canal et des décisions critiques en matière de sécurité. Le HSM peut évaluer si une transaction représente un paiement légitime, une opération de routage ou une tentative potentiellement malveillante, fournissant ainsi aux utilisateurs des informations significatives en matière de sécurité.


Les applications Lightning basées sur le Web bénéficient considérablement de la philosophie de conception sans appel système de LDK. Étant donné que les environnements WebAssembly n'ont pas d'accès direct aux ressources système telles que les systèmes de fichiers, les sockets réseau ou les sources d'entropie, l'approche pure de LDK permet à la fonctionnalité Lightning de fonctionner de manière transparente dans les environnements de navigation. Les développeurs peuvent mettre en œuvre des couches réseau personnalisées à l'aide de WebSockets et fournir des sources de persistance et d'aléa compatibles avec les navigateurs, tout en conservant une conformité totale au protocole Lightning.


### Composants de base et architecture pilotée par les événements


L'architecture interne de LDK s'articule autour de plusieurs composants clés qui fonctionnent ensemble par le biais d'un système piloté par les événements. Le système de gestion des pairs gère toutes les communications avec d'autres nœuds Lightning, en mettant en œuvre le protocole de bruit pour le cryptage et en gérant les structures de message pour la conformité au protocole Lightning. Ce composant fonctionne indépendamment du mécanisme de transport sous-jacent, ce qui permet aux développeurs de mettre en place un réseau via des sockets TCP, des WebSockets, des connexions série USB ou tout autre canal de communication bidirectionnel.


Le gestionnaire du canal sert de coordinateur central pour les opérations du canal Lightning, travaillant en étroite collaboration avec le gestionnaire des pairs pour exécuter les opérations d'ouverture, de fermeture et de paiement du canal. Lorsqu'un développeur lance l'ouverture d'un canal, le gestionnaire de canal crée les messages de protocole nécessaires et se coordonne avec le gestionnaire de pairs pour gérer le processus de négociation en plusieurs étapes. Cette séparation des préoccupations permet une abstraction nette entre la logique du protocole Lightning et les détails de la communication réseau.


Le système d'événements de LDK fournit des notifications asynchrones pour toutes les opérations importantes et les changements d'état. Les événements couvrent tout le spectre des opérations Lightning, des connexions et déconnexions de pairs aux succès et échecs de paiement, aux changements d'état des canaux et aux confirmations de la blockchain. Cette approche événementielle permet aux applications de répondre de manière appropriée à l'activité du réseau Lightning tout en maintenant une séparation nette entre la fonctionnalité principale de LDK et la logique propre à l'application. Les développeurs peuvent mettre en œuvre des gestionnaires d'événements personnalisés qui mettent à jour les interfaces utilisateur, déclenchent des notifications ou initient des actions de suivi basées sur les événements du réseau Lightning.


### Blockchain Intégration et gestion des données


L'intégration des données Blockchain représente l'une des couches d'abstraction de LDK, conçue pour s'adapter à tout, des nœuds Bitcoin complets aux clients mobiles légers. LDK prend en charge deux modes principaux d'interaction avec la blockchain, chacun étant optimisé pour des contraintes de ressources et des exigences opérationnelles différentes. Le mode bloc complet permet aux applications ayant accès aux données complètes de la blockchain de transmettre des blocs entiers à LDK, ce qui permet une surveillance complète des transactions et une réponse immédiate aux événements pertinents de la blockchain.


Pour les environnements aux ressources limitées, LDK propose une approche basée sur le filtrage qui réduit les besoins en bande passante et en stockage. Dans ce mode, LDK communique ses intérêts en matière de surveillance par le biais d'interfaces abstraites, en demandant la surveillance d'ID de transaction, d'UTXO ou de modèles de script spécifiques. La couche applicative peut alors mettre en œuvre cette surveillance à l'aide de serveurs Electrum, d'explorateurs de blocs ou d'autres sources de données légères de la blockchain. Cette approche permet aux portefeuilles mobiles et aux applications web de conserver la fonctionnalité Lightning sans nécessiter une synchronisation complète de la blockchain.


La couche de persistance de LDK suit les mêmes principes d'abstraction, en fournissant aux applications des blocs de données binaires qui doivent être stockés et récupérés de manière fiable. LDK gère toute la complexité de la sérialisation et de la désérialisation des états du canal Lightning, des données sur les potins du réseau et d'autres informations critiques. Les applications doivent simplement mettre en œuvre des mécanismes de stockage fiables, que ce soit à l'aide de systèmes de fichiers locaux, de services de stockage en nuage ou de systèmes de base de données spécialisés. Cette conception garantit que la gestion des états Lightning reste robuste tout en permettant aux applications de choisir des solutions de stockage qui correspondent à leurs exigences opérationnelles et à leurs modèles de sécurité.


### Fonctionnalités avancées et modèles d'intégration


Les capacités de LDK s'étendent aux caractéristiques du Lightning Network, telles que les paiements à chemins multiples, l'optimisation des itinéraires et la gestion des ragots du réseau. Le système de routage conserve une vue d'ensemble de la topologie du Lightning Network grâce à la participation au protocole de commérage, ce qui permet de trouver des chemins intelligents pour les paiements. Les applications peuvent influencer les décisions de routage par le biais de paramètres de configuration et peuvent même mettre en œuvre une logique de routage personnalisée pour des cas d'utilisation spécialisés.


Le système de liaison linguistique de la bibliothèque permet l'intégration du LDK dans plusieurs environnements de programmation, prenant en charge Java, Kotlin, Swift, TypeScript, JavaScript et C++. Cette compatibilité multiplateforme permet aux applications mobiles écrites dans des langages natifs d'intégrer les fonctionnalités de Lightning tout en conservant des caractéristiques de performance optimales. Le système de liaison préserve l'architecture événementielle et la conception modulaire de LDK dans tous les langages pris en charge, ce qui garantit des expériences cohérentes pour les développeurs, quelle que soit la plateforme cible.


L'estimation des frais et la diffusion des transactions sont d'autres domaines dans lesquels LDK offre de la flexibilité. Les applications peuvent mettre en œuvre des stratégies d'estimation des frais personnalisées qui tiennent compte de leurs modèles opérationnels spécifiques et des exigences des utilisateurs. De même, la diffusion des transactions peut être personnalisée pour fonctionner avec diverses interfaces réseau Bitcoin, des connexions full node directes aux services de diffusion tiers. Cette flexibilité garantit que les applications basées sur le LDK peuvent optimiser leurs interactions avec la blockchain pour leurs cas d'utilisation particuliers tout en maintenant la conformité au protocole Lightning et les normes de sécurité.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### Le défi du développement de la foudre


Le développement d'applications intégrant les paiements Lightning représente un obstacle important pour la plupart des développeurs. Pour créer une application dotée d'une fonctionnalité de paiement Lightning, les développeurs doivent essentiellement devenir des experts Lightning et comprendre des concepts complexes tels que la gestion des canaux, l'équilibrage des liquidités et la topologie du réseau. Cette exigence d'expertise crée un problème fondamental pour l'adoption de Lightning : alors que le réseau Lightning lui-même est opérationnel et que les paiements sont fiables, la complexité technique empêche une intégration généralisée dans les applications quotidiennes.


Le principal défi réside dans l'écart entre les besoins des développeurs et ce qu'ils souhaitent obtenir. Les développeurs travaillent généralement dans des délais serrés et préfèrent des solutions simples qui leur permettent de se concentrer sur la fonctionnalité principale de leur application plutôt que de devenir des experts de l'infrastructure de paiement. Lorsque l'intégration de Lightning est difficile, les développeurs s'orientent naturellement vers des solutions de conservation parce qu'elles offrent la voie de la moindre résistance. Cependant, cette tendance aux services de garde sape la proposition de valeur fondamentale de Bitcoin, à savoir la souveraineté financière sans garde.


### La vision de Breez, des éclairs partout


Breez est née d'une vision simple mais ambitieuse : connecter tout le monde au réseau Lightning grâce à des interfaces intuitives permettant d'accéder à l'économie Lightning. L'approche de l'entreprise reconnaît que si le réseau Lightning fonctionne bien d'un point de vue technique, il a désespérément besoin d'être adopté par les utilisateurs pour atteindre son plein potentiel. Ce défi de l'adoption va au-delà des utilisateurs individuels et englobe l'ensemble de l'écosystème des applications et des services qui pourraient bénéficier de l'intégration de Lightning.


L'application originale Breez a illustré cette vision en fournissant aux utilisateurs un nœud Lightning non gardien fonctionnant directement sur leur téléphone portable. Cette application présentait des fonctionnalités Lightning telles que la diffusion de micropaiements aux podcasteurs et la fonctionnalité de point de vente. Cependant, l'application Breez a également révélé une limitation architecturale critique : l'écosystème des applications mobiles ne facilite pas la communication entre les applications, ce qui oblige les développeurs à intégrer toutes les fonctionnalités liées à Lightning dans une seule application plutôt que de permettre aux applications spécialisées de tirer parti de l'infrastructure Lightning partagée.


Les enseignements tirés par l'entreprise de l'application Breez ont permis de dégager une idée cruciale : l'avenir de l'adoption de Lightning dépend de la conquête des développeurs. Si l'intégration de Lightning sans dépôt devient l'option la plus facile pour les développeurs, elle deviendra le choix par défaut. Cette approche présente également des avantages sur le plan réglementaire, car les logiciels non dépositaires sont confrontés à moins d'obstacles réglementaires que les services dépositaires, ce qui permet aux développeurs d'expédier plus facilement leurs applications à l'échelle mondiale.


### Architecture du SDK Breez


Le SDK Breez offre une approche alternative pour l'intégration de la fonctionnalité Lightning dans les applications. Plutôt que d'exiger que chaque application exécute son propre nœud Lightning, le SDK propose une architecture qui maintient les principes de non-détention tout en simplifiant l'expérience du développeur. À la base, le SDK permet à chaque utilisateur final d'avoir son propre nœud Lightning personnel fonctionnant sur l'infrastructure Greenlight, le service d'hébergement de nœuds Lightning basé sur le nuage de Blockstream.


Cette architecture résout simultanément plusieurs problèmes critiques. Les utilisateurs n'ont pas à se préoccuper de la gestion des bases de données, de la disponibilité des serveurs ou de la maintenance de l'infrastructure - des préoccupations qui seraient accablantes pour les consommateurs typiques. Cependant, contrairement aux solutions de garde traditionnelles, Greenlight n'a jamais accès aux clés des utilisateurs. Le nœud Lightning dans le nuage ne peut effectuer aucune opération sans une application activement connectée qui peut signer les transactions et les messages. Cette conception maintient les avantages de sécurité de l'autodétention tout en éliminant la complexité opérationnelle.


Le SDK prend également en charge l'interopérabilité. Plusieurs applications peuvent se connecter au nœud Lightning d'un même utilisateur à l'aide de la même phrase seed, ce qui permet aux utilisateurs de conserver un seul solde Lightning dans différentes applications spécialisées. Par exemple, un utilisateur peut avoir à la fois une application Lightning wallet générale et une application de podcasting spécialisée, toutes deux accédant aux mêmes fonds et aux mêmes canaux Lightning. Cette architecture permet de développer des applications spécialisées et ciblées tout en maintenant une infrastructure financière unifiée.


### Les fournisseurs de services éclair et la liquidité en temps réel


Un élément essentiel du SDK Breez est son intégration avec les fournisseurs de services Lightning (LSP), qui fonctionnent de manière analogue aux fournisseurs de services Internet, mais pour le réseau Lightning. Les LSP résolvent l'un des défis les plus complexes de Lightning : la gestion des liquidités. Dans les canaux Lightning, les fonds ne peuvent circuler que dans les directions où il y a des liquidités, un peu comme des billes sur un boulier qui ne peuvent se déplacer que là où il y a de la place.


Le SDK met en œuvre des canaux "juste à temps" par l'intermédiaire des PSL, gérant automatiquement les liquidités sans intervention de l'utilisateur. Lorsqu'un utilisateur a besoin de recevoir un paiement mais qu'il ne dispose pas de liquidités suffisantes, le FSL ouvre automatiquement un nouveau canal Lightning au moment où le paiement arrive. Ce processus se déroule de manière transparente en arrière-plan, garantissant que les utilisateurs peuvent toujours recevoir des paiements sans comprendre les mécanismes sous-jacents du canal.


Cette intégration des PSL va au-delà de la simple gestion des liquidités. Le SDK comprend d'emblée une fonctionnalité Lightning complète : services de tour de guet intégrés pour la sécurité, interopérabilité on-chain par le biais de swaps sous-marins, accès aux devises par le biais de services tels que MoonPay, et prise en charge des protocoles LNURL. Le système assure également une sauvegarde et une récupération transparentes, garantissant que les utilisateurs ne perdent jamais l'accès à leurs fonds, même si les fournisseurs d'infrastructure changent ou deviennent indisponibles.


### Expérience de la mise en œuvre et des développeurs


Le SDK Breez donne la priorité à l'expérience des développeurs grâce à son approche complète, batteries incluses. Le SDK fournit des liaisons pour plusieurs langages de programmation, notamment Rust, Swift, Kotlin, Python, Go, React Native, Flutter et C#, ce qui permet aux développeurs d'intégrer les paiements Lightning à l'aide de leurs outils de développement préférés. L'architecture fait abstraction de la complexité de Lightning par le biais d'API tout en maintenant la sécurité du réseau Lightning.


Des composants clés travaillent ensemble pour offrir cette expérience simplifiée. L'analyseur d'entrée traite automatiquement les différents formats de paiement, en déterminant si une chaîne représente une facture, un LNURL ou une autre méthode de paiement et en l'acheminant vers la fonction de traitement appropriée. Le signataire intégré gère toutes les opérations cryptographiques en arrière-plan, tandis que l'échangeur gère les interactions on-chain de manière transparente. Cette conception permet aux développeurs de se concentrer sur la proposition de valeur unique de leur application plutôt que de devenir des experts de l'infrastructure Lightning.


L'architecture sans confiance du SDK garantit que si Greenlight peut observer les états des canaux et les informations de routage, il ne peut pas accéder aux fonds des utilisateurs ou effectuer des opérations non autorisées. Les utilisateurs conservent le contrôle total de leurs clés privées, qui ne quittent jamais leurs appareils. Cette approche représente un compromis soigneusement étudié entre la simplicité opérationnelle et la confidentialité, offrant une voie pratique pour l'adoption générale de Lightning tout en préservant les principes fondamentaux de la souveraineté financière de Bitcoin.


## LDK vs Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Comprendre les limites du kit de développement Lightning (LDK)


Le kit de développement Lightning est un ensemble de bibliothèques Rust conçues pour offrir aux développeurs une certaine flexibilité lors de la création d'applications Lightning Network. Toutefois, cette flexibilité s'accompagne d'importants défis de mise en œuvre qui sont apparus lors du développement en conditions réelles à Lipa. La nature de bas niveau du LDK signifie que les développeurs doivent traiter de nombreuses tâches complexes de manière indépendante, de la synchronisation des graphes de réseau à l'optimisation du routage des paiements. Bien que cette approche offre un contrôle total sur la mise en œuvre de Lightning, elle nécessite des ressources de développement considérables et une expertise technique approfondie pour obtenir une fiabilité prête à la production.


L'une des fonctionnalités manquantes les plus importantes de LDK était la prise en charge de LNURL, une norme largement adoptée qui simplifie les interactions Lightning Network pour les utilisateurs finaux. En outre, l'absence de sorties d'ancrage posait de sérieux problèmes opérationnels, en particulier dans les environnements où les frais sont élevés. Les sorties Anchor résolvent un problème fondamental lié aux fermetures forcées des canaux Lightning : lorsque les frais de réseau augmentent considérablement, il peut devenir impossible de fermer unilatéralement les canaux dont les frais sont prédéfinis, car les frais prédéfinis ne suffisent plus à confirmer les transactions. Cette limitation s'est avérée particulièrement problématique pour les applications mobiles wallet, où les utilisateurs peuvent abandonner la wallet sans coordonner les fermetures de canaux coopératifs, laissant des fonds potentiellement bloqués pendant les pics de frais.


La relative immaturité du LDK s'est également traduite par un manque de fiabilité dans l'acheminement des paiements, un problème critique pour toute application Lightning. Bien qu'il s'agisse d'une implémentation techniquement solide, la vaste portée du LDK en tant que solution générique a rendu difficile la résolution rapide de problèmes spécifiques. L'équipe de développement a passé un temps considérable à résoudre des problèmes de routage et à mettre en œuvre des fonctionnalités qui devraient idéalement être gérées au niveau de la bibliothèque, ce qui a finalement eu un impact sur la vitesse de développement et la qualité de l'expérience utilisateur.


### Découvrir les avantages du SDK Breez et de Greenlight


La transition vers le SDK Breez a représenté un changement d'approche architecturale, passant d'un nœud Lightning autogéré à une solution basée sur le cloud et alimentée par le service Greenlight de Blockstream. Ce changement a permis de résoudre immédiatement plusieurs problèmes critiques rencontrés lors de la mise en œuvre du SDK. L'amélioration la plus significative a concerné la fiabilité des paiements, principalement grâce à la capacité de Greenlight à maintenir un graphe de réseau toujours à jour. Contrairement aux implémentations mobiles traditionnelles de Lightning qui doivent synchroniser les informations de réseau au démarrage de l'application, les nœuds de Greenlight fonctionnent en continu dans le nuage, conservant une connaissance du réseau en temps réel et fournissant instantanément des données de graphe complètes lorsque les utilisateurs se connectent.


Cette architecture s'appuie sur l'implémentation éprouvée de Core Lightning (CLN), qui assure avec succès le routage des paiements depuis des années en tant que l'une des implémentations originales de Lightning Network. L'expérience accumulée et la fiabilité éprouvée de CLN ont permis d'améliorer immédiatement la stabilité par rapport au projet LDK plus jeune. Lorsque les utilisateurs activent leur wallet alimenté par Greenlight, ils héritent instantanément de toute la connaissance du réseau et des capacités de routage d'un nœud Lightning fonctionnant en continu, ce qui élimine les retards de synchronisation et les incertitudes de routage qui affectaient l'implémentation précédente.


La philosophie de conception du SDK Breez, basée sur les opinions, a été utile pour le développement de wallet. Plutôt que de fournir une boîte à outils Lightning générique, Breez se concentre spécifiquement sur les applications wallet destinées aux utilisateurs finaux, ce qui permet à l'équipe de développement de concentrer ses efforts sur la création de solutions complètes pour ce cas d'utilisation spécifique. Cette approche ciblée a permis à Breez d'intégrer des services essentiels directement dans le SDK, y compris la fonctionnalité Lightning Service Provider (LSP) qui permet aux utilisateurs de recevoir des paiements immédiatement après l'installation de wallet, sans nécessiter de procédures manuelles d'ouverture de canaux.


### Fonctionnalités complètes et amélioration de l'expérience utilisateur


L'approche intégrée du SDK Breez va au-delà de la fonctionnalité Lightning de base, en incorporant des caractéristiques qui améliorent l'expérience de l'utilisateur. L'intégration des FSL élimine l'obstacle traditionnel consistant à exiger des utilisateurs qu'ils comprennent la gestion des canaux, ce qui permet la réception immédiate des paiements pour les nouvelles installations wallet. Ce processus d'embarquement contribue à l'adoption générale, car les utilisateurs peuvent commencer à recevoir des paiements Lightning sans aucune connaissance technique ou procédure de configuration.


La fonctionnalité de swap en chaîne fournit une autre couche d'optimisation de l'expérience utilisateur en permettant la présentation d'un solde unifié aux utilisateurs. Plutôt que d'obliger les utilisateurs à comprendre la distinction entre Lightning et on-chain Bitcoin, le service de swap permet une conversion automatique entre ces couches selon les besoins. Lorsque les utilisateurs ont besoin d'effectuer des paiements en on-chain, le système peut échanger en toute transparence des fonds Lightning contre des fonds on-chain Bitcoin en coulisses, ce qui permet de maintenir l'illusion d'un solde unique et liquide tout en gérant la complexité technique en interne.


La prise en charge par le SDK des réserves de canal nulles répond à un problème d'expérience utilisateur important dans les implémentations traditionnelles de Lightning. Les réserves de canaux empêchent généralement les utilisateurs de dépenser la totalité de leur solde affiché, ce qui crée une confusion lorsque les paiements échouent malgré des fonds apparemment suffisants. En éliminant ces réserves, la Breez permet aux utilisateurs de dépenser l'intégralité de leur solde affiché, bien que le LSP doive pour cela accepter un risque supplémentaire. Ce compromis illustre l'approche centrée sur l'utilisateur de Breez, où la complexité technique et le risque sont absorbés par les fournisseurs de services afin de créer des expériences intuitives pour les utilisateurs.


Des fonctionnalités supplémentaires telles que la prise en charge de LNURL, les services de taux de change et la synchronisation multi-appareils démontrent l'approche globale du SDK pour le développement de wallet. L'architecture basée sur le cloud permet aux utilisateurs d'accéder à leur nœud Lightning à partir de plusieurs appareils ou applications, Breez se chargeant de la synchronisation des états entre ces différents points d'accès. Les futurs éléments de la feuille de route comprennent la fonctionnalité "spend-all" pour le drainage complet du wallet, l'épissage pour la gestion dynamique des canaux, et une place de marché de LSP concurrents pour introduire une saine concurrence dans la fourniture de services.


### Évaluation des compromis et des problèmes de centralisation


La transition vers le SDK Breez et Greenlight introduit d'importants compromis de centralisation qui doivent être soigneusement pris en compte dans le contexte des principes de décentralisation de Bitcoin. L'architecture basée sur le nuage signifie que les nœuds Lightning des utilisateurs fonctionnent sur l'infrastructure de Blockstream, créant des dépendances à la fois sur le fonctionnement continu de Greenlight et sur le développement continu de Breez. Cette centralisation va au-delà de la simple commodité, car elle peut avoir un impact sur la capacité des utilisateurs à récupérer leurs fonds en cas d'indisponibilité des services ou de censure.


Les scénarios de récupération présentent des défis particuliers dans cette architecture. Bien que les utilisateurs conservent le contrôle de leurs clés privées, l'accès aux fonds sans l'infrastructure de Greenlight nécessiterait une expertise technique pour démarrer des nœuds Core Lightning indépendants et restaurer les états des canaux. Pour les utilisateurs individuels, ce processus de récupération s'avérerait probablement trop complexe, et même les fournisseurs wallet seraient confrontés à des difficultés considérables pour migrer des bases d'utilisateurs entières vers une infrastructure alternative si les services de Greenlight étaient interrompus.


Les considérations relatives à la protection de la vie privée évoluent également avec ce changement d'architecture. Le routage basé sur le cloud signifie que Greenlight peut potentiellement avoir une visibilité sur les destinations des paiements, alors que les architectures précédentes basées uniquement sur les LSP limitaient les fuites d'informations aux montants et au calendrier des paiements. La génération de Invoice dans le nuage élargit encore l'exposition potentielle à l'information, car les factures inutilisées qui restaient auparavant privées sur les appareils des utilisateurs passent maintenant par l'infrastructure de Blockstream.


Malgré ces problèmes de centralisation, les avantages pratiques l'emportent souvent sur les risques théoriques pour de nombreux cas d'utilisation. La fiabilité accrue, l'ensemble des fonctionnalités et l'expérience utilisateur supérieure permettent aux développeurs de wallet de se concentrer sur les innovations de la couche applicative plutôt que sur la gestion de l'infrastructure Lightning. Cette répartition des tâches est le reflet d'un écosystème en pleine maturation, dans lequel des fournisseurs de services spécialisés s'occupent de défis techniques complexes, ce qui permet aux développeurs d'applications de se concentrer sur l'expérience utilisateur et la logique d'entreprise. L'essentiel est de comprendre clairement ces compromis et de prendre des décisions éclairées en fonction des exigences des cas d'utilisation spécifiques et des niveaux de tolérance au risque.




# Section finale

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Critiques et évaluations

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusion

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>