---
name: BIP-39 Passphrase Ledger
description: Ledger Wallet에 passphrase를 추가하는 방법은 무엇인가요?
---
![cover](assets/cover.webp)


BIP39 passphrase는 선택적 비밀번호로, Mnemonic 문구와 결합하면 결정론적 및 계층적 Bitcoin 지갑에 추가적인 Layer의 보안을 제공합니다. 이 튜토리얼에서는 (모델에 관계없이) 보안 Bitcoin Wallet에 passphrase를 설정하는 방법을 함께 살펴보겠습니다.


이 튜토리얼을 시작하기 전에 passphrase의 개념, 작동 방식, Bitcoin Wallet에 미치는 영향에 대해 잘 모르신다면 제가 모든 것을 설명한 다른 이론 문서를 참조하시기 바랍니다:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## passphrase는 Ledger에서 어떻게 작동하나요?


Ledger 디바이스의 경우, Wallet에서 passphrase을 구성할 수 있는 두 가지 옵션이 있습니다: "*핀 연결*" 옵션과 "*임시*" 옵션.


"*PIN-tied*" 옵션을 사용하면 passphrase를 Ledger의 두 번째 PIN과 연결할 수 있습니다. 즉, 하나는 passphrase 없이 일반 Wallet에 액세스하기 위한 PIN이고, 다른 하나는 passphrase로 보호되는 두 번째 Wallet에 액세스하기 위한 PIN이 2개가 됩니다.


![PASSPHRASE BIP39](assets/notext/03.webp)


기본적으로 이 passphrase 옵션이 두 번째 PIN에 연결되어 있어도 passphrase는 여전히 passphrase로 유지됩니다. 즉, Ledger을 분실하고 다른 장치나 소프트웨어에서 비트코인을 복구하려는 경우 24단어 문구와 **완전한 passphrase**가 반드시 필요합니다. passphrase와 연결된 PIN은 현재 Ledger에서 액세스하는 데만 사용되며, 다른 레저나 다른 소프트웨어에서는 작동하지 않습니다. 따라서 passphrase를 물리적 매체에 완전히 백업하는 것이 중요합니다. **보조 PIN을 아는 것만으로는 Wallet**에 다시 액세스하는 데 충분하지 않으며, 이는 Ledger의 편의 기능일 뿐입니다.


두 번째 PIN 옵션은 물리적 공격에 대처할 때 특히 유용합니다. 예를 들어 공격자가 자금을 훔치기 위해 디바이스 잠금을 해제하도록 강요하는 경우, 첫 번째 PIN을 사용하여 소량의 비트코인이 들어 있는 미끼 Wallet에 액세스하고 두 번째 PIN 뒤에 주요 자금을 안전하게 보관할 수 있습니다.


또한 이 옵션은 서명 장치를 사용할 때마다 수동으로 입력해야 하는 제약 없이 BIP39 passphrase의 모든 보안 이점을 제공합니다. 따라서 길고 임의의 passphrase을 사용할 수 있으므로 무차별 암호 대입 공격에 대한 보호가 강화되는 동시에 장치의 작은 버튼에 매번 수동으로 입력해야 하는 번거로움을 피할 수 있습니다.

"임시 passphrase"의 옵션은 passphrase을 장치에 저장하지 않습니다. 보호된 Wallet에 액세스하려면 매번 Ledger에 passphrase을 수동으로 입력해야 합니다. 이렇게 하면 사용이 더 번거로워지지만 장치에 passphrase의 흔적이 남지 않아 보안이 약간 강화됩니다. 장치를 끄는 즉시 기본 상태로 되돌아가며 숨겨진 계정에 액세스하려면 전체 passphrase을 새로 입력해야 합니다. 따라서 이 '임시 passphrase' 옵션은 다른 하드웨어 지갑의 작동 방식과 유사합니다.

이 튜토리얼에서는 Ledger Flex를 예로 들어 설명합니다. 그러나 다른 Ledger 모델을 사용하는 경우에도 프로세스는 동일하게 유지됩니다. Ledger Stax의 경우 Interface은 Ledger Flex와 동일합니다. 나노 S, 나노 S 플러스, 나노 X 모델의 경우 Interface은 다르지만 프로세스와 메뉴 이름은 동일하게 유지됩니다.


