---
name: Specter Desktop
description: 자체 노드로 멀티서명 Bitcoin 포트폴리오를 전체 주권으로 관리하세요
---

![cover](assets/cover.webp)



스펙터 데스크톱은 2019년부터 크립토어드밴스에서 개발한 오픈 소스 애플리케이션(MIT 라이선스)으로, 하드웨어 지갑(Ledger, 트레저, 콜드카드, 비트박스02, 패스포트 등) 및 자체 Bitcoin 인프라(Bitcoin 코어 노드 또는 Electrum 서버)로 Bitcoin 지갑을 쉽게 관리할 수 있는 애플리케이션입니다. 이 애플리케이션은 특히 다중 서명 구성에 탁월하며, 여러 개의 독립적인 하드웨어 지갑에 서명 권한을 분산하여 거액을 보호할 수 있습니다.



**이 튜토리얼에서는 다음을 학습합니다




- 컴퓨터(Windows, macOS 또는 Linux)에 Specter Desktop을 설치하고 구성합니다
- 스펙터를 Electrum 서버에 연결합니다(이 예제에서는 엄브렐을 사용하겠습니다)
- wallet 하드웨어(콜드카드)로 간단한 wallet 만들기
- 완전한 주권으로 비트코인을 받고 보내세요
- 여러 개의 하드웨어 지갑으로 2대3 다중 서명 wallet 설정하기
- 엄브렐 서버에 스펙터 설치(고급 보너스)



모든 거래는 외부 서버로 정보를 전송하지 않고 자체 인프라를 통해 로컬에서 검증되므로 기밀성과 금융 주권이 보장됩니다. 서명하기 전에 항상 wallet 하드웨어 화면에서 거래를 확인하세요.



## 다운로드 및 설치



애플리케이션을 다운로드하려면 공식 스펙터 데스크톱 웹사이트를 방문하세요.



