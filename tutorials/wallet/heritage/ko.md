---
name: 유산
description: Taproot 스크립트를 통한 통합 상속 메커니즘을 갖춘 Bitcoin 포트폴리오
---

![cover](assets/cover.webp)



사망 또는 무능력한 상황에서 비트코인을 물려주는 것은 모든 암호화폐 자산 보유자에게 큰 도전 과제입니다. 적절한 상속 계획이 없다면 이러한 자산은 사랑하는 사람에게 복구할 수 없게 됩니다.



헤리티지는 Bitcoin 블록체인에 직접 데드맨 스위치 메커니즘을 구현하여 우아한 해답을 제시합니다. 이 오픈 소스 wallet를 사용하면 on-chain 승계 조건을 설정할 수 있습니다. 소유자가 정해진 기간 동안 추가 거래를 하지 않으면 미리 지정된 대체 키가 자금을 해제할 수 있습니다.



## 헤리티지란 무엇인가요?



Heritage는 Taproot 스크립트를 통해 상속 메커니즘을 기본적으로 통합한 Bitcoin 포트폴리오입니다. 제레미 로돈이 MIT 라이선스에 따라 개발한 이 오픈 소스 소프트웨어는 투명성과 내구성을 보장합니다.



Heritage는 Bitcoin 주소로 인코딩된 Taproot 스크립트를 사용합니다. 각 UTXO에는 두 가지 유형의 지출 조건이 통합되어 있습니다:





- 기본 경로** : 소유자는 기본 키로 언제든지 비트코인을 사용할 수 있습니다
- 대체 경로**: 지정된 각 상속인에 대해 스크립트는 공개 키와 타임록을 결합합니다



각 소유자 거래는 상속 조항의 활성화 날짜를 자동으로 연기합니다. 장기간 활동하지 않는 경우(사망, 무능력) 조건이 자동으로 트리거됩니다.



## 헤리티지 서비스(선택 사항)



Heritage는 두 가지 사용 옵션을 제공합니다:



**직접 해보세요(무료)**: 오픈소스 애플리케이션만으로도 가능합니다. 자신의 노드로 모든 것을 자율적으로 관리합니다. 이 옵션은 내장된 백업 액세스, 내장된 상속 및 비트코인에 대한 독점적 제어 기능을 제공합니다. 하지만 타임록 갱신을 잊지 않도록 직접 알림(캘린더, 리마인더)을 만들어야 하며, 상속인에게 자동으로 알림이 전송되지 않습니다.



**서비스 사용(연간 0.05%)** : Btc-heritage.com 서비스는 관리를 간소화하는 기능을 추가합니다:




- 마감일 만료 전 자동 알림
- 상속인에게 자동 알림을 보내 복구 프로세스를 안내합니다
- 우선 지원
- 간소화된 설명자 관리



수수료: 연간 관리 금액의 0.05%, 최소 0.5mBTC/년. 첫해 무료.



이 서비스는 비수탁형 서비스로, 개인 키가 기기를 떠나지 않습니다. 헤리티지는 회원님의 자금에 액세스할 수 없습니다.



## Heritage CLI



터미널을 선호하는 고급 사용자를 위해 Heritage는 세분화된 제어 및 에어 갭 머신 작동을 위한 명령줄 도구(CLI)를 제공합니다.



![Page Heritage CLI](assets/fr/03.webp)



전체 CLI 문서는 [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli)에서 확인할 수 있습니다. 여기에서 다운로드, 서비스 연결, 지갑 생성(Ledger 또는 로컬 키 사용), 상속인 및 거래 관리에 대한 지침을 확인할 수 있습니다.



이 튜토리얼에서는 대부분의 사용자가 더 쉽게 접근할 수 있는 데스크톱 애플리케이션에 중점을 둡니다.



## 헤리티지 데스크톱



Heritage 데스크톱은 직관적인 인터페이스를 갖춘 그래픽 애플리케이션으로, 구성 프로세스의 모든 단계를 사용자에게 안내합니다.



### 다운로드



