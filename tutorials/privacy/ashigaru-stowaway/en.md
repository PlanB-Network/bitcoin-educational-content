---
name: Ashigaru - Stowaway
description: How do I make a Payjoin transaction on Ashigaru?
---
![cover](assets/cover.webp)


> *Force blockchain spies to rethink everything they think they know.*

Payjoin is a Bitcoin transaction structure designed to enhance user confidentiality by involving direct collaboration with the payment recipient. Several implementations exist to facilitate its implementation and automate the process. The best-known of these is undoubtedly Stowaway, initially developed by the Samurai Wallet team and now integrated into its fork Ashigaru.


## How does Stowaway work?


As previously mentioned, Ashigaru integrates a PayJoin tool called `Stowaway`. This is available in the Ashigaru app on Android. For a Payjoin to be carried out, the recipient (who also takes on the role of collaborator) must be using software compatible with Stowaway, i.e. only Ashigaru for the moment.


Stowaway is based on a category of transactions that Samurai referred to as "Cahoots". A Cahoot is a collaborative transaction between several users, involving an exchange of information outside the Bitcoin blockchain. Ashigaru currently offers two Cahoots tools: Stowaway (Payjoins) and StonewallX2.


https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots transactions require the exchange of partially signed transactions between users. This process can be long and tedious, especially when carried out remotely. However, it is still possible to do this manually, if the collaborators are in the same location. In concrete terms, this involves scanning five QR codes in succession, exchanged between the two participants.


At a distance, this method becomes too complex. To remedy this, Samourai has developed a Tor-based encrypted communication protocol called "*Soroban*". Thanks to Soroban, the exchanges required for a Payjoin are automated and take place in the background.


These encrypted communications require a connection and authentication between Cahoot participants. This is why Soroban relies on users' Paynyms. If you're not yet familiar with how Paynyms work, take a look at this dedicated tutorial to learn more:


https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

In a nutshell, a Paynym is a unique identifier associated with your wallet, enabling you to activate various functions, including encrypted exchanges. It takes the form of an identifier accompanied by an illustration. Here, for example, is the one I use on the Testnet:


![Image](assets/fr/01.webp)


**To sum up:**



- payjoin" = Specific collaborative transaction structure;



- `Stowaway` = Payjoin implementation available on Ashigaru ;



- `Cahoots` = Name given by Samourai to all their types of collaborative transactions, in particular the Payjoin `Stowaway`, taken over today on Ashigaru ;



- soroban = Encrypted communication protocol established on Tor that allows collaboration with other users in a `Cahoots` transaction;



- paynym" = Unique wallet identifier used to establish communication with another user on "Soroban", in order to carry out a "Chahoots" transaction.


For a more in-depth look at how Payjoins work and their usefulness in onchain privacy, I recommend this other tutorial:


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## How do I establish a connection between Paynyms?


To get started, you will of course need to install Ashigaru and create a :


https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

To carry out a remote Cahoots transaction, including a PayJoin (*Stowaway*) via Ashigaru, you must first "follow" the user you wish to collaborate with, using their Paynym. In the case of a Stowaway, this means following the person to whom you wish to send bitcoins. If you don't yet know how to follow another Paynym, you'll find the detailed procedure in this tutorial :


https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## How do I make a Payjoin on Ashigaru?


To carry out a Stowaway transaction, click on the image of your Paynym in the top left-hand corner of the screen, then open the `Collaborate` menu. The person taking part in the transaction with you must do the same, unless you are exchanging QR codes in person.


![Image](assets/fr/02.webp)


You have two options: select `Initiate` if you are the sender of the payment, or `Participate` if you are the payee of this payjoin.


![Image](assets/fr/03.webp)


If you are the recipient, the procedure is very simple. For remote collaboration via the Soroban network, click on `Participate`, choose the account you wish to use, then press `LISTEN FOR CAHOOTS REQUESTS` to await the request sent by the payer.


![Image](assets/fr/04.webp)


On the other hand, for in-person collaboration via QR code scanning, go to the home page of your wallet, press the QR code icon at the top of the screen, then scan the QR code provided by the payer initiating the transaction.


![Image](assets/fr/05.webp)


If you are in the payer role, i.e. the one initiating the transaction, go to the `Collaborate` menu, then select `Initiate`.


![Image](assets/fr/06.webp)


For the transaction type, since we wish to make a Payjoin Stowaway, choose this option.


![Image](assets/fr/07.webp)


You can then choose between online collaboration (*Cahoots* via *Soroban*) or face-to-face collaboration, with QR code exchanges.


![Image](assets/fr/08.webp)


### Cahoots online


If you have chosen the `Online` option, then select the recipient from the Paynyms you are following.


![Image](assets/fr/09.webp)


Click on `Set up transaction`, then choose the account from which you wish to make the expenditure.


![Image](assets/fr/10.webp)


On the next page, enter the transaction details: the amount to be sent to the recipient and the charge rate. There's no need to enter a receiving address, as the recipient will transmit it himself during PSBT exchanges.


Then click on `Review transaction setup`.


![Image](assets/fr/11.webp)


Check the information carefully, make sure your collaborator is listening to the *Cahoots* requests, then click on the green `BEGIN TRANSACTION` button to initiate the exchange of PSBTs via Soroban.


![Image](assets/fr/12.webp)


Wait until both participants have signed the transaction, then broadcast it on the Bitcoin network.


![Image](assets/fr/13.webp)


### Face-to-face discussions


If you wish to carry out the exchange in person, select the `STONEWALL X2` transaction type, then choose the `In Person / Manual` option.


![Image](assets/fr/14.webp)


Click on `Set up transaction`, then choose the account from which you wish to make the expenditure.


![Image](assets/fr/15.webp)


On the next page, enter the transaction details: the amount to be sent to the recipient and the charge rate. There's no need to enter a receiving address, as the recipient will transmit it himself during PSBT exchanges.


Then click on `Review transaction setup`.


![Image](assets/fr/16.webp)


Check the details, then press the green `BEGIN TRANSACTION` button to start exchanging PSBTs via QR code scanning.


![Image](assets/fr/17.webp)


The exchange is done by alternating the scan with the collaborator: click on `SHOW QR CODE` to display your QR code to your collaborator, who will scan it. He will then click on `SHOW QR CODE` to display his, and you will scan it with `LAUNCH QR Scanner`. Repeat this process until all five exchange steps have been completed.


![Image](assets/fr/18.webp)


Once all exchanges have been completed, check the transaction details, then release it by dragging the green arrow at the bottom of the screen.


![Image](assets/fr/19.webp)


[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Its structure is as follows:


![Image](assets/fr/20.webp)


*Credit: [mempool.space](https://mempool.space/)*


If we analyze this transaction, we see my UTXO of `164,211 sats` on the input side, as well as the UTXO of `190,002 sats` belonging to the actual recipient of the payment. On the output side, I receive an exchange UTXO of `63,995 sats`, while the recipient receives a UTXO of `290,002 sats`. Comparing inputs and outputs, we can see that the recipient has indeed earned `100,000 sats`, which corresponds to the amount of my actual payment, and that I have lost `100,000 sats`, to which I have added the mining costs.


Obviously, I can describe this structure because I built the transaction myself. But for an outside observer, it's generally impossible to determine which UTXOs belong to which participant, either in inputs or outputs.


To deepen your knowledge of onchain privacy management on Bitcoin, I recommend you take my BTC 204 training on Plan ₿ Academy :


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c