---
name: Alby Hub
description: 나만의 라이트닝 노드를 쉽게 시작하려면 어떻게 해야 하나요?
---
![cover](assets/cover.webp)


Alby Hub는 인기 있는 Lightning 웹 확장 프로그램의 개발사인 Alby의 최신 오픈 소스 소프트웨어입니다. Alby Hub는 가장 사용하기 쉬운 라이트닝 노드를 갖춘 자체 관리형 Wallet로, 어디서나 액세스하여 수십 개의 앱과 통합할 수 있습니다. Alby Hub는 라이트닝 노드를 관리하기 위한 사용하기 쉬운 Interface입니다.


이 튜토리얼에서는 알비 허브의 다양한 사용 방법과 알비 고, 알비의 모바일 앱 또는 알비 브라우저 확장에 연결하는 방법을 살펴봅니다. 이렇게 하면 노드를 자율적으로 관리하면서 이동 중에도 Sats를 사용할 수 있습니다.


![ALBY HUB](assets/fr/01.webp)


## 앨비 허브란 무엇인가요?


앨비 허브는 앨비 생태계의 새로운 주력 도구가 될 예정입니다. 이 소프트웨어를 통해 사용자는 통합된 라이트닝 노드를 통해 자신의 Wallet를 쉽게 관리할 수 있으며, 동시에 자신의 키(셀프 커스터디)인 Ownership를 유지할 수 있습니다.


Alby Hub는 적응력이 뛰어난 도구입니다. 초보자와 고급 사용자 모두의 요구를 충족시킬 수 있습니다. 초보자는 이 도구를 사용하여 근본적인 복잡성을 처리할 필요 없이 혼자서 실제 Lightning 노드를 쉽게 운영할 수 있습니다. 숙련된 사용자의 경우, Alby Hub를 완전한 Interface로 사용하여 기존 Lightning 노드를 고급 관리할 수 있습니다.


필요에 따라 Alby Hub는 4가지 구성으로 제공됩니다:




- 앨비 허브 클라우드 :**


초보자에게 이상적인 첫 번째 옵션은 Alby 클라우드 옵션입니다. 이 옵션을 사용하면 Alby 허브 Interface을 통해 액세스할 수 있는 Alby 관리 서버에 직접 허브를 배포할 수 있습니다. Alby가 서버를 관리하지만, 키는 본인만 아는 비밀번호를 사용하여 암호화되므로 자금에 대한 주권은 귀하가 보유합니다. 그러나 노드가 작동하려면 키가 RAM에서 해독된 상태로 유지되어야 하므로 이론적으로 누군가 서버에 물리적으로 액세스할 경우 키가 위험에 노출될 수 있습니다. 초보자에게는 흥미로운 절충안이지만 위험을 인식하는 것이 중요합니다.


이 옵션의 가장 큰 장점은 호스팅을 직접 관리할 필요 없이 24시간 연중무휴로 운영할 수 있다는 것입니다. 또한 채널 백업을 직접 관리해야 하는 자체 호스팅 옵션에 비해 Lightning 노드의 백업이 간소화되고 자동화됩니다.


