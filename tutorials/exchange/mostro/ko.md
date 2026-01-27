---
name: Mostro
description: 라이트닝과 노스트르를 통한 KYC-free Bitcoin P2P 교환 플랫폼
---

![cover](assets/cover.webp)



금융 주권을 침해하지 않고 어떻게 비트코인을 구매하거나 판매할 수 있을까요? 중앙화된 플랫폼은 사용자의 개인 데이터를 노출하는 침습적인 KYC 절차를 시행하며, 임의적인 계정 동결이나 국가 감시의 가능성이 있습니다.



**모스트로 P2P**는 Lightning Network, 노스트르 프로토콜, 홀드 인보이스를 결합한 탈중앙화 대안을 제공합니다. 주요 혁신은 자동화된 에스크로 시스템으로, 거래소에서 비트코인을 계속 관리할 수 있어 도난, 거래소 파산 또는 임의 몰수 위험을 제거합니다.



## 모스트로 P2P란 무엇인가요?



모스트로 P2P는 2021년에 출시된 인기 텔레그램 봇 **lnp2pbot**의 개발자인 **grunch**가 만든 오픈 소스 Bitcoin 교환 프로토콜입니다. Lnp2pbot은 이미 라이트닝을 통해 KYC가 필요 없는 P2P 교환을 가능하게 했지만, 큰 취약점을 가지고 있었습니다: **텔레그램은 정부의 검열에 취약한 중앙 집중식 장애 지점**을 구성한다는 것입니다.



모스트로는 이러한 개념의 **탈중앙화된 진화**를 나타냅니다: 모스트로는 텔레그램을 **Nostr** 프로토콜(검열 불가능한 분산 릴레이 네트워크)로 대체함으로써, 이러한 시스템적 위험을 제거합니다. 이 프로토콜은 즉각적인 거래를 위한 Lightning Network, 검열에 강한 통신을 위한 노스트르, 그리고 **보류 송장**을 결합하여 진정한 비수탁 자동 에스크로를 생성합니다.



### 기술 아키텍처



Mostro는 세 가지 구성 요소를 통해 작동합니다:




- 데몬 모스트로드**: 사용자와 Lightning Network 간의 교환을 조정합니다
- 라이트닝** 노드: 보류 인보이스 생성(~24시간 암호화 에스크로)
- Mostro** 고객: 사용자 인터페이스(CLI, 모바일, 웹)



주문은 공개 이벤트(유형 38383)로 노스트러에 게시되며, 비공개 거래는 종단간 암호화 메시지(NIP-59, NIP-44)를 통해 전송됩니다. 각 모스트로 인스턴스는 자체 수수료(일반적으로 0.3%에서 1% 사이)와 거래 한도(인스턴스에 따라 수천에서 수십만 sats 범위)를 정의합니다.



### 결정적인 이점



**검열 저항성**: 노스트르 릴레이가 전 세계 어딘가에 존재하는 한, 어떤 정부도 모스트로를 폐쇄할 수 없습니다. 취약한 텔레그램을 통한 lnp2pbot과 달리, 모스트로는 **검열 방지**가 가능한 교환을 허용합니다.



**에스크로 비수탁**: 라이트닝 홀드 인보이스는 비트코인을 영구적으로 전송하지 않고 잠급니다. 자금은 회원님의 통제 하에 있으며 문제가 발생하면 자동으로 반환됩니다(최대 24시간).



**설계상 기밀 유지**: 필요에 따라 두 가지 모드를 사용할 수 있습니다. 평판 모드**는 사용자의 평판을 노스트르 키에 연결하여 지속적인 신뢰를 구축합니다. 완전 비공개 모드**는 일회용 임시 키로 완전한 익명성을 보장합니다.



## 주요 기능



**탈중앙화된 커뮤니케이션**: 모든 주문은 암호화된 서명 이벤트를 통해 노스트르에 게시됩니다. 비공개 협상은 종단 간 암호화된 메시지를 통해 전송되어 절대적인 기밀성을 보장합니다.



