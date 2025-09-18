---
name: Tapsigner
description: 쌍절곤으로 탭시그너 설정 및 사용하기
---
![cover](assets/cover.webp)


Hardware Wallet은 Bitcoin Wallet의 개인키 관리 및 보안을 위한 전자 장치입니다. 인터넷에 연결된 범용 컴퓨터에 설치되는 소프트웨어 지갑(또는 Hot 지갑)과 달리 하드웨어 지갑은 개인 키를 물리적으로 격리할 수 있어 해킹과 도난의 위험을 줄여줍니다.


Hardware Wallet의 주요 목표는 장치의 기능을 최소화하여 공격 표면을 줄이는 것입니다. 공격 표면이 작다는 것은 잠재적인 공격 벡터, 즉 공격자가 비트코인에 접근하기 위해 악용할 수 있는 시스템의 취약점이 적다는 의미이기도 합니다.


특히 비트코인을 절대 금액으로 보유하거나 총 자산의 비율로 보유하는 경우, Hardware Wallet를 사용하여 비트코인을 보호하는 것이 좋습니다.


하드웨어 지갑은 컴퓨터나 스마트폰의 Wallet 관리 소프트웨어와 함께 사용됩니다. 이 소프트웨어는 거래 생성을 관리하지만, 이러한 거래의 유효성을 검사하는 데 필요한 암호화 서명은 Hardware Wallet 내에서만 이루어집니다. 즉, 개인 키가 잠재적으로 취약한 환경에 노출되지 않습니다.


하드웨어 지갑은 사용자를 이중으로 보호합니다: 한편으로는 개인 키를 오프라인으로 유지하여 원격 공격으로부터 비트코인을 보호하고, 다른 한편으로는 일반적으로 키를 추출하려는 시도에 대해 더 나은 물리적 저항력을 제공합니다. 이 두 가지 보안 기준에 따라 시중에 나와 있는 다양한 모델을 판단하고 순위를 매길 수 있습니다.


이 튜토리얼에서는 이러한 솔루션 중 하나인 Coinkite의 탭시그너를 소개합니다.


## 탭시그너 소개


탭시그너는 콜드카드를 생산하는 회사로 잘 알려진 Coinkite에서 NFC 카드 형태로 디자인한 Hardware Wallet입니다.


![TAPSIGNER NUNCHUK](assets/notext/01.webp)


탭사이너를 사용하면 마스터 개인키와 BIP32에 따른 chain code로 구성된 쌍을 저장하여 암호화 키 트리를 도출할 수 있습니다. 이 키를 사용하여 휴대폰이나 NFC 카드 리더에 탭사이너를 대고 트랜잭션에 서명할 수 있습니다.

이 NFC 카드는 19.99달러에 판매되며, 시중에 판매되는 다른 하드웨어 지갑에 비해 매우 저렴합니다. 하지만 탭시그너는 형식 때문에 다른 디바이스만큼 많은 옵션을 제공하지 않습니다. 카드이기 때문에 배터리도, 카메라도, 마이크로 SD 카드 리더기도 당연히 없습니다. 제 생각에 가장 큰 단점은 Hardware Wallet에 화면이 없기 때문에 특정 유형의 원격 공격에 더 취약하다는 것입니다. 실제로 이로 인해 사용자는 맹목적으로 서명하고 컴퓨터 화면에 표시되는 내용을 신뢰해야 합니다.


이러한 한계에도 불구하고 탭시그너는 가격이 저렴하다는 점에서 흥미로울 수 있습니다. 이 Wallet은 특히 화면이 장착된 Hardware Wallet로 보호되는 저축용 Wallet과 더불어 소비용 Wallet의 보안을 강화하는 데 사용할 수 있습니다. 또한 소량의 비트코인을 보유하고 있고 더 정교한 장치에 100유로를 투자하고 싶지 않은 분들에게도 좋은 솔루션이 될 수 있습니다. 또한, Multisig 구성 또는 향후 타임락 기능이 있는 Wallet 시스템에서 탭시그너를 사용하면 흥미로운 이점을 제공할 수 있습니다.


## 탭시그너는 어떻게 구매하나요?


