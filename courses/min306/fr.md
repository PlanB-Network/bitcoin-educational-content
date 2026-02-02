---
name:  Maîtrise du minage open source avec Bitaxe
goal: Maîtriser l'ensemble de l'écosystème Bitaxe, de l'assemblage du matériel à la personnalisation avancée et à l'optimisation des performances
objectives: 

  - Comprendre la philosophie du matériel de minage Bitcoin open source
  - Construire des appareils de minage Bitaxe à partir de zéro
  - Configurer et optimiser le logiciel de minage, y compris AxeOS et Public Pool
  - Mise en œuvre d'optimisations avancées des performances, y compris l'overclocking et le benchmarking

---

# Votre guide de minage avec Bitaxe 


Bienvenue dans le cours complet de Bitaxe, où vous maîtriserez le matériel révolutionnaire open source de minage bitcoin qui démocratise l'accès à la technologiede minage. Ce cours vous emmène de la compréhension des fondements philosophiques du minage décentralisé à la personnalisation avancée du matériel et aux techniques d'optimisation des performances.


Le projet Bitaxe représente un changement de paradigme dans le minage de bitcoin, brisant le monopole des fabricants de ASIC propriétaires en fournissant des conceptions, des micrologiciels et des logiciels entièrement libres. Ces chapitres pratiques vous permettront d'acquérir des compétences pratiques en matière d'assemblage de matériel, de configuration de logiciels, de conception de circuits imprimés et d'optimisation des performances.


Aucune expérience préalable de minage n'est requise, bien qu'une connaissance de base de l'électronique et une familiarité avec GitHub soient utiles. Ce cours vous fera passer du statut d'observateur curieux à celui de constructeur et contributeur Bitaxe compétent.


+++


# Introduction


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Aperçu du cours


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Bienvenue au cours MIN 306 _**Bitaxe Open Source Mining Mastery**_, un voyage complet dans le monde de minage avec Bitaxe. Ce cours est conçu pour ceux qui veulent comprendre, construire et optimiser leur propre matériel de minage Bitaxe tout en explorant les fondements philosophiques et techniques qui rendent ce projet unique au sein de l'écosystème Bitcoin.


### Comprendre Bitaxe


La première section pose les bases essentielles : vous découvrirez les origines du projet Bitaxe, son évolution, et les valeurs de décentralisation et de transparence qui le définissent. Vous apprendrez ce qu'est réellement un Bitaxe, en quoi il diffère des ASICs propriétaires, et où trouver les ressources de la communauté pour approfondir vos connaissances. Cette section fournit le contexte nécessaire pour comprendre pourquoi Bitaxe représente un tournant dans l'histoire du minage de bitcoin.


### Logiciels et opérations


La deuxième section se concentre sur l'environnement logiciel, avec une présentation détaillée de *AxeOS* : le système d'exploitation open source conçu spécifiquement pour les appareils Bitaxe. Vous apprendrez ses principales fonctionnalités et comment configurer et interagir avec votre appareil pour démarrer votre première opération de minage.


### Communauté et collaboration


La troisième section met en lumière l'aspect collaboratif du projet. Vous explorerez la philosophie open source appliquée au développement matériel et logiciel de Bitaxe. Au travers d'exercices pratiques, vous apprendrez à contribuer directement au code source, et vous découvrirez également _Public Pool_, une plateforme communautaire de mise en commun de la puissance de calcul. Vous apprendrez également à l'installer sur un nœud Umbrel pour une intégration locale et souveraine.


### Assemblage du matériel et dépannage


Dans la quatrième section, vous plongerez dans le matériel lui-même. Vous apprendrez à identifier les outils nécessaires à l'assemblage d'un Bitaxe, à résoudre les problèmes de soudure et à effectuer un diagnostic complet en utilisant *AxeOS* et les outils USB. Cette section met l'accent sur la pratique et une compréhension profonde de la façon dont les composants matériels et logiciels interagissent.


### Personnalisation avancée


La cinquième section est consacrée à la personnalisation. Vous apprendrez à modifier le PCB (circuit imprimé), à créer un fichier d'usine et à utiliser le _Bitaxe Web Flasher_. Cette section s'adresse à ceux qui veulent aller plus loin que le simple assemblage et véritablement concevoir des versions personnalisées de leur propre appareil.


### Optimisation des performances


Enfin, la sixième section couvre les techniques d'optimisation avancées. Vous apprendrez à benchmarker votre Bitaxe pour évaluer ses performances et à l'optimiser efficacement. Ces compétences vous aideront à tirer le meilleur parti de votre matériel tout en respectant ses limites physiques.


Comme pour tous les cours de Plan ₿ Academy, la section finale comprend une évaluation destinée à renforcer vos connaissances.


Plongez dans cette aventure technique — l'avenir du minage Bitcoin est entre vos mains !


# Comprendre Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## L'histoire

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Le projet Bitaxe représente un changement révolutionnaire dans le développement de matériel de minage de Bitcoin, apportant les principes de l'open source à une industrie dominée par les solutions propriétaires. Cette série éducative explore l'histoire complète, les innovations techniques et l'évolution de Bitaxe sous l'impulsion de la communauté, permettant de comprendre comment la vision d'un seul ingénieur s'est transformée en un écosystème florissant de matériel de minage décentralisé. En examinant les origines, les défis et les réalisations du projet, nous acquérons une compréhension précieuse à la fois des complexités techniques du développement ASIC et de la puissance de la collaboration open source dans l'espace Bitcoin.


### L'histoire des origines : De la découverte de Silk Road au Solar Mining Vision (La vision du minage solaire)


Skot, le fondateur de Bitaxe, a commencé son voyage dans le Bitcoin lors d'une soirée universitaire où il a appris l'existence du Bitcoin par l'intermédiaire de quelqu'un qui achetait des articles sur Silk Road. Ce premier contact avec le bitcoin à environ 20 dollars par pièce a éveillé une curiosité qui s'est transformée plus tard en un projet révolutionnaire de minage. Les bases techniques de son futur travail ont été établies pendant ses études universitaires, où il a eu accès à de vastes ressources FPGA en laboratoire. En collaboration avec son superviseur, Skot a commencé à expérimenter des flux de bits (flux binaires) FPGA open source pour le minage de bitcoins, initialement avec l'objectif modeste de miner suffisamment de Bitcoin pour acheter une pizza pour leur bureau.


Le passage de l'expérimentation académique au développement sérieux s'est produit des années plus tard, lorsque Skot travaillait sur des passerelles alimentées par l'énergie solaire pour la collecte de données à distance en Afrique. Cette expérience professionnelle avec les systèmes d'alimentation solaire lui a fait réaliser que les ASICs de minage de bitcoins, étant fondamentalement des dispositifs à courant continu basse tension, s'associeraient parfaitement avec les panneaux solaires. Le concept semblait naturel et élégant. Cependant, lorsque Skot a commencé à rechercher des solutions existantes, il a découvert une lacune importante sur le marché : contrairement aux débuts du minage de bitcoins, lorsque les conceptions FPGA étaient librement disponibles, l'avènement des ASICs a fait évoluer l'industrie vers des solutions complètement propriétaires et à code source fermée.


L'absence de matériel de minage open source est devenue une source de frustration pour Skot, notamment en raison de son expérience dans le développement de logiciels open source et de sa conviction que la nature open source de Bitcoin devrait s'étendre à son infrastructure de minage. Cet alignement philosophique sur les principes de l'open source, combiné au défi technique que représentait la rétro-ingénierie des conceptions propriétaires du ASIC, a ouvert la voie à ce qui allait devenir le projet Bitaxe. La vision initiale était ambitieuse, mais pratique : créer un mineur Bitcoin alimenté par l'énergie solaire qui pourrait fonctionner de manière indépendante sans nécessiter d'ordinateur distinct pour le contrôler, ce qui permettrait de le déployer dans des endroits éloignés sous des panneaux solaires.


### Défis techniques et avancées en matière de rétro-ingénierie


Le développement de Bitaxe a nécessité de surmonter d'importants obstacles techniques, principalement liés à l'absence totale de documentation sur les puces ASIC de Bitmain. L'approche de Skot face à ce défi illustre la détermination et l'ingéniosité nécessaires à une rétro-ingénierie réussie. Sans accès aux fiches techniques officielles ou aux spécifications techniques, il a dû examiner les puces au microscope, mesurer le pas des broches avec des pieds à coulisse et même scanner les puces pour déterminer leurs dimensions exactes. Ce processus minutieux a abouti à l'échec de plusieurs prototypes, les deux premières itérations du "day miner" ne fonctionnant pas correctement en raison de calculs erronés.


La percée s'est produite avec la troisième itération en mai 2022, lorsque Skot a réussi à créer un design fonctionnel à deux puces en utilisant des puces BM1387 récoltées sur des unités Antminer S9. Cette réussite a marqué la naissance du nom Bitaxe, inspiré par le concept d'une pioche de minage pour Bitcoin. Le succès de cette conception a validé l'approche de la rétro-ingénierie et a démontré que les développeurs indépendants pouvaient créer du matériel de minage fonctionnel sans l'aide du fabricant. Cependant, les défis techniques allaient au-delà de l'interfaçage des puces et incluaient la conception d'une alimentation électrique complexe, car les ASICs nécessitaient une régulation précise de la tension à des courants élevés, fonctionnant souvent à des tensions aussi basses que 0,6 volt tout en consommant une intensité importante.


Le développement du micrologiciel présentait un autre niveau de complexité, car le projet nécessitait la création d'un logiciel de minage pouvant fonctionner directement sur un microcontrôleur ESP32, plutôt que de dépendre d'ordinateurs externes exécutant des logiciels tels que CGMiner. Cette approche autonome était essentielle à la vision de Skot, qui souhaitait créer des unités de minage déployables et indépendantes. La combinaison de la rétro-ingénierie matérielle et du développement de microprogrammes intégrés a créé un défi technique complet qui a nécessité une expertise dans de nombreuses disciplines, de l'ingénierie électrique et de la conception de circuits imprimés à la programmation intégrée et aux protocoles de réseau.


### Formation de communautés et collaboration open source


La transformation de Bitaxe d'un projet solo en une initiative communautaire florissante représente l'un des aspects les plus significatifs de son succès. Au départ, les tentatives de Skot pour susciter l'intérêt par le biais des forums Bitcoin et des médias sociaux ont rencontré un accueil mitigé et parfois même du scepticisme. La percée s'est produite lorsque des membres de la communauté comme SirVapesAlot ont reconnu le potentiel du minage open source et ont créé le serveur Discord **Open Source Miners United** (OSMU). Cette plateforme a fourni l'environnement collaboratif nécessaire à l'épanouissement du projet, attirant des contributeurs d'horizons divers qui partageaient un intérêt commun pour la démocratisation de la technologie de minage de bitcoin.


Le modèle de développement communautaire s'est avéré remarquablement efficace, avec des contributeurs clés comme johnny9 et Ben qui ont émergé pour relever des défis techniques spécifiques. L'expertise de Johnny9 en matière de développement de micrologiciels a permis de résoudre des problèmes critiques d'implémentation de logiciels, tandis que les compétences de Ben en matière de développement front-end ont permis de créer le tableau de bord intuitif AxeOS qui a simplifié la configuration et la surveillance des appareils. Ben a également contribué à la mise en place de capacités de fabrication et à la création de Public Pool, un pool de minage open source optimisé pour les appareils Bitaxe. Cette approche collaborative a démontré comment les principes de l'open source pouvaient accélérer le développement au-delà de ce qu'un contributeur individuel pouvait réaliser seul.


La communauté OSMU a également favorisé un environnement inclusif où les nouveaux arrivants pouvaient apprendre et contribuer, quelle que soit leur expertise technique initiale. Le parcours de Ben, qui est passé du statut de novice en soudure à celui de grand fabricant, illustre cette approche accueillante du développement des compétences. L'engagement de la communauté en faveur de l'éducation et du soutien mutuel a créé un cercle vertueux dans lequel les membres expérimentés ont encadré les nouveaux venus, qui sont ensuite devenus eux-mêmes des contributeurs. Ce modèle s'est avéré essentiel pour étendre le projet au-delà de sa portée initiale et établir un écosystème durable pour une innovation et une croissance continues.


### Vision pour le minage décentralisé et son impact futur 

La vision à long terme de Skot pour Bitaxe va bien au-delà de la création d'un autre dispositif de minage : il s'agit d'une transformation fondamentale du paysage du minage de bitcoin. L'objectif ambitieux de produire un million de mineurs d'une puissance d'un térahash créerait une puissance de minage distribuée d'un exahash, ce qui représenterait une avancée significative vers la décentralisation du minage. Cette vision répond aux préoccupations majeures concernant la centralisation du minage, où les grands pools et les opérations industrielles pourraient potentiellement être soumis à des pressions gouvernementales ou à la réglementation. En répartissant la puissance de minage entre d'innombrables mineurs domestiques, le réseau devient plus résilient et s'aligne sur les principes décentralisés de Bitcoin.


Le modèle économique qui soutient cette vision repose sur les caractéristiques uniques du minage domestique, où les coûts d'infrastructure sont pratiquement nuls et où les mineurs peuvent opérer avec une supervision minimale. Contrairement aux opérations industrielles de minage qui nécessitent des investissements massifs dans des installations, des infrastructures électriques et des systèmes de refroidissement, les mineurs à domicile peuvent simplement brancher des appareils sur des prises électriques et des connexions Internet existantes. Cette approche pourrait théoriquement apporter un taux de hachage significatif en ligne sans les barrières traditionnelles à l'entrée qui caractérisent les opérations de minage à grande échelle.


Le succès du projet a déjà commencé à influencer l'écosystème du minage de bitcoin au sens large, et pourrait inspirer d'autres fabricants à adopter des modèles de développement open source. La viabilité financière démontrée par les fabricants de Bitaxe prouve que le matériel open source peut être un succès commercial tout en maintenant la transparence et l'implication de la communauté. Alors que le projet continue d'évoluer avec de nouvelles intégrations de puces, des conceptions améliorées et des partenariats de fabrication élargis, il sert de preuve de concept de la façon dont le minage de bitcoin peut revenir à ses racines décentralisées tout en adoptant la technologie moderne ASIC. L'objectif ultime va au-delà de la simple distribution du taux de hachage pour inclure un impact éducatif, en mettant davantage de personnes en contact direct avec le processus fondamental du minage de bitcoin et en encourageant une compréhension plus profonde du modèle de sécurité du réseau.


## Qu'est-ce que le Bitaxe ?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Vue d'ensemble du matériel et capacités


L'écosystème Bitaxe englobe de multiples itérations matérielles, chacune conçue pour optimiser différents aspects de l'expérience de minage tout en maintenant la philosophie de base de l'accessibilité open source. Ces appareils servent non seulement de matériel de minage fonctionnel, mais aussi d'outils pédagogiques permettant aux utilisateurs de comprendre la relation complexe entre les puces ASIC, les microcontrôleurs et le processus de minage de bitcoin. La compréhension de la philosophie de conception et de la mise en œuvre technique du Bitaxe fournit des informations précieuses sur la manière dont le matériel de minage moderne fonctionne à la fois au niveau des composants et des systèmes.



### Bitaxe Max, implémentation de première génération


Le Bitaxe Max représente l'implémentation fondamentale du concept Bitaxe, utilisant la puce ASIC BM1397 développée à l'origine par Bitmain pour sa série de minage S17. Cette intégration de puce démontre comment le matériel open source peut réutiliser la technologie ASIC existante pour créer des solutions de minage accessibles. Le Bitaxe Max offre un taux de hachage estimé entre 300 et 400 gigahashs par seconde, ce qui le positionne comme une plateforme de minage éducative et expérimentale plutôt que comme une solution à l'échelle commerciale.


L'intégration de la puce BM1397 dans le Bitaxe Max a nécessité un examen minutieux de la gestion de l'énergie, du contrôle thermique et des protocoles de communication. La conception de la carte répond aux exigences spécifiques de ce ASIC tout en fournissant les circuits de soutien nécessaires à un fonctionnement stable. Cette mise en œuvre montre comment le développement de matériel open source peut tirer parti de la technologie des semi-conducteurs existante pour créer de nouvelles applications et des opportunités d'apprentissage au sein de la communauté de minage.


### Bitaxe Ultra, technologie avancée des puces


Le Bitaxe Ultra représente l'évolution de la plateforme Bitaxe, incorporant la puce BM1366 ASIC plus avancée de la série S19 de Bitmain. Cette nouvelle technologie apporte à la plateforme Bitaxe une efficacité et des performances accrues, tout en conservant la même philosophie de conception fondamentale. La mise à niveau vers la puce BM1366 démontre l'adaptabilité de la plateforme et l'engagement de la communauté à incorporer les avancées technologiques dans les solutions de minage open source.


Le passage de la puce BM1397 à la puce BM1366 a nécessité des modifications des systèmes d'alimentation de la carte, de la gestion thermique et des algorithmes de contrôle. Ces changements illustrent la nature itérative du développement du matériel et l'importance de maintenir la compatibilité tout en améliorant les performances. La mise en œuvre du Bitaxe Ultra permet aux utilisateurs d'accéder à la technologie ASIC plus récente tout en préservant la nature éducative et expérimentale de la plateforme.


### Microcontrôleur et systèmes de communication


Au cœur de chaque appareil Bitaxe se trouve un microcontrôleur ESP qui sert d'interface principale entre l'utilisateur et la puce ASIC. Ce microcontrôleur exécute un logiciel spécialisé développé par la communauté Open Source Miners United (OSMU), permettant un contrôle précis des paramètres de fonctionnement du ASIC. La communication entre le microcontrôleur et le ASIC se fait par le biais de lignes de communication série soigneusement conçues qui sont gravées directement sur le circuit imprimé sous forme de traces visibles.