**평판 시스템**: 노스트르에 영구적으로 저장되는 반복 계산을 통한 별 5개 등급. 신뢰할 수 있는 트레이더로서의 평판을 점진적으로 쌓을 수 있습니다.



**분산형 중재**: 분쟁이 발생하면 공정한 중재자가 증거를 검토하고 투명한 기준에 따라 결정을 내립니다. 각 분쟁은 추적을 위해 고유한 token을 생성합니다.



**결제 유연성**: Yadio.io 환율 서비스를 통해 다양한 법정화폐를 지원합니다. SEPA 송금, PayPal, Revolut, 현금 및 당사자 간에 합의된 모든 방법을 허용합니다.



## Mostro 고객 사용 가능



모스트로는 P2P 거래소를 위한 두 가지 주요 운영 클라이언트를 제공합니다.



### Mostro CLI - 명령줄 클라이언트



모스트로 CLI**는 가장 성숙하고 기능적인 클라이언트입니다. Rust로 작성된 이 제품은 명령줄 인터페이스를 통해 모스트로의 모든 기능을 제공합니다. MacOS, Linux 및 Windows와 호환됩니다.



**주요 컨트롤** :




- `목록 주문`: 사용 가능한 모든 주문 표시
- `새 주문` : 새 매수 또는 매도 주문 생성
- 테이크셀`/`테이크바이`: 매수 또는 매도 주문 받기
- '피아트': 법정화폐 결제 전송 확인
- '해제'를 클릭합니다: 에스크로를 해제하고 교환을 완료합니다
- `getdm`: 쪽지 보기
- `rate` : 교환 후 상대방을 평가합니다



기술 사용자, 자동화 및 최대한의 안전이 요구되는 환경에 이상적입니다.



### Mostro Mobile - 스마트폰 애플리케이션



알파 버전의 **모바일 앱**을 사용하면 스마트폰에서 직접 P2P 거래를 할 수 있습니다. 탭 탐색, 주문 보기, 고급 필터, 거래 상대방과 소통할 수 있는 통합 채팅 기능을 갖춘 직관적인 그래픽 Interface입니다.



안드로이드**에서 사용 가능(GitHub의 APK를 통해)하며, 간편함과 가끔씩 모바일 거래를 선호하는 사용자에게 최적의 선택입니다.



### Mostro-web - Interface 웹(개발 중)



Interface 고급 자바스크립트 웹 애플리케이션이 활발히 개발 중입니다. 광범위한 트레이딩 및 포트폴리오 관리 기능으로 완벽한 사용자 경험을 제공하도록 설계되었습니다. 설치 없이 브라우저를 통해 액세스할 수 있습니다.



## 설치 및 구성



이 튜토리얼에서는 두 가지 주요 모스트로 클라이언트의 설치 및 사용 방법을 안내합니다: CLI과 모바일 애플리케이션입니다.



### 필수 전제 조건



시작하기 전에 다음이 필요합니다:





- 충분한 유동성을 갖춘 작동 중인 Lightning Network** wallet(또는 라이트닝 호환)
 - 추천합니다: 추천: Phoenix, 브리즈, Wallet의 Satoshi...
 - 테스트할 최소 1000사토시의 유동성



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Nostr** 개인 키(형식 `nsec1...`)
 - Nostrkeygen.com](https://nostrkeygen.com/)에서 전용 거래 키를 생성합니다
 - 중요**: 기본 개인 Nostr 키를 사용하지 마세요
 - 개인 키를 안전한 곳에 보관하세요(비밀번호 관리자)





- 선택 사항이지만 권장**: IP 주소 마스킹을 위한 VPN 또는 토르 연결



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI 설치



#### MacOS에서



**1단계: Rust 확인**



Rust이 설치되어 있는지 확인합니다(버전 1.64 이상 필요):



```bash
rustc --version
```



Rust가 설치되지 않은 경우 :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**2단계: 리포지토리 복제**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**3단계: 구성**



를 복사하여 편집합니다:



```bash
cp .env-sample .env
```



.env`를 열고 설정을 구성합니다:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**CLI/모바일** 동기화에 중요합니다: CLI과 모바일 앱에서 동일한 주문에 액세스하려면 두 클라이언트에서 **동일한 모스트로 펍키**와 **동일한 노스트르 릴레이**를 사용해야 합니다. 모바일 앱의 설정에서 이러한 설정을 확인하세요.



