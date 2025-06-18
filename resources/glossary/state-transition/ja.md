---
term: State Transition
---

RGB プロトコルでは、State Transition は Contract の状態を新しいコンフィギュレーションに変更するための操作である。Global State と Owned States の両方のデータを変更することができる．各遷移はContractのSchemaで定義されたルールに従って厳密にチェックされ、変更がGenesisで確立された制約に従うことが保証される。この操作はCommitmentを介してBlockchain Bitcoinに固定される。