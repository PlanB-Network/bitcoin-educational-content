---
term: BIP0111
definition: 增加 NODE_BLOOM 服務位，允許節點發出其支持布隆過濾器 (BIP37) 的信號。
---

建議增加一個名為 `NODE_BLOOM` 的服務位元，允許節點明確地表示他們支援 BIP37 所描述的 Bloom Filters。引入 `NODE_BLOOM` 後，節點操作者可以停用這項服務，以降低 DoS 的風險。BIP37 選項在 Bitcoin Core 中預設為停用。若要啟用，必須在設定檔中輸入參數 `peerbloomfilters=1` 。