Le rôle du microcontrôleur va au-delà du simple contrôle du ASIC : il comprend la gestion de l'alimentation, la surveillance de la température et les fonctions d'interface utilisateur. Grâce à l'écran d'affichage intégré, les utilisateurs peuvent surveiller les paramètres opérationnels critiques tels que la température, le taux de hachage, l'adresse IP et d'autres statistiques pertinentes du minage. Ce système de retour d'information en temps réel fournit des informations précieuses sur les performances de l'appareil et aide les utilisateurs à optimiser les opérations de minage tout en apprenant à connaître le comportement du matériel sous-jacent.


### Considérations relatives à la gestion de l'alimentation et à la sécurité


La plateforme Bitaxe fonctionne avec une alimentation stricte de 5 volts, ce qui rend la sélection d'une alimentation appropriée critique pour la longévité et la sécurité de l'appareil. Le système de gestion de l'alimentation des cartes Bitaxe comprend des circuits sophistiqués conçus pour réguler la tension fournie à la puce ASIC tout en surveillant la consommation d'énergie dans les différents modes opérationnels. Cette capacité de gestion de l'énergie permet à l'appareil de fonctionner efficacement à travers une gamme de fréquences et de tensions internes, consommant typiquement entre 5 et 25 watts selon la configuration.


La compréhension des exigences en matière de puissance devient cruciale si l'on considère qu'une application incorrecte de la tension peut endommager l'appareil de façon permanente. La relation entre la fréquence, la tension, la consommation d'énergie et le taux de hachage démontre les principes fondamentaux du fonctionnement du ASIC qui s'appliquent à tout le matériel de minage. Les utilisateurs peuvent expérimenter différents réglages de puissance pour comprendre les compromis d'efficacité inhérents aux opérations de minage, en acquérant une expérience pratique des concepts qui s'appliquent aux implémentations de minage à plus grande échelle.


### Focus sur le Solo Mining et participation au réseau


La plateforme Bitaxe vise spécifiquement les applications de minage en solo, où les mineurs individuels tentent de résoudre les blocs Bitcoin de manière indépendante plutôt que de participer à de grands pools de minage. Bien que le taux de hachage des appareils Bitaxe rende statistiquement improbable la découverte de blocs réussis, cette approche remplit d'importantes fonctions éducatives et philosophiques au sein de la communauté Bitcoin. Le minage en solo ou minage solitaire avec des appareils Bitaxe aide les utilisateurs à comprendre les mécanismes fondamentaux du système proof-of-work de Bitcoin tout en contribuant à la décentralisation du réseau.


L'accent mis sur le minage solitaire reflète l'engagement de la communauté OSMU à encourager la participation individuelle au modèle de sécurité du Bitcoin. En fournissant du matériel accessible qui peut fonctionner indépendamment, la plateforme Bitaxe permet aux utilisateurs d'exécuter leurs propres opérations de minage sans dépendre d'une infrastructure commune. Cette approche favorise une meilleure compréhension du mécanisme de consensus de Bitcoin tout en soutenant la nature décentralisée du réseau grâce à une plus grande diversité de mineurs.


### Évolution du matériel et amélioration de la production


La plateforme Bitaxe continue d'évoluer grâce aux commentaires de la communauté et à l'optimisation de la production. Les nouvelles versions intègrent des améliorations qui renforcent la capacité de production et l'expérience de l'utilisateur. Les mises à jour de versions se concentrent généralement sur l'efficacité de la production plutôt que sur des changements de performance fondamentaux, garantissant que les utilisateurs existants ne sont pas confrontés à la pression de l'obsolescence. Des fonctionnalités telles que le passage des connecteurs micro-USB à USB-C et l'amélioration des systèmes de connexion d'alimentation reflètent l'attention portée par la communauté aux améliorations pratiques en matière d'ergonomie.


Cette approche évolutive démontre les avantages du développement de matériel open source, où l'apport de la communauté permet des améliorations progressives qui profitent à tous les utilisateurs. La philosophie "if it hashes, it hashes" met l'accent sur la fonctionnalité de la plateforme plutôt que sur les mises à jour constantes, encourageant les utilisateurs à entretenir et à utiliser leurs appareils plutôt qu'à rechercher les versions les plus récentes. Cette approche soutient des pratiques matérielles durables tout en maintenant la valeur éducative de Bitaxe.


## Où puis-je en savoir plus ?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Le projet Bitaxe représente une initiative complète de minage open source qui s'étend bien au-delà d'un seul appareil. Comprendre où trouver des informations fiables, des ressources techniques et le soutien de la communauté sont cruciaux pour quiconque cherche à s'engager dans cet écosystème. Ce chapitre fournit un guide complet des plateformes et des ressources essentielles qui constituent la base de la communauté Bitaxe et Open Source Miners United (OSMU).


### Bitaxe.org, la plateforme centrale


Le site web Bitaxe.org est le principal point d'accès à toutes les informations et ressources liées au projet. Cette plateforme centralisée est votre premier point de référence lorsque vous souhaitez en savoir plus sur les appareils Bitaxe ou explorer d'autres projets au sein de la communauté OSMU. La conception du site web met l'accent sur l'accessibilité et l'organisation, en présentant aux visiteurs des liens soigneusement sélectionnés qui renvoient à diverses ressources spécialisées dans l'ensemble de l'écosystème.


L'importance de ce centre ne peut être surestimée, car il élimine la confusion qui accompagne souvent les projets open source décentralisés. Plutôt que de chercher sur de multiples plateformes ou de se fier à des informations potentiellement obsolètes provenant de sources non officielles, les utilisateurs peuvent faire confiance à Bitaxe.org pour fournir des liens actualisés et vérifiés vers toutes les ressources essentielles. Cette approche garantit que les nouveaux venus comme les membres expérimentés de la communauté peuvent trouver efficacement les informations spécifiques dont ils ont besoin pour leurs projets.


### Ressources techniques et matériel de développement


Le dépôt de fichiers de conception de matériel sur GitHub représente l'une des ressources les plus précieuses pour toute personne intéressée par la compréhension ou la construction de dispositifs Bitaxe. Ce dépôt public contient une documentation complète qui couvre tous les aspects du processus de conception du matériel, des concepts initiaux aux spécifications de fabrication finales. Le dépôt comprend des images détaillées, des objectifs de projet, des descriptions de fonctionnalités et des explications sur les composants intégrés qui fournissent à la fois une profondeur technique et des conseils pratiques.


Pour ceux qui souhaitent fabriquer leurs propres appareils, le dépôt comprend des fichiers de documentation spécifiques tels que building.md, qui fournit des instructions étape par étape pour l'ensemble du processus de production. Cette documentation couvre les outils logiciels nécessaires à la conception des circuits imprimés, les procédures d'envoi des fichiers aux fabricants et les étapes de réception et de validation des circuits imprimés fabriqués. Ce niveau de détail garantit que les particuliers ou les petites organisations peuvent naviguer avec succès dans le processus de fabrication sans avoir une expérience préalable approfondie de la production de matériel.


Le dépôt ESP-Miner sert d'emplacement central pour tout le code et la documentation relatifs au micrologiciel. Ce dépôt GitHub contient chaque ligne de code écrite pour le micrologiciel Bitaxe, ainsi qu'une documentation complète qui explique les exigences du système, les spécifications matérielles et les options de configuration. La structure du dépôt est conçue pour accommoder à la fois les utilisateurs qui préfèrent les fichiers binaires précompilés et les développeurs qui veulent construire le micrologiciel à partir du code source.


La documentation de ce référentiel comprend des sections détaillées sur les exigences matérielles, les options de préconfiguration et les valeurs recommandées pour divers paramètres. Ces informations s'avèrent précieuses pour les utilisateurs qui souhaitent personnaliser leurs appareils ou résoudre des problèmes spécifiques. En outre, le dépôt comprend des informations sur les nouveaux développements, tels que l'intégration du Raspberry Pi, ce qui garantit que la documentation reste à jour par rapport à l'évolution continue du projet.


### Outils de gestion et de maintenance des appareils


Le flasheur web Bitaxe représente une solution pratique pour la maintenance et la mise à jour des appareils. Cet outil basé sur le web permet aux utilisateurs de flasher le micrologiciel de leurs appareils sans nécessiter de logiciel spécialisé ou de procédures de ligne de commande complexes. Le flasheur supporte plusieurs variantes d'appareils, y compris le Bitaxe Ultra avec différentes versions de port et les anciens modèles Bitaxe Max. Les utilisateurs peuvent choisir de mettre à jour le micrologiciel existant via l'interface web ou d'effectuer des réinitialisations d'usine complètes à l'aide de connexions USB.


Cet outil répond à l'un des défis les plus courants auxquels sont confrontés les passionnés de matériel informatique : la maintenance et la mise à jour des microprogrammes des appareils. Grâce à une interface web conviviale, le flasheur élimine de nombreux obstacles techniques qui pourraient empêcher les utilisateurs de maintenir leurs appareils à jour avec les dernières versions du micrologiciel. La conception de l'outil privilégie la simplicité tout en conservant la flexibilité nécessaire aux différentes configurations d'appareils et aux scénarios de mise à jour.


### Plateformes communautaires et canaux de communication


Le serveur Discord représente le cœur de l'interaction et du soutien en temps réel de la communauté au sein de l'écosystème Bitaxe. L'organisation du serveur reflète les divers intérêts et besoins des membres de la communauté, avec des canaux soigneusement structurés qui facilitent les discussions sur des sujets spécifiques. Les nouveaux membres sont soumis à un processus de vérification qui nécessite la lecture et l'acceptation des règles de la communauté, afin de s'assurer que tous les participants comprennent les attentes en matière d'interaction respectueuse et productive.


La structure des canaux du serveur comprend des zones de discussion générale couvrant des sujets tels que l'intégration de l'énergie solaire, les pools de minage et les discussions liées au Bitcoin. Des sections plus spécialisées se concentrent sur des appareils spécifiques, y compris des canaux dédiés aux variantes Bitaxe Ultra, Hex et Supra. Le canal consacré au micrologiciel offre un espace ciblé pour les discussions techniques sur le développement de logiciels et le dépannage, tandis que le canal consacré aux communiqués officiels permet aux membres de la communauté de recevoir des notifications opportunes sur les nouveaux développements.


Il comporte également un espace abonné qui offre des avantages supplémentaires aux membres de la communauté qui choisissent de soutenir financièrement le projet. Cette approche progressive permet à la communauté d'offrir des services améliorés tout en maintenant un accès ouvert aux informations essentielles et aux canaux d'assistance. Le canal d'aide est un espace dédié au dépannage et à l'assistance technique, qui permet aux utilisateurs de bénéficier d'un soutien rapide lorsqu'ils rencontrent des difficultés.



Le wiki Open Source Miners United (osmu.wiki) fournit une documentation détaillée qui complète les discussions en temps réel qui se déroulent sur Discord. Contrairement aux plateformes de discussion, le wiki offre une documentation structurée et consultable qui couvre tous les aspects du projet Bitaxe et des initiatives connexes. Son organisation reflète la structure du projet, avec des sections dédiées aux différentes séries d'appareils et des guides d'installation complets.


La nature open source du wiki permet aux membres de la communauté de contribuer directement à la documentation. Les utilisateurs peuvent modifier les pages, soumettre des corrections et ajouter de nouvelles informations grâce à l'intégration de GitHub, ce qui garantit que la base de connaissances reste à jour et transparente. Cette approche collaborative tire parti de l'expertise collective de la communauté tout en maintenant un contrôle de la qualité grâce à un processus de révision des modifications soumises.


Le wiki comprend des ressources pratiques telles que des guides d'installation PDF qui fournissent des instructions étape par étape pour la configuration et l'utilisation de l'appareil. Ces guides constituent des références précieuses pour les nouveaux utilisateurs et les membres expérimentés de la communauté qui ont besoin d'un accès rapide à des procédures spécifiques ou à des détails de configuration.


### Informations sur les achats et les fournisseurs


La liste officielle de Bitaxe répond à un besoin critique au sein de la communauté du matériel open source : identifier les vendeurs dignes de confiance et éviter les vendeurs frauduleux. Cette liste comprend des revendeurs et des fabricants vérifiés qui répondent à des critères spécifiques de légitimité et de soutien de la communauté. Chaque liste comprend des liens directs vers les sites web des vendeurs, des informations régionales et des descriptions d'entreprises qui aident les utilisateurs à prendre des décisions d'achat éclairées.


Il est important de noter que la liste indique si chaque vendeur contribue en retour à la communauté de l'OSMU, que ce soit financièrement ou par d'autres formes de soutien. Cette transparence aide les membres de la communauté à comprendre quels sont les vendeurs qui soutiennent activement le développement et la durabilité du projet. La liste sert également de mesure de protection contre les escroqueries courantes, telles que les précommandes non autorisées de produits non commercialisés, qui ont historiquement causé des problèmes au sein de la communauté.


L'accent mis sur les liens non affiliés démontre l'engagement de la communauté à fournir des recommandations impartiales. Les utilisateurs peuvent être sûrs que les recommandations sont fondées sur la légitimité des fournisseurs et la contribution de la communauté plutôt que sur des incitations financières, ce qui garantit que les décisions d'achat soutiennent à la fois les besoins individuels et la durabilité de la communauté.



# Logiciels et opérations

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Qu'est-ce que l'AxeOS ?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS est un micrologiciel et une interface web pour les appareils de minage Bitaxe, offrant aux utilisateurs un contrôle complet et des capacités de surveillance par le biais d'un tableau de bord intuitif basé sur un navigateur. Ce système transforme la tâche complexe de la gestion des ASICs en une expérience accessible, permettant aux mineurs de contrôler les performances, d'ajuster les paramètres et de gérer plusieurs appareils à partir d'une seule interface. Comprendre AxeOS est essentiel pour maximiser le potentiel de votre appareil Bitaxe et maintenir des opérations de minage optimales.


### Aperçu du tableau de bord et indicateurs clés


Le tableau de bord AxeOS est votre principale fenêtre sur les performances de votre appareil Bitaxe, présentant les mesures critiques de minage dans un format organisé et en temps réel. Lorsque vous naviguez vers l'adresse IP de votre appareil Bitaxe, vous êtes immédiatement confronté à quatre indicateurs de performance clés qui définissent l'état actuel de votre opération de minage. L'affichage du taux de hachage montre la vitesse de calcul réelle de votre puce ASIC lorsqu'elle traite le modèle de bloc actuel, fournissant un retour d'information immédiat sur la fonctionnalité principale de votre appareil.


Adjacent au taux de hachage, le compteur d'actions suit chaque solution valide que votre appareil Bitaxe soumet au pool de minage, s'incrémentant à chaque soumission réussie et servant de mesure directe de la contribution de votre appareil aux efforts du pool de minage. L'indicateur d'efficacité fournit des informations cruciales sur la performance énergétique de votre appareil en calculant le rapport entre le taux de hachage et la consommation d'énergie, ce qui vous aide à optimiser la rentabilité de votre opération. L'indicateur de la meilleure difficulté conserve un enregistrement de la part de difficulté la plus élevée que votre appareil ait jamais trouvée, conservant cet accomplissement même après les redémarrages et les mises à jour, et ne se réinitialisant que lorsque vous effectuez un flash d'usine complet.


Le système de menu extensible du tableau de bord, contrôlé par un bouton à bascule, permet d'accéder à toutes les fonctionnalités d'AxeOS tout en conservant une interface propre. Le graphique du taux de hachage en direct représente l'une des fonctionnalités les plus précieuses, affichant des données de performance en temps réel qui deviennent de plus en plus précises et informatives au fur et à mesure que vous maintenez votre session. Les sections d'alimentation, de chaleur et de performance fournissent une surveillance complète de l'état opérationnel de votre appareil, y compris des avertissements de tension d'entrée qui vous alertent sur des problèmes potentiels d'alimentation tout en assurant un fonctionnement continu dans des paramètres sûrs.


### Surveillance avancée et informations sur le système


Les capacités de surveillance d'AxeOS vont bien au-delà du simple suivi du taux de hachage, fournissant des informations détaillées sur chaque aspect du fonctionnement de votre appareil Bitaxe. La section alimentation affiche la consommation d'énergie calculée à partir des circuits intégrés embarqués, les mesures de tension d'entrée de votre connexion d'alimentation, et les niveaux de tension ASIC demandés. Lorsque des baisses de tension se produisent, AxeOS présente immédiatement des notifications d'avertissement, bien que celles-ci n'affectent généralement pas les opérations de minage et indiquent simplement les opportunités potentielles d'optimisation de l'alimentation électrique.


Le contrôle de la température se concentre sur la gestion thermique de la puce ASIC, avec des lectures prises à des endroits stratégiques de l'appareil pour fournir des données thermiques précises avec des décalages appropriés pour la précision au niveau de la puce. Les affichages de fréquence et de tension offrent un retour d'information en temps réel sur les paramètres de réglage de votre ASIC, la tension mesurée représentant la lecture la plus précise disponible, prise directement à l'emplacement de la puce ASIC. Cette précision permet d'affiner les paramètres de performance tout en maintenant des conditions de fonctionnement sûres.


La section sur l'état de la connexion offre une visibilité immédiate sur la configuration de votre pool de minage, en affichant l'URL de la strate, le port et l'identification de l'utilisateur. Pour les appareils connectés à des pools publics, AxeOS génère des liens rapides pratiques qui vous transportent directement vers l'interface web de votre pool, où vous pouvez accéder à des statistiques détaillées, à des listes d'appareils et à des données de performance historiques. Cette intégration rationalise le processus de surveillance en connectant les informations au niveau de l'appareil et au niveau du pool dans un flux de travail transparent.


### Gestion du Swarm et contrôle multi-appareils