![Configuration .env](assets/fr/02.webp)



**4단계: 설치**



CLI을 컴파일하고 설치합니다:



```bash
cargo install --path .
```



컴파일에는 1~2분이 소요됩니다. Mostro-cli` 실행 파일은 `~/.cargo/bin/`에 설치됩니다.



![Installation du CLI](assets/fr/03.webp)



**5단계: 확인**



모든 것이 작동하는지 확인합니다:



```bash
mostro-cli --help
```



전체 주문 목록이 표시됩니다.



![Vérification avec --help](assets/fr/04.webp)



#### Linux(우분투/데비안)에서



를 추가하여 macOS와 동일하게 설치합니다:



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



그런 다음 macOS 섹션의 3단계와 4단계를 따릅니다.



#### Windows에서



먼저 [rustup.rs](https://rustup.rs/)를 통해 Rust를 설치한 다음 PowerShell 을 사용합니다:



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



동일한 구성: '.env-sample'을 '.env'에 복사하고 매개변수를 입력합니다.



### Mostro Mobile 설치



#### Android에서



**1단계**: GitHub 릴리스 페이지](https://github.com/MostroP2P/mobile/releases)로 이동하여 **app-release.apk** 파일(약 65MB)을 다운로드합니다.



![Page GitHub Releases](assets/fr/10.webp)



**2단계: 다운로드가 완료되면 다운로드에서 APK 파일을 엽니다. Android에서 이 소스에서 설치를 승인하라는 메시지가 표시됩니다.



![Téléchargement et installation APK](assets/fr/11.webp)



**3단계**: 기능을 소개하는 온보딩 화면을 따릅니다:




- Bitcoin을 자유롭게 거래하세요 - KYC** 없이** : 노스트라와 함께 신원 확인 없이 거래하세요
- 기본적으로 개인정보 보호**: 평판 모드와 전체 개인정보 보호 모드 중에서 선택
- 모든 단계의 보안**: 비보관 보류 송장을 통한 보호



![Écrans d'accueil Mostro](assets/fr/12.webp)



**4단계**: 온보딩을 계속 진행하여 :




- 완전 암호화된 채팅**: 엔드투엔드 암호화 통신
- 오퍼 받기**: 주문서를 검색하고 오퍼를 선택합니다
- 필요한 것을 찾을 수 없나요? 나만의 맞춤 주문 만들기



![Suite onboarding](assets/fr/13.webp)



**5단계: 온보딩이 완료되면 앱에서 자동으로 Nostr 키 쌍을 생성합니다. 메뉴(☰)로 이동한 다음 **계정**으로 이동하여 **비밀어**(복구 문구)를 저장합니다. 또한 이 화면에서 앞서 언급한 개인정보 보호 모드를 변경할 수 있는 옵션이 있습니다.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**중요**: 안전한 장소(비밀번호 관리자, 종이 금고)에 복구 문구를 적어 두세요.



### 초기 보안 구성



어떤 플랫폼을 사용하든 :





- 전용 키**: 거래 시 별도의 노스트르 신원 사용
- 소액**: 시작하려면 sats 10,000 미만으로 시작하세요
- 다중 릴레이**: 지리적으로 다양한 3~5개의 릴레이 구성
- 네트워크 보호**: VPN 또는 Tor를 활성화하여 IP 주소 숨기기
- Wallet 보안**: wallet Lightning의 자동 잠금 활성화



## CLI과 함께 사용



이 섹션에서는 실제 사용 사례를 통해 모스트로 CLI을 통해 비트코인을 구매하는 방법을 보여드리겠습니다.



### 1단계: 사용 가능한 주문 목록



목록 주문` 명령은 모든 활성 주문을 표시합니다:



```bash
mostro-cli listorders
```



각 주문의 세부 정보가 포함된 표가 표시됩니다: ID, 유형(구매/판매), 금액, 통화, 결제 방법.



![Liste des ordres disponibles](assets/fr/05.webp)



이 예시에서는 Revolut을 통해 5 EUR를 매도하는 주문이 표시됩니다(ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### 2단계: 주문 받기



이 비트코인을 구매하려면 `takesell`로 주문하세요:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



모스트로는 BTC를 받기 위해 **라이트닝 인보이스**를 제공하도록 요청할 것입니다. 정확한 금액은 사토시 단위로 표시됩니다(예: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### 3단계: Lightning 인보이스 제공



wallet(Phoenix, Breez 등)에서 정확한 금액에 대한 Lightning 인보이스를 생성한 다음 전송합니다:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



시스템에서 배송을 확인하고 에스크로를 활성화하기 전에 판매자가 보류 송장을 결제할 때까지 기다리라고 알려줍니다.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### 4단계: 판매자에게 문의



에스크로가 활성화되면 `dmtouser`를 사용하여 판매자에게 결제 세부 정보를 요청합니다:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### 5단계: 답변 검색



쪽지를 확인하여 판매자의 응답을 확인하세요:



```bash
mostro-cli getdm
```



판매자가 결제 ID(여기서는 Revtag: `@satoshi`)를 알려줍니다.



![Réception de la réponse](assets/fr/09.webp)



### 6단계: 법정 화폐 결제하기



동의한 방법(이 예에서는 Revolut)을 통해 제공된 연락처 정보로 대금을 송금합니다. **모든 증빙 서류**(스크린샷, 거래 참조)를 보관합니다.



### 7단계: 결제 발송 확인



결제가 완료되면 모스트로에 알려주세요:



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### 8단계: 비트코인 수령



판매자가 법정화폐 수령을 확인하고 '릴리스' 명령으로 에스크로를 해제하는 즉시 제공한 라이트닝 인보이스로 비트코인을 즉시 수령할 수 있습니다.



### 9단계: 평가



판매자를 평가하여 탈중앙화된 평판에 기여하세요:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### 유용한 명령어



**주문 취소하기** (주문이 접수되기 전) :


```bash
mostro-cli cancel -o <order-id>
```



**새 판매 주문 생성** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**분쟁 열기** :


```bash
mostro-cli dispute -o <order-id>
```



## 모바일 애플리케이션과 함께 사용



이 섹션에서는 실제 사용 사례를 통해 모스트로 모바일을 통한 비트코인 판매에 대해 설명합니다.



### Interface 메인



애플리케이션에는 3개의 기본 탭이 있습니다:





- 주문서**: 사용 가능한 매수(BTC 매수) 및 매도(BTC 매도) 주문 찾아보기
- 내 트레이딩**: 활성 및 과거 주문 보기
- 채팅**: 수치를 사용하여 상대방과 소통하세요



![Interface principale](assets/fr/14.webp)



### 권장 구성



거래하기 전에 메뉴(☰) > **설정**을 통해 몇 가지 설정을 구성하세요:





- Lightning Address**(선택 사항): 결제를 직접 받으려면
- 릴레이**: 복원력을 위해 여러 노스트르 릴레이를 추가합니다(예: `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: 사용 중인 모스트로 인스턴스의 공개키를 확인하세요



![Paramètres de l'application](assets/fr/16.webp)



*gW-45/모바일 동기화**에 중요**: CLI와 모바일 앱을 모두 사용하는 경우 두 클라이언트에서 **정확하게 동일한 Nostr 릴레이와 Mostro Pubkey**를 구성하세요. 이렇게 동일하게 구성하지 않으면 두 인터페이스에서 동일한 주문이 표시되지 않습니다. 설정(위 스크린샷)에 표시되는 릴레이와 모스트로 펍키가 CLI `.env' 파일에 있는 것과 일치해야 합니다.



### 1단계: 판매 주문 만들기



오른쪽 하단의 녹색 **"+"** 버튼을 누른 다음 **판매**(빨간색 버튼)를 선택합니다.



![Boutons de création d'ordre](assets/fr/17.webp)



생성 양식을 작성합니다 :



1. **통화**: 받고자 하는 통화(EUR, USD 등)를 선택합니다


2. **금액** : 금액을 법정 화폐 단위로 입력합니다(예: 1~3유로)


3. **결제 방법** : 방법 선택(예: "Revolut")


4. **가격 유형**: "시장 가격"을 선택합니다


5. **프리미엄**: 프리미엄 조정(-10%에서 +10%까지 슬라이더, 빠른 판매를 위해 0% 권장)



제출**을 눌러 주문을 게시합니다.



### 2단계: 게시 확인



주문이 게시되었습니다! 24시간 동안 사용할 수 있습니다. 구매자가 상품을 수령하기 전에 언제든지 `취소` 명령을 실행하여 취소할 수 있습니다.



![Ordre publié](assets/fr/18.webp)



주문은 **내 거래** 탭에 "보류 중" 상태와 "내가 만든" 배지와 함께 표시됩니다.



### 3단계: 구매자가 주문을 받습니다



구매자가 주문을 받으면 알림을 받게 됩니다. 자세한 내용은 **내 거래**에서 확인하세요.



![Ordre pris par un acheteur](assets/fr/19.webp)



**중요 지침**: 이제 표시된 보류 청구서를 **결제**하여 에스크로에 비트코인(여기서는 4674 sats, 1~5유로)을 잠궈야 합니다. 최대 **15분**의 시간이 주어지며 그렇지 않으면 거래가 취소됩니다.



보류 인보이스를 복사하여 wallet Lightning(Phoenix, Breez 등)에서 결제하세요.



### 4단계: 구매자와 커뮤니케이션



에스크로가 활성화되면 **CONTACT**를 눌러 구매자와 암호화된 채팅을 엽니다.



구매자(여기서는 "익명 글로리아 자오")가 결제 세부 정보를 요청하기 위해 연락을 드릴 것입니다. 세부 정보(Revtag, IBAN 등)를 회신해 주세요.



![Chat avec l'acheteur](assets/fr/20.webp)



### 5단계: 법정 화폐 결제 수령



Revolut 계정(또는 기타 합의된 방법)으로 법정화폐 결제를 받을 때까지 기다리세요. **주의 깊게 확인하세요**:




- 정확한 금액
- 발신자
- 요청 시 참조



구매자가 채팅을 통해 결제금을 송금했음을 알려줄 것입니다. 모스트로는 법정화폐가 전송되었음을 확인하는 메시지도 표시합니다.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### 6단계: 에스크로 해제



계정에서 법정 화폐 결제의 **수령 확인**이 완료되면 녹색 **해제** 버튼을 누르고 구매자에게 사츠 전송을 확인합니다.



![Libération de l'escrow](assets/fr/20.webp)



비트코인은 라이트닝 인보이스를 통해 구매자에게 즉시 전송됩니다.



### 7단계: 고려 사항 평가



출시 후 **평가**를 눌러 구매자를 평가합니다. 별 1개에서 5개(여기서는 5/5)를 선택하고 **평점 제출**을 누릅니다.



![Évaluation de la contrepartie](assets/fr/21.webp)



교환이 끝났습니다!



### 모바일 앱으로 비트코인 구매



비트코인을 **구매**하는 과정은 비슷하지만 그 반대입니다:



1. 주문서** > **BUY BTC** 탭으로 이동하여 판매 주문을 확인합니다


2. 흥미로운 주문을 클릭하면 세부 정보를 볼 수 있습니다


3. 주문하기**를 누릅니다


4. Lightning 인보이스 제공(wallet에서 생성)


5. 판매자가 에스크로를 활성화할 때까지 기다립니다


6. 결제 세부 정보는 **CONTACT**를 통해 판매자에게 문의하세요


7. 법정 화폐 결제 보내기(증거 보관)


8. 판매자는 확인 후 에스크로를 해제합니다


9. 라이트닝 인보이스로 비트코인을 즉시 수령하세요


10. 판매자 평가하기(별 1~5개)



### 문제 관리



**주문 취소**: 내 트레이딩**에서 주문을 누른 다음 **취소** 버튼을 누릅니다(주문이 체결되기 전에만 사용 가능).



*분쟁을 **개시**합니다: 분쟁이 발생하면 주문 세부정보에서 **분쟁 제기**를 누릅니다. 모든 증거(채팅 스크린샷, 은행 거래 참조)를 첨부하세요.



## 장점과 한계



### 혜택



**금융 주권**: 보류 송장 메커니즘 덕분에 비트코인이 직접 통제를 벗어나지 않으므로 거래소 파산이나 불법 복제의 위험이 없습니다.



**검열 방지**: 어떤 기관도 네트워크를 종료하거나 주문을 검열할 수 없습니다. 이 시스템은 노스트르 릴레이가 작동하는 한 작동합니다.



**기본 익명성**: KYC나 개인 데이터 없이 익명의 Nostr 키만으로 사용자를 식별합니다. 엔드투엔드 암호화 통신.



**결제 유연성**: 상호 허용되는 모든 결제 수단(이체, 모바일 앱, 현금, 물물교환)을 사용할 수 있습니다.



### 제한 사항



**초기 개발 단계**: 초보적인 인터페이스와 기술 학습 곡선이 필요합니다.



**유동성 제한**: 특히 대량 주문이나 희귀 통화의 경우 주문 수량이 제한됩니다.



**기술 요구 사항**: Lightning 및 Nostr에 대한 기본적인 이해가 필요합니다.



**개인 책임**: 문제 발생 시 중앙에서 지원하지 않으므로 주의가 필요합니다.



## 결론



모스트로 P2P은 진정한 탈중앙화 거래를 위해 Lightning Network, 노스트라와 자동화된 에스크로를 결합한 중앙화된 거래소의 유망한 대안입니다. 개발 초기이고 유동성이 제한적이지만, 이 플랫폼은 이미 금융 주권, 검열 저항성, 기본 익명성을 제공합니다.



자율성과 기밀성을 선호하는 비트코인 사용자라면 모스트로는 점진적으로 탐색해볼 만한 가치가 있는 옵션입니다. 모스트로의 탈중앙화 아키텍처는 상업적 진화보다는 커뮤니티를 보장하며, 진정한 무료 Bitcoin 거래소의 미래를 위한 길을 열어줍니다.



## 리소스



### 공식 문서




- [모스트로 공식 웹사이트](https://mostro.network)
- [기술 문서](https://mostro.network/docs-english/index.html)
- [모스트로 재단](https://mostro.foundation)



### 소스 코드 및 개발




- [메인 GitHub 리포지토리](https://github.com/MostroP2P/mostro)
- [웹 클라이언트](https://github.com/MostroP2P/mostro-web)
- [고객 CLI](https://github.com/MostroP2P/mostro-cli)



### 커뮤니티




- [노스트르 프로토콜](https://nostr.com)
- [Lightning Network 가이드](https://lightning.network)