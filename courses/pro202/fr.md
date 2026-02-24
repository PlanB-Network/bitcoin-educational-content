---
name: Programmation Bitcoin
goal: Construire une bibliothèque Bitcoin complète à partir de zéro et comprendre les fondements cryptographiques de Bitcoin
objectives: 

 - Mettre en œuvre l'arithmétique des corps finis et les opérations sur les courbes elliptiques en Python
 - Construire et analyser les transactions Bitcoin de manière programmatique
 - Créer des adresses testnet et diffuser des transactions sur le réseau
 - Maîtriser les fondements mathématiques du modèle de sécurité Bitcoin

---
# Un voyage dans les scripts et les programmes de Bitcoin


Ce cours intensif de deux jours, enseigné par Jimmy Song, vous plonge dans les fondements techniques de Bitcoin en construisant une bibliothèque Bitcoin complète à partir de la base. En commençant par les mathématiques essentielles des champs finis et des courbes elliptiques, vous progresserez dans l'analyse des transactions, l'exécution des scripts et la communication réseau. Grâce à des exercices de codage pratiques dans des carnets Jupyter, vous créerez votre propre adresse testnet, construirez des transactions manuellement et les diffuserez directement sur le réseau, tout en acquérant une compréhension profonde des principes cryptographiques qui rendent le Bitcoin sûr et sans confiance.


Bon voyage !


+++

# Introduction


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Aperçu du cours


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Bienvenue au cours PRO 202 _**Programmation Bitcoin**_, un voyage intensif qui vous emmène de l'arithmétique des champs finis jusqu'à la construction et la diffusion de transactions réelles sur Bitcoin's Testnet.


Dans ce cours, vous construirez progressivement une bibliothèque Bitcoin en Python tout en acquérant les bases cryptographiques, protocolaires et logicielles nécessaires pour raisonner précisément sur la sécurité et le fonctionnement interne de Bitcoin. L'approche PRO 202 est totalement pratique : chaque concept est immédiatement mis en œuvre dans des carnets Jupyter, garantissant que la théorie et le code se renforcent l'un l'autre.


### Concepts mathématiques essentiels pour Bitcoin


Cette première section pose les bases mathématiques indispensables. Vous mettrez en œuvre l'arithmétique des corps finis et les opérations sur les courbes elliptiques (loi de groupe, addition, doublement, multiplication scalaire...), les prérequis de l'ECDSA. L'objectif est double : comprendre la structure algébrique qui rend possible les signatures cryptographiques et construire des outils Python fiables pour les manipuler.


Vous formaliserez ensuite les composants de l'ECDSA : génération de clés, formatage de points, hachage, création de signatures et vérification. Cette section relie directement la théorie à la pratique, en mettant l'accent sur les détails d'implémentation et la robustesse du modèle de sécurité sous-jacent.


### Fonctionnement interne de la transaction Bitcoin


Dans la deuxième section, vous décortiquerez la structure d'une transaction Bitcoin : UTXO, entrées/sorties, séquences, scripts, encodages, etc. Vous écrirez du code pour construire, signer et vérifier les transactions, en acquérant une compréhension précise de ce qui est engagé par le hachage et pourquoi.


Ensuite, vous mettrez en œuvre un exécuteur _Script_ minimal, examinerez les codes d'opération clés et validerez les chemins de dépenses. L'objectif est de vous rendre capable d'auditer le comportement des transactions, de diagnostiquer les échecs de validation et de raisonner sur la sécurité des politiques de dépenses.


### Fonctionnement interne du réseau Bitcoin


Dans la troisième section, vous placerez les transactions dans le cadre plus large du système : structure des blocs, en-têtes, difficultés et mécanisme Proof-of-Work. Vous manipulerez des messages de protocole, des en-têtes de blocs et des arbres de Merkle.


Enfin, vous étudierez la communication entre nœuds pair-à-pair, l'optimisation des messages et l'introduction de SegWit.


Comme pour tous les cours sur le Plan ₿ Academy, la dernière section comprend une évaluation destinée à consolider votre compréhension. Prêt à découvrir les rouages de Bitcoin et à écrire le code qui l'alimente ? C'est parti !










# Concepts mathématiques essentiels pour Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Mathématiques pour la mise en œuvre de Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Fondements de la programmation : Structures mathématiques de base


