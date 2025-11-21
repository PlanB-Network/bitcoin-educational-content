---
term: Anchor 輸出
---

一項旨在改善 Lightning 通道內交易費用管理的提案。Lightning 通道每次發生狀態變更時，利益相關者都會創建並簽署一份新的 Commitment Transaction，以反映通道內新的資金分配情況。此機制的問題在於在創建時確定交易費用。事實上，Bitcoin 網路的交易費用會大幅波動，無論是向上或向下。如果在單邊關閉通道時，最後一個 Commitment Transaction 設定的費用不足，不僅交易需要相當長的時間才能確認，而且時間鎖定機制 (timelocks) 也可能讓資金被盜用。Anchor 輸出在 Commitment Transaction 中保留一小部分資金，以支付未來的費用。在網路擁塞和費用上升的情況下，Anchor 輸出允許在建立 Commitment Transaction 之後修改交易費用，從而確保充分快速地關閉「閃電」通道。