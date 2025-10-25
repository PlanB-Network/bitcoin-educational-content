---
name: RGB CLI
description: RGB에서 스마트 컨트랙트를 생성하고 Exchange를 생성하려면 어떻게 해야 하나요?
---
![cover](assets/cover.webp)


이 튜토리얼에서는 LNP/BP 협회에서 만든 명령줄 도구 'RGB'를 사용하여 Contract을 작성하는 단계별 프로세스를 따르겠습니다. CLI을 설치 및 조작하고, Schema을 컴파일하고, Interface와 Interface Implementation를 임포트한 다음 RGB 에셋을 발행하는 방법을 보여드리는 것이 목표입니다. 또한 컴파일 및 상태 유효성 검사를 포함한 기본 로직도 살펴볼 것입니다. 이 튜토리얼이 끝나면 프로세스를 재현하고 자신만의 RGB 컨트랙트를 만들 수 있을 것입니다.


## RGB 프로토콜 알림


RGB은 Bitcoin 위에서 실행되는 프로토콜로, 기반이 되는 Blockchain에 과부하를 주지 않으면서 Smart contract 기능과 디지털 자산 관리를 에뮬레이트합니다. 예를 들어 이더리움에서와 같은 기존의 On-Chain 스마트 컨트랙트와 달리, RGB은 "*Client-side Validation*" 시스템에 의존합니다. 대부분의 데이터와 상태 기록은 관련된 참여자들에 의해서만 교환되고 저장되는 반면, Bitcoin은 *Tapret* 또는 *Opret* 같은 메커니즘을 통해 소규모 암호화 약정만 호스팅합니다. 따라서 RGB 프로토콜에서 Bitcoin Blockchain는 타임스탬프 서버와 Double-spending 보호 시스템으로만 사용됩니다.


RGB Contract는 진화적 상태 머신처럼 구조화되어 있습니다. 엄격하게 유형화되고 컴파일된 Schema에 따라 초기 상태(예: Supply, 티커 또는 기타 메타데이터를 설명)를 정의하는 Genesis로 시작합니다. 그런 다음 상태 전환과 필요한 경우 상태 확장을 적용하여 이 상태를 수정하거나 확장합니다. 대체 가능한 자산(RGB20)을 전송하든 고유 자산(RGB21)을 생성하든 각 작업에는 *일회용 씰*이 포함됩니다. 이는 Bitcoin UTXO를 off-chain 상태에 연결하고 이중 지출을 방지하는 동시에 기밀성과 확장성을 보장합니다.


RGB 프로토콜의 작동 방식에 대해 자세히 알아보려면 이 종합 교육 과정을 수강하는 것이 좋습니다:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

RGB의 내부 로직은 Rust 라이브러리를 기반으로 하며, 개발자는 *Client-side Validation* 부분을 관리하기 위해 프로젝트에 가져올 수 있습니다. 또한, LNP/BP 팀은 다른 언어에 대한 바인딩 작업을 진행 중이지만 아직 확정되지 않았습니다. 또한 비트파이넥스와 같은 다른 기관에서 자체 통합 스택을 개발하고 있지만, 이에 대해서는 다른 튜토리얼에서 다룰 예정입니다. 당분간은 상대적으로 다듬어지지 않은 상태이긴 하지만 'RGB' CLI이 공식 참조입니다.


## RGB CLI 도구의 설치 및 프레젠테이션


메인 명령은 간단히 'RGB'이라고 합니다. 이는 `git`과 유사하게 설계되었으며, 컨트랙트 조작, 호출, 자산 발행 등을 위한 일련의 하위 명령이 포함되어 있습니다. Bitcoin Wallet는 현재 통합되지 않았지만 곧 출시될 버전(0.11)에 포함될 예정입니다. 이 다음 버전에서는 사용자가 'RGB'에서 직접 (설명자를 통해) 지갑을 생성하고 관리할 수 있으며, PSBT 세대, 서명을 위한 외부 하드웨어(예: Hardware Wallet)와의 호환성, Sparrow와 같은 소프트웨어와의 상호운용성 등이 포함될 예정입니다. 이렇게 하면 전체 자산 발행 및 이전 시나리오가 간소화됩니다.


### 카고를 통한 설치


를 사용하여 Rust에 도구를 설치합니다:


```bash
cargo install rgb-contracts --all-features
```


(참고: 상자의 이름은 `RGB-contracts`이며, 설치된 명령의 이름은 `RGB`입니다. 이미 `RGB`라는 이름의 상자가 존재했다면 충돌이 있었을 수 있으므로 이름이 바뀐 것입니다.)


이 설치는 많은 종속성(예: 명령 구문 분석, Electrum 통합, 영지식 증명 관리 등)을 컴파일합니다.


설치가 완료되면 :


```bash
rgb
```


(인수 없이) `RGB`를 실행하면 `인터페이스`, `Schema`, `수입`, `수출`, `이슈`, `Invoice`, `전송` 등과 같은 사용 가능한 하위 명령어 목록이 표시됩니다. 로컬 스토리지 디렉터리(모든 로그, 회로도 및 구현이 저장된 Stash)를 변경하거나 네트워크(Testnet, Mainnet)를 선택하거나 Electrum 서버를 구성할 수 있습니다.


