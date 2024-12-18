---
name: OXT - Chain Analysis
description: Master the basics of chain analysis on Bitcoin
---
![cover](assets/cover.webp)

***WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, **the website OXT.me is currently inaccessible**. However, it remains possible that this tool might be relaunched in the coming weeks. In the meantime, you can still benefit from this tutorial to understand the basics of chain analysis on Bitcoin. All heuristics and patterns presented here remain applicable to Bitcoin transactions. Even though these tools are less optimized than OXT, you can temporarily use [Mempool.space](https://mempool.space/) or [Bitcoin Explorer](https://bitcoinexplorer.org/) to put the theoretical concepts of this article into practice.*

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

---

In this article, you will learn the essential theoretical foundations needed to embark on basic chain analyses on Bitcoin, and more importantly, to understand how those observing you operate. Although this article is not a practical tutorial on the OXT tool (a topic we will cover in a future tutorial), it compiles a set of crucial knowledge for its use. For each model, metric, and indicator presented, a link to an example transaction on OXT is provided, which will allow you to better understand its use and to practice alongside your reading.

## Introduction
One of the functions of money is to solve the problem of the double coincidence of wants. In a system based on barter, completing an exchange requires not only finding an individual who is offering a good that meets my need but also providing them with a good of equivalent value that satisfies their own need. Finding this balance proves complex. That's why we resort to money, which allows us to move value both in space and in time.

For money to solve this problem, it is essential that the party providing a good or service is convinced of their ability to spend that sum later on. Thus, any rational individual willing to accept a piece of money, whether digital or physical, will ensure that it meets two fundamental criteria:
- The coin must be intact and authentic;
- and it must not be double-spent.

If we use physical money, it’s the first characteristic that is the most complex to assert. At different periods in history, the integrity of metal coins has often been affected by practices such as clipping or drilling. For example, during ancient Rome, it was common for citizens to scrape the edges of gold coins to collect a bit of precious metal, while still keeping them for future transactions. This is notably why grooves were later stamped on the edge of coins. Authenticity is also a difficult characteristic to verify on a physical monetary medium. Nowadays, techniques to combat counterfeiting are increasingly complex, forcing merchants to invest in expensive verification systems.

On the other hand, due to their nature, double spending is not a problem for physical currencies. If I give you a €10 bill, it irrevocably leaves my possession to enter yours, thereby excluding any possibility of multiple spending of the monetary units it represents.
For digital currency, the challenge is different. Ensuring the authenticity and integrity of a coin is often simpler, but ensuring the absence of double spending is more complex. Every digital good is essentially information. Unlike physical goods, information does not divide during exchanges but propagates by multiplying. For example, if I send you a document by email, it then gets duplicated. On your end, you cannot verify with certainty that I have deleted the original document.

The only way to avoid this duplication of a digital good is to be aware of all the exchanges on the system. In this way, one can know who owns what and update everyone's accounts based on the transactions made. This is what is done, for example, with scriptural money. When you pay €10 to a merchant by credit card, the bank notes this exchange and updates the ledger.

On Bitcoin, the prevention of double spending is done in the same way. It seeks to confirm the absence of a transaction that has already spent the coins in question. If these have never been used, then we can be assured that no double spending will occur. This is the famous phrase from Satoshi Nakamoto in the White Paper: "*The only way to confirm the absence of a transaction is to be aware of all transactions.*"

Unlike the banking model, on Bitcoin, we do not wish to have to trust a central entity. Therefore, all users must be able to confirm this absence of double spending, without relying on a third party. Thus, everyone must be aware of all Bitcoin transactions.

It is precisely this public dissemination of information that complicates the protection of privacy on Bitcoin. In the traditional banking system, in theory, only the financial institution is aware of the transactions made. However, on Bitcoin, all users are informed of all transactions, via their respective nodes.

Because of this constraint on dissemination, Bitcoin's privacy model differs from that of the banking system. In the latter, transactions are associated with the user's identity, but the flow of information is cut off between the trusted third party and the public. In other words, your banker knows that you buy your baguette every morning at the local bakery, but your neighbor is not aware of all these transactions. In the case of Bitcoin, since the flow of information cannot be broken between transactions and the public domain, the privacy model relies on separating the user's identity from the transactions themselves.
![analysis](assets/en/1.webp)
*Diagram inspired by Satoshi Nakamoto's in the White Paper: Bitcoin: A Peer-to-Peer Electronic Cash System, section 10 "Privacy".*
Since Bitcoin transactions are made public, it becomes possible to establish links between them to deduce information about the parties involved. This activity even constitutes a specialty in itself, commonly called "chain analysis". In this article, I invite you to explore the fundamentals of chain analysis to understand how your bitcoins are tracked.

The majority of companies specializing in chain analysis operate as black boxes, and do not disclose their methodologies. Therefore, it is difficult to obtain information about this practice. For the writing of this article, I mainly relied on the few open resources available:
- The bulk of my article is extracted from the series of four articles named: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), produced by Samourai Wallet in 2021;
- I also used various reports from [OXT Research](https://medium.com/oxt-research), as well as their free chain analysis tool ;
- More broadly, my knowledge comes from the different tweets and content from [@LaurentMT](https://twitter.com/LaurentMT) and [@ErgoBTC](https://twitter.com/ErgoBTC);
- I was also inspired by [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) in which I participated alongside [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), and [@LaurentMT](https://twitter.com/LaurentMT).

I would like to thank their authors, developers, and producers. Without their various contents and software, this article would not exist. I also thank the reviewers who meticulously corrected this text and graced me with their expert advice:
- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).

*For your information, I have added a technical miniglossary at the end of the article to define certain terms. If you see a word you do not understand with an asterisk, its definition is at the bottom of the page.*

## What is chain analysis?
Chain analysis is a practice that encompasses all methods for tracking Bitcoin flows on the blockchain. Generally, chain analysis relies on observing characteristics in samples of previous transactions. It then involves identifying these same characteristics in a transaction that one wishes to analyze and deducing plausible interpretations. This problem-solving method, based on a practical approach to find a sufficiently good solution, is what is called a heuristic.

To simplify, chain analysis is done in two main steps:
1. The identification of known characteristics;
2. The deduction of hypotheses.

One of the objectives of chain analysis is to group various activities on Bitcoin to determine the uniqueness of the user who carried them out. Subsequently, it will be possible to attempt to link this bundle of activities to a real identity.

Remember my introduction. I explained why Bitcoin's privacy model originally relied on separating the user's identity from their transactions. It would, therefore, be tempting to think that chain analysis is unnecessary, since even if one manages to group on-chain activities, they cannot be associated with a real identity. Theoretically, this statement is accurate. Cryptographic key pairs are used to establish conditions on the UTXOs. By essence, these key pairs do not disclose any information about the identity of their holders. Thus, even if one succeeds in grouping activities associated with different key pairs, this tells us nothing about the entity behind these activities.

However, the practical reality is much more complex. There are a multitude of behaviors that risk linking a real identity to an on-chain activity. In analysis, this is called an entry point, and there are many of them. The most common, of course, is KYC (Know Your Customer). If you withdraw your bitcoins from a regulated platform to one of your personal receiving addresses, then some people are able to link your identity to this address. More broadly, an entry point can be any form of interaction between your real life and a Bitcoin transaction. For example, if you publish a receiving address on your social networks, this can be an entry point for analysis. If you make a payment in bitcoins to your baker, they can associate your face (which is part of your identity) with a Bitcoin address.
These entry points are almost inevitable when using Bitcoin. Although one might seek to limit their scope, they will remain present. That's why it's crucial to combine methods aimed at preserving your privacy. While maintaining an acceptable separation between your real identity and your transactions is a commendable approach, it remains insufficient. Indeed, if all your on-chain activities can be grouped together, then even the smallest entry point could compromise the single layer of privacy you had established.

Therefore, it's also necessary to deal with chain analysis in our use of Bitcoin. By doing so, we can minimize the aggregation of our activities and limit the impact of an entry point on our privacy. Precisely, to better counteract chain analysis, what better approach than to familiarize oneself with the methods used in chain analysis? If you want to know how to improve your privacy on Bitcoin, you must understand these methods. This will allow you to better grasp techniques like [Coinjoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) or [Payjoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), and to reduce the mistakes you might make.

In this, we can draw an analogy with cryptography and cryptanalysis. A good cryptographer is first and foremost a good cryptanalyst. To imagine a new encryption algorithm, one must know what attacks it will face, and also study why previous algorithms were broken. The same principle applies to privacy on Bitcoin. Understanding the methods of chain analysis is the key to protecting against it. That's why I'm offering you this article.

It is crucial to understand that chain analysis is not an exact science. It relies on heuristics derived from previous observations or logical interpretations. These rules allow for fairly reliable results, but never with absolute precision. In other words, chain analysis always involves a dimension of probability in the conclusions drawn. We can estimate with more or less certainty that two addresses belong to the same entity, but total certainty will always be out of reach.

The whole objective of chain analysis lies precisely in the aggregation of various heuristics to minimize the risk of error. It is, in a way, an accumulation of evidence that allows us to get closer to reality.

These famous heuristics can be grouped into different categories that we will detail together:
- Transaction patterns (or transaction models);
- Internal heuristics to the transaction;
- External heuristics to the transaction.

It's worth noting that the first two heuristics on Bitcoin were formulated by Satoshi Nakamoto himself. He discusses them in part 10 of the White Paper. As we will see later, it is interesting to observe that these two heuristics still maintain a preeminence in chain analysis today. These are:
- the Common Input Ownership Heuristic (CIOH);
- and address reuse.

Let's explore together the observable characteristics and the interpretations that can be drawn to conduct an analysis.

## Transaction patterns (or transaction models)
A transaction pattern is simply a typical transaction model that can be found on the blockchain, whose interpretation is likely known. When studying patterns, we will focus on a single transaction that we will analyze at a high level. In other words, we will only look at the number of inputs and outputs, without dwelling on its more specific details or its environment. From the observed model, we will be able to interpret the nature of the transaction. We will then look for characteristics about its structure and deduce an interpretation.

### The simple send (or simple payment)
This model is characterized by the consumption of one or more UTXOs as input and the production of two UTXOs as output.

![analysis](assets/en/2.webp)

The interpretation of this model is that we are in the presence of a send or payment transaction. The user has consumed their own UTXOs as input to satisfy in output a payment UTXO and a change UTXO (change coming back to the same user). We therefore know that the observed user is likely no longer in possession of one of the two UTXOs in output (the payment one), but is still in possession of the other UTXO (the change one).

At this point, it is impossible for us to specify which output represents which UTXO, since that is not the goal of this model. We will be able to do so by relying on the heuristics that we will study in the following part. At this stage, our goal is limited to identifying the nature of the transaction in question, which is, in this case, a simple send.

For example, here is a Bitcoin transaction that adopts the simple send pattern:
### Sweep ("sweep" in English)
This model is characterized by the consumption of a single UTXO as input and the production of a single UTXO as output.

![analysis](assets/en/3.webp)

The interpretation of this model is that we are in the presence of a self-transfer. The user has transferred their bitcoins to themselves, to another address they own. Indeed, since there is no change in the transaction, it is very unlikely that we are dealing with a payment. We then know that the observed user is likely still in possession of this UTXO.

For example, here is a Bitcoin transaction that adopts the sweep pattern:
[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)

However, this type of pattern can also reveal a self-transfer to an exchange account (cryptocurrency exchange platform). It will be the study of known addresses and the context of the transaction that will allow us to know if it's a sweep to a self-custody wallet or a withdrawal to a platform.

### Consolidation
This model is characterized by the consumption of several UTXOs as input and the production of a single UTXO as output.

![analysis](assets/en/4.webp)

The interpretation of this model is that we are in the presence of a consolidation. This is a common practice among Bitcoin users, aiming to merge several UTXOs in anticipation of a possible increase in transaction fees. By performing this operation during a period when fees are low, it is possible to save on future fees.

We can deduce that the user behind this transaction was likely in possession of all the UTXOs in input and is still in possession of the UTXO in output. Therefore, it is surely a self-transfer.

Just like the sweep, this type of pattern can also reveal a self-transfer to an exchange account. It will be the study of known addresses and the context of the transaction that will allow us to know if it's a consolidation to a self-custody wallet or a withdrawal to a platform.

For example, here is a Bitcoin transaction that adopts the consolidation pattern:
[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)
### The Batch Spending Model
This model is characterized by the consumption of a few UTXOs as input (often only one) and the production of many UTXOs as output.

![analysis](assets/en/5.webp)

The interpretation of this model is that we are in the presence of a batch spending. This is a practice that likely reveals significant economic activity, such as an exchange, for example. Batch spending allows these entities to save on fees by combining their expenditures into a single transaction.

We can deduce that the UTXO input comes from a company with significant economic activity and that the UTXOs outputs will disperse. Some will belong to the company's clients. Others may go towards partner companies. Finally, there will certainly be a change that returns to the issuing company.

For example, here is a Bitcoin transaction that adopts the batch spending pattern:
[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)

### Protocol-Specific Transactions
Among the transaction patterns, we can also identify models that reveal the use of a specific protocol. For example, Whirlpool coinjoins will have an easily identifiable structure that allows them to be differentiated from other classic transactions.

![analysis](assets/en/6.webp)

The analysis of this pattern suggests that we are likely in the presence of a collaborative transaction. It is also possible to observe a coinjoin. If this latter hypothesis proves to be accurate, then the number of outputs could provide us with an approximate estimate of the number of participants.

For example, here is a Bitcoin transaction that adopts the pattern of the collaborative transaction type coinjoin:
[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)

There are many other protocols that have their own specific structures. Thus, we could distinguish transactions of the Wabisabi type or Stamps transactions, for example.

## Internal Transaction Heuristics
An internal heuristic is a specific characteristic identified within a transaction itself, without the need to examine its environment, which allows us to make deductions. Unlike patterns that focus on the overall structure of the transaction, internal heuristics are based on the set of extractable data. This includes:
- The amounts of different UTXOs both incoming and outgoing;
- Everything related to scripts: receiving addresses, versioning, locktimes...

Generally, this type of heuristic allows us to identify the change in a specific transaction. By doing so, we can then continue to trace an entity across multiple different transactions.

Once again, I remind you that these heuristics are not absolutely precise. Taken individually, they only allow us to identify plausible scenarios. It is the accumulation of several heuristics that contributes to reducing uncertainty, without ever completely eliminating it.

### Internal Similarities
This heuristic involves studying the similarities between the inputs and outputs of the same transaction. If the same characteristic is observed on the inputs and on only one of the outputs of the transaction, then it is likely that this output constitutes the change.

The most obvious characteristic is the reuse of a receiving address in the same transaction.

![analysis](assets/en/7.webp)

This heuristic leaves little room for doubt. Unless their private key has been compromised, the same receiving address inevitably reveals the activity of a single user. The interpretation that follows is that the change of the transaction is the output with the same address as the input. This allows us to continue tracing the individual from this change.

For example, here is a transaction where this heuristic can likely be applied:
[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)

These similarities between the inputs and outputs do not stop at address reuse. Any resemblance in the use of scripts can allow for the application of a heuristic. For example, sometimes the same versioning between an input and one of the outputs of the transaction can be observed.

![analysis](assets/en/8.webp)
In this diagram, we can see that input number 0 unlocks a P2WPKH script (SegWit V0 starting with "bc1q"). Output number 0 uses the same type of script. However, output number 1 uses a P2TR script (SegWit V1 starting with "bc1p"). The interpretation of this characteristic is that it is likely that the address with the same versioning as the input is the change address. It would therefore still belong to the same user.
Here is a transaction where this heuristic can likely be applied:
[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)

In this transaction, we can see that input number 0 and output number 1 use P2WPKH scripts (SegWit V0), while output number 0 uses a different script type, P2PKH (Legacy).

### Round Number Payments
Another internal heuristic that can help us identify the change is that of the round number. Generally, when faced with a simple payment pattern (1 input and 2 outputs), if one of the outputs spends a round amount, then it represents the payment.

![analysis](assets/en/9.webp)

By process of elimination, if one output represents the payment, the other represents the change. Therefore, we can interpret that it is likely that the user in input still possesses the output identified as being the change.

It should be noted that this heuristic is not always applicable, since the majority of payments are still made in fiat currency units. Indeed, when a merchant in France accepts bitcoin, generally, they do not display stable prices in sats. They would rather opt for a conversion between the price in euros and the amount in bitcoins to be paid. Therefore, there should not be a round number in the transaction output. Nevertheless, an analyst could attempt to perform this conversion taking into account the exchange rate in effect when the transaction was broadcast on the network.

If one day, bitcoin becomes the preferred unit of account in our exchanges, this heuristic could become even more useful for analysis.

For example, here is a transaction where this heuristic can likely be applied:
### The Big Spend

When a sufficiently large gap is spotted between two transaction outputs in a simple payment model, it can be estimated that the larger output is likely the change.

![analysis](assets/en/10.webp)

This heuristic of the largest output is probably the most imprecise of all. If identified on its own, it is quite weak. However, this characteristic can be combined with other heuristics to reduce the uncertainty of our interpretation.

For example, if we examine a transaction featuring an output with a round amount and another output with a larger amount, the joint application of the round payments heuristic and that concerning the largest output allows us to reduce our level of uncertainty.

For instance, here is a transaction where this heuristic can likely be applied:
[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)

## External Heuristics to the Transaction
The study of external heuristics is the analysis of similarities, patterns, and characteristics of certain elements that are not inherent to the transaction itself. In other words, if previously we limited ourselves to exploiting elements intrinsic to the transaction with internal heuristics, we are now expanding our field of analysis to the transaction's environment thanks to external heuristics.

### Address Reuse
This is one of the most well-known heuristics among Bitcoiners. Address reuse allows establishing a link between different transactions and different UTXOs. It is observed when a Bitcoin receiving address is used multiple times.

The interpretation of address reuse is that all the UTXOs locked on this address belong (or have belonged) to the same entity. This heuristic leaves little room for uncertainty. When it is identified, the interpretation that follows has a strong chance of corresponding to reality.
As explained in the introduction, this heuristic was discovered by Satoshi Nakamoto himself. In the White Paper, he specifically mentions a solution to prevent users from producing it, which is simply to use a fresh address for each new transaction: "*As an additional firewall, a new pair of keys could be used for each transaction to keep them unlinked to a common owner.*"

For example, here is an address reused across multiple transactions:
[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://mempool.space/address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)

### The Similarity of Scripts and Wallet Fingerprints
Beyond address reuse, there are many other heuristics that can link actions to the same wallet or to a cluster of addresses.

Firstly, an analyst can use similarities in script usage. For example, certain minority scripts like multisig can be more easily spotted than SegWit V0 scripts. The larger the group we hide in, the harder it is to spot us. This is notably why, on the Coinjoin Whirlpool protocol, all participants use exactly the same type of script.

More broadly, an analyst can also focus on the characteristic fingerprints of a wallet. These are specific processes to a usage that one might seek to identify in order to exploit them as tracing heuristics. In other words, if one observes an accumulation of the same internal characteristics on transactions attributed to the traced entity, one can attempt to identify these same characteristics on other transactions.

For example, it can be identified that the traced user systematically sends their change to P2TR* addresses (bc1p…). If this process repeats, it can be used as a heuristic for the continuation of our analysis. Other fingerprints can also be used, such as the order of the UTXOs, the placement of the change in the outputs, the signaling of RBF (Replace-by-Fee), or even, the version number and the locktime.
As [@LaurentMT](https://twitter.com/LaurentMT) specifies in [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (a Francophone podcast), the utility of wallet fingerprints in chain analysis is significantly increasing over time. Indeed, the growing number of script types and the increasingly gradual deployment of these new features by wallet software accentuate the differences. It even happens that one can accurately identify the software used by the traced entity. Therefore, it is important to understand that the study of a wallet's fingerprint is particularly relevant for recent transactions, more so than for those initiated in the early 2010s.
To summarize, a fingerprint can be any specific practice, performed automatically by the wallet or manually by the user, that can be found on other transactions to assist in our analysis.

### The CIOH
The CIOH, for "Common Input Ownership Heuristic," which could be translated as "heuristic of common ownership of inputs" or "co-spending heuristic," is a heuristic stating that when a transaction has multiple inputs, these likely all come from a single entity. Consequently, their ownership is common.

To apply the CIOH, one first observes a transaction that has multiple inputs. This could be two inputs, as well as thirty inputs. Once this characteristic is spotted, one checks if the transaction does not fit into a known pattern. For example, if it has 5 inputs with roughly the same amount and 5 outputs with exactly the same amount, we know that it’s the structure of a Coinjoin Whirlpool. Therefore, the CIOH cannot be applied.

However, if the transaction does not fit into any known pattern of collaborative transaction, then it can be interpreted that all the inputs likely come from the same entity. This can be very useful for expanding an already known cluster or for continuing tracking.

![analysis](assets/en/11.webp)

The CIOH was discovered by Satoshi Nakamoto. He discusses it in part 10 of the White Paper: "*[...] the link is inevitable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner. The risk is that if the owner of a key is revealed, the links may reveal other transactions that belonged to the same owner.*"
It is particularly fascinating to note that Satoshi Nakamoto, even before the official launch of Bitcoin, had already identified the two main privacy vulnerabilities for users, namely the CIOH and address reuse. Such foresight is quite remarkable, as these two heuristics remain, even today, the most useful in chain analysis.

### Off-chain Data
Obviously, chain analysis is not limited to on-chain data. Any data from a previous analysis or accessible on the Internet can also be used to refine an analysis.

For example, if it is observed that the traced transactions are systematically broadcast from the same Bitcoin node and its IP address can be identified, it might be possible to spot other transactions from the same entity.

The analyst also has the option to rely on analyses previously made open-source, or on their own prior analyses. Perhaps one might find an output that points to a cluster of addresses that had already been identified. Sometimes, it is also possible to rely on outputs that point to an exchange, the addresses of these platforms being generally known.

Similarly, one can perform an analysis by elimination. For example, if during the analysis of a transaction with two outputs, one of them is linked to a known but distinct cluster of addresses from the entity being traced, then it can be interpreted that the other output likely represents the change.

Chain analysis also includes a part of OSINT (Open Source Intelligence) that is a bit more generalist with internet searches. This is why it is advised against posting receiving addresses directly on social media or on a website, whether under a pseudonym or not.

### Temporal Models
One might not immediately think of it, but certain human behaviors are recognizable on-chain. The most useful in a study is your sleep pattern! Yes, when you are sleeping, you presumably are not broadcasting Bitcoin transactions. Since you generally sleep at about the same hours, it is common to use temporal analyses in on-chain analysis. It simply involves recording the times at which a given entity's transactions are broadcast to the Bitcoin network. Analyzing these temporal patterns allows us to deduce numerous pieces of information.
First and foremost, a temporal analysis can sometimes identify the nature of the entity being traced. If one observes that transactions are broadcast consistently over 24 hours, this may indicate a strong economic activity. The entity behind these transactions is likely a business, potentially international, and perhaps with automated procedures internally.

For example, I had recognized this pattern a few weeks ago while analyzing a transaction that had mistakenly allocated 19 bitcoins in fees. A simple temporal analysis had allowed me to hypothesize that we were dealing with an automated service, and therefore likely a large entity such as an exchange: https://twitter.com/Loic_Pandul/status/1701127409712452072

Indeed, a few days later, it was discovered that the funds belonged to PayPal, via the Paxos exchange.

Conversely, if one sees that the temporal pattern is rather spread over 16 specific hours, then it can be estimated that we are dealing with an individual user, or perhaps a local business depending on the volumes exchanged.

Beyond the nature of the observed entity, the temporal pattern can also give us an approximate location of the user. We can thus correlate other transactions, and use the timestamp of these as an additional heuristic that can be added to our analysis.

For example, on the address reused several times that I previously mentioned, one can observe that the transactions, whether incoming or outgoing, are concentrated over a 13-hour interval.
![analysis](assets/notext/12.webp)
*Credit: OXT*

This interval likely corresponds to Europe, Africa, or the Middle East. Therefore, it can be interpreted that the user behind these transactions lives there.

In a different register, it is also a temporal analysis of this type that allowed the hypothesis that Satoshi Nakamoto was not operating from Japan, but indeed from the United States: [https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f)

### The Analysis of Volumes
Another external heuristic that can be used is the analysis of trading volumes. Based on the amounts present in each transaction attributed to an entity, this information can be used as an additional heuristic for the rest of the analysis.
This heuristic is obviously quite weak, but it can help reduce uncertainty when added to other heuristics.

## How to protect yourself against chain analysis?
As a Bitcoin user, you have the right to protect your privacy. This stems from your natural rights to own and dispose of yourself, which are inherent to every individual, regardless of any legislative constraint.

This natural right to protect one's privacy is also converted into a claim-right, enshrined in Article 12 of the Universal Declaration of Human Rights, stating that "*No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honour and reputation. Everyone has the right to the protection of the law against such interference or attacks.*".

However, the core business of companies specializing in chain analysis consists precisely of intruding into your private sphere, thus compromising the confidentiality of your correspondence. While one might hope that, in accordance with the aforementioned claim-right, states would vigorously defend our privacy, not only do they neglect to do so, but they also substantially fund the financing of these analysis companies. It would also be vain to hope for support from sector associations, which seem willing to make all concessions in the face of the legislator.

De facto, this claim-right to privacy on Bitcoin does not exist. It is therefore up to you, the user, to assert your natural right and protect the confidentiality of your correspondence. This involves adopting various techniques and usage practices, which will allow you to prevent or deceive the heuristics used for chain analysis.

### Avoiding falling into heuristics
First of all, before considering more radical methods, it is advisable to limit our exposure to the heuristics used for chain analysis as much as possible. As mentioned earlier, the two most powerful heuristics are address reuse and the COINJOIN.

The basic principle for ensuring your privacy on Bitcoin lies in using a new, clean address for each incoming transaction to your wallet. Address reuse is truly the main threat to confidentiality on Bitcoin.
For an individual user, generating a new address for each incoming payment is very simple. Modern wallets do this automatically as soon as you click on "Receive". So, if you place even the slightest importance on the privacy of your transactions, using fresh addresses represents the bare minimum. If you ever need a static point of contact on the internet, instead of putting a receiving address, you can use solutions [like PayNym that implement BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).
Next, if you want to act against chain analysis, avoid merging UTXOs at the input of a transaction. At a minimum, if you really need to merge, prefer UTXOs that have the same source. This recommendation implies having good management of your UTXOs. When buying your bitcoins, prefer transfers involving large amounts to maximize the number of payments you can make without having to merge. I also advise you to label your UTXOs in your software to identify their origin and avoid merging from distinct sources.

More broadly, for all other heuristics, you need to know them to try not to fall into them:
- Do not use minority scripts. Prefer SegWit V0 or possibly SegWit V1;
- Do not make payments in round numbers. For example, if you need to send 100k sats to a friend, send them 114,486 sats. They will buy you a drink in return;
- Try not to always have a change that is much larger than the payment output;
- Do not post your receiving addresses on social media;
- Use your own node under Tor to broadcast your transactions;
- Try not to always broadcast your Bitcoin transactions at the same time…

### Using privacy tools
You can also turn to methods that make your use of Bitcoin ambiguous in order to prevent or deceive chain analysis.

The most popular technique is surely Coinjoin, a collaborative transaction structure that mobilizes several UTXOs of the same amounts. The goal here is to break deterministic links, thus preventing analyses from the present to the past and from the past to the present. Coinjoin allows for plausible deniability by hiding your coins within a large group of indistinguishable coins. If you want to learn more about Coinjoin, both technically and practically, I suggest you read these other articles and tutorials:
- [COINJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [COINJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).
![analysis](assets/en/13.webp)

CoinJoin is an excellent tool for creating plausible deniability for coins, but it is not optimized for all user privacy needs. Specifically, CoinJoin was not designed to become a payment tool. It is very rigid about the amounts exchanged in order to perfect the production of plausible deniability. Since one cannot freely choose the amount of transaction outputs, CoinJoin cannot be used to make payments in bitcoins.

For instance, imagine I want to pay for my baguette in bitcoins while optimizing my privacy. Given the impossibility of selecting the amount of the resulting UTXO from the CoinJoin, I would find myself unable to adjust the amount of my expenditure to the price set by the baker. Therefore, CoinJoin proves inadequate for payment transactions.

Other tools have been conceived to meet privacy needs in more specific use cases. For example, we have [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), a kind of mini-CoinJoin, involving only two participants and based on a structure that allows for payment.

The uniqueness of PayJoin lies in its ability to produce a transaction that looks ordinary, while it is actually a mini-CoinJoin between two users. In this structure, the recipient of the transaction participates among the inputs alongside the actual sender. Thus, the recipient inserts a payment to themselves within the transaction that facilitates the actual payment.

For example, if you buy a baguette from your baker for 6,000 sats from a UTXO of 10,000 sats, and you want to do a PayJoin, your baker will add a UTXO of 15,000 sats that belongs to them as an input to your original transaction, which they will fully recover as an output, in order to deceive the heuristics:

![analysis](assets/en/14.webp)

Transaction fees are neglected to simplify the understanding of the scheme.

The goals of PayJoin are twofold. Firstly, it aims to deceive an external observer by creating a decoy through the COH. Indeed, when an analyst observes this transaction, they will think they can apply the COH, and thus presume a common ownership of the different inputs. In reality, this assumption is incorrect, as one input belongs to the sender, while the other is owned by the recipient. Therefore, PayJoin corrupts chain analysis by leading the analyst down the wrong path.
The second goal of PayJoin is to deceive the analyst about the actual amount of the transaction, thanks to the specific structure of its outputs. Thus, PayJoin falls within the field of steganography. It allows the real amount of the transaction to be concealed within a deceptive transaction.

Indeed, if we revisit our example of using PayJoin to buy a baguette, an external observer might think that we are dealing with a payment of 4,000 sats or 21,000 sats. In reality, the payment for the baguette is 6,000 sats: 21,000 - 15,000 = 6,000. The real value of the payment is therefore hidden within a fake payment that acts as a decoy for chain analysis.

Beyond PayJoin and CoinJoin, there are many other Bitcoin transaction structures that either block chain analysis or deceive it. Among these, I could mention the [Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) and [StonewallX2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b) transactions, which allow either to make a flexible mini Coinjoin or to imitate a flexible mini Coinjoin. There are also [Ricochet](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) transactions that simulate a change of ownership of bitcoins by making a multitude of fake transfers to oneself.

All these tools are available on Samourai Wallet on mobile, and Sparrow Wallet on PC. If you want to learn more about these specific transaction structures, I advise you to discover my tutorials:
- [PAYJOIN](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PAYJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PAYJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

## Conclusion
Chain analysis is a practice that involves trying to trace the flow of bitcoins on-chain. To do this, analysts look for patterns and characteristics in order to draw more or less plausible hypotheses and interpretations.

The accuracy of these heuristics varies: some provide a higher degree of certainty than others, but none can claim to be infallible. However, the accumulation of several converging heuristics can mitigate this inherent doubt, although it remains impossible to completely eliminate it.
We can categorize these methods into three distinct major categories:
- Patterns, focused on the overall structure of each transaction;
- Internal heuristics, which allow for the exhaustive examination of all the details of a transaction, without extending to its context;
- External heuristics, which encompass the analysis of the transaction in its environment, as well as any external data that may provide insight.

As a Bitcoin user, it is essential to master the fundamental principles of chain analysis to effectively counter it and thus protect your privacy.

## Technical Mini-Glossary:
**P2PKH:** acronym for Pay to Public Key Hash. It is a standard script model used to establish spending conditions on a UTXO. It allows locking bitcoins on a hash of a public key, that is, on a receiving address. This script is associated with the Legacy standard and was introduced in the first versions of Bitcoin by Satoshi Nakamoto. Unlike P2PK, where the public key is explicitly included in the script, P2PKH uses a cryptographic imprint of the public key, with some metadata, also called a "receiving address". This script includes the RIPEMD160 hash of the SHA256 of the public key and stipulates that, to access the funds, the recipient must provide a public key matching this hash, as well as a valid digital signature generated from the associated private key. P2PKH addresses are encoded using the Base58Check format, which gives them resistance to typographical errors through the use of a checksum. These addresses always start with the number 1.
**P2TR:** acronym for Pay to Taproot ("pay to the root"). It is a standard script model used to establish spending conditions on a UTXO. P2TR was introduced with the implementation of Taproot in November 2021. It utilizes the Schnorr protocol to aggregate cryptographic keys, as well as Merkle trees for alternative scripts, known as MAST (Merkelized Alternative Script Tree). Unlike traditional transactions where spending conditions are publicly exposed (sometimes at receipt, sometimes at spending), P2TR allows for the hiding of complex scripts behind a single apparent public key. Technically, a P2TR script locks bitcoins on a unique Schnorr public key, denoted as K. However, this K key is actually an aggregate of a public key P and a public key M, the latter being calculated from the Merkle root of a list of ScriptPubKeys. Key aggregation is performed using the Schnorr signature protocol. Bitcoins locked with a P2TR script can be spent in two distinct ways: either by publishing a signature for the public key P, or by satisfying one of the scripts contained in the Merkle tree. The first option is called "key path" and the second "script path." Thus, P2TR allows users to send bitcoins either to a public key or to multiple scripts of their choice. Another advantage of this script is that, although there are multiple ways to spend a P2TR output, only the one that is used needs to be revealed at spending, allowing the unused alternatives to remain private. For example, thanks to Schnorr key aggregation, the public key P can itself be an aggregated key, potentially representing a multisig. P2TR is a version 1 SegWit output, meaning that signatures for P2TR inputs are stored in the witness of a transaction, and not in the ScriptSig. P2TR addresses use Bech32m encoding and start with bc1p.
**P2WPKH:** Acronym for Pay to Witness Public Key Hash. It is a standard script model used to establish spending conditions on a UTXO. P2WPKH was introduced with the implementation of SegWit in August 2017. This script is similar to P2PKH (Pay to Public Key Hash), in that it also locks bitcoins based on the hash of a public key, that is, a receiving address. The difference lies in how signatures and scripts are included in the transaction. In the case of P2WPKH, the signature script information (ScriptSig) is moved from the traditional transaction structure to a separate section called Witness. This move is a feature of the SegWit (Segregated Witness) update. This technique has the advantage of reducing the size of transaction data in the main body, while retaining the necessary script information for validation in a separate section. Consequently, P2WPKH transactions are generally less expensive in terms of fees compared to Legacy transactions. P2WPKH addresses are written using Bech32 encoding, which contributes to a more concise and less error-prone writing thanks to the BCH checksum. These addresses always start with bc1q, making them easily distinguishable from Legacy receiving addresses. P2WPKH is a version 0 SegWit output.

**UTXO:** Acronym for Unspent Transaction Output. A UTXO is a transaction output that has not yet been spent or used as an input for a new transaction. UTXOs represent the fraction of bitcoins that a user owns and that are currently available to be spent. Each UTXO is associated with a specific output script, which defines the necessary conditions to spend the bitcoins. Transactions in Bitcoin consume these UTXOs as inputs and create new UTXOs as outputs. The UTXO model is fundamental to Bitcoin, as it allows for easy verification that transactions are not trying to spend bitcoins that do not exist or have already been spent. Essentially, a UTXO is a piece of Bitcoin.






