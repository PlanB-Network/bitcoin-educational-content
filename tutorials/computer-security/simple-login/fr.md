---
name: Connexion simple
description: Identité protégée par des alias
---
![cover](assets/cover.webp)

## Login = email = perte de la vie privée


Dans le monde numérique, il est devenu courant d'avoir un compte pour chaque plateforme à laquelle on souhaite accéder.

Chacun de ces services nécessite une connexion, généralement associée au couple _nom d'utilisateur_ et _mot de passe_. Souvent, le nom d'utilisateur est l'adresse électronique personnelle de l'utilisateur.


Lorsque l'on utilise son email personnel Address à chaque connexion, il est facile d'imaginer la première conséquence : la perte de confidentialité, qui devient majeure si le Address est composé de _name.surname@serviceemail.com_.


Les développeurs d'outils open-source ont créé une série de suites d'applications, conçues précisément pour permettre aux utilisateurs de retrouver un peu de leur vie privée : ils se connecteront toujours, mais en utilisant un alias au lieu de l'outil qui révèle leur identité privée.


Le plus simple de ceux que j'ai personnellement essayés et que je teste encore est [Simple Login] (https://simplelogin.io/).


## Alias


Un alias de courriel remplace simplement la partie _nom.nom_ de votre courriel Address par un nom fictif. Pour l'utilisateur, rien ne change ; le service d'alias transfère les courriels vers et depuis le Address habituel comme d'habitude. Chacun peut continuer à utiliser sa boîte de réception comme il le fait toujours, mais au lieu d'afficher son vrai nom, il affichera un utilisateur méconnaissable. Ce service doit être efficace, et jusqu'à présent, Simple Login a prouvé qu'il l'était.


Lorsque vous visitez le site Simple Login pour la première fois, vous devez créer un compte (ici aussi !), en utilisant l'adresse électronique "officielle" Address. Ici, vous devez entrer l'email, un mot de passe, et résoudre un captcha.


![image](assets/it/02.webp)


Simple Login envoie un message de vérification à l'adresse électronique Address indiquée. Au lieu de cliquer sur le bouton de vérification, il est conseillé de copier le lien et de le coller dans la barre Address.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Le tableau de bord Simple Login s'ouvre immédiatement, avec un bref tutoriel de navigation.


![image](assets/it/05.webp)


Il convient de noter que Simple Login active automatiquement l'abonnement à la lettre d'information, qui peut être désactivé à partir de la commande appropriée.


![image](assets/it/06.webp)


## Paramètres


Vous pouvez jeter un coup d'œil aux _Paramètres_ tout de suite pour découvrir les caractéristiques du service. Simple Login démarre avec toutes les options actives, y compris les options _Premium_, qui restent utilisables pendant 10 jours. Une fois la période d'essai terminée, vous aurez la possibilité de créer 10 alias avec ce profil et vous pourrez relier directement votre email Proton, puisque Simple Login a été racheté par le fournisseur d'email suisse.


![image](assets/it/07.webp)


Vous pouvez définir une série de paramètres ou vérifier si votre courrier électronique a déjà été compromis en termes de confidentialité.


![image](assets/it/08.webp)


Enfin, vous pouvez exporter une sauvegarde de votre profil ou en importer une d'un autre fournisseur.


![image](assets/it/09.webp)


### Courriel professionnel


Les personnes qui utilisent le courrier électronique avec un domaine personnel comme courrier électronique professionnel peuvent configurer leur domaine privé.


![image](assets/it/10.webp)


Depuis le panneau principal, en choisissant _Boîtes aux lettres_, il est même possible d'ajouter d'autres adresses électroniques et d'utiliser les alias qui seront créés en conséquence. Dans ce tutoriel, par exemple, j'ai décidé de créer le profil avec une boîte aux lettres _gmail.com_, puis d'y associer un Address _proton.me_.


![image](assets/it/11.webp)


En ajoutant un nouveau Address, surtout s'il appartient au fournisseur Proton, la procédure guidée montre la possibilité d'entrer en mode _sudo_, super utilisateur. Simple Login demandera d'entrer le mot de passe de cette boîte aux lettres, pour prouver la légitimité du Ownership.


⚠️ **Je déconseille personnellement de faire cela**. ⚠️


![image](assets/it/12.webp)


**Il est préférable d'accéder à la boîte aux lettres électronique -> de copier le lien de vérification et de le coller dans la barre URL -> et d'obtenir la vérification sans révéler le mot de passe**


![image](assets/it/13.webp)


Sur les deux adresses saisies, l'une devient l'adresse par défaut et l'autre est secondaire, mais elles peuvent être facilement interverties, et le paramètre est facilement identifiable dans le tableau de bord.


![image](assets/it/14.webp)


Après avoir ajouté un deuxième email Address (optionnel), voyons ce que nous pouvons faire avec Simple Login.


## Création d'alias


Dans le panneau, la première option de menu est intitulée _Alias_, et c'est là que vous pouvez les créer. Vous avez la possibilité de créer des alias generate de manière aléatoire en cliquant sur le bouton Alias aléatoire, qui est le bouton Green illustré dans la photo suivante. Cette fonction permet de créer un courriel unique et intrigant Address.


![image](assets/it/24.webp)


Toutefois, si vous souhaitez différencier les services en leur donnant des noms différents, vous devez choisir _Nouveau alias personnalisé_. Ce faisant, vous pouvez donner à l'alias le nom du service auquel vous souhaitez accéder (médias sociaux, prestataires de services, événements en ligne, inconnus rencontrés par hasard, etc.) Le reste est pris en charge par Simple Login.

