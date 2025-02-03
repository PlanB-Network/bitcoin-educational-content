---
term: ELTOO

---
A general protocol for Bitcoin's second layers that defines how to jointly manage the ownership of a UTXO. Eltoo was designed by Christian Decker, Rusty Russell, and Olaoluwa Osuntokun, particularly to solve the problems associated with the negotiation mechanisms of Lightning channel states, that is, between opening and closing. The Eltoo architecture simplifies the negotiation process by introducing a linear state management system, replacing the established penalty-based approach with a more flexible and less punitive update method. This protocol requires the use of a new type of SigHash that allows for ignoring all inputs in the signature of a transaction. This SigHash was initially called `SIGHASH_NOINPUT`, then `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Its implementation is planned in BIP118.

> ► *Eltoo is sometimes also referred to as "LN-Symmetry".*