La fonctionnalité Swarm représente la solution d'AxeOS à la complexité de la gestion de plusieurs appareils Bitaxe à travers un réseau, éliminant le besoin de se souvenir et de naviguer vers de nombreuses adresses IP. Ce système de gestion centralisé vous permet d'ajouter des appareils en entrant simplement leur adresse IP, en détectant automatiquement les mineurs Bitaxe actifs et en les incorporant dans un tableau de bord de contrôle unifié. Une fois configuré, Swarm offre un contrôle complet sur l'ensemble de vos opérations minage à partir d'une seule interface.


Grâce à l'interface Swarm, vous pouvez effectuer des tâches de gestion critiques sur plusieurs appareils simultanément ou individuellement, notamment des modifications de la configuration du pool, des redémarrages d'appareils, des ajustements de fréquence et la surveillance des performances. Cette approche centralisée réduit considérablement les frais administratifs liés à la gestion d'opérations de minage de grande envergure, tout en garantissant une configuration cohérente sur l'ensemble des appareils. Le système préserve l'identité de chaque appareil tout en offrant des capacités de gestion collective, ce qui permet d'atteindre un équilibre optimal entre le contrôle granulaire et l'efficacité opérationnelle.


Le tableau de bord Swarm présente chaque appareil géré avec son état actuel, ses mesures de performance et ses commandes d'accès rapide, ce qui permet de réagir rapidement aux problèmes de performance ou aux changements de configuration. Cette fonctionnalité s'avère particulièrement précieuse pour les mineurs qui exploitent plusieurs appareils dans des lieux différents ou pour ceux qui ajustent fréquemment les paramètres de de minage en fonction des conditions du marché ou de la performance du pool.


### Gestion de la configuration et paramètres du système


La section Paramètres d'AxeOS offre un contrôle complet sur chaque aspect configurable de votre appareil Bitaxe, de la connectivité réseau aux paramètres de minage et à l'optimisation du matériel. La configuration du réseau commence avec la configuration Wi-Fi, où vous spécifiez votre nom de réseau et votre mot de passe, AxeOS recommandant des noms de réseau d'un seul mot sans espace pour assurer une connectivité fiable. Le système gère l'ensemble du processus de configuration sans fil, ce qui permet une gestion à distance et des capacités de surveillance.


La configuration du Minage est centrée sur les paramètres de la strate, où vous spécifiez l'URL du pool de minage choisi sans préfixe de protocole ni numéro de port, qui sont traités dans des champs distincts. Le champ utilisateur de la strate répond à diverses exigences en matière de pool, en prenant en charge les adresses Bitcoin pour le minage en solo et les systèmes de nom d'utilisateur pour le pool de minage, avec la possibilité d'ajouter des identifiants d'appareil pour les opérations multiappareils. La fonctionnalité de mot de passe de la strate, récemment ajoutée, prend en charge les pools nécessitant une authentification, bien que la plupart des pools publics fonctionnent sans cette exigence.


L'optimisation du matériel par l'ajustement de la fréquence et de la tension du cœur représente la capacité de réglage des performances la plus puissante d'AxeOS. En fonction de la version de votre appareil et de votre navigateur, ces paramètres peuvent apparaître sous forme de menus déroulants avec des configurations prédéfinies ou sous forme de champs ouverts permettant des valeurs personnalisées. Les réglages par défaut de la fréquence de 485 MHz et de la tension du cœur de 1200 mV fournissent un fonctionnement stable pour les tests initiaux, tandis que les utilisateurs avancés peuvent optimiser ces paramètres pour une performance ou une efficacité maximale en fonction de leurs exigences spécifiques et de leurs conditions d'utilisation.


### Maintenance du système et fonctions avancées


AxeOS inclut des fonctionnalités sophistiquées de maintenance du système conçues pour maintenir votre appareil Bitaxe à des performances optimales tout en fournissant des informations de diagnostic pour le dépannage et l'optimisation. Le système de mise à jour rationalise la gestion du firmware en affichant la dernière version disponible directement dans l'interface et en fournissant des liens de téléchargement direct vers les fichiers officiels du firmware. Cette intégration élimine le besoin de naviguer manuellement dans les dépôts GitHub ou de gérer les téléchargements de fichiers, simplifiant ainsi le processus de mise à jour en quelques clics.


L'interface de mise à jour accepte les fichiers de firmware correctement nommés, en particulier esp-miner.bin et www.bin, ce qui garantit la compatibilité et évite les erreurs d'installation. Pour les utilisateurs qui rencontrent des difficultés avec le processus de mise à jour standard, AxeOS fournit des références à des procédures complètes de flashage d'usine qui peuvent restaurer les appareils à leur fonctionnalité d'origine. Cette double approche s'adapte à la fois aux mises à jour de routine et aux scénarios de récupération.


Les informations en temps réel sur le fonctionnement des appareils sont fournies par le système de journalisation, qui affiche des informations détaillées sur les modèles de puces ASIC, le temps de fonctionnement du système, l'état de la connectivité Wi-Fi, la mémoire disponible, les versions du micrologiciel et les révisions de la carte. Ces journaux (rapports d'activité) sont d'une valeur inestimable pour les développeurs et les utilisateurs avancés qui cherchent à comprendre le comportement de l'appareil, à diagnostiquer les problèmes ou à optimiser les performances. La visualisation en temps réel des journaux (rapports) offre des informations opérationnelles en temps réel, telles que le traitement des nonces, les calculs de difficulté et les paramètres de soumission de minage, offrant ainsi une visibilité inédite sur le processus de minage lui-même.


Les autres caractéristiques du système comprennent le contrôle de l'orientation de l'écran pour les appareils utilisés dans des boîtiers personnalisés, l'inversion de la polarité du ventilateur pour les configurations de refroidissement spécialisées, et le contrôle automatique du ventilateur qui ajuste le refroidissement en fonction de la température du ASIC. Le contrôle manuel de la vitesse des ventilateurs permet une gestion précise du refroidissement lorsque les systèmes automatiques ne répondent pas à des exigences spécifiques. Tous les changements de configuration nécessitent une sauvegarde et un redémarrage de l'appareil pour être pris en compte, ce qui garantit un fonctionnement stable et empêche les états de configuration partiels qui pourraient avoir un impact sur les performances du minage.



# Communauté et collaboration

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Aperçu des contributions open source

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub et son rôle dans le développement de logiciels


GitHub représente un changement fondamental dans la manière dont les projets de développement de logiciels sont gérés et partagés au sein de la communauté mondiale des programmeurs. En tant que plateforme basée sur le cloud qui héberge des projets de développement de logiciels utilisant Git, un système de contrôle de version distribué, GitHub permet aux développeurs de collaborer de manière transparente sur des projets, indépendamment de leur emplacement physique. La plateforme sert à la fois d'outil technique et de réseau social pour les programmeurs, leur permettant de suivre les modifications, de fusionner les mises à jour, de maintenir différentes versions de leur code et de contribuer à des initiatives open source telles que le projet BitX d'Open Source Miners United.


La puissance de GitHub réside dans sa capacité à simplifier le processus complexe du développement collaboratif. Lorsque plusieurs développeurs travaillent sur un même projet, GitHub fournit l'infrastructure nécessaire pour gérer les contributions, examiner les modifications, traiter les problèmes liés au projet et maintenir une documentation complète. Cette approche collaborative a fait de GitHub un composant essentiel des flux de développement de logiciels modernes, transformant la façon dont les développeurs individuels et les grandes organisations abordent la gestion de projet et le partage de code.


### Navigation dans l'interface GitHub et la structure du dépôt


Pour comprendre l'interface de GitHub, il faut d'abord reconnaître les éléments clés qui composent la page d'un dépôt. La barre de navigation supérieure contient plusieurs sections essentielles, notamment **Code, Issues, Pull Requests, Discussions, Actions, Projects, Security et Insights**. Chaque section a une fonction spécifique dans l'écosystème de la gestion de projet, la section **Code** affichant les fichiers et dossiers qui composent le projet.


La structure du dépôt reflète l'approche organisationnelle des responsables du projet. Certains dépôts ne contiennent qu'un seul fichier, peut-être un simple script shell, tandis que d'autres, comme le projet matériel BitX, contiennent de nombreux fichiers organisés en répertoires et sous-répertoires. Le nom du dépôt apparaît en évidence et sert à la fois d'identifiant et de brève description de l'objectif du projet. Parmi les éléments interactifs essentiels figurent le bouton "Watch", qui permet de recevoir des notifications sur les mises à jour du dépôt, le bouton "Fork", qui permet de créer des copies personnelles du dépôt, et le bouton "Star", qui fonctionne comme un système d'approbation par la communauté, similaire à un "pouce levé".


La section "À propos" fournit des informations cruciales sur le projet dans un format condensé, y compris une description en une ligne, des informations sur la licence et des détails clés sur le projet. Pour le projet BitX, cette section l'identifie comme "open source ASIC Bitcoin miner hardware" et spécifie la licence GPL 3.0. Il est particulièrement important de comprendre les licences, car GitHub fonctionne comme une plateforme open source où les dépôts publics sont accessibles à l'ensemble de la communauté, mais où le contenu ne peut être utilisé et distribué que conformément aux règles de conformité de chaque licence.


### Travailler avec des branches et des versions de projet


Le concept de branches représente l'une des fonctionnalités les plus puissantes de GitHub pour gérer différentes versions et pistes de développement au sein d'un même projet. Une branche crée essentiellement une copie ou une version modifiée de la base de code principale, permettant aux développeurs de travailler sur des fonctionnalités spécifiques, des corrections de bogues ou des modifications expérimentales sans affecter la ligne de développement principale. La branche principale sert généralement de version par défaut et la plus stable du projet, tandis que des branches supplémentaires permettent de gérer différentes itérations, phases de test ou variantes de produits entièrement différentes.


Dans le projet matériel BitX, plusieurs branches existent pour gérer les différentes versions et configurations matérielles. Par exemple, la branche Ultra v2 contient des fichiers spécifiques à cette itération matérielle, tandis que la branche Super 401 se concentre sur les implémentations utilisant la puce S21 ASIC pour une meilleure efficacité. Chaque branche peut avoir plusieurs commits d'avance ou de retard par rapport à la branche principale, ce qui indique l'ampleur des modifications et de l'activité de développement. En examinant les différentes branches, les utilisateurs remarqueront des structures de fichiers, une documentation et même des représentations visuelles complètement différentes, reflétant les exigences et les spécifications uniques de chaque variante matérielle.


Le système de branches évite toute confusion parmi les contributeurs et les utilisateurs en séparant clairement les différentes pistes de développement. Plutôt que de mélanger des fonctionnalités expérimentales avec des versions stables, ou de combiner différentes versions de matériel en un seul endroit, les branches permettent une séparation nette tout en conservant la possibilité de fusionner les changements réussis dans la ligne de développement principale lorsque c'est nécessaire. Cette approche organisationnelle permet aux utilisateurs de trouver facilement la version spécifique dont ils ont besoin, tandis que les développeurs peuvent travailler sur des améliorations sans perturber le projet principal.


### Contribuer à travers les Issues (problèmes)


La section Issues est le principal canal de communication entre les utilisateurs et les responsables du projet pour signaler les problèmes, suggérer des améliorations et documenter les bogues. Cependant, il est essentiel de comprendre que la section Issues est spécifiquement conçue pour les problèmes techniques légitimes plutôt que pour les questions générales ou les demandes d'assistance. Lorsque les utilisateurs rencontrent des dysfonctionnements réels, des comportements inattendus ou identifient des améliorations potentielles, la création d'un problème bien documenté aide l'ensemble de la communauté en attirant l'attention sur des problèmes susceptibles d'affecter plusieurs utilisateurs.


Un rapport d'incident efficace nécessite une documentation détaillée du problème, y compris les circonstances qui ont conduit à l'incident, les étapes pour reproduire le problème et tous les détails techniques pertinents. Le projet BitX illustre ce principe à travers divers problèmes clos qui montrent le processus de résolution, depuis l'identification initiale du problème jusqu'à la résolution, en passant par les discussions au sein de la communauté. Certains problèmes donnent lieu à des améliorations matérielles, comme l'ajout de trous de montage pour augmenter les options de refroidissement, tandis que d'autres peuvent être résolus par l'éducation des utilisateurs ou des mises à jour logicielles.


La distinction entre Issues et Discussions est importante pour maintenir une interaction organisée au sein de la communauté. Alors que les Issues se concentrent sur des problèmes techniques spécifiques, la section Discussions fournit un environnement de type forum pour les questions, les idées et l'engagement général de la communauté. Bien que le serveur Discord soit devenu le principal canal de communication pour la communauté BitX, la section Discussions de GitHub reste disponible pour des conversations plus formelles ou consultables qui bénéficient d'une documentation permanente et d'une référence facile.


### Comprendre les Pull Requests


Les demandes de fusion représentent le mécanisme par lequel les contributeurs externes proposent des modifications au référentiel (dépôt) d'un projet. Lorsque quelqu'un identifie une amélioration, une correction de bogue ou une nouvelle fonctionnalité qui pourrait profiter au projet, il peut créer une demande de fusion pour soumettre ses modifications à un examen et à une intégration potentielle dans la base de code principale. Ce processus garantit que toutes les modifications sont examinées avant d'être intégrées au projet officiel, ce qui permet de maintenir la qualité du code et la cohérence du projet tout en favorisant les contributions de la communauté.


Le processus de demande de fusion commence généralement lorsqu'un contributeur clône le dépôt, crée sa propre copie où il peut apporter des modifications, puis soumet ces modifications au projet d'origine par le biais d'une demande de fusion. Les responsables du projet peuvent alors examiner les modifications proposées, en discuter avec le contributeur et, enfin, décider de les intégrer ou non dans le projet principal. Ce processus d'examen collaboratif permet de maintenir les normes du projet tout en encourageant la participation et l'amélioration de la communauté.


La compréhension des balises et des versions ajoute une couche supplémentaire à la gestion de projet et au contrôle des versions. Les balises servent de marqueurs dans le calendrier de développement, en identifiant des points spécifiques qui représentent des versions ou des étapes particulières. Dans les projets de matériel comme BitX, les balises correspondent souvent à des numéros de modèles spécifiques ou à des révisions de matériel, fournissant des points de référence clairs pour les utilisateurs qui recherchent des versions particulières. Les versions, plus couramment utilisées dans les projets de logiciels, représentent des distributions formelles de fonctionnalités achevées et de corrections de bogues, souvent accompagnées de notes de version détaillées et de paquets téléchargeables.


L'écosystème GitHub crée un environnement complet pour la collaboration open source qui va bien au-delà du simple partage de fichiers. En comprenant ces différents composants et leur utilisation correcte, les contributeurs peuvent participer efficacement aux projets, aider à améliorer la conception des logiciels et du matériel, et bénéficier de la connaissance collective et des efforts de la communauté mondiale du développement. Qu'il s'agisse de signaler des problèmes, de suggérer des améliorations ou de contribuer au code, GitHub fournit les outils et la structure nécessaires à une collaboration fructueuse dans le monde du logiciel libre.


## Contribution à l'Open Source

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

S'appuyant sur les bases de la création de problèmes et de l'exploration de projets open source, ce chapitre se concentre sur les aspects pratiques des contributions directes par le biais de demandes de fusion et de la gestion des dépôts. Comprendre comment gérer les dépôts fork, effectuer des modifications et soumettre des demandes de fusion représente un ensemble de compétences cruciales pour tout développeur souhaitant contribuer de manière significative à des projets open source, qu'ils impliquent le développement de logiciels ou la conception de matériel.


Le processus d'apport de modifications au code suit un flux de travail standardisé qui garantit l'intégrité du projet tout en permettant un développement collaboratif. Ce processus consiste à créer sa propre copie du dépôt d'un projet, à effectuer des modifications dans un environnement contrôlé, puis à proposer ces modifications au projet d'origine dans le cadre d'un processus de révision formel. Bien que les exemples de ce chapitre se concentrent principalement sur les contributions logicielles, les mêmes principes et procédures s'appliquent également aux projets matériels impliquant des conceptions de circuits imprimés, des schémas et d'autres documents techniques.


### Comprendre la structure des copies et des dépôts


La base de la contribution à tout projet open source commence par la création d'un fork, qui sert de copie personnelle du dépôt original. Lorsque vous naviguez vers un dépôt GitHub et que vous cliquez sur le bouton "fork", vous créez une copie indépendante sous votre propre compte GitHub qui maintient une connexion claire avec la source originale. Ce dépôt forké apparaît dans votre compte avec une indication claire de son origine, affichant un texte tel que "forked from [original-owner]/[repository-name]" sous le titre du dépôt.


Votre dépôt forké fonctionne indépendamment de l'original, ce qui vous permet d'apporter des modifications sans affecter le projet principal. Cependant, il reste au courant des mises à jour du dépôt original grâce aux fonctionnalités de synchronisation de GitHub. Lorsque le dépôt original reçoit des mises à jour qui manquent à votre fork, GitHub affiche des informations d'état telles que "Cette branche a X commits de retard" ou "X commits d'avance", fournissant une visibilité claire de la relation entre votre fork et le dépôt en amont. Vous pouvez synchroniser votre fork avec le dépôt original à tout moment en cliquant sur le bouton "Sync fork", ce qui permet de récupérer les dernières modifications de la source en amont.


La relation entre votre fork et le dépôt original devient particulièrement importante lorsque vous commencez à faire des changements. Au fur et à mesure que vous effectuez des modifications et que vous les livrez à votre fork, GitHub suit ces différences et les affiche comme des livraisons en avance sur le dépôt d'origine. Ce système de suivi permet le processus de demande de fusion, où vous pouvez proposer vos changements pour inclusion dans le projet principal tout en conservant un historique clair de ce qui a été modifié.


### Configuration de l'environnement de développement


