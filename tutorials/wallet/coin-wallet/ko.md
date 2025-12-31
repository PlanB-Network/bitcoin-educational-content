---
name: Coin Wallet
description: Coin Wallet에 대한 튜토리얼 및 개인 정보 보호 및 보안 강화 방법
---

![cover](assets/cover.webp)


이 튜토리얼에서는 모바일 디바이스용 자체 보관 암호화 Coin(https://coin.space/)와 모바일 wallet 앱 사용 시 보안 및 개인정보 보호 강화 방법에 대해 설명합니다.



## Coin Wallet 정보


**Coin Wallet**은 2015년 Bitcoin 애호가들로 구성된 팀이 만든 자체 관리/비관리 오픈소스 wallet입니다. 웹 애플리케이션으로 시작하여 2017년에 iOS 앱으로, 2020년에 Android 앱으로 출시되었으며 Google Play, 삼성 갤럭시 스토어, Huawei 앱갤러리에서 이용할 수 있습니다.


주요 이점:


- 비수탁 아키텍처
- 전체 [오픈 소스 코드](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- 심플하고 깔끔한 디자인
- 불필요한 기능 없이 암호화폐를 안전하게 보관하는 핵심 목적에 집중합니다
- 크로스 플랫폼 지원: 모바일(iOS 및 Android), 데스크톱, 웹
- RBF(수수료 대체) 지원 - 중단된 트랜잭션의 속도를 언제든지 높일 수 있습니다
- 유비키](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2 키를 사용한 하드웨어 2FA
- 내장된 토르 지원 - 모든 트래픽을 토르 네트워크를 통해 라우팅하여 프라이버시를 극대화합니다



## 1️⃣ Coin Wallet 설치하기

Coin Wallet은 모든 주요 플랫폼에서 사용할 수 있습니다.



- [iOS 앱 스토어](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [안드로이드 구글 플레이](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android(갤럭시 스토어)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android(화웨이 앱갤러리)](https://appgallery.huawei.com/app/C112183767)



- [안드로이드(업다운)](https://coin-wallet.en.uptodown.com/android)



- [안드로이드 APK](https://coin.space/api/v3/download/android-apk/any)



- [모든 릴리스 링크](https://github.com/CoinSpace/CoinSpace/releases)


데스크톱(윈도우, 리눅스, 맥OS), 웹 앱, 토어를 통해서도 이용 가능합니다.


![image](assets/en/01.webp)


## 2️⃣ Wallet 생성 및 PIN 설정하기


wallet는 [2048단어 목록](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts)에서 생성된 공백으로 구분된 12개의 단어로 이루어진 무작위 시퀀스인 passphrase을 사용하여 만들어집니다.

Coin Wallet는 다른 지갑에서 가져온 12, 15, 18, 21 또는 24단어 암호를 지원합니다.


passphrase은 사람이 읽을 수 있는 형태의 마스터 개인 키입니다. 안전하게 저장해야 합니다. passphrase은 wallet에 액세스하거나 복원하는 데 필요한 모든 것입니다. passphrase을 분실하면 wallet와 모든 자금이 영구적으로 손실됩니다. passphrase은 절대 공유해서는 안 됩니다. Coin Wallet은 서버나 데이터베이스에 키를 저장하지 않습니다.


**12워드 passphrase은 안전한가요?

위치당 2048개의 가능한 단어가 있으므로 2048¹² ≈ 10³⁹의 조합이 가능하며, Bitcoin 개인 키와 비슷한 128비트 수준의 보안을 제공합니다. 이 수준이면 충분하다고 널리 알려져 있습니다.


![image](assets/en/02.webp)


passphrase을 기록하고 확인하면 앱에서 일상적인 액세스를 위해 **4자리 PIN**을 설정하라는 메시지가 표시됩니다. 편의를 위해 PIN 대신 생체 인증(지문 또는 얼굴 인식)을 활성화할 수 있습니다.


![image](assets/en/03.webp)



계정, 키 복구, passphrase 재설정, 트랜잭션 되돌리기는 제공되지 않습니다. 보안은 전적으로 사용자의 책임입니다.


니모닉 문구 저장에 대한 자세한 모범 사례를 확인하세요:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ 비밀번호 + PIN. 사용 시기 및 방법


**passphrase는 언제 필요한가요?

이렇게 드문 경우에만 해당됩니다:


- 새 기기에서 wallet 설정하기
- Coin Wallet 앱 다시 설치하기
- 앱/브라우저 데이터 지우기(로컬 저장소)
- 계정에서 하드웨어 키 제거하기
- 잘못된 비밀번호를 세 번 입력하면 보안을 위해 앱이 잠깁니다


일상적인 사용에서는 4자리 PIN으로 wallet의 잠금을 해제하는 데 충분합니다.


**비밀번호 + 비밀번호: 작동 방식**

passphrase은 진정한 마스터 개인 키이며 모든 장치에서 작동합니다.

매번 12~24개의 단어를 입력하는 것은 불편하기 때문에 Coin Wallet은 4자리 PIN을 사용하여 현재 장치에서 일상적으로 빠르게 액세스할 수 있습니다.

단순한 PIN만으로는 마스터 키를 직접 보호할 만큼 충분히 안전하지 않으므로 암호화에는 절대 사용되지 않습니다. 대신:



- PIN은 서버로 전송되어 긴 암호화 token으로 교환됩니다.
- 이 token는 장치에만 저장된 암호화된 마스터 키를 복호화합니다.


PIN을 세 번 잘못 입력하면 서버에서 token을 영구 삭제합니다. 로컬에 저장된 키는 사용할 수 없게 되며, wallet을 복구하는 유일한 방법은 원본 passphrase를 입력하는 것입니다.

이 디자인은 편리함과 강력한 폴백 보호 기능을 모두 제공합니다.



## 4️⃣ ₿잇코인 받기 - Address 유형 및 개인정보 보호


Coin Wallet은 세 가지 Bitcoin 주소 형식을 모두 지원합니다:



- 네이티브 SegWit(Bech32)** - **bc1q**로 시작 - 최저 수수료, 권장됨
- 중첩된 SegWit(P2SH)** - **3**로 시작됨
- 레거시 (P2PKH)** - **1**로 시작합니다


![image](assets/en/04.webp)


**입금할 때마다 주소가 변경되는 이유는 무엇인가요?

이는 의도적인 것이며 개인정보를 보호합니다. 코인이 수신될 때마다 Coin Wallet는 사용하지 않는 새 주소를 자동으로 생성합니다. 동일한 주소가 재사용되는 경우(예: 월급), 누구나 블록체인 탐색기에서 들어오는 모든 거래를 쉽게 합산하고 총 수입을 알 수 있습니다.


이전 주소는 영원히 유효하므로 계속 받을 수 있지만, 매번 새 주소를 사용하는 것이 개인정보 보호 모범 사례로 권장됩니다.


**Bitcoin 수령 방법:**

1. 동전 열기

2. 받기**를 탭합니다

3. 원하는 주소 유형 선택(**bc1q** - '기본 SegWit' 선호)

4. QR 코드를 보여주거나 주소를 복사하여 결제자에게 전송합니다


**선택 사항 - Mecto(대면 결제용):**

같은 수신 화면에는 '멕토' 버튼이 있습니다.

전원을 켰을 때


- 닉네임**(그라바타)을 입력하라는 메시지가 표시됩니다
- 현재 위치 + 수신 주소가 Mecto를 활성화한 다른 Coin Wallet 사용자와 일시적으로 공유됩니다
- 작은 지도에서 사용자를 검색하고 타이핑이나 스캔 없이 코인을 보낼 수 있습니다


데이터는 다른 Mecto 사용자에게만 표시되며 1시간 후(또는 전원을 끄면 즉시) 자동으로 삭제됩니다.

멕토는 완전히 선택 사항이므로 최대한의 프라이버시를 원한다면 해제하세요.


![image](assets/en/05.webp)


## 5️⃣ ₿itcoin 보내기


Bitcoin을 보내려면:


1. 코인 열기 → **보내기** 탭하기

2. 주소 붙여넣기 또는 QR코드 스캔

3. 금액 입력(또는 **최대** 탭)

4. 트랜잭션 속도를 선택합니다:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. 4자리 PIN으로 확인 → 거래가 브로드캐스트됩니다


### 보류 중인 ₿itcoin 트랜잭션 속도를 높이는 방법(RBF)


느린 수수료를 선택했는데 거래가 중단된 경우:


1. 기록** 탭으로 이동

2. 보류 중인 트랜잭션을 탭합니다

3. 가속**(유료로 교체)을 탭합니다

4. 확인 → 거래가 더 높은 수수료로 재방송됩니다


현재 RBF 가속이 지원됩니다:

Bitcoin - 눈사태 - 바이낸스 스마트 체인 - 이더리움 - 이더리움 클래식 - 폴리곤


Replace-by-fee(RBF)에 대한 자세한 정보: https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ 개인 키 내보내기


**실제로 개인 키가 필요한 경우는 언제인가요?

(99%의 사용자는 절대 사용하지 않습니다. 12단어 passphrase이면 충분합니다.)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Coin Wallet에서 개인 키를 내보내는 방법


1. 오픈 **Bitcoin (BTC)**

2. 페이지 하단으로 스크롤하여 **개인키 내보내기**를 탭합니다

3. 앱은 잔액과 **WIF** 형식(5, K 또는 L로 시작)의 개인 키가 있는 모든 주소와 QR 코드를 표시합니다.


비어 있지 않은 주소만 표시됩니다.


**WIF 키 예시**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**다음에 수행할 작업(권장 사항)**


- Electrum, Sparrow, BlueWallet 또는 모든 하드웨어 wallet 열기
- 개인 키 가져오기/스윕
- 모든 자금은 현재 seed의 새 보안 주소로 즉시 이동합니다


개인 키를 일반 텍스트로 디지털 방식으로 저장하지 마세요. 스위핑 후에는 안전하게 삭제할 수 있습니다.


개인 키 및 파생 경로에 대한 전체 가이드: [개인 키 작업 방법: 궁극의 가이드](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ 기술 세부 정보 - BIP39, BIP32 및 파생 경로


Coin Wallet은 거의 모든 진지한 지갑에서 사용하는 공식 Bitcoin 표준을 엄격하게 따릅니다.


'BIP39` - passphrase이 마스터 개인 키가 되는 방법


- 기본 단어 수입니다: 12
- 옵션 passphrase/비밀번호: 없음("")
- 초기 엔트로피: 128비트(12단어) → 256비트(24단어)
- 오픈 소스 구현: https://github.com/paulmillr/scure-bip39
- 단어 목록: 2048 단어의 표준 영어 목록
- 다른 BIP39 wallet에서 12, 15, 18, 21, 24단어 구문 가져오기 지원


`BIP32 + BIP44/BIP49/BIP84` - 모든 주소의 결정론적 생성

wallet는 하나의 마스터 키로 엄격하게 정의된 순서대로 82억 개의 주소를 generate할 수 있습니다. 그렇기 때문에 Electrum, Sparrow, 트레저, Ledger, 블루월렛 등에 동일한 12개의 단어를 입력해도 주소와 잔액이 정확히 동일하게 표시됩니다.


*gW-88에서 사용된 파생 경로 Wallet의 경우 Bitcoin****


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

각 경로 내부:


- 0` - 외부 체인(결제를 받기 위해 표시하는 주소)
- `/1` - 내부 체인(wallet가 자체적으로 사용하는 주소 변경)


Coin Wallet은 변경 없이 이러한 공개 표준을 따르기 때문에 10-20-30년 후에도 호환되는 다른 wallet에서 자금을 회수할 수 있습니다.


## 8️⃣ 토르로 익명성 강화하기


**Coin Wallet에서 Tor를 사용하는 이유**

토르는 Bitcoin 노드, 거래소, 옵저버로부터 사용자의 실제 IP 주소를 숨깁니다.

모든 트래픽(잔액, 거래, 스왑)은 직접 연결이나 IP 유출 없이 토르 네트워크를 통과합니다.

이는 앱의 소스 코드에서 직접 구현됩니다([.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31) 참조).


Coin Wallet에는 숨겨진 .onion 주소가 있으며, v6.6.3(2024년 12월)부터 **모바일 앱에 직접 토르 지원이 내장**되어 있습니다.


### Android 및 iOS에서 토르 활성화 방법


1. **오봇 설치** - 공식 토르 프로젝트 앱 (무료)


   - 안드로이드 → [구글 플레이](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - 아이폰/아이패드 → [앱스토어](https://apps.apple.com/us/app/orbot/id1609461599)


2. **오봇 열기 → 시작**을 탭합니다

목록에서 **Coin Wallet**를 선택하여 wallet만 Tor를 사용하도록 합니다(선택 사항이지만 권장)

"연결됨"**이라고 표시될 때까지 기다립니다(10~30초)


3. **Coin Wallet 열기 → 설정 → 네트워크**에서 확인하세요

토르 사용** 켜기


4. **상태 확인**

상단 표시줄에 **보라색 토르 양파 아이콘**이 나타납니다 → 이제 모든 트래픽이 토르를 통해 라우팅됩니다


![image](assets/en/06.webp)


모바일 Coin Wallet는 완전히 익명으로 처리됩니다.


프라이빗 암호화폐 관리를 즐겨보세요!


## 📝 결론


[Coin Wallet](https://coin.space/) - 10년간의 개발 역사를 가진 진정한 Bitcoin wallet의 선구자 중 하나입니다.

의도적으로 단순하며 암호화폐를 안전하게 보관하는 핵심 임무에 집중하고 있습니다.

광고, 뉴스 피드, 구독, 소셜 기능, 방해 요소가 없는 깔끔하고 빠른 자체 관리형 wallet이 본연의 기능을 정확하게 수행합니다.

Coin Wallet은 단순함과 보안을 최우선으로 생각하며 언제나 그랬고, 앞으로도 그럴 것입니다.


## 📖 리소스


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39