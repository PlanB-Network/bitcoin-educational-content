---
name: COLDCARD Mk

description: 콜드카드 장치 및 Bitcoin core로 Bitcoin 개인 키 생성, 백업 및 사용
---

![cover](assets/cover.webp)


콜드카드 장치 및 Bitcoin 코어로 Bitcoin 개인 키 생성, 백업 및 사용__


## 콜드카드를 사용하여 개인키를 생성하고 Bitcoin core 노드의 Interface를 통해 사용하는 방법에 대한 전체 가이드!


Bitcoin 네트워크 사용의 핵심은 비대칭 암호화 개념으로, 데이터를 암호화하고 해독하는 한 쌍의 키(비공개 키와 공개 키)를 사용하여 통신의 프라이버시를 보장하는 개념입니다.


Bitcoin의 경우 이러한 개인 키와 공개 키 쌍을 생성하여 비트코인을 저장하고(UTXO 또는 미사용 거래 출력) 이를 사용하기 위해 트랜잭션에 서명할 수 있습니다.


오늘날 지갑이 Mnemonic 구문(seed 구문)을 암호화 키와 연결하는 방법을 결정하는 표준인 BIP 39를 사용해 개인 키를 무작위로 생성하고 텍스트 형식으로 백업하는 데 사용할 수 있는 여러 도구가 있습니다. 대부분의 경우 Mnemonic 문구는 12개 또는 24개의 단어로 구성되며, Wallet과 해당 비트코인을 복구하기 위해서는 안전하게 백업해야 합니다.


이 글에서는 세계에서 가장 널리 사용되고 안전한 장치 중 하나인 콜드카드 Mk4를 사용하여 개인키를 generate로 만드는 방법과 주사위 굴리기 방식을 사용하여 엔트로피를 최대화하는 방법, 에어 갭 방식으로 Bitcoin core과 함께 사용하는 방법에 대해 알아보겠습니다!


**참고: 🧰** 가이드를 사용하려면 다음 도구를 준비하세요:



- 콜드카드 장치(Mk3 또는 Mk4)
- MicroSD 카드(4GB면 충분)
- 전원 전용 마그네틱 USB 케이블(Mk3용 미니 USB, Mk4용 USB-C)
- 하나 이상의 고급 주사위


## 콜드카드로 새 Mnemonic 문구 생성하기


PIN이 이미 설정되어 있는 콜드카드의 포장을 새로 풀었다고 가정하고 처음부터 개인 키를 만드는 과정을 시작합니다(장치 초기화 중 콜드카드의 단계를 따르세요).


**참고: ** 이미 구성된 콜드카드의 개인 키를 재설정하려면 다음 단계를 따르세요:

_고급/도구 > 위험 구역 > seed 기능 > seed 파괴 > ✓_


**주의:** 이 단계를 수행하면 콜드카드에서 개인키를 잊어버리게 됩니다. 나중에 복구하려면 Mnemonic 문구를 제대로 백업했는지 확인하세요.


## 따라야 할 단계:


비밀번호로 콜드카드에 연결 > 새 seed 단어 > 24 단어 주사위 굴리기


주사위를 100번 굴려서 1부터 6까지 나온 결과를 콜드카드에 적습니다. 이 방법을 실행하면 256바이트의 엔트로피를 생성하여 완전히 무작위적인 개인 키를 생성하는 데 유리합니다. 코인카이트는 엔트로피 생성 시스템을 독립적으로 검증하는 데 필요한 문서도 제공합니다.


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


100개의 주사위 굴리기가 완료되면 ✓를 누른 다음 얻은 단어 24개를 순서대로 적습니다. 두 번 확인하고 ✓를 누릅니다. 마지막으로 콜드카드에 있는 24개의 단어에 대한 인증 테스트를 완료하기만 하면 새로운 개인키가 생성됩니다!


다음으로 표시된 단계에 따라 NFC(Mk4) 및 USB 기능을 활성화할지 여부를 선택합니다. 메인 메뉴에 들어가면 이제 디바이스의 펌웨어를 업데이트할 차례입니다. 고급/도구 > 펌웨어 업그레이드 > 버전 보기로 이동하여 공식 웹사이트에서 사용 가능한 최신 버전을 확인하고 다운로드하세요. 보안을 최대한 활용하려면 콜드카드를 업데이트하는 것이 좋습니다.


계속 진행하기 전에 개인 키와 연결된 마스터 키 지문(XFP)을 기록해 두는 것이 좋습니다. 이 데이터를 통해 복구 시 올바른 Wallet에 있는지 빠르게 확인할 수 있습니다. 고급/도구 > 신원 보기 > 마스터 키 지문(XFP)으로 이동하여 얻은 일련의 영숫자 8자리를 기록합니다. XFP는 Mnemonic 문구와 같은 위치에 기록할 수 있으며 민감한 데이터가 아닙니다.


