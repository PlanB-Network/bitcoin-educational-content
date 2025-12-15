---
name: Electrum Airgap
description: Un premier pas vers la sécurité, un cold wallet avec Electrum
---
![cover](assets/cover.webp)

## Cold Wallet

Dans ce tutoriel, je vais t’expliquer comment réaliser ton premier dispositif de signature airgap, totalement déconnecté d’Internet, même sans posséder de hardware wallet dédié. Tout ce dont tu as besoin, c’est de deux ordinateurs :
- un ancien appareil auquel tu interdiras définitivement toute connexion à Internet ;
- ton ordinateur d’utilisation quotidienne.

Cette configuration permet d’obtenir un degré de sécurité supérieur par rapport à un simple `hot wallet` : l’ancien ordinateur – sans connexion au réseau – conserve tes clés privées, qui ne sont jamais exposées en ligne, mais bien gardées hors ligne (« airgap » ou « cold »).

Sur ton ordinateur principal, tu installeras en revanche un wallet de visualisation (« watch-only »), connecté à Internet et qui te permettra, par exemple, de consulter le solde et de préparer les transactions de réception.

## Wallet Airgap : Quoi et Comment

En suivant les étapes de ce guide, nous installerons deux logiciels Electrum sur deux ordinateurs distincts et, finalement, nous créerons deux wallets avec des keystore différents :  
- le wallet airgap utilisera toute la hiérarchie du wallet HD ;  
- le wallet de visualisation sera généré à partir de la clé publique master.

Ces deux wallets seront très différents l’un de l’autre. La seule chose qu’ils auront en commun, comme nous le verrons, ce sont les adresses :
- le wallet sur l’ordinateur airgap peut uniquement signer mais, déconnecté du réseau, il ne connaît ni le solde ni les adresses utilisées ;
- le wallet sur l’ordinateur quotidien peut uniquement préparer et diffuser des transactions, sans pouvoir dépenser les fonds, faute de posséder les clés privées.

## Préparation Préliminaire

Pour télécharger Electrum, je te conseille de suivre les premiers pas de ce tutoriel :

https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Après le téléchargement, vérifie toujours la release avant de l’installer, puis procède à la configuration « One Server », comme indiqué dans la section du guide au chapitre `Commence avec un wallet fictif`.

L’opération de configuration « One Server » est nécessaire uniquement pour le wallet installé sur l’ordinateur quotidien, puisque l’autre appareil restera toujours hors ligne.

Les étapes suivantes doivent être effectuées sur deux ordinateurs (et wallets) différents. Pour plus de clarté et de praticité, j’ai choisi de configurer le wallet airgap avec le thème clair, tandis que le wallet de visualisation utilise le thème sombre.

## Création du Wallet Airgap

Après avoir téléchargé et vérifié Electrum, copie l’exécutable et transfère-le sur l’ordinateur hors ligne. Lance-le ensuite et installe Electrum.

Avec un double clic, démarre Electrum : l’ordinateur sur lequel tu utilises ce wallet est hors ligne, ignore donc les paramètres réseau et procède directement à la création du wallet que, dans ce guide, nous appellerons `airgap`.

![image](assets/en/01.webp)

Choisis _Standard wallet_.

![image](assets/en/02.webp)

Puis sélectionne _Create a new seed_ pour générer la phrase mnémotechnique via le logiciel.

![image](assets/en/03.webp)

Transcris soigneusement les 12 mots générés par Electrum sur un support papier et procède à la vérification en les ressaisissant dans l’ordre, lorsque le logiciel te le demande.

![image](assets/en/04.webp)

![image](assets/en/05.webp)

À la fin de la création du wallet, définis un mot de passe complexe (`Strong`) afin de chiffrer le fichier du wallet sur l’appareil airgap. Ce passage est très délicat et essentiel, car le mot de passe choisi à ce stade empêche tout accès au wallet qui détient la capacité de dépenser les fonds et de signer les transactions.

![image](assets/en/06.webp)

En cliquant sur _Finish_, le wallet est créé et s’affiche à l’écran. Naturellement, l’indicateur de connexion réseau, représenté par le point coloré en bas à droite, est rouge, puisque l’ordinateur est déconnecté et que le wallet ne peut exposer aucune clé en ligne.

![image](assets/en/07.webp)

## Création du Wallet de Visualisation

Désormais, tes clés privées sont hors ligne. Il te faut préparer un wallet de visualisation, ou `watch-only`, qui te permettra de consulter le solde et de générer des transactions de réception afin de continuer à accumuler des sats en toute sécurité.