![Page d'accueil Specter](assets/fr/01.webp)



다운로드 페이지에서 운영 체제에 해당하는 버전(macOS, Windows 또는 Linux)을 선택합니다.



![Téléchargement selon l'OS](assets/fr/02.webp)



다운로드가 완료되면 운영 체제의 일반적인 지침에 따라 애플리케이션을 설치합니다. MacOS의 경우 아이콘을 애플리케이션으로 드래그합니다. Windows의 경우 설치 프로그램을 실행합니다. Linux의 경우 패키지 지침을 따릅니다.



## 초기 구성



처음 실행하면 Specter Desktop에서 연결 유형을 선택하라는 메시지가 표시됩니다. Electrum 서버 또는 자체 Bitcoin 코어 노드에 연결할 수 있습니다.



![Choix du type de connexion](assets/fr/03.webp)



이 예제에서는 Umbrel에서 실행되는 Electrum 서버에 연결합니다.



자세한 내용은 엄브렐 튜토리얼을 참조하세요:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

이 옵션은 Bitcoin 코어보다 빠른 동기화를 제공합니다. 원하는 경우 'Bitcoin 코어'를 선택하고 로컬 노드에 대한 연결을 구성할 수 있습니다. 다음 단계는 선택에 관계없이 동일하게 유지됩니다.



"Electrum 연결"을 선택한 다음 "나만의 서버 입력"을 선택하여 나만의 Electrum 서버를 구성합니다.



![Configuration Electrum](assets/fr/04.webp)



Electrum 서버의 주소를 입력합니다. Umbrel의 경우, 주소는 `umbrel.local`이며 포트는 `50001`입니다. "연결"을 클릭하여 연결을 설정합니다.



연결되면 시작을 위한 체크리스트와 함께 환영 화면이 나타납니다. 이제 하드웨어 지갑을 추가해야 합니다.



![Écran d'accueil](assets/fr/05.webp)



## wallet 하드웨어 추가



왼쪽 메뉴에서 '장치 추가'를 클릭하여 wallet 하드웨어를 추가합니다.



스펙터 데스크톱은 다양한 하드웨어 지갑을 지원합니다: 트레저, Ledger, 비트박스02, 콜드카드, 킵키, 키스톤, 코보 볼트 등이 있습니다.



자세한 내용은 하드웨어 wallet 튜토리얼을 참조하세요.



![Sélection du type de hardware wallet](assets/fr/06.webp)



wallet 하드웨어를 선택합니다. 이 예에서는 콜드카드 MK4를 사용하고 있습니다.



아래에서 이 wallet 하드웨어에 대한 튜토리얼을 확인할 수 있습니다:



https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

콜드카드의 경우, USB 연결 또는 microSD 카드를 통해 wallet 하드웨어에서 공개 키를 내보내야 합니다.



![Import des clés du Coldcard](assets/fr/07.webp)



표시되는 지침에 따라 콜드카드에서 키를 내보냅니다. wallet 하드웨어에 이름을 지정합니다(여기서는 "MK4 Tuto"). 키를 가져온 후에는 단일 키로 wallet을 만들거나 다른 하드웨어 지갑을 추가하여 다중 서명 wallet을 만들 수 있습니다.



![Dispositif ajouté](assets/fr/08.webp)



## 포트폴리오 생성



wallet 하드웨어를 추가한 후 "단일 키 wallet 만들기"를 클릭하여 단일 서명 wallet를 생성합니다.



포트폴리오에 이름을 지정하고(예: "Wallet for tuto") 주소 유형을 선택합니다. 거래 비용을 최적화하는 네이티브 bech32 주소를 사용하려면 "세그윗"을 선택합니다.



![Configuration du portefeuille](assets/fr/09.webp)



포트폴리오가 생성되면 Specter는 포트폴리오를 복원하는 데 필요한 모든 공개 정보(설명자, 확장 공개 키)가 포함된 백업 PDF 파일을 저장할 것을 제안합니다. 이 파일에는 개인 키가 포함되어 있지 않습니다.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## 비트코인 받기



비트코인을 받으려면 왼쪽 메뉴에서 wallet를 선택한 다음 '받기' 탭을 클릭합니다.



스펙터는 QR 코드가 포함된 새 수신 주소를 자동으로 생성합니다.



![Génération d'une adresse de réception](assets/fr/11.webp)



주소를 복사하거나 QR 코드를 스캔할 수 있습니다. 다른 사람에게 주소를 전달하기 전에 항상 wallet 하드웨어 화면에서 주소를 확인하세요.



## 기록 및 주소 보기



비트코인을 받으면 '거래' 탭에서 거래를 확인할 수 있습니다.



![Historique des transactions](assets/fr/12.webp)



'주소' 탭에서는 포트폴리오에서 생성된 모든 주소를 사용 현황 및 관련 금액과 함께 볼 수 있습니다.



![Liste des adresses](assets/fr/13.webp)



## 비트코인 보내기



비트코인을 보내려면 '보내기' 탭을 클릭합니다. 받는 사람의 주소와 송금할 금액을 입력하고 UTXO(코인 컨트롤)를 수동으로 선택하려면 고급 옵션에 체크합니다.



![Création d'une transaction](assets/fr/14.webp)



"서명되지 않은 트랜잭션 생성"을 클릭하여 트랜잭션을 생성합니다. 그러면 스펙터가 wallet 하드웨어로 트랜잭션에 서명할 것을 요청할 것입니다.



![Signature de la transaction](assets/fr/15.webp)



콜드카드를 사용하는 경우 USB를 통해 서명하거나 마이크로SD 카드(에어 갭)를 사용하여 서명할 수 있습니다. wallet 하드웨어 화면에서 거래를 확인하며 도착지 주소와 금액을 꼼꼼히 확인합니다.



트랜잭션이 서명되면 Bitcoin 네트워크에서 브로드캐스트할 수 있습니다.



![Options de diffusion](assets/fr/16.webp)



트랜잭션을 보내려면 "트랜잭션 보내기"를 클릭합니다. 스펙터에서 트랜잭션이 전송되었는지 확인하며, 트랜잭션 탭에서 트랜잭션 상태를 추적할 수 있습니다.



![Diffusion de la transaction](assets/fr/17.webp)



## 다중 서명 포트폴리오 만들기 및 사용



스펙터 데스크톱의 주요 자산 중 하나는 다중 서명 포트폴리오 관리를 간소화하는 기능입니다. 다중 서명 wallet는 거래를 승인하기 위해 여러 서명이 필요하므로 단일 실패 지점을 제거합니다. 예를 들어 2대 3 구성에서는 지출을 검증하기 위해 세 개의 개별 하드웨어 지갑에서 두 개의 서명이 필요합니다.



다중서명 wallet을 만들려면 '장치 추가'를 통해 모든 서명 하드웨어 지갑을 추가하는 것부터 시작합니다. 이 예에서는 Coldcard MK4(이미 앞서 추가한), Passport, Ledger의 세 가지 하드웨어 지갑을 사용하겠습니다. 이렇게 제조업체를 다양화하면 단일 공급망이나 펌웨어에 대한 의존을 피할 수 있어 보안이 강화됩니다.



다음은 Ledger 및 Passport 튜토리얼에 대한 링크입니다:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

wallet 하드웨어에 이름을 지정하고(예: "Passport multi") microSD 카드 또는 QR 코드를 통해 키를 가져와서 Passport를 추가합니다. 그런 다음 '계속'을 클릭하여 계속합니다.



![Ajout du Passport](assets/fr/23.webp)



그런 다음 USB를 통해 Ledger를 연결하고 Bitcoin 하드웨어에서 wallet 애플리케이션을 열어 Ledger를 추가합니다. 이름을 지정하고(예: "ledger multi") "USB를 통해 가져오기"를 클릭한 다음 "계속"을 클릭하여 공개 키를 가져옵니다.



![Ajout du Ledger](assets/fr/24.webp)



스펙터에 3개의 하드웨어 지갑을 등록한 후 "wallet 추가"를 클릭하고 "다중 서명" 옵션을 선택해 다중 서명 wallet을 생성합니다.



![Choix du type de wallet](assets/fr/25.webp)



다중 서명 쿼럼에 포함할 하드웨어 지갑 3개를 선택합니다: MK4 Tuto, 패스포트 멀티, 레저 멀티입니다. 다음 단계로 진행하려면 '계속'을 클릭합니다.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



다중 서명 구성을 선택합니다. 최적화된 수수료 혜택을 받으려면 주소 유형으로 "세그윗"을 선택합니다. "거래 승인에 필요한 서명 수(m of 3)" 매개변수를 통해 임계값을 정의할 수 있습니다. 2대 3 구성의 경우 2개의 서명이 필요합니다. 각 wallet 하드웨어는 해당 멀티서명 키를 표시합니다. "wallet 만들기"를 클릭하여 생성을 완료합니다.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



이제 "멀티 투토" 다중 서명 포트폴리오가 생성되었습니다. 스펙터는 즉시 포트폴리오 설명자가 포함된 백업 PDF 파일을 저장할 것을 권장합니다. "백업 PDF 저장"을 클릭하여 이 중요한 파일을 다운로드하세요.



![Wallet multisig créé](assets/fr/28.webp)



또한 스펙터를 사용하면 QR코드나 파일을 통해 각 하드웨어 지갑으로 wallet 정보를 내보낼 수 있습니다. 이를 통해 특정 하드웨어 지갑(예: 콜드카드 또는 패스포트)은 멀티서명 구성을 메모리에 직접 저장할 수 있습니다.



Passport의 경우 장치의 잠금을 해제하고 '계정 관리' > 'Wallet 연결' > '스펙터' > 'Multisig' > 'QR 코드'로 이동한 다음 스펙터에서 생성된 QR 코드를 스캔합니다. 그러면 Passport에서 멀티시그 구성의 유효성을 검사하기 위해 wallet의 수신 주소를 스캔하라는 메시지가 표시됩니다.



MK4의 경우, PC에 연결하고 잠금을 해제합니다. 그런 다음 'MK4 Tuto 파일 저장'을 클릭하고 파일을 MK4에 저장합니다. 다음에 wallet 하드웨어에 서명할 때 MK4는 이 파일을 사용하여 멀티서명 구성을 완료합니다.



![Export vers les hardware wallets](assets/fr/29.webp)



참고로 포트폴리오의 '설정' 탭에서 언제든지 백업에 액세스한 다음 '내보내기'를 클릭하면 백업에 액세스할 수 있습니다:



![Accès au backup PDF](assets/fr/30.webp)



일상적인 사용은 평소와 같이 wallet 수신 주소와 비슷하게 유지됩니다. 비트코인을 보내려면 '보내기' 탭으로 이동하여 수취인 주소와 금액을 입력한 다음 '서명되지 않은 거래 만들기'를 클릭합니다.



![Création d'une transaction multisig](assets/fr/31.webp)



스펙터가 PSBT(Partially Signed Bitcoin Transaction)을 빌드하고 "서명 2개 중 0개를 획득했습니다"라고 표시합니다. 이제 3개의 하드웨어 지갑 중 최소 2개 이상의 지갑으로 서명해야 합니다. 첫 번째 wallet 하드웨어(예: "MK4 Tuto")를 클릭하여 콜드카드로 서명한 다음, 두 번째 하드웨어(예: "Passport multi")를 클릭하여 필요한 두 번째 서명을 받습니다.



![Signature de la transaction](assets/fr/32.webp)



필요한 2개의 서명을 받으면(인터페이스에 "획득한 2개의 서명 중 2개" 및 "트랜잭션을 보낼 준비가 되었습니다"라고 표시됨), "트랜잭션 보내기"를 클릭하여 Bitcoin 네트워크에 트랜잭션을 브로드캐스트합니다.



![Transaction prête à être diffusée](assets/fr/33.webp)



이 다중 서명 방식은 특히 회사(여러 관리자가 지출을 승인해야 하는 경우), 가족(다세대 상속 재산 보호) 또는 거액을 관리하는 개인(국지적 재난에 대비한 하드웨어 지갑의 지리적 분산)에 적합합니다.



### 다중 서명 백업의 중요성



**참고**: 다중 서명 포트폴리오를 백업하는 것은 단일 포트폴리오를 백업하는 것과 근본적으로 다릅니다. 복구 구문(seed 구문)만으로는 멀티서명 포트폴리오를 복원하는 데 충분하지 않습니다. 멀티서명 포트폴리오의 구성 정보가 포함된 **output descriptor**(output descriptor)도 백업해야 합니다.



output descriptor에는 각 공동 서명자의 확장 공개 키(xpub), 서명 임계값(예시에서는 2 대 3), 사용된 스크립트 유형(기본, 중첩 또는 레거시 세그윗), 각 wallet 하드웨어의 바이패스 경로 등 필수 데이터가 포함되어 있습니다. 이 설명자가 없으면 복구 구문 3개 중 2개가 있더라도 wallet를 다시 빌드하거나 비트코인에 액세스할 수 없습니다. 설명자는 소프트웨어가 공개 키를 generate과 자금에 해당하는 Bitcoin 주소에 결합하는 방법을 알려줍니다.



스펙터 데스크톱은 다중 서명 포트폴리오를 만들 때 백업 PDF 파일을 자동으로 생성합니다. 이 PDF에는 전체 설명자, 각 wallet 하드웨어의 지문, 복원에 필요한 모든 공개 정보가 포함되어 있습니다. **이 파일에는 개인 키가 포함되어 있지 않으므로** 그 자체로는 비트코인을 사용할 수 없지만, 이 파일에 액세스하는 모든 사람이 전체 거래 내역과 잔액을 볼 수 있습니다.



다중 서명 구성을 올바르게 백업하려면 다음 절차를 따르세요. 포트폴리오를 만든 후 '설정' 탭을 클릭한 다음 '내보내기'를 클릭하고 '백업 PDF 저장'을 선택하세요. 이 PDF의 사본을 여러 개 만드세요: 종이에 두 부 이상 인쇄하고 암호화된 디지털 사본도 보관하세요. 각 복구 문구와 함께 PDF 사본을 지리적으로 분리된 위치에 하나씩 보관하세요.



내화 및 방수 금속판에 복구 문구를 새겨서 오래도록 보관하세요. 컴퓨터에서 `~/.specter` 폴더를 잃어버리고 설명자 백업이 없는 하드웨어 지갑 중 하나를 잃어버리면 2대3 구성으로도 모든 자금을 복구할 수 없게 됩니다. 다중 서명 이중화는 wallet 하드웨어의 손실로부터 보호하지만, 이는 wallet의 설명자를 올바르게 백업한 경우에만 해당됩니다.



## 스펙터 데스크톱의 장점과 한계



**혜택**: 타사 서버 없이 완벽한 로컬 유효성 검사를 통한 최적의 기밀성. 고급 구성(기업, 가족, 개인)을 위한 다중 서명 유연성. 완벽한 상호 운용성을 갖춘 광범위한 하드웨어 wallet 지원(USB 및 에어 갭).



**제한 사항**: 고급 Bitcoin 개념(UTXO, 설명자, 파생 경로)에 대한 상당한 학습 곡선.



## 모범 사례



유효성 검사 전에 항상 하드웨어 wallet 화면에서 주소와 금액을 확인하여 멀웨어로부터 자신을 보호하세요.



PDF 백업을 시드와 별도로 보관하세요. 이러한 공개 설명자는 은행 금고 또는 암호화된 클라우드에 저장할 수 있으므로 개인 키를 노출하지 않고도 쉽게 복구할 수 있습니다.



대규모 자금으로 포트폴리오를 사용하기 전에 token 금액에 대한 복구를 테스트하세요. 절차를 검증하기 위해 생성, 테스트, 삭제 및 복원하세요.



스펙터와 펌웨어를 최신 상태로 유지하세요. 다중 서명 공동 서명자를 지리적으로 분산(집/사무실/근처)하여 지역화된 재난을 견딜 수 있도록 하세요. 설명이 포함된 라벨을 사용해 회계 및 세금 신고를 용이하게 하세요.



## 보너스: Bitcoin 서버에 설치(Umbrel, RaspiBlitz, Start9)



Umbrel, RaspiBlitz, MyNode 또는 Start9와 같은 Bitcoin 서버를 이미 소유하고 있는 경우 해당 애플리케이션 스토어에서 직접 Specter Desktop을 설치할 수 있습니다. 이 방법은 몇 가지 중요한 이점을 제공합니다. 애플리케이션이 로컬 Bitcoin 코어 노드와 함께 자동으로 구성되고, 네트워크의 모든 기기에서 웹 인터페이스를 통해 연중무휴 24시간 액세스할 수 있으며, 심지어 Tor를 통해 원격으로 안전하게 액세스할 수 있습니다. 전체 Bitcoin 인프라가 단일 전용 서버에 중앙 집중화되어 있어 관리가 간소화되고 사용자의 주권이 강화됩니다.



### 엄브렐 앱 스토어에서 설치



엄브렐 인터페이스에서 앱 스토어로 이동하여 스펙터 데스크톱을 검색합니다. '설치'를 클릭하여 설치를 시작합니다.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



설치가 완료되면 엄브렐에서 스펙터 데스크톱을 엽니다. 시작 화면에서 연결 유형을 선택하라는 메시지가 표시됩니다. 엄브렐에서 스펙터를 사용하는 경우 '설정 업데이트'를 클릭하여 연결을 구성합니다.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



원격 엄브렐 서버에서 스펙터를 사용하면서 로컬 컴퓨터에 연결된 USB 하드웨어 지갑을 사용하려면 "원격 스펙터 USB 연결"을 선택합니다.



![Configuration Remote Specter USB](assets/fr/20.webp)



표시되는 지침에 따라 HWI 브리지를 구성합니다. 장치 브리지 설정에 액세스하여 `http://umbrel.local:25441` 도메인을 화이트리스트에 추가해야 합니다. "업데이트"를 클릭하여 구성을 저장합니다.



![HWI Bridge Settings](assets/fr/21.webp)



로컬 컴퓨터에서도 USB 하드웨어 지갑을 사용하려면 컴퓨터에 Specter 데스크톱 애플리케이션을 다운로드하고 "예, 원격으로 Specter를 실행합니다"로 설정합니다. '저장'을 클릭하여 구성을 완료합니다.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## 결론



스펙터 데스크톱은 고급 Bitcoin 구성을 대중화하여 사용자의 주권이나 기밀성을 희생하지 않고도 다중 서명에 액세스할 수 있도록 합니다. 상당한 금액을 관리하는 사용자의 경우, 기관의 관행을 개인이 배포할 수 있는 솔루션으로 전환할 수 있습니다.



이 애플리케이션은 인프라와 학습에 초기 투자가 필요하지만, 검증 인프라 제어, 키의 물리적 소유권, 제3자 감시로부터 자유로운 거래 등 완전한 주권을 제공합니다. 개인이 저축을 보호하든, 다세대 안전금고를 만드는 가족이든, 현금 흐름을 관리하는 기업이든, Specter Desktop은 최고의 보안과 절대적인 주권을 조화시키는 기준이 되는 도구입니다.



## 리소스



### 공식 문서




- [스펙터 데스크톱 공식 웹사이트](https://specter.solutions/desktop/)
- [깃허브 소스 코드](https://github.com/cryptoadvance/specter-desktop)
- [전체 문서](https://docs.specter.solutions/)



### 커뮤니티 및 지원




- [텔레그램 스펙터 커뮤니티 그룹](https://t.me/spectersupport)
- [레딧 토론 포럼](https://reddit.com/r/specterdesktop/)
- [깃허브 버그 리포트](https://github.com/cryptoadvance/specter-desktop/issues)