**참고: 💡** 다른 소프트웨어에서 Mnemonic 문구 백업을 테스트하는 것이 좋습니다. 이 작업을 안전하게 수행하려면 5분 이내에 Tails로 Bitcoin Wallet 백업 확인하기 문서를 참조하세요.


## 보안 보너스: "비밀 문구"(선택 사항)


passphrase(비밀 문구)는 비트코인을 보호하기 위해 Wallet 구성에 Layer 보안을 추가하기 위해 추가할 수 있는 훌륭한 요소입니다. passphrase는 Mnemonic 문구에 대한 일종의 25번째 단어 역할을 합니다. 추가하면 개인 키 및 관련 Mnemonic 구문과 함께 완전히 새로운 Wallet이 생성됩니다. 이 Wallet은 초기 Mnemonic 구문을 선택한 passphrase와 결합하여 액세스할 수 있으므로 새 Mnemonic 구문을 기록할 필요는 없습니다.


두 항목에 모두 액세스할 수 있는 공격자는 자금에 액세스할 수 있기 때문에 passphrase를 Mnemonic 문구와 별도로 기록하는 것이 목표입니다. 반면에 이러한 항목 중 하나에만 액세스할 수 있는 공격자는 자금에 액세스할 수 없으며, 이러한 특정 이점이 바로 Wallet 구성의 보안 수준을 최적화하는 것입니다.


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## 콜드카드로 passphrase를 추가하는 단계:


passphrase > 단어 추가(권장) > 적용을 클릭합니다. 장치에 새로 생성된 Wallet의 XFP가 passphrase과 함께 표시되며, 앞서 설명한 것과 같은 이유로 passphrase과 함께 기록해 두어야 합니다.


**팁💡** 여기에 passphrase와 관련된 추가 리소스가 있습니다:



- [여기](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af)에는 _Trezor_의 첫 번째 글이 있습니다;
- [여기](https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/)에서 두 번째는 _코인카이트_에서 찾을 수 있습니다;
- 그리고 [여기](https://armantheparman.com/passphrase/)에서 _armantheparman_의 마지막 작품을 찾을 수 있습니다.


## Wallet를 Bitcoin core로 내보내기


이제 Bitcoin 네트워크와 상호 작용하기 위해 Wallet를 소프트웨어로 내보낼 준비가 되었습니다. 이 가이드에서는 Bitcoin core(v24.1)을 사용하겠습니다.


Bitcoin core에 대한 설치 및 구성 가이드를 참조하세요:



- Bitcoin core로 자체 노드 실행하기:** https://agora256.com/faire-tourner-son-propre-noeud-avec-Bitcoin-core/
- Bitcoin core 노드에 Tor 구성하기:** https://agora256.com/configuration-tor-Bitcoin-core/


먼저 마이크로 SD 카드를 콜드카드에 삽입한 다음 다음 단계에 따라 Wallet을 Bitcoin core용으로 내보냅니다: 고급/도구 > Wallet 내보내기 > Bitcoin core. 마이크로 SD 카드에 두 개의 파일이 기록됩니다: Bitcoin-core.sig & Bitcoin-core.txt. 마이크로 SD 카드를 Bitcoin core이 설치된 컴퓨터에 삽입하고 .txt 파일을 엽니다. "마스터 키 지문이 있는 Wallet의 경우"라는 줄이 표시됩니다 8자 XFP가 개인 키를 만들 때 기록한 것과 일치하는지 확인합니다

파일의 지침을 따르기 전에 다음 단계에 따라 Bitcoin core Interface에서 Wallet을 준비해 보겠습니다: 파일 탭 > Wallet 만들기로 이동합니다. 아래 이미지와 같이 Wallet의 이름(Core에서 "porte-monnaie"와 같은 용어)을 선택하고 개인 키 비활성화, 빈 Wallet 만들기 및 Wallet 설명자 옵션을 선택합니다. 그런 다음 만들기 버튼을 누릅니다.


![create a wallet](assets/guide-agora/3.webp)


Bitcoin core에서 Wallet를 생성한 후 창 탭 > 콘솔로 이동하여 페이지 상단의 선택한 Wallet에 생성한 Wallet의 이름이 표시되는지 확인합니다.


이제 앞서 콜드카드에서 생성한 .txt 파일에서 importdescriptors로 시작하는 줄을 복사한 다음 Bitcoin core 콘솔에 붙여넣습니다. "성공": true 줄이 포함된 응답이 반환되어야 합니다.


![nodes window](assets/guide-agora/4.webp)


응답에 "메시지"가 포함된 경우 "원거리 설명자에 레이블이 없어야 합니다"라는 메시지가 포함된 경우 "레이블" 항목을 지웁니다: "콜드카드 xxxx0000"을 .txt 파일에서 복사한 줄에서 지운 다음 전체 줄을 Bitcoin core 콘솔에 다시 붙여넣습니다.


필요한 경우 콜드카드 깃허브에서 도움말[여기](https://github.com/Coldcard/firmware/blob/master/docs/Bitcoin-core-usage.md)을 참조하세요.


## Bitcoin core에서 Wallet 가져오기 유효성 검사


작업이 성공적으로 이루어졌는지 확인하려면 원하는 Wallet를 Bitcoin core로 가져왔는지 확인해야 합니다. 이를 확인하는 간단한 방법은 콜드카드에서 생성된 주소가 Bitcoin core에서 생성된 주소와 일치하는지 확인하는 것입니다.


Bitcoin core: 수신 > 새 수신 Address 만들기

콜드카드: Address 탐색기 > bc1q로 시작하는 Address을 선택합니다. 콜드카드 Address 'bc1q'는 Bitcoin core에 표시된 Address과 일치해야 합니다.

'에어 갭' 모드에서 트랜잭션 수신 및 전송


트랜잭션 수신은 매우 간단합니다. 수신을 누르고, 트랜잭션에 라벨을 붙인 다음(선택 사항이지만 권장), 새 수신 Address을 생성하기만 하면 됩니다. 그런 다음 발신자와 Address을 공유하기만 하면 됩니다.


이제 이 콜드카드 + Bitcoin core 설정의 핵심 요소는 콜드카드와 개인키가 인터넷에 연결되지 않은 상태에서 트랜잭션을 전송하는 것으로, Bitcoin의 TBSP(PSBT - 부분적으로 서명된 Bitcoin 트랜잭션) 기능을 사용하는 에어 갭이라고 하는 방법입니다.

기본적으로 Bitcoin core Interface를 사용하여 트랜잭션을 구성한 다음 마이크로 SD 카드를 통해 콜드카드로 내보내 서명하고 서명된 트랜잭션 파일을 Bitcoin core로 반환하고 트랜잭션을 네트워크에 브로드캐스트합니다. 이렇게 해야 하는 이유는 Bitcoin core로 가져온 Wallet에는 개인 키가 없고 공개 키(수신 주소를 generate화할 수 있는)만 있기 때문에 소프트웨어에서 직접 트랜잭션에 서명하여 비트코인을 사용할 수 없기 때문입니다.


계속 진행하기 전에 설정 > Wallet에서 다음 옵션이 활성화되어 있는지 확인하세요:



- Coin 제어 기능 활성화
- 미확인 코인 사용(선택 사항)
- TBPS 검사 사용


![option ](assets/guide-agora/5.webp)


### 에어 갭 모드로 전송하는 단계:


보내기 > 입력 > 원하는 UTXO을 선택한 다음 받는 사람에 수취인 Address을 입력합니다. 거래 수수료: 선택... > 사용자 지정 > 거래 수수료 입력(Bitcoin core은 대부분의 대체 Wallet 솔루션처럼 sat/바이트가 아닌 Sats/킬로바이트 단위로 계산합니다. 따라서 4000 Sats/킬로바이트 = 4 Sats/바이트). 서명되지 않은 트랜잭션 생성 > 파일을 마이크로 SD 카드에 저장하고 콜드카드에 삽입합니다.


콜드카드에서 서명 준비를 누르고 거래 세부 정보를 확인한 다음 ✓를 누르고 서명된 파일이 생성되면 마이크로 SD 카드를 컴퓨터에 다시 삽입합니다.


Bitcoin core로 돌아가서 파일 탭 > 파일에서 TBSP 로드로 이동하여 서명된 트랜잭션 파일 .PSBT을 입력합니다. 화면에 PSBT 작업 상자가 나타나 트랜잭션이 완전히 서명되었고 브로드캐스트할 준비가 되었음을 확인합니다. 이제 브로드캐스트 트랜잭션을 누르기만 하면 됩니다.


![PSBT operations](assets/guide-agora/6.webp)


### 결론


콜드카드 장치와 자체 노드를 실행하는 Bitcoin core의 조합은 강력합니다. 여기에 100번의 주사위 굴림으로 생성된 개인 키와 비밀 문구를 추가하면 Wallet 구성은 정교하고 강력한 요새가 됩니다.


언제든지 문의하여 의견과 질문을 공유해 주세요! 우리의 목표는 지식을 공유하고 날마다 이해도를 높이는 것입니다.