La création d'un environnement de développement efficace nécessite une attention particulière à la fois aux outils de développement généraux et aux exigences spécifiques du projet. Visual Studio Code est un excellent environnement de développement intégré (IDE) pour la plupart des contributions open source, offrant des fonctionnalités essentielles pour l'édition de code, l'intégration du contrôle de version et la gestion de projet. Le premier élément essentiel consiste à installer et à configurer l'extension Git, qui permet une intégration transparente avec les dépôts GitHub directement à partir de votre environnement de développement.


Les versions modernes de Visual Studio Code incluent généralement la prise en charge de Git par défaut, mais vous devez vous authentifier avec votre compte GitHub pour activer toutes les fonctionnalités. Ce processus d'authentification implique de se connecter à GitHub via l'IDE, ce qui vous permet ensuite de cloner des dépôts, de valider des modifications et de pousser des mises à jour directement depuis votre environnement de développement. L'intégration GitHub apparaît sous forme d'icône dans la barre latérale gauche, donnant accès aux fonctionnalités de clonage du dépôt, de gestion de branche et de synchronisation sans nécessiter d'opérations en ligne de commande.


Pour les projets impliquant des systèmes embarqués ou des plates-formes matérielles spécifiques, des outils supplémentaires deviennent nécessaires. L'extension ESP-IDF représente un composant crucial pour les projets ciblant les microcontrôleurs ESP32, nécessitant une compatibilité de version spécifique pour garantir un fonctionnement correct. Le processus d'installation implique la sélection de la version ESP-IDF appropriée, la configuration des chemins d'accès aux outils et la mise en place de l'environnement de développement. La version 5.1.3 représente actuellement la configuration recommandée pour de nombreux projets basés sur l'ESP32, bien que ces exigences puissent évoluer au fur et à mesure que les projets mettent à jour leurs dépendances et leurs chaînes d'outils.


### Modifications et gestion des modifications


Une fois que votre environnement de développement est correctement configuré, le processus de contribution commence par le téléchargement ou le clonage de votre dépôt forké sur votre machine locale. Vous pouvez le faire soit en téléchargeant un fichier ZIP du contenu du dépôt, soit en utilisant la fonctionnalité de clonage intégrée de Visual Studio Code, qui fournit un flux de travail plus rationalisé pour le développement en cours. Le processus de clonage crée une copie locale de votre dépôt qui reste synchronisée avec votre GitHub fork, ce qui vous permet de travailler hors ligne tout en conservant des capacités de contrôle de version.


Lorsque vous travaillez avec le dépôt local, vous avez accès à la structure complète du projet, y compris les fichiers de code source, les fichiers de configuration, la documentation et tous les fichiers de conception matérielle. La plupart des projets de microprogrammes utilisent des langages de programmation tels que le C pour les fonctionnalités de base, avec des composants supplémentaires écrits en TypeScript pour les interfaces utilisateur ou en Java pour des utilitaires spécifiques. La compréhension de la structure du projet vous aide à identifier les fichiers appropriés à modifier et garantit que vos modifications sont conformes aux modèles architecturaux et aux normes de codage du projet.


Le processus de validation représente un aspect fondamental du contrôle de version qui nécessite une attention particulière à la fois à la précision technique et à la clarté de la communication. Avant d'apporter des modifications, vous devez bien comprendre le code existant et tester toutes les modifications dans votre environnement local. La règle cardinale de la contribution à l'open source est de ne jamais publier de code non testé, car cela peut introduire des bogues ou des vulnérabilités de sécurité qui affectent l'ensemble de la communauté du projet. En outre, vous ne devez jamais publier d'informations sensibles telles que des mots de passe, des jetons API ou des informations d'identification personnelles dans des référentiels publics, car ces informations deviennent accessibles en permanence à toute personne ayant accès au référentiel.


### Création et gestion des Pull Requests


Le point culminant de votre effort de contribution implique la création d'une demande de fusion, qui sert de proposition formelle pour fusionner vos changements dans le dépôt original du projet. Ce processus commence dans votre GitHub fork, où vous pouvez examiner les différences entre votre dépôt et la source en amont. L'interface de GitHub affiche clairement le nombre de commits en avance ou en retard, ce qui permet d'avoir une visibilité immédiate sur l'étendue des modifications proposées. Avant de créer une demande de fusion, vous devez vous assurer que votre fork est synchronisé avec les dernières modifications en amont afin de minimiser les conflits potentiels.


La création d'une demande de fusion efficace ne se limite pas à la simple soumission de vos modifications de code. La description de la demande de fusion vous permet de communiquer l'objectif, la portée et l'impact de vos modifications aux responsables du projet et à la communauté. Une description bien rédigée explique les problèmes auxquels vos modifications répondent, la manière dont vous avez mis en œuvre la solution et les implications potentielles pour d'autres parties du projet. Cette documentation est particulièrement importante pour les modifications complexes qui peuvent ne pas être immédiatement évidentes si l'on examine uniquement les différences de code.


Le processus de révision représente un aspect collaboratif du développement open source, dans lequel les responsables du projet et des contributeurs expérimentés évaluent les modifications que vous proposez. Vous pouvez demander l'intervention de réviseurs spécialisés dans les domaines concernés par vos modifications, afin de vous assurer que des membres compétents de la communauté examinent votre travail. Le processus de révision peut comporter plusieurs itérations, les réviseurs fournissant des commentaires, demandant des modifications ou des tests supplémentaires. Ce processus collaboratif d'amélioration permet de maintenir la qualité du code tout en offrant de précieuses opportunités d'apprentissage aux contributeurs, quel que soit leur niveau d'expérience.


Comprendre que toutes les demandes ne sont pas acceptées permet de définir des attentes appropriées pour le processus de contribution. Les responsables du projet peuvent rejeter des demandes pour diverses raisons, notamment en raison d'un mauvais alignement avec les objectifs du projet, de tests insuffisants ou de l'existence de solutions alternatives déjà en cours de développement. Plutôt que de considérer le rejet comme un échec, il faut y voir une occasion de tirer des enseignements des commentaires, d'affiner l'approche et, éventuellement, d'apporter des solutions alternatives qui répondent mieux aux besoins du projet. La communauté open source se nourrit de ce processus itératif de proposition, d'examen et d'affinement qui, en fin de compte, fait avancer les projets grâce à l'effort collectif et au partage de l'expertise.



## Qu'est-ce que Public-Pool ?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool représente une approche révolutionnaire du minage de bitcoin qui répond à de nombreuses préoccupations des mineurs concernant les pools de minage traditionnels. En tant que pool de minage de bitcoin solo entièrement open source, Public Pool modifie fondamentalement le modèle de distribution des récompenses auquel les mineurs sont habitués. Contrairement aux pools de minage traditionnels où les participants partagent les récompenses lorsque n'importe quel mineur du pool trouve un bloc, Public Pool fonctionne selon le principe du minage en solo où les mineurs individuels conservent 100 % de leurs récompenses lorsqu'ils parviennent à extraire un bloc.


La caractéristique la plus convaincante du Public Pool est sa structure sans frais. Lorsque les mineurs réussissent à trouver un bloc à l'aide de Public Pool, ils reçoivent la récompense complète du bloc ainsi que tous les frais de transaction associés, sans aucune déduction pour les coûts d'exploitation du pool. Cela contraste fortement avec les pools de minage traditionnels qui facturent généralement des frais allant de 1 à 3 % des récompenses de minage. Le modèle sans frais rend Public Pool particulièrement attractif pour les mineurs qui souhaitent maximiser leurs revenus potentiels tout en gardant un contrôle total sur leurs opérations de minage.


Pour comprendre la position unique de Public Pool, il est important de saisir la différence fondamentale entre le minage en solo et le minage en pool. Le vrai minage en solo signifie que vous minez indépendamment et que vous recevez la récompense complète du bloc (actuellement 3,125 BTC + frais) si vous trouvez un bloc, mais la probabilité est proportionnelle à votre taux de hachage par rapport à l'ensemble du réseau, ce qui crée une variance extrême qui peut s'étaler sur des mois ou des années entre les récompenses. Les pools traditionnels combinent la puissance de hachage pour trouver des blocs plus fréquemment, distribuant les récompenses proportionnellement et fournissant un revenu régulier et prévisible. Pour les mineurs qui ont investi des sommes considérables dans le matériel et les coûts d'exploitation, le pur solo mining (minage en solo) n'est généralement pas pratique, quels que soient ses avantages philosophiques : la variance rend presque impossible la couverture des coûts d'électricité et le recouvrement des investissements. Cette réalité économique signifie que la plupart des mineurs choisiront le pool de minage pour des raisons financières pratiques. Public Pool fonctionne comme un pool de minage en solo, ce qui signifie que vous êtes toujours confronté à la variance du minage en solo (vous n'êtes récompensé que lorsque vous trouvez personnellement un bloc), mais vous bénéficiez de l'infrastructure du pool et d'un fonctionnement transparent et sans frais.


### L'avantage de l'Open Source et la mise en œuvre technique


L'engagement de Public Pool en faveur du développement de logiciels libres offre aux mineurs une transparence et un contrôle sans précédent sur leurs opérations de minage. L'ensemble de la base de code est disponible sur GitHub, ce qui permet aux mineurs d'examiner exactement le fonctionnement du logiciel, de le modifier en fonction de leurs besoins et même de contribuer à son développement. Cette transparence répond à une préoccupation importante de la communauté de minage concernant les configurations et pratiques inconnues des pools de minage traditionnels.


L'architecture logicielle comprend à la fois la fonctionnalité principale du pool de minage et un référentiel d'interface utilisateur séparé, tous deux disponibles gratuitement pour téléchargement et modification. Les mineurs peuvent exécuter Public Pool dans diverses configurations, y compris des conteneurs Docker, ce qui permet de l'adapter à différentes configurations matérielles et préférences techniques. La documentation complète fournie dans les dépôts GitHub propose des guides d'installation détaillés, des options de configuration et des instructions de modification, ce qui la rend accessible aux mineurs ayant différents niveaux d'expertise technique.


La connexion au pool public nécessite une configuration minimale par rapport aux configurations de minage traditionnelles. Les mineurs doivent simplement configurer leurs appareils de minage avec les détails de connexion de Stratum et fournir leur adresse Bitcoin comme nom d'utilisateur. Un nom de travailleur optionnel peut être ajouté après un séparateur de points à des fins d'organisation.


### Caractéristiques de la communauté et modèle de durabilité


Public Pool intègre plusieurs fonctionnalités innovantes qui renforcent la communauté de minage de Bitcoin tout en maintenant son fonctionnement sans frais. La plateforme affiche des statistiques complètes, notamment le taux de hachage total des mineurs connectés, qui se situait généralement entre 1 et 2 PetaHash par seconde en 2024 et autour de 40 PH/s en novembre 2025, et fournit des informations détaillées sur les appareils de minage connectés. L'accent mis par la plateforme sur le matériel de minage open source est particulièrement remarquable, les appareils marqués par des étoiles indiquant des conceptions entièrement open source, avec des liens vers leurs dépôts GitHub respectifs.


La viabilité du fonctionnement de Public Pool à tarif zéro repose sur un partenariat créatif avec les vendeurs de matériel de minage dans le cadre d'un programme d'affiliation. Lorsque les mineurs achètent du matériel auprès des entreprises partenaires en utilisant le code de réduction "SOLO", cinquante pour cent des gains des affiliés soutiennent les coûts opérationnels de Public Pool, tandis que les cinquante pour cent restants sont distribués sous forme de récompenses aux mineurs qui atteignent les parts de difficulté les plus élevées chaque mois. Ce modèle crée une relation symbiotique dans laquelle les mineurs bénéficient de réductions sur leurs achats d'équipement, les vendeurs gagnent des clients et Public Pool maintient ses opérations sans facturer de frais directs.


### Philosophie et bonnes pratiques en matière de décentralisation


Bien que Public Pool offre une excellente alternative aux pools de minage traditionnels, il est important de comprendre son rôle dans le contexte plus large de la décentralisation Bitcoin. La plateforme sert de tremplin vers l'objectif ultime, à savoir que les mineurs individuels gèrent leurs propres pools de minage. L'exploitation de son propre pool de minage représente le plus haut niveau de décentralisation, car elle élimine la dépendance à l'égard d'une infrastructure ou d'un logiciel tiers, quelle que soit la transparence ou les bonnes intentions de ce tiers.


La nature open source de Public Pool en fait une plateforme d'apprentissage idéale pour les mineurs qui souhaitent comprendre le fonctionnement du pool avant de mettre en œuvre leurs propres solutions. La disponibilité de guides d'installation pour plusieurs systèmes d'exploitation et la documentation complète fournissent aux mineurs les connaissances nécessaires pour passer de l'utilisation de Public Pool à l'exploitation de leur propre infrastructure de minage. Cet aspect éducatif s'aligne sur les principes fondamentaux de Bitcoin d'auto-souveraineté et de décentralisation, permettant aux mineurs individuels de prendre le contrôle complet de leurs opérations de minage tout en contribuant à la sécurité globale et à la décentralisation du réseau Bitcoin.


L'interface utilisateur de la plateforme offre aux mineurs des capacités de surveillance détaillées, notamment l'état des travailleurs, les statistiques sur le taux de hachage et les mesures de performance. Ces fonctionnalités aident les mineurs à optimiser leurs opérations tout en apprenant les principes de gestion des pools qu'ils peuvent ensuite appliquer à leurs propres implémentations de pools de minage.


## Comment installer Public-Pool sur Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Gérer son propre pool de minage Bitcoin à domicile est devenu de plus en plus accessible grâce à du matériel moderne et des solutions logicielles simplifiées. Ce chapitre explore la mise en œuvre pratique d'un pool public à domicile à l'aide d'un mini-PC abordable et d'un logiciel de gestion de nœuds simplifié. À la fin de ce guide, vous comprendrez les exigences matérielles, le processus d'installation du logiciel et la configuration de base nécessaire pour établir votre propre infrastructure de  pool de minage.


### Configuration matérielle requise et installation


La base de toute installation de pool de minage à domicile commence par le choix d'un matériel approprié qui concilie les performances, le coût et l'efficacité énergétique. Un mini PC représente une solution idéale pour cette application, car il offre une puissance de traitement suffisante tout en conservant un encombrement réduit et une consommation d'énergie raisonnable. La configuration recommandée comprend un processeur Intel N100, qui fournit des ressources de calcul adéquates pour les opérations de pool, associé à un téraoctet de stockage NVMe au moins pour accueillir la blockchain Bitcoin et les données associées.


L'exigence de stockage est particulièrement critique puisque l'exécution d'un pool de minage nécessite le maintien d'un nœud Bitcoin entièrement synchronisé. Le disque NVMe d'un téraoctet garantit des opérations de lecture/écriture rapides, essentielles à la synchronisation de la blockchain et au traitement des transactions en cours. En outre, l'allocation d'une quantité suffisante de RAM permet un fonctionnement sans heurts du système d'exploitation Linux sous-jacent et du logiciel de gestion des nœuds qui coordonnera les activités du pool.


### Architecture logicielle et gestion des nœuds


La pile logicielle d'un pool de minage domestique repose sur une base Linux, offrant la stabilité et la sécurité nécessaires aux opérations Bitcoin. Au-dessus de ce système de base, un logiciel de gestion de nœuds spécialisé comme Umbrel crée une interface intuitive pour la gestion de l'infrastructure Bitcoin. Cette approche fait abstraction d'une grande partie de la complexité traditionnellement associée à l'exploitation des nœuds Bitcoin, ce qui rend le fonctionnement du pool accessible aux utilisateurs n'ayant pas de connaissances techniques approfondies.


Umbrel est une plateforme complète de gestion des nœuds qui gère l'installation, la synchronisation et la maintenance continue du Bitcoin Core par le biais d'une interface web. Le modèle de magasin d'applications de la plateforme permet d'installer facilement des services supplémentaires, y compris le logiciel de pool de minage, par le biais d'opérations simples de type "pointer et cliquer". Cette architecture permet aux utilisateurs de se concentrer sur l'exploitation du pool plutôt que sur l'administration du système, tout en conservant un contrôle total sur leur infrastructure Bitcoin.


### Installation et configuration du pool public


L'installation d'un logiciel de pool public par le biais de la plateforme Umbrel démontre la nature rationalisée du déploiement d'une infrastructure Bitcoin moderne. Le processus commence par l'accès au magasin d'applications d'Umbrel via l'interface Web, où une simple recherche de "pool public" révèle les logiciels de pool de minage disponibles. L'installation ne nécessite que quelques clics : sélection de l'application, confirmation de l'installation et attente de la fin du processus d'installation automatisé.


Le processus d'installation configure automatiquement les connexions nécessaires entre le logiciel du pool public et le nœud Bitcoin sous-jacent. Cette intégration garantit que le pool peut valider les transactions, construire des modèles de blocs et distribuer le travail aux mineurs connectés sans nécessiter la configuration manuelle de paramètres de réseau complexes. Une fois l'installation terminée, l'interface du pool devient immédiatement accessible via le réseau local, offrant des capacités de surveillance et de gestion en temps réel.


### Connexion des mineurs et considérations relatives au réseau


Pour connecter le matériel de minage à votre nouveau pool, il faut configurer les paramètres du pool du mineur pour qu'il pointe vers votre infrastructure locale. Cela implique de remplacer l'adresse par défaut du pool par votre adresse IP locale et le numéro de port approprié attribué lors de l'installation du pool public. Le changement de configuration redirige les efforts de calcul de votre matériel de minage des pools externes vers votre infrastructure locale, ce qui vous permet de garder un contrôle total sur les opérations de minage et les récompenses potentielles.


