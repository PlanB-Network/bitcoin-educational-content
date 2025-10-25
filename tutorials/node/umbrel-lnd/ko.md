---
name: Umbrel LND
description: 엄브렐에 Lightning Network Daemon(LND) 설치 및 구성에 대한 고급 튜토리얼
---
![cover](assets/cover.webp)




## 소개



이 고급 튜토리얼에서는 엄브렐 노드에서 라이트닝 노드(LND) 애플리케이션을 설치, 구성 및 사용하는 방법을 단계별로 안내합니다. 채널을 열고, 유동성을 관리하고, 노드를 모바일 애플리케이션과 동기화하는 방법을 배우게 됩니다.



## 1. 전제 조건: 기능적 Bitcoin 엄브렐 노드



Lightning을 배포하기 전에 Umbrel에서 완전히 작동하는 Bitcoin 노드가 있어야 합니다. 이를 위해서는 Umbrel(Raspberry Pi, NAS 또는 기타 머신에)을 설치하고 Blockchain Bitcoin을 완전히 동기화해야 합니다.



Umbrel을 설치하고 Bitcoin 노드를 구성하려면 전용 튜토리얼을 따르는 것이 좋습니다:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Lightning Network은 모든 off-chain 트랜잭션에 의존하므로 Bitcoin 노드가 최신 상태이고 제대로 작동하는지 확인하세요.



## 2. Lightning Network 소개



Lightning Network는 메인 Blockchain 외부에서 수행하여 Bitcoin 트랜잭션의 속도를 높이고 비용을 절감하도록 설계된 보조 Layer 프로토콜입니다.



구체적으로 설명하자면, 라이트닝은 노드 간 결제 채널 네트워크를 사용합니다. 두 명의 사용자가 On-Chain BTC(초기 거래)를 차단하여 채널을 개설한 다음 이 채널 내에서 즉시 Exchange 결제를 진행할 수 있습니다. 이러한 off-chain 트랜잭션은 Blockchain에 기록되지 않으므로 속도가 빠르며 사실상 비용이 거의 들지 않습니다.



결제는 중개 노드 덕분에 여러 채널을 통해 네트워크의 모든 수신자에게 전달될 수 있으므로 거의 무제한에 가까운 규모의 인스턴트 거래가 가능합니다. 따라서 Lightning은 일상적인 결제나 소액 거래에 이상적인 매우 빠르고 저렴한 트랜잭션을 제공하는 동시에 Blockchain Bitcoin의 부하를 줄여줍니다.



라이트닝 노드가 작동하려면 네트워크에 영구적으로 연결되어 있어야 하며 다른 라이트닝 노드와 상호 작용해야 합니다. 다양한 소프트웨어 구현(LND, Core Lightning, Eclair 등)이 존재하며, 모두 서로 호환됩니다. 엄브렐은 공식 라이트닝 노드 애플리케이션의 일부로 LND(Lightning Network Daemon)을 사용합니다. 이 튜토리얼에서는 LND에 중점을 둡니다.



Lightning Network에 대한 완전한 이론적 소개는 전용 강좌 를 수강하는 것이 좋습니다:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

이 과정에서는 Lightning Network의 기본 개념을 철저히 학습한 후 LND 노드로 실습을 진행합니다.



## 3. LND을 셀프 호스팅하는 이유는 무엇인가요?



엄브렐에서 자체 라이트닝 노드(LND)를 운영하면 커스터디 또는 반커스터디 솔루션에 비해 자금과 채널에 대한 완전한 주권을 가질 수 있습니다.



### 라이트닝 솔루션 비교 :



**솔루션 커스터디(예: Satoshi의 Wallet)** :




- 라이트닝 비트코인은 신뢰할 수 있는 제3자가 관리합니다
- 간편한 사용, 기술적 복잡성 없음
- 운영자가 자금을 보유하고 거래를 추적할 수 있습니다
- 제어 및 개인정보 보호 희생



**상품이 아닌 소비자 지갑(예: 피닉스, 브리즈)** :




- 사용자는 자신의 개인 키와 BTC의 Ownership을 유지합니다
- 완전한 노드 관리 없음 - 애플리케이션이 백그라운드에서 채널을 관리합니다
- 단순성과 주권 사이의 타협
- 유동성을 위한 공급업체 인프라에 대한 의존도
- 기술적 제한(한 스마트폰에서 다른 스마트폰으로 결제를 라우팅할 수 없음)



