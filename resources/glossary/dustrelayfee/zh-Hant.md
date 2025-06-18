---
term: DUSTRELAYFEE
---

網路節點使用的標準化規則，用以決定他們認為的 「Dust 限制」。此參數設定了以 Sats 為單位的每虛擬千位元組收費率 (Sats/kvB)，作為計算 UTXO 的價值是否少於將其納入交易的必要費用的參考。事實上，如果 UTXO 所需的轉讓費用高於其本身所代表的價值，則該 UTXO 會被視為 Bitcoin 上的「Dust」。此限制的計算如下：


```text
limit = (input size + output size) * fee rate
```


由於要包含在 Bitcoin 區塊中的交易所需的費率不斷變化，「DustRelayFee」參數允許每個節點定義在此計算中使用的費率。根據預設，在 Bitcoin Core 上，此值設定為 3,000 Sats/kvB。例如，若要計算 P2PKH 輸入和輸出（分別為 148 和 34 位元組）的 Dust 限制，則計算方法如下：


```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```


這表示有關節點不會轉送包括 P2PKH 安全 UTXO 值小於 546 Sats 的交易。