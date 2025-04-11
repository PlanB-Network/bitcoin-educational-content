---
name: Nakamochi
description: Node Running Made Easy - Comment configurer et utiliser Nakamochi Bitcoin et Lightning node.
---
L'exploitation de votre propre nœud Bitcoin et Lightning ne doit plus être une tâche complexe réservée aux experts techniques. Traditionnellement, la mise en place et la gestion des nœuds exigeaient des connaissances approfondies en cryptographie, en réseau et en développement de logiciels. Nakamochi change cela en rendant les nœuds accessibles à tous, quel que soit le bagage technique.

Avec Nakamochi, n'importe qui peut mettre en place et exploiter un nœud depuis son domicile, ce qui permet une totale confidentialité et une indépendance financière. L'exploitation d'un nœud complet permet non seulement de sécuriser ses propres transactions, mais aussi de contribuer à la solidité du réseau Bitcoin. Un réseau Bitcoin décentralisé et résistant repose sur une large distribution de nœuds pour garantir sa sécurité et son indépendance.

### Table des matières


- Qu'est-ce que le Nakamochi et comment fonctionne-t-il ?
- Mise en place de Nakamochi
- À propos du réseau Lightning
- Ouvrir des canaux et effectuer des transactions dans le Lightning Network

## Qu'est-ce que le Nakamochi et comment fonctionne-t-il ?

Nakamochi est un nœud complet exclusivement bitcoin qui prend en charge les réseaux Bitcoin et Lightning. Il comprend un portefeuille Bitcoin et Lightning intégré, permettant aux utilisateurs d'exécuter un nœud Bitcoin sécurisé et auto-souverain tout en bénéficiant de la vitesse et des faibles coûts de transaction du réseau Lightning.

