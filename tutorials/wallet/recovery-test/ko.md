---
name: 복구 테스트
description: 비트코인을 잃어버리지 않도록 백업을 테스트하는 방법은 무엇인가요?
---
![cover](assets/cover.webp)


Bitcoin Wallet를 생성할 때 보통 12개 또는 24개의 단어로 구성된 Mnemonic 문구를 적어두라는 메시지가 표시됩니다. 이 문구를 통해 Wallet를 호스팅하는 장치의 분실, 손상 또는 도난 시 비트코인에 대한 액세스 권한을 복구할 수 있습니다. 새 Bitcoin Wallet를 사용하기 전에 이 Mnemonic 문구의 유효성을 확인하는 것이 매우 중요합니다. 이를 위한 가장 좋은 방법은 드라이런 복구 테스트를 수행하는 것입니다.


이 테스트는 비트코인을 입금하기 전에 Wallet 복원을 시뮬레이션하는 것입니다. Wallet가 비어 있는 상태에서 키를 호스팅하는 장치가 분실되고 남은 것은 Mnemonic 문구뿐인 상황을 시뮬레이션하여 비트코인을 복구하려고 시도합니다.


![RECOVERY TEST](assets/notext/01.webp)


## 목적이 무엇인가요?


이 테스트 프로세스를 통해 종이 또는 금속에 있는 Mnemonic 문구의 물리적 백업이 제대로 작동하는지 확인할 수 있습니다. 이 복구 테스트에서 실패하면 문구 백업에 오류가 있다는 신호이므로 비트코인이 위험에 처할 수 있습니다. 반면에 테스트가 성공하면 Mnemonic 문구가 정상적으로 작동하는 것으로 확인되며, 이 Wallet를 사용하여 안심하고 비트코인을 보호할 수 있습니다.


드라이런 복구 테스트를 수행하면 두 가지 이점이 있습니다. Mnemonic 문구의 정확성을 확인할 수 있을 뿐만 아니라 Wallet 복구 프로세스에 익숙해질 수 있는 기회도 얻을 수 있습니다. 이렇게 하면 실제 상황이 발생하기 전에 잠재적인 어려움을 발견할 수 있습니다. 실제로 Wallet을 복구해야 하는 날에는 이미 프로세스를 숙지하고 있기 때문에 스트레스를 덜 받고 오류의 위험도 줄일 수 있습니다. 그렇기 때문에 이 테스트 단계를 소홀히 하지 말고 필요한 시간을 들여 올바르게 수행하는 것이 중요합니다.


## 복구 테스트란 무엇인가요?


테스트 과정은 매우 간단합니다:


- 새 Bitcoin Wallet을 생성한 후 첫 번째 사토시를 입금하기 전에 xpub, 첫 번째 수신 Address 또는 마스터 키 지문과 같은 증인 정보를 기록해 두세요;
- 그런 다음, 예를 들어 Hardware Wallet를 공장 설정으로 초기화하여 아직 비어 있는 Wallet을 일부러 삭제합니다;
- 그런 다음, Mnemonic 문구의 종이 백업과 passphrase를 사용하는 경우 그 백업만을 사용하여 Wallet의 복구를 시뮬레이션합니다;
- 마지막으로, 증인 정보가 재생성된 Wallet의 정보와 일치하는지 확인합니다. 정보가 일치하면 물리적 백업의 신뢰성을 확신할 수 있으며, 첫 번째 비트코인을 이 Wallet로 전송할 수 있습니다.

복구 테스트 중에는 Wallet의 공격 표면이 증가하지 않도록 **최종 Wallet와 동일한 장치를 사용해야 합니다**. 예를 들어 트레저 세이프 5에서 Wallet를 생성한 경우, 동일한 트레저 세이프 5에서 복구 테스트를 수행해야 합니다. 복구 문구를 다른 소프트웨어에 입력하면 Wallet가 아직 비어 있더라도 Hardware Wallet이 제공하는 보안이 손상될 수 있으므로 다른 소프트웨어에 복구 문구를 입력하지 않는 것이 중요합니다.


## 복구 테스트는 어떻게 수행하나요?


이 튜토리얼에서는 Sparrow wallet(Hot Wallet의 경우)를 사용하여 Bitcoin Software Wallet에서 복구 테스트를 수행하는 방법을 설명합니다. 그러나 다른 유형의 장치에 대해서도 프로세스는 동일하게 유지됩니다. 다시 한 번 말씀드리지만, **Hardware Wallet을 사용하는 경우 Sparrow wallet에서 복구 테스트를 수행하지 마세요**(이전 섹션 참조).


방금 Sparrow wallet에 새로운 Wallet을 만들었습니다. 현재로서는 아직 비트코인을 보내지 않았습니다. 비어 있습니다.


