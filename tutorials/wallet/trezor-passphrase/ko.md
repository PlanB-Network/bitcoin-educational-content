---
name: BIP-39 Passphrase Trezor
description: Trezor Wallet에 passphrase을 추가하려면 어떻게 하나요?
---
![cover](assets/cover.webp)



passphrase BIP39는 선택적 비밀번호로, Mnemonic 문구와 결합하여 결정론적 및 계층적 Bitcoin 지갑에 추가적인 Layer 보안을 제공합니다. 이 튜토리얼에서는 트레저(안전 3, 안전 5, 모델 1)의 보안 Bitcoin Wallet에 passphrase을 설정하는 방법을 함께 알아보겠습니다.



![Image](assets/fr/01.webp)



이 튜토리얼을 시작하기 전에 passphrase 개념, 작동 방식, Bitcoin Wallet에 미치는 영향에 대해 잘 모르신다면, 제가 모든 것을 설명한 다른 이론 문서를 참조하시기 바랍니다(작동 방식을 완전히 이해하지 않고 passphrase을 사용하면 비트코인이 위험에 처할 수 있으므로 매우 중요합니다):



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

구성 시 BIP39 표준을 선택한 경우 Trezor의 passphrase는 기존 방식으로 처리됩니다(*멀티 공유 백업*이 필요하지 않은 경우 권장). Trezor의 특별한 점은 Hardware Wallet에 직접 passphrase를 입력하거나 Trezor Suite 소프트웨어를 사용하여 컴퓨터의 키보드를 통해 입력할 수 있다는 것입니다. 두 번째 옵션은 컴퓨터의 공격면이 Hardware Wallet보다 훨씬 더 넓기 때문에 보안성이 상당히 떨어집니다. 그러나 복잡한 passphrase를 입력할 때 일반 키보드를 사용하는 것이 Hardware Wallet보다 빠를 수 있으므로 강력한 암호를 사용하도록 유도할 수 있습니다. 따라서 아예 사용하지 않는 것보다는 입력해야 하는 경우에도 passphrase를 사용하는 것이 항상 더 낫습니다. 하지만 숫자 공격의 위험이 증가한다는 사실을 항상 염두에 두는 것이 중요합니다.



이러한 옵션은 모든 Trezor 호환 Wallet 관리 소프트웨어에서 사용할 수 있는 것은 아닙니다. 예를 들어, 모델 1의 경우 Sparrow wallet의 키보드를 통해 passphrase를 입력할 수 있습니다. Model T, Safe 3 및 Safe 5 모델의 경우 몇 년 전 HWI에서 Sparrow을 통한 입력 옵션이 비활성화되었으므로 Trezor Suite를 사용하거나 Hardware Wallet에서 passphrase를 직접 입력해야 합니다.



![Image](assets/fr/02.webp)



트레저 스위트에서는 두 가지 방법으로 passphrase 수요를 관리할 수 있습니다. "*장치*" 탭에서 "*passphrase*" 옵션을 활성화할 수 있습니다. 이 옵션을 활성화하면 Trezor Suite 및 기타 모든 Wallet 관리 소프트웨어가 시작할 때마다 passphrase를 입력하라는 메시지를 체계적으로 표시합니다. passphrase를 보다 신중하게 사용하려면 설정을 "*표준*"으로 유지하면 됩니다. 이 경우 Hardware Wallet의 왼쪽 상단에 있는 메뉴에 수동으로 액세스하여 시작할 때마다 "*+ passphrase*" 버튼을 클릭해야 합니다.



이 튜토리얼을 시작하기 전에 트레저를 이미 초기화하고 Mnemonic 문구를 생성했는지 확인하세요. 초기화하지 않았고 트레저를 처음 사용하는 경우 Plan ₿ Network에서 제공되는 모델별 튜토리얼을 따르세요. 이 단계를 완료한 후에는 이 튜토리얼로 돌아올 수 있습니다.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Safe 3 또는 Safe 5에 passphrase 추가하기



Wallet을 생성하고 Mnemonic를 저장한 후 PIN을 설정하면 트레저 스위트 홈 메뉴로 이동합니다. 왼쪽 상단에 passphrase BIP39를 활성화하라는 창이 나타납니다.



![Image](assets/fr/03.webp)



이 창이 나타나지 않으면 '*장치*' 설정 탭에서 '*passphrase*' 옵션을 수동으로 활성화해야 합니다.



![Image](assets/fr/04.webp)



이 창에서 passphrase을 입력하라는 메시지가 표시됩니다. 강력한 passphrase을 선택하고 즉시 종이나 금속과 같은 매체에 물리적인 백업을 만드세요. 이 예에서는 passphrase을 선택했습니다: `fH3&kL@9mP#2sD5qR!82`. 이것은 예시일 뿐이므로 조금 더 긴 passphrase을 선택하는 것이 좋습니다. 30~40자 정도가 가장 이상적입니다(좋은 비밀번호처럼).



