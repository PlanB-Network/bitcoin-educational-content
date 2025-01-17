---
term: STONEWALL
---

A specific form of Bitcoin transaction aimed at increasing user privacy during a spend by mimicking a coinjoin between two people, without actually being one. Indeed, this transaction is not collaborative. A user can construct it alone, involving only their own UTXOs as inputs. Therefore, you can create a Stonewall transaction for any occasion, without needing to synchronize with another user.

The operation of the Stonewall transaction is as follows: at the input of the transaction, the sender uses 2 UTXOs that belong to them. The transaction then produces 4 outputs, 2 of which will be exactly the same amount. The other 2 will constitute the change. Among the 2 outputs of the same amount, only one will actually go to the recipient of the payment.

Thus, there are only 2 roles in a Stonewall transaction:
* The sender, who makes the actual payment;
* The recipient, who may be unaware of the specific nature of the transaction and simply awaits a payment from the sender.

![](../../dictionnaire/assets/33.webp)
Stonewall transactions are available on both the Samourai Wallet application and the Sparrow Wallet software.

The Stonewall structure adds a lot of entropy to the transaction and obscures the trail for chain analysis. From the outside, such a transaction can be interpreted as a small coinjoin between two people. But in reality, just like the Stonewall x2 transaction, it is a payment. This method thus generates uncertainties in chain analysis, or even leads to false trails. Even if an external observer manages to identify the pattern of the Stonewall transaction, they will not have all the information. They will not be able to determine which of the two UTXOs of the same amounts corresponds to the payment. Moreover, they will not be able to determine if the two UTXOs at the input come from two different people or if they belong to a single person who merged them. This last point is due to the fact that Stonewall x2 transactions follow exactly the same pattern as Stonewall transactions. From the outside and without additional context information, it is impossible to differentiate a Stonewall transaction from a Stonewall x2 transaction. However, the former are not collaborative transactions, while the latter are. This adds even more doubt about this expenditure.