Votre nœud Nakamochi est géré via une application mobile, [BitBanana (Android)](https://bitbanana.app) et [Zeus (iOS)](https://bitbanana.app), qui vous permet de le contrôler commodément depuis n'importe où. Ces applications agissent comme une télécommande pour votre nœud, vous permettant de payer directement avec Bitcoin ou Lightning, de gérer les transactions, d'ouvrir ou de fermer des canaux, de vérifier les soldes et de surveiller les performances de votre nœud, le tout en toute simplicité.

## L'installation de Nakamochi ne prend que 5 minutes

### Étape 1 : Se brancher et commencer

1. Connectez Nakamochi à l'alimentation électrique et au Wi-Fi.

2. Cliquez sur **"Créer un nouveau portefeuille "** et enregistrez en toute sécurité votre phrase de récupération de 24 mots.

3. Utilisez une application de gestion de nœuds (Zeus ou BitBanana) pour vous connecter à votre Nakamochi :

4. Ouvrez l'application et scannez le code QR affiché sur votre Nakamochi.

5. Pour plus de sécurité, définissez un code PIN sur votre appareil.

![image](assets/en/01.webp)

connectez-vous à l'électricité et écrivez votre phrase-clé de 24 mots

![image](assets/en/02.webp)

attendez que la blockchain ait rattrapé son retard

![image](assets/en/03.webp)

créer un nouveau portefeuille dans l'onglet "Lightning"

![image](assets/en/04.webp)

scanner le code QR avec l'application de gestion des nœuds

![image](asset/en/05.webp)

pour une plus grande sécurité, définissez un code PIN

**Note:** _Autorisez votre nœud Nakamochi à se synchroniser avec la blockchain. Ce processus peut prendre un certain temps en fonction de votre connexion internet

## À propos du réseau Lightning

Le Bitcoin Lightning Network révolutionne les transactions Bitcoin en les rendant plus rapides, moins chères et plus efficaces. Il est parfait pour une utilisation quotidienne, permettant des paiements quasi instantanés avec des frais minimes, idéal pour les microtransactions comme l'achat d'un café ou la gestion de petits achats fréquents.

En fonctionnant hors chaîne, Lightning est conçu pour s'adapter et prendre en charge des milliers de transactions par seconde sans surcharger la chaîne de blocs principale de Bitcoin. Cela en fait un acteur clé de l'évolution de Bitcoin vers un système de paiement pratique et mondial.

La confidentialité est un autre avantage, car les transactions sur Lightning sont acheminées par des canaux de paiement privés au lieu d'être enregistrées directement sur la blockchain. Cela permet d'effectuer des transactions plus discrètes tout en maintenant la sécurité robuste de Bitcoin.

#### Les canaux de paiement expliqués

Le réseau Lightning fonctionne grâce à des canaux de paiement, qui sont des connexions entre deux parties permettant des transactions multiples sans interagir directement avec la blockchain. Lorsqu'un canal est ouvert, le solde entre les deux parties est mis à jour sur cette solution Lightning de deuxième couche pour chaque transaction, ce qui garantit des paiements rapides et peu coûteux. Seules l'ouverture et la fermeture du canal sont enregistrées sur la chaîne, ce qui réduit l'encombrement de la blockchain Bitcoin. Cette conception garantit l'évolutivité et la confidentialité, car les transactions individuelles ne sont pas enregistrées dans le grand livre public.

**Exemple:** Alice et Bob ouvrent une chaîne en y engageant des bitcoins. Alice envoie des bitcoins à Bob, et leurs soldes hors chaîne sont mis à jour instantanément sans enregistrement sur la chaîne. Si Alice paie ensuite Charlie, et qu'Alice n'a pas de canal direct avec Charlie, le paiement peut être acheminé par le canal de Bob pour atteindre Charlie. L'acheminement par des nœuds intermédiaires garantit les paiements même en l'absence de connexions directes, ce qui rend le réseau très efficace.

## Ouvrir des canaux et effectuer des transactions dans le Lightning Network

Une fois votre Nakamochi configuré et connecté à une application de gestion de nœuds, vous pouvez commencer à utiliser le Lightning Network en ouvrant des canaux et en effectuant des transactions.

### Ouverture des chaînes sur Zeus (iOS) :

1. Allez dans l'onglet **"Channels "** (menu du bas).

2. Cliquez sur le **"+"** pour ouvrir un nouveau canal.

3. Scannez ou saisissez la clé publique du nœud auquel vous souhaitez vous connecter.

4. Saisissez le montant bloqué (choisissez avec votre homologue ou utilisez le montant fixe minimum pour les nœuds bien connus).

5. Cliquez sur **"Open Channel "**.

![image](asset/en/06.webp)

capture d'écran de ZEUS

Pour plus d'informations : [Canaux | Documentation Zeus](https://docs.zeusln.app/)

### Ouverture de chaînes sur BitBanana (Android) :

1. Ouvrez le menu hamburger (à gauche).

2. Allez dans **"Chaînes "**.

3. Cliquez sur le **"+"** pour ajouter/ouvrir un nouveau canal.

4. Scannez ou collez la clé publique.

5. Saisissez le montant bloqué (choisissez avec votre homologue ou utilisez le montant fixe minimum pour les nœuds bien connus).

![image](asset/en/07.webp)

capture d'écran de Bitbanana

Pour plus d'informations : [BitBanana] (https://bitbanana.com)

Une fois que votre canal est ouvert, les paiements peuvent être acheminés vers d'autres participants du réseau. Les soldes sont ajustés en dehors de la chaîne, ce qui garantit que les transactions sont presque instantanées et n'entraînent que des frais minimes.

Si vous n'avez plus besoin d'un canal, vous pouvez le fermer. Cette action permet de régler le solde final entre vous et votre homologue et de l'enregistrer sur la chaîne. Dans l'idéal, les deux parties sont d'accord et sont en ligne pour une "clôture coopérative" (plus rapide et avec moins de frais qu'une "clôture forcée" avec un pair qui ne répond pas ou qui n'est pas en ligne).

En règle générale, nous recommandons de laisser les canaux ouverts afin de réduire les coûts et d'accroître la fiabilité et l'efficacité du réseau. En laissant les canaux ouverts, vous minimisez les frais de transaction sur la chaîne, vous évitez les temps d'arrêt liés aux reconnexions des canaux et vous maintenez une capacité d'acheminement stable pour un traitement transparent des paiements. Cette approche favorise un réseau robuste et résilient tout en améliorant l'expérience globale de l'utilisateur et en réduisant les frais généraux d'exploitation.

### Liens utiles


- [A propos de Nakamochi](https://nakamochi.io/)
- [S'abonner à la lettre d'information de Nakamochi] (https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)