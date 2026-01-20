---
name: Ashigaru - Ricochet
description: Understanding and using Ricochet transactions
---
![cover ricochet](assets/cover.webp)


> *A premium tool that adds extra hops of history to your transaction. Stump the blacklists and help guard against unjust 3rd party account closures.*

## What's a Ricochet?


Ricochet is a technique consisting in performing several fictitious transactions towards oneself to simulate a transfer of bitcoin ownership. This tool differs from Ashigaru's other transactions (inherited from Samourai Wallet) in that it doesn't provide prospective anonymity, but rather a form of retrospective anonymity. In fact, Ricochet blurs the specificities that can compromise the fungibility of a Bitcoin part.


For example, if you make a coinjoin, your part coming out of the mix will be identified as such. Chain analysis tools are able to detect the paterns of coinjoin transactions and assign a label to the pieces coming out of them. In effect, coinjoin aims to break a coin's historical links, but its passage through coinjoins remains detectable. By way of analogy, this phenomenon is akin to the encryption of a text: although the original text cannot be accessed in clear text, it is easy to identify that encryption has been applied.


The label "coinjoined" can affect the fungibility of a UTXO. Regulated entities, such as exchange platforms, may refuse to accept a coinjoined UTXO, or even demand explanations from its owner, with the risk of having your account blocked or your funds frozen. In some cases, the platform may even report your behavior to state authorities.


This is where the Ricochet method comes in. To fade the imprint left by a coinjoin, Ricochet executes four successive transactions in which the user transfers his funds to himself at different addresses. After this sequence of transactions, the Ricochet tool finally routes the bitcoins to their final destination, such as an exchange platform. The aim is to create distance between the original coinjoin transaction and the final act of spending. In this way, blockchain analysis tools will assume that there has probably been a transfer of ownership after the coinjoin, and that there is therefore no need to take action against the issuer.


![image](assets/fr/01.webp)


Faced with the Ricochet method, one might imagine that chain analysis software would deepen its examination beyond four bounces. However, these platforms face a dilemma in optimizing the detection threshold. They need to establish a threshold number of hops after which they accept that a change of ownership has likely occurred, and that the link to a previous coinjoin should be ignored. However, determining this threshold is risky: each extension in the number of jumps observed exponentially increases the volume of false positives, i.e. individuals erroneously marked as participants in a coinjoin, when in fact the operation was carried out by someone else. This scenario poses a major risk for these companies, as false positives lead to dissatisfaction, which can drive affected customers to the competition. In the long term, an over-ambitious detection threshold leads a platform to lose more customers than its competitors, which could threaten its viability. It is therefore complicated for these platforms to increase the number of bounces observed, and 4 is often a sufficient number to counter their analyses.


Thus, **the most common use case for Ricochet arises when it is necessary to conceal a previous participation in a coinjoin on a UTXO that you own.** Ideally, it is best to avoid transferring bitcoins that have undergone a coinjoin to regulated entities. Nevertheless, in the event of being left with no other option, particularly in the urgent need to liquidate bitcoins in state currency, Ricochet offers an effective solution.


## How does Ricochet work on Ashigaru?


Ricochet is simply a method of sending bitcoins to oneself, originally invented by the developers of Samourai Wallet. It is therefore perfectly possible to simulate a Ricochet manually, without the need for a specialized tool. However, for those wishing to automate the process while enjoying a more polished result, the Ricochet tool available via the Ashigaru application (which is a Samourai fork) represents a good solution.


Since Ashigaru charges for its service, a Ricochet costs `100,000 sats` as a service fee, plus a mining fee. Its use is therefore recommended for transfers of significant amounts.


The Ashigaru application offers two Ricochet variants:



- Reinforced Ricochet, or "staggered delivery", which offers the advantage of spreading Ashigaru's service charges over the five successive transactions. This option also ensures that each transaction is broadcast at a separate time and recorded in a different block, mimicking as closely as possible the behavior of a change of ownership. Although slower, this method is preferable for those who are not in a hurry, as it maximizes Ricochet's efficiency by strengthening its resistance to chain analysis;



- The classic Ricochet, which is designed to execute the operation with speed, broadcasting all transactions in a reduced time interval. This method, therefore, offers less confidentiality and less resistance to analysis than the reinforced method. It should only be used for urgent shipments.


## How to make a Ricochet on Ashigaru?


Making a ricochet on Ashigaru is very simple: just activate the corresponding option when creating a send transaction. To begin, click on the `+` button, then on `Send`, and select the account from which you wish to send the funds.


![Image](assets/fr/02.webp)


Fill in the transaction information: the amount to be sent and the recipient's final address after the Ricochet jumps. Then check the `Ricochet` option.


![Image](assets/fr/03.webp)


You can then choose between the two Ricochet modes discussed in the theory section: either classic Ricochet, where all transactions are included in the same block, or staggered delivery, which improves Ricochet quality at the cost of a longer delay.


Once you've made your choice, press the arrow at the bottom of the screen to confirm.


![Image](assets/fr/04.webp)


On the next screen, you'll see a complete summary of your transaction. This is also where you can adjust the fee rate for your Ricochet transactions according to market conditions. If everything is to your satisfaction, drag the green arrow to sign and distribute Ricochet transactions.


![Image](assets/fr/05.webp)


Wait while the various jumps run automatically.


![Image](assets/fr/06.webp)


Your transactions have been successfully broadcast.


![Image](assets/fr/07.webp)


You're now fully familiar with the Ricochet option available in the Ashigaru application. To go further, I recommend you take my BTC 204 training course, which will teach you in detail how to strengthen your onchain confidentiality.


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
