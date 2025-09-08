---
name: Electrum OP_RETURN
description: Inscrire un message sur la blockchain Bitcoin avec Electrum
---

![cover](assets/cover.webp)


Ce tutoriel vous guide pas à pas pour inscrire un message sur la blockchain Bitcoin à l’aide du wallet Electrum. Cette opération utilise l’instruction OP_RETURN pour insérer un texte dans une transaction, visible publiquement sur la blockchain. Suivez ces étapes simples pour réussir votre inscription.

---
## Prérequis

- Un ordinateur (Windows, macOS ou Linux).
- Une connexion Internet.
- Quelques satoshis (sats) ou bitcoins (BTC) dans votre wallet pour couvrir le montant de la transaction et les frais (fees).
- Un convertisseur texte vers hexadécimal (par exemple, un site en ligne) ou un outil dédié comme [ce générateur de script OP_RETURN](https://resources.davidcoen.it/opreturnelectrum/).

---

## Étape 1 : Télécharger et installer Electrum

![image](assets/fr/01.webp)

1. Rendez-vous sur le site officiel d’Electrum : [electrum.org](https://electrum.org/).
2. Téléchargez la version correspondant à votre système d’exploitation (Windows, macOS, Linux).
3. Installez Electrum en suivant les instructions de l’installateur.
4. Vérifiez l’intégrité du fichier téléchargé (optionnel, mais recommandé pour la sécurité) en comparant la signature ou le hash du fichier.

→ Plus de détails sur le tutoriel Electrum :

https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Étape 2 : Créer ou importer un wallet

1. Lancez Electrum.
2. Choisissez Créer un nouveau wallet ou Restaurer un wallet existant si vous avez déjà une seed phrase (phrase de récupération).
3. Suivez les instructions pour configurer votre wallet :
	- Pour un nouveau wallet, notez soigneusement votre seed phrase et conservez-la en lieu sûr (papier, coffre, etc.).
	- Pour un wallet existant, entrez votre seed phrase pour le restaurer.
4. Définissez un mot de passe pour sécuriser votre wallet.

→ Plus de détails sur le tutoriel Electrum :

https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Étape 3 : Vérifier les fonds disponibles

Assurez-vous que votre wallet contienne suffisamment de bitcoins (BTC) ou satoshis (sats) pour :
- Le montant de la transaction (par exemple, 0.00001 BTC ou 1000 sats).
- Les frais de transaction (fees), qui varient selon l’encombrement du réseau (généralement quelques milliers de sats).

Consultez la Balance dans Electrum pour vérifier vos fonds.

![image](assets/fr/02.webp)

Si nécessaire, transférez des BTC ou sats pour alimenter votre wallet. Pour cela, aller dans l’onglet ‘Receive’ et cliquer sur ‘Create Request’ :

![image](assets/fr/03.webp)

Ce qui fera apparaître une adresse de réception :

![image](assets/fr/04.webp)

→ Plus de détails sur le tutoriel Electrum :

https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Étape 4 : Préparer le message à inscrire

Choisissez le message que vous souhaitez inscrire (par exemple, `Thanks Satoshi`). Note : Les messages OP_RETURN sont limités à 80 octets, soit environ 80 caractères ASCII.

*Prenez un instant pour réfléchir : ce que vous inscrivez sur la blockchain Bitcoin est éternel et accessible à tous, alors :*
- *laissez une belle expression de notre humanité,*  
- *évitez d’inscrire du contenu que vous pourriez regretter.*  

*L’espace de la blockchain et vos bitcoins sont précieux, utilisez-les avec sagesse et intention.*

Convertissez votre message en hexadécimal :
- Vous pouvez recourir à un [outil en ligne](https://www.rapidtables.com/convert/number/ascii-to-hex.html), mais veillez à ne pas y traiter de données sensibles (même si, en principe, les informations destinées à être publiées sur la blockchain Bitcoin via un OP_RETURN ne présentent pas d’enjeu de confidentialité) ;
- Pour davantage de confidentialité, effectuez la conversion localement à l’aide d’un petit script Python :

```py
#!/usr/bin/env python3

def main():
    ascii_text = input("Enter ASCII text: ")
    try:
        hex_output = ascii_text.encode('ascii').hex()
        print(hex_output)
    except UnicodeEncodeError:
        print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
    import sys
    main()
```

Exemple : `Thanks Satoshi` en ASCII donne `5468616e6b73205361746f736869` en hexadécimal.

Préparez le script de transaction. Voici un exemple de format attendu :  

```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001  
script(OP_RETURN 5468616e6b73205361746f736869), 0
```

qui est constitué ainsi : 

- **Adresse destinataire** : Une adresse Bitcoin valide. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Cela peut être une adresse qui vous appartient, si vous souhaitez vous renvoyer les fonds transférés ;
- **Montant transféré** : le montant de la transaction, ici `0.00001` BTC. **Attention** : puisque l’unité utilisée dans Electrum est le BTC, le montant indiqué dans le script de la transaction doit également être exprimé en BTC, et non en sats ;
- **Script OP_RETURN** : Le message converti en hexadécimal précédé de script(`OP_RETURN <messsage>), 0`. Ici, `5468616e6b73205361746f736869` pour le message en hexadécimal.

⚠️ **Attention** : Il est très important d’indiquer `0` après l’OP_RETURN, car cet opcode marque le script comme invalide, ce qui rend ainsi l’output définitivement non dépensable. Les nœuds du réseau supprimeront cet output de leur UTXO set. Si vous renseignez une autre valeur que `0`, celle-ci sera irrémédiablement perdue : vos bitcoins seront considérés comme brûlés. Il convient donc de toujours inscrire `0` avec un OP_RETURN afin d’enregistrer les données désirées, mais sans y associer des fonds qui seraient perdus.

Astuce : Utilisez l’outil [OP_RETURN Generator](https://resources.davidcoen.it/opreturnelectrum/) pour générer automatiquement le script. Même si cet outil propose de renseigner le montant en BTC, conservez l’unité qui est configurée dans Electrum.

![image](assets/fr/05.webp)

Pour changer l’unité utilisée par Electrum, dans la barre de menu trouvez “Préférences”, puis dans l’onglet “Unités” sélectionnez BTC / mBTC / bits ou sats :

![image](assets/fr/06.webp)


---

## Étape 5 : Envoyer la transaction

Dans Electrum, allez dans l’onglet Send / Envoyer.

![image](assets/fr/07.webp)

Dans le champ "Pay to", collez le script préparé (par exemple, celui ci-dessus).

![image](assets/fr/08.webp)

Le champ “Pay to” doit s’afficher en vert, et le montant de la transaction doit se reporter à la ligne du dessous.

Vérifiez le montant et son unité dans le champ Amount / Montant. 

Cliquez sur “Pay…” puis ajuster vos frais de transaction selon le montant que vous êtes prêt à payer et la vitesse à laquelle vous souhaitez que votre transaction soit prise en charge par un mineur et intégrée dans un bloc.

![image](assets/fr/09.webp)

Cliquez sur OK et confirmez la transaction avec votre mot de passe. Vous obtenez une fenêtre de confirmation.


---

## Étape 6 : Vérifier l’inscription

Une fois la transaction confirmée (cela peut prendre quelques minutes), allez dans l’onglet "History".

![image](assets/fr/10.webp)

Faites un clic droit sur la transaction et sélectionnez "View on Explorer" pour voir les détails.

Alternativement, copiez l’adresse de destination (par exemple, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) et consultez-la sur un explorateur de blockchain comme [mempool.space](https://mempool.space/) ou [blockstream.info](https://blockstream.info/).

Cherchez le champ OP_RETURN dans les détails de la transaction pour voir votre message.

![image](assets/fr/11.webp)


![image](assets/fr/12.webp)


---

## Conseils et bonnes pratiques

- Testez avec un petit montant : Commencez avec une petite transaction (par exemple, 1000 sats) pour éviter des erreurs coûteuses.
- Assurez-vous que le montant de l'output qui contient l'OP_RETURN est bien égal à zéro, sinon vos bitcoins seront définitivement perdus.
- Vérifiez l’unité : Assurez-vous que le montant saisi correspond à l’unité affichée dans Electrum (BTC, mBTC ou sats).
- Frais de transaction : Si le réseau est encombré, augmentez les frais pour une confirmation plus rapide.
- Message court : Les inscriptions OP_RETURN sont limitées à 80 octets. Planifiez votre message en conséquence.

---

## Ressources utiles

- Téléchargement d’Electrum : [electrum.org](https://electrum.org/)
- Générateur de script OP_RETURN : [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Explorateurs de blockchain : [mempool.space](https://mempool.space/), [blockstream.info](https://blockstream.info/)