Pour m'amuser (mais pas vraiment, à vrai dire), j'ai décidé de créer un alias pour la banque et je l'ai appelé `BANK`. Même s'il est vrai que ma banque sait tout de moi, je trouve amusant de communiquer avec elle en utilisant un Address incompréhensible pour elle. Simple Login génère en effet un nom aléatoire, qui est séparé de celui que nous choisissons par un `.`


Ici, le nouveau courriel Address peut devenir :


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- et ainsi de suite


Il est possible de choisir plus d'un domaine : les domaines publics sont disponibles avec le plan gratuit, tandis que d'autres, indiqués comme privés (y compris _@simplelogin.com_), élargissent le choix pour les utilisateurs qui décident de souscrire à un plan payant.


![image](assets/it/15.webp)


 L'alias devient prêt et actif après avoir cliqué sur _Create_


![image](assets/it/16.webp)


Le nouvel e-mail Address a été créé et il est maintenant visible, prêt à être envoyé (à la banque !) simplement en le copiant.


![image](assets/it/18.webp)


À ce stade, vous pouvez vous concentrer sur la création d'un alias pour chaque service ou plateforme auquel vous souhaitez accéder et pour lequel l'adresse électronique est un paramètre essentiel pour la création d'un compte.


![image](assets/it/19.webp)


Pour les adeptes de la protection de la vie privée, il est également possible de créer un alias Address basé sur le protocole UUID (et non sur des noms identifiables), qui crée un identifiant unique de 128 bits qui n'est pas contrôlé par des parties centralisées. Cette fonction, utile pour les comptes sensibles, se trouve dans le menu _Alias aléatoires_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Comme vous pouvez le constater, il s'agit d'un email Address qui nécessite une gestion appropriée.


Si vous changez d'avis et ne souhaitez plus utiliser un alias, il vous suffit de cliquer sur la commande _Plus_ de chaque alias individuel et de choisir _Supprimer_.


![image](assets/it/23.webp)


## Gestion des alias


La création d'alias est simple, tout comme leur gestion, qui ne demande qu'un peu d'attention et de discipline. En fait, tout le trafic passera toujours par la boîte aux lettres électronique que nous avons définie, au début, comme la boîte officielle. Les notifications et les communications importantes provenant des plateformes continueront d'arriver sur Gmail, Proton ou tout autre fournisseur de courrier électronique.


Le résultat, cependant, est que nous avons conservé le Address principal qui, à partir du moment de la création des alias, nous sommes libres de décider à qui le révéler et à qui ne pas le révéler.


Un alias fonctionne à la fois pour la réception et l'envoi : un autre utilisateur recevra en effet la réponse de alias.preoccupy789@8shield.net, s'il s'agit du pseudonyme choisi pour ce destinataire particulier.


## Pour


Dans l'ensemble, l'utilisation d'alias est un moyen efficace de protéger son identité et sa vie privée. Les adresses électroniques sont souvent collectées par des courtiers en données et des sites web pour suivre les habitudes et les comportements des utilisateurs. Bien qu'un pseudonyme ne vous rende pas totalement intraçable, l'utilisation systématique d'un pseudonyme est un pas positif vers la protection de vos informations. De plus, dans notre "village numérique mondial", où le piratage, la vente de données et les failles de sécurité sont monnaie courante, il est fort probable que l'adresse électronique que vous utilisez pour vous inscrire sur divers sites web ait déjà été compromise ou ciblée.


Un pseudonyme unique, utilisé pour chaque connexion, **permet immédiatement de comprendre quelle plateforme envoie du spam (ou pire) dans notre boîte aux lettres, car l'e-mail est identifié par l'alias qui lui est associé**. Vous n'avez aucune idée de la quantité de spam et de phishing provenant de canaux dits fiables, parce qu'ils sont institutionnels, jusqu'à ce que vous commenciez à utiliser un alias pour les banques, un pour les services postaux, ou un spécifique pour certains services gouvernementaux obligatoires. Une fois l'expéditeur du spam (ou pire) identifié, vous saurez que ce site a été compromis, et vous prendrez toutes les précautions nécessaires pour protéger toutes les données fournies (pensez aux cartes de crédit !) à ce site spécifique, qui peut se rendre compte de la faille des semaines plus tard.


En ce qui concerne Simple Login, cet outil présente les caractéristiques suivantes :



- (également de F-Droid) et une extension de navigateur, pour gérer les alias dans n'importe quelle situation ;
- une authentification à deux facteurs pour chaque nouveau pseudonyme, ce qui augmente le degré d'indépendance par rapport au service lui-même ;
- Prise en charge de PGP (pour les utilisateurs de _Premium) ;
- création simple de tous les types d'alias (personnalisés, aléatoires et UUID) ;
- parmi les offres gratuites du secteur, la possibilité d'utiliser des alias avec plus de boîtes aux lettres "officielles". D'autres concurrents se limitent à une seule.


## Cons


- 10 alias peuvent ne pas être suffisants si vous envisagez d'utiliser Simple Login de manière intensive. Dans ce cas, le plan payant, qui est assez abordable, est utile pour augmenter le nombre d'alias possibles.
- Il n'est pas possible de créer un alias avec un nom et un domaine spécifiques.  Les médias sociaux traditionnels refusent généralement d'accorder des comptes créés avec ce type d'adresses e-mail. Nostr résout ce problème !
- Si vous utilisez un alias pour envoyer un message à quelqu'un, il est facile d'atterrir dans le dossier spam du destinataire. Dans un premier temps, il est conseillé d'utiliser le pseudonyme pour recevoir, comme dans le cas de la création d'un compte, de l'inscription à une liste de diffusion, etc.