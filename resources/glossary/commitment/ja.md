---
term: Commitment
---

Commitment（暗号的な意味でのCommitment）とは、構造化データ$m$（メッセージ）に対する演算と、乱数値$r$から決定論的に導かれる数学的オブジェクトのことで、$C$と表記する。と書く：


$$
C = \text{commit}(m, r)
$$


このメカニズムは、主に2つのオペレーションから構成されている：




- コミット：メッセージ$m$とランダム$r$に暗号関数を適用し、$C$を生成する；
- Verify: $C$、$m$メッセージ、$r$値を用いて、このCommitmentが正しいかどうかをチェックする。この関数は `True` または `False` を返す。


Commitmentは2つの特性を尊重しなければならない：




- バインド：同じ$C$を生成する2つの異なるメッセージを見つけることは不可能でなければならない：


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


など：


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- 隠蔽：$C$の知識によって$m$の内容が明らかになってはならない。


RGBプロトコルの場合、Bitcoinトランザクションの中にCommitmentが含まれ、情報そのものを開示することなく、ある時点におけるある情報の存在を証明する。