**주의: ** passphrase를 활성화하기 전에 Ledger로 이미 비트코인을 받은 경우, Bitcoin 트랜잭션을 통해 비트코인을 전송해야 합니다. passphrase는 새로운 키 세트를 생성하므로 초기 Wallet와는 완전히 독립적인 Wallet를 생성합니다. passphrase를 추가하면 비어 있는 새 Wallet를 갖게 됩니다. 그러나 이렇게 해도 passphrase가 없는 첫 번째 Wallet가 삭제되지는 않습니다. passphrase를 입력하지 않고도 Ledger를 통해 직접 액세스하거나 24단어 구문을 사용하여 다른 소프트웨어를 통해 계속 액세스할 수 있습니다.


이 튜토리얼을 시작하기 전에 Ledger을 이미 초기화하고 Mnemonic 문구를 생성했는지 확인하세요. 그렇지 않고 Ledger을 처음 사용하는 경우 PlanB 네트워크에서 제공되는 해당 모델에 대한 특정 튜토리얼을 따르세요. 이 단계가 완료되면 이 튜토리얼로 돌아올 수 있습니다.


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Ledger로 임시 passphrase을 설정하는 방법은 무엇인가요?


Ledger의 홈페이지에서 설정 톱니바퀴를 클릭합니다.


![PASSPHRASE BIP39](assets/notext/04.webp)


'고급' 메뉴를 선택한 다음 'passphrase 설정'을 선택합니다.


![PASSPHRASE BIP39](assets/notext/05.webp)


이전 부분에서 설명한 "PIN에 연결" 옵션 또는 "임시" 옵션 중에서 선택할 수 있는 단계입니다. 여기서는 임시 passphrase를 설정하는 방법을 설명할 테니 '임시 passphrase 설정'을 클릭하세요.


![PASSPHRASE BIP39](assets/notext/06.webp)

그런 다음 passphrase을 입력하라는 메시지가 표시됩니다. 강력한 passphrase을 선택하고 즉시 종이 또는 금속과 같은 매체에 물리적 백업을 진행합니다. 이 예에서는 `fH3&kL@9mP#2sD5qR!82`라는 passphrase을 선택했습니다. passphrase을 입력한 후 "*계속*" 버튼을 클릭합니다.

![PASSPHRASE BIP39](assets/notext/07.webp)


passphrase가 실제 백업에 기록한 내용과 일치하는지 확인한 다음 "*예, 맞습니다*" 버튼을 클릭하여 확인합니다.


![PASSPHRASE BIP39](assets/notext/08.webp)


passphrase 생성을 완료하려면 Ledger의 PIN 코드를 입력합니다. 이제부터 Ledger에서 passphrase로 Wallet에 액세스하려는 경우 여기에 설명된 것과 동일한 단계를 따라야 합니다.


![PASSPHRASE BIP39](assets/notext/09.webp)


이제 Sparrow wallet에서 공개 키 세트를 가져와서 Wallet을 관리할 수 있습니다. Sparrow에서는 passphrase가 없는 초기 Wallet과 다른 Wallet에 해당합니다.


Sparrow wallet를 엽니다. 소프트웨어가 노드에 연결되어 있는지 확인한 다음 "*파일*" 탭을 클릭하고 "*새 Wallet*"을 선택합니다.


![PASSPHRASE BIP39](assets/notext/10.webp)


passphrase로 보호되는 Wallet의 이름을 선택합니다. 이 예에서는 "*passphrase*"라는 용어가 명시적으로 포함된 이름을 선택했습니다. 그러나 이 Wallet를 컴퓨터에서 재량에 맡기고 싶다면 덜 연상되는 이름을 선택할 수 있습니다.


![PASSPHRASE BIP39](assets/notext/11.webp)


Wallet의 스크립트 유형을 선택하세요. "*Taproot*" 또는 "*Native SegWit*"을 선택하는 것이 좋습니다.


![PASSPHRASE BIP39](assets/notext/12.webp)


Ledger를 컴퓨터에 연결한 다음 "*연결된 Hardware Wallet*"를 클릭합니다. Ledger에 passphrase을 이미 입력했는지 확인하세요. 그렇지 않은 경우 이전 단계로 돌아가 passphrase을 입력하세요. 스캔을 진행하기 전에 Ledger에서 "*Bitcoin*" 애플리케이션을 여는 것도 잊지 마세요.


![PASSPHRASE BIP39](assets/notext/13.webp)


"*스캔...*" 버튼을 클릭합니다.


![PASSPHRASE BIP39](assets/notext/14.webp)


Ledger 옆에 있는 "*키 저장소 가져오기*"를 클릭합니다.


![PASSPHRASE BIP39](assets/notext/15.webp)


이제 passphrase에 의해 보호되는 Wallet이 Sparrow에 생성됩니다. 확인하려면 "*적용*" 버튼을 클릭하세요.


![PASSPHRASE BIP39](assets/notext/16.webp)

