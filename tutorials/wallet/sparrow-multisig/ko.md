---
name: Sparrow Wallet - Multisig
description: Sparrow에서 다중 서명 Wallet 만들기
---
![cover](assets/cover.webp)



다중 서명 Wallet(흔히 "*Multisig*"라고도 함)은 지출을 승인하기 위해 서로 다른 키에서 여러 개의 암호화 서명이 필요한 Bitcoin Wallet 구조입니다. 하나의 개인 키로 UTXO의 잠금을 해제하는 기존("*싱글서명*") Wallet과 달리, Multisig는 **m-of-n** 모델을 기반으로 하며, Wallet에 연결된 _n_ 키 중 _m_은 각 거래에 필수적으로 공동 서명해야 합니다.



이 메커니즘을 사용하면 Wallet의 제어를 여러 주체 또는 장치 간에 공유할 수 있습니다. 예를 들어, 2대 3 구성에서는 3개의 독립적인 키 세트가 생성되지만 자금을 릴리스하는 데는 2개의 키만 필요합니다. 이 아키텍처는 키의 손상 또는 분실과 관련된 위험을 크게 줄입니다. 하나의 키에만 접근할 수 있는 도둑이 Wallet을 비울 수 없고, 하나를 분실한 사용자도 나머지 두 개로 자금에 계속 액세스할 수 있습니다.



![Image](assets/fr/01.webp)



하지만 이렇게 보안이 강화된 만큼 복잡성도 커집니다. Multisig Wallet을 설정하려면 여러 개의 Mnemonic 구문(서명 요소당 하나)과 확장 공개키("*xpub*")를 보호해야 합니다. 실제로 Multisig 2×3 Wallet을 사용하는 경우 Wallet을 검색하려면 세 개의 Mnemonic 구문을 모두 가지고 있거나 세 개의 구문 중 최소 두 개를 가지고 있어야 합니다. 그러나 세 개의 구문 중 두 개만 가지고 있는 경우, 세 개의 *xpub*에 액세스할 수 있어야 하며, 그렇지 않으면 보호하는 비트코인에 액세스하는 데 필요한 공개 키를 검색할 수 없습니다.



요약하면, Multisig Wallet을 복구하려면 다음을 수행해야 합니다:




- 또는 각 서명 요소와 관련된 모든 Mnemonic 문구에 액세스하세요;
- 서명할 수 있는 임계값에 필요한 최소한의 Mnemonic 문구를 가지고 있거나, 필요한 공개 키를 검색하기 위해 모든 요소의 xpub에 액세스할 수 있어야 합니다.



![Image](assets/fr/02.webp)



이러한 Multisig Wallet 백업 관리는 *출력 스크립트 설명자*를 통해 이루어지며, 이 설명자는 자금에 액세스하는 데 필요한 모든 공개 데이터를 함께 그룹화합니다. 그러나 이 기능은 아직 모든 Wallet 관리 소프트웨어에 구현되어 있지는 않습니다.



Multisig은 특히 상당한 양의 비트코인을 보유한 회사, 협회, 가족 또는 개인 사용자 등 보안을 강화하거나 자금을 공동으로 관리하고자 하는 비트코인 사용자에게 적합합니다. 예를 들어 여러 관리자 또는 팀원에게 서명 권한을 분산하는 등 탈중앙화된 거버넌스 체계를 만드는 데 사용할 수 있습니다.



이 튜토리얼에서는 **Sparrow wallet**를 사용하여 클래식 멀티서명 Wallet을 만들고 사용하는 방법을 배워보겠습니다. 타임록이 포함된 사용자 지정 멀티서명 Wallet을 만들고 싶다면 Liana을 사용하는 것이 좋습니다:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## 전제 조건



