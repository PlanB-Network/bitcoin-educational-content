---
name: Mullvad VPN
description: 비트코인으로 결제하는 VPN 설정하기
---
![cover](assets/cover.webp)


VPN("*가상 사설망*")은 휴대폰 또는 컴퓨터와 VPN 제공업체가 관리하는 원격 서버 간에 안전하게 암호화된 연결을 설정하는 서비스입니다.


기술적으로 VPN에 연결하면 사용자의 인터넷 트래픽은 암호화된 터널을 통해 VPN 서버로 리디렉션됩니다. 이 과정을 통해 인터넷 서비스 제공업체(ISP) 또는 악의적인 공격자와 같은 제3자가 사용자의 데이터를 가로채거나 읽기 어렵게 만듭니다. 그런 다음 VPN 서버는 사용자를 대신하여 사용하려는 서비스에 연결하는 중개자 역할을 합니다. 이 서버는 사용자의 연결에 새로운 IP Address을 할당하여 사용자가 방문하는 사이트에서 실제 IP Address을 숨기는 데 도움을 줍니다. 그러나 일부 온라인 광고에서 말하는 것과는 달리, 모든 트래픽을 볼 수 있는 VPN 제공업체에 대한 신뢰가 필요하기 때문에 VPN을 사용한다고 해서 익명으로 인터넷을 브라우징할 수 있는 것은 아닙니다.

![MULLVAD VPN](assets/fr/01.webp)

VPN을 사용하면 얻을 수 있는 이점은 많습니다. 첫째, VPN 제공 업체가 고객님의 정보를 공유하지 않는다는 전제 하에, 고객님의 온라인 활동 정보를 ISP나 정부로부터 보호합니다. 둘째, 특히 MITM("**중간자**") 공격에 취약한 공용 Wi-Fi 네트워크에 연결할 때 데이터를 보호합니다. 셋째, VPN은 IP Address을 숨겨 지리적 제한과 검열을 우회하여 해당 지역에서 사용할 수 없거나 차단된 콘텐츠에 액세스할 수 있도록 합니다.


보시다시피, VPN은 트래픽 관찰의 위험을 VPN 제공업체에 전가합니다. 따라서 VPN 제공 업체를 선택할 때 등록에 필요한 개인 데이터를 고려하는 것이 중요합니다. 제공 업체가 전화 번호, 이메일 Address, 은행 카드 세부 정보 또는 더 심한 경우 우편 Address와 같은 정보를 요청하면 사용자의 신원이 트래픽과 연결될 위험이 높아집니다. 제공업체가 해킹당하거나 법적 압수수색을 당할 경우 사용자의 트래픽을 개인 데이터와 쉽게 연결할 수 있습니다. 따라서 개인 정보를 요구하지 않고 비트코인과 같은 익명 결제를 허용하는 제공업체를 선택하는 것이 좋습니다.


이 튜토리얼에서는 개인 정보가 필요하지 않은 간단하고 효율적이며 합리적인 가격의 VPN 솔루션을 소개합니다.


## 멀바드 VPN 소개

Mullvad VPN은 스웨덴의 서비스로, 사용자 개인 정보 보호에 대한 Commitment가 돋보이는 서비스입니다. 주요 VPN 제공 업체와 달리 Mullvad는 가입 시 개인 데이터를 요구하지 않습니다. 이메일 Address, 전화번호 또는 이름을 제공할 필요가 없으며, 대신 결제 및 서비스 액세스에 사용되는 익명의 계정 번호를 할당합니다. 또한 Mullvad는 서버를 통과하는 활동 로그를 보관하지 않는다고 주장합니다.

![MULLVAD VPN](assets/notext/02.webp)

멀바드는 Bitcoin 결제를 허용하므로 결제 시 신용카드 정보를 제공할 필요는 없습니다(공식 사이트에서만 온체인으로 결제할 수 있지만, 라이트닝을 통해 결제하는 비공식적인 방법도 있습니다). 또한 우편을 통한 현금 결제도 가능합니다.