물론 이 튜토리얼에서처럼 passphrase를 인터넷에서 공유해서는 안 됩니다. 이 예제 Wallet은 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다.



passphrase 선택에 대한 보다 구체적인 권장 사항은 이 다른 문서를 다시 한 번 참조하시기 바랍니다:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

컴퓨터 키보드를 통해 passphrase을 입력하려면 제공된 필드에 입력한 다음 "*passphrase Wallet* 액세스"를 클릭합니다.



![Image](assets/fr/05.webp)



그러면 Hardware Wallet에 passphrase이 표시됩니다. 계속하려면 화면을 클릭하기 전에 실제 백업(종이 또는 금속)과 일치하는지 확인하세요.



![Image](assets/fr/06.webp)



이렇게 하면 passphrase로 보호된 Wallet에 액세스할 수 있습니다.



![Image](assets/fr/07.webp)



트레저에서만 passphrase를 입력하여 보안을 강화하려면 메시지가 표시되면 "*트레저에 passphrase 입력*"을 클릭하세요.



![Image](assets/fr/08.webp)



Trezor에 T9 키보드가 나타나 passphrase을 입력할 수 있습니다. 입력을 완료했으면 Green 체크 표시를 클릭하여 passphrase을 Wallet에 적용합니다.



![Image](assets/fr/09.webp)



그러면 passphrase 보안 Wallet에 액세스할 수 있습니다.



![Image](assets/fr/10.webp)



Sparrow wallet을 사용하려면 절차는 비슷하지만 모델 T, Safe 3 및 Safe 5의 경우 컴퓨터 키보드가 아닌 Hardware Wallet에 passphrase을 입력해야 합니다.



Sparrow wallet이 트레저에 액세스해야 하는데 마지막 시작 이후 아직 passphrase가 적용되지 않은 경우, T9 키보드를 사용하여 입력해야 합니다.



![Image](assets/fr/11.webp)



## 모델 1에 passphrase 추가하기



모델 1에서는 passphrase BIP39를 사용하는 것이 거의 필수적입니다. 이 장치에는 secure element이 통합되어 있지 않기 때문에 민감한 정보를 비교적 쉽게 추출할 수 있습니다. 따라서 물리적 공격에 강하지 않습니다. 하지만 전원이 꺼진 후에는 passphrase가 디바이스에 남아 있지 않으므로 강력한(무력화되지 않는) passphrase를 사용하면 이 모델에 대해 알려진 대부분의 물리적 공격으로부터 사용자를 보호할 수 있습니다.



모델 1에서는 passphrase를 Hardware Wallet에 직접 입력할 수 없습니다. 컴퓨터 키보드를 통해 입력해야 합니다.



Wallet을 생성하고 Mnemonic을 저장한 후 비밀번호를 설정하면 트레저 스위트 홈 메뉴로 이동합니다. 왼쪽 상단에 passphrase BIP39를 활성화하라는 창이 나타납니다.



![Image](assets/fr/12.webp)



이 창이 나타나지 않으면 설정의 "*장치*" 탭에서 "*passphrase*" 옵션을 활성화해야 합니다.



![Image](assets/fr/13.webp)



이 창에서 passphrase를 입력하라는 메시지가 표시됩니다. 강력한 passphrase를 선택하고 즉시 종이나 금속과 같은 매체에 물리적인 백업을 만드세요. 이 예에서는 `fH3&kL@9mP#2sD5qR!82`라는 passphrase를 선택했습니다. 이것은 예시일 뿐이므로 조금 더 긴 passphrase를 선택하는 것이 좋습니다. 30~40자 정도가 가장 이상적입니다(좋은 비밀번호처럼).



passphrase 선택에 대한 보다 구체적인 권장 사항은 이 다른 글을 다시 한 번 참조하시기 바랍니다:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

제공된 필드에 passphrase을 입력한 다음 "*passphrase Wallet*에 액세스" 버튼을 클릭합니다.



![Image](assets/fr/14.webp)



Hardware Wallet에 passphrase가 표시됩니다. 실제 백업(종이 또는 금속)과 일치하는지 확인한 다음 오른쪽 버튼을 클릭하여 계속 진행하세요.



![Image](assets/fr/15.webp)



그러면 passphrase로 보호되는 Wallet으로 이동합니다.



![Image](assets/fr/16.webp)



이후 Sparrow wallet을 사용하려면 절차는 동일하게 유지됩니다. Sparrow이 Hardware Wallet에 액세스해야 하고 장치를 마지막으로 시작한 이후 passphrase를 입력하지 않은 경우 매번 입력해야 합니다.



![Image](assets/fr/17.webp)



이제 트레저 하드웨어 지갑에서 passphrase BIP39를 빠르게 사용하실 수 있게 되었습니다. Wallet의 보안을 한 단계 더 강화하고 싶으시다면 트레저의 *멀티 공유* 백업 시스템(*샤미르의 비밀 공유 체계*)에 대한 튜토리얼을 확인해보세요:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!