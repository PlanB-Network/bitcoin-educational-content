---
name: BIP-39 Passphrase SeedSigner
description: 시드사인 포트폴리오에 passphrase을 추가하려면 어떻게 해야 하나요?
---

![cover](assets/cover.webp)



passphrase BIP39는 니모닉 문구와 결합하여 결정론적 및 계층적 Bitcoin 지갑에 추가적인 보안 계층을 제공하는 선택적 암호입니다. 이 튜토리얼에서는 시드서명과 함께 사용하는 Bitcoin wallet에 passphrase를 설정하는 방법을 함께 알아보겠습니다.



![Image](assets/fr/01.webp)



## 암호 문구를 추가하기 전 전제 조건



이 튜토리얼을 시작하기 전에 passphrase 개념, 작동 방식, Bitcoin wallet에 미치는 영향에 대해 잘 모르신다면, 제가 모든 것을 설명한 다른 이론 문서를 참조하시기 바랍니다(작동 방식을 완전히 이해하지 않고 passphrase를 사용하면 비트코인이 위험에 처할 수 있으므로 매우 중요합니다):



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

이 튜토리얼을 시작하기 전에 시드사인을 이미 초기화하고 니모닉 문구를 생성했는지 확인하세요. 초기화하지 않았고 시드서명기를 처음 사용하는 경우 Plan ₿ 아카데미의 튜토리얼을 따르세요. 이 단계를 완료한 후에는 이 튜토리얼로 돌아올 수 있습니다:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 시드서명자에 passphrase을 추가하려면 어떻게 하나요?



시드서명을 통해 관리되는 포트폴리오에 passphrase를 추가하면 완전히 새로운 포트폴리오가 생성되어 완전히 별도의 키 세트가 생성됩니다. 따라서 이미 수능이 포함된 포트폴리오가 있는 경우, 완전히 다른 포트폴리오가 생성되므로 passphrase를 사용하면 더 이상 해당 포트폴리오에 액세스할 수 없습니다.



시드사인에 passphrase을 적용하려면 기기를 켜고 평소처럼 시드QR을 스캔하세요. 그러면 시드서명기에 현재 wallet의 지문이 표시되며, 이는 **passphrase이 없는** 지문에 해당합니다. passphrase이 있는 wallet은 다른 지문을 갖게 됩니다.



'BIP-39 패스프레이즈' 버튼을 클릭합니다.



![Image](assets/fr/02.webp)



그런 다음 화면 키보드를 사용해 제공된 필드에 원하는 passphrase을 입력합니다. 하나 이상의 물리적 백업(종이 또는 금속)을 만들어 두시기 바랍니다. 이 passphrase을 분실하면 비트코인에 영구적으로 액세스할 수 없게 됩니다. **wallet를 복원하려면 니모닉과 passphrase이 모두 필수입니다 ** 둘 중 하나를 분실하면 비트코인이 복구할 수 없게 차단됩니다.



입력을 완료했으면 시드서명기의 오른쪽 하단에 있는 'KEY3' 버튼을 눌러 유효성을 검사합니다.



![Image](assets/fr/03.webp)



*이 예에서는 passphrase `pba`를 사용했습니다. 그러나 귀하의 경우에는 견고한 passphrase를 선택해야 합니다. 최적의 passphrase를 정의하는 방법을 알아보려면 다음 다른 문서를 참조하세요



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

그러면 시드서명이 passphrase wallet의 새 지문을 표시합니다. 이 지문을 여러 개 복사하세요: passphrase과 함께 wallet을 사용할 때는 passphrase을 입력할 때마다 입력 오류가 없었는지, 올바른 wallet에 액세스하고 있는지 확인할 수 있으므로 이 지문을 복사하는 것이 중요합니다.



예를 들어, 제 경우 시드서명기를 시작할 때 실수로 passphrase `Pba`를 `pba` 대신에 소문자에서 대문자로 변경하면 액세스하려는 포트폴리오와 완전히 다른 포트폴리오가 생성됩니다.



이 지문은 wallet의 보안이나 기밀성에 위험을 초래하지 않습니다. 공개 또는 비공개 키에 대한 어떠한 정보도 공개하지 않습니다. 따라서 니모닉 및 passphrase와 달리 지문을 디지털 매체에 저장할 수 있습니다. 종이, 비밀번호 관리자 등 여러 곳에 사본을 보관하는 것이 좋습니다.



지문을 저장한 후 '완료'를 클릭합니다.



![Image](assets/fr/04.webp)



그러면 기존 SeedSigner에서와 마찬가지로 포트폴리오의 모든 기능에 액세스할 수 있습니다.



![Image](assets/fr/05.webp)



이제 키스토어를 Sparrow Wallet으로 가져와서 wallet를 정상적으로 사용할 수 있습니다. 다시 시작할 때마다 여기에서와 같이 키보드를 사용하여 SeedQR을 스캔하고 passphrase에 다시 입력해야 합니다.



wallet을 passphrase와 함께 실제로 사용하기 전에 전체 비우기 복구 테스트를 수행할 것을 강력히 권장합니다. 이렇게 하면 니모닉 문구와 passphrase의 백업이 유효한지 확인할 수 있습니다. 이 검사를 수행하는 방법을 알아보려면 다음 튜토리얼을 참조하세요:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895