탭시그너는 [코인사이트 공식 웹사이트](https://store.coinkite.com/store/category/tapsigner)에서 구매할 수 있습니다. 오프라인 매장에서 구매하려면 [인증된 리셀러 목록](https://coinkite.com/resellers)에서도 찾을 수 있습니다.


또한 NFC 통신과 호환되는 휴대폰 또는 표준 주파수인 13.56MHz에서 NFC 카드를 읽을 수 있는 USB 장치가 필요합니다.


## 쌍절곤으로 탭시그너를 초기화하는 방법은 무엇인가요?


Tapsigner를 받은 후 첫 번째 단계는 포장이 개봉되지 않았는지 확인하는 것입니다. 포장이 손상된 경우 카드가 손상되어 진품이 아닐 수 있습니다. 코인카이트는 전파를 차단하는 케이스와 함께 탭시그너를 배송합니다. 패키지에 케이스가 포함되어 있는지 확인하세요.


![TAPSIGNER NUNCHUK](assets/notext/02.webp)


Wallet를 관리하기 위해 **Nunchuk Wallet** 모바일 앱을 사용합니다. 스마트폰이 NFC와 호환되는지 확인한 다음, [구글 플레이 스토어](https://play.google.com/store/apps/details?id=io.nunchuk.android), [앱 스토어](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073)에서 또는 [`.apk` 파일](https://github.com/nunchuk-io/nunchuk-android/releases)을 통해 직접 Nunchuk을 다운로드하세요.


![TAPSIGNER NUNCHUK](assets/notext/03.webp)

쌍절곤을 처음 사용하는 경우 앱에서 계정을 만들라는 메시지가 표시됩니다. 이 튜토리얼의 목적상 계정을 만들 필요는 없습니다. 따라서 계정 없이 계속 진행하려면 "*손님으로 계속하기*"를 선택하세요.

![TAPSIGNER NUNCHUK](assets/notext/04.webp)


그런 다음 "*비지원 Wallet*"을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/05.webp)


다음으로 '*내가 직접 탐색하겠습니다*' 버튼을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/06.webp)


쌍절곤에서 '*키*' 탭 옆에 있는 '*+*' 버튼을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/07.webp)


"*NFC 키 추가*"를 선택합니다.


![TAPSIGNER NUNCHUK](assets/notext/08.webp)


그런 다음 "*탭서명 추가*"를 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/09.webp)


"*계속*"을 클릭한 다음 탭시그너 NFC 카드를 스마트폰에 갖다 대세요.


![TAPSIGNER NUNCHUK](assets/notext/10.webp)


탭시그너를 처음 사용하는 경우, Nunchuk에서 초기화를 제안합니다. "*예*"를 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/11.webp)


이제 마스터 chain code을 generate로 전환하는 방법을 선택해야 합니다.


탭사이너는 BIP32 표준을 사용합니다. 즉, 비트코인을 보호하는 암호화 키의 파생은 BIP39 지갑과 같은 Mnemonic 문구에 의존하지 않고 마스터 개인 키와 마스터 chain code에 직접 의존합니다. 이 2개의 Elements은 HMAC 함수를 통과하여 결정론적, 계층적으로 나머지 Wallet를 도출합니다.


마스터 개인키는 탭시그너에 통합된 TRNG(*진성 난수 생성기*)가 직접 생성합니다. 반면에 마스터 chain code은 외부에서 제공해야 합니다. 이 단계에서는 "*자동*"을 클릭하여 쌍절곤이 자동으로 generate를 생성하도록 하거나 "*고급*"을 선택하고 제공된 필드에 입력하여 직접 generate를 생성하도록 선택할 수 있습니다.


![TAPSIGNER NUNCHUK](assets/notext/12.webp)


다음으로 PIN 코드를 선택해야 합니다. "*시작 PIN*" 영역에 탭시그너 뒷면에 적힌 PIN 코드를 입력합니다.


![TAPSIGNER NUNCHUK](assets/notext/13.webp)


PIN 코드를 선택하여 탭시그너에 대한 물리적 액세스를 보호하세요. 이 PIN 코드는 Wallet 복구 프로세스에서 아무런 역할을 하지 않습니다. 유일한 기능은 트랜잭션에 서명하기 위해 Tapsigner의 잠금을 해제하는 것입니다. 이 PIN 코드를 잊어버리지 않도록 저장해 두세요. 계속하려면 "*계속*"을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/14.webp)

지금 탭시그너 카드를 휴대폰 뒷면에 놓아 초기화하세요.

![TAPSIGNER NUNCHUK](assets/notext/15.webp)


그러면 쌍절곤이 generate에 복구 파일을 생성하여 NFC 카드를 분실했을 때 비트코인에 다시 액세스할 수 있도록 해줍니다. 이 파일은 탭시그너 뒷면에 기록된 백업 코드로 암호화되어 있습니다. 비트코인을 복구하려면 이 파일과 암호 해독을 위한 코드가 반드시 필요합니다. 따라서 NFC 카드를 분실하면 현재로서는 카드에만 기록되어 있으므로 이 코드에 대한 액세스도 손실되므로 이 코드의 종이 사본을 만드는 것이 중요합니다. 또한 암호화된 복구 파일의 백업을 여러 개 만들어야 합니다.