La configuration du réseau joue un rôle crucial dans l'accessibilité et la fonctionnalité des pools. La configuration du réseau local implique généralement un adressage IP standard, mais les utilisateurs peuvent rencontrer des variations dans la résolution DNS en fonction de la configuration de leur routeur. Certains routeurs fournissent des services DNS locaux qui créent des noms conviviaux pour les services locaux, tandis que d'autres requièrent un accès direct à l'adresse IP. Pour une accessibilité plus large au-delà du réseau local, il peut être nécessaire de configurer la redirection des ports sur le routeur, bien que cela introduise des considérations de sécurité supplémentaires qui nécessitent une évaluation minutieuse des risques et des avantages associés.


L'établissement réussi d'un pool de minage domestique représente une étape importante vers une infrastructure Bitcoin décentralisée, fournissant à la fois une valeur éducative et des capacités de minage pratiques tout en conservant un contrôle total sur vos opérations Bitcoin.


# Assemblage du matériel et dépannage

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Quels outils utiliser ?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

Dans le monde de soudage de composants montés en surface (CMS), en particulier lorsque l'on travaille sur des projets Bitaxe, disposer des bons outils fait la différence entre la frustration et réussite. Ce guide complet couvre l'équipement essentiel nécessaire pour s'attaquer efficacement aux projets de soudage CMS, des outils manuels de base aux équipements spécialisés qui amélioreront vos capacités de soudure.


Si vous souhaitez vous référer à de la documentation sur les schémas, consultez ce [GitHub repo](https://github.com/skot/bitaxe-doc/tree/main).


### Outils à main basiques et instruments de précision


La base de toute installation de soudure CMS commence par une pince à épiler de qualité, qui sert d'outil principal pour le placement des composants. Deux types de pinces s'avèrent particulièrement utiles pour ce travail : les pinces standard à bout droit et celles dont la pointe est légèrement courbée. La pince à bout droit permet de manipuler la plupart des composants CMS que l'on trouve dans les kits Bitaxe typiques, tandis que la pince à bout courbé excelle lorsqu'il s'agit de travailler avec des composants extrêmement petits qui nécessitent un positionnement précis. Ces outils sont souvent inclus dans les kits de réparation, tels que les kits iFixit conçus pour les réparations de téléphones, ce qui les rend facilement accessibles à la plupart des amateurs.


En complément de la pince à épiler, une bonne paire de ciseaux est indispensable pour couper le ruban électrique, qui a de multiples fonctions dans les projets électroniques. Le ruban électrique fournit une isolation essentielle pour les câbles et les composants, et le fait de disposer d'un ruban de qualité facilite le processus de soudure. Ces fournitures de base peuvent être obtenues dans des quincailleries ou auprès de détaillants en ligne, sans nécessiter de fournisseurs spécialisés en électronique.


### Application et gestion de la pâte à souder


L'application de la pâte à souder représente l'un des aspects les plus critiques du brasage CMS, et les bons outils rendent ce processus à la fois précis et agréable. Les petites seringues non tranchantes remplies de pâte à souder offrent un contrôle exceptionnel de l'application de la pâte. Cette méthode permet d'appliquer avec précision la quantité exacte de pâte à souder nécessaire pour chaque joint, et la plupart des gens acquièrent rapidement la bonne technique de contrôle de la pression et du débit grâce à la pratique.


Le choix de la pâte à souder elle-même a un impact significatif sur la réussite du age. ChipQuik TS391SNL50 est une pâte à souder exceptionnelle pour les projets Bitaxe et les travaux SMD en général. Cette pâte conserve une consistance et des caractéristiques de fusion adéquates, évitant les problèmes associés aux alternatives moins chères qui ont des points de fusion excessivement bas. Les pâtes à souder de mauvaise qualité peuvent créer des problèmes lorsque des joints précédemment soudés redeviennent fluides lorsque l'on chauffe les zones adjacentes, ce qui entraîne un déplacement des composants et de mauvaises connexions. Bien que les pâtes à souder de qualité représentent un investissement initial plus élevé, l'amélioration des résultats et la réduction des frustrations justifient la dépense.


### Outils de résolution de problèmes et de nettoyage


Même les soudeurs expérimentés rencontrent des problèmes qui doivent être corrigés, ce qui rend l'équipement de déssoudage essentiel à toute boîte à outils complète. Un appareil de déssoudage, essentiellement un outil chauffé sous vide, élimine l'excès de soudure et corrige les connexions entre les broches des composants. Ces outils sont plus efficaces lorsqu'ils sont associés à un flux, qui améliore l'écoulement de la soudure et permet au processus de déssoudage d'être plus efficace.


Le flux se présente sous différentes formes, y compris des variétés solides et liquides, et sert à de multiples fins au-delà de l'assistance au déssoudage. Lorsque la pâte à souder commence à perdre de son efficacité au cours de sessions de travail prolongées, l'application d'un flux supplémentaire rétablit les caractéristiques d'écoulement appropriées et garantit des connexions fiables. Un petit outil en forme de cuillère, que l'on trouve souvent dans les kits de réparation de précision, facilite l'application précise du flux sur des zones spécifiques sans contaminer les composants environnants.


Le nettoyage de la planche est l'étape finale d'un travail de qualité professionnelle, qui nécessite de l'alcool isopropylique et une brosse de nettoyage spécifique. Une vieille brosse à dents fait parfaitement l'affaire, et un flacon compressible contenant de l'isopropanol permet de contrôler l'application de la solution de nettoyage. Cette combinaison permet d'éliminer les résidus de flux et de pâte, laissant les cartes avec un aspect propre et professionnel qui facilite également l'inspection des joints de soudure.


### Équipements spécialisés et outils avancés


Pour les projets impliquant des circuits intégrés complexes, en particulier les ASICs, les pochoirs transforment le processus de brasage, qui passe d'un placement manuel fastidieux à une application efficace et précise de la pâte. Ces gabarits découpés avec précision garantissent une épaisseur de pâte et un placement homogènes, ce qui réduit considérablement le temps nécessaire pour les composants complexes tout en améliorant la fiabilité. L'investissement dans des pochoirs de qualité porte ses fruits en termes de gain de temps et d'amélioration des résultats.


La gestion thermique devient cruciale lorsque l'on travaille avec des composants de puissance, ce qui fait de la pâte thermique ou de la graisse thermique des fournitures essentielles. Ces matériaux assurent un transfert de chaleur correct entre les dissipateurs de chaleur et les circuits intégrés, évitant ainsi les dommages thermiques et garantissant un fonctionnement fiable. Des matériaux d'interface thermique de qualité représentent un petit investissement qui protège des composants beaucoup plus coûteux.


Le cœur de toute installation de brasage CMS est la station de reprise à air chaud, qui fournit la chaleur contrôlée nécessaire aux travaux de montage en surface. Si les stations bon marché de l'ordre de 30 à 50 dollars peuvent fonctionner correctement, elles n'ont souvent pas la fiabilité et la précision des équipements plus haut de gamme. Ces stations d'entrée de gamme fonctionnent généralement à 355°C et incluent une réduction automatique de la température lorsque la pièce à main est replacée sur son support. Toutefois, leur fiabilité peut être irrégulière, certains appareils tombant en panne prématurément. Pour les travaux sérieux, l'investissement dans des équipements de qualité supérieure provenant de fournisseurs d'électronique spécialisés offre une meilleure valeur à long terme grâce à une fiabilité accrue et à un contrôle plus précis de la température.


La combinaison de ces outils crée une capacité de brasage CMS complète qui va bien au-delà des projets Bitaxe et s'étend aux travaux d'électronique générale. Comprendre le rôle de chaque outil et choisir un équipement de qualité adapté à votre niveau de compétence et aux exigences du projet garantit des résultats fructueux et une expérience de brasage agréable.



## Résoudre les problèmes de soudure

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Le kit d'émetteur-récepteur Bitaxe présente des défis uniques lors de l'assemblage qui nécessitent une attention particulière à l'orientation des composants, à la prévention des ponts de soudure et à la gestion correcte de la chaleur. Il est essentiel de comprendre ces problèmes courants et leurs solutions pour réussir la construction du kit et éviter des dommages coûteux aux composants. Ce chapitre examine les problèmes de soudure les plus fréquents rencontrés lors de l'assemblage du Bitaxe et fournit des techniques pratiques pour les identifier et les résoudre.


### Orientation et identification des composants


L'orientation correcte des composants représente l'un des aspects les plus critiques d'un assemblage Bitaxe réussi, en particulier avec les MOSFETs Q1 et Q2. Ces composants présentent des marqueurs d'orientation distinctifs qui doivent être soigneusement observés lors de l'installation. Chaque MOSFET contient un petit point qui correspond à une disposition spécifique des pastilles sur le circuit imprimé. La clé d'une orientation correcte réside dans la compréhension de la structure physique de ces composants, qui comportent quatre broches disposées avec une grande pastille et trois petites pastilles qui n'ont pas de connexion avec la grande pastille.


Lors de l'installation de Q1 et Q2, examinez attentivement le composant et le circuit imprimé. La configuration de la carte indique clairement l'orientation prévue grâce à la configuration des plots, avec quatre broches positionnées de manière à correspondre à la structure du MOSFET. Avant de souder un gros composant, vérifiez toujours l'orientation en comparant les repères physiques du composant avec la disposition des plots de la carte. Cette simple étape de vérification permet d'éviter les frustrations liées au déssoudage et à la réinstallation de composants mal orientés.


Les conséquences d'une orientation incorrecte vont au-delà de simples problèmes de fonctionnalité. Des MOSFETs mal orientés peuvent créer des dysfonctionnements de circuit qui sont difficiles à diagnostiquer et peuvent nécessiter le remplacement complet des composants. Prendre le temps de vérifier l'orientation avant d'appliquer la chaleur garantit le bon fonctionnement du circuit et évite des dépannages inutiles à un stade ultérieur du processus d'assemblage.


### Gestion des ponts de soudure et des excédents de soudure


Les ponts de soudure représentent un autre défi courant dans l'assemblage Bitaxe, en particulier autour des composants à pas fin comme U10. Ces connexions indésirables entre des broches adjacentes peuvent entraîner des dysfonctionnements du circuit et nécessitent des techniques d'élimination minutieuses. L'approche la plus efficace consiste à utiliser une mèche de dessoudage, un matériau tressé en cuivre qui absorbe l'excès de soudure lorsqu'il est chauffé. Cette technique requiert de la patience et une sélection appropriée des outils afin d'éviter d'endommager les composants délicats.


Lors du traitement des ponts de soudure sur les circuits intégrés, utilisez un support de circuit imprimé ou une pince articulée pour maintenir fermement le composant pendant le travail. Appliquez une chaleur douce sur la zone concernée et tirez soigneusement la mèche de dessoudage sur les connexions pontées. La tresse de cuivre absorbe naturellement l'excès de soudure et sépare les connexions indésirables. Ce processus peut nécessiter plusieurs tentatives, mais la persévérance permet d'obtenir des connexions propres et correctement séparées.


La prévention reste la meilleure approche de la gestion des ponts de soudure. L'utilisation de quantités appropriées de pâte à souder et le maintien d'une main ferme lors de la mise en place des composants réduisent considérablement la formation de ponts. Lorsque des ponts se forment, il faut les traiter immédiatement plutôt que d'espérer qu'ils n'affecteront pas le fonctionnement du circuit. Même des ponts apparemment mineurs peuvent causer des problèmes de fonctionnement importants qui sont difficiles à diagnostiquer une fois que la carte est entièrement assemblée.


### Composants critiques et considérations particulières


Le convertisseur buck U9 mérite une attention particulière en raison de son rôle critique dans la conversion de 5 volts en 1,2 volt pour la puce ASIC. Ce composant présente des défis uniques en raison de ses cinq petites connexions et de sa tendance à la défaillance. Une installation correcte nécessite une application précise de pâte à souder et une gestion attentive de la chaleur. Une quantité insuffisante de pâte à souder sous U9 peut entraîner de mauvaises connexions qui empêchent une conversion correcte de la tension, tandis qu'un excès de pâte peut créer des ponts qui entraînent un dysfonctionnement du circuit.


L'U9 produit des signatures audio distinctives lorsqu'il rencontre des problèmes de pont de soudure, générant un bruit à haute fréquence qui diffère du fonctionnement normal du ASIC. Cette technique de diagnostic auditif peut aider à identifier les problèmes, bien qu'elle nécessite une bonne audition des hautes fréquences pour être détectée. Lorsque le diagnostic auditif n'est pas possible, l'inspection visuelle devient essentielle. Examinez soigneusement toutes les connexions, à la recherche de ponts ou d'une couverture de soudure insuffisante.


Si U9 n'émet pas les 1,2 volts requis alors qu'il semble correctement soudé, la cause probable est une quantité insuffisante de pâte à souder. Retirez le composant, appliquez une petite quantité de pâte à souder supplémentaire et réinstallez-le. Dans les cas où certaines broches ne sont pas suffisamment recouvertes de pâte à souder, appliquez soigneusement de petites quantités de pâte à souder à des endroits spécifiques à l'aide d'une pince à épiler. La pâte à souder s'écoulera naturellement sous le composant lorsqu'il est chauffé, créant ainsi des connexions correctes par capillarité.


### Gestion de la chaleur et protection des composants


Une bonne gestion de la chaleur protège les composants sensibles des dommages thermiques tout en garantissant la fiabilité des joints de soudure. Les composants tels que l'oscillateur à cristal Y1 et U1 sont particulièrement sensibles à une exposition prolongée à la chaleur et nécessitent un contrôle minutieux de la température. Maintenez la température du fer à souder à 350 degrés Celsius, mais réduisez le temps d'application de la chaleur pour éviter d'endommager les composants. Des techniques de soudure rapides et efficaces protègent ces composants sensibles tout en assurant des connexions fiables.


La puce ASIC nécessite des techniques de manipulation particulières en raison de la structure complexe de ses broches et de sa sensibilité aux contraintes mécaniques. Lorsque vous utilisez des pochoirs pour l'application de la pâte à souder, veillez à ce que toutes les broches soient couvertes de manière uniforme afin d'éviter que les composants ne se placent de manière irrégulière. Si un excès de pâte à souder entraîne un positionnement inégal du ASIC, laissez l'assemblage refroidir complètement avant d'effectuer des corrections. Appliquez une légère pression uniquement sur les bords étiquetés du composant, jamais sur la zone centrale de la matrice, pendant le réchauffage afin d'obtenir une bonne mise en place.


Le composant U8 présente des difficultés particulières en raison de ses nombreuses broches et de la possibilité de plier les fils. Lorsque les broches se déforment durant la manipulation, utilisez un support de circuit imprimé ou une pince articulée pour fixer le composant et redresser avec précaution les broches concernées. Travaillez lentement et patiemment pour éviter de casser les fils délicats. Le fait de comprendre que certains groupes de broches de l'U8 sont connectés en interne peut simplifier le dépannage, car les ponts entre ces broches spécifiques n'affectent pas le fonctionnement du circuit. Toutefois, les ponts entre d'autres broches doivent être retirés avec précaution pour garantir un fonctionnement correct.


## Comment déboguer votre Bitaxe en utilisant AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Lorsque l'on travaille avec les appareils de minage Bitaxe, les défaillances matérielles peuvent se manifester de différentes manières qui peuvent ne pas être immédiatement évidentes. Comprendre comment diagnostiquer systématiquement ces problèmes en utilisant le système d'exploitation AxeOS peut faire gagner beaucoup de temps et éviter des remplacements de composants inutiles. Ce chapitre explore les techniques de diagnostic et les méthodologies de dépannage que les techniciens expérimentés utilisent pour identifier les problèmes matériels spécifiques à travers l'analyse logicielle.


### Comprendre les indicateurs de consommation d'énergie


Le premier et le plus critique des indicateurs de diagnostic dans AxeOS est le contrôle de la consommation d'énergie. Les appareils Bitaxe normaux, y compris les modèles Bitaxe Ultra et Bitaxe Supra, consomment typiquement entre 10 et 17 watts lors d'un fonctionnement standard. Cette mesure de base sert d'indicateur de santé principal pour l'ensemble du système. Lorsque la consommation d'énergie chute de manière significative en dessous de cette fourchette, en particulier en dessous de 3 watts, cela signale un problème fondamental avec la puce ASIC ou ses circuits de soutien.


Les scénarios de faible consommation d'énergie requièrent une attention immédiate, car ils indiquent que la puce de minage ne fonctionne pas du tout ou qu'elle fonctionne dans un état très dégradé. Cette seule mesure peut vous aider à différencier rapidement les problèmes de performance des pannes matérielles complètes. La lecture de la puissance dans AxeOS fournit un feedback en temps réel qui vous permet de contrôler l'efficacité de toutes les tentatives de réparation que vous faites sur l'appareil.


### Analyse des mesures de tension ASIC


La fonction de mesure de tension ASIC dans AxeOS fournit des informations de diagnostic cruciales qui aident à identifier la nature exacte des problèmes matériels. Lorsque vous examinez les lectures de tension, vous devez comprendre la relation entre la tension mesurée et la tension demandée pour diagnostiquer correctement les problèmes. Le système affiche à la fois la tension fournie à la puce ASIC et la tension que la puce demande au système de gestion de l'énergie.


Lorsque vous observez une mesure de tension ASIC d'exactement 1,2 volt combinée à une consommation d'énergie inférieure à 3 watts, cette combinaison spécifique indique soit un problème de soudure avec la puce ASIC, soit un ASIC complètement défectueux. Cette mesure de tension suggère que la puissance atteint l'emplacement de la puce, mais que la puce elle-même ne fonctionne pas correctement. L'inspection physique de la puce ASIC peut révéler des fissures ou d'autres dommages visibles qui expliqueraient ce comportement.


Un scénario de diagnostic différent apparaît lorsque vous observez une faible consommation d'énergie associée à des lectures de tension demandées très faibles, telles que 100 millivolts ou 0,5 volt. Ce schéma indique que la puce ASIC ne reçoit pas une tension d'alimentation adéquate, ce qui indique généralement des problèmes avec le composant convertisseur buck U9. Le convertisseur buck est responsable de la régulation précise de la tension dont les puces ASIC ont besoin pour fonctionner correctement.


### Interprétation des données du journal et communication ASIC


Le système de journalisation d'AxeOS fournit des informations précieuses sur la communication de votre puce ASIC avec le système de contrôle. Lorsque vous accédez aux journaux (rapports d'activité de la puce ASIC) par la fonction "show logs", la présence d'entrées "ASIC results" confirme que la puce n'est pas seulement alimentée, mais aussi qu'elle traite activement le travail et renvoie des résultats. Cette communication indique que le ASIC est correctement soudé et qu'il maintient sa connexion avec le circuit de contrôle.


