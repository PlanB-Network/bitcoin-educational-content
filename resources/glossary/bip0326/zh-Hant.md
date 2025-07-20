---
term: BIP0326
---

一項針對支援 Taproot 交易的 Bitcoin Wallet 軟體開發人員的改進提案。其主要目標是增強可能使用 PTLCs (*Point Time Locked Contracts*)（例如 CoinSwap、Lightning Network 或 DLCs (*Discreet Log Contracts*)）的第二 Layer 協定的隱私性。為了達成這個目標，提案希望透過自動設定 Taproot 交易的「nSequence」欄位，就像設定其他類型交易的「nLocktime」欄位一樣，以阻止搶費攻擊，從而創造似是而非的推诿。換句話說，BIP326 要求 Wallet 軟體使用 `nSequence` 欄位而不是 `nLocktime` 欄位來阻止搶費攻擊，以便以類似的方式為使用此欄位的所有 off-chain 協定提供更高的隱私性。因此，在 `nSequence` 欄位中具有特定值的 Taproot 交易既可以是標準的 Wallet 支出，也可以是具有時間鎖定的第二個 Layer 協定的結算交易，使得這兩種情況無法區分。如果這個改進提案被 Bitcoin Wallet 軟體開發人員廣泛採用，將大大提高 Bitcoin 的整體隱私性和可替代性。