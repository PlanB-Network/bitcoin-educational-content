---
term: PSBT

---
Acronym for "Partially Signed Bitcoin Transaction". It is a specification introduced with BIP174 to standardize the way in which unfinished transactions are constructed in software related to Bitcoin, such as wallet software. A PSBT encapsulates a transaction in which the inputs may not be fully signed. It includes all the necessary information for a participant to sign the transaction without requiring additional data. Thus, a PSBT can take on 3 different forms:


- A fully constructed transaction, but not yet signed;
- A partially signed transaction, where some inputs are signed while others are not yet;
- Or a fully signed Bitcoin transaction, which can be converted to be ready for broadcast on the network.

The PSBT format facilitates interoperability between different wallet software and signature devices (hardware wallet). Currently, version 0 of the PSBT is used, as defined in BIP174, but version 2 is being proposed via BIP370.

> ► *Version 1 of the PSBT does not exist. Since version 0 was the first version, the second version was informally called version 2. Ava Chow, who authored BIP370, thus decided to assign number 2 to this new version to avoid any confusion.*