L'absence de résultats ASIC dans les journaux (rapports), en particulier lorsqu'elle est associée à d'autres symptômes, permet de circonscrire le problème à des composants spécifiques ou à des problèmes de connexion. Cette approche diagnostique vous permet de distinguer les puces qui ne répondent pas du tout de celles qui peuvent avoir des problèmes de connexion intermittents. L'analyse des journaux devient particulièrement précieuse lors du dépannage de problèmes complexes pour lesquels plusieurs symptômes peuvent suggérer des causes différentes.


### Approche systématique du dépannage


Lors du diagnostic des problèmes matériels de Bitaxe, une approche systématique permet d'éviter de négliger des problèmes critiques et d'assurer des processus de réparation efficaces. Commencez par documenter la consommation d'énergie et les relevés de tension, puis mettez ces mesures en corrélation avec les données du journal pour obtenir une image complète du comportement du système. Cette approche méthodique permet d'identifier si les problèmes proviennent de la puce ASIC elle-même, du système d'alimentation électrique ou des voies de communication entre les composants.


Dans les cas où le convertisseur buck U9 semble être à l'origine du problème, une inspection physique et un éventuel ressoudage peuvent s'avérer nécessaires. Le composant U9 est particulièrement sensible aux problèmes de soudure, en particulier lors d'un premier assemblage. Lorsque des problèmes de régulation de tension sont suspectés, l'utilisation d'un multimètre pour vérifier que 1,2 volt est effectivement présent sur les broches ASIC permet de confirmer définitivement les problèmes d'alimentation. Si la tension est présente sur les broches, mais que le ASIC ne fonctionne toujours pas, et que l'inspection physique ne révèle aucun dommage, le remplacement de la puce ASIC devient l'étape logique suivante. Si les problèmes persistent même après le remplacement du ASIC, le composant U2, qui pilote la puce ASIC, peut nécessiter une attention particulière en tant qu'élément final de la séquence de dépannage.


## Comment déboguer en utilisant l'USB ?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Lors du dépannage des appareils de minage Bitaxe, l'accès direct au système de journalisation interne de l'appareil fournit des informations inestimables que les interfaces basées sur le web ne peuvent pas offrir. Ce chapitre explique comment établir une connexion série USB directe avec votre appareil Bitaxe en utilisant le cadre ESP-IDF, permettant de surveiller en temps réel les journaux du système, les séquences de démarrage et les messages d'erreur. Cette approche de débogage est particulièrement cruciale lorsqu'il s'agit d'appareils qui subissent des redémarrages fréquents ou des défaillances matérielles, car elle capture toutes les informations de diagnostic qui pourraient être perdues lors des redémarrages du système.


Le processus de débogage nécessite Visual Studio Code avec l'extension ESP-IDF, bien que n'importe quel IDE compatible puisse être utilisé. Cette méthode fonctionne avec toutes les variantes de Bitaxe qui incluent un port USB, y compris le Bitaxe Ultra 204 et d'autres modèles de la série. La connexion série directe contourne les limitations potentielles de l'interface web et fournit un accès non filtré aux informations sur l'état interne de l'appareil.


### Configuration de la communication en série


L'établissement de la communication avec votre appareil Bitaxe commence par la connexion du câble USB et l'ouverture du terminal ESP-IDF dans votre environnement de développement. La commande `idf.py monitor` initie le processus de connexion, en balayant automatiquement les ports COM disponibles pour établir une communication UART avec la puce ESP32 de votre appareil Bitaxe. Le système fait défiler les ports disponibles (COM3, COM4, COM16, etc.) jusqu'à ce qu'il trouve la bonne connexion.


Une fois connecté, le terminal affiche la séquence de démarrage complète et les journaux opérationnels en cours. Le processus de connexion initiale peut prendre quelques instants, le temps que le système identifie le port de communication correct. Si la détection automatique du port échoue, vous pouvez spécifier manuellement le port COM via l'interface de sélection du port de l'IDE. Ce canal de communication direct reste actif pendant toute la durée de fonctionnement de l'appareil, ce qui permet d'accéder en permanence aux diagnostics et aux mesures de performance du système.


### Interprétation de la séquence de démarrage et des journaux de fonctionnement normal


La séquence de démarrage fournit des informations essentielles sur la configuration matérielle et le processus d'initialisation de votre appareil Bitaxe. Les journaux(rapports) de démarrage normaux commencent par des informations sur la version de l'ESP-IDF, suivies par le message distinctif "Welcome to the Bitaxe. Hack the planet" qui confirme la réussite du chargement du micrologiciel. Le système affiche ensuite la configuration de la fréquence ASIC, l'identification du modèle de l'appareil et les détails de la version de la carte.


Un appareil fonctionnant correctement montrera une initialisation I2C réussie et une régulation de tension ASIC réglée à 1,2 volt. Les journaux affichent des informations sur l'état des GPIO et les séquences d'initialisation Wi-Fi, suivies de la configuration du serveur DHCP et de l'attribution de l'adresse IP. L'un des indicateurs les plus importants est le message de détection de la puce ASIC, qui doit indiquer "detected one ASIC chip" (détecté une puce ASIC) pour un appareil à puce unique. Cette confirmation confirme que le matériel de minage est correctement connecté et communique avec le contrôleur ESP32.


Les journaux opérationnels révèlent l'existence de plusieurs tâches concurrentes exécutées sur l'appareil, notamment la communication API de la strate, la coordination des tâches principales, la gestion des tâches ASIC et le traitement des tâches de la strate. Ces différents identificateurs de tâches permettent d'isoler les problèmes des composants spécifiques du système. Le fonctionnement normal comprend l'établissement d'une connexion au pool, les messages d'ajustement de la difficulté, la mise en file d'attente et le retrait de la file d'attente des tâches, et les rapports de génération de nonce. Les opérations de minage réussies affichent les résultats ASIC avec les calculs de difficulté et les confirmations de soumission de minage lorsque les parts atteignent le seuil requis.


### Identification des défaillances matérielles et des schémas d'erreur


Les défaillances matérielles se manifestent dans les journaux par des modèles d'erreur spécifiques qui indiquent les composants qui fonctionnent mal. Le mode de défaillance le plus courant implique des erreurs de communication I2C avec des circuits intégrés spécifiques sur la carte Bitaxe. Par exemple, les échecs de communication de la DS4432U apparaissent sous la forme de messages "ESP_ERROR_CHECK failed" avec des indicateurs de délai, indiquant des problèmes de régulation de la tension ou des problèmes de soudure affectant le composant U10 responsable de la communication avec l'écran.


Ces messages d'erreur contiennent des informations de débogage détaillées telles que le fichier source spécifique (main_ds4432u.c), l'appel de fonction défaillant et le cœur du processeur qui gère la tâche. Les informations de la trace arrière fournissent un contexte supplémentaire pour un dépannage avancé. Des schémas d'erreur similaires peuvent se produire avec la puce de contrôle de la température et du ventilateur EMC2101, chacune générant des signatures de journal distinctes qui aident à identifier le composant défaillant.


Les problèmes matériels se manifestent souvent par des cycles d'erreurs répétés suivis d'un redémarrage du système. Si votre appareil produit un bruit audible pendant son fonctionnement, cela indique généralement des problèmes de soudure tels que des ponts entre les broches des composants ou des joints de soudure inadéquats. Bien que ces problèmes mécaniques ne génèrent pas toujours des entrées de journal spécifiques, ils créent des conditions de fonctionnement instables qui se manifestent par des plantages fréquents et des cycles de redémarrage dans le output monitoring (sortie de surveillance).


### Stratégies avancées de dépannage


La surveillance en série offre plusieurs avantages par rapport aux interfaces de débogage basées sur le web, en particulier pour les pannes intermittentes ou les appareils qui subissent des redémarrages fréquents. La capture continue des journaux garantit qu'aucune information de diagnostic n'est perdue lors des redémarrages du système, contrairement aux interfaces web qui peuvent perdre des données lors d'événements de déconnexion. Cette capacité de journalisation complète permet d'identifier des modèles de défaillance et de corréler des conditions d'erreur spécifiques avec des facteurs matériels ou environnementaux.


Lors de l'analyse des dispositifs problématiques, il convient de se concentrer sur la séquence d'événements conduisant aux défaillances plutôt que sur des messages d'erreur isolés. Une communication ASIC réussie doit montrer des cycles réguliers de traitement des tâches, de génération de nonce et de soumission de parts. Les résultats ASIC manquants dans les journaux indiquent des échecs de communication entre l'ESP32 et la puce de minage, souvent causés par des problèmes d'alimentation, des traces endommagées ou des défaillances de composants.


Pour un dépannage systématique, documentez les schémas d'erreur et les défaillances spécifiques aux composants avant de solliciter l'aide de la communauté. Les journaux d'erreurs détaillés, y compris les identificateurs de puces et les modes de défaillance spécifiques, permettent aux utilisateurs expérimentés de fournir des conseils de réparation ciblés, tels que des procédures de remplacement de composants ou des corrections de soudure. Cette approche méthodique du débogage du matériel améliore considérablement le taux de réussite des réparations et réduit le temps de dépannage pour les problèmes complexes.


# Personnalisation avancée

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Modifier le circuit imprimé

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad est l'un des outils open source les plus puissants disponibles pour la conception et le routage de circuits imprimés (PCB). Ce logiciel de qualité professionnelle permet aux ingénieurs et aux amateurs de créer des conceptions électroniques complexes en plaçant des composants sur des cartes virtuelles et en routant les traces complexes qui relient ces composants entre eux. Ce qui rend KiCad particulièrement utile pour l'enseignement et le développement, c'est sa nature entièrement libre, qui permet aux utilisateurs de modifier, de personnaliser et d'apprendre à partir de conceptions existantes sans restrictions de licence.


Le projet Bitaxe illustre la puissance du développement de matériel open source, en fournissant une conception complète de circuit imprimé que les utilisateurs peuvent examiner, modifier et personnaliser en fonction de leurs besoins spécifiques. Cette accessibilité crée un excellent environnement d'apprentissage où les étudiants et les praticiens peuvent explorer des conceptions de circuits imprimés du monde réel tout en développant leur compréhension des systèmes électroniques. La possibilité de personnaliser des éléments visuels tels que des logos offre un point d'entrée accessible aux utilisateurs qui peuvent être intimidés par la complexité technique de la conception électronique.


### Configuration de l'environnement KiCad


Avant de commencer tout travail de personnalisation, il est essentiel de configurer correctement votre environnement de développement. Le référentiel (dépôt) Bitaxe doit être téléchargé sur votre machine locale, généralement via la fonctionnalité de téléchargement ZIP de GitHub. Ce dépôt contient tous les fichiers de projet nécessaires, y compris les fichiers de projet KiCad, les bibliothèques de composants et la documentation de conception requise pour une modification réussie.


L'installation de KiCad doit être réalisée en utilisant la distribution officielle du site web de KiCad, ce qui garantit la compatibilité avec les fichiers de projet et l'accès aux dernières fonctionnalités. Une fois le référentiel et KiCad correctement installés, l'ouverture du projet nécessite de naviguer jusqu'au fichier de projet Bitaxe Ultra KiCad dans la structure du référentiel téléchargé. Ce fichier de projet sert de pivot central qui relie tous les fichiers de conception associés, les bibliothèques de composants et les paramètres de configuration.


La vue initiale d'une conception de circuit imprimé complexe peut sembler écrasante, avec de nombreux composants, traces et couches créant un paysage visuel dense. Cependant, la fonctionnalité de visualisation 3D de KiCad fournit un outil inestimable pour comprendre la disposition physique et les relations spatiales au sein de la conception. Cette perspective tridimensionnelle transforme la représentation schématique abstraite en une visualisation réaliste du produit manufacturé final, facilitant ainsi la compréhension du placement des composants et de l'esthétique générale de la conception.


### Processus de personnalisation du logo


La personnalisation des logos sur les conceptions de circuits imprimés représente l'une des modifications les plus accessibles pour les utilisateurs novices de KiCad, car elle ne nécessite qu'un minimum de connaissances techniques tout en offrant des résultats visuels immédiats. Le processus commence avec l'outil de conversion d'image, qui transforme les fichiers d'image standard en formats d'empreinte compatibles avec le logiciel de conception de circuits imprimés. Ce processus de conversion nécessite une attention particulière aux paramètres de dimensionnement, généralement mesurés en millimètres, afin de garantir une mise à l'échelle correcte sur la carte finale fabriquée.


Le flux de travail du convertisseur d'images comprend plusieurs étapes critiques qui déterminent l'aspect final et l'emplacement des logos personnalisés. La sélection de l'image source doit privilégier les dessins à fort contraste qui se traduiront bien par le processus de sérigraphie utilisé dans la fabrication des circuits imprimés. La spécification de la taille devient cruciale, car les logos doivent être suffisamment grands pour rester lisibles après la fabrication, sans interférer avec l'emplacement ou la fonctionnalité des composants. Le choix entre les couches de sérigraphie avant et arrière influe à la fois sur la visibilité et sur les considérations relatives à la fabrication.


La gestion des bibliothèques d'empreintes représente un aspect fondamental de la personnalisation de KiCad, exigeant des utilisateurs qu'ils comprennent comment le logiciel organise et accède aux éléments de conception. L'ajout de logos personnalisés implique la création de nouvelles bibliothèques d'empreintes ou la modification de bibliothèques existantes, puis la liaison correcte de ces bibliothèques au sein de la structure du projet. Ce processus garantit que les éléments personnalisés restent accessibles au cours des différentes sessions de conception et qu'ils peuvent être facilement partagés avec d'autres membres de l'équipe ou collaborateurs.


### Exploration et compréhension de la conception avancée


Au-delà de la simple personnalisation du logo, KiCad fournit des outils puissants pour explorer et comprendre des conceptions de circuits imprimés complexes. Le système de gestion des couches permet aux utilisateurs de visualiser sélectivement différents aspects de la conception, depuis le placement et le routage des composants jusqu'aux spécifications de fabrication et aux informations d'assemblage. Cette approche par couches permet d'analyser en détail des éléments de conception spécifiques sans que les composants non apparentés n'encombrent l'écran.


L'analyse du routage des traces représente l'un des aspects les plus éducatifs de l'exploration des circuits imprimés, car elle révèle la manière dont les connexions électriques circulent entre les composants et les sous-systèmes. En suivant des traces individuelles ou des groupes de signaux apparentés, les utilisateurs peuvent mieux comprendre la fonctionnalité des circuits et les décisions de conception. Par exemple, l'examen des réseaux de distribution d'énergie révèle comment la régulation de la tension et les composants de filtrage travaillent ensemble pour fournir une alimentation propre et stable aux composants électroniques sensibles.


La relation entre la conception schématique et l'agencement physique devient évidente grâce à un examen minutieux des décisions de placement et de routage des composants. Comprendre pourquoi des composants spécifiques sont placés à des endroits particuliers, comment les considérations thermiques influencent les décisions d'implantation et comment les exigences en matière d'intégrité des signaux déterminent les choix de routage fournit des informations précieuses sur les pratiques professionnelles en matière de conception de circuits imprimés. Ces connaissances s'avèrent inestimables pour les utilisateurs qui développent leurs propres conceptions ou modifient des conceptions existantes pour des applications spécifiques.


Les outils complets de vérification des règles de conception de KiCad garantissent que les modifications maintiennent la compatibilité électrique et de fabrication. Ces systèmes automatisés permettent d'éviter les erreurs de conception courantes tout en informant les utilisateurs sur les normes et les meilleures pratiques de l'industrie. L'intégration de la visualisation 3D aux données de conception électrique crée un environnement d'apprentissage puissant où les concepts théoriques deviennent tangibles grâce à la représentation visuelle et à l'exploration interactive.


## Comment créer un fichier d'usine ?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

La création de microprogrammes personnalisés pour les appareils de minage basés sur l'ESP nécessite une attention particulière à la configuration, aux dépendances et au processus de création approprié. Ce guide complet décrit l'ensemble du processus de création de binaires de microprogrammes standard et de fichiers d'usine comprenant des paramètres préconfigurés, ce qui rend le déploiement plus efficace et réduit le temps d'installation pour les utilisateurs finaux.


Notez que ce chapitre est assez technique et ne peut être parcouru que par curiosité.


### Configuration de l'environnement de développement


Pour commencer le développement d'un firmware ESP-Miner, il faut d'abord établir l'environnement de développement adéquat dans Visual Studio Code, idéalement sur une distribution Linux. L'extension ESP-IDF est la pierre angulaire de cette configuration, car elle fournit les outils et le cadre d'intégration nécessaires au développement de l'ESP32. Lors de la première installation de l'extension ESP-IDF, les utilisateurs trouvent un guide d'installation qui facilite le processus de configuration.


