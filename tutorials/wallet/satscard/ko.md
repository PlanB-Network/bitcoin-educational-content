---
name: Satscard
description: 쌍절곤으로 새츠카드 설정 및 사용하기
---
![cover](assets/cover.webp)


Bitcoin은 P2P 거래를 할 수 있는 전자 현금 시스템입니다. 그러나 거래가 불변임을 확신하기 위해서는 송금인의 이중 지출 시도를 방지하기 위해 여러 번의 확인(보통 6회)을 기다려야 합니다. 이러한 확인 지연은 때때로 불편할 수 있으며, 특히 실물 현금과 유사한 즉각적인 완결성을 원할 때 더욱 그렇습니다. 지폐의 소유권이 즉시 이전되는 현금과 달리, Bitcoin 거래는 최종적으로 되돌릴 수 없는 것으로 간주되기까지 대기 시간이 필요합니다.


바로 이 지점에서 샛카드가 등장합니다. 이 카드는 On-Chain 거래를 수행할 필요 없이 비트코인을 물리적이고 즉각적으로 전송할 수 있는 방법을 제공합니다. 사츠카드는 무기명 카드로서 Bitcoin Ownership을 안전하게 전송할 수 있어 기존 현금에 가까운 경험을 제공합니다. 이 튜토리얼에서는 이 솔루션에 대해 소개해드리겠습니다.


## Satscard란 무엇인가요?


코인라이트의 샛카드는 오픈타임의 후속 제품입니다. 이 카드는 지폐나 Coin와 유사하게 비트코인을 물리적으로 전송할 수 있는 NFC 카드입니다. 기존의 Hardware Wallet와 달리 사츠카드는 무기명 카드로, 카드를 물리적으로 소유하는 것은 카드에 저장된 키로 보호되는 비트코인의 Ownership와 동일합니다. 가격은 선택한 디자인에 따라 6.99달러에서 17.99달러 사이입니다.


![SATSCARD](assets/notext/01.webp)


사츠카드 칩에는 10개의 슬롯이 장착되어 있어 10개의 다른 주소에 최대 10번까지 비트코인을 저장할 수 있습니다. 각 슬롯은 독립적으로 작동하며 이론적으로 비트코인을 잠그는 데 한 번만 사용해야 합니다. 비트코인을 사용하려면 쌍절곤과 같은 호환 애플리케이션으로 Satscard 뒷면에 표시된 6자리 인증 코드를 입력하여 슬롯의 봉인을 해제하기만 하면 됩니다.


이 카드는 Blockchain의 비트코인을 보호하는 개인 키를 이전 소유자가 물리적으로 카드를 분리한 후에도 보유할 수 없도록 보장합니다. 또한 수령인은 Exchange을 받을 때 슬롯의 유효성과 슬롯에 저장된 금액을 확인할 수 있습니다.


이 시스템은 특히 비트코인으로 실물 상품을 구매하거나 비트코인을 선물할 때 유용합니다.


## Satscard는 어떻게 구매하나요?


