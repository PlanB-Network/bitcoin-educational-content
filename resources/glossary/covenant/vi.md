---
term: COVENANT

---
A mechanism that allows for the imposition of specific conditions on how a given piece of currency can be spent, including in future transactions. Beyond the conditions usually allowed by the script language on a UTXO, the covenant enforces additional constraints on how this Bitcoin can be spent in subsequent transactions. Technically, the establishment of a covenant occurs when the `scriptPubKey` of a UTXO defines restrictions on the `scriptPubKey` of the outputs of a transaction that spends said UTXO. By expanding the scope of the script, covenants would enable numerous developments on Bitcoin such as the bilateral anchoring of drivechains, the implementation of vaults, or the improvement of overlay systems like Lightning. Covenant proposals are differentiated based on three criteria:


- Their scope;
- Their implementation;
- Their recursivity.

There are many proposals that would allow for the use of covenants on Bitcoin. The most advanced in the implementation process are: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO), and `OP_VAULT`. Among other proposals, there are: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, etc.

To better understand the concept of a covenant, consider this analogy: imagine a safe containing 500€ in small bills. If you manage to unlock this safe with the right key, then you are free to use this money as you wish. This is the normal situation with Bitcoin. Now, imagine that the same safe does not contain 500€ in banknotes, but rather meal vouchers of equivalent value. If you succeed in opening this safe, you can use this sum. However, your freedom to spend is restricted, as you can only use these vouchers to pay in certain restaurants. Thus, there is a first condition to spend this money, which is to manage to open the safe with the appropriate key. But there is also an additional condition regarding the future use of this sum: it must be spent exclusively in partner restaurants, and not freely. This system of constraints on future transactions is what is called a covenant.

> ► *In French, there is no term that precisely captures the meaning of the word "covenant". One could talk about "clause", "pact", or "commitment", but these would not exactly correspond to the term "covenant". This term is borrowed from legal terminology that allows describing a contractual clause imposing persistent obligations on a property.*