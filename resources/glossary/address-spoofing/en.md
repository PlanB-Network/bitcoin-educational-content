---
term: Address SPOOFING
---

Attack in which a malicious actor creates an address (or other payment identifier) closely resembling that of the victim. The aim is to trick the user into copying this wrong address during a transaction, which results in bitcoins being sent to the attacker instead of the intended destination.

The attacker exploits the user's haste to copy the wrong address if he carries out the transaction without checking its accuracy. In general, to implement this attack, the attacker makes payments with small sums to the victim's wallet to integrate the false address into his transaction history. This attack tends to be used with altcoins, where it is common practice to reuse the same receiving addresses, unlike Bitcoin, where the use of blank addresses for each transaction is a more widespread practice. However, Bitcoin users are not immune to this attack.

Another method of putting the wrong address in front of the victim is the use of fraudulent wallet management software that mimics legitimate software, or changing the address when a machine is compromised, between the time it is copied and the time the transaction is built. This is sometimes referred to as "*Address swapping*".

To protect yourself against these different methods of attack, it is important to check several characters of the address, especially its checksum (at the end), on the screen of the signing device before signing the transaction.

> ► *This attack is also sometimes referred to as Address Poisoning