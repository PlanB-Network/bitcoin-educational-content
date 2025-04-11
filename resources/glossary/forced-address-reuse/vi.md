---
term: FORCED ADDRESS REUSE

---
An attack that involves sending tiny amounts of bitcoins to a large number of receiving addresses. The attacker's goal is to compel the recipients to consolidate these amounts with other UTXOs. The attacker then tracks the future movements of these small quantities of bitcoins, aiming to form clusters of addresses, that is, to determine if multiple addresses belong to the same entity. By cross-referencing the information gathered during the attack with other data and heuristics used in chain analysis, it is possible for the attacker to identify certain entities and their associated addresses. This method represents a threat only to the privacy of users, but does not affect the security of their funds.

> ► *The original term to describe this attack is "Dusting Attack," but some bitcoiners suggest using the term "forced address reuse," as they find the term "dust" to be inappropriate here.*