![TAPSIGNER NUNCHUK](assets/notext/16.webp)


Wallet의 이름을 선택하세요.


![TAPSIGNER NUNCHUK](assets/notext/17.webp)


이제 Wallet의 기반이 설정되었습니다. 탭시그너의 진위 여부를 확인하려면 언제든지 "*상태 확인 실행*" 버튼을 클릭하면 됩니다.


![TAPSIGNER NUNCHUK](assets/notext/18.webp)


비밀번호를 입력합니다.


![TAPSIGNER NUNCHUK](assets/notext/19.webp)


그런 다음 카드를 휴대폰 뒷면에 놓습니다.


![TAPSIGNER NUNCHUK](assets/notext/20.webp)


## 탭시그너에서 Wallet을 생성하는 방법은 무엇인가요?


Nunchuk 홈페이지로 돌아가면 사용 가능한 서명 장치에 탭시그너가 등록되어 있는 것을 확인할 수 있습니다.


![TAPSIGNER NUNCHUK](assets/notext/21.webp)


이제 Bitcoin Wallet의 키를 generate로 변경해야 합니다. 이렇게 하려면 '*지갑*' 탭 오른쪽에 있는 '*+*' 버튼을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/22.webp)


"*새 Wallet 만들기*"를 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/23.webp)


그런 다음 "*기존 키를 사용하여 새 Wallet 만들기*" 옵션을 선택합니다.


![TAPSIGNER NUNCHUK](assets/notext/24.webp)


Wallet의 이름을 선택한 다음 "*계속*"을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/25.webp)


이 새 키 세트에 대한 서명 장치로 탭시그너를 선택한 다음 "*계속*"을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/26.webp)


모든 것이 만족스럽다면 생성을 확인합니다.


![TAPSIGNER NUNCHUK](assets/notext/27.webp)

그런 다음 Wallet의 구성 파일을 저장할 수 있습니다. 이 파일에는 내 공개 키만 포함되어 있으므로 누군가 이 파일에 액세스하더라도 내 비트코인을 훔칠 수 없습니다. 하지만 모든 거래를 추적할 수는 있습니다. 따라서 이 파일은 개인 정보에 대한 위험만 존재합니다. 경우에 따라 Wallet을 복구하는 데 필수적일 수 있습니다.

![TAPSIGNER NUNCHUK](assets/notext/28.webp)


이제 Wallet이 성공적으로 생성되었습니다!


![TAPSIGNER NUNCHUK](assets/notext/29.webp)


탭시그너를 사용하지 않을 때는 무단 열람을 방지하기 위해 전파를 차단하는 Coinkite에서 제공하는 케이스에 보관하세요.


## 탭시그너에서 비트코인을 받는 방법은 무엇인가요?


비트코인을 받으려면 Wallet를 클릭하세요.


![TAPSIGNER NUNCHUK](assets/notext/30.webp)


그런 다음 생성된 Address을 사용하여 비트코인을 받습니다. 이전에 이 Wallet에서 비트코인을 받은 적이 있는 경우 "*수신*" 버튼을 클릭하여 새로운 빈 Address을 generate으로 전송해야 합니다.


![TAPSIGNER NUNCHUK](assets/notext/31.webp)


발신자의 트랜잭션이 브로드캐스트되면 Wallet에 해당 트랜잭션이 표시됩니다.


![TAPSIGNER NUNCHUK](assets/notext/32.webp)


"*코인 보기*"를 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/33.webp)


새 UTXO를 선택합니다.


![TAPSIGNER NUNCHUK](assets/notext/34.webp)


"*태그*" 옆의 "*+*"를 클릭해 UTXO에 라벨을 추가하세요. 이는 코인의 출처를 기억하고 향후 지출을 위해 개인 정보를 최적화하는 데 도움이 되므로 좋은 습관입니다.


![TAPSIGNER NUNCHUK](assets/notext/35.webp)


기존 태그를 선택하거나 새 태그를 만든 다음 "*저장*"을 클릭합니다. 또한 "*컬렉션*"을 생성하여 코인을 보다 체계적으로 정리할 수 있는 옵션도 있습니다.


![TAPSIGNER NUNCHUK](assets/notext/36.webp)


## 탭시그너로 비트코인을 전송하는 방법은 무엇인가요?


이제 Wallet에 비트코인이 있으니 전송할 수도 있습니다. 이렇게 하려면 원하는 Wallet을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/37.webp)


"*보내기*" 버튼을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/38.webp)