**자체 호스팅 LND 노드(엄브렐)** :




- 최대 주권: On-Chain 및 off-chain BTC는 전적으로 귀하의 통제하에 있습니다
- 제3자가 채널 개설이나 결제 관리에 관여하지 않습니다
- 개인정보 보호 강화(채널과 거래는 본인과 직계 동료에게만 공개)
- 사용의 자유: 나만의 서비스와 지갑에 연결하기
- 타인을 위한 거래 라우팅 가능성(소액 수수료 보상)
- 기술적 책임 증가(유지보수, 유동성 관리, 백업)



요컨대, 셀프 호스팅 LND는 최대한의 제어권을 제공하지만 더 많은 기술력이 필요합니다. 이는 편의성과 주권 사이의 절충안입니다.



## 4. 단계별 튜토리얼



### 4.1 엄브렐에 라이트닝 노드 애플리케이션 설치 및 구성하기



엄브렐 노드(Bitcoin)가 동기화되면 다음 단계를 따르세요:



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Interface 엄브렐의 '앱 스토어' 섹션에서 라이트닝 노드 애플리케이션을 설치합니다.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND(Lightning Network Daemon)가 엄브렐에 애플리케이션으로 배포됩니다. 처음 열면 Lightning이 실험 중인 기술임을 알리는 경고 메시지가 표시됩니다.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



새 노드를 만들거나 백업/seed에서 노드를 복원하는 방법 중에서 선택할 수 있습니다. 처음 설치하는 경우 새 노드 생성을 선택합니다. 라이트닝 노드 앱은 24단어 Mnemonic 문구(seed 라이트닝)를 generate로 생성합니다. 필요한 경우 라이트닝 자금을 복원하는 데 사용되므로 매우 신중하게(오프라인, 종이에 적는 것이 이상적) 적어두세요.



**참고: 최신 버전의 엄브렐에서는 라이트닝 앱을 설치하면 이 24단어 seed가 제공됩니다(Bitcoin 엄브렐 노드 자체는 제공되지 않음).



![Interface principale de Lightning Node](assets/fr/04.webp)



초기화 후, 라이트닝 노드의 기본 Interface에 액세스하게 됩니다.



