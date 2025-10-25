---
name: Trezor Safe 5
description: Hardware Wallet Safe 5 구성 및 사용
---
![cover](assets/cover.webp)



*이미지 출처: [Trezor.io](https://trezor.io/)*


![video](https://youtu.be/LI_EMXn6_Ss)


트레저 세이프 5는 사토시랩스에서 설계하여 2024년에 출시한 최신형 Hardware Wallet입니다. 인체공학 및 내구성에 중점을 둔 Safe 3의 고급 버전으로 포지셔닝됩니다. 이전 모델인 Safe 3와 동일한 안전 기술이 적용되었으며, 모델 1 및 모델 T와 비교하여 안전성이 향상되었습니다.



169유로의 가격으로 책정된 Safe 5는 고급 Hardware Wallet 카테고리에 속하며, Coldcard, Ledger Nano X 및 Flex, Jade Plus, Passport 및 Bitbox와 같은 모델과 경쟁합니다.



Safe 5는 충격과 긁힘에 강한 *고릴라 글래스*로 보호되는 1.54인치 컬러 터치스크린이 특징입니다. 또한 터치 시 미세한 진동을 발생시키는 *트레저 터치* 햅틱 엔진이 탑재되어 있습니다. Safe 3와 마찬가지로 secure element가 통합되어 있으며 USB-C 연결을 통해 작동하며 마이크로 SD 포트가 추가되었습니다.



Safe 3와 Safe 5의 주요 차이점은 안전 측면을 제외하면 기기의 품질에 있습니다. 더 부드러운 작동과 더 편안한 화면으로 사용자 경험을 크게 향상시킵니다. 안전성 측면에서는 동등합니다.



![Image](assets/fr/01.webp)



Safe 5는 passphrase BIP39의 뛰어난 통합을 포함하여 우수한 Hardware Wallet에서 기대할 수 있는 모든 필수 기능을 갖추고 있습니다. 하지만 아직 미니스크립트는 지원하지 않습니다.



이 모델은 특히 초보자와 중급 사용자에게 적합합니다. 반면, 콜드카드와 같은 장치에서 사용할 수 있는 보다 구체적인 기능을 원하는 고급 사용자의 기대치를 모두 충족시키지 못할 수도 있습니다. 그럼에도 불구하고 이러한 고급 옵션이 필요하지 않다면 트레저 세이프 5는 훌륭한 선택이 될 수 있습니다.



## 트레저 세이프 5 안전 모델



Safe 3와 마찬가지로 Trezor Safe 5에는 모델 1 및 모델 T와 같은 이전 모델보다 크게 발전한 EAL6+ 인증 **secure element**이 장착되어 있습니다. 이 칩은 seed을 직접 저장하지는 않지만 암호화 구성 요소로 작동하여 액세스를 보호하는 OPTIGA Trust M V3 칩입니다. secure element은 사용자가 PIN을 올바르게 입력한 경우에만 액세스할 수 있는 비밀을 유지합니다. 그런 다음 이 비밀은 디바이스의 메인 메모리에 암호화된 상태로 저장된 seed의 암호를 해독하는 데 사용됩니다.



이 하이브리드 보안 시스템은 특히 모델 1이 취약했던 문제인 추출 공격이나 침입 분석에 대해 향상된 물리적 보호 기능을 제공하며, 특히 PIN 관리에서 취약했습니다. 이러한 취약점은 이제 secure element을 사용하여 우회할 수 있습니다. 이 모델은 또한 오픈 소스 소프트웨어 아키텍처를 유지하여 개인 키의 생성 및 사용을 관리하는 코드에 완전히 액세스하고 검증할 수 있습니다. OPTIGA 칩은 Bitcoin Wallet 키 관리의 외부 요소인 PIN 코드만 관리합니다. seed를 해독하는 데 사용할 수 있는 비밀을 공개하는 것으로 제한됩니다. 또한, OPTIGA Trust M V3 칩은 상대적으로 무료 라이선스의 혜택을 누리며, SatoshiLabs는 잠재적인 취약점을 자유롭게 공개할 수 있습니다(NDA-Free).



제 생각에 이 보안 모델은 현재 시장에서 사용할 수 있는 최고의 절충안 중 하나입니다. secure element의 장점과 오픈소스 소프트웨어 관리의 장점을 결합한 것입니다. 이전에는 사용자가 칩을 통한 강화된 물리적 보안과 오픈소스를 통한 투명성 중 하나를 선택해야 했지만, 트레저 세이프에서는 이 두 가지를 모두 누릴 수 있습니다.



이 튜토리얼에서는 트레저 세이프 5를 안전하게 구성하고 사용하는 방법을 알아보세요.



## 트레저 세이프 5 개봉기



Safe 5를 받으면 상자와 Seal가 손상되지 않았는지 확인하여 포장이 개봉되지 않았는지 확인하세요. 나중에 장치를 설정할 때 장치의 진위 여부와 무결성에 대한 소프트웨어 검사도 수행됩니다.



상자 내용물은 다음과 같습니다:




- 트레저 세이프 5;
- Mnemonic 문구, 스티커, 설명서를 기록할 수 있는 카드지가 들어 있는 파우치입니다;
- USB-C to USB-C 케이블.



트레저 세이프 5를 개봉하면 보호용 플라스틱으로 보호되어 있어야 하며, USB-C 포트는 홀로그램 Seal으로 고정되어 있어야 합니다. 그것이 있는지 확인하세요.



![Image](assets/fr/02.webp)



기기의 탐색 기능은 매우 직관적입니다:




- 앞으로 이동하려면 화면 하단을 터치합니다;
- 아래로 슬라이드하여 뒤로 이동합니다 ;
- 화면을 길게 눌러 작업을 확인합니다.



## 전제 조건



이 튜토리얼에서는 트레저 세이프 5를 [Sparrow wallet Wallet 관리 소프트웨어](https://sparrowwallet.com/download/)와 함께 사용하는 방법을 보여드리겠습니다. 아직 이 소프트웨어를 설치하지 않았다면 지금 설치하세요. 도움이 필요하시면 Sparrow wallet 구성에 대한 자세한 튜토리얼도 있습니다:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

또한 Safe 5를 구성하고, 정품 여부를 확인하고, 펌웨어를 설치하려면 Trezor Suite 소프트웨어가 필요합니다. 이 소프트웨어는 해당 용도로만 사용되며 이후에는 펌웨어 업데이트에만 필요합니다. Wallet의 일상적인 관리에는 Bitcoin에 최적화되어 있고 초보자도 쉽게 사용할 수 있는 Sparrow wallet를 독점적으로 사용할 것입니다(Sparrow은 알트코인이 아닌 Bitcoin만 지원).



[공식 웹사이트에서 트레저 스위트 다운로드](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



이 두 프로그램의 경우, 컴퓨터에 설치하기 전에 (GnuPG를 통해) 진위 여부와 (Hash을 통해) 무결성을 모두 확인할 것을 강력히 권장합니다. 이 작업을 수행하는 방법을 모르는 경우 이 다른 튜토리얼 을 참조하세요:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 트레저 세이프 5 시작하기



Trezor Suite와 Sparrow wallet가 이미 설치된 컴퓨터에 Safe 5를 연결합니다.



![Image](assets/fr/04.webp)



트레저 스위트를 연 다음 "*내 트레저 설정하기*"를 클릭합니다.



![Image](assets/fr/05.webp)



"*Bitcoin 전용 펌웨어*"를 선택한 다음 "*Bitcoin 전용 설치*"를 클릭합니다.



![Image](assets/fr/06.webp)



그러면 Trezor Suite가 Safe 5에 펌웨어를 설치합니다. 설치하는 동안 잠시 기다려주세요.



![Image](assets/fr/07.webp)



"*계속*"을 클릭합니다.



![Image](assets/fr/08.webp)



그런 다음 진위 테스트를 진행하여 Hardware Wallet이 위조 또는 손상되지 않았는지 확인합니다.



![Image](assets/fr/09.webp)



Safe 5에서 화면을 눌러 확인합니다.



![Image](assets/fr/10.webp)



트레저가 정품인 경우, 트레저 스위트에서 확인 메시지가 나타납니다.



![Image](assets/fr/11.webp)



그런 다음 기본 작동 지침이 있는 창을 건너뛸 수 있습니다.



![Image](assets/fr/12.webp)



## Bitcoin Wallet 생성



트레저 스위트에서 "*새 Wallet* 만들기" 버튼을 클릭합니다.



![Image](assets/fr/13.webp)



표준 BIP39 Wallet을 만들려면 먼저 드롭다운 메뉴에서 "*레거시 Wallet 백업 유형*"을 선택한 다음 12단어 또는 24단어 Mnemonic 문구 중 하나를 선택합니다(현재 12단어 권장). 이렇게 하면 클래식 싱글사인 Wallet을 만들 수 있습니다. 검색을 용이하게 하고 특정 환경으로 제한되는 것을 피하기 위해 여기에서 BIP39 준수 매개변수를 선택하는 것이 좋습니다. 완료하려면 "*Wallet* 만들기"를 클릭합니다.



다중 공유 백업*을 포함하여 Trezor에서 사용할 수 있는 다른 백업 옵션에 대해 자세히 알아보려면 이 튜토리얼도 참조하는 것이 좋습니다:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Hardware Wallet의 이용 약관에 동의합니다.



![Image](assets/fr/15.webp)



화면을 길게 눌러 새 Wallet을 생성합니다.



![Image](assets/fr/16.webp)



트레저 스위트에서 "*백업 계속*"을 클릭합니다.



![Image](assets/fr/17.webp)



이 소프트웨어는 Mnemonic 문구를 관리하는 방법에 대한 지침을 제공합니다.



이 Mnemonic는 모든 비트코인에 대한 완전한 무제한 액세스를 제공합니다. 이 문구를 소유한 사람은 트레저 금고 5에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다.



12단어 문구는 Hardware Wallet의 분실, 도난 또는 파손 시 비트코인에 대한 액세스를 복원합니다. 따라서 신중하게 보관하고 안전한 장소에 보관하는 것이 매우 중요합니다.



상자에 동봉된 판지에 적거나, 화재, 홍수 또는 붕괴로부터 보호하기 위해 스테인리스 스틸 베이스에 각인하는 것을 추천합니다.



지침을 확인한 후 "*Wallet 백업 생성*" 버튼을 클릭합니다.



![Image](assets/fr/18.webp)



Safe 5는 난수 생성기를 사용하여 Mnemonic 문구를 생성합니다. 이 작업 중에는 감시당하고 있지 않은지 확인하세요. 화면에 표시된 단어를 원하는 물리적 매체에 적습니다. 보안 전략에 따라 문구를 여러 장 복사하는 것도 고려할 수 있지만, 무엇보다도 문구를 나누지 마세요. 단어에 번호를 매기고 순차적인 순서를 유지하는 것이 중요합니다.



**이 튜토리얼에서는 이 단어를 인터넷에서 절대 공유해서는 안 됩니다. 이 예제 Wallet은 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다**



Mnemonic 문구를 저장하고 관리하는 올바른 방법에 대한 자세한 내용은 특히 초보자라면 이 다른 튜토리얼을 따르는 것이 좋습니다:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



다음 단어로 이동하려면 화면 하단을 클릭합니다. 아래로 슬라이드하면 뒤로 돌아갈 수 있습니다. 모든 단어를 적고 나면 화면에 손가락을 계속 대고 있으면 다음 단계로 넘어갈 수 있습니다.



![Image](assets/fr/20.webp)



Mnemonic 문구의 단어를 순서에 따라 선택하여 올바르게 적었는지 확인합니다.



![Image](assets/fr/21.webp)



이 확인 절차가 완료되면 화면을 클릭하여 계속 진행합니다.



![Image](assets/fr/22.webp)



## PIN 코드 설정



다음 단계는 PIN 코드 단계입니다. PIN 코드는 트레저의 잠금을 해제합니다. 따라서 무단 물리적 액세스로부터 보호할 수 있습니다. 이 PIN 코드는 Wallet의 암호화 키를 생성하는 데 관여하지 않습니다. 따라서 PIN 코드에 액세스할 수 없더라도 12단어 Mnemonic 문구를 소지하고 있으면 비트코인에 다시 액세스할 수 있습니다.



트레저 스위트에서 "*비밀번호 계속*"을 클릭한 다음 "*비밀번호 설정*" 버튼을 클릭합니다.



![Image](assets/fr/23.webp)



안전 5로 확인합니다.



![Image](assets/fr/24.webp)



가능한 한 무작위로 PIN 코드를 선택하는 것이 좋습니다. 이 코드는 트레저가 저장된 곳과 별도의 위치(예: 비밀번호 관리자)에 저장하세요. 8자리에서 50자리 사이의 PIN 코드를 정의할 수 있습니다. 보안을 강화하기 위해 가능한 한 긴 PIN 코드를 선택하는 것이 좋습니다.



터치패드를 사용하여 비밀번호를 입력합니다.



![Image](assets/fr/25.webp)



완료되면 오른쪽 하단의 Green 체크 표시를 클릭한 다음 비밀번호를 다시 한 번 확인합니다.



![Image](assets/fr/26.webp)



PIN 코드가 등록되었습니다.



![Image](assets/fr/27.webp)



트레저 스위트에서 "*설정 완료*" 버튼을 클릭합니다.



![Image](assets/fr/28.webp)



이제 Safe 5의 구성이 완료되었습니다. 원하는 경우 Hardware Wallet의 이름과 홈 페이지를 변경할 수 있습니다.



![Image](assets/fr/29.webp)



Hardware Wallet에서 정기 펌웨어 업데이트를 수행하거나 복구 테스트를 실행하려는 경우를 제외하고는 더 이상 Trezor Suite 소프트웨어가 필요하지 않습니다. 이 소프트웨어는 Bitcoin 전용으로 사용하기에 완벽하게 적합하므로 이제 Sparrow를 사용하여 Wallet을 관리할 것입니다.



## Sparrow wallet에서 Wallet 설정하기



아직 설치하지 않았다면 [공식 웹사이트](https://sparrowwallet.com/)에서 Sparrow wallet을 다운로드하여 컴퓨터에 설치하는 것으로 시작하세요.



Sparrow wallet를 열었으면 소프트웨어가 Interface의 오른쪽 하단에 있는 체크 표시가 있는 Bitcoin 노드에 연결되어 있는지 확인합니다. Sparrow 연결에 문제가 있는 경우 이 튜토리얼의 시작 부분을 참조하는 것이 좋습니다:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

"*파일*" 탭을 클릭한 다음 "*새 Wallet*"을 클릭합니다.



![Image](assets/fr/30.webp)



Wallet의 이름을 지정한 다음 "*Wallet 만들기*"를 클릭합니다.



![Image](assets/fr/31.webp)



"*스크립트 유형*" 드롭다운 메뉴에서 비트코인을 보호하는 데 사용할 스크립트 유형을 선택합니다. "*Taproot*" 또는 "*Native SegWit*"을 권장합니다.



![Image](assets/fr/32.webp)



"*연결된 Hardware Wallet*" 버튼을 클릭합니다. 물론 Safe 5가 컴퓨터에 연결되어 있고 잠금이 해제되어 있어야 합니다.



Sparrow wallet가 열려 있는 컴퓨터에 Safe 5를 연결하면 Hardware Wallet 화면에 passphrase BIP39를 입력하라는 메시지가 표시됩니다. 이 고급 옵션은 향후 튜토리얼에서 다룰 예정입니다. 지금은 오른쪽 상단에 있는 Green 체크 표시를 클릭하여 빈 passphrase(즉, passphrase가 없는 상태)를 사용하겠다는 것을 확인하면 됩니다. 트레저를 시작할 때마다 passphrase를 입력하라는 메시지를 표시하지 않으려면 트레저 스위트로 이동하여 설정에 액세스하고 "*장치*"에서 옵션을 변경하세요 > "*Wallet 기본값*"을 "*passphrase*" 대신 "*표준*"으로 변경하세요.



![Image](assets/fr/33.webp)



"*스캔*" 버튼을 클릭합니다. Safe 5가 나타납니다. "*키 저장소 가져오기*"를 클릭합니다.



![Image](assets/fr/34.webp)



이제 첫 번째 계정의 확장 공개키를 포함하여 Wallet의 세부 정보를 확인할 수 있습니다. "*적용*" 버튼을 클릭하여 Wallet 생성을 완료합니다.



![Image](assets/fr/35.webp)



Sparrow wallet에 안전하게 액세스하려면 강력한 비밀번호를 선택하세요. 이 비밀번호는 Sparrow wallet 데이터에 안전하게 액세스하여 무단 액세스로부터 공개 키, 주소, 레이블 및 거래 내역을 보호합니다.



이 비밀번호를 잊지 않도록 비밀번호 관리자에 저장해 두는 것이 좋습니다.



![Image](assets/fr/36.webp)



이제 Wallet을 Sparrow wallet으로 가져왔습니다!



![Image](assets/fr/37.webp)



Wallet에서 첫 비트코인을 받기 전에 **비어 있는 복구 테스트를 수행할 것을 강력히 권장합니다**. Xpub과 같은 몇 가지 참조 정보를 적어둔 다음, Wallet가 비어 있는 상태에서 트레저 세이프 5를 초기화하세요. 그런 다음 종이 백업을 사용하여 Trezor에서 Wallet를 복원해 보세요. 복원 후 생성된 xpub이 원래 기록했던 것과 일치하는지 확인하세요. 일치한다면 종이 백업이 안정적이라고 안심할 수 있습니다.



복구 테스트를 수행하는 방법에 대해 자세히 알아보려면 이 다른 튜토리얼을 참조하세요:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 트레저 세이프 5로 비트코인을 받으려면 어떻게 해야 하나요?



Sparrow에서 "*수신*" 탭을 클릭합니다.



![Image](assets/fr/38.webp)



Sparrow wallet가 제안한 Address을 사용하기 전에 트레저의 화면에서 이를 확인하세요. 이를 통해 Sparrow에 표시된 Address이 가짜가 아닌지, Address으로 보호된 비트코인을 사용하는 데 필요한 개인키를 Hardware Wallet가 실제로 보유하고 있는지 확인할 수 있습니다. 이를 통해 여러 유형의 공격을 피할 수 있습니다.



이 확인을 수행하려면 "*Address 표시*" 버튼을 클릭합니다.



![Image](assets/fr/39.webp)



트레저에 표시된 Address이 Sparrow wallet에 표시된 것과 일치하는지 확인하세요. 또한 Address을 발신자에게 전달하기 직전에 이 확인을 수행하여 유효성을 확인하는 것이 좋습니다. 화면을 눌러 확인하면 됩니다.



![Image](assets/fr/40.webp)



그런 다음 "*라벨*"을 추가하여 이 Address로 보호할 비트코인의 출처를 설명할 수 있습니다. 이는 UTXO를 더 잘 관리할 수 있는 좋은 방법입니다.



![Image](assets/fr/41.webp)



그런 다음 이 Address를 사용하여 비트코인을 받을 수 있습니다.



![Image](assets/fr/42.webp)



## 트레저 세이프 5로 비트코인을 어떻게 전송하나요?



이제 세이프 5 보안 Wallet로 첫 Sats를 받으셨으니, 이제 사용하실 수 있습니다! 트레저를 컴퓨터에 연결하고 PIN 코드로 잠금을 해제하고 Sparrow wallet을 실행한 다음 "*보내기*" 탭으로 이동하여 새 트랜잭션을 생성하세요.



![Image](assets/fr/43.webp)



Coin 제어*, 즉 트랜잭션에서 소비할 UTXO를 구체적으로 선택하려면 "*UTXO*" 탭으로 이동하세요. 사용하고자 하는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다. "*송금*" 탭의 동일한 화면으로 리디렉션되지만, 트랜잭션에 대해 이미 UTXO가 선택된 상태로 표시됩니다.



![Image](assets/fr/44.webp)



목적지 Address을 입력합니다. "*+ 추가*" 버튼을 클릭하여 여러 주소를 입력할 수도 있습니다.



![Image](assets/fr/45.webp)



이 비용의 목적을 기억하기 위해 "*라벨*"을 적어 두세요.



![Image](assets/fr/46.webp)



이 Address로 송금할 금액을 선택합니다.



![Image](assets/fr/47.webp)



현재 시장에 따라 거래 수수료율을 조정하세요. 예를 들어, [Mempool.space](https://Mempool.space/)를 사용하여 적절한 수수료율을 선택할 수 있습니다.



모든 트랜잭션 매개변수가 올바른지 확인한 다음 "*거래 생성*"을 클릭합니다.



![Image](assets/fr/48.webp)



모든 것이 만족스럽다면 "*서명을 위한 거래 마무리*"를 클릭합니다.



![Image](assets/fr/49.webp)



"*서명*"을 클릭합니다.



![Image](assets/fr/50.webp)



Trezor Safe 5 옆의 "*서명*"을 클릭합니다.



![Image](assets/fr/51.webp)



Hardware Wallet 화면에서 수취인 Address, 송금 금액, 수수료 등 거래 매개변수를 확인합니다. 트레저에서 거래가 확인되면 화면을 길게 눌러 서명합니다.



![Image](assets/fr/52.webp)



이제 트랜잭션이 서명되었습니다. 모든 것이 정상인지 다시 한 번 확인한 다음 "*거래 브로드캐스트*"를 클릭하여 Bitcoin 네트워크에 브로드캐스트합니다.



![Image](assets/fr/53.webp)



Sparrow wallet의 "*거래*" 탭에서 찾을 수 있습니다.



![Image](assets/fr/54.webp)



이제 트레저 세이프 5와 Sparrow wallet의 기본 사용법을 익히셨으니 축하드립니다! 한 단계 더 나아가고 싶으시다면 트레저 Hardware Wallet과 passphrase BIP39를 함께 사용하여 안전을 강화하는 방법에 대한 종합적인 튜토리얼을 추천합니다:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!