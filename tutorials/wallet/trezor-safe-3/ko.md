---
name: Trezor Safe 3
description: Hardware Wallet Safe 3 구성 및 사용
---
![cover](assets/cover.webp)



*이미지 출처: [Trezor.io](https://trezor.io/)*



트레저 세이프 3는 사토시랩스에서 2023년에 제작한 Hardware Wallet입니다. 초급자와 중급자 모두를 위해 설계된 매우 작고 가벼운 모델(14g)입니다. 유명한 모델 1의 후속 모델로, 주요 경쟁 제품인 Ledger와 차별화되는 브랜드의 오픈 소스 접근 방식을 유지하면서 중요한 기능이 추가되었습니다. Safe 3의 가격은 79유로입니다. 따라서 중급 Hardware Wallet 세그먼트에 위치하며 Ledger 나노 S 플러스와 직접 경쟁합니다.



Safe 3는 배터리가 없으며 전원과 통신에 모두 사용되는 USB-C 연결로만 작동합니다. 0.96인치의 작은 흑백 OLED 디스플레이와 두 개의 물리적 버튼이 있습니다.



![Image](assets/fr/01.webp)



Safe 3는 passphrase BIP39의 뛰어난 통합을 포함하여 우수한 Hardware Wallet에 기대되는 모든 필수 기능을 제공합니다. 하지만 아직 미니스크립트는 지원하지 않습니다.



이 모델은 특히 초보자에게 적합하며, 신규 사용자에게 추천하고 싶은 Hardware Wallet일 수도 있습니다. 중급 사용자에게도 적합합니다. 반면에 콜드카드와 같은 기기에서 제공되는 보다 구체적인 기능을 원하는 고급 사용자의 기대치를 모두 충족시키지는 못할 수도 있습니다. 그럼에도 불구하고 이러한 고급 옵션이 필요하지 않다면 트레저 세이프 3는 훌륭한 선택이 될 수 있습니다.



## 트레저 세이프 3 안전 모델



트레저 세이프 3에는 모델 1 및 모델 T와 같은 이전 모델보다 크게 향상된 EAL6+ 인증 **secure element**가 장착되어 있습니다. 이 칩은 seed을 직접 저장하지는 않지만 암호화 구성 요소로 작동하여 액세스를 보호하는 OPTIGA Trust M V3 칩입니다. secure element에는 사용자가 PIN을 올바르게 입력한 경우에만 액세스할 수 있는 비밀이 저장됩니다. 그런 다음 이 비밀은 디바이스의 메인 메모리에 암호화된 상태로 저장된 seed의 암호를 해독하는 데 사용됩니다.



이 하이브리드 보안 시스템은 특히 모델 1이 취약했던 문제인 추출 공격이나 침입 분석에 대해 향상된 물리적 보호 기능을 제공하며, 특히 PIN 관리에서 취약했습니다. 이러한 취약점은 이제 secure element을 사용하여 우회할 수 있습니다. 또한 이 모델은 오픈 소스 소프트웨어 아키텍처를 유지하여 개인 키의 생성 및 사용을 관리하는 코드에 완전히 액세스하고 검증할 수 있습니다. OPTIGA 칩은 Bitcoin Wallet 키 관리의 외부 요소인 PIN 코드만 관리합니다. seed의 암호를 해독하는 데 사용할 수 있는 비밀만 공개합니다. 또한, OPTIGA Trust M V3 칩은 상대적으로 무료 라이선스의 이점을 누리며, SatoshiLabs가 잠재적인 취약점을 자유롭게 공개할 수 있도록 허가합니다.



제 생각에 이 보안 모델은 현재 시장에서 사용할 수 있는 최고의 절충안 중 하나입니다. secure element의 장점과 오픈 소스 소프트웨어 관리가 결합되어 있습니다. 이전에는 사용자가 칩을 통한 강화된 물리적 보안과 오픈소스를 통한 투명성 중 하나를 선택해야 했지만, Trezor Safe 3를 사용하면 두 가지 모두의 이점을 누릴 수 있습니다.



이 튜토리얼에서는 트레저 세이프 3를 안전하게 설정하고 사용하는 방법을 보여드리겠습니다.



## 트레저 금고 3 개봉하기



Safe 3를 받으면 상자와 Seal이 손상되지 않았는지 확인하여 포장이 개봉되지 않았는지 확인하세요. 나중에 장치를 설정할 때 장치의 진위 여부와 무결성에 대한 소프트웨어 검증도 수행됩니다.



상자 내용물은 다음과 같습니다:




- 트레저 세이프 3;
- Mnemonic 문구, 스티커, 설명서를 기록할 수 있는 카드지가 들어 있는 파우치입니다;
- USB-C to USB-C 케이블.



![Image](assets/fr/02.webp)



트레저 세이프 3를 개봉하면 보호용 플라스틱으로 보호되어 있어야 하며, USB-C 포트는 홀로그램 Seal로 고정되어 있어야 합니다. 그것이 있는지 확인하세요.



![Image](assets/fr/03.webp)



오른쪽 버튼으로 오른쪽으로 스크롤하고 왼쪽 버튼으로 왼쪽으로 스크롤하는 등 기기에서 탐색은 간단합니다. 두 버튼을 동시에 누르면 작업을 확인할 수 있습니다.



![Image](assets/fr/04.webp)



## 전제 조건



이 튜토리얼에서는 트레저 세이프 3를 [Sparrow wallet Wallet 관리 소프트웨어](https://sparrowwallet.com/download/)와 함께 사용하는 방법을 보여드리겠습니다. 아직 이 소프트웨어를 설치하지 않으셨다면 지금 설치하시기 바랍니다. 도움이 필요하시면 Sparrow wallet 구성에 대한 자세한 튜토리얼도 있습니다:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

또한 Safe 3를 구성하고, 정품 여부를 확인하고, 펌웨어를 설치하려면 Trezor Suite 소프트웨어가 필요합니다. 이 소프트웨어는 이 용도로만 사용되며 이후에는 펌웨어 업데이트에만 필요합니다. Wallet의 일상적인 관리에는 Bitcoin에 최적화되어 있고 초보자도 쉽게 사용할 수 있는 Sparrow wallet을 독점적으로 사용할 것입니다(Sparrow은 알트코인이 아닌 Bitcoin만 지원).



[공식 웹사이트에서 트레저 스위트 다운로드](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



이 두 프로그램의 경우, 컴퓨터에 설치하기 전에 (GnuPG를 통해) 진위 여부와 (Hash를 통해) 무결성을 모두 확인할 것을 강력히 권장합니다. 이 작업을 수행하는 방법을 모르는 경우 이 다른 튜토리얼 을 참조하세요:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 트레저 세이프 3 시작하기



Trezor Suite와 Sparrow wallet이 이미 설치되어 있는 컴퓨터에 Safe 3를 연결합니다.



![Image](assets/fr/06.webp)



트레저 스위트를 연 다음 "*내 트레저 설정하기*"를 클릭합니다.



![Image](assets/fr/07.webp)



"*Bitcoin 전용 펌웨어*"를 선택한 다음 "*Bitcoin 전용 설치*"를 클릭합니다.



![Image](assets/fr/08.webp)



그러면 Trezor Suite가 Safe 3에 펌웨어를 설치합니다. 설치하는 동안 잠시 기다려주세요.



![Image](assets/fr/09.webp)



"*계속*"을 클릭합니다.



![Image](assets/fr/10.webp)



그런 다음 진위 테스트를 진행하여 Hardware Wallet가 위조 또는 손상되지 않았는지 확인합니다.



![Image](assets/fr/11.webp)



Safe 3에서 오른쪽 버튼을 눌러 확인합니다.



![Image](assets/fr/12.webp)



트레저가 정품인 경우, 트레저 스위트에서 확인 메시지가 나타납니다.



![Image](assets/fr/13.webp)



그런 다음 기본 작동 지침이 있는 창을 건너뛸 수 있습니다.



![Image](assets/fr/14.webp)



## Bitcoin Wallet 생성



트레저 스위트에서 "*새 Wallet* 만들기" 버튼을 클릭합니다.



![Image](assets/fr/15.webp)



표준 Wallet의 경우 기본 백업 유형을 선택할 수 있습니다. 이렇게 하면 12단어 Mnemonic 문구가 포함된 클래식 싱글사인 Wallet이 생성됩니다. "*Wallet 만들기*"를 클릭합니다.



다중 공유 백업*을 포함하여 Trezor에서 사용할 수 있는 다른 백업 옵션에 대해 자세히 알아보려면 이 튜토리얼도 참조하는 것이 좋습니다:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Hardware Wallet의 이용 약관에 동의합니다.



![Image](assets/fr/17.webp)



오른쪽 버튼을 다시 눌러 새 Wallet를 생성합니다.



![Image](assets/fr/18.webp)



트레저 스위트에서 "*백업 계속*"을 클릭합니다.



![Image](assets/fr/19.webp)



이 소프트웨어는 Mnemonic 문구를 관리하는 방법에 대한 지침을 제공합니다.



이 Mnemonic는 모든 비트코인에 대한 완전한 무제한 액세스를 제공합니다. 이 문구를 소유한 사람은 트레저 금고 3에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다.



12단어 문구는 Hardware Wallet의 분실, 도난 또는 파손 시 비트코인에 대한 액세스를 복원합니다. 따라서 신중하게 보관하고 안전한 장소에 보관하는 것이 매우 중요합니다.



상자에 동봉된 판지에 적거나, 화재, 홍수 또는 붕괴로부터 보호하기 위해 스테인리스 스틸 베이스에 각인하는 것을 추천합니다.



지침을 확인한 후 "*Wallet 백업 생성*" 버튼을 클릭합니다.



![Image](assets/fr/20.webp)



Safe 3는 난수 생성기를 사용하여 Mnemonic 문구를 생성합니다. 이 작업 중에는 감시당하고 있지 않은지 확인하세요. 화면에 표시된 문구를 원하는 물리적 매체에 적습니다. 보안 전략에 따라 문구를 여러 장 복사하는 것도 고려해 볼 수 있습니다(하지만 무엇보다도 문구를 나누지 마세요). 단어에 번호를 매기고 순차적인 순서를 유지하는 것이 중요합니다.



**이 튜토리얼에서는 이 단어를 인터넷에서 절대 공유해서는 안 됩니다. 이 예제 Wallet는 Testnet에서만 사용되며 튜토리얼이 끝나면 삭제됩니다**



Mnemonic 문구를 저장하고 관리하는 올바른 방법에 대한 자세한 내용은 특히 초보자라면 이 다른 튜토리얼을 따르는 것이 좋습니다:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



다음 단어로 이동하려면 마우스 오른쪽 버튼을 클릭합니다. 왼쪽 버튼을 클릭하면 뒤로 돌아갈 수 있습니다. 모든 단어를 적고 나면 오른쪽 버튼을 길게 눌러 다음 단계로 넘어갑니다.



![Image](assets/fr/22.webp)



Mnemonic 문구의 단어를 순서에 따라 선택하여 올바르게 적었는지 확인합니다. 왼쪽 및 오른쪽 버튼을 사용하여 제안서 사이를 탐색한 다음 2개의 버튼을 동시에 클릭하여 올바른 단어를 선택합니다.



![Image](assets/fr/23.webp)



이 인증 절차가 완료되면 오른쪽에 있는 버튼을 클릭합니다.



![Image](assets/fr/24.webp)



## PIN 코드 설정



다음 단계는 PIN 코드 단계입니다. PIN 코드는 트레저의 잠금을 해제합니다. 따라서 무단 물리적 액세스로부터 보호할 수 있습니다. 이 PIN 코드는 Wallet의 암호화 키를 생성하는 데 관여하지 않습니다. 따라서 PIN 코드에 액세스할 수 없더라도 12단어 Mnemonic 문구를 소지하고 있으면 비트코인에 다시 액세스할 수 있습니다.



트레저 스위트에서 "*비밀번호 계속*"을 클릭한 다음 "*비밀번호 설정*" 버튼을 클릭합니다.



![Image](assets/fr/25.webp)



안전 3으로 확인합니다.



![Image](assets/fr/26.webp)



가능한 한 무작위로 PIN 코드를 선택하는 것이 좋습니다. 이 코드는 트레저가 저장된 곳과 별도의 위치(예: 비밀번호 관리자)에 저장하세요. 8자리에서 50자리 사이의 PIN 코드를 정의할 수 있습니다. 보안을 강화하기 위해 가능한 한 긴 PIN 코드를 선택하는 것이 좋습니다.



왼쪽 및 오른쪽 버튼을 사용하여 각 숫자를 선택합니다. 선택을 확인하고 다음 숫자로 이동하려면 두 버튼을 동시에 누릅니다.



![Image](assets/fr/27.webp)



완료되면 숫자 시작 부분의 '*입력*' 확인 표시를 클릭한 다음 비밀번호를 다시 한 번 확인합니다.



![Image](assets/fr/28.webp)



PIN 코드가 등록되었습니다.



![Image](assets/fr/29.webp)



트레저 스위트에서 "*설정 완료*" 버튼을 클릭합니다.



![Image](assets/fr/30.webp)



이제 Safe 3의 구성이 완료되었습니다. 원하는 경우 Hardware Wallet의 이름과 홈 페이지를 변경할 수 있습니다.



![Image](assets/fr/31.webp)



Hardware Wallet에서 정기 펌웨어 업데이트를 수행하거나 복구 테스트를 실행하려는 경우를 제외하고는 더 이상 Trezor Suite 소프트웨어가 필요하지 않습니다. 이 소프트웨어는 Bitcoin 전용으로 사용하기에 완벽하게 적합하므로 이제 Sparrow을 사용하여 Wallet을 관리할 것입니다.



## Sparrow wallet에서 Wallet 설정하기



아직 설치하지 않았다면 [공식 웹사이트](https://sparrowwallet.com/)에서 Sparrow wallet을 다운로드하여 컴퓨터에 설치하는 것으로 시작하세요.



Sparrow wallet를 열었으면 소프트웨어가 Bitcoin 노드에 연결되어 있는지 확인합니다(오른쪽 하단에 있는 체크 표시가 Interface에 표시되어 있음). Sparrow를 연결하는 데 문제가 있는 경우 이 튜토리얼의 시작 부분을 읽어보는 것이 좋습니다:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

"*파일*" 탭을 클릭한 다음 "*새 Wallet*"을 클릭합니다.



![Image](assets/fr/32.webp)



Wallet의 이름을 지정한 다음 "*Wallet 만들기*"를 클릭합니다.



![Image](assets/fr/33.webp)



"*스크립트 유형*" 드롭다운 메뉴에서 비트코인을 보호하는 데 사용할 스크립트 유형을 선택합니다. "*Taproot*" 또는 "*Native SegWit*"를 권장합니다.



![Image](assets/fr/34.webp)



"*연결된 Hardware Wallet*" 버튼을 클릭합니다. 물론 Safe 3가 컴퓨터에 연결되어 있고 잠금이 해제되어 있어야 합니다.



![Image](assets/fr/35.webp)



"*스캔*" 버튼을 클릭합니다. Safe 3가 나타납니다. "*키 저장소 가져오기*"를 클릭합니다.



![Image](assets/fr/36.webp)



이제 첫 번째 계정의 확장 공개키를 포함하여 Wallet의 세부 정보를 확인할 수 있습니다. "*적용*" 버튼을 클릭하여 Wallet 생성을 완료합니다.



![Image](assets/fr/37.webp)



Sparrow wallet에 안전하게 액세스하려면 강력한 비밀번호를 선택하세요. 이 비밀번호는 Sparrow wallet 데이터에 대한 안전한 액세스를 보장하여 무단 액세스로부터 공개 키, 주소, 레이블 및 거래 내역을 보호합니다.



이 비밀번호를 잊지 않도록 비밀번호 관리자에 저장해 두는 것이 좋습니다.



![Image](assets/fr/38.webp)



이제 Wallet를 Sparrow wallet으로 가져왔습니다!



![Image](assets/fr/39.webp)



Wallet에서 첫 비트코인을 받기 전에 **빈 복구 테스트를 수행할 것을 강력히 권장합니다**. Xpub과 같은 몇 가지 참조 정보를 적어둔 다음, Wallet가 비어 있는 상태에서 Trezor Safe 3를 초기화하세요. 그런 다음 종이 백업을 사용하여 Trezor에서 Wallet를 복원해 보세요. 복원 후 생성된 xpub이 원래 기록했던 것과 일치하는지 확인하세요. 일치한다면 종이 백업이 안정적이라고 안심할 수 있습니다.



복구 테스트를 수행하는 방법에 대해 자세히 알아보려면 이 다른 튜토리얼을 참조하세요:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 트레저 세이프 3로 어떻게 비트코인을 받을 수 있나요?



Sparrow에서 "*수신*" 탭을 클릭합니다.



![Image](assets/fr/40.webp)



Sparrow wallet이 제안한 Address를 사용하기 전에 트레저의 화면에서 이를 확인하세요. 이를 통해 Sparrow에 표시된 Address가 가짜가 아닌지, Hardware Wallet이 실제로 이 Address로 보호된 비트코인을 사용하는 데 필요한 개인 키를 보유하고 있는지 확인할 수 있습니다. 이를 통해 여러 유형의 공격을 피할 수 있습니다.



이 확인을 수행하려면 "*Address 표시*" 버튼을 클릭합니다.



![Image](assets/fr/41.webp)



트레저에 표시된 Address이 Sparrow wallet에 표시된 것과 일치하는지 확인하세요. 또한 Address을 발신자에게 전달하기 직전에 이 확인을 수행하여 유효성을 확인하는 것이 좋습니다. 버튼을 사용하여 확인할 수 있습니다.



![Image](assets/fr/42.webp)



그런 다음 "*레이블*"을 추가하여 이 Address로 보호할 비트코인의 출처를 설명할 수 있습니다. 이는 UTXO를 더 잘 관리할 수 있는 좋은 방법입니다.



![Image](assets/fr/43.webp)



그런 다음 이 Address를 사용하여 비트코인을 받을 수 있습니다.



![Image](assets/fr/44.webp)



## 트레저 세이프 3로 비트코인을 어떻게 전송하나요?



이제 세이프 3 보안 Wallet로 첫 Sats를 받으셨으니 이제 사용하셔도 됩니다! 트레저를 컴퓨터에 연결하고 PIN 코드를 사용해 잠금을 해제하고 Sparrow wallet을 실행한 다음 "*보내기*" 탭으로 이동해 새 트랜잭션을 생성하세요.



![Image](assets/fr/45.webp)



Coin 제어*, 즉 트랜잭션에서 소비할 UTXO를 구체적으로 선택하려면 "*UTXO*" 탭으로 이동하세요. 사용하고자 하는 UTXO를 선택한 다음 "*선택한 항목 보내기*"를 클릭합니다. "*송금*" 탭의 동일한 화면으로 리디렉션되지만, 트랜잭션에 대해 이미 UTXO가 선택된 상태로 표시됩니다.



![Image](assets/fr/46.webp)



목적지 Address를 입력합니다. "*+ 추가*" 버튼을 클릭하여 여러 주소를 입력할 수도 있습니다.



![Image](assets/fr/47.webp)



이 비용의 목적을 기억하기 위해 "*라벨*"을 적어 두세요.



![Image](assets/fr/48.webp)



이 Address으로 송금할 금액을 선택합니다.



![Image](assets/fr/49.webp)



현재 시장에 따라 거래 수수료율을 조정하세요. 예를 들어, [Mempool.space](https://Mempool.space/)를 사용하여 적절한 수수료율을 선택할 수 있습니다.



모든 트랜잭션 매개변수가 올바른지 확인한 다음 "*거래 생성*"을 클릭합니다.



![Image](assets/fr/50.webp)



모든 것이 만족스럽다면 "*서명을 위한 거래 마무리*"를 클릭합니다.



![Image](assets/fr/51.webp)



"*서명*"을 클릭합니다.



![Image](assets/fr/52.webp)



Trezor Safe 3 옆의 "*서명*"을 클릭합니다.



![Image](assets/fr/53.webp)



Hardware Wallet 화면에서 수취인 Address, 송금 금액, 요금 등 거래 매개변수를 확인합니다. 트레저에서 거래가 확인되면 두 버튼을 동시에 클릭하여 서명합니다.



![Image](assets/fr/54.webp)



이제 트랜잭션이 서명되었습니다. 모든 것이 정상인지 다시 한 번 확인한 다음 "*거래 브로드캐스트*"를 클릭하여 Bitcoin 네트워크에 브로드캐스트합니다.



![Image](assets/fr/55.webp)



Sparrow wallet의 "*거래*" 탭에서 찾을 수 있습니다.



![Image](assets/fr/56.webp)



이제 Sparrow wallet과 함께 트레저 세이프 3의 기본 사용법을 익히셨으니 축하드립니다! 한 단계 더 나아가기 위해 passphrase BIP39와 함께 Hardware Wallet 트레저를 사용하여 안전을 강화하는 방법에 대한 종합적인 튜토리얼을 추천합니다:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!