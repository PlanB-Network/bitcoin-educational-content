---
term: Anchor
---

RGB 프로토콜에서 Anchor은 트랜잭션에 단일 Commitment이 포함되어 있음을 증명하는 데 사용되는 클라이언트 측 데이터 집합을 나타냅니다. RGB 프로토콜에서 Anchor은 다음 Elements로 구성됩니다:




- Witness Transaction에서 Bitcoin transaction ID(txid);
- Multi Protocol Commitment(MPC);
- Deterministic Bitcoin Commitment(DBC);
- Tapret Commitment 메커니즘을 사용하는 경우 추가 거래 증명(ETP).


따라서 Anchor는 특정 Bitcoin 트랜잭션과 RGB 프로토콜로 검증된 개인 데이터 사이에 검증 가능한 링크를 설정하는 역할을 합니다. 이 데이터는 정확한 내용이 공개적으로 공개되지 않더라도 실제로 Blockchain에 포함되어 있음을 보장합니다.