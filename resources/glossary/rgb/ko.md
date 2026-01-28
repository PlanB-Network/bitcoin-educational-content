---
term: RGB
definition: 비트코인 상에서 실행되는 탈중앙화되고 기밀이 유지되는 스마트 컨트랙트 시스템.
---

Bitcoin 및 Lightning Network와 함께 작동하도록 설계된 분산형 기밀 Smart contract 시스템. RGB은 Client-side Validation 모델에서 작동하며 Contract State의 저장소를 Blockchain에서 분리하여 암호화 커미트먼트만 보관합니다. 이러한 방식으로 전체 상태 기록이 체인 외부에 보관되어 확장성과 기밀성을 높일 수 있습니다. 따라서 RGB을 사용하면 Bitcoin 위에 직접 토큰, 대체 불가능한 토큰, 탈중앙화된 신원 또는 DeFi 솔루션을 저장하는 복잡한 컨트랙트를 생성할 수 있습니다.


RGB에서는 Double-spending에 대한 내성은 Bitcoin의 UTXO가 한 번만 사용할 수 있다는 사실을 활용하는 암호화 메커니즘인 Single-Use Seal를 사용하여 보장됩니다. token의 신뢰성은 Contract 생성부터 가장 최근 상태까지 상태 기록을 클라이언트 측에서 검증함으로써 보장됩니다.