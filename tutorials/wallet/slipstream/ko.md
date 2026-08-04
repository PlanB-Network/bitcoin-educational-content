---
name: Slipstream
description: Bitcoin 네트워크에 브로드캐스트하지 않고, Slipstream으로 서명된 트랜잭션을 마이너에게 직접 보내기
---

![커버](assets/cover.webp)

일반적으로 트랜잭션에 서명하면 해당 트랜잭션은 네트워크의 모든 Bitcoin 노드에 자동으로 브로드캐스트됩니다. 그런 다음 채굴되기를 기다립니다.

하지만 트랜잭션이 블록에 포함되기 전까지는, 개인 키를 확보한 공격자가 이를 대체하여 자금을 훔칠 수 있습니다. 이는 일반적으로 ColdCard 하드웨어 지갑을 사용하는 경우에 해당합니다.

채굴 회사 MARA의 Slipstream 도구를 사용하면 트랜잭션을 네트워크에 브로드캐스트하는 과정을 우회할 수 있습니다. 트랜잭션은 마이너에게 직접(그리고 오직 마이너에게만) 전송되어 비공개로 유지되고 네트워크에 노출되지 않습니다. 트랜잭션이 채굴되기까지는 아마 더 오래 걸리겠지만, 대체 공격으로부터 보호됩니다.

아래에서는 [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) 사용자와 [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) 지갑 사용자가 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) 페이지를 통해 마이너 MARA의 Slipstream 도구를 사용하는 튜토리얼을 제공합니다.

⚠️ **경고**: 이 도구는 주로 Liana 지갑, Miniscript 지갑, 일부 유형의 멀티시그처럼 특정 프로필만을 위한 것입니다. Wizardsardine은 자금이 이미 치명적인 도난 위험에 놓인 지갑, 예를 들어 난수 생성기 취약점의 영향을 받는 ColdCard 기기에서 복구 문구가 생성된 지갑에는 이 도구 사용을 **명시적으로 권장하지 않습니다**. 이런 상황에서는 공격자와의 경주가 초 단위로 벌어지며, 단일 마이너에게 보낸 트랜잭션은 정상적으로 브로드캐스트된 트랜잭션보다 확인되는 데 훨씬 더 오래 걸립니다. 이에 해당한다면 먼저 전용 튜토리얼을 읽어보세요:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Liana 사용자의 경우

Liana는 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) 페이지의 게시자인 Wizardsardine이 관리하므로 경로가 직접적입니다. 트랜잭션을 브로드캐스트하는 대신 서명된 PSBT 파일을 내보내기만 하면 됩니다.

*전제 조건: Liana 지갑에 자금이 있어야 합니다.*

### 1단계: Liana로 트랜잭션 만들기

평소처럼 목적지 주소, 설명, 금액(여기서는 지갑에서 사용 가능한 최대 금액)을 추가하여 트랜잭션을 구성합니다.

수수료율을 설정하려면:

- 왼쪽 하단의 "Coins selection" 아래에 있는 작은 상자를 클릭하여 사용하려는 코인을 선택합니다;
- 그런 다음 수수료율을 입력합니다. 이 페이지에 설명된 것처럼 제안된 수수료율보다 훨씬 높은 수수료를 설정해야 한다는 점을 기억하세요: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

마지막으로 "Next"를 클릭합니다.

![Liana에서 트랜잭션 구성하기](assets/fr/01.webp)

### 2단계: 트랜잭션 세부 정보 확인하기

"Sign"을 클릭하기 전에 트랜잭션 세부 정보를 확인하세요. 특히:

- 보낼 금액;
- 트랜잭션 수수료에 할당된 satoshis의 수;
- 무엇보다도 자금을 보내는 주소("address poisoning" 공격을 피하기 위해 주소의 처음 5/6자, 마지막 5/6자, 그리고 주소 중간의 5/6자를 확인해야 한다는 점을 기억하세요).

![트랜잭션 세부 정보 확인하기](assets/fr/02.webp)

### 3단계: 서명 지갑 선택하기

다음으로, 트랜잭션에 서명하는 데 필요한 소프트웨어 및/또는 하드웨어 지갑을 선택합니다. 간단히 상기하자면, 2-of-2 멀티시그 지갑의 경우 2개 중 2개의 서명이 필요합니다.

