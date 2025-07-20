---
term: GETWORK
---

GETWORK 是由 m0mchil 於 2010 年為 Bitcoin 建立的舊 Mining 協定。它允許礦工從 Full node 接收工作資料。它基於 RPC 請求，能夠獲得區塊標頭以找到有效的 Proof of Work。GETWORK 已針對 GPU Mining 進行最佳化。它是第一個開放原始碼軟體，旨在優化節點與礦工之間的通訊，當時只有少數玩家將這類軟體保密。GETWORK 漸漸被 Stratum 取代，Stratum 更有效率，特別是對 ASIC 而言，對頻寬的需求也較少。