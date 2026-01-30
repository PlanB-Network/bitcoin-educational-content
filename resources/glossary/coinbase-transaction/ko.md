---
term: 코인베이스 트랜잭션
definition: 블록 보상과 서브시디를 받기 위해 마이너가 생성하는 블록의 첫 번째 트랜잭션.
---

Coinbase Transaction은 Bitcoin Blockchain의 모든 블록에 포함된 특별하고 고유한 트랜잭션입니다. 이는 블록의 첫 번째 트랜잭션을 나타내며 Proof of Work(*Proof-of-Work*)을 검증하는 헤더, 즉 목표보다 작거나 같은 헤더를 성공적으로 찾은 Miner에 의해 생성됩니다.


Coinbase Transaction은 주로 두 가지 목적으로 사용됩니다: Miner에 Block reward을 수여하고 유통 화폐인 Supply에 새로운 비트코인을 추가하는 것입니다. 채굴자가 Proof of Work에 참여하도록 하는 경제적 인센티브인 Block reward에는 블록에 포함된 거래에 대한 누적 수수료와 새로 생성된 일정 금액의 무상의 비트코인(블록 보조금)이 포함됩니다. 2009년에 처음 블록당 50비트코인으로 설정된 이 금액은 "Halving"라는 이벤트 기간 동안 21만 블록마다(약 4년마다) 절반으로 줄어듭니다


Coinbase Transaction는 몇 가지 점에서 일반 트랜잭션과 다릅니다. 첫째, 입력이 없으므로 기존 트랜잭션 출력(UTXO)이 소비되지 않습니다. 다음으로, Coinbase Transaction의 서명 스크립트(`scriptSig`)에는 일반적으로 사용자 지정 메시지나 Mining 소프트웨어 버전 정보와 같은 추가 데이터를 통합할 수 있는 임의의 필드가 포함되어 있습니다. 마지막으로, Coinbase Transaction에서 생성된 비트코인은 체인 재구성 시 존재하지 않는 비트코인의 잠재적 지출을 방지하기 위해 100블록(101개 확인)의 만기 기간을 거쳐야 사용할 수 있습니다.