![Paramètres de l'application](assets/fr/05.webp)



애플리케이션 설정에는 여러 가지 중요한 옵션이 있습니다:




   - 노드 ID(노드의 고유 식별자)를 참조하세요
   - 외부 Wallet 연결하기(Wallet 연결)
   - 비밀 단어 보기
   - 고급 설정에 액세스
   - 채널 복구
   - 채널 백업 파일 다운로드
   - 자동 백업 사용
   - 토르를 통한 백업 구성(토르를 통한 백업)



이러한 옵션은 라이트닝 노드의 보안과 관리에 필수적입니다. 자동 백업을 활성화하고 비밀 단어를 안전하게 보관하세요.



**유용한 리소스:**




- [엄브렐 커뮤니티](https://community.umbrel.com) - 엄브렐과 그 생태계에 관한 문제와 해결책을 공유하는 사용자 토론 포럼입니다


> - [엄브렐 앱스토어 - 라이트닝 노드(LND)](https://apps.umbrel.com/app/lightning) - 엄브렐의 라이트닝 노드 앱 기능에 대한 설명
> - [LND 문서 - 빠른 시작](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - LND 공식 문서

### 4.2 라이트닝 채널 열기



LND가 가동되고 나면 첫 번째 라이트닝 채널을 열 수 있습니다. 연결할 양질의 노드를 찾습니다:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/)는 채널을 개설할 수 있는 신뢰할 수 있는 노드를 찾기 위한 탐색기입니다.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



예를 들어, [ACINQ 노드](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f)는 뛰어난 가용성과 유동성 통계로 인정받는 노드입니다.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



이 튜토리얼에서는 [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca)로 채널을 열겠습니다. 연결에 필요한 정보(pubkey@ip:port)는 앰보스 페이지에 나와 있습니다.



채널을 열려면 :



![Bouton d'ouverture de canal](assets/fr/09.webp)



라이트닝 노드 홈 페이지에서 "+ 채널 열기" 버튼을 클릭합니다



![Configuration du canal](assets/fr/10.webp)



채널 구성 페이지에서 :




   - Amboss에서 복사한 노드 ID를 붙여넣습니다(형식: pubkey@ip:port)
   - 채널 용량을 정의합니다(ACINQ와 같은 일부 노드에는 최소값이 있습니다. 예: 400k Sats)
   - 필요한 경우 개시 거래 수수료 조정



![Canal en cours d'ouverture](assets/fr/11.webp)



트랜잭션이 전송되면 채널이 홈 페이지에 "개설 중"으로 표시됩니다. On-Chain 트랜잭션이 확인될 때까지 기다립니다.



![Détails du canal](assets/fr/12.webp)



채널을 클릭하면 자세한 내용을 볼 수 있습니다:




   - 현재 상태
   - 총 용량
   - 유동성 분석(수신/발신)
   - 원격 노드의 공개 키
   - 기타 기술 정보



### Lightning Network+를 사용하여 유입 유동성 확보하기



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



엄브렐 앱스토어에서 Lightning Network+를 구매하면 수입 현금을 더 쉽게 확보할 수 있습니다.



![Interface principale de LN+](assets/fr/14.webp)



기본 Interface는 세 가지 중요한 옵션을 제공합니다:




- "유동성 스왑: 사용 가능한 스왑 오퍼 살펴보기
- "나를 위해 열기": 자격이 되는 스왑을 필터링합니다
- '문서로': 문서에 액세스



![Message d'erreur LN+](assets/fr/15.webp)



참고: 아직 채널이 개설되어 있지 않은 경우 '나를 위해 열기'를 클릭하면 이 오류 메시지가 표시됩니다.



![Liste des swaps disponibles](assets/fr/16.webp)



"유동성 스왑" 페이지에는 네트워크에서 사용 가능한 모든 스왑 오퍼가 표시됩니다.



![Swaps éligibles](assets/fr/17.webp)



"나를 위해 열기"는 노드가 필요한 조건을 충족하는 스왑만 필터링합니다.



![Détails d'un swap](assets/fr/18.webp)



스왑 세부 정보 예시 :




- 펜타곤 구성(참가자 5명)
- 채널당 300k Sats 용량
- 전제 조건: 총 용량이 1M Sats인 최소 10개 오픈 채널
- 이용 가능한 장소: 4/5



### 4.3 모바일 애플리케이션(Zeus)과의 동기화



라이트닝 노드를 원격(스마트폰)으로 제어하려면 Zeus(iOS/Android에서 사용 가능한 오픈 소스 애플리케이션)를 사용할 수 있습니다.



**엄브렐이 포함된 제우스 구성 :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



엄브렐 노드에 액세스할 수 있는지 확인하세요(기본값은 Tor를 통해).


Interface 엄브렐에서 라이트닝 노드 앱을 연 다음 화살표가 가리키는 대로 'Wallet 연결' 버튼을 클릭합니다.



![Page de connexion avec QR code](assets/fr/20.webp)



LND 액세스 데이터가 lndconnect 형식으로 포함된 QR 코드가 나타납니다. 이 QR 코드는 특히 정보가 밀집되어 있으므로 주저하지 말고 확대하여 쉽게 읽을 수 있도록 하세요.



![Configuration initiale de Zeus](assets/fr/21.webp)



휴대폰에서 :




   - 제우스 열기
   - 홈 페이지에서 '고급 설정'을 클릭하여 나만의 라이트닝 노드를 연결합니다
   - 매개변수에서 "Wallet 생성 또는 연결"을 선택합니다



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



제우스에서:




   - 연결 유형으로 "LND(REST)"를 선택합니다
   - QR 코드를 스캔하거나(권장 방법) 정보를 수동으로 입력할 수 있습니다. (엄브렐 QR 코드는 매우 촘촘하므로 주저하지 마시고 확대하세요.)
   - 중요: 엄브렐이 토르(기본값)를 통해서만 액세스할 수 있는 경우 "토르 사용" 옵션을 활성화합니다
   - 구성 저장



이제 제우스가 엄브렐 노드에 연결되어 라이트닝 결제를 하고 채널, 잔액 등을 확인하면서 완전히 자체적으로 관리할 수 있습니다.



**고급 연결 옵션:**



기본적으로 제우스 ↔ 엄브렐 연결은 토르를 통해 이루어집니다. 더 빠른 연결을 위해 두 가지 대안이 있습니다:



**라이트닝 노드 연결(LNC)** :




   - 라이트닝 랩의 암호화된 연결 메커니즘
   - 엄브렐에 라이트닝 터미널 앱을 설치합니다(LNC 액세스 포함)
   - generate 라이트닝 터미널의 연결 QR코드(연결 → LNC를 통해 Zeus 연결)
   - Zeus로 스캔합니다(연결 유형으로 "LNC" 선택)



**VPN 테일스케일**:




   - 구성하기 쉬운 메시 VPN
   - 엄브렐(App Store)과 휴대폰에 Tailscale을 설치하세요
   - 토르 Address 대신 테일스케일 사설 IP를 통해 제우스를 연결하세요



이러한 옵션은 필수는 아니며, 대부분의 경우 Tor + Zeus 솔루션이 잘 작동합니다.



> **유용한 리소스:**
> - [제우스 문서 - 엄브렐 연결](https://community.umbrel.com/t/zeus-LN-mobile/7619) - 제우스와 엄브렐 연결 공식 가이드
> - [제우스 깃허브](https://github.com/ZeusLN/zeus) - 제우스 오픈소스 프로젝트
> - [엄브렐 커뮤니티 - 테일스케일을 통한 제우스 연결하기](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - 테일스케일을 사용하여 제우스를 엄브렐에 연결하는 방법 가이드

## 5. 안전 및 모범 사례



자체 호스팅된 라이트닝 노드를 관리하려면 보안에 특히 주의해야 합니다.



### 노드 백업 및 보안



**필수 백업 유형**



라이트닝 엄브렐 노드에는 두 가지 유형의 백업이 필요합니다:



**seed 문장(24단어)**




- On-Chain 자금 회수
- Wallet 라이트닝을 다시 생성하는 데 필요합니다
- 매우 안전한 스토리지(오프라인, 종이)



**정적 채널 백업(SCB)** 파일




- 라이트닝 채널 정보 포함
- 크래시 발생 시 강제 채널 폐쇄 활성화
- 중요:** `channel.db` 파일을 수동으로 저장하지 마세요(불이익을 받을 수 있습니다)



**수동 백업 절차**



채널을 수동으로 저장하려면 :


1. 라이트닝 노드 메뉴('+ 채널 열기' 옆의 점 "⋮" 3개)에 액세스합니다


2. 채널 백업 파일 다운로드


3. 각 채널 수정 후 새 SCB 내보내기


4. SCB를 안전하게 저장(암호화된 미디어, 오프사이트 복사본)



**엄브렐** 자동 백업 시스템



Umbrel은 정교한 자동 백업 시스템을 갖추고 있어 :



*데이터 보호:*




- 전송 전 클라이언트 측 암호화
- 토르 네트워크를 통한 전송
- 무작위 채우기로 보완된 데이터
- 장치에 고유한 암호화 키



*보안 강화:*




- 상태 변경 시 즉시 백업
- 무작위 간격으로 "디코이" 백업하기
- 백업 크기 변경 사항 숨기기
- 시간 분석에 대한 보호



*복원 프로세스:*




- seed 엄브렐에서 파생된 식별자 및 키
- Mnemonic 문구만으로 완전한 복원 가능
- 최신 백업 자동 복구
- 채널 설정 및 데이터 복원



### 충돌 복구



노드가 분실된 경우(하드웨어 오류, SD 카드 손상) :




- 엄브렐 재설치
- Lightning 앱에 24단어 seed을 입력하세요
- 복원 중 SCB 파일 가져오기



LND은 기존 채널의 각 파트너에게 연락하여 채널을 폐쇄하고 On-Chain 기금에 대한 귀하의 몫을 회수합니다. 채널은 영구적으로 폐쇄됩니다(필요한 경우 다시 열릴 수 있음).



### 가용성 및 사기 방지



매듭을 가능한 한 자주 온라인에 두는 것이 가장 이상적입니다. 장기간 부재 중인 경우:




- 악의적인 피어가 이전 채널 상태를 브로드캐스트하려고 시도할 수 있습니다
- 라이트닝은 '항의 기간'(LND의 경우 약 2주)을 제공합니다
- 장기간 자리를 비울 예정이라면 Watchtower를 설정하세요



**Watchtower 구성:**




- LND 고급 설정에서 신뢰할 수 있는 Watchtower 서버의 URL을 추가합니다
- 퍼블릭 서비스를 사용하거나 자체 Watchtower를 설치할 수 있습니다




워치타워를 구성하고 사용하는 방법에 대해 자세히 알아보려면 전용 튜토리얼 을 살펴보는 것이 좋습니다:



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### 기타 모범 사례





- 소프트웨어 업데이트:** Umbrel 및 LND을 최신 상태로 유지(보안 수정)
- 하드웨어 보호: ** 안정적인 시스템(SSD가 장착된 라즈베리 파이, 미니 PC) 및 UPS 사용
- 네트워크 보안: ** 기본 토르 구성 유지, 엄브렐 관리자 비밀번호 변경(기본값: "moneyprintergobrrr")
- 암호화:** 가능하면 디스크 암호화를 활성화합니다



## 6. 추가 도구



엄브렐의 라이트닝 노드 앱은 채널 관리에 필수적인 기능을 제공하지만, 타사 도구는 고급 기능을 제공합니다.



### ThunderHub



엄브렐 앱 스토어를 통해 설치할 수 있는 최신 웹 기반 라이트닝 노드 관리 시스템 Interface.



**기능:**




- 채널(용량, 잔액)의 실시간 시각화
- 통합 리밸런싱 도구
- 다중 경로 청구(MPP) 지원
- QR코드 생성 LNURL
- 거래 관리 On-Chain



ThunderHub는 활성 라우팅 노드를 모니터링하고 간단한 리밸런싱을 수행하는 데 이상적입니다.



### 라이드 더 라이트닝(RTL)



Interface 웹은 여러 라이트닝 구현(LND, 코어 라이트닝, 에클레어)과 호환됩니다.



**주요 내용:**




- 멀티 노드 관리
- 상황에 맞는 대시보드
- 잠수함 스왑 지원(라이트닝 루프)
- 2단계 인증
- 채널 백업 내보내기/가져오기



RTL은 보다 전문가 지향적인 접근 방식으로 라이트닝 노드를 관리할 수 있는 완벽한 '스위스 군용 칼'입니다.



### 기타 유용한 도구





- 라이트닝 셸**: 브라우저를 통한 명령줄(lncli)
- BTC RPC 익스플로러 및 Mempool**: Blockchain 모니터링
- LNmetrics & Torq**: 라우팅 성능 분석
- Amboss & 1ML**: 노드의 "소셜" 관리(별칭, 연락처, 네트워크 분석)



이러한 도구는 복잡한 설정 없이 엄브렐 앱 스토어에서 클릭 몇 번으로 설치할 수 있습니다.



**추가 도구 리소스:**




- [ThunderHub.io - 기능](https://thunderhub.io) - ThunderHub 기능 개요
- [Ride The Lightning(RTL) 정보](https://www.ridethelightning.info/) - RTL 문서
- [데이비드 카스파 - 썬더허브를 통한 리밸런싱](https://blog.davidkaspar.com) - 리밸런싱에 대한 실용적인 가이드
- [가이드 "라이트닝 노드 관리"](https://github.com/openoms/lightning-node-management) - 파워 사용자를 위한 고급 문서



## 결론



엄브렐에서 자체 LND 노드를 운영하는 것은 금융 주권을 향한 중요한 단계입니다. 커스터디 솔루션보다 더 많은 기술적 개입이 필요하지만, 제어, 개인정보 보호 및 Lightning Network에 대한 적극적인 참여 측면에서 얻을 수 있는 이점은 상당합니다.



이 가이드를 따라 LND을 설치하고, 채널을 열고, 유동성을 관리하고, 노드에 원격으로 액세스할 수 있을 것입니다. 에코시스템에 익숙해지면 고급 기능과 추가 도구를 점차적으로 살펴보시기 바랍니다.



자금의 보안은 안전장치와 관행에 따라 달라진다는 점을 기억하세요. 큰 금액을 송금하기 전에 시간을 들여 모든 측면을 이해하세요.