![RECOVERY TEST](assets/notext/02.webp)


저는 종이에 12단어 Mnemonic 문구를 꼼꼼히 적어 두었습니다. 그리고 이 Wallet의 보안을 강화하기 위해 다른 종이에 저장해 둔 BIP39 passphrase도 설정해 두었습니다:


```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```


```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```


***이 튜토리얼에서 설명하는 것과는 달리 Mnemonic 문구와 passphrase를 인터넷에서 공유해서는 안 된다는 점을 분명히 말씀드립니다. 이 예제 Wallet는 사용되지 않으며 튜토리얼이 끝날 때 삭제됩니다***


이제 Wallet의 증인 정보를 초안에 적어 두겠습니다. 첫 번째 수신 Address, xpub 또는 마스터 키 지문과 같은 다양한 정보를 선택할 수 있습니다. 개인적으로는 첫 번째 수신 Address를 선택하는 것을 추천합니다. 이렇게 하면 이 Address로 이어지는 완전한 첫 번째 파생 경로를 찾을 수 있는지 확인할 수 있습니다.


Sparrow에서 "*주소*" 탭을 클릭합니다.


![RECOVERY TEST](assets/notext/03.webp)


그런 다음 Wallet의 첫 번째 수신 Address을 종이에 적어 두세요. 제 예에서는 Address입니다:


```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```


정보를 기록한 후 "*파일*" 메뉴로 이동한 다음 "*Wallet 삭제*"를 선택합니다. 이 작업을 진행하기 전에 Bitcoin Wallet이 비어 있어야 한다는 점을 다시 한 번 알려드립니다.


![RECOVERY TEST](assets/notext/04.webp)


Wallet가 실제로 비어 있으면 Wallet의 삭제를 확인하세요.


![RECOVERY TEST](assets/notext/05.webp)


이제 Wallet 생성 과정을 반복하되, 종이 백업을 사용해야 합니다. "*파일*" 메뉴를 클릭한 다음 "*새 Wallet*"을 클릭합니다.


![RECOVERY TEST](assets/notext/06.webp)


Wallet의 이름을 다시 입력합니다.


![RECOVERY TEST](assets/notext/07.webp)


"*스크립트 유형*" 메뉴에서 이전에 삭제한 Wallet와 동일한 스크립트 유형을 선택해야 합니다.


![RECOVERY TEST](assets/notext/08.webp)


그런 다음 "*새롭거나 가져온 Software Wallet*" 버튼을 클릭합니다.


![RECOVERY TEST](assets/notext/09.webp)


seed에 맞는 단어 수를 선택합니다.


![RECOVERY TEST](assets/notext/10.webp)


소프트웨어에 Mnemonic 구문을 입력합니다. "*잘못된 체크섬*" 메시지가 나타나면 Mnemonic 문구의 백업이 잘못되었다는 뜻입니다. 복구 테스트에 실패한 것이므로 Wallet 생성을 처음부터 다시 시작해야 합니다.


![RECOVERY TEST](assets/notext/11.webp)


제 경우처럼 passphrase이 있는 경우에도 입력하세요.


![RECOVERY TEST](assets/notext/12.webp)


"*키 저장소 만들기*"를 클릭한 다음 "*키 저장소 가져오기*"를 클릭합니다.


![RECOVERY TEST](assets/notext/13.webp)


마지막으로 "*신청*" 버튼을 클릭합니다.


![RECOVERY TEST](assets/notext/14.webp)


이제 '*주소*' 탭으로 돌아갈 수 있습니다.


![RECOVERY TEST](assets/notext/15.webp)


마지막으로 첫 번째 수신 Address이 초안에서 증인으로 표시한 것과 일치하는지 확인합니다.


![RECOVERY TEST](assets/notext/16.webp)


수신 주소가 일치하면 복구 테스트가 성공한 것이며 새 Bitcoin Wallet를 사용할 수 있습니다. 일치하지 않으면 스크립트 유형 선택에 오류가 있어 파생 경로가 잘못되었거나 Mnemonic 구문 또는 passphrase의 백업에 문제가 있는 것일 수 있습니다. 두 경우 모두 위험을 피하기 위해 처음부터 다시 시작하여 Bitcoin Wallet를 새로 만들 것을 강력히 권장합니다. 이번에는 Mnemonic 문구를 오류 없이 기록하는 데 주의하세요.

축하합니다, 이제 복구 테스트를 수행할 수 있게 되었습니다! 모든 Bitcoin 지갑을 생성할 때 이 과정을 일반화하는 것이 좋습니다. 이 튜토리얼이 도움이 되셨다면 아래에 좋아요를 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!