Ce cours condense les mathématiques essentielles derrière les systèmes cryptographiques de Bitcoin dans un flux de travail très pratique. Les concepts sont expliqués, démontrés à l'aide d'exemples, puis mis en œuvre dans Jupyter Notebook. L'idée directrice est simple : on ne comprend vraiment une primitive cryptographique qu'une fois qu'on l'a codée. Au cours des deux jours, les étudiants generate testnet addresses, construisent et diffusent des [transactions](https://planb.academy/resources/glossary/transaction-tx), et finalement interagissent avec le réseau sans explorateurs de blocs. Tout cela nécessite des bases solides en matière de champs finis et de courbes elliptiques.


### Champs finis : Le moteur arithmétique de la cryptographie


Un corps fini F(p) est un système arithmétique défini par un nombre premier p, contenant les éléments 0 à p-1. Les corps premiers garantissent que chaque élément non nul a un inverse et que toutes les opérations restent à l'intérieur du corps. L'arithmétique s'articule autour de l'utilisation de modulo p pour l'addition, la soustraction et la multiplication. La fonction Python `pow(base, exp, mod)` permet une exponentiation modulaire efficace, cruciale pour les grands exposants utilisés dans les opérations cryptographiques réelles.


#### Comportement multiplicatif

La multiplication de tout élément non nul k par tous les éléments d'un champ de nombres premiers produit une permutation du champ. Cette propriété garantit l'uniformité et prévient les faiblesses structurelles, ce qui rend les champs de nombres premiers idéaux pour la génération de clés sécurisées et les [signatures numériques](https://planb.academy/resources/glossary/digital-signature).


#### Division et petit théorème de Fermat

La division est mise en œuvre par le biais d'inverses multiplicatifs. Le petit théorème de Fermat stipule que

n^(p-1) ≡ 1 (mod p),

donc l'inverse est n^(p-2). Python le supporte directement avec `pow(n, -1, p)`. Ces opérations apparaissent constamment dans les routines cryptographiques sous-jacentes de l'[ECDSA](https://planb.academy/resources/glossary/ecdsa) et du Bitcoin.


### Courbes elliptiques : Structures non linéaires pour la sécurité des clés publiques


Les courbes elliptiques suivent l'équation y² = x³ + ax + b. Bitcoin utilise secp256k1, définie comme y² = x³ + 7 sur un corps fini. Les points d'une courbe elliptique forment un groupe mathématique sous addition de points. Une ligne tracée à partir de deux points P et Q coupe la courbe en un troisième point R ; la réflexion de R sur l'axe des x donne P + Q. Ce système est associatif et comprend un élément d'identité : le point à l'infini.

Le doublement d'un point utilise une ligne tangente au lieu d'une ligne sécante, la pente étant dérivée de la dérivée de la courbe. Bien que ces formules fassent appel au calcul sur les nombres réels, elles deviennent totalement discrètes et exactes lorsque la courbe est définie sur un corps fini - le contexte utilisé dans Bitcoin.


### Des mathématiques à la cryptographie Bitcoin


Les champs finis fournissent une arithmétique déterministe et inversible ; les courbes elliptiques fournissent une structure non linéaire où le calcul de k·P est facile mais où l'inversion est infaisable. La combinaison de ces deux éléments constitue la base des clés publiques/privées de Bitcoin, des signatures ECDSA et de la sécurité des transactions. La compréhension de ces principes fondamentaux prépare les étudiants à mettre en œuvre les clés, les transactions et les signatures directement, sans abstractions ni outils externes.


## Cryptographie à courbe elliptique

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Ce chapitre présente les courbes elliptiques définies sur des corps finis et explique pourquoi elles constituent l'épine dorsale mathématique de la [cryptographie](https://planb.academy/resources/glossary/cryptography) Bitcoin. Alors que les courbes elliptiques sur les nombres réels semblent lisses et continues, l'application des mêmes équations sur un corps fini crée un ensemble de points discrets et dispersés. Malgré la différence visuelle, toutes les formules d'addition de points, les pentes et les règles algébriques se comportent exactement de la même manière, seule l'arithmétique se transforme en arithmétique modulaire. Bitcoin utilise la courbe y² = x³ + 7 (secp256k1), qui préserve la symétrie et le comportement non linéaire essentiels à la sécurité cryptographique.


### Vérification des points et mise en œuvre des champs finis


Un point se trouve sur une courbe elliptique à champ fini si ses coordonnées satisfont l'équation de la courbe sous modulo p. Pour vérifier un point tel que (73,128) sur F₁₃₇, il faut vérifier que y² mod p est égal à x³ + 7 mod p. Pour mettre cela en œuvre dans le code, il faut créer des classes pour les éléments du champ fini et les points de la courbe. La surcharge des opérateurs garantit que toute l'arithmétique - addition, multiplication, exponentiation, division - est automatiquement effectuée modulo p. Une fois que ces abstractions existent, les opérations cryptographiques plus avancées deviennent simples à écrire et à raisonner.


#### Propriétés des groupes et addition de points

Les points de la courbe elliptique forment un groupe mathématique sous addition. Ce groupe satisfait aux conditions de fermeture, d'associativité, d'identité (le point à l'infini) et d'inversion (réflexion sur l'axe des x). Les constructions géométriques confirment ces propriétés, rendant la multiplication scalaire (P ajouté à lui-même de façon répétée) bien définie. Ces règles de groupe permettent la cryptographie à courbe elliptique et garantissent un comportement cohérent et prévisible en cas d'opérations répétées sur les points.


### Groupes cycliques et problème du logarithme discret


Le choix d'un point générateur G sur une courbe nous permet de générer un groupe cyclique : G, 2G, 3G, ..., nG = 0. Les points apparaissent non linéaires et imprévisibles, même lorsqu'ils sont générés de manière séquentielle. Cette imprévisibilité est à la base du problème du logarithme discret : il est facile de calculer P = sG, mais il est impossible de déterminer s à partir de P pour les grands groupes. C'est cette fonction à sens unique qui assure la sécurité de la cryptographie à clé publique. Les scalaires ([clés privées](https://planb.academy/resources/glossary/private-key)) sont écrites en minuscules, les points ([clés publiques](https://planb.academy/resources/glossary/public-key)) en majuscules.


#### Multiplication scalaire efficace

Pour calculer efficacement sG, les implémentations utilisent l'algorithme de double ajout : elles analysent la représentation binaire du scalaire, doublent le point à chaque étape et n'ajoutent G que lorsque le bit est à 1. Cela réduit le calcul de O(n) additions à O(log n), ce qui permet des opérations cryptographiques pratiques même avec des scalaires de 256 bits.


#### La courbe secp256k1 chez Bitcoin


Bitcoin utilise la courbe secp256k1, définie par y² = x³ + 7 sur un corps premier où p = 2²⁵⁶ - 2³² - 977. Le point générateur G a des coordonnées fixes choisies en utilisant une procédure déterministe NUMS ("nothing up my sleeve"). L'ordre du groupe n est un grand nombre premier proche de 2²⁵⁶, ce qui garantit que chaque point non nul génère le même groupe. La taille de 2²⁵⁶ (~10⁷⁷) est astronomique, ce qui rend le brute force des clés privées physiquement impossible. Même un trillion de superordinateurs fonctionnant pendant un trillion d'années ne réduirait pas de manière significative l'espace des clés.


### Clés publiques, clés privées et sérialisation SEC


La clé privée est un scalaire aléatoire s ; la clé publique est P = sG. La résolution du problème du logarithme discret étant infaisable, P peut être partagé sans révéler s. Les clés publiques doivent être sérialisées pour être transmises au moyen du format SEC. Le format SEC non compressé utilise 65 octets : préfixe 0x04 + coordonnées x + coordonnées y. Le format compressé n'utilise que 33 octets. Le format compressé n'utilise que 33 octets : préfixe 0x02 ou 0x03 (selon la parité de y) + coordonnée x. Bitcoin utilisait à l'origine des clés non compressées, mais préfère désormais les clés compressées pour des raisons d'efficacité.


#### Bitcoin Address Création


Les adresses Bitcoin sont des hachages de clés publiques, et non les clés brutes elles-mêmes. Pour obtenir une adresse générée, il faut sérialiser la clé publique au format SEC, calculer le hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256) puis RIPEMD-160), ajouter le préfixe du réseau (0x00 pour mainnet, 0x6F pour testnet), calculer une somme de contrôle en utilisant le double de SHA-256, ajouter les quatre premiers octets de la somme de contrôle et encoder le résultat en utilisant Base58. Ce codage supprime les caractères ambigus et inclut la somme de contrôle pour éviter les erreurs de transcription. Le pipeline en plusieurs étapes cache la clé publique jusqu'à ce qu'une dépense se produise, ajoute l'identification du réseau et garantit des adresses lisibles par l'homme et résistantes aux erreurs.


# Fonctionnement interne de la transaction Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Analyse des transactions et signatures ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Comprendre l'ECDSA : la fondation de la signature numérique de Bitcoin


Le Bitcoin s'appuie sur l'ECDSA, un système de signature basé sur la courbe elliptique qui offre une grande sécurité avec des tailles de clés beaucoup plus petites que le RSA. Sa sécurité provient du problème du logarithme discret de la courbe elliptique : étant donné P = eG, il est facile de calculer eG, mais dériver e à partir de P est infaisable sur le plan informatique. Cette asymétrie permet la cryptographie à clé publique tout en préservant la sécurité des clés privées.


#### Encodage DER des signatures ECDSA


Le Bitcoin encode les signatures ECDSA en utilisant le format DER :


- 0x30 (marqueur de séquence)
- longueur octet
- 0x02 + longueur + R octets
- 0x02 + longueur + S octets


Cela ajoute une surcharge, faisant passer une signature de 64 octets à environ 71-72 octets. [Taproot](https://planb.academy/resources/glossary/taproot) élimine cette inefficacité en adoptant des signatures [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol) de taille fixe.


### Engagements de signature et processus de signature


Les signatures ECDSA reposent sur une équation d'engagement : UG + VP = KG. Le signataire sélectionne des valeurs U et V non nulles, ainsi qu'un [nonce](https://planb.academy/resources/glossary/nonce) aléatoire K, prouvant ainsi qu'il connaît la clé privée sans la révéler. Le message est haché en Z, un K aléatoire est généré, R est la coordonnée x de KG et S = (Z + RE)/K. La signature est la paire (R, S). La sécurité dépend essentiellement de l'utilisation d'un K unique et imprévisible : si K est réutilisé ou fuit, la clé privée est compromise. Les implémentations modernes utilisent la génération déterministe de K (RFC 6979) pour éviter les défaillances du RNG.


#### Vérification de la signature

Étant donné Z, (R, S) et la clé publique P, le vérificateur calcule U = Z/S et V = R/S, puis vérifie si la coordonnée x de UG + VP est égale à R. Cela fonctionne parce que l'algèbre de vérification reconstruit KG sans avoir besoin de la clé privée. Pour falsifier des signatures, il faudrait résoudre le problème du logarithme discret ou casser la fonction de hachage.


#### Signatures Schnorr et contexte historique


Les signatures Schnorr sont mathématiquement plus propres et prennent en charge les fonctions d'agrégation, mais elles étaient brevetées au moment du lancement de Bitcoin. L'ECDSA offrait une alternative gratuite, mais avec plus de complexité et des signatures plus grandes. Les brevets ayant expiré, Bitcoin a ajouté les signatures Schnorr via Taproot, fournissant des signatures fixes de 64 octets et améliorant la confidentialité. L'ECDSA reste prise en charge pour des raisons de compatibilité.



### Structure des transactions et entrées/sorties


Une transaction Bitcoin consiste en


- version (4 octets, little-endian)
- liste des entrées
- liste des sorties
- locktime (4 octets)


Les entrées font référence aux [UTXO](https://planb.academy/resources/glossary/utxo) précédentes par leur numéro de transaction et leur index de sortie, et comprennent un [script](https://planb.academy/resources/glossary/script) de déverrouillage (scriptSig) et un numéro de séquence utilisé pour les timelocks ou RBF. Les sorties précisent le montant (8 octets) et le script de verrouillage (scriptPubKey), définissant les conditions de dépense. Les adresses Bitcoin sont des représentations de ces scripts.


#### Le modèle UTXO

Le Bitcoin suit les produits non dépensés plutôt que les soldes des comptes. Les UTXO doivent être dépensés entièrement - les dépenses partielles sont impossibles. Pour dépenser 1 BTC d'un UTXO de 100 BTC, une transaction doit inclure une sortie de changement. L'oubli de la sortie de changement transforme le reste en frais de [minage](https://planb.academy/resources/glossary/mining).


#### Sérialisation et analyse des transactions


Les transactions utilisent un format binaire compact. Après le champ de la version, un varint code le nombre d'entrées. Les entrées comprennent :


- hachage tx précédent (32 octets)
- index de sortie (4 octets)
- scriptSig (varstr)
- séquence (4 octets)


Les sorties comprennent un montant de 8 octets et le scriptPubKey (varstr). Le temps de blocage détermine le moment où la transaction devient valide. La sérialisation utilise l'ordre little-endian pour la plupart des entiers. Les analyseurs consomment les octets de manière séquentielle et délèguent à des classes spécialisées pour les entrées, les sorties et les scripts.


### Frais, changement et malléabilité


Les frais sont implicites :

fee = somme(valeurs d'entrée) - somme(valeurs de sortie).

Toute valeur non attribuée devient un droit, ce qui rend essentielle la construction d'une sortie de changement correcte. Avant [SegWit](https://planb.academy/resources/glossary/segwit), les signatures permettaient la malléabilité - modifier S en N-S produisait une nouvelle transaction valide avec un ID différent. Le Bitcoin applique désormais une règle de faible S, et SegWit isole les signatures du calcul de la txid, ce qui rend les ID stables et permet des protocoles de deuxième couche comme [Lightning](https://planb.academy/resources/glossary/lightning-network).


## Bitcoin Validation des scripts et des transactions

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script est un petit langage de contrat intelligent basé sur une pile qui définit comment les pièces peuvent être dépensées. Chaque sortie porte un scriptPubKey (script de verrouillage) et chaque entrée porte un scriptSig (script de déverrouillage). Ensemble, ils forment un programme qui doit être évalué à "vrai" pour que la dépense soit valide. Le script n'est volontairement pas Turing-complet afin que tous les chemins d'exécution soient prévisibles et faciles à valider sur le réseau.


### Opérations de script et modèle d'exécution


Un script est une séquence d'éléments de données et d'opcodes. Les poussées de données (signatures, clés publiques, hachages) sont placées sur la pile, tandis que les opcodes commençant par `OP_` transforment la pile. Après l'exécution, l'élément supérieur de la pile doit être différent de zéro pour que le script aboutisse. Exemples : `OP_DUP` duplique l'élément supérieur, `OP_HASH160` applique SHA256 puis RIPEMD160, et `OP_CHECKSIG` vérifie une signature par rapport au sighash de la transaction et à une clé publique, en poussant 1 pour valide, 0 pour invalide. Les règles d'analyse font la distinction entre les données brutes (longueur préfixée) et les opcodes (recherchés par valeur d'octet), et une petite machine virtuelle les exécute de manière déterministe sur chaque [nœud](https://planb.academy/resources/glossary/node).


### P2PK et P2PKH : modèles de paiement de base


Le premier modèle, Pay-to-Public-Key (P2PK), verrouille les pièces directement sur une clé publique complète : le scriptPubKey est `<pubkey> OP_CHECKSIG`, et le scriptSig est juste une signature. Il est simple mais peu encombrant et expose la clé publique avant que les pièces ne soient dépensées.


#### P2PKH et adresses

Pay-to-Public-Key-Hash (P2PKH) améliore cela en se verrouillant sur un hachage de 20 octets de la clé publique. Le scriptPubKey est `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, et le scriptSig fournit `<signature> <pubkey>`. L'exécution vérifie que la clé publique fournie est hachée à la valeur engagée, puis vérifie la signature. Cela permet de cacher la clé publique jusqu'au moment de la dépense, de réduire la taille et de correspondre au format d'adresse familier "1..." Format d'adresse mainnet familier.


### Validation des transactions et hachage des signatures


Un nœud validant une transaction doit s'assurer que

1) Chaque entrée fait référence à une sortie existante et non dépensée.

2) La valeur totale des intrants ≥ la valeur totale des extrants (la différence est la redevance).

3) Chaque scriptSig déverrouille correctement le scriptPubKey à laquelle il fait référence.


La vérification de la signature nécessite la construction du message exact qui a été signé, appelé sighash. Pour l'ancien ECDSA, la validation vide tous les scriptSig, remplace le scriptSig de l'entrée courante par le scriptPubKey correspondante, ajoute un type de hachage de 4 octets (habituellement `SIGHASH_ALL`), et double le hachage du résultat. Cette valeur de 256 bits est celle utilisée par `OP_CHECKSIG`. D'autres types de hachage (par exemple, `SINGLE`, `NONE`, avec ou sans `ANYONECANPAY`) changent les parties de la transaction qui sont engagées, permettant des cas d'utilisation de niche comme le financement collaboratif ou les transactions partiellement spécifiées, mais ils sont rarement utilisés dans la pratique.


#### Hachage quadratique et SegWit

Étant donné que chaque entrée d'une transaction héritée nécessite son propre calcul du sighash sur une structure qui comprend toutes les entrées, le temps de validation peut augmenter de façon quadratique avec le nombre d'entrées. Les grandes transactions à entrées multiples entraînaient autrefois des retards de validation notables. SegWit a repensé le calcul du sighash pour mettre en cache les parties partagées et réduire la complexité à un temps linéaire, améliorant ainsi l'évolutivité et rendant plus difficiles les attaques par déni de service.


### Casse-tête de script et leçons de sécurité


Les scripts peuvent exprimer bien plus qu'un simple "une signature déverrouille ces pièces". Les puzzles Script le démontrent en encodant des conditions arbitraires - problèmes mathématiques, défis de préimage de hachage, ou même primes de collision - où quiconque fournit les données correctes peut dépenser les pièces. Cependant, les résultats qui reposent uniquement sur des données publiques (pas de signatures) sont vulnérables au minage en amont : une fois qu'une solution valide apparaît dans le [mempool](https://planb.academy/resources/glossary/mempool), n'importe quel [mineur](https://planb.academy/resources/glossary/miner) peut la copier et rediriger le paiement à son profit.


La leçon pratique est que les contrats du monde réel comprennent presque toujours des contrôles de signature, même lorsqu'ils contiennent une logique plus complexe telle que le multisig, les timelocks ou les hashlocks. Les signatures lient la solution à une partie spécifique, préservant les incitations et empêchant les autres de voler le paiement. Comprendre le modèle de pile de Script, les modèles standard et les pièges subtils est essentiel pour concevoir des contrats intelligents Bitcoin sécurisés et pour raisonner sur la façon dont les transactions sont réellement validées sur le réseau.


## Construction de transactions et Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Construction des transactions Bitcoin et P2SH


La construction des transactions Bitcoin fait le lien entre la connaissance théorique du protocole et la mise en œuvre pratique. Une transaction sélectionne les UTXO à dépenser, construit des sorties avec des scripts de verrouillage, crée des signatures pour chaque entrée et sérialise le tout dans le format exact attendu par les nœuds. Le processus nécessite de comprendre la génération de sighash, le comportement des scripts et la gestion correcte des frais et des changements.


### Construction d'une transaction de base


Chaque entrée de transaction fait référence à une sortie précédente par txid et index. Les sorties spécifient des montants en satoshis et des scripts de verrouillage. La différence entre le total des entrées et le total des sorties correspond aux frais. Pour signer une entrée, une version modifiée de la transaction est sérialisée, son sighash est calculé et la clé privée la signe. La signature résultante et la clé publique forment le ScriptSig. Une fois que chaque entrée est signée, la transaction brute peut être diffusée sur le réseau.


### Transactions multi-signatures


Bare multisig utilise `OP_CHECKMULTISIG` pour exiger m-de-n signatures. En raison d'un bug précoce, OP_CHECKMULTISIG consomme un élément de pile supplémentaire, nécessitant un `OP_0` initial dans le ScriptSig. Le multisig nu est fonctionnel mais inefficace : toutes les clés publiques apparaissent on-chain, ce qui rend les scriptPubKeys volumineux, coûteuses et difficiles à coder en tant qu'adresses. Ces limitations ont motivé l'introduction du pay-to-script-hash.


#### Architecture P2SH

P2SH cache les scripts complexes derrière un HASH160 de 20 octets. La clé scriptPubKey est fixe : `OP_HASH160 <20-byte hash> OP_EQUAL`. Le script de rédemption sous-jacent, qui contient du multisig, des timelocks ou d'autres conditions, n'est révélé et exécuté qu'au moment de la dépense. L'expéditeur ne voit que le hachage, tandis que le destinataire gère le script de rachat en privé. Cette conception réduit la taille on-chain, améliore la confidentialité et permet de conclure des contrats complexes sans alourdir le fardeau des expéditeurs.


### Dépenses et mise en œuvre du P2SH


Pour dépenser une sortie P2SH, le ScriptSig doit inclure les données de déverrouillage nécessaires *plus* le script de rédemption lui-même. La validation se fait en deux étapes :

1) HASH160(redeem_script) doit correspondre au hash scriptPubKey.

2) Après vérification, le script de rachat est exécuté avec les données fournies.


Lorsqu'il génère des signatures pour une entrée P2SH, le processus sighash utilise le script redeem à la place de la clé scriptPubKey. Chaque signataire doit posséder le script de rachat complet pour que les signatures générées soient valides. Les adresses P2SH utilisent l'octet de version 0x05 sur mainnet (adresses "3...") et 0xC4 sur testnet (adresses "2...").


#### Considérations pratiques sur la sécurité


La perte d'un script de rachat signifie la perte de fonds : les dépenses nécessitent à la fois les clés privées et le script de rachat lui-même. Les participants à la multisig doivent vérifier que leurs clés publiques sont correctement incluses avant d'accepter des dépôts. P2SH supporte des constructions avancées comme le multisig, les timelocks et les hashlocks, mais les erreurs dans la logique du script peuvent bloquer les fonds de façon permanente, c'est pourquoi il est essentiel de tester sur testnet.

La P2SH améliore la confidentialité en masquant les conditions de dépense jusqu'à la première dépense, mais une fois que le script de remboursement apparaît on-chain, il devient visible en permanence. Malgré cela, les avantages de la taille réduite, de la rétrocompatibilité et de la prise en charge de contrats flexibles ont fait de la P2SH une étape majeure, qui a influencé les mises à jour ultérieures telles que la SegWit et la Taproot.


# Fonctionnement interne du réseau Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Blocs Bitcoin et Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Les [blocs](https://planb.academy/resources/glossary/block) Bitcoin regroupent les transactions et les sécurisent à l'aide de [proof-of-work](https://planb.academy/resources/glossary/proof-of-work). Chaque bloc comprend un [en-tête](https://planb.academy/resources/glossary/block-header) de 80 octets et une liste de transactions. Malgré le coût énergétique élevé de la production d'un bloc valide, sa vérification est peu coûteuse : le stockage de l'ensemble des quelque 900 000 en-têtes ne nécessite que 72 Mo, ce qui permet même aux petits appareils de vérifier efficacement le proof of work de la chaîne.


### Transactions Coinbase et Block Rewards


Chaque bloc commence par une [transaction Coinbase](https://planb.academy/resources/glossary/coinbase-transaction), la seule façon pour les nouveaux bitcoins d'entrer en circulation. Il possède un hachage prev-tx réduit à zéro et un index de 0xffffffff, qui l'identifie de manière unique. La subvention a commencé à 50 BTC et diminue de moitié tous les 210 000 blocs (50, 25, 12,5, 6,25, 3,125, ...). Les mineurs incluent également des frais de transaction. Le nonce de 4 octets étant trop petit pour les ASIC modernes, les mineurs modifient les données dans la transaction Coinbase pour changer la racine de [Merkle](https://planb.academy/resources/glossary/merkle-tree) et créer un espace de recherche supplémentaire. Le [BIP](https://planb.academy/resources/glossary/bip)34 exige l'intégration de la hauteur du bloc dans le scriptSig de Coinbase afin de garantir que chaque txid de Coinbase est unique.


### Champs d'en-tête de bloc et signalisation Soft Fork


L'en-tête de 80 octets contient


- version (4 octets)
- hachage du bloc précédent (32 octets)
- racine de Merkle (32 octets)
- horodatage (4 octets)
- bits (cible de [difficulté](https://planb.academy/resources/glossary/difficulty), 4 octets)
- nonce (4 octets)


Les numéros de version ont évolué vers un système de signalisation par champ binaire via le BIP9, permettant aux mineurs de coordonner l'état de préparation du [soft-fork](https://planb.academy/resources/glossary/soft-fork). L'horodatage est une valeur temporelle Unix de 32 bits et devra être mis à jour autour de l'année 2106.


#### Champ de bits et cibles

Le champ "bits" code la cible sous forme compacte : cible = coefficient × 256^(exposant-3). Les hachages de blocs valides doivent être numériquement inférieurs à cette cible. Les hachages étant interprétés comme des entiers de grands taille, les hachages valides apparaissent souvent avec de nombreux zéros de fin lorsqu'ils sont affichés en hexadécimal.


### Difficulté, validation et ajustements


La difficulté est définie comme la cible la plus basse / la cible actuelle, ce qui indique à quel point le mining est plus difficile aujourd'hui par rapport à la difficulté la plus facile possible. La validation ne nécessite que la comparaison du hachage de l'en-tête avec la cible - extrêmement bon marché par rapport au mining.


Tous les blocs de 2016, Bitcoin ajuste la difficulté pour cibler des intervalles de blocs d'environ 10 minutes. L'ajustement compare le temps réel des 2016 blocs précédents avec les deux semaines prévues. Les limites limitent les ajustements à un facteur de quatre. Des événements majeurs du monde réel, tels que l'interdiction du mining en Chine, ont démontré la résilience de ce mécanisme lorsque le taux de hachage a chuté brusquement et que la difficulté a été ajustée à la baisse pour compenser.


### Subvention globale et total Supply


La subvention à la hauteur h est calculée comme suit : subvention = 5_000_000_000 >> (h // 210_000). On obtient ainsi le calendrier de réduction de moitié qui converge vers une offre totale de ~21 millions de BTC. La somme des séries géométriques (50 + 25 + 12,5 + ...) × 210 000 explique le plafond. Les mineurs peuvent demander moins que la subvention autorisée, mais jamais plus, sinon le bloc devient invalide. Au fur et à mesure que les subventions diminuent, les frais de transaction deviennent une composante de plus en plus importante des revenus des mineurs et de la sécurité à long terme du réseau.


## Communication en réseau et arbres de Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Architecture du réseau


Le réseau [pair-à-pair](https://planb.academy/resources/glossary/peertopeer-p2p) de Bitcoin fonctionne comme un système de rumeurs décentralisé dans lequel les nœuds relaient les transactions et les blocs sans se faire confiance. Les nouveaux nœuds s'amorcent en contactant des graines DNS codées en dur et gérées par les développeurs principaux. Ces graines DNS renvoient les adresses IP des pairs actifs, ce qui permet aux nœuds de découvrir le réseau et de demander des pairs supplémentaires via getaddr. Le réseau n'est intentionnellement pas critique pour le [consensus](https://planb.academy/resources/glossary/consensus), de sorte que les implémentations peuvent différer tant que les règles de consensus restent inchangées.


### Structure du message et poignée de main


Tous les messages Bitcoin P2P utilisent une enveloppe fixe : une valeur magique de 4 octets (F9BEB4D9 pour mainnet), une commande ASCII de 12 octets, une longueur de charge utile little-endian de 4 octets, une somme de contrôle de 4 octets (les 4 premiers octets de hash256), et la charge utile. Les commandes courantes sont version, verack, inv, getdata, tx, block, getheaders, headers, ping et pong.


La poignée de main commence lorsqu'un nœud de connexion envoie un message de version. Le destinataire répond avec verack et sa propre version. Une fois que les deux parties ont échangé ces deux messages, la connexion est active et les nœuds peuvent commencer à transmettre des inventaires et des données.


### Arbres de Merkle et racines de Merkle


Bitcoin stocke une racine Merkle unique de 32 octets dans l'en-tête de chaque bloc en tant qu'engagement pour toutes les transactions du bloc. Les transactions sont hachées (hash256), appariées, concaténées et hachées à plusieurs reprises jusqu'à ce qu'il ne reste plus qu'un seul [hachage](https://planb.academy/resources/glossary/hash-function). Lorsqu'un niveau a un nombre impair, le dernier hachage est dupliqué. En interne, les hachages sont big-endian, alors que les données sérialisées des blocs sont little-endian, ce qui nécessite des inversions avant et après la construction de l'arbre.


#### Preuves de Merkle et SPV

Les preuves de Merkle permettent de vérifier qu'une transaction est incluse dans un bloc sans télécharger le bloc entier. La preuve consiste en des hachages de frères et sœurs le long du chemin menant à la racine. Les clients SPV légers ne stockent que les en-têtes de blocs et demandent ces preuves aux [nœuds complets](https://planb.academy/resources/glossary/full-node). Étant donné qu'un arbre de Merkle croît de manière logarithmique, la preuve de l'inclusion dans un bloc contenant des milliers de transactions ne nécessite que quelques centaines d'octets.


Taproot étend ce concept en engageant les conditions de dépenses dans un arbre de script Merklized (MAST), ne révélant que la branche exécutée avec une preuve de Merkle. Cela améliore à la fois l'efficacité et la confidentialité.


### Fonctionnement du réseau et synchronisation des blocs


Les nœuds utilisent getdata pour demander des transactions ou des blocs, en spécifiant un ID de type (1=tx, 2=bloc, 3=bloc filtré, 4=bloc compact) plus un identifiant de 32 octets. Pour la synchronisation en chaîne, les nœuds envoient des getheaders avec un hachage de bloc de départ, et reçoivent jusqu'à 2000 en-têtes en réponse. Chaque en-tête renvoyé est composé de 80 octets suivis d'un nombre de transactions fictives égal à zéro.


La vérification complète des blocs reçus nécessite deux contrôles :

1. Le hachage du bloc doit être inférieur à la cible encodée dans le champ "bits".

2. La racine de Merkle calculée à partir de toutes les transactions (avec une gestion appropriée de l'endianness) doit correspondre à la racine de l'en-tête.


Ce n'est que si les deux conditions sont remplies qu'un nœud accepte le bloc, conformément au principe Bitcoin "ne faites pas confiance, vérifiez".


## Communication avancée entre nœuds et témoins séparés

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Cette session unifie la mise en réseau avancée P2P avec Segregated Witness, en montrant comment les logiciels Bitcoin modernes interagissent directement avec les nœuds tout en utilisant des structures de transaction compatibles avec SegWit. Les développeurs apprennent à récupérer des blocs, à rechercher des transactions pertinentes et à construire des transactions en utilisant uniquement la communication réseau brute - aucun explorateur de blocs n'est nécessaire.


### Recherche de transactions par blocs et protection de la vie privée


Les [portefeuilles](https://planb.academy/resources/glossary/wallet) doivent détecter les paiements entrants en analysant les blocs à la recherche de sorties correspondant à leur clé scriptPubKey. La récupération de blocs entiers protège mieux la vie privée que la demande de transactions individuelles, qui révèle des signaux forts sur l'activité de l'utilisateur. Même les demandes de blocs peuvent donner lieu à des fuites d'informations sur les chaînes à faible volume, ce qui rend les filtres de blocs compacts (BIP158) essentiels pour les clients légers préservant la confidentialité. Les filtres peuvent produire des faux positifs mais jamais de faux négatifs, ce qui permet aux clients de ne télécharger que les blocs potentiellement pertinents sans révéler d'adresses spécifiques.


### Trustless Interaction en réseau


Le flux de travail `get_block` démontre une utilisation correcte du réseau : envoyer getdata, recevoir un bloc, puis vérifier indépendamment sa racine Merkle et son proof of work. Un bloc n'est accepté que si le hachage de l'en-tête reçu correspond au hachage demandé et si la racine Merkle calculée correspond à l'en-tête. Cette méthode incarne le principe "ne pas faire confiance, vérifier", garantissant que même des pairs malveillants ne peuvent pas inciter les nœuds à accepter des données modifiées.


#### Récupération des transactions dans les blocs

Les transactions d'un bloc peuvent être analysées à la recherche de scriptPubKeys correspondantes par simple itération. Les portefeuilles de production effectuent cette opération en continu au fur et à mesure de l'arrivée de nouveaux blocs, en prouvant la propriété des résultats strictement par validation cryptographique plutôt qu'en s'appuyant sur des API tierces.


### SegWit Objectifs et conception


Le témoin séparé (SegWit) a corrigé la malléabilité des transactions en supprimant les données relatives à la signature dans le calcul de la txid. Cela a permis de créer des chaînes de transactions pré-signées fiables et de rendre la Lightning Network pratique. La SegWit a également augmenté la capacité des blocs en utilisant le "poids des blocs" : les anciens nœuds voient toujours des blocs de ≤1 Mo, tandis que les nœuds mis à niveau valident jusqu'à 4 Mo, y compris les données des témoins. Les programmes de témoins versionnés (v0-v1 jusqu'à présent) créent une voie de mise à niveau structurée pour les futurs types de scripts.


#### P2WPKH (Native SegWit)


P2WPKH remplace l'ancienne structure P2PKH par un script de 22 octets : OP_0 + push20 + hash160(pubkey). Spending déplace la signature et la clé publique dans un champ témoin séparé.


- Nœuds antérieurs à la SegWit : voir "n'importe qui peut dépenser", le considérer comme valide.
- Nœuds post-SegWit : reconnaissance de OP_0 + hachage de 20 octets et validation à l'aide de données témoins.


Cette séparation permet de corriger la malléabilité et de réduire les frais. Le témoin utilise un compte varint suivi de la signature et de la clé publique.


#### P2SH-P2WPKH (rétrocompatible SegWit)


Pour permettre aux anciens portefeuilles d'envoyer à des adresses SegWit, les scripts P2WPKH peuvent être enveloppés dans P2SH.


- scriptPubKey : standard P2SH hash160(redeemScript)
- scriptSig : le script de rédemption (le programme P2WPKH)
- témoin : signature + clé publique


Couches de validation :

1. Les nœuds antérieurs au BIP16 acceptent le redémarrage comme valide.

2. Les nœuds post-BIP16 l'évaluent, laissant OP_0 + hash sur la pile.

3. Les nœuds SegWit effectuent une validation complète des témoins.


#### P2WSH pour les scripts complexes


P2WSH généralise SegWit pour les scripts multisig et avancés en s'engageant sur SHA256(script) au lieu de hash160. Une pile de témoins multisig typique de 2 sur 3 :


- élément vide (bogue CHECKMULTISIG)
- sig1
- sig2
- le script témoin (le script multisig)


Les nœuds SegWit vérifient que SHA256(witnessScript) correspond au hachage scriptPubKey, puis l'exécutent. L'utilisation de SHA256 et d'un hachage de 32 octets permet de distinguer P2WSH de P2WPKH et de renforcer la sécurité.


#### P2SH-P2WSH (Compatibilité maximale)


Les scripts SegWit complexes peuvent également être enveloppés de P2SH :


- scriptSig : redeemScript (OP_0 + hachage de 32 octets)
- témoin : signatures + witnessScript


La validation passe par trois générations de règles, exactement comme avec P2SH-P2WPKH. Cette enveloppe était essentielle pour les premiers déploiements de Lightning qui nécessitaient une signature multiple sans malléabilité. Bien que le P2WSH natif soit préféré aujourd'hui, la forme enveloppée assure la compatibilité avec les anciens systèmes de wallet.


### L'impact du SegWit


SegWit fournit :


- les identifiants de transactions stables
- réduction des frais grâce à des données de témoins actualisées
- débit de blocs plus élevé grâce à la pondération des blocs
- compatibilité avec les anciens nœuds
- une voie de mise à niveau propre pour Taproot et les extensions futures


Ces outils, associés à une interaction réseau sans confiance, constituent l'épine dorsale du développement moderne de Bitcoin.



# Section finale


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Critiques et évaluations


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Examen final


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Conclusion



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>
