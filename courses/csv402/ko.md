---
name: RGB 프로그래밍
goal: RGB을 이해하고 사용하는 데 필요한 기술을 습득하세요
objectives:
- RGB 프로토콜의 기본 개념 이해하기
- Client-side Validation 및 Bitcoin 약속의 원칙 마스터하기
- RGB 계약 생성, 관리 및 이전 방법 알아보기
- RGB 호환 라이트닝 노드 작동 방법
---
# RGB 프로토콜 알아보기


Bitcoin Blockchain의 합의 규칙과 운영을 기반으로 계약과 자산의 형태로 디지털 권리를 구현하고 집행하도록 설계된 프로토콜인 RGB의 세계로 들어가 보세요. 이 종합 교육 과정에서는 'Client-side Validation'과 '일회용 씰'의 개념부터 고급 스마트 계약의 구현에 이르기까지 RGB의 기술적, 실용적 토대를 안내합니다.


체계적인 단계별 프로그램을 통해 Client-side Validation의 메커니즘, Bitcoin의 결정론적 약정, 사용자 간의 상호 작용 패턴에 대해 알아볼 수 있습니다. Bitcoin 또는 Lightning Network에서 RGB 토큰을 생성, 관리 및 전송하는 방법을 알아보세요.


개발자, Bitcoin 애호가 또는 단순히 이 기술에 대해 더 자세히 알고 싶은 분이라면 이 교육 과정을 통해 RGB을 마스터하고 Bitcoin에서 혁신적인 솔루션을 구축하는 데 필요한 도구와 지식을 얻을 수 있습니다.


이 과정은 풀구르벤처스가 주최하는 라이브 세미나를 기반으로 하며, 세 명의 저명한 강사와 RGB 전문가가 강의합니다.


+++
# 소개


<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>


## 코스 프레젠테이션


<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>


안녕하세요, Bitcoin 및 Lightning Network에서 실행되는 클라이언트 측 검증 Smart contract 시스템인 RGB 전용 교육 과정에 오신 것을 환영합니다. 이 과정의 구조는 이 복잡한 주제를 심도 있게 탐구할 수 있도록 설계되었습니다. 교육 과정의 구성은 다음과 같습니다:


**섹션 1: 이론**


첫 번째 섹션에서는 Client-side Validation과 RGB의 기본을 이해하는 데 필요한 이론적 개념을 다룹니다. 이 강좌를 통해 알게 되겠지만, RGB에서는 Bitcoin에서는 일반적으로 볼 수 없었던 다양한 기술 개념을 소개합니다. 이 섹션에서는 RGB 프로토콜과 관련된 모든 용어에 대한 정의를 제공하는 용어집도 찾을 수 있습니다.


**섹션 2: 연습**


두 번째 섹션에서는 섹션 1에서 살펴본 이론적 개념의 적용에 초점을 맞출 것입니다. RGB 컨트랙트를 생성하고 조작하는 방법을 배워보겠습니다. 또한 이러한 도구로 프로그래밍하는 방법도 살펴볼 것입니다. 이 첫 두 섹션은 Maxim Orlovsky가 진행합니다.


**섹션 3: 애플리케이션**


마지막 섹션에서는 다른 연사들이 구체적인 RGB 기반 애플리케이션을 소개하며 실제 사용 사례를 강조합니다.


