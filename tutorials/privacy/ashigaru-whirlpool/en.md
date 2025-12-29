---
name: Ashigaru - Whirlpool Coinjoin
description: How do I make coinjoins on the Ashigaru application?
---

![cover](assets/cover.webp)


"*a bitcoin wallet for the streets*"


In this tutorial, you'll learn what a coinjoin is and how to make one with the Ashigaru Terminal application and the Whirlpool implementation, a coinjoin protocol inherited from Samourai Wallet.


## How Whirlpool coinjoints work


In this tutorial, I won't go back over the notion of a coinjoin, its usefulness or the theoretical operation of Whirlpool, as these topics are already explained in detail in Part 5 of the BTC 204 training course on Plan ₿ Academy. If you haven't yet mastered the operation of Whirlpool or the principle of a coinjoin, I strongly recommend that you consult this part 5 before continuing :


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

However, here are a few quick facts and figures that may come in handy.


Whirlpool compatible portfolios use 4 separate accounts to meet the needs of the coinjoin process:


- The **Deposit** account, identified by index `0'` ;
- The **Bad Bank** (or *doxxic exchange*) account, identified by the index `2,147,483,644'` ;
- The **Premix** account, identified by the index `2 147 483 645'` ;
- The **Postmix** account, identified by the index `2 147 483 646'`.


On Ashigaru, in November 2025, two pool denominations are available (this list will probably evolve in the coming months: so remember to check the values as you read):


- 0.25 BTC`, with an entry fee of `0.0125 BTC`;
- 0.025 BTC, with an entry fee of 0.00125 BTC.


Each mixing cycle can involve between 5 and 10 UTXOs in input and output.


![Image](assets/fr/01.webp)


## Software requirements


To make coinjoins with Whirlpool, you will need three separate programs:



- Ashigaru Terminal**, which lets you manage your coinjoins directly from your computer;


https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add


- Ashigaru Wallet**, the application on your smartphone with which you can spend your bitcoins in *postmix* from anywhere ;


https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f


- Dojo**, a Bitcoin node implementation guaranteeing you a sovereign connection to the network, with no dependence on a third-party server.


https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Install each of these tools by following their respective tutorials, then you can start making your first coinjoins.


## Receive bitcoins


After creating your portfolio, you'll start with a single account, identified by the index `0'`. This is the `Deposit` account. It's to this account that you'll send bitcoins destined for coinjoins. You can receive them either via the Ashigaru application (see part 5 of the dedicated tutorial), or via Ashigaru Terminal (also detailed in part 5 of the dedicated tutorial).


Once your deposit account contains at least the amount needed to participate in the smallest pool (plus service charges and the minimum required to cover mining costs) you'll be ready to initiate your first coinjoins.


![Image](assets/fr/02.webp)


## Make the Tx0


Once the funds have arrived in your deposit account and the transaction has been confirmed, you can start the coinjoin process. To do this, on Ashigaru Terminal, open the `Wallets` menu, then select your wallet. If your wallet is locked, the software will ask you for your password and passphrase.


![Image](assets/fr/03.webp)


Then select the `Deposit` account.


![Image](assets/fr/04.webp)


Go to the `UTXOs` menu.


![Image](assets/fr/05.webp)


Here you'll see a list of all the UTXOs in your deposit account. Select the ones you wish to send in the coinjoin cycles.


For greater confidentiality and to avoid *Common Input Ownership Heuristic (CIOH)*, it is recommended to use only one UTXO per input in Whirlpool (a detailed explanation of this principle can be found in BTC 204).


Press the `ENTER` key on your keyboard to select a UTXO: an asterisk `(*)` will appear next to it to indicate that it is selected.


![Image](assets/fr/06.webp)


Then click on the `Mix Selected` button.


![Image](assets/fr/07.webp)


If you have a UTXO large enough to participate in either of the two available pools, you can select the destination pool using the arrows. On this page, you'll see the details of your Tx0 :


- the number of UTXOs that will enter the pool;
- the various fees applied (service charges and mining fees) ;
- the amount of the *doxxic change*.