이 튜토리얼에서는 [Sparrow wallet Wallet 관리 소프트웨어](https://sparrowwallet.com/download/)를 사용하여 Multisig을 만드는 방법을 보여드리겠습니다. 아직 이 소프트웨어를 설치하지 않았다면 지금 설치하세요. 도움이 필요하시면 Sparrow wallet 구성에 대한 자세한 튜토리얼도 참조하세요:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

다중 서명 Wallet을 설정하려면 서로 다른 하드웨어 지갑이 필요합니다. 예를 들어 Multisig 2-de-3의 경우 를 사용할 수 있습니다:




- 트레저 모델 1;
- Ledger Flex;
- 콜드카드 MK3.



![Image](assets/fr/03.webp)



Multisig 구성에 다른 제조사의 Hardware Wallet을 사용하는 것이 좋습니다. 이렇게 하면 특정 모델에 심각한 문제가 발생하더라도 Multisig의 전반적인 안전성에 영향을 미치지 않습니다. 또한 각 디바이스의 특정 이점을 활용할 수 있습니다. 예를 들어, 제 구성에서는 :





- 트레저 모델 1은 완전한 오픈 소스이기 때문에 seed 세대를 검증할 수 있습니다. 하지만 secure element이 장착되어 있지 않기 때문에 물리적 공격에 취약한 상태입니다;





- 반면 Ledger Flex는 확인되지 않은 독점 펌웨어를 사용하지만 뛰어난 물리적 보호 기능을 제공하는 secure element가 통합되어 있습니다;





- 콜드카드에는 secure element가 장착되어 있으며 해당 코드를 검색할 수 있습니다. 다른 모델에서는 사용할 수 없는 확인 기능을 제공하기 때문에 저희 구성에 흥미로운 선택입니다.



Multisig Wallet을 구성하기 전에 각 Hardware Wallet가 올바르게 구성되었는지 확인하세요(Mnemonic 생성 및 저장, PIN 정의). 자세한 지침은 각 Hardware Wallet에 대한 튜토리얼을 참조하세요(예: 를 참조하세요):



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

이 튜토리얼의 뒷부분에서 살펴보겠지만, Hardware Wallet와 연결되지 않았지만 개인 키가 PC에 저장되어 있는 요소를 Multisig 구성에 통합할 수도 있습니다. 이 방법은 하드웨어 지갑을 독점적으로 사용하는 것보다 보안성이 떨어지지만, 특정 경우에는 적절할 수 있습니다. 예를 들어, Multisig 2-de-3의 경우 두 개의 하드웨어 지갑과 하나의 Software Wallet을 선택할 수 있습니다.



## Multisig Wallet 만들기



Sparrow wallet를 열고 "*파일*" 탭을 클릭한 다음 "*새 Wallet*"를 선택합니다.



![Image](assets/fr/04.webp)



다중 서명 Wallet에 이름을 지정한 다음 "*Wallet 만들기*"를 클릭하여 확인합니다.



![Image](assets/fr/05.webp)



"*정책 유형*" 드롭다운 메뉴에서 "*다중 서명*" 옵션을 선택합니다.



![Image](assets/fr/06.webp)



이제 오른쪽 상단에서 Multisig의 총 키 수와 비용 승인에 필요한 공동 서명자 수를 정의할 수 있습니다. 제 예에서는 2인 3조 방식입니다.



![Image](assets/fr/07.webp)



창 하단에 Sparrow wallet은 3개의 "*키스토어*"를 표시합니다. 각각은 키 세트를 나타냅니다. 여기서는 3개의 하드웨어 지갑을 사용하고 있으므로 각 "*키스토어*"는 그 중 하나에 해당합니다. 이제 이를 구성하겠습니다.



콜드카드로 시작합니다. "*키스토어 1*" 탭에서 "*에어갭 Hardware Wallet*" 옵션을 선택합니다.



![Image](assets/fr/08.webp)



콜드카드에서 기기의 잠금이 해제되면 "*설정*" 메뉴로 이동한 다음 "*Multisig 지갑*"으로 이동합니다.



![Image](assets/fr/09.webp)



이 메뉴에서는 콜드카드가 참여하는 Multisig 지갑을 관리할 수 있습니다. 새 지갑을 만들고 싶어서 "*XPUB 내보내기*"를 선택합니다.



![Image](assets/fr/10.webp)



'*계정 번호*' 입력란은 하나의 계정만 관리하는 경우 비워두고 확인 버튼을 눌러 바로 유효성을 검사할 수 있습니다.



![Image](assets/fr/11.webp)



그러면 콜드카드가 마이크로 SD 카드에 저장된 xpub이 포함된 파일을 generate로 생성합니다.



![Image](assets/fr/12.webp)



이 마이크로 SD를 컴퓨터에 삽입합니다. Sparrow wallet에서 '*콜드카드 Multisig*' 옆의 '*파일 가져오기...*' 버튼을 클릭한 다음 카드의 콜드카드에서 생성한 파일을 선택합니다.



![Image](assets/fr/13.webp)



Xpub을 성공적으로 가져왔습니다. 이제 다른 두 개의 하드웨어 지갑에 대해서도 절차를 반복하겠습니다.



![Image](assets/fr/14.webp)



Ledger Flex의 경우 "*키스토어 2*"를 선택한 다음 "*연결된 Hardware Wallet*"를 클릭합니다. Ledger이 컴퓨터에 연결되어 있고 잠금이 해제되어 있으며 Bitcoin 애플리케이션이 열려 있는지 확인합니다.



![Image](assets/fr/15.webp)



그런 다음 "*스캔...*" 버튼을 클릭합니다.



![Image](assets/fr/16.webp)



Hardware Wallet의 이름 옆에 있는 "*키 저장소 가져오기*"를 클릭합니다.



![Image](assets/fr/17.webp)



이제 두 번째 서명자가 Sparrow wallet에 올바르게 등록되었습니다.



![Image](assets/fr/18.webp)



트레저 원에서도 똑같은 절차를 반복하여 Multisig 구성을 마무리했습니다.



![Image](assets/fr/19.webp)



제 구성에서는 이 경우를 다루지 않지만, Software Wallet을 통한 서명을 Sparrow(Hot Wallet)에 포함하려면 "*새롭거나 가져온 Software Wallet*" 버튼을 클릭하기만 하면 됩니다.



이제 모든 서명 장치를 Sparrow wallet으로 가져왔으므로 "*적용*"을 클릭하여 Multisig 생성을 마무리할 수 있습니다.



![Image](assets/fr/20.webp)



Sparrow wallet Wallet에 안전하게 액세스하려면 강력한 비밀번호를 선택하세요. 이 비밀번호는 무단 액세스로부터 공개 키, 주소, 라벨 및 거래 내역을 보호합니다.



비밀번호를 분실하지 않도록 비밀번호 관리자와 같은 안전한 곳에 보관하세요.



![Image](assets/fr/21.webp)



## Multisig Wallet 백업하기



이제 *출력 스크립트 Descriptor*를 콜드카드에 저장하고(이는 Multisig에 콜드카드가 있는 사용자에게만 해당), 무엇보다도 독립된 매체에 백업을 보관하겠습니다.



Descriptor*에는 Multisig Wallet의 모든 xpub과 키를 generate에 사용하는 파생 경로가 포함되어 있습니다. 1부에서 살펴본 내용을 기억하세요: Multisig Wallet을 복원하려면 Mnemonic 구문을 **모두** 가지고 있거나 서명 임계값에 도달하는 데 필요한 최소한의 수만 가지고 있어야 합니다. 그러나 후자의 경우 누락된 서명자의 **엑스펍**도 필수입니다. Descriptor*에는 Multisig의 모든 xpub이 포함되어 있습니다.



명확하지 않은 경우, 이 점만 기억하세요. Multisig를 검색하려면 임계값에 따라 사용된 각 Hardware Wallet에 대해 최소 Mnemonic 구문 수(제 경우: 2구문)와 *Descriptor*이 필요합니다.



이 *Descriptor*에는 개인 키가 없고 공개 키만 포함되어 있습니다. 즉, 자금에 대한 액세스 권한을 부여하지 않습니다. 따라서 비트코인에 대한 전체 액세스 권한을 부여하는 Mnemonic 문구만큼 중요하지 않습니다. Descriptor*의 위험은 전적으로 기밀 유지와 관련된 것입니다. 해킹이 발생하면 제3자가 모든 거래를 관찰할 수는 있지만 자금을 사용할 수는 없습니다.



이 *Descriptor*를 여러 장 복사하여 Multisig의 각 서명 장치에 보관할 것을 강력히 권장합니다. 예를 들어 제 경우에는 *Descriptor*를 종이에 인쇄하여 한 부는 콜드카드에, 다른 한 부는 트레저에, 다른 한 부는 Ledger에 보관하고 있습니다. 또한 이 *Descriptor*를 세 개의 USB 스틱에 PDF 파일로 저장하고, 각각 하드웨어 지갑 중 하나에 저장합니다. 이렇게 하면 *Descriptor*를 잃어버릴 확률을 최소화할 수 있고, 각 장치에 두 개의 사본(실물 사본과 디지털 사본)을 가지고 있을 수 있습니다.



Multisig Wallet이 생성되면 Sparrow이 자동으로 이 *Descriptor*을 제공합니다. "*PDF 저장...*" 버튼을 클릭하여 텍스트와 QR 코드로 모두 저장하세요.



![Image](assets/fr/22.webp)



그런 다음 이 PDF를 인쇄하여 USB 스틱에 복사할 수 있습니다.



![Image](assets/fr/23.webp)



또한 이 *Descriptor*를 콜드카드에 등록합니다(구성에 콜드카드를 사용하는 경우). 이렇게 하면 Coldcard는 나중에 서명된 각 트랜잭션이 올바른 xpub, 올바른 Address 형식, 올바른 파생 경로 등 원본 Wallet에 해당하는지 확인할 수 있습니다. 이렇게 가져온 *Descriptor*가 없으면 Coldcard는 Exchange 주소가 도용되지 않았는지 또는 PSBT이 변조되지 않았는지 확인할 수 없습니다.



다른 하드웨어 지갑에서는 허용하지 않는 특정 정교한 공격에 대한 추가 확인 기능을 제공합니다(물론 서명을 위해 사용한다는 전제 하에).



Sparrow에서 "*설정*" 메뉴에 액세스한 다음 "*내보내기...*"를 클릭합니다.



![Image](assets/fr/24.webp)



"*콜드카드 Multisig*" 옵션 옆의 "*파일 내보내기...*"를 클릭하고 텍스트 파일을 마이크로 SD 카드에 저장합니다.



![Image](assets/fr/25.webp)



그런 다음 카드를 콜드카드에 삽입합니다. "*설정*" 메뉴로 이동한 다음 "*Multisig 지갑*"으로 이동하여 "*SD에서 가져오기*"를 선택합니다.



![Image](assets/fr/26.webp)



적절한 파일을 선택하고 가져오기를 확인합니다.



![Image](assets/fr/27.webp)



새로 가져온 Multisig의 이름을 클릭합니다.



![Image](assets/fr/28.webp)



Multisig 구성 매개변수를 확인한 다음 등록을 확인합니다.



![Image](assets/fr/29.webp)



이제 Multisig이 콜드카드에 올바르게 저장되었습니다. 동일한 Multisig에 여러 개의 콜드카드가 있는 경우 각 콜드카드에 대해 이 절차를 반복합니다.



Descriptor*를 저장하는 것 외에도 각 시그니처 디바이스에 대한 Mnemonic 문구를 저장하는 데 특히 주의를 기울이는 것을 잊지 마세요. 이제 막 시작하는 분이라면 다른 튜토리얼을 참조하여 올바르게 저장하고 관리하는 방법을 배우는 것이 좋습니다:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Multisig에서 첫 비트코인을 받기 전에 **빈 복구 테스트를 수행할 것을 강력히 권장합니다**. 처음 수신한 Address와 같은 몇 가지 참고 정보를 메모한 다음, Wallet이 비어 있는 상태에서 하드웨어 지갑을 초기화하세요. 그런 다음, Mnemonic 문구 종이 백업을 사용하여 하드웨어 지갑에서 Multisig Wallet을 복원하고, *Descriptor*을 사용하여 Sparrow을 복원해 보세요. 복원 후 생성된 첫 번째 Address가 원래 적어둔 것과 일치하는지 확인합니다. 일치한다면 종이 백업이 신뢰할 수 있는 것이니 안심해도 됩니다.



복구 테스트를 수행하는 방법에 대해 자세히 알아보려면 이 다른 튜토리얼을 참조하세요:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Multisig에서 비트코인 받기



이제 Wallet에서 비트코인을 받을 준비가 되었습니다. Sparrow에서 "*수신*" 탭을 클릭합니다.



![Image](assets/fr/30.webp)



Sparrow wallet에서 생성된 Address을 사용하기 전에 시간을 내어 하드웨어 지갑 화면에서 직접 확인하시기 바랍니다. 이렇게 하면 Address이 변경되지 않았는지, 기기에 관련 자금을 사용하는 데 필요한 개인키가 보관되어 있는지 확인할 수 있습니다. 이렇게 하면 여러 공격 벡터로부터 사용자를 보호하는 데 도움이 됩니다.



이렇게 하려면 "*디스플레이 Address*"을 클릭하여 트레저 또는 케이블로 연결된 경우 Address을 Ledger에 표시합니다.



![Image](assets/fr/31.webp)



콜드카드를 사용하면 Sparrow과의 상호작용 없이도 이 인증을 수행할 수 있습니다. "*Address 탐색기*" 메뉴를 연 다음 맨 아래에서 Multisig를 선택하기만 하면 됩니다.



![Image](assets/fr/32.webp)



그러면 Multisig에서 생성된 수신 주소가 표시됩니다.



![Image](assets/fr/33.webp)



각 Hardware Wallet에 표시된 Address가 Sparrow wallet에 표시된 것과 정확히 일치하는지 확인합니다. Address를 결제자와 공유하기 직전에 이 작업을 수행하여 무결성을 확인하는 것이 좋습니다.



그런 다음 이 Address에 "*라벨*"을 할당하여 수신한 비트코인의 출처를 표시할 수 있습니다. 이는 UTXO를 체계적으로 관리할 수 있는 좋은 방법입니다.



![Image](assets/fr/34.webp)



확인이 완료되면 Address을 사용하여 비트코인을 받을 수 있습니다.



![Image](assets/fr/35.webp)



## Multisig로 비트코인 보내기



이제 Multisig Wallet에서 첫 번째 Sats를 받았으니 이제 사용해도 됩니다! Sparrow에서 "*송금*" 탭으로 이동하여 새 트랜잭션을 작성합니다.



![Image](assets/fr/36.webp)



Coin 제어*를 사용하려면, 즉 지출하려는 UTXO를 수동으로 선택하려면 "*UTXO*" 탭으로 이동하세요. 사용하려는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다. "*송금*" 탭으로 자동 리디렉션되며, 이미 UTXO가 미리 채워져 있습니다.



![Image](assets/fr/37.webp)



목적지 Address을 입력합니다. "*+ 추가*"를 클릭하여 여러 주소를 추가할 수 있습니다.



![Image](assets/fr/38.webp)



이 비용의 목적을 설명하는 "*라벨*"을 추가하면 거래를 더 쉽게 추적할 수 있습니다.



![Image](assets/fr/39.webp)



선택한 Address로 송금할 금액을 입력합니다.



![Image](assets/fr/40.webp)



현재 네트워크 상태에 따라 충전 속도를 조정하세요. 예를 들어, [Mempool.space](https://Mempool.space/)를 참조하여 적절한 충전 수준을 선택하세요.



모든 트랜잭션 매개변수를 확인한 후 "*거래 생성*"을 클릭합니다.



![Image](assets/fr/41.webp)



모든 것이 만족스러우면 "*서명을 위한 거래 마무리*"를 클릭합니다.



![Image](assets/fr/42.webp)



화면 하단에 Sparrow이 2개의 서명을 기다리고 있는 것을 볼 수 있습니다. 이는 정상입니다. 여기서 사용된 Wallet은 Multisig 2-de-3입니다.



![Image](assets/fr/43.webp)



콜드카드로 서명을 시작합니다. 이렇게 하려면 컴퓨터에 Micro SD 카드를 삽입한 다음 "*거래 저장*"을 클릭합니다.



![Image](assets/fr/44.webp)



서명할 트랜잭션을 Hardware Wallet로 전송한 다음 Sparrow에서 검색하는 방법에는 3가지가 있습니다. 첫 번째는 콜드카드의 경우처럼 마이크로 SD 카드를 사용하는 것입니다. 두 번째는 케이블 연결을 이용하는 것으로, 두 번째 서명(Ledger 및 Trezor)에 사용할 것입니다. 마지막으로 콜드카드 Q, 제이드 플러스 또는 패스포트 V2와 같은 카메라가 장착된 디바이스의 경우 QR코드 통신을 사용할 수 있습니다.



PSBT(*Partially Signed Bitcoin Transaction*)을 마이크로 SD에 저장한 후 Coldcard MK3에 삽입한 다음 "*서명 준비 완료*" 메뉴를 선택합니다.



![Image](assets/fr/45.webp)



Hardware Wallet 화면에서 수취인의 Address, 송금 금액, 요금 등 거래 매개변수를 주의 깊게 확인합니다. 거래가 확인되면 유효성을 검사하여 서명을 진행합니다.



![Image](assets/fr/46.webp)



그런 다음 Micro SD를 컴퓨터로 반환하고 Sparrow에서 "*거래 로드*"를 클릭합니다. 파일에서 콜드카드가 서명한 PSBT을 선택합니다.



![Image](assets/fr/47.webp)



콜드카드 서명이 추가된 것을 볼 수 있습니다. 이제 두 번째 장치(이 경우 Ledger)를 사용하여 필요한 두 번째 서명을 수행하겠습니다. 연결하고 잠금을 해제한 다음 Sparrow에서 "*서명*"을 클릭합니다.



![Image](assets/fr/48.webp)



Hardware Wallet의 이름 옆에 있는 "*서명*"을 클릭합니다.



![Image](assets/fr/49.webp)



Ledger을 이 Multisig과 함께 처음 사용하면 Sparrow에서 공동 서명자의 확장 공개 키(xpub)를 확인하라는 메시지가 표시됩니다. 콜드카드와 마찬가지로 이 단계를 통해 나중에 맹목적으로 서명하는 것을 방지할 수 있습니다. 이 정보를 확인하려면 Ledger 화면에 표시된 xpub를 다른 하드웨어 지갑에서 직접 제공한 것과 비교하세요.



![Image](assets/fr/50.webp)



수취인의 Address, 이체 금액 및 거래 수수료를 확인한 다음 거래에 서명합니다.



![Image](assets/fr/51.webp)



화면을 눌러 서명합니다.



![Image](assets/fr/52.webp)



이제 Sparrow이 Multisig Wallet에서 자금을 릴리스하는 데 필요한 두 개의 서명을 받았습니다. 트랜잭션을 마지막으로 한 번 더 확인하고 모든 것이 정상이라면 "*거래 브로드캐스트*"를 클릭하여 네트워크를 통해 브로드캐스트합니다.



![Image](assets/fr/53.webp)



이 트랜잭션은 Sparrow wallet의 "*거래*" 탭에서 찾을 수 있습니다.



![Image](assets/fr/54.webp)



이제 Sparrow에서 다중 서명 Wallet을 설정하고 사용하는 방법을 알게 되었습니다. 이 튜토리얼이 유용했다면 아래에 Green 썸네일을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 공유해 주셔서 감사합니다!



더 나아가 Bitcoin Wallet의 보안을 강화하는 또 다른 방법인 passphrase BIP39 에 대한 이 튜토리얼을 참조하는 것이 좋습니다:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7