Mullvad VPN은 또한 투명성과 보안으로 차별화됩니다. 소프트웨어는 오픈 소스이며, 애플리케이션과 인프라를 평가하기 위해 정기적으로 독립적인 보안 감사를 받고 그 결과를 [웹사이트에 게시](https://mullvad.net/fr/blog/tag/audits)합니다. 멀바드는 엄격한 개인정보 보호법으로 유명한 스웨덴에 본사를 둔 회사입니다. 자체 호스팅 서버만을 사용하므로 하이퍼스케일러 AWS, Google Cloud 또는 Microsoft Azure와 같은 타사 클라우드 서비스 사용과 관련된 위험을 제거합니다.


기능 측면에서 Mullvad는 VPN 연결이 끊어질 경우 사용자의 트래픽을 보호하는 킬 스위치, 특정 애플리케이션에 대한 VPN 비활성화 옵션, 여러 VPN 서버를 통해 트래픽을 라우팅하는 기능 등 좋은 VPN 클라이언트에서 기대할 수 있는 모든 기능을 제공합니다.


물론 이러한 서비스 품질에는 비용이 들지만, 공정한 가격은 종종 품질과 정직성을 나타내는 지표가 됩니다. 이는 회사가 사용자의 개인 데이터를 제3자에게 판매하지 않고도 비즈니스 모델을 가지고 있다는 신호일 수 있습니다. Mullvad VPN은 월 5유로의 정액제를 제공하며, 최대 5대 기기에서 사용할 수 있습니다.

![MULLVAD VPN](assets/notext/03.webp)

주류 VPN 제공업체와 달리, Mullvad는 반복적인 자동 구독이 아닌 서비스 액세스 시간을 구매하는 모델을 사용합니다. 선택한 기간 동안 비트코인을 일회성으로 결제하기만 하면 됩니다. 예를 들어, 1년 이용권을 구매하면 해당 기간 동안 서비스를 이용할 수 있으며, 그 이후에는 Mullvad 웹사이트로 돌아와서 이용 시간을 갱신해야 합니다.

또 다른 고품질 VPN 제공 업체인 IVPN과 비교했을 때, Mullvad는 약간 더 경제적입니다. 예를 들어, IVPN에서 3년 구매를 선택하더라도 월 비용은 약 5.40유로입니다. 하지만 IVPN은 몇 가지 추가 서비스를 제공하고 Mullvad보다 저렴한 요금제(표준 요금제)를 제공하지만, 이는 2개의 장치로만 제한되며 "멀티 홉" 프로토콜이 제외됩니다.

또한 비공식적인 속도 테스트를 통해 IVPN과 Mullvad를 비교했습니다. 성능 면에서 IVPN이 약간 우위를 보였지만, Mullvad의 속도는 여전히 매우 만족스러웠습니다. 주류 VPN 제공 업체와 비교했을 때, IVPN과 Mullvad는 경우에 따라서는 우월하지는 않더라도 최소한 비슷한 수준의 효율을 보여주었습니다.


## 컴퓨터에 Mullvad VPN을 설치하는 방법은 무엇인가요?


멀바드 공식 웹사이트](https://mullvad.net/en/download/)를 방문하여 "*다운로드*" 메뉴를 클릭합니다.

![MULLVAD VPN](assets/notext/04.webp)

Windows 또는 macOS 사용자의 경우, 사이트에서 직접 소프트웨어를 다운로드하고 설치 마법사의 안내에 따라 설치를 완료하세요.

![MULLVAD VPN](assets/notext/05.webp)

Linux 사용자의 경우 ["*Linux*"](https://mullvad.net/en/download/vpn/linux) 섹션에서 사용 중인 배포판에 맞는 지침을 찾을 수 있습니다.

![MULLVAD VPN](assets/notext/06.webp)

설치가 완료되면 계정 ID를 입력해야 합니다. 이 튜토리얼의 다음 섹션에서 이를 얻는 방법을 살펴보겠습니다.


## 스마트폰에 Mullvad VPN을 설치하는 방법은 무엇인가요?


IOS 사용자의 경우 [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513), Android 사용자의 경우 [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) 또는 [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/) 등 앱 스토어에서 Mullvad VPN을 다운로드하세요. 안드로이드를 사용하는 경우, [멀버드 사이트](https://mullvad.net/en/download/vpn/android)에서 '.apk' 파일을 직접 다운로드할 수도 있습니다.

![MULLVAD VPN](assets/notext/07.webp)

앱을 처음 사용하면 로그아웃됩니다. 서비스를 활성화하려면 계정 ID를 입력해야 합니다.

![MULLVAD VPN](assets/notext/08.webp)

이제 디바이스에서 Mullvad를 활성화하는 단계로 넘어가겠습니다.


## Mullvad VPN을 어떻게 결제하고 활성화하나요?


멀바드 공식 웹사이트](https://mullvad.net/)로 이동하여 "*시작하기*" 버튼을 클릭합니다.

![MULLVAD VPN](assets/notext/09.webp)

"*generate 계정 번호*" 버튼을 클릭합니다.

![MULLVAD VPN](assets/notext/10.webp)Mullvad will then create your account. You do not need to provide any personal information. It is only your account number that will allow you to log in. It acts somewhat like an access key. Save it in a safe place like your password manager, for example. You can also make a paper copy.

![MULLVAD VPN](assets/notext/11.webp)

그런 다음 "*계정에 시간 추가*" 버튼을 클릭합니다.

![MULLVAD VPN](assets/notext/12.webp)

그러면 계정의 로그인 페이지로 이동합니다. 계정 번호를 입력한 다음 '*로그인*' 버튼을 클릭합니다.

![MULLVAD VPN](assets/notext/13.webp)

결제 방법을 선택하세요. 비트코인으로 결제하면 10% 할인 혜택을 받을 수 있으므로 월 4.50유로까지 비용이 낮아지므로 비트코인을 사용하는 것이 좋습니다. 라이트닝을 통한 결제를 선호하는 경우 다음 부분에서 대체 방법을 알려드리겠습니다.

![MULLVAD VPN](assets/notext/14.webp)

"*일회성 결제 Address* 생성하기" 버튼을 클릭합니다.

![MULLVAD VPN](assets/notext/15.webp)

그런 다음 받은 Address에 표시된 금액을 Bitcoin Wallet으로 결제합니다.

![MULLVAD VPN](assets/notext/16.webp)

거래가 확인된 후 사이트에서 결제를 감지하기까지 몇 분 정도 걸릴 수 있습니다. Mullvad에서 결제가 감지되면 페이지 왼쪽 상단에 "*남은 시간 없음*"이라는 멘션 대신 구독 기간이 표시됩니다.

![MULLVAD VPN](assets/notext/17.webp)

그런 다음 소프트웨어에 계정 번호를 입력하여 VPN을 활성화할 수 있습니다.

![MULLVAD VPN](assets/notext/18.webp)

모바일 애플리케이션에서 VPN을 활성화하는 과정도 완전히 동일합니다. 계정 번호만 입력하면 됩니다.

![MULLVAD VPN](assets/notext/19.webp)

## 라이트닝으로 Mullvad VPN을 결제하는 방법은 무엇인가요?


아시다시피, 멀바드는 아직 Lightning Network을 통한 결제를 허용하지 않습니다. 하지만 [Lounès](https://x.com/louneskmt)의 추천으로 이 제한을 우회할 수 있는 비공식 서비스를 발견했습니다. Vpn.sovereign.engineering](https://vpn.sovereign.engineering/)에서 이용할 수 있는 이 서비스는 Lightning에서 결제를 수락하고 그 대가로 Mullvad의 유효한 요금제를 제공합니다.

![MULLVAD VPN](assets/notext/20.webp)

사이트 관리자를 신뢰하고 계정 번호를 직접 입력한 다음 "*로그인*"을 클릭하면 Mullvad 패키지가 자동으로 인증됩니다. 또는 "*예!"* 버튼을 클릭하여 Lightning에서 바우처를 구입한 다음 공식 Mullvad 사이트에서 패키지를 받을 때 사용할 수 있습니다. ![MULLVAD VPN](assets/notext/21.webp) 두 경우 모두 패키지 기간을 선택하라는 메시지가 표시됩니다. 6개월에서 1년 중에서 선택할 수 있습니다. ![MULLVAD VPN](assets/notext/22.webp) 그런 다음 "*Top-up with Lightning*" 버튼을 클릭하세요. ![MULLVAD VPN](assets/notext/23.webp) 구매를 완료하려면, 라이트닝 Wallet으로 Invoice를 결제하세요. ![MULLVAD VPN](assets/notext/24.webp) 바우처 구매를 선택한 경우, Mullvad 사이트에서 계정에서 사용 가능한 결제 방법 중 "*바우처*"를 선택하세요. 그런 다음, vpn.sovereign.engineering 사이트에서 받은 바우처 번호를 지정된 상자에 입력하세요. ![Mullvad VPN](assets/notext/25.webp) ## Mullvad VPN 사용 및 구성 방법은?


이제 활성 계정이 있고 Mullvad 소프트웨어 또는 앱에 계정 번호를 입력했으므로 VPN 서비스를 완전히 즐길 수 있습니다. ![MULLVAD VPN](assets/notext/26.webp) VPN 연결을 해제하려면 "*연결 해제*" 버튼을 클릭하기만 하면 됩니다. ![MULLVAD VPN](assets/notext/27.webp) "*연결 해제*" 버튼 옆의 작은 빨간색 화살표로 현재 위치를 변경하지 않고 서버를 변경할 수 있습니다. ![MULLVAD VPN](assets/notext/28.webp) VPN 서버의 도시를 변경하려면 "*위치 전환*"을 클릭하여 새 위치를 선택하세요. ![MULLVAD VPN](assets/notext/29.webp) 화면 상단에 기기의 닉네임과 남은 패키지 기간을 확인할 수 있습니다. ![MULLVAD VPN](assets/notext/30.webp) 작은 남자 아이콘을 클릭하면 계정에 대한 자세한 정보에 액세스할 수 있습니다. ![MULLVAD VPN](assets/notext/31.webp) 설정에 액세스하려면 톱니바퀴를 클릭하세요. ![MULLVAD VPN](assets/notext/32.webp) "*사용자 Interface 설정*" 메뉴에서 Interface 언어와 시스템에서의 동작 등 소프트웨어의 설정을 사용자 지정할 수 있습니다. ![MULLVAD VPN](assets/notext/33.webp) "*VPN 설정*" 메뉴에서 VPN과 관련된 옵션을 찾을 수 있습니다. "*시작 시 앱 실행*" 및 "*자동 연결*" 옵션을 활성화하여 컴퓨터가 시작될 때 VPN 연결이 자동으로 실행되도록 하는 것이 좋습니다.

![MULLVAD VPN](assets/notext/34.webp) In the "*DNS content blockers*" submenu, you have the option to filter and block DNS requests to malicious, advertising, or unwanted websites.

![MULLVAD VPN](assets/notext/35.webp)

마지막으로, "*분할 터널링*" 메뉴를 사용하면 컴퓨터에서 인터넷 트래픽이 VPN을 통해 라우팅되지 않는 특정 애플리케이션을 선택할 수 있습니다.

![MULLVAD VPN](assets/notext/36.webp)

웹사이트의 '*장치*' 메뉴를 클릭하면 Mullvad 계정에 대한 개요를 확인하고 연결된 다양한 장치를 관리할 수 있습니다.

![MULLVAD VPN](assets/notext/37.webp)

이제 Mullvad VPN을 완벽하게 즐길 수 있는 준비가 끝났습니다. 기능 및 가격 측면에서 Mullvad와 유사한 다른 VPN 제공 업체를 찾고 싶다면, IVPN에 대한 튜토리얼을 확인해보시기 바랍니다:


https://planb.academy/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68