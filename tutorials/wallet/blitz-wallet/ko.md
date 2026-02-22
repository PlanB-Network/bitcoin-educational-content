---
name: Blitz Wallet
description: 가장 간단한 Bitcoin 지갑.
---

![cover](assets/cover.webp)

사용자 경험은 Bitcoin 지갑을 선택할 때 가장 중요한 요소 중 하나입니다. 이 튜토리얼에서는 단순함을 핵심에 둔 지갑인 Blitz Wallet을 소개합니다. **Spark** 프로토콜의 통합 덕분에 Blitz는 즉각적인 결제와 기술적 관리 없이도 시장에서 가장 간단하고 완전한 Bitcoin 지갑 중 하나를 제공합니다.

## Blitz Wallet이란?

Blitz Wallet은 사용자의 주권과 유연하고 직관적인 사용자 경험에 중점을 둔 **self-custodial** 및 **open source** Bitcoin 지갑입니다.

[Blitz Wallet](https://blitz-wallet.com/)은 Android(Play Store)와 iOS(App Store)에서 사용할 수 있는 모바일 애플리케이션입니다.

결제 채널과 인바운드 유동성을 관리해야 하는 기존 Lightning 지갑과 달리, Blitz Wallet은 **Spark 프로토콜**을 활용하여 이러한 기술적 복잡성을 제거합니다. 결과적으로, 첫 번째 satoshi를 받는 순간부터 사전 설정 없이 즉각적인 결제가 가능합니다. Blitz의 목표는 자금의 self-custody를 절대 포기하지 않으면서 일반 결제 앱처럼 간단하게 bitcoin 결제를 가능하게 하는 것입니다.

Blitz Wallet은 `사용자@도메인.com` 형식의 **읽기 쉬운 주소**(LNURL 기반)도 지원하므로, 매 거래마다 긴 invoice나 QR 코드를 다루지 않고도 이메일처럼 쉽게 bitcoin을 보낼 수 있습니다.

## Spark 프로토콜 이해하기

실습으로 넘어가기 전에, Blitz Wallet을 작동시키는 내부 기술인 **Spark 프로토콜**을 이해하는 것이 도움이 됩니다.

### Spark란?

Spark는 Lightspark 팀이 개발한 Bitcoin 위에 구축된 open source 레이어 프로토콜입니다. bitcoin의 self-custody를 유지하면서 즉각적이고 저렴한 거래를 가능하게 합니다.

두 당사자 간의 **결제 채널**에 의존하는 Lightning Network와 달리, Spark는 **statechain**(상태 체인)이라는 기술을 사용합니다. 기본 원리는 다음과 같습니다: 매 거래마다 블록체인에서 bitcoin을 이동하는 대신, Spark는 on-chain 이동 없이 한 사용자에서 다른 사용자로 **지출 권한**을 이전합니다.

### 어떻게 작동하나요?

Spark를 직관적으로 이해하기 위해, Spark에서 bitcoin을 지출하려면 두 조각의 퍼즐을 완성해야 한다고 상상해 봅시다:
- 한 조각은 사용자가 보유합니다(예: Alice).
- 다른 조각은 **Spark Entity (SE)**라는 운영자 그룹이 보유합니다.

해당하는 두 조각의 조합만이 bitcoin을 지출할 수 있게 합니다.

Alice가 Bob에게 bitcoin을 보내고 싶을 때 다음과 같은 일이 발생합니다: Bob과 SE 사이에 새로운 퍼즐이 공동으로 생성됩니다. 퍼즐은 같은 형태를 유지하지만, 구성하는 조각이 변경됩니다. 이제 Bob의 조각이 SE의 조각과 일치합니다. SE가 대응하는 조각을 파기했기 때문에 Alice의 이전 조각은 사용할 수 없게 됩니다. bitcoin의 소유권이 **블록체인상의 어떠한 거래도 없이** 이전되었습니다.

Bob은 이후 같은 과정을 반복하여 이 bitcoin을 Carol에게 보낼 수 있으며, 이런 식으로 계속됩니다. 각 이전은 on-chain 자금 이동이 아닌 퍼즐 조각의 교체로 작동합니다.

### 왜 안전한가요?

정당한 질문이 제기됩니다: SE가 실제로 이전 조각을 파기하지 않으면 어떻게 되나요?

Spark Entity는 단일 주체가 아니라 독립적인 운영자들의 그룹입니다. SE의 조각은 결코 단일 운영자가 보유하지 않습니다. 퍼즐의 교체에는 여러 운영자의 협력이 필요합니다. 이전 퍼즐의 재활성화를 방지하려면 이전 시 **단 한 명의 운영자만 정직**하면 됩니다. 어떤 개별 운영자도 비밀리에 이전 활성 퍼즐을 보존하거나 나중에 재생성할 수 없습니다.

또한, Spark는 일방적 출구 메커니즘을 포함합니다: SE의 협력 없이도 언제든지 on-chain으로 bitcoin을 회수할 수 있습니다. 이 백업 메커니즘은 Spark 아키텍처의 핵심 부분이며, 자금에 접근하기 위해 네트워크에 의존하지 않는다는 것을 보장합니다.

### Spark vs Lightning Network

Spark와 Lightning은 경쟁 관계가 아니라 **상호 보완적**입니다. Blitz Wallet은 둘 다 통합하여 각각의 장점을 활용할 수 있게 합니다.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **기술**                      | Statechains (상태 체인)       | 결제 채널              |
| **채널 관리**                  | 불필요                       | 필요                   |
| **인바운드 유동성**             | 불필요                       | 필요                   |
| **즉각 거래**                  | 예                           | 예                    |
| **Self-custody**              | 예                           | 예                    |
| **Lightning 호환성**           | 예 (atomic swaps 통해)       | 네이티브               |

Lightning Network는 즉각적인 결제를 위한 훌륭한 프로토콜이지만, 초보자에게 장벽이 될 수 있는 기술적 제약(채널 관리, 인바운드 유동성, 온라인 노드...)이 있습니다. Spark는 Lightning과의 호환성을 유지하면서 이러한 제약을 제거합니다.

## 설치 및 설정

이 튜토리얼에서는 Blitz Wallet의 Android 버전을 기준으로 설명하지만, 아래에 제시된 모든 과정은 iOS에서도 동일하게 적용됩니다.

![installation](assets/fr/01.webp)

Blitz Wallet은 self-custody 지갑이므로, **새 지갑 생성** 또는 기존 지갑의 **복구 문구 가져오기**(12개 또는 24개 단어) 중 선택할 수 있습니다.

여기서는 새 지갑 생성으로 진행합니다. 복구 문구 백업에 대한 권장 사항은 아래를 참조하세요:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **중요** : 이 12개 또는 24개의 복구 단어는 **bitcoin에 접근할 수 있는 유일한 키**입니다. Blitz는 self-custodial 지갑입니다: Blitz도 Spark도 복구 문구나 자금에 접근할 수 없습니다. 이 단어를 분실하면 bitcoin에 대한 접근을 영구적으로 잃게 됩니다. 누구와도 공유하지 마세요: 이 단어를 가진 사람은 누구든 bitcoin을 사용할 수 있습니다.

그런 다음 지갑 접근을 보호하기 위한 **PIN 코드**를 생성하세요.

![setup-wallet](assets/fr/02.webp)

## Blitz 시작하기

Blitz로 거래하는 것은 대부분의 다른 Bitcoin 지갑보다 직관적입니다. 인터페이스는 미니멀하며 세 가지 주요 작업에 집중합니다: 보내기, 스캔, 받기.

### Bitcoin 받기

Blitz 지갑에서 bitcoin을 받으려면 **"아래 화살표"** 아이콘(↓)을 클릭하고, 받고 싶은 satoshi 금액을 입력하고, 선택적 설명을 추가하면 지갑이 발신자에게 공유할 수 있는 인보이스(invoice)를 생성합니다.

⚠️ **참고** : satoshi(또는 "sat")는 bitcoin의 최소 단위입니다: **1 bitcoin = 100,000,000 satoshis**.

Blitz Wallet의 특징 중 하나는 Bitcoin 생태계의 여러 네트워크와 프로토콜을 지원한다는 점입니다:

- **Lightning Network** : 매우 낮은 수수료로 즉각적인 소액 결제를 가능하게 하는 Bitcoin의 레이어 중 하나입니다. 일상적인 소액 결제에 이상적입니다.

- **Bitcoin (on-chain)** : Bitcoin 프로토콜의 메인 블록체인으로, 최대 보안과 최종성이 우선시되는 대규모 거래에 적합합니다.

- **Liquid Network** : Blockstream이 개발한 Bitcoin의 sidechain(병렬 체인)으로, Liquid Bitcoin(L-BTC)을 사용하여 빠르고 기밀성 있는 거래를 가능하게 합니다.

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

기본적으로 Blitz는 Lightning 인보이스를 생성하지만, **"Choose format"**(형식 선택) 버튼을 클릭하여 satoshi를 받고 싶은 네트워크를 선택할 수 있습니다.

![receive-sats](assets/fr/03.webp)

### 연락처 만들기

Blitz Wallet은 연락처 시스템을 통해 반복적인 bitcoin 전송을 간소화합니다.

**Contacts** 메뉴에서 자주 거래하는 Blitz 사용자 이름이나 Lightning 주소(LNURL)를 등록할 수 있습니다.

이렇게 하면 매번 QR 코드를 스캔하거나 수동으로 주소를 입력하지 않고도 몇 번의 클릭만으로 이 주소들에 satoshi를 보낼 수 있습니다.

### Bitcoin 보내기

일반적인 bitcoin 전송 방법(QR 코드 스캔, 수동 주소 입력) 외에도 Blitz는 여러 편리한 옵션을 제공합니다:

- **이미지에서** (*From Image*) : 사진 갤러리에서 QR 코드를 가져옵니다.
- **클립보드에서** (*From Clipboard*) : 이전에 복사한 주소나 인보이스를 붙여넣습니다.
- **수동 입력** (*Manual Input*) : Bitcoin 주소, Lightning 인보이스 또는 읽기 쉬운 주소(예: `utilisateur@walletofsatoshi.com`)를 직접 입력합니다.
- **연락처에서** : 미리 등록된 수신자를 선택하여 몇 번의 클릭으로 전송합니다.

**Wallet** 메뉴에서 **"위 화살표"** 버튼(↑)을 클릭하고, 전송 방법을 선택하고, 보낼 금액을 입력하고, 설명을 추가하고 거래를 확인합니다.

전송 최소 금액은 현재 **1,000 satoshis**입니다.

![send-bitcoin](assets/fr/05.webp)

## Blitz 스토어

bitcoin 전송 작업 외에도 Blitz Wallet에는 앱에서 직접 디지털 서비스를 구매하는 데 bitcoin을 사용할 수 있는 스토어가 내장되어 있습니다.

메인 메뉴에서 **Store** 탭을 클릭하여 스토어에 접근하세요. 전 세계 수천 개의 상점에서 bitcoin으로 직접 기프트 카드를 구매할 수 있는 **Bitrefill** 플랫폼에 대한 접근도 제공됩니다.

- **인공지능** : 최신 생성형 AI 모델(Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5)에 접근하고 satoshi로 직접 크레딧을 결제하세요. 필요에 따라 여러 요금제가 제공됩니다(Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **익명 SMS** : 개인 전화번호를 공개하지 않고 전 세계 어디서나 SMS를 주고받을 수 있습니다. 발송된 각 메시지에 대해 satoshi로 요금이 부과됩니다.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard** : Blitz 스토어에서 bitcoin으로 직접 결제 가능한 WireGuard VPN 구독(주간, 월간 또는 분기별)을 통해 온라인 프라이버시를 보호하세요. 기기에 WireGuard 클라이언트 앱을 다운로드하기만 하면 이용할 수 있습니다.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet 내부 살펴보기: 더 깊이 알아보기

Blitz Wallet의 사용 편의성 뒤에는 Bitcoin 생태계의 여러 레이어를 결합한 잘 설계된 기술 아키텍처가 있습니다.

### 잔액 분배

Blitz Wallet은 필요에 따라 여러 프로토콜 간에 자금을 분배하여 잔액을 투명하게 관리합니다. 잔액이 500,000 satoshis 미만인 경우, Blitz는 **Liquid Network**와 atomic swaps를 사용하여 유연한 경험을 제공하고 소액으로도 Lightning Network에서 거래할 수 있게 합니다.

이 접근 방식은 새로운 사용자가 기본 메커니즘을 이해할 필요 없이 간단하게 시작할 수 있도록 보장합니다. **설정 > Balance Info** 메뉴에서 다양한 레이어 간 잔액 분배를 확인할 수 있습니다.

![balance](assets/fr/09.webp)

### Lightning 모드 (선택 사항)

기본적으로 Blitz Wallet은 Liquid Network와 Spark 프로토콜을 사용하여 기술적 설정 없이 유연한 경험을 제공합니다. 그러나 Blitz는 잔액이 **500,000 satoshis**(0.005 BTC)에 도달하면 자동으로 결제 채널을 여는 **Lightning 모드**를 활성화할 수 있는 옵션을 제공합니다.

Lightning 모드를 활성화하려면 **설정**으로 이동한 다음, **기술 설정** 섹션에서 **Node Info** 옵션을 클릭하세요.

![enable-lightning](assets/fr/10.webp)

Spark 프로토콜 덕분에 이 활성화는 **선택 사항**입니다: Spark는 이미 채널을 열거나 인바운드 유동성을 관리할 필요 없이 Lightning 호환 결제를 수행할 수 있습니다. 네이티브 Lightning 모드는 앱 내에 자체 Lightning 노드를 보유하고자 하는 고급 사용자에게 유용합니다.

### 판매 시점 (PoS)

Blitz Wallet은 상인들이 앱에서 직접 bitcoin 결제를 수락할 수 있는 **판매 시점** 기능을 포함합니다.

**설정 > Point-of-sale** 메뉴에서 다음을 구성할 수 있습니다:

- 매장의 고유 식별자
- 가격을 표시할 현지 법정 통화
- 직원을 위한 안내 사항
- 고객을 위한 팁 옵션

고객은 생성된 QR 코드를 스캔하기만 하면 bitcoin으로 즉각적으로 결제할 수 있습니다.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

이 튜토리얼 작성에 사용된 자료:
- [Breez](https://breez.technology/) Technology 블로그: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
