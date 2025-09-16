---
term: ADDRESS SPOOFING
---

An attack in which a malicious actor generates an address (or another payment identifier) that closely resembles the victim's address. The goal is to trick the user into copying the wrong address when making a transaction, resulting in the bitcoins being sent to the attacker instead of the intended recipient.

The attacker exploits the user's haste, who may copy the wrong address if he performs the transaction without carefully verifying its accuracy. A common method to execute this attack is by sending small payments to the victim’s wallet, thereby inserting the spoofed address into their transaction history. This type of attack is more common with altcoins, where address reuse is more prevalent. In Bitcoin, address reuse is discouraged and the use of fresh addresses is more common, which helps reduce the risk. However, Bitcoin users are not immune to this type of attack.

Another method used to present the wrong address to the victim is the use of fraudulent wallet software that mimics legitimate applications, or by tampering with the address when a machine is compromised, between the time it is copied and the time the transaction is created. This is sometimes referred to as "*Address swapping*".

To protect against such attacks, it is important to check several characters of the address, especially its checksum (at the end), on the screen of the signing device before signing the transaction.

> ► *This attack is also sometimes referred to as "Address Poisoning".*