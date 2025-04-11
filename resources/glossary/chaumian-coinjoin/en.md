---
term: CHAUMIAN COINJOIN
---

A coinjoin protocol that utilizes David Chaum's blind signatures and Tor for communications between participants and the coordinator's server. The goal of a Chaumian coinjoin is to ensure participants that the coordinator cannot steal bitcoins, nor link the inputs and outputs together.

To achieve this, users submit their input and a cryptographically blinded reception address to the coordinator. This address, once unblinded, is intended to receive the bitcoins as an output from the coinjoin. The coordinator signs these tokens and returns them to the users. The users then reconnect anonymously to the coordinator's server with a new Tor identity and reveal their output addresses in plaintext for the transaction construction. The coordinator can verify that all these reception addresses come from legitimate users, as he has previously signed their blinded version with his private key. However, he cannot associate a specific output address with a given input user. Therefore, there is no link between the inputs and outputs, even from the coordinator's perspective. Once the transaction is constructed by the coordinator, he sends it back to the participants who sign it to unlock their input, after verifying that their output is indeed in this transaction. The participants send the signature to the coordinator. Once all signatures are collected, the coordinator can broadcast the coinjoin transaction on the Bitcoin network.

![](../../dictionnaire/assets/38.webp)

This method ensures that the coordinator can neither compromise the anonymity of the participants nor steal the bitcoins during the entire coinjoin process.

It is difficult to determine with certainty who first introduced the idea of coinjoin on Bitcoin, and who had the idea to use David Chaum's blind signatures in this context. It is often thought that Gregory Maxwell was the first to discuss it in [a message on BitcoinTalk in 2013](https://bitcointalk.org/index.php?topic=279249.0):

> *"By using Chaum blind signatures: Users connect and provide inputs (and change addresses) as well as a cryptographically blinded version of the address to which they wish to send their private coins; the server signs the tokens and returns them. Users reconnect anonymously, unmask their output addresses, and return them to the server. The server can see that all the outputs have been signed by him and that, therefore, all the outputs come from valid participants. Later, people reconnect and sign."*

Maxwell, G. (2013, August 22). *CoinJoin: Bitcoin privacy for the real world*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0
However, there are other earlier mentions, both for Chaum's signatures in the context of mixing, as well as for coinjoins. [In June 2011, Duncan Townsend presented on BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) a mixer that uses Chaum's signatures in a way quite similar to modern Chaumian coinjoins. In the same thread, there is [a message from hashcoin in response to Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) to improve his mixer. This message precisely presents what most closely resembles coinjoins. There is also a mention of a similar system in [a message from Alex Mizrahi in 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), while he was advising the creators of Tenebrix. The term "coinjoin" itself would not have been invented by Greg Maxwell, but it would come from an idea by Peter Todd.
