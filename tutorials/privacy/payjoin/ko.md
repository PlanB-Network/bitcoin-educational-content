---
name: Payjoin
description: Bitcoin의 PayJoin란 무엇인가요?
---
![Payjoin thumbnail - steganography](assets/cover.webp)





## Bitcoin에서 PayJoin 트랜잭션 이해하기


PayJoin는 결제 수신자와의 협업을 통해 결제 시 사용자 개인정보 보호를 강화하는 Bitcoin 트랜잭션의 특정 구조입니다.


2015년에 [LaurentMT](https://twitter.com/LaurentMT)는 [여기](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt)에 액세스할 수 있는 문서에서 이 방법을 "스테가노그래피 트랜잭션"이라고 처음 언급했습니다. 이 기법은 이후 사무라이 Wallet에 의해 채택되었으며, 2018년 Stowaway 툴로 이를 구현한 최초의 클라이언트가 되었습니다. PayJoin의 개념은 [BIP79](https://github.com/Bitcoin/BIPs/blob/master/BIP-0079.mediawiki) 및 [BIP78](https://github.com/Bitcoin/BIPs/blob/master/BIP-0078.mediawiki)에서도 찾아볼 수 있습니다. PayJoin을 지칭하기 위해 여러 용어가 사용됩니다:


- PayJoin
- 스타우어웨이
- P2EP(엔드-투-엔드 포인트 결제)
- 스테가노그래피 트랜잭션


PayJoin의 독창성은 언뜻 평범해 보이지만 실제로는 두 당사자 간의 미니 CoinJoin인 거래를 generate로 만들 수 있다는 데 있습니다. 이를 위해 트랜잭션 구조에는 실제 송금인과 함께 결제 수취인이 입력에 포함됩니다. 수취인은 거래 중간에 자신에 대한 지불을 포함하며, 이를 통해 대금을 받을 수 있습니다.


구체적인 예를 들어 '4000 Sats'의 UTXO을 사용하여 '10,000 Sats'의 바게트를 구매하고 PayJoin을 선택하면 제빵사는 '4000 Sats'에 더해 자신이 속한 '15,000 Sats'의 UTXO을 입력으로 추가하여 출력으로 전액 수령하게 됩니다:

![Payjoin transaction diagram](assets/en/1.webp)


이 예에서 제빵사는 `15,000 Sats`을 입력으로 입력하고 `19,000 Sats`이 출력으로 나오며, 그 차이는 정확히 `4000 Sats`으로 바게트 가격입니다. 사용자 측에서는 `10,000 Sats`을 입력하면 `6,000 Sats`이 출력으로 나오며, 이는 바게트 가격인 `-4000 Sats`의 잔액을 나타냅니다. 예시를 단순화하기 위해 이 거래에서 일부러 Mining 수수료를 생략했습니다.


## PayJoin 거래의 목적은 무엇인가요?


PayJoin 거래는 사용자의 결제 개인정보 보호를 강화하는 두 가지 목적을 달성하기 위한 것입니다.

우선, PayJoin는 체인 분석에서 미끼를 만들어 외부 관찰자를 오도하는 것을 목표로 합니다. 이는 공통 입력 Ownership 휴리스틱(CIOH)을 통해 가능합니다. 일반적으로 Blockchain의 트랜잭션에 여러 개의 입력이 있는 경우, 이러한 모든 입력은 동일한 엔터티 또는 사용자의 것으로 간주합니다. 따라서 분석가가 PayJoin 트랜잭션을 조사할 때 모든 입력이 동일한 사람으로부터 나온 것이라고 믿게 됩니다. 그러나 결제 수취인도 실제 결제자와 함께 입력을 기여하기 때문에 이러한 인식은 잘못된 것입니다. 따라서 연쇄 분석은 잘못된 것으로 판명된 해석으로 전환됩니다.


또한 PayJoin은 실제 지불된 금액에 대해 외부 관찰자를 속이는 것도 허용합니다. 분석가는 거래 구조를 살펴봄으로써 지불 금액이 산출물 중 하나의 금액과 동일하다고 믿을 수 있습니다. 그러나 실제로는 결제 금액이 산출물 중 어느 것과도 일치하지 않습니다. 실제로는 수신자의 산출물 UTXO과 수신자의 입력물 UTXO 사이의 차액입니다. 이러한 의미에서 PayJoin 트랜잭션은 스테가노그래피의 영역에 속합니다. 이를 통해 미끼 역할을 하는 가짜 트랜잭션 내에 실제 거래 금액을 숨길 수 있습니다.


**Stenography 정의에 유의하십시오:

> 스테가노그래피는 숨겨진 정보의 존재를 인지할 수 없도록 다른 데이터나 객체 안에 정보를 숨기는 기술입니다. 예를 들어, 비밀 메시지를 텍스트의 점 안에 숨겨서 육안으로 감지할 수 없도록 하는 것이 마이크로포인트 기법입니다. 복호화 키 없이는 정보를 이해할 수 없게 만드는 암호화와 달리 스테가노그래피는 정보를 수정하지 않습니다. 정보는 눈에 잘 띄는 상태로 유지됩니다. 스테가노그래피의 목적은 비밀 메시지의 존재를 숨기는 것이지만, 암호화는 키 없이는 접근할 수 없지만 숨겨진 정보의 존재를 명확하게 드러냅니다.

바게트 결제를 위한 PayJoin 거래의 예로 돌아가 보겠습니다.

![Payjoin transaction schema from the outside](assets/en/2.webp)

일반적인 체인 분석의 휴리스틱을 따르는 외부 관찰자는 Blockchain에서 이 거래를 보고 다음과 같이 해석할 수 있습니다: "*Alice은 '19,000 Sats'을 Bob*에 지불하기 위해 2개의 UTXO를 트랜잭션의 입력으로 병합했습니다."

![Incorrect interpretation of Payjoin transaction from the outside](assets/en/3.webp)

이미 아시다시피 두 개의 입력 UTXO는 동일한 사람의 소유가 아니므로 이 해석은 명백히 잘못된 것입니다. 또한 실제 지불 가치는 '19,000 Sats'가 아니라 '4,000 Sats'입니다. 따라서 외부 관찰자의 분석은 이해관계자의 프라이버시 보호를 보장하면서 잘못된 결론으로 향하게 됩니다.![PayJoin 트랜잭션 다이어그램](assets/en/1.webp)

실제 PayJoin 트랜잭션을 분석하고 싶으시다면, Testnet에서 수행한 트랜잭션을 참고하세요: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://Mempool.space/fr/Testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)



**외부 리소스:**


- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/Bitcoin/BIPs/blob/master/BIP-0078.mediawiki.
- https://PayJoin.org/

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c