### 4단계: 트랜잭션의 PSBT 파일 내보내기

이제 Bitcoin 트랜잭션이 적절한 키로 서명되었습니다. "Broadcast"를 클릭하지 마세요. 그렇지 않으면 트랜잭션이 전체 네트워크에 공유되며, ColdCard 하드웨어 지갑을 사용하는 경우 트랜잭션이 공개적으로 노출되어 자금이 위험에 처하게 됩니다.

이제 "Export"를 클릭한 다음 PSBT 파일을 컴퓨터에 로컬로 저장할 수 있습니다.

![Liana에서 PSBT 파일 내보내기](assets/fr/03.webp)

### 5단계: outofband.wizardsardine.com을 통해 마이너에게 트랜잭션 보내기

이제 마지막 단계입니다. 트랜잭션을 마이너에게 보내려면 PSBT 파일을 가져와 지정된 영역에 끌어다 놓기만 하면 됩니다.

![outofband.wizardsardine.com에 PSBT 파일 드롭하기](assets/fr/04.webp)

그러면 트랜잭션이 아래와 같이 표시됩니다.

![대기열의 트랜잭션](assets/fr/05.webp)

### 6단계: Slipstream을 통해 트랜잭션 보내기

마지막으로, 트랜잭션이 Slipstream을 통해 MARA로 전송되도록 "Send"를 클릭하기만 하면 됩니다.

![Slipstream을 통해 트랜잭션 보내기](assets/fr/06.webp)

몇 초 안에 트랜잭션은 "Sending"에서 "Accepted"로 바뀝니다:

![Slipstream에서 승인된 트랜잭션](assets/fr/07.webp)

