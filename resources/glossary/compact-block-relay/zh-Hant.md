---
term: 緊湊型塊狀繼電器
---

2016 年透過 BIP152 在 Bitcoin Core 中引入的協定，為網路節點提出節省頻寬的方法。Compact Block Relay 允許以精簡的方式傳輸區塊資訊，其基礎是假設節點在其 Mempool 中已經擁有最近區塊的大部分交易。Compact Block Relay 建議只傳送對等方已知交易的簡短識別碼，以及幾個選定的交易 (主要是 Coinbase Transaction 和節點可能不知道的交易)，而不是完整傳送每個交易，因為這樣會造成重複。節點隨後可以向對等機構請求任何遺漏的交易。Compact Block Relay 因此可以減少區塊傳播時交換的資料量，進而降低頻寬尖峰，並改善網路的整體效率。