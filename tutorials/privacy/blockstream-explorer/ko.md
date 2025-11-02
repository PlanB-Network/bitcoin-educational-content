---
name: BLOCKSTREAM 탐색기
description: Bitcoin 및 Liquid Network의 주요 Layer 살펴보기
---

![cover](assets/cover.webp)



BLOCKSTREAM 익스플로러는 트랜잭션 탐색을 용이하게 하는 프로젝트로, Bitcoin 프로토콜의 Global State와 BLOCKSTREAM 회사에서 개발한 [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid의 탐색을 용이하게 합니다.



아담 백이 설립한 BLOCKSTREAM이 2014년에 시작한 [BLOCKSTREAM.info](https://BLOCKSTREAM.info) 탐색기는 Bitcoin을 위한 강력한 인프라를 제공하여 계층 간 상호 운용성 및 거래 추적을 보장하는 동시에 사용자 보안과 프라이버시를 강화하는 것을 목표로 하고 있으며 레이어(On-Chain과 Liquid) 간 상호 운용성을 보장합니다.



이 튜토리얼에서는 Bitcoin의 차별화 요소와 서비스, On-Chain 및 Liquid 계층의 운영 및 상태를 원활하게 모니터링하는 방법을 소개합니다.



## BLOCKSTREAM 시작하기



### 메인 채널 탐색



BLOCKSTREAM.info 탐색기로 이동하면 "**대시보드**"에서 기본 Bitcoin 프로토콜 채널이 기본적으로 선택되어 있습니다. 이 Interface에서는 에 대한 개요를 볼 수 있습니다:





- 메인 체인 크기: 최근 채굴된 블록.



![blocks](assets/fr/01.webp)



이 섹션에서는 최근 채굴된 블록, Timestamp, 각 BLOCK에 포함된 트랜잭션 수, 킬로바이트(kB) 단위의 크기, 각 BLOCK의 무게 단위(**WU** = *중량 단위*) 측정값에 대한 정보를 제공합니다. 이 마지막 측정값은 메인 체인의 각 BLOCK이 `4,000,000 WU` 또는 `4,000 kWU`로 제한된다는 점을 감안할 때 BLOCK의 최적화를 평가할 수 있게 해주기 때문에 흥미롭습니다.





- 최근 거래.



![transactions](assets/fr/02.webp)



트랜잭션 섹션에서는 트랜잭션의 고유 식별자, 관련된 Bitcoin 값, 모든 데이터(입력 및 출력)의 합계를 나타내는 가상 바이트(vB) 크기, 관련 요금률에 대한 정보를 제공합니다. 예를 들어 '2 sat/vB'의 비율로 크기가 '153 vB'인 트랜잭션은 '306 사토시'의 요금이 부과됩니다.



### 유체 탐색



"**블록**" 메뉴에서 마지막으로 채굴된 BLOCK까지 전체 메인 체인의 이력을 추적할 수 있습니다.



![blocs](assets/fr/03.webp)



특정 BLOCK를 클릭하면 여기에 포함된 정보 및 거래에 대한 자세한 내용을 확인할 수 있습니다. 예를 들어, BLOCK 919330의 경우 BLOCK의 Hash이 있습니다. 또한 채굴된 각 BLOCK(Genesis 제외)는 이전 BLOCK에 연결되어 이전 Hash을 유지하므로 이전 BLOCK로 이동할 수도 있습니다.



![metadata](assets/fr/04.webp)



"세부 정보"** 버튼을 클릭하면 이 BLOCK에 대한 자세한 정보(예: 보유 및 전파된 메인 체인에 추가되었음을 확인할 수 있는 상태)를 확인할 수 있습니다. 또한 이 BLOCK이 채굴되는 난이도도 확인할 수 있습니다. 이 난이도는 Mining의 암호화 문제를 해결하는 데 필요한 컴퓨팅 파워를 나타내며 2016블록(약 2주)마다 조정됩니다.



![details](assets/fr/05.webp)



이 세부 정보 섹션 아래에서 이 BLOCK에 포함된 모든 트랜잭션을 확인할 수 있습니다.



BLOCK의 첫 번째 트랜잭션을 **거래 코인베이스**라고 합니다. 이는 Miner의 Mining 보상(BLOCK에 포함된 거래와 관련된 모든 수수료 및 BLOCK 보조금)을 할당하는 데 사용됩니다. 이 거래로 생성된 비트코인은 100개의 블록이 연속으로 채굴된 후에만 사용할 수 있습니다. 즉, Miner를 사용하려면 BLOCK **919430**이 생산될 때까지 기다려야 합니다. 이를 [*"만기 기간"*](https://planb.network/fr/resources/glossary/maturity-period)이라고 합니다.



코인베이스는 이전 거래에서 비트코인을 사용하지 않기 때문에 실제 입력이 없는 유일한 거래입니다.




![coinbase](assets/fr/06.webp)



다른 모든 트랜잭션은 입력과 출력의 두 섹션으로 나뉩니다.



비트코인을 새 거래의 입력으로 사용하려면 거래 개시자가 특정 스크립트에 해당하는 서명을 제공하여 자신의 소유를 증명해야 합니다. 각 비트코인(UTXO)에는 일반적으로 보유자의 개인 키만 제공할 수 있는 특정 서명을 요구하는 스크립트가 포함되어 있습니다. 이러한 스크립트는 Bitcoin 스크립트로 작성된 ***scriptSig***(ASM)이며, 다양한 유형이 있을 수 있습니다. 이 예제에서는 P2WPKH(*Pay-to-Witness-Public-Key-Hash*) 유형의 출력에 P2SH 유형의 UTXO가 사용되었음을 알 수 있습니다.



휴리스틱을 사용하여 특정 UTXO의 이력을 추적할 수 있습니다. 다양한 Bitcoin 휴리스틱과 Bitcoin 거래의 기밀성을 강화하는 방법에 대해 알아보세요:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



이 거래의 송금 비용을 예로 들어보겠습니다. 거래 식별자를 클릭하면 거래 세부 정보 페이지의 **거래** 섹션으로 리디렉션됩니다.



![transaction](assets/fr/08.webp)



이 페이지에서 트랜잭션이 어떤 BLOCK에 포함되었는지 확인할 수 있습니다. 사용된 Address 유형에 따라 트랜잭션은 데이터(*가상 바이트*)를 최적화할 수 있으므로 트랜잭션 수수료를 더 적게 지불할 수 있습니다. 예를 들어, 이 트랜잭션은 `bc1q`로 시작하는 기본 SegWit BECH32 Address 형식을 사용하여 수수료를 53% 절감했습니다.



![trx_details](assets/fr/09.webp)



## Liquid 코팅



Liquid Network는 [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain)이며 Bitcoin 프로토콜을 위한 레벨 2 오픈 소스 솔루션입니다. 특히 더 빠르고 기밀이 유지되는 Bitcoin 트랜잭션을 가능하게 합니다.



BLOCKSTREAM.info 탐색기에서 **"Liquid"** 버튼을 클릭하여 Liquid Network로 전환합니다.



![liquid](assets/fr/10.webp)



추적하고자 하는 트랜잭션 중 하나를 클릭하면 Bitcoin 조각의 금액이 "**기밀**"이라는 단어로 대체되는 것을 볼 수 있습니다. 이 네트워크에서는 거래가 기밀로 유지될 수 있으므로 거래의 안팎에서 각 UTXO의 금액은 확인할 수 없습니다.



![liquid_trx](assets/fr/11.webp)



그러나 Layer 프로토콜의 기본 Bitcoin에 존재하는 원칙과 메커니즘, 즉 Bitcoin 잠금 스크립트와 UTXO 추적성은 동일하다는 점에 유의하시기 바랍니다.



![liquid_details](assets/fr/12.webp)



Liquid Network은 조직에서 사용할 수 있는 비예치 디지털 자산도 제공합니다. "자산"** 메뉴에서 등록된 자산 목록과 총액, 해당 자산과 관련된 도메인을 확인할 수 있습니다.



![assets](assets/fr/13.webp)



각 자산에 대해 발행 및 소각 거래 내역을 추적할 수 있습니다(유통 중인 총량을 삭제).



![assets_trxs](assets/fr/14.webp)




## 추가 옵션



BLOCKSTREAM.info 탐색기에는 Testnet, Bitcoin, On-Chain 및 Liquid Network의 거래에 대한 시각화 및 추적 기능도 포함되어 있습니다.



![testnet](assets/fr/15.webp)



Testnet 네트워크로 이동하면 실제 비트코인을 사용하지는 않지만 위에서 설명한 모든 기능을 사용할 수 있습니다.



![liquid_testnet](assets/fr/16.webp)



이 네트워크에는 다양한 체인 길이가 있으며, 이를 통해 Bitcoin 및 Liquid 메커니즘의 작동을 연결하고 테스트할 수 있습니다.





- API 섹션은 특정 탐색기 기능을 자신의 애플리케이션에 통합하고자 하는 모든 사용자를 위한 섹션입니다. 예를 들어 이 API을 통해 여러 레이어(On-Chain 및 Liquid)의 메인 체인을 조사하고, 트랜잭션을 추적하고, BLOCK의 평균 거래 수수료를 확인할 수 있습니다.



![api](assets/fr/17.webp)



이제 BLOCKSTREAM 탐색기의 잠재력을 최대한 활용하여 On-Chain 및 Liquid 레이어에서 블록체인을 쿼리할 준비가 되셨습니다. 이 튜토리얼이 도움이 되셨기를 바라며, 다른 Bitcoin 탐색기에 대한 튜토리얼도 추천해 드립니다:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f