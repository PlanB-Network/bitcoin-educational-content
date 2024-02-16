---
name: Stonewall
description: Understanding and using Stonewall transactions
---
![cover stonewall](assets/cover.jpeg)

> *"Break the assumptions of blockchain analysis with mathematically provable doubt between sender and recipient of your transactions."*


What is a Stonewall transaction?
Stonewall is a specific form of Bitcoin transaction aimed at increasing user privacy during a spend by mimicking a coinjoin between two people, without actually being one. Indeed, this transaction is not collaborative. A user can construct it alone, only involving the UTXOs owned by them as inputs. Therefore, you can create a Stonewall transaction for any occasion without needing to synchronize with another user.

The operation of a Stonewall transaction is as follows: as input, the sender uses 2 UTXOs that they own. As output, the transaction produces 4 outputs, including 2 that will be of the exact same amount. The other 2 will be change. Among the 2 outputs of the same amount, only one will actually go to the payment recipient.

Therefore, there are only 2 roles in a Stonewall transaction:
- The sender, who makes the actual payment;
- The recipient, who can ignore the specific nature of the transaction and simply expect a payment from the sender.

Let's take an example to understand this transaction structure. Alice is at the bakery to buy her baguette, which costs 4,000 sats. She wants to pay in bitcoins while maintaining a certain level of privacy for her payment. Therefore, she decides to construct a Stonewall transaction for the payment.
![transaction stonewall bakery](assets/fr/1.png)
By analyzing this transaction, we can see that the baker indeed received 4,000 sats as payment for the baguette. Alice used 2 UTXOs as inputs: one of 10,000 sats and one of 15,000 sats. As output, she received 3 UTXOs: one of 4,000 sats, one of 6,000 sats, and one of 11,000 sats. Alice has a net balance of -4,000 sats in this transaction, which corresponds to the price of the baguette.

In this example, I intentionally neglected the mining fees to facilitate understanding. In reality, the transaction fees are fully covered by the sender.

What is the difference between Stonewall and Stonewall x2?
The Stonewall transaction operates in the same way as the StonewallX2 transaction, with the exception that the latter requires collaboration, unlike the classic Stonewall transaction, hence the "x2" designation. Indeed, the Stonewall transaction can be executed without external cooperation: the sender can complete it without the assistance of another person. However, for a Stonewall x2 transaction, an additional participant, called the "collaborator," joins the process. The collaborator contributes their own bitcoins as inputs, alongside those of the sender, and receives the entire sum as outputs (minus mining fees).

Let's revisit our example with Alice at the bakery. If she had wanted to make a Stonewall x2 transaction, Alice would have had to collaborate with Bob (a third party) during the transaction creation. They would each have provided a UTXO as input. Bob would then have received the entirety of his contribution as output. The baker would have received payment for the baguette in the same way as in the Stonewall transaction, while Alice would have received her initial balance, minus the cost of the baguette.
![transaction stonewall x2](assets/fr/2.png)

From an external perspective, the transaction pattern would have remained exactly the same.
![Stonewall or Stonewall x2 ?](assets/fr/3.png)
In summary, Stonewall and Stonewall x2 transactions share an identical structure. The distinction between the two lies in their collaborative nature. The Stonewall transaction is created individually, without the need for collaboration. On the other hand, the Stonewall x2 transaction relies on cooperation between two individuals for its implementation.

## What is the purpose of a Stonewall transaction?
The Stonewall structure adds a significant amount of entropy to the transaction and obscures the analysis of the blockchain. From an external perspective, such a transaction can be interpreted as a small coinjoin between two people. However, in reality, just like the Stonewall x2 transaction, it is a payment. This method generates uncertainties in blockchain analysis and can even lead to false leads.

Let's revisit the example of Alice at the bakery. The transaction on the blockchain would appear as follows:
![Stonewall or Stonewall x2 ?](assets/fr/4.png)
An external observer relying on common chain analysis heuristics could mistakenly conclude that "two people have performed a small coinjoin, with each having one UTXO as input and two UTXOs as output."
![Stonewall or Stonewall x2 ?](assets/fr/5.png)
This interpretation is inaccurate because, as you know, a UTXO was sent to the baker, the 2 UTXOs in the input come from Alice, and she received 3 change outputs.![transaction stonewall baker](assets/fr/1.png)
Even if the external observer manages to identify the pattern of the Stonewall transaction, they will not have all the information. They will not be able to determine which of the two UTXOs of the same amounts corresponds to the payment. Furthermore, they will not be able to determine if the two input UTXOs come from two different people or if they belong to a single person who merged them. This last point is due to the fact that Stonewall x2 transactions, which we mentioned above, follow exactly the same pattern as Stonewall transactions. From the outside and without additional information about the context, it is impossible to differentiate a Stonewall transaction from a Stonewall x2 transaction. However, the former are not collaborative transactions, while the latter are. This adds even more doubts about this expense.
![Stonewall or Stonewall x2?](assets/fr/3.png)
## How to make a Stonewall transaction on Samourai Wallet?
Unlike Stowaway or Stonewall x2 (cahoots) transactions, the Stonewall transaction does not require the use of Paynyms. It can be done directly, without any preparation steps. To do this, follow our video tutorial on Samourai Wallet: 
![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## How to make a Stonewall transaction on Sparrow Wallet?
Unlike Stowaway or Stonewall x2 (cahoots) transactions, the Stonewall transaction does not require the use of Paynyms. It can be done directly, without any preparation steps. To do this, follow our video tutorial on Sparrow Wallet: 
![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)


**External resources:**
- https://docs.samourai.io/en/spend-tools#stonewall ;
- https://samouraiwallet.com/stonewall.
