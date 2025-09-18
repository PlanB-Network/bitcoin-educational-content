---
name: Ocean Mining

description: Ocean Mining 소개
---

![signup](assets/cover.webp)


**2024년 5월**


Ocean Mining는 다소 독특한 Mining pool입니다. 여기에서는 계정, 이메일 주소, 비밀번호가 필요하지 않습니다. Bitcoin과 마찬가지로 모든 것이 투명하고 익명으로 처리되며, 기여자는 네 가지 블록 템플릿 중에서 선택할 수 있습니다.


### 보상 시스템


Ocean의 보상 시스템은 TIDES, 즉 "투명한 확장 주식 지수"라고 불립니다. 이 시스템은 채굴자가 제공한 작업, 즉 "지분"을 기록합니다. 풀은 각 기여자에 대한 "지분"의 비율을 계산한 다음, 풀의 블록 템플릿에 이 비율의 Block reward의 수혜자로서 그들의 Bitcoin Address을 추가합니다.


블록 템플릿은 약 10초마다 업데이트되어 가장 수익성이 높은 신규 트랜잭션을 고려하고 필요한 경우 Block reward의 분포를 변경합니다.


![signup](assets/rem.webp)


풀이 새 블록을 채굴할 때 머신이 연결되어 있는지 여부는 중요하지 않습니다. 이미 제출된 작업은 풀이 발견한 다음 8개의 블록에 대해 보관됩니다.


새로운 블록이 채굴될 때마다 카운터를 0으로 초기화하는 대신 8개의 블록에 대한 작업을 유지한다는 것은 기여를 시작한 후 풀이 8개의 블록을 찾았을 때만 보상이 100%가 된다는 것을 의미합니다. 이는 또한 풀에 대한 기여를 중단하더라도 8블록에 대한 보상을 계속 받을 수 있다는 의미이기도 합니다.


이 메커니즘은 보상을 원활하게 하고 다음 블록을 찾을 가능성이 가장 높은 풀에 따라 정기적으로 풀을 전환하는 '풀 호핑'을 방지합니다.


### 인출


Ocean Mining의 운영을 통해 기여자들은 "깨끗한" 비트코인, 즉 Block reward에서 직접 발행한 비트코인을 회수할 수 있습니다.


대부분의 다른 풀과 달리 오션은 새로 채굴된 비트코인을 받지 않으며, 기여자의 주소가 블록 템플릿에 직접 통합됩니다.


현재로서는 클린 비트코인의 진정한 혜택을 받기 위한 최소 금액은 1,048,576 Sats입니다. 풀에서 채굴되는 각 블록에 대해 "지분"이 1,048,576 Sats 이상이어야 Block reward이 직접 지급할 수 있는 자격을 얻게 됩니다.

그렇지 않으면 총 보상이 이 금액을 초과할 때까지 Sats이 오션에 보관됩니다.


