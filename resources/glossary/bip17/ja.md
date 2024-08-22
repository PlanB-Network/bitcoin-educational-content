---
term: BIP17
---

Luke Dashjrによる提案で、BIP12およびBIP16と競合しました。BIP17は新しいオペコード`OP_CHECKHASHVERIFY`を導入し、資金を解放する前に`scriptSig`内のスクリプトを`scriptPubKey`内のそのハッシュと照合することを可能にするよう設計されました。激しい議論の期間を経て、BIP16 (P2SH)がBIP17 (CHV)よりも好まれることになりました。