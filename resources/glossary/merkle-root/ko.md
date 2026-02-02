---
term: 머클 루트
definition: 블록의 모든 트랜잭션을 요약한 고유한 해시로, 블록 헤더에 포함됨.
---

트리에 있는 모든 정보의 요약을 나타내는 Merkle Tree의 다이제스트 또는 "최상위 Hash"입니다. Merkle Tree는 암호화 어큐뮬레이터 구조로, "Hash 트리"라고도 합니다. Bitcoin의 맥락에서 머클 트리는 블록 내 트랜잭션을 구성하고 특정 트랜잭션의 포함 여부를 신속하게 확인하는 데 사용됩니다. 따라서 Bitcoin 블록에서는 Hash가 하나만 남을 때까지 트랜잭션을 쌍으로 연속적으로 해싱하여 Merkle Root을 얻습니다(Merkle Root). 그런 다음 해당 블록의 헤더에 포함됩니다. 이 Hash 트리는 UTXO 노드 집합을 압축할 수 있는 구조인 UTREEXO와 MAST Taproot에서도 볼 수 있습니다.