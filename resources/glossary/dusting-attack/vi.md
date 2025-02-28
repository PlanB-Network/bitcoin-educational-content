---
term: DUSTING ATTACK

---
A Dusting Attack involves sending tiny amounts of bitcoins to a large number of receiving addresses. The attacker's goal is to compel the recipients to consolidate these amounts with other UTXOs. The attacker then tracks the future movements of these small amounts of bitcoins, aiming to form clusters of addresses, that is, to determine if multiple addresses belong to the same entity. By correlating the information gathered during a dusting attack with other data and heuristics used in chain analysis, it is possible for the attacker to identify certain entities and their associated addresses. This method represents a threat only to the privacy of users, but does not affect the security of their funds.

> ► *Some bitcoiners suggest no longer using the term "dusting attack" as it may be misleading. Indeed, the term "dust" describes something very specific in Bitcoin Core. If the dusting attack actually used dust as described in Core, the attack would be ineffective. Therefore, some suggest using the term "forced address reuse" to more accurately describe this attack.*