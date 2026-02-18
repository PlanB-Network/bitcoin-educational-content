---
term: BIP0023
definition: Extension of BIP22 for mining pools, allowing miners to audit and modify proposed blocks.
---

This BIP is an extension of BIP22, aiming to encourage its adoption by the software used by mining pools, especially by the Getwork protocol, the predecessor of Stratum. Proposed by Luke Dashjr, this extension seeks to integrate the BIP22 standard into Getwork by default, in order to facilitate its adoption by mining pools. 
The main goal of BIP23 is to transmit the entire block template to miners, allowing them to audit and possibly modify the structure of the block proposed by the pool. This approach was intended to address concerns about mining centralization by giving individual miners greater control and transparency over the block creation process.