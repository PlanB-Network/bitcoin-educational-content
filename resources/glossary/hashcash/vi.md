---
term: HASHCASH

---
HashCash is a proof-of-work system designed by Adam Back in 1997 to combat spam and DoS attacks. It is based on the principle that a sender must perform a computational task (specifically, finding a partial collision on a cryptographic hash function) to prove their work. This task is costly in terms of time and energy for the sender, but verifying the result by the recipient is quick and simple. This protocol has proven particularly suited to fighting spam in email communications, as it is minimally burdensome for legitimate users while posing a significant obstacle for spammers. Indeed, sending a single email requires a few seconds of computation, but replicating this operation millions of times becomes extremely costly in terms of energy and time, which often negates the economic interest of spam campaigns, whether they are for marketing purposes or malicious. Moreover, it allows for the preservation of the sender's anonymity.

HashCash was quickly adopted by cypherpunks who were looking to develop an anonymous electronic currency system without intermediaries. Indeed, Adam Back's innovation introduced the concept of scarcity in the digital world for the first time. The concept of proof of work is then found in several electronic currency systems predating Bitcoin, including:


- b-money by Wei Dai published in 1998;
- R-POW by Hal Finney published in 2004;
- BitGold by Nick Szabo published in 2005.

The principle of HashCash is also found within the Bitcoin protocol, where it is used as a protection mechanism against Sybil attacks.