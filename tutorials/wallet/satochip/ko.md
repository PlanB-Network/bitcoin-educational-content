---
name: Satochip
description: 사토칩 스마트 카드 설정 및 사용하기
---
![cover](assets/cover.webp)


Hardware Wallet은 Bitcoin Wallet의 개인키를 관리하고 보호하는 전용 전자 장치입니다. 인터넷에 연결된 범용 컴퓨터에 설치되는 소프트웨어 지갑(또는 Hot 지갑)과 달리 하드웨어 지갑은 개인 키를 물리적으로 격리할 수 있어 해킹과 도난의 위험을 줄여줍니다.


Hardware Wallet의 주요 목표는 장치의 기능을 최소화하여 공격 표면을 줄이는 것입니다. 공격 표면이 작다는 것은 잠재적인 공격 벡터, 즉 공격자가 비트코인에 접근하기 위해 악용할 수 있는 시스템의 취약점이 적다는 의미이기도 합니다.


특히 비트코인을 절대 금액으로 보유하거나 총 자산의 비율로 보유하는 경우, Hardware Wallet를 사용하여 비트코인을 보호하는 것이 좋습니다.


하드웨어 지갑은 컴퓨터나 스마트폰의 Wallet 관리 소프트웨어와 함께 사용됩니다. 이 소프트웨어는 거래 생성을 관리하지만, 이러한 거래의 유효성을 검사하는 데 필요한 암호화 서명은 Hardware Wallet 내에서만 이루어집니다. 즉, 개인 키가 잠재적으로 취약한 환경에 노출되지 않습니다.


하드웨어 지갑은 사용자를 이중으로 보호합니다: 한편으로는 개인 키를 오프라인으로 유지하여 원격 공격으로부터 비트코인을 보호하고, 다른 한편으로는 일반적으로 키를 추출하려는 시도에 대해 더 나은 물리적 저항력을 제공합니다. 이 두 가지 보안 기준에 따라 시중에 나와 있는 다양한 모델을 판단하고 순위를 매길 수 있습니다.


이 튜토리얼에서는 이러한 솔루션 중 하나인 사토칩에 대해 알아볼 것을 제안합니다.


## 사토칩 소개


사토칩은 매우 높은 보안 표준인 *EAL6+* 인증 칩이 탑재된 카드 형태의 Hardware Wallet입니다(*NXP JCOP*). 벨기에 회사에서 생산합니다.


![SATOCHIP](assets/notext/01.webp)


이 스마트 카드는 시중의 다른 하드웨어 지갑에 비해 매우 저렴한 €25에 판매됩니다. 칩은 secure element로 물리적 공격에 대한 저항력이 매우 뛰어납니다. 게다가 코드가 오픈 소스(*AGPLv3*)입니다.

하지만 사토칩은 그 형식 때문에 다른 하드웨어만큼 많은 옵션을 제공하지 않습니다. 카드이기 때문에 배터리도, 카메라도, 마이크로 SD 카드 리더기도 없습니다. 제 생각에 가장 큰 단점은 Hardware Wallet에 화면이 없어 특정 유형의 원격 공격에 더 취약하다는 것입니다. 실제로 이로 인해 사용자는 맹목적으로 서명하고 컴퓨터 화면에 표시되는 내용을 신뢰해야 합니다.


이러한 한계에도 불구하고 사토칩은 가격이 저렴하다는 점에서 여전히 흥미롭습니다. 이 Wallet은 특히 화면이 장착된 Hardware Wallet로 보호되는 저축용 Wallet과 더불어 소비용 Wallet의 보안을 강화하는 데 사용할 수 있습니다. 또한 소량의 비트코인을 보유하고 있고 더 정교한 장치에 100유로를 투자하고 싶지 않은 사람들에게도 좋은 솔루션이 될 수 있습니다. 또한, Multisig 구성 또는 향후 타임락 기능이 있는 Wallet 시스템에서 사토칩을 사용하면 흥미로운 이점을 제공할 수 있습니다.


사토칩은 다른 두 가지 제품도 제공합니다. 비트코인을 오프라인에 보관할 수 있도록 설계된 무기명 카드이지만 거래는 허용하지 않는 사토딤이 있습니다. 이는 훨씬 더 안전한 일종의 종이 Wallet로, 예를 들어 선물용으로 사용할 수 있습니다. 마지막으로 Mnemonic 문구 관리자인 시드키퍼가 있습니다. 종이에 직접 메모하지 않고도 seed을 안전하게 저장하는 데 사용할 수 있습니다.


## 사토칩은 어떻게 구매하나요?