Le choix de la version appropriée de l'ESP-IDF est un élément essentiel du processus d'installation. Alors que la version 5.1.3 était précédemment recommandée, l'expérience pratique a révélé que cette version peut causer des problèmes de construction qui compliquent le processus de développement. L'approche recommandée consiste désormais à utiliser la version 5.3 Beta 1 d'ESP-IDF, qui s'est révélée capable de résoudre ces problèmes de construction et de garantir le bon fonctionnement des appareils Bitaxe. Le processus d'installation nécessite de sélectionner l'option d'installation express et de choisir spécifiquement la version 5.3 Beta 1 parmi les options disponibles.


La configuration de l'environnement de développement va au-delà de l'installation de l'ESP-IDF et inclut la configuration correcte du terminal. Visual Studio Code propose plusieurs méthodes pour accéder aux fonctionnalités de l'ESP-IDF, notamment l'option de la palette de commandes pour ouvrir un terminal ESP-IDF ou l'utilisation de l'icône de terminal dédiée située dans l'interface. Cet environnement terminal spécialisé garantit le bon fonctionnement de toutes les commandes ESP-IDF et permet d'accéder à l'ensemble de la chaîne d'outils.


### Configuration des paramètres de l'ESP-Miner


Le fichier de configuration représente le cœur du processus de personnalisation de l'ESP-Miner, car il contient tous les paramètres essentiels qui définissent la manière dont l'appareil fonctionnera dans son environnement cible. Cette configuration englobe les paramètres du réseau, les connexions au pool de minage et les paramètres spécifiques au matériel qui doivent être adaptés au scénario de déploiement spécifique.


La configuration du réseau constitue le principal élément du processus d'installation, car elle nécessite la spécification d'informations d'identification Wi-Fi, notamment le SSID et le mot de passe. Plutôt que d'utiliser des valeurs de remplacement telles que "test", les configurations de production doivent inclure les identifiants réseau réels que l'appareil utilisera dans son environnement opérationnel. La configuration s'adapte également à diverses configurations de pool de minage, prenant en charge à la fois les configurations de pool privé avec des adresses IP spécifiques et les pools publics tels que public-pool.io avec leurs paramètres de port correspondants.


Les paramètres de configuration spécifiques au minage comprennent le paramètre utilisateur stratum, qui correspond généralement à l'adresse Bitcoin vers laquelle les récompenses du minage doivent être dirigées. D'autres paramètres matériels tels que les réglages de fréquence, les configurations de tension et les spécifications de type ASIC doivent être alignés sur la plateforme matérielle cible. Le dépôt GitHub fournit des exemples préconfigurés pour différentes variantes matérielles, tels que la configuration BM1368 conçue pour les appareils Super et les paramètres BM1366 pour les variantes Ultra. Les spécifications relatives à la version de la carte, telles que le réglage de la version du port sur 401 pour les révisions matérielles plus récentes, garantissent la compatibilité avec les caractéristiques spécifiques de l'appareil cible.


### Construction du Web Interface et du micrologiciel de base


Le projet ESP-Miner incorpore une interface web sophistiquée qui nécessite une compilation séparée avant que le processus de construction du firmware principal puisse commencer. Cette interface web, appelée firmware AxeOS, fournit aux utilisateurs une interface de gestion complète pour surveiller et contrôler leurs appareils de minage.


Le processus de construction de l'interface web commence par une navigation dans le répertoire du serveur HTTP au sein de la structure principale du référentiel, et plus précisément dans le sous-répertoire AxeOS. Cet emplacement contient l'application web basée sur Node.js qui nécessite l'installation de dépendances via la commande npm install. Le système de compilation suppose que Node.js est correctement installé sur le système de développement, car il s'agit d'une exigence fondamentale pour le processus de compilation de l'interface web.


Après l'installation des dépendances, la commande npm run build compile les composants de l'interface web, en créant les fichiers nécessaires qui seront intégrés dans le firmware de l'ESP32. Ce processus de compilation génère des ressources web optimisées qui fournissent les fonctionnalités de l'interface utilisateur tout en maintenant une utilisation efficace de la mémoire sur la plateforme ESP32. La réussite de cette étape de compilation est essentielle avant de passer à la compilation du micrologiciel principal, car le micrologiciel ESP-Miner incorpore ces composants d'interface web en tant que fonctionnalité intégrale.


### Création de fichiers d'usine avec configuration intégrée


La création de fichiers d'usine représente une stratégie de déploiement avancée qui intègre les paramètres de configuration directement dans le binaire du micrologiciel, éliminant ainsi la nécessité d'une configuration manuelle lors de l'installation de l'appareil. Cette approche s'avère particulièrement précieuse pour les déploiements à grande échelle ou pour les situations où une configuration cohérente sur plusieurs appareils est essentielle.


Le processus de création du fichier d'usine commence par la génération d'un binaire de configuration à partir du fichier de configuration CSV à l'aide de l'outil NVS partition generator de l'ESP-IDF. Cet outil, situé dans le répertoire des composants de l'ESP-IDF sous nvs-flash/nvs-partition-generator, convertit la configuration lisible par l'homme en un format binaire adapté au stockage direct en mémoire flash. Le script nvs-partition-gen.py traite le fichier config.csv et génère un fichier config.binary qui cible l'espace d'adressage mémoire 0x6000.


L'assemblage final des fichiers d'usine utilise des scripts de fusion spécialisés qui combinent les binaires du micrologiciel de base avec les données de configuration. Le référentiel propose plusieurs options de fusion, notamment un script de fusion standard pour les fichiers d'usine de base et un script de fusion incluant la configuration pour les fichiers d'usine complets. Le script merge-bin-with-config.sh crée des fichiers d'usine qui incluent à la fois les fonctionnalités du micrologiciel et les paramètres préconfigurés, ce qui permet d'obtenir un ensemble complet de déploiement. Cette approche permet de créer des fichiers d'usine spécifiques aux appareils, tels que des versions adaptées aux appareils Bitaxe Ultra avec des révisions de cartes spécifiques, tout en conservant la flexibilité de générer des fichiers d'usine génériques sans configurations intégrées pour les scénarios nécessitant une flexibilité de configuration manuelle.


Les fichiers d'usine complétés fournissent aux équipes de déploiement des binaires prêts à être flashés qui incluent tous les composants du micrologiciel et les paramètres de configuration nécessaires, rationalisant ainsi le processus d'approvisionnement des appareils et garantissant des paramètres opérationnels cohérents pour tous les appareils de minage déployés.


## Comment utiliser le Bitaxe Web Flasher ?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Le programe d'installation Web Bitaxe représente une approche rationalisée de la gestion des microprogrammes pour les appareils Bitaxe, offrant aux utilisateurs de multiples options d'installation par le biais d'une interface basée sur le web. Cet outil complet élimine la complexité traditionnellement associée aux mises à jour de micrologiciels et aux nouvelles installations, rendant la gestion des appareils accessible aux utilisateurs quelle que soit leur expertise technique. Il est essentiel de comprendre l'utilisation correcte de cet installateur pour maintenir les performances optimales des appareils et éviter les pièges courants qui peuvent rendre les appareils temporairement inopérants.


### Exigences en matière d'accès et de compatibilité des navigateurs


