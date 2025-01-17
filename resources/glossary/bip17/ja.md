---
用語BIP17

---
BIP12 と BIP16 と競合した Luke Dashjr による提案。BIP17は新しいオペコード `OP_CHECKHASHVERIFY` を導入し、資金をアンロックする前に `scriptSig` にあるスクリプトを `scriptPubKey` にあるハッシュと照合できるようにした。BIP16（P2SH）は、激しい議論の末、最終的にBIP17（CHV）よりも優先された。