---
name: Liana
description: Setting up and using a wallet on Liana
---
![cover](assets/cover.webp)

In this tutorial, we'll explain step-by-step how to use the Liana application on a computer. Among other things, you'll learn how to set up an automated succession plan, receive and send bitcoins in normal situations, and retrieve funds from an existing portfolio after a given period.

In January 2025, the hardware wallets compatible with Liana were: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.

If you wish to recover funds from an existing Liana wallet, read the presentation below and go directly to the "Recovering bitcoins" section.

## Introducing Liana software

Liana is an open-source software package designed for the creation and management of advanced portfolios, notably as part of an automated inheritance system or a robust backup mechanism. The project has been developed since 2022 by Wizardsardine, a company co-founded by Kévin Loaec and Antoine Poinsot. On the official website, Liana is presented as "a simple portfolio for personal curation, with recovery and inheritance functionalities". The software runs on computers -- Linux, MacOS, Windows -- and its (open) source code is available [on GitHub](https://github.com/wizardsardine/liana).

Liana builds on Bitcoin's programmability to create an advanced wallet. In particular, it takes advantage of time locks (*timelocks*), which allow funds to be spent only once a given period of time has elapsed, and which are involved in the recovery of Bitcoins. A Liana wallet is thus made up of several spending paths:


- A main spending path, which is always available;
- At least one recovery path, which becomes accessible after a certain time.

The diagram below illustrates the operation of a portfolio with two spending paths:

![Schéma explicatif](assets/fr/01.webp)

This operation allows you to set up various configurations, including :


- A succession (or inheritance) plan, enabling heirs to recover funds in the event of the user's death. For more information on this subject, we recommend reading [part 4](https://planb.network/courses/btc102/233c88d3-2e8e-5eba-ac06-efe67a209038) of the BTC102 course.
- A reinforced backup with a recovery time, giving the user the possibility of using his wallet without having to keep the corresponding secret phrase and risk having it stolen, during a burglary for example.
- A safety net for people starting out with Bitcoin: they will manage their own wallet, and their "guardian" (a relative, for example) will reserve the right to recover their funds after a given period.
- A multi-party signature scheme (*multisig*) with reduced requirements over time, to cope with the disappearance of one or more of the participants, such as a company's partners.

The great strength of Liana is that it introduces a standardized way of guaranteeing the recovery of funds in the event of loss of the main key, used for current expenditure. This represents a huge innovation for the clean safekeeping of funds, which is fraught with risk, especially if you're not well-informed on the subject. Liana could therefore encourage even the most risk-averse users to stop using a custodian (such as an exchange platform) to hold their funds and regain ownership of their money, in keeping with Bitcoin's cypherpunk ethos.

Of course, Liana does have its drawbacks. The first is that you have to update your wallet on a regular basis by making a transaction on the Bitcoin blockchain. This can be a pain (depending on how often you use the software) and costly (depending on the level of fees at the time), but it's the price you pay for extra security.

A second negative point may be confidentiality. When you involve another person in the configuration, he or she is privy to all your addresses and can therefore monitor your activity. However, this won't be a problem if you opt for a reinforced backup, or for a succession plan in which your heir has no immediate knowledge of the portfolio's details.

## Preparation

In this tutorial, we'll set up a succession plan. We'll be using :


- A Ledger Nano S Plus, for everyday expenses;

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- A Blockstream Jade, used to recover funds;

https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- Two storage media (USB sticks) to store the portfolio descriptor;
- A letter of succession, containing instructions for recovering the funds;
- A numbered sealed bag, to ensure that the recovery device (the Jade) has not been used.

## Installation and configuration

Visit the official Wizardsardine website and download Liana at https://wizardsardine.com/liana/. You can also download the latest version [from the GitHub repository](https://github.com/wizardsardine/liana/releases), where you can check the authenticity of the software. The version used in this tutorial is 0.9.

![Télécharger Liana](assets/fr/02.webp)

To find out how to manually verify the authenticity and integrity of software before installation, we recommend you consult this tutorial :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Install the software on your machine and launch it. Choose the "*Create a new Liana wallet*" option to configure your wallet.

![Accueil Liana](assets/fr/03.webp)

Choose your portfolio type. If you want to set up an enhanced backup with recovery time, you can select the "*Build your own*" option and opt for the default scheme. This will work in much the same way, except that you won't need to retain the hardware wallet recovery phrase.

We're ignoring here the case of the *Expanding multisig*, which sets up a more complex configuration.

For the purposes of this tutorial, we'll be using simple inheritance.

![Choisir type de portefeuille](assets/fr/04.webp)

A quick explanation follows.

![Rapide explication](assets/fr/05.webp)

Once you've read the explanation, you'll be able to set up the keys to your Liana wallet. This is a crucial step, as it determines the spending characteristics of your account.

![Configurer clés](assets/fr/06.webp)

First of all, in the "Advanced Settings" menu, you can decide on the "descriptor type", i.e. the way in which the contract will be written on the chain. You can choose between two types: P2WSH (SegWit) or Taproot. In both cases, the semantics of the spending conditions will be the same. While P2WSH makes the contract easier to understand, Taproot is superior in that it hides unused conditions and saves costs during retrieval.

This choice is optional: if in doubt, leave the default option (P2WSH in the case of version 0.9, but this is subject to change).

![Choisir le type de descripteur](assets/fr/07.webp)

Next, configure your primary key (*primary key*). This key (or rather, this set of keys) will be used for the current expenditure of funds, which is not subject to any timing conditions. By clicking on "*Set*", you can select the corresponding *signing device*. In our case, we've chosen the Ledger Nano S Plus hardware wallet.

Authorize sharing of the extended public key from the device. Give this key a meaningful name (in this case, "Nano S+"). Note that all applications installed on the device will continue to function normally.

![Configurer clé principale](assets/fr/08.webp)

Next, set the payback delay, i.e. the time after which the funds can be spent by the *inheritance key*. This delay is defined in terms of blocks, with each block separated by an average of 10 minutes. It can range from 10 minutes (1 block) to around 15 months (65,535 blocks). This upper limit is a limitation of the Bitcoin protocol, as the locking time is encoded on 16 bits.

Barring special circumstances, opt for the longest lead time: 15 months or 65,535 blocks. This will save you costs. We do, however, recommend that you carry out the updating procedure (described in the "Updating the portfolio" section) once a year, always at the same time of year, to "ritualize" this practice and avoid forgetting.

Here, we've set up a recovery time of one hour (6 blocks) to carry out our tests.

![Configurer temps de verrouillage](assets/fr/09.webp)

Finally, set up your estate key. This key (or rather, set of keys) will be used to recover funds in the event of your disappearance. Click on "*Set*", choose the signing device and validate the sharing of the extended public key on it.

For this tutorial, we've chosen Jade. Give the key an evocative name (here "Jade"). As with the first device, conventional accounts will continue to function.

![Configurer clé de succession](assets/fr/10.webp)

Once all these actions have been completed, check that everything is in order and click on "*Continue*" to confirm your choices.

![Confirmer clés](assets/fr/11.webp)

The next step is to save your portfolio descriptor. This is the information you need to find the funds in your account. Contrary to the mnemonic phrase, the descriptor does not allow you to spend funds, so disclosing it will only pose a confidentiality problem (the person will know all your transactions).

Save two copies of the descriptor on electronic media, such as USB sticks. Make sure you also print out two copies on paper, so that you can access them in the event of damage to the electronic media. Each backup must be associated with a signature device.

![Sauvegarder descripteur](assets/fr/12.webp)

Our descriptor (which is analyzed at the end of the tutorial) is as follows:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

The final step in the initial portfolio configuration is to verify the descriptor in each of the hardware portfolios that serve as signature devices.

![Enregistrer descripteur](assets/fr/13.webp)

Do the same for each signing device. You will need to check and confirm that the descriptor has been added to each hardware portfolio.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

Your wallet information is now registered, and all that's left is to configure how you want to connect to the Bitcoin network. You can choose to use your own node (local or remote) or use WizardSardine's infrastructure. In the latter case, you'll need to link an e-mail address to your wallet, which will enable you to retrieve the descriptor. WizardSardine will have access to all your transactions. The first option is therefore suggested.

![Sélectionner connexion réseau](assets/fr/15.webp)

We've chosen to use our own node. You can use an existing node, or install a *pruned node* on your machine. If you don't have access to any other node, install your own node on your machine, which should take some time (on the order of several days).

![Choisir type de nœud](assets/fr/16.webp)

For this tutorial, we've used an existing (public) Electrum server. But be careful! It had access to all our activity with the Liana wallet. So use your own node if you want to protect your privacy.

![Connexion serveur Electrum public](assets/fr/17.webp)

Once the node configuration is complete, the main screen should open, displaying your freshly created Liana wallet.

Take the opportunity to store the recovery unit in a safe place. It should be stored in a strategic location, so that it can be found by your heirs in the event of your death.

For added security, you can place the components used for recovery in a sealed bag (*tamper-evident bag*) and write down its serial number somewhere. This ensures that no one has accessed it, and that your device remains valid.

In our example, we have assembled the following elements:


- Blockstream Jade as signature device for the estate;
- A USB cable for connecting and recharging the device;
- A paper backup of the sentence in the event of malfunction or damage to the device (note that the medium can also be metal, and therefore protected from the elements, as is the case with Cryptosteel capsules, for example);
- The USB key containing the portfolio descriptor ;
- A paper backup of the descriptor, in case of malfunction or damage to the USB key (this backup has not been photographed here);
- A letter of succession describing the steps to be taken to recover the funds.

![Éléments de récupération](assets/fr/18.webp)

And we put these items under seal!

![Sachet scellé récupération](assets/fr/19.webp)

## Receipt of funds

Liana's main screen displays your balance and the transactions (past and current) linked to your portfolio. In our case, the balance is zero, which is normal.

![Écran principal](assets/fr/20.webp)

To receive funds, go to the "*Receive*" tab and click on "*Generate address*". A new address should appear on your screen. It's longer than in conventional portfolios: it's an address linked to a stand-alone contract (P2WSH or Taproot).

![Générer nouvelle adresse](assets/fr/21.webp)

You need to verify this address on your hardware portfolio by clicking on "*Verify on hardware device*".

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Once the funds have been sent, the transaction appears on the main screen (first as unconfirmed, then as confirmed). Here, we've sent 50,000 satoshis (just over $50 at the time of transfer) for this test. It goes without saying that the amount transferred in your case will have to be an order of magnitude higher than this value, due to transaction fees.

![Vérifier solde](assets/fr/23.webp)

You can check the expiry status of your funds by going to the "*Coins*" tab. This tab shows you the different coins (UTXO) in your wallet. Here, we can see that the 50,000 satoshis coin created by our transaction expires on the same day (one hour's time).

![Obtenir informations pièce](assets/fr/24.webp)

To better understand the UTXO representation model used in Bitcoin, you can consult the first part of the course on confidentiality in Bitcoin written by Loïc Morel :

https://planb.network/courses/btc204
## Current expenditure

Current spending is the normal situation for using Liana. Sending bitcoins with the master key works as in all classic Bitcoin wallets such as Electrum or Sparrow.

To make a charge, go to the "*Send*" tab and enter the essential information: the recipient's BTC address, the amount to be sent and the desired charge rate. A description (saved locally) can also be added for your personal convenience. In our example, we sent 10,000 satoshis to a certain Bob, for a charge rate of 4 sat/ov, or $0.67 at the time of the transaction.

Liana also offers "coin control": you indicate which coin (UTXO) you wish to spend. Here, we've chosen the 50,000 satoshis coin previously created.

![Envoyer fonds clé principale](assets/fr/25.webp)

Then sign the transaction with your signature device linked to the master key by clicking on "*Sign*". You'll need to verify and confirm the transaction on your hardware wallet. Here, we've used the Nano S Plus to sign the transaction.

![Signer transaction clé principale](assets/fr/26.webp)

Finally, broadcast the transaction over the network by clicking "*Broadcast*". Note that sending funds will reset the recovery time for used coins.

![Diffuser transaction clé principale](assets/fr/27.webp)

The transaction will appear on the main screen and your balance will be updated.

![Solde après dépense](assets/fr/28.webp)

## Portfolio update

As explained above, the Liana wallet requires you to update your funds regularly by performing a transaction on the blockchain. If you fail to do so, your funds may be recovered by your heir (or by your second device in the case of an enhanced backup). This situation is not extremely dangerous, but it does defeat the purpose of setting up this mechanism: to remain in control of your bitcoins without recourse to a trusted third party, while benefiting from a safety net.

A warning will be displayed before your funds (or part of them) expire and can be spent by the recovery key. It will indicate that your "recovery path" (*recovery path*) will soon be available. Given the shortness of our recovery time (one hour), this message is displayed directly in our case.

![Avertissement chemin récupération](assets/fr/29.webp)

When the deadline approaches, a button will appear prompting you to update the funds concerned.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

To update your coins, go to the "*Coins*" tab and click on "*Refresh coin*" in the corresponding coin box. If you have several coins, you should refresh them one by one, and at relatively short intervals, for reasons of confidentiality. To keep costs down, you can consolidate your funds by sending the entire portfolio to a new receiving address, but this will affect your confidentiality.

![Actualiser pièce](assets/fr/31.webp)

Indicate the desired fee rate for the transaction. Since this is a transfer to yourself, you can set a fairly low fee rate, especially if you do it several days before expiration.

![Transfert à soi-même](assets/fr/32.webp)

The transaction (labeled "*self-transfer*") will only be visible in the "*Transactions*" tab.

![Transactions après auto-transfert](assets/fr/33.webp)

Once confirmed, your coin is safe! You can rest easy until the next expiration date.

## Bitcoin recovery

When recovering funds from the Liana portfolio, you may be faced with one of two situations. You may have access to the computer on which the software is installed, in which case all you have to do is open it (which will happen in the case of the enhanced backup model). However, you may not have access to this computer, so we'll start from scratch here. Note that the recovery procedure is the same in both cases.

To get started, download Liana from [the official Wizardsardine website](https://wizardsardine.com/liana/), or from [the GitHub repository](https://github.com/wizardsardine/liana/releases), where you can check the software's authenticity. Install the software and run it. The version used in our case is 0.9, so the visuals may have changed. On the welcome screen, select the "Add an existing Liana wallet" option.

![Ajouter portefeuille existant](assets/fr/34.webp)

Configure how you want to connect to the network. You can choose to use your own node (local or remote) or use WizardSardine's infrastructure. In the latter case, you'll need the e-mail address used by the portfolio creator, so that funds can be located automatically. If you don't have this information, choose the first option.

![Sélectionner connexion réseau](assets/fr/35.webp)

If you're using your own node, import the portfolio descriptor. This is a technical description of the account, enabling you to retrieve the funds held in it. In our case, it's the following information:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

Liana then asks you to enter a mnemonic phrase. If you have a working signature device (hardware wallet), skip this part. If your device is missing or damaged, but you have the corresponding 12 or 24 words, you can still use this option. To be on the safe side (if the amount to be recovered is high), we still suggest that you obtain a new hardware wallet and use the mnemonic to restore the keys on it.

In our case, we use the Blockstream Jade hardware wallet as a recovery device and choose to skip ("*Skip*") this step.

![Passer phrase mnémotechnique](assets/fr/37.webp)

Check and save the descriptor in your signature device by selecting it on the screen. If your hardware wallet does not appear, check that it is connected and unlocked. Check and confirm that this information has been added to your device.

![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Configure your node. You can use an existing node or install a *pruned node* on your machine. In our case, we've used an existing node.

![Choisir type de nœud](assets/fr/39.webp)

For this tutorial, we used a public Electrum server. However, it had access to all our activity with the Liana wallet. If you want to protect your privacy, you'd better use your own node.

![Connexion serveur Electrum public](assets/fr/17.webp)

Once you've set up your node, you're taken to the main wallet screen, where you can view the balance and past transactions linked to the account. You can also see if funds can be retrieved. Here, we see that a coin can be retrieved.

![Accueil Liana récupération](assets/fr/40.webp)

To recover the funds in the portfolio, go to Settings ("*Settings*") at bottom left and click on "*Recovery*".

![Récupération dans paramètres](assets/fr/41.webp)

Spend the coin in the wallet by ticking the appropriate box. Indicate the BTC address to which you wish to send the funds, as well as the transaction fee rate. Then click on "*Next*".

![Récupération des pièces](assets/fr/42.webp)

Sign the transaction by clicking on "*Sign*" and validating the transaction on your hardware wallet.

![Signer transaction clé de récupération](assets/fr/43.webp)

Then broadcast it over the network by clicking on "*Broadcast*".

![Diffuser transaction clé de récupération](assets/fr/44.webp)

The transaction should appear on the main screen. Once confirmed, recovery is complete!

![Écran principal après récupération](assets/fr/45.webp)

## Videos

If you'd like to know more about Liana, there's some video content that will give you a clearer idea of how it works. Here's a video presentation of Liana with Kévin Loaec and Antoine Poinsot :

![Vidéo de présentation avec Kévin Loaec et Antoine Poinsot](https://youtu.be/siuLmQo1lM8)

And here's a tutorial on how to use Liana, with Antoine Poinsot :

![Vidéo-tutoriel avec Antoine Poinsot](https://youtu.be/JrG4WMVPZDQ)

The manipulations shown in the latter are similar to those presented in this tutorial.

## Bonus: descriptor analysis

The descriptor is a human-readable character string that exhaustively describes a set of addresses. It combines a number of essential pieces of information for retrieving the parts (UTXO) of an advanced portfolio. The way the descriptor is written is based on [Miniscript syntax](https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/), the scripting language developed by Andrew Poelstra, Pieter Wuille and Sanket Kanjalkar in 2019.

To better understand why this character string is important, let's analyze the descriptor in our example, which is :

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

The following information can be extracted from this descriptor:


- `wsh` (short for *witness script hash*): This is the type of transactional output created. If we had chosen to use Taproot, the identifier would have been `tr`.
- `or_d`: This is a logical operator indicating that *one of the following two* conditions must be met for the expense to be accepted (the `_d` indicates a particular syntax).
- `pk` (short for *public key*): This operator checks a given signature against the following public key, and gives the answer as a Boolean (TRUE or FALSE).
- `[3689a8e7/48'/0'/0'/2']`: This element includes the *fingerprint* of the master key for the main hardware wallet (in this case the Nano S Plus), and the derivation path to the linked extended private key (from which all other private keys are derived).
- `xpub6FKY ... WQa`: This is the extended public key linked to the main hardware portfolio (here the Nano S Plus)
- `/<0;1>/*`: These are the derivation paths for obtaining simple keys and addresses: `0` for reception, `1` for internal operations (*change*), with a "wildcard" (`*`) allowing sequential derivation of several addresses in a configurable way, similar to the "gap limit" management of classic portfolio software.
- and_v`: This is a logical operator indicating that *the following two* conditions must be met for the expense to be accepted (the `_v` indicates a particular syntax).
- `v:pkh` (short for *verify: public key hash*): This operator verifies a given signature and public key against the public key hash (*hash*) that follows. This is essentially the same check as for P2PKH and P2WPKH scripts.
- `[42e629dd/48'/0'/0'/2']`: This is the same element as above (consisting of the trace and the derivation path), except that the trace of the master key of the hardware recovery portfolio (in this case the Jade) is indicated.
- `xpub6DpQ ... WQd`: This is the extended public key linked to the hardware recovery wallet (here the Jade).
- `older(6)` : This operator checks that the transactional output created must have an age strictly greater than 6 blocks in order to be spent.

The last data item (`8alrve5h`) is the descriptor checksum, and corresponds to the portfolio identifier.

The scripts created by this portfolio will take the following form:

```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```

Since the security of your Bitcoin wallet also depends on your understanding of how it works, I suggest you study the mechanisms of deterministic and hierarchical wallets in depth by taking this free training course on Plan ₿ Network :

https://planb.network/courses/cyp201