L'installateur web Bitaxe est accessible via l'URL dédiée [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (celle présentée dans la vidéo est désormais obsolète), servant de centre pour toutes les activités d'installation de microprogrammes. Cependant, le bon fonctionnement de cet outil web nécessite la compatibilité du navigateur, car l'installateur s'appuie sur des technologies web spécifiques qui ne sont pas universellement supportées par tous les navigateurs. Chrome est le principal navigateur recommandé pour le programme d'installation, parce qu'il offre une compatibilité totale avec toutes les caractéristiques et fonctions. Bien que d'autres navigateurs basés sur Chromium puissent offrir des fonctionnalités similaires, des alternatives populaires telles que Brave et Firefox ne prennent pas en charge la série web API nécessaire, ce qui les rend incompatibles avec les opérations de base de l'installateur.


Cette limitation du navigateur provient du fait que l'installateur s'appuie sur la communication série directe avec les appareils Bitaxe par l'intermédiaire de l'interface web. L'interface web API, qui permet cette communication, reste une norme web relativement nouvelle qui n'a pas encore été adoptée par tous les navigateurs. Les utilisateurs qui tentent d'accéder au programme d'installation à l'aide de navigateurs non pris en charge rencontreront des échecs de connexion et l'impossibilité de communiquer avec leurs appareils, ce qui nécessitera de passer à un navigateur compatible avant de procéder à toute activité d'installation.


### Exigences en matière d'alimentation et préparation de l'appareil


Les appareils Bitaxe ont des besoins en énergie différents en fonction de leur modèle et de leur version, ce qui fait qu'une bonne gestion de l'énergie est essentielle à la réussite de l'installation du micrologiciel. Les appareils fonctionnant avec la version 204 ou inférieure peuvent fonctionner uniquement grâce à l'alimentation USB, en tirant suffisamment de courant de l'ordinateur connecté pour maintenir le fonctionnement pendant le processus de flashage. Ce dispositif d'alimentation simplifié rend ces versions antérieures particulièrement pratiques pour les mises à jour de microprogrammes, car les utilisateurs n'ont qu'à brancher un seul câble USB pour commencer le processus d'installation.


Toutefois, les appareils fonctionnant à partir de la version 205 nécessitent des sources d'alimentation externes en plus de la connexion USB, ce qui reflète les changements dans la consommation d'énergie et la conception des circuits dans les révisions matérielles plus récentes. Ces appareils ne peuvent pas être suffisamment alimentés par la seule connexion USB, ce qui nécessite de les connecter à leur alimentation électrique standard pendant l'installation du micrologiciel. Le fait de ne pas fournir une alimentation adéquate à ces nouveaux appareils entraînera des échecs d'installation et une corruption potentielle du processus de mise à jour du microprogramme.


Le processus de connexion physique nécessite un timing spécifique et une manipulation des boutons pour assurer une communication correcte entre l'installateur et l'appareil. Les utilisateurs doivent appuyer sur le bouton de démarrage de leur appareil Bitaxe et le maintenir enfoncé avant de connecter le câble USB-C à leur ordinateur. Cette séquence place l'appareil en mode bootloader, permettant à l'installateur de communiquer directement avec le stockage du micrologiciel de l'appareil. Connecter le câble USB avant d'enclencher le bouton de démarrage entraînera un fonctionnement normal de l'appareil plutôt que le mode bootloader requis pour l'installation du micrologiciel, empêchant l'installateur d'établir le canal de communication nécessaire.


### Options d'installation et leurs applications


L'installateur Web Bitaxe propose quatre options d'installation distinctes, chacune conçue pour des cas d'utilisation et des configurations d'appareils spécifiques. La version 4.0.1 de la carte Bitaxe Superboard représente le firmware le plus récent pour les appareils du modèle Super, la version 4.0.2 étant prévue pour une publication future. Cette option comprend des variantes d'usine et de mise à jour, offrant une flexibilité dans l'approche de l'installation en fonction des besoins de l'utilisateur et de l'état de l'appareil.


Les installations d'usine représentent des remplacements complets de microprogrammes qui reflètent le processus de fabrication d'origine, y compris des procédures d'autotest complètes qui vérifient le fonctionnement de l'appareil dans tous les systèmes. Lorsque les utilisateurs choisissent une installation d'usine, l'installateur procède à un effacement complet des microprogrammes et des données de configuration existants et les remplace par une nouvelle installation propre, identique à celle qui serait appliquée lors de la fabrication. Ce processus comprend un auto-test automatisé qui valide le bon fonctionnement du matériel, ce qui oblige les utilisateurs à redémarrer leur appareil avant qu'il ne reprenne son fonctionnement normal. Les installations d'usine s'avèrent particulièrement utiles lorsque les appareils rencontrent des problèmes persistants ou lorsque les utilisateurs souhaitent rétablir les spécifications d'origine de leur appareil.


Les installations de mise à jour offrent une approche plus conservatrice, préservant les données de configuration existantes tout en ne mettant à jour que les principaux composants du micrologiciel. Cette option est idéale pour les utilisateurs qui ont personnalisé les paramètres de leur appareil et qui souhaitent conserver leurs configurations personnelles tout en bénéficiant des améliorations du micrologiciel et des corrections de bogues. Le processus de mise à jour ne cible que les composants du micrologiciel qui nécessitent une modification, laissant les paramètres spécifiques à l'utilisateur, les identifiants Wifi et les adresses Bitcoin intacts tout au long du processus d'installation.


### Considérations critiques sur l'installation et la protection des données


La distinction entre les installations d'usine et les mises à jour a des implications significatives pour la configuration de l'appareil et la préservation des données de l'utilisateur. Les installations d'usine effacent complètement l'appareil, supprimant tous les paramètres configurés par l'utilisateur, y compris les identifiants Wifi, les adresses Bitcoin et tous les paramètres personnalisés de l'appareil. Après une installation d'usine, les utilisateurs doivent se reconnecter au réseau Wifi par défaut de l'appareil et reconfigurer tous les paramètres personnels à partir de zéro, ce qui revient à traiter l'appareil comme s'il était neuf, c'est-à-dire comme s'il provenait du fabricant.


Les installations de mises à jour requièrent une attention particulière à l'option d'effacement de l'appareil présentée au cours du processus d'installation. Le programme d'installation posera aux utilisateurs la question "Voulez-vous effacer l'appareil avant d'installer Bitaxe Flasher ?", accompagnée d'un avertissement indiquant que toutes les données de l'appareil seront perdues. Les utilisateurs effectuant des installations de mise à jour doivent refuser cette option en cliquant sur "Suivant" plutôt que de confirmer l'opération d'effacement. L'acceptation de l'option d'effacement au cours d'une installation de mise à jour supprimera le fichier de configuration de l'appareil, ce qui risque de rendre l'appareil inutilisable jusqu'à ce qu'une configuration correcte soit rétablie. Bien que cette situation n'endommage pas l'appareil de manière permanente, elle crée des complications inutiles et nécessite des étapes de configuration supplémentaires pour rétablir un fonctionnement normal.


Le processus d'installation proprement dit se déroule automatiquement une fois que les utilisateurs ont fait et confirmé leurs choix. Le programme d'installation prend en charge tous les aspects techniques du transfert et de la vérification des microprogrammes, en fournissant des indicateurs de progression et des mises à jour de l'état tout au long du processus. Cette approche automatisée évite aux utilisateurs d'avoir à comprendre des procédures complexes d'installation de micrologiciels, tout en garantissant des résultats fiables et cohérents pour différents modèles d'appareils et versions de micrologiciels.


## Comment créer et commander le PCB ?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Ce chapitre se concentre sur le processus pratique de génération de fichiers de fabrication à partir de projets KiCad et de commande de circuits imprimés professionnels auprès de fabricants en ligne. En utilisant le projet Bitaxe comme exemple, nous allons parcourir le flux de travail complet, de la génération de fichiers à la passation d'une commande auprès d'un fabricant de circuits imprimés.


### Comprendre le processus de fabrication des circuits imprimés


Le passage d'une conception KiCad achevée à un circuit imprimé physique implique plusieurs étapes critiques qui comblent le fossé entre la conception numérique et la fabrication physique. Lorsque vous travaillez sur des projets complexes comme le Bitaxe, l'éditeur de PCB de KiCad fournit une vue d'ensemble de votre conception, affichant tous les composants et leurs interconnexions par le biais de traces colorées. Les lignes rouges et bleues que vous voyez représentent les connexions électriques entre les différents circuits intégrés et composants de la carte. La fonction de visualisation 3D de KiCad vous permet de visualiser l'aspect final de la carte assemblée, ce qui vous donne un aperçu précieux de l'emplacement des composants et des conflits mécaniques potentiels.


Le processus de fabrication nécessite des formats de fichiers spécifiques que les fabricants de PCB peuvent interpréter et utiliser pour fabriquer vos cartes. Ces fichiers contiennent des informations précises sur les couches de cuivre, les trous de perçage, l'emplacement des composants et d'autres spécifications de fabrication. Il est essentiel de comprendre ce flux de travail, que vous travailliez avec la conception standard de Bitaxe ou que vous créiez des modifications telles que l'ajout de logos personnalisés, la modification de la valeur des composants ou l'ajustement de la disposition de la carte pour répondre à des exigences spécifiques.


### Génération de fichiers Gerber pour la fabrication


Les fichiers Gerber constituent la norme industrielle pour la communication des informations relatives à la conception des circuits imprimés aux fabricants. Ces fichiers contiennent toutes les données nécessaires à la fabrication de votre PCB, y compris les motifs des couches de cuivre, les définitions des masques de soudure et les emplacements des trous de perçage. Pour générer ces fichiers dans KiCad, naviguez vers l'éditeur de PCB et accédez aux sorties de fabrication via le menu Fichiers. Le logiciel configure automatiquement les paramètres appropriés pour les processus de fabrication standard, y compris la structure de répertoire de sortie appropriée, généralement organisée sous la forme de "fichiers de fabrication/gerbers"


Le processus de génération crée plusieurs fichiers Gerber, chacun représentant différents aspects de la conception de votre PCB. Ces fichiers se combinent pour fournir aux fabricants des instructions de fabrication complètes. Une fois générés, ces fichiers doivent être compressés dans une archive ZIP, car il s'agit du format standard attendu par la plupart des fabricants de circuits imprimés. Le fichier ZIP contient toutes les données de fabrication nécessaires et garantit qu'aucun fichier n'est perdu ou corrompu pendant le processus de téléchargement vers le site web du fabricant.


Il est intéressant de noter que de nombreux projets open source, y compris le Bitaxe, incluent souvent des fichiers de fabrication pré-générés dans leurs dépôts. Cependant, il est essentiel de comprendre comment générer soi-même ces fichiers lors de modifications de la conception ou de l'utilisation de différentes versions de cartes. Cette connaissance est particulièrement précieuse pour personnaliser les conceptions ou résoudre les problèmes de fabrication.


### Sélectionner les fabricants de circuits imprimés et comprendre les options


Le paysage de la fabrication de circuits imprimés offre plusieurs options réputées, JLCPCB et PCBWay figurant parmi les choix les plus populaires pour les amateurs comme pour les professionnels. Les deux fabricants proposent des services similaires à des prix compétitifs et une qualité fiable, bien que chacun présente des avantages spécifiques en fonction des exigences de votre projet. JLCPCB attire souvent les nouveaux utilisateurs grâce à des prix promotionnels et à des interfaces conviviales, tandis que PCBWay peut proposer différentes options de matériaux ou des services spécialisés.


Lorsque vous téléchargez vos fichiers Gerber sur le site web d'un fabricant, le système analyse automatiquement votre conception et vous présente différentes options de fabrication. Les paramètres par défaut fournis par ces plateformes conviennent généralement à la plupart des conceptions standard, et il est généralement recommandé de conserver ces paramètres, à moins que vous n'ayez des exigences spécifiques. Les paramètres clés sont l'épaisseur du circuit imprimé, le poids du cuivre, l'état de surface et les quantités minimales. La plupart des fabricants exigent des commandes minimales de cinq cartes, ce qui convient parfaitement aux projets d'amateurs pour lesquels il est utile d'avoir des cartes de rechange ou de partager avec des amis.


Les options de couleur représentent l'un des rares choix esthétiques disponibles au cours du processus de fabrication. Si le vert reste l'option traditionnelle et la plus rentable, les fabricants proposent généralement des alternatives telles que le bleu, le rouge, le jaune, le violet et le noir. Le choix de la couleur est purement esthétique et n'affecte pas les performances électriques de votre PCB, bien que certaines couleurs puissent avoir de légères implications en termes de coûts ou de temps de fabrication.


### Considérations relatives à la fabrication avancée et options d'assemblage


Au-delà de la fabrication de base des circuits imprimés, les fabricants modernes offrent des services supplémentaires qui peuvent rationaliser de manière significative l'achèvement de votre projet. Les pochoirs représentent l'un des services complémentaires les plus précieux, en particulier pour les conceptions comportant des composants à pas fin, comme les puces ASIC que l'on trouve dans les projets de minage de bitcoin. Un pochoir est essentiellement un gabarit en aluminium découpé avec précision et dont les ouvertures correspondent exactement aux emplacements des pastilles de soudure sur votre circuit imprimé. Cet outil permet une application cohérente et précise de la pâte à souder, ce qui améliore considérablement la qualité de l'assemblage et réduit la probabilité d'erreurs de soudure.


Les options de pochoir comprennent généralement des pochoirs uniques avec des motifs supérieurs et inférieurs, ou des pochoirs séparés pour chaque côté de la planche. Pour la plupart des projets, un pochoir combiné s'avère plus pratique et plus rentable. L'épaisseur du pochoir est soigneusement calculée pour déposer la quantité appropriée de pâte à souder pour vos types de composants et tailles de pastilles spécifiques. L'utilisation d'un pochoir transforme ce qui pourrait être un processus manuel fastidieux et sujet aux erreurs en une étape d'assemblage rapide et professionnelle.


Bien que certains fabricants proposent des services d'assemblage partiel ou complet, ces options doivent être soigneusement étudiées pour des projets complexes tels que le Bitaxe. La disponibilité des composants, les implications financières et la valeur éducative de l'auto-assemblage sont autant de facteurs qui entrent en ligne de compte dans cette décision. De nombreux composants spécialisés requis pour les projets de minage de bitcoin peuvent ne pas être facilement disponibles auprès des services d'assemblage de PCB standard, ce qui fait de l'approvisionnement en composants et de l'assemblage manuel l'approche la plus pratique. Les prochains épisodes de cette série traiteront des stratégies d'approvisionnement en composants et des techniques d'assemblage pour vous aider à mener à bien votre projet Bitaxe, du circuit imprimé nu à l'appareil fonctionnel.


Le processus de fabrication et d'assemblage représente un pont crucial entre la conception numérique et la mise en œuvre physique. La compréhension de ces flux de travail vous permet de prendre le contrôle de vos projets, de réduire les coûts et d'acquérir une expérience pratique précieuse des processus de fabrication professionnels. Que vous construisiez un prototype unique ou que vous planifiez une petite production, la maîtrise de ces compétences vous ouvre de nouvelles possibilités pour donner vie à vos conceptions électroniques.


# Optimisation des performances

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Benchmarking de votre Bitaxe

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

La recherche d'une performance optimale de minage nécessite une approche systématique de la configuration matérielle qui équilibre le hashrate, l'efficacité et la gestion thermique. Les Bitaxe offrent de nombreux paramètres de configuration qui peuvent avoir un impact significatif sur les performances, mais tester manuellement chaque combinaison de paramètres serait peu pratique et prendrait beaucoup de temps. Ce chapitre explique comment utiliser des outils d'analyse comparative automatisés pour optimiser scientifiquement les performances de votre Bitaxe tout en maintenant des conditions de fonctionnement sûres.


### Comprendre les mesures de performance de Bitaxe et la configuration de la ligne de base


Avant de se plonger dans les techniques d'optimisation, il est essentiel de comprendre les indicateurs de performance clés qui définissent l'efficacité opérationnelle de votre Bitaxe. Les principales mesures comprennent le hashrate mesuré en térahash par seconde, l'efficacité énergétique exprimée en joules par térahash, la fréquence ASIC en mégahertz et la tension du cœur en volts. Un Bitaxe bien configuré pourrait atteindre environ 1,1 térahash avec un rendement d'environ 17 joules par térahash, fonctionnant à 550 mégahertz avec une tension ASIC mesurée de 1,14 volt. Ces chiffres de base fournissent un point de référence pour comprendre les améliorations potentielles disponibles grâce à une optimisation systématique.


La relation entre ces paramètres est complexe et interdépendante. Des fréquences plus élevées augmentent généralement le hashrate, mais aussi la consommation d'énergie et la production de chaleur. De même, les ajustements de tension affectent à la fois les performances et les caractéristiques thermiques. Le défi consiste à trouver l'équilibre optimal qui maximise soit le hashrate, soit l'efficacité, tout en maintenant un fonctionnement stable dans des limites de température sûres. Ce processus d'optimisation nécessite des tests méthodiques sur de multiples combinaisons de paramètres, ce qui rend les outils automatisés inestimables pour obtenir des résultats optimaux.


### Architecture de l'outil de référence Bitaxe Hashrate


L'outil [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) est une solution sophistiquée basée sur Python, développée à l'origine par White Cookie et améliorée par la suite par mrv777. Cet outil open source, distribué sous licence GPLv3, automatise le processus complexe de test de multiples combinaisons de configurations afin d'identifier les paramètres optimaux pour votre matériel spécifique. La principale force de l'outil réside dans son approche systématique du test des paramètres, en ajustant progressivement les paramètres de fréquence et de tension tout en surveillant continuellement les mesures de performance et les conditions thermiques.


Le processus d'évaluation comparative dure généralement de 30 à 40 minutes, au cours desquelles l'outil teste méthodiquement diverses combinaisons de paramètres de fréquence et de tension ASIC. L'outil commence par des réglages de base conservateurs, généralement à 1,15 volt et 500 mégahertz, puis augmente progressivement ces paramètres tout en surveillant le hashrate, la température et la stabilité. Il est important de noter que l'outil donne la priorité à un fonctionnement sûr plutôt qu'à des performances maximales, en revenant automatiquement sur les paramètres qui provoquent une génération de chaleur excessive ou une instabilité. Cette approche conservatrice garantit que le processus d'optimisation ne compromet pas la longévité ou la fiabilité du matériel.


### Exigences en matière d'installation et de configuration


La mise en œuvre de l'outil Bitaxe Hashrate Benchmark nécessite plusieurs composants logiciels prérequis sur votre ordinateur local. Il s'agit principalement de Python pour l'exécution des scripts de benchmarking, de Git pour la gestion du dépôt et, en option, de Visual Studio Code pour l'amélioration des capacités de l'environnement de développement. Bien que l'outil puisse être utilisé à partir d'interfaces de ligne de commande, l'utilisation d'un environnement de développement intégré tel que VS Code offre une meilleure visibilité sur le processus d'analyse comparative et l'analyse des résultats.


Le processus d'installation suit les pratiques de développement Python standard, en commençant par cloner le dépôt de GitHub sur votre machine locale. Une fois le dépôt téléchargé, vous devrez créer un environnement virtuel pour isoler les dépendances de l'outil de l'installation Python de votre système. Cette isolation évite les conflits potentiels avec d'autres applications Python et garantit un fonctionnement cohérent. Après avoir activé l'environnement virtuel, vous installerez les dépendances requises à l'aide du fichier d'exigences fourni, qui configure automatiquement toutes les bibliothèques et tous les modules nécessaires au bon fonctionnement de l'outil.


### Exécution des analyses comparatives et interprétation des résultats


L'exécution du benchmark nécessite l'exécution d'une seule commande Python qui inclut l'adresse IP de votre Bitaxe en tant que paramètre. L'outil se connecte automatiquement à l'interface web de votre mineur et commence le processus de test systématique. Pendant l'exécution, l'outil fournit des informations de journalisation détaillées montrant l'itération de test actuelle, les paramètres de tension et de fréquence appliqués, le hashrate résultant, la tension d'entrée, les relevés de température et les données thermiques des composants critiques comme le convertisseur buck. Ce retour d'information en temps réel vous permet de suivre la progression de l'analyse comparative et de comprendre comment les différents paramètres affectent les performances de votre mineur.


La gestion thermique intelligente de l'outil devient évidente lorsque les températures approchent le seuil de sécurité de 66 degrés Celsius. Plutôt que de dépasser les limites de sécurité, le benchmark réduit automatiquement les paramètres pour maintenir la stabilité thermique. Cette approche conservatrice garantit que le processus d'optimisation donne la priorité à la fiabilité à long terme du matériel plutôt qu'aux gains de performance à court terme. Une fois terminé, l'outil génère des résultats complets au format JSON, classant les cinq configurations les plus performantes en termes de hashrate et d'efficacité optimale. Ces résultats fournissent des conseils clairs pour sélectionner la configuration qui correspond le mieux à vos priorités opérationnelles, qu'il s'agisse d'une production maximale ou d'une efficacité énergétique.


L'outil d'analyse comparative offre également des options de personnalisation pour les utilisateurs avancés qui souhaitent modifier les paramètres de test. Les arguments de la ligne de commande vous permettent de spécifier des tensions et des fréquences de départ personnalisées, ce qui permet une optimisation plus ciblée pour des cas d'utilisation spécifiques. Par exemple, si vous savez déjà que votre matériel fonctionne bien à des fréquences plus élevées, vous pouvez lancer le benchmark avec des paramètres élevés plutôt que de commencer avec les valeurs par défaut conservatrices. Cette flexibilité rend l'outil précieux à la fois pour les utilisateurs novices à la recherche d'une optimisation automatisée et pour les mineurs expérimentés qui souhaitent affiner les caractéristiques de performance spécifiques.


## Overclocker votre Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

L'overclocking d'un appareil Bitaxe nécessite de prendre en compte les limitations matérielles et les besoins en refroidissement. Bien que de nombreux utilisateurs préfèrent sous-cadencer leurs appareils pour un fonctionnement plus silencieux, il est essentiel de comprendre les techniques d'overclocking appropriées pour ceux qui recherchent des performances maximales sans endommager leur matériel. Le processus consiste à augmenter la fréquence et éventuellement à ajuster les paramètres de tension au-delà des spécifications d'usine, ce qui augmente intrinsèquement la production de chaleur et le stress sur les composants.


La base d'un overclocking réussi repose sur une infrastructure de refroidissement adéquate. Avant d'essayer de modifier la fréquence, vous devez vous assurer que votre Bitaxe dispose de capacités de dissipation thermique adéquates. Un Bitaxe Gamma avec un dissipateur et un ventilateur de qualité fournit la gestion thermique nécessaire pour un overclocking sûr. Les appareils dotés de petits dissipateurs et de ventilateurs inadéquats ne doivent pas être overclockés, car une mauvaise performance de refroidissement conduira à un étranglement thermique et à des dommages matériels potentiels. Il est essentiel de comprendre la relation entre la chaleur et la longévité des composants : une chaleur excessive crée un stress qui dégrade les composants électroniques au fil du temps, réduisant ainsi de manière significative la durée de vie opérationnelle de votre appareil.


### Placement stratégique du dissipateur thermique


Le composant le plus critique nécessitant un refroidissement supplémentaire est le convertisseur buck, un petit composant noir situé à l'arrière du Bitaxe près de la grande bobine. Ce dispositif convertit l'alimentation électrique de 5 V en une tension appropriée pour la puce ASIC, typiquement autour de 1,2 V. Le convertisseur buck, souvent appelé TPS, génère une chaleur importante pendant son fonctionnement et représente un goulot d'étranglement thermique qui limite le potentiel d'overclocking. L'installation d'un petit dissipateur thermique adhésif sur ce composant permet non seulement d'augmenter la marge d'overclocking, mais aussi d'améliorer l'efficacité globale en réduisant les pertes thermiques.


La mise en place d'un dissipateur thermique supplémentaire peut être bénéfique pour d'autres zones de la carte où le courant est élevé. Le circuit de régulation de la tension subit des contraintes électriques importantes lorsque l'énergie circule de la section d'entrée jusqu'à la puce ASIC en passant par les différentes pistes de la carte. De nombreux overclockers expérimentés installent des dissipateurs sur la face avant du Bitaxe dans ces zones à fort courant afin d'améliorer la dissipation thermique. Bien qu'elles ne soient pas strictement nécessaires pour un overclocking modéré, ces mesures de refroidissement supplémentaires deviennent importantes lorsque les fréquences sont poussées à des niveaux extrêmes.


### Considérations et limites du système de refroidissement


Le contrôleur ESP32, visible comme le composant argenté sur la carte, ne nécessite généralement pas de refroidissement supplémentaire. Ce composant génère peu de chaleur de manière autonome et ne s'échauffe qu'en raison du transfert thermique des composants environnants. L'installation de dissipateurs thermiques à proximité de l'ESP32 peut interférer avec l'antenne Wi-Fi adjacente, dégradant ainsi la connectivité sans fil et la qualité du signal. Concentrez vos efforts de refroidissement sur les composants de régulation de puissance et la zone ASIC plutôt que sur le circuit de contrôle.


Les configurations à double ventilateur présentent à la fois des opportunités et des limites. Bien que l'ajout d'un second ventilateur pour souffler de l'air à l'arrière du Bitaxe puisse améliorer les performances de refroidissement, le firmware de l'appareil ne peut contrôler correctement qu'un seul ventilateur. Le Bitaxe possède deux têtes de ventilateur, mais un seul contrôleur de ventilateur, ce qui signifie que la connexion de deux ventilateurs perturbera le firmware qui recevra des signaux RPM contradictoires. Cette configuration fonctionnera, mais peut entraîner un comportement imprévisible du contrôle des ventilateurs.


### Évaluation des performances de base


Avant de tenter toute modification d'overclocking, établissez des mesures de performance de base en faisant fonctionner votre Bitaxe avec les paramètres de base pendant plusieurs heures. Surveillez la température du ASIC, la température du régulateur de tension et le pourcentage de vitesse du ventilateur via l'interface web. Les températures de fonctionnement optimales doivent maintenir le ASIC en dessous de 60° C et le régulateur de tension en dessous de 60° C dans des conditions normales. Si votre appareil fonctionne déjà à plus de 65° C pour le ASIC ou à plus de 70-80° C pour le régulateur de tension dans les réglages d'origine, il est nécessaire d'ajouter du matériel de refroidissement avant de procéder à l'overclocking.


L'approche systématique de l'augmentation de la fréquence consiste à procéder par étapes en utilisant les options de fréquence prédéfinies dans le menu des paramètres. Commencez par sélectionner le prochain pas de fréquence disponible au-dessus de votre réglage actuel tout en conservant la tension par défaut du noyau. Cette approche conservatrice vous permet d'évaluer les impacts thermiques et de stabilité avant de procéder à des changements supplémentaires. Laissez l'appareil fonctionner à chaque nouveau réglage de fréquence pendant au moins 30 minutes à une heure, en surveillant les tendances de la température et la stabilité du taux de hachage tout au long de la période d'évaluation.


### Configuration personnalisée avancée


Pour accéder aux réglages personnalisés de fréquence et de tension, il faut activer l'interface d'overclocking avancée en ajoutant "?OC" à l'URL de l'interface web de l'appareil. Cela permet de déverrouiller les champs de saisie manuelle pour un contrôle précis de la fréquence et de la tension, accompagné d'avertissements appropriés sur les risques liés à un fonctionnement en dehors des paramètres prévus. L'interface personnalisée permet un réglage fin au-delà des étapes de fréquence standard, ce qui permet aux utilisateurs expérimentés d'optimiser les performances en fonction de leurs configurations de refroidissement spécifiques.


Lors de l'utilisation de réglages personnalisés, il convient de conserver des incréments prudents de 10 à 15 MHz par étape de réglage. Cette approche méthodique évite les pics thermiques soudains et permet de tester correctement la stabilité à chaque niveau de fréquence. Certains utilisateurs avancés atteignent des fréquences de l'ordre de 700 MHz avec des tensions de cœur réglées à 1,175 V ou à des valeurs similaires, mais ces réglages extrêmes nécessitent des modifications importantes du refroidissement et une surveillance attentive. Le régulateur de tension peut fonctionner à des températures allant jusqu'à 100° C sans dommage immédiat, mais des températures plus élevées réduisent l'efficacité et la fiabilité à long terme. Un overclocking réussi exige de la patience, des tests systématiques et une surveillance continue pour obtenir des améliorations stables des performances tout en préservant l'intégrité du matériel.


# Section finale

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Évaluer ce cours

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusion

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>
