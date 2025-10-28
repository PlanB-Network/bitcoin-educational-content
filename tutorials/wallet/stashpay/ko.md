---
name: StashPay
description: 모두를 위한 미니멀리스트 Bitcoin Wallet
---

![cover](assets/cover.webp)



사용자 경험은 전 세계적으로 Bitcoin 솔루션을 채택하는 데 있어 핵심적인 요소입니다. 많은 지갑과 Exchange 플랫폼은 원활하고 단순하며 기술적으로 방해받지 않는 경험을 제공하는 것을 최우선 과제로 삼고 있습니다. 이러한 측면에서 StashPay는 미니멀한 접근 방식이 돋보이는 동시에 Lightning Network의 강력한 성능을 보여줍니다.



이 튜토리얼에서는 이 포트폴리오의 작동 방식과 소규모 비즈니스 또는 개인 사업자에게 이상적인 포트폴리오를 살펴봅니다.



## StashPay 시작하기



StashPay는 미니멀한 사용자 중심의 사용자 경험으로 인정받은 라이트닝 셀프 커스터디 Wallet입니다.  이 Wallet를 사용하면 기술적 지식이 없어도 첫 사토시를 수신하고 전송할 수 있습니다.



스태시페이는 리액트 네이티브로 개발된 오픈소스 프로젝트로, Bitcoin 프로토콜의 메인 체인에서 거래할 때에도 높은 거래 수수료 문제를 해결하는 것을 목표로 합니다. 웹사이트](https://stashpay.me/)에 있는 다운로드 링크를 통해 Android 및 iOS 플랫폼에서 모바일 앱으로 사용할 수 있습니다.



![introduce](assets/fr/01.webp)



Android 애플리케이션은 Google Play 스토어에서 사용할 수 없으므로 웹사이트에서 다운로드하는 것이 중요합니다.


다운로드가 완료되면 Android 휴대폰에 애플리케이션을 설치할 수 있도록 필요한 권한을 부여하세요.



애플리케이션이 설치되면 StashPay는 처음 열 때 초기 Bitcoin Wallet을 생성합니다. 거래하기 전에 이 Wallet을 백업하는 것이 좋습니다. 아래에서 복구 문구가 제대로 백업되었는지 확인하기 위한 모든 지침을 확인하실 수 있습니다.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

"설정" 아이콘을 클릭하여 StashPay 설정에 액세스한 다음 **백업 생성** 옵션을 클릭합니다. 그런 다음 복구 문구 표시를 승인합니다. 휴대폰에 설치된 다른 사기성 애플리케이션에서 액세스할 수 있으므로 복구 문구를 휴대폰의 클립보드에 복사하지 마세요.



![backup](assets/fr/02.webp)



또한 **Wallet 복구하기** 옵션을 클릭하고 12개 또는 24개의 복구 단어를 입력하여 이미 사용 중인 Bitcoin Wallet을 검색할 수도 있습니다.



### StashPay에서 첫 사토시 받기



홈 화면에서 **받기** 버튼을 클릭하고 빨간색으로 지정된 금액보다 큰 금액을 설정합니다. 저희의 경우, StashPay Wallet로 0.11 USD 미만을 받을 수 없습니다.



![receive](assets/fr/03.webp)



금액을 정의했으면 **Invoice 생성** 버튼을 클릭한 다음 Invoice를 스캔하거나 복사하여 사토시 발신자에게 전송할 수 있습니다.



![receive_sats](assets/fr/04.webp)



홈 페이지에서 '시계' 아이콘을 클릭하면 거래 내역을 확인할 수 있습니다.



![network_fee](assets/fr/05.webp)



사토시를 받으려면 네트워크 수수료를 지불해야 한다는 것을 알고 계실 것입니다. 이 수수료는 곧 받게 될 사토시에서 차감됩니다. 이는 StashPay가 Breez 개발 키트에 기반한 Wallet이기 때문입니다. 라이트닝 노드 없이 키트를 구현하여 사토시를 받으려면 Breez는 고객에게 '0.25% + 40 사토시'를 청구합니다(저희의 경우 StashPay). 자세한 내용은 미스티 브리즈 튜토리얼에서 확인하세요.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### StashPay로 비트코인 보내기



미니멀한 Interface 덕분에 StashPay로 비트코인을 송금하는 것은 매우 직관적입니다. 홈 화면에서 **송금** 버튼을 클릭합니다. QR 코드를 스캔하거나 사토시를 보내고자 하는 Address를 붙여넣습니다. StashPay는 비트코인을 보내고자 하는 Bitcoin 프로토콜 체인을 자동으로 감지합니다.



![send](assets/fr/06.webp)



스태시페이는 브리즈 개발 키트를 기반으로 하는 Wallet이므로, 메인 체인에서 저렴한 비용으로 비트코인을 전송할 수 있다는 흥미로운 이점이 있습니다. 브리즈는 볼트 서비스를 사용하여 Bitcoin 프로토콜의 여러 체인 간에 거래를 수행하므로 개발 키트를 구현하는 고객은 애플리케이션에서 직접 이 서비스의 이점을 누릴 수 있습니다.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

그러나 브리즈 SDK는 메인 체인에서 Address로 비트코인을 전송할 수 있는 최소 금액을 부과합니다.



![onchain](assets/fr/07.webp)



수취인의 라이트닝 Address을 사용해 비트코인을 보낼 수도 있습니다. 거래 세부 정보를 검토한 다음 **송금** 버튼을 클릭하여 확인합니다.



![confirm](assets/fr/08.webp)



## 더 많은 구성



StashPay 설정에서 설정을 조정하여 Wallet의 사용을 개인화할 수 있습니다.



StashPay를 사용하면 선택한 현지 통화를 기준으로 Exchange 사토시를 받을 수 있습니다. 통화** 옵션을 클릭한 다음 StashPay에서 제공하는 +113개 통화 목록에서 원하는 통화를 검색하세요.



![currencies](assets/fr/09.webp)



수령 옵션** 메뉴에서 StashPay로 비트코인을 수령하기 위한 모든 설정을 찾을 수 있습니다. 예를 들어, **라이트닝 또는 온체인 선택**을 선택하면 Wallet이 메인 체인에서 비트코인을 받을 수 있도록 설정할 수 있습니다.



![receive-onchain](assets/fr/10.webp)



온체인 주소 스캔** 옵션을 사용하면 다양한 주소에 연결된 모든 UTXO(아직 사용하지 않은 비트코인)를 확인하여 Wallet의 잔액을 새로 고칠 수 있습니다.



![rescan](assets/fr/11.webp)



로그 내보내기** 메뉴에는 다양한 Bitcoin 프로토콜 체인 간의 거래 및 원자 교환과 관련된 모든 브리즈 및 볼츠 인프라 작업이 나열되어 있습니다.



![export](assets/fr/12.webp)



이제 스테이시페이의 미니멀한 Bitcoin Wallet에 익숙해지기만 하면 됩니다. 이 튜토리얼이 유용했다면, Bitcoin을 시작하고 첫 비트코인을 얻는 방법에 대한 튜토리얼을 추천합니다.



https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f