이제 남은 것은 트랜잭션 식별자(TXID)를 복사한 다음 [mempool.space](https://mempool.space/)에 붙여넣어 채굴되는 과정을 지켜보는 것입니다:

![mempool.space에서 TXID 조회하기](assets/fr/08.webp)

참고: 마이너인 MARA가 블록을 채굴하고 그 안에 트랜잭션을 포함하기 전까지 트랜잭션은 "Transaction not found"로 표시됩니다. MARA는 Bitcoin 네트워크 해시레이트의 약 4.5%만 보유하고 있기 때문에 수십 분, 심지어 몇 시간이 걸릴 수 있습니다. 2026년 8월 4일 기준으로 이는 대략 3시간 45분마다 블록 하나가 채굴되는 것에 해당합니다.

## 다른 지갑 사용자의 경우

[Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04)를 사용하지 않지만 여전히 이 도구를 사용하고 싶다면, 여기 2-of-2 멀티시그 지갑을 사용하는 튜토리얼이 있습니다. 이를 위해 [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) 소프트웨어 지갑을 사용하겠습니다.

*전제 조건: Sparrow 지갑에 자금이 있어야 합니다.*

### 1단계: 트랜잭션 만들기

[Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)로 멀티시그 지갑에서 트랜잭션을 만듭니다. 이 페이지에 설명된 것처럼 제안된 수수료율보다 훨씬 높은 수수료를 설정해야 한다는 점을 기억하세요: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

트랜잭션을 만든 후 "Create Transaction"을 클릭합니다.

![Sparrow에서 트랜잭션 만들기](assets/fr/09.webp)

### 2단계: 트랜잭션 완료하기

트랜잭션을 완료하려면 이제 서명해야 합니다. 이렇게 하려면 "Finalize Transaction for Signing"을 클릭합니다.

![서명을 위해 트랜잭션 완료하기](assets/fr/10.webp)

### 3단계: 여러 키로 트랜잭션 서명하기

이제 트랜잭션에 서명할 차례입니다. 이렇게 하려면 사용하는 소프트웨어 또는 하드웨어 지갑으로 서명하기만 하면 됩니다.

![멀티시그 키로 트랜잭션 서명하기](assets/fr/11.webp)

### 4단계: 서명된 트랜잭션을 다운로드하고, 네트워크에 브로드캐스트하지 않기

이제 Bitcoin 트랜잭션은 2-of-2 멀티시그의 두 키 모두로 서명되었습니다. "Broadcast Transaction"을 클릭하지 마세요. 그렇지 않으면 트랜잭션이 전체 네트워크에 공유되며, ColdCard 하드웨어 지갑을 사용하는 경우 트랜잭션이 공개적으로 노출되어 자금이 위험에 처하게 됩니다.

![서명 완료, 준비되었지만 브로드캐스트되지 않은 트랜잭션](assets/fr/12.webp)

### 5단계: 서명된 트랜잭션 스크립트 표시 또는 PSBT 파일 다운로드하기

서명된 Bitcoin 트랜잭션을 표시하려면 이제 "View Final Transaction"을 클릭합니다. 그런 다음 서명된 Bitcoin 트랜잭션 스크립트를 복사할 수 있습니다:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![서명된 트랜잭션 스크립트 표시하기](assets/fr/13.webp)

트랜잭션 파일을 다운로드하려면 다음 중 하나를 선택할 수 있습니다:

- "File"을 클릭한 다음 "Save transaction…"을 클릭합니다;
- 또는 오른쪽 하단의 네트워크 연결 버튼(노란색 버튼)을 클릭한 다음 "Save Final Transaction"을 클릭합니다.

그러면 트랜잭션이 컴퓨터에 로컬로 저장됩니다.

![최종 트랜잭션을 로컬로 저장하기](assets/fr/14.webp)

### 6단계: outofband.wizardsardine.com을 통해 마이너에게 트랜잭션 보내기

이제 마지막 단계입니다. 트랜잭션을 마이너에게 보내려면 다음만 하면 됩니다:

- [outofband.wizardsardine.com](https://outofband.wizardsardine.com/)으로 이동합니다;
- 이전 단계에서 복사한 서명된 트랜잭션 스크립트를 붙여넣은 다음, 아래의 "ADD TO QUEUE"를 클릭합니다;

![도구에 트랜잭션 스크립트 붙여넣기](assets/fr/15.webp)

- 또는 파일을 가져와 지정된 영역에 끌어다 놓습니다.

![도구에 트랜잭션 파일 드롭하기](assets/fr/16.webp)

그러면 트랜잭션이 아래와 같이 표시됩니다.

![대기열의 트랜잭션](assets/fr/17.webp)

트랜잭션의 총 입력 satoshis 금액을 알 수 없다는 메시지가 표시되면(그 결과 수수료에 필요한 satoshis 수를 계산할 수 없다는 뜻입니다), 총 입력 satoshis 금액을 직접 입력하기만 하면 됩니다. 이를 찾으려면 Sparrow에서 트랜잭션 표시를 클릭하면 됩니다. 다이어그램 중앙에 있습니다:

![Sparrow에 표시된 총 입력 금액](assets/fr/18.webp)

그런 다음 이 금액(우리 예시에서는 15,904 sats)을 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) 도구에 입력합니다:

![총 입력 금액 직접 입력하기](assets/fr/19.webp)

마지막으로 수수료율이 올바른지 확인합니다.

### 7단계: Slipstream을 통해 트랜잭션 보내기

마지막으로, 트랜잭션이 Slipstream을 통해 MARA로 전송되도록 "Send"를 클릭하기만 하면 됩니다.

![Slipstream을 통해 트랜잭션 보내기](assets/fr/20.webp)

몇 초 안에 트랜잭션은 "Sending"에서 "Accepted"로 바뀝니다:

![Slipstream에서 승인된 트랜잭션](assets/fr/21.webp)

이제 남은 것은 트랜잭션 식별자(TXID)를 복사한 다음 [mempool.space](https://mempool.space/)에 붙여넣어 채굴되는 과정을 지켜보는 것입니다:

![mempool.space에서 TXID 조회하기](assets/fr/22.webp)

참고: 마이너인 MARA가 블록을 채굴하고 그 안에 트랜잭션을 포함하기 전까지 트랜잭션은 "Transaction not found"로 표시됩니다. MARA는 Bitcoin 네트워크 해시레이트의 약 4.5%만 보유하고 있기 때문에 수십 분, 심지어 몇 시간이 걸릴 수 있습니다. 2026년 8월 4일 기준으로 이는 대략 3시간 45분마다 블록 하나가 채굴되는 것에 해당합니다.