Btc-heritage.com](https://btc-heritage.com)으로 이동하여 "애플리케이션 다운로드"를 클릭합니다.



![Page d'accueil Heritage](assets/fr/01.webp)



사용 중인 운영 체제에 해당하는 버전을 선택합니다(Linux 64비트 또는 Windows 64비트). 바이너리는 디지털 서명이 되어 있지 않으므로 보안 경고가 표시될 수 있습니다.



![Page de téléchargement](assets/fr/02.webp)



### Linux에 설치



Linux에서는 애플리케이션이 AppImage 형식으로 배포됩니다. 실행하려면 먼저 `libfuse2` 종속성을 설치해야 합니다:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



그런 다음 파일을 실행 파일로 만들어 실행합니다:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### 첫 출시



처음 시작할 때 온보딩 마법사는 세 가지 선택 사항을 제공합니다:



![Onboarding initial](assets/fr/05.webp)





- 유산 Wallet**를 설정합니다: 헤리티지 계획으로 새 wallet 만들기
- 비트코인 상속**: 상속인으로서 비트코인 복구
- 혼자 탐색**: 도움 없이 탐색 기능 탐색



"헤리티지 Wallet 설정"을 선택하여 첫 번째 wallet을 생성합니다.



### Bitcoin 네트워크 연결



Bitcoin 네트워크에 연결하는 방법을 선택합니다:



![Choix connexion](assets/fr/06.webp)





- 유산 서비스 사용**: 상속인을 위한 더 간편한 관리형 인프라
- 내 노드 사용**: 자체 Bitcoin 코어 또는 Electrum 노드에 연결합니다



이 튜토리얼에서는 자체 노드를 사용합니다.



### 개인 키 관리



개인 키 관리 방법을 선택합니다:



![Gestion des clés](assets/fr/07.webp)





- Ledger 하드웨어 장치** 사용** : wallet 하드웨어 사용 시 안전성 극대화(권장)
- 비밀번호가 있는 로컬 저장소**: 암호로 보호되는 로컬 저장소 키
- 기존 wallet 복원** : 기존 seed에서 복원



### 노드 구성



자체 노드를 사용하는 경우 애플리케이션에서 노드 구성을 안내합니다. Bitcoin 또는 Electrum 노드가 :




- 설치 및 실행 중
- Bitcoin 네트워크와 동기화
- RPC 연결을 허용하도록 구성(Bitcoin 코어용)



![Configuration nœud](assets/fr/08.webp)



노드가 준비되면 "내 Bitcoin 노드가 실행 중입니다."를 클릭합니다.



### 상태 패널



오른쪽 상단의 '상태'를 클릭한 다음 '구성 열기'를 클릭하여 연결 매개변수에 액세스합니다.



![Panneau Status](assets/fr/09.webp)



Electrum 서버의 URL을 설정합니다(예: Umbrel을 사용하는 경우 `umbrel.local:50001`).



![Configuration Electrum](assets/fr/10.webp)



### wallet 생성



연결이 완료되면 지갑 탭에서 "Wallet 만들기"를 클릭합니다.



![Créer wallet](assets/fr/11.webp)



헤리티지의 분할 아키텍처를 설명하는 팝업이 표시됩니다:



![Architecture split](assets/fr/12.webp)



1. **키 공급자(오프라인)**: 개인 키를 관리하고 트랜잭션에 서명합니다. Ledger 또는 wallet 소프트웨어일 수 있습니다.


2. **온라인 Wallet**: Bitcoin 네트워크와의 동기화, 주소 생성 및 트랜잭션 브로드캐스팅을 처리합니다.



생성 양식을 작성합니다 :



![Formulaire création wallet](assets/fr/13.webp)





- Wallet 이름**: wallet을 식별할 수 있는 고유 이름
- 키 공급자**: 이 튜토리얼에서는 로컬 키 저장소를 선택합니다
- 신규/복원**: "신규"를 선택하여 generate에 새 seed을 생성합니다
- 단어 수**: 최대 보안을 위해 24단어 권장



강력한 비밀번호를 입력하고 온라인 Wallet 옵션을 선택합니다:



![Options Online Wallet](assets/fr/14.webp)





- 로컬 노드**: 자체 Electrum 또는 Bitcoin 코어 노드 사용
- 헤리티지 서비스**: 헤리티지 서비스 사용(알림 기능에 권장)



"Wallet 만들기"를 클릭하여 생성을 완료합니다.



### Interface에서 wallet



이제 wallet이 생성되었습니다. 인터페이스에 :



![Interface wallet](assets/fr/15.webp)





- 잔액
- 보내기 및 받기 버튼
- 거래 내역
- 헤리티지 구성 기록
- wallet 주소



### 상속인 만들기



상속인을 만들려면 '상속인' 탭으로 이동합니다.



![Page Heirs](assets/fr/16.webp)



정보 팝업에 설명이 표시됩니다:




- 상속인은 개인과 연결된 Bitcoin 공개 키입니다
- 모든 상속인에게는 고유한 니모닉 문구가 있습니다
- 첫 번째 상속인은 자신을 위한 '백업'이어야 합니다(메인 wallet 분실 시)



#### 백업 상속인 생성



'상속인 만들기'를 클릭하고 이름을 '백업'으로 지정합니다.



![Création héritier Backup](assets/fr/17.webp)



이 팝업은 passphrase가 없는 12단어 문장이 상속인에게 안전한 이유를 설명합니다:


1. **즉시 액세스 불가**: 상속인 키는 타임락이 만료될 때까지 자금에 액세스할 수 없습니다


2. **침해 탐지**: 누군가 이 문구에 액세스하면 헤리티지 구성을 업데이트할 수 있습니다


3. **장기적인 접근성**: passphrase는 수년이 지나면 잊혀질 수 있습니다



상속인 구성하기 :



![Configuration héritier](assets/fr/18.webp)





- 키 공급자** : 로컬 키 저장소
- 신규**: 새로운 seed 생성
- 단어 수**: 12 단어



생성을 완료합니다 :



![Finalisation héritier](assets/fr/19.webp)





- 상속인 유형**: 확장 공개 키
- 서비스로 내보내기**: 선택 사항, 상속인에게 자동 알림을 활성화합니다



이제 백업 상속인이 생성되었습니다:



![Héritier créé](assets/fr/20.webp)



#### 상속인의 니모닉 문구 저장하기



백업 상속인을 클릭한 다음 "Mnemonic 표시" 를 클릭합니다:



![Afficher mnemonic](assets/fr/21.webp)



**중요: 이 12개의 단어를 메모하여 안전한 곳에 보관하세요. 이것이 자금 회수의 열쇠입니다.



![Phrase mnémotechnique](assets/fr/22.webp)



#### 애플리케이션에서 seed 제거하기



문구를 적고 나면 상속인 매개변수(톱니바퀴 아이콘)에 액세스합니다:



![Paramètres héritier](assets/fr/23.webp)



'상속인 시드 제거'를 사용하여 애플리케이션에서 개인 키를 제거합니다. 문구를 저장했는지 확인합니다.



![Strip Heir Seed](assets/fr/24.webp)



이는 보안을 위한 조치로, 애플리케이션에는 상속을 구성하기에 충분한 공개 키만 남아 있습니다.



#### 두 번째 상속인 생성



이 과정을 반복하여 두 번째 상속인(예: "Satoshi")을 만듭니다. 이제 두 명의 상속인이 생깁니다:



![Deux héritiers](assets/fr/25.webp)





- 백업**: 개인 비상 키
- Satoshi**: 지정된 상속인



### 헤리티지 구성



wallet로 돌아가서 설정 아이콘을 클릭합니다:



![Paramètres wallet](assets/fr/26.webp)



"유산 구성" 섹션에서 "만들기"를 클릭합니다:



![Heritage Configuration](assets/fr/27.webp)



각 상속인에 대해 시간 제한을 설정합니다:



![Configuration délais](assets/fr/28.webp)





- 백업**: 180일(6개월) - 만기일: 2026-06-18
- Satoshi**: 455일(15개월) - 만기일: 2027-03-20



**중요**: 각 상속인은 이전 상속인보다 더 긴 지연 시간을 가져야 합니다. 첫 번째 상속인(백업)이 먼저 자금에 액세스할 수 있습니다.



또한 구성 :



![Configuration finale](assets/fr/29.webp)





- 참조 날짜**: 리드 타임 계산 시작일
- 최소 만기 지연**: 거래 후 최소 지연(10일 권장)



'만들기'를 클릭하여 구성을 확인합니다.



이제 헤리티지 구성이 활성화되었습니다:



![Configuration active](assets/fr/30.webp)



두 상속인 모두의 기한과 만료일이 표시됩니다.



### 설명자 저장



**중요**: wallet 설명자를 저장하세요. 설명어가 없으면 니모닉 문구가 있어도 자금 회수가 불가능합니다.



클릭 "백업 설명자" :



![Bouton Backup](assets/fr/31.webp)



Bitcoin 디스크립터가 포함된 JSON 파일을 저장합니다:



![Backup descripteurs](assets/fr/32.webp)



이 파일은 각각의 니모닉 문구와 함께 상속인에게 전달되어야 합니다.



### 비트코인 받기



"수신"을 클릭하여 generate에 수신 주소를 입력합니다:



![Recevoir bitcoins](assets/fr/33.webp)



축하합니다! 헤리티지 Wallet에서 비트코인을 받을 준비가 되었습니다. 생성된 각 주소에는 자동으로 헤리티지 조건이 적용됩니다.



거래를 받으면 잔액이 업데이트됩니다:



![Solde mis à jour](assets/fr/34.webp)



기록에는 트랜잭션 및 관련 유산 구성이 표시됩니다.



---

## 상속인에 의한 복구



설정된 시간이 경과하면 상속인은 자금을 회수할 수 있습니다.



### 전제 조건



상속인에게 필요한 것은 :


1. 그의 12단어 니모닉 문구


2. 원본 wallet 설명자 백업 파일(JSON)



### 상속인 만들기 Wallet



'상속' 탭에서 이러한 전제 조건을 알려주는 팝업이 표시됩니다:



![Page Heir Wallets](assets/fr/35.webp)



**참고**: 설명자 백업 파일이 없으면 올바른 니모닉 문구가 있어도 자금에 액세스할 수 없습니다.



클릭 "상속인 만들기 Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



양식을 작성해 주세요:



![Formulaire Heir Wallet](assets/fr/37.webp)





- 상속인 Wallet 이름**: 이 상속인을 식별하기 위한 이름 wallet
- 키 공급자** : 로컬 키 저장소
- 복원**: 기존 문구를 입력하려면 이 옵션을 선택합니다



상속인의 니모닉 문구 12단어를 입력하고 유산 제공자를 구성합니다:



![Entrée mnemonic](assets/fr/38.webp)





- 헤리티지 공급자**: 백업 파일과 함께 자체 노드를 사용하려면 "로컬"을 선택합니다



JSON 백업 파일을 로드하고 "상속인 생성 Wallet" 를 클릭합니다:



![Chargement backup](assets/fr/39.webp)



### Interface 계승자 Wallet



상속인 Wallet가 생성됩니다. 처음에는 타임록이 아직 만료되지 않은 경우 상속을 사용할 수 없습니다:



![Pas d'héritage disponible](assets/fr/40.webp)



지연 시간이 경과하고 자금이 Bitcoin 네트워크와 동기화되면 상속 목록에 표시됩니다:



![Héritage disponible](assets/fr/41.webp)



인터페이스에 :




- 키 유형 및 지문
- 상속 가능한 총 자금
- 현재 사용 가능한 금액(타임락이 아직 만료되지 않은 경우 0시트)
- 만기 및 만료일



만기일에 도달하면 '지출' 버튼을 누르면 비트코인이 개인 wallet로 이체됩니다.



---

## 모범 사례



### 설명자 저장



wallet 설명자는 유산 주소를 재구성하는 데 필수적입니다. **설명자가 없으면 니모닉 문구가 있어도 자금을 찾을 수 없습니다.



### 키 보안





- 가능하면 메인 키로 Ledger를 사용하세요
- 상속인의 문장을 자신의 문장과 같은 위치에 저장하지 마세요
- 여러 미디어와 위치로 정보 확산



### 사랑하는 사람을 위한 문서



복구 프로세스의 각 단계를 설명하는 명확한 지침을 작성하세요. 상속인이 중요한 순간에 Bitcoin에 익숙하지 않을 수 있습니다.



## 대안



비트코인 전송을 관리할 수 있는 다른 솔루션으로는 Liana와 Bitcoin Keeper이 있습니다. 아래 튜토리얼을 참조하세요:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## 결론



Heritage를 사용하면 데스크톱 애플리케이션을 통해 주권적인 방식으로 Bitcoin 승계를 계획할 수 있습니다. 이를 실행하려면 적절한 기간을 신중하게 고려하고 비밀을 보호해야 합니다. 상속인에게 물려주는 것을 잊지 마세요:




- 12단어 니모닉 문구
- 설명자 백업 파일
- 복구 지침



## 리소스





- [헤리티지 공식 웹사이트](https://btc-heritage.com)
- [문서 CLI](https://btc-heritage.com/heritage-cli)
- [깃허브 헤리티지 CLI](https://github.com/crypto7world/heritage-cli)
- [깃허브 헤리티지 데스크톱](https://github.com/crypto7world/heritage-gui)