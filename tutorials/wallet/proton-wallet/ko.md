---
name: Proton Wallet
description: Proton Bitcoin Wallet 설치 및 사용
---
![cover](assets/cover.webp)


Proton은 2014년 CERN 과학자들이 설립한 디지털 개인정보 보호 전문 스위스 회사입니다. 오픈 소스 솔루션으로 잘 알려진 프로톤은 프로톤 메일, 프로톤 VPN, 프로톤 드라이브를 포함한 서비스 제품군을 제공합니다.


Proton은 최근 모바일 앱 또는 웹 클라이언트로 사용할 수 있는 오픈 소스 셀프 커스터디 Bitcoin Wallet인 Proton Wallet를 출시했으며, 이는 Proton 계정과 연동됩니다. Wallet의 기능은 현재로서는 비교적 클래식하며, RBF(*Replace-by-fee*), 태깅 또는 BIP39 passphrase 추가 기능과 같이 좋은 Bitcoin Wallet에서 기대되는 필수 도구가 포함되어 있습니다.


이 Wallet의 특별한 기능은 수신자의 이메일 Address를 사용해 비트코인을 전송하는 기능으로, 프로톤은 사용자의 Wallet에 연결된 빈 Bitcoin Address를 자동으로 생성합니다. 프로톤은 향후 라이트닝과 코인 조인을 포함한 새로운 기능을 추가할 계획입니다(GitHub 저장소의 활동으로 볼 때 아마도 Whirlpool을 사용할 것으로 보입니다).


## Proton 계정 만들기


프로톤 Wallet를 사용하려면 프로톤 계정이 필요합니다. 이 튜토리얼의 첫 번째 단계("*프로톤 계정 만들기*" 섹션만 해당)에 따라 프로톤 사서함을 만들면 무료로 계정을 만들 수 있습니다. 계정이 설정되면 이 튜토리얼의 나머지 부분을 계속 진행할 수 있습니다.


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## 프로톤 Wallet에 연결


