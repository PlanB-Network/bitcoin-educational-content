---
term: WTXID
definition: SegWit과 함께 도입된 TXID의 확장형으로, witness 데이터를 포함하는 트랜잭션 식별자.
---

SegWit와 함께 도입된 증인 데이터를 포함한 기존 txid의 확장입니다. txid는 증인을 제외한 트랜잭션 데이터의 Hash인 반면, WTXID는 증인을 포함한 전체 트랜잭션 데이터의 `SHA256d`입니다. WTXID는 별도의 Merkle Tree에 저장되며, 그 루트는 Coinbase Transaction에 위치합니다. 이러한 분리를 통해 txid의 트랜잭션 가변성을 제거할 수 있습니다.