---
name: Elements 및 Liquid Network으로 구축
goal: Elements 오픈 소스 Blockchain 플랫폼과 주요 기능으로 사용 및 개발하는 방법 알아보기
objectives: 

  - Elements Blockchain 플랫폼과 Liquid 사이드체인의 기본 개념을 이해합니다.
  - 독립형 및 Sidechain 구성을 위한 Elements 노드 설정 및 실행 방법을 알아보세요.
  - 연합된 block signing과 Federated 2-Way Peg로 실무 경험을 쌓으세요.
  - 실제 사용 사례를 위해 안전하고 효율적인 Blockchain 환경을 설정하고 관리하세요.

---

# Liquid 및 Elements를 기반으로 구축


Liquid 및 Elements의 고급 기능을 살펴보고 이러한 도구를 효과적으로 활용하여 개발 프로젝트를 향상시키는 방법을 알아보세요. 이 교육은 완벽한 이론 및 실무 기반을 제공하여 Confidential Transactions, Issued Assets 및 연합 block signing과 같은 기능을 마스터할 수 있도록 합니다.


Elements 프레임워크를 기반으로 하는 Liquid은 금융 및 기술 솔루션의 개인정보 보호, 확장성, 기능을 개선하도록 설계되었습니다. 이 과정에서는 자산 발행 및 관리, Federated 2-Way Peg, elementsd 및 elements-cli과 같은 도구 사용에 대한 실무 경험을 쌓아 필요에 맞는 혁신적인 솔루션을 만들 수 있는 역량을 키웁니다.


이 과정은 모든 경험 수준의 개발자를 대상으로 합니다. 초급 및 중급 사용자는 쉽게 이해할 수 있는 설명과 실용적인 예제를, 고급 사용자는 Liquid 및 Elements의 기술적 세부 사항과 잘 알려지지 않은 기능에 대해 자세히 알아볼 수 있습니다.


저희와 함께 기술을 향상시키고, Liquid과 Elements의 잠재력을 최대한 활용하고, Liquid 혁신의 미래를 위한 영향력 있는 도구를 만들어 보세요.

+++

# 소개


<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>


## 코스 개요


<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>


:::video id=e0166470-5561-4b3b-9d0d-4edee69b64d8:::


SID202 과정에 오신 것을 환영합니다!


Elements 아카데미*의 목표는 Liquid Sidechain의 기반이 되는 오픈소스 플랫폼인 *Elements*의 주요 개념을 소개하고 설명하는 것입니다. 이 과정을 마치면 Elements의 주요 기능인 Confidential Transactions, Issued Assets는 물론 Elements Core 운영 프로세스에 대해 확실히 이해할 수 있습니다. 이 과정의 각 섹션에는 설명 텍스트와 동영상이 포함된 강의와 퀴즈가 포함되어 있습니다.


이 교육은 오픈 소스 Elements 플랫폼을 사용하고 개발하는 방법을 알려주는 것을 목표로 하며, Liquid Network에 중점을 두고 있습니다. 이러한 기술을 통해 개발 프로젝트의 개인정보 보호, 확장성 및 기능을 향상시킬 수 있는 방법을 알아볼 수 있습니다. 초보자이든 숙련된 개발자이든 이 과정을 통해 Elements 및 Liquid의 기본 개념과 실제 적용 방법을 마스터할 수 있는 강력한 기반을 다질 수 있습니다.


**섹션 1: 소개**

Elements 개념에 대한 포괄적인 개요부터 시작하겠습니다. 이 플랫폼이 어떻게 Liquid과 같은 사이드체인 생성을 위한 모듈식의 유연한 기반을 제공하도록 설계되었는지 배우게 됩니다. 실제 적용 사례를 살펴보기 전에 Elements의 구조를 이해하는 것이 목표입니다.


**섹션 2: Elements**

이 섹션에서는 Elements의 작동 방식에 대해 중점적으로 설명합니다. Elements 노드를 구성하고 독립형 모드로 작동하거나 Sidechain로 사용하는 방법을 배웁니다.


**섹션 3: Elements 사용 - 실제 사용 사례**

이론적 기초를 습득한 후에는 Elements의 실제 적용 방법을 다룹니다. Confidential Transactions를 수행하고, 자산을 발행하고, 자산 재발급을 관리하는 방법을 배우게 됩니다.


**섹션 4: Elements 연합**

여기에서는 연합 block signing, Elements을 Sidechain으로 사용, 독립 블록체인 생성 등 고급 메커니즘을 살펴봅니다. 이 섹션에서는 Elements 기반 블록체인의 보안, 무결성 및 상호 운용성을 보장하는 방법을 이해하는 데 도움이 될 것입니다.


Elements와 Liquid Sidechain의 잠재력을 살펴볼 준비가 되셨나요? 지금 바로 시작하세요!



## Elements 개요


<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>


:::video id=eae666b4-eddc-4e00-adea-2a5f94396044:::


Elements은 Sidechain를 지원하는 오픈 소스 Blockchain 플랫폼으로, 커뮤니티 구성원들이 개발한 강력한 기능에 액세스할 수 있습니다(예: Confidential Transactions 및 Issued Assets).


Elements은 핵심적으로 분산형 Blockchain Ledger에 저장된 자산의 이전과 생성을 관리하는 거래 내역과 규칙에 대한 합의를 형성할 수 있는 프로토콜입니다.


Elements에 대한 자세한 배경 정보는 Elements 프로젝트 웹사이트(https://elementsproject.org/), Liquid 공식 블로그(https://blog.Liquid.net/), 개발자 포털(https://Liquid.net/devs)에서 쉽게 확인할 수 있습니다.


### Elements


2015년에 출시된 Elements는 내부 개발 및 연구 비용을 절감하고 최신 Blockchain 기술을 활용하여 다양한 새로운 사용 사례를 구현할 수 있습니다. Elements 기반 Blockchain은 독립형 Blockchain으로 작동하거나 다른 Sidechain에 페깅하여 Sidechain로 작동할 수 있습니다. Elements를 Sidechain로 실행하면 서로 다른 블록체인 간에 자산을 검증 가능하게 전송할 수 있습니다.


Bitcoin의 코드베이스를 기반으로 구축되고 확장되어, bitcoind API에 익숙한 개발자가 빠르고 비용 효율적으로 작동하는 블록체인을 생성하고 개념 증명 프로젝트를 테스트할 수 있습니다. 또한 Bitcoin 코드베이스를 기반으로 구축되었기 때문에 Elements은 Bitcoin 프로토콜 자체의 변경을 위한 테스트베드로도 기능할 수 있습니다.


Elements의 주요 기능 중 일부는 다음과 같습니다.


#### Confidential Transactions


기본적으로 Elements의 모든 주소는 Confidential Transactions을 사용하는 blinded입니다. 블라인딩은 전송되는 자산의 양과 유형을 참여자와 Blinding key를 공개하기로 선택한 사람을 제외한 모든 사람에게 암호학적으로 숨기는 프로세스입니다.


#### Issued Assets


Elements의 Issued Assets은 네트워크 참여자 간에 여러 유형의 자산을 발행하고 전송할 수 있도록 합니다. 발행된 자산은 Confidential Transactions의 혜택도 받을 수 있으며, 관련 reissuance token을 보유한 사람은 누구나 재발행하거나 파기할 수 있습니다.


#### Federated 2-Way Peg


Elements은 한 체인에서 다른 체인으로 자산을 양방향으로 전송할 수 있도록 기존 Blockchain(예: Bitcoin)에 "페깅"할 수도 있는 범용 Blockchain 플랫폼입니다. Elements을 Sidechain로 구현하면 메인 체인에 보호된 자산이 제공하는 보안을 어느 정도 유지하면서 메인 체인의 고유한 속성 중 일부를 우회할 수 있습니다.


#### 서명된 블록


Elements은 블록 서명자라고 하는 서명자들로 구성된 Strong Federation를 사용하여 안정적이고 적시에 블록을 서명하고 생성합니다. 이는 무작위 푸아송 분포로 인해 블록 시간 편차가 큰 PoW Mining 프로세스의 트랜잭션 지연을 제거합니다. 연합 block signing 프로세스는 제3자 신뢰나 계산 '알고리즘' 기반 Mining을 도입하지 않고도 신뢰할 수 있는 블록 생성을 달성합니다.


Elements은 Bitcoin core 코드베이스 위에 이러한 모든 기능을 추가하여 mainchain 프로토콜의 기능을 확장하고 Sidechain 또는 독립형 Blockchain 솔루션으로 배포할 때 새로운 비즈니스 사용 사례를 가능하게 합니다.


# 요소


<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>


## Elements 작동 방식


<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>


:::video id=7c8c7981-11e5-47a2-a257-ef998f4892f5:::


Elements은 Blockchain 사용자가 매일 직면하는 트랜잭션 지연 시간, 프라이버시 부족, 대체 가능성 위험 등의 문제에 대한 기술적 해결책을 제공합니다.


Elements는 연합 block signing 및 Confidential Transactions을 사용하여 이러한 문제를 극복합니다.


Bitcoin 네트워크와 달리, Elements 내의 block signing 프로세스는 동적 멤버십 다자간 서명(DMMS)과 Proof of Work(작업 증명)에 의존하지 않습니다. 대신, Elements은 블록 서명자라고 불리는 서명자들로 구성된 Strong Federation을 사용하여 안정적이고 적시에 블록을 서명하고 생성할 수 있습니다. 이는 무작위 푸아송 분포로 인해 블록 시간 편차가 큰 작업 증명 Mining 프로세스의 트랜잭션 지연을 제거합니다. 연합 block signing 프로세스는 제3자 신뢰 없이도 안정적인 블록 생성을 달성합니다.


Elements은 Bitcoin와 같은 다른 Blockchain에 Sidechain로 연결하거나 다른 네트워크에 대한 종속성 없이 독립형 Blockchain으로 실행할 수 있습니다.


Sidechain로 사용될 경우, Strong Federation에는 메인체인과 Elements Sidechain 간에 자산을 안전하고 통제된 방식으로 전송할 수 있는 멤버도 포함됩니다. 자산의 통제된 전송을 Federated 2-Way Peg이라고 하며, 자산 전송 역할을 수행하는 멤버를 watchmen라고 합니다.


Elements 네트워크의 운영과 관련된 프로세스와 네트워크 참여자의 역할은 Elements의 작동 방식을 이해하는 데 중요합니다.


Sidechain로 구현하든 독립형 Blockchain으로 구현하든, Elements은 강력한 블록 서명자 연합을 사용하여 블록을 생성합니다.


### 강력한 연합


Elements은 블록스트림에서 처음 제안한 합의 모델인 강력한 연합을 사용합니다. Strong Federation는 Proof of Work(작업 증명)이 필요하지 않으며, 대신 함수형이라고 하는 상호 신뢰하는 참가자 그룹의 집단 행동에 의존합니다.


Strong Federation 내에서 기능 담당자가 수행할 수 있는 역할은 다음과 같습니다: 블록 서명자 및 watchmen. 블록 서명자는 Sidechain 또는 독립형 Blockchain 모드에서 Elements를 실행하는 경우 필요하지만, watchmen은 Sidechain 설정에서만 필요합니다.


Strong Federation의 구성원이 수행할 수 있는 작업은 보안을 강화하고 공격자가 입힐 수 있는 피해를 제한하기 위해 두 가지 역할로 나뉩니다.


이러한 참여자들의 역할을 결합하면 Elements는 신속한 블록 생성(더 빠르고 최종적인 거래 확인)과 확실한 양도 자산(다른 Blockchain에 직접 연결 가능한 페깅된 자산)을 모두 제공할 수 있습니다.


강력한 연합 백서는 여기에서 읽을 수 있습니다: https://blockstream.com/strong-federations.pdf


### 서명자 차단


Bitcoin와 같은 Blockchain은 동적 블록 서명자 그룹의 일부를 구성하는 사람이 Proof of Work이 소모되었음을 입증하여 체인을 확장할 때 확장됩니다. 세트의 동적 특성으로 인해 이러한 시스템에 내재된 지연 문제가 발생합니다.


연합 모델은 고정 서명자 집합을 사용함으로써 동적 집합을 알려진 집합의 다중 서명 체계로 대체합니다. Blockchain을 확장하는 데 필요한 참여자 수를 줄이면 시스템의 속도와 확장성이 향상되고, 모든 당사자의 검증을 통해 거래 내역의 무결성이 보장됩니다.


연합 block signing는 여러 단계로 구성되어 있습니다:



- 1단계 - 블록 서명자는 다른 모든 참여 블록 서명자에게 라운드 로빈 방식으로 후보 블록을 제안합니다.



- 2단계 - 각 block signer는 주어진 후보 블록에 서명하기 위해 사전 커밋하여 의사를 표시합니다.



- 3단계 - 사전 Commitment에 대한 주어진 임계값이 충족되면 각 block signer이 블록에 서명합니다.



- 4단계 - 서명 임계값(3단계의 임계값과 다를 수 있음)이 충족되면 블록이 승인되어 네트워크로 전송됩니다. Strong Federation이 최신 트랜잭션 블록에 대한 합의에 도달했습니다.



- 5단계 - 라운드 로빈에서 다음 block signer가 다음 블록을 제안하고 프로세스가 반복됩니다.


Strong Federation의 블록 생성은 확률적이지 않고 고정된 서명자 집합을 기반으로 하기 때문에 다중 블록 재구성의 영향을 받지 않습니다. 따라서 트랜잭션 확인과 관련된 대기 시간을 크게 줄일 수 있습니다. 또한 이익을 위해 채굴하려는 인센티브(즉, 블록 보상)를 제거하고 모든 참여자가 동일한 목표를 공유하는 네트워크에 생산적으로 참여하려는 인센티브로 대체하여 네트워크가 모두에게 이익이 되는 방식으로 계속 작동하도록 보장합니다. 이는 단일 장애 지점이나 더 높은 신뢰 요건을 도입하지 않고도 가능합니다.


### Elements을 Sidechain - watchmen 및 Federated 2-Way Peg로 변경하기


Sidechain으로 운영되는 경우, Strong Federation의 일부 멤버는 watchmen의 역할을 추가로 수행해야 합니다. watchmen은 '페그인'과 '페그아웃'으로 알려진 프로세스를 통해 자산을 Elements Sidechain으로 전송하고 전송받는 역할을 담당합니다.


Sidechain이 신뢰할 수 있는 방식으로 작동하려면 참가자가 자산의 Supply이 통제되고 검증 가능한지 확인할 수 있어야 합니다. Elements Sidechain은 2-Way federated peg를 사용하여 자산을 양방향으로 주고받을 수 있습니다. 이는 증명 가능한 발행과 체인 간 전송의 요건을 충족합니다.


Federated 2-Way Peg 기능을 사용하면 자산을 다른 블록체인과 상호 운용할 수 있으며 다른 Blockchain의 네이티브 자산을 대표할 수 있습니다. Blockchain를 다른 블록체인에 페깅하면 mainchain의 기능을 확장하고 내재된 일부 한계를 극복할 수 있습니다.


높은 수준에서 Sidechain로의 전송은 누군가 mainchain 자산을 다중 서명 watchmen Wallet에 의해 제어되는 Address으로 보낼 때 발생합니다. 이렇게 하면 mainchain의 자산이 효과적으로 동결됩니다. 그런 다음 watchmen는 트랜잭션의 유효성을 검사하고 Sidechain 내에서 동일한 양의 관련 자산을 릴리스합니다. 해제된 자산은 원래 mainchain 자산에 대한 소유권을 증명할 수 있는 Sidechain Wallet로 전송됩니다. 이 과정을 통해 자산이 부모 체인에서 Sidechain로 효과적으로 이동합니다.


자산을 mainchain으로 다시 전송하기 위해 사용자는 Sidechain에서 특수 페그아웃 트랜잭션을 수행합니다. 이 트랜잭션은 watchmen가 확인한 다음 Wallet가 관리하는 다중 서명 mainchain의 트랜잭션 지출에 서명합니다. 페더레이션의 임계값 수만큼의 참여자가 서명해야 mainchain 트랜잭션이 유효해집니다. watchmen가 자산을 mainchain으로 다시 보내면 Sidechain의 해당 금액도 소멸되어 블록체인 간에 자산이 효과적으로 전송됩니다.


## Elements 설정 및 실행


<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>


:::video id=1f73dfee-3623-483b-ab42-07d9286ed999:::


Elements은 Bitcoin 코드베이스를 기반으로 하므로, 작동하는 네트워크를 구성하는 구성 요소는 매우 유사합니다.


Elements 노드 소프트웨어 자체는 'elementsd'라고 불리며, 사용자 컴퓨터에서 daemon로 실행됩니다. daemon(또는 Windows의 서비스)은 로그온한 사용자가 직접 제어할 필요 없이 백그라운드 서비스로 실행되는 프로그램입니다.


참고: 이 문서에서는 항상 elementsd를 daemon 버전으로 지칭하지만 서버 옵션이 활성화된 경우 Elements-qt로 모든 작업을 수행할 수 있습니다.


Elements daemon은 네트워크의 다른 노드에 연결하여 네트워크의 Blockchain의 로컬 복사본을 검증하고 확장하여 데이터를 Exchange 트랜잭션 및 차단할 수 있습니다.


Elements 소프트웨어는 명령줄에서 elementsd로 원격 프로시저 호출(RPC) 명령을 보낼 수 있는 'elements-cli'라는 클라이언트 프로그램도 포함하고 있습니다. 예를 들어 Wallet 잔액을 조회하거나, 트랜잭션 또는 블록 데이터를 보거나, 트랜잭션을 브로드캐스트하는 데 사용할 수 있습니다. 이 설정은 Bitcoin에 상응하는 bitcoind과 bitcoin-cli을 사용해 본 사용자라면 누구나 익숙할 것입니다.


Elements 노드는 시작 시 또는 구성 파일을 통해 매개변수를 전달하여 구성할 수 있으므로 동일한 시스템에서 두 개 이상의 인스턴스를 실행할 수 있습니다. 이는 단일 머신에서 자체 로컬 네트워크를 설정하고, 각 Elements 노드가 자체 Blockchain 데이터 사본을 가지고, 확인되지 않은 유효한 트랜잭션 풀을 관리하고, 다른 포트에서 RPC 요청을 수신할 수 있으므로 테스트 및 개발 목적에 유용합니다.


### Elements 코드 저장소 및 커뮤니티


Elements은 오픈 소스 프로젝트이며 소스 코드는 Elements GitHub 리포지토리(https://github.com/ElementsProject/Elements)에서 찾을 수 있습니다. 이 리포지토리에는 elementsd 및 elements-cli 프로그램의 소스와 함께 지원 설치 및 빌드 도구, 테스트 모음 및 일부 지침 문서가 포함되어 있습니다.


코드 리포지토리를 보완하기 위해 커뮤니티 중심의 리소스인 https://elementsproject.org 웹사이트에도 Elements의 정의, 작동 방식, 종합적인 튜토리얼 섹션이 포함되어 있습니다. 튜토리얼은 명령줄 예제를 따라 Elements에 대해 배우는 데 중점을 두고 있으며, 이를 기반으로 간단한 데스크톱 및 웹 애플리케이션을 구축하는 방법을 보여줍니다. 또한 이 사이트에는 인기 있는 Elements 커뮤니티 토론 포럼이 나열되어 있으며, GitHub에서 호스팅되므로 커뮤니티에서 이 사이트의 콘텐츠에 기여할 수 있습니다.


컴퓨터에서 Elements를 실행하려면 먼저 소스 코드를 복제(복사본 다운로드)하고, 코드에 포함된 종속 요소를 설치한 후 마지막으로 daemon 및 클라이언트 실행 파일을 빌드해야 합니다. 그러면 Elements 소프트웨어를 구성하고 실행할 준비가 완료됩니다.


## 노드 및 네트워킹 구성


<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>


시작 시 구성 설정을 Elements 노드에 전달하여 실행, 데이터 유효성 검사, 다른 노드에 연결 및 Blockchain 데이터 초기화 방식을 변경할 수 있습니다.


설정은 지정된 `Elements.conf` 파일에서 로드하거나 명령줄을 통해 매개변수로 전달합니다.


이러한 매개변수를 사용하여 몇 가지 사항을 변경할 수 있습니다:



- 독립형 Blockchain 구현에 사용되는 default asset의 이름입니다.
- 생성된 초기 에셋의 개수입니다.
- 네트워크에서 거래 수수료를 지불할 때 사용할 자산입니다.
- Blockchain 데이터 파일의 저장 위치입니다.
- Bitcoin 노드에 연결하는 데 사용되는 RPC 자격 증명입니다.
- 충족해야 하는 `n of m` 임계값과 블록에 서명할 수 있는 유효한 공개 키입니다.
- Sidechain에서 자산을 주고받기 위해 충족해야 하는 스크립트입니다.
- Bitcoin 노드를 Sidechain으로 연결할지 여부.


이러한 규칙 중 다수는 네트워크 합의 규칙의 일부를 구성하므로, 시작 시 모든 노드에 적용하는 것이 중요합니다. 일부는 체인이 초기화된 후에 변경할 수 있지만, 일부는 체인을 초기화한 후에 수정해야 합니다.


매개변수 사용은 각 섹션과 관련하여 강좌 뒷부분에서 다룰 예정입니다.


### 명령줄을 사용한 기본 작업


이 강좌에서는 `elements-cli` 프로그램을 사용하여 하나 이상의 Elements 노드에 RPC 호출을 하는 예제를 보여드리겠습니다. 이 작업은 터미널 세션에서 수행되며 명령을 더 간결하게 만들기 위해 `별칭`이 사용됩니다. 이 규칙에 따라 다음과 같은 명령이 표시됩니다:


```bash
e1-dae

e1-cli getnewaddress
```


E1-dae`와 `e1-CLI`은 실제로 터미널의 `별칭` 기능을 활용한 타이포그래피 단축키입니다. 명령이 실행될 때 `e1-dae`와 `e1-CLI`은 실제로 대체되며 실행되는 명령은 다음과 유사합니다:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```


위에서 볼 수 있는 것은 Elements daemon를 시작하기 위한 호출과 `$HOME/Elements/src` 디렉토리에 있는 elements-cli 프로그램에 대한 호출 및 `datadir` 파라미터의 값입니다. 데이터디르` 매개변수를 통해 daemon와 클라이언트 인스턴스가 구성 파일을 찾을 위치를 지정할 수 있으며, daemon의 경우 Blockchain의 복사본을 저장할 위치를 지정할 수 있습니다. 구성 파일을 공유하면 클라이언트는 daemon로 RPC 호출을 할 수 있습니다.


위의 명령을 다시 실행하되 다른 `datadir` 값을 사용하면 각각 별도의 Blockchain 및 구성 설정 사본이 있는 둘 이상의 Elements 인스턴스를 시작할 수 있습니다. 이 규칙에 따라 이 과정에서는 `e2-dae` 및 `e2-CLI`라는 별칭을 사용하여 e1과 다른 데이터 디렉터리를 참조할 것입니다. 따라서 두 번째 `e2` 인스턴스에 대한 위의 예는 다음과 같습니다:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```


이를 통해 노드 간 자산 거래, 자산 발행, 동일한 네트워크의 다른 노드 간 Confidential Transactions에서 블라인드 사용 확인과 같은 모든 작업을 수행할 수 있습니다.


# 요소 사용 실제 사용 사례


<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>


## Confidential Transactions


<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>


:::video id=ea2121b6-24a8-458d-91e6-0c92eaf4dc65:::


이 섹션에서는 Elements의 Confidential Transactions 기능을 사용하는 방법에 대해 설명합니다.


Elements의 모든 주소는 기본적으로 Confidential Transactions를 사용하는 blinded이며, 전송된 자산의 양과 유형은 거래 참여자(그리고 Blinding key를 공개하기로 선택한 사람)만 볼 수 있도록 유지하면서 사용 가능한 것보다 더 많은 코인을 사용할 수 없도록 암호학적으로 보장합니다.


### 기밀 주소 및 Confidential Transactions


기본적으로 `getnewaddress` 명령을 사용하여 Elements에서 새 Address를 생성하면 Confidential Address로 생성됩니다.


Confidential Transactions을 시연하기 위해 e2가 스스로 자금을 송금하도록 한 다음 e1에서 트랜잭션을 확인해보겠습니다. 이를 통해 Elements에서 거래의 기밀성을 입증할 수 있습니다.


Elements 노드에서 생성된 모든 새로운 Address은 기본적으로 기밀입니다. E2를 generate에 새로운 Address으로 전송하여 이를 증명할 수 있습니다.


```
e2-cli getnewaddress
```


Address는 e1로 시작한다는 점에 유의하세요. 이것은 Confidential Address로 식별됩니다. Getaddressinfo 명령을 사용하여 Address를 더 자세히 살펴보면 Address에 대한 자세한 내용을 확인할 수 있습니다.


```
e2-cli getaddressinfo <address>
```


Confidential Address임을 알려주는 confidential_key 속성이 있는 것을 볼 수 있습니다.


Confidential_key는 Confidential Address 자체에 추가되는 공개 Blinding key입니다. 이것이 Confidential Address의 길이가 긴 이유입니다.


또한 관련 Unconfidential address이 있습니다. Elements 내에서 기밀이 아닌 일반 트랜잭션을 사용하려면 접두사가 lq1인 Address 대신 이 Unconfidential address으로 자산을 전송해야 합니다.


이제 e2가 생성한 Address으로 일부 자금을 보내도록 할 수 있습니다. 나중에 e1은 거래 당사자가 아니므로 거래의 세부 정보를 볼 수 없음을 보여줄 것입니다.


```
e2-cli sendtoaddress <address>
```


transaction ID을 참고합니다. 거래를 확인합니다.


```
e2-cli -generate 101
```


E2가 자신에게 일부 자금을 송금한 거래를 e2 자체의 관점에서 살펴봅니다.


```
e2-cli gettransaction <txid>
```


트랜잭션 세부 정보를 위로 스크롤하면 e2가 송금 및 수신 금액과 거래된 자산을 볼 수 있음을 확인할 수 있습니다. 거래에 관여하지 않은 다른 노드의 세부 정보를 블라인드하는 데 사용되는 금액 블라인더와 자산 블라인더 속성도 볼 수 있습니다.


E1에서 동일한 거래의 세부 정보를 확인하려면 먼저 원시 거래 세부 정보를 가져와야 합니다.


```
e1-cli getrawtransaction <txid>
```


그러면 원시 거래 세부 정보가 반환됩니다. 출금 섹션을 살펴보면 세 가지 인스턴스가 있음을 알 수 있습니다. 처음 두 인스턴스는 수령 금액과 잔액이고 세 번째 인스턴스는 거래 수수료입니다. 이 세 가지 금액 중 수수료만 값을 확인할 수 있는데, 수수료 자체는 항상 Elements 내에서 unblinded이므로 값을 확인할 수 있는 유일한 금액입니다.


### 블라인드 키


처음 두 개의 바우트 섹션에 표시되는 것은 가치 금액의 "Blinded ranges"과 실제 거래된 자산의 금액과 유형에 대한 증거 역할을 하는 Commitment 데이터입니다.


E2의 개인 키를 e1의 Wallet으로 가져온다고 해도 e2가 사용하는 Blinding key에 대한 지식이 없기 때문에 거래된 자산의 금액과 유형을 확인할 수 없습니다. 이를 증명하기 위해 e2의 Wallet에서 사용하는 개인 키를 e1의 개인 키로 가져와 보겠습니다. 먼저 e2에서 키를 내보내야 합니다


```
e2-cli dumpprivkey <address>
```


그런 다음 e1으로 가져옵니다.


```
e1-cli importprivkey <privkey>
```


이제 e1이 여전히 값을 볼 수 없다는 것을 증명할 수 있습니다.


```
e1-cli gettransaction <txid>
```


실제로는 1이었지만 실제로는 0으로 표시됩니다.


블라인딩되지 않은 실제 값을 보려면 Blinding key가 필요합니다. 이를 위해 먼저 e2에서 Blinding key를 내보냅니다.


```
e2-cli dumpblindingkey <address>
```


그런 다음 e1으로 가져옵니다.


```
e1-cli importblindingkey <address> <blinding key>
```


이제 e1에서 거래 세부 정보를 가져옵니다.


```
e1-cli gettransaction <txid>
```


Blinding key를 가져오면 이제 트랜잭션 내에서 실제 값 1을 볼 수 있음을 보여줍니다.


이 섹션에서는 Blinding key을 사용하면 거래에서 자산의 금액과 유형을 숨길 수 있으며, 올바른 Blinding key을 가져오면 해당 값을 공개할 수 있다는 것을 살펴보았습니다. 예를 들어, 거래 당사자가 보유한 자산의 금액과 유형을 확인해야 하는 경우 Blinding key을 감사자에게 제공할 수 있습니다. Confidential Transactions의 Elements 기능을 사용하면 "범위 증명"도 수행할 수 있습니다. 범위 증명은 실제 금액 자체를 노출할 필요 없이 특정 범위 내에서 자산을 보유하고 있음을 증명할 수 있습니다.


또한 Confidential Transactions는 선택 사항이지만 새 Address이 생성될 때 기본적으로 활성화됩니다.


이번 레슨은 여기까지입니다. 퀴즈를 잘 풀고 다음 레슨에서 뵙겠습니다!


## Issued Assets


<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>


:::video id=7ac63148-d730-496d-85d4-0032aaf09be1:::


이 섹션에서는 Issued Assets의 Elements 기능을 사용하는 방법을 알아봅니다.


Issued Assets를 사용하면 여러 유형의 자산을 발행하고 Elements 네트워크 참여자 간에 전송할 수 있습니다. 네트워크의 모든 노드는 자체 자산을 발행할 수 있습니다. 발행은 바우처, 쿠폰, 통화, 예금, 채권, 주식 등 모든 자산의 대체 가능한 Ownership를 나타낼 수 있습니다. Issued Assets는 자체 Trustless 거래소, 옵션 및 기타 고급 스마트 컨트랙트를 구축할 수 있는 문을 열어줍니다.


발행된 자산은 Confidential Transactions의 혜택도 받을 수 있으며, 관련 token를 보유한 사람은 누구나 재발행할 수 있습니다.


첫 번째 단계는 두 개의 Elements 노드, 즉 e1과 e2에 액세스하는 것입니다. 이 노드들은 블록체인을 리셋하고 default asset을 분할했습니다.


두 노드는 동일한 로컬 네트워크에 있으며 서로 연결되어 있으므로 트랜잭션 Mempool과 동일한 블록체인의 동일한 트랜잭션을 공유합니다. 동일한 컴퓨터에서 실행되고 있지만, 동일한 실제 Blockchain 파일을 공유하지는 않는다는 점에 주목할 필요가 있습니다. 각 노드는 합의 상태에 있고 서로 동일한 프로토콜 규칙을 준수하기 때문에 동일한 거래 내역을 포함하는 Blockchain의 로컬 복사본을 관리합니다.


네트워크의 기존 자산 발행에 대한 각 노드의 뷰를 확인하는 것부터 시작하겠습니다.


이 작업은 listissuances 명령을 사용하여 수행합니다.


```
e1-cli listissuances

e2-cli listissuances
```


보시다시피 두 노드 모두 동일한 발행 내역을 표시합니다. 두 노드 모두 on chain 초기화에서 생성된 2100만 개의 Bitcoin이라는 하나의 자산을 표시합니다. 위의 명령을 실행한 결과에서 자산의 16진수 ID와 자산에 할당된 레이블인 'Bitcoin'을 확인할 수 있습니다.


체인이 초기화될 때 default asset에는 항상 레이블이 부여된다는 점에 주목할 필요가 있습니다. 자체 자산을 발행할 때 라벨을 직접 설정할 수 있으며, 곧 그렇게 할 예정입니다. 그러기 위해서는 먼저 자체 자산을 발행해야 합니다.


E1이 새 자산을 발행하도록 합니다. 이 작업은 issueasset 명령을 사용하여 수행됩니다.


```
e1-cli issueasset 100 1 false
```


'issueasset'는 3개의 매개변수를 허용합니다.


발행할 새 자산의 양. 100을 사용했습니다. 생성할 토큰의 양(토큰은 자산의 양을 다시 발행하는 데 사용됨), 이 중 1을 선택했습니다. 마지막 매개변수는 Elements에 자산 발행을 blinded 또는 unblinded으로 생성하도록 지시합니다. 1분 후에 e2의 발행 금액을 확인하려면 unblinded을 사용해야 하므로 거짓을 입력하겠습니다.


명령을 실행하면 발행에 대한 데이터가 반환됩니다. 여기에는 나중에 사용할 수 있도록 복사할 수 있는 transaction ID, 자산의 고유 16진수 값, 자산의 token 고유 16진수 값이 포함됩니다.


generate는 발행 거래를 확인하기 위한 블록입니다.


```
e1-cli -generate 1
```


E1에 대해 `listissuances` 명령을 다시 실행합니다.


```
e1-cli listissuances
```


이제 e1은 Bitcoin의 초기 발행과 새로 발행한 자산의 두 가지 발행을 인식하고 있으며, 이 중 100개를 볼 수 있습니다. 새 자산의 16진수 값과 Bitcoin 발행과 마찬가지로 관련 자산 레이블이 없다는 점에 유의하세요.


E2의 알려진 이슈 목록을 다시 확인하세요.


```
e2-cli listissuances
```


이는 e2가 e1이 발행한 자산을 알지 못한다는 것을 보여줍니다. 이미 볼 수 있는 Bitcoin의 초기 발행만 볼 수 있습니다.


이는 e2가 e1에서 새 자산을 발행할 때 해당 자산이 전송된 Address를 알지 못하고 감시하지 않기 때문입니다.


E2가 발행 자체를 볼 수 없더라도 e1이 자산의 일부를 e2로 보낼 수 있다는 점에 주목할 필요가 있습니다. 그러면 새 자산은 원래 발행을 인식하지 못하더라도 e2의 Wallet에 사용 가능한 잔액으로 표시됩니다.


E2에서 실제 발행량(따라서 발행된 금액)을 볼 수 있도록 하려면 Address을 감시 중인 Address로 e2에 추가해야 합니다.


이를 위해서는 자산이 전송된 Address을 찾아야 합니다. 이를 위해 앞서 복사한 transaction ID를 사용하고 e1이 해당 거래의 세부 정보를 검색하도록 하여 올바른 Address을 찾아 e2의 Wallet 감시 목록에 추가할 수 있도록 합니다.


```
e1-cli gettransaction <the-issuance-transaction-id>
```


거래 데이터의 16진수를 지나 위로 스크롤하면 새 자산 100개를 받은 Address를 볼 수 있으며, 해당 16진수 값으로 식별할 수 있습니다.


Address을 복사하여 e2로 가져올 수 있도록 합니다.


이제 Address을 e2로 가져와 보겠습니다. 이를 위해 importaddress 명령을 사용합니다.


```
e2-cli importaddress <the-issued-to-address>
```


이제 e2의 발행 목록을 확인해 보겠습니다.


```
e2-cli listissuances
```


이제 새로 발행된 자산이 목록에 포함된 것을 확인할 수 있습니다. 또한 e2 노드는 발행이 unblinded 발행이므로 관련 token의 양과 함께 발행된 자산의 양을 확인할 수 있습니다. 자산 ID를 사용하여 Elements 내에서 이름 매핑을 사용하려면 먼저 Elements을 중지하세요.


```
e1-cli stop
```


그런 다음 에셋의 16진수를 제공된 레이블에 매핑하는 추가 매개변수를 사용하여 다시 시작합니다. 이렇게 하면 노드에서 에셋에 대한 데이터를 사람이 읽기 쉬운 형식으로 표시할 수 있습니다. 원하는 경우 Elements.conf의 마지막에 추가할 수 있으며, 그러면 daemon을 시작할 때마다 인수를 추가할 필요가 없습니다. 예를 들어


```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```


하지만 여기서는 인수 메서드를 사용하겠습니다.


```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```


노드에 발행 목록을 다시 쿼리합니다.


```
e1-cli listissuances
```


이는 자산의 16진수 값과 레이블의 매핑이 제대로 작동하고 있음을 보여줍니다. E2 노드의 발행 목록을 다시 확인합니다.


```
e2-cli listissuances
```


레이블은 설정한 노드에서만 사용할 수 있으므로 e2 노드는 이 레이블에 액세스할 수 없음을 알 수 있습니다. 실제로 e2의 동일한 자산 헥스에 e1에서 했던 것과 다른 레이블을 할당할 수 있습니다. 먼저 e2 노드를 중지합니다.


```
e2-cli stop
```


새 자산의 헥스에 다른 레이블을 지정하여 다시 시작합니다.


```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```


E2에서 발행을 상장합니다.


```
e2-cli listissuances
```


자산 레이블은 각 노드에 로컬로 표시되며, 네트워크의 다른 노드에서는 자산의 16진수만 인식할 수 있습니다.


레이블을 자산 헥스에 매핑하면 거래 및 Wallet 잔액 조회와 같은 작업을 수행할 때 자산을 약어로 참조할 수 있으므로 유용합니다. 예를 들어 라벨을 사용하지 않고 새 자산의 일부(금액 10)를 e1에서 e2로 보내려고 한다고 가정해 보겠습니다.


먼저 에셋을 전송할 Address를 확보해야 합니다.


```
e2-cli getnewaddress
```


그런 다음 sendtoaddress 명령을 사용합니다.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```


블록을 생성하여 트랜잭션을 확인합니다.


```
generate 1
```


E2에서 자산이 수신되었는지 확인합니다.


```
e2-cli getwalletinfo
```


자산이 실제로 수신되었음을 확인할 수 있습니다.


E2는 수신한 자산의 헥스를 매핑하고 자체 레이블을 사용하여 표시합니다. 동일한 작업을 수행하는 더 쉬운 방법은 전송할 때 e1의 에셋 레이블을 사용하는 것입니다.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```


그 이면에는 Elements이 로컬 레이블을 16진수 값에 매핑하여 Issued Assets의 사용을 간소화하는 데 도움을 줍니다.


이 섹션에서는 자산을 발행하고 레이블을 지정하는 방법을 살펴보았습니다. 다음 섹션에서는 발행한 자산의 금액을 재발행하고 폐기하는 방법에 대해 살펴보겠습니다.


## 자산 재발급


<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>


:::video id=7df967b0-ffff-42e1-b1d5-868e76289faf:::


이 섹션에서는 이미 발행한 자산을 더 많이 발행하는 방법과 발행한 자산을 소멸하는 방법에 대해 알아봅니다.


자산을 재발행(추가 생성)하거나 자산의 양을 소각해야 하는 경우는 자산이 고정된 Supply가 없는 것을 나타내는 경우 발생할 가능성이 높습니다. 예를 들어 금고에 보관된 금을 나타내는 자산의 경우, 금 단위가 금고에 들어오고 나가면 금고의 Supply를 나타내는 자산도 그에 따라 상향 또는 하향 조정해야 합니다.


자산을 재발행하려면 자산을 처음 발행할 때 함께 생성된 관련 token의 Ownership이 필요합니다.


자산을 더 많이 생성할 때, 자산을 재발행하는 노드가 일반적으로 자산의 reissuance token라고 하는 것을 소유하고 있다면 처음에 자산을 발행한 노드가 어느 노드인지는 중요하지 않습니다. reissuance token를 처음 생성하는 방법과 이를 사용하여 자산을 재발행하는 방법, 그리고 다른 노드에게 reissuance token를 전송하여 다른 노드도 자산을 재발행할 수 있는 권한을 갖도록 하는 방법을 살펴보겠습니다.


두 개의 Elements 노드에 액세스해야 하는데, 이를 e1과 e2라고 부릅니다. 이 노드들은 블록체인을 재설정하고 default asset을 분할했습니다.


E1이 100개의 새 자산을 발행하고 동일한 자산에 대해 reissuance token 1개를 생성하겠습니다. 예제를 단순화하기 위해 unblinded으로 발행을 생성하겠습니다. 이제 자산과 관련 reissuance token를 발행해 보겠습니다.


```
e1-cli issueasset 100 1 false
```


자산의 ID와 (재발급) token의 ID도 기록해 두세요.


나중에 e2에서 더 많은 자산을 재발행할 예정이므로 자산이 발급된 transaction ID을 메모하고 이를 사용하여 자산이 전송된 Address를 가져와야 합니다.


거래를 확인합니다.


```
e1-cli -generate 1
```


이제 gettransaction 명령을 사용하여 트랜잭션의 세부 정보를 확인하겠습니다:


```
e1-cli gettransaction <txid>
```


거래 데이터의 헥스를 지나 위로 스크롤하면 거래에서 e1이 1 reissuance token과 관련 자산 100개를 받은 것을 확인할 수 있습니다.


Address의 사본을 가져와서 e2로 가져올 수 있도록 합니다.


이제 Address을 e2의 Wallet로 가져옵니다.


```
e2-cli importaddress <address>
```


이제 e1과 e2가 모두 자산 발행을 인지하고 있음을 알 수 있습니다.


```
e1-cli listissuances

e2-cli listissuances
```


현재 e1은 자산의 일부와 1 reissuance token를 보유하고 있지만 e2는 보유하고 있지 않습니다.


```
e1-cli getwalletinfo
```


또한 e1은 거래 수수료를 충당하기 위해 소액을 지불했기 때문에 이전보다 default asset이 적다는 점에 유의하세요. 이 금액은 생성된 블록이 100블록 이상 만기될 때 e1에서 징수할 예정입니다.


```
e2-cli getwalletinfo
```


E1은 reissuance token을 보유하고 있으므로 더 많은 것을 재발급할 수 있습니다. 이 작업은 reissueasset 명령을 사용하여 수행합니다. E1이 자산을 100개 더 재발행하도록 해 봅시다.


```
e1-cli reissueasset <asset-id> 100
```


재발급이 제대로 되었는지 확인했습니다.


```
e1-cli getwalletinfo
```


이제 예상대로 e1이 200개의 자산을 보유하고 있음을 알 수 있습니다.


E2는 reissuance token를 보유하고 있지 않으므로 자산을 재발급하려고 하면 오류가 발생합니다.


```
e2-cli reissueasset <asset-id> 100
```


오류 메시지에 유의하세요.


listissuances 명령을 사용하여 e1에서 재발급에 대한 세부 정보를 볼 수 있습니다.


```
e1-cli listissuances
```


Is_reissuance` 플래그에 유의하세요.


이제 e2에 reissuance token을 보내면 자산의 일정 금액을 직접 재발급할 수 있습니다. 먼저 이를 보낼 Address이 필요합니다. reissuance token은 잔액을 전송하고 표시할 때 Elements 내의 다른 자산과 동일하게 취급되며 다른 자산과 마찬가지로 더 작은 단위로 나눌 수 있으므로 자산을 재발행하기 위해 1 reissuance token을 e2로 보낼 필요는 없습니다. 어떤 액면으로도 충분합니다. E2가 reissuance token을 받기 위해 Address을 생성합니다.


```
e2-cli getnewaddress
```


그런 다음 RIT의 일부를 e1에서 e2로 보냅니다.


```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```


거래를 확인합니다.


```
e1-cli -generate 1
```


이제 e2가 전송된 0.1을 보유하고 있음을 알 수 있습니다.


```
e2-cli getwalletinfo
```


즉, e2는 이제 Wallet에서 보유하고 있는 RIT와 관련된 자산을 더 많이 재발행할 수 있습니다. E2는 500개의 자산을 재발행할 것입니다.


```
e2-cli reissueasset <asset-id> 500
```


재발급 결과를 확인합니다.


```
e2-cli getwalletinfo
```


E2는 현재 Wallet 잔고에 재발행된 금액을 보유하고 있으며 자산 재발행 과정에서 RIT 자체가 소비되지 않았음을 알 수 있습니다.


자산을 파기하는 것은 파기할 금액 이상을 보유한 사람이라면 누구나 할 수 있는 일이며, reissuance token의 적용을 받지 않습니다.


```
e2-cli destroyamount <asset-id>

e2-cli getwalletinfo
```


이 섹션에서는 자산을 발행하는 방법과 함께 자산 발행의 일부로 선택적으로 생성되는 reissuance token을 활용하는 방법을 살펴보았습니다. 또한 reissuance token을 양도하는 것이 다른 자산을 양도하는 것만큼 간단하며, reissuance token을 일정량 이상 보유하면 보유자에게 관련 자산을 더 많이 발행할 수 있는 권한이 부여된다는 사실도 살펴보았습니다. 따라서 네트워크에서 토큰 재발행에 접근할 수 있는 사람을 통제하는 것은 매우 중요합니다. 또한 자산을 소멸하는 방법과 이 과정이 reissuance token의 소유에 의해 통제되지 않는다는 사실도 확인했습니다.


# 요소 페더레이션


<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>


## block signing


<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>


:::video id=c5a81820-77d7-4a0c-9a4e-9323386a74ac:::


Elements은 연합 서명 모델을 지원하여 유효한 블록을 생성하기 위해 제안된 블록에 서명해야 하는 Strong Federation 멤버의 수를 지정할 수 있습니다.


이전에는 예를 들어 쉽게 설명하기 위해 `generate` 명령을 사용해 블록을 생성했는데, 생성된 블록이 네트워크에서 유효한 것으로 승인되기 위해 다중 서명 요건을 충족할 필요는 없었습니다.


2대 2 Multisig 블록 생성이 필요하도록 노드를 설정할 것입니다. 이는 구성 파일에 추가하거나 시작 시 노드에 전달할 수 있는 signblockscript 파라미터를 사용하여 설정할 수 있습니다. 이 파라미터로 체인을 초기화하려면 먼저 체인을 구성하는 스크립트를 빌드해야 합니다.


기존 노드 몇 개를 사용해 이 작업을 수행하고, 노드가 출력하는 데이터를 저장한 다음 체인을 지워 signblockscript 매개변수를 사용해 다시 시작할 수 있도록 합니다. 이는 스크립트가 네트워크 합의 규칙의 일부를 구성하기 때문에 필요하며, on chain 초기화를 설정해야 합니다. 나중에 이미 존재하는 체인에 추가할 수 없습니다.


E1과 e2라고 부르는 두 개의 Elements 노드에 액세스해야 합니다. 이 노드들은 블록체인을 재설정하고 default asset을 분할했습니다.


con_max_block_sig_size 매개변수가 Elements.conf 파일에서 높은 값으로 설정되어 있는지 확인하세요. 그렇지 않으면 이 섹션의 뒷부분에서 block signing가 실패합니다. 이 튜토리얼에서는 con_max_block_sig_size=2000으로 설정했습니다.


Blockchain를 리셋하고 e1 및 e2와 연결된 지갑을 지울 것이므로, 나중에 사용할 수 있도록 주소, 공개 키 및 개인 키의 사본을 block signing 스크립트의 generate으로 가져가야 합니다.


먼저 block signing 노드에서 generate 노드가 될 각각의 Address을 새로 복사해야 합니다.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


그런 다음 주소에서 공개 키를 추출하여 나중에 사용할 수 있도록 메모해 두어야 합니다.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


그런 다음 나중에 다시 가져올 개인 키를 추출하여 Blockchain 및 Wallet 데이터를 다시 초기화한 후 노드가 블록에 서명할 수 있도록 합니다.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


이제 2중 2 다중 서명 요구 사항이 있는 Redeem 스크립트를 generate해야 합니다. 이를 위해 createmultisig 명령을 사용하고 첫 번째 매개변수를 2로 전달한 다음 두 개의 공개 키를 제공하면 됩니다. 나중에 블록이 생성될 때 Ownership가 증명해야 하는 것은 바로 이 키입니다.


노드 e1 또는 e2 중 하나는 generate을 Multisig로 만들 수 있습니다.


```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```


이렇게 하면 redeemscript가 생성되며, 나중에 복사하여 사용할 수 있습니다.


이제 체인의 합의 규칙의 일부로 새로운 signblockscript로 다시 시작할 수 있도록 기존 Blockchain과 Wallet 데이터를 지워야 합니다. 그렇기 때문에 새 체인에서 블록을 서명하는 데 사용할 개인 키와 같은 일부 데이터의 복사본을 미리 만들어야 했습니다. 계속 진행하기 전에 이 작업을 수행해야 합니다.


기존 Wallet과 체인 데이터가 삭제되었으므로 이제 노드를 시작하고 signblockscript 파라미터를 사용하여 새 체인을 초기화하도록 할 수 있습니다. 이 예제에서는 고급 기능이 필요하지 않으므로 -evbparams=dynafed:0:: 를 전달하여 dynafed 활성화를 비활성화하겠습니다.


```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::

e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```


이제 노드가 제안된 블록에 서명하고 완료할 수 있도록 앞서 저장한 개인 키를 가져와야 합니다.


```
e1-cli importprivkey <e1-priv-key>

e2-cli importprivkey <e2-priv-key>
```


이제 generate 명령의 사용은 현재 노드에서 시행하는 필수 block signing 규칙을 충족하지 못하므로 오류가 발생합니다.


```
e1-cli -generate 1
```


새 블록을 제안하기 위해 어느 노드든 getnewblockhex 명령을 호출할 수 있습니다. 이는 네트워크의 모든 노드에서 승인되기 전에 서명이 필요한 새 블록의 16진수를 반환합니다.


```
e1-cli getnewblockhex
```


이 명령은 제안된 블록을 생성할 뿐, generate 블록을 생성하는 것은 아니라는 점을 기억하세요.


이를 확인하기 위해 현재 Blockchain에 블록이 없는 것을 확인할 수 있습니다.


```
e1-cli getblockcount
```


먼저 서명하지 않고 블록 헥스를 제출하려고 합니다.


```
e1-cli submitblock <block-hex>
```


블록 증명이 유효하지 않다는 메시지가 표시됩니다. 이는 필요한 2명의 당사자 중 2명이 아직 서명하지 않았기 때문입니다.


이제 e1이 제안된 블록에 서명하도록 하겠습니다.


```
e1-cli signblock <block-hex>
```


E2에게 육각에 서명하게 합니다.


```
e2-cli signblock <block-hex>
```


E2는 제안된 블록에 서명하는 e1에서 생성된 출력에 서명하지 않는다는 점에 유의하세요. 둘은 서로의 결과와 독립적으로 제안된 블록에 서명합니다.


이제 e1과 e2의 블록 서명을 결합해야 합니다. 어느 노드든 이 작업을 수행할 수 있으며, 다른 노드의 서명된 블록 헥스만 있으면 됩니다.


```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```


combineblocksigs 명령은 서명된 블록의 헥스와 완료 상태를 출력하여 블록 헥스를 제출할 준비가 되었음을 알려줍니다.


이제 어느 노드든 완성된 블록 헥스를 제출할 수 있습니다. E1이 이를 수행하도록 하겠습니다.


```
e1-cli submitblock <combined-signed-hex>
```


제출물이 유효한 제출물인지 확인합니다.


```
e1-cli getblockcount

e2-cli getblockcount
```


E1과 e2 모두 블록을 유효한 것으로 수락하고 로컬 복사본의 Blockchain 끝에 추가한 것을 볼 수 있습니다.


프로세스를 요약하면 다음과 같습니다. 이 섹션에서는


- 블록을 제안했습니다.
- 각 노드에 서명을 받습니다.
- 서명을 결합했습니다.
- 서명이 유효하고 체인의 redeemscript 임계값을 충족하는지 확인했습니다.
- 블록을 제출했습니다.


네트워크의 각 노드는 블록의 유효성을 검사하고 Blockchain의 로컬 사본에 블록을 추가했습니다.


### block signing


처음에는 프로세스가 복잡해 보이지만 block signing과 Elements의 순서는 항상 동일하며 초기 설정은 한 번만 수행하면 됩니다:


1. 초기 설정(1회 수행)

2. 연합 블록 서명자의 공개 키를 사용하여 'signblockscript'이라는 다중 서명 Address를 생성합니다.

3. 이 스크립트의 Redeem 스크립트는 새로운 Blockchain를 시작하는 데 사용됩니다.

4. 블록 생산(진행 중)

5. 제안된 블록이 생성되고 서명을 위해 교환됩니다.


임계값에 해당하는 수의 서명자가 제안된 블록에 서명하면 블록이 결합되어 네트워크에 제출됩니다. 체인의 'signblockscript'의 기준을 충족하면 노드는 이를 유효한 블록으로 받아들입니다.


## 사이드 체인으로서의 요소


<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>


:::video id=c15e7eaf-9b5d-4696-bb36-bd10e7b56967:::


Elements은 오픈소스 범용 Blockchain 플랫폼으로, Bitcoin와 같은 기존 Blockchain에 '페깅'할 수도 있습니다. 다른 Blockchain에 페깅되면 Elements은 'Sidechain'로 작동한다고 합니다. 사이드체인은 한 체인에서 다른 체인으로 자산을 양방향으로 전송할 수 있게 해줍니다. Elements을 Sidechain로 구현하면 mainchain의 내재적 한계를 일부 해결하면서 mainchain에 보호된 자산이 제공하는 보안을 어느 정도 유지할 수 있습니다.


Sidechain은 mainchain와 그 거래 내역을 인식하지만, mainchain는 Sidechain을 인식하지 못하며 작동에 필요하지 않습니다. 이를 통해 사이드체인은 mainchain 프로토콜 개선 제안과 관련된 제한이나 지연 없이 혁신할 수 있습니다. 메인 프로토콜을 직접 변경하지 않고 확장하면 mainchain 자체의 보안과 전문성을 유지하여 Sidechain의 원활한 작동을 뒷받침할 수 있습니다.


Bitcoin의 기능을 확장하고 기본 보안을 활용함으로써 Elements 기반 Sidechain은 이전에는 mainchain 사용자에게 제공되지 않았던 새로운 기능을 제공할 수 있습니다. 실제 사용 중인 Elements 기반 Sidechain의 예로는 Liquid Network가 있습니다.


Elements Blockchain을 Sidechain로 초기화하려면 federated peg script 파라미터를 사용해야 합니다. 이 매개변수는 노드의 구성 파일에서 설정하거나 시작 시 전달할 수 있습니다.


federated peg script는 Strong Federation의 어떤 멤버가 페그인 및 페그아웃 기능을 수행할 수 있는지 정의합니다. 이러한 기능자는 mainchain과 Sidechain에서 유효한 페그인 및 페그아웃 트랜잭션을 감시하고 유효한 경우 이를 실행하기 때문에 'watchmen'이라고 합니다. '페그아웃'은 페깅된 자산을 Sidechain에서 mainchain로 이동하는 것을 의미하며, '페그인'은 페깅된 자산을 mainchain에서 Sidechain로 이동하는 것을 의미합니다. 'Sidechain로 이동'이라고 할 때 실제로는 자금이 mainchain의 다중 서명 Address에 고정되고 그에 해당하는 양의 자산이 Elements Sidechain에 생성되는 것을 의미합니다. 'Sidechain에서 이동'이라는 말은 Elements Sidechain에서 자산이 소멸되고 mainchain에 보관된 잠긴 자금에서 해당 금액이 해제된다는 의미입니다. 페그인 및 페그아웃 기능을 수행하려면 기능 담당자가 federated peg script에 사용된 공개 키 중 Ownership을 증명해야 합니다. 이는 해당 개인키를 사용하여 수행됩니다.


따라서 federated peg script를 생성하려면 먼저 각 노드 generate에 공개키가 있어야 합니다. 또한 기존 체인 데이터를 모두 지우고 federated peg script를 사용하여 새 체인을 초기화해야 하므로 나중에 사용할 수 있도록 관련 개인키를 저장해야 합니다. 이는 federated peg script가 Sidechain의 합의 규칙의 일부를 형성하며, 나중에 페깅되지 않은 기존 Blockchain에 적용될 수 없기 때문입니다.


따라서 각 노드에 Address를 생성하고 나중에 사용할 수 있도록 관련 데이터를 저장하고 generate은 나중에 Sidechain을 초기화하는 데 사용할 federated peg script을 생성해 보겠습니다.


먼저 네트워크에서 watchmen 역할을 할 각 노드를 generate에 새로운 Address로 연결해야 합니다.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


그런 다음 Address의 유효성을 검사하여 공개 키를 얻습니다.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


그런 다음 각 Address와 연결된 개인 키를 검색합니다.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


나중에 사용할 수 있도록 개인 키와 공개 키를 저장합니다.


이제 federated peg script를 사용하여 새 체인을 초기화할 것이므로 기존 Blockchain 및 Wallet 데이터를 지워야 합니다. 이제 이 작업을 수행할 수 있습니다. 페그인해야 할 Bitcoin daemon를 시작하는 것을 잊지 마세요.


이제 앞서 저장한 공개키를 사용해 만든 federated peg script으로 새 체인을 초기화할 수 있습니다. 우리가 입력하고 공개 키를 둘러싼 숫자는 사용되는 키의 수를 정의하고 구분하며, Sidechain에 페그인 및 페그아웃하기 위해 증명해야 하는 키 Ownership을 정의합니다.


```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae

e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```


이제 이전에 저장한 개인 키를 가져와서 나중에 노드가 체인 간 자산 전송을 서명하고 완료하고 federated peg script의 요구 사항을 충족할 수 있도록 합니다.


```
e1-cli importprivkey <priv-key-1>

e2-cli importprivkey <priv-key-1>
```


이제 두 체인 모두에서 일부 블록을 성숙시켜야 합니다. 블록의 성숙도는 mainchain의 블록 재구성으로 인해 pegged asset Supply이 Sidechain 내에서 인플레이션되는 것을 방지하기 위한 페그 프로세스의 필수 요건입니다.


이번 섹션에서는 federated peg에 초점을 맞추기 위해 지난 섹션에서 살펴본 block signing 모델을 사용하지 않고 블록을 생성하고, 다시 'generate' 명령을 사용하여 새 블록을 생성하도록 하겠습니다.


```
b-cli generate 101

e1-cli generate 1
```


지금 당장 Elements을 위해 generate 블록을 만들 필요는 없습니다. 하지만 어쨌든 generate를 만들어 봅시다. 잠재적인 불일치를 피하는 것이 좋습니다.


이제 체인을 페그인할 준비가 되었습니다. 페그인을 하려면 getpeginaddress 명령을 사용하여 특수한 종류의 Address을 generate해야 합니다. getpeginaddress으로 페그인 Address을 생성하고 claimpegin로 이를 청구하는 사이의 기간을 최대한 짧게 유지해야 합니다. 페그인 주소는 장기적으로 지속되지 않으므로 재사용해서는 안 됩니다.


```
e1-cli getpeginaddress
```


이 명령은 페그인 자금을 청구하기 위해 충족해야 하는 새 스크립트뿐만 아니라 새 mainchain Address을 생성하는 것을 볼 수 있습니다. mainchain Address은 watchmen 네트워크 내에서 Elements 역할을 수행하는 기능자가 사용할 '스크립트 Hash에 대한 지불' Address입니다.


getnewaddress과 마찬가지로 getpeginaddress는 호출 노드의 Wallet에 새로운 비밀을 추가하므로 Wallet 파일의 백업을 노드 관리 프로세스에 고려하는 것이 중요합니다.


이제 mainchain에서 Bitcoin을 Sidechain로 보내겠습니다. mainchain 회귀 테스트 Wallet에는 이미 일부 자금이 있습니다.


```
b-cli getwalletinfo
```


Wallet이 Bitcoin 50개를 보유하고 있음을 알 수 있습니다. mainchain에서 Bitcoin 하나를 Sidechain로 보내겠습니다. 앞서 노드에서 생성한 mainchain Address로 자금을 보내야 합니다.


```
b-cli sendtoaddress <e1-pegin-address>
```


나중에 자금 증빙을 위해 이 거래의 ID를 보관해야 하므로 보관해야 합니다.


이제 mainchain Wallet 잔액이 송금한 금액만큼 감소하고 거래 수수료를 충당하기 위한 소액이 추가로 감소한 것을 확인할 수 있습니다.


```
b-cli getwalletinfo
```


거래를 다시 성숙시켜야 합니다.


```
b-cli generate 101
```


Elements 노드가 페그인 자금을 청구하기 위해서는 페그인 거래가 이루어졌다는 '증거'를 확보해야 합니다. 암호학적 증명은 자금 transaction ID을 사용하여 메르켈 경로를 계산하고 트랜잭션이 확인된 블록에 존재함을 증명합니다.


```
b-cli gettxoutproof '["<tx-id>"]'
```


또한 원시 거래 데이터도 필요합니다.


```
b-cli getrawtransaction <tx-id>
```


페그인 트랜잭션에 대한 증명과 원시 데이터를 확보한 Elements 노드는 이제 원시 트랜잭션과 트랜잭션 증명을 사용하여 페그인을 주장할 수 있습니다.


```
e1-cli claimpegin <raw> <proof>
```


claimpegin에 제공할 수 있는 선택적 세 번째 인수가 있다는 점에 유의하세요. 이 세 번째 매개변수는 청구된 자금을 전송할 Sidechain Address을 지정하는 데 사용할 수 있습니다. 이 예제에서는 청구된 자금을 보낼 Address을 소유한 동일한 노드에서 명령을 호출했기 때문에 이 인수는 필요하지 않았습니다.


E1의 잔액을 확인합니다.


```
e1-cli getwalletinfo
```


클레임을 확인하기 위해 블록을 생성합니다.


```
e1-cli generate 1
```


E1의 잔액을 확인합니다.


```
e1-cli getwalletinfo
```


페그인이 성공적으로 청구되었음을 확인할 수 있습니다.


페그아웃의 과정도 비슷합니다. Address가 생성되고 자금이 전송되며 거래가 유효하면 자금이 릴리스된다는 점에서 비슷합니다. 전체 페그아웃 과정은 이 강좌의 범위를 벗어나는 mainchain에 대한 작업이 포함되므로 여기서는 다루지 않겠습니다. Elements 이벤트의 단계는 mainchain에서 Address가 생성되는 것입니다.


```
b-cli getnewaddress
```


자금은 sendtomainchain 명령을 사용하여 Elements 노드에서 mainchain Address로 전송됩니다.


```
e1-cli sendtomainchain <new-address> 1
```


트랜잭션을 확인하기 위해 블록을 생성합니다.


```
e1-cli generate 1
```


노드의 Wallet 잔액을 확인합니다.


```
e1-cli getwalletinfo
```


그리고 잔액이 줄어든 것을 확인합니다.


이 섹션에서는 방법을 살펴봤습니다:


- generate a federated peg script.
- 스크립트를 네트워크 합의 매개변수 규칙으로 사용하는 새 체인을 초기화합니다.
- mainchain에서 Sidechain로 자금을 송금합니다.
- Elements Sidechain 내에서 자금을 청구하세요.
- mainchain으로 자금을 송금하는 방법을 이해합니다.


### 페더레이션 페그스크립트



Elements가 Sidechain로 작동하도록 하려면 Blockchain의 Genesis 블록에 `fedpegscript`가 있는 상태로 생성해야 합니다. 이는 노드 시작 시 `fedpegscript` 파라미터를 전달하여 수행됩니다. 그러면 이 스크립트는 Elements Blockchain의 합의 규칙의 일부를 구성하고 페그인 및 페그아웃 요청을 검증하고 실행할 수 있게 됩니다.


'페그 스크립트'는 페그 작업을 수행할 권한이 있는 사람이 제어하는 공개 키로 구성됩니다. 다음은 2대 2 다중 서명 페드페그 스크립트의 예시 형식입니다:


```
fedpegscript=5221<public key 1>21<public key 2>52ae
```


참고: 공개키 외부의 문자는 공개키와 'm'의 'n' 요구사항을 나타내는 구분 기호입니다. 예를 들어, 1 대 1 페드펙 스크립트의 템플릿은 '5121<공개 키 1>51ae'입니다.


### 페그인


Elements Sidechain에서 페그인을 수락하기 전에 mainchain에서 충분한 확인을 받아야 합니다. 이는 mainchain의 재구성으로 인해 발생할 수 있는 Elements Sidechain의 Supply 인플레이션을 방지하기 위해 필요합니다.


Proof of Work(작업 증명) 합의 메커니즘의 정상적인 작동의 일환으로 Bitcoin Blockchain의 끝부분이 짧게 재구성될 것으로 예상됩니다. 따라서 Elements은 Bitcoin Blockchain 내에서 충분한 깊이가 있는 경우에만 페그인을 유효한 것으로 받아들입니다. 이는 Elements이 동일한 페그인을 두 번 이상 수락하는 것을 방지하는 역할을 합니다.


### 페그아웃


페그아웃은 Elements 노드가 `sendtomainchain` 명령을 호출할 때 발생하며, 이 명령은 mainchain Address(페그아웃 대상)과 `인출`할 pegged asset의 양을 입력으로 받습니다. 이렇게 하면 Sidechain에 페그아웃 트랜잭션이 생성됩니다. watchmen 역할을 하는 오퍼레이터는 Sidechain에서 페그아웃 거래가 확인된 것을 감지하면, 앞서 배운 대로 mainchain의 자산을 페그아웃 대상에게 실제로 릴리스하는 작업을 처리합니다.


## 독립형 Blockchain로서의 Elements


<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>


:::video id=4955306b-4be3-429c-9d30-068f7644ea73:::


지금까지 Elements를 Sidechain으로 실행하는 방법에 대해 살펴봤습니다. 그러나 자체 기본 네이티브 자산을 사용하여 독립형 Blockchain 솔루션으로도 작동할 수 있습니다. 이 설정에서 Elements Blockchain는 Confidential Transactions 및 Issued Assets과 같은 Sidechain 구현의 모든 기능을 그대로 유지하지만 유통에서 default asset 금액을 추가하거나 제거하기 위한 페그인 또는 페그아웃이 필요하지 않습니다.


이 섹션에서는 다음과 같이 설명합니다:


'newasset'이라는 이름의 default asset로 새 Elements Blockchain을 초기화합니다.


생성할 '신규 자산' 1,000,000개와 이를 위한 재발행 토큰 2개를 지정합니다.


모든 anyone-can-spend '신규 자산' 코인을 획득하세요.


'신규 자산'에 대한 모든 anyone-can-spend 재발급 토큰을 청구합니다.


에셋과 해당 reissuance token을 다른 노드의 Wallet로 보냅니다.


두 노드에서 더 많은 '신규 자산'을 재발행합니다.


독립형 Blockchain로 작동하도록 Elements 네트워크를 초기화하려면 각 노드를 몇 가지 기본 파라미터로 시작해야 합니다. 이러한 매개변수는 노드에 다른 Blockchain의 페그인을 시도하지 않고 유효성을 검사하도록 지시하는 데 사용되며, 네트워크의 default asset 이름과 생성할 default asset 및 연결된 reissuance token의 양을 지정합니다.


이제 연결된 두 개의 Elements 노드에서 이 매개변수를 사용하여 새로운 체인을 시작하겠습니다. default asset의 이름을 `새로운 자산`으로 지정하고 100만 개와 `새로운 자산` 재발행 토큰 2개를 발행합니다.


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000

e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


여기서 사용된 금액은 네트워크에서 허용할 수 있는 가장 작은 액면가이므로, 2억 개의 재발행 토큰은 실제로는 전체 토큰 2개에 해당합니다. 초기 무료 코인의 액면가도 마찬가지입니다.


노드의 현재 Wallet 잔액을 확인하세요.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


초기화가 올바르게 작동했음을 알 수 있습니다.


초기 발행 자산은 '누구나 사용할 수 있는' 상태로 생성되므로, e1이 자산을 모두 소유하게 하여 e2의 접근 권한을 제거할 수 있습니다.


```
e1-cli getnewaddress

e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```


전송할 자산은 이미 default asset이므로 'newasset'을 지정할 필요가 없으며, 따라서 네트워크 요금을 지불하는 데 사용되는 default asset도 마찬가지입니다.


Elements 내에서 여러 자산 유형을 동일한 Address로 보낼 수 있으므로 방금 생성한 Address를 재사용하여 default asset을 수신하고 재발행 토큰의 대상 Address로 사용할 수 있습니다.


```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


거래를 확인합니다.


```
e1-cli generate 101
```


현재 자산과 reissuance token의 유일한 보유자는 e1임을 확인하겠습니다.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


실제로 그렇다는 것을 알 수 있습니다.


이제 '신규 자산'의 일부를 현재 잔고가 0인 e2에게 보냅니다.


```
e2-cli getnewaddress

e1-cli sendtoaddress <e2-address> 500 "" "" false
```


네트워크의 default asset로 'newasset'이 생성되었으므로 전송할 자산 유형을 지정할 필요가 없습니다


또한 'newasset'에 대한 재발행 토큰 중 일부를 e2로 보내겠습니다.


```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


거래를 확인합니다.


```
e1-cli generate 101
```


지갑이 그에 따라 업데이트되었는지 확인할 수 있습니다.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


이제 e1에서 default asset 중 일부를 재발급하겠습니다. 이 기능은 초기 재발급 토큰 시작 매개변수를 통해 활성화할 수 있습니다. 이 매개 변수를 생략하거나 0으로 설정하면 나중에 default asset를 재발급할 수 없게 됩니다.


```
e1-cli reissueasset newasset 100
```


Elements 체인은 항상 default asset에 레이블을 붙이기 때문에 16진수 ID 값을 제공할 필요 없이 'newasset'이라는 레이블을 사용할 수 있었습니다.


default asset 재발급이 작동하는지 확인합니다:


```
e1-cli generate 101

e1-cli getwalletinfo
```


이제 e2는 '신규 자산' 재발행 토큰을 일부 보유하고 있기 때문에 default asset도 재발행할 수 있음을 증명할 것입니다.


```
e2-cli reissueasset newasset 100
```


E2에서 default asset 재발급이 작동하는지 확인합니다.


```
e2-cli generate 101

e2-cli getwalletinfo
```


이 섹션에서는 Elements를 독립형 Blockchain로 설정하고 기본 기능이 예상대로 작동하는지 확인했습니다.


시작 매개 변수를 사용했습니다:


'newasset'이라는 이름의 default asset으로 새 Elements Blockchain를 초기화합니다.


on chain 초기화를 생성할 default asset의 양을 지정합니다.


default asset에 대한 재발급 토큰을 생성하고 두 노드에서 더 많은 default asset을 재발급합니다.


독립형 Blockchain Elements 네트워크에서 다른 모든 트랜잭션 작업은 강좌의 주요 섹션에서 다룬 예제와 동일한 방식으로 작동하지만 기본 및 수수료 자산으로 'Bitcoin'이 아닌 'newasset'을 사용합니다.


### 노드 시작 및 체인 초기화 파라미터


Elements 노드가 독립형 Blockchain로 작동하도록 하려면 몇 가지 파라미터를 함께 사용해야 합니다. 지금부터 각각의 매개변수를 살펴보고 그 기능을 알아보겠습니다.


#### `validatepegin=0`

독립형 Blockchain는 페그인 또는 페그아웃 트랜잭션의 유효성을 검사할 필요가 없으므로 이러한 검사를 비활성화해야 합니다. 이 설정을 사용하면 Elements 네트워크가 독립적으로 작동하므로 Bitcoin 클라이언트 소프트웨어를 실행하거나 Blockchain의 사본을 저장할 필요가 없습니다.


#### `기본 페깅된 자산 이름`

이를 통해 Blockchain 초기화 시 생성된 default asset의 이름을 지정할 수 있습니다.


#### 초기프리코인`

생성할 default asset의 숫자(Bitcoin의 Satoshi 단위와 동일)입니다.


#### `초기발행토큰`

default asset가 생성할 재발행 토큰의 수(Bitcoin의 Satoshi 단위와 동일)입니다. 이것이 없으면 default asset를 더 많이 생성할 수 없습니다. default asset의 추가 생성을 원하지 않는 경우 이 값을 0으로 설정하거나 생략할 수 있습니다.


이러한 매개변수를 사용하여 노드를 시작하는 일반적인 방법은 다음과 같습니다:


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


### 기본 작업


기본 페깅된 자산 이름` 매개 변수는 default asset에 레이블을 적용합니다. 이 설정이 없으면 default asset의 이름은 자동으로 `Bitcoin`이 됩니다. 이전 섹션에서는 자체 발행한 에셋을 다른 노드로 전송할 때 에셋 헥스 또는 로컬로 적용된 에셋 레이블을 지정하여 Elements이 어떤 에셋을 전송하는지 알려주어야 했습니다. 디폴트페깅된자산명`은 모든 노드에 적용되므로 `Bitcoin`이 아니더라도 전송할 때 이름을 지정할 필요가 없습니다. 이전에는 기본적으로 `Bitcoin`을 전송했던 모든 함수는 이제 사용자가 default asset에 레이블로 선택한 것을 전송합니다.


따라서 새로운 default asset 10개를 Address로 전송하는 것은 매우 간단합니다:


```
e1-cli sendtoaddress <destination address> 10 "" "" true
```


또한 노드에 0보다 큰 '초기재발행토큰' 값을 제공했다면 Elements를 Sidechain로 실행할 경우 불가능한 default asset을 더 많이 재발행할 수도 있습니다.


이렇게 하려면 default asset과 연결된 token를 보유한 모든 노드가 해당 형식의 명령을 실행하기만 하면 됩니다:


```
e1-cli reissueasset <default asset name> <amount>
```


위의 매개변수를 사용하면 Elements을 default asset 및 다른 블록체인과 분리된 독립형 Blockchain으로 운영할 수 있습니다.


## 결론


<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>


:::video id=bd5167d5-edba-40b0-a8b1-ba8b74493a08:::


이 과정에서는 Elements이 오픈 소스 네트워크 프로토콜로서 Sidechain을 다른 Blockchain에 연결하거나 독립형 Blockchain 솔루션으로 구현할 수 있다는 것을 배웠습니다.


Elements의 소스 코드와 웹사이트(https://github.com/ElementsProject/Elements)는 GitHub에서 호스팅되며, 빌드 온 L2(https://community.Liquid.net/c/developers/) 또는 Liquid 개발자 텔레그램(https://t.me/liquid_devel)과 같은 커뮤니티 토론 포럼에서 Elements 및 Liquid의 애플리케이션 배포 및 개발에 대해 자세히 알아볼 수 있습니다. Confidential Transactions 및 Issued Assets와 같은 주요 기능과 함께 Strong Federation의 구성원이 연합된 block signing 및 양방향 페그 메커니즘을 활성화하는 방법도 다뤘습니다.


다음 단계는 이전 섹션을 모두 아우르는 누적 퀴즈에 도전하고 Elements 여정을 시작하는 것입니다... 행운을 빕니다!


# 최종 섹션


<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>


## 리뷰 및 평가


<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## 결론


<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

<isCourseConclusion>true</isCourseConclusion>