---
이 교육 과정은 원래 [풀구르벤처스](https://fulgur.ventures/)가 토스카나 비아레조에서 주최한 2주간의 고급 개발 부트캠프에서 시작되었습니다. Rust과 SDK에 초점을 맞춘 첫 주는 이 다른 강좌에서 확인할 수 있습니다:


https://planb.network/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58

이 과정에서는 부트캠프의 두 번째 주에 집중하여 RGB를 집중적으로 다룹니다.


**1주차 - LNP402:**


![RGB-Bitcoin](assets/en/001.webp)


**2주차 - 현재 교육 CSV402:**


![RGB-Bitcoin](assets/en/002.webp)


이 라이브 강좌의 주최자와 참여해주신 세 분의 선생님께 감사드립니다:




- 막심 오를로프스키: *전 테네브라 센텐시아 사피엔스 도미니나비투르 아스트리스. 사이퍼, 인공지능, 로봇공학, 트랜스휴머니즘. RGB, 프라임, 래디언트 및 lnp_bp, mycitadel_io 및 cyphernet_io*의 창시자;
- 헌터 트루질로: *개발자, Rust, Bitcoin, 라이트닝, RGB*;
- 페데리코 텐가: *저는 세상을 Cypherpunk 디스토피아로 바꾸기 위해 노력하고 있습니다. 현재 비트파이넥스*에서 RGB를 개발 중입니다.


이 교육 과정의 서면 버전은 두 가지 주요 리소스를 사용하여 초안을 작성했습니다:




- 라이트닝 부트캠프에서 진행된 Maxim Orlovsky, Hunter Trujilo, Frederico Tenga의 세미나 동영상입니다;
- RGB 문서는 [비트파이넥스](https://www.bitfinex.com/)의 후원을 받아 제작되었습니다.


복잡하고 매혹적인 RGB의 세계로 뛰어들 준비가 되셨나요? 시작하세요!


# 이론상 RGB


<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>


## 분산 컴퓨팅 개념 소개


<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>


:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::


RGB는 Bitcoin Blockchain의 합의 규칙과 운영을 기반으로 디지털 권리(계약과 자산의 형태)를 확장 가능하고 비밀스러운 방식으로 적용하고 집행하기 위해 고안된 프로토콜입니다. 이 첫 장의 목적은 RGB 프로토콜에 대한 기본 개념과 용어를 제시하는 것이며, 특히 Client-side Validation 및 일회용 씰과 같은 기본 분산 컴퓨팅 개념과의 밀접한 연관성을 강조하는 것입니다.


이 장에서는 **분산 합의 시스템**의 기초를 살펴보고, RGB가 이 기술 계열에 어떻게 부합하는지 살펴봅니다. 또한 RGB가 Bitcoin의 자체 합의 메커니즘으로부터 독립적이고 확장 가능한 것을 목표로 하면서도 필요한 경우 이를 의존하는 이유를 이해하는 데 도움이 되는 주요 원칙을 소개합니다.


### 소개


컴퓨터 과학의 특정 분야인 분산 컴퓨팅은 노드 네트워크에서 정보를 유통하고 처리하는 데 사용되는 프로토콜을 연구합니다. 이러한 노드와 프로토콜 규칙이 함께 분산 시스템으로 알려진 것을 구성합니다. 이러한 시스템을 특징짓는 필수 속성 중에는 다음과 같은 것들이 있습니다:




- 각 노드가 특정 데이터를 독립적으로 검증하고 유효성을 검사**할 수 있는** 기능입니다;
- 노드가 (프로토콜에 따라) 정보의 전체 또는 부분 보기를 구성할 수 있는 가능성. 이러한 뷰는 분산 시스템의 **상태**입니다;
- 데이터에 안정적으로 타임스탬프가 찍히고 이벤트 순서(상태 순서)에 대한 합의가 이루어질 수 있도록 작업의 **시차적 순서**를 지정합니다.


특히 분산 시스템에서의 **합의**라는 개념은 두 가지 측면을 포괄합니다:




- **상태 변경의 유효성** 인정(프로토콜 규칙에 따라);
- 이러한 상태 변경의 **순서에 대한 합의**로 인해 검증된 연산을 사후에 다시 쓰거나 되돌릴 수 없습니다(Bitcoin에서는 이를 "이중 지출 보호"라고도 합니다).


분산 합의 메커니즘의 첫 번째 기능적, 허가 없는 구현은 Blockchain 데이터 구조와 Proof-of-Work(작업 증명) 알고리즘의 결합 덕분에 Satoshi 나카모토가 Bitcoin과 함께 도입했습니다. 이 시스템에서 블록 기록의 신뢰성은 노드(채굴자)의 컴퓨팅 파워에 따라 달라집니다. 따라서 Bitcoin은 모두에게 개방된(*퍼미션리스*) 분산 합의 시스템의 주요하고 역사적인 예시입니다.


Blockchain과 분산 컴퓨팅의 세계에서는 두 가지 기본 패러다임을 구분할 수 있습니다: *전통적인 의미의 **Blockchain***과 ***스테이트 채널***, 그 중 가장 좋은 예는 Lightning Network입니다. Blockchain은 시간순으로 정렬된 이벤트의 레지스터로 정의되며, 허가가 필요 없는 개방형 네트워크 내에서 합의를 통해 복제됩니다. 반면 상태 채널은 피어 투 피어 채널로, 두 명 이상의 참여자가 채널을 열고 닫을 때만 Blockchain을 사용하여 업데이트된 상태 off-chain를 유지할 수 있습니다.


Bitcoin의 맥락에서 여러분은 Mining의 원칙, 탈중앙화 및 거래의 최종성, 그리고 결제 채널의 작동 방식에 대해 잘 알고 계실 것입니다. RGB에서는 **Client-side Validation**이라는 새로운 패러다임이 도입되는데, 이는 Blockchain이나 라이트닝과 달리 Smart contract의 상태 전환을 로컬(클라이언트 측)에 저장하고 검증하는 방식으로 구성됩니다. 이는 다른 "디파이" 기술(_rollups_, _plasma_, _ARK_ 등)과도 다른데, Client-side Validation은 Blockchain에 의존하여 Double-spending를 방지하고 타임스탬프 시스템을 갖추면서 off-chain 상태 및 전환의 등록을 관련 참여자에게만 유지합니다.


![RGB-Bitcoin](assets/en/003.webp)


나중에 중요한 용어인 "**Stash**"라는 개념도 소개할 텐데요, 이 데이터는 네트워크를 통해 전 세계적으로 복제되지 않기 때문에 Contract의 상태를 보존하는 데 필요한 클라이언트 측 데이터 집합을 가리킵니다. 마지막으로 Client-side Validation을 활용하는 프로토콜인 RGB의 이론적 근거와 기존 접근 방식(Blockchain 및 상태 채널)을 보완하는 이유에 대해 살펴봅니다.


### 분산 컴퓨팅의 트릴레마


Client-side Validation과 RGB가 해결하지 못한 Blockchain과 Lightning의 문제를 이해하기 위해 분산 컴퓨팅의 3가지 주요 '트릴레마'를 살펴봅시다:




- 확장성, 탈중앙화, **프라이버시**;
- **CAP** 정리(일관성, 가용성, 파티션 허용 오차);
- **CIA** 트릴레마(기밀성, 무결성, 가용성).


#### 1. 확장성, 탈중앙화 및 기밀성




- **Blockchain(Bitcoin)**


Blockchain은 고도로 탈중앙화되어 있지만 확장성이 뛰어나지는 않습니다. 또한 모든 것이 글로벌 공개 레지스터에 저장되기 때문에 기밀성이 제한됩니다. 영지식 기술(Confidential Transactions, 밈블윔블 방식 등)로 기밀성을 개선할 수는 있지만, 퍼블릭 체인은 트랜잭션 그래프를 숨길 수 없습니다.




- **라이트닝/스테이트 채널**


스테이트 채널(Lightning Network와 마찬가지로)은 Blockchain보다 확장성이 뛰어나며, 트랜잭션이 off-chain에서 이루어지기 때문에 더 비공개적입니다. 그러나 특정 Elements(자금 거래, 네트워크 토폴로지)을 공개적으로 발표해야 하는 의무와 네트워크 트래픽 모니터링으로 인해 기밀성이 부분적으로 손상될 수 있습니다. 라우팅은 현금 집약적이며, 주요 노드가 중앙 집중화 지점이 될 수 있기 때문에 탈중앙화에도 문제가 있습니다. 이러한 현상이 바로 라이트닝에서 나타나기 시작한 현상입니다.




- **Client-side Validation(RGB)**


이 새로운 패러다임은 영지식 증명 기술을 통합할 수 있을 뿐만 아니라 아무도 전체 레지스터를 보유하지 않기 때문에 글로벌 트랜잭션 그래프가 없기 때문에 훨씬 더 확장 가능하고 기밀성이 높습니다. 다른 한편으로, 이는 탈중앙화에 대한 특정 타협을 의미하기도 합니다. Smart contract의 발행자는 이더리움의 "Contract 배포자"와 같은 중앙 역할을 할 수 있습니다. 그러나 Blockchain와 달리 Client-side Validation을 사용하면 관심 있는 컨트랙트만 저장하고 검증할 수 있으므로 기존의 모든 상태를 다운로드하고 검증할 필요가 없어 확장성이 향상됩니다.


![RGB-Bitcoin](assets/en/004.webp)


#### 2. CAP 정리(일관성, 가용성, 파티션 허용 오차)


CAP 정리는 분산 시스템이 *정합성*, *가용성*, *파티션 허용 오차*를 동시에 만족하는 것은 불가능하다는 점을 강조합니다.




- **Blockchain**


Blockchain는 일관성과 가용성에 유리하지만 네트워크 파티셔닝에는 적합하지 않습니다. 블록을 볼 수 없으면 전체 네트워크와 동일한 뷰를 갖고 행동할 수 없기 때문입니다.




- **Lightning**


상태 채널 시스템에는 가용성 및 파티셔닝 허용 오차(네트워크가 조각난 경우에도 두 노드가 서로 연결된 상태를 유지할 수 있으므로)가 있지만 전반적인 일관성은 Blockchain의 채널 열기 및 닫기에 따라 달라집니다.




- **Client-side Validation(RGB)**


RGB와 같은 시스템은 일관성(각 참가자가 모호함 없이 로컬에서 데이터를 검증)과 파티셔닝 허용 범위(데이터를 자율적으로 보관)를 제공하지만, 글로벌 가용성을 보장하지는 않습니다(모든 참가자가 관련 기록을 가지고 있는지 확인해야 하며 일부 참가자는 아무것도 게시하지 않거나 특정 정보 공유를 중단할 수 있습니다).


![RGB-Bitcoin](assets/en/005.webp)


#### 3. CIA 트릴레마(기밀성, 무결성, 가용성)


이 트릴레마는 기밀성, 무결성, 가용성을 동시에 최적화할 수 없다는 사실을 상기시켜 줍니다. Blockchain, Lightning, Client-side Validation은 이 균형에 따라 다르게 적용됩니다. 단일 시스템이 모든 것을 제공할 수는 없으며, 여러 가지 접근 방식(Blockchain의 타임스탬프, Lightning의 동기식 접근 방식, RGB의 로컬 검증)을 결합하여 각 측면에서 우수한 보증을 제공하는 일관된 패키지를 확보해야 한다는 것입니다.


![RGB-Bitcoin](assets/en/006.webp)


### Blockchain의 역할과 샤딩의 개념


Blockchain(이 경우 Bitcoin)은 주로 _타임 스탬핑_ 메커니즘과 이중 지출에 대한 보호 역할을 합니다. Smart contract 또는 탈중앙화 시스템의 전체 데이터를 삽입하는 대신 트랜잭션에 **암호화 약정**을 포함하기만 하면 됩니다(Client-side Validation의 의미에서 "상태 전환"이라고 부를 것입니다). 따라서




- Blockchain은 대량의 데이터와 로직으로부터 자유로워집니다;
- 각 사용자는 Global State를 복제하는 대신 Contract(자신의 "*Shard*")의 자신의 부분에 필요한 기록만 저장합니다.


샤딩은 분산 데이터베이스(예: 페이스북이나 트위터와 같은 소셜 네트워크용 MySQL)에서 유래한 개념입니다. 데이터 용량과 동기화 지연 문제를 해결하기 위해 데이터베이스를 _샤드_(미국, 유럽, 아시아 등)로 분할합니다. 각 세그먼트는 로컬에서 일관성을 유지하며 다른 세그먼트와 부분적으로만 동기화됩니다.


RGB 유형의 스마트 컨트랙트의 경우, 계약 자체에 따라 Shard을 사용합니다. 각 Contract는 독립적인 _샤드_입니다. 예를 들어, USDT 토큰만 보유하고 있다면 USDC와 같은 다른 token의 전체 이력을 저장하거나 검증할 필요가 없습니다. Bitcoin에서는 Blockchain이 _샤딩_을 하지 않습니다: 글로벌 UTXO 세트가 있습니다. Client-side Validation를 사용하면 각 참가자는 자신이 보유하거나 사용하는 Contract 데이터만 유지합니다.


따라서 다음과 같은 생태계를 상상할 수 있습니다:




- 최소 레지스터의 완전한 복제를 보장하고 타임스탬핑 Layer의 역할을 하는 기초로서 **Blockchain(Bitcoin)**를 사용합니다;
- 빠른 **Lightning Network**은 Confidential Transactions의 보안 및 최종 결제를 기반으로 하며, Bitcoin Blockchain는 여전히 보안 및 최종 결제를 기반으로 합니다;
- Blockchain을 복잡하게 만들거나 기밀성을 잃지 않으면서도 더 복잡한 Smart contract 로직을 추가할 수 있도록 RGB 및 **Client-side Validation**을 지원합니다.


![RGB-Bitcoin](assets/en/007.webp)


이 세 개의 Elements는 "Layer 2", "Layer 3" 등의 선형 스택이 아닌 삼각형 전체를 형성합니다. 라이트닝은 Bitcoin에 직접 연결하거나 RGB 데이터를 통합하는 Bitcoin 트랜잭션과 연결될 수 있습니다. 마찬가지로 "BiFi"(Bitcoin의 금융)는 기밀성, 확장성 또는 Contract 로직에 대한 필요에 따라 Blockchain, Lightning 및 RGB와 함께 구성할 수 있습니다.


![RGB-Bitcoin](assets/en/008.webp)


### 상태 전환의 개념


모든 분산 시스템에서 검증 메커니즘의 목표는 **상태 변경의 유효성과 시간 순서를 결정**할 수 있도록 하는 것입니다. 프로토콜 규칙이 준수되었는지 확인하고, 이러한 상태 변경이 확정적이고 공격할 수 없는 순서로 서로 뒤따른다는 것을 증명하는 것이 목표입니다.


이 검증이 **Bitcoin**의 맥락에서 어떻게 작동하는지 이해하고, 보다 일반적으로 Client-side Validation의 철학을 파악하기 위해 먼저 Bitcoin Blockchain의 메커니즘을 살펴본 다음, Client-side Validation이 이들과 어떻게 다르고 어떤 최적화를 가능하게 하는지를 살펴보겠습니다.


![RGB-Bitcoin](assets/en/009.webp)


Bitcoin Blockchain의 경우 트랜잭션 유효성 검사는 간단한 규칙을 기반으로 합니다:




- 모든 네트워크 노드는 모든 블록과 트랜잭션을 다운로드합니다;
- 이러한 트랜잭션의 유효성을 검사하여 UTXO 세트(모든 미사용 출력)의 올바른 진화를 확인합니다;
- 이 데이터를 블록 형태로 저장하여 필요한 경우 기록을 재생할 수 있도록 합니다.


![RGB-Bitcoin](assets/en/010.webp)


하지만 이 모델에는 두 가지 큰 단점이 있습니다:




- **확장성**: 각 노드가 모든 사람의 트랜잭션을 처리, 검증, 보관해야 하기 때문에 트랜잭션 용량에는 분명한 한계가 있으며, 특히 최대 블록 크기(쿠키를 제외한 Bitcoin의 경우 평균 10분 동안 1MB)와 관련이 있습니다;
- **프라이버시**: 모든 정보(금액, 목적지 주소 등)가 공개적으로 전송 및 저장되므로 거래의 기밀성이 제한됩니다.


![RGB-Bitcoin](assets/en/012.webp)


실제로 이 모델은 Bitcoin을 기본 Layer(Layer 1)로 사용하지만, 높은 트랜잭션 처리량과 일정 수준의 기밀성이 동시에 필요한 복잡한 용도로는 불충분할 수 있습니다.


Client-side Validation는 전체 네트워크가 모든 거래를 검증하고 저장하는 대신, 각 참여자(클라이언트)가 자신과 관련된 기록의 일부만 검증하는 반대 개념에 기반합니다:




- 자산(또는 기타 디지털 자산)을 받을 때, 해당 자산으로 이어지는 일련의 작업(상태 전환)을 알고 확인하고 그 자산의 정당성을 증명하기만 하면 됩니다;
- 이 일련의 작업은 ***Genesis***(초기 발행)에서 가장 최근 거래까지 비순환 방향 그래프(DAG) 또는 Shard, 즉 전체 내역의 일부분을 형성합니다.


![RGB-Bitcoin](assets/en/013.webp)


동시에 나머지 네트워크(또는 더 정확하게는 Bitcoin과 같은 기본 Layer)가 이 데이터의 세부 사항을 보지 않고도 최종 상태를 잠글 수 있도록 Client-side Validation은 ***Commitment***라는 개념에 의존합니다.


*Commitment*는 암호화 Commitment이며, 일반적으로 _해시_(예: SHA-256)가 Bitcoin 트랜잭션에 삽입되어 이 데이터를 공개하지 않고 개인 데이터가 포함되었음을 증명합니다.


이러한 _약속_ 덕분에 우리는 증명할 수 있습니다:




- 정보의 존재(Hash에 커밋되어 있기 때문에);
- 이 정보의 선행성(Blockchain에 날짜 및 블록 순서와 함께 고정되고 타임스탬프가 찍혀 있기 때문에).


그러나 정확한 내용은 공개되지 않으므로 기밀이 유지됩니다.


구체적으로 RGB State Transition의 작동 방식은 다음과 같습니다:




- 새 State Transition을 준비합니다(예: RGB token의 이전);
- 이 전환에 암호화된 Commitment을 generate로 변환하고 이를 Bitcoin 트랜잭션에 삽입합니다(이러한 커밋을 RGB 프로토콜에서는 "*앵커*"라고 합니다);
- 거래 상대방(수신자)은 이 자산과 관련된 고객 측 이력을 검색하고 Genesis의 Smart contract에서 전송하는 전환까지 엔드투엔드 일관성을 검증합니다.


![RGB-Bitcoin](assets/en/014.webp)


Client-side Validation은 두 가지 주요 이점을 제공합니다:




- **확장성:**


Blockchain에 포함된 *커밋*은 수십 바이트 정도의 작은 크기입니다. 따라서 Hash만 포함하면 되므로 블록 공간이 포화 상태가 되지 않습니다. 또한 각 사용자는 자신의 히스토리 조각(자신의 _stash_)만 저장하면 되기 때문에 off-chain 프로토콜이 발전할 수 있습니다.




- 개인 정보 보호:


트랜잭션 자체(즉, 세부 내용)는 공개되지 않습니다(On-Chain). 오직 지문(*Hash*)만 공개됩니다. 따라서 금액, 주소, Contract 로직은 비공개로 유지되며, 수신자는 이전의 모든 트랜잭션을 검사하여 자신의 Shard의 유효성을 로컬에서 확인할 수 있습니다. 분쟁이 발생하거나 증거가 필요한 경우를 제외하고는 수신자가 이 데이터를 공개할 이유가 없습니다.


RGB와 같은 시스템에서는 서로 다른 컨트랙트(또는 서로 다른 자산)의 여러 상태 전환을 단일 _commitment_를 통해 단일 Bitcoin 트랜잭션으로 집계할 수 있습니다. 이 메커니즘은 On-Chain 트랜잭션과 off-chain 데이터(클라이언트 측에서 검증된 트랜지션) 사이에 결정론적인 타임스탬프 링크를 설정하고, 여러 샤드를 단일 Anchor 포인트에 동시에 기록할 수 있게 하여 On-Chain 비용과 공간을 더욱 절감할 수 있게 합니다.


실제로 이 Bitcoin 트랜잭션이 검증되면 Blockchain에 이미 새겨진 Hash를 수정할 수 없게 되므로 기본 계약의 상태가 영구적으로 "잠기게" 됩니다.


![RGB-Bitcoin](assets/en/015.webp)


### Stash 컨셉


**Stash**은 참여자가 RGB Smart contract의 무결성과 기록을 유지하기 위해 반드시 보유해야 하는 클라이언트 측 데이터 집합입니다. 공유된 정보에서 특정 상태를 로컬로 재구성할 수 있는 라이트닝 채널과 달리, RGB Contract의 **Stash**은 다른 곳에 복제되지 않으므로 분실할 경우 기록에 대한 책임은 참여자에게 있으므로 누구도 이를 복원할 수 없습니다. 그렇기 때문에 RGB에 안정적인 백업 절차를 갖춘 시스템을 도입해야 합니다.


![RGB-Bitcoin](assets/en/016.webp)


### Single-Use Seal: 기원 및 작동


통화와 같은 자산을 수락할 때는 두 가지 보증이 필수적입니다:




- 수령한 아이템의 진품 여부;
- 이중 지출을 방지하기 위해 수령한 아이템의 고유성입니다.


지폐와 같은 물리적 자산의 경우, 복제되지 않았음을 증명하는 데는 물리적 존재만으로도 충분합니다. 그러나 자산이 순전히 정보인 디지털 세계에서는 정보가 쉽게 증식하고 복제될 수 있기 때문에 이러한 검증이 더 복잡합니다.


앞서 살펴본 것처럼 발신자가 상태 전환 내역을 공개하면 RGB token의 진위 여부를 확인할 수 있습니다. Genesis 트랜잭션 이후의 모든 트랜잭션에 액세스하면 token의 진위 여부를 확인할 수 있습니다. 이 원리는 코인의 이력을 원래의 Coinbase Transaction까지 추적하여 유효성을 확인할 수 있는 Bitcoin의 원리와 유사합니다. 그러나 Bitcoin과 달리 RGB의 상태 전환 이력은 비공개이며 클라이언트 측에 보관됩니다.


Double-spending 토큰의 RGB을 방지하기 위해 "**Single-Use Seal**"라는 메커니즘을 사용합니다. 이 시스템은 한 번 사용된 각 token을 두 번 다시 부정하게 재사용할 수 없도록 보장합니다.


일회용 씰은 피터 토드가 2016년에 제안한 암호화 기본 요소로, 물리적 씰의 개념과 유사하며, 일단 Seal이 컨테이너에 배치되면 Seal을 비가역적으로 깨뜨리지 않고는 컨테이너를 열거나 수정할 수 없게 됩니다.


![RGB-Bitcoin](assets/en/018.webp)


디지털 세계로 전환된 이 접근 방식은 일련의 이벤트가 실제로 발생했으며 더 이상 사후적으로 변경할 수 없음을 증명할 수 있게 해줍니다. 따라서 일회용 씰은 'Hash + Timestamp'라는 단순한 논리를 넘어 '단 한 번만' 닫을 수 있는 Seal이라는 개념을 추가합니다.


![RGB-Bitcoin](assets/en/017.webp)


일회용 씰을 사용하려면 출판물의 존재 여부를 증명할 수 있고, 일단 정보가 유포된 후에는 위조가 어렵고(불가능하지는 않더라도) 출판물을 증명할 수 있는 매체가 필요합니다. 예를 들어 대중에게 배포되는 종이 신문과 마찬가지로 **Blockchain**(Bitcoin과 같은)가 이 역할을 수행할 수 있습니다. 아이디어는 다음과 같습니다:




- 메시지 `h(m)`의 내용을 공개하지 않고 메시지 `m`에 대한 특정 Commitment가 청중에게 공개되었음을 증명하고 싶습니다;
- H(m')` 대신에 다른 경쟁 `h(m)'` 메시지 Commitment가 게시되지 않았음을 증명하고자 합니다;
- 또한 특정 날짜 이전에 'm'이라는 메시지가 존재하는지 확인할 수 있기를 원합니다.


트랜잭션이 블록에 포함되는 즉시 전체 네트워크는 그 존재와 내용에 대한 위조 불가능한 동일한 증거를 갖게 됩니다(_커밋_은 메시지의 진위를 증명하는 동시에 세부 사항을 숨길 수 있기 때문에 적어도 부분적으로는).


따라서 Single-Use Seal은 모든 이해 당사자가 확인할 수 있는 방식으로 단 한 번만 메시지를 공개하겠다는 공식적인 약속으로 볼 수 있습니다(현 단계에서는 아직 알려지지 않음).


존재 날짜를 증명하는 단순한 _공약_(Hash) 또는 타임스탬프와 달리, Single-Use Seal은 **대체 Commitment**가 공존할 수 없다는 추가 보증을 제공합니다: 동일한 Seal을 두 번 닫거나 봉인된 메시지를 교체하려고 시도할 수 없습니다.


다음 비교는 이 원칙을 이해하는 데 도움이 됩니다:




- **암호화 Commitment(Hash)**: Hash 기능을 사용하면 Hash을 게시하여 데이터(숫자)를 커밋할 수 있습니다. 사전 이미지를 공개할 때까지 데이터는 비밀로 유지되지만, 미리 알고 있었다는 것을 증명할 수 있습니다;
- **Timestamp (Blockchain)**: 이 Hash을 Blockchain에 삽입함으로써 정확한 순간(블록에 포함되는 순간)에 이를 알고 있었음을 증명합니다;
- **Single-Use Seal**: 일회용 씰을 사용하면 Commitment를 한 단계 더 특별하게 만들 수 있습니다. 하나의 Hash로 여러 개의 모순된 약속을 동시에 만들 수 있습니다(가족에게는 "*남자아이다*"라고 발표하고 개인 일기에는 "*여자아이다*"라고 발표하는 의사의 문제). Single-Use Seal은 Commitment를 Bitcoin Blockchain과 같은 출판 증명 매체에 연결하여 이러한 가능성을 제거함으로써 UTXO의 지출이 Commitment를 최종적으로 봉인하도록 합니다. 한 번 사용한 UTXO는 Commitment를 대체하기 위해 다시 사용할 수 없습니다.


|                                                                                  | Simple commitment (digest/hash) | Timestamps | Single-use seals |
| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |
| Publishing the commitment does not reveal the message                           | Yes                             | Yes        | Yes              |
| Proof of the commitment date / existence of the message before a certain date  | Impossible                      | Possible   | Possible         |
| Proof that no alternative commitment can exist                                 | Impossible                      | Impossible | Possible         |

일회용 씰은 크게 세 단계로 작동합니다:


**Seal Definition:**




- Alice는 Seal의 게시 규칙(언제, 어디서, 어떻게 메시지를 게시할지)을 미리 정의합니다;
- Bob은 이러한 조건을 수락하거나 인정합니다.


![RGB-Bitcoin](assets/en/021.webp)


**Seal 클로징:**




- 런타임에 Alice은 실제 메시지를 게시하여 Seal을 닫습니다(일반적으로 _commitment_ 형식, 예: Hash);
- 또한 Seal이 닫혀 있고 취소할 수 없음을 증명하는 **증인**(암호화 증명)을 제공합니다.


![RGB-Bitcoin](assets/en/019.webp)


**Seal 인증:**




- Seal이 닫히면 Bob는 더 이상 열 수 없으며 닫혔는지 여부만 확인할 수 있습니다;
- Bob은 Seal, **목격자**, 메시지(또는 그의 Commitment)를 수집하여 모든 것이 일치하는지, 경쟁 인장이나 다른 버전이 없는지 확인합니다.


프로세스는 다음과 같이 요약할 수 있습니다:


```txt
# Defined by Alice, validated or accepted by Bob
seal <- Define()
# Seal is closed by Alice with the message
witness <- Close(seal, message)
# Verification by Bob
bool <- Verify(seal, witness, message)
```


그러나 Client-side Validation은 한 단계 더 나아가 Seal의 정의 자체가 Blockchain 외부에 남아 있다면, 누군가가 (이론적으로) 해당 Seal의 존재 또는 정당성에 대해 이의를 제기할 수 있습니다. 이 문제를 극복하기 위해 서로 연동되는 일회용 씰 체인이 사용됩니다:




- 닫힌 각 Seal에는 다음 Seal의 정의가 포함되어 있습니다;
- 저희는 이러한 폐쇄(_약속_과 함께)를 Blockchain(Bitcoin 트랜잭션에서)에 등록합니다;
- 따라서 이전 Seal를 수정하려는 시도는 Bitcoin에 포함된 기록과 모순됩니다.


이것이 바로 RGB 시스템이 하는 일입니다:




- 게시된 메시지는 클라이언트 측의 유효성이 검증된 데이터에 대한 _커밋_입니다;
- Seal Definition은 Bitcoin UTXO와 연결되어 있습니다;
- Seal은 이 UTXO가 소비되거나 동일한 Commitment에 새 출력이 적립되면 닫힙니다;
- 이러한 UTXO를 사용하는 트랜잭션 체인은 발행 증명에 해당하며, 따라서 RGB의 모든 전환 또는 상태 변경은 Bitcoin에 고정됩니다.


요약하자면




- 봉인 정의_는 향후 Seal을 Commitment로 만들려는 UTXO입니다;
- 이 UTXO를 사용하면 _봉인 마감_이 발생하여 Commitment이 포함된 트랜잭션을 생성합니다;
- 증인_은 트랜잭션 자체로, 이 콘텐츠로 Seal을 청산했음을 증명하는 트랜잭션입니다;
- Seal이 닫히지 않았다는 것을 증명할 수는 없지만(아직 보지 못한 블록에서 UTXO가 이미 사용되지 않았거나 사용되지 않을 것이라고 절대적으로 확신할 수는 없습니다), 실제로 닫혔다는 것은 증명할 수 있습니다.


이 고유성은 Client-side Validation에서 중요합니다. State Transition를 검증할 때, 경쟁하는 Commitment에서 이전에 사용된 것이 아닌 고유한 UTXO에 해당하는지 확인해야 합니다. 이것이 바로 off-chain 스마트 컨트랙트에서 이중 지출이 발생하지 않도록 보장하는 것입니다.


### 여러 커밋과 루트


RGB Smart contract는 여러 개의 일회용 씰(여러 개의 UTXO)을 동시에 사용해야 할 수 있습니다. 또한 단일 Bitcoin 트랜잭션은 여러 개의 개별 컨트랙트를 참조할 수 있으며, 각 컨트랙트는 자체 State Transition을 봉인합니다. 이를 위해서는 **멀티 Commitment** 메커니즘을 통해 중복되는 커밋이 없음을 결정론적이고 고유하게 증명할 수 있어야 합니다. RGB에서 **Anchor**이라는 개념이 등장하는데, 이는 Bitcoin 트랜잭션과 하나 이상의 클라이언트 측 커밋(상태 전환)을 연결하는 특수 구조로, 각각 다른 Contract에 속할 가능성이 있습니다. 다음 장에서 이 개념에 대해 자세히 살펴보겠습니다.


![RGB-Bitcoin](assets/en/023.webp)


프로젝트의 주요 GitHub 리포지토리 중 두 곳(LNPBP 조직 산하)에는 첫 번째 장에서 학습한 이러한 개념의 기본 구현이 모여 있습니다:




- **클라이언트_사이드_검증**: 로컬 유효성 검사를 위한 Rust 프리미티브가 포함되어 있습니다;
- **single_use_seals**: 이러한 씰을 안전하게 정의하고 닫는 로직을 구현합니다.


![RGB-Bitcoin](assets/en/020.webp)


이러한 소프트웨어 브릭은 Bitcoin에 구애받지 않으며, 이론적으로는 다른 출판 증명 매체(다른 레지스트리, 저널 등)에도 적용할 수 있다는 점에 유의하세요. 실제로 RGB은 견고함과 광범위한 합의로 인해 Bitcoin에 의존하고 있습니다.


![RGB-Bitcoin](assets/en/021.webp)


### 대중의 질문


#### 일회용 씰의 폭넓은 사용을 위해


피터 토드는 또한 _오픈 타임스탬프_ 프로토콜을 만들었으며, Single-Use Seal 개념은 이러한 아이디어의 자연스러운 확장입니다. RGB 외에도 _병합 채굴_에 의존하지 않고 _사이드체인_을 구축하거나 BIP300과 같은 드라이브체인 관련 제안과 같은 다른 사용 사례도 상상할 수 있습니다. 원칙적으로 단일 Commitment를 필요로 하는 모든 시스템은 이 암호화 프리미티브를 활용할 수 있습니다. 현재 RGB이 본격적으로 구현된 첫 번째 주요 사례입니다.


#### 데이터 가용성 문제


Client-side Validation에서는 각 사용자가 자신의 기록 일부를 저장하기 때문에 전 세계적으로 데이터 가용성이 보장되지 않습니다. Contract 발행자가 특정 정보를 보류하거나 취소하는 경우, 사용자는 오퍼의 실제 진행 상황을 알지 못할 수 있습니다. 일부 경우(예: 스테이블 코인)에는 발행자가 유통량을 증명하기 위해 공개 데이터를 유지해야 하지만, 그렇게 할 기술적 의무는 없습니다. 따라서 의도적으로 불투명한 계약을 설계할 수 있으며, 이는 신뢰에 대한 의문을 제기할 수 있습니다.


#### 샤딩 및 Contract 격리


각 Contract은 고립된 _샤드_를 나타냅니다: 예를 들어 USDT와 USDC는 이력을 공유할 필요가 없습니다. 아토믹 스왑은 여전히 가능하지만, 레지스터를 병합하는 것은 포함되지 않습니다. 모든 것은 각 참가자에게 전체 내역 그래프를 공개하지 않고 암호화 Commitment에 의해 수행됩니다.


### 결론


Client-side Validation의 개념이 Blockchain 및 _상태 채널_과 어떻게 부합하는지, 분산 컴퓨팅 트릴레마에 어떻게 대응하는지, Double-spending을 피하고 *타임스탬핑*을 위해 Bitcoin Blockchain을 어떻게 고유하게 활용하는지를 살펴봤습니다. 이 아이디어는 **Single-Use Seal**의 개념을 기반으로 하며, 마음대로 재사용할 수 없는 고유한 약속을 생성할 수 있게 해줍니다. 이러한 방식으로 각 참가자는 꼭 필요한 내역만 업로드하여 스마트 컨트랙트의 확장성과 기밀성을 높이는 동시에 Bitcoin의 보안을 배경으로 유지합니다.


다음 단계에서는 이 Single-Use Seal 메커니즘이 Bitcoin에 어떻게 적용되는지(UTXO를 통해), 앵커가 어떻게 생성되고 검증되는지, 그리고 RGB에서 완전한 스마트 컨트랙트가 어떻게 구축되는지 더 자세히 설명할 것입니다. 특히 다중 커미트먼트 문제, 즉 취약점이나 이중 커미트먼트 없이 Bitcoin 트랜잭션이 여러 컨트랙트의 여러 상태 전환을 동시에 봉인한다는 것을 증명하는 기술적 과제에 대해 살펴볼 것입니다.


두 번째 장의 기술적인 세부 사항을 살펴보기 전에 주요 정의(Client-side Validation, Single-Use Seal, 앵커 등)를 다시 한 번 읽고 전체적인 논리를 기억하세요. 저희는 Bitcoin Blockchain의 장점(보안, 탈중앙화, 타임스탬프)과 off-chain 솔루션의 장점(속도, 기밀성, 확장성)을 조화시키고자 하며, 이것이 바로 RGB과 Client-side Validation가 달성하고자 하는 목표라는 것을 기억하시기 바랍니다.


## Commitment Layer


<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>


:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::


이 장에서는 Bitcoin Blockchain 내에서 Client-side Validation 및 일회용 씰의 구현에 대해 살펴보겠습니다. RGB의 **Commitment Layer**(Layer 1)의 주요 원칙을 소개하며, 특히 Bitcoin 트랜잭션에서 Seal을 정의하고 종료하는 데 사용하는 **TxO2** 체계에 중점을 두고 설명하겠습니다. 다음으로 아직 자세히 다루지 않은 두 가지 중요한 사항에 대해 설명하겠습니다:




- 결정론적 Bitcoin 커미트먼트_;
- 다중 프로토콜 약정.


이러한 개념의 조합을 통해 단일 UTXO, 즉 단일 Blockchain 위에 여러 시스템 또는 계약을 중첩할 수 있습니다.


설명한 암호화 연산은 절대적인 측면에서 다른 블록체인이나 퍼블리싱 미디어에도 적용될 수 있지만, 탈중앙화, 검열에 대한 저항, 모두에게 개방성이라는 측면에서 Bitcoin의 특성은 **RGB**에서 요구하는 것과 같은 고급 프로그래밍 기능을 개발하는 데 이상적인 기반이 된다는 점을 기억해야 합니다.


### Commitment의 Bitcoin 체계 및 RGB에서의 사용


과정의 첫 장에서 살펴본 것처럼 일회용 씰은 일반적인 개념으로, 트랜잭션의 특정 위치에 Commitment(_commitment_)를 포함하겠다는 약속을 하고 이 위치는 메시지에서 닫는 Seal처럼 작동합니다. 그러나 Bitcoin Blockchain에서는 이 _commitment_를 어디에 배치할지 선택할 수 있는 몇 가지 옵션이 있습니다.


로직을 이해하기 위해 기본 원칙을 상기해 보겠습니다. _일회용 봉인_을 닫으려면 주어진 메시지에 _커밋_을 삽입하여 봉인된 영역을 소비합니다. Bitcoin에서는 여러 가지 방법으로 이 작업을 수행할 수 있습니다:




- **공개 키 또는 Address** 사용


특정 공개 키 또는 Address가 _일회용 씰_이라고 결정할 수 있습니다. 이 키 또는 Address가 트랜잭션에서 On-Chain로 나타나면, 이는 Seal이 특정 메시지와 함께 닫힌다는 것을 의미합니다.




- **Bitcoin** 트랜잭션 출력 사용


즉, _일회용 씰_은 정확한 _아웃포인트_(txid + 출력 번호 쌍)로 정의됩니다. 이 _아웃포인트_가 소비되는 즉시 Seal은 닫힙니다.


RGB을 작업하는 동안 Bitcoin에서 이러한 씰을 구현하는 최소 4가지 방법을 확인했습니다:




- 공개 키를 통해 Seal를 정의하고 _output_에서 닫습니다;
- 아웃포인트_로 Seal을 정의하고 _출력_으로 닫습니다;
- 공개 키 값을 통해 Seal를 정의하고 _input_에서 닫습니다;
- 아웃포인트_를 통해 Seal를 정의하고 _입력_에서 닫습니다.


| Schema Name | Seal Definition           | Seal Closure              | Additional Requirements                                        | Main Application            | Possible Commitment Schemes     |
| ----------- | ------------------------- | ------------------------- | -------------------------------------------------------------- | --------------------------- | -------------------------------- |
| PkO         | Public Key Value          | Transaction Output        | P2(W)PKH                                                       | None at the moment          | Keytweak, taptweak, opret       |
| TxO2        | Transaction Output        | Transaction Output        | Requires deterministic commitments on Bitcoin                  | RGBv1 (universal)           | Keytweak, tapret, opret         |
| PkI         | Public Key Value          | Transaction Input         | Taproot only & not compatible with legacy wallets              | Bitcoin-based identities    | Sigtweak, witweak               |
| TxO1        | Transaction Output        | Transaction Input         | Taproot only & not compatible with legacy wallets              | None at the moment          | Sigtweak, witweak               |


RGB에서는 **Seal**의 정의로 _아웃포인트_를 사용하고 이 _아웃포인트_를 소비하는 트랜잭션의 출력에 _커밋_을 배치하기로 선택했기 때문에 이러한 각 구성에 대해서는 자세히 설명하지 않겠습니다. 따라서 속편에서는 다음과 같은 개념을 도입할 수 있습니다:




- **"Seal Definition"**: 주어진 _아웃포인트_(txid + 출력 번호로 식별됨);
- **"Seal 닫는 중"**: 이 _아웃포인트_를 소비하는 트랜잭션으로, _커미트먼트_가 메시지에 추가됩니다.


이 구성은 RGB 아키텍처와의 호환성을 위해 선택되었지만 다른 구성도 다양한 용도에 유용할 수 있습니다.


"TxO2"의 "O2"는 정의와 종결이 모두 트랜잭션 출력의 지출(또는 생성)을 기반으로 한다는 점을 상기시켜 줍니다.


### TxO2 다이어그램 예시


다시 한 번 말씀드리지만, _일회용 씰_을 정의한다고 해서 반드시 On-Chain 트랜잭션을 게시할 필요는 없습니다. 예를 들어 Alice에는 이미 사용하지 않은 UTXO가 있으면 충분합니다. 그녀는 결정할 수 있습니다: "이 _아웃포인트_(이미 존재하는)는 이제 내 Seal이다"라고 결정할 수 있습니다. 그녀는 이를 로컬(_클라이언트 측_)에 기록하고, 이 UTXO가 소비될 때까지 Seal는 열려 있는 것으로 간주합니다.


![RGB-Bitcoin](assets/en/024.webp)


Seal을 닫으려는 날(이벤트에 신호를 보내거나 특정 메시지를 Anchor에 보내기 위해), 이 UTXO을 새 트랜잭션에 보냅니다(이 트랜잭션을 흔히 "_증인 트랜잭션_(_segwit_과 관련이 없으며, 그냥 우리가 부르는 용어입니다)"이라고 합니다). 이 새 트랜잭션에는 메시지에 대한 _커밋먼트_가 포함됩니다.


![RGB-Bitcoin](assets/en/025.webp)


이 예제에서는




- 이 트랜잭션에 특정 메시지가 숨겨져 있다는 사실은 Bob(또는 Alice가 전체 증거를 공개하기로 선택한 사람)을 제외하고는 아무도 알 수 없습니다;
- 아웃포인트_가 소비되었다는 것은 누구나 확인할 수 있지만, 메시지가 실제로 트랜잭션에 고정되었다는 증거는 Bob만이 보유하고 있습니다.


이 TxO2 체계를 설명하기 위해 PGP 키를 해지하는 메커니즘으로 _일회용 씰_을 사용할 수 있습니다. 서버에 해지 인증서를 게시하는 대신 Alice은 다음과 같이 말할 수 있습니다: "이 Bitcoin 출력은 사용되었다면 내 PGP 키가 해지되었음을 의미합니다."라고 말할 수 있습니다.


따라서 Alice에는 특정 상태 또는 데이터(그녀에게만 알려진)가 로컬(클라이언트 측)에 연결된 특정 UTXO가 있습니다.


Alice은 UTXO이 지출되면 특정 이벤트가 발생한 것으로 간주한다고 Bob에게 알립니다. 겉으로 보기에는 Bitcoin 트랜잭션으로 보이지만 Bob는 이 지출에 숨겨진 의미가 있다는 것을 알고 있습니다.


![RGB-Bitcoin](assets/en/026.webp)


Alice은 이 UTXO을 사용하면서 새 키를 나타내는 메시지 또는 단순히 이전 키의 해지를 나타내는 메시지로 Seal를 닫습니다. 이러한 방식으로 On-Chain을 모니터링하는 사람은 누구나 UTXO이 사용되었음을 알 수 있지만 전체 증명을 가진 사람만 이것이 정확히 PGP 키의 해지라는 것을 알 수 있습니다.


![RGB-Bitcoin](assets/en/027.webp)


Bob 또는 다른 관련자가 숨겨진 메시지를 확인하려면 Alice가 off-chain 정보를 제공해야 합니다.


![RGB-Bitcoin](assets/en/028.webp)


따라서 Alice은 Bob에게 다음을 제공해야 합니다:




- 메시지 자체(예: 새 PGP 키);
- 메시지가 거래에 관련되었다는 암호화 증명(_추가 거래 증명_ 또는 _앵커_라고 함).


![RGB-Bitcoin](assets/en/029.webp)


타사에는 이 정보가 없습니다. UTXO가 사용되었다는 사실만 확인할 수 있습니다. 따라서 기밀성이 보장됩니다.


구조를 명확히 하기 위해 프로세스를 두 가지 트랜잭션으로 요약해 보겠습니다:




- **트랜잭션 1**: 여기에는 _봉인 정의_, 즉 Seal의 역할을 할 _아웃포인트_가 포함되어 있습니다.


![RGB-Bitcoin](assets/en/031.webp)




- 트랜잭션 2: 이 _아웃포인트_를 씁니다. 이렇게 하면 Seal이 닫히고 동일한 트랜잭션에서 메시지에 _commitment_를 삽입합니다.


![RGB-Bitcoin](assets/en/033.webp)


따라서 두 번째 트랜잭션을 "_증인 트랜잭션_"이라고 부릅니다.


이를 다른 각도에서 설명하기 위해 두 개의 레이어로 표현할 수 있습니다:




- **최상위 Layer(Blockchain, 공개)**: 모든 사람이 거래를 보고 *아웃포인트*가 사용되었다는 것을 알 수 있습니다;
- **하위 Layer(클라이언트 측, 비공개)**: 암호화 증명과 로컬에 보관하는 메시지를 통해 Alice(또는 관련자)만이 이 비용이 이러한 메시지에 해당한다는 것을 알 수 있습니다.


![RGB-Bitcoin](assets/en/034.webp)


그러나 Seal을 닫을 때 _commitment_를 어디에 삽입해야 하는지에 대한 의문이 생깁니다.


이전 섹션에서는 Client-side Validation 모델을 RGB 및 기타 시스템에 적용하는 방법에 대해 간략하게 언급했습니다. 여기서는 **결정론적 Bitcoin 커미트먼트**와 이를 트랜잭션에 통합하는 방법에 대해 다루겠습니다. 왜 단일 Commitment을 _증인 트랜잭션_에 삽입하려고 하는지, 그리고 무엇보다도 공개되지 않은 다른 경쟁 커밋이 없도록 하는 방법을 이해하는 것이 중요합니다.


### 거래의 Commitment 위치


특정 메시지가 트랜잭션에 포함되어 있다는 증거를 누군가에게 제공할 때, 동일한 트랜잭션에 공개되지 않은 다른 형태의 Commitment(두 번째 숨겨진 메시지)이 존재하지 않는다는 것을 보장할 수 있어야 합니다. Client-side Validation가 견고하게 유지되려면, 트랜잭션에 단일 _공약_을 배치하여 _일회용 봉인_을 닫는 **결정론적** 메커니즘이 필요합니다.


증인 거래_는 유명한 UTXO(또는 _봉인 정의_)을 소비하며, 이 지출은 Seal의 종결에 해당합니다. 엄밀히 말하면 각 아웃포인트는 한 번만 사용할 수 있다는 것을 알고 있습니다. 이것이 바로 Bitcoin의 이중 지출에 대한 저항을 뒷받침하는 것입니다. 그러나 지출 트랜잭션에는 여러 개의 _입력_, 여러 개의 _출력_이 있거나 복잡한 방식(코인조인, 라이트닝 채널 등)으로 구성될 수 있습니다. 따라서 이 구조에서 _약정_을 삽입할 위치를 명확하고 일관되게 정의해야 합니다.


어떤 방식(PkO, TxO2 등)이든 _commitment_를 삽입할 수 있습니다:




- **입력** 비아에서:
- 시그트위크**("Sign-to-Contract" 원칙과 유사하게 ECDSA 서명의 `r` 구성 요소를 수정함)**;
- 위트위크**(트랜잭션의 _분리된 증인_ 데이터가 수정됨)**.
- **출력** 비아에서:
- 키 조정**(수신자의 공개 키가 메시지와 함께 "조정"됨)**;
- **Opret**(메시지는 비사용 출력 `OP_RETURN`에 배치됨);
- Tapret**(또는 _Taptweak_)**은 Taproot 키의 스크립트 부분에 Commitment를 삽입하여 공개키를 결정론적으로 수정하는 Taproot에 의존합니다.


![RGB-Bitcoin](assets/en/035.webp)


각 방법에 대한 자세한 내용은 다음과 같습니다:


![RGB-Bitcoin](assets/en/038.webp)


***서명 조정(서명-Contract):***


이전에는 서명의 무작위 부분(ECDSA 또는 슈노르)을 악용하여 _약속_을 삽입하는 방식이 있었는데, 이것이 "**Sign-to-Contract**"으로 알려진 기법입니다. 무작위로 생성된 Nonce를 데이터가 포함된 Hash로 대체합니다. 이렇게 하면 트랜잭션에 추가 공간 없이 서명을 통해 Commitment가 암시적으로 드러납니다. 이 접근 방식에는 여러 가지 장점이 있습니다:




- On-Chain 과부하 없음(기본 Nonce과 동일한 위치 사용);
- 이론적으로는 Nonce이 처음에는 임의의 데이터이므로 이는 상당히 불연속적일 수 있습니다.


하지만 두 가지 큰 단점이 드러났습니다:




- Multisig 이전 버전: 서명자가 여러 명인 경우, 어떤 서명에 _약속_을 담을지 결정해야 합니다. 서명은 서로 다르게 주문할 수 있으며 서명자가 거부하면 _약속_의 결과에 대한 통제권을 잃게 됩니다;
- MuSig와 공유 Nonce: 슈노르 Multisig(*MuSig*)을 사용하면 Nonce 생성은 다자간 알고리즘이므로 Nonce를 개별적으로 조정하는 것이 사실상 불가능해집니다.


실제로 **sig tweak**은 기존 하드웨어(하드웨어 지갑) 및 형식(라이트닝 등)과도 호환이 잘 되지 않습니다. 그래서 이 좋은 아이디어를 실행에 옮긴 것이 Hard입니다.


***키 조정(유료-Contract):***


**키 조정**은 *계약에 대한 지불*이라는 과거 개념을 사용합니다. 공개 키 `X`에 `H(메시지)` 값을 추가하여 조정합니다. 구체적으로, `X = x * G`이고 `h = H(메시지)`라면, 새로운 키는 `X' = X + h * G`가 됩니다. 이 조정된 키는 Commitment를 `메시지`에 숨깁니다. 원래 개인 키의 소유자는 자신의 개인 키 `x`에 `h`를 추가하여 출력을 사용할 수 있는 키를 가지고 있음을 증명할 수 있습니다. 이론적으로 이것은 우아합니다:




- 커미트먼트_는 추가 필드를 추가하지 않고 입력합니다;
- 추가 On-Chain 데이터는 저장하지 않습니다.


그러나 실제로는 다음과 같은 어려움에 직면하게 됩니다:




- 지갑은 표준 공개키가 "조정"되었기 때문에 더 이상 인식하지 못하며, 따라서 UTXO을 일반적인 키와 쉽게 연결할 수 없습니다;
- 하드웨어 지갑은 표준 파생 키에서 파생되지 않은 키로 서명하도록 설계되지 않았습니다;
- 스크립트, 설명자 등을 조정해야 합니다.


RGB의 맥락에서 이 경로는 2021년까지 계획되었지만 현재의 표준 및 인프라에서 작동하기에는 너무 복잡하다는 것이 입증되었습니다.


***증인 조정:***


인스크립션 오디날스(_inscriptions Ordinals_)와 같은 특정 프로토콜이 실행에 옮긴 또 다른 아이디어는 트랜잭션의 '증인' 섹션에 데이터를 직접 배치하는 것입니다(따라서 "증인 조정"이라는 표현이 사용됨). 그러나 이 방법은




- 참여도를 즉시 확인할 수 있습니다(말 그대로 원시 데이터를 증인에 붙여넣기만 하면 됩니다);
- 검열의 대상이 될 수 있습니다(너무 크거나 기타 임의의 특성으로 인해 채굴자 또는 노드가 릴레이를 거부할 수 있음);
- 신중함과 가벼움이라는 RGB의 목표와 달리 블록의 공간을 소비합니다.


또한 증인은 특정 상황에서 잘라낼 수 있도록 설계되었기 때문에 강력한 증거를 확보하는 것이 더 복잡해질 수 있습니다.


***오픈 리턴(opret):***


작동이 매우 간단한 'OP_RETURN'을 사용하면 트랜잭션의 특수 필드에 Hash 또는 메시지를 저장할 수 있습니다. 그러나 즉시 감지할 수 있습니다. 모든 사람이 트랜잭션에 _커밋_이 있다는 것을 알 수 있으며, 검열하거나 폐기할 수 있을 뿐만 아니라 추가 출력을 추가할 수도 있습니다. 이렇게 하면 투명성과 크기가 증가하기 때문에 Client-side Validation 솔루션의 관점에서는 만족도가 떨어지는 것으로 간주됩니다.


```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|

1-byte       1-byte         32 bytes
```


### Tapret


마지막 옵션은 **Taproot**(BIP341과 함께 도입)을 *Tapret* 체계와 함께 사용하는 것입니다. *Tapret*은 결정론적 Commitment의 더 복잡한 형태로, Blockchain의 설치 공간과 Contract 작업의 기밀성 측면에서 개선된 기능을 제공합니다. 주요 아이디어는 [Taproot 트랜잭션](https://github.com/Bitcoin/BIPs/blob/master/BIP-0341.mediawiki)의 '스크립트 경로 지출' 부분에서 Commitment를 숨기는 것입니다.


![RGB-Bitcoin](assets/en/036.webp)


Commitment이 Taproot 트랜잭션에 어떻게 삽입되는지 설명하기 전에, 다음과 같이 64바이트 문자열 [구성](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196)과 **필수적으로** 일치해야 하는 Commitment의 **정확한 형식**을 살펴보겠습니다:


```txt
64-byte_Tapret_Commitment =

OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|

TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```




- 29바이트의 `OP_RESERVED`, `OP_RETURN`, `OP_PUSHBYTE_33`이 31바이트의 _prefix_ 부분을 구성합니다;
- 다음으로 32바이트의 _약속_(보통 **MPC**의 Merkle Root)에 1바이트의 **Nonce**를 추가합니다(이 두 번째 부분의 경우 총 33바이트).


따라서 64바이트의 `Tapret` 메서드는 29바이트의 `OP_RESERVED` 접두사를 붙이고 Nonce로 추가 바이트를 추가한 `Opret`처럼 보입니다.


구현, 기밀성 및 확장 측면에서 유연성을 유지하기 위해 Tapret 체계는 요구사항에 따라 다양한 사용 사례를 고려합니다:




- 기존 스크립트 경로 구조 없이 Tapret Commitment을 Taproot 트랜잭션에 고유하게 통합합니다;
- 스크립트 경로가 이미 장착된 Taproot 트랜잭션에 Tapret Commitment을 통합합니다.


이 두 가지 시나리오를 각각 자세히 살펴보겠습니다.


#### 기존 스크립트 경로 없이 탭렛 통합


이 첫 번째 경우에는 연결된 스크립트 경로(*Script Path*)가 없이 내부 공개 키 'P' *(내부 키*)만 포함된 Taproot 출력 키(*Taproot 출력 키*) 'Q'에서 시작합니다:


![RGB-Bitcoin](assets/en/047.webp)




- p`: _키 경로 지출_에 대한 내부 공개 키입니다.
- g`: 타원 커브의 생성점 [secp256k1](https://en.Bitcoin.it/wiki/Secp256k1).

-t = tH_TWEAK(P)`는 [BIP86](https://github.com/Bitcoin/BIPs/blob/master/BIP-0086.mediawiki#Address-derivation)에 따라 _태그 해시_(예: `SHA-256(TapTweak) || P)를 통해 계산된 트윅 계수입니다. 이는 숨겨진 스크립트가 없음을 증명합니다.


탭렛 **Commitment**을 포함하려면 다음과 같이 **고유 스크립트**와 함께 **스크립트 경로 지출**을 추가하세요:


![RGB-Bitcoin](assets/en/048.webp)




- t = tH_TWEAK(P || Script_root)`는 **Script_root**를 포함한 새로운 조정 인자가 됩니다.
- 스크립트_루트 = tH_BRANCH(64-byte_Tapret_Commitment)`는 이 **스크립트**의 루트를 나타내며, 이는 간단히 `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)` 타입의 Hash입니다.


여기서 Taproot 트리의 포함 및 고유성 증명은 단일 내부 공개 키 'P'로 귀결됩니다.


#### 기존 스크립트 경로에 탭렛 통합


두 번째 시나리오는 이미 여러 스크립트가 포함된 더 복잡한 `Q` **Taproot** 출력에 관한 것입니다. 예를 들어 3개의 스크립트로 구성된 트리가 있습니다:


![RGB-Bitcoin](assets/en/049.webp)




- tH_LEAF(x)`는 리프 스크립트의 정규화된 태그가 지정된 Hash 함수를 지정합니다.
- 'A, B, C'는 Taproot 구조에 이미 포함된 스크립트를 나타냅니다.


Tapret Commitment를 추가하려면 트리의 첫 번째 레벨에 *사용할 수 없는 스크립트*를 삽입하여 기존 스크립트를 한 레벨 아래로 이동시켜야 합니다. 시각적으로 트리가 다음과 같이 됩니다:


![RGB-Bitcoin](assets/en/050.webp)




- 'tHABC`는 최상위 그룹 `A, B, C`의 태그가 지정된 Hash을 나타냅니다.
- tHT`는 64바이트 `Tapret`에 해당하는 스크립트의 Hash를 나타냅니다.


Taproot 규칙에 따르면 각 가지/잎은 사전적 Hash 순서에 따라 결합해야 합니다. 두 가지 경우가 있습니다:




- **tHT` > `tHABC`**: 탭렛 Commitment이 트리의 오른쪽으로 이동합니다. 고유성 증명에는 `tHABC`와 `P`만 필요합니다;
- **tHT` < `tHABC`**: 왼쪽에 Tapret Commitment이 배치되어 있습니다. 오른쪽에 다른 타프렛 Commitment이 없음을 증명하려면 `tHAB`와 `tHC`를 공개하여 다른 스크립트가 없음을 입증해야 합니다.


첫 번째 경우의 시각적 예시(`tHABC < tHT`):


![RGB-Bitcoin](assets/en/051.webp)


두 번째 경우의 예(`tHABC > tHT`):


![RGB-Bitcoin](assets/en/052.webp)


#### Nonce를 사용한 최적화


기밀성을 향상시키기 위해 `<Nonce>`(64바이트 `Tapret`의 마지막 바이트)의 값을 "마이닝"(더 정확한 용어는 "브루트포싱")하여 `tHABC < tHT`가 되도록 Hash `tHT`를 얻으려고 시도할 수 있습니다. 이 경우 Commitment이 오른쪽에 배치되어 사용자가 Tapret의 고유성을 증명하기 위해 기존 스크립트의 전체 내용을 공개할 필요가 없습니다.


요약하자면, '타프렛'은 Commitment를 Taproot 트랜잭션에 통합하는 개별적이고 결정론적인 방법을 제공하면서 RGB의 Client-side Validation 및 Single-Use Seal 로직에 필수적인 고유성과 모호성에 대한 요구 사항을 존중합니다.


#### 유효한 종료


RGB Commitment 트랜잭션의 경우, 유효한 Bitcoin Commitment 체계의 주요 요건은 다음과 같습니다: 트랜잭션(*Witness Transaction*)에는 반드시 단일 Commitment가 포함되어야 합니다. 이 요건 때문에 동일한 트랜잭션 내에서 클라이언트 측 유효성 검사 데이터에 대한 대체 기록을 구성하는 것은 불가능합니다. 이는 _일회용 씰_이 닫히는 메시지가 고유하다는 것을 의미합니다.


이 원칙을 충족하기 위해 트랜잭션의 출력 수에 관계없이 **단 하나의 출력**만 Commitment를 포함할 수 있어야 합니다. 사용되는 각 스키마(*Opret* 또는 *Tapret*)에 대해 RGB _commitment_를 포함할 수 있는 유일한 유효한 출력은 다음과 같습니다:




- 해석: 스키마에 대한 첫 번째 출력 `OP_RETURN`(있는 경우)입니다;
- **Taproot** 체계에 대한 첫 번째 Taproot 출력(있는 경우).


트랜잭션이 두 개의 개별 출력에 하나의 `Opret` Commitment과 하나의 `Tapret` Commitment을 포함할 수 있다는 점에 유의하시기 바랍니다. Seal Definition의 결정론적 특성 덕분에 이 두 커미트먼트는 클라이언트 측에서 유효성이 검증된 두 개의 별개의 데이터 조각에 해당합니다.


### RGB의 분석 및 실용적인 선택


RGB를 시작할 때, 저희는 결정론적인 방식으로 트랜잭션에서 _커밋_을 어디에 어떻게 배치할지 결정하기 위해 이러한 모든 방법을 검토했습니다. 몇 가지 기준을 정의했습니다:




- 다양한 시나리오와의 호환성(예: Multisig, 라이트닝, 하드웨어 지갑 등);
- On-Chain 공간에 미치는 영향;
- 구현 및 유지 관리의 어려움;
- 기밀 유지 및 검열에 대한 저항.


| Method                                             | On-chain trace & size | Client-side size | Wallet Integration | Hardware Compatibility | Lightning Compatibility | Taproot Compatibility |
| -------------------------------------------------- | --------------------- | ---------------- | ------------------ | ---------------------- | ---------------------- | --------------------- |
| Keytweak (deterministic P2C)                      | 🟢                     | 🟡                 | 🔴                   | 🟠                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🟢 MuSig  |
| Sigtweak (deterministic S2C)                      | 🟢                     | 🟢                 | 🟠                   | 🔴                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🔴 MuSig  |
| Opret (OP_RETURN)                                 | 🔴                     | 🟢                 | 🟢                   | 🟠                     | 🔴 BOLT, 🟠 Bifrost     | -                     |
| Tapret Algorithm: top-left node                   | 🟠                     | 🔴                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Tapret Algorithm #4: any node + proof             | 🟢                     | 🟠                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Deterministic Commitment Scheme                               | Standard       | On-Chain Cost                                                                                                          | Proof Size on Client Side                                                                                       |
| ------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Keytweak (Deterministic P2C)                                  | LNPBP-1, 2     | 0 bytes                                                                                                                | 33 bytes (non-tweaked key)                                                                                       |
| Sigtweak (Deterministic S2C)                                  | WIP (LNPBP-39) | 0 bytes                                                                                                                | 0 bytes                                                                                                          |
| Opret (OP_RETURN)                                             | -              | 36 (v)bytes (additional TxOut)                                                                                         | 0 bytes                                                                                                          |
| Tapret Algorithm: top-left node                               | LNPBP-6        | 32 bytes in the witness (8 vbytes) for any n-of-m multisig and spending through script path                           | 0 bytes on scriptless scripts taproot ~270 bytes in a single script case, ~128 bytes if multiple scripts       |
| Tapret Algorithm #4: any node + uniqueness proof              | LNPBP-6        | 32 bytes in the witness (8 vbytes) for single script cases, 0 bytes in the witness in most other cases                | 0 bytes on scriptless scripts taproot, 65 bytes until the Taptree contains a dozen scripts                      |


| Layer                          | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| **Type**                       | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**               | **Tapret #4**            | **Keytweak**             | **Sigtweak**             | **Opret**                |
| Single-sig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | 0?                       | 0                        |
| MuSig (n-of-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | ? > 0                    | 0                        |
| Multi-sig 2-of-3               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~270                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 3-of-5               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~340                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 2-of-3 with timeouts | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                       | 65                       | 32                       | n/a                      | 0                        |


| Layer                            | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | Client-Side Cost (bytes) | Client-Side Cost (bytes) |
| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |
| **Type**                         | **Base**               | **Tapret #2**          | **Tapret #4**          | **Tapret #2**            | **Tapret #4**            |
| MuSig (n-of-n)                   | 16.5                   | 0                      | 0                      | 0                        | 0                        |
| FROST (n-of-m)                   | ?                      | 0                      | 0                      | 0                        | 0                        |
| Multi_a (n-of-m)                 | 1+16n+8m               | 8                      | 8                      | 33 * m                   | 65                       |
| Branch MuSig / Multi_a (n-of-m)  | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| With timeouts (n-of-m)           | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| Method                                    | Privacy & Scalability | Interoperability | Compatibility | Portability | Complexity |
| ----------------------------------------- | ---------------------- | ---------------- | ------------- | ----------- | ---------- |
| Keytweak (Deterministic P2C)              | 🟢                      | 🔴               | 🔴            | 🟡          | 🟡         |
| Sigtweak (Deterministic S2C)              | 🟢                      | 🔴               | 🔴            | 🟢          | 🔴         |
| Opret (OP_RETURN)                         | 🔴                      | 🟠               | 🔴            | 🟢          | 🟢         |
| Algo Tapret: Top-left node                | 🟠                      | 🟢               | 🟢            | 🔴          | 🟠         |
| Algo Tapret #4: Any node + proof          | 🟢                      | 🟢               | 🟢            | 🟠          | 🔴         |






연구 과정에서 Commitment 체계 중 어느 것도 현재 라이트닝 표준(Taproot, _muSig2_ 또는 추가 _commitment_ 지원을 사용하지 않음)과 완벽하게 호환되지 않는다는 것이 밝혀졌습니다. RGB 커미트먼트를 삽입할 수 있도록 Lightning의 채널 구조(*BiFrost*)를 수정하기 위한 노력이 진행 중입니다. 이는 트랜잭션 구조, 키, 채널 업데이트 서명 방식을 검토해야 하는 또 다른 영역입니다.


분석 결과, 실제로 다른 방법(키 조정, 서명 조정, 증인 조정 등)에서도 다른 형태의 합병증이 발생한다는 사실이 밝혀졌습니다:




- On-Chain 볼륨이 큰 경우입니다;
- 기존 Wallet 코드와 근본적으로 호환되지 않습니다;
- 비협조적인 Multisig에서는 솔루션을 실행할 수 없습니다.


RGB에서는 특히 두 가지 방법이 눈에 띕니다: *"트랜잭션 출력"으로 분류되며 프로토콜에서 사용하는 TxO2 모드와 호환되는 **Opret***와 ***Tapret***입니다.


### 멀티 프로토콜 커미트먼트 - MPC


이 섹션에서는 **RGB**이 결정론적 방식(`Opret` 또는 `Tapret`에 따라)을 통해 단일 Commitment(*Commitment*)에 기록된 여러 컨트랙트(또는 더 정확하게는 그 _전환 번들_)의 합산을 처리하는 방법을 살펴봅니다. 이를 위해 다양한 컨트랙트의 메르켈화 순서는 **MPC 트리**(_멀티 프로토콜 Commitment 트리_)라는 구조에서 이루어집니다. 이 섹션에서는 이 MPC 트리의 구조와 루트를 얻는 방법, 여러 콘트랙트가 동일한 트랜잭션을 비밀스럽고 명확하게 공유하는 방법에 대해 살펴보겠습니다.


Multi Protocol Commitment(MPC)는 두 가지 요구 사항을 충족하도록 설계되었습니다:




- Mpc::Commitment` Hash의 구성: 이것은 `Opret` 또는 `Tapret` 체계에 따라 Bitcoin Blockchain에 포함되며, 검증할 모든 상태 변경 사항을 반영해야 합니다;
- 단일 _약속_에 여러 컨트랙트를 동시에 저장하여 여러 자산 또는 RGB 컨트랙트에 대한 개별 업데이트를 단일 Bitcoin 트랜잭션으로 관리할 수 있습니다.


구체적으로 말하면, 각 _트랜지션 번들_은 특정 Contract에 속합니다. 이 모든 정보는 **MPC 트리**에 삽입되고, 그 루트(`mpc::Root`)가 다시 해시되어 `mpc::Commitment`가 됩니다. 선택된 결정론적 방식에 따라 Bitcoin 트랜잭션(_증인 트랜잭션_)에 배치되는 것이 바로 이 마지막 Hash입니다.


![RGB-Bitcoin](assets/en/042.webp)


#### MPC 루트 Hash


실제로 `Opret` 또는 `Tapret`에 기록된 On-Chain 값은 `mpc::Commitment`라고 합니다. 이것은 공식에 따라 [BIP-341](https://github.com/Bitcoin/BIPs/blob/master/BIP-0341.mediawiki)의 형태로 계산됩니다:


```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```


어디에:




- `mpc_tag`는 태그입니다: `urn:ubideco:mpc:Commitment#2024-01-31`, [RGB 태그 규칙]에 따라 선택됨(https://github.com/RGB-WG/RGB-core/blob/master/doc/Commitments.md);
- '깊이'(1바이트)는 *MPC 트리*의 깊이를 나타냅니다;
- 계수`(16비트, 리틀 엔디안)는 트리에서 각 Contract에 할당된 위치의 고유성을 높이는 데 사용되는 매개변수입니다;
- 엠피씨::루트`는 다음 섹션에서 설명하는 프로세스에 따라 계산된 *MPC 트리*의 루트입니다.


![RGB-Bitcoin](assets/en/044.webp)


#### MPC 트리 구성


이 MPC 트리를 구축하려면 각 Contract가 고유한 리프 위치에 해당하는지 확인해야 합니다. 다음과 같이 가정해 보겠습니다:




- c` 계약은 `i` = {0,1,..,C-1}에서 `i`로 인덱싱되어 포함됩니다;
- 각 Contract `c_i`에는 `ContractId(i) = c_i`라는 식별자가 있습니다.


그런 다음 각 Contract를 별도의 _잎_에 배치할 수 있도록 `2^d = w`, `w > C`가 되도록 너비 `w`와 깊이 `d`의 트리를 구성합니다. 트리에서 각 Contract의 위치 `pos(c_i)`는 다음에 의해 결정됩니다:


```txt
pos(c_i) = c_i mod (w - cofactor)
```


여기서 '계수'는 각 Contract에 대해 고유한 위치를 얻을 확률을 높이는 정수입니다. 실제로 구축은 반복적인 프로세스를 따릅니다:




- 최소 깊이에서 시작합니다(정확한 계약 수를 숨기기 위해 관례상 'd=3'으로 표시);
- 다양한 '계수'(최대 'w/2' 또는 성능상의 이유로 최대 500까지)를 시도합니다;
- 충돌 없이 모든 컨트랙트를 포지셔닝하지 못하면 `d`를 증가시키고 다시 시작합니다.


목표는 충돌 위험을 최소화하면서 너무 키가 큰 나무를 피하는 것입니다. 충돌 현상은 [기념일 패러독스](https://en.wikipedia.org/wiki/Birthday_problem)와 관련된 무작위 분포 로직을 따릅니다.


#### 사람이 거주하는 잎


계약 `i = {0,1,..,C-1}`에 대해 `C` 고유 포지션 `pos(c_i)`가 얻어지면 각 시트는 Hash 함수(*태그가 붙은 Hash*)로 채워집니다:


```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```


어디에:




- 머클 태그는 항상 RGB의 머클 규칙에 따라 `merkle_tag = urn:ubideco:merkle:node#2024-01-31`로 선택됩니다;
- 0x10`은 _컨트랙트 리프_를 식별합니다;
- `c_i`는 32바이트 Contract 식별자(Genesis Hash에서 파생됨)입니다;
- 번들아이디(c_i)`는 (*Transition Bundle*로 수집된) `c_i`에 상대적인 `상태 전환` 집합을 설명하는 32바이트 Hash입니다.


#### 무인 잎


Contract에 할당되지 않은 나머지 잎(즉, `w - C` 잎)은 "더미" 값(_엔트로피 잎_)으로 채워집니다:


```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```


어디에:




- 머클 태그는 항상 RGB의 머클 규칙에 따라 `merkle_tag = urn:ubideco:merkle:node#2024-01-31`로 선택됩니다;
- '0x11'은 _엔트로피 리프_를 나타냅니다;
- '엔트로피'는 트리를 만드는 사람이 선택한 64바이트의 임의의 값입니다;
- 'j'는 트리에서 이 잎의 위치(32비트 리틀 엔디안)입니다.


#### MPC 노드


'w' 잎(거주 여부)을 생성한 후 머켈라이제이션을 진행합니다. 모든 내부 노드는 다음과 같이 해시됩니다:


```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```


어디에:




- 머클 태그는 항상 RGB의 머클 규칙에 따라 `merkle_tag = urn:ubideco:merkle:node#2024-01-31`로 선택됩니다;
- b`는 _분지 계수_(8비트)입니다. 트리가 2진수이고 완전하기 때문에 대부분 `b=0x02`가 됩니다;
- d`는 트리에서 노드의 깊이입니다;
- 'w'는 트리 너비입니다(256비트 리틀 엔디안 바이너리);
- tH1`과 `tH2`는 위와 같이 이미 계산된 자식 노드(또는 리프)의 해시입니다.


이런 식으로 진행하면 루트 `mpc::Root`를 얻습니다. 그런 다음 위에서 설명한 대로 `mpc::Commitment`을 계산하여 On-Chain에 삽입하면 됩니다.


이를 설명하기 위해 `C=3`(3개의 컨트랙트)의 예를 들어보겠습니다. 이들의 위치는 `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`로 가정합니다. 다른 잎(위치 0, 1, 3, 5, 6)은 _엔트로피 잎_입니다. 아래 다이어그램은 루트에 대한 해시 시퀀스를 보여줍니다:




- 번들아이디(c_i)`를 나타내는 `BUNDLE_i`입니다;
- tH_MPC_LEAF(A)` 등으로 잎을 나타냅니다(일부는 컨트랙트, 일부는 엔트로피);
- 각 분기 `tH_MPC_BRANCH(...)`는 두 자식의 해시를 결합합니다.


최종 결과는 **mpc::Root**, 그 다음에는 `mpc::Commitment`이 됩니다.


![RGB-Bitcoin](assets/en/053.webp)


#### MPC 샤프트 점검


검증자가 `c_i` Contract(및 해당 `BundleId`)이 최종 `mpc::Commitment`에 포함되어 있는지 확인하고자 할 때, 머클 증명을 받기만 하면 됩니다. 이 증명은 리프(이 경우 `c_i`의 _계약 리프_)를 루트까지 추적하는 데 필요한 노드를 나타냅니다. 전체 *MPC 트리*를 공개할 필요는 없습니다. 이는 다른 컨트랙트의 기밀성을 보호합니다.


예제에서 `c_2` 검증자는 중간 Hash(`tH_MPC_LEAF(D)`), 두 개의 `tH_MPC_BRANCH(...)`, `pos(c_2)` 위치 증명 및 `계수` 값만 필요합니다. 그런 다음 로컬에서 루트를 재구성한 다음 `mpc::Commitment`을 다시 계산하고 이를 Bitcoin 트랜잭션(`Opret` 또는 `Tapret` 내)에 쓰여진 것과 비교할 수 있습니다.


![RGB-Bitcoin](assets/en/054.webp)


이 메커니즘은 이를 보장합니다:




- '_c_2'와 관련된 상태는 실제로 집계 정보 블록(클라이언트 측)에 포함됩니다;
- On-Chain _commitment_는 단일 MPC 루트를 가리키기 때문에 누구도 동일한 트랜잭션으로 대체 기록을 만들 수 없습니다.


#### MPC 구조 요약


Multi Protocol Commitment*(MPC)는 다른 참여자에 대한 약속의 고유성과 기밀성을 유지하면서 RGB이 여러 컨트랙트를 하나의 Bitcoin 트랜잭션으로 통합할 수 있도록 하는 원리입니다. 트리의 결정론적 구조 덕분에 각 Contract에는 고유한 위치가 할당되며, "더미" 잎(*엔트로피 잎*)의 존재는 거래에 참여하는 총 컨트랙트 수를 부분적으로 가립니다.


전체 Merkle Tree는 클라이언트에 저장되지 않습니다. 각 Contract에 대해 _머클 경로_를 generate로 생성하여 수신자에게 전송하면 수신자는 Commitment의 유효성을 검사할 수 있습니다. 경우에 따라 동일한 UTXO을 통과한 자산이 여러 개 있을 수 있습니다. 그런 다음 여러 개의 _머클 경로_를 소위 _멀티 프로토콜 Commitment 블록_으로 병합하여 너무 많은 데이터가 중복되는 것을 방지할 수 있습니다.


따라서 각각의 _머클 증명_은 특히 RGB에서 트리 깊이가 32를 초과하지 않기 때문에 가볍습니다. 더 많은 정보(단면, 엔트로피 등)를 보유하는 '머클 블록'이라는 개념도 있어 여러 가지 가지를 결합하거나 분리하는 데 유용합니다.


그래서 RGB을 완성하는 데 시간이 오래 걸렸습니다. 저희는 2019년부터 모든 것을 클라이언트 측에 두고 토큰을 순환시키는 off-chain이라는 전체적인 비전을 가지고 있었습니다. 하지만 다중 컨트랙트에 대한 샤딩, Merkle Tree의 구조, 충돌 처리 및 병합 증명 방법과 같은 세부 사항은 모두 반복이 필요했습니다.


### 앵커: 글로벌 어셈블리


커미트먼트(`Opret` 또는 `Tapret`)와 MPC(*Multi Protocol Commitment*)의 구축에 이어, RGB 프로토콜에서 **Anchor**이라는 개념을 Address에 추가해야 합니다. Anchor은 클라이언트 측에서 검증된 구조로, Bitcoin Commitment가 실제로 특정 계약 정보를 포함하고 있는지 확인하는 데 필요한 Elements을 한데 모은 것입니다. 즉, Anchor은 위에서 설명한 _약정_을 검증하는 데 필요한 모든 데이터를 요약합니다.


Anchor는 세 개의 정렬된 필드로 구성됩니다:




- `txid`
- 'MPC 증명'
- 추가 거래 증명 - ETP


이러한 각 필드는 기본 Bitcoin 트랜잭션을 재구성하거나 숨겨진 Commitment의 존재를 증명하는 등(특히 '타프렛'의 경우) 검증 프로세스에서 중요한 역할을 합니다.


#### txid


txid` 필드는 `Opret` 또는 `Tapret` Commitment을 포함하는 Bitcoin 트랜잭션의 32바이트 식별자에 해당합니다.


이론적으로는 일회용 씰의 논리에 따라 각 Witness Transaction을 가리키는 일련의 상태 전환을 추적하여 이 'txid'을 찾을 수 있습니다. 그러나 검증을 용이하고 빠르게 하기 위해 이 `txid`은 단순히 Anchor에 포함되어 있으므로 검증자가 전체 off-chain 기록을 거슬러 올라가지 않아도 됩니다.


#### MPC 증명


두 번째 필드인 'MPC 증명'은 이 특정 Contract(예: `c_i`)이 _멀티 프로토콜 커미트먼트_에 포함되어 있다는 증명을 나타냅니다. 의 조합입니다:




- mPC 트리에서 이 Contract의 위치인 `pos_i`입니다;
- 코팩터`, 위치 충돌을 해결하기 위해 정의된 값입니다;
- 머클 증명`, 즉 MPC 루트를 재구성하고 Contract 식별자와 그 `Transition Bundle`가 루트에 커밋되었는지 확인하는 데 사용되는 노드와 해시 집합입니다.


이 메커니즘은 이전 *MPC 트리* 구축 섹션에서 설명한 바 있으며, 각 Contract은 덕분에 고유한 잎을 얻게 됩니다:


```txt
pos(c_i) = c_i mod (w - cofactor)
```


그런 다음 결정론적 메르켈화 방식을 사용하여 모든 잎(컨트랙트 + 엔트로피)을 합산합니다. 결국 `MPC 증명`은 루트를 로컬에서 재구성하고 `mpc::Commitment`에 포함된 On-Chain과 비교할 수 있게 해줍니다.


#### 추가 거래 증명 - ETP


세 번째 필드인 **ETP**는 사용된 Commitment의 유형에 따라 다릅니다. Commitment가 '해석' 유형인 경우 추가 증명이 필요하지 않습니다. 유효성 검사기는 트랜잭션의 첫 번째 `OP_RETURN` 출력을 검사하고 거기서 바로 `mpc::Commitment`를 찾습니다.


**Commitment이 '탭렛' 유형인 경우 *추가 트랜잭션 증명 - ETP*라는 추가 증명을 제공해야 합니다.** 여기에는 다음이 포함됩니다:




- **Commitment**이 내장된 Taproot 출력의 내부 공개키(`P`)입니다;
- 스크립트 트리에서 이 스크립트의 정확한 위치를 증명하기 위해 '스크립트 경로 지출'의 파트너 노드(탭렛 *Commitment*가 스크립트에 삽입된 경우)를 Taproot 트리에 추가합니다:
 - 오른쪽 브랜치에 `Tapret` *Commitment*이 있으면 왼쪽 노드(예: `tHABC`)가 표시됩니다,
 - 왼쪽에 '탭렛' *Commitment*가 있는 경우, 오른쪽에 다른 *Commitment*가 없음을 증명하기 위해 2개의 노드(예: `tHAB`, `tHC`)를 공개해야 합니다.
- 'Nonce'를 사용하여 최적의 구성을 '채굴'하여 *Commitment*을 트리 오른쪽에 배치할 수 있습니다(증명 최적화).


이 추가 증명이 필수적인 이유는 `Opret`와 달리 `Tapret` Commitment는 Taproot 스크립트의 구조에 통합되어 있기 때문에 *Commitment*의 위치를 정확하게 검증하기 위해 Taproot 트리의 일부를 공개해야 하기 때문입니다.


![RGB-Bitcoin](assets/en/045.webp)


따라서 **앵커**는 Bitcoin의 맥락에서 Commitment을 검증하는 데 필요한 모든 정보를 RGB에 캡슐화합니다. 이들은 관련 트랜잭션(`txid`)과 Contract 포지셔닝 증명(`MPC 증명`)을 모두 나타내며, `Tapret`의 경우 추가 증명(`ETP`)을 관리합니다. 이러한 방식으로 Anchor은 동일한 트랜잭션이 다른 계약 데이터에 대해 재해석될 수 없도록 함으로써 off-chain 상태의 무결성과 고유성을 보호합니다.


### 결론


이 장에서는 이러한 내용을 다루었습니다:




- Bitcoin에서 일회용 씰 개념을 적용하는 방법(특히 _아웃포인트_를 통해);
- 트랜잭션에 _커밋_을 결정론적으로 삽입하는 다양한 방법(서명 조정, 키 조정, 증인 조정, OP_RETURN, Taproot/Tapret)을 제공합니다;
- RGB이 Tapret 약속에 집중하는 이유입니다;
- 다중 프로토콜 커미트먼트_를 통한 다중 Contract 관리, 특정 지점을 증명하고자 할 때 전체 상태나 다른 컨트랙트를 노출하고 싶지 않을 때 필수적입니다;
- 또한 모든 것을 하나의 패키지로 통합하는 _앵커_의 역할(트랜잭션 txid, Merkle Tree 증명 및 Taproot 증명)도 살펴봤습니다.


실제로 기술 구현은 여러 개의 전용 Rust _크레이트_(_client_side_validation_, _commit-verify_, _bp_core_ 등)로 나뉩니다. 기본 개념은 여기에 있습니다:


![RGB-Bitcoin](assets/en/046.webp)


다음 장에서는 RGB의 순수한 off-chain 구성 요소, 즉 Contract 로직에 대해 살펴보겠습니다. 부분적으로 복제된 '유한 상태 머신'으로 구성된 RGB 컨트랙트가 데이터의 기밀성을 유지하면서 Bitcoin 스크립트보다 훨씬 높은 표현력을 달성하는 방법을 살펴볼 것입니다.


## 스마트 컨트랙트와 그 상태 소개


<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>


:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::


이번 장과 다음 장에서는 RGB 환경 내에서 **Smart contract**의 개념을 살펴보고 이러한 컨트랙트가 *상태*를 정의하고 발전시킬 수 있는 다양한 방법을 살펴보겠습니다. 일회용 씰의 정렬된 시퀀스를 사용하는 RGB 아키텍처를 통해 중앙화된 레지스트리를 거치지 않고 확장 가능한 방식으로 다양한 유형의 ***Contract 작업***을 실행할 수 있는 이유를 살펴볼 것입니다. 또한 Contract State의 진화를 구성하는 ***Business Logic***의 근본적인 역할에 대해서도 살펴볼 것입니다.


### 스마트 컨트랙트와 디지털 무기명 권리


RGB의 목표는 Bitcoin에서 스마트 계약을 구현하기 위한 인프라를 제공하는 것입니다. "Smart contract"는 조항을 시행하기 위한 사람의 개입 없이 자동으로 컴퓨터로 시행되는 여러 당사자 간의 계약을 의미합니다. 즉, Contract의 법률은 신뢰할 수 있는 제3자가 아닌 소프트웨어에 의해 시행됩니다.


이러한 자동화는 탈중앙화라는 문제를 제기합니다. 어떻게 중앙화된 레지스트리(예: 중앙 플랫폼 또는 데이터베이스)에서 벗어나 Ownership과 Contract의 성능을 관리할 수 있을까요? RGB에서 채택한 원래 아이디어는 "무기명 상품"으로 알려진 Ownership의 모드로 돌아가는 것입니다. 역사적으로 특정 증권(채권, 주식 등)은 무기명 형태로 발행되어 문서를 물리적으로 소유한 사람이 자신의 권리를 행사할 수 있었습니다.


![RGB-Bitcoin](assets/en/055.webp)


RGB은 이 개념을 디지털 세계에 적용하여 권리(및 의무)가 조작된 데이터에 캡슐화되고, 이 데이터의 상태는 참여자 스스로가 검증합니다. 이를 통해 선험적으로 공공 등록부를 기반으로 하는 다른 접근 방식보다 훨씬 더 높은 수준의 기밀성과 독립성을 보장할 수 있습니다.


### Smart contract RGB 상태 소개


RGB의 Smart contract은 다음과 같이 정의되는 상태 머신으로 볼 수 있습니다:




- **상태**, 즉 Contract의 현재 구성을 반영하는 정보 집합입니다;
- 어떤 조건에서 누구에 의해 상태를 수정할 수 있는지 설명하는 **Business Logic**(규칙 집합)입니다.


![RGB-Bitcoin](assets/en/056.webp)


이러한 계약은 단순한 토큰 전송에만 국한되지 않는다는 점을 이해하는 것이 중요합니다. 토큰, 주식, 채권 등 전통적인 자산부터 사용 권한, 상업적 조건 등 보다 복잡한 메커니즘에 이르기까지 다양한 애플리케이션을 구현할 수 있습니다. 모든 사람이 Contract 코드에 액세스하고 실행할 수 있는 다른 블록체인과 달리, RGB의 접근 방식은 참가자("***Contract 참가자***")에게 Contract에 대한 액세스 및 지식을 구획화합니다. 여러 역할이 있습니다:




- Contract의 Genesis 및 초기 변수를 정의하는 **Contract의 발행자** 또는 생성자;
- 권리**(*Ownership*)** 또는 기타 집행 권한이 있는 당사자;
- **옵저버**, 특정 정보를 볼 수 있지만 수정을 트리거할 수 없는 잠재적 제한이 있는 사람입니다.


이러한 역할 분리는 권한이 있는 사람만 계약 상태와 상호작용할 수 있도록 함으로써 검열 저항에 기여합니다. 또한 RGB는 수평적으로 확장할 수 있는 기능을 제공합니다. 대부분의 검증은 Blockchain 외부에서 이루어지고 암호화 앵커(*커밋*)만이 Bitcoin에 새겨집니다.


### 상태 및 Business Logic의 RGB


실용적인 관점에서 볼 때 Contract의 **Business Logic**은 규칙과 스크립트의 형태를 취하며, RGB에서 **Schema**라고 부르는 것으로 정의됩니다. Schema는 인코딩합니다:




- 상태 구조(어떤 필드가 공개되어 있나요? 어떤 필드가 어떤 당사자가 소유하고 있나요?
- 유효성 조건(상태 업데이트를 승인하기 전에 확인해야 하는 사항);
- 권한(누가 *State Transition*을 시작할 수 있나요? 누가 참관만 할 수 있나요?).


동시에 **Contract State**는 종종 두 가지 구성 요소로 나뉩니다:




- A **Global State**: 공개 부분, 모든 사람이 잠재적으로 관찰할 수 있습니다(구성에 따라 다름);
- **소유 상태**: Contract 로직에 참조된 UTXO를 통해 소유자에게 특별히 할당된 개인 부품입니다.


다음 장에서 살펴보겠지만, 모든 상태 업데이트(*Contract Operation*)는 (`Opret` 또는 `Tapret`을 통해) Bitcoin _commitment_에 도킹하고 *Business Logic* 스크립트를 준수해야 유효한 것으로 간주됩니다.


### Contract 작전: 국가의 탄생과 진화


RGB 세계에서 ***Contract Operation***는 Contract을 **이전 상태**에서 **새 상태**로 변경하는 모든 이벤트입니다. 이러한 작업은 다음 로직을 따릅니다:




- Contract의 현재 상태에 주목합니다;
- 규칙 또는 연산(***State Transition***, 첫 번째 상태인 경우 ***Genesis***, 다시 트리거할 공개 *Valency*가 있는 경우 ***State Extension***)을 적용합니다;
- Blockchain에서 새로운 _커밋_을 통해 수정 사항을 Anchor로 변경하여 하나의 _일회용 씰_을 닫고 다른 씰을 생성합니다;
- 관련 권리 보유자는 전환이 *Schema*을 준수하고 관련 Bitcoin 트랜잭션이 On-Chain에 등록되어 있는지 로컬(*클라이언트 측*)에서 확인합니다.


![RGB-Bitcoin](assets/en/057.webp)


최종 결과는 이제 다른 상태를 가진 업데이트된 Contract입니다. 이 전환은 Blockchain에 작은 암호화 지문(_commitment_)만 기록되기 때문에 전체 Bitcoin 네트워크가 세부 사항에 신경 쓸 필요가 없습니다. 일회용 씰의 시퀀스는 Double-spending 또는 스테이트의 이중 사용을 방지합니다.


### 운영 체인: Genesis에서 터미널 상태까지


이를 설명하기 위해 RGB Smart contract은 첫 번째 상태인 **Genesis**으로 시작합니다. 그 후 다양한 Contract 오퍼레이션이 서로 뒤따르면서 DAG(*Directed Acyclic Graph*)의 오퍼레이션을 형성합니다:




- 각 전환은 이전 상태(또는 수렴 전환의 경우 여러 상태)를 기반으로 합니다;
- 시간 순서는 Bitcoin Anchor에 각 전환을 포함함으로써 보장되며, 타임스탬프가 찍히고 Proof-of-Work의 합의에 따라 변경할 수 없습니다;
- 더 이상 작업이 진행되지 않으면 **단말 상태**에 도달하게 되는데, 이는 Contract의 가장 최근의 완전한 상태입니다.


![RGB-Bitcoin](assets/en/012.webp)


단순한 선형 체인 대신 이 DAG 토폴로지는 서로 모순되지 않는 한 Contract의 여러 부분이 병렬로 진화할 수 있는 가능성을 반영합니다. 그런 다음 RGB은 관련된 각 참여자에 대한 *클라이언트 측* 검증을 통해 불일치를 방지합니다.


### 요약


RGB의 스마트 컨트랙트는 탈중앙화되었지만 타임 스탬핑과 거래 순서를 보장하기 위해 Bitcoin에 고정된 디지털 무기명 상품 모델을 도입합니다. 이러한 계약의 자동화된 실행은 다음을 기반으로 합니다:




- Contract State의 현재 구성(권한, 잔액, 변수 등)을 나타내는 **Contract**입니다;
- 어떤 전환이 허용되고 어떻게 검증되어야 하는지를 정의하는 **Business Logic**(*Schema*)입니다;
- Contract 트랜잭션에 고정된 커밋 덕분에 이 상태를 단계적으로 업데이트하는 **Bitcoin 작업**이 있습니다.


다음 장에서는 off-chain 수준에서 이러한 ***상태***와 ***상태 전환***의 구체적인 표현과 Bitcoin에 내장된 UTXO 및 일회용 씰과의 관계에 대해 더 자세히 살펴보도록 하겠습니다. Client-side Validation을 기반으로 하는 RGB의 내부 메커니즘이 어떻게 데이터 기밀성을 유지하면서 스마트 컨트랙트의 일관성을 유지하는지를 확인할 수 있는 기회가 될 것입니다.


## RGB Contract 작업


<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>


:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::


이 장에서는 스마트 콘트랙트와 상태 트랜지션의 작동 방식을 RGB 프로토콜 내에서 다시 살펴볼 것입니다. 또한 여러 참여자가 협력하여 자산의 Ownership를 전송하는 방법을 이해하는 것이 목표입니다.


### 상태 전환과 그 메커니즘


일반적인 원칙은 여전히 상태 데이터를 소유자가 보유하고 수신자가 검증하는 Client-side Validation의 원칙입니다. 그러나 RGB의 특이점은 수신자인 Bob이 수신 자산을 실질적으로 제어하기 위해 자신의 UTXO 중 하나에 대한 숨겨진 참조를 통해 특정 정보를 Alice에 요청하여 Contract 데이터에 통합한다는 사실에 있습니다.


State Transition*(Contract의 기본 ***RGB 작업*** 중 하나)의 프로세스를 설명하기 위해 Alice과 Bob 간의 자산 이전을 단계별로 예로 들어보겠습니다:


**초기 상황:**


Alice에는 로컬로 검증된 데이터(*클라이언트 측*)의 ***Stash RGB***가 있습니다. 이 Stash은 Bitcoin의 UTXO 중 하나를 참조합니다. 즉, 이 데이터의 _봉인 정의_는 Alice에 속하는 UTXO을 가리킵니다. 이 아이디어는 그녀가 자산에 연결된 특정 디지털 권리(예: RGB 토큰)를 Bob로 전송할 수 있도록 하는 것입니다.


![RGB-Bitcoin](assets/en/058.webp)


**Bob에는 UTXO도 있습니다:**


반면에 Bob은 Alice와 직접 연결되지 않은 자신의 UTXO을 하나 이상 가지고 있습니다. Bob에 UTXO이 없는 경우에도 *Witness Transaction* 자체를 사용하여 그에게 전송할 수 있습니다. 이 트랜잭션의 출력에는 Commitment(_commitment_)가 포함되며 새로운 Contract의 Ownership을 암묵적으로 Bob과 연결합니다.


![RGB-Bitcoin](assets/en/059.webp)


**새 부동산 건설(*새 상태*):**


Bob은 ***Invoice***(이후 장에서 Invoice 구성에 대해 자세히 설명하겠습니다) 형식으로 인코딩된 Alice 정보를 전송하여 Contract의 규칙을 따르는 새 상태를 생성하도록 요청합니다. 이 스테이트에는 Bob의 UTXO 중 하나를 가리키는 새로운 *Seal Definition*이 포함됩니다. 이런 식으로 Bob은 이 새 스테이트에 정의된 자산 중 Ownership, 예를 들어 일정량의 RGB 토큰을 받게 됩니다.


![RGB-Bitcoin](assets/en/060.webp)


**샘플 트랜잭션 준비:**


그런 다음 Alice은 이전 Seal(자신을 소유자로 합법화한 트랜잭션)에서 참조한 UTXO을 소비하는 Bitcoin 트랜잭션을 생성합니다. 이 트랜잭션의 출력에서 *Commitment*(`Opret` 또는 `Tapret`을 통해)가 새로운 RGB 상태인 Anchor에 삽입됩니다. Opret` 또는 `Tapret` 커미트먼트는 (이전 장에서 살펴본 것처럼) *MPC 트리*에서 파생되며, 이는 여러 컨트랙트의 여러 트랜지션을 통합할 수 있습니다.


**Consignment**를 Bob으로 전송:


트랜잭션을 브로드캐스트하기 전에 Alice는 필요한 모든 *클라이언트 측* 데이터(자신의 *Stash*)와 Bob에게 유리한 새로운 상태 정보가 포함된 ***Consignment***를 Bob에게 전송합니다. 이 시점에서 Bob은 RGB 합의 규칙을 적용합니다:




- 자산의 Ownership을 부여하는 새 상태를 포함하여 *Consignment*에 포함된 모든 RGB 데이터의 유효성을 검사합니다;
- Consignment에 포함된 **앵커**에 의존하여 증인 거래의 연대기를 확인하고(Genesis부터 가장 최근 전환까지) Blockchain의 해당 커미트먼트를 검증합니다.


**전환 완료:**


Bob가 만족하면 승인할 수 있습니다(예: *Consignment*에 서명). 그러면 Alice는 준비된 샘플 트랜잭션을 브로드캐스트할 수 있습니다. 확인이 완료되면 Alice가 보유하고 있던 Seal이 종료되고 Bob가 Ownership을 공식화합니다. 그런 다음 Bitcoin에서와 동일한 메커니즘에 따라 UTXO이 소비되어 Alice가 더 이상 재사용할 수 없음을 증명하는 Anti-Double-spending 보안이 이루어집니다.


![RGB-Bitcoin](assets/en/061.webp)


이제 새 상태는 Bob의 UTXO을 참조하여 Bob이 이전에 Alice가 보유했던 Ownership을 갖게 됩니다. RGB 데이터가 고정된 Bitcoin 출력은 Ownership의 전송에 대한 취소할 수 없는 증거가 됩니다.


두 개의 Contract 연산(**Genesis** 다음 ***State Transition***)으로 구성된 최소 DAG(*Directed Acyclic Graph*)의 예는 RGB 상태(*클라이언트 측* Layer, 빨간색)가 Bitcoin Blockchain(*Commitment* Layer, 오렌지색)에 어떻게 연결되는지 보여줄 수 있습니다.


![RGB-Bitcoin](assets/en/062.webp)


Genesis이 Seal(*Seal Definition*)을 정의한 다음 *State Transition*이 이 Seal을 닫아 다른 UTXO에 새로 생성하는 것을 보여줍니다.


이러한 맥락에서 용어에 대한 몇 가지 알림을 알려드립니다:




- **Assignment**는 다음을 결합합니다:
    - A ***Seal Definition***(UTXO를 가리킴);
- **소유 상태**, 즉 Ownership에 연결된 데이터(예: 전송된 토큰 수량).
- **Global State**은 Contract의 일반적인 속성을 통합하여 모든 사람이 볼 수 있으며, 진화의 글로벌 일관성을 보장합니다.


*이전 장에서 설명한* **상태 전환**은 Contract Operation의 주요 형태입니다. 하나 이상의 이전 상태(Genesis 또는 다른 State Transition에서)를 참조하여 새 상태로 업데이트합니다.


![RGB-Bitcoin](assets/en/063.webp)


이 다이어그램은 *상태 Transition Bundle*에서 단일 샘플 트랜잭션으로 여러 개의 씰을 닫으면서 동시에 새로운 씰을 여는 방법을 보여줍니다. 실제로 RGB 프로토콜의 흥미로운 특징은 확장 기능입니다. 여러 트랜지션을 Transition Bundle로 집계할 수 있으며, 각 집계는 *MPC 트리*(고유 번들 식별자)의 개별 리프와 연결됩니다. Deterministic Bitcoin Commitment*(DBC) 메커니즘 덕분에 전체 메시지가 `Tapret` 또는 `Opret` 출력에 삽입되는 동시에 이전 봉인을 닫고 새 봉인을 정의할 수도 있습니다. Anchor`은 Blockchain에 저장된 Commitment과 Client-side Validation 구조(*클라이언트 측*) 사이의 직접 연결 고리 역할을 합니다.


다음 장에서는 State Transition를 구축하고 검증하는 데 관련된 모든 구성 요소와 프로세스에 대해 살펴보겠습니다. 이러한 Elements의 대부분은 **RGB 코어 라이브러리**에서 구현된 RGB 컨센서스의 일부입니다.


### Transition Bundle


RGB에서는 동일한 Contract에 속하는 서로 다른 상태 트랜지션을 묶을 수 있습니다(즉, Genesis **OpId**에서 파생된 동일한 **ContractId**를 공유하는 경우). 가장 간단한 경우, 위 예시의 Alice과 Bob 사이처럼 **Transition Bundle**에는 하나의 트랜지션만 포함됩니다. 하지만 멀티플레이어 작업(코인조인, 라이트닝 채널 오픈 등)을 지원하면 여러 사용자가 하나의 번들에 상태 트랜지션을 결합할 수 있습니다.


일단 수집되면 이러한 트랜지션은 단일 Bitcoin 트랜잭션에 (MPC + DBC 메커니즘에 의해) 고정됩니다:




- 각 State Transition은 해시되어 Transition Bundle으로 그룹화됩니다;
- Transition Bundle는 그 자체로 해시되어 이 Contract(번들아이디)에 해당하는 MPC 트리 리프에 삽입됩니다;
- MPC 트리는 최종적으로 Witness Transaction의 `Opret` 또는 `Tapret`을 통해 결합되어 소비된 봉인을 닫고 새로운 봉인을 정의합니다.


기술적으로 말하자면, MPC 시트에 삽입된 **BundleId**는 번들의 *InputMap* 필드에 엄격한 직렬화를 적용한 태그가 붙은 Hash에서 얻습니다:


```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```


예를 들어 `bundle_tag = urn:lnp-bp:RGB:bundle#2024-02-03`입니다.


입력맵은 샘플 트랜잭션의 각 입력 'i'에 대해 해당 State Transition의 **OpId**에 대한 참조를 나열하는 데이터 구조입니다. 예를 들어


```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|

MapElement1                MapElement2                       MapElementN
```




- 'N'은 트랜잭션에서 `OpId`를 참조하는 총 항목 수입니다;
- opId(input_j)`는 번들에 존재하는 상태 전환 중 하나의 연산 식별자입니다.


각 항목을 한 번만 순서대로 참조함으로써 동일한 Seal이 두 번의 동시 상태 전환에 두 번 소비되는 것을 방지합니다.


### 상태 생성 및 활성 상태


따라서 상태 전환은 자산의 Ownership를 한 사람에서 다른 사람으로 이전하는 데 사용할 수 있습니다. 그러나 RGB 프로토콜에서 가능한 오퍼레이션은 이 두 가지뿐이 아닙니다. 이 프로토콜은 세 가지 **Contract 오퍼레이션**을 정의합니다:




- **State Transition**;
- **Genesis**;
- State **Extension**.


이 중 **Genesis**과 **State Extension**은 상태를 즉시 닫지 않고 새로운 상태를 생성하기 때문에 "*상태 생성 작업*"이라고도 합니다. 이것은 매우 중요한 포인트입니다: **Genesis** 및 **State Extension**은 Seal를 닫는 작업을 포함하지 않습니다. 오히려 새로운 Seal를 정의하고, 그 다음 후속 **State Transition**가 사용해야만 Blockchain 기록에서 진정한 유효성을 검사할 수 있습니다.


![RGB-Bitcoin](assets/en/064.webp)


Contract의 **활성 상태**는 종종 Genesis부터 시작하여 Bitcoin Blockchain의 모든 앵커를 따르는 트랜잭션의 기록(DAG)에서 발생하는 최신 상태 집합으로 정의됩니다. 이미 사용되지 않는 오래된 상태(즉, 사용된 UTXO에 연결된 상태)는 더 이상 활성 상태로 간주되지 않지만 히스토리의 일관성을 확인하는 데 필수적인 요소로 남아 있습니다.


### Genesis


Genesis은 모든 RGB Contract의 시작점입니다. Contract 발급자가 생성하며 **Schema**에 따라 초기 파라미터를 정의합니다. 예를 들어 RGB token의 경우 Genesis에서 지정할 수 있습니다:




- 원래 생성된 토큰의 수와 소유자입니다;
- 가능한 총 발행 한도;
- 재발급 규정 및 자격이 있는 참가자.


Contract의 첫 번째 트랜잭션인 Genesis는 이전 상태를 참조하지 않으며, Seal을 청산하지도 않습니다. 그러나 기록에 나타나고 유효성을 확인하려면 첫 번째 State Transition(발행자 자체에 대한 스캔/자동 지출 거래 또는 사용자에 대한 초기 배포)에 의해 Genesis가 **소비**(종료)되어야 합니다.


### State Extension


**상태 확장**은 스마트 컨트랙트를 위한 독창적인 기능을 제공합니다. 이를 통해 Contract 정의에 규정된 특정 디지털 권한(*밸런시*)을 Seal을 즉시 종료하지 않고도 Redeem으로 전환할 수 있습니다. 이는 대부분 다음과 관련된 문제입니다:




- token 문제 배포;
- 자산 스왑 메커니즘;
- 조건부 재발급(다른 자산의 파기 등이 포함될 수 있음).


엄밀히 말하면 State Extension은 이전에 정의된 *Valency*(예: Genesis 또는 다른 State Transition에서)에 해당하는 *Redeem*(특정 유형의 RGB 입력)을 참조합니다. 이는 혜택을 받는 사람이나 조건이 사용할 수 있는 새로운 Seal를 정의합니다. 이 Seal가 효력을 발휘하려면 후속 State Transition가 이를 사용해야 합니다.


![RGB-Bitcoin](assets/en/065.webp)


예를 들어, Genesis은 발행권(*Valency*)을 생성합니다. 이 권한은 권한 있는 행위자가 행사할 수 있으며, 권한 있는 행위자는 State Extension을 작성합니다:




- Valency(Redeem)를 의미합니다;
- UTXO을 가리키는 새 *Assignment*(새 *Owned State* 데이터)를 생성합니다;
- 이 새로운 UTXO의 소유자가 발행하는 향후 State Transition가 실제로 새로 발행된 토큰을 전송하거나 배포합니다.


### Contract Operation의 구성 요소


이제 RGB의 **Contract Operation**을 구성하는 각 Elements에 대해 자세히 살펴보겠습니다. Contract Operation은 Contract의 상태를 수정하는 작업으로, 클라이언트 측에서 정당한 수신자에 의해 결정론적 방식으로 유효성을 검사합니다. 특히 Contract Operation이 한편으로는 Contract의 **이전 상태**를, 다른 한편으로는 **새 상태**의 정의를 어떻게 고려하는지 살펴볼 것입니다.


```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |

+---------------------------------------------------------------------------------------------------------------------+
```


위의 다이어그램을 보면 Contract Operation에는 **새 상태**를 참조하는 Elements와 업데이트된 **오래 상태**를 참조하는 다른 Elements가 포함되어 있는 것을 볼 수 있습니다.


새 상태**의** Elements은 다음과 같습니다:




- **과제**가 정의되어 있습니다:
- **Seal Definition**;
- Owned **State**.
- 수정하거나 보강할 수 있는 **Global State**;
- **Valencies**, 아마도 State Transition 또는 Genesis에 정의되어 있을 것입니다.


이전 상태는 **이전 상태**를 통해 참조됩니다:




- 입력**, 이전 상태 전환의 *할당*을 가리킵니다(Genesis에는 없음);
- **리뎀스**는 이전에 정의된 유효성을 참조합니다(상태 확장에서만).


또한 Contract Operation에는 작업과 관련된 보다 일반적인 필드가 포함되어 있습니다:




- `ffv`(* 빨리 감기 버전*): gW-851 버전을 나타내는 2바이트 정수입니다;
- 트랜지션 타입` 또는 `익스텐션 타입`: gW-852에 따라 트랜지션 또는 확장 유형을 지정하는 16비트 정수입니다;
- `ContractId`: gW-853 Genesis의 *OpId*를 참조하는 32바이트 숫자. 트랜지션 및 확장에는 포함되지만 Genesis에는 포함되지 않습니다;
- schemaId: Genesis에만 존재하며, Contract의 구조(*Schema*)를 나타내는 32바이트 Hash입니다;
- `Testnet`: Testnet 또는 Mainnet 네트워크에 있는지 여부를 나타내는 부울입니다. Genesis만 해당;
- `altlayers1`: Bitcoin 외에 Anchor 데이터에 사용되는 대체 Layer(Sidechain 또는 기타)을 식별하는 변수입니다. Genesis에만 존재합니다;
- '메타데이터': 임시 정보를 저장할 수 있는 필드로, 복잡한 Contract의 유효성을 검사하는 데 유용하지만 최종 상태 기록에 기록되어서는 안 되는 필드입니다.


마지막으로, 이러한 모든 필드는 맞춤형 해싱 프로세스를 통해 압축되어 고유한 지문인 'OpId'를 생성합니다. 이 'OpId'는 Transition Bundle에 통합되어 프로토콜 내에서 인증 및 검증될 수 있습니다.


따라서 각 *Contract Operation*는 'OpId'라는 32바이트 Hash로 식별됩니다. 이 Hash는 연산을 구성하는 모든 Elements의 SHA256 Hash에 의해 계산됩니다. 즉, 각 *Contract Operation*에는 자체 암호화 Commitment이 있으며, 여기에는 작업의 진위성과 일관성을 확인하는 데 필요한 모든 데이터가 포함됩니다.


그런 다음 RGB Contract은 (Genesis 이전 연산이 없으므로) Genesis `OpId`에서 파생된 `ContractId`로 식별됩니다. 구체적으로 설명하자면, Genesis `OpId`를 가져와서 바이트 순서를 뒤집고 Base58 인코딩을 적용합니다. 이 인코딩은 `ContractId`를 더 쉽게 처리하고 인식할 수 있게 해줍니다.

### 상태 업데이트 방법 및 규칙


**Contract State**은 RGB 프로토콜이 주어진 Contract에 대해 추적해야 하는 정보 집합을 나타냅니다. 다음으로 구성됩니다:




- **단일 Global State**: 모든 사람이 볼 수 있는 Contract의 공개적이고 글로벌한 부분입니다;
- 하나 이상의 **소유 상태**: 각 Owned State은 고유한 Seal(따라서 Bitcoin의 UTXO)과 연결됩니다. 구분이 이루어집니다:
- **공공** 소유 국가,
- **개인** 소유 상태.


![RGB-Bitcoin](assets/en/066.webp)


Global State*은 *Contract Operation*에 단일 블록으로 직접 포함되어 있습니다. 소유 상태*는 *Seal Definition*과 함께 각 *Assignment*에 정의되어 있습니다.


RGB의 주요 특징은 Global State 및 소유 상태가 수정되는 방식입니다. 일반적으로 두 가지 유형의 동작이 있습니다:




- **변경 가능**: 상태 요소가 변경 가능한 것으로 설명되면 새로운 작업이 있을 때마다 이전 상태를 새 상태로 대체합니다. 그러면 이전 데이터는 더 이상 사용되지 않는 것으로 간주됩니다;
- **누적**: 상태 요소가 누적되는 것으로 정의된 경우, 새로운 작업을 수행할 때마다 이전 상태를 덮어쓰지 않고 새 정보를 추가합니다. 그 결과 일종의 누적 히스토리가 생성됩니다.


Contract에서 상태 요소가 변경 가능 또는 누적으로 정의되지 않은 경우 이 요소는 후속 작업에서 비어 있는 상태로 유지됩니다(즉, 이 필드에 대한 새 버전이 없습니다). 상태(전역 또는 소유)가 변경 가능한지, 누적되는지 또는 고정되는지를 결정하는 것은 Contract Schema(즉, 코딩된 Business Logic)입니다. Genesis가 정의되면 이러한 속성은 Contract 자체에서 허용하는 경우에만 수정할 수 있습니다(예: 특정 State Extension을 통해).


아래 표는 각 유형의 Contract Operation이 Global State 및 Owned State을 어떻게 조작할 수 있는지(또는 조작하지 않을 수 있는지) 보여줍니다:


|                              | Genesis | State Extension | State Transition |
| ---------------------------- |:-----: |:-------------: |:--------------: |
| **Addition of Global State** |    +    |        -        |        +         |
| **Mutation of Global State** |   n/a   |        -        |        +         |
| **Addition of Owned State**  |    +    |        -        |        +         |
| **Mutation of Owned State**  |   n/a   |       No        |        +         |
| **Addition of Valencies**    |    +    |        +        |        +         |


**`+`**: Contract의 Schema이 허용하는 경우 가능한 작업입니다.


**`-`**: 작업은 후속 State Transition에서 확인해야 합니다(State Extension만으로는 Single-Use Seal를 닫을 수 없음).


또한 각 데이터 유형의 시간적 범위와 업데이트 권한은 다음 표에서 구분할 수 있습니다:


|                        | Metadata                                | Global State                                     | Owned State                                                                                              |
| ---------------------- | --------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **Scope**              | Defined for a single Contract Operation | Defined globally for the contract                | Defined for each seal (*Assignment*)                                                                     |
| **Who can update it?** | Non-updatable (ephemeral data)          | Operation issued by actors (issuer, etc.)        | Depends on the legitimate holder who owns the seal (the one who can spend it in a following transaction) |
| **Temporal Scope**     | Only for the current operation          | State is established at the end of the operation | State is defined before the operation (by the *Seal Definition* of the previous operation)               |


### Global State


Global State는 종종 "아무도 소유하지 않고 모두가 아는" 것으로 묘사됩니다. 여기에는 공개적으로 볼 수 있는 Contract에 대한 일반적인 정보가 포함되어 있습니다. 예를 들어, token을 발급하는 Contract에는 다음과 같은 내용이 포함될 수 있습니다:




- 티커(token의 기호적 약어): '티커';
- token의 전체 이름입니다: 이름`;
- 정밀도(소수점 이하 자릿수): 정밀도: '정밀도';
- 초기 오퍼(및/또는 최대 token 한도): 발행된 공급량`;
- 발행 날짜: `생성됨`;
- 법률 데이터 또는 기타 공개 정보: '데이터'.


이 Global State은 퍼블릭 리소스(웹사이트, IPFS, 노스트르, 토렌트 등)에 배치하여 커뮤니티에 배포할 수 있습니다. 또한 경제적 인센티브(토큰을 보유하고 전송할 필요성 등)로 인해 Contract 사용자는 자연스럽게 이 데이터를 스스로 유지하고 전파하도록 유도할 수 있습니다.


### 과제


*Assignment*은 정의를 위한 기본 구조입니다:




- Seal(*Seal Definition*)는 특정 UTXO을 가리킵니다;
- *Owned State*, 즉 이 Seal과 관련된 속성 또는 데이터입니다.


**Assignment**은 Bitcoin 트랜잭션 출력과 유사하다고 볼 수 있지만 유연성이 더 뛰어납니다. 여기에는 자산 이전 논리가 있습니다: **Assignment**은 특정 유형의 자산 또는 권리(`AssignmentType`)를 Seal와 연결합니다. 이 Seal에 연결된 UTXO의 개인키를 소유한 사람(또는 이 UTXO을 사용할 수 있는 사람)은 이 **Owned State**의 소유자로 간주됩니다.


RGB의 가장 큰 강점 중 하나는 *Seal Definition* 및 *Owned State* 필드를 마음대로 *표시*하거나 숨길 수 있다는 것입니다(*은폐*). 이는 기밀성과 선택성의 강력한 조합을 제공합니다. 예를 들어, 모든 데이터를 공개하지 않고도 전환이 유효하다는 것을 증명할 수 있는데, 이를 검증해야 하는 사람에게는 공개된 버전을 제공하고 제3자는 숨겨진 버전(Hash)만 볼 수 있습니다. 실제로 전환의 'OpId'는 항상 *숨겨진* 데이터에서 계산됩니다.


![RGB-Bitcoin](assets/en/067.webp)


#### Seal Definition


공개된 형태의 *Seal Definition*에는 네 가지 기본 필드가 있습니다: 'txptr', 'vout', '블라인드' 및 '메소드':




- **txptr**: Bitcoin의 UTXO에 대한 참조입니다:
- **Genesis Seal**의 경우 기존 UTXO(Genesis와 연결된 것)를 직접 가리킵니다;
- 그래프 **Seal**의 경우, 다음과 같이 할 수 있습니다:
        - 특정 UTXO을 가리키는 경우 간단한 'txid'을 입력합니다,
        - 또는 자체 참조를 지정하는 'WitnessTx': Seal은 트랜잭션 자체를 가리킵니다. 이는 라이트닝 채널 오프닝 트랜잭션과 같이 외부 UTXO를 사용할 수 없거나 수신자가 UTXO를 가지고 있지 않은 경우에 특히 유용합니다.
- **vout**: `txptr`로 표시된 트랜잭션의 출력 번호. 표준 그래프 Seal에만 존재합니다(`WitnessTx`에는 존재하지 않음);
- **블라인드**: 기밀성을 강화하고 UTXO의 신원에 대한 무차별 대입 시도를 방지하기 위해 8바이트의 임의의 숫자로 설정합니다;
- **method**: 사용된 앵커링 방법(`Tapret` 또는 `Opret`)을 나타냅니다.


Seal Definition의 *은폐된* 형태는 이 4개의 필드를 연결한 SHA256 Hash(태그가 있는)으로, RGB에 특정한 태그가 있습니다.


![RGB-Bitcoin](assets/en/068.webp)


#### 소유 상태


**Assignment**의 두 번째 구성 요소는 **Owned State**입니다. **Global State**와 달리 공개 또는 비공개 형태로 존재할 수 있습니다:




- **공개 Owned State**: 누구나 Seal와 관련된 데이터를 알고 있습니다. 예를 들어, 공개 이미지입니다;
- **비공개 Owned State**: 데이터는 숨겨져 있으며 소유자(필요한 경우 검증자)만 알 수 있습니다. 예를 들어, 보유한 토큰 수입니다.


RGB는 Owned State에 대해 네 가지 가능한 상태 유형(*StateTypes*)을 정의합니다:




- **선언적**: 수치 데이터 없이 선언적 권리(예: 투표권)만 포함합니다. 숨겨진 형태와 공개된 형태는 동일합니다;
- **대체 가능**: 토큰처럼 대체 가능한 수량을 나타냅니다. 공개된 형태에는 '금액'과 '블라인드'가 있습니다. 숨겨진 형태에서는 금액과 블라인딩을 숨기는 단일 *Pedersen commitment*이 있습니다;
- **구조화**: 구조화된 데이터(최대 64KB)를 저장합니다. 드러난 형태는 데이터 블롭입니다. 숨겨진 형태에서는 이 블롭의 태그가 지정된 Hash입니다:


```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```


예를 들어


```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```




- **첨부 파일**: 파일(오디오, 이미지, 바이너리 등)을 Owned State에 연결하여 Hash `파일 해시`, MIME 유형 `미디어 유형` 및 암호화 솔트 `솔트`를 저장합니다. 파일 자체는 다른 곳에서 호스팅됩니다. 숨겨진 형태에서는 앞의 세 가지 데이터 항목으로 태그가 지정된 Hash입니다:


```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```


예를 들어


```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```


요약하자면, 공개 및 숨김 형태의 4가지 상태 유형은 다음과 같습니다:


```txt
State                      Concealed form                              Revealed form

+---------------------------------------------------------------------------------------------------------

+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |

+--------------------------+             +---------------------------------------+

```



| **Element**     | **Declarative** | **Fungible**                      | **Structured**       | **Attachments**        |
| --------------- | --------------- | --------------------------------- | -------------------- | ---------------------- |
| **Data**        | None            | Signed or unsigned 64-bit integer | Any strict data type | Any file               |
| **Info Type**   | None            | Signed or unsigned                | Strict types         | MIME Type              |
| **Privacy**     | Not required    | Pedersen commitment               | Hash with blinding   | Hashed file identifier |
| **Size Limits** | N/A             | 256 bytes                         | Up to 64 KB          | Up to ~500 GB          |


### 입력


Contract Operation*의 입력은 이 새 작업에서 소비되는 *과제*를 참조합니다. 입력은 다음을 나타냅니다:




- 이전 작업의 식별자(`OpId`): *Assignment*이 위치했던 이전 작업의 식별자(`OpId`);
- '할당 유형': *Assignment*의 유형(예: token의 경우 `자산 소유자`);
- '인덱스': 이전 'OpId'와 연결된 목록에서 *Assignment*의 인덱스이며, 숨겨진 씰의 사전적 정렬 후 결정됩니다.


입력은 이전 할당이 없기 때문에 Genesis에는 나타나지 않습니다. 상태 확장에도 나타나지 않습니다(상태 확장은 봉인을 닫는 것이 아니라 원자가를 기반으로 새 봉인을 재정의하기 때문입니다).


'대체 가능' 유형의 소유 상태가 있을 때, 유효성 검사 로직(AluVM에 제공된 Schema 스크립트를 통해)은 들어오는 토큰(*입력*)의 합계가 나가는 토큰(새로운 *할당*)의 합계와 같아야 한다는 합계의 일관성을 확인합니다.


### 메타데이터


**메타데이터** 필드는 최대 64KB까지 가능하며 유효성 검사에 유용한 임시 데이터를 포함하는 데 사용되지만 Contract의 영구 상태에는 통합되지 않습니다. 예를 들어 복잡한 스크립트의 중간 계산 변수를 여기에 저장할 수 있습니다. 이 공간은 글로벌 기록에 저장하기 위한 것이 아니므로 소유 상태 또는 Global State의 범위를 벗어납니다.


### 밸런스


**밸런스**는 RGB 프로토콜 고유의 메커니즘입니다. Genesis, 상태 트랜지션 또는 상태 확장에서 찾을 수 있습니다. 이는 State Extension(*Redeems*를 통해)에 의해 활성화된 다음 후속 트랜지션에 의해 최종 확정될 수 있는 수치상의 권리를 나타냅니다. 각 Valency는 `ValencyType`(16비트)으로 식별됩니다. 그 의미(재발행권, token 스왑, 소각권 등)는 Schema에 정의되어 있습니다.


구체적으로 설명하자면, Genesis가 "재발행 권한" Valency을 정의한다고 상상할 수 있습니다. State Extension는 특정 조건이 충족되면 이를 소비(*Redeem*)하여 새로운 수량의 토큰을 도입합니다. 그런 다음, 이렇게 생성된 Seal의 소유자로부터 나오는 State Transition이 이 새로운 토큰을 전송할 수 있습니다.


### 사용


사용은 과제를 위한 입력에 해당하는 Valency입니다. 이전에 정의된 Valency가 활성화되는 곳이기 때문에 상태 확장에만 나타납니다. Redeem은 두 개의 필드로 구성됩니다:




- '이전옵아이디': Valency이 지정된 작업의 `옵아이디`입니다;
- valencyType`: 활성화하려는 Valency의 유형(각 `ValencyType`은 State Extension에서 한 번만 사용할 수 있습니다).


예: Valency에 코딩된 내용에 따라 Redeem는 코인스왑 실행에 해당할 수 있습니다.


### RGB 상태 특성


이제 RGB의 몇 가지 기본 상태 특성을 살펴보겠습니다. 특히 다음 사항을 살펴보겠습니다:




- **엄격한 유형 시스템**은 데이터의 정확한 유형 구성을 강요합니다;
- **검증**과 **Ownership**을 분리하는 것의 중요성;
- RGB의 **합의 진화** 시스템에는 *빠르기*와 *푸시백*의 개념이 포함되어 있습니다.


항상 그렇듯이, Contract 상태와 관련된 모든 것은 프로토콜에 명시된 합의 규칙에 따라 클라이언트 측에서 검증되며, 최종 암호화 참조는 Bitcoin 트랜잭션에 고정되어 있다는 점을 명심하시기 바랍니다.


#### 엄격한 유형 시스템


RGB은 *스트릭트 타입 시스템*과 결정론적 직렬화 모드(*스트릭트 인코딩*)를 사용합니다. 이 조직은 Contract 데이터의 정의, 처리 및 유효성 검사에서 완벽한 재현성과 정밀성을 보장하도록 설계되었습니다.


많은 프로그래밍 환경(JSON, YAML...)에서 데이터 구조는 유연할 수 있으며, 심지어 너무 허용적일 수도 있습니다. 반면에 RGB에서는 각 필드의 구조와 유형이 명시적인 제약 조건으로 정의됩니다. 예를 들어




- 각 변수에는 특정 유형(예: 8비트 부호 없는 정수 'u8' 또는 16비트 부호 있는 정수 등)이 있습니다;
- 유형을 구성할 수 있습니다(중첩된 유형). 즉, 다른 유형(예: `u8` 필드, `bool` 필드를 포함하는 집계 유형 등)을 기반으로 유형을 정의할 수 있습니다;
- 컬렉션을 지정할 수도 있습니다: 목록(*list*), 집합(*set*) 또는 사전(*map*), 결정론적 진행 순서에 따라 지정할 수 있습니다;
- 각 필드에는 제한이 있습니다(*하한선* / *상한선*). 또한 컬렉션(봉쇄)의 Elements 개수에도 제한을 두고 있습니다;
- 데이터는 바이트 정렬되며 직렬화는 엄격하게 정의되고 모호하지 않습니다.


이 엄격한 인코딩 프로토콜 덕분입니다:




- 필드의 순서는 사용되는 구현이나 프로그래밍 언어에 관계없이 항상 동일합니다;
- 따라서 동일한 데이터 세트에서 계산된 해시는 재현 가능하고 동일합니다(엄격하게 결정론적인 *공약*);
- 경계는 데이터 크기의 통제되지 않는 증가(예: 너무 많은 필드)를 방지합니다;
- 이러한 형태의 인코딩은 각 참여자가 데이터를 직렬화하고 Hash하는 방법을 정확히 알고 있기 때문에 암호화 검증을 용이하게 합니다.


실제로는 구조(*Schema*)와 결과 코드(*Interface* 및 관련 로직)가 컴파일됩니다. 설명 언어는 Contract(유형, 필드, 규칙)과 엄격한 바이너리 형식인 generate를 정의하는 데 사용됩니다. 컴파일되면 결과는 다음과 같습니다:




- 각 필드에 대한 *메모리 레이아웃*입니다;
- 의미 식별자(메모리 구조가 동일하게 유지되더라도 변수 이름 변경이 로직에 영향을 미치는지 여부를 나타내는 식별자).


또한 엄격한 유형 시스템을 통해 변경 사항을 정밀하게 모니터링할 수 있습니다. 구조에 대한 수정(필드 이름 변경 포함)은 감지할 수 있으며 전체 설치 공간의 변경을 초래할 수 있습니다.


마지막으로, 각 컴파일은 코드의 정확한 버전(데이터, 규칙, 유효성 검사)을 증명하는 암호화 식별자인 핑거프린트를 생성합니다. 예를 들어, 다음과 같은 형식의 식별자입니다:


```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```


이를 통해 합의 또는 구현 업데이트를 관리하는 동시에 네트워크에서 사용되는 버전에 대한 상세한 추적성을 보장할 수 있습니다.


클라이언트 측에서 검증하기 너무 번거로워지는 것을 방지하기 위해, 합의 규칙은 검증 계산에 관련된 모든 데이터에 대해 최대 '2^16' 바이트(64 Kio)의 크기를 부과합니다. 이는 각 변수 또는 구조에 적용되며, 65536바이트 또는 이에 상응하는 숫자(16비트 정수 32768개 등)를 넘지 않아야 합니다. 이는 컬렉션(목록, 집합, 맵)에도 적용되며, `2^16` Elements를 초과할 수 없습니다.


이 한도는 보장합니다:




- State Transition 중에 조작할 데이터의 최대 크기를 제어합니다;
- 유효성 검사 스크립트를 실행하는 데 사용되는 가상 머신(*AluVM*)과의 호환성.


#### 검증!= Ownership 패러다임


RGB의 주요 혁신 중 하나는 두 가지 개념을 엄격하게 분리한 것입니다:




- **유효성 검사**: State Transition이 Contract의 규칙(Business Logic, 기록 등)을 준수하는지 확인합니다;
- **Ownership**(Ownership 또는 제어): Single-Use Seal를 사용(또는 폐쇄)할 수 있는 Bitcoin UTXO를 소유하고 있다는 사실, 따라서 State Transition이 발생할 수 있다는 사실입니다.


**유효성 검사**는 RGB 소프트웨어 스택(라이브러리, *커밋* 프로토콜 등) 수준에서 이루어집니다. 그 역할은 Contract의 내부 규칙(금액, 권한 등)이 준수되는지 확인하는 것입니다. 옵저버 또는 다른 참여자들도 데이터 이력을 검증할 수 있습니다.


*반면에* **Ownership**는 전적으로 Bitcoin의 보안에 의존합니다. UTXO의 개인 키를 소유한다는 것은 새로운 전환을 시작할 수 있는 기능을 제어한다는 의미입니다(Single-Use Seal을 닫음). 따라서 누군가 데이터를 보거나 유효성을 검사할 수 있더라도 해당 UTXO을 소유하고 있지 않으면 상태를 변경할 수 없습니다.


![RGB-Bitcoin](assets/en/069.webp)


이 접근 방식은 더 복잡한 블록체인에서 발생하는 전형적인 취약점을 제한합니다(Smart contract의 모든 코드가 공개되고 누구나 수정할 수 있어 때때로 해킹으로 이어지기도 함). RGB에서는 상태(*Ownership*)에 대한 행동 권한이 Bitcoin Layer에 의해 보호되므로 공격자는 On-Chain 상태와 단순히 상호 작용할 수 없습니다.


또한 이러한 디커플링을 통해 RGB을 Lightning Network과 자연스럽게 통합할 수 있습니다. 매번 On-Chain *커밋*을 하지 않고도 Lightning 채널을 사용하여 RGB 에셋을 연동하고 이동할 수 있습니다. 이 강좌의 뒷부분에서 Lightning에서 RGB의 통합에 대해 자세히 살펴보겠습니다.


#### RGB의 컨센서스 개발


시맨틱 코드 버전 관리 외에도 RGB에는 시간이 지남에 따라 Contract의 합의 규칙을 진화시키거나 업데이트하는 시스템이 포함되어 있습니다. 진화에는 두 가지 주요 형태가 있습니다:




- **빨리 감기**
- **푸시백**


빨리 감기는 이전에 유효하지 않은 규칙이 유효하게 될 때 발생합니다. 예를 들어, Contract가 새로운 유형의 `AssignmentType` 또는 새 필드를 허용하도록 진화하는 경우입니다:




- RGB은 Client-side Validation에서 작동하며 Blockchain의 전반적인 호환성에 영향을 미치지 않으므로 기존 Blockchain 하드포크와 비교할 수 없습니다;
- 실제로 이러한 유형의 변경은 Contract Operation의 `Ffv`(*빨리 감기 버전*) 필드로 표시됩니다;
- 현재 보유자는 피해를 입지 않습니다. 보유 상태는 유효하게 유지됩니다;
- 반면에 신규 수혜자(또는 신규 사용자)는 새 규칙을 인식하기 위해 소프트웨어(Wallet)를 업데이트해야 합니다.


푸시백은 이전에 유효했던 규칙이 무효화되는 것을 의미합니다. 따라서 이는 규칙을 '강화'하는 것이지만 엄밀히 말하면 소프트포크는 아닙니다:




- 기존 보유자는 영향을 받을 수 있습니다(새 버전에서는 자산이 쓸모없거나 무효화될 수 있습니다);
- 새로운 규칙을 채택하는 사람은 기존 규칙에서 벗어나는 것이므로 사실상 새로운 프로토콜을 만든다고 볼 수 있습니다;
- 발행자는 이 새로운 프로토콜에서 자산을 다시 발행하기로 결정할 수 있으며, 사용자가 두 가지 버전을 모두 관리하고 싶다면 두 개의 지갑(이전 프로토콜용 지갑과 새 프로토콜용 지갑)을 유지해야 합니다.


RGB Contract 운영에 관한 이 장에서는 이 프로토콜의 기본 원칙을 살펴봤습니다. 아시다시피 RGB 프로토콜의 고유한 복잡성 때문에 많은 기술 용어를 사용해야 합니다. 따라서 다음 장에서는 이 첫 번째 이론적 부분에서 다룬 모든 개념을 요약한 용어집과 RGB과 관련된 모든 기술 용어의 정의를 제공하겠습니다. 그런 다음 다음 섹션에서는 RGB 계약의 정의와 구현에 대해 실무적으로 살펴보겠습니다.


## RGB 용어집


<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>


RGB 세계에서 사용되는 중요한 기술 용어(알파벳 순서대로 나열됨)에 대한 이 짧은 용어집을 다시 참조하면 유용할 것입니다. 첫 번째 섹션에서 다룬 모든 내용을 이미 이해했다면 이 장이 꼭 필요하지는 않습니다.


#### AluVM


약어 AluVM은 "_알고리즘 논리 단위 가상 머신_"의 약자로, Smart contract 검증 및 분산 컴퓨팅을 위해 설계된 레지스터 기반 가상 머신입니다. RGB 컨트랙트의 유효성 검사에 사용됩니다(독점적으로 예약된 것은 아님). 따라서 RGB Contract에 포함된 스크립트나 작업은 AluVM 환경에서 실행할 수 있습니다.


자세한 내용은 [AluVM 공식 웹사이트](https://www.AluVM.org/)


#### Anchor


Anchor는 트랜잭션에 고유한 _커밋_이 포함되어 있음을 증명하는 데 사용되는 클라이언트 측 데이터 집합을 나타냅니다. RGB 프로토콜에서 Anchor는 다음 Elements로 구성됩니다:




- **Bitcoin**의 트랜잭션 식별자(txid)는 **Witness Transaction**입니다;
- **Multi Protocol Commitment (MPC)**;
- **Deterministic Bitcoin Commitment (DBC)**;
- **탭렛** Commitment 메커니즘을 사용하는 경우 **추가 트랜잭션 증명(ETP)**(이 모델 전용 섹션 참조)을 사용합니다.


따라서 Anchor는 특정 Bitcoin 트랜잭션과 RGB 프로토콜에 의해 검증된 개인 데이터 사이에 검증 가능한 링크를 설정하는 역할을 합니다. 이는 정확한 내용이 공개적으로 노출되지 않고도 이러한 데이터가 실제로 Blockchain에 포함되어 있음을 보장합니다.


#### Assignment


RGB의 로직에서 Assignment는 Contract의 상태 내에서 특정 속성을 수정, 업데이트 또는 생성하는 트랜잭션 출력과 동일합니다. Assignment는 두 개의 Elements로 구성됩니다:




- A **Seal Definition**(특정 UTXO 참조);
- Owned State**(이 새 소유자와 관련된 상태를 설명하는 데이터)**입니다.


따라서 Assignment은 상태의 일부(예: 자산)가 이제 특정 보유자에게 할당되었음을 나타내며, 이는 UTXO에 연결된 Single-Use Seal를 통해 식별됩니다.


#### Business Logic


Business Logic은 **Schema**(즉, Contract 자체의 구조)에 의해 설명되는 Contract의 모든 규칙과 내부 작동을 그룹화합니다. 이는 Contract의 상태가 어떻게 진화할 수 있는지, 어떤 조건에서 진화할 수 있는지를 설명합니다.


#### Client-side Validation


Client-side Validation은 프로토콜의 규칙에 따라 각 당사자(클라이언트)가 비공개로 교환되는 일련의 데이터를 검증하는 프로세스를 말합니다. RGB의 경우, 이렇게 교환된 데이터는 **위임**이라는 이름으로 함께 그룹화됩니다. 모든 트랜잭션을 On-Chain에 공개해야 하는 Bitcoin 프로토콜과 달리, RGB는 _커미트먼트_(Bitcoin에 고정된)만 공개적으로 저장할 수 있고, 필수 Contract 정보(전환, 증명, 증명)는 관련 사용자 간에만 공유하는 off-chain을 유지합니다.


#### Commitment


(암호학적 의미에서) Commitment은 구조화된 데이터 'm'(메시지)과 임의의 값 'r'에 대한 연산에서 결정론적으로 파생된 'C'로 표시되는 수학적 객체입니다. 우리는 씁니다:


$$
C = \text{commit}(m, r)
$$


이 메커니즘은 두 가지 주요 작업으로 구성됩니다:




- **Commit**: 메시지 `m`과 난수 `r`에 암호화 함수를 적용하여 `C`를 생성합니다;
- **Verify**: `C`, `m` 메시지 및 `r` 값을 사용하여 이 Commitment이 올바른지 확인합니다. 이 함수는 `True` 또는 `False`를 반환합니다.


Commitment는 두 가지 속성을 준수해야 합니다:




- **바인딩**: 동일한 `C`를 생성하는 두 개의 다른 메시지를 찾는 것은 불가능해야 합니다:


$$
m': \, | \,: m' \neq m \quad \text{and} \quad r': \, | \,: r' \neq r \quad
$$


예를 들면 다음과 같습니다:


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- **숨기기**: 'ㄷ'에 대한 지식이 'ㅁ'의 내용을 드러내지 않아야 합니다.


RGB 프로토콜에서는 정보 자체를 공개하지 않고 특정 시점에 특정 정보의 존재를 증명하기 위해 Commitment이 Bitcoin 트랜잭션에 포함되어 있습니다.


#### Consignment


**Consignment**는 Client-side Validation에 따라 당사자 간에 교환된 데이터를 RGB에 그룹화합니다. Consignment에는 두 가지 주요 범주가 있습니다:




- **Contract Consignment**: *발급자*(Contract 발급자)가 제공하며, Schema, Genesis, Interface 및 Interface Implementation 등의 초기화 정보가 포함되어 있습니다.
- **전송 Consignment**: 결제 당사자(*결제자*)가 제공합니다. 여기에는 Terminal Consignment(즉, 지불자가 받은 최종 상태)까지 이어지는 상태 전환의 전체 이력이 포함됩니다.


이러한 위탁은 Blockchain에 공개적으로 기록되지 않으며, 해당 당사자가 선택한 통신 채널을 통해 직접 교환됩니다.


#### Contract


Contract은 RGB 프로토콜을 통해 여러 행위자 간에 디지털 방식으로 실행되는 권한 집합입니다. 활성 상태와 Business Logic이 있으며, 어떤 작업(전송, 확장 등)이 승인되는지 지정하는 Schema에 의해 정의됩니다. Contract의 상태와 유효성 규칙은 Schema에 표현됩니다. 언제든지 Contract은 이 Schema와 유효성 검사 스크립트(예: AluVM에서 실행)에 의해 허용되는 것에 따라서만 진화합니다.


#### Contract Operation


Contract Operation은 Schema 규칙에 따라 수행되는 Contract 상태 업데이트입니다. RGB에는 다음 작업이 존재합니다:




- **State Transition**;
- **Genesis**;
- State **Extension**.


각 작업은 특정 데이터를 추가하거나 대체하여 상태를 수정합니다(Global State, Owned State...).


#### Contract Participant


Contract Participant은 Contract와 관련된 작전에 참여하는 행위자입니다. RGB에서는 둘을 구분합니다:




- Contract을 생성하는 Genesis의 발행자(Contract의 원본)입니다;
- Contract 당사자, 즉 Contract 상태에 대한 권리 보유자;
- 공공 당사자는 Contract가 대중이 액세스할 수 있는 밸런스를 제공하는 경우 상태 확장을 구축할 수 있습니다.


#### Contract Rights


Contract Rights은 RGB Contract에 관련된 사람들이 행사할 수 있는 다양한 권리를 나타냅니다. 이러한 권리는 여러 범주로 나뉩니다:




- 특정 Ownership의 UTXO와 연결된 Ownership 권한(**봉인 정의**를 통해);
- **집행 권한**, 즉 Schema에 따라 하나 이상의 전환(상태 전환)을 구축할 수 있는 권한입니다;
- **공공 권한**, 예를 들어 Schema가 Valency의 상환을 통해 State Extension을 생성하는 등 특정 공공 사용을 승인하는 경우입니다.


#### Contract State


Contract State은 특정 시점의 Contract의 현재 상태에 해당합니다. Contract의 상태를 반영하여 공개 데이터와 비공개 데이터로 구성될 수 있습니다. RGB은 둘을 구분합니다:




- Global State의 공개 속성을 포함하는 **Contract**(Genesis에서 설정되거나 승인된 업데이트를 통해 추가됨)가 있습니다;
- **소유 상태**는 특정 소유자가 소유한 상태로, 해당 소유자의 UTXO가 식별합니다.


#### Deterministic Bitcoin Commitment - DBC


Deterministic Bitcoin Commitment(DBC)은 Bitcoin 트랜잭션에서 _commitment_를 증명 가능하고 고유하게 등록하는 데 사용되는 규칙 집합입니다. RGB 프로토콜에는 두 가지 주요 형태의 DBC가 있습니다:




- **Opret**
- **Tapret**


이러한 메커니즘은 Bitcoin 트랜잭션의 출력 또는 구조에서 _약속_이 인코딩되는 방식을 정확하게 정의하여 이 Commitment을 결정론적으로 추적 및 검증할 수 있도록 합니다.


#### Directed Acyclic Graph - DAG


DAG(또는 *순환 유도 그래프*)는 주기가 없는 그래프로, 위상 스케줄링을 가능하게 합니다. RGB 콘트랙트의 _샤드_와 같은 블록체인은 DAG로 표현할 수 있습니다.


자세한 내용은 [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)


#### 인그레이빙


각인은 Contract의 역대 소유자가 Contract 이력에 입력할 수 있는 선택적 데이터 문자열입니다. 이 기능은 예를 들어 **RGB21** Interface에 존재하며 기념 또는 설명 정보를 Contract 기록에 추가할 수 있습니다.


#### 추가 거래 증명 - ETP


ETP(*추가 트랜잭션 증명*)는 **Tapret** *Commitment*(_taproot_의 맥락에서)의 유효성을 검사하는 데 필요한 추가 데이터를 포함하는 Anchor의 일부입니다. 여기에는 무엇보다도 Taproot 스크립트의 내부 공개 키(_내부 PubKey_)와 _Script Path Spend_와 관련된 정보가 포함됩니다.


#### Genesis


Genesis는 Schema에 의해 관리되는 데이터 집합을 말하며, RGB에서 모든 Contract의 초기 상태를 형성합니다. Bitcoin의 _제네시스 블록_ 개념 또는 Coinbase Transaction 개념과 비교할 수 있지만 여기서는 _클라이언트 측_ 및 RGB token 수준에서 비교합니다.


#### Global State


Global State은 Contract State에 포함된 공개 속성 집합입니다. Genesis에 정의되어 있으며 Contract 규칙에 따라 승인된 전환을 통해 업데이트할 수 있습니다. 소유 상태와 달리 Global State은 특정 주체에 속하지 않으며 Contract 내의 공공 레지스트리에 더 가깝습니다.


#### Interface


Interface는 Schema 또는 Contract 연산과 그 상태에서 컴파일된 이진 데이터를 디코딩하여 사용자 또는 Wallet이 읽을 수 있도록 하는 데 사용되는 명령어 집합입니다. 해석 Layer 역할을 합니다.


#### Interface Implementation


Interface Implementation은 **Interface**를 **Schema**에 연결하는 선언의 집합입니다. 이는 Interface 자체에서 의미 변환을 수행하여 사용자 또는 관련 소프트웨어(지갑)가 Contract의 원시 데이터를 이해할 수 있도록 합니다.


#### Invoice


Invoice은 [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58)로 인코딩된 URL의 형태를 취하며, (지불자가) **State Transition**을 구성하는 데 필요한 데이터를 포함합니다. 즉, 거래 상대방(*지불자*)이 자산을 전송하거나 Contract의 상태를 업데이트하기 위해 해당 트랜지션을 생성할 수 있도록 하는 Invoice입니다.


#### Lightning Network


Lightning Network은 2/2 다중 서명 지갑으로 구성된 Bitcoin의 결제 채널(또는 _상태 채널_)의 탈중앙화 네트워크입니다. 이는 빠르고 저렴한 비용의 _오프체인_ 거래를 가능하게 하며, 필요한 경우 중재(또는 종료)를 위해 Bitcoin의 Layer 1에 의존합니다.


라이트닝 작동 방식에 대한 자세한 내용은 이 다른 강좌를 수강하는 것을 추천합니다:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

#### Multi Protocol Commitment - MPC


Multi Protocol Commitment(MPC)는 단일 Merkle Tree 트랜잭션 내에 서로 다른 컨트랙트의 여러 **전환 번들**을 포함하기 위해 RGB에서 사용된 Bitcoin 구조를 말합니다. 이 아이디어는 블록 공간 점유를 최적화하기 위해 여러 개의 커미트먼트(잠재적으로 다른 컨트랙트 또는 다른 자산에 해당)를 단일 Anchor 포인트에 그룹화한다는 것입니다.


#### Owned State


Owned State는 Assignment으로 묶여 있고 특정 보유자와 연결된(UTXO를 가리키는 Single-Use Seal을 통해) Contract State의 일부입니다. 예를 들어 디지털 자산 또는 특정인에게 할당된 특정 계약상의 권리를 나타냅니다.


#### Ownership


Ownership은 Seal Definition이 참조하는 UTXO을 제어하고 소비할 수 있는 기능을 말합니다. Owned State이 UTXO에 연결된 경우, 이 UTXO의 소유자는 Contract의 규칙에 따라 잠재적으로 관련 상태를 전송하거나 발전시킬 수 있는 권리를 갖습니다.


#### Partially Signed Bitcoin Transaction - PSBT


PSBT(_부분적으로 서명된 Bitcoin 트랜잭션_)은 아직 완전히 서명되지 않은 Bitcoin 트랜잭션입니다. 트랜잭션이 On-Chain 배포 준비가 완료된 것으로 간주될 때까지 특정 Elements(서명, 스크립트 등)을 추가하거나 확인할 수 있는 여러 엔터티 간에 공유할 수 있습니다.


자세한 내용은 [BIP-0174](https://github.com/Bitcoin/BIPs/blob/master/BIP-0174.mediawiki)


#### Pedersen commitment


Pedersen commitment은 더하기 연산과 관련하여 **동형적**이라는 속성을 가진 암호화 Commitment의 한 유형입니다. 즉, 개별 값을 공개하지 않고도 두 커미트먼트의 합계를 검증할 수 있습니다.


공식적으로는


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


그런 다음


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


이 속성은 예를 들어 교환된 토큰의 양을 숨기면서도 총액을 확인할 수 있을 때 유용합니다.


추가 정보: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)


#### Redeem


State Extension에서 Redeem은 이전에 신고된 **Valency**을 회수(또는 착취)하는 행위를 의미합니다. Valency은 공공의 권리이므로, Redeem은 권한이 있는 참여자가 특정 Contract State Extension를 청구할 수 있도록 허용합니다.


#### Schema


RGB의 Schema는 Contract의 작동을 지배하는 변수, 규칙 및 Business Logic(*Business Logic*)의 집합을 설명하는 선언적 코드입니다. Schema는 상태 구조, 허용되는 트랜지션 유형 및 유효성 검사 조건을 정의합니다.


#### Seal Definition


Seal Definition는 Assignment의 일부로, _약정_을 새 소유자가 소유한 UTXO과 연결합니다. 즉, 조건이 어디에 있는지(어느 UTXO에 있는지)를 나타내며 자산 또는 권리의 Ownership을 설정합니다.


#### Shard


Shard은 RGB Contract의 상태 전환 기록의 DAG에서 한 분기를 나타냅니다. 즉, Contract의 전체 이력의 일관된 하위 집합으로, 예를 들어 _Genesis_ 이후 특정 자산의 유효성을 증명하는 데 필요한 트랜지션 시퀀스에 해당합니다.


#### Single-Use Seal


Single-Use Seal는 아직 알려지지 않은 메시지에 대한 Commitment의 암호화 약속으로, 향후 단 한 번만 공개되며 특정 대상의 모든 구성원만 알 수 있어야 합니다. 목표는 동일한 Seal에 대해 여러 개의 경쟁 약속이 생성되는 것을 방지하는 것입니다.


#### Stash


Stash는 사용자가 하나 이상의 RGB 컨트랙트에 대해 유효성 검사 목적으로 저장하는 클라이언트 측 데이터 집합입니다(*Client-side Validation*). 여기에는 전환 내역, 위탁, 유효성 증명 등이 포함됩니다. 각 보유자는 필요한 기록의 일부(*샤드*)만 보유합니다.


#### State Extension


State Extension는 이전에 선언된 **밸런시**를 사용하여 상태 업데이트를 다시 트리거하는 데 사용되는 Contract Operation입니다. 유효하려면 State Extension가 State Transition에 의해 닫혀야 합니다(Contract의 최종 상태를 업데이트하는).


#### State Transition


State Transition은 RGB Contract의 상태를 새로운 상태로 변경하는 작업입니다. Global State 및/또는 Owned State 데이터를 수정할 수 있습니다. 실제로 각 전환은 Schema 규칙에 의해 확인되고 _commitment_를 통해 Bitcoin Blockchain에 고정됩니다.


#### Taproot


BIP341](https://github.com/Bitcoin/BIPs/blob/master/BIP-0341.mediawiki) 및 [BIP342](https://github.com/Bitcoin/BIPs/blob/master/BIP-0342.mediawiki)에서 도입한 Bitcoin의 SegWit v1 트랜잭션 형식을 참조합니다. Taproot은 특히 트랜잭션을 더 간결하게 만들고 서로 구별하기 어렵게 만들어 스크립트의 기밀성과 유연성을 향상시킵니다.


#### Terminal Consignment - Consignment Endpoint


Terminal Consignment(또는 _위탁 엔드포인트_)은 수취인의 Invoice(*수취인*)에서 생성된 State Transition를 포함하여 Contract의 최종 상태를 포함하는 *전송 Consignment*입니다. 따라서 전송의 엔드포인트이며, Ownership 또는 상태가 전송되었음을 증명하는 데 필요한 데이터를 포함합니다.


#### Transition Bundle


Transition Bundle은 모두 동일한 ***Witness Transaction*** Bitcoin에 관여하는 RGB 상태 전환(동일한 Contract에 속하는)의 집합입니다. 따라서 여러 개의 업데이트 또는 전송을 하나의 On-Chain Anchor로 묶을 수 있습니다.


#### UTXO


Bitcoin UTXO(*사용되지 않은 트랜잭션 출력*)은 트랜잭션의 Hash와 출력 인덱스(*vout*)로 정의됩니다. 아웃포인트_라고도 합니다. RGB 프로토콜에서 **Seal Definition**을 통해 UTXO을 참조하면 **Owned State**의 위치, 즉 Blockchain에 보관된 프로퍼티를 확인할 수 있습니다.


#### Valency


Valency은 국가 보관을 필요로 하지 않지만 **State Extension**을 통해 상환할 수 있는 공공 권리입니다. 따라서 이는 추후에 특정 확장을 수행하기 위해 모든 플레이어(또는 특정 플레이어)에게 열려 있는 일종의 가능성으로, Contract의 논리에 선언되어 있습니다.


#### Witness Transaction


Witness Transaction은 Bitcoin 트랜잭션으로, Multi Protocol Commitment(MPC)이 포함된 메시지를 중심으로 Single-Use Seal를 닫습니다. 이 트랜잭션은 UTXO을 보내거나 Seal을 생성하여 RGB 프로토콜에 연결된 Commitment을 Seal으로 만듭니다. 이는 특정 시점에 상태가 설정되었음을 증명하는 On-Chain의 역할을 합니다.


# RGB에서 프로그래밍


<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>


## RGB 계약 이행하기


<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>


:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::


이 장에서는 RGB Contract이 어떻게 정의되고 구현되는지 자세히 살펴보겠습니다. RGB Contract의 구성 요소는 무엇이고, 각 구성 요소의 역할은 무엇이며 어떻게 구성되는지 살펴보겠습니다.


### RGB의 구성 요소 Contract


지금까지 Contract의 시작점을 나타내는 **Genesis**에 대해 이미 논의했으며, 이것이 *Contract Operation*의 로직 및 프로토콜의 상태와 어떻게 부합하는지 살펴봤습니다. 그러나 RGB Contract의 완전한 정의는 Genesis에만 국한되지 않으며, 세 가지 상호 보완적인 구성 요소가 함께 구현의 핵심을 형성합니다.


첫 번째 구성 요소는 **Schema**입니다. 이것은 Contract의 기본 구조와 Business Logic(*Business Logic*)를 설명하는 파일입니다. 여기에는 사용되는 데이터 유형, 유효성 검사 규칙, 허용되는 작업(예: 초기 token 발급, 전송, 특수 조건 등), 즉 Contract의 작동 방식을 지시하는 일반적인 프레임워크가 명시되어 있습니다.


두 번째 구성 요소는 **Interface**입니다. 이는 사용자(그리고 더 나아가 포트폴리오 소프트웨어)가 이 Contract와 상호작용하는 방식에 초점을 맞추고 있습니다. 이는 의미론, 즉 다양한 필드와 동작의 가독성 있는 표현을 설명합니다. 따라서 Schema가 Contract의 기술적인 작동 방식을 정의하는 반면, Interface은 메서드 이름, 데이터 표시 등 이러한 기능을 표시하고 노출하는 방법을 정의합니다.


세 번째 구성 요소는 **Interface Implementation**으로, Schema과 Interface 사이의 일종의 가교 역할을 함으로써 앞의 두 가지를 보완합니다. 즉, Interface이 표현하는 의미를 Schema에 정의된 기본 규칙과 연결합니다. 예를 들어, 이 구현은 Wallet에 입력된 매개변수와 프로토콜에 의해 부과된 이진 구조 간의 변환 또는 기계어로 된 유효성 검사 규칙의 컴파일을 관리합니다.


이러한 모듈성은 프로토콜의 합의 규칙을 따르는 한, 서로 다른 개발자 그룹이 이러한 측면(*Schema*, *Interface*, *구현*)에서 개별적으로 작업할 수 있게 해준다는 점에서 RGB의 흥미로운 특징입니다.


요약하자면, 각 Contract은 다음과 같이 구성됩니다:




- Contract의 초기 상태인 **Genesis**(자산, 권리 또는 기타 매개변수화 가능한 데이터의 첫 번째 Ownership를 정의하는 특수 트랜잭션에 비유할 수 있음)에 해당합니다;
- **Schema**, Contract의 Business Logic(데이터 유형, 유효성 검사 규칙 등)을 설명합니다;
- 지갑과 인간 사용자 모두에게 시맨틱 **Interface**을 제공하여 트랜잭션의 읽기 및 실행을 명확히 하는 Layer을 제공합니다;
- **구현 Interface**은 Business Logic와 프레젠테이션 사이의 간극을 메워 Contract 정의가 사용자 경험과 일관성을 유지하도록 합니다.


![RGB-Bitcoin](assets/en/070.webp)


Wallet가 RGB 자산(대체 가능한 token이든 모든 종류의 권리이든)을 관리하려면 이 모든 Elements가 컴파일되어야 한다는 점에 유의하세요: *Schema*, *Interface*, *Interface Implementation* 및 *Genesis*. 이는 ***Contract Consignment***, 즉 클라이언트 측 Contract의 유효성을 검사하는 데 필요한 모든 것이 포함된 데이터 패키지를 통해 전송됩니다.


이러한 개념을 명확히 하기 위해 RGB의 구성 요소를 객체 지향 프로그래밍(OOP) 또는 이더리움 생태계에서 이미 알려진 개념과 비교한 요약 표를 준비했습니다:


| RGB Contract Component       | Meaning                        | OOP Equivalent                                     | Ethereum Equivalent                |
| ---------------------------- | ------------------------------ | -------------------------------------------------- | ---------------------------------- |
| **Genesis**                  | Initial state of the contract  | Class constructor                                  | Contract constructor               |
| **Schema**                   | Business logic of the contract | Class                                              | Contract                           |
| **Interface**                | Semantics of the contract      | Interface (Java) / Trait (Rust) / Protocol (Swift) | ERC Standard                       |
| **Interface Implementation** | Mapping semantics and logic    | Impl (Rust) / Implements (Java)                    | Application Binary Interface (ABI) |


왼쪽 열은 Elements 프로토콜과 관련된 RGB을 보여줍니다. 가운데 열은 각 구성 요소의 구체적인 기능을 보여줍니다. 그런 다음 'OOP 등가' 열에서 객체 지향 프로그래밍의 등가 용어를 찾습니다:




- **Genesis**은 *클래스 생성자*와 유사한 역할을 수행하며, 여기에서 Contract의 상태가 초기화됩니다;
- **Schema**은 클래스에 대한 설명, 즉 속성, 메서드 및 기본 로직에 대한 정의입니다;
- **Interface**는 *인터페이스*(Java), *특성*(Rust) 또는 *프로토콜*(Swift)에 해당합니다: 이들은 함수, 이벤트, 필드에 대한 공개 정의입니다...;
- **Interface Implementation**는 Rust의 *Impl* 또는 Java의 *Implements*에 해당하며, 코드가 Interface에서 발표된 메서드를 실제로 실행하는 방법을 지정합니다.


이더리움 맥락에서 Genesis은 *Contract 생성자*에, Schema은 Contract 정의에, Interface은 ERC-20 또는 ERC-721과 같은 표준에, Interface Implementation은 Contract와의 상호작용 형식을 지정하는 ABI(*Application Binary Interface*)에 더 가깝다고 할 수 있습니다.


RGB의 모듈성의 장점은 *Schema*의 로직과 *Interface*의 의미를 존중하는 한, 다양한 이해관계자가 예를 들어 자체 Interface Implementation를 작성할 수 있다는 사실에도 있습니다. 따라서 발행자는 Contract의 로직을 수정하지 않고 보다 사용자 친화적인 새로운 프론트엔드(Interface)를 개발하거나, 반대로 Schema를 확장하여 기능을 추가하고 적응된 Interface Implementation의 새 버전을 제공하면서 기본 기능에 대해서는 이전 구현이 유효하게 유지될 수 있습니다.


새로운 Contract을 컴파일할 때, 자산을 발행하거나 배포하는 첫 번째 단계인 generate과 그 구성 요소(Schema, Interface, Interface Implementation)를 Genesis로 컴파일합니다. 그 후 Contract은 완전히 작동하며 지갑과 사용자에게 전파할 수 있습니다. Genesis가 이 세 가지 구성 요소와 결합된 이 방법은 높은 수준의 사용자 정의(각 Contract은 자체 로직을 가질 수 있음), 탈중앙화(누구나 주어진 구성 요소에 기여할 수 있음), 보안(다른 블록체인에서 흔히 발생하는 것처럼 임의의 온-chain code에 의존하지 않고 프로토콜에서 엄격하게 정의된 유효성 검사를 유지함)을 보장합니다.


이제 **Schema**, **Interface**, **Interface Implementation**의 각 구성 요소에 대해 자세히 살펴보겠습니다.


### Schema


이전 섹션에서 RGB 생태계에서 Contract는 초기 상태를 설정하는 Genesis과 기타 여러 보완 구성 요소인 여러 Elements으로 구성되어 있음을 살펴보았습니다. Schema의 목적은 데이터 구조, 사용되는 유형, 허용된 작업 및 조건 등 Contract의 모든 Business Logic을 선언적으로 설명하는 것입니다. 따라서 각 참여자(예: Wallet)는 수신하는 상태 전환이 Schema에 정의된 논리를 준수하는지 확인해야 하므로 클라이언트 측에서 Contract를 작동시키는 데 있어 매우 중요한 요소입니다.


Schema은 객체 지향 프로그래밍(OOP)의 "클래스"에 비유할 수 있습니다. 일반적으로 다음과 같이 Contract의 구성 요소를 정의하는 모델 역할을 합니다:




- 소유 상태 및 과제의 다양한 유형;
- 권한, 즉 특정 작업에 대해 트리거(*상환*)할 수 있는 특별한 권한입니다;
- Global State의 글로벌, 공개 및 공유 속성을 설명하는 Contract 필드입니다;
- Genesis 구조(Contract를 활성화하는 첫 번째 작업);
- 허용된 상태 전환 및 상태 확장의 형태와 이러한 작업을 통해 어떻게 수정할 수 있는지 설명합니다;
- 임시 또는 추가 정보를 저장하기 위해 각 작업과 관련된 메타데이터를 저장합니다;
- 내부 Contract 데이터의 진화 방식을 결정하는 규칙(예: 필드가 변경 가능한지 또는 누적되는지 여부)입니다;
- 유효한 것으로 간주되는 작업 순서: 예를 들어, 준수해야 하는 전환 순서 또는 충족해야 하는 일련의 논리적 조건입니다.


![RGB-Bitcoin](assets/en/071.webp)


RGB에서 자산의 *발행자*가 Contract를 게시하면, 이와 관련된 Genesis과 Schema를 제공합니다. 자산과 상호작용하고자 하는 사용자나 지갑은 이 Schema를 검색하여 Contract의 로직을 이해하고 나중에 참여하게 될 트랜지션이 합법적인지 확인할 수 있습니다.


RGB 자산에 대한 정보를 받는 사람(예: token 전송)의 경우 첫 번째 단계는 이 정보를 Schema과 비교하여 검증하는 것입니다. 여기에는 Schema 컴파일을 사용하는 것이 포함됩니다:




- 소유 상태, 할당 및 기타 Elements가 올바르게 정의되어 있고 부과된 유형(소위 *엄격 유형 시스템*)을 준수하는지 확인합니다;
- 전환 규칙(유효성 검사 스크립트)이 충족되는지 확인합니다. 이러한 스크립트는 클라이언트 측에 있는 AluVM을 통해 실행할 수 있으며, Business Logic의 일관성(이체 금액, 특수 조건 등)을 검증하는 역할을 담당합니다.


실제로 chain code(이더리움의 EVM)에 저장하는 블록체인에서 볼 수 있듯이, Schema은 실행 가능한 코드가 아닙니다. 반대로 RGB은 Business Logic(선언적)을 Blockchain(암호화 앵커로 제한됨)의 실행 코드와 분리합니다. 따라서 Schema은 규칙을 결정하지만, 이러한 규칙의 적용은 Client-side Validation 원칙에 따라 각 참여자의 사이트에서 Blockchain 외부에서 이루어집니다.


RGB 애플리케이션에서 사용하려면 먼저 Schema을 컴파일해야 합니다. 이 컴파일은 바이너리 파일(예: `.RGB`) 또는 암호화된 바이너리 파일(`.rgba`)을 생성합니다. Wallet는 이 파일을 가져올 때 이를 인식합니다:




- 엄격한 타입 시스템 덕분에 각 데이터 유형(정수, 구조체, 배열 등)이 어떻게 생겼는지 알아보세요;
- Genesis의 구조화 방법(자산 초기화를 이해하기 위해);
- 다양한 유형의 작업(상태 전환, 상태 확장) 및 상태를 수정하는 방법에 대해 설명합니다;
- AluVM 엔진이 작업의 유효성을 확인하기 위해 적용할 스크립팅 규칙(Schema에 도입됨)입니다.


이전 장에서 설명한 대로 *스트릭트 타입 시스템*은 안정적이고 결정론적인 인코딩 형식을 제공합니다. 소유 상태, 전역 상태 또는 Valencies 등 모든 변수가 정확하게 설명됩니다(크기, 필요한 경우 하한 및 상한, 부호 또는 부호 없는 타입 등). 예를 들어 복잡한 사용 사례를 지원하기 위해 중첩 구조를 정의할 수도 있습니다.


선택적으로 Schema는 기존 기본 구조(템플릿)의 재사용을 용이하게 하는 루트 `SchemaId`를 참조할 수 있습니다. 이러한 방식으로 Contract를 발전시키거나 이미 검증된 템플릿에서 변형(예: 새로운 유형의 token)을 만들 수 있습니다. 이러한 모듈성은 전체 계약을 다시 작성할 필요를 없애고 모범 사례의 표준화를 장려합니다.


또 다른 중요한 점은 상태 진화 논리(전송, 업데이트 등)가 스크립트, 규칙 및 조건의 형태로 Schema에 설명되어 있다는 것입니다. 따라서 Contract 설계자가 재발행을 승인하거나 소각 메커니즘(토큰 소멸)을 적용하고자 하는 경우 AluVM의 유효성 검사 부분에서 Schema에 해당하는 스크립트를 지정할 수 있습니다.


#### 프로그래밍 가능한 On-Chain 블록체인과의 차이점


Smart contract 코드(실행 파일)가 Blockchain 자체에 기록되는 이더리움과 같은 시스템과 달리, RGB는 컴파일된 선언적 문서 형태로 Contract(로직)인 off-chain을 저장합니다. 이는 다음을 의미합니다:




- Bitcoin 네트워크의 모든 노드에서 실행되는 튜링 완료 VM은 없습니다. RGB Contract의 규칙은 Blockchain에서 실행되는 것이 아니라 상태를 검증하고자 하는 각 사용자에서 실행됩니다;
- Contract 데이터는 Blockchain을 오염시키지 않습니다: 암호화 증거(*커밋*)만이 Bitcoin 트랜잭션에 포함됩니다(`Tapret` 또는 `Opret`를 통해);
- Schema는 Bitcoin Blockchain에서 Fork을 사용하지 않고도 업데이트하거나 거부(*빠르게 전달*, *푸시백* 등)할 수 있습니다. 지갑은 새로운 Schema를 가져와 합의 변경에 적응하기만 하면 됩니다.


#### 발급자 및 사용자의 사용


발행자가 자산(예: 인플레이션이 없는 대체 가능한 token)을 생성하면 이를 준비합니다:




- 배출, 전송 등의 규칙을 설명하는 Schema입니다;
- 이 Schema에 맞게 조정된 Genesis(발행된 총 토큰 수, 최초 소유자의 신원, 재발행을 위한 특별 유효성 등)를 포함합니다.


그런 다음 컴파일된 Schema('.RGB' 파일)를 사용자에게 제공하므로, 이 token을 전송받는 사람은 누구나 로컬에서 작업의 일관성을 확인할 수 있습니다. 이 Schema가 없으면 사용자는 상태 데이터를 해석하거나 Contract 규칙을 준수하는지 확인할 수 없습니다.


따라서 새로운 Wallet이 자산을 지원하고자 할 때 관련 Schema를 통합하기만 하면 됩니다. 이 메커니즘을 사용하면 Wallet의 소프트웨어 기반을 변경하지 않고도 새로운 RGB 자산 유형에 호환성을 추가할 수 있습니다. Schema 바이너리를 가져와 구조를 파악하기만 하면 됩니다.


Schema는 RGB에서 Business Logic을 정의합니다. 여기에는 Contract의 진화 규칙, 데이터 구조(소유 상태, Global State, Valencies) 및 관련 유효성 검사 스크립트(AluVM에 의해 실행 가능)가 나열되어 있습니다. 이 선언적 문서 덕분에 Contract(컴파일된 파일)의 정의는 규칙의 실제 실행(클라이언트 측)과 명확하게 분리되어 있습니다. 이러한 분리는 RGB에 뛰어난 유연성을 제공하여 광범위한 사용 사례(대체 가능한 토큰, NFT, 보다 정교한 계약)를 가능하게 하는 동시에 프로그래밍 가능한 On-Chain 블록체인의 일반적인 복잡성과 결함을 피할 수 있게 합니다.


#### Schema 예제


Schema의 구체적인 예로 RGB Contract을 살펴보겠습니다. 이는 Rust의 파일 `nia.rs`("*비인플레이션 자산*"의 이니셜)에서 발췌한 것으로, 초기 Supply(비인플레이션 자산) 이상으로 재발행할 수 없는 대체 가능한 토큰의 모델을 정의하는 것입니다. 이러한 유형의 token는 RGB 세계에서는 이더리움의 ERC20, 즉 특정 기본 규칙(예: 전송, Supply 초기화 등)을 준수하는 대체 가능한 토큰에 해당한다고 볼 수 있습니다.


코드를 살펴보기 전에 RGB Schema의 일반적인 구조를 기억해 두는 것이 좋습니다. 일련의 선언이 프레임을 구성하고 있습니다:




- 다른 기본 Schema를 템플릿으로 사용했음을 나타내는 가능한 '스키마 아이디'입니다;
- **글로벌 상태** 및 **소유 상태**(엄격한 유형 포함);
- 원자가**(있는 경우)**;
- 이러한 상태와 원자를 참조할 수 있는 **작동**(Genesis, 상태 전환, 상태 확장)을 참조하세요;
- **엄격한 유형 시스템**은 데이터를 기술하고 검증하는 데 사용됩니다;
- 유효성 검사 스크립트**(AluVM을 통해 실행)**.


![RGB-Bitcoin](assets/en/072.webp)


아래 코드는 Rust Schema의 전체 정의를 보여줍니다. 아래 (1) ~ (9)의 주석에 따라 부분별로 주석을 달겠습니다:


```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {

// definitions of libraries and variables

// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),

// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},

// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},

// ===== PART 5: Valencies =====
valency_types: none!(),

// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},

// ===== PART 7: Extensions =====
extensions: none!(),

// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},

// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```




- (1) - **함수 헤더 및 하위 스키마**


'nia_schema()` 함수는 '하위 스키마'를 반환하는데, 이는 이 Schema이 보다 일반적인 Schema로부터 부분적으로 상속받을 수 있음을 나타냅니다. RGB 에코시스템에서는 이러한 유연성을 통해 마스터 Schema의 특정 표준 Elements을 재사용한 다음 해당 Contract에 특정한 규칙을 정의할 수 있습니다. 여기서는 `subset_of`가 `None`이 되므로 상속을 활성화하지 않도록 선택합니다.




- (2) - 일반 속성: **ffv, subset_of, type_system**


'fv` 속성은 Contract의 *빨리 감기* 버전에 해당합니다. 여기서 `zero!()` 값은 버전 0 또는 이 Schema의 초기 버전에 있음을 나타냅니다. 나중에 새로운 기능(새로운 유형의 작업 등)을 추가하려는 경우, 이 버전을 증가시켜 합의 변경을 나타낼 수 있습니다.


Subset_of: None` 속성은 상속이 없음을 확인합니다. Type_system` 필드는 `types` 라이브러리에 이미 정의된 엄격한 유형 시스템을 참조합니다. 이 줄은 Contract에서 사용하는 모든 데이터가 해당 라이브러리에서 제공하는 엄격한 직렬화 구현을 사용함을 나타냅니다.




- (3) - 글로벌 국가


글로벌_유형` 블록에서 4개의 Elements을 선언합니다. 나중에 참조하기 위해 `GS_NOMINAL` 또는 `GS_ISSUED_SUPPLY`와 같은 키를 사용합니다:




- gS_NOMINAL`은 생성된 token의 다양한 필드(전체 이름, 티커, 정밀도...)를 설명하는 `DivisibleAssetSpec` 유형을 참조합니다;
- 'GS_DATA'는 고지 사항, 메타데이터 또는 기타 텍스트와 같은 일반 데이터를 나타냅니다;
- 'GS_TIMESTAMP'는 발행 날짜를 나타냅니다;
- gS_ISSUED_SUPPLY`는 총 Supply, 즉 생성할 수 있는 토큰의 최대 개수를 설정합니다.


키워드 `once(...)`는 이러한 각 필드가 한 번만 표시될 수 있음을 의미합니다.




- (4) - 소유 유형


소유된 유형`에서 대체 가능한 상태를 설명하는 `OS_ASSET`을 선언합니다. StateSchema::Fungible(FungibleType::Unsigned64Bit)`을 사용하여 자산(토큰)의 수량이 64비트 부호 없는 정수로 저장되어 있음을 나타냅니다. 따라서 모든 트랜잭션은 이 token의 일정량을 전송하게 되며, 이 엄격한 숫자 구조에 따라 유효성이 검증됩니다.




- (5) - **밸런스**


밸런시_유형: none!()`을 표시하는데, 이는 이 Schema에 밸런시가 없음을, 즉 특별하거나 추가적인 권리(예: 재발행, 조건부 소각 등)가 없음을 의미합니다. Schema에 어떤 권한이 포함되어 있다면 이 섹션에 선언됩니다.




- (6) - Genesis: 첫 번째 작업


여기서 Contract 작업을 선언하는 부분으로 들어갑니다. Genesis은 다음과 같이 설명합니다:




- 메타데이터`가 없는 경우(필드 '메타데이터: Ty::<SemId>::UNIT.id(None)`);
- 각각 한 번씩 존재해야 하는 글로벌 상태(`한 번`);
- OS_ASSET`이 '한 번 이상'으로 표시되어야 하는 할당 목록. 즉, Genesis에는 하나 이상의 `OS_ASSET` Assignment(초기 보유자)가 필요합니다;
- 아니요 Valency: `값: 없음!()`.


초기 token 발행의 정의를 제한하는 방법은 다음과 같습니다. 발행된 Supply(`GS_ISSUED_SUPPLY`)과 하나 이상의 홀더(`OS_ASSET` 유형의 Owned State)를 선언해야 합니다.




- (7) - 확장 프로그램


'확장: 없음!()` 필드는 이 Contract에서 State Extension이 예상되지 않음을 나타냅니다. 즉, 디지털 권한(Valency)을 Redeem로 전환하거나 전환 전에 State Extension을 수행하는 작업이 없다는 뜻입니다. 모든 작업은 Genesis 또는 상태 전환을 통해 수행됩니다.




- (8) - 전환: TS_TRANSFER


트랜지션`에서는 `TS_TRANSFER` 작업 유형을 정의합니다. 이에 대해 설명합니다:




- 메타데이터가 없습니다;
- Global State(이미 Genesis에 정의되어 있음)는 수정하지 않습니다;
- 하나 이상의 `OS_ASSET`을 입력으로 받습니다. 즉, 기존 소유 상태를 사용해야 합니다;
- 하나 이상의 새로운 `OS_ASSET`을 생성(`할당`)합니다(즉, 수신자 또는 수신자가 토큰을 받습니다);
- 새로운 Valency은 생성되지 않습니다.


이는 UTXO에서 토큰을 소비한 다음 수신자에게 유리하도록 새로운 소유 상태를 생성하는 기본 전송의 동작을 모델링하여 입력과 출력 간의 총 금액의 동일성을 유지합니다.




- (9) - AluVM 스크립트 및 엔트리 포인트 **(프랑스어)**


마지막으로 AluVM 스크립트(`Script::AluVM(AluScript { ... })`)를 선언합니다. 이 스크립트에는 다음이 포함됩니다:




- 유효성 검사 중에 사용할 하나 이상의 외부 라이브러리(`lib`);
- AluVM 코드의 함수 오프셋을 가리키는 엔트리 포인트로, Genesis(`ValidateGenesis`)과 선언된 각 전환(`ValidateTransition(TS_TRANSFER)`)의 유효성 검사에 해당합니다.


이 유효성 검사 코드는 Business Logic을 적용하는 역할을 합니다. 예를 들어 확인합니다:




- Genesis 동안 `GS_ISSUED_SUPPLY`가 초과되지 않도록 합니다;
- '입력'(사용한 토큰)의 합계가 'TS_TRANSFER'에 대한 '할당'(받은 토큰)의 합계와 같아야 합니다.


이러한 규칙을 준수하지 않으면 전환이 유효하지 않은 것으로 간주됩니다.


"*비팽창형 대체 가능 자산*"의 예시입니다 Schema을 통해 간단한 RGB 대체 가능한 token Contract의 구조를 더 잘 이해할 수 있습니다. 데이터 설명(글로벌 및 소유 상태), 연산 선언(Genesis, 트랜지션, 확장), 검증 구현(AluVM 스크립트) 간의 분리를 명확하게 볼 수 있습니다. 이 모델 덕분에 token는 기존의 대체 가능한 token처럼 동작하지만 클라이언트 측에서 유효성을 검사하고 코드를 실행하기 위해 On-Chain 인프라에 의존하지 않습니다. 암호화 커미트먼트만 Bitcoin Blockchain에 고정됩니다.


### Interface


Interface은 Contract을 사용자(사람 읽기)와 포트폴리오(소프트웨어 읽기) 모두에서 읽고 조작할 수 있도록 설계된 Layer입니다. 따라서 Interface은 Business Logic의 내부 세부 사항을 드러내지 않고도 Contract의 기능 구조를 노출하고 명확히 한다는 점에서 객체 지향 프로그래밍 언어(Java, Rust 특성 등)에서 Interface과 유사한 역할을 수행합니다.


순수하게 선언적이고 바이너리 파일로 컴파일되어 그대로 사용하기 어려운 Schema과 달리, Interface은 필요한 읽기 키를 제공합니다:




- Contract에 포함된 글로벌 국가 및 소유 국가를 나열하고 설명합니다;
- 각 필드의 이름과 값에 액세스하여 표시할 수 있도록 합니다(예: token의 경우 시세, 최대 금액 등 확인);
- 데이터를 이해할 수 있는 이름과 연결하여 Contract 연산(Genesis, State Transition 또는 State Extension)을 해석하고 구성합니다(예: 이진 식별자 대신 '금액'을 명확하게 지정하여 전송 수행).


![RGB-Bitcoin](assets/en/073.webp)


예를 들어 Interface을 사용하면 필드를 조작하는 대신 '토큰 수', '자산 이름' 등의 레이블을 직접 조작하는 코드를 Wallet에서 작성할 수 있습니다. 이렇게 하면 Contract를 보다 직관적으로 관리할 수 있습니다. 이렇게 하면 Contract 관리가 더욱 직관적으로 됩니다.


#### 일반 작업


이 방법에는 많은 장점이 있습니다:




- **표준화:**


동일한 유형의 Contract를 표준 Interface에서 지원할 수 있으며, 여러 Wallet 구현 간에 공유할 수 있습니다. 이를 통해 호환성 및 코드 재사용이 용이해집니다.




- **Schema와 Interface의 명확한 분리:**


RGB 설계에서 Schema(Business Logic)와 Interface(프레젠테이션 및 조작)은 두 개의 독립된 개체입니다. Contract 로직을 작성하는 개발자는 인체공학이나 데이터 표현에 대한 걱정 없이 Schema에 집중할 수 있고, 다른 팀(또는 같은 팀이지만 다른 타임라인에 있는 팀)은 Interface을 개발할 수 있습니다.




- **유연한 진화:**


Contract를 변경하지 않고도 자산이 발행된 후 Interface을 수정하거나 추가할 수 있습니다. 이는 Interface(종종 실행 코드와 혼합)이 Blockchain에 고정되어 있는 일부 On-Chain Smart contract 시스템과 큰 차이점입니다.




- 멀티 Interface 기능


최종 사용자를 위한 간단한 Interface, 복잡한 구성 작업을 관리해야 하는 발급자를 위한 고급 인터페이스 등 각자의 필요에 따라 동일한 Contract을 서로 다른 인터페이스를 통해 노출할 수 있습니다. 그런 다음 Wallet는 용도에 따라 가져올 Interface을 선택할 수 있습니다.


![RGB-Bitcoin](assets/en/074.webp)


실제로 Wallet가 '.RGB` 또는 '.rgba` 파일을 통해 RGB Contract을 검색할 때 관련 Interface도 가져오는데, 이 역시 컴파일됩니다. 예를 들어 런타임에 Wallet는 다음과 같이 할 수 있습니다:




- 상태 목록을 찾아보고 이름을 읽으면 읽을 수 없는 숫자 식별자 대신 사용자 Interface에 티커, 개시 금액, 발행일 등이 표시됩니다;
- 명시적 매개변수 이름을 사용하여 작업(예: 전송)을 빌드하면, `assignments { OS_ASSET => 1 }`을 작성하는 대신 사용자에게 양식에 "금액" 필드를 제공하고 이 정보를 Contract에서 예상하는 엄격한 형식의 필드로 변환할 수 있습니다.


#### 이더리움 및 다른 시스템과의 차이점


이더리움에서 Interface(ABI를 통해 설명되는 *애플리케이션 바이너리 Interface*)은 일반적으로 On-Chain 저장 코드(Smart contract)에서 파생됩니다. Contract 자체를 건드리지 않고 Interface의 특정 부분을 수정하는 것은 비용이 많이 들거나 복잡할 수 있습니다. 그러나 RGB는 전적으로 off-chain 로직을 기반으로 하며, 데이터는 Bitcoin의 *커밋*에 고정되어 있습니다. 이 설계는 비즈니스 규칙의 유효성 검사가 Schema 및 참조된 AluVM 코드에 남아 있기 때문에 Contract의 기본 보안에 영향을 미치지 않고 Interface(또는 그 구현)을 수정할 수 있게 해줍니다.


#### Interface 편집


Schema과 마찬가지로 Interface은 소스 코드(주로 Rust)에 정의되며 '.RGB` 또는 '.rgba` 파일로 컴파일됩니다. 이 바이너리 파일에는 Wallet에 필요한 모든 정보가 포함되어 있습니다:




- 이름으로 필드를 식별합니다;
- 각 필드(및 해당 값)를 Contract에 정의된 엄격한 시스템 유형에 연결합니다;
- 허용되는 다양한 작업과 이를 구축하는 방법을 알아보세요.


Interface를 가져오면 Wallet는 Contract을 올바르게 표시하고 사용자에게 인터랙션을 제안할 수 있습니다.


### LNP/BP 협회에서 표준화한 인터페이스


RGB 에코시스템에서 Interface은 Contract의 데이터와 연산에 읽기 쉽고 조작 가능한 의미를 부여하는 데 사용됩니다. 따라서 Interface은 Business Logic를 내부적으로 설명하는 Schema을 보완합니다(엄격한 유형, 유효성 검사 스크립트 등). 이 섹션에서는 일반적인 Contract 유형(대체 가능한 토큰, NFT 등)을 위해 LNP/BP 협회에서 개발한 표준 인터페이스를 살펴보겠습니다.


다시 말해, 각 Interface은 Wallet 쪽에서 Contract을 표시하고 조작하는 방법을 설명하며, 필드 이름을 명확하게 지정하고(예: `spec`, `ticker`, `issuedSupply`...) 가능한 작업(예: `Transfer`, `Burn`, `Rename`...)을 정의한다는 아이디어가 있습니다. 이미 몇 가지 인터페이스가 운영되고 있지만 앞으로 더 많은 인터페이스가 추가될 예정입니다.


#### 바로 사용할 수 있는 몇 가지 인터페이스


**RGB20**은 대체 가능한 자산을 위한 Interface으로, 이더리움의 ERC20 표준과 비교할 수 있습니다. 하지만 한 단계 더 나아가 더 광범위한 기능을 제공합니다:




- 예를 들어, 자산이 발행된 후 이름을 변경(*티커* 또는 전체 이름 변경)하거나 정밀도를 조정(*주식 분할*)할 수 있는 기능입니다;
- 또한 특정 조건에서 자산을 소각한 다음 다시 생성할 수 있도록 발행자에게 권한을 부여하기 위해 2차 재발급(제한 또는 무제한) 및 소각 후 교체 메커니즘을 설명할 수도 있습니다;


예를 들어 RGB20 Interface는 비팽창형 초기 Supply를 부과하는 **비팽창형 자산(NIA) 체계**에 연결하거나 필요에 따라 다른 고급 체계에 연결할 수 있습니다.


**RGB21**은 NFT형 계약, 더 넓게는 디지털 미디어(이미지, 음악 등)의 표현과 같은 모든 고유 디지털 콘텐츠에 관한 것입니다. 단일 자산의 발행과 전송을 설명하는 것 외에도 다음과 같은 기능이 포함됩니다:




- Contract에 파일(최대 16MB)을 직접 포함할 수 있도록 통합 지원(클라이언트 측 검색용)합니다;
- 소유자가 기록에 "*각인*"을 입력하여 NFT의 과거 Ownership을 증명할 수 있는 가능성.


**RGB25**는 대체 가능한 측면과 대체 불가능한 측면을 결합한 하이브리드 표준입니다. 부동산 토큰화와 같이 하나의 루트 자산에 대한 링크를 유지하면서 자산을 분할하려는 경우(즉, 대체 불가능한 주택에 연결된 대체 가능한 주택 조각이 있는 경우) 부분적으로 대체 가능한 자산을 위해 설계되었습니다. 기술적으로 이 Interface은 원래 자산을 추적하면서 분할하는 개념을 고려한 **Collectible Fungible Asset** *(CFA)* Schema에 연결할 수 있습니다.


#### 개발 중인 인터페이스


다른 인터페이스는 보다 전문적인 용도로 계획되어 있지만 아직 제공되지 않습니다:




- 디지털 ID 전용 **RGB22**를 사용하여 RGB 에코시스템에서 식별자 및 On-Chain 프로필을 관리합니다;
- **RGB23**, 고급 타임스탬핑을 위해 *Opentimestamps*의 일부 아이디어를 사용하지만 추적 기능이 있는 고급 타임스탬프입니다;
- **RGB24**는 *이더리움 네임 서비스*와 유사한 탈중앙화 도메인 네임 시스템(DNS)을 지향합니다;
- RGB26**은 보다 복잡한 형식(거버넌스, 투표 등)의 DAO(*탈중앙화 자율 조직*)를 관리하도록 설계되었습니다;
- RGB20과 매우 유사하지만 탈중앙화된 초기 발행을 고려하고 스테이트 익스텐션을 사용한다는 특수성이 있는 **RGB30**. 이는 여러 기관이 재발행을 관리하거나 더 세밀한 조건이 적용되는 자산에 사용될 수 있습니다.


물론 이 과정을 참조하는 날짜에 따라 이러한 인터페이스가 이미 작동하고 액세스할 수 있을 수도 있습니다.


#### Interface 예제


이 Rust 코드 스니펫은 [RGB20](https://github.com/RGB-WG/RGB-std/blob/master/src/Interface/rgb20.rs) Interface(대체 가능한 자산)를 보여줍니다. 이 코드는 표준 RGB 라이브러리의 `rgb20.rs` 파일에서 가져온 것입니다. 이를 통해 Interface의 구조를 이해하고, 한편으로는 Business Logic(Schema에 정의됨)과 지갑과 사용자에게 노출되는 기능 사이의 다리를 제공하는 방법을 살펴보겠습니다.


```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());

Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```


이 Interface에서는 Global State, 소유 상태, Contract 작업(Genesis 및 전환), 오류 처리의 선언이 Schema 구조와 유사하다는 점을 발견할 수 있습니다. 그러나 Interface는 Wallet 또는 기타 애플리케이션을 위한 이러한 Elements의 표시 및 조작에 중점을 둡니다.


Schema과의 차이점은 타입의 성격에 있습니다. Schema은 엄격한 타입(예: `FungibleType::Unsigned64Bit`)과 더 많은 기술 식별자를 사용합니다. Interface는 필드 이름, 매크로(`fname!()`, `tn!()`), 인자 클래스(`ArgSpec`, `OwnedIface::Rights`...)에 대한 참조를 사용합니다. 여기서는 Elements의 기능적 이해와 Wallet에 대한 구성을 용이하게 하는 것이 목표입니다.


또한 Interface는 최종적으로 검증된 클라이언트 측 로직과 일관성을 유지하는 한 기본 Schema에 추가 기능(예: `번에포크` 권한 관리)을 도입할 수 있습니다. Schema의 AluVM "스크립트" 섹션은 암호화 유효성을 보장하고, Interface는 사용자(또는 Wallet)가 이러한 상태 및 전환과 상호 작용하는 방법을 설명합니다.


#### Global State 및 과제


글로벌 상태` 섹션에는 `spec`(자산 설명), `데이터`, `생성`, `발행 공급`, `소각 공급`, `교체 공급`과 같은 필드가 있습니다. 이러한 필드는 Wallet가 읽고 표시할 수 있는 필드입니다. 예를 들어




- spec`을 입력하면 token 구성이 표시됩니다;
- 발행된 공급량` 또는 `소각된 공급량`은 발행되거나 소각된 토큰의 총 개수 등을 알려줍니다.


'할당' 섹션에서는 다양한 역할 또는 권한을 정의합니다. 예를 들어




- 자산 소유자`는 토큰 보유에 해당합니다(대체 가능한 *Owned State*);
- burnRight`는 토큰을 소각하는 기능에 해당합니다;
- updateRight`는 에셋 이름을 변경할 수 있는 권한에 해당합니다.


공개` 또는 `비공개` 키워드(예: `AssignIface::공개(...)`는 이러한 상태가 공개(`공개`) 또는 비공개(`비공개`)인지를 나타냅니다.) 요청::없음`, `요청::선택`의 경우, 예상되는 발생을 나타냅니다.


#### Genesis 및 전환


'Genesis' 부분은 에셋이 초기화되는 방법을 설명합니다:




- Spec`, `데이터`, `생성된`, `발행된공급` 필드는 필수입니다(`ArgSpec::필수()`);
- 자산 소유자`와 같은 할당은 여러 복사본에 존재할 수 있으므로(`ArgSpec::many()`) 여러 초기 소유자에게 토큰을 배포할 수 있습니다;
- 인플레이션 허용치` 또는 `번에포크`와 같은 필드는 Genesis에 포함될 수도 있고 포함되지 않을 수도 있습니다.


그런 다음 각 트랜지션(`전송`, `발행`, `소각`...)에 대해 Interface은 작업이 입력으로 예상하는 필드, 작업이 출력으로 생성할 필드 및 발생할 수 있는 오류를 정의합니다. 예를 들어


**전환:**




- 입력: 이전` → `자산 소유자`여야 합니다;
- 할당: 수혜자` → 새로운 `자산 소유자`가 됩니다;
- 오류: `NON_EQUAL_AMOUNTS`(따라서 Wallet은 입력 합계가 출력 합계와 일치하지 않는 경우를 처리할 수 있습니다).


**전환 `이슈`:**




- 추가 방출이 반드시 활성화되는 것은 아니므로 선택 사항(`옵션: true`)으로 설정합니다;
- 입력: 사용됨` → `인플레이션 허용량`, 즉 토큰을 더 추가할 수 있는 권한입니다;
- 할당: '수혜자'(신규 토큰 수령) 및 '미래'(남은 '인플레이션 허용치');
- 가능한 오류: '공급_미스매치', '발행_초과_허용' 등


**굽기 전환:**




- 입력: 사용` → `burnRight`;
- 전역: `burnedSupply` 필수;
- 할당: '미래' → 모든 것을 소각하지 않은 경우 'burnRight'의 가능한 연속입니다;
- 오류: 공급_불일치`, `무효_증명`, `부족_범위`.


따라서 각 작업은 Wallet에서 읽을 수 있는 방식으로 설명됩니다. 이를 통해 사용자가 명확하게 볼 수 있는 곳에 그래픽 Interface를 표시할 수 있습니다: "귀하는 소각할 권리가 있습니다. 일정량을 소각하시겠습니까? 이 코드는 '소각 공급' 필드를 채우고 '소각 권리'가 유효한지 확인합니다.


요약하자면, Interface가 아무리 완벽하더라도 그 자체로 Contract의 내부 로직을 정의하지는 않는다는 점을 명심해야 합니다. 작업의 핵심은 엄격한 유형, Genesis 구조, 전환 등을 포함하는 **Schema**에 의해 수행됩니다. Interface는 이러한 Elements을 애플리케이션에서 사용할 수 있도록 보다 직관적이고 명명된 방식으로 노출할 뿐입니다.


RGB의 모듈성 덕분에 Contract 전체를 다시 작성하지 않고도 Interface를 업그레이드(예: `이름 바꾸기` 전환 추가, 필드 표시 수정 등)할 수 있습니다. 이 Interface 사용자는 '.RGB` 또는 '.rgba` 파일을 업데이트하는 즉시 이러한 개선 사항의 혜택을 누릴 수 있습니다.


하지만 Interface을 선언한 후에는 해당 Schema에 연결해야 합니다. 이는 ***Interface Implementation***를 통해 이루어지며, 이는 각 명명된 필드(예: `fname!("assetOwner")`)를 Schema에 정의된 엄격한 ID(예: `OS_ASSET`)에 매핑하는 방법을 지정합니다. 예를 들어, Wallet가 `burnRight` 필드를 조작할 때, 이는 Schema에서 토큰을 소각하는 기능을 설명하는 상태임을 보장합니다.


### Interface Implementation


RGB 아키텍처에서는 각 구성 요소(Schema, Interface 등)가 독립적으로 개발 및 컴파일될 수 있음을 확인했습니다. 그러나 이러한 서로 다른 구성 요소를 서로 연결하는 필수 요소가 하나 더 있는데, 바로 ***Interface Implementation***입니다. 이것은 Schema(Business Logic 쪽)에 정의된 식별자 또는 필드를 Interface(프레젠테이션 및 사용자 상호 작용 쪽)에 선언된 이름에 명시적으로 매핑하는 역할을 합니다. 따라서 Wallet가 Contract을 로드할 때 어떤 필드가 무엇에 해당하는지, Interface에서 명명된 작업이 Schema의 로직과 어떻게 관련되는지 정확히 이해할 수 있습니다.


중요한 점은 Interface Implementation가 반드시 모든 Schema 기능이나 모든 Interface 필드를 노출하기 위한 것이 아니라 하위 집합으로 제한될 수 있다는 것입니다. 실제로는 이를 통해 Schema의 특정 측면을 제한하거나 필터링할 수 있습니다. 예를 들어, 네 가지 유형의 연산이 있는 Schema이 있지만 주어진 컨텍스트에서 그 중 두 가지만 매핑하는 구현 Interface가 있을 수 있습니다. 반대로 Interface가 추가 엔드포인트를 제안하는 경우 여기서는 이를 구현하지 않도록 선택할 수 있습니다.


다음은 *비팽창형 에셋*(NIA) Schema를 RGB20 Interface에 연결한 Interface Implementation의 대표적인 예시입니다:


```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();

IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```


이 구현에서는 Interface:




- 우리는 `nia_schema()`를 통해 Schema를 명시적으로 참조하고 `Rgb20::iface()`를 통해 Interface를 참조합니다. Schema.schema_id()` 및 `iface.iface_id()` 호출은 컴파일 측에서 Interface Implementation을 Anchor에 사용합니다(이 두 구성 요소의 암호화 식별자를 연결합니다);
- Schema Elements과 Interface Elements 사이에 매핑이 설정됩니다. 예를 들어, Schema의 `GS_NOMINAL` 필드는 Interface 쪽의 `"spec"` 문자열에 연결됩니다(`NamedField::with(GS_NOMINAL, fname!("spec"))`). Interface에서 `"Transfer"`에 연결되는 `TS_TRANSFER`와 같은 작업도 동일하게 수행합니다...;
- 원자가(`valencies: none!()`)나 확장자(`extensions: none!()`)가 없는 것을 볼 수 있는데, 이는 이 NIA Contract이 이러한 기능을 사용하지 않는다는 사실을 반영합니다.


컴파일 후 결과는 별도의 '.RGB` 또는 '.rgba` 파일로 생성되며, Schema 및 Interface과 함께 Wallet으로 가져올 수 있습니다. 따라서 소프트웨어는 이 NIA Contract(로직은 Schema로 설명됨)을 "RGB20" Interface(인간 이름과 대체 가능한 토큰의 상호 작용 모드 제공)에 구체적으로 연결하여 둘 사이의 게이트웨이로 이 Interface Implementation를 적용하는 방법을 알고 있습니다.


#### Interface Implementation를 분리하는 이유는 무엇인가요?


분리는 유연성을 향상시킵니다. 단일 Schema에는 각각 다른 기능 세트를 매핑하는 여러 개의 고유한 Interface 구현이 있을 수 있습니다. 또한 Schema이나 Interface을 변경하지 않고도 Interface Implementation 자체를 발전시키거나 재작성할 수 있습니다. 프로토콜에 의해 부과된 호환성 규칙(동일한 식별자, 유형의 일관성 등)을 준수하는 한 각 구성 요소(Schema, Interface, Interface Implementation)는 독립적으로 버전 및 업데이트할 수 있다는 RGB의 모듈성 원칙을 유지합니다.


실제 사용 시 Wallet이 Contract을 로드할 때는 반드시 Contract을 로드해야 합니다:




- 컴파일된 **Schema**을 로드합니다(Business Logic의 구조를 파악하기 위해);
- 컴파일된 **Interface**를 로드합니다(이름 및 사용자 측 작업을 이해하기 위해);
- 컴파일된 **Interface Implementation**를 로드합니다(Schema 로직을 Interface 이름, 연산별, 필드별로 연결하기 위해).


이 모듈식 아키텍처는 다음과 같은 사용 시나리오를 가능하게 합니다:




- 특정 사용자에 대한 특정 작업 제한: 예를 들어 굽기 또는 업데이트 기능을 제공하지 않고 기본 전송에 대한 액세스 권한만 부여하는 부분 구현 Interface을 제공하세요;
- 프레젠테이션 변경: Interface의 필드 이름을 바꾸거나 Contract의 기초를 변경하지 않고 다르게 매핑하는 Interface Implementation를 디자인합니다;
- 다중 스키마 지원: Wallet은 구조가 호환되는 경우 동일한 Interface 유형에 대해 여러 Interface 구현을 로드하여 서로 다른 스키마(서로 다른 token 로직)를 처리할 수 있습니다.


다음 장에서는 Contract 송금이 작동하는 방식과 RGB 송장이 생성되는 방식에 대해 살펴보겠습니다.


## Contract 전송


<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>


:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::


이 장에서는 RGB 에코시스템에서 Contract이 전송되는 과정을 분석해 보겠습니다. 이를 설명하기 위해 평소 주인공인 Alice과 Bob이 RGB 자산인 Exchange를 RGB로 이전하고자 하는 경우를 살펴보겠습니다. 또한 `RGB` 명령줄 도구에서 발췌한 몇 가지 명령을 보여드리며 실제로 어떻게 작동하는지 살펴보겠습니다.


### RGB Contract 전송 이해


Alice와 Bob 간의 전송을 예로 들어 보겠습니다. 이 예에서는 Bob이 이제 막 RGB을 사용하기 시작했고, Alice는 이미 Wallet에 RGB 자산을 보유하고 있다고 가정합니다. Bob이 자신의 환경을 설정하고 관련 Contract을 가져온 다음 Alice에 전송을 요청하고 마지막으로 Alice가 Bitcoin Blockchain에서 실제 거래를 수행하는 방법을 살펴보겠습니다.


#### 1) RGB Wallet 설치하기


우선 Bob는 프로토콜과 호환되는 소프트웨어, 즉 RGB Wallet를 설치해야 합니다. 여기에는 처음부터 계약이 포함되어 있지 않습니다. Bob도 필요합니다:




- UTXO를 관리하기 위한 Bitcoin Wallet;
- Bitcoin 노드(또는 일렉트럼 서버)에 연결하여 UTXO를 식별하고 네트워크에서 트랜잭션을 전파할 수 있습니다.


다시 한 번 말씀드리자면, RGB의 **소유 상태**는 Bitcoin UTXO를 나타냅니다. 따라서 저희는 항상 Bitcoin 데이터를 가리키는 암호화 커미트먼트(`Tapret` 또는 `Opret`)를 통합하는 RGB 트랜잭션에서 UTXO를 관리하고 사용할 수 있어야 합니다.


#### 2) Contract 정보 수집


그런 다음 Bob는 관심 있는 Contract 데이터를 검색해야 합니다. 이 데이터는 웹사이트, 이메일, 메시징 애플리케이션 등 모든 채널을 통해 유통될 수 있습니다. 실제로는 ***Consignment***, 즉 작은 데이터 패킷으로 함께 그룹화됩니다:




- Contract의 초기 상태를 정의하는 **Genesis**;
- Business Logic(엄격한 유형, 유효성 검사 스크립트 등)을 설명하는 **Schema**를 참조하세요;
- 프레젠테이션 Layer(필드 이름, 액세스 가능한 작업)을 정의하는 **Interface**;
- Schema와 Interface을 구체적으로 연결하는 **Interface Implementation**.


![RGB-Bitcoin](assets/en/075.webp)


각 구성요소의 무게는 일반적으로 200바이트 미만이므로 총 크기는 수 킬로바이트 정도인 경우가 많습니다. 이 Consignment을 Base58, 검열 방지 채널(예: Nostr 또는 Lightning Network 등)을 통해 또는 QR 코드로 방송할 수도 있습니다.


#### 3) Contract 가져오기 및 유효성 검사


Bob이 Consignment을 받으면 이를 RGB Wallet로 가져옵니다. 그러면 이렇게 됩니다:




- Genesis 및 Schema이 유효한지 확인합니다;
- Interface 및 Interface Implementation를 로드합니다;
- 클라이언트 측 데이터 Stash을 업데이트하세요.


Bob는 이제 Wallet에서 자산을 보고(아직 소유하고 있지 않더라도) 어떤 필드를 사용할 수 있는지, 어떤 작업이 가능한지 파악할 수 있습니다. 그런 다음 이전할 자산을 실제로 소유한 사람에게 연락해야 합니다. 이 예에서는 Alice입니다.


특정 RGB 자산을 보유한 사람을 찾는 과정은 Bitcoin 지급자를 찾는 과정과 유사합니다. 이 연결의 세부 사항은 용도(마켓플레이스, 비공개 채팅 채널, 송장 발행, 상품 및 서비스 판매, 급여...)에 따라 다릅니다.


#### 4) Invoice 발급


RGB 자산의 이전을 시작하려면 Bob에서 먼저 Invoice을 발급해야 합니다. 이 Invoice이 사용됩니다:




- Alice에 수행할 작업 유형을 알려줍니다(예: RGB20 Interface에서 '전송');
- Alice에게 Bob의 *Seal Definition*(즉, 그가 자산을 받고자 하는 UTXO)을 제공합니다;
- 필요한 활성 성분의 수량을 지정합니다(예: 100단위).


Bob는 명령줄에서 `RGB` 도구를 사용합니다. ContractId`가 알려진 token 100개를 원하고, `Tapret`에 의존하며, UTXO(`456e3..dfe1:0`)을 지정한다고 가정해 보겠습니다:


```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```


이 장의 마지막 부분에서 RGB 송장의 구조에 대해 자세히 살펴보겠습니다.


#### 5) Invoice 전송


생성된 Invoice(예: URL: `RGB:2WBcas9.../RGB20/100+utxob:...`)에는 Alice이 전송을 준비하는 데 필요한 모든 정보가 포함되어 있습니다. Consignment과 마찬가지로 컴팩트하게 인코딩(Base58 또는 다른 형식)하여 메시징 애플리케이션, 이메일, Nostr...을 통해 전송할 수 있습니다.


![RGB-Bitcoin](assets/en/076.webp)


#### 6) Alice 측에서의 트랜잭션 준비


Alice은 Bob의 Invoice을 받습니다. RGB의 Wallet에는 이전할 자산이 포함된 Stash가 있습니다. 자산이 포함된 UTXO을 사용하려면 먼저 자신이 가진 UTXO을 사용하여 PSBT(*Partially Signed Bitcoin Transaction*), 즉 불완전한 Bitcoin 트랜잭션을 generate로 보내야 합니다:


```bash
alice$ wallet construct tx.psbt
```


이 기본 트랜잭션(현재는 서명되지 않음)은 Bob로의 전송에 연결된 암호화 Commitment를 Anchor에 사용하는 데 사용됩니다. 따라서 Alice의 UTXO이 소비되고, 출력에는 Bob에 대한 `Tapret` 또는 `Opret` Commitment가 배치됩니다.


#### 7) 전송 Consignment 생성


다음으로 Alice는 명령을 통해 ***Terminal Consignment***("전송 Consignment"이라고도 함)을 빌드합니다:


```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```


이 새로운 `Consignment.RGB` 파일에는 다음이 포함됩니다:




- 현재 시점(Genesis 이후)까지 에셋을 검증하는 데 필요한 상태 전환의 전체 기록입니다;
- Alice에서 Bob로 자산을 이전하는 새로운 State Transition은 Invoice Bob가 발행한 Invoice에 따라 발행되었습니다;
- Alice의 Single-Use Seal을 사용하는 불완전한 Bitcoin 트랜잭션(*Witness Transaction*)(`tx.PSBT`)은 암호화 Commitment를 Bob에 포함하도록 수정되었습니다.


이 단계에서는 트랜잭션이 아직 Bitcoin 네트워크에 브로드캐스트되지 않습니다. Consignment은 자산의 합법성을 증명하는 전체 내역(*증명 체인*)을 포함하므로 기본 Consignment보다 규모가 더 큽니다.


#### 8) Bob은 Consignment를 확인하고 수락합니다


Alice는 이 **Terminal Consignment**을 Bob으로 전송합니다. 그러면 Bob이




- State Transition의 유효성을 확인합니다(이력이 일관성이 있는지, Contract 규칙이 준수되는지 등);
- 로컬 Stash에 추가하세요;
- Consignment에 서명(`sig:...`)을 추가하여 검토 및 승인되었음을 증명할 수 있습니다("*급여 명세서*"라고도 함).


```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```


![RGB-Bitcoin](assets/en/077.webp)


#### 9) 옵션: Bob이 Alice(*급여 명세서*)로 확인을 다시 보냅니다


Bob가 원하면 이 서명을 Alice에게 다시 보낼 수 있습니다. 이것은 다음을 나타냅니다:




- 전환을 유효한 것으로 인식합니다;
- Bitcoin 트랜잭션이 방송되는 것에 동의합니다.


이는 의무 사항은 아니지만 Alice에 이전과 관련하여 추후 분쟁이 발생하지 않을 것이라는 확신을 줄 수 있습니다.


#### 10) Alice가 거래에 서명하고 게시합니다


그러면 Alice이 가능합니다:




- Bob의 서명을 확인합니다(`RGB 확인 <sig>`);
- **Witness Transaction**에 서명하면 여전히 PSBT(`Wallet 기호`)이 됩니다;
- Witness Transaction를 Bitcoin 네트워크에 게시합니다(`-publish`).


```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```


![RGB-Bitcoin](assets/en/078.webp)


확인되면 이 트랜잭션은 전송이 완료된 것으로 표시됩니다. Bob이 자산의 새 소유자가 됩니다. 이제 Owned State가 자신이 관리하는 UTXO을 가리키며, 거래에 Commitment가 존재한다는 것이 증명됩니다.


전체 이전 프로세스를 요약하면 다음과 같습니다:


![RGB-Bitcoin](assets/en/079.webp)


### RGB 전송의 장점




- **기밀 유지**:


Alice와 Bob만이 모든 State Transition 데이터에 액세스할 수 있습니다. 이들은 위탁을 통해 이 정보를 Blockchain 외부로 Exchange 전송합니다. Bitcoin 거래의 암호화 약정은 자산의 유형이나 금액을 공개하지 않으므로 다른 On-Chain token 시스템보다 훨씬 더 높은 기밀성을 보장합니다.




- **고객 측 검증**:


Bob은 *Consignment*을 Bitcoin Blockchain의 *앵커*와 비교하여 전송의 일관성을 확인할 수 있습니다. 타사 검증이 필요하지 않습니다. Alice은 Blockchain에 전체 기록을 게시할 필요가 없으므로 기본 프로토콜의 부하가 줄어들고 기밀성이 향상됩니다.




- 단순화된 **원자성**:


복잡한 교환(예: BTC와 RGB 자산 간의 아토믹 스왑)을 단일 트랜잭션 내에서 수행할 수 있으므로 HTLC 또는 PTLC 스크립트가 필요하지 않습니다. 합의가 브로드캐스트되지 않으면 누구나 다른 방식으로 UTXO를 재사용할 수 있습니다.


### 전송 요약 다이어그램


송장을 자세히 살펴보기 전에 RGB 송금의 전체 흐름을 요약한 도표가 있습니다:




- Bob은 RGB Wallet을 설치하고 초기 Contract Consignment를 얻습니다;
- Bob는 자산을 받을 수 있는 UTXO을 언급하는 Invoice을 발행합니다;
- Alice는 Invoice를 수신하여 PSBT을 빌드하고 Terminal Consignment을 생성합니다;
- Bob이 이를 수락하고 확인한 후 자신의 Stash에 데이터를 추가하고 필요한 경우 서명(*급여명세서*)합니다;
- Alice은 Bitcoin 네트워크에 트랜잭션을 게시합니다;
- 거래가 확인되면 전송이 공식적으로 완료됩니다.


![RGB-Bitcoin](assets/en/080.webp)


이 전송은 RGB 프로토콜의 모든 힘과 유연성을 보여줍니다: 클라이언트 측에서 검증된 비공개 Exchange, Bitcoin Blockchain에 최소한으로 신중하게 고정되고 프로토콜의 최고의 보안을 유지(Double-spending의 위험 없음)합니다. 따라서 RGB은 On-Chain 프로그래머블 블록체인보다 더 기밀성이 높고 확장 가능한 가치 전송을 위한 유망한 생태계가 될 것입니다.


### 송장 RGB


이 섹션에서는 RGB 생태계에서 **인보이스**가 어떻게 작동하는지, 그리고 이를 통해 Contract로 작업(특히 송금)을 수행하는 방법을 자세히 설명해드리겠습니다. 먼저 사용된 식별자를 살펴본 다음, 식별자가 인코딩되는 방식을 살펴보고 마지막으로 URL(지갑에서 사용하기에 편리한 형식)로 표현되는 Invoice의 구조를 살펴보겠습니다.


#### 식별자 및 인코딩


고유 식별자는 다음 Elements 각각에 대해 정의됩니다:




- RGB Contract;
- Schema(Business Logic);
- Interface 및 Interface Implementation;
- 자산(토큰, 대체 불가능한 토큰 등),


시스템의 각 구성 요소를 구별할 수 있어야 하므로 이러한 고유성은 매우 중요합니다. 예를 들어, Contract X를 다른 Contract Y와 혼동해서는 안 되며, 서로 다른 두 인터페이스(예: RGB20 대 RGB21)에는 고유한 식별자가 있어야 합니다.


이러한 식별자를 효율적이고(작은 크기) 가독성 있게 만들기 위해 다음과 같은 방법을 사용합니다:




- Base58 인코딩은 혼란스러운 문자(예: `0`과 문자 `O`)의 사용을 피하고 비교적 짧은 문자열을 제공합니다;
- 식별자의 성격을 나타내는 접두사로, 일반적으로 `RGB:` 또는 이와 유사한 URN 형식입니다.


예를 들어, `ContractId`는 다음과 같이 표현할 수 있습니다:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


'RGB:` 접두사는 이것이 HTTP 링크나 다른 프로토콜이 아닌 RGB 식별자임을 확인합니다. 이 접두사 덕분에 지갑은 문자열을 올바르게 해석할 수 있습니다.


#### 식별자 세분화


기본 (암호화) 보안을 위해 256비트 이상의 필드가 필요할 수 있으므로 RGB 식별자는 상당히 긴 경우가 많습니다. 사람이 쉽게 읽고 확인할 수 있도록 이러한 문자열을 하이픈(`-`)으로 구분된 여러 블록으로 *청크*합니다. 즉, 끊김 없이 긴 문자열을 사용하는 대신 더 짧은 블록으로 나누는 것입니다. 이 방식은 신용카드나 전화번호에서 흔히 사용되는 방식이며, 인증의 용이성을 위해 여기에도 적용됩니다. 예를 들어 사용자나 파트너에게 다음과 같이 말할 수 있습니다: "*세 번째 블록이 `9GEgnyMj7`*인지 확인해 주세요."라고 말하면 전체를 한 번에 비교하지 않아도 됩니다. 마지막 블록은 오류나 오타 감지 시스템을 갖추기 위해 **체크섬**으로 사용되는 경우가 많습니다.


예를 들어, base58로 인코딩되고 세그먼트화된 `ContractId`가 될 수 있습니다:


```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


각 대시는 문자열을 섹션으로 나눕니다. 이는 코드의 의미에는 영향을 주지 않고 표시에만 영향을 줍니다.


#### 인보이스에 URL 사용


RGB Invoice는 URL로 제공됩니다. 즉, 클릭하거나 스캔(QR코드)하면 Wallet이 이를 직접 해석하여 트랜잭션을 수행할 수 있습니다. 이러한 간단한 상호 작용은 소프트웨어의 여러 필드에 다양한 데이터를 복사하여 붙여넣어야 하는 다른 시스템과는 다릅니다.


대체 가능한 token(예: RGB20 token)의 Invoice는 다음과 같이 보일 수 있습니다:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


이 URL을 분석해 보겠습니다:




- gW-1898: **(접두사)**: RGB 프로토콜을 호출하는 링크를 나타냅니다(다른 맥락에서는 `http:` 또는 `Bitcoin:`와 유사);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`: 조작하려는 token의 `ContractId`를 나타낼 수 있습니다;
- **rGB20/100**: `RGB20` Interface을 사용하며 100개의 에셋을 요청함을 나타냅니다. 구문은 다음과 같습니다: `/Interface/금액`;
- utxob:`**: 수신자 UTXO(또는 더 정확하게는 Single-Use Seal의 정의)에 대한 정보가 추가되도록 지정합니다;
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`: 이것은 *blinded* UTXO(또는 Seal Definition)입니다. 즉, Bob가 자신의 정확한 UTXO을 마스킹했기 때문에 발신자(Alice)는 정확한 Address가 무엇인지 알지 못합니다. 그녀는 Bob가 제어하는 UTXO을 참조하는 유효한 Seal이 있다는 것만 알고 있습니다.


모든 것이 하나의 URL에 들어 있기 때문에 Wallet에서 간단히 클릭하거나 스캔하기만 하면 작업을 실행할 준비가 완료됩니다.


컨트랙트아이디` 대신 간단한 티커(예: `USDT`)가 사용되는 시스템을 상상할 수 있습니다. 그러나 이는 신뢰와 보안에 큰 문제를 야기할 수 있습니다. 티커는 고유한 참조가 아니기 때문입니다(여러 컨트랙트가 `USDT`라고 주장할 수 있습니다). RGB를 사용하면 고유하고 모호하지 않은 암호화 식별자가 필요합니다. 따라서 base58로 인코딩되고 세그먼트화된 256비트 문자열을 채택했습니다. 사용자는 다른 어떤 것이 아니라 `2WBcas9-yjz...`라는 ID를 가진 Contract을 정확하게 조작하고 있다는 것을 알 수 있습니다.


#### 추가 URL 매개변수


HTTP와 같은 방식으로 URL에 다음과 같은 추가 매개변수를 추가할 수도 있습니다:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```




- sig=...`: 예를 들어, 일부 지갑에서 확인할 수 있는 Invoice과 관련된 서명을 나타냅니다;
- Wallet가 이 서명을 관리하지 않으면 이 매개변수를 무시합니다.


RGB21 Interface를 통한 NFT의 경우를 예로 들어보겠습니다. 예를 들어


```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


여기 있습니다:




- `RGB:`**: URL 접두사;
- **`7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Contract ID (NFT);
- **rGB21**: 대체 불가능한 자산(NFT)을 위한 Interface;
- **`DbwzvSu-4BZU81jEp-...`**: NFT의 고유 부분(예: 데이터 블롭의 Hash(미디어, 메타데이터...))에 대한 명시적 참조입니다;
- **`+utxob:egXsFnw-...`**: Seal Definition.


Wallet이 해석할 수 있는 고유 링크를 전송하여 전송할 고유 자산을 명확하게 식별하는 것은 동일합니다.


#### URL을 통한 기타 작업


RGB URL은 단순히 송금을 요청하는 데만 사용되는 것이 아닙니다. 새 토큰 발행(*발행*)과 같은 고급 작업도 인코딩할 수 있습니다. 예를 들어


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


여기에서 찾을 수 있습니다:




- `RGB:`: 프로토콜;
- `2WBcas9-...`: Contract ID;
- rGB20/issue/100000`: "*발행*" 트랜지션을 호출하여 100,000개의 토큰을 추가로 생성할 것임을 나타냅니다;
- `+utxob:`: Seal Definition.


예를 들어 Wallet는 다음과 같이 표시될 수 있습니다: "저는 'RGB20' Interface에서 '문제' 작업을 수행해 달라는 요청을 받았습니다. 이런 Contract에서 10만 대를 위해, 이런 Single-Use Seal의 이익을 위해."


이제 Elements 프로그래밍의 주요 RGB에 대해 살펴봤으니 다음 장에서는 RGB Contract을 작성하는 방법에 대해 설명하겠습니다.


## 스마트 컨트랙트 작성


<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>


:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::


이 장에서는 명령줄 도구인 `RGB`을 사용하여 Contract를 작성하는 방법을 단계별로 살펴보겠습니다. CLI을 설치 및 조작하고, **Schema**을 컴파일하고, **Interface**와 **Interface Implementation**을 임포트한 다음 에셋을 발행(*발행*)하는 방법을 보여드리는 것이 목표입니다. 또한 컴파일 및 상태 유효성 검사를 포함한 기본 로직도 살펴봅니다. 이 장이 끝나면 프로세스를 재현하고 자신만의 RGB 컨트랙트를 생성할 수 있을 것입니다.


다시 한 번 말씀드리지만, RGB의 내부 로직은 Rust 라이브러리를 기반으로 하며, 개발자는 프로젝트에 가져와서 Client-side Validation 부분을 관리할 수 있습니다. 또한 LNP/BP 협회 팀은 다른 언어에 대한 바인딩 작업을 진행 중이지만 아직 확정되지 않았습니다. 또한 비트파이넥스와 같은 다른 단체에서도 자체 통합 스택을 개발하고 있습니다(이에 대해서는 강좌의 마지막 2장에서 다룰 예정입니다). 따라서 당분간은 상대적으로 다듬어지지 않은 상태이긴 하지만 `RGB` CLI이 공식적인 참조입니다.


### RGB 도구의 설치 및 프레젠테이션


메인 명령은 간단히 'RGB'라고 불립니다. 이는 `git`과 유사하게 설계되었으며, 컨트랙트 조작, 호출, 자산 발행 등을 위한 일련의 하위 명령이 포함되어 있습니다. Bitcoin Wallet은 현재 통합되지 않았지만 곧 출시될 버전(0.11)에 포함될 예정입니다. 이 다음 버전에서는 사용자가 (설명자를 통해) 'RGB'에서 직접 지갑을 생성하고 관리할 수 있으며, PSBT 세대, 서명을 위한 외부 하드웨어(예: Hardware Wallet)와의 호환성, Sparrow 같은 소프트웨어와의 상호운용성 등이 포함될 것입니다. 이렇게 하면 전체 자산 발행 및 이전 시나리오가 간소화됩니다.


#### 카고를 통한 설치


Rust에 도구를 설치합니다:


```bash
cargo install rgb-contracts --all-features
```


(참고: 상자의 이름은 `RGB-contracts`이며, 설치된 명령의 이름은 `RGB`입니다. 이미 `RGB`이라는 이름의 상자가 존재했다면 충돌이 발생했을 수 있으므로 이름이 달라집니다.)


이 설치는 많은 종속성(예: 명령 구문 분석, Electrum 통합, 영지식 증명 관리 등)을 컴파일합니다.


설치가 완료되면


```bash
rgb
```


(인수 없이) `RGB`을 실행하면 `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer` 등과 같은 사용 가능한 하위 명령 목록이 표시됩니다. 로컬 스토리지 디렉토리(모든 로그, 회로도 및 구현이 저장된 Stash)를 변경하거나 네트워크(Testnet, Mainnet)를 선택하거나 일렉트럼 서버를 구성할 수 있습니다.


![RGB-Bitcoin](assets/en/081.webp)


#### 컨트롤의 첫 번째 개요


다음 명령을 실행하면 기본적으로 `RGB20` Interface이 이미 통합되어 있는 것을 확인할 수 있습니다:


```bash
rgb interfaces
```


이 Interface가 통합되지 않은 경우 복제하세요:


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


![RGB-Bitcoin](assets/en/082.webp)


반면에 Schema는 아직 소프트웨어로 가져오지 않았다고 들었습니다. Stash에는 Contract도 없습니다. 이를 확인하려면 다음 명령을 실행하세요:


```bash
rgb schemata
```


그런 다음 리포지토리를 복제하여 특정 도식을 검색할 수 있습니다:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-Bitcoin](assets/en/083.webp)


이 저장소에는 `src/` 디렉토리에 스키마("*비팽창형 자산*"의 NIA, "*유니크 디지털 자산*"의 UDA 등)를 정의하는 여러 Rust 파일(예: `nia.rs`)이 포함되어 있습니다. 컴파일하려면 실행하면 됩니다:


```bash
cd rgb-schemata
cargo run
```


이렇게 하면 컴파일된 도식에 해당하는 여러 개의 `.RGB` 및 `.rgba` 파일이 생성됩니다. 예를 들어, `NonInflatableAsset.RGB`가 있습니다.


#### Schema 및 Interface Implementation 가져오기


이제 회로도를 `RGB`로 임포트할 수 있습니다:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-Bitcoin](assets/en/084.webp)


이렇게 하면 로컬 Stash에 추가됩니다. 다음 명령을 실행하면 이제 Schema가 나타나는 것을 볼 수 있습니다:


```bash
rgb schemata
```


### Contract 생성(발행)


새 에셋을 만드는 방법에는 두 가지가 있습니다:




- Rust의 스크립트 또는 코드를 사용하여 Schema 필드(Global State, 소유 주 등)를 채워 Contract을 작성하고 '.RGB` 또는 '.rgba` 파일을 생성합니다;
- 또는 token의 속성을 설명하는 YAML(또는 TOML) 파일과 함께 `issue` 하위 명령을 직접 사용하세요.


'예제' 폴더의 Rust에서 '계약 빌더'를 빌드하고, 'Global State'(자산 이름, 티커, Supply, 날짜 등)을 채우고, Owned State(UTXO가 할당된)을 정의한 다음 이 모든 것을 *Contract Consignment*로 컴파일하여 내보내기, 검증 및 Stash으로 가져올 수 있는 방법을 설명하는 예시를 찾을 수 있습니다.


다른 방법은 YAML 파일을 수동으로 편집하여 `티커`, `이름`, `Supply` 등을 사용자 지정하는 것입니다. 파일 이름이 `RGB20-demo.yaml`이라고 가정합니다. 지정할 수 있습니다:




- `spec`: 티커, 이름, 정밀도;
- '용어': 법적 고지를 위한 필드입니다;
- 발행된 공급량`: 발행된 token의 양입니다;
- '과제': Single-Use Seal(*Seal Definition*)와 잠금 해제된 수량을 나타냅니다.


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


![RGB-Bitcoin](assets/en/085.webp)


그런 다음 명령을 실행하기만 하면 됩니다:


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-Bitcoin](assets/en/086.webp)


제 경우 고유 Schema 식별자(작은따옴표로 묶어야 함)는 `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k`이고 발급자를 넣지 않았습니다. 그래서 제 주문은


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Schema ID를 모르는 경우 다음 명령을 실행하세요:


```bash
rgb schemata
```


CLI는 새로운 Contract가 발급되어 Stash에 추가되었다고 응답합니다. 다음 명령을 입력하면 방금 발급된 Contract에 해당하는 Stash이 추가로 발급된 것을 볼 수 있습니다:


```bash
rgb contracts
```


![RGB-Bitcoin](assets/en/087.webp)


그런 다음 다음 명령은 글로벌 상태(이름, 티커, Supply...)와 소유 상태 목록, 즉 할당을 표시합니다(예: UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`에 정의된 1백만 `PBN`토큰).


```bash
rgb state '<ContractId>'
```


![RGB-Bitcoin](assets/en/088.webp)


### 내보내기, 가져오기 및 유효성 검사


이 Contract을 다른 사용자와 공유하려면 Stash에서 a로 내보내면 됩니다:


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-Bitcoin](assets/en/089.webp)


MyContractPBN.RGB` 파일을 다른 사용자에게 전달할 수 있으며, 이 사용자는 다음 명령을 사용하여 자신의 Stash에 추가할 수 있습니다:


```bash
rgb import myContractPBN.rgb
```


가져올 때 간단한 *Contract Consignment*인 경우 "`Consignment RGB 가져오기 중`"이라는 메시지가 표시됩니다. 더 큰 *State Transition Consignment*인 경우 명령이 달라집니다(`RGB accept`).


유효성을 보장하기 위해 로컬 유효성 검사 기능을 사용할 수도 있습니다. 예를 들어, 실행할 수 있습니다:


```bash
rgb validate myContract.rgb
```


#### Stash 사용, 검증 및 표시


다시 한 번 말씀드리자면, Stash은 스키마, 인터페이스, 구현 및 컨트랙트(Genesis + 전환)의 로컬 인벤토리입니다. '가져오기'를 실행할 때마다 Stash에 요소가 추가됩니다. 이 Stash은 명령을 사용하여 자세히 볼 수 있습니다:


```bash
rgb dump
```


![RGB-Bitcoin](assets/en/090.webp)


이렇게 하면 generate 전체에 대한 세부 정보가 있는 폴더가 Stash가 됩니다.


### 이전 및 PSBT


이전을 수행하려면 로컬 Bitcoin Wallet를 조작하여 `Tapret` 또는 `Opret` 커밋을 관리해야 합니다.


#### generate 및 Invoice


대부분의 경우, Contract의 참여자(예: Alice과 Bob) 간의 상호작용은 Invoice 생성을 통해 이루어집니다. Alice이 Bob가 무언가를 실행하기를 원하는 경우(token 전송, 재발행, DAO에서의 작업 등), Alice은 Bob에 대한 자신의 지시를 자세히 설명하는 Invoice을 생성합니다. 이렇게 합니다:




- **Alice** (Invoice 발행자);
- **Bob**(Invoice를 수신하고 실행하는 사람).


다른 생태계와 달리 RGB Invoice은 결제의 개념에 국한되지 않습니다. 키 취소, 투표, NFT에 각인(*각인*) 생성 등 Contract에 연결된 모든 요청을 포함할 수 있습니다. 해당 작업은 Contract Interface에서 설명할 수 있습니다. 해당 작업은 Contract Interface에 설명되어 있습니다.


다음 명령은 RGB Invoice을 생성합니다:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


With:




- `$Contract`: Contract 식별자(*ContractId*);
- `$Interface`: 사용할 Interface(예: `RGB20`);
- `$ACTION`: Interface에 지정된 작업의 이름(간단한 대체 가능한 token 전송의 경우, "Transfer"일 수 있음). Interface가 이미 기본 작업을 제공하는 경우 여기에 다시 입력할 필요가 없습니다;
- `$STATE`: 전송할 상태 데이터(예: 대체 가능한 token가 전송되는 경우 토큰의 양);
- `$Seal`: 수혜자(Alice)의 Single-Use Seal, 즉 UTXO에 대한 명시적 참조. Bob은 이 정보를 사용하여 Witness Transaction를 빌드하고 해당 출력은 Alice에 속하게 됩니다(*blinded UTXO* 또는 암호화되지 않은 형태).


예를 들어 다음 명령을 사용합니다


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI는 generate와 마찬가지로 Invoice이 될 것입니다:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


모든 채널(텍스트, QR코드 등)을 통해 Bob로 전송할 수 있습니다.


#### 송금하기


이 Invoice에서 전송하려면:




- Bob(Stash에 토큰을 보유한 사람)은 Bitcoin Wallet를 가지고 있습니다. 그는 필요한 RGB 토큰이 있는 UTXO를 사용하는 Bitcoin 트랜잭션(예: `tx.PSBT`)과 통화(Exchange)를 위한 UTXO 트랜잭션(예: PSBT 형태)을 준비해야 합니다;
- Bob는 다음 명령을 실행합니다:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- 이렇게 하면 `Consignment.RGB` 파일이 생성됩니다:
 - 토큰이 진짜임을 증명하는 트랜잭션 이력을 Alice에 제공합니다;
 - 토큰을 Alice의 Single-Use Seal로 이전하는 새로운 전환입니다;
 - Witness Transaction(서명되지 않음).
- Bob는 이 `Consignment.RGB` 파일을 Alice으로 전송합니다(이메일, 공유 서버 또는 RGB-RPC 프로토콜, Storm 등을 통해);
- Alice은 `Consignment.RGB`을 수신하고 자체 Stash에서 이를 받아들입니다:


```bash
alice$ rgb accept consignment.rgb
```




- CLI은 전환의 유효성을 검사하여 Alice의 Stash에 추가합니다. 유효하지 않은 경우 자세한 오류 메시지와 함께 명령이 실패합니다. 그렇지 않으면 성공하고 샘플 트랜잭션이 아직 Bitcoin 네트워크에 브로드캐스트되지 않았다고 보고합니다(Bob는 Alice의 Green 표시를 기다리고 있음);
- 확인을 위해 `수락` 명령은 Alice이 *Consignment*의 유효성을 검사했음을 보여주기 위해 Bob에게 보낼 수 있는 서명(*급여 명세서*)을 반환합니다;
- 그런 다음 Bob은 자신의 Bitcoin 트랜잭션에 서명하고 게시(`--게시`)할 수 있습니다:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- 이 거래가 On-Chain로 확인되는 즉시 자산의 Ownership은 Alice로 이전된 것으로 간주됩니다. 트랜잭션의 Mining를 모니터링하는 Alice의 Wallet은 자신의 Stash에 새로운 Owned State가 나타나는 것을 확인합니다.


다음 장에서는 RGB을 Lightning Network에 통합하는 방법에 대해 자세히 살펴보겠습니다.


## RGB의 Lightning Network


<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>


:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::


이 장에서는 Lightning Network 내에서 RGB를 사용하여 off-chain 결제 채널을 통해 RGB 자산(토큰, NFT 등)을 통합하고 이동하는 방법을 살펴볼 것을 제안합니다.


기본 아이디어는 RGB State Transition(*State Transition*)을 Bitcoin 트랜잭션에 커밋할 수 있으며, 이는 다시 라이트닝 채널이 닫힐 때까지 off-chain로 유지될 수 있다는 것입니다. 따라서 채널이 업데이트될 때마다 새로운 RGB State Transition을 새 커밋 트랜잭션에 통합하여 이전 전환을 무효화할 수 있습니다. 이러한 방식으로 라이트닝 채널을 사용하여 RGB 자산을 전송할 수 있으며, 기존 라이트닝 결제와 동일한 방식으로 라우팅할 수 있습니다.


### 채널 생성 및 펀딩


RGB 에셋을 전송하는 라이트닝 채널을 생성하려면 두 개의 Elements이 필요합니다:




- 채널의 2/2 Multisig(채널의 기본 UTXO)를 만들기 위한 Bitcoin 자금입니다;
- RGB 펀딩을 통해 동일한 Multisig로 자산을 전송합니다.


Bitcoin 조건에서 펀딩 트랜잭션은 소량의 Sats만 포함하더라도 기준 UTXO을 정의하기 위해 존재해야 합니다(향후 Commitment 트랜잭션의 각 산출량이 모두 동일하게 Dust 한도 이상으로 유지되는 문제일 뿐입니다). 예를 들어, Alice은 10k Sats와 500 USDT(RGB 자산으로 발행)를 제공하기로 결정할 수 있습니다. 펀딩 트랜잭션에서 Commitment(`Opret` 또는 `Tapret`)을 추가하여 RGB State Transition을 앵커링합니다.


![RGB-Bitcoin](assets/en/091.webp)


펀딩 트랜잭션이 준비되면(아직 브로드캐스트되지 않은 상태) Commitment 트랜잭션이 생성되어 어느 쪽이든 언제든지 일방적으로 채널을 닫을 수 있습니다. 이러한 트랜잭션은 새로운 State Transition에 연결된 RGB Anchor(OP_RETURN 또는 Taproot)를 포함하는 추가 출력을 추가한다는 점을 제외하면 Lightning의 기존 Commitment 트랜잭션과 유사합니다.


그런 다음 RGB State Transition는 자금의 2/2 Multisig에서 Commitment Transaction의 출력으로 자산을 이동합니다. 이 프로세스의 장점은 RGB 상태의 보안이 라이트닝의 징벌 메커니즘과 정확히 일치한다는 것입니다. Bob이 오래된 채널 상태를 브로드캐스트하면 Alice가 그를 처벌하고 출력을 소비하여 Sats 토큰과 RGB 토큰을 모두 회수할 수 있다는 것입니다. 따라서 공격자는 Sats뿐만 아니라 채널의 RGB 자산도 잃을 수 있기 때문에 RGB 자산이 없는 라이트닝 채널보다 인센티브가 훨씬 더 강력합니다.


따라서 Alice가 서명하고 Bob으로 전송된 Commitment Transaction은 다음과 같이 보입니다:


![RGB-Bitcoin](assets/en/092.webp)


그리고 Bob이 서명하여 Alice로 보낸 Commitment Transaction은 다음과 같이 보입니다:


![RGB-Bitcoin](assets/en/093.webp)


### 채널 업데이트


두 채널 참여자 간에 결제가 발생하거나 자산 배분을 변경하고자 할 때, 두 채널 참여자는 새로운 Commitment 트랜잭션 쌍을 생성합니다. 각 출력의 Sats에 있는 금액은 구현에 따라 변경되지 않을 수도 있고 변경될 수도 있는데, 그 주된 역할은 유효한 UTXO를 구성하는 것이기 때문입니다. 반면, OP_RETURN(또는 Taproot) 출력은 채널의 새로운 자산 분배를 나타내는 새로운 RGB Anchor을 포함하도록 수정해야 합니다.


예를 들어, Alice이 채널에서 Bob로 30 USDT를 전송하면, 새로운 State Transition에는 Alice에 400 USDT, Bob에 100 USDT의 잔액이 반영됩니다. 커밋 트랜잭션은 이 전환을 포함하도록 OP_RETURN/Taproot Anchor에 추가(또는 수정)됩니다. RGB의 관점에서 볼 때, 전환에 대한 입력은 초기 Multisig(채널이 닫힐 때까지 On-Chain 자산이 실제로 할당되는 곳)로 유지된다는 점에 유의하세요. 결정된 재분배에 따라 RGB 출력(할당)만 변경됩니다.


Commitment Transaction는 Alice이 서명하고 Bob이 배포할 준비가 되었습니다:


![RGB-Bitcoin](assets/en/094.webp)


Commitment Transaction는 Bob가 서명했고, Alice이 배포할 준비가 되었습니다:


![RGB-Bitcoin](assets/en/095.webp)


### HTLC 관리


실제로 Lightning Network은 HTLC(*해시된 시간 고정 계약*)를 사용하여 여러 채널을 통해 결제를 라우팅할 수 있습니다. RGB도 마찬가지입니다. 채널을 통해 전송되는 모든 결제에 대해 커밋 트랜잭션에 HTLC 출력이 추가되고, 이 HTLC에 연결된 RGB 할당이 추가됩니다. 따라서 HTLC 출력을 사용하는 사람은 (비밀 덕분에 또는 타임락이 만료된 후) Sats과 관련 RGB 자산을 모두 회수합니다. 반면에 Sats과 RGB 자산 모두 충분한 현금이 있어야 합니다.


![RGB-Bitcoin](assets/en/096.webp)


따라서 Lightning에서 RGB의 작동은 Lightning Network 자체의 작동과 병행하여 고려해야 합니다. 이 주제에 대해 더 자세히 알아보고 싶다면 다른 종합 교육 과정을 살펴볼 것을 적극 권장합니다:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### RGB 코드 맵


마지막으로 다음 섹션으로 넘어가기 전에 RGB에 사용된 코드에 대한 개요를 알려드리고자 합니다. 이 프로토콜은 일련의 Rust 라이브러리와 오픈 소스 사양을 기반으로 합니다. 다음은 주요 리포지토리와 크레이트에 대한 개요입니다:


![RGB-Bitcoin](assets/en/097.webp)


#### Client-side Validation




- **리포지토리**: [클라이언트_사이드_검증](https://github.com/LNP-BP/client_side_validation)
- **크레이트**: [클라이언트_사이드_검증](https://crates.io/crates/client_side_validation), [싱글유즈_씰](https://crates.io/crates/single_use_seals)


off-chain 유효성 검사 및 일회용 씰 로직 관리.


#### 결정론적 Bitcoin 커미트먼트(DBC)




- **리포지토리**: [bp-core](https://github.com/BP-WG/bp-core)
- **Crate**: [bp-dbc](https://crates.io/crates/bp-dbc)


Bitcoin 트랜잭션의 결정론적 앵커링 관리(Tapret, OP_RETURN 등).


#### Multi Protocol Commitment(MPC)




- **리포지토리**: [클라이언트_사이드_검증](https://github.com/LNP-BP/client_side_validation)
- **Crate**: [commit_verify](https://crates.io/crates/commit_verify)


다양한 참여 조합 및 다양한 프로토콜과의 통합.


#### 엄격한 유형 및 엄격한 인코딩




- **사양**: [웹사이트 strict-types.org](https://www.strict-types.org/)
- **리포지토리**: [엄격한 유형](https://github.com/strict-types/strict-types), [엄격한 인코딩](https://github.com/strict-types/strict-encoding)
- **Crates**: [엄격_유형](https://crates.io/crates/strict_types), [엄격_인코딩](https://crates.io/crates/strict_encoding)


Client-side Validation에는 엄격한 타이핑 시스템과 결정론적 직렬화가 사용되었습니다.


#### RGB 코어




- **리포지토리**: [RGB-core](https://github.com/RGB-WG/RGB-core)
- **Crate**: [RGB-core](https://crates.io/crates/RGB-core)


RGB 검증의 주요 로직을 포괄하는 프로토콜의 핵심입니다.


#### RGB 표준 라이브러리 및 Wallet




- **리포지토리**: [RGB-std](https://github.com/RGB-WG/RGB-std)
- **Crate**: [RGB-std](https://crates.io/crates/RGB-std)


표준 구현, Stash 및 Wallet 관리.


#### RGB CLI




- **리포지토리**: [RGB](https://github.com/RGB-WG/RGB)
- **상자**: [RGB-CLI](https://crates.io/crates/RGB-CLI), [RGB-Wallet](https://crates.io/crates/RGB-Wallet)


컨트랙트의 커맨드 라인 조작을 위한 `RGB` CLI 및 상자 Wallet.


#### RGB Schema




- **리포지토리**: [RGB-schemata](https://github.com/RGB-WG/RGB-schemata/)


스키마(NIA, UDA 등) 및 그 구현의 예가 포함되어 있습니다.


#### AluVM




- **Info**: [AluVM.org](https://www.AluVM.org/)
- **리포지토리**: [AluVM-spec](https://github.com/AluVM/AluVM-spec), [alure](https://github.com/AluVM/alure)
- **크레이트**: [AluVM](https://crates.io/crates/AluVM), [알루아스](https://crates.io/crates/aluasm)


유효성 검사 스크립트를 실행하는 데 사용되는 레지스트리 기반 가상 머신입니다.


#### Bitcoin 프로토콜 - BP




- **리포지토리**: [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-Wallet](https://github.com/BP-WG/bp-Wallet)


Bitcoin 프로토콜(트랜잭션, 바이패스 등)을 지원하는 애드온.


#### 유비쿼터스 결정론적 컴퓨팅 - UBIDECO




- **저장소**: [유비데코](https://github.com/UBIDECO)


오픈 소스 결정론적 개발과 연결된 에코시스템.


# RGB을 기반으로 구축


<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>


## DIBA와 비트마스크 프로젝트


<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>


:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::


이 과정의 마지막 섹션은 RGB 부트캠프에서 다양한 연사들이 진행한 프레젠테이션을 기반으로 합니다. 여기에는 RGB와 그 생태계에 대한 평가와 반성, 그리고 프로토콜을 기반으로 한 도구와 프로젝트에 대한 프레젠테이션이 포함됩니다. 첫 번째 챕터의 사회는 Hunter Beast가, 다음 두 챕터의 사회는 Frederico Tenga가 맡았습니다.


### JavaScript에서 Rust로, 그리고 Bitcoin 에코시스템으로의 전환


처음에는 헌터 비스트는 주로 자바스크립트로 작업했습니다. 그러다 **Rust**를 발견했는데, 처음에는 문법이 매력적이지 않고 답답해 보였습니다. 그러나 그는 이 언어의 강력한 성능, 메모리(*heap* 및 *stack*)에 대한 제어, 보안 및 성능에 대해 높이 평가하게 되었습니다. 그는 Rust가 컴퓨터 작동 원리를 심도 있게 이해할 수 있는 훌륭한 교육장이라고 강조합니다.


헌터 비스트는 이더리움(솔리디티, 타입스크립트 등)과 이후 파일코인 등 *Altcoin* 생태계의 다양한 프로젝트에 참여했던 자신의 배경에 대해 이야기합니다. 그는 처음에는 일부 프로토콜에 깊은 인상을 받았지만 결국 대부분의 프로토콜에 환멸을 느꼈다고 설명하며, 특히 토큰 노믹스 때문에 더욱 그랬다고 말합니다. 그는 모호한 재정적 인센티브, 투자자를 희석시키는 토큰의 인플레이션 생성, 그리고 이러한 프로젝트의 잠재적인 착취적 측면을 비난합니다. 그래서 그는 결국 Bitcoin의 건전한 경제 메커니즘과 이 시스템의 견고함에 눈을 뜬 일부 사람들 덕분에 **Bitcoin Maximalist** 입장을 채택하게 되었습니다.


### RGB의 매력과 레이어 기반 구축


그의 말에 따르면 Bitcoin의 관련성을 결정적으로 확신하게 된 것은 RGB과 레이어 개념의 발견이었습니다. 그는 다른 블록체인의 기존 기능을 기본 프로토콜을 변경하지 않고도 Bitcoin 이상의 상위 레이어에서 재현할 수 있다고 믿었습니다.


2022년 2월, 그는 **DIBA**에 합류하여 RGB, 특히 **비트마스크** Wallet에 대해 집중적으로 작업했습니다. 당시 비트마스크는 아직 0.01 버전이었고, 단일 토큰 관리용으로만 0.4 버전의 RGB을 실행하고 있었습니다. 그는 로직이 부분적으로 서버 기반이었기 때문에 오늘날보다 자기 관리 지향적이지 않았다고 말합니다. 그 이후로 아키텍처는 이 모델로 발전해왔고, 비트코인 사용자들은 이를 높이 평가했습니다.


### RGB 프로토콜의 기초


**RGB** 프로토콜은 2012~2013년경에 이미 모색된 *컬러 코인* 개념의 가장 최근의 가장 발전된 구현입니다. 당시에는 여러 팀이 서로 다른 Bitcoin 값을 UTXO에 연결하려고 했기 때문에 여러 가지 구현이 흩어져 있었습니다. 당시에는 표준화의 부족과 낮은 수요로 인해 이러한 솔루션이 지속적인 발판을 마련하지 못했습니다.


오늘날 RGB은 개념적 견고성과 LNP/BP 협회를 통한 통일된 사양으로 주목받고 있습니다. 이 원칙은 Client-side Validation을 기반으로 합니다. Bitcoin Blockchain은 암호화 약정(_약정_, Taproot 또는 OP_RETURN를 통해)만 저장하고 대부분의 데이터(Contract 정의, 전송 내역 등)는 해당 사용자가 저장합니다. 이러한 방식으로 Blockchain에 부담을 주지 않으면서 스토리지 부하를 분산하고 거래소의 기밀성을 강화할 수 있습니다. 이러한 접근 방식을 통해 모듈식 확장 가능한 프레임워크 내에서 대체 가능한 자산(**RGB20** 표준) 또는 고유 자산(**RGB21** 표준)을 생성할 수 있습니다.


### token 기능(RGB20) 및 고유 에셋(RGB21)


**RGB20**을 사용하면 Bitcoin에서 대체 가능한 token을 정의할 수 있습니다. 발행자는 *공급*, *정확도*를 선택하고 전송을 할 수 있는 *계약*을 생성합니다. 각 전송은 **Single-Use Seal** 역할을 하는 Bitcoin UTXO를 참조합니다. 이 로직은 UTXO를 사용할 수 있는 사람만이 클라이언트 측 Contract의 상태를 업데이트하는 키를 실제로 보유하고 있기 때문에 사용자가 동일한 자산을 두 번 사용할 수 없도록 보장합니다.


**RGB21**은 고유 에셋(또는 "NFT")을 대상으로 합니다. 자산의 Supply은 1이며, 특정 필드를 통해 설명된 메타데이터(이미지 파일, 오디오 등)와 연결될 수 있습니다. 퍼블릭 블록체인의 NFT와 달리, 데이터와 해당 MIME 식별자는 소유자의 재량에 따라 비공개로 분산된 P2P로 유지될 수 있습니다.


### 비트마스크 솔루션: RGB용 Wallet


RGB의 기능을 실제로 활용하기 위해 **DIBA** 프로젝트는 [Bitmask](https://bitmask.app/)라는 Wallet를 설계했습니다. 이 아이디어는 웹 애플리케이션 또는 브라우저 확장으로 액세스할 수 있는 비수탁형 Taproot 기반 도구를 제공하는 것입니다. Bitmask는 RGB20과 RGB21 자산을 모두 관리하고 다양한 보안 메커니즘을 통합합니다:




- 핵심 코드는 Rust으로 작성된 후 WebAssembly로 컴파일되어 JavaScript 환경(React)에서 실행됩니다;
- 키는 로컬에서 생성된 후 로컬에 암호화되어 저장됩니다;
- 상태 데이터(Stash)는 메모리에 보관되며, Blake3를 사용하여 압축, 오류 수정, 암호화 및 스트림 검증을 수행하는 **Carbonado** 라이브러리를 통해 직렬화 및 암호화됩니다.


이 아키텍처 덕분에 모든 자산 거래는 클라이언트 측에서 이루어집니다. 외부에서 보면 Bitcoin 트랜잭션은 전형적인 Taproot 지출 거래에 지나지 않으며, 대체 가능한 토큰이나 NFT를 전송한다고 의심할 사람은 아무도 없습니다. On-Chain 오버로딩(공개적으로 저장된 메타데이터 없음)이 없기 때문에 어느 정도의 재량권이 보장되며 검열 시도에 쉽게 저항할 수 있습니다.


### 보안 및 분산 아키텍처


RGB 프로토콜이 각 참여자에게 트랜잭션 기록을 보관하도록 요구하는 한(수신한 전송의 유효성을 증명하기 위해), 스토리지 문제가 발생합니다. 비트마스크는 이 Stash를 로컬에서 직렬화한 다음 여러 서버 또는 클라우드(선택 사항)로 전송할 것을 제안합니다. 데이터는 **카보네이도**를 통해 사용자가 암호화된 상태로 유지되므로 서버에서 읽을 수 없습니다. 부분적으로 손상된 경우 오류 수정 Layer이 콘텐츠를 재구성할 수 있습니다.


충돌 없는 복제 데이터 유형_(CRDT)을 사용하면 서로 다른 버전의 Stash을 병합할 수 있습니다. 하나의 Full node에 자산에 연결된 모든 정보가 담겨 있지 않기 때문에 누구나 원하는 곳에 자유롭게 데이터를 호스팅할 수 있습니다. 이는 각 소유자가 Client-side Validation 자산의 유효성에 대한 증거를 저장할 책임이 있는 *RGB* 철학을 정확히 반영한 것입니다.


### 더 넓은 에코시스템을 향해: 마켓플레이스, 상호 운용성 및 새로운 기능


비트마스크는 단순한 Wallet 개발에만 국한하지 않습니다. DIBA는 더 많은 것을 개발하고자 합니다:




- 토큰을 교환할 수 있는 **마켓플레이스**, 특히 **RGB21** 형태의 토큰을 교환할 수 있습니다;
- 다른 지갑과의 호환성(예: *Iris Wallet*);
- **전송 일괄 처리** 기술, 즉 단일 트랜잭션에 여러 개의 연속적인 RGB 전송을 포함할 수 있습니다.


동시에, 저희는 **WebBTC** 또는 **WebLN**(웹사이트가 Wallet에 Bitcoin 또는 라이트닝 거래에 서명하도록 요청할 수 있는 표준)과 오디날 항목을 "텔레번"(Ordals를 보다 신중하고 유연한 RGB 형식으로 송환하려는 경우)하는 기능에 대해 작업하고 있습니다.


### 결론


전체 프로세스는 강력한 기술 솔루션을 통해 RGB 에코시스템이 어떻게 배포되고 최종 사용자가 액세스할 수 있는지를 보여줍니다. Altcoin의 관점에서 Bitcoin 중심의 비전으로의 전환은 *Client-side Validation*의 발견과 함께 상당히 논리적인 경로를 보여줍니다. 저희는 Blockchain를 포크하지 않고도 Taproot 거래 또는 OP_RETURNS의 암호화 약속을 활용하여 다양한 기능(대체 가능한 토큰, NFT, 스마트 계약 등)을 구현하는 것이 가능하다는 것을 이해하게 되었습니다.


**비트마스크** Wallet는 이러한 접근 방식의 일부입니다. Blockchain 측에서는 일반적인 Bitcoin 트랜잭션만 표시되고, 사용자 측에서는 웹 Interface를 조작하여 모든 종류의 Exchange 자산을 생성하고 저장합니다. 이 모델은 화폐 인프라(Bitcoin)와 발행 및 전송 로직(RGB)을 명확하게 분리하는 동시에 높은 수준의 기밀성과 더 나은 확장성을 보장합니다.


## 비트파이넥스의 RGB 작업


<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>


:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::


이 장에서는 프레데리코 텐가의 발표를 바탕으로, 이 프로토콜을 중심으로 풍부하고 다양한 생태계의 출현을 촉진하기 위해 비트파이넥스 팀이 RGB 전용으로 만든 일련의 도구와 프로젝트에 대해 살펴봅니다. 이 팀의 초기 목표는 특정 상용 제품을 출시하는 것이 아니라 소프트웨어 빌딩 블록을 제공하고, RGB 프로토콜 자체에 기여하며, 모바일 Wallet(*아이리스 Wallet*) 또는 RGB 호환 라이트닝 노드와 같은 구체적인 구현 레퍼런스를 제안하는 것이었습니다.


### 배경 및 목표


2022년경부터 비트파이넥스 RGB 팀은 RGB을 효율적으로 활용하고 테스트할 수 있는 기술 스택을 개발하는 데 집중해왔습니다. 여러 가지 기여가 이루어졌습니다:




- 개선 제안서 작성, 버그 수정 등을 포함한 소스 코드 및 프로토콜 사양에 참여합니다;
- 개발자가 애플리케이션에 RGB을 간편하게 통합할 수 있는 도구입니다;
- 아이리스](https://iriswallet.com/)라는 이름의 모바일 Wallet를 설계하여 RGB 사용의 모범 사례를 실험하고 설명합니다;
- RGB 에셋으로 채널을 관리할 수 있는 맞춤형 라이트닝 노드를 생성합니다;
- 다양성과 강력한 생태계를 장려하기 위해 RGB에서 솔루션을 구축하는 다른 팀을 지원합니다.


이 접근 방식은 Wallet을 구현할 수 있는 로우레벨 라이브러리(*[RGBlib](https://github.com/RGB-Tools/RGB-lib)*)부터 프로덕션 측면(라이트닝 노드, 안드로이드용 Wallet 등)에 이르는 전체 요구 사항을 포괄하는 것을 목표로 합니다.


### RGBlib 라이브러리: RGB 애플리케이션 개발 간소화


RGB 지갑과 애플리케이션을 민주적으로 만드는 데 있어 중요한 점은 개발자가 프로토콜의 내부 로직에 대해 모든 것을 배울 필요가 없도록 충분히 간단한 추상화를 제공하는 것입니다. 이것이 바로 Rust로 작성된 **RGBlib**의 목표입니다.


RGBlib은 이전 장에서 살펴본 RGB의 매우 유연하지만 때로는 복잡한 요구사항과 애플리케이션 개발자의 구체적인 요구사항 사이의 가교 역할을 합니다. 즉, token 전송, 자산 발행, 검증 등을 관리하고자 하는 Wallet(또는 서비스)은 모든 암호화 세부 사항이나 사용자 정의 가능한 모든 RGB 파라미터를 알지 못해도 RGBlib에 의존할 수 있습니다.


서점에서 제공합니다:




- 자산(대체 가능 여부와 상관없이) 발행(_발행_)을 위한 턴키 기능;
- 간단한 객체(주소, 금액, UTXO 등)를 조작하여 자산을 전송(송금/수신)하는 기능입니다;
- Client-side Validation에 필요한 상태 정보(*커미션*)를 저장하고 로드하는 메커니즘입니다.


따라서 RGBlib은 RGB(Client-side Validation, Tapret/Opret 앵커)에 특정한 복잡한 개념에 의존하지만 이를 캡슐화하여 최종 애플리케이션에서 모든 것을 다시 프로그래밍하거나 위험한 결정을 내릴 필요가 없도록 합니다. 또한 RGBlib은 이미 여러 언어(Kotlin 및 Python)로 바인딩되어 있어 단순한 Rust 유니버스를 넘어 다양한 용도로 사용할 수 있는 길이 열려 있습니다.


### Iris Wallet: Android에서 RGB Wallet의 예시


RGBlib의 효과를 증명하기 위해 비트파이넥스 팀은 현재 안드로이드 전용으로 **아이리스 Wallet**을 개발했습니다. 이는 모바일 Wallet로, 자산을 발행하고, 전송하고, 받고, 이력을 확인할 수 있으며, 셀프 커스터디 모델을 유지하면서 일반 Bitcoin과 유사한 사용자 경험을 보여줍니다.


Iris에는 여러 가지 흥미로운 기능이 있습니다:


**Electrum 서버 사용:**


다른 Wallet와 마찬가지로 아이리스도 Blockchain의 트랜잭션 확인에 대해 알아야 합니다. 아이리스는 완전한 노드를 내장하지 않고 기본적으로 비트파이넥스 팀이 관리하는 일렉트럼 서버를 사용합니다. 그러나 사용자는 자체 서버 또는 다른 타사 서비스를 구성할 수 있습니다. 이러한 방식으로 Bitcoin 트랜잭션의 유효성을 검사하고 모듈식 방식으로 정보를 검색(인덱싱)할 수 있습니다.


**RGB 프록시 서버:**


Bitcoin과 달리 RGB은 발신자와 수신자 간에 off-chain 메타데이터(*위임*)의 Exchange이 필요합니다. 이 프로세스를 간소화하기 위해 Iris는 프록시 서버를 통해 통신이 이루어지는 솔루션을 제공합니다. 수신 Wallet은 발신자가 *클라이언트 측* 데이터를 전송해야 하는 위치를 언급하는 *Invoice*를 생성합니다. 기본적으로 URL은 비트파이넥스 팀이 호스팅하는 프록시를 가리키지만, 이 프록시를 변경하거나 직접 호스팅할 수 있습니다. 이 아이디어는 복잡한 추가 조작 없이 수신자가 QR 코드를 표시하고 발신자가 이 코드를 스캔하여 거래를 진행하는 익숙한 사용자 환경으로 돌아가는 것입니다.


**연속 백업:**


엄밀히 말해 Bitcoin의 경우, 일반적으로 seed을 백업하는 것으로 충분합니다(요즘은 seed과 설명자를 백업하는 것을 권장하지만). RGB의 경우 이것만으로는 충분하지 않습니다. RGB 자산을 실제로 소유하고 있음을 증명하는 로컬 기록(*위임장*)도 보관해야 합니다. 영수증을 받을 때마다 디바이스는 새로운 데이터를 저장하며, 이는 이후 지출에 필수적입니다. Iris는 사용자의 Google 드라이브에서 암호화된 백업을 자동으로 관리합니다. 백업이 암호화되므로 Google을 특별히 신뢰할 필요가 없으며, 향후에는 타사 운영자에 의한 검열이나 삭제 위험을 피하기 위해 개인 서버와 같은 더 강력한 옵션이 계획되어 있습니다.


**기타 기능:**




- 실험이나 홍보를 위해 토큰을 빠르게 테스트하거나 배포하려면 Faucet를 생성하세요;
- 인증 시스템(현재 중앙 집중식)은 합법적인 token과 유명 티커를 모방한 가짜를 구별하기 위한 것입니다. 향후 이 인증은 DNS 또는 기타 메커니즘을 통해 더욱 탈중앙화될 수 있습니다.


전반적으로 Iris는 RGBlib과 프록시 서버 사용 덕분에 추가적인 복잡성(Stash 관리, *Consignment* 기록 등)을 감추고 기존 Bitcoin Wallet에 가까운 사용자 경험을 제공합니다.


### 프록시 서버 및 사용자 경험


위에서 소개한 프록시 서버는 원활한 사용자 경험의 핵심이므로 자세히 설명할 필요가 있습니다. 발신자가 수신자에게 *위탁*을 수동으로 전송하는 대신, RGB 트랜잭션은 a를 통해 백그라운드에서 이루어집니다:




- 수신자는 *Invoice*(무엇보다도 프록시 Address를 포함)을 생성합니다;
- 발신자는 (HTTP 요청을 통해) 전환 프로젝트(*Consignment*)를 프록시로 보냅니다;
- 수신자는 이 프로젝트를 검색하고 로컬에서 *클라이언트 측* 유효성 검사를 실행합니다;
- 그런 다음 수신자는 프록시를 통해 State Transition의 수락(또는 거부 가능성)을 게시합니다;
- 발신자는 유효성 검사 상태를 확인하고 수락되면 전송을 완료하는 Bitcoin 트랜잭션을 브로드캐스트할 수 있습니다.


이런 식으로 Wallet은 거의 일반 Wallet처럼 작동합니다. 사용자는 모든 중간 단계를 알지 못합니다. 물론 현재 프록시는 암호화되거나 인증되지 않아 기밀성 및 무결성에 대한 우려가 있지만, 이후 버전에서는 이러한 문제가 개선될 수 있습니다. 프록시 개념은 "내가 QR 코드를 보내면 스캔하여 결제하는" 경험을 재현하는 데 여전히 매우 유용합니다.


### Lightning Network에 RGB 통합


비트파이넥스 팀의 또 다른 핵심 작업은 Lightning Network을 RGB 자산과 호환되도록 하는 것입니다. 목표는 USDT(또는 다른 token)에서 라이트닝 채널을 활성화하고 라이트닝에서 Bitcoin과 동일한 이점(거의 즉각적인 거래, 라우팅 등)을 누릴 수 있도록 하는 것입니다. 이를 구체적으로 설명하자면 다음과 같이 수정된 라이트닝 노드를 생성하는 것입니다:




- 사토시뿐만 아니라 하나 이상의 RGB 자산을 펀딩 UTXO Multisig에 배치하여 채널을 개설하세요;
- generate 라이트닝 Commitment 트랜잭션(Bitcoin 쪽)에 해당 RGB 상태 전환이 수반됩니다. 채널이 업데이트될 때마다 RGB 트랜지션은 라이트닝 출력의 자산 분포를 재정의합니다;
- Lightning Network 규칙(HTLC, 타임락, 처벌 등)에 따라 자산이 전용 UTXO에서 회수되는 일방적 폐쇄를 활성화합니다.


"**RGB 라이트닝 노드**"라고 불리는 이 솔루션은 LDK(*라이트닝 개발 키트*)를 기본으로 사용하며, RGB 토큰을 채널에 주입하는 데 필요한 메커니즘을 추가합니다. 라이트닝 커밋은 기존 구조(천공 가능한 출력, 타임락...)를 유지하며, Anchor에 RGB State Transition(`Opret` 또는 `Tapret`을 통해)를 추가합니다. 사용자에게는 스테이블코인 또는 RGB을 통해 발행된 다른 자산에서 라이트닝 채널을 사용할 수 있는 길이 열립니다.


### DEX 잠재력과 Bitcoin에 미치는 영향


여러 자산이 라이트닝을 통해 관리되면, 동일한 시크릿과 타임락 로직을 사용해 단일 라이트닝 라우팅 경로에서 **아토믹 Exchange**을 상상할 수 있게 됩니다. 예를 들어, 사용자 A는 하나의 라이트닝 채널에 Bitcoin를 보유하고 있고 사용자 B는 다른 라이트닝 채널에 USDT RGB을 보유하고 있다고 가정해 보겠습니다. 이들은 신뢰 없이도 두 채널을 연결하는 경로를 구축하여 동시에 Exchange BTC를 USDT로 교환할 수 있습니다. 이는 여러 홉에서 일어나는 **아토믹 스왑**에 불과하며, 외부 참여자는 단순한 라우팅이 아닌 거래를 하고 있다는 사실을 거의 알지 못합니다. 이 접근 방식은 다음과 같은 이점을 제공합니다:




- 모든 것이 Lightning에서 off-chain로 유지되므로 지연 시간이 매우 짧습니다.
- 뛰어난 **개인정보 보호**: 정상적인 라우팅이 아닌 거래라는 사실을 아무도 모릅니다;
- On-Chain DEX의 반복되는 문제인 프론트 러닝을 방지합니다;
- 비용 절감(블록 공간은 지불하지 않고, 라이트닝 라우팅 요금만 지불).


그러면 라이트닝 노드가 유동성을 제공해 스왑 가격을 제시하는 생태계를 상상해볼 수 있습니다. 각 노드는 원한다면 라이트닝에서 다양한 자산을 사고파는 _마켓 메이커_의 역할을 할 수 있습니다. 이러한 _레이어-2_ DEX의 전망은 탈중앙화 자산 거래소를 얻기 위해 Fork을 사용하거나 타사 블록체인을 사용할 필요가 없다는 생각을 강화합니다.


Bitcoin에 미치는 영향은 긍정적일 수 있습니다: 라이트닝의 인프라(노드, 채널, 서비스)는 이러한 *스테이블코인*, 파생상품 및 기타 토큰에서 생성되는 거래량 덕분에 더 충분히 활용될 수 있습니다. 라이트닝에서 USDT 결제에 관심이 있는 판매자는 라이트닝에서 (동일한 스택으로 관리되는) BTC 결제를 기계적으로 검색할 수 있습니다. Lightning Network 인프라의 유지 및 자금 조달은 이러한 비 BTC 흐름의 증가를 통해 이익을 얻을 수 있으며, 이는 Bitcoin 사용자에게 간접적으로 도움이 될 것입니다.


### 결론 및 리소스


RGB을 전담하는 비트파이넥스 팀은 작업을 통해 프로토콜 위에서 할 수 있는 일의 다양성을 보여줍니다. 한편으로는 지갑과 애플리케이션의 설계를 용이하게 하는 라이브러리인 RGBlib이 있습니다. 다른 한편으로는 깔끔한 최종 사용자 Interface의 실제 데모인 Iris Wallet이 있습니다. 마지막으로, RGB과 라이트닝의 통합은 스테이블코인 채널이 가능하다는 것을 보여주며, 라이트닝에서 잠재적인 탈중앙화 DEX로 가는 길을 열어줍니다.


이 접근 방식은 아직 실험적인 단계에 있으며 계속 발전하고 있습니다. RGBlib 라이브러리는 계속 개선되고 있고, Iris Wallet는 정기적으로 개선되고 있으며, 전용 Lightning 노드는 아직 주류 Lightning 클라이언트가 아닙니다.


더 자세히 알아보거나 기여하고자 하는 분들을 위해 다음과 같은 여러 리소스를 이용할 수 있습니다:




- [GitHub RGB 도구 리포지토리](https://github.com/RGB-Tools);
- [아이리스 Wallet 전용 정보 사이트](https://iriswallet.com/)에서 Android에서 Wallet을 테스트할 수 있습니다.


다음 장에서는 RGB 라이트닝 노드를 시작하는 방법에 대해 자세히 살펴보겠습니다.


## RLN - RGB 라이트닝 노드


<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>


:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::


이 마지막 장에서는 프레데리코 텐가가 레그테스트 환경에서 라이트닝 RGB 노드를 설정하는 과정을 단계별로 안내하고, 그 위에서 RGB 토큰을 생성하는 방법을 보여드립니다. 또한 두 개의 개별 노드를 실행하여 두 노드와 Exchange RGB 자산 간에 라이트닝 채널을 여는 방법도 알아보세요.


이 동영상은 이전 장에서 다룬 내용과 유사한 튜토리얼 역할을 하지만 이번에는 특히 라이트닝에 초점을 맞췄습니다!


이 비디오의 주요 리소스는 깃허브 리포지토리 [RGB 라이트닝 노드](https://github.com/RGB-Tools/RGB-lightning-node)로, Regtest에서 이 구성을 쉽게 실행할 수 있습니다.


### RGB 호환 라이트닝 노드 배포하기


이 과정은 이전 장에서 다룬 모든 개념을 다루고 실천에 옮깁니다:




- 라이트닝 채널의 2/2 Multisig에서 차단된 **UTXO**은 비트코인뿐만 아니라 Single-Use Seal의 RGB 자산(대체 가능 여부와 상관없이)도 받을 수 있다는 아이디어입니다;
- 각 라이트닝 참여 트랜잭션에서 RGB State Transition를 고정하기 위한 전용 출력(`Tapret` 또는 `Opret`)을 추가합니다;
- Bitcoin 트랜잭션 및 Exchange *클라이언트 측* 데이터의 유효성을 검사하기 위한 관련 인프라(bitcoind/인덱서/프록시).


### RGB-라이트닝 노드 소개


'RGB-lightning-node' 프로젝트는 채널 내 RGB 자산의 존재를 고려하도록 수정된 'Rust-lightning'(LDK) daemon을 기반으로 한 Fork입니다. 채널이 열리면 에셋의 존재 여부를 지정할 수 있으며, 채널 상태가 업데이트될 때마다 라이트닝 출력에 에셋의 분포를 반영하는 RGB 전환이 생성됩니다. 이를 통해




- 예를 들어 USDT로 라이트닝 채널을 엽니다;
- 라우팅 경로에 충분한 유동성이 있는 경우 네트워크를 통해 이러한 토큰을 라우팅합니다;
- 라이트닝의 처벌 및 타임락 로직을 수정하지 않고 활용하세요: Commitment Transaction의 추가 출력에서 Anchor을 RGB로 전환하기만 하면 됩니다.


이 코드는 아직 알파 단계이므로 **regtest** 또는 **Testnet**에서만 사용하는 것을 권장합니다.


### 노드 설치


RGB-lightning-node` 바이너리를 컴파일하고 설치하려면 먼저 리포지토리와 하위 모듈을 복제한 다음 실행합니다:


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RGB-Bitcoin](assets/en/098.webp)




- Recurse-submodules` 옵션은 필요한 하위 장치(`Rust-lightning`의 수정된 버전 포함)도 복제합니다;
- Shallow-submodules` 옵션은 복제 깊이를 제한하여 다운로드 속도를 높이는 동시에 필수 커밋에 대한 액세스를 계속 제공합니다.


프로젝트 루트에서 다음 명령을 실행하여 바이너리를 컴파일하고 설치합니다:


```bash
cargo install --locked --debug --path .
```


![RGB-Bitcoin](assets/en/099.webp)




- 잠김`은 종속성 버전이 엄격하게 준수되도록 합니다;
- 디버그`는 필수는 아니지만 집중하는 데 도움이 될 수 있습니다(원하는 경우 `--해제`를 사용할 수 있습니다);
- 경로 .`는 현재 디렉터리에서 설치하도록 `cargo install`에 지시합니다.


이 명령이 끝나면 `$CARGO_HOME/bin/`에서 `RGB-lightning-node` 실행 파일을 사용할 수 있습니다. 이 경로가 `$PATH`에 있는지 확인하여 어느 디렉토리에서나 명령을 호출할 수 있도록 하세요.


### 성능 요구 사항


작동하려면 `RGB-lightning-node` daemon의 존재와 구성이 필요합니다:




- **bitcoind** 노드


각 RLN 인스턴스는 On-Chain 트랜잭션을 브로드캐스트하고 모니터링하기 위해 `bitcoind`과 통신해야 합니다. 인증(로그인/비밀번호) 및 URL(호스트/포트)을 daemon에 제공해야 합니다.




- 인덱서**(일렉트럼 또는 에스플로라)**


특히 자산이 앵커링된 UTXO을 찾으려면 daemon이 On-Chain 트랜잭션을 나열하고 탐색할 수 있어야 합니다. 일렉트럼 서버 또는 Esplora의 URL을 지정해야 합니다.




- **RGB** 프록시


이전 챕터에서 살펴본 것처럼 **프록시 서버**는 라이트닝 피어 간 *위탁*의 Exchange를 간소화하기 위한 구성 요소(선택 사항이지만 적극 권장)입니다. 다시 한 번 URL을 지정해야 합니다.


API를 통해 daemon을 _잠금 해제_할 때 ID와 URL을 입력합니다. 이에 대한 자세한 내용은 나중에 설명합니다.


### 다시 테스트 시작


간단한 사용을 위해, Docker를 통해 일련의 서비스를 자동으로 시작하는 `regtest.sh` 스크립트가 있습니다: gW-2391`, `electrs`(인덱서), `RGB-proxy-server`.


![RGB-Bitcoin](assets/en/100.webp)


이를 통해 미리 구성된 격리된 로컬 환경을 시작할 수 있습니다. 재부팅할 때마다 컨테이너와 데이터 디렉터리를 생성하고 삭제합니다. 먼저 시작하겠습니다:


```bash
./regtest.sh start
```


이 스크립트는




- 저장할 `docker/` 디렉터리를 만듭니다;
- Regtest에서 `bitcoind`과 인덱서 `electrs` 및 `RGB-proxy-server`를 실행합니다;
- 모든 것이 사용할 준비가 될 때까지 기다리세요.


![RGB-Bitcoin](assets/en/101.webp)


다음으로 여러 개의 RLN 노드를 실행해 보겠습니다. 예를 들어, 별도의 셸에서 실행하여 3개의 RLN 노드를 실행합니다:


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RGB-Bitcoin](assets/en/102.webp)




- 네트워크 regtest` 매개변수는 regtest 구성의 사용을 나타냅니다;
- '--daemon-listening-port'는 Lightning 노드가 API 호출(JSON)을 수신 대기할 REST 포트를 나타냅니다;
- `--ldk-peer-listening-port`는 수신할 Lightning P2P 포트를 지정합니다;
- 데이터알드케이0/`, `데이터알드케이1/`은 스토리지 디렉터리 경로입니다(각 노드는 정보를 개별적으로 저장합니다).


브라우저에서 RLN 노드에서 명령을 실행할 수도 있습니다:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


노드가 채널을 열려면 먼저 다음 명령어로 생성된 Address에 비트코인이 있어야 합니다(예: 노드 n°1의 경우):


```bash
curl -X POST http://localhost:3001/address
```


답변은 Address을 제공합니다.


![RGB-Bitcoin](assets/en/103.webp)


bitcoind` 레그테스트에서 몇 개의 비트코인을 채굴해 보겠습니다. Run:


```bash
./regtest.sh mine 101
```


![RGB-Bitcoin](assets/en/104.webp)


위에서 생성한 노드 Address으로 자금을 전송합니다:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RGB-Bitcoin](assets/en/105.webp)


그런 다음 블록을 채굴하여 거래를 확인합니다:


```bash
./regtest.sh mine 1
```


![RGB-Bitcoin](assets/en/106.webp)


### Testnet 출시(도커 제외)


보다 현실적인 시나리오를 테스트하려면 Regtest가 아닌 Testnet에서 3개의 RLN 노드를 실행하여 퍼블릭 서비스를 가리키면 됩니다:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


기본적으로 구성을 찾을 수 없는 경우 daemon은 다음을 사용하려고 시도합니다:




- 비트코인드_rpc_호스트`: `electrum.iriswallet.com`
- 비트코인드_rpc_port`: `18332`
- 인덱서_URL`: `ssl://electrum.iriswallet.com:50013`
- 프록시 엔드포인트`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


로그인 시:




- `bitcoind_rpc_username`: `사용자`
- 비트코인드_rpc_사용자명`: `비밀번호`


'초기화`/`잠금해제` API를 통해 Elements를 사용자 지정할 수도 있습니다.


### RGB token 발행


token을 발급하려면 먼저 '컬러링 가능한' UTXO를 생성합니다:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RGB-Bitcoin](assets/en/107.webp)


물론 순서를 조정할 수도 있습니다. 트랜잭션을 확인하기 위해 마이닝합니다:


```bash
./regtest.sh mine 1
```


이제 RGB 에셋을 만들 수 있습니다. 명령은 생성하려는 에셋의 유형과 매개변수에 따라 달라집니다. 여기서는 Supply가 1000 단위인 "PBN"이라는 이름의 NIA(*비팽창형 에셋*) token을 생성하겠습니다. '정밀도'를 사용하면 단위의 분할 가능성을 정의할 수 있습니다.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RGB-Bitcoin](assets/en/108.webp)


응답에는 새로 생성된 에셋의 ID가 포함됩니다. 이 식별자를 기억하세요. 제 경우에는


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RGB-Bitcoin](assets/en/109.webp)


그런 다음 On-Chain로 전송하거나 라이트닝 채널에 할당할 수 있습니다. 다음 섹션에서 바로 이 작업을 수행하겠습니다.


### 채널 열기 및 RGB 에셋 전송하기


먼저 `/connectpeer` 명령을 사용하여 노드를 Lightning Network의 피어에 연결해야 합니다. 제 예제에서는 두 노드를 모두 제어합니다. 따라서 이 명령으로 두 번째 라이트닝 노드의 공개 키를 검색하겠습니다:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


이 명령은 내 노드 n°2의 공개 키를 반환합니다:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RGB-Bitcoin](assets/en/110.webp)


다음으로 관련 에셋(`PBN`)을 지정하여 채널을 열겠습니다. Openchannel` 명령을 사용하면 채널의 크기를 사토시 단위로 정의하고 RGB 에셋을 포함하도록 선택할 수 있습니다. 생성하려는 자산에 따라 다르지만, 제 경우에는 다음과 같이 명령합니다:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


여기에서 자세히 알아보세요:




- 피어_공개키_및_옵트_주소`: 연결하려는 피어의 식별자(앞서 찾은 공개 키);
- 용량_샛`: 사토시 단위의 총 채널 용량입니다;
- pUSH_MSAT`: 채널이 열릴 때 처음에 피어에게 전송되는 밀리사토시 단위의 금액(여기서는 나중에 RGB 전송을 할 수 있도록 10,000 Sats을 즉시 전송합니다);
- `자산_금액`: 채널에 커밋할 RGB 에셋의 양입니다;
- `자산_id`: 채널에 연결된 RGB 에셋의 고유 식별자입니다;
- 공개`: 네트워크에서 라우팅을 위해 채널을 공개할지 여부를 나타냅니다.


![RGB-Bitcoin](assets/en/111.webp)


거래를 확인하기 위해 6개의 블록이 채굴됩니다:


```bash
./regtest.sh mine 6
```


![RGB-Bitcoin](assets/en/112.webp)


이제 라이트닝 채널이 열렸으며 노드 n°1 측에 500개의 `PBN` 토큰이 있습니다. 노드 n°2가 `PBN` 토큰을 받으려면 generate과 Invoice을 생성해야 합니다. 방법은 다음과 같습니다:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


With:




- `amt_msat`: 밀리사토시 단위의 Invoice 양(최소 3000 Sats);
- 만료_초`: Invoice 만료 시간(초)입니다;
- `asset_id`: Invoice와 연결된 RGB 에셋의 식별자입니다;
- `자산_금액`: 이 Invoice로 전송할 RGB 자산의 양입니다.


이에 대한 응답으로 이전 장에서 설명한 대로 RGB Invoice를 받게 됩니다:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RGB-Bitcoin](assets/en/113.webp)


이제 필요한 현금을 보유하고 있는 첫 번째 노드에서 이 Invoice을 `PBN` token로 지불합니다:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RGB-Bitcoin](assets/en/114.webp)


결제가 완료되었습니다. 명령을 실행하여 확인할 수 있습니다:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RGB-Bitcoin](assets/en/115.webp)


RGB 에셋을 전송하도록 수정된 라이트닝 노드를 배포하는 방법은 다음과 같습니다. 이 데모는 다음을 기반으로 합니다:




- Regtest 환경(`./regtest.sh`를 통해) 또는 Testnet;
- bitcoind`, 인덱서 및 `RGB-proxy-server`를 기반으로 하는 라이트닝 노드(`RGB-lightning-node`);
- 채널 열기/닫기, 토큰 발행, 라이트닝을 통한 자산 전송 등을 위한 일련의 JSON REST API입니다.


이 프로세스 덕분입니다:




- 라이트닝 참여 트랜잭션에는 RGB 전환의 앵커링과 함께 추가 출력(OP_RETURN 또는 Taproot)이 포함됩니다;
- 송금은 기존 라이트닝 결제와 똑같은 방식으로 이루어지지만, RGB token이 추가됩니다;
- 경로에 비트코인과 자산 RGB 모두에 충분한 유동성이 있는 경우, 여러 RLN 노드를 연결하여 여러 노드에서 결제를 라우팅하고 실험해볼 수 있습니다.


이 프로젝트는 아직 알파 단계에 머물러 있습니다. 따라서 테스트 환경(regtest, Testnet)으로 제한할 것을 강력히 권장합니다.


LN-RGB 호환성을 통해 라이트닝의 스테이블코인, DEX Layer-2, 매우 저렴한 비용으로 대체 가능한 토큰 또는 NFT 전송 등 상당한 기회가 열렸습니다.... 이전 장에서는 개념적 아키텍처와 검증 로직에 대해 간략하게 설명했습니다. 이제 향후 개발이나 테스트를 위해 이러한 노드를 가동하고 실행하는 방법에 대한 실용적인 관점을 갖게 되었습니다.


# 최종 섹션


<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## 리뷰 및 평가


<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>


<isCourseReview>true</isCourseReview>

## 결론


<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>


<isCourseConclusion>true</isCourseConclusion>