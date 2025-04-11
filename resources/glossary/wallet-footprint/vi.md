---
term: WALLET FOOTPRINT

---
A set of distinctive characteristics observable in transactions made by the same Bitcoin wallet. These characteristics can include similarities in the use of script types, reuse of addresses, the order of UTXOs, the placement of change outputs, the signaling of RBF (*Replace-by-Fee*), the version number, the `nSequence` field, and the `nLockTime` field.

Wallet footprints are used by analysts to trace the activities of a particular entity on the blockchain by identifying recurring patterns in its transactions. For example, a user who systematically sends their change to P2TR addresses (`bc1p…`) creates a distinctive footprint that can be used to track their future transactions.

As LaurentMT explains in Space Kek #19 (a French-speaking podcast), the usefulness of wallet footprints in chain analysis significantly increases over time. Indeed, the growing number of script types and the increasingly gradual deployment of these new features by wallet software accentuate the differences. It is even possible to accurately identify the software used by the traced entity. Therefore, it is important to understand that studying a wallet's footprint is particularly relevant for recent transactions, more so than for those initiated in the early 2010s.