Sparrow wallet에 안전하게 액세스하려면 강력한 비밀번호를 선택하세요. 이 비밀번호는 Wallet의 Sparrow 데이터에 대한 액세스의 보안을 보장하여 무단 액세스로부터 공개 키, 주소, 레이블 및 거래 내역을 보호하는 데 도움이 됩니다.

이 비밀번호를 잊지 않도록 비밀번호 관리자에 저장해 두는 것이 좋습니다.


![PASSPHRASE BIP39](assets/notext/17.webp)


이제 Wallet이 생성되었습니다! "*설정*" 메뉴에서 Sparrow은 "*마스터 지문*"을 제공합니다. 이는 마스터 키의 지문을 나타내며, Wallet을 생성하는 데 기초로 사용됩니다. 이 지문의 사본을 보관하는 것이 좋습니다. 제 예시에서는 281ee33a`에 해당합니다.


![PASSPHRASE BIP39](assets/notext/18.webp)


이전 부분에서 언급한 내용을 기억하세요. 사소한 실수라도 passphrase를 잘못 입력하면 다른 키로 완전히 새로운 Wallet가 generate이 됩니다. 올바른 passphrase로 올바른 Wallet에 액세스하고 있는지 확인해야 할 때마다 마스터 키의 지문이 적어둔 지문과 일치하는지 확인하세요. 이 정보는 그 자체로 자금 보안이나 개인정보 보호에 위험을 초래하지 않습니다.


Wallet을 passphrase와 함께 사용하기 전에 드라이런 복구 테스트를 수행할 것을 강력히 권장합니다. Xpub 또는 마스터 키의 지문과 같은 참조 정보를 메모한 다음 Wallet이 아직 비어 있는 상태에서 Ledger을 재설정합니다. 그런 다음 24단어 문구의 종이 백업과 passphrase를 사용하여 Ledger에서 Wallet을 복원해 보세요. 복원 후 생성된 정보가 처음에 기록한 내용과 일치하는지 확인합니다. 일치한다면 종이 백업이 신뢰할 수 있다는 것을 확신할 수 있습니다.


## Ledger로 PIN에 연결된 passphrase을 설정하는 방법은 무엇인가요?


Ledger의 홈페이지에서 설정 톱니바퀴를 클릭합니다.


![PASSPHRASE BIP39](assets/notext/19.webp)


"*고급*" 메뉴를 선택한 다음 "*passphrase 설정*"을 선택합니다.


![PASSPHRASE BIP39](assets/notext/20.webp)


이전 부분에서 설명한 "*PIN에 연결*" 또는 "*임시*" 옵션 중 하나를 선택할 수 있는 단계입니다. 여기서는 PIN에 연결된 passphrase를 설정하는 방법을 설명할 테니 "*passphrase를 설정하고 새 PIN에 연결*"을 클릭하세요.


![PASSPHRASE BIP39](assets/notext/21.webp)

그런 다음 passphrase에 연결할 PIN 코드를 선택해야 합니다. 기본 PIN 코드와 마찬가지로 가능한 한 무작위로 8자리 PIN 코드를 선택하는 것이 좋습니다. 또한 이 코드를 Ledger Flex가 저장된 위치와 다른 위치에 저장해야 합니다.

제 경우에는 기본 비밀번호는 `58293647`이고 passphrase와 연결된 보조 비밀번호로 `71425839`을 선택했습니다.


![PASSPHRASE BIP39](assets/notext/22.webp)


그런 다음 passphrase을 입력하라는 메시지가 표시됩니다. 강력한 passphrase을 선택하고 즉시 종이 또는 금속과 같은 매체에 물리적 백업을 진행합니다. 이 예에서는 `fH3&kL@9mP#2sD5qR!82`라는 passphrase을 선택했습니다. passphrase을 입력한 후 "*계속*" 버튼을 클릭합니다.


![PASSPHRASE BIP39](assets/notext/23.webp)


passphrase이 실제 백업에 기록한 내용과 일치하는지 확인한 다음 "*예, 맞습니다*" 버튼을 클릭하여 확인합니다.


![PASSPHRASE BIP39](assets/notext/24.webp)


passphrase 생성을 완료하려면 Ledger의 기본 PIN 코드(passphrase에 연결된 PIN 코드가 아님)를 입력합니다.


![PASSPHRASE BIP39](assets/notext/25.webp)


이제부터 Ledger에서 passphrase으로 Wallet에 액세스하려면 기본 PIN 코드가 아닌 보조 PIN 코드를 입력해야 합니다:


- 기본 PIN 코드(`58293647`) > Wallet(passphrase 제외).
- 보조 PIN 코드(`71425839`) > Wallet(passphrase 포함).


