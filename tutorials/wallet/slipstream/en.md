---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

Normally, when you sign a transaction, it is automatically broadcast to every Bitcoin node on the network. It then waits to be mined.

However, for as long as it is not in a block, an attacker who has obtained your private key could replace it and steal the funds. This is typically the case if you use a ColdCard hardware wallet.

The Slipstream tool from the mining company MARA lets you bypass broadcasting the transaction to the network: it is sent directly (and only) to a miner, which keeps it private and avoids exposing it on the network. The transaction will probably take longer to be mined, but it will be protected against a replacement attack.

Below, we offer a tutorial allowing users of [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), as well as users of the [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) wallet, to use miner MARA's Slipstream tool through the [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) page.

⚠️ **Warning**: this tool is only meant for certain profiles, mainly Liana wallets, miniscript wallets and some types of multisig. Wizardsardine **explicitly advises against** using it for wallets whose funds are already at critical risk of theft, for example those whose recovery phrase was generated on a ColdCard device affected by the random number generator vulnerability. In that situation, the race against the attacker is a matter of seconds, and a transaction sent to a single miner takes far longer to confirm than a normally broadcast one. If this concerns you, read our dedicated tutorial first:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## For Liana users

Liana is maintained by Wizardsardine, the publisher of the [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) page, so the path is direct: you simply export the signed PSBT file instead of broadcasting it.

*Prerequisite: have funds on your Liana wallet.*

### Step 1: Create your transaction with Liana

As usual, build your transaction by adding the destination address, the description, and the amount (here, the maximum available in the wallet).

To set the fee rate:

- select the coins you want to spend by clicking the small box at the bottom left, under "Coins selection";
- then enter the fee rate. Remember to set fees much higher than the suggested rate, as described on this page: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Finally, click "Next".

![Building the transaction in Liana](assets/fr/01.webp)

### Step 2: Check your transaction details

Before clicking "Sign", check your transaction details; in particular:

- the amount sent;
- the number of satoshis allocated to transaction fees;
- but above all, the address you are sending the funds to (remember to check the first 5/6 characters, the last 5/6, and 5/6 characters in the middle of the address in order to avoid "address poisoning" attacks).

![Checking the transaction details](assets/fr/02.webp)

### Step 3: Select the signing wallets

Next, select the software and/or hardware wallets you need to sign your transaction with. A quick reminder: in the case of a 2-of-2 multisig wallet, you need 2 signatures out of 2.

### Step 4: Export your transaction's PSBT file

The Bitcoin transaction is now signed by the appropriate keys. Do not click "Broadcast", otherwise it will be shared with the entire network and, if you use a ColdCard hardware wallet, your transaction will be publicly exposed and your funds will be at risk.

You can now click "Export", then save the PSBT file locally on your computer.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Step 5: Send the transaction to the miner via outofband.wizardsardine.com

Now for the final steps. To send the transaction to the miner, all you have to do is take the PSBT file and drag and drop it into the designated area.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

The transaction is then displayed as shown below.

![Transaction in the queue](assets/fr/05.webp)

### Step 6: Send the transaction via Slipstream

Finally, all you have to do is click "Send" so that the transaction is sent to MARA via Slipstream.

![Sending the transaction via Slipstream](assets/fr/06.webp)

Within a few seconds, the transaction then goes from "Sending" to "Accepted":

![Transaction accepted by Slipstream](assets/fr/07.webp)

All that is left is to copy the transaction identifier (TXID), then paste it into [mempool.space](https://mempool.space/) in order to watch it being mined:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Please note: the transaction will show as "Transaction not found" until the miner, MARA, mines a block and includes your transaction in it. This can take several tens of minutes, or even hours, because MARA only holds around 4.5% of the Bitcoin network's hash rate. As of 4 August 2026, this corresponds to roughly one block mined every 3 hours and 45 minutes.

## For users of other wallets

If you do not use [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) but still want to use the tool, here is a tutorial using a 2-of-2 multisig wallet. To do this, we will use the [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) software wallet.

*Prerequisite: have funds on your Sparrow wallet.*

### Step 1: Create your transaction

With [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), create the transaction on your multisig wallet. Remember to set fees much higher than the suggested rate, as described on this page: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Once created, click "Create Transaction".

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Step 2: Finalize your transaction

In order to finalize your transaction, you now need to sign it. To do this, click "Finalize Transaction for Signing".

![Finalizing the transaction for signing](assets/fr/10.webp)

### Step 3: Sign your transaction with your different keys

Now comes the time to sign the transaction. To do this, simply sign it with the software or hardware wallet(s) you use.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Step 4: Download the signed transaction, and do not broadcast it to the network

The Bitcoin transaction is now signed by both keys of our 2-of-2 multisig. Do not click "Broadcast Transaction", otherwise it will be shared with the entire network and, if you use a ColdCard hardware wallet, your transaction will be publicly exposed and your funds will be at risk.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Step 5: Display the signed transaction script, or download the PSBT file

To display the signed Bitcoin transaction, now click "View Final Transaction". You can then copy the signed Bitcoin transaction script:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

If you want to download the transaction file, you can either:

- click "File", then "Save transaction…";
- or click the network connection button at the bottom right (yellow button), then click "Save Final Transaction".

The transaction will then be saved locally on your computer.

![Saving the final transaction locally](assets/fr/14.webp)

### Step 6: Send the transaction to the miner via outofband.wizardsardine.com

Now for the final steps. To send the transaction to the miner, all you have to do is:

- go to [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- paste the signed transaction script copied in the previous step, then click "ADD TO QUEUE" below;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- or take the file and drag and drop it into the designated area.

![Dropping the transaction file on the tool](assets/fr/16.webp)

The transaction is then displayed as shown below.

![Transaction in the queue](assets/fr/17.webp)

If a message tells you that the total input amount of satoshis in your transaction is unknown (and that, as a result, the number of satoshis for the fees cannot be computed), you simply need to enter the total input amount of satoshis manually. To find it, just click on the display of your transaction in Sparrow, in the middle of the diagram:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Then enter that amount (15,904 sats in our example) into the [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) tool:

![Manually entering the total input amount](assets/fr/19.webp)

Finally, check that the fee rate is correct.

### Step 7: Send the transaction via Slipstream

Finally, all you have to do is click "Send" so that the transaction is sent to MARA via Slipstream.

![Sending the transaction via Slipstream](assets/fr/20.webp)

Within a few seconds, the transaction then goes from "Sending" to "Accepted":

![Transaction accepted by Slipstream](assets/fr/21.webp)

All that is left is to copy the transaction identifier (TXID), then paste it into [mempool.space](https://mempool.space/) in order to watch it being mined:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Please note: the transaction will show as "Transaction not found" until the miner, MARA, mines a block and includes your transaction in it. This can take several tens of minutes, or even hours, because MARA only holds around 4.5% of the Bitcoin network's hash rate. As of 4 August 2026, this corresponds to roughly one block mined every 3 hours and 45 minutes.
