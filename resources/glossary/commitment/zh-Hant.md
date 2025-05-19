---
term: Commitment
---

Commitment (在密碼學的意義上) 是一個數學物件，表示為 $C$，由結構化資料 $m$(訊息) 和隨機值 $r$ 的運算確定地衍生出來。我們寫成 ：


$$
C = \text{commit}(m, r)
$$


此機制包含兩個主要操作：




- 承認：我們將一個加密函數應用於一個訊息 $m$ 和一個隨機 $r$ 以產生 $C$ ；
- 驗證：我們使用 $C$、$m$ 訊息和 $r$ 值來檢查此 Commitment 是否正確。函式會回傳 `True` 或 `False`。


Commitment 必須尊重兩個屬性：




- 綁定：一定不可能找到兩個不同的訊息產生相同的 $C$ ：


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


例如：


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- 隱藏: $C$ 的知識不能透露 $m$ 的內容.


在 RGB 通訊協定的情況下，Commitment 會包含在 Bitcoin 交易中，以證明在特定時間某項資訊的存在，而不會揭露資訊本身。