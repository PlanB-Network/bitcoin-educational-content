---
term: BIP0008
---

SegWit 使用 BIP9 來啟動，BIP8 是在 SegWit 的爭論之後開發的，它是一種 Soft Fork 啟動方法，本機整合了自動 UASF (*User-Activated Soft Fork*) 機制。如同 BIP9，BIP8 利用 Miner 訊號，但增加了 `LOT` (*Lock-in On Time out*) 參數。如果 `LOT` 設定為 `true`，在信令時間結束但未達到所需閾值時，會自動觸發 UASF，強制啟動 Soft Fork。這種方式強迫礦工合作，否則會有使用者強加 UASF 的風險。此外，與 BIP9 不同的是，BIP8 根據區塊高度定義訊號發佈週期，消除了礦工透過 Hash 速率進行操控的可能性。BIP8 也允許設定可變的投票臨界值，並引進啟動最低區塊高度的參數，讓礦工有時間事先準備並發出同意信號，而不一定要準備就緒。當 Soft Fork 透過 BIP8 以 `LOT=true` 參數啟動時，這會對礦工使用非常激進的方法，礦工會立即面臨潛在的 UASF 壓力。事實上，這讓他們只有 2 個選擇：


- 合作，從而促進啟動過程；
- 不合作，在這種情況下，使用者會自動執行 UASF，強制執行 Soft Fork。