---
name: Trezor Model One
description: Hardware Wallet 모델 1 설정 및 사용
---
![cover](assets/cover.webp)



*이미지 출처: [Trezor.io](https://trezor.io/)*



트레저 모델 1은 사토시랩스가 2014년에 출시한 최초의 Hardware Wallet입니다. 출시된 지 10년이 넘었지만, 기술적으로나 예산 면에서 접근 가능한 Hardware Wallet을 찾는 사용자들에게 여전히 흥미로운 선택지입니다. 실제로 트레저 공식 웹사이트의 가격은 49유로입니다. 이 가격대의 유일한 하드웨어 지갑 중 하나입니다. 화면이 없는 탭시그너와 같은 약 20유로의 보급형 기기와 Ledger 나노 S 플러스 또는 트레저 세이프 3와 같은 약 80유로의 중급형 기기의 중간에 위치합니다.



모델 1은 0.96인치 흑백 OLED 디스플레이와 두 개의 물리적 버튼이 있습니다. 이 제품은 배터리 없이 전원 및 데이터용 마이크로 USB 연결 Exchange만 사용하여 작동합니다.



![Image](assets/fr/01.webp)



모델 1의 가장 큰 단점은 secure element가 없기 때문에 다양한 물리적 공격에 취약하다는 점이며, 그 중 일부는 비교적 간단하게 실행할 수 있는 공격입니다. 이러한 공격에는 보조 채널을 분석하여 디바이스 PIN을 알아내거나, 암호화된 seed을 추출하여 나중에 무차별 대입하는 고급 기술이 포함될 수 있습니다. 이러한 공격에는 디바이스에 물리적으로 접근해야 한다는 점에 유의하세요. 그러나 이 취약점은 견고한 passphrase BIP39를 사용하면 상당히 줄일 수 있습니다. 이 Hardware Wallet를 선택하는 경우 passphrase를 구성할 것을 강력히 권장합니다.



모델 1은 두 가지 중요한 이점을 제공합니다:




- 완전한 오픈 소스 아키텍처를 기반으로 합니다. secure element을 사용하는 최신 모델과 달리 모든 Model One 하드웨어 및 소프트웨어 구성 요소는 감사할 수 있습니다;
- 화면이 장착되어 있습니다. 제가 알기로는 이 가격대의 시장에서 디스플레이가 있는 Hardware Wallet은 이 제품이 유일합니다. 이는 서명된 정보와 수신 주소를 확인할 수 있어 많은 디지털 공격을 방지할 수 있기 때문에 매우 중요한 기능입니다.



따라서 트레저 모델 원은 제한된 예산의 초급 및 중급 사용자에게 현명한 선택이 될 수 있습니다. 하지만 secure element이 없기 때문에 물리적 보호 측면에서 한계가 있다는 점을 인지하는 것이 중요합니다. 예산이 제한되어 있다면 이 모델도 좋은 선택이지만, 79유로의 Trezor Safe 3와 같은 상위 모델을 선택할 여유가 있다면 secure element이 포함된 모델을 선택하는 것이 좋습니다.



## 트레저 모델 원 개봉하기



모델 1을 받으면 박스와 Seal이 손상되지 않았는지 확인하여 포장이 개봉되지 않았는지 확인하세요. 나중에 설정할 때 디바이스의 진위 여부와 무결성에 대한 소프트웨어 검증도 수행됩니다.



상자 내용물은 다음과 같습니다:




- 트레저 모델 1;
- Mnemonic 문구, 스티커 및 지침을 기록할 수 있는 카드지입니다;
- USB-A-마이크로 USB 케이블.



![Image](assets/fr/02.webp)



디바이스 탐색은 매우 간단합니다:




- 마우스 오른쪽 버튼을 클릭하여 확인하고 다음 단계로 진행합니다;
- 돌아가려면 왼쪽 버튼을 사용합니다.



## 전제 조건



이 튜토리얼에서는 트레저 모델 원과 [Sparrow wallet Wallet 관리 소프트웨어](https://sparrowwallet.com/download/)를 함께 사용하는 방법을 보여드리겠습니다. 아직 이 소프트웨어를 설치하지 않았다면 지금 설치하세요. 도움이 필요하시면 Sparrow wallet 구성에 대한 자세한 튜토리얼도 있습니다:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

또한 모델 1을 구성하고, 정품 여부를 확인하고, 펌웨어를 설치하려면 트레저 스위트 소프트웨어가 필요합니다. 이 소프트웨어는 이 용도로만 사용되며 이후에는 펌웨어 업데이트에만 필요합니다. Wallet의 일상적인 관리에는 Bitcoin에 최적화되어 있고 초보자도 쉽게 사용할 수 있는 Sparrow wallet를 독점적으로 사용할 것입니다(Sparrow은 알트코인이 아닌 Bitcoin만 지원).



[공식 웹사이트에서 트레저 스위트 다운로드](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



이 두 프로그램의 경우, 컴퓨터에 설치하기 전에 (GnuPG를 통해) 진위 여부와 (Hash를 통해) 무결성을 모두 확인할 것을 강력히 권장합니다. 이 작업을 수행하는 방법을 모르는 경우 이 다른 튜토리얼 을 참조하세요:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 트레저 모델 1 시작하기



트레저 스위트와 Sparrow wallet이 이미 설치되어 있는 컴퓨터에 모델 1을 연결합니다.



![Image](assets/fr/04.webp)



트레저 스위트를 연 다음 "*내 트레저 설정하기*"를 클릭합니다.



![Image](assets/fr/05.webp)



"*Bitcoin 전용 펌웨어*"를 선택한 다음 "*Bitcoin 전용 설치*"를 클릭합니다.



![Image](assets/fr/06.webp)



그러면 Trezor Suite가 모델 1에 펌웨어를 설치합니다. 설치하는 동안 잠시 기다려주세요.



![Image](assets/fr/07.webp)



"*계속*"을 클릭합니다.



![Image](assets/fr/08.webp)



## Bitcoin Wallet 생성



트레저 스위트에서 "*새 Wallet* 만들기" 버튼을 클릭합니다.



![Image](assets/fr/09.webp)



Hardware Wallet의 이용 약관에 동의합니다.



![Image](assets/fr/10.webp)



트레저 스위트에서 "*백업 계속*"을 클릭합니다.



![Image](assets/fr/11.webp)



이 소프트웨어는 Mnemonic 문구를 관리하는 방법에 대한 지침을 제공합니다.



이 Mnemonic은 모든 비트코인에 대한 완전한 무제한 액세스를 제공합니다. 이 문구를 소유한 사람은 누구나 트레저 모델 원에 물리적으로 접근하지 않아도 자금을 훔칠 수 있습니다.



24단어 문구는 Hardware Wallet의 분실, 도난 또는 파손 시 비트코인에 대한 액세스를 복원합니다. 따라서 신중하게 보관하고 안전한 장소에 보관하는 것이 매우 중요합니다.



상자에 동봉된 판지에 적거나, 화재, 홍수 또는 붕괴로부터 보호하기 위해 스테인리스 스틸 베이스에 각인하여 보안을 강화하는 것이 좋습니다.



지침을 확인한 후 "*Wallet 백업 생성*" 버튼을 클릭합니다.



![Image](assets/fr/12.webp)



모델 원은 난수 생성기를 사용하여 Mnemonic 문구를 생성합니다. 이 작업을 하는 동안 감시당하고 있지 않은지 확인하세요. 화면에 표시된 문구를 원하는 물리적 매체에 적습니다. 보안 전략에 따라 문구를 여러 장 복사하는 것도 고려할 수 있지만, 무엇보다도 문구를 나누지 마세요. 단어에 번호를 매기고 순차적인 순서를 유지하는 것이 중요합니다.



**이 튜토리얼에서는 이 단어를 인터넷에서 절대 공유해서는 안 됩니다. 이 예제 Wallet는 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다**



Mnemonic 문구를 저장하고 관리하는 올바른 방법에 대한 자세한 내용은 특히 초보자라면 이 다른 튜토리얼을 따르는 것이 좋습니다:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

다음 단어로 넘어가려면 마우스 오른쪽 버튼을 클릭합니다. 모든 단어를 적고 나면 오른쪽 버튼을 다시 클릭하여 다음 단계로 넘어갑니다.



![Image](assets/fr/13.webp)



Hardware Wallet가 다시 모든 단어를 표시합니다. 모든 단어를 적었는지 확인합니다.



![Image](assets/fr/14.webp)



## PIN 코드 설정



다음 단계는 PIN 코드 단계입니다. PIN 코드는 트레저의 잠금을 해제합니다. 따라서 무단 물리적 액세스로부터 보호할 수 있습니다. 이 PIN 코드는 Wallet의 암호화 키를 생성하는 데 관여하지 않습니다. 따라서 PIN 코드에 액세스할 수 없더라도 12단어 Mnemonic 문구를 소지하고 있으면 비트코인에 다시 액세스할 수 있습니다.



트레저 스위트에서 "*비밀번호 계속*"을 클릭한 다음 "*비밀번호 설정*" 버튼을 클릭합니다.



![Image](assets/fr/15.webp)



모델 1에서 확인합니다.



![Image](assets/fr/16.webp)



가능한 한 무작위로 PIN 코드를 선택하는 것이 좋습니다. 이 코드는 트레저가 저장된 곳과 별도의 위치(예: 비밀번호 관리자)에 저장하세요. 8자리에서 50자리 사이의 PIN 코드를 정의할 수 있습니다. 보안을 강화하기 위해 가능한 한 긴 PIN 코드를 선택하는 것이 좋습니다.



PIN 코드는 트레저 모델 1에 표시된 키보드 구성에 따라 숫자에 해당하는 점을 클릭하여 컴퓨터의 트레저 스위트에서 입력해야 합니다.



트레저 스위트 또는 Sparrow wallet을 통해 트레저 모델 1의 잠금을 해제할 때마다 이 특정 PIN 입력 방법이 필요합니다.



![Image](assets/fr/17.webp)



완료되면 "*비밀번호 입력*" 버튼을 클릭합니다.



![Image](assets/fr/18.webp)



비밀번호를 다시 적어 확인합니다.



![Image](assets/fr/19.webp)



트레저 스위트에서 "*설정 완료*" 버튼을 클릭합니다.



![Image](assets/fr/20.webp)



이제 모델 1의 구성이 완료되었습니다. 원하는 경우 Hardware Wallet의 이름과 홈 페이지를 변경할 수 있습니다.



![Image](assets/fr/21.webp)



Hardware Wallet에서 정기 펌웨어 업데이트를 수행하거나 복구 테스트를 실행하려는 경우를 제외하고는 더 이상 Trezor Suite 소프트웨어가 필요하지 않습니다. 이 소프트웨어는 Bitcoin 전용으로 사용하기에 완벽하게 적합하므로 이제 Sparrow을 사용하여 Wallet를 관리할 것입니다.



## Sparrow wallet에서 Wallet 설정하기



아직 설치하지 않았다면 [공식 웹사이트](https://sparrowwallet.com/)에서 Sparrow wallet를 다운로드하여 컴퓨터에 설치하는 것으로 시작하세요.



Sparrow wallet을 열었으면 소프트웨어가 Interface의 오른쪽 하단에 있는 체크 표시가 있는 Bitcoin 노드에 연결되어 있는지 확인합니다. Sparrow 연결에 문제가 있는 경우 이 튜토리얼의 시작 부분을 참조하는 것이 좋습니다:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

"*파일*" 탭을 클릭한 다음 "*새 Wallet*"을 클릭합니다.



![Image](assets/fr/22.webp)



Wallet의 이름을 지정한 다음 "*Wallet 만들기*"를 클릭합니다.



![Image](assets/fr/23.webp)



"*스크립트 유형*" 드롭다운 메뉴에서 비트코인을 보호하는 데 사용할 스크립트 유형을 선택합니다. "*Taproot*" 또는 "*Native SegWit*"을 권장합니다.



![Image](assets/fr/24.webp)



"*연결된 Hardware Wallet*" 버튼을 클릭합니다. 물론 모델 원은 컴퓨터에 연결되어 있어야 합니다.



![Image](assets/fr/25.webp)



"*스캔*" 버튼을 클릭합니다. 모델 1이 나타납니다.



Sparrow wallet가 열려 있는 상태에서 모델 1을 컴퓨터에 연결하면 Sparrow에 passphrase BIP39를 입력하라는 메시지가 표시됩니다. 이 고급 옵션은 향후 튜토리얼에서 다룰 예정입니다. 지금은 "*Toggle passphrase Off*"를 선택하면 트레저를 시작할 때마다 passphrase을 입력하라는 메시지가 표시되지 않도록 할 수 있습니다.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



"*키 저장소 가져오기*"를 클릭합니다.



![Image](assets/fr/27.webp)



이제 첫 번째 계정의 확장 공개키를 포함한 Wallet의 세부 정보를 확인할 수 있습니다. "*적용*" 버튼을 클릭하여 Wallet 생성을 완료합니다.



![Image](assets/fr/28.webp)



Sparrow wallet에 안전하게 액세스하려면 강력한 비밀번호를 선택하세요. 이 비밀번호는 Sparrow wallet 데이터에 안전하게 액세스하여 무단 액세스로부터 공개 키, 주소, 레이블 및 거래 내역을 보호합니다.



이 비밀번호를 잊지 않도록 비밀번호 관리자에 저장해 두는 것이 좋습니다.



![Image](assets/fr/29.webp)



이제 Wallet을 Sparrow wallet으로 가져왔습니다!



![Image](assets/fr/30.webp)



Wallet에서 첫 비트코인을 받기 전에 **빈 복구 테스트를 수행할 것을 강력히 권장합니다**. Xpub과 같은 몇 가지 참조 정보를 적어둔 다음, Wallet가 비어 있는 상태에서 트레저 모델 1을 초기화하세요. 그런 다음 종이 백업을 사용하여 Trezor에서 Wallet를 복원해 보세요. 복원 후 생성된 xpub이 원래 기록했던 것과 일치하는지 확인합니다. 일치한다면 종이 백업이 안정적이라고 안심할 수 있습니다.



복구 테스트를 수행하는 방법에 대해 자세히 알아보려면 이 다른 튜토리얼을 참조하세요:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 트레저 모델 원으로 비트코인을 받는 방법은 무엇인가요?



Sparrow에서 "*수신*" 탭을 클릭합니다.



![Image](assets/fr/31.webp)



Sparrow wallet가 제안한 Address을 사용하기 전에 트레저의 화면에서 이를 확인하세요. 이를 통해 Sparrow에 표시된 Address이 가짜가 아닌지, Hardware Wallet가 이 Address으로 보호된 비트코인을 사용하는 데 필요한 개인 키를 실제로 보유하고 있는지 확인할 수 있습니다. 이는 여러 유형의 공격을 피하는 데 도움이 됩니다.



이 확인을 수행하려면 "*Address 표시*" 버튼을 클릭합니다.



![Image](assets/fr/32.webp)



트레저에 표시된 Address이 Sparrow wallet에 표시된 것과 일치하는지 확인하세요. 또한 Address을 발신자에게 전달하기 직전에 이 확인을 수행하여 유효성을 확인하는 것이 좋습니다. 오른쪽 버튼을 눌러 확인하면 됩니다.



![Image](assets/fr/33.webp)



또한 "*라벨*"을 추가하여 이 Address로 보호할 비트코인의 출처를 설명할 수도 있습니다. 이는 UTXO를 더 잘 관리할 수 있는 좋은 방법입니다.



![Image](assets/fr/34.webp)



그런 다음 이 Address를 사용하여 비트코인을 받을 수 있습니다.



![Image](assets/fr/35.webp)



## 트레저 모델 원으로 비트코인을 전송하는 방법은 무엇인가요?



이제 보안이 설정된 Wallet 모델 1에서 첫 번째 Sats를 받았으니 이제 사용해도 됩니다! 트레저를 컴퓨터에 연결하고 Sparrow wallet을 실행한 다음 "*송금*" 탭으로 이동하여 새 트랜잭션을 생성하세요.



![Image](assets/fr/36.webp)



Coin 제어*, 즉 트랜잭션에서 소비할 UTXO를 구체적으로 선택하려면 "*UTXO*" 탭으로 이동하세요. 사용하고자 하는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다. "*송금*" 탭의 동일한 화면으로 리디렉션되지만, 트랜잭션에 대해 이미 UTXO가 선택된 상태로 표시됩니다.



![Image](assets/fr/37.webp)



목적지 Address을 입력합니다. "*+ 추가*" 버튼을 클릭하여 여러 주소를 입력할 수도 있습니다.



![Image](assets/fr/38.webp)



이 비용의 목적을 기억하기 위해 "*라벨*"을 적어 두세요.



![Image](assets/fr/39.webp)



이 Address로 송금할 금액을 선택합니다.



![Image](assets/fr/40.webp)



현재 시장에 따라 거래 수수료율을 조정하세요. 예를 들어, [Mempool.space](https://Mempool.space/)를 사용하여 적절한 수수료율을 선택할 수 있습니다.



모든 트랜잭션 매개변수가 올바른지 확인한 다음 "*거래 생성*"을 클릭합니다.



![Image](assets/fr/41.webp)



모든 것이 만족스럽다면 "*서명을 위한 거래 마무리*"를 클릭합니다.



![Image](assets/fr/42.webp)



"*서명*"을 클릭합니다.



![Image](assets/fr/43.webp)



트레저 모델 1 옆에 있는 '*서명*'을 클릭합니다.



![Image](assets/fr/44.webp)



Hardware Wallet 화면에서 수취인 Address, 송금 금액, 수수료 등 거래 매개변수를 확인합니다. 트레저에서 거래가 확인되면 마우스 오른쪽 버튼을 클릭하여 서명합니다.



![Image](assets/fr/45.webp)



이제 트랜잭션이 서명되었습니다. 모든 것이 정상인지 다시 한 번 확인한 다음 "*거래 브로드캐스트*"를 클릭하여 Bitcoin 네트워크에 브로드캐스트합니다.



![Image](assets/fr/46.webp)



Sparrow wallet의 "*거래*" 탭에서 찾을 수 있습니다.



![Image](assets/fr/47.webp)



이제 Sparrow wallet가 장착된 트레저 모델 1의 기본 사용법을 익히셨습니다! 한 단계 더 나아가기 위해 Hardware Wallet 트레저와 passphrase BIP39를 함께 사용하여 안전을 강화하는 방법에 대한 종합적인 튜토리얼을 추천합니다:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

이 튜토리얼이 유용했다면 아래에 Green 엄지 손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!