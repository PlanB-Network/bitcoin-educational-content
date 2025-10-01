---
name: Umbrel
description: Umbrel - Bitcoin 노드 및 홈 서버 알아보기 및 설치하기
---

![cover](assets/cover.webp)


![video](https://youtu.be/qFfhr4sApso)


## 소개



### Bitcoin 노드란 무엇인가요?



Bitcoin 노드는 Bitcoin core 소프트웨어 또는 대체 클라이언트를 실행하여 Bitcoin 네트워크에 참여하는 컴퓨터입니다. 네트워크의 운영과 보안에 필수적인 역할을 합니다:





- Blockchain 스토리지**: Blockchain Bitcoin의 완전한 최신 사본을 유지합니다
- 트랜잭션 검증**: 프로토콜 규칙에 따라 각 트랜잭션과 블록의 유효성을 검사합니다
- 정보 전파**: 새로운 트랜잭션과 블록을 다른 노드와 공유합니다
- 합의 형성**: 네트워크 규칙 적용에 기여



자체 Bitcoin 노드를 운영하는 것은 금융 주권을 향한 중요한 단계이며, 몇 가지 주요 이점을 제공합니다:





- 기밀 유지**: 제3자에게 정보를 공개하지 않고 거래를 공유하세요
- 검열에 대한 저항**: 아무도 Bitcoin 사용을 막을 수 없습니다
- 독립적인 검증**: 거래를 검증하기 위해 다른 사람의 노드를 신뢰할 필요가 없습니다
- 공감대 형성**: Bitcoin 네트워크 규칙 적용에 기여합니다
- 네트워크 지원**: 네트워크 배포 및 탈중앙화에 적극적으로 참여하세요



### 엄브렐: Bitcoin 노드를 실행하기 위한 간단한 솔루션



엄브렐은 Bitcoin 노드의 설치와 관리를 간소화하는 오픈 소스 운영체제입니다. 또한 컴퓨터를 개인 및 개인 홈 서버로 전환하여 쉽게 호스팅할 수 있습니다:





- 완전한 Bitcoin 노드
- Bitcoin 필수 애플리케이션(Electrs, Mempool.space)
- 기타 개인 서비스(클라우드 스토리지, 스트리밍, VPN 등)



우아하고 직관적인 사용자 Interface를 통해 누구나 셀프 호스팅 서비스에 액세스할 수 있으며, 데이터에 대한 완전한 제어권을 유지합니다.



## 엄브렐 설치 옵션



엄브렐은 턴키 옵션(엄브렐 홈)과 무료 오픈 소스 버전(엄브렐OS)의 두 가지 주요 솔루션 사용 방법을 제공합니다.



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### 엄브렐 홈: 턴키 솔루션



엄브렐 홈은 최적의 환경을 위해 특별히 설계된 사전 구성된 홈 서버입니다. 이 올인원 하드웨어 솔루션에는 다음이 포함됩니다:



**하드웨어 기능**




- 셀프 호스팅에 최적화된 고성능 프로세서
- 사전 설치된 고속 SSD 스토리지
- 저소음 냉각 시스템
- 컴팩트하고 우아한 디자인
- 통합 USB 및 이더넷 포트



**독점 혜택**




- 플러그 앤 플레이 설치: 플러그를 꽂고 바로 사용
- 전담 지원을 통한 프리미엄 지원
- 자동 업데이트 보장
- 통합 마이그레이션 마법사
- 전체 하드웨어 보증
- 모든 기능에 대한 완벽한 지원



**가격**: €399(시즌에 따라 가격이 달라질 수 있음)



### UmbrelOS: 오픈 소스 버전



UmbrelOS는 Umbrel 운영 체제의 무료 오픈 소스 버전입니다. 이 유연한 솔루션을 사용하면 자체 하드웨어를 사용하면서 Umbrel의 필수 기능을 활용할 수 있습니다.



**혜택**




- 완전 무료
- 검증 가능한 공개 소스 코드
- 선택의 자유
- 고급 사용자 지정 옵션



**지원 플랫폼**




- 라즈베리 파이 5: 대중적이고 경제적인 솔루션
- X86 시스템: 표준 PC 또는 서버용
- 가상 머신: 기존 인프라에서 테스트 또는 사용



**제한 사항**




- 커뮤니티 지원 전용
- 엄브렐 홈 전용의 일부 고급 기능
- 보다 기술적인 초기 구성
- 성능은 선택한 하드웨어에 따라 다릅니다



이 버전은 :




- 기술 사용자
- 이미 호환 장비를 소유하고 계신 분
- 배우고 실험하고 싶은 사람
- 프로젝트에 기여하고자 하는 개발자



공식 설치 링크 :




- [라즈베리 파이 5에 설치](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [x86 시스템에 설치(https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [가상 머신 설치](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



이 튜토리얼에서는 라즈베리 파이 5에 엄브렐OS를 설치하는 데 중점을 두지만 기본 원칙은 다른 플랫폼에서도 비슷합니다.



## 라즈베리파이 5에 엄브렐 OS 설치하기



### 필수 구성 요소



이 설치에는 다음이 필요합니다:





- 라즈베리 파이 5(4GB 또는 8GB RAM)
- 공식 라즈베리파이 파워 Supply(안정성을 위해 필수!)
- MicroSD 카드(최소 32GB)
- MicroSD 카드 리더기
- 데이터 저장용 외장 SSD
- 이더넷 케이블
- SSD 연결용 USB 케이블



### 설치 단계



**UmbrelOS 다운로드**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- 공식 웹사이트](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5) 방문하기
- 라즈베리 파이 5용 UmbrelOS 최신 버전 다운로드



**발레나 에처** 설치



![Téléchargement Balena Etcher](assets/fr/02.webp)




- 컴퓨터에 [발레나 에처](https://www.balena.io/etcher/)를 다운로드하여 설치합니다



**microSD** 카드 준비하기



![Insertion carte microSD](assets/fr/03.webp)




- 컴퓨터의 카드 리더에 microSD 카드를 삽입합니다



**이미지 깜박임**



![Flashage UmbrelOS](assets/fr/04.webp)




- 발레나 에처 출시
- 다운로드한 UmbrelOS 이미지를 선택합니다
- MicroSD 카드를 대상으로 선택
- "플래시!"를 클릭하고 프로세스가 완료될 때까지 기다립니다
- 안전하게 카드 꺼내기



**마이크로SD 카드 설치**



![Installation microSD](assets/fr/05.webp)




- 라즈베리 파이 5에 microSD 카드를 삽입합니다



**주변기기 연결**



![Connexion périphériques](assets/fr/06.webp)




- 외장 SSD를 사용 가능한 USB 포트에 연결
- Pi와 라우터 사이에 이더넷 케이블을 연결합니다



**전원 켜기**



![Démarrage du Pi](assets/fr/07.webp)




- 공식 라즈베리파이 전원 Supply 연결하기
- 시스템이 시작될 때까지 몇 분 정도 기다립니다



**첫 번째 액세스**



![Accès interface web](assets/fr/08.webp)




- 동일한 네트워크에 연결된 디바이스에서 브라우저를 엽니다
- 엄브렐의 Interface 웹 사이트에 접속하세요: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



엄브렐.local`이 작동하지 않는 경우, 로컬 네트워크에서 라즈베리파이의 IP Address을 찾아야 합니다. 당신은 :




- 라우터의 Interface를 참조하세요
- Nmap과 같은 네트워크 스캐너 사용
- 컴퓨터 터미널에서 `arp -a` 명령을 사용합니다



## 엄브렐의 첫 걸음



엄브렐이 시작되고 브라우저를 통해 액세스할 수 있게 되면 다음 단계에 따라 시작하세요:



### 초기 구성



**계정 만들기**



![Création compte](assets/fr/10.webp)




- 사용자 이름 선택
- 보안 비밀번호 설정
- 엄브렐에 액세스하려면 다음 자격 증명이 필요합니다



**계정 확인**



![Confirmation compte](assets/fr/11.webp)




- "다음"을 클릭하여 대시보드에 액세스합니다



**Interface의 발견**



![Interface Umbrel](assets/fr/12.webp)




- 엄브렐 앱 스토어에 액세스
- 사용 가능한 다양한 애플리케이션 알아보기
- Bitcoin에 필수적인 애플리케이션 설치부터 시작하겠습니다



### Bitcoin 애플리케이션 설치



**Bitcoin 노드**



![Bitcoin Node](assets/fr/13.webp)




- 첫 번째 애플리케이션 설치
- Blockchain Bitcoin 전체 다운로드 및 확인



**Electrs**



![Installation Electrs](assets/fr/14.webp)




- Bitcoin 지갑 연결을 위한 일렉트럼 서버
- Bitcoin 노드와 동기화



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Blockchain용 Interface 디스플레이
- 트랜잭션과 블록을 실시간으로 추적



## Mempool.space로 거래 추적하기



Mempool.space는 Blockchain 네트워크의 실시간 시각화를 제공하는 오픈 소스 Bitcoin 탐색기입니다. 트랜잭션을 추적하고 네트워크에서 트랜잭션이 어떻게 전파되는지 이해할 수 있습니다.



### Mempool 및 확인 이해



"Mempool"(메모리 풀)은 블록에 포함되기 전에 모든 미확인 Bitcoin 트랜잭션이 저장되는 가상 대기실과 같은 곳입니다. 트랜잭션이 처리되는 방식은 다음과 같습니다:



1. **브로드캐스트**: 트랜잭션을 전송하면 먼저 Bitcoin 네트워크에서 브로드캐스트됩니다


2. **Mempool에서 대기 중**: 비용에 따라 Miner에서 선정되기를 기다리는 중입니다


3. **첫 번째 확인**: 미성년자가 블록에 포함됨(1차 확인)


4. **추가 확인**: 트랜잭션이 포함된 블록 이후에 채굴되는 각 새 블록은 확인을 추가합니다



권장 확인 횟수는 금액에 따라 다릅니다 :




- 소량의 경우: 1~2회 확인으로 충분할 수 있습니다
- 많은 금액의 경우: 일반적으로 6개의 확인은 매우 안전한 것으로 간주됩니다



### Interface에서 Mempool.space 살펴보기



1. **홈페이지**에서 Bitcoin 네트워크에 대한 개요를 확인할 수 있습니다:




   - 최근 채굴된 블록
   - 다양한 우선순위에 따른 비용 추정
   - Mempool의 현재 상태



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **트랜잭션 검색**: 특정 거래를 추적하려면 페이지 상단의 검색창에 해당 거래의 식별자(txid)를 붙여넣습니다.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### 거래 세부 정보 분석



거래가 발견되면 Mempool.space는 완전한 분석 결과를 제공합니다:



1. **필수 정보** :




   - 상태(확인 여부)
   - 지불한 비용(Sats/vB 기준)
   - 예상 확인 시간



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **트랜잭션 구조** :




   - 입력 및 출력의 시각적 표현
   - 관련 주소의 상세 목록
   - 이체 금액



3. **기술 데이터** :




   - 트랜잭션 가중치
   - 가상 크기
   - 사용 형식 및 버전
   - 기타 특정 메타데이터



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### 엄브렐에서 Mempool.space 사용의 이점



1. **기밀성**: 사용자의 요청은 자체 노드를 통해 전달됩니다


2. **독립성**: 타사 서비스에 의존할 필요 없음


3. **신뢰성**: 공용 브라우저가 다운된 상태에서도 데이터 액세스



이 애플리케이션을 사용하면 거래를 효율적으로 모니터링하고, 수수료가 확인 속도에 어떤 영향을 미치는지 이해하고, Bitcoin 네트워크의 작동 방식을 더 잘 이해할 수 있습니다.



## Wallet Bitcoin을 노드에 연결하기



### Electrs 구성



**로컬 연결**



![Connexion locale](assets/fr/18.webp)




- 로컬 네트워크에서 사용
- 더 빠르고 쉬운 설정



**토어를 통한 원격 연결**



![Connexion Tor](assets/fr/19.webp)




- 어디서나 노드에 액세스하려면
- 보안 및 비공개성 강화



### Sparrow wallet와 연결



**매개변수에 대한 액세스**



![Paramètres Sparrow](assets/fr/20.webp)




- Sparrow wallet 열기
- 환경설정 > 서버로 이동합니다
- "기존 연결 수정"을 클릭합니다



**연결 유형 선택**



Sparrow는 세 가지 연결 모드를 제공합니다:



***퍼블릭 서버***




- 퍼블릭 서버 연결(예: blockstream.info, Mempool.space)
- 단순하지만 덜 사적인



***Bitcoin core***




- Bitcoin 노드에 직접 연결
- 비공개이지만 느린 속도



***개인 일렉트럼***




- Electrs 서버에 연결
- 개인 정보 보호와 성능의 결합



**Electrs** 구성



앞서 살펴본 Electrs 애플리케이션에 표시된 정보를 사용하여 연결 유형을 선택합니다:



두 경우 모두 'SSL 사용' 및 '프록시 사용' 옵션을 선택하지 않은 상태로 둡니다.



**로컬 연결**


호스트: umbrel.local


포트 번호: 50001



**원격 연결(토르)**


호스트 : [your-Address-onion]


포트 번호: 50001



로컬 네트워크 외부에서 노드에 액세스하려면 토르 연결이 필요합니다.



![Configuration connexion](assets/fr/21.webp)


Sparrow wallet 소프트웨어에 대한 자세한 내용은 종합 튜토리얼 을 참조하세요:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## 결론



이제 엄브렐을 사용할 준비가 되었습니다. 데이터에 대한 완전한 제어권을 유지하면서 Bitcoin 네트워크에 적극적으로 참여할 수 있습니다. 엄브렐 앱 스토어에서 제공되는 다른 많은 애플리케이션을 자유롭게 탐색하여 홈 서버의 기능을 확장하세요.



## 유용한 리소스



### 공식 문서




- [엄브렐 공식 웹사이트](https://umbrel.com)
- [엄브렐 문서](https://github.com/getumbrel/umbrel/wiki)
- [앱스토어 엄브렐](https://apps.umbrel.com)



### Bitcoin 애플리케이션




- [Bitcoin core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow wallet](https://sparrowwallet.com)



### 커뮤니티




- [포럼 엄브렐](https://community.getumbrel.com)
- [깃허브 엄브렐](https://github.com/getumbrel)
- [트위터 엄브렐](https://twitter.com/umbrel)