Depuis le wallet installé sur l’appareil hors ligne, choisis le menu _Wallet_ -> _Information_

![image](assets/en/08.webp)

Une fenêtre s’ouvre avec toutes les informations de ton wallet, où tu peux vérifier le `derivation path` et le `master fingerprint`, que tu peux noter à côté de ta phrase mnémotechnique (fortement recommandé).

![image](assets/en/09.webp)

Souviens-toi que ces données proviennent d’un ordinateur non connecté. Tu devras donc copier/coller la `zpub` dans un fichier texte et la sauvegarder sur une clé USB.

Tu peux maintenant passer à l’ordinateur connecté à Internet, lancer Electrum et créer un nouveau wallet.

Depuis le menu _File_, choisis _New/Restore_.

![image](assets/en/10.webp)

Le nouveau wallet est en lecture seule ; dans ce guide, nous l’appellerons `watch-only`.

![image](assets/en/12.webp)

À l’écran suivant, sélectionne _Standard wallet_ et clique sur _Next_.

![image](assets/en/13.webp)

Lors du choix du `Keystore`, fais attention : pour créer le wallet de visualisation, sélectionne _Use a master key_. Clique ensuite sur _Next_.

![image](assets/en/14.webp)

Colle ici la `zpub` copiée depuis le wallet hors ligne et transférée via clé USB.

![image](assets/en/15.webp)

Pour terminer, définis un mot de passe robuste également pour ce wallet, idéalement différent de celui du cold wallet correspondant.

Le wallet de visualisation apparaîtra avec un avertissement. Le message rappelle qu’il s’agit d’un wallet en lecture seule et qu’il est impossible de dépenser les fonds associés.

**Nota Bene** : **il sera donc toujours nécessaire de posséder les clés privées pour dépenser les UTXO de ce wallet**. Avec un bon système de sauvegarde, tu conserveras sans difficulté la pleine propriété de tes bitcoins.

![image](assets/en/16.webp)

Cet avertissement apparaîtra à chaque ouverture du wallet. Clique sur _Ok_ et passons à la vérification.

## Vérification des Deux Wallets

Comme nous l’avons appris au début de ce guide, un wallet airgap et son wallet de visualisation sont deux portefeuilles distincts, mais **partageant les mêmes adresses**.

Si nous les comparons côte à côte, on remarque que dans le wallet airgap figure l’icône du « seed », alors qu’elle n’apparaît pas dans le wallet watch-only. Ce détail te rappellera que le wallet de visualisation n’a pas les clés privées.

![image](assets/en/17.webp)

Pour une première vérification précise, sélectionne dans les deux wallets le menu `Addresses` : puisque les adresses sont partagées, la liste doit être identique dans les deux cas.

![image](assets/en/18.webp)

⚠️ **ATTENTION** : **il ne peut y avoir aucune différence ; les adresses doivent être strictement identiques. Si elles diffèrent, il est nécessaire de tout supprimer et de recommencer depuis le début**.

Tu peux maintenant effectuer deux vérifications supplémentaires. D’abord, supprime les deux wallets et restaure-les depuis zéro, chacun sur son ordinateur respectif. Pour le wallet de visualisation, les étapes sont identiques à celles décrites plus haut.

Pour le wallet airgap, en revanche, à l’écran du `keystore`, choisis _I already have a seed_ et saisis les mots depuis ta sauvegarde papier.

Une fois cette vérification « à blanc » terminée, tu peux effectuer une transaction avec un petit montant et la dépenser immédiatement.

## Transactions de Réception et de Dépense

Pour commencer à utiliser ton Electrum airgap, tu peux recevoir une petite somme, puis la dépenser vers une autre de tes adresses. Cela te permettra de te familiariser avec la procédure et de vérifier que tu as bien le contrôle de tes fonds.

**Note** : je te déconseille de déposer une somme importante sur le wallet tant que tu n’es pas certain de pouvoir exécuter toutes les opérations avec aisance.

Les étapes décrites ci-dessous peuvent sembler complexes de prime abord. Ne t’en inquiète pas : une fois la première tentative effectuée, tu verras qu’elles ne prennent que quelques minutes.

Pour recevoir des fonds, tu dois obligatoirement utiliser le wallet de visualisation sur ton ordinateur connecté. Depuis le menu `Receive`, clique sur _Create request_ pour que Electrum génère la première adresse disponible et utilise-la pour y envoyer quelques sats.

![image](assets/en/19.webp)

![image](assets/en/20.webp)

