---
term: Betterhash
definition: Mining protocol allowing miners to control transaction selection themselves, reducing pool centralization. Precursor to Stratum V2.
---

A mining protocol developed by Matt Corallo in 2018 to counter the growing centralization of mining within pools. It differs from Stratum, the standard protocol at the time, by giving individual miners more control over which transactions are included in block templates. The main idea behind BetterHash is to return to miners the ability to construct block templates themselves while still benefiting from mining pools' advantages, such as reduced revenue variance.

In the Stratum protocol, mining pools control block template creation, selecting the transactions to include in blocks and determining the chain to mine on. This centralization weakens Bitcoin by making the transaction confirmation process more vulnerable to censorship.

BetterHash enables miners to regain control of these operations while allowing pools to continue managing reward distribution. It is considered one of the precursors to Stratum V2.