오션이 임시로 보관하는 모든 비트코인은 이 Address에 있습니다: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, 모든 것은 타임체인에서 확인 가능합니다.](https://Mempool.space/Address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)

BOLT12를 사용하여 라이트닝을 통해 Sats을 인출할 수도 있습니다. 설정 방법을 살펴보겠습니다.


### 수영장 요금


수수료는 선택한 블록 템플릿에 따라 0%에서 2%까지 다양합니다.


## 바다의 투명성


### 기여자 데이터


![signup](assets/1.webp)


모든 사용자 데이터를 포함하여 풀에 대한 모든 정보는 투명하게 공개됩니다. 이 점을 이해하기 위해 한 가지 예를 들어보겠습니다:


[오션 대시보드](https://ocean.xyz/dashboard)에서는 지난 6개월 동안의 Hashrate, 풀 참여자 수, 채굴된 총 비트코인 수 등 다양한 정보를 확인할 수 있습니다.


"기여자" 섹션을 중점적으로 살펴보겠습니다. 지난 3시간 동안의 평균 Hashrate과 함께 모든 기여자 목록과 나머지 풀 대비 **"공유"** 및 **"Hash"**의 비율을 확인할 수 있습니다.


**"공유 %"**는 마지막 8개 블록의 창에서 기여자가 제공한 작업의 비율을 나머지 풀과 비교하여 나타냅니다.


**"Hash %"**는 지난 3시간 동안 기여자가 제공한 평균 Hashrate이 나머지 풀에 비해 차지하는 비율입니다.


![signup](assets/2.webp)


"기여자"는 Bitcoin Address로 식별되는 것을 알 수 있습니다. 이 주소 중 하나를 클릭하면 자세한 내용을 확인할 수 있습니다.


첫 번째 사용자, 즉 Hashrate가 가장 높은 사용자 [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ)를 보면 이 사용자에 대한 모든 세부 정보를 확인할 수 있습니다: Hashrate, 채굴한 비트코인의 수, 어떤 블록으로 채굴했는지, 심지어 각 머신(ASIC)의 세부 정보까지 확인할 수 있습니다. 그러나 Bitcoin와 마찬가지로 익명으로 유지됩니다.


### 블록 템플릿


대시보드의 왼쪽 상단에는 '다음 블록'이 있습니다. 이 페이지에는 네 가지 블록 템플릿이 있습니다. Ocean에서는 각 기여자가 지원하고자 하는 블록 템플릿을 선택할 수 있습니다. 이는 여러분의 보상에 직접적인 영향을 미치지 않습니다. 풀에서 블록을 채굴할 때, 모든 기여자는 선택한 템플릿에 관계없이 보상을 받습니다. 이는 단순히 모든 사람이 자신에게 적합한 블록 템플릿에 "투표"할 수 있게 해줍니다.


![signup](assets/3.webp)


**핵심:** 수수료 2%, "거래 및 대부분의 스팸 포함" 페이지에 명시된 대로 필터가 없는 클래식 Bitcoin core 템플릿입니다


**코어+안티스팸:** 수수료 0%, Bitcoin core "거래 포함 및 스팸 제한"과 같은 특정 거래에 대한 필터가 있는 Ordinal "거래 포함 및 스팸 제한"


**OCEAN:** 수수료 0%, Bitcoin Knot "트랜잭션과 상당히 적은 데이터만 포함"


**데이터 무료:** 수수료 0%, Bitcoin 매듭 "임의의 데이터가 없는 거래만 포함"


### Bitcoin core과 Bitcoin 매듭의 차이점

Bitcoin core은 전 세계 Bitcoin 노드의 약 99%가 작동할 수 있도록 하는 소프트웨어입니다. Bitcoin는 프로토콜로, 여러 개의 브라우저가 존재하는 인터넷과 마찬가지로 동일한 타임체인에 여러 개의 다른 소프트웨어 프로그램이 공존할 수 있습니다. 그러나 호환성에 대한 우려와 타임체인에 지울 수 없는 흔적을 남길 수 있는 버그의 위험을 제한하기 위해 거의 모든 Bitcoin 개발자는 Bitcoin core에서 작업합니다. Bitcoin Knots는 Bitcoin core의 Fork으로, 코드의 대부분을 공유하여 버그의 위험을 크게 제한합니다. 이 Fork은 Hard Fork를 만들지 않고 Bitcoin core보다 더 제한적인 규칙을 적용하고 싶었던 Luke Dashjr에 의해 만들어졌습니다. 현재는 나카모토 컨센서스 덕분에 Bitcoin core과 Bitcoin Knots가 공존하고 있습니다.


## 워커 추가하기


워커를 추가하려면 먼저 블록 템플릿을 선택합니다. 이 선택에 따라 Miner(ASIC)에 입력할 풀 URL이 결정됩니다.



- CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- Core+antispam**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`


다음으로 사용자 필드에 소유하고 있는 Bitcoin Address을 입력합니다. 호환되는 Address 유형 목록은 다음과 같습니다:


- P2PKH** (오리지널 Address 타입. "1"로 시작)
- P2SH** (다중 서명 또는 P2SH-SegWit. "3"으로 시작)
- Bech32**(SegWit. "bc"로 시작)
- Bech32m**(Taproot. "bc"로 시작. Bech32보다 길다.)


채굴자가 여러 명인 경우, 모든 채굴자에 대해 동일한 Address를 입력하면 Hash 요금이 합산되어 하나의 Miner로 표시됩니다. 또한 각각에 고유한 이름을 추가하여 구분할 수도 있습니다. 이렇게 하려면 Bitcoin Address 뒤에 '.workername'을 추가하기만 하면 됩니다.


마지막으로 비밀번호 필드에 `x`를 입력합니다.


**예시:**

OCEAN** 템플릿을 선택한 경우 Bitcoin Address의 이름은 `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`이고, Miner의 이름을 "Brrrr"로 지정하려면 Miner의 Interface에 다음 정보를 입력해야 합니다:



- URL**: `stratum+tcp://mine.ocean.xyz:3334`
- USER**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- 비밀번호**: `x`


Mining를 시작한 지 몇 분 후, Address을 검색하여 Ocean 사이트에서 데이터를 확인할 수 있습니다.


### 대시보드 개요


- 보상 창**의 공유: 이 데이터는 풀에서 채굴한 마지막 8개 블록의 기간 동안 풀에 전송한 작업량인 공유 수를 나타냅니다.
- Windows**에서 예상 보상**: 이미 완료한 작업으로 얻을 수 있는 Sats의 추정치입니다. 거래 수수료는 고려하지 않고 네트워크에서 발행한 새로운 비트코인인 코인베이스만 고려합니다.
- 다음 블록 예상 수익**: 현재 블록을 채굴할 경우 얻을 수 있는 Sats의 추정치입니다. 이 값이 1,048,576 Sats보다 작으면 Sats을 Address으로 직접 받지 못한다는 점을 기억하세요. 수익이 이 임계값을 초과할 때까지 오션의 Address으로 전송됩니다.


아래에는 최대 6개월까지의 Hashrate 이력이 표시된 그래프가 있습니다.


![signup](assets/4.webp)


여기에는 60초부터 24시간까지 다양한 시간대별 평균 Hashrate와 풀에서 채굴한 블록 중 기여하고 보상을 받은 내역이 표시됩니다.


![signup](assets/5.webp)


CSV 다운로드** 버튼을 사용하여 이 기록의 CSV 파일을 내보낼 수 있습니다.


![signup](assets/6.webp)


다음 섹션에는 이 Address로 풀에 연결한 모든 채굴자의 목록이 있습니다. 물론 개별 Hashrate은 물론, 그들이 개별적으로 받은 Sats의 개수도 확인할 수 있습니다.


![signup](assets/7.webp)


Miner의 **닉네임**을 클릭하면 됩니다. 그러면 방금 본 모든 정보를 볼 수 있지만, 특히 해당 Miner에 대한 정보가 표시됩니다.


그리고 페이지 하단에는 Address에 대한 지급 내역, 채굴했지만 아직 지급되지 않은 Sats, 채굴한 총 Sats를 확인할 수 있는 몇 가지 추가 정보가 표시됩니다.


![signup](assets/8.webp)


여기에서 **최소 지급까지 예상 시간** 상자에 라이트닝이라고 표시된 것을 볼 수 있는데, 이는 BOLT12 오퍼를 설정했기 때문입니다.


### 라이트닝 인출 설정


아시다시피, Ocean은 투명성을 극대화하고 보관(사용자를 대신하여 Sats을 보관)을 최소화하는 것을 목표로 합니다.


그렇기 때문에 라이트닝 인출을 위해서는 **BOLT12 오퍼**를 사용해야 합니다. 이는 2024년에 등장하기 시작한 Lightning Network에서 결제하는 새로운 방법이며 여러 가지를 허용합니다:


- 재사용 가능한 결제 링크로 자동 결제가 가능하며, 라이트닝 Address과 달리 BOLT12는 비수탁형입니다.
- 또한 결제가 이루어졌다는 증거를 제공하는 결제 수단이지만, LNURL은 그렇지 않습니다.
- 매우 중요한 것은 Bitcoin 서명과 함께 사용하여 BTC Address와 BOLT12 오퍼의 소유자임을 증명할 수 있다는 점입니다.

현재(2024년 5월) 이 방법을 사용할 수 있는 솔루션은 거의 존재하지 않습니다. 이 예제에서는 코어 라이트닝이 포함된 Start9 서버를 사용합니다. 예를 들어 Phoenix Wallet과 같은 다른 도구에 BOLT12 오퍼가 통합되어 있는 경우에도 이 튜토리얼은 계속 적용됩니다. 유입되는 유동성이 있는 채널이 열려 있는지 확인하세요. 그렇지 않으면 결제가 작동하지 않습니다.


먼저 Ocean 사이트의 대시보드로 이동하여 BTC Address를 입력한 다음 **설정** 탭을 클릭합니다.


![signup](assets/9.webp)


여기에 **설명** 텍스트를 복사합니다:

'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`에 대한 OCEAN 지급액


이제 Start9 서버(또는 BOLT12 오퍼를 제공할 수 있는 Wallet)의 코어 라이트닝 Interface으로 이동합니다.


![signup](assets/10.webp)


받기**를 클릭합니다.


오퍼**에 체크한 다음 이전에 복사한 텍스트를 **설명** 필드에 붙여넣고 **금액** 필드는 비워둡니다.


![signup](assets/11.webp)


generate 혜택**을 클릭합니다.


![signup](assets/12.webp)


라이트닝 주소의 경우처럼 중앙 서버가 필요 없는 재사용 가능한 영구 결제 링크를 생성했습니다. 링크를 복사한 다음 Ocean 페이지로 돌아옵니다.


라이트닝 볼트12 오퍼** 필드에 결제 링크를 붙여넣고 **블록 높이** 필드는 기본값으로 놔둡니다. generate**을 클릭합니다.


![signup](assets/13.webp)


Ocean에서 계정 시스템을 사용하지 않고 이 결제 링크가 실제로 회원님의 것인지 확인하려면 사용 중인 Bitcoin Address에 해당하는 개인 키로 방금 생성된 메시지에 서명해야 합니다. 개인 키로 메시지에 서명하는 솔루션은 여러 가지가 있습니다. 이 튜토리얼에서는 블루월렛을 예로 들어 설명하지만, 방법은 모든 지갑에 동일합니다.


![signup](assets/14.webp)


개인 키가 BlueWallet에 있다고 가정하고(Hardware Wallet로도 동일하게 할 수 있습니다), 해당 Wallet을 클릭합니다.


![signup](assets/15.webp)


그런 다음 오른쪽 상단의 **...**를 클릭합니다.


![signup](assets/15bis.webp)


그리고 **메시지 서명/확인**.


![signup](assets/16.webp)


이 창에는 세 개의 필드가 있습니다: **Address**, **서명**, **메시지**.


Address** 필드에 Bitcoin Address를 입력합니다. 예제로 돌아가서 Address를 입력하면 `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`가 됩니다.


서명** 필드를 비워둡니다.

그리고 생성된 메시지를 오션 페이지의 **메시지** 필드에 붙여넣습니다: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`

서명**을 클릭합니다.


이렇게 하면 Address `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`의 소유자임을 증명하는 암호화 서명이 generate가 되며, 이 서명은 BOLT12 결제 링크에서 생성된 Ocean에서 제공하는 메시지 덕분에 고유합니다.


![signup](assets/17.webp)


서명을 복사하여 Ocean 페이지에 붙여넣은 다음 **확정**을 클릭합니다.


![signup](assets/18.webp)


확인 메시지가 표시될 것입니다.


![signup](assets/19.webp)


이제 **내 통계** 탭으로 이동합니다. 이전에 Start9에서 Core Lightning으로 생성한 BOLT12 결제 링크와 함께 추가 정보가 상단에 표시됩니다.


![signup](assets/20.webp)