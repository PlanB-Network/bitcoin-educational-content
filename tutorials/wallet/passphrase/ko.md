---
name: BIP-39 Passphrase
description: passphrase의 작동 방식 이해
---
![cover](assets/cover.webp)


## BIP39 passphrase란 무엇인가요?


HD 지갑은 일반적으로 12개 또는 24개의 단어로 구성된 Mnemonic 구문으로 생성됩니다. 이 구문은 물리적 매체(예: Hardware Wallet)가 분실된 경우 Wallet의 모든 키를 복원할 수 있기 때문에 매우 중요합니다. 그러나 이 문구가 손상되면 공격자가 모든 비트코인을 훔칠 수 있기 때문에 단일 실패 지점에 해당합니다.


![PASSPHRASE BIP39](assets/notext/01.webp)


이때 passphrase이 등장합니다. 이는 사용자가 자유롭게 선택할 수 있는 선택적 비밀번호로, 키 파생 과정에서 Mnemonic 문구에 추가되어 Wallet의 보안을 강화합니다.


![PASSPHRASE BIP39](assets/notext/02.webp)


passphrase을 Hardware Wallet의 PIN 코드 또는 컴퓨터에서 Wallet에 대한 액세스를 잠금 해제하는 데 사용되는 비밀번호와 혼동하지 않도록 주의하세요. Elements과 달리 passphrase은 Wallet의 키를 생성하는 데 중요한 역할을 합니다. **즉, 이 키가 없으면 비트코인을 복구할 수 없습니다**


passphrase은 Mnemonic 구문과 함께 작동하여 키가 생성되는 seed을 변경합니다. 따라서 누군가 12단어 또는 24단어 구문을 입수하더라도 passphrase이 없으면 자금에 액세스할 수 없습니다. **passphrase을 사용하면 기본적으로 고유한 키를 가진 새로운 Wallet이 생성됩니다. passphrase을 조금이라도 수정하면 generate가 다른 Wallet으로 변경됩니다.**


## passphrase을 사용해야 하는 이유는 무엇인가요?


passphrase는 임의이며 사용자가 선택한 모든 문자를 조합할 수 있습니다. 따라서 passphrase를 사용하면 몇 가지 장점이 있습니다. 첫째, 자금에 접근하기 위해 두 번째 요소(도난, 집 접근 등)를 요구함으로써 Mnemonic 문구의 유출과 관련된 모든 위험을 줄일 수 있습니다.


다음으로, 악명 높은 "*$5 렌치 공격*"과 같은 물리적 제약에 대처하기 위해 전략적으로 미끼 Wallet을 생성하여 자금을 훔치는 데 사용할 수 있습니다. 이 시나리오에서는 잠재적 공격자를 만족시키기에 충분한 소량의 비트코인이 포함된 passphrase을 숨긴 채 Wallet을 보유하는 것입니다. 후자는 동일한 Mnemonic 문구를 사용하지만 추가 passphrase로 보안을 유지합니다.


마지막으로, Wallet의 seed 세대의 무작위성을 제어하고자 할 때 passphrase를 사용하는 것이 흥미롭습니다.


## 좋은 passphrase을 선택하는 방법은?

passphrase이 효과를 발휘하려면 충분히 길고 무작위여야 합니다. 강력한 비밀번호와 마찬가지로, 무차별 암호 대입 공격이 불가능하도록 다양한 문자, 숫자, 기호가 포함된 가능한 한 길고 무작위로 구성된 passphrase을 선택하는 것이 좋습니다.


2019년 Trezor에서 실시한 연구](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af)에 따르면, seed에 액세스하고 AWS에서 대여한 하이엔드 GPU(NVIDIA Tesla V100)를 사용하는 공격자는 1달러로 약 6억 2천만 개의 비밀번호를 테스트할 수 있다고 합니다. 대략적인 추정치로, 2019년 기능으로 12개의 무작위 소문자로 구성된 passphrase를 해독하는 데 평균 **7700만 달러**가 소요될 것으로 예상됩니다.


하지만 12자로 제한하지 않는 것이 좋습니다. 대신 2025년에는 숫자, 소문자, 대문자, 기호를 포함한 13자 이상(소문자와 대문자만 사용하는 경우 14자 이상)의 무작위 문자로 구성된 강력한 비밀번호를 목표로 하세요. 물론, 향후 상황을 예측하고 이 연구에서 고려하지 않은 인적 위험을 고려하기 위해 기호를 포함한 20자 passphrase을 선택하는 등 더 높은 수준을 목표로 하는 것이 좋습니다.


passphrase 문구와 같은 방식으로 이 Mnemonic을 올바르게 저장하는 것도 중요합니다. **분실하면 비트코인에 대한 액세스 권한을 잃게 됩니다**. 분실 위험이 비합리적으로 증가하므로 머릿속으로만 외우지 않는 것을 강력히 권장합니다. 가장 이상적인 방법은 Mnemonic 문구와 분리된 물리적 매체(종이 또는 금속)에 적어두는 것입니다. 이 백업본은 Mnemonic 문구를 보관하는 곳과 다른 곳에 보관하여 두 가지가 동시에 손상되는 것을 방지해야 합니다.


## 튜토리얼


Ledger 디바이스(Stax, Flex 또는 Nano)에서 passphrase를 설정하려면 이 튜토리얼을 참조하세요:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

콜드카드에서:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

제이드 플러스에서:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

여권(배치 2):


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Trezor 장치(Safe 3, Safe 5 또는 모델 1)에서:


https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42