프로톤 Wallet 웹사이트](https://proton.me/Wallet)로 이동하여 "*프로톤 Wallet 받기*" 버튼을 클릭합니다.


![Image](assets/fr/01.webp)


"*무료*" 구독 옵션을 선택한 다음 "*로그인*"을 클릭합니다.


![Image](assets/fr/02.webp)


Proton 계정과 연결된 이메일과 비밀번호를 입력하여 로그인합니다.


![Image](assets/fr/03.webp)


이제 계정이 표시될 것입니다. "*지금 Proton Wallet 사용 시작하기*"를 클릭합니다.


![Image](assets/fr/04.webp)


## Bitcoin Wallet 생성


계정의 기본 법정 화폐를 선택한 다음 "*새 Wallet* 만들기"를 클릭합니다.


![Image](assets/fr/05.webp)


이제 Bitcoin Wallet가 생성되었습니다. 이론적으로는 즉시 사용을 시작할 수 있지만, 먼저 Mnemonic을 저장하는 것이 매우 중요합니다. 이렇게 하려면 Interface의 오른쪽 상단에 있는 "*Wallet 보호*"를 클릭하세요.


![Image](assets/fr/06.webp)


Proton에서 아직 백업을 설정하지 않은 경우 계정에 대한 백업을 설정하고 2단계 인증 방법을 사용하여 계정을 보호하라는 메시지가 표시됩니다. 이러한 보안 조치는 전체 Proton 계정에 적용되지만, Bitcoin Wallet가 통합된 경우 더욱 중요합니다. 이러한 보안 조치를 구현할 것을 강력히 권장합니다.


![Image](assets/fr/07.webp)


Mnemonic 문구를 저장하려면 "*이 Wallet의 seed 문구 백업*"을 클릭합니다.


![Image](assets/fr/08.webp)


프로톤 비밀번호를 입력합니다.


![Image](assets/fr/09.webp)


그런 다음 "*Wallet seed 문구 보기*"를 클릭하여 Wallet의 Mnemonic 문구를 표시합니다.


![Image](assets/fr/10.webp)


양성자 Wallet는 12단어 Mnemonic 문구를 표시합니다. **이 Mnemonic은 모든 비트코인에 대한 완전한 무제한 액세스를 제공합니다**. 이 문구를 소유한 사람은 누구나 귀하의 Proton 계정에 액세스하지 않더라도 자금을 훔칠 수 있습니다. 12단어 문구는 계정에 액세스하지 못할 경우 비트코인에 대한 액세스 권한을 복원하는 데 사용할 수 있습니다. 따라서 신중하게 저장하고 안전한 장소에 보관하는 것이 매우 중요합니다.


종이에 적거나 보안을 강화하려면 화재, 홍수 또는 붕괴로부터 보호하기 위해 스테인리스 스틸 받침대에 새겨 넣는 것이 좋습니다.


![Image](assets/fr/11.webp)


Mnemonic 문구를 저장하고 관리하는 올바른 방법에 대한 자세한 내용은 특히 초보자라면 이 다른 튜토리얼을 따르는 것이 좋습니다:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

물론 이 튜토리얼에서 설명하는 것과는 달리 이 단어들을 사진으로 찍어서는 안 됩니다**_


문구를 저장한 후 "*완료*" 버튼을 클릭합니다.


![Image](assets/fr/12.webp)


## Interface 알아보기


Proton Wallet의 Interface는 매우 직관적입니다. 왼쪽에는 여러 지갑과 관련 계정이 있습니다. "*기본*" 계정이 기본 계정입니다. 기밀 유지를 위해 Proton 이메일 Address을 통해 받은 비트코인은 "*Bitcoin via Email*"이라는 별도의 계정에 보관됩니다.


![Image](assets/fr/13.webp)


새 계정을 추가하려면 "*계정 추가*"를 클릭합니다.


![Image](assets/fr/14.webp)


새 Wallet를 만들려면 "*지갑*" 옆의 "*+*" 기호를 클릭합니다.


![Image](assets/fr/15.webp)


여기에서 BIP39 passphrase을 새 Wallet에 추가할 수 있습니다.


![Image](assets/fr/16.webp)


passphrase에 대한 지식을 더 깊이 알고 싶다면 이 튜토리얼을 추천합니다:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## 비트코인 받기


Wallet로 비트코인을 받으려면 Interface 왼쪽에서 원하는 계정을 선택한 다음 "*수령*" 버튼을 클릭합니다.


![Image](assets/fr/17.webp)


그러면 프로톤 Wallet이 자동으로 새로운 빈 Address를 생성합니다.


![Image](assets/fr/18.webp)


트랜잭션이 완료되면 "*거래*" 섹션에서 트랜잭션을 찾을 수 있습니다. "*+추가*"를 클릭하여 트랜잭션에 라벨을 지정합니다.


![Image](assets/fr/19.webp)


## 비트코인 보내기


이제 Wallet에 비트코인이 들어왔으니 전송할 수 있습니다. Interface의 왼쪽에서 원하는 계정을 선택한 다음 "*송금*"을 클릭합니다.


![Image](assets/fr/20.webp)


받는 사람의 Bitcoin Address를 입력합니다. 작은 로고를 클릭하여 QR 코드를 스캔할 수 있습니다. 이메일 Address로 보내려면 이 필드에 직접 입력합니다. Bitcoin Address를 입력했으면 작은 화살표를 클릭한 다음 "*확인*"을 클릭합니다.


![Image](assets/fr/21.webp)


송금할 금액을 법정 화폐 또는 비트코인으로 입력한 다음 "*검토*"를 클릭합니다.


![Image](assets/fr/22.webp)


현재 시장 상황에 따라 거래 수수료를 선택합니다.


![Image](assets/fr/23.webp)


거래에 라벨을 추가한 다음 모든 세부 정보를 다시 확인합니다. 모든 것이 정확하다면 '*확인 후 보내기*'를 클릭하여 거래에 서명하고 전송합니다.


![Image](assets/fr/24.webp)


이제 계정의 "*거래*" 섹션에 거래가 확인을 기다리는 상태로 표시됩니다.


![Image](assets/fr/25.webp)


## 애플리케이션에 로그인


웹 클라이언트 외에도 모바일 애플리케이션을 통해서도 Proton Wallet에 액세스할 수 있습니다. Wallet을 Proton 계정에 연결하면 웹 클라이언트와 모바일 앱 간에 Wallet을 동기화할 수 있습니다.


애플리케이션 스토어에서 Proton Wallet를 다운로드하세요:




- [앱 스토어](https://apps.apple.com/us/app/proton-Wallet-secure-btc/id6479609548);
- [구글 플레이 스토어](https://play.google.com/store/apps/details?id=me.proton.Wallet.android).


![Image](assets/fr/26.webp)


설치 후 "*로그인*"을 클릭하고 이메일 Address와 Proton 비밀번호를 입력합니다.


![Image](assets/fr/27.webp)


그러면 웹 클라이언트에서와 동일한 기능으로 Bitcoin Wallet에 액세스할 수 있습니다.


![Image](assets/fr/28.webp)


이제 Proton Wallet을 설정하고 사용하는 방법을 알게 되었습니다. 이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 공유해 주셔서 감사합니다!


더 자세히 알아보려면 블록스트림의 최신 Hardware Wallet인 제이드 플러스에 대한 이 튜토리얼을 추천합니다:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262