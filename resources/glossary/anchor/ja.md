---
term: Anchor
---

RGBプロトコルでは、Anchorは、トランザクションに1つのCommitmentが含まれることを 証明するために使用されるクライアント側データのセットを表す。RGBプロトコルでは、Anchorは以下のElementsから構成される：




- Witness Transactionからtransaction ID Bitcoin（txid） ；
- Multi Protocol Commitment（MPC）；
- Deterministic Bitcoin Commitment（DBC）；
- Tapret Commitment メカニズムが使用されている場合は、ETP（Extra Transaction Proof）。


したがって、Anchor は、特定の Bitcoin トランザクションと RGB プロトコルによって検証されたプライベート・データとの間に検証可能なリンクを確立する役割を果たす。Anchorは、これらのデータがBlockchainに含まれていることを保証します。