![RGB-CLI](assets/fr/01.webp)


### 컨트롤의 첫 번째 개요


다음 명령을 실행하면 기본적으로 `RGB20` Interface이 이미 통합되어 있는 것을 확인할 수 있습니다:


```bash
rgb interfaces
```


이 Interface이 통합되지 않은 경우 :


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


컴파일합니다:


```bash
cargo run
```


그런 다음 원하는 Interface을 가져옵니다:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


그러나 아직 Schema을 소프트웨어로 가져온 적이 없다고 들었습니다. Stash에도 Contract가 없습니다. 이를 확인하려면 다음 명령을 실행하세요:


```bash
rgb schemata
```


그런 다음 리포지토리를 복제하여 특정 도식을 검색할 수 있습니다:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


이 저장소에는 `src/` 디렉토리에 스키마("*비팽창형 자산*"의 경우 NIA, "*유니크 디지털 자산*"의 경우 UDA 등)를 정의하는 여러 Rust 파일(예: `nia.rs`)이 포함되어 있습니다. 그런 다음 컴파일하려면 :


```bash
cd rgb-schemata
cargo run
```


그러면 컴파일된 스키마에 해당하는 여러 개의 `.RGB` 및 `.rgba` 파일이 생성됩니다. 예를 들어, `NonInflatableAsset.RGB`이 있습니다.


### Schema 및 Interface Implementation 가져오기


이제 회로도를 `RGB`으로 임포트할 수 있습니다:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


이렇게 하면 로컬 Stash에 추가됩니다. 다음 명령을 실행하면 이제 Schema이 나타나는 것을 볼 수 있습니다:


```bash
rgb schemata
```


## Contract 생성(발급)


새 에셋을 만드는 방법에는 두 가지가 있습니다:




- Rust의 스크립트 또는 코드를 사용하여 Schema 필드(Global State, 소유 상태 등)를 채우고 '.RGB` 또는 '.rgba` 파일을 생성하여 Contract을 빌드합니다;
- 또는 token의 속성을 설명하는 YAML(또는 TOML) 파일과 함께 `issue` 하위 명령을 직접 사용하세요.


'예제' 폴더의 Rust에서 '계약 빌더'를 빌드하고, 'Global State'(자산 이름, 티커, Supply, 날짜 등)을 채우고, Owned State(UTXO이 할당된)을 정의한 다음 이 모든 것을 *Contract Consignment*로 컴파일하여 내보내기, 검증 및 Stash로 가져오는 방법을 설명하는 예시를 찾을 수 있습니다.


다른 방법은 YAML 파일을 수동으로 편집하여 `티커`, `이름`, `Supply` 등을 사용자 지정하는 것입니다. 파일 이름이 `RGB20-demo.yaml`이라고 가정합니다. 를 지정할 수 있습니다:




- spec`: 티커, 이름, 정밀도 ;
- '용어': 법적 고지를 위한 필드입니다;
- 발행된 공급량` : 발행된 token의 양입니다;
- '할당': Single-Use Seal(*Seal Definition*)과 잠금 해제된 수량을 표시합니다.


다음은 생성할 YAML 파일의 예입니다:


```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-CLI](assets/fr/05.webp)


그런 다음 명령을 실행하기만 하면 됩니다:


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


제 경우 고유 Schema 식별자(작은따옴표로 묶어야 함)는 `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k`이고 발급자를 넣지 않았습니다. 그래서 내 주문은 :


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Schema ID를 모르는 경우 다음 명령을 실행하세요:


```bash
rgb schemata
```


CLI는 새로운 Contract이 발급되어 Stash에 추가되었다고 응답합니다. 다음 명령을 입력하면 방금 발급된 Contract에 해당하는 Stash이 추가로 발급된 것을 확인할 수 있습니다:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


