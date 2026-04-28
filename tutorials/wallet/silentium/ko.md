---
name: Silentium
description: 무음 결제가 지원되는 프로그레시브 웹 wallet(BIP-352)
---

![cover](assets/cover.webp)



Bitcoin 주소의 재사용은 사용자 기밀성에 대한 가장 직접적인 위협 중 하나입니다. 수취인이 하나의 주소를 공유하여 여러 차례 결제를 받는 경우, 모든 관찰자는 관련된 모든 거래를 추적하고 재정 내역을 재구성할 수 있습니다. 이 문제는 특히 개인정보 침해 없이 기부 주소를 공개적으로 표시하고자 하는 콘텐츠 제작자, 자선단체 또는 활동가에게 영향을 미칩니다.



Silentium는 브라우저에서 직접 액세스할 수 있는 우아한 솔루션으로 이 문제에 대응합니다. 루이스 싱어가 2024년 5월에 출시한 이 오픈 소스 프로그레시브 웹 애플리케이션(PWA)은 재사용 가능한 정적 주소인 사일런트 페이먼트(BIP-352)를 구현하여 각 결제가 별도의 blockchain 주소로 끝나며 거래 간의 사전 상호작용이나 관찰 가능한 링크가 없습니다.



**중요 경고**: Silentium은 사일런트 페이먼트의 경량 wallet의 *개념 증명*을 위한 실험적인 프로젝트입니다. 일상적인 wallet로 사용하거나 많은 양을 저장하는 용도로 사용해서는 안 됩니다. 개발자는 다음과 같이 명시하고 있습니다:



> 본인 책임하에 사용하세요.

이 wallet는 테스트넷 또는 재테스트로 사용할 수 있습니다.



## Silentium이란 무엇인가요?



### 철학 및 목표



Silentium은 가벼운 wallet 브라우저에서 자동 결제 기능을 구현하기 위한 기술 데모입니다. 기존 Bitcoin 주소도 지원하지만, 사용자가 이 개인정보 보호 기술을 간단한 방법으로 실험해볼 수 있도록 무음 결제에 중점을 두고 있습니다.



### 자동 결제는 어떻게 작동하나요?



자동 결제(BIP-352)는 타원 곡선 디피-헬만 키 Exchange(ECDH)를 사용합니다. 수취인은 결제를 감지하는 스캔 키와 이를 사용하기 위한 지출 키의 두 가지 공개 키로 구성된 정적 주소(mainnet의 경우 `sp1...`, 테스트넷의 경우 `tsp1...`)를 생성합니다.



발신자는 자신의 개인 입력 키와 수신자의 스캔 키를 결합하여 암호화 '조정'을 생성하는 공유 비밀을 계산합니다. 이 조정이 지출 키에 추가되면 각 트랜잭션에 대해 고유한 Taproot 주소가 생성됩니다. 수취인은 자신의 개인 스캔 키를 사용하여 이 계산을 재현하여 사전 상호 작용 없이 자금을 감지하고 지출합니다.



장점: 발신자와 수신자의 기밀성 강화, 타사 서버 필요 없음, 기존 Taproot 결제와 구분할 수 없는 거래. 주요 단점: 결제를 감지하기 위해 blockchain을 집중적으로 스캔해야 합니다.



자동 결제의 이론적 작동 방식에 대해 자세히 알아보려면 BTC,204 과정의 마지막 부분인 Plan ₿ Academy 을 참조하세요:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 지원 플랫폼



Silentium는 모든 최신 브라우저(모바일 또는 데스크톱)에서 액세스할 수 있는 프로그레시브 웹 앱(PWA)입니다. 'app.silentium.dev'에서 직접 사용하거나 브라우저를 통해 기본 애플리케이션으로 설치하거나 로컬에 배포할 수 있습니다. 공식 스토어를 거치지 않고 브라우저에서 직접 설치할 수 있습니다.



## 웹 앱 사용



### 액세스 및 설치



