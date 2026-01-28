---
term: Extra transaction proof
definition: RGB 協定中用於驗證 Tapret 類型承諾的補充資料。
---

在 RGB 協定中，ETP 是 Anchor 的一部分，它整合了驗證 Tapret 型 Commitment 所需的額外資料（在 Taproot 的情況下）。其中包括與 Taproot script 相關的內部公開金鑰，以及 *Script Path Spend* 所需的特定資訊。因此，此元件可確保加密承諾的準確驗證。