그런 다음 다음 명령은 글로벌 상태(이름, 티커, Supply...)와 소유 상태 목록, 즉 할당을 표시합니다(예: UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`에 정의된 1백만 `PBN`토큰).


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## 내보내기, 가져오기 및 유효성 검사


이 Contract를 다른 사용자와 공유하려면 Stash에서 :


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


MyContractPBN.RGB` 파일을 다른 사용자에게 전달할 수 있으며, 이 사용자는 명령 을 사용하여 자신의 Stash에 추가할 수 있습니다:


```bash
rgb import myContractPBN.rgb
```


가져올 때 간단한 *Contract Consignment*인 경우 "`Consignment RGB 가져오는 중`"이라는 메시지가 표시됩니다. 더 큰 *State Transition Consignment*인 경우 명령이 달라집니다(`RGB 수락`).


유효성을 보장하기 위해 로컬 유효성 검사 기능을 사용할 수도 있습니다. 예를 들어, :


```bash
rgb validate myContract.rgb
```


### Stash 사용, 확인 및 표시


다시 말해, Stash는 스키마, 인터페이스, 구현 및 컨트랙트(Genesis + 트랜지션)의 로컬 인벤토리입니다. "가져오기"를 실행할 때마다 Stash에 요소가 추가됩니다. 이 Stash는 명령으로 자세히 볼 수 있습니다:


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


이렇게 하면 전체 Stash에 대한 세부 정보가 있는 폴더가 generate이 됩니다.


## 전송 및 PSBT


전송을 수행하려면 로컬 Bitcoin Wallet을 조작하여 `Tapret` 또는 `Opret` 커밋을 관리해야 합니다.


### generate 및 Invoice


대부분의 경우, Contract의 참여자(예: Alice와 Bob) 간의 상호작용은 Invoice의 생성을 통해 이루어집니다. Alice가 Bob이 무언가를 실행하기를 원하면(token 전송, 재발행, DAO에서의 작업 등), Alice는 Bob에게 자신의 지시를 자세히 설명하는 Invoice를 생성합니다. 그래서 우리는 :




- Alice** (Invoice 발행자) ;
- Bob**(Invoice을 수신하고 실행하는 사람).


다른 생태계와 달리 RGB Invoice는 결제의 개념에만 국한되지 않습니다. Contract에 연결된 모든 요청(키 취소, 투표, NFT에 각인(*각인*) 생성 등)을 포함할 수 있습니다. 해당 작업은 Contract Interface에 설명되어 있습니다. 해당 작업은 Contract Interface에 설명되어 있습니다.


다음 명령은 RGB Invoice을 생성합니다:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


와 함께 :




- `$Contract`: Contract 식별자 (*ContractId*) ;
- `$Interface`: 사용할 Interface(예: `RGB20`) ;
- `$ACTION`: Interface에 지정된 작업의 이름(간단한 대체 가능한 token 전송의 경우 "전송"이 될 수 있음). Interface에서 이미 기본 작업을 제공하는 경우 여기에 다시 입력할 필요가 없습니다;
- `$STATE`: 전송할 상태 데이터(예: 대체 가능한 token가 전송되는 경우 토큰의 양);
- `$Seal`: 수혜자(Alice)의 Single-Use Seal, 즉 UTXO에 대한 명시적 참조. Bob는 이 정보를 사용하여 Witness Transaction을 빌드하고 해당 출력은 Alice에 속하게 됩니다(*blinded UTXO* 또는 암호화되지 않은 형태).


예를 들어 다음 명령을 사용합니다


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI는 generate과 같은 Invoice이 됩니다:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


모든 채널(텍스트, QR코드 등)을 통해 Bob으로 전송할 수 있습니다.


### 송금하기


이 Invoice에서 전송하려면 :




- Bob(Stash에 토큰을 보유한 사람)은 Bitcoin Wallet을 가지고 있습니다. 그는 필요한 RGB 토큰이 있는 UTXO를 사용하는 Bitcoin 트랜잭션(예: `tx.PSBT`)과 통화(Exchange)를 위한 UTXO을 준비해야 합니다;
- Bob은 다음 명령을 실행합니다:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- 이렇게 하면 `Consignment.RGB` 파일이 생성되며 이 파일에는 :
 - 토큰이 진짜임을 Alice에 증명하는 트랜잭션 기록입니다;
 - 토큰을 Alice의 Single-Use Seal로 전송하는 새로운 전환 ;
 - Witness Transaction(서명되지 않음).
- Bob는 이 `Consignment.RGB` 파일을 Alice로 전송합니다(이메일, 공유 서버 또는 RGB-RPC 프로토콜, Storm 등을 통해);
- Alice은 `Consignment.RGB`을 수신하여 자체 Stash에서 이를 수용합니다:


```bash
alice$ rgb accept consignment.rgb
```




- CLI는 전환의 유효성을 검사하여 Alice의 Stash에 추가합니다. 유효하지 않은 경우 자세한 오류 메시지와 함께 명령이 실패합니다. 그렇지 않으면 성공하고 샘플 트랜잭션이 아직 Bitcoin 네트워크에 브로드캐스트되지 않았다고 보고합니다(Bob은 Alice의 Green 표시를 기다리고 있음);
- 확인을 위해 `수락` 명령은 서명(*급여 명세서*)을 반환하며, Alice은 Bob에게 *Consignment*를 확인했음을 보여주기 위해 이 서명을 보낼 수 있습니다;
- 그런 다음 Bob는 자신의 Bitcoin 트랜잭션에 서명하고 게시(`--게시`)할 수 있습니다:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- 이 거래가 On-Chain로 확인되는 즉시 자산의 Ownership은 Alice로 이전된 것으로 간주됩니다. 거래의 Mining을 모니터링하는 Alice의 Wallet는 자신의 Stash에 새로운 Owned State이 나타나는 것을 확인합니다.


이제 RGB Contract을 발행하고 전송하는 방법을 알게 되었습니다. 이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 올려주시면 대단히 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


또한 RGB 호환 라이트닝 노드를 Exchange 토큰으로 거의 즉시 실행하는 방법을 설명하는 다른 튜토리얼을 추천합니다:


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea