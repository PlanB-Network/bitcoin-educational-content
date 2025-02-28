---
term: GAP LIMIT

---
A parameter used in Bitcoin wallet software to determine the maximum number of consecutive unused addresses to generate before stopping the search for additional transactions. Adjusting this parameter is often necessary when recovering a wallet to ensure that all transactions are found. An insufficient Gap Limit could result in missing some transactions if addresses were skipped during the derivation phases. Increasing the Gap Limit allows the wallet to search further in the address sequence, in order to recover all associated transactions.

Indeed, a single `xpub` can theoretically derive more than 4 billion receiving addresses (both internal and external addresses). However, wallet software cannot derive and check all of them for usage without incurring a huge operational cost. Thus, they proceed in index order, as this is normally the order in which all wallet software generates addresses. The software records each used address before moving on to the next one, and it stops its search when it encounters a number of consecutively empty addresses. This number is what is called the Gap Limit.

If, for example, the Gap Limit is set to `20`, and the address `m/84'/0'/0'/0/15/` is empty, the wallet will derive addresses up to `m/84'/0'/0'/0/34/`. If this range of addresses remains unused, the search stops there. Consequently, a transaction using the address `m/84'/0'/0'/0/40/` would not be detected in this example.