---
name: COLDCARD - 공동 서명
description: 공동 서명 기능을 살펴보고 콜드카드에서 사용하세요
---

![cover](assets/cover.webp)


*참고: 이 튜토리얼은 다중서명 지갑, 코인라이트 디바이스, Sparrow wallet 또는 Nunchuk*과 같은 소프트웨어에 이미 어느 정도 경험이 있는 분들을 대상으로 합니다



![video](https://youtu.be/MjMPDUWWegw)




**왜 콜드카드 공동서명인가?



이 기능을 사용하면 하드웨어 보안 모듈(HSM) 방식으로 ColdCard(Q 또는 Mk4) 장치에 **지출 조건**을 추가하여 자금을 보호하는 동시에 상당한 유연성과 제어력을 유지할 수 있습니다.



예를 들어 지출 조건은 다음과 같습니다:





- 규모 제한**: 단일 거래에서 사용할 수 있는 비트코인 금액을 제한합니다.
- 속도 제한: ** 단위 시간당(시간당, 일당, 주당 등) 수행할 수 있는 트랜잭션 수를 결정하고, 최소 블록 수를 요구합니다.
- 사전 승인된 주소: ** 사전 승인된 주소로만 비트코인을 전송할 수 있습니다.
- 2단계 인증: ** 인터넷에 연결된 NFC 지원 스마트폰/태블릿에서 타사 2단계 인증 모바일 애플리케이션(TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)을 통해 확인해야 합니다.



**작동 방식



이 튜토리얼에서는 "지출 정책 키"라고 하는 두 번째 seed을 ColdCard Mk4 또는 Q 장치에 추가하면 되며, 이 키는 "C 키"라고 부릅니다.


이 추가 seed 외에도 Wallet Multisig 2-on-N을 생성하기 위해 "백업 키"라고 부르는 추가 키(XPUB)를 하나 이상 Supply해야 합니다.



요약하면, Wallet Multisig을 생성하고, ColdCard 장치에는 자금을 사용하는 데 필요한 2개의 개인 키, 즉 장치의 seed 마스터와 "지출 정책 키"가 포함됩니다.



'C 키'에 서명을 요청할 때마다 지정된 지출 조건이 적용되며, 거래가 해당 조건을 준수하는 경우에만 ColdCard가 서명합니다.



이러한 지출 조건을 적용하지 않으려는 경우 그렇게 할 수 있습니다:




- 백업 키와 seed 손 중 하나 또는 Multisig의 크기에 따라 백업 키 두 개로 서명합니다.
- "공동 서명" 메뉴에서 "지출 정책 키" 또는 "C 키"를 입력하면 됩니다. **후자는 기기에서 직접 확인할 수 없으며, 그렇지 않으면 설정된 지출 조건을 누구나 취소할 수 있습니다**




## ColdCard 공동 서명 구성



![video](https://youtu.be/MjMPDUWWegw)



### 1- 기능 활성화



우선, 디바이스에 최신 펌웨어 버전이 설치되어 있는지 확인하세요:




- Mk4: v5.4.2
- Q: v1.3.2Q




Mk4 또는 ColdCardQ에서 *고급 도구 > ColdCard 공동 서명*으로 이동합니다.



![Co-Sign](assets/fr/01.webp)



*다음 튜토리얼에서는 편의를 위해 ColdCardQ에서 스크린샷을 찍었지만, 단계와 메뉴는 Mk4와 Q에서 동일합니다*



기능에 대한 요약이 표시됩니다.


키를 지정하는 데 사용되는 용어는 곧 만들 2대3 다중 서명 Wallet에서 다시 사용하게 될 용어입니다:



키 A = 콜드카드 마스터 seed


키 B = 백업 키


키 C = 지출 정책 키



"**"를 클릭합니다.



![Co-Sign](assets/fr/02.webp)



다음 단계는 어떤 개인키가 "지출 정책 키" 또는 "키 C"로 작동할지 결정하는 것입니다.



우리에게 몇 가지 옵션이 열려 있음을 알 수 있습니다:





- 또는 **"입력"**를 눌러 12단어로 구성된 새로운 seed 문장을 generate으로 입력합니다.





- ""(1)"**를 클릭하여 기존 12단어 seed를 가져오거나 **""(2)"**를 선택하여 기존 24단어 seed를 가져옵니다.





- 또는 **"(6) "**를 눌러 장치의 볼트에서 seed을 가져옵니다.



이 튜토리얼에서는 **"(1) "**를 눌러 기존 12단어 seed을 가져오기로 했습니다. 이미 소유하고 있고 백업이 분명히 있는 seed BIP39를 가져올 수 있습니다.



키보드를 사용하여 seed의 12단어를 입력합니다. 이 예에서는 seed 유효 문구인 beef x 12를 선택합니다. 그런 다음 **"ENTER"**를 누릅니다.


*참고: 이 seed의 백업이 없는 경우, 지출 조건*을 변경하기 위해 디바이스에서 '공동 서명' 설정을 더 이상 수정할 수 없습니다



이제 장치에서 '공동 서명' 기능이 활성화되었습니다. 다음으로 지출 조건을 선택한 다음 다중 서명 Wallet 생성을 완료해야 합니다.



![Co-Sign](assets/fr/03.webp)



### 2- 지출 조건 또는 "*지출 정책*"을 선택합니다



여기서는 **"C 키"** 또는 **"지출 정책 키**"가 트랜잭션에 서명할 때 충족해야 하는 지출 조건을 지정합니다.



"공동 서명"** 메뉴에서 **"지출 정책**"을 클릭합니다.



그런 다음 최대 규모, 즉 단일 거래에서 사용할 수 있는 최대 사토시 수를 선택할 수 있습니다.



이 예에서는 최대 크기 **21212** 사토시를 선택하겠습니다. 확인하려면 **"입력"**을 클릭합니다.




![Co-Sign](assets/fr/04.webp)



그런 다음 최대 속도, 즉 장치가 단위 시간당 서명할 수 있는 트랜잭션 수를 설정하도록 선택합니다. 이 튜토리얼에서는 무제한 속도, 즉 트랜잭션 수에 제한이 없는 속도를 선택하겠습니다.




![Co-Sign](assets/fr/05.webp)



### 3- Wallet Multisig 2-on-N 생성



장치의 **마스터 Wallet**(키 A) 및 **"지출 정책 키"**(키 C) 외에 세 번째 키, 즉 **"백업 키"**(키 B)를 선택해야 합니다.



'B 키'는 SD 카드를 통해 가져오거나 ColdCardQ의 경우 QR 코드를 통해 가져와야 합니다.


이렇게 하려면 '키 B'를 사용하는 두 번째 ColdCard Mk4 또는 Q 장치가 필요합니다.



"백업 키"**가 들어 있는 두 번째 장치(이 예에서는 ColdCard Mk4)에서 메인 메뉴에서 **"설정"**으로 이동한 다음 **"Multisig Wallet"**, 마지막으로 **"Xpub 내보내기"**로 이동합니다.


(물론 두 번째 장치가 ColdCardQ인 경우 QR 코드를 통해 Xpub을 내보낼 수 있는 옵션이 있습니다).





![Co-Sign](assets/fr/06.webp)





다음 화면에서 SD 카드를 삽입하고 오른쪽 하단의 **"유효성 검사"** 버튼을 클릭합니다. 그런 다음 **"(1)"**를 클릭하여 SD 카드에 파일을 저장합니다.



파일 이름에 공개 키 지문(*지문*)이 포함되며, 파일 형식은 `ccxp-0F056943.json`입니다.




![Co-Sign](assets/fr/07.webp)



그런 다음 SD 카드를 "초기" ColdCardQ에 삽입하여 "백업 키"(키 B)를 가져옵니다.


'콜드카드 공동 서명' 메뉴에서 '빌드 2-of-N'을 선택한 다음 다음 화면에서 **"입력"**을 클릭한 다음 다시 **"입력"**을 클릭하여 SD 카드에서 '백업 키'를 가져옵니다.



![Co-Sign](assets/fr/08.webp)



다음 화면에서 '계좌 번호'를 비워두고(정확히 알고 있는 경우가 아니라면) **"입력"**을 다시 클릭합니다.



![Co-Sign](assets/fr/09.webp)



드디어 다음과 같이 구성된 새로운 Wallet Multisig 2-sur-3을 사용할 준비가 되었습니다:



키 A= 콜드카드 Q 마스터 seed


키 B= 백업 키(두 번째 콜드카드 장치에서 방금 가져온 키)


키 C= 지출 정책 키(서명에 사용되는 경우 미리 정의된 지출 조건을 부과)



## Sparrow wallet과 공동 서명



필요한 경우 아래 튜토리얼을 참조하여 Sparrow wallet 소프트웨어에 익숙해지세요:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Wallet Multisig 2-sur-3을 Sparrow wallet으로 내보내기



이제 첫 번째 사토시를 배치할 수 있도록 Wallet Multisig을 Sparrow로 내보내야 합니다.



콜드카드큐의 메인 메뉴에서 **"설정"**을 선택한 다음 **"Multisig 지갑"**을 선택합니다.


이제 콜드카드에 알려진 Multisig 지갑 세트가 표시되며, 여기에 포함된 키의 수는 "2/3"(2-sur3)입니다. 방금 생성한 Multisig **"콜드카드 공동 서명"**을 선택한 다음 **"콜드카드 내보내기"**를 클릭합니다.



![Co-Sign](assets/fr/10.webp)




마지막으로 Wallet를 Sparrow로 내보낼 수 있는 방법을 선택합니다. 여기서는 SD 카드를 선택하므로 장치의 슬롯 A에 SD 카드를 삽입한 후 **"(1) "**를 클릭합니다.



![Co-Sign](assets/fr/11.webp)



그런 다음 Sparrow wallet에서 "Wallet 가져오기"를 선택합니다.



![Co-Sign](assets/fr/12.webp)



그런 다음 **"파일 가져오기"**를 클릭합니다. 그런 다음 SD 카드에 있는 **"export-Coldcard_Co-sign.txt"** 파일을 선택합니다.



![Co-Sign](assets/fr/13.webp)



Sparrow에 표시되는 대로 Wallet의 이름을 지정하고 Wallet을 암호화할 비밀번호를 선택합니다(또는 사용하지 않을 수도 있음).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



이제 첫 번째 사토시를 받고 Wallet에 적용한 지출 조건을 테스트할 준비가 되었습니다.



![Co-Sign](assets/fr/16.webp)



### 2- 사전 정의된 지출 정책 테스트



다시 말씀드리자면, 저희는 Wallet Multisig의 최대 규모를 21212 사토시로 결정했습니다. 즉, 지출 정책 키(키 C)가 거래에 서명할 때마다 지출된 금액이 21212 사토시 이하일 때만 유효하다는 의미였습니다.



테스트해 보겠습니다.


먼저 Sparrow에서 '수신' 탭을 클릭하고 이 튜토리얼에서 사용할 Wallet에 Sats를 몇 개 드롭해 보겠습니다.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



그런 다음 50,000 Sats 거래를 시뮬레이션하여 허용된 21212 사토시보다 더 많이 사용해 보겠습니다.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



콜드카드큐로 *서명되지 않은* 거래를 나타내는 QR 코드를 스캔하여 거래를 가져오면 다음과 같은 화면이 표시됩니다. 지출 조건이 충족되지 않았다는 경고 메시지가 표시됩니다. 어쨌든 거래에 서명하면 2개의 키 중 하나(장치의 seed 마스터, "키 C"는 아님)만 서명됩니다.




![Co-Sign](assets/fr/23.webp)



여기서 트랜잭션을 Sparrow로 가져온 후, 트랜잭션에 서명 중 하나만 적용된 것을 볼 수 있습니다.



![Co-Sign](assets/fr/24.webp)




이제 실험을 반복하되, 21,000 사토시, 즉 이 Wallet에 설정한 최대 규모(21212 Sats)보다 적은 거래에 대해 반복해 보겠습니다.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



콜드카드큐로 이 거래에 서명해 보겠습니다.



이번에는 문제없이 경고 메시지가 나타나지 않으며 서명된 트랜잭션을 Sparrow wallet로 가져올 때 이번에는 2개의 서명이 적용되어 트랜잭션이 유효하고 배포할 준비가 되었습니다.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## 쌍절곤으로 공동 서명



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- 웹 2FA 및 화이트리스트 주소



이 단락에서는 Wallet Multisig 공동 사인을 사용하여 새로운 지출 조건을 적용하여 어떻게 진행되는지 살펴볼 것입니다.



고급 도구 > 콜드카드 공동 서명*으로 이동합니다.


지출 조건을 변경할 수 있는 메뉴에 액세스하려면 "지출 정책 키"를 입력하라는 메시지가 표시됩니다. 저희의 경우 "쇠고기"를 12번 입력했습니다.



이 튜토리얼과 관련된 현실적인 이유로 최대 "제한 속도"는 21212 Sats으로 유지하기로 결정했습니다. 반면에 **"화이트리스트 주소"** 메뉴를 사용하여 자금을 사용할 수 있는 주소를 지정할 것입니다.




![Co-Sign](assets/fr/31.webp)




화이트리스트에 추가하려는 주소(2개 선택)와 관련된 QR 코드를 스캔한 다음 **"입력"**을 클릭합니다. "ENTER"**를 연속으로 눌러 주소를 확인하면 매그니튜드 및 수취인 주소에 제한이 적용된 것을 확인할 수 있습니다.



![Co-Sign](assets/fr/32.webp)



마지막으로 '공동 서명'이 제공하는 가능성을 완벽하게 파악하기 위해 '웹 2FA' 옵션을 활성화해 보겠습니다.


이 기능을 사용하면 구글 인증기/엔테 인증기/프로톤 인증기/오티 2FA/이지스 인증기 등 TOTP RFC-6238 호환 애플리케이션을 사용하여 Layer의 보안을 추가할 수 있습니다.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

구체적으로 설명하자면, 거래에 서명하기 전에 NFC가 활성화되고 인터넷에 연결된 장치를 Coldcard에 가까이 가져가야 합니다. 그러면 자동으로 coldcard.com 웹 페이지로 이동하여 애플리케이션의 6자리 코드를 입력하라는 메시지가 표시됩니다. 올바른 코드를 입력하면 웹 페이지에 ColdCardQ를 스캔할 수 있는 QR코드 또는 Mk4에 입력할 수 있는 8자리 코드가 표시되어 장치에 서명할 수 있는 권한이 부여됩니다.





![Co-Sign](assets/fr/33.webp)



이중 인증 애플리케이션에 표시된 QR 코드를 스캔하고 콜드카드 공동 서명(CCC) 계정을 추가한 후, 2FA 코드를 입력하여 모든 것이 정상인지 확인하라는 메시지가 표시됩니다.



NFC 장치 뒷면에 콜드카드를 입력합니다.



![Co-Sign](assets/fr/34.webp)



웹 페이지가 열리면 즐겨 사용하는 애플리케이션의 2FA 코드를 입력합니다. 그런 다음 ColdCardQ에 표시된 QR 코드를 스캔합니다(또는 Mk4에 표시된 8자리 코드를 입력).



![Co-Sign](assets/fr/35.webp)




이제 크기(21212 Sats), 대상 주소 및 이중 인증에 제한을 두었습니다.



![Co-Sign](assets/fr/36.webp)



### 2- Wallet Multisig을 쌍절곤으로 2대3 내보내기



이전에 Sparrow에서 했던 것처럼 이번에는 Wallet Multisig 2대3을 쌍절곤으로 내보내 보겠습니다.


설정 > Multisig 지갑 > 2/3: 콜드카드 공동 서명 > 콜드카드 내보내기*로 이동합니다.



![Co-Sign](assets/fr/10.webp)



이번에는 **"NFC"**라는 이름의 ColdcardQ 버튼을 클릭하여 내보내기용 NFC 옵션을 선택합니다.



![Co-Sign](assets/fr/37.webp)



쌍절곤에서 애플리케이션을 처음 여는 경우 **"기존 Wallet 복구"**를 클릭합니다.



![Co-Sign](assets/fr/38.webp)



애플리케이션에 이미 Wallet이 있는 경우 오른쪽 상단의 **"+"**를 클릭한 다음 **"기존 Wallet 복구"**를 클릭합니다.



![Co-Sign](assets/fr/39.webp)




그런 다음 **"콜드카드에서 Wallet 복구"**를 선택한 다음 **"Multisig Wallet"**를 선택합니다.



![Co-Sign](assets/fr/40.webp)



마지막으로 스마트폰 뒷면을 ColdCardQ 화면에 탭하여 NFC를 통해 Wallet을 가져옵니다.



![Co-Sign](assets/fr/41.webp)



이전에 Sparrow wallet를 통해 입금된 계정과 사토시가 다시 돌아왔습니다.



![Co-Sign](assets/fr/42.webp)



### 3- 사전 정의된 지출 정책 테스트



이제 설정한 두 가지 지출 조건을 위반하는 트랜잭션을 만들어 보겠습니다. **승인되지 않은 Address에 21212 Sats을 초과하여 지출해 보겠습니다.** 무작위 Address에 22222 Sats을 전송해 보겠습니다.



![Co-Sign](assets/fr/43.webp)



거래가 생성되면 오른쪽 상단에 있는 작은 점 3개를 클릭하여 콜드카드로 내보냅니다.



![Co-Sign](assets/fr/44.webp)



그런 다음 **"BBQR을 통해 내보내기"**를 선택하고 ColdCardQ에 표시된 QR 코드를 스캔합니다.



![Co-Sign](assets/fr/45.webp)



그러면 화면 하단으로 스크롤하면 예상대로 해당 거래가 지출 조건을 위반한다는 경고가 ColdcardQ에 표시됩니다.



**잠재적인 공격자가 제한을 우회하는 것을 방지하기 위해 어떤 지출 조건이 적용되는지는 알려주지 않습니다**




![Co-Sign](assets/fr/46.webp)



그래도 **"ENTER"**를 눌러 유효성을 확인하면 서명된 트랜잭션을 나타내는 QR코드가 나타납니다. 쌍절곤으로 가져오면 서명이 하나만 적용된 것을 확인할 수 있습니다.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






이번에는 정확히 동일한 작업을 수행하되, 이번에는 크기 제한(21212 Sats)을 준수하고 미리 구성한 2개의 주소 중 하나에 사토시를 보내는 트랜잭션을 사용해 보겠습니다.



쌍절곤 12121 Sats을 두 주소 중 한 곳으로 보냅니다. 그런 다음 이전에 수행한 것처럼 거래를 콜드카드로 내보냅니다.



![Co-Sign](assets/fr/49.webp)




서명되지 않은 트랜잭션을 콜드카드큐로 가져온 후, 이번에는 어떤 내용이 표시되는지 살펴봅시다.



경고는 항상 표시되지만 이번에는 화면 하단으로 스크롤하면 2FA를 통해 거래를 확인해야 한다는 메시지가 표시됩니다. 이 장치는 인터넷에 연결된 NFC 단말기(스마트폰 또는 태블릿)에 ColdcardQ를 가까이 가져가라고 요청하며, 그렇게 합니다.



![Co-Sign](assets/fr/50.webp)



스마트폰에 웹 페이지가 열리고 2FA 코드를 입력하라는 메시지가 표시되며, 프로톤 인증기 덕분에 입력합니다.



![Co-Sign](assets/fr/51.webp)





그런 다음 웹 페이지에 표시되는 QR 코드를 스캔하여 거래에 서명할 콜드카드를 승인합니다.


이제 트랜잭션이 2개의 키로 서명되었으므로 유효합니다.



콜드카드큐에서 '푸시 송신'이 활성화되어 있으면 스마트폰 뒷면을 탭하는 것만으로 거래를 네트워크에 직접 송신할 수 있습니다.



![Co-Sign](assets/fr/52.webp)




"Push tx"가 활성화되어 있지 않은 경우, 이전 예시와 같은 방법으로 ColdCardQ의 "QR" 버튼을 눌러 서명된 거래를 QR 코드로 표시하고 이를 Nunchuk으로 가져옵니다.



![Co-Sign](assets/fr/53.webp)



이번에는 2개의 서명이 적용되었으므로 트랜잭션이 Bitcoin 네트워크에서 브로드캐스트될 준비가 된 것을 알 수 있습니다.



![Co-Sign](assets/fr/54.webp)




이번 튜토리얼에서는 코인라이트의 콜드카드큐와 Mk4 디바이스에 통합된 코사인 기능의 가능성과 Sparrow, Nunchuk과 같은 지갑을 통한 사용법에 대해 간략하게 살펴보겠습니다.