---
term: Witness Transaction
---

RGB プロトコルにおいて Witness Transaction とは、Multi Protocol Commitment(MPC)を組み込んだメッセージの Single-Use Seal を閉じる Bitcoin トランザクションを指す。この操作は、プロトコルに書き込まれた契約上のCommitmentをロックするために、既存のUTXOを消費するか、新しいUTXOを作成することからなる。したがってWitness Transactionは、RGBのContractの状態が特定の時点で固定されていることを証明するOn-Chainである。