Check the information carefully, then click on `Broadcast` to broadcast the Tx0.


![Image](assets/fr/08.webp)


Ashigaru will then display the TXID of your Tx0, confirming that the transaction has been broadcast on the network.


![Image](assets/fr/09.webp)


## Making coinjoins


Once the Tx0 has been broadcast, return to your deposit account home page, then click on `Accounts` and select the `Premix` account.


![Image](assets/fr/10.webp)


In the `UTXOs` menu, you'll see the various equalized parts, ready to enter the coinjoin cycles. As soon as Tx0 is confirmed, Ashigaru Terminal will automatically initiate their first mixing cycle.


![Image](assets/fr/11.webp)


Once the Tx0 has been confirmed, the first coinjoin transaction will be created and broadcast automatically by Ashigaru Terminal. By going to `Accounts > Postmix > UTXOs`, you can view your equalized UTXOs, awaiting confirmation of their first cycle.


![Image](assets/fr/12.webp)


You can now leave Ashigaru Terminal running in the background: it will continue to mix and remix your tracks automatically.


## Finishing coinjoins


Now you can let your coins remix themselves automatically. The Whirlpool model means that there are no extra charges for remixing: no service fees, no mining fees. So letting your coins participate in more mixing cycles can only benefit your confidentiality.


For a better understanding of this mechanism and how many cycles it is worth waiting for, I recommend reading this article:


https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

To view the number of remixes performed by each of your pieces, open the `UTXOs` menu in the `Postmix` account.


![Image](assets/fr/13.webp)


To spend your mixed coins, go to the Ashigaru application, which uses the same wallet as your Ashigaru Terminal software. The wallet displayed on opening corresponds to your `Deposit` account. To access the `Postmix` account, which contains your mixed UTXOs, click on the Whirlpool symbol in the top right-hand corner.


![Image](assets/fr/14.webp)


In this account, you'll see all your coins currently being mixed. To spend them, press the `+` symbol at the bottom right of the screen, then select `Send`.


![Image](assets/fr/15.webp)


Fill in the details of your transaction: the recipient's address, the amount to be sent, and, if you wish, choose a specific transaction structure to further enhance your confidentiality (see the corresponding tutorials).


![Image](assets/fr/16.webp)


Carefully check the transaction details, then drag the arrow at the bottom of the screen to confirm the shipment.


![Image](assets/fr/17.webp)


Your transaction has been signed and broadcast on the Bitcoin network.


![Image](assets/fr/18.webp)


## Spend Doxxic Change


Remember: Whirlpool's model is based on the equalization of your pieces at Tx0, before they enter the pools. It's this mechanism that breaks the tracking of UTXOs. In my opinion, this is the most efficient coinjoin model, but it does have one drawback: it generates a *change* that doesn't go through the coinjoin process.


This change corresponds to a UTXO created for each Tx0. It is isolated in a specific account named `Doxxic Change` or `Bad Bank`, depending on the software, to avoid using it with your other UTXOs. This is very important, because these UTXOs have not been mixed: their traceability links remain intact, and they can compromise your confidentiality by establishing a connection between you and your coinjoin activity. So handle them with care and **never use them with other UTXOs**, whether mixed or not. Combining a toxic UTXO with a mixed UTXO will wipe out all the privacy gains you've gained from coinjoining.


For the moment, Ashigaru doesn't offer direct access to this `Doxxic Change` account (at least, I haven't found it). This feature will probably be added in a future update. In the meantime, the only way to retrieve these funds is to import your seed into Sparrow Wallet. The latter will normally automatically detect that this is a wallet used with Whirlpool and give you access to all four accounts, including the `Doxxic Change` account. You can then spend these UTXOs like regular bitcoins from Sparrow.


Here are several possible strategies for managing your foreign exchange UTXOs from coinjoins without compromising your privacy:



- Mixing them into smaller pools:** If your toxic UTXO is large enough to join a smaller pool, this is generally the best option. Be careful, however, never to merge several toxic UTXOs to achieve this, as this will create a link between your various entries in Whirlpool.