[브라우저에서 `https://app.silentium.dev/`로 이동](https://app.silentium.dev/). 애플리케이션이 즉시 로드되고 홈 화면이 표시됩니다.



IOS에서 기본 애플리케이션으로 설치하려면 공유 버튼(위쪽 화살표가 있는 사각형)을 누른 다음 '홈 화면에'를 선택합니다. Android에서는 일반적으로 브라우저에서 "홈 화면에 추가" 알림을 바로 제공합니다. 설치가 완료되면 Silentium이 전용 아이콘과 함께 나타나며 기본 애플리케이션으로 작동하지만 트랜잭션을 동기화하려면 인터넷 연결이 필요합니다.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### 포트폴리오 생성



처음 실행할 때 'Wallet 생성'을 선택하여 새 wallet를 생성하거나 'Wallet 복원'을 선택하여 기존 복구 구문에서 복원합니다.



"Wallet 만들기"를 선택합니다. 애플리케이션에서 12단어 문구가 생성되며, 이 문구를 주의 깊게 적어야 합니다. 이 문구는 자금을 복구할 수 있는 유일한 방법입니다. 테스트넷에서도 좋은 백업 방법을 채택하세요. 문구를 저장한 후 "계속"을 누릅니다.



그러면 애플리케이션에서 wallet에 대한 보안 액세스를 위해 비밀번호를 설정하라는 메시지가 표시됩니다. 강력한 비밀번호를 선택하고 확인합니다.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



문구가 확인되고 비밀번호가 설정되면 기본 인터페이스로 이동합니다.



### Interface 메인 및 파라미터



메인 인터페이스에는 잔액이 satoshi초 단위(초기에는 0 sats)로 표시되며, 하단에 3개의 버튼이 있습니다:




- 동기화**: wallet를 blockchain과 동기화합니다
- 받기**: 자금을 받다
- 보내기**: 비트코인을 보내려면



오른쪽 상단의 아이콘(가로 막대 3개)을 통해 설정에 액세스합니다. 설정 메뉴에는 여러 가지 옵션이 있습니다:





- 정보**: 애플리케이션 정보
- 백업**: 복구 문구 백업
- 탐색기**: blockchain 탐색기(기본값은 Mempool) 및 Silentiumd 서버를 선택합니다
- 네트워크**: 네트워크 선택(mainnet/테스트넷)
- 비밀번호**: 비밀번호 변경
- 재장전**: wallet 재장전
- 초기화**: 초기화 완료
- 테마**: 테마 변경



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



익스플로러** 섹션은 특히 중요한데, 이 섹션에서는 사용하는 blockchain 익스플로러(기본값은 Mempool)를 선택할 수 있고 Silentiumd 서버의 URL(mainnet의 경우 `https://bitcoin.silentium.dev/v1`)도 표시합니다. 자체 Silentiumd 서버를 호스팅하거나 테스트넷을 사용하려는 경우 여기에서 이러한 매개변수를 구성할 수 있습니다.



### 자금 수령



메인 인터페이스에서 "수신" 버튼을 누릅니다. 기본적으로 Silentium는 QR코드와 함께 자동 결제 주소를 표시합니다. 주소는 mainnet의 경우 `sp1...`로 시작하거나 테스트넷의 경우 `tsp1...`로 시작합니다.



화면 하단의 "클래식 주소로 전환"/ "무음 주소로 전환" 버튼을 사용하여 무음 결제와 기존 Bitcoin 주소 사이를 전환할 수 있습니다.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




거래가 브로드캐스트되면 몇 분 정도 기다려주세요. 자동 결제의 경우, Silentium은 blockchain에서 귀하를 대상으로 하는 거래를 자동으로 검색합니다. 거래는 점진적으로 확인되기 전에 "미확인" 상태로 표시됩니다.



### 결제 보내기



메인 인터페이스에서 '보내기' 버튼을 누릅니다. 보내기 화면에서 다음과 같은 메시지가 표시됩니다:



1. **Address**: 자동 결제 주소(`sp1...` 또는 `tsp1...`) 또는 기존 Bitcoin 주소를 붙여넣습니다. QR 스캔 아이콘을 사용하여 주소를 스캔할 수 있습니다.


2. **금액**: 송금할 금액을 satoshi초 단위로 입력합니다. 숫자 키패드가 표시되어 쉽게 입력할 수 있습니다. 사용 가능한 잔액이 상단에 표시되어 참고할 수 있습니다.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



주소와 금액을 입력한 후 '진행'을 눌러 계속 진행합니다. 애플리케이션에서 거래를 확인하기 전에 원하는 수수료 수준을 선택하라는 메시지가 표시됩니다.



## wallet 셀프 호스팅



### 셀프 호스팅을 하는 이유는 무엇인가요?



Silentium의 로컬 호스팅은 완전한 주권, 코드 검증, 개발 환경, 공식 사이트 장애에 대비한 복원력을 제공합니다.



### 전제 조건



Node.js(버전 14 이상), npm 또는 yarn, Git, 500MB 정도의 디스크 공간이 필요합니다.



### 로컬 설치



리포지토리를 복제하고 :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### 시작 및 사용



개발 모드에서 애플리케이션을 시작합니다:



```bash
yarn start
```



브라우저에서 `http://localhost:3000`로 이동합니다. 최적화된 프로덕션 버전의 경우 :



```bash
yarn build
```



Build/`에서 생성된 파일은 nginx, Apache 또는 모든 웹 서버에서 제공할 수 있습니다. 기본적으로 Silentium는 퍼블릭 `bitcoin.silentium.dev` 서버에 연결합니다. 테스트넷 또는 자체 서버를 사용하려면 매개변수에서 이 설정을 수정하세요.



## Silentiumd 서버



### 역할 및 운영



Silentium는 **Silentiumd** 인덱싱 서버를 사용하여 결제 감지를 최적화합니다. 브라우저나 휴대폰으로 모든 Taproot 거래를 스캔하는 것은 너무 번거롭습니다.



Silentiumd는 각 Taproot 트랜잭션에 대한 중간 데이터(조정)를 미리 계산합니다. wallet는 이러한 조정 데이터(거래당 몇 바이트)를 다운로드하고 로컬에서 최종 계산을 수행하여 결제의 소유권을 확인합니다. 서버는 기존 Electrum 서버와 달리 사용자의 키를 알거나 거래를 식별할 수 없습니다.



컴팩트한 BIP158 필터를 사용하면 wallet이 주소를 노출하지 않고 스캔할 블록을 결정할 수 있으므로 기밀을 유지할 수 있습니다.



### 공용 서버



벌펨 벤처스가 후원하는 퍼블릭 서버 'bitcoin.silentium.dev'(mainnet)는 간단하고 즉각적인 경험을 제공합니다. 기밀성은 유지되지만 이 접근 방식은 타사 인프라에 대한 상대적인 신뢰를 의미합니다.



### 나만의 Silentiumd 서버 호스팅



완전한 주권을 위해 자체 Silentiumd 서버를 호스팅하세요. 전제 조건: Txindex=1` 및 `blockfilterindex=1`이 있는 Bitcoin 코어 비앵글 노드, Go 1.21 이상, 10~20GB 디스크 공간, 시스템 관리 기술.



**설치:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



환경 변수를 통해 구성합니다(자세한 내용은 리포지토리의 `config.md` 참조). 서버는 blockchain을 인덱싱하고 wallet에서 쿼리할 수 있는 API을 노출합니다.



현재 Umbrel 또는 Start9를 위한 패키지 솔루션은 존재하지 않아 기술 전문가가 아닌 사용자의 접근성이 제한됩니다.



## 장점과 한계



### 하이라이트





- 접근성 극대화**: 모든 브라우저에서 사용, 무거운 설치 필요 없음
- 멀티 플랫폼**: PWA 기술 덕분에 모바일(Android/iOS) 및 데스크톱에서 작동합니다
- 간단한 셀프 호스팅**: 몇 가지 명령어로 로컬 설치 가능
- 오픈 소스**: GitHub에서 완전히 감사 가능한 코드
- 개인 정보 보호 중심**: 추적, 분석, 로컬 암호화 계산 없음
- 별도의 아키텍처**: wallet(클라이언트)과 인덱싱 서버의 명확한 분리
- 계정 없음**: 등록 또는 개인 데이터가 필요하지 않습니다



### 고려해야 할 제약 조건





- 실험적 프로젝트**: 개념 증명용이며, 일상적인 사용이나 생산을 목적으로 하지 않습니다
- 보장 없음**: 버그, 취약성, 자금 손실 가능성 위험
- 제한된 지원**: 사용자 문서가 적고, 커뮤니티가 작으며, 공식 지원이 없습니다
- 서버 종속성**: 작동 중인 Silentiumd 서버(퍼블릭 또는 자체 호스팅)가 필요합니다
- 집중 스캔**: 자동 결제 감지는 대역폭을 소모합니다
- 기능 감소**: 코인 컨트롤 없음, 라이트닝 없음, multi-sig 네이처 없음



## 모범 사례



### seed 안전



테스트넷에서도 복구 문구를 신중하게 다루세요. 적어두었다가 안전한 곳에 보관하세요. 테스트넷용 wallet과 mainnet는 별도로 보관하세요. 실제 자금용 wallet에 테스트용 seed을 사용하지 마세요.



### 소스 코드 검증



셀프 호스팅의 장점 중 하나는 실행하기 전에 소스 코드를 확인할 수 있다는 점입니다. 실제 자금으로 Silentium을 사용할 계획이라면 시간을 내어 코드를 감사하거나 신뢰할 수 있는 개발자에게 감사를 의뢰하세요. 또한 `app.silentium.dev`에 배포된 코드의 hash와 GitHub 리포지토리의 코드를 비교하여 진위 여부를 확인하세요.



### 백업 및 복원



자동 결제 자금을 복구하려면 BIP-352 프로토콜과 호환되는 wallet이 필요합니다. 표준 wallet은 blockchain을 스캔하여 UTXO 자동 결제를 검색할 수 없습니다. 필요한 경우 Silentium를 계속 설치하거나 호환되는 다른 wallet(예: Cake Wallet 또는 기타 향후 구현)에 액세스하여 자금을 복원할 수 있는지 확인하세요.



## 결론



Silentium은 기술적 마찰 없이 자동 결제를 이해할 수 있는 접근 가능한 테스트 환경을 제공합니다. 개념 증명으로서, 이 개인정보 보호 기술이 어떻게 자기 소유권을 유지하면서 wallet 브라우저에 통합될 수 있는지 보여줍니다. 테스트넷에서 실험을 통해 on-chain 개인정보 보호를 위한 이 유망한 돌파구를 발견하세요.



## 리소스



### 공식 문서




- Silentium GitHub 리포지토리(wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub 리포지토리(서버): https://github.com/louisinger/silentiumd
- 웹 애플리케이션: https://app.silentium.dev/
- 자동 결제 커뮤니티 사이트: https://silentpayments.xyz
- 사양 BIP-352: https://bips.dev/352



### 기사 및 리소스




- 공식 발표(트위터): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin 옵텍 - 자동 결제: https://bitcoinops.org/en/topics/silent-payments/



### Testnet 도구




- Testnet 수도꼭지: https://testnet-faucet.com/
- Mempool 테스트넷 탐색기: https://mempool.space/testnet