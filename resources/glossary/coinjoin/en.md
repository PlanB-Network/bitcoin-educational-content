---
term: COINJOIN
---

Coinjoin is a technique used to break the traceability of bitcoins. It relies on a collaborative transaction with a specific structure of the same name: the coinjoin transaction. Coinjoin transactions help improve the privacy protection of Bitcoin users by making it more difficult for external observers to analyze transactions. This structure allows for mixing multiple coins in a single transaction, making it difficult to determine the links between input and output addresses.

The general operation of coinjoin is as follows: different users wishing to mix deposit an amount as input of a transaction. These inputs will come out as different outputs of the same amount. At the end of the transaction, it is impossible to determine which output belongs to which user. There is technically no link between the inputs and outputs of the coinjoin transaction. The link between each user and each UTXO is broken, in the same way that the history of each coin is.

![](../../dictionnaire/assets/4.webp)

To allow for coinjoin without any user losing control over their funds at any time, the transaction is first constructed by a coordinator and then transmitted to each user. Each one then signs the transaction on their side after verifying that it suits them, and then all the signatures are added to the transaction. If a user or the coordinator attempts to steal the funds of others by modifying the outputs of the coinjoin transaction, then the signatures will be invalid and the transaction will be rejected by the nodes. When the recording of the participants' output is done using Chaum's blind signatures to avoid the link with the input, this is referred to as "Chaumian coinjoin".

This mechanism increases the confidentiality of transactions without requiring modifications to the Bitcoin protocol. Specific implementations of coinjoin, such as Whirlpool, JoinMarket, or Wabisabi, offer solutions to facilitate the coordination process among participants and enhance the efficiency of the coinjoin transaction. Here is an example of a coinjoin transaction:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

It is difficult to determine with certainty who first introduced the idea of coinjoin on Bitcoin, and who had the idea of using David Chaum's blind signatures in this context. It is often thought that Gregory Maxwell was the first to discuss it in [a message on BitcoinTalk in 2013](https://bitcointalk.org/index.php?topic=279249.0):
Using Chaum blind signatures: Users connect and provide inputs (and change addresses) as well as a cryptographically blinded version of the address to which they wish to send their private coins; the server signs the tokens and returns them. Users reconnect anonymously, unmask their output addresses, and send them back to the server. The server can see that all the outputs have been signed by it and that, consequently, all the outputs come from valid participants. Later, people reconnect and sign.
Maxwell, G. (2013, August 22). *CoinJoin: Bitcoin privacy for the real world*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

However, there are earlier mentions, both for Chaum signatures in the context of mixing, as well as for coinjoins. [In June 2011, Duncan Townsend presents on BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) a mixer that uses Chaum signatures in a way quite similar to modern Chaumian coinjoins. In the same thread, there is [a message from hashcoin in response to Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) to improve his mixer. This message presents what most closely resembles coinjoins. There is also a mention of a similar system in [a message from Alex Mizrahi in 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), while he was advising the creators of Tenebrix. The term "coinjoin" itself was not invented by Greg Maxwell, but it came from an idea by Peter Todd.

> ► *The term "coinjoin" does not have a French translation. Some bitcoiners also use the terms "mix", "mixing", or "mixage" to refer to the coinjoin transaction. Mixing is rather the process used at the heart of the coinjoin. Also, it is important not to confuse mixing through coinjoins with mixing through a central actor who takes possession of the bitcoins during the process. This has nothing to do with the coinjoin where the user does not lose control of their bitcoins during the process.*