사토칩은 [공식 웹사이트](https://satochip.io/product/satochip/)에서 판매되고 있습니다. 오프라인 매장에서 구매하려면 사토칩 웹사이트에서 [공인 리셀러 목록](https://satochip.io/resellers/)을 확인할 수도 있습니다.


사토칩은 NFC 통신 또는 스마트 카드 리더기를 통해 Wallet 관리 소프트웨어와 상호 작용할 수 있는 두 가지 가능성을 제공합니다. NFC 옵션의 경우 기기가 이 기술과 호환되는지 확인하거나 외부 NFC 리더기를 구입하세요. 사토칩은 표준 주파수인 13.56MHz에서 작동합니다. 그렇지 않은 경우 스마트 카드 리더를 구입할 수도 있습니다. Satochip 웹사이트 또는 다른 곳에서 찾을 수 있습니다.


![SATOCHIP](assets/notext/02.webp)


## Sparrow로 사토칩을 설정하는 방법은 무엇인가요?


사토칩을 수령한 후 첫 번째 단계는 포장이 개봉되지 않았는지 확인하는 것입니다. 사토칩의 포장에는 밀봉 스티커가 있어야 합니다. 이 스티커가 없거나 손상된 경우 스마트 카드가 손상되어 진품이 아닐 수 있습니다.

![SATOCHIP](assets/notext/03.webp)

안에 사토칩이 들어 있습니다.


![SATOCHIP](assets/notext/04.webp)


이 튜토리얼에서는 Wallet을 관리하기 위해 Sparrow을 사용하는 것이 좋습니다. 아직 소프트웨어가 없는 경우 공식 웹사이트를 방문하여 다운로드하세요(https://sparrowwallet.com/download/). Sparrow wallet(곧 제공 예정)에 대한 튜토리얼도 확인할 수 있습니다.


![SATOCHIP](assets/notext/05.webp)


사토칩을 스마트 카드 리더에 삽입하거나 NFC 리더에 올려놓고 리더를 Sparrow가 열려 있는 컴퓨터에 연결합니다.


![SATOCHIP](assets/notext/06.webp)


Sparrow wallet을 열고 Bitcoin 노드에 제대로 연결되어 있는지 확인합니다. 이렇게 하려면 오른쪽 하단의 체크 표시를 확인하세요. 퍼블릭 노드에 연결되어 있으면 노란색, Bitcoin core에 연결되어 있으면 Green, 일렉트럼에 연결되어 있으면 파란색이어야 합니다.


![SATOCHIP](assets/notext/07.webp)


Sparrow wallet에서 "*파일*" 탭을 클릭합니다.


![SATOCHIP](assets/notext/08.webp)


그런 다음 "*새로운 Wallet*" 메뉴를 클릭합니다.


![SATOCHIP](assets/notext/09.webp)


Wallet의 이름을 선택한 다음 "*Wallet 만들기*"를 클릭합니다.


![SATOCHIP](assets/notext/10.webp)


"*연결된 Hardware Wallet*" 버튼을 클릭합니다.


![SATOCHIP](assets/notext/11.webp)


"*스캔...*" 버튼을 클릭합니다.


![SATOCHIP](assets/notext/12.webp)


사토칩이 나타납니다. "*키 저장소 가져오기*"를 클릭합니다.


![SATOCHIP](assets/notext/13.webp)


다음으로, 사토칩 잠금을 해제하기 위해 PIN 코드를 설정해야 합니다. 4~16자 사이의 강력한 비밀번호를 선택하세요. 이 비밀번호를 백업해 두세요.


이 비밀번호는 passphrase이 아니라는 점에 유의하세요. 즉, 이 비밀번호가 없어도 Mnemonic 문구를 사용하면 필요한 경우 Wallet을 소프트웨어로 다시 가져올 수 있습니다. 비밀번호는 사토칩 자체에 대한 액세스를 보호하는 데만 사용됩니다. 다른 하드웨어 지갑에 있는 PIN 코드와 동일합니다.


비밀번호를 입력한 후 "*키 저장소 가져오기*" 버튼을 다시 클릭합니다.


![SATOCHIP](assets/notext/14.webp)


비밀번호를 다시 메모한 다음 "*초기화*" 버튼을 클릭합니다.


![SATOCHIP](assets/notext/15.webp)


그러면 Mnemonic 문구를 생성할 수 있는 창이 나타납니다. "*generate 신규*" 버튼을 클릭합니다.


![SATOCHIP](assets/notext/16.webp)

복구 문구를 종이 또는 금속 매체에 적어 하나 이상의 실제 사본을 만드세요. 이 문구는 추가적인 보호 조치 없이 비트코인에 대한 전체 액세스 권한을 부여한다는 점에 유의하세요. 따라서 누군가 이를 발견하면 사토칩이나 비밀번호에 대한 액세스 권한이 없어도 즉시 비트코인을 훔칠 수 있습니다. 따라서 이러한 백업을 보호하는 것이 중요합니다. 또한, 이 문구를 사용하면 사토칩을 분실하거나 손상된 경우 또는 PIN 코드를 잊어버린 경우에도 비트코인에 다시 액세스할 수 있습니다.

![SATOCHIP](assets/notext/17.webp)


Bitcoin Wallet이 성공적으로 생성되었습니다.


![SATOCHIP](assets/notext/18.webp)


"*키 저장소 가져오기*" 버튼을 다시 클릭합니다.


![SATOCHIP](assets/notext/19.webp)


이제 Wallet이 생성되었습니다. 이제 개인 키가 사토칩의 스마트카드에 저장됩니다. 계속하려면 "*적용*" 버튼을 클릭합니다.


![SATOCHIP](assets/notext/20.webp)


사토칩의 PIN 코드 외에 Sparrow wallet에서 관리하는 공개 정보를 보호하기 위해 추가 비밀번호를 설정하는 것이 좋습니다. 이 비밀번호는 Sparrow wallet에 대한 접근 보안을 보장하여 무단 액세스로부터 공개 키, 주소 및 거래 내역을 보호하는 데 도움이 됩니다.


![SATOCHIP](assets/notext/21.webp)


두 필드에 비밀번호를 입력한 다음 "*비밀번호 설정*" 버튼을 클릭합니다.


![SATOCHIP](assets/notext/22.webp)


이제 사토칩이 Sparrow wallet에 구성되었습니다.


![SATOCHIP](assets/notext/23.webp)


이제 Wallet이 생성되었으므로 사토칩을 분리할 수 있습니다. 안전한 곳에 보관하세요!


## 사토칩으로 비트코인을 받는 방법은 무엇인가요?


Wallet에 들어가면 "*수신*" 탭을 클릭합니다.


![SATOCHIP](assets/notext/24.webp)


Sparrow wallet은 Wallet에 대한 Address를 생성합니다. 일반적으로 다른 하드웨어 지갑의 경우 "*Address 표시*"를 클릭해 장치 화면에서 직접 Address를 확인하는 것이 좋습니다. 안타깝게도 이 옵션은 사토칩에서는 사용할 수 없지만 다른 지갑에서는 반드시 사용하시기 바랍니다.


![SATOCHIP](assets/notext/25.webp)


"*라벨*"을 추가하여 이 Address으로 보호할 비트코인의 출처를 설명할 수 있습니다. 이는 UTXO를 더 잘 관리하는 데 도움이 되는 좋은 습관입니다.


![SATOCHIP](assets/notext/26.webp)


라벨링에 대한 자세한 내용은 이 다른 튜토리얼도 확인하시기 바랍니다:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

그런 다음 이 Address을 사용하여 비트코인을 받을 수 있습니다.


![SATOCHIP](assets/notext/27.webp)

## 사토칩으로 비트코인을 전송하는 방법은 무엇인가요?

이제 사토칩을 통해 안전한 Wallet로 첫 번째 Sats을 받았으니 이제 사용할 수도 있습니다! 사토칩을 컴퓨터에 연결하고 Sparrow wallet을 실행한 다음 "*송금*" 탭으로 이동하여 새 트랜잭션을 생성하세요.


![SATOCHIP](assets/notext/28.webp)


Coin 제어를 수행하려면, 즉 트랜잭션에서 소비할 UTXO를 구체적으로 선택하려면 "*UTXO*" 탭으로 이동하세요. 사용하려는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다. "*송금*" 탭의 동일한 화면으로 리디렉션되지만, 트랜잭션에 대해 이미 UTXO가 선택된 상태로 표시됩니다.


![SATOCHIP](assets/notext/29.webp)


목적지 Address를 입력합니다. "*+ 추가*" 버튼을 클릭하여 여러 주소를 입력할 수도 있습니다.


![SATOCHIP](assets/notext/30.webp)


이 지출의 목적을 기억하기 위해 "*라벨*"을 표시하세요.


![SATOCHIP](assets/notext/31.webp)


이 Address으로 송금할 금액을 선택합니다.


![SATOCHIP](assets/notext/32.webp)


현재 시장에 따라 거래 수수료율을 조정하세요.


![SATOCHIP](assets/notext/33.webp)


트랜잭션의 모든 매개변수가 올바른지 확인한 다음 "*거래 생성*"을 클릭합니다.


![SATOCHIP](assets/notext/34.webp)


모든 것이 만족스럽다면 "*서명을 위한 거래 마무리*"를 클릭합니다.


![SATOCHIP](assets/notext/35.webp)


"*서명*"을 클릭합니다.


![SATOCHIP](assets/notext/36.webp)


사토칩 옆에 있는 '*서명*'을 다시 클릭합니다.


![SATOCHIP](assets/notext/37.webp)


사토칩의 PIN 코드를 입력한 다음 "*서명*"을 다시 클릭하여 거래에 서명합니다.


![SATOCHIP](assets/notext/38.webp)


이제 트랜잭션이 서명되었습니다. "*거래 브로드캐스트*"를 클릭하여 Bitcoin 네트워크에 브로드캐스트합니다.


![SATOCHIP](assets/notext/39.webp)


Sparrow wallet의 "*거래*" 탭에서 찾을 수 있습니다.


![SATOCHIP](assets/notext/40.webp)


이제 사토칩 사용에 대해 잘 알게 되셨습니다! 이 튜토리얼이 도움이 되었다면 아래에 엄지 손가락을 올려주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!