- Mark them as non-spendable:** Another prudent approach is simply to keep them as they are in their separate account and leave them untouched. This will prevent you from accidentally spending them. If the value of bitcoin increases, new pools adapted to their size could be opened.



- Make donations:** You can choose to turn these toxic UTXOs into donations to Bitcoin developers, open-source projects or associations that accept BTC. This allows you to usefully dispose of them while supporting the ecosystem.



- Buy prepaid gift cards or Visa cards:** Platforms like [Bitrefill](https://www.bitrefill.com/) allow you to exchange your bitcoins for gift cards or reloadable Visa cards that can be used in shops. This can be a simple and discreet way to spend your toxic UTXOs.



- Swap them for Monero:** Samourai Wallet used to offer a now-defunct BTC/XMR atomic swap service. If a similar service exists (I don't know of any personally), it's an excellent solution for isolating these UTXOs, converting them to Monero, and then eventually sending them back to Bitcoin. However, this method was expensive and dependent on available liquidity.



- Transfer them to the Lightning Network:** Transferring these UTXOs to the Lightning Network to benefit from reduced transaction fees is a potentially interesting option. However, this method may reveal certain information depending on your use of Lightning, and should therefore be used with caution.


## How can I find out about the quality of our coinjoin cycles?


For a coinjoin to be truly effective, it must present a high degree of uniformity between input and output amounts. This uniformity increases the number of possible interpretations for an outside observer, which in turn increases uncertainty about the transaction. To measure this uncertainty, we use the concept of entropy applied to the transaction. The Whirlpool model is recognized as one of the most effective in this respect, as it guarantees excellent homogeneity between participants. For a more in-depth look at this principle, I recommend that you consult the last chapter of Part 5 of the BTC 204 training course.


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

The performance of several coinjoin cycles is measured by the size of the sets in which a coin is hidden. These sets define what are known as *anonsets*. There are two types: the first measures confidentiality in the face of retrospective analysis (from the present to the past), and the second measures resistance to prospective analysis (from the past to the present). For a full explanation of these two indicators, please read the following tutorial (or, once again, the BTC 204 training course):


https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## How to manage the postmix?


After running several coinjoin cycles, the best strategy is to keep your UTXOs in the `Postmix` account, letting them remix indefinitely until you really need to spend them.


Some users prefer to transfer their mixed bitcoins to a wallet secured by wallet hardware. This option is possible, but requires a certain amount of rigor to ensure that the confidentiality acquired with coinjoins is not compromised.


Merging UTXOs is the most frequent error. It is important never to combine mixed UTXOs with unmixed UTXOs in the same transaction, otherwise you risk triggering the *Common Input Ownership Heuristic (CIOH)*. This implies rigorous management of your UTXOs, notably through clear and precise labeling. Generally speaking, merging UTXOs is a bad practice that often leads to a loss of confidentiality when poorly managed.


https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

You should also be cautious about consolidating mixed UTXOs. Limited consolidations can be considered if the UTXOs have significant anonsets, but they inevitably reduce your level of confidentiality. Avoid massive or rushed consolidations, carried out before a sufficient number of remixes, as they could establish inferential links between your pre- and post-mix pieces. In case of doubt, it's best not to consolidate your postmix UTXOs and to transfer them one by one to your wallet hardware, generating a new blank reception address each time. Don't forget to label each transferred UTXO.


We strongly advise against moving your postmix UTXOs to portfolios using minority scripts. For example, if you participated in Whirlpool from a multi-sig portfolio in `P2WSH`, there will be few of you sharing this type of script. By sending your postmix UTXOs to this same type of script, you considerably reduce your anonymity. Beyond the type of script, other specific wallet fingerprints can compromise your confidentiality, so the best thing to do is to spend them from the Ashigaru application.


Finally, as with all Bitcoin transactions, never re-use a receiving address. Each payment must be sent to a new, unique, blank address.


The simplest and safest method is to let your mixed UTXOs rest in their `Postmix` account, let them remix naturally, and only spend them when needed from Ashigaru.


The Ashigaru and Sparrow wallets incorporate additional safeguards against the most common errors associated with blockchain analysis, helping you to preserve the confidentiality of your transactions.