샛스카드는 [코인사이트 공식 웹사이트](https://store.coinkite.com/store/category/satscard)에서 구매할 수 있습니다. 오프라인 매장에서 구매하려면 [인증된 리셀러 목록](https://coinkite.com/resellers)에서도 확인할 수 있습니다.

또한 NFC 통신과 호환되는 휴대폰 또는 표준 주파수인 13.56MHz에서 NFC 카드를 읽을 수 있는 USB 장치가 필요합니다.

## Satscard에 슬롯을 로드하는 방법은 무엇인가요?


Satscard를 받으면 가장 먼저 포장이 개봉되지 않았는지 확인해야 합니다. 포장이 손상된 경우 카드가 손상되었거나 진품이 아닐 수 있습니다.


Satscard를 관리하기 위해 모바일 애플리케이션 **Nunchuk Wallet**을 사용합니다. 스마트폰이 NFC와 호환되는지 확인한 다음, [구글 플레이 스토어](https://play.google.com/store/apps/details?id=io.nunchuk.android), [앱 스토어](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) 또는 [`.apk` 파일](https://github.com/nunchuk-io/nunchuk-android/releases)을 통해 직접 Nunchuk을 다운로드하세요.


![SATSCARD](assets/notext/02.webp)


이론적으로는 쌍절곤을 사용하지 않고 사츠카드 뒷면에 지정된 Address로 직접 비트코인을 전송할 수 있습니다. 하지만 첫 번째 슬롯의 Address이 실제로 Satscard에 저장된 개인 키에서 파생된 것인지, 사기성 Address이 아닌지 먼저 확인해야 하므로 이렇게 하는 것은 권장하지 않습니다.


쌍절곤을 처음 사용하는 경우 앱에서 계정을 만들라는 메시지가 표시됩니다. 이 튜토리얼의 목적상 계정을 만들 필요는 없습니다. 따라서 계정 없이 계속하려면 "*손님으로 계속하기*"를 선택하세요.


![SATSCARD](assets/notext/03.webp)


그런 다음 "*비지원 Wallet*"를 클릭합니다.


![SATSCARD](assets/notext/04.webp)


다음으로 '*내가 직접 탐색하겠습니다*' 버튼을 클릭합니다.


![SATSCARD](assets/notext/05.webp)


Nunchuk 홈 화면에서 화면 상단의 "*NFC*" 로고를 클릭합니다.


![SATSCARD](assets/notext/06.webp)


Satscard를 휴대폰 뒷면에 대고 스캔합니다.


![SATSCARD](assets/notext/07.webp)


쌍절곤은 Satscard의 첫 번째 슬롯에 해당하는 수신 Address을 표시합니다. 일반적으로 이 Address은 카드 뒷면에 수동으로 작성한 것과 동일해야 합니다. 이 Address을 복사해 이 슬롯에 잠그고자 하는 비트코인을 전송할 때 사용합니다.


![SATSCARD](assets/notext/08.webp)


## 슬롯에 있는 비트코인은 어떻게 확인하나요?


거래가 확인되면 쌍절곤으로 사츠카드 슬롯을 스캔하여 잔액을 확인할 수 있습니다. 따라서 거래가 진행되는 동안 비트코인을 받는 사람은 쌍절곤 앱을 통해 카드에 실제로 비트코인이 들어 있는지 즉시 확인할 수 있습니다.


![SATSCARD](assets/notext/09.webp)

상대방이 쌍절곤 앱을 설치하지 않은 경우에도 Satscard의 유효성을 확인할 수 있습니다. 스마트폰에서 NFC를 활성화하고 Satscard를 기기 뒷면에 갖다 대기만 하면 됩니다. 그러면 브라우저에서 Satscard 웹사이트가 자동으로 열리며, 여기에서 카드의 유효성과 연결된 비트코인의 금액을 확인할 수 있습니다.

![SATSCARD](assets/notext/10.webp)


## 슬롯에서 비트코인을 출금하는 방법은 무엇인가요?


이제 Satscard의 첫 번째 슬롯에 일정량의 비트코인이 충전되었으므로 결제 수취인에게 카드를 전달할 수 있습니다.


![SATSCARD](assets/notext/11.webp)


받는 사람인 경우 쌍절곤을 설치해야 합니다. 앱에 들어가면 화면 상단의 "*NFC*" 로고를 클릭합니다.


![SATSCARD](assets/notext/12.webp)


Satscard를 휴대폰 뒷면에 놓습니다.


![SATSCARD](assets/notext/13.webp)


쌍절곤은 Address에 확보한 금액을 공개합니다.


![SATSCARD](assets/notext/14.webp)


개인키를 봉인 해제하고 비트코인을 소유한 Address로 옮기려면 "*봉인 해제 및 잔액 스윕*" 버튼을 클릭합니다.


![SATSCARD](assets/notext/15.webp)


"*Wallet로 스윕*" 옵션을 사용하면 쌍절곤 앱에 이미 있는 Wallet로 직접 비트코인을 보낼 수 있습니다. 다른 수신 Address으로 자금을 이체하려면 "*Address으로 출금*"을 선택하세요.


![SATSCARD](assets/notext/16.webp)


Satscard로 보안이 설정된 비트코인을 송금할 수신 Address을 입력합니다. 입력한 Address이 정확한지 확인한 다음(이 때만 확인할 수 있음) "*거래 생성*" 버튼을 클릭합니다.


![SATSCARD](assets/notext/17.webp)


Satscard의 PIN 코드를 입력합니다. 이 6자리 코드는 실물 카드 뒷면에 기재되어 있습니다.


![SATSCARD](assets/notext/18.webp)


NFC 카드에 저장된 개인 키로 거래에 서명하는 동안 Satscard를 스마트폰 뒷면에 보관하세요.


![SATSCARD](assets/notext/19.webp)


이제 거래가 Bitcoin 네트워크에서 서명되고 브로드캐스트되었으므로 Satscard에 사용된 슬롯은 이제 비어 있습니다.


![SATSCARD](assets/notext/20.webp)


## Satscard를 재사용하는 방법은 무엇인가요?


오픈타임과 같은 일회용 솔루션과 달리 Satscard에는 10개의 독립 슬롯이 포함된 칩이 장착되어 있어 카드 한 장으로 최대 10개의 작업을 수행할 수 있습니다. Coinkite에서 공장에서 미리 구성한 첫 번째 슬롯은 Satscard 뒷면에 적혀 있는 수신 Address에 해당합니다.


![SATSCARD](assets/notext/21.webp)

나머지 9개의 슬롯을 활성화하려면 쌍절곤 앱을 통해 generate 키 쌍과 Address를 활성화해야 합니다. 앱 홈페이지에서 화면 상단의 "*NFC*" 로고를 클릭합니다.

![SATSCARD](assets/notext/22.webp)


Satscard를 휴대폰 뒷면에 놓습니다.


![SATSCARD](assets/notext/23.webp)


쌍절곤은 카드에 활성화된 슬롯이 없음을 나타내며, 이는 첫 번째 슬롯은 이미 사용되었고 두 번째 슬롯은 아직 생성되지 않았기 때문에 정상입니다. 이전에 사용한 슬롯을 보려면 "*봉인 해제된 슬롯 보기*"를 클릭하세요. 이러한 슬롯을 재사용하는 것은 Address 재사용으로 이어져 On-Chain 개인정보에 해를 끼칠 수 있으므로 재사용하지 않는 것이 좋습니다. 따라서 "*예*" 버튼을 클릭하여 새 슬롯을 설정합니다.


![SATSCARD](assets/notext/24.webp)


이제 마스터 chain code를 generate으로 전환하는 방법을 선택해야 합니다.


사츠카드의 슬롯은 BIP32 표준을 따르며, 이는 비트코인을 보호하는 암호화 키의 파생이 BIP39 지갑에서처럼 Mnemonic 문구에 의존하지 않고 마스터 개인 키와 마스터 chain code에 직접 의존한다는 것을 의미합니다. 이 두 개의 Elements은 HMAC-SHA512 기능에서 하위 키 쌍인 generate에 대한 입력으로 사용됩니다. 각 슬롯에는 자체 마스터 키와 자체 마스터 chain code이 있습니다. 각 슬롯에는 파생 레벨이 하나만 있습니다.


첫 번째 슬롯의 키 쌍은 코인카이트에서 미리 생성합니다. 그렇기 때문에 쌍절곤을 통해 직접 액세스할 수 있으며, NFC 카드 뒷면에 수신 Address이 적혀 있습니다. 하지만 다른 슬롯의 키는 사용자가 직접 생성해야 합니다.


각 슬롯의 마스터 개인 키는 Satscard에서 직접 생성하며, 마스터 체인 코드는 외부에서 제공해야 합니다. 새 슬롯의 chain code의 경우, "*자동*"을 선택하여 쌍절곤 generate이 자동으로 생성하도록 하거나 "*고급*"을 선택하고 전용 공간에 입력하여 직접 생성하는 두 가지 옵션이 있습니다. chain code를 효과적으로 사용하려면 가능한 한 무작위여야 합니다.


![SATSCARD](assets/notext/25.webp)


수능 카드 뒷면에 표시된 6자리 PIN을 입력합니다.


![SATSCARD](assets/notext/26.webp)


Satscard를 휴대폰 뒷면에 놓습니다.


![SATSCARD](assets/notext/27.webp)


새 슬롯이 성공적으로 구성되었습니다. 이제 비트코인을 입금할 수신 Address를 확인할 수 있습니다. 로드를 계속 진행하려면 이 튜토리얼의 "*샛카드에 슬롯을 로드하는 방법*" 섹션의 지침을 따르세요.

이 과정은 각 Satscard에서 최대 10회까지 반복할 수 있습니다.


이제 Satscard 사용법을 익히셨으니 축하드립니다! 이 튜토리얼이 도움이 되었다면 아래에 좋아요를 남겨 주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!