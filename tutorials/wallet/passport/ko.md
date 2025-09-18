---
name: Passport Core
description: 수동 모드에서 Passport Hardware Wallet 구성 및 사용하기
---
![cover](assets/cover.webp)


패스포트는 2020년 4월 보스턴에 설립된 미국 회사 파운데이션 디바이스(Foundation Devices)가 설계한 Bitcoin 전용 Hardware Wallet입니다.


이 튜토리얼에서 소개하는 패스포트 "*배치 2*"는 "*파운더스 에디션*"의 후속 제품입니다. 프리미엄 디자인, 고화질 컬러 화면, 인체공학적 물리적 키보드가 돋보이는 제품입니다. "*에어 갭*" 모드로 작동하여 Wallet의 개인 키가 완전히 격리된 상태로 유지되며, MicroSD 카드 또는 QR 코드를 통해 통신할 수 있습니다. 이 디바이스에는 1200mAh 용량의 탈착식 충전식 Nokia BL-5C 배터리가 장착되어 있습니다. 이 비독점 배터리는 BL-5C 모델이 시중에서 널리 판매되므로 쉽게 교체할 수 있습니다.


업데이트:** 2025년 3월부터 이 Hardware Wallet의 이름은 더 이상 "Passport" 또는 "Passport V2"가 아닌 "Passport Core"로 변경됩니다.


연결성과 관련하여 Passport에는 MicroSD 포트, 충전용 USB-C 포트, QR 코드 스캔을 위한 후면 카메라가 장착되어 있습니다.


보안 측면에서 Passport는 secure element를 통합하고 있으며, 기기의 소스 코드는 완전히 오픈 소스입니다. 우수한 Bitcoin Hardware Wallet에서 기대할 수 있는 모든 기능을 제공합니다. Passport는 아직 미니스크립트를 지원하지 않지만, 이 기능은 2025년 2분기에 지원될 예정입니다.


199달러로 책정된 Passport는 고급형 Hardware Wallet로, Coldcard Q, Jade Plus, Tezor Safe 5 및 Ledger의 최상급 모델과 경쟁합니다.


![Image](assets/fr/01.webp)


패스포트에서 보안 Wallet를 관리하려면 몇 가지 옵션이 있습니다. 이 Hardware Wallet은 Sparrow wallet, 스펙터 데스크톱, 쌍절곤, 키퍼 등 시중에 나와 있는 대부분의 Wallet 관리 소프트웨어와 호환됩니다. 이 튜토리얼에서는 Sparrow wallet과 함께 사용하는 방법을 알아보겠습니다.


초보자라면 가장 쉬운 방법은 재단에서 개발한 기본 Envoy 애플리케이션과 함께 Passport를 사용하는 것입니다. Passport에서 Envoy를 사용하는 방법을 알아보려면 이 다른 튜토리얼 을 확인하세요:


https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## 패스포트 개봉하기


Passport를 받으면 상자와 상자의 Seal이 손상되지 않았는지 확인하여 포장이 개봉되지 않았는지 확인하세요. 장치를 설정할 때 장치의 진위 여부와 무결성에 대한 소프트웨어 검증도 수행됩니다.


![Image](assets/fr/02.webp)


상자 내용물은 다음과 같습니다:




- 여권;
- Mnemonic 문구를 적을 카드보드 한 장;
- 충전용 USB-C 케이블 ;
- MicroSD 카드 ;
- MicroSD - Lightning 또는 USB-C 어댑터 2개 ;
- 스티커.


장치에서 찾을 수 있습니다:




- 키보드(1) ;
- USB-C 포트(2);
- 삭제 버튼(3);
- 돌아가기 버튼(4) ;
- 확인 버튼(5);
- 방향 패드(6);
- 켜기/끄기 버튼(7);
- 상태 표시기(8);
- MicroSD 포트(9) ;
- 모드 변경 버튼 aA1 (10) ;
- 후면 카메라.


