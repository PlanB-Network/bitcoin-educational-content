---
name: Sparrow Wallet - Stonewall
description: Understanding and using Stonewall transactions on Sparrow
---

![cover](assets/cover.webp)



> *Break the assumptions of blockchain analysis with mathematically provable doubt between sender and recipient of your transactions.*

## What's a Stonewall transaction?


Stonewall is a specific form of Bitcoin transaction designed to increase users' confidentiality when spending by imitating a coinjoin between two people, without actually being one. In fact, this transaction is not collaborative. A user can build it on his own, using only the UTXOs belonging to him as input. So you can create a Stonewall transaction for any occasion, without having to synchronize with another user.


The Stonewall transaction works as follows: as input to the transaction, the issuer uses 2 UTXO which belong to it. On the output side, the transaction produces 4 outputs, 2 of which are of exactly the same amount. The other 2 will be foreign exchange. Of the 2 outputs of the same amount, only one will actually go to the payee.


So there are only 2 roles in a Stonewall transaction:


- The issuer, who makes the actual payment ;
- The recipient, who may be unaware of the specific nature of the transaction and simply expects payment from the sender.


Let's take an example to understand this transaction structure. Alice is at the baker's to buy her baguette, which costs `4,000 sats`. She wants to pay in bitcoins, while maintaining some form of confidentiality about her payment. So she decides to build a Stonewall transaction for the payment.


![image](assets/fr/01.webp)


By analyzing this transaction, we can see that the baker has indeed received `4,000 sats` in payment for the baguette. Alice used 2 UTXOs as inputs: one of `10,000 sats` and one of `15,000 sats`. On output, it has recovered 3 UTXO: one of `4,000 sats`, one of `6,000 sats` and one of `11,000 sats`. Alice therefore has a net balance of `- 4,000 sats` on this transaction, which corresponds well to the price of the baguette.


In this example, I have intentionally neglected the mining fees to make it easier to understand. In reality, transaction costs are borne entirely by the issuer.


## What's the difference between Stonewall and Stonewall x2?


The Stonewall transaction works identically to the StonewallX2 transaction, except that the latter requires collaboration, unlike the classic Stonewall transaction, hence the name "x2". This is because the Stonewall transaction is executed without the need for external cooperation: the sender can carry it out without the help of another person. In contrast, for a Stonewall x2 transaction, an additional participant, known as the "collaborator", joins the process. He or she contributes his or her own bitcoins to the transaction, alongside those of the sender, and takes over the entire amount at the end (minus the mining costs).


Let's go back to our example with Alice at the bakery. If she had wanted to make a Stonewall x2 transaction, Alice would have had to collaborate with Bob (a third party) when setting up the transaction. They would each have brought in a UTXO. Bob would then have received the full amount of his contribution on exit. The baker would have received payment for his baguette in the same way as in the Stonewall transaction, while Alice would have recovered its initial balance, less the cost of the baguette.


![image](assets/fr/02.webp)


From an outsider's point of view, the transaction would have remained exactly the same.


![image](assets/fr/03.webp)


To sum up, Stonewall and Stonewall x2 transactions share an identical structure. The distinction between the two lies in their collaborative or non-collaborative nature. The Stonewall transaction is developed individually, without the need for collaboration. The Stonewall x2 transaction, on the other hand, relies on cooperation between two individuals to set it up.


[**-> Learn more about Stonewall transactions x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)


## What's the point of a Stonewall transaction?


The Stonewall structure adds an enormous amount of entropy to the transaction, blurring the lines of chain analysis. Seen from the outside, such a transaction can be interpreted as a small coinjoin between two people. But in reality, like the Stonewall x2 transaction, it is a payment. This method therefore generates uncertainties in chain analysis, or even leads to false leads.


Let's take the example of Alice at the baker's. The transaction on the blockchain would look like this:


![image](assets/fr/04.webp)


An outside observer relying on common chain analysis heuristics might wrongly conclude that "*two people have made a small coinjoin, with one UTXO each as input and two UTXOs each as output*".


![image](assets/fr/05.webp)


This interpretation is inaccurate, because, as you know, one UTXO was sent to the baker, the 2 incoming UTXOs came from Alices, and she recovered 3 exchange outputs.


![image](assets/fr/01.webp)


Even if the outside observer manages to identify the paterne of the Stonewall transaction, he won't have all the information. He won't be able to determine which of the two UTXOs of the same amounts corresponds to the payment. In addition, he won't be able to determine whether the two UTXO entries come from two different people, or whether they belong to a single person who has merged them. This last point is due to the fact that Stonewall x2 transactions, mentioned above, follow exactly the same pattern as Stonewall transactions. Seen from the outside and without additional contextual information, it's impossible to tell the difference between a Stonewall transaction and a Stonewall x2 transaction. The former are not collaborative transactions, whereas the latter are. This adds even more doubt to the expense.


![image](assets/fr/03.webp)


## How do I make a Stonewall transaction on Sparrow?


Originally developed by the Samurai Wallet team, Stonewall transactions were taken over by the Ashigaru application, a fork from the original portfolio created following the arrest of the Samurai developers, and also on Sparrow Wallet.


You will need to install Sparrow and create a :


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Unlike Stowaway or Stonewall x2 (*cahoots*) transactions, Stonewall transactions do not require the use of Paynyms. They can be carried out directly, without any special preparation or collaboration with another user.


To perform a Stonewall transaction on Sparrow, the procedure is very simple: start by creating a transaction as usual, either via the `Send` menu, or from the `UTXOs` menu if you wish to do *Coin Control*.


![Image](assets/fr/06.webp)


Then enter the transaction details: the recipient's address, a label, the amount to be sent and the amount or rate of charges, depending on market conditions.


![Image](assets/fr/07.webp)


Before confirming, this is where you can select the Stonewall structure. At the bottom of the interface, replace `Efficiency` with `Privacy`. If this option does not appear, this means that your portfolio does not have a sufficient number of UTXOs to build this type of transaction.


![Image](assets/fr/08.webp)


After selecting the `Privacy` option, you'll notice that the structure of the transaction is completely modified: it becomes a Stonewall transaction, consuming several of your UTXOs as inputs and producing two outputs of identical amounts, one of which corresponds to the actual payment of `100,000 sats`, in addition to the exchange outputs.


![Image](assets/fr/09.webp)


If everything is correct, click on `Create Transaction`.


You can then check your transaction details one last time, and click on `Finalize Transaction for Signing`.


![Image](assets/fr/10.webp)


Then sign the transaction according to the method specific to your portfolio, and click on `Broadcast Transaction` to broadcast it on the Bitcoin network, awaiting confirmation.


![Image](assets/fr/11.webp)


You now know how a Stonewall transaction works on Sparrow Wallet and how to create one. To deepen your mastery of these tools designed to strengthen your onchain confidentiality, I invite you to follow my BTC 204 training on Plan ₿ Academy :


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c