송금할 금액을 선택한 다음 "*계속*"을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/39.webp)


향후 거래에 '*주석*'을 추가하여 거래 목적을 기억하세요.


![TAPSIGNER NUNCHUK](assets/notext/40.webp)

그런 다음 지정된 필드에 수신자의 Address을 수동으로 입력합니다.

![TAPSIGNER NUNCHUK](assets/notext/41.webp)


화면 오른쪽 상단에 있는 아이콘을 클릭하여 QR코드가 인코딩된 Address을 스캔할 수도 있습니다.


![TAPSIGNER NUNCHUK](assets/notext/42.webp)


"*거래 생성*" 버튼을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/43.webp)


거래 내역을 확인한 다음 탭서명자 옆에 있는 '*서명*' 버튼을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/44.webp)


비밀번호를 입력하여 잠금을 해제하세요.


![TAPSIGNER NUNCHUK](assets/notext/45.webp)


그런 다음 스마트폰 뒷면에 탭시그너를 놓습니다.


![TAPSIGNER NUNCHUK](assets/notext/46.webp)


이제 트랜잭션이 서명되었습니다. 모든 것이 올바른지 다시 한 번 확인한 다음 "*거래 브로드캐스트*"를 클릭하여 Bitcoin 네트워크에 브로드캐스트합니다.


![TAPSIGNER NUNCHUK](assets/notext/47.webp)


이제 거래가 확인을 기다리고 있습니다.


![TAPSIGNER NUNCHUK](assets/notext/48.webp)


## 탭시그너 분실 시 Wallet을 복구하는 방법은 무엇인가요?


탭시그너를 분실하신 경우 카드 뒷면에 기재된 코드를 사용하여 Wallet을 복구할 수 있습니다. 따라서 카드를 분실하면 이 코드에 대한 액세스 권한도 손실되므로 이 코드를 Tapsigner와 별도로 저장하는 것이 중요합니다. 또한 Wallet의 암호화된 백업도 필요합니다.


복구 시에는 쌍절곤 앱을 사용하지만, 이는 Hot Wallet에 자금을 임시로 보호하는 것을 의미한다는 점에 유의하시기 바랍니다. 탭시그너로 상당한 금액을 보호하고 있었다면, 대신 새 콜드카드로 동일한 복구 절차를 따르는 것을 고려해 보세요.


쌍절곤 앱을 열고 '*키*' 탭 옆에 있는 '*+*' 버튼을 클릭합니다.


![TAPSIGNER NUNCHUK](assets/notext/49.webp)


"*NFC 키 추가*"를 선택합니다.


![TAPSIGNER NUNCHUK](assets/notext/50.webp)


"*백업에서 탭사인 키 복구*" 옵션을 선택합니다.


![TAPSIGNER NUNCHUK](assets/notext/51.webp)


그러면 기기의 파일 탐색기로 리디렉션됩니다. Wallet의 암호화된 백업 파일을 찾아 선택합니다. 일반적으로 이 파일의 이름은 `backup...`으로 시작합니다.


![TAPSIGNER NUNCHUK](assets/notext/52.webp)


백업 파일의 암호를 해독하는 비밀번호를 입력합니다. 이 비밀번호는 탭시그너 뒷면에 처음 표시된 비밀번호와 일치합니다.


![TAPSIGNER NUNCHUK](assets/notext/53.webp)

그런 다음 복구 Wallet의 이름을 선택합니다.

![TAPSIGNER NUNCHUK](assets/notext/54.webp)


이제 비트코인에 다시 액세스할 수 있게 되었습니다. 이제 쌍절곤 앱의 "*키*" 탭에서 Wallet이 Hot로 관리됩니다. 다음으로, 이 키를 연결하여 "*지갑*" 섹션에 새로운 암호화 키 세트를 만들어야 합니다. 이렇게 하려면 이 튜토리얼의 "*탭사이너에서 Wallet을 만드는 방법*" 부분에서 단계를 다시 따르시면 됩니다.


![TAPSIGNER NUNCHUK](assets/notext/55.webp)


탭시그너를 분실하셨다면, 즉시 비트코인을 소유하고 있는 다른 Wallet로 옮기시길 강력히 권장하며, 이상적으로는 Hardware Wallet로 보호되는 것이 좋습니다. 실제로 분실하신 탭시그너는 잠재적으로 악의적인 사람의 손에 들어갈 수 있습니다. 따라서 방금 복구한 Wallet를 비우고 사용을 중단하는 것이 중요합니다.


이제 탭시그너를 빠르게 사용하실 수 있게 되었습니다! 이 튜토리얼이 도움이 되었다면 아래에 좋아요를 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!