![Image](assets/fr/03.webp)


## 패스포트 시작


장치 측면의 켜기/끄기 버튼을 눌러 전원을 켭니다.


![Image](assets/fr/04.webp)


확인 버튼을 눌러 다음 메뉴에 액세스합니다.


![Image](assets/fr/05.webp)


이 튜토리얼에서는 Sparrow wallet를 사용하여 패스포트 보안이 설정된 Wallet을 관리하겠습니다. "*수동 설정*"을 선택합니다.


![Image](assets/fr/06.webp)


그런 다음 이용 약관에 동의합니다.


![Image](assets/fr/07.webp)


다음 단계는 기기를 확인하는 것입니다. 이를 통해 여권의 진위 여부를 확인하고 운송 중에 여권이 변조되지 않았는지 확인할 수 있습니다. QR 코드를 스캔하라는 메시지가 표시됩니다.


![Image](assets/fr/08.webp)


공식 인증 사이트](https://validate.foundationdevices.com/)로 이동하여 "*여권*"을 선택합니다.


![Image](assets/fr/09.webp)


Passport의 카메라를 사용하여 사이트에 표시된 QR 코드를 스캔합니다.


![Image](assets/fr/10.webp)


그러면 기기에 4개의 단어가 표시됩니다.


![Image](assets/fr/11.webp)


웹사이트에 이 단어를 입력하여 여권의 진위 여부를 확인한 후 "*확인*"을 클릭합니다.


![Image](assets/fr/12.webp)


"*합격*" 메시지가 표시되면 Hardware Wallet이 정품입니다. 이제 Bitcoin Wallet를 보호하는 데 사용할 수 있습니다.


![Image](assets/fr/13.webp)


여권에서 테스트 결과를 확인합니다.


![Image](assets/fr/14.webp)


## PIN 코드 설정


다음은 PIN 코드 단계입니다. PIN 코드는 여권의 잠금을 해제합니다. 따라서 무단 물리적 액세스로부터 보호할 수 있습니다. PIN 코드는 Wallet의 암호화 키를 생성하는 데 관여하지 않습니다. 따라서 PIN 코드에 액세스할 수 없더라도 12단어 또는 24단어 Mnemonic 문구를 소지하고 있으면 비트코인에 다시 액세스할 수 있습니다.


![Image](assets/fr/15.webp)


가능한 한 무작위로 PIN 코드를 선택하는 것이 좋습니다. 또한 이 코드는 비밀번호 관리자 등 여권이 저장된 곳과 다른 곳에 저장하세요.


6자리에서 12자리 사이의 PIN 코드를 선택할 수 있습니다. 가능한 한 길게 설정하는 것이 좋습니다.


키패드를 사용하여 PIN 번호를 입력합니다. 입력이 완료되면 확인 버튼을 클릭합니다.


![Image](assets/fr/16.webp)


비밀번호를 다시 한 번 확인합니다.


![Image](assets/fr/17.webp)


PIN 코드가 등록되었습니다.


![Image](assets/fr/18.webp)


## Passport 펌웨어 업데이트


Hardware Wallet에서 펌웨어를 업데이트할 것을 제안합니다. 최신 버전이 제공하는 개선 사항과 수정 사항을 활용하려면 즉시 업데이트하는 것이 좋습니다. 계속하려면 오른쪽의 확인 버튼을 클릭하세요.


![Image](assets/fr/19.webp)


Passport는 MicroSD 카드를 통해 새 펌웨어를 받을 준비가 되었습니다.


![Image](assets/fr/20.webp)


이렇게 하려면 Passport 박스(또는 다른 박스)에 들어 있는 MicroSD 카드를 컴퓨터에 삽입하세요. 재단 문서 사이트](https://docs.foundation.xyz/firmware-updates/passport/) 또는 [해당 GitHub 리포지토리](https://github.com/Foundation-Devices/passport2/releases)에서 최신 펌웨어 버전을 다운로드합니다.


![Image](assets/fr/21.webp)


장치에 설치하기 전에 다운로드한 펌웨어의 진위 여부와 무결성을 확인하는 것이 좋습니다. 이에 대한 도움이 필요하면 이 튜토리얼 을 참조하세요:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

.bin` 파일을 확인한 후 MicroSD에 넣은 다음 Passport에 삽입합니다. Passport 파일 탐색기가 열립니다. 파일 `vN.N.N-passport.bin`을 선택합니다.


![Image](assets/fr/22.webp)


"*선택*"을 클릭합니다.


![Image](assets/fr/23.webp)


그런 다음 펌웨어 설치를 확인합니다.


![Image](assets/fr/24.webp)


업데이트가 완료될 때까지 기다려주세요.


![Image](assets/fr/25.webp)


업데이트가 완료되면 PIN 코드를 입력하여 디바이스의 잠금을 해제하고 구성을 계속합니다.


![Image](assets/fr/26.webp)


## 새 Bitcoin Wallet 만들기


이제 새로운 Bitcoin Wallet을 만들 차례입니다. 확인 버튼을 클릭합니다.


![Image](assets/fr/27.webp)


새 Wallet을 만들려면 "*새 seed 만들기*"를 클릭합니다.


![Image](assets/fr/28.webp)


12단어 또는 24단어 Mnemonic 문구 중에서 선택할 수 있습니다. 두 옵션이 제공하는 보안 수준은 비슷하므로 저장하기 쉬운 12단어 중 하나를 선택하면 됩니다.


![Image](assets/fr/29.webp)


"*계속*"을 클릭합니다.


![Image](assets/fr/30.webp)


이제 패스포트에 "*백업 코드*"가 generate로 표시됩니다. 이는 MicroSD에 저장된 Wallet의 백업을 해독하는 데 사용할 수 있는 일련의 숫자입니다. 이 백업 시스템은 Foundation 장치 전용으로, Mnemonic 문구에 대한 추가 백업을 구성하지만 다른 Bitcoin 소프트웨어와 호환되지 않습니다.


이 "*백업 코드*"를 사용하기로 결정한 경우, Wallet의 암호화된 백업이 들어 있는 MicroSD와는 다른 위치에 보관해야 합니다. 그러나 Mnemonic 문구의 충분한 백업으로 충분하다고 생각되면 이 시스템을 사용하지 않을 수도 있습니다.


![Image](assets/fr/31.webp)


"*백업 코드*"를 입력하여 올바르게 저장했는지 확인합니다.


![Image](assets/fr/32.webp)


MicroSD를 삽입한 경우 Wallet의 암호화된 백업이 여기에 저장됩니다.


![Image](assets/fr/33.webp)


패스포트에 12단어 Mnemonic 문구가 표시됩니다. 이 Mnemonic은 모든 비트코인에 대한 완전한 무제한 액세스를 제공합니다. 이 문구를 소유한 사람은 누구든 내 여권에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다.


이 12단어 문구는 여권 분실, 도난 또는 파손 시 비트코인에 대한 액세스를 복원합니다. 따라서 신중하게 저장하고 안전한 장소에 보관하는 것이 매우 중요합니다.


상자에 동봉된 판지에 적거나, 화재, 홍수 또는 붕괴로부터 보호하기 위해 스테인리스 스틸 베이스에 각인하여 보안을 강화하는 것이 좋습니다.


확인 버튼을 클릭하면 Mnemonic 문구를 확인할 수 있습니다.


![Image](assets/fr/34.webp)


Mnemonic 문구를 저장하고 관리하는 올바른 방법에 대한 자세한 내용은 특히 초보자라면 이 다른 튜토리얼을 따르는 것이 좋습니다:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

물론 이 튜토리얼에서 하는 것처럼 인터넷에서 이러한 단어를 공유해서는 안 됩니다. 이 샘플 Wallet은 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다.


이 문장을 물리적으로 백업하세요.


![Image](assets/fr/35.webp)


Passport가 성공적으로 구성되었습니다. 계속하려면 확인 버튼을 클릭합니다.


![Image](assets/fr/36.webp)


## 메뉴 검색


Passport Interface에는 세 가지 주요 메뉴가 있습니다:




- "*계정*";
- "*더 보기*";
- "*설정*".


이러한 메뉴 사이를 탐색하려면 방향 패드의 왼쪽 및 오른쪽 화살표를 사용합니다.


### *계정*" 메뉴


"*계정*" 메뉴에서 Bitcoin Wallet의 주요 기능을 확인할 수 있습니다. 카메라 또는 MicroSD 포트를 통해 거래에 서명할 수 있습니다.


![Image](assets/fr/37.webp)


"*계정 도구*" 하위 메뉴에서는 Address 확인, 메시지 서명 또는 Wallet의 주소 조회 등의 옵션을 제공합니다.


![Image](assets/fr/38.webp)


"*계정 관리*" 하위 메뉴에서 Bitcoin Wallet을 Wallet 관리 소프트웨어(이 튜토리얼의 다음 단계에서 다룰 예정)에 연결하거나 계정을 보고 이름을 변경할 수 있습니다.


![Image](assets/fr/39.webp)


### 더보기" 메뉴


"*더보기*" 메뉴에서 동일한 Mnemonic 문구에 연결된 Wallet에서 새 계정을 만들 수 있습니다.


![Image](assets/fr/40.webp)


BIP39 passphrase을 입력하거나(다음 섹션 참조) 임시 seed를 사용할 수도 있습니다.


![Image](assets/fr/41.webp)


### 설정" 메뉴


"*설정*" 메뉴에서 모든 Wallet 및 기기 설정을 확인할 수 있습니다.


![Image](assets/fr/42.webp)


'*장치*' 하위 메뉴에서는 화면 밝기 사용자 지정, 자동 잠금 전 지연 시간 설정, 비밀번호 변경 또는 장치 이름 변경 등의 옵션을 사용할 수 있습니다.


![Image](assets/fr/43.webp)


"*백업*" 하위 메뉴에서는 암호화된 Wallet 백업을 내보내거나 기존 백업의 유효성을 확인하거나 "*백업 코드*"를 다시 조회할 수 있습니다.


![Image](assets/fr/44.webp)


"*펌웨어*" 하위 메뉴는 Passport의 펌웨어를 업데이트하는 데 사용됩니다. 최신 수정 사항과 기능을 활용하려면 정기적으로 업데이트를 수행하는 것이 좋습니다.


![Image](assets/fr/45.webp)


"*Bitcoin*" 하위 메뉴에서는 표시되는 단위(BTC 또는 사토시)를 변경하거나, 가능한 Multisig Wallet을 관리하거나, "*Testnet*" 모드로 전환할 수 있습니다.


![Image](assets/fr/46.webp)


"*고급*"에서는 이전에 수행한 것처럼 Mnemonic 문구의 단어를 보거나, 삽입된 MicroSD에 대한 작업을 수행하거나, Passport를 공장 설정으로 초기화하거나, 진위 여부를 확인할 수 있습니다.


![Image](assets/fr/47.webp)


PIN 코드의 첫 네 자리를 입력한 후 장치를 잠금 해제할 때 특정 단어 두 개를 표시하여 보안을 강화하는 기능인 '*보안 단어*'를 활성화할 수 있습니다. 이 단어는 설정 중에 저장되어 패스포트가 교체되거나 변조되지 않았는지 확인할 수 있습니다. 나중에 불일치하는 경우 장치를 사용하지 않는 것이 좋습니다. 기기의 물리적 손상 위험을 대부분 방지하려면 이 옵션을 활성화하는 것이 좋습니다.


![Image](assets/fr/48.webp)


마지막으로 '*확장 기능*' 하위 메뉴에서는 Whirlpool CoinJoin 프로토콜과 같이 기기의 특정 용도에 맞는 기능을 활성화할 수 있습니다.


![Image](assets/fr/49.webp)


## BIP39 passphrase 추가


계속하기 전에 원하는 경우 BIP39 passphrase를 추가할 수 있습니다. BIP39 passphrase는 자유롭게 선택할 수 있는 옵션 비밀번호로, Wallet 보안을 강화하기 위해 Mnemonic 문구에 추가할 수 있습니다. 이 기능을 활성화하면 Bitcoin Wallet에 액세스하려면 Mnemonic와 passphrase가 모두 필요합니다. 둘 중 하나가 없으면 Wallet을 복구할 수 없습니다.


패스포트에서 이 옵션을 구성하기 전에 이 글을 읽고 passphrase의 이론적 작동을 완전히 이해하고 비트코인의 손실로 이어질 수 있는 오류를 방지하는 것이 좋습니다:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

활성화하려면 "*더보기*" 메뉴로 이동하여 "*passphrase 입력*"을 클릭하세요.


![Image](assets/fr/50.webp)


AA1 키패드를 사용하여 passphrase을 입력하고 실제 미디어(종이 또는 금속)에 한 번 이상 저장해야 합니다. 이 예에서는 매우 약한 passphrase을 사용했지만 모든 문자 유형을 포함하고 충분히 긴(강력한 비밀번호처럼) 강력한 무작위 passphrase을 선택해야 합니다.


![Image](assets/fr/51.webp)


BIP39 암호는 대소문자 및 오타에 민감하다는 점에 유의하세요. 처음에 구성한 것과 약간 다른 passphrase을 입력하면 Passport는 오류를 보고하지 않지만 초기 Wallet에 있는 키가 아닌 다른 암호화 키 집합을 도출합니다.


따라서 구성할 때 다음 단계에서 부여받을 마스터 키 지문을 어딘가에 적어두는 것이 중요합니다. 예를 들어, passphrase '플랜 B 네트워크'의 경우 마스터 키 지문은 '745D526B'입니다.


![Image](assets/fr/52.webp)


Passport를 잠금 해제할 때마다 이 메뉴로 돌아가서 passphrase를 입력하고 Wallet에 적용해야 합니다. 패스포트는 passphrase를 저장하지 않습니다.


잠금을 해제할 때마다 passphrase을 기록한 후 이 확인 화면에서 입력한 지문이 구성할 때 기록한 지문과 동일한지 확인하세요. 일치하면 passphrase이 올바르고 올바른 Bitcoin Wallet에 액세스하고 있는 것입니다. 그렇지 않다면 잘못된 Wallet에 접속한 것이므로 입력 오류가 발생하지 않도록 주의하면서 다시 시도해야 합니다.


Wallet에서 첫 비트코인을 받기 전에 **빈 복구 테스트를 수행할 것을 강력히 권장합니다**. Xpub 또는 처음 받은 Address과 같은 몇 가지 참조 정보를 메모한 다음, 아직 비어 있는 상태에서 패스포트에서 Wallet를 삭제하세요(`설정 -> 고급 -> 패스포트 지우기`). 그런 다음 Mnemonic 문구와 passphrase의 종이 백업을 사용하여 Wallet를 복원해 보세요. 복원 후 생성된 쿠키 정보가 원래 기록했던 쿠키 정보와 일치하는지 확인하세요. 일치한다면 종이 백업이 신뢰할 수 있는 것이니 안심해도 됩니다. 테스트 복구를 수행하는 방법에 대해 자세히 알아보려면 이 다른 튜토리얼 을 참조하세요:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)


## Sparrow wallet에서 Wallet 구성하기


이 튜토리얼에서는 Sparrow wallet을 사용한 Passport의 고급 사용법을 보여드리겠습니다. 하지만 이 Hardware Wallet는 Envoy(재단 애플리케이션), Keeper, BlueWallet, 쌍절곤, 스펙터 등 다양한 애플리케이션과도 호환됩니다...


아직 설치하지 않았다면 [공식 웹사이트](https://sparrowwallet.com/)에서 Sparrow wallet을 다운로드하여 컴퓨터에 설치하는 것으로 시작하세요.


![Image](assets/fr/54.webp)


설치하기 전에 소프트웨어의 진위 여부와 무결성을 반드시 확인하세요. 이를 수행하는 방법을 모르는 경우 이 튜토리얼을 참조하세요:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sparrow wallet이 열리면 "*파일*" 탭을 클릭한 다음 "*새 Wallet*"를 클릭합니다.


![Image](assets/fr/55.webp)


Wallet의 이름을 지정한 다음 "*Wallet 만들기*"를 클릭합니다.


![Image](assets/fr/56.webp)


"*에어갭 Hardware Wallet*"을 선택합니다.


![Image](assets/fr/57.webp)


"*여권*" 옵션 옆의 "*스캔...*"을 클릭합니다. 그러면 웹캠이 열립니다.


![Image](assets/fr/58.webp)


Hardware Wallet에서 "*계정*" 메뉴로 이동하여 "*계정 관리*" 하위 메뉴를 선택한 후 "*Wallet 연결*"을 클릭합니다.


![Image](assets/fr/59.webp)


표시되는 드롭다운 목록에서 "*Sparrow*"를 선택합니다.


![Image](assets/fr/60.webp)


그런 다음 Multisig가 없는 일반 구성의 경우 "*단일 서명*"을 선택합니다.


![Image](assets/fr/61.webp)


"*QR 코드*" 옵션을 선택합니다.


![Image](assets/fr/62.webp)


그러면 여권에 generate 동적 QR코드가 생성됩니다. 컴퓨터의 웹캠을 사용하여 Sparrow 소프트웨어로 스캔합니다.


![Image](assets/fr/63.webp)


이제 passphrase을 입력할 때 여권에 표시된 지문과 일치하는 xpub 및 마스터 키 지문이 표시되어야 합니다. "*적용*" 버튼을 클릭합니다.


![Image](assets/fr/64.webp)


Sparrow wallet에 대한 보안 액세스를 위해 강력한 비밀번호를 설정하세요. 이 비밀번호는 무단 액세스로부터 공개 키, 주소, 라벨 및 거래 내역을 보호합니다. 비밀번호를 잊어버리지 않도록 비밀번호 관리자에 저장해 두는 것이 좋습니다.


![Image](assets/fr/65.webp)


그러면 첫 번째 수신 Address을 스캔하여 가져오기에 성공했는지 확인하라는 메시지가 표시됩니다.


![Image](assets/fr/66.webp)


Sparrow에서 "*수신*" 탭으로 이동하여 첫 번째 Address의 QR 코드를 스캔합니다.


![Image](assets/fr/67.webp)


작업이 성공하면 여권에 "*확인됨*"이 표시됩니다.


![Image](assets/fr/68.webp)


그러면 가져오기에 성공했음을 확인할 수 있습니다.


![Image](assets/fr/69.webp)


## 비트코인 받기


이제 패스포트 설정이 완료되었으므로 새 Bitcoin Wallet에서 첫 번째 Sats을 받을 준비가 되었습니다. 그러려면 Sparrow에서 "*수신*" 메뉴를 클릭합니다.


![Image](assets/fr/70.webp)


Sparrow은 Wallet에 첫 번째 빈 영수증 Address을 표시합니다. 레이블을 추가할 수 있습니다.


![Image](assets/fr/71.webp)


사용하기 전에 패스포트 화면에서 Address을 확인하여 Bitcoin Wallet에 속하는지 확인합니다. 필요한 경우 Sparrow에서 Address의 QR 코드를 클릭하여 확대할 수 있습니다. Passport의 "*계정*" 메뉴에서 "*계정 도구*"를 선택합니다.


![Image](assets/fr/72.webp)


"*Address 확인*"을 클릭한 다음 Sparrow wallet에 표시된 QR 코드를 스캔합니다.


![Image](assets/fr/73.webp)


여권에 표시된 Address이 Sparrow에 표시된 것과 정확히 일치하는지, "*확인됨*"이 표시되는지 확인합니다.


![Image](assets/fr/74.webp)


이제 이를 사용해 비트코인을 받을 수 있습니다. 트랜잭션이 네트워크에 브로드캐스트되면 Sparrow에 표시됩니다. 트랜잭션이 확정된 것으로 간주할 만큼 충분한 확인을 받을 때까지 기다리세요.


![Image](assets/fr/75.webp)


## 비트코인 보내기


이제 Wallet에 Sats을 몇 개 가지고 있으니 일부도 보낼 수 있습니다. 그러려면 "*UTXO*" 메뉴를 클릭하세요.


![Image](assets/fr/76.webp)


이 트랜잭션의 입력으로 사용하려는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다.


![Image](assets/fr/77.webp)


수취인의 Address, 거래 목적을 알려주는 라벨 및 이 Address로 송금하려는 금액을 입력합니다.


![Image](assets/fr/78.webp)


현재 시장 상황에 따라 수수료율을 조정한 다음 "*거래 생성*"을 클릭합니다.


![Image](assets/fr/79.webp)


모든 트랜잭션 매개변수가 올바른지 확인한 다음 "*서명을 위한 트랜잭션 마무리*"를 클릭합니다.


![Image](assets/fr/80.webp)


"*QR 표시*"를 클릭하면 PSBT(*Partially Signed Bitcoin Transaction*)가 표시됩니다. Sparrow은 트랜잭션을 생성했지만, 입력에 사용된 비트코인의 잠금을 해제하기 위한 서명이 아직 부족합니다. 이러한 서명은 거래에 서명하는 데 필요한 개인 키에 대한 액세스 권한을 부여하는 seed를 호스팅하는 패스포트에서만 수행할 수 있습니다.


![Image](assets/fr/81.webp)


Passport에서 "*계정*" 메뉴에 액세스하고 "*QR코드로 서명*"을 클릭합니다.


![Image](assets/fr/82.webp)


Sparrow wallet에 표시된 PSBT(*Partially Signed Bitcoin Transaction*)을 스캔합니다.


![Image](assets/fr/83.webp)


수신 Address와 송금 금액이 정확한지 확인한 다음 확인 버튼을 누릅니다.


![Image](assets/fr/84.webp)


Exchange Address을 확인합니다. 제 예제에서는 트랜잭션에 단일 출력이 포함되어 있으므로 아무것도 없습니다.


![Image](assets/fr/85.webp)


선택한 수수료가 맞는지 확인하세요.


![Image](assets/fr/86.webp)


모든 정보가 정확하면 확인 버튼을 클릭하여 거래에 서명합니다.


![Image](assets/fr/87.webp)


Sparrow wallet에서 "*스캔 QR*"을 클릭하고 여권에 표시된 QR 코드를 스캔합니다.


![Image](assets/fr/88.webp)


이제 서명된 트랜잭션을 Bitcoin 네트워크에서 브로드캐스트할 준비가 되었으며, Miner에 의해 블록에 포함될 것입니다. 모든 것이 정확하다면 "*거래 브로드캐스트*"를 클릭합니다.


![Image](assets/fr/89.webp)


거래가 브로드캐스트되었으며 확인을 기다리는 중입니다.


![Image](assets/fr/90.webp)


이제 Passport를 구성하고 사용하는 방법을 알게 되었습니다. 이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 공유해 주셔서 감사합니다!


자세한 내용은 Liana 소프트웨어 튜토리얼을 참조하세요:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04