Alby Cloud는 유료 서비스입니다[자세한 내용은 요금 확인](https://albyhub.com/#pricing)을 참조하세요. 요금은 Alby에서 발급한 Lightning Invoice을 통해 Wallet에서 자동으로 차감됩니다. 이는 구독과 관련된 Alby 인보이스를 자동으로 결제하도록 노드를 구성하는 NWC 연결을 통해 이루어집니다.





- 기존 노드가 있는 Alby Hub :**


예를 들어 Umbrel 또는 Start9에 이미 호스팅된 노드가 있는 경우, Alby Hub를 ThunderHub 또는 RTL과 같은 방식으로 고급 관리 Interface로 사용할 수 있습니다.




- 앨비 허브 로컬 :**


PC에 직접 Alby Hub를 설치할 수도 있지만, 이 옵션은 라이트닝 노드에 원격으로 액세스하려면 PC가 항상 활성 상태를 유지해야 하므로 실용성이 떨어집니다. 하지만 이 방법은 특정 요구 사항에 적합할 수 있습니다.




- 개인 서버의 Alby Hub :**


고급 사용자의 경우 간단한 명령으로 개인 서버에 Alby Hub를 배포할 수 있습니다. 이 옵션은 이 튜토리얼에서 다루지 않지만 Alby의 GitHub에서 전용 지침을 찾을 수 있습니다(https://github.com/getAlby/hub?tab=readme-ov-file#docker).


이 튜토리얼은 주로 Interface에 초점을 맞추지만, 선택한 옵션에 관계없이 동일합니다. 또한 유료 클라우드 옵션과 노드 인 박스 옵션(Umbrel 또는 Start9)을 사용하여 Alby Hub를 배포하는 방법도 살펴봅니다.


![ALBY HUB](assets/fr/02.webp)


PC에 로컬로 설치하려면 운영 체제에 따라 소프트웨어를 다운로드하여 설치한 다음(https://github.com/getAlby/hub/releases), Interface에서 동일한 지침을 따릅니다.


![ALBY HUB](assets/fr/03.webp)


## Alby 계정 만들기


첫 번째 단계는 Alby 계정을 만드는 것입니다. Alby Hub를 사용하는 데 반드시 필요한 것은 아니지만, 이를 통해 Lightning Address를 얻을 수 있는 가능성을 포함하여 사용 가능한 옵션을 최대한 활용할 수 있습니다.


알비 공식 웹사이트](https://getalby.com/)로 이동하여 "*계정 만들기*" 버튼을 클릭합니다.


![ALBY HUB](assets/fr/04.webp)


닉네임과 이메일 Address을 입력한 다음 "*가입하기*"를 클릭합니다. 이 이메일 Address은 나중에 계정에 로그인할 때 사용됩니다.


![ALBY HUB](assets/fr/05.webp)


이메일로 받은 인증 코드를 입력합니다.


![ALBY HUB](assets/fr/06.webp)


온라인 계정에 로그인한 후 '*계속*' 버튼을 클릭합니다.


![ALBY HUB](assets/fr/07.webp)


"*계속*"을 다시 클릭합니다.


![ALBY HUB](assets/fr/08.webp)


## 클라우드 호스팅 옵션


그런 다음 자신의 디바이스에 Alby Hub를 설치하는 자체 호스팅 옵션 또는 프리미엄 옵션 중에서 선택해야 합니다. 먼저 프로 클라우드 옵션을 진행하는 방법부터 설명하겠습니다(유료 옵션이므로 이전 섹션의 자세한 내용을 참조하세요).


"*업그레이드*"를 클릭합니다.


![ALBY HUB](assets/fr/09.webp)


"*지금 구독하기*"를 클릭하여 확인합니다.


![ALBY HUB](assets/fr/10.webp)


"*알비 허브 시작*"을 클릭합니다.


![ALBY HUB](assets/fr/11.webp)


노드가 생성되는 동안 잠시 기다리세요.


![ALBY HUB](assets/fr/12.webp)


이제 Alby Hub가 구성되었습니다. 다음 섹션에서는 기존 노드에 Alby Hub를 설치하는 방법을 보여드리겠습니다. 아직 라이트닝 노드가 없는 경우 다음 섹션으로 건너뛰고 Alby Cloud에서 Alby Hub를 구성할 수 있습니다.


![ALBY HUB](assets/fr/13.webp)


## 셀프 호스팅 옵션


기존 Lightning 노드에 Alby Hub를 Interface로 사용하려는 경우 서버에 설치하거나 컴퓨터에 로컬로 설치하거나 노드 인 박스(Umbrel 또는 Start9)를 통해 설치하는 등 여러 가지 옵션이 있습니다. 이러한 구성에서 Alby Hub를 사용하는 것은 무료입니다. 물리적 액세스가 없는 서버 옵션은 클라우드 버전과 비슷한 위험을 내포하고 있으며 PC에 로컬 설치는 부적합한 경우가 많으므로 여기서는 노드 인 박스 옵션에 집중하겠습니다.


Umbrel에서 이를 설정하려면(Start9의 단계는 동일), 먼저 LND 노드가 이미 구성되어 있어야 합니다.


엄브렐 Interface에 로그인하고 애플리케이션 스토어로 이동합니다.


![ALBY HUB](assets/fr/14.webp)


"*알비 허브*" 애플리케이션을 찾습니다.


![ALBY HUB](assets/fr/15.webp)


노드에 설치합니다.


![ALBY HUB](assets/fr/16.webp)


이제 Alby Hub Interface이 준비되었습니다. 나머지 튜토리얼은 클라우드 Interface을 사용하는 것처럼 따라할 수 있지만 유료 버전의 옵션이 없습니다. 또한 클라우드 버전과 달리 키는 Alby 서버가 아닌 노드에 로컬로 저장됩니다.


![ALBY HUB](assets/fr/17.webp)


## Alby Hub 시작


"*시작하기*" 버튼을 클릭합니다.


![ALBY HUB](assets/fr/18.webp)


그러면 Alby Hub에서 비밀번호를 선택하라는 메시지가 표시됩니다. 이 비밀번호는 Wallet을 암호화하는 데 사용되므로 매우 중요합니다. 유료 클라우드 버전에서는 사용자 키가 Alby 서버에 저장되며, 사용자만 아는 이 비밀번호로 암호화된 다음 해독되어 필요할 때 트랜잭션에 서명하기 위해 RAM에만 저장됩니다.


따라서 강력한 비밀번호를 선택하는 것이 중요합니다. 이 비밀번호를 아는 사람은 누구나 잠재적으로 내 노드에 액세스할 수 있습니다. 또한 보안을 강화하기 위해 이 비밀번호를 종이나 금속 조각에 하나 이상의 물리적 백업본을 만들어 두는 것이 좋습니다.


비밀번호를 신중하게 선택하고 저장한 후 "*비밀번호 생성*"을 클릭합니다.


![ALBY HUB](assets/fr/19.webp)


이제 라이트닝 노드에 액세스할 수 있습니다.


![ALBY HUB](assets/fr/20.webp)


가장 먼저 해야 할 일은 키가 파생된 복구 문구를 저장하는 것입니다. 이렇게 하려면 "설정"을 클릭합니다. 이 문구를 사용하면 자동 백업을 활성화한 경우 Wallet에 대한 액세스를 복구할 수 있습니다.


![ALBY HUB](assets/fr/21.webp)


그런 다음 '*백업*' 탭으로 이동합니다. 비밀번호를 입력하여 액세스합니다.


![ALBY HUB](assets/fr/22.webp)


그러면 12단어 복구 문구에 액세스할 수 있습니다. 이 문구를 종이나 금속에 하나 이상 복사하여 안전한 곳에 보관하세요.


![ALBY HUB](assets/fr/23.webp)


문구를 저장한 후 확인란을 선택하여 저장했음을 확인하고 "*계속*"을 클릭합니다.


![ALBY HUB](assets/fr/24.webp)


## 비트코인에 대한 액세스 권한을 복구하려면 어떻게 해야 하나요?


알비 허브에 자금을 송금하기 전에 문제 발생 시 자금을 복구하는 방법과 복구에 필요한 정보를 이해하는 것이 중요합니다. 프로세스는 복구할 자금의 성격과 노드의 호스팅 모드에 따라 다릅니다.


유료 클라우드 사용자의 경우, 비트코인을 완전히 복구하려면 세 가지 필수 Elements이 필요합니다:



- 복구 문구;
- Alby 계정에 액세스하여 자동 백업을 검색합니다.


이 두 가지 정보 중 하나라도 없으면 비트코인을 전액 복구할 수 없습니다.


자체 기기에서 Alby Hub를 실행하는 경우 복구 프로세스는 [여기](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account)에 문서화되어 있습니다.


기존 노드에 Alby Hub를 설치한 경우 해당 특정 노드 운영 체제의 복구 프로세스를 따라야 합니다. 예를 들어 엄브렐은 라이트닝 채널의 최신 상태를 암호화하고 Tor를 통해 동적으로 익명으로 저장할 수 있는 [옵션](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md)을 제공합니다. Alby의 자동 백업을 통해서만 채널을 닫지 않고도 허브를 완전히 복구할 수 있다는 점에 유의하세요.


## 첫 번째 라이트닝 채널 구매


이제 Alby Hub에서 제공하는 지침을 따를 수 있습니다. 버튼을 클릭하여 첫 번째 현금 수신 채널을 엽니다.


![ALBY HUB](assets/fr/25.webp)


"*개방 채널*"을 선택합니다. 라우팅 노드가 되고 싶지 않고 특별히 필요하지 않다면 비공개 채널을 선택하는 것이 좋습니다.


![ALBY HUB](assets/fr/26.webp)


앨비 허브는 generate을 Invoice로 지급합니다. 이 지불에는 채널 개설에 필요한 거래 수수료와 노드에 채널을 개설해줄 LSP(*라이트닝 서비스 제공자*)의 서비스 수수료가 포함되며, 즉시 대금을 받을 수 있습니다.


![ALBY HUB](assets/fr/27.webp)


Invoice이 결제되고 거래가 확인되면 첫 번째 라이트닝 채널이 설정됩니다.


![ALBY HUB](assets/fr/28.webp)


"*노드*" 탭에서 이제 현금이 들어오는 것을 확인할 수 있으며, 라이트닝을 통해 결제를 받을 수 있습니다.


![ALBY HUB](assets/fr/29.webp)


대금을 받으려면 "*Wallet*" 탭을 클릭한 다음 "*수령*"을 클릭하세요.


![ALBY HUB](assets/fr/30.webp)


금액을 입력하고 필요한 경우 설명을 추가한 다음 "*Invoice* 생성"을 클릭합니다.


![ALBY HUB](assets/fr/31.webp)


120,000 Sats의 첫 지급금을 받았습니다.


![ALBY HUB](assets/fr/32.webp)


"*Wallet*" 탭으로 돌아가면 Wallet 잔액을 확인할 수 있습니다. 첫 결제 시 Alby Hub는 자동으로 354 Sats을 적립합니다. 이후 개설하는 각 Lightning 채널에 대해 Alby Hub는 채널 용량의 1%에 해당하는 예비금을 자동으로 적립합니다. 이 준비금은 피어가 사기를 시도하는 경우 노드가 채널의 자금을 회수할 수 있도록 하는 보안 조치입니다. 그렇기 때문에 120,000 Sats을 송금했지만 잔액에 119,646 Sats만 표시되는 것입니다.


![ALBY HUB](assets/fr/33.webp)


## 체인에 비트코인 입금하기


결제를 위해 현금을 송금하고 싶다면 직접 채널을 개설할 수도 있습니다. 이렇게 하려면 Wallet에 온체인 비트코인이 필요합니다.


"*노드*" 탭에서 "*예치금*"을 클릭합니다.


![ALBY HUB](assets/fr/34.webp)


표시된 Address으로 비트코인을 전송합니다. 이 Address은 이전에 저장한 복구 문구에서 파생된 것입니다.


![ALBY HUB](assets/fr/35.webp)


72,000 Sats을 보냈습니다. 이제 라이트닝이 아닌 "*저축 잔액*"에 표시되며, 여기에는 제가 보유한 모든 자금이 포함됩니다.


![ALBY HUB](assets/fr/36.webp)


## 라이트닝 채널 열기


이제 온체인 자금을 확보했으니 새로운 라이트닝 채널을 개설할 수 있습니다. 항상 제약 없이 결제할 수 있도록 충분한 금액으로 여러 개의 채널을 개설하는 것이 좋습니다. 대부분의 LSP(*라이트닝 서비스 공급자*)는 채널을 개설하려면 최소 150,000 Sats가 필요합니다.


"*노드*" 탭에서 "*채널 열기*"를 클릭합니다.


![ALBY HUB](assets/fr/37.webp)


채널의 크기를 선택합니다. 너무 작은 채널은 열지 않는 것이 좋으며, 라이트닝 노드이고 키를 호스팅하는 컴퓨터가 Hardware Wallet과 같은 수준의 보안을 제공하지 않는다는 점을 염두에 두세요. 따라서 차단할 양을 신중하게 선택해야 합니다.


![ALBY HUB](assets/fr/38.webp)


"*고급 옵션*" 메뉴에서 채널을 열 LSP를 선택하거나 다른 라이트닝 노드를 수동으로 입력할 수 있습니다.


![ALBY HUB](assets/fr/39.webp)


그런 다음 "*채널 열기*"를 클릭합니다.


![ALBY HUB](assets/fr/40.webp)


채널이 온체인으로 확인될 때까지 기다리세요.


![ALBY HUB](assets/fr/41.webp)


이제 새 채널이 '*노드*' 탭에 표시됩니다.


![ALBY HUB](assets/fr/42.webp)


## 노드 관리


라이트닝 채널 관리는 생각보다 쉽습니다. Alby Hub를 사용하면 지출 잔액과 On-Chain 잔액 간에 Sats를 이체할 수 있습니다. 이를 통해 지출 또는 수신 용량을 늘릴 수 있습니다.


![ALBY HUB](assets/fr/66.webp)


## 경비 신청서 연결


이제 작동하는 라이트닝 노드가 생겼으니, 이 노드를 사용해 매일 Sats을 받고 사용할 수 있습니다. Alby Hub의 웹 Interface은 노드를 관리하는 데는 편리하지만, 이동 중에 빠르게 트랜잭션을 처리하는 데는 적합하지 않습니다. 이를 위해 스마트폰에 설치된 라이트닝 Wallet 앱을 사용하겠습니다.


이 튜토리얼에서는 사용하기 매우 쉬운 Alby Go를 선택하는 것이 좋지만 Zeus와 같은 다른 호환 가능한 애플리케이션을 사용할 수도 있습니다.


![ALBY HUB](assets/fr/43.webp)


Alby Go를 설치하려면 디바이스의 애플리케이션 스토어로 이동합니다:




- [Android용](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple용](https://apps.apple.com/us/app/alby-go/id6471335774).


![ALBY HUB](assets/fr/44.webp)


안드로이드 사용자는 '.apk' 파일[Alby의 GitHub에서 다운로드 가능](https://github.com/getAlby/go/releases)을 통해 앱을 설치할 수도 있습니다.


![ALBY HUB](assets/fr/45.webp)


애플리케이션이 실행되면 "*Wallet 연결*"을 클릭합니다.


![ALBY HUB](assets/fr/46.webp)


Alby Hub의 App Store에서 "Alby Go"를 찾아 "연결"을 클릭합니다

![ALBY HUB](assets/fr/47.webp)

"원탭 연결로 연결"을 클릭합니다. 이렇게 하면 클릭 한 번으로 Alby Hub를 Alby Go를 사용하는 다른 앱에 연결할 수 있습니다.


![ALBY HUB](assets/fr/48.webp)


그러면 Alby Hub가 Alby Go에 대한 연결을 설정하기 위해 비밀을 generate으로 설정합니다.


![ALBY HUB](assets/fr/49.webp)


Alby Go 애플리케이션으로 돌아가서 QR 코드를 스캔하거나 비밀번호를 붙여넣습니다.


![ALBY HUB](assets/fr/50.webp)


"마침"을 클릭합니다.


![ALBY HUB](assets/fr/51.webp)


이제 스마트폰에서 라이트닝 노드로 구동되는 Alby Hub에 원격으로 액세스할 수 있으므로 매일 이동 중에도 Sats을 쉽게 보내고 받을 수 있습니다.


![ALBY HUB](assets/fr/52.webp)


필요한 경우 이 연결을 클릭하여 Alby Hub에서 직접 이 연결에 대한 권한을 관리할 수 있습니다.


![ALBY HUB](assets/fr/53.webp)


Sats를 받으려면 "*받기*"를 클릭하기만 하면 됩니다.


![ALBY HUB](assets/fr/54.webp)


"*Invoice*"을 클릭하여 Invoice 금액과 설명을 수정합니다.


![ALBY HUB](assets/fr/55.webp)


Invoice를 충전하여 Sats를 수신합니다.


![ALBY HUB](assets/fr/56.webp)


Sats을 보내려면 "*보내기*"를 클릭합니다.


![ALBY HUB](assets/fr/57.webp)


결제하려는 Invoice을 스캔합니다.


![ALBY HUB](assets/fr/58.webp)


그런 다음 "*결제*"를 클릭합니다.


![ALBY HUB](assets/fr/59.webp)


거래가 확정되었습니다.


![ALBY HUB](assets/fr/60.webp)


작은 화살표를 클릭하면 거래 내역에 액세스할 수 있습니다.


![ALBY HUB](assets/fr/61.webp)


이러한 거래는 Alby Hub에서도 볼 수 있습니다.


![ALBY HUB](assets/fr/62.webp)


## Lightning Address 사용자 지정


Alby는 라이트닝 Address 옵션을 제공합니다. 이 옵션을 사용하면 매번 수동으로 generate 또는 Invoice을 설정할 필요 없이 노드에서 결제를 받을 수 있습니다. 기본적으로 Alby는 Lightning Address을 할당하지만 사용자 지정할 수 있습니다. Alby 온라인 계정에 로그인하고 오른쪽 상단의 이름을 클릭한 다음 "*설정*"을 선택합니다.


![ALBY HUB](assets/fr/63.webp)


"*라이트닝 Address*" 메뉴로 이동합니다.


![ALBY HUB](assets/fr/64.webp)


Address을 수정한 다음 "*라이트닝 Address 업데이트*"를 클릭하여 확인합니다.


![ALBY HUB](assets/fr/65.webp)


Address가 변경되면 더 이상 내 소유가 아니라는 점에 유의하세요. 따라서 다시는 Sats를 보내지 마세요.


이제 알비 허브 도구를 사용하여 자체 노드에서 라이트닝을 사용하는 방법을 배웠습니다. 이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 올려주시면 정말 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


이 튜토리얼에서 조작 한 모든 번개 메커니즘을 자세히 이해하려면 주제에 대한 무료 교육 을 찾아 보는 것이 좋습니다:


https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb