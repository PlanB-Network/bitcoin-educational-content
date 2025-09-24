---
name: Liana
description: Liana에서 Wallet 설정 및 사용하기
---
![cover](assets/cover.webp)


![video](https://youtu.be/rTId6hfiRm0)


이 튜토리얼에서는 컴퓨터에서 Liana 애플리케이션을 사용하는 방법을 단계별로 설명해드리겠습니다. 무엇보다도 자동 승계 계획을 설정하는 방법, 일반적인 상황에서 비트코인을 받고 보내는 방법, 주어진 기간이 지난 후 기존 Wallet에서 자금을 회수하는 방법을 배우게 됩니다.


2025년 1월, Liana와 호환되는 하드웨어 지갑은 다음과 같습니다: 비트박스02, 블록스트림 제이드, 블록스트림 제이드 플러스, 콜드카드 MK4, 콜드카드 Q, Ledger 나노 S, Ledger 나노 S 플러스, Ledger 나노 X, Ledger 플렉스, 스펙터 DIY.


기존 Liana Wallet에서 자금을 회수하려면 아래 프레젠테이션을 읽고 "비트코인 회수하기" 섹션으로 바로 이동하세요.


## Liana 소프트웨어 소개


Liana은 특히 자동화된 상속 시스템이나 강력한 백업 메커니즘의 일부로 고급 지갑을 생성하고 관리하기 위해 설계된 오픈소스 소프트웨어 패키지입니다. 이 프로젝트는 케빈 로에크(Kévin Loaec)와 앙투안 푸앵소(Antoine Poinsot)가 공동 설립한 위자딘(Wizardine)에서 2022년부터 개발해왔습니다. 공식 웹사이트에서 Liana은 "복구 및 상속 기능을 갖춘 개인 큐레이션을 위한 간단한 Wallet"으로 소개되고 있습니다. 이 소프트웨어는 Linux, MacOS, Windows 등 컴퓨터에서 실행되며, (오픈) 소스 코드는 [GitHub](https://github.com/wizardsardine/Liana)에서 확인할 수 있습니다.


Liana는 Bitcoin의 프로그래밍 기능을 기반으로 고급 Wallet을 만들었습니다. 특히, 일정 시간이 경과해야만 자금을 사용할 수 있고 비트코인 회수에 관여하는 타임락(*타임락*)을 활용합니다. 따라서 Liana Wallet은 여러 가지 지출 경로로 구성됩니다:




- 항상 사용할 수 있는 주요 지출 경로입니다;
- 일정 시간이 지나면 액세스할 수 있는 복구 경로가 하나 이상 있습니다.


아래 다이어그램은 두 가지 지출 경로가 있는 Wallet의 작동을 보여줍니다:


![Schéma explicatif](assets/fr/01.webp)


이 작업을 통해 다음을 포함한 다양한 구성을 설정할 수 있습니다:




- 사용자가 사망한 경우 상속인이 자금을 회수할 수 있도록 하는 승계(또는 상속) 계획. 이 주제에 대한 자세한 내용은 BTC102 과정의 [파트 4](https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f/233c88d3-2e8e-5eba-ac06-efe67a209038)를 읽어보시기 바랍니다.
- 복구 시간이 있는 강화된 백업을 통해 사용자는 예를 들어 도난을 당했을 때 해당 비밀 문구를 보관하고 도난당할 위험 없이 Wallet을 사용할 수 있습니다.
- Bitcoin로 시작하는 사람들을 위한 안전망: Wallet은 스스로 관리하며, '보호자'(예: 친척 등)가 일정 기간이 지나면 자금을 회수할 권리를 보유합니다.
- 시간이 지남에 따라 요구 사항이 줄어드는 다자간 서명 체계(*Multisig*)로, 회사의 파트너와 같은 참여자 중 한 명 이상이 사라지는 경우에 대처할 수 있습니다.


Liana의 가장 큰 장점은 현재 지출에 사용되는 메인 키 분실 시 자금 회수를 보장하는 표준화된 방법을 도입했다는 점입니다. 이는 특히 해당 주제에 대해 잘 알지 못하는 경우 위험이 따르는 자금의 깨끗한 보관을 위한 큰 혁신을 의미합니다. 따라서 Liana는 가장 위험을 회피하는 사용자도 Bitcoin의 Cypherpunk 정신에 따라 수탁자(예: Exchange 플랫폼) 사용을 중단하고 자금을 보관하고 Ownership의 자금을 되찾을 수 있도록 장려할 수 있습니다.


물론 Liana에도 단점이 있습니다. 첫 번째는 Bitcoin Blockchain에서 거래하여 Wallet을 정기적으로 업데이트해야 한다는 것입니다. 이는 (소프트웨어 사용 빈도에 따라) 번거롭고 (당시 수수료 수준에 따라) 비용이 많이 들 수 있지만, 보안 강화를 위해 지불하는 대가입니다.


두 번째 단점은 기밀성일 수 있습니다. 다른 사람을 구성에 참여시키면 그 사람은 모든 주소를 알 수 있으므로 활동을 모니터링할 수 있습니다. 그러나 강화된 백업을 선택하거나 상속인이 Wallet의 세부 정보를 즉시 알 수 없는 승계 계획을 세우는 경우에는 문제가 되지 않습니다.


## 준비


이 튜토리얼에서는 승계 계획을 설정해 보겠습니다. 를 사용하겠습니다:




- 일상적인 비용을 위한 Ledger 나노 S 플러스;


https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4


- 자금을 회수하는 데 사용되는 블록스트림 옥입니다;


https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3


- Wallet Descriptor을 저장할 저장 미디어(USB 스틱) 2개;
- 자금 회수 지침이 포함된 승계 서신입니다;
- 복구 장치(제이드)가 사용되지 않았는지 확인하기 위해 번호가 매겨진 봉인된 가방입니다.


## 설치 및 구성


위자드인 공식 웹사이트(https://wizardsardine.com/Liana/)를 방문하여 Liana을 다운로드하세요. 소프트웨어의 진위 여부를 확인할 수 있는 GitHub 리포지토리(https://github.com/wizardsardine/Liana/releases)에서 최신 버전을 다운로드할 수도 있습니다. 이 튜토리얼에 사용된 버전은 0.9입니다.


![Télécharger Liana](assets/fr/02.webp)


설치 전에 소프트웨어의 진위 여부와 무결성을 수동으로 확인하는 방법을 알아보려면 이 튜토리얼 을 참조하는 것이 좋습니다:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

컴퓨터에 소프트웨어를 설치하고 실행합니다. "*새 Liana Wallet 만들기*" 옵션을 선택하여 Wallet를 구성합니다.


![Accueil Liana](assets/fr/03.webp)


Wallet 유형을 선택합니다. 복구 시간이 포함된 향상된 백업을 설정하려면 '*자체 구축*' 옵션을 선택하고 기본 구성표를 선택하면 됩니다. 이 옵션은 Hardware Wallet 복구 문구를 유지할 필요가 없다는 점을 제외하면 거의 동일한 방식으로 작동합니다.


여기서는 좀 더 복잡한 구성을 설정하는 *확장형 Multisig*의 경우는 제외합니다.


이 튜토리얼에서는 간단한 상속을 사용하겠습니다.


![Choisir type de portefeuille](assets/fr/04.webp)


간단한 설명은 다음과 같습니다.


![Rapide explication](assets/fr/05.webp)


설명을 읽으셨다면 Liana Wallet의 키를 설정할 수 있습니다. 이는 계정의 지출 특성을 결정하기 때문에 매우 중요한 단계입니다.


![Configurer clés](assets/fr/06.webp)


우선, "고급 설정" 메뉴에서 "Descriptor 유형", 즉 Contract가 체인에 기록되는 방식을 결정할 수 있습니다. 두 가지 유형 중에서 선택할 수 있습니다: P2WSH(SegWit) 또는 Taproot. 두 경우 모두 지출 조건의 의미는 동일합니다. P2WSH는 Contract를 더 이해하기 쉽게 만들지만, Taproot은 사용하지 않은 조건을 숨기고 검색 시 비용을 절약할 수 있다는 점에서 더 우수합니다.


이 옵션은 선택 사항이므로 확실하지 않은 경우 기본 옵션(버전 0.9의 경우 P2WSH)을 그대로 두세요(단, 변경될 수 있음).


![Choisir le type de descripteur](assets/fr/07.webp)


다음으로, 기본 키(*기본 키*)를 구성합니다. 이 키(또는 이 키 세트)는 현재 자금 지출에 사용되며, 타이밍 조건이 적용되지 않습니다. "*세트*"를 클릭하면 해당 *서명 장치*를 선택할 수 있습니다. 저희의 경우 Ledger Nano S Plus Hardware Wallet를 선택했습니다.


장치에서 확장 공개 키의 공유를 승인합니다. 이 키에 의미 있는 이름을 지정합니다(이 경우 "Nano S+"). 장치에 설치된 모든 애플리케이션은 계속 정상적으로 작동합니다.


![Configurer clé principale](assets/fr/08.webp)


다음으로, *상속 키*가 자금을 사용할 수 있는 시간, 즉 회수 지연을 설정합니다. 이 지연은 블록 단위로 정의되며, 각 블록은 평균 10분 간격으로 나뉩니다. 10분(1블록)에서 약 15개월(65,535블록)까지 다양합니다. 이 상한은 잠금 시간이 16비트로 인코딩되기 때문에 Bitcoin 프로토콜의 한계입니다.


특별한 상황이 아니라면 가장 긴 리드 타임인 15개월 또는 65,535블록을 선택하세요. 이렇게 하면 비용을 절감할 수 있습니다. 하지만 1년에 한 번, 항상 같은 시기에 업데이트 절차('Wallet 업데이트하기' 섹션에 설명되어 있음)를 수행하여 이 작업을 '의식화'하고 잊어버리지 않도록 하는 것이 좋습니다.


여기서는 테스트를 수행하기 위해 복구 시간을 1시간(6블록)으로 설정했습니다.


![Configurer temps de verrouillage](assets/fr/09.webp)


마지막으로 부동산 키를 설정합니다. 이 키(또는 키 세트)는 회원님이 실종된 경우 자금을 복구하는 데 사용됩니다. "*설정*"을 클릭하고 서명 장치를 선택한 다음 해당 장치에서 확장 공개 키 공유를 확인합니다.


이 튜토리얼에서는 Jade를 선택했습니다. 키에 연상되는 이름을 지정합니다(여기서는 "Jade"). 첫 번째 장치와 마찬가지로 기존 계정은 계속 작동합니다.


![Configurer clé de succession](assets/fr/10.webp)


이 모든 작업이 완료되면 모든 것이 정상인지 확인하고 "*계속*"을 클릭하여 선택 사항을 확인합니다.


![Confirmer clés](assets/fr/11.webp)


다음 단계는 Wallet Descriptor를 저장하는 것입니다. 이것은 계정에서 자금을 찾는 데 필요한 정보입니다. Mnemonic 문구와 달리 Descriptor는 자금을 사용할 수 없으므로 공개하면 기밀성 문제가 발생할 수 있습니다(상대방이 모든 거래를 알 수 있음).


USB 스틱과 같은 전자 매체에 Descriptor 사본 2부를 보관하세요. 전자 매체가 손상된 경우 액세스할 수 있도록 종이로 사본 2부를 인쇄해 두어야 합니다. 각 백업은 서명 장치와 연결해야 합니다.


![Sauvegarder descripteur](assets/fr/12.webp)


튜토리얼 마지막에 분석된 Descriptor은 다음과 같습니다:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


초기 Wallet 구성의 마지막 단계는 서명 장치 역할을 하는 각 하드웨어 지갑에서 Descriptor를 확인하는 것입니다.


![Enregistrer descripteur](assets/fr/13.webp)


각 서명 장치에 대해 동일한 작업을 수행합니다. 각 Hardware Wallet에 Descriptor이 추가되었는지 확인하고 확인해야 합니다.


![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)


이제 Wallet 정보가 등록되었으므로 남은 것은 Bitcoin 네트워크에 연결할 방법을 구성하는 것뿐입니다. 자체 노드(로컬 또는 원격)를 사용하거나 위자드사딘의 인프라를 사용하도록 선택할 수 있습니다. 후자의 경우 이메일 Address를 Wallet에 연결해야 Descriptor을 검색할 수 있습니다. 위자드사딘은 모든 거래에 액세스할 수 있습니다. 따라서 첫 번째 옵션이 권장됩니다.


![Sélectionner connexion réseau](assets/fr/15.webp)


저희는 자체 노드를 사용하기로 했습니다. 기존 노드를 사용하거나 머신에 *pruned 노드*를 설치할 수 있습니다. 다른 노드에 액세스할 수 없는 경우 컴퓨터에 자체 노드를 설치해야 하는데, 이 작업에는 며칠 정도 시간이 걸립니다.


![Choisir type de nœud](assets/fr/16.webp)


이 튜토리얼에서는 기존 (공용) 일렉트럼 서버를 사용했습니다. 하지만 조심하세요! 이 서버는 Liana Wallet으로 모든 활동에 액세스할 수 있었습니다. 따라서 개인 정보를 보호하려면 자체 노드를 사용하세요.


![Connexion serveur Electrum public](assets/fr/17.webp)


노드 구성이 완료되면 메인 화면이 열리고 새로 생성한 Liana Wallet가 표시됩니다.


복구 장치를 안전한 장소에 보관하세요. 사망 시 상속인이 찾을 수 있도록 전략적인 위치에 보관해야 합니다.


보안을 강화하려면 복구에 사용된 부품을 밀봉된 봉투(*변조 방지 봉투*)에 넣고 일련번호를 어딘가에 적어두면 됩니다. 이렇게 하면 아무도 접근하지 못하도록 하고 디바이스의 유효성을 유지할 수 있습니다.


이 예제에서는 다음과 같은 Elements을 조립했습니다:




- 블록스트림 제이드는 부동산의 서명 장치로 사용됩니다;
- 장치를 연결하고 충전할 수 있는 USB 케이블입니다;
- 기기가 오작동하거나 손상된 경우 문장의 종이 백업(예를 들어 크립토스틸 캡슐의 경우처럼 매체는 금속일 수도 있으므로 Elements로부터 보호됩니다);
- Wallet Descriptor가 포함된 USB 키 ;
- USB 키의 오작동 또는 손상 시를 대비한 Descriptor의 종이 백업(이 백업은 여기에서 촬영되지 않음);
- 자금 회수를 위해 취해야 할 조치를 설명하는 승계 서신입니다.


![Éléments de récupération](assets/fr/18.webp)


그리고 이 항목들을 Seal에 넣었습니다!


![Sachet scellé récupération](assets/fr/19.webp)


## 자금 수령


Liana의 메인 화면에는 잔액과 Wallet에 연결된 거래(과거 및 현재)가 표시됩니다. 저희의 경우 잔액은 0이며 이는 정상입니다.


![Écran principal](assets/fr/20.webp)


자금을 받으려면 "*수령*" 탭으로 이동하여 "*generate Address*"을 클릭합니다. 화면에 새로운 Address이 나타납니다. 기존 지갑보다 더 길어진 Address은 독립형 Contract(P2WSH 또는 Taproot)에 연결된 Address입니다.


![Générer nouvelle adresse](assets/fr/21.webp)


"*하드웨어 장치에서 확인*"을 클릭하여 Hardware Wallet에서 이 Address을 확인해야 합니다.


![Vérifier adresse portefeuille matériel](assets/fr/22.webp)


자금이 송금되면 메인 화면에 거래가 표시됩니다(처음에는 미확인으로 표시된 다음 확인됨으로 표시됨). 여기서는 이 테스트를 위해 50,000사토시(송금 당시 50달러가 조금 넘음)를 송금했습니다. 거래 수수료로 인해 실제 송금 금액은 이 값보다 훨씬 더 많아야 한다는 것은 말할 필요도 없습니다.


![Vérifier solde](assets/fr/23.webp)


"*코인*" 탭으로 이동하여 자금의 만료 상태를 확인할 수 있습니다. 이 탭에는 Wallet에 있는 다른 코인(UTXO)이 표시됩니다. 여기에서 거래로 생성된 50,000 사토시 Coin가 같은 날(1시간 후) 만료되는 것을 확인할 수 있습니다.


![Obtenir informations pièce](assets/fr/24.webp)


Bitcoin에서 사용되는 UTXO 표현 모델을 더 잘 이해하려면 Loïc Morel이 작성한 Bitcoin의 기밀성 강좌의 첫 번째 부분을 참조할 수 있습니다:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 현재 지출


현재 지출은 Liana을 사용하는 일반적인 상황입니다. 마스터 키로 비트코인을 전송하는 것은 일렉트럼 또는 Sparrow과 같은 모든 기존 Bitcoin 지갑에서와 마찬가지로 작동합니다.


송금하려면 "*송금*" 탭으로 이동하여 수취인의 BTC Address, 송금할 금액, 원하는 충전 요금 등 필수 정보를 입력하세요. 개인적인 편의를 위해 설명(로컬에 저장)을 추가할 수도 있습니다. 예시에서는 특정 Bob에 10,000사토시를 4사토시/개, 즉 거래 시점에 $0.67의 충전 요금으로 전송했습니다.


Liana은 'Coin 제어' 기능도 제공합니다. 어떤 Coin(UTXO)를 사용할지 지정합니다. 여기서는 이전에 생성한 50,000개의 사토시 Coin를 선택했습니다.


![Envoyer fonds clé principale](assets/fr/25.webp)


그런 다음 "*서명*"을 클릭하여 마스터 키에 연결된 서명 장치로 거래에 서명합니다. Hardware Wallet에서 거래를 확인하고 확인해야 합니다. 여기서는 Nano S Plus를 사용하여 트랜잭션에 서명했습니다.


![Signer transaction clé principale](assets/fr/26.webp)


마지막으로 "*브로드캐스트*"를 클릭하여 네트워크를 통해 트랜잭션을 브로드캐스트합니다. 자금을 송금하면 사용한 코인의 회수 시간이 초기화된다는 점에 유의하세요.


![Diffuser transaction clé principale](assets/fr/27.webp)


거래가 메인 화면에 표시되고 잔액이 업데이트됩니다.


![Solde après dépense](assets/fr/28.webp)


## 포트폴리오 업데이트


위에서 설명한 것처럼 Liana Wallet은 Blockchain에서 거래를 수행하여 자금을 정기적으로 업데이트해야 합니다. 그렇게 하지 않으면 상속인(또는 강화 백업의 경우 두 번째 장치)이 자금을 회수할 수 있습니다. 이러한 상황은 매우 위험하지는 않지만, 신뢰할 수 있는 제3자에게 의존하지 않고 비트코인을 계속 관리하면서 안전망의 혜택을 누리고자 하는 이 메커니즘의 설정 목적에 어긋납니다.


자금(또는 일부)이 만료되기 전에 경고가 표시되며 복구 키로 사용할 수 있습니다. 이 메시지는 "복구 경로"(*복구 경로*)를 곧 사용할 수 있음을 나타냅니다. 저희의 경우 복구 시간이 1시간으로 짧기 때문에 이 메시지가 바로 표시됩니다.


![Avertissement chemin récupération](assets/fr/29.webp)


마감일이 가까워지면 해당 자금을 업데이트하라는 버튼이 나타납니다.


![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)


코인을 업데이트하려면 "*코인*" 탭으로 이동하여 해당 Coin 상자에서 "*Coin 새로고침*"을 클릭합니다. 코인이 여러 개 있는 경우 기밀 유지를 위해 비교적 짧은 간격으로 하나씩 새로 고쳐야 합니다. 비용을 낮추기 위해 Wallet 전체를 새로운 수신 Address로 전송하여 자금을 통합할 수 있지만, 이는 기밀 유지에 영향을 미칩니다.


![Actualiser pièce](assets/fr/31.webp)


거래에 대해 원하는 수수료율을 표시합니다. 본인에게 이체하는 것이므로 특히 만료 며칠 전에 이체하는 경우 상당히 낮은 수수료율을 설정할 수 있습니다.


![Transfert à soi-même](assets/fr/32.webp)


거래("*자체 이체*"라고 표시된 거래)는 "*거래*" 탭에서만 볼 수 있습니다.


![Transactions après auto-transfert](assets/fr/33.webp)


확인이 완료되면 Coin은 안전합니다! 다음 만료일까지 안심하고 사용하실 수 있습니다.


## Bitcoin 복구


Liana Wallet에서 자금을 복구할 때 다음 두 가지 상황 중 하나에 직면할 수 있습니다. 소프트웨어가 설치된 컴퓨터에 액세스할 수 있는 경우, 이 경우 해당 컴퓨터를 열기만 하면 됩니다(향상된 백업 모델의 경우). 그러나 이 컴퓨터에 액세스할 수 없는 경우에는 처음부터 다시 시작하겠습니다. 복구 절차는 두 경우 모두 동일하다는 점에 유의하세요.


시작하려면 [위자딘 공식 웹사이트](https://wizardsardine.com/Liana/) 또는 소프트웨어의 진위 여부를 확인할 수 있는 [GitHub 저장소](https://github.com/wizardsardine/Liana/releases)에서 Liana을 다운로드하세요. 소프트웨어를 설치하고 실행합니다. 저희의 경우 0.9 버전을 사용했기 때문에 비주얼이 변경되었을 수 있습니다. 시작 화면에서 "기존 Liana Wallet 추가" 옵션을 선택합니다.


![Ajouter portefeuille existant](assets/fr/34.webp)


네트워크에 연결할 방법을 구성합니다. 자체 노드(로컬 또는 원격)를 사용하거나 위자드사딘의 인프라를 사용하도록 선택할 수 있습니다. 후자의 경우 자금을 자동으로 찾을 수 있도록 Wallet 생성자가 사용하는 이메일 Address이 필요합니다. 이 정보가 없는 경우 첫 번째 옵션을 선택하세요.


![Sélectionner connexion réseau](assets/fr/35.webp)


자체 노드를 사용하는 경우 Wallet Descriptor를 가져옵니다. 이것은 계정에 대한 기술적 설명으로, 계정에 보관된 자금을 검색할 수 있게 해줍니다. 저희의 경우에는 다음과 같은 정보입니다:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


![Importer descripteur](assets/fr/36.webp)


그러면 Liana에서 Mnemonic 구문을 입력하라는 메시지가 표시됩니다. 작동하는 서명 장치(Hardware Wallet)가 있는 경우 이 단계를 건너뛰세요. 장치가 없거나 손상되었지만 해당 12개 또는 24개 단어가 있는 경우에도 이 옵션을 사용할 수 있습니다. 안전을 위해(복구해야 할 금액이 많은 경우) 새 Hardware Wallet을 구한 후 Mnemonic를 사용하여 키를 복원하는 것이 좋습니다.


저희의 경우 블록스트림 제이드 Hardware Wallet를 복구 장치로 사용하며 이 단계를 건너뛰도록("*스킵*") 선택했습니다.


![Passer phrase mnémotechnique](assets/fr/37.webp)


화면에서 Descriptor을 선택하여 서명 장치에 저장합니다. Hardware Wallet가 표시되지 않으면 연결 및 잠금 해제되었는지 확인하세요. 이 정보가 장치에 추가되었는지 확인하고 확인합니다.


![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)


노드를 구성합니다. 기존 노드를 사용하거나 머신에 *pruned 노드*를 설치할 수 있습니다. 저희의 경우 기존 노드를 사용했습니다.


![Choisir type de nœud](assets/fr/39.webp)


이 튜토리얼에서는 공용 일렉트럼 서버를 사용했습니다. 하지만 이 서버는 Liana Wallet의 모든 활동에 액세스할 수 있었습니다. 개인 정보를 보호하려면 자체 노드를 사용하는 것이 좋습니다.


![Connexion serveur Electrum public](assets/fr/17.webp)


노드를 설정하면 Wallet 메인 화면으로 이동하여 계좌에 연결된 잔액과 과거 거래를 볼 수 있습니다. 자금을 검색할 수 있는지 여부도 확인할 수 있습니다. 여기에서는 Coin을 검색할 수 있음을 알 수 있습니다.


![Accueil Liana récupération](assets/fr/40.webp)


Wallet에서 자금을 복구하려면 왼쪽 하단의 설정("*설정*")으로 이동하여 "*복구*"를 클릭합니다.


![Récupération dans paramètres](assets/fr/41.webp)


해당 박스에 체크하여 Coin를 Wallet에 송금합니다. 송금할 BTC Address과 거래 수수료율을 표시하세요. 그런 다음 "*다음*"을 클릭합니다.


![Récupération des pièces](assets/fr/42.webp)


"*서명*"을 클릭하고 Hardware Wallet에서 거래의 유효성을 검사하여 거래에 서명합니다.


![Signer transaction clé de récupération](assets/fr/43.webp)


그런 다음 "*방송*"을 클릭하여 네트워크를 통해 브로드캐스트합니다.


![Diffuser transaction clé de récupération](assets/fr/44.webp)


거래가 메인 화면에 표시되어야 합니다. 확인되면 복구가 완료된 것입니다!


![Écran principal après récupération](assets/fr/45.webp)


## 보너스: Descriptor 분석


Descriptor은 사람이 읽을 수 있는 문자 문자열로 주소 집합을 상세히 설명합니다. 고급 Wallet의 부품(UTXO)을 검색하기 위한 여러 가지 필수 정보를 결합한 것입니다. Descriptor의 작성 방식은 2019년에 Andrew Poelstra, Pieter Wuille, Sanket Kanjalkar가 개발한 스크립팅 언어인 [Miniscript syntax](https://bitbox.swiss/blog/understanding-Bitcoin-miniscript-part-2/)를 기반으로 합니다.


이 문자 문자열이 중요한 이유를 더 잘 이해하기 위해 예제에서 Descriptor인 를 분석해 보겠습니다:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


이 Descriptor에서 다음 정보를 추출할 수 있습니다:




- wsh`(*감시 스크립트 Hash*의 줄임말): 이것은 생성된 트랜잭션 출력 유형입니다. Taproot를 사용하기로 선택했다면 식별자는 `tr`이 되었을 것입니다.
- or_d`: 이는 비용이 승인되려면 다음 두 가지 조건 중 하나가 충족되어야 함을 나타내는 논리 연산자입니다(`_d`는 특정 구문을 나타냅니다).
- pk`(*공개키*의 줄임말): 이 연산자는 주어진 서명을 다음 공개 키와 비교하여 확인하고 부울(true 또는 false)로 응답을 반환합니다.
- `[3689a8e7/48'/0'/0'/2']`: 이 요소에는 기본 Hardware Wallet(이 경우 나노 S 플러스)에 대한 마스터 키의 *지문*과 연결된 확장 개인 키의 파생 경로(다른 모든 개인 키가 파생되는 경로)가 포함됩니다.
- `xpub6FKY ... WQa`: 이것은 기본 Hardware Wallet(여기서는 Nano S Plus)에 연결된 확장 공개 키입니다
- `/<0;1>/*`: 이는 간단한 키와 주소를 얻기 위한 파생 경로입니다: 수신은 `0`, 내부 연산(*변경*)은 `1`이며, 기존 Wallet 소프트웨어의 "간격 제한" 관리와 유사하게 구성 가능한 방식으로 여러 주소를 순차적으로 파생할 수 있는 "와일드카드"(`*`)가 있습니다.
- and_v`: 이는 비용이 승인되려면 *다음 두 가지* 조건이 충족되어야 함을 나타내는 논리 연산자입니다(`_v`는 특정 구문을 나타냅니다).
- v:pkh`(*verify: 공개 키 Hash*의 줄임말): 이 연산자는 주어진 서명과 공개키를 뒤에 오는 공개키 Hash(*Hash*)과 비교하여 검증합니다. 이는 P2PKH 및 P2WPKH 스크립트와 본질적으로 동일한 확인입니다.
- `[42e629dd/48'/0'/0'/2']`: 이것은 위와 동일한 요소(추적 및 파생 경로로 구성)이지만 하드웨어 복구 Wallet의 마스터 키(이 경우 Jade)의 추적이 표시된다는 점을 제외하면 위와 동일합니다.
- `xpub6DpQ ... WQd`: 이것은 하드웨어 복구 Wallet(여기서는 Jade)에 연결된 확장 공개 키입니다.
- old(6)` : 이 연산자는 생성된 트랜잭션 출력이 6블록보다 엄격하게 큰 나이를 가져야 사용 가능한지 확인합니다.


마지막 데이터 항목(`8alrve5h`)은 Descriptor 체크섬이며, Wallet 식별자에 해당합니다.


이 Wallet에 의해 생성된 스크립트는 다음과 같은 형식을 취합니다:


```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```


Bitcoin Wallet의 보안은 작동 방식에 대한 이해에 달려 있으므로, Plan ₿ Network 에 대한 무료 교육 과정을 수강하여 결정론적 지갑과 계층적 지갑의 메커니즘에 대해 깊이 있게 공부해 보시기 바랍니다:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f