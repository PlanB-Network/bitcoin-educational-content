---
term: BIP0326
definition: Use of the nSequence field for Taproot to improve the privacy of second-layer protocols.
---

An improvement proposal for developers of Bitcoin wallet software that supports Taproot transactions. 
Its main goal is to enhance the privacy of second-layer protocols that use PTLCs (*Point Time Locked Contracts*), such as CoinSwap, the Lightning Network, or DLCs (*Discreet Log Contracts*). 
The proposal introduces plausible deniability by automatically configuring the `nSequence` field of Taproot transactions similarly to how the `nLocktime` field was previously set in other transaction types to discourage fee‑sniping attacks. 
In other words, BIP326 encourages wallet software to use the `nSequence` field rather than `nLocktime` for anti‑fee‑sniping purposes, thereby improving privacy for all off‑chain protocols using this field in similar ways. 
As a result, a Taproot transaction with a specific value in the `nSequence` field could either represent a regular wallet spend or a second‑layer settlement transaction with a time lock, making the two indistinguishable. 
If this improvement proposal is widely adopted by Bitcoin wallet software developers, it would greatly improve the privacy and fungibility of Bitcoin overall.