Une fois la transaction propagée, tu remarqueras – ce qui est normal – qu’elle est visible uniquement dans le wallet de visualisation et non dans le wallet airgap.

![image](assets/en/21.webp)

Après quelques confirmations, tu peux préparer une dépense et tester la procédure de signature sur le wallet hors ligne. Prépare la transaction sur le watch-only et clique sur _Preview_ pour la vérifier.

![image](assets/en/22.webp)

La fenêtre de transaction avancée apparaît et tu constates que :
- la transaction n’est pas signée (`Status: Unsigned`) ;
- les commandes `Sign` et `Broadcast` sont désactivées.

La seule opération possible est d’exporter la transaction telle quelle, afin de la transférer sur le wallet airgap pour signature.

Insère une clé USB dans ton ordinateur, puis depuis le menu en bas à gauche, choisis _Share_.

![image](assets/en/23.webp)

Sélectionne ensuite _Save to file_.

![image](assets/en/24.webp)

Sauvegarde la transaction sur la clé USB.

Tu remarqueras qu’Electrum attribue au fichier un nom reprenant les premiers caractères du transaction ID, avec l’extension `.psbt`, signifiant `Partially Signed Bitcoin Transaction`.

Retire ensuite la clé USB et insère-la dans l’ordinateur hors ligne.

Depuis le wallet airgap, sélectionne le menu _Tools_, puis _Load transaction_ et ensuite _From file_.

![image](assets/en/25.webp)

Avec le gestionnaire de fichiers, choisis le `.psbt` à l’endroit où tu l’as sauvegardé.

![image](assets/en/29.webp)

Le logiciel hors ligne ouvrira automatiquement la fenêtre de transaction avancée, identique à celle vue sur le wallet de visualisation. Le statut est `Unsigned`, mais cette fois la commande `Sign` est active. C’est précisément ce qu’il faut exécuter.

![image](assets/en/26.webp)

![image](assets/en/27.webp)

La transaction est maintenant signée, mais souviens-toi que ton wallet est sur une machine hors ligne. Même si le bouton `Broadcast` est actif, il est impossible de propager la transaction vers le réseau Bitcoin.

Il te faut donc exporter à nouveau la transaction signée sur la clé USB, afin de l’importer sur l’ordinateur connecté et de la diffuser.

Depuis le menu en bas à gauche, choisis encore _Share_ puis _Save to file_.

![image](assets/en/28.webp)

Le fichier a désormais une autre extension : **au lieu de `.psbt`, la transaction possède l’extension `.txn`. À partir de maintenant, Electrum distinguera ainsi les transactions signées des non signées**.

![image](assets/en/30.webp)

Pour propager définitivement la transaction, retire la clé USB de l’ordinateur hors ligne et insère-la dans celui connecté à Internet.

Depuis le wallet watch-only, répète l’importation en allant dans le menu _Tools_ -> _Load transaction_ -> _From file_.

![image](assets/en/31.webp)

Electrum ouvrira la fenêtre de transaction, cette fois différente de celle vue précédemment sur ce wallet, car elle est signée (`Status: Signed`) et le bouton `Broadcast` est accessible.

La dernière étape consiste précisément à cliquer sur ce bouton :

![image](assets/en/32.webp)

## Conclusions

Tes tests sont maintenant terminés. Si tu as suivi ce guide et obtenu les mêmes résultats, tu as créé un wallet cold avec Electrum, réparti sur deux ordinateurs distincts, que tu pourras utiliser en mode airgap pour conserver tes bitcoins.

Deux points demandent ton attention maximale :
1) **ne jamais utiliser le wallet airgap pour générer des adresses de réception**. Étant hors ligne, il proposera toujours la première adresse, qui correspond à celle utilisée pour la transaction de test ;

![image](assets/en/33.webp)

_Comme tu peux le constater sur l’image ci-dessus, le wallet hors ligne ignore totalement l’historique de ses adresses. Il est complètement aveugle de ce point de vue. **Son seul rôle est de conserver les clés hors ligne et de signer tes transactions**._

2) Utilise une clé USB dédiée uniquement à cet usage. **N’emploie pas un support que tu utilises fréquemment**. Les périphériques de stockage utilisés au quotidien présentent davantage de risques d’infection et, sans le vouloir, tu pourrais contaminer aussi l’ordinateur que tu maintiens déconnecté. Une clé USB réservée à cet usage n’aura que très rarement l’occasion d’être branchée à ton PC connecté, surtout si tu es un hodler qui dépense peu, ce qui réduit considérablement les risques de transmission de virus, malwares, etc.