이제 Sparrow wallet에서 공개 키 세트를 가져와서 Wallet을 관리할 수 있습니다. Sparrow에서는 passphrase이 없는 초기 Wallet과는 다른 Wallet에 해당합니다.


Sparrow wallet을 엽니다. 소프트웨어가 노드에 연결되어 있는지 확인한 다음 "*파일*" 탭을 클릭하고 "*새 Wallet*"를 선택합니다.


![PASSPHRASE BIP39](assets/notext/26.webp)


passphrase으로 보호되는 Wallet의 이름을 선택합니다. 이 예에서는 "*passphrase*"이라는 용어가 명시적으로 포함된 이름을 선택했습니다. 그러나 이 Wallet의 재량권을 컴퓨터에 유지하고 싶다면 덜 연상되는 이름을 선택할 수 있습니다.


![PASSPHRASE BIP39](assets/notext/27.webp)


Wallet의 스크립트 유형을 선택합니다. "*Taproot*"를 선택하거나 그렇지 않은 경우 "*Native SegWit*"을 선택하는 것이 좋습니다.


![PASSPHRASE BIP39](assets/notext/28.webp)

Ledger을 컴퓨터에 연결한 다음 "*연결된 Hardware Wallet*"을 클릭합니다. 보조 PIN 코드로 잠금을 해제하여 Ledger에 passphrase가 이미 있는지 확인합니다. 그렇지 않은 경우 Ledger을 다시 시작하고 passphrase와 연결된 PIN 코드를 입력합니다. 스캔을 진행하기 전에 Ledger에서 "*Bitcoin*" 애플리케이션을 여는 것도 잊지 마세요.


![PASSPHRASE BIP39](assets/notext/29.webp)


"*스캔...*" 버튼을 클릭합니다.


![PASSPHRASE BIP39](assets/notext/30.webp)


"*키 저장소 가져오기*"를 클릭합니다.


![PASSPHRASE BIP39](assets/notext/31.webp)


이제 passphrase에 의해 보호되는 Wallet가 Sparrow에 생성됩니다. 확인하려면 "*적용*" 버튼을 클릭합니다.


![PASSPHRASE BIP39](assets/notext/32.webp)


Sparrow wallet에 대한 보안 액세스를 위해 강력한 비밀번호를 선택하세요. 이 비밀번호는 Sparrow에서 Wallet 데이터에 대한 액세스의 보안을 보장하여 무단 액세스로부터 공개 키, 주소, 레이블 및 거래 내역을 보호하는 데 도움이 됩니다.


이 비밀번호를 잊지 않도록 비밀번호 관리자에 저장해 두는 것이 좋습니다.


![PASSPHRASE BIP39](assets/notext/33.webp)


이제 Wallet가 생성되었습니다! "*설정*" 메뉴에서 Sparrow은 "*마스터 지문*"을 제공합니다. 이는 Wallet 파생의 기본으로 사용되는 마스터 키의 지문을 나타냅니다. 이 지문의 사본을 보관하는 것이 좋습니다. 제 예시에서는 281ee33a`에 해당합니다.


![PASSPHRASE BIP39](assets/notext/34.webp)


이전 부분에서 언급했던 내용을 기억하세요. 사소한 실수라도 passphrase을 잘못 입력하면 다른 키로 완전히 새로운 Wallet가 generate이 됩니다. 올바른 passphrase으로 올바른 Wallet에 액세스해야 할 때마다 마스터 키의 지문이 기록해 둔 지문과 일치하는지 확인하세요. 이 정보 자체는 자금 보안이나 개인 정보 보호에 위험을 초래하지 않습니다.

Wallet를 passphrase과 함께 사용하기 전에 드라이런 복구 테스트를 수행할 것을 강력히 권장합니다. Xpub 또는 마스터 키의 지문과 같은 참조 정보를 메모한 다음 Wallet가 아직 비어 있는 상태에서 Ledger를 재설정합니다. 그런 다음 24단어 문구의 종이 백업과 passphrase을 사용하여 Ledger에서 Wallet를 복원해 보세요. 복원 후 생성된 정보가 처음에 기록한 내용과 일치하는지 확인합니다. 일치한다면 종이 백업이 신뢰할 수 있다는 것을 확신할 수 있습니다.


축하합니다, 이제 Bitcoin Wallet을 passphrase으로 보호할 수 있게 되었습니다! 이 튜토리얼이 도움이 되었다면 아래에 좋아요를 남겨 주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


Ledger Flex를 사용하는 방법에 대한 다른 전체 튜토리얼도 확인해 보시기 바랍니다:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a