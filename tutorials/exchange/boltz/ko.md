---
name: Boltz
description: 제어권을 유지하면서 다른 Bitcoin 레이어 간을 전환할 수 있습니다.
---


![cover](assets/cover.webp)



2009년 배포된 이후 Bitcoin의 P2P 전자 현금 시스템은 기하급수적으로 성장하여 오늘날 우리가 일상 생활에서 즉시 사용할 수 있는 시스템으로 거듭났으며, 특히 Lightning Network을 통해 더욱 발전했습니다.



하지만 Bitcoin 프로토콜 계층 사이에는 유동적인 상호운용성이라는 큰 문제가 남아있었습니다. Bitcoin의 잠재력을 최대한 활용하기 위해서는 프로토콜의 여러 계층 간에 거래를 가능하게 하는 솔루션을 찾는 것이 필수적이었습니다. 이러한 필요성에 따라 2019년에 여러 Bitcoin 레이어를 연결하는 다리인 Boltz가 탄생했습니다.



## 볼츠는 무엇인가요?



[볼츠](https://boltz.Exchange)는 Bitcoin 프로토콜의 여러 계층 간에 거래하고자 하는 모든 사용자에게 이상적인 비수탁 플랫폼입니다:




- on chain**: 평균 10분마다 거래가 확인되는 Bitcoin의 메인 체인에서는 거래 수수료가 높은 경우가 많아 사용자의 요구를 반드시 충족시키지 못합니다;
- Lightning Network**: 저렴한 수수료로 즉시 결제가 가능한 Bitcoin 오버레이로, 일일 결제에 Bitcoin를 사용할 수 있습니다;
- Liquid Network**: 블록스트림에서 만든 Bitcoin용 오버레이로, 빠른 Confidential Transactions 및 기타 Bitcoin 기반 금융상품을 사용할 수 있습니다;
- 루트스톡**: Bitcoin 프로토콜을 기반으로 스마트 컨트랙트를 개발하기 위한 솔루션입니다.



![layers](assets/fr/01.webp)



이러한 서로 다른 계층 간의 상호 운용성은 사용자가 Bitcoin 에코시스템이 제공하는 모든 것을 최대한 활용하는 데 필요한 유연성을 제공하기 때문에 매우 중요합니다.



볼츠는 아토믹 스왑을 사용합니다. 이 기술을 사용하면 신뢰가 필요 없고 중개자 없이도 두 당사자 간에 직접 두 개의 레이어(예: Exchange의 BTC 온체인과 라이트닝의 BTC) 간에 비트코인을 교환할 수 있습니다. 이러한 거래소는 두 가지 결과만 생성할 수 있기 때문에 "아토믹"이라고 불립니다:




- Exchange이 성공하고 두 참가자가 BTC를 효과적으로 교환했거나 ;
- Exchange이 실패하거나 두 참가자 모두 원래 BTC를 가지고 떠납니다.



이러한 방식으로 사용자는 비트코인을 영구적으로 자기 소유로 유지하며, Exchange은 거래 상대방에 대한 신뢰를 기반으로 하지 않기 때문에 Exchange이 성공하거나 실패하더라도 어느 쪽도 상대방의 자금을 훔칠 수 없습니다.



아토믹 Exchange은 스마트 컨트랙트 [HTLC](https://planb.network/resources/glossary/htlc)(*해시된 타임락 Contract*)와 함께 작동합니다. 이 유형의 Contract에서는 양방향 채널에 금액이 "잠기고" 시간 제한이 도입되어 특정 시간 내에 거래가 완료되지 않으면 잔액이 입금자에게 반환됩니다. 이것이 바로 볼츠 플랫폼에서 사용하는 메커니즘입니다.



## 볼츠와의 첫 교류



볼츠는 개인 정보를 요구하지 않는 비예금형 웹 플랫폼입니다. 볼츠는 1분 이내에 거래를 시작할 수 있는 미니멀하고 유동적인 Interface를 제공합니다.



![boltz](assets/fr/02.webp)



플랫폼에 들어가면 Bitcoin 생태계의 여러 계층 간에 원자 교환을 생성할 수 있습니다.



![home](assets/fr/03.webp)



볼츠를 통해 거래할 수 있는 최소 및 최대 사토시(Bitcoin의 최소 단위)와 네트워크 수수료, 0.1%에서 0.5% 사이의 볼츠가 부과하는 비율을 확인할 수 있습니다.



![fees](assets/fr/04.webp)



그런 다음 원자 Exchange를 만들고자 하는 Layer을 선택하고 비트코인을 받고자 하는 Layer을 선택합니다.



![couches](assets/fr/05.webp)



이 튜토리얼에서는 기본 Layer에서 Lightning Network까지의 원자 Exchange에 초점을 맞출 것입니다.



옵션 중에서 선택하여 거래소의 기본 유닛을 구성할 수 있습니다:




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



기본 구성을 완료했으면 원자 Exchange의 양을 입력한 다음 같은 양의 Lightning Invoice를 생성하거나 간단히 LNURL을 입력합니다.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



안전을 위해 원자 Exchange의 매개변수를 확인하여 Exchange에 연결된 백업 키를 내보내세요.



설정** 아이콘에서 백업 키를 다운로드하고 파일을 적절히 저장합니다.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



이 파일에는 원자 거래소와 관련된 포트폴리오의 12가지 키워드가 포함되어 있습니다.



그런 다음 **원자 Exchange 생성** 버튼을 클릭하고 표시된 금액의 결제를 진행합니다.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

결제가 완료되고 확인되면 해당 금액이 자동으로 Lightning Wallet로 전송됩니다.



환불** 메뉴에서 원자 Exchange 내역을 찾아 환불을 받고자 하는 Exchange을 확인합니다. 예를 들어, 다른 기기에서 교환한 내역은 해당 교환과 연결된 백업 키 파일을 사용하여 가져올 수도 있습니다.



![refund](assets/fr/11.webp)



히스토리** 메뉴에서 **백업** 버튼을 클릭하면 구조 키와 연결된 거래 내역에 대한 자세한 내역을 다운로드할 수 있습니다.



![backup](assets/fr/12.webp)



⚠️ 이 파일에는 거래와 관련된 모든 정보와 이러한 거래에 연결된 백업 키가 포함되어 있으므로 이 파일도 공개하지 마세요.



볼츠는 토르 네트워크의 '.onion' 링크를 통해 액세스하기 때문에 높은 수준의 기밀성을 제공합니다. 브라우저에서 토르 브라우징을 활성화한 후 **양파** 메뉴를 선택하면 원자 교환을 완전히 익명으로 처리할 수 있습니다.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

이제 Exchange 에코시스템의 여러 계층 간에 상호 운용성을 지원하는 고유한 Bitcoin 플랫폼인 Boltz에 대해 잘 알고 계실 것입니다.