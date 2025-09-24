---
name: GrapheneOS

description: 안드로이드 기반의 보안 및 개인 정보 보호에 중점을 둔 모바일 운영 체제
---

![cover](assets/cover.webp)

> [그래핀OS](https://grapheneos.org/)는 안드로이드 애플리케이션과 완벽하게 호환되면서도 높은 수준의 개인정보 보호 및 보안을 제공하도록 설계된 비영리 오픈소스 모바일 운영체제입니다.

2014년에 'CopperheadOS'라는 이름으로 설립된 GrapheneOS는 기존 안드로이드 코드(AOSP)를 기반으로 하지만, 사용자 개인정보 보호 및 보안을 개선하기 위해 많은 변경과 개선이 이루어졌습니다. 그래핀OS는 거대 기술 회사가 아닌 사용자가 자신의 휴대폰을 제어할 수 있도록 합니다.


![video](https://youtu.be/VnumtalYLFI)


### Sommaire:



- 소개
- 준비
- 설치
- 앱 대안
- 단점
- 유용한 정보


*이 튜토리얼은 [MIT 라이선스 하에 Bitcoiner.Guide의 BitcoinQnA](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md)에 게시된 원본 콘텐츠를 각색한 것으로, 최초 작성에 대한 모든 저작권은 해당 게시자에게 있습니다*


## 왜 그래핀OS를 사용하나요?


최신 휴대폰은 500~1000달러에 달하는 추적 및 데이터 수집 장치입니다. 우리 삶의 모든 측면이 휴대폰을 통해 이루어지며, 안타깝게도 이러한 데이터의 대부분은 어떤 형태로든 제3자와 공유됩니다.

그래핀OS는 이러한 데이터 공유를 줄이고 잠재적인 공격 벡터로부터 디바이스 보안을 강화하기 위해 특별히 설계되었습니다. GrapheneOS 계정 같은 것은 없습니다. 앱을 다운로드하거나 OS와 상호 작용하기 위해 계정이 필요하지 않습니다. 간단히 말해, 사용자는 제품이 아닙니다.


그래핀OS는 몇 가지 간단한 핵심 원칙을 통해 안드로이드 환경에 추가적인 보안을 제공합니다.


1. **공격 표면 감소** - 불필요한 코드(또는 블로트웨어)를 제거합니다.

2. **취약점 노출 방지** - 사용자가 원하는 수준의 보안을 선택할 수 있도록 세분화합니다.

3. **샌드박스 봉쇄** - GrapheneOS는 기존 안드로이드 샌드박스를 강화하여 각 앱이 휴대폰의 나머지 부분과 통신하는 기능을 더욱 제한합니다.


그래핀OS 기능 세트의 기술적 세부 사항에 대한 자세한 내용은 [여기](https://grapheneos.org/features)에서 확인하세요.


### 쉽게 전환하기


수년간 구글이나 애플 생태계에 익숙해졌다면 하루아침에 그 편리함을 모두 잃는다는 생각은 두려운 일일 수 있습니다. 하지만 앱 설치를 신중하게 결정하면(나중에 다룸) 예상되는 어려움을 상당 부분 줄이거나 없앨 수 있습니다.


대안이 점점 좋아지고 있지만, 이러한 변화에 대한 생각은 여전히 불편할 수 있습니다. 이런 상황에 처했다면, 한동안 기존 휴대폰과 함께 새 GrapheneOS 기기를 함께 사용하는 것이 가장 좋습니다. 그 후 일주일에 2~3개의 앱만 사용하다가 GrapheneOS 기기만 사용하게 될 때까지 천천히 앱을 줄여나가면 됩니다.


이 접근 방식을 취하는 경우, 스스로에게 엄격하고 감시되는 대안에 대한 의존을 최대한 빨리 끊어야 합니다. 인간은 게으르고 저항이 가장 적은 길을 택하는 경우가 많습니다. 애초에 전환을 결정한 이유를 기억하세요.


**개인 데이터로 결제하는 대신 시간으로 결제하는 것을 선택했으며, 때로는 (설치하는 대체 앱에 따라) Hard 적립금을 사용하기도 합니다**


## 시작하기


그래핀OS는 현재 _(다소 아이러니하게도)_ [구글 픽셀](https://grapheneos.org/faq#supported-devices) 제품군에서만 생산되고 있습니다. 하지만 그럴 만한 이유가 있는 것은 아닙니다. 픽셀은 OS를 강화하기 위해 수행한 작업을 보완하기 위해 최고의 하드웨어 기반 보안을 제공합니다. 여기에는 특정 구성 요소 격리 및 확인된 부팅과 같은 것이 포함됩니다.


### 디바이스 선택


GrapheneOS를 설치할 Pixel을 선택할 때 기기가 기본 [보안 업데이트](https://support.google.com/pixelphone/answer/4457705?hl=en#zippy=%2Cpixel-xl-a-a-g-a-g)를 계속 받을 수 있는 기간을 확인해야 합니다.


이 글을 쓰는 시점에 Pixel 6a는 2027년 7월까지 장기 지원이 보장되는 가장 저렴한 모델입니다. 이 모델을 선택하는 경우, 출고 시 기본 제공된 OS 버전에서는 OEM 잠금 해제가 작동하지 않습니다. 무선 업데이트를 통해 2022년 6월 이후 릴리스 버전으로 업데이트해야 합니다. 업데이트한 후에는 OEM 잠금 해제를 수정하기 위해 디바이스를 초기화해야 합니다. 통신사 잠금 해제된 다른 모든 모델은 즉시 GrapheneOS를 사용할 수 있습니다.


디바이스를 선택할 때는 잠금 해제된 버전을 구매해야 합니다. Verizon과 같은 특정 이동통신사에서는 부트로더가 잠긴 상태로 디바이스를 배송하여 다음 프로세스를 완전히 차단합니다.


### GrapheneOS 설치


웹 설치 프로그램](https://grapheneos.org/install/web)을 사용하면 누구나 10분 이내에 전체 과정을 쉽게 완료할 수 있습니다.

다음 지침은 위 링크에서 발췌한 내용을 축소한 것입니다.


손만 내밀면 됩니다:



- 픽셀
- 휴대폰에서 컴퓨터로 연결하기 위한 USB 케이블
- 웹 브라우저를 실행할 컴퓨터(크롬 기반 브라우저: 크롬, 엣지, 브레이브 등)


자세히 알아보겠습니다:


1. 첫 번째 단계는 **설정** > **휴대폰 정보**로 이동하여 **'개발자 모드'**가 활성화될 때까지 빌드 번호를 반복해서 탭하는 것입니다.

2. 다음으로 **설정** > **시스템** > **개발자 옵션**으로 이동하여 **'OEM 잠금 해제'**를 활성화합니다.

3. 이제 기기를 재부팅하고 휴대폰이 다시 켜지는 동안 볼륨 작게 버튼을 길게 누릅니다.

4. 휴대폰을 노트북에 연결하고 인증을 요청하는 메시지가 표시되면 연결을 허용합니다.

5. 웹 인스톨러 페이지에서 '부트로더 잠금 해제'를 클릭합니다.

6. 그러면 휴대폰 옵션이 변경되는 것을 볼 수 있습니다. 볼륨 버튼을 사용하여 선택 항목을 '잠금 해제'로 변경하고 전원 버튼을 사용하여 수락합니다.

7. 다음으로 웹 설치 관리자 페이지에서 릴리스 다운로드를 클릭합니다.

8. 다운로드가 완료되면 다음 단계로 이동하여 '플래시 릴리스'를 클릭합니다. 이 과정은 1~2분 정도 소요되며 휴대폰을 전혀 만질 필요가 없습니다.

9. 마지막으로 웹 인스톨러의 다음 단계로 이동하여 **부트로더 잠금**을 클릭합니다. 선택 항목을 변경하고 앞서와 같은 방법으로 전원 버튼으로 확인해야 합니다.

10. '시작'이라는 단어가 표시되면 전원 버튼으로 이를 확인하면 기기가 새로운 Google 프리 운영 체제로 부팅됩니다.


![image](assets/fr/2.webp)

그래핀OS 시작 화면



초기 부팅 및 설정 후에는 설정 > 시스템 > 개발자 옵션에서 OEM 잠금 해제를 비활성화하는 것이 좋습니다


선택 사항이지만 권장되는 추가 단계인 Auditor 앱을 통한 설치 확인을 수행할 수도 있습니다. 이 단계를 완료하려면 앱이 설치된 별도의 Android 휴대폰이 필요합니다. 이에 대한 지침은 [여기](https://attestation.app/tutorial)._에서 확인할 수 있습니다



![video](https://www.youtube.com/embed/L1KZWjZVnAw)

위에서 설명한 간단한 단계를 자세히 설명하는 동영상



이러한 간단한 단계가 너무 어렵게 느껴진다면 GrapheneOS 소프트웨어가 [사전 설치된](https://ronindojo.io/en/roninmobile) Pixel을 구입하는 것도 고려해 볼 수 있습니다. 단, 공급업체에 약간의 신뢰가 필요하다는 점에 유의하세요.


### 사전 설치된 앱


이제 설정이 완료되었으므로 처음 설치할 때 GrapheneOS가 어떻게 나타나는지 알 수 있습니다. 기본적으로 다음 앱이 설치되어 있습니다:


![image](assets/fr/3.webp)


기본 앱


익숙하지 않을 수 있는 두 가지는 '감사'와 '바나듐'입니다.



- Auditor 앱](https://play.google.com/store/apps/details?id=app.attestation.auditor)은 하드웨어 기반 보안 기능을 사용하여 운영 체제의 진위 여부 및 무결성과 함께 기기의 신원을 확인합니다. 이 앱은 디바이스가 부트 로더가 잠긴 상태에서 기본 운영 체제를 실행하고 있는지, 운영 체제에 변조가 발생하지 않았는지 확인합니다.
- [바나듐](https://github.com/GrapheneOS/Vanadium)은 개인 정보 보호 및 보안이 강화된 크롬 웹 브라우저의 변형 버전입니다.


## 사용자 지정


휴대폰 설정은 개인적인 취향에 따라 달라질 수 있지만, 집과 같은 편안함을 느끼기 위해 GrapheneOS를 설치할 때 가장 먼저 변경하는 항목은 다음과 같습니다.


### 배경화면 설정 및 테마 업데이트하기


설정 > 배경화면 및 스타일로 이동합니다. 여기에서:



- 웹에서 다운로드한 이미지의 홈 및 잠금 화면 배경을 업데이트하세요.
- UI 전체에 사용되는 강조 색상을 선택합니다.
- 어두운 테마를 활성화합니다.


### 배터리 비율 표시


설정** > **배터리**로 이동한 다음 상태 표시줄에서 **배터리 비율 표시**를 활성화합니다.


### 연락처 가져오기


**다른 Android 휴대폰에서** - 연락처 앱으로 이동하여 VCF로 내보내기 옵션을 찾습니다.


**iOS에서** - 연락처 내보내기와 같은 앱을 사용하고 'vCard' 내보내기 옵션을 사용하여 VCF 파일을 내보냅니다.

VCF 파일이 있으면 microSD 카드나 USB 드라이브와 같은 외부 저장소 옵션을 사용하여 GrapheneOS 디바이스로 전송할 수 있습니다. 이러한 저장 장치가 없는 경우 아래 나열된 여러 앱 중 하나를 통해 공유할 수 있습니다.


![image](assets/fr/4.webp)


개인화된 홈 화면



## 대체 앱


휴대폰을 유용하게 사용하려면 몇 가지 애플리케이션을 설치해야 합니다! 다음 옵션은 제가 개인적으로 사용했거나 광범위한 개인 정보 보호 커뮤니티에서 강력한 추천을 받았기 때문에 포함되었습니다. 여기에 언급되지 않은 다른 훌륭한 대안도 많이 있으며, [Awesome Privacy](https://awesome-privacy.xyz)에서는 모든 유형의 디바이스를 위한 매우 광범위한 개인 정보 보호 애플리케이션 목록을 제공합니다.


앱이 무료 오픈 소스 소프트웨어(FOSS)라고 해서 잠재적인 개인정보 유출로부터 자유롭다는 의미는 아닙니다. 엑소더스](https://reports.exodus-privacy.eu.org/en/)를 사용하여 선호하는 앱의 개인정보 감사 결과를 확인하세요.


### F-Droid


[F-Droid](https://f-droid.org/)는 안드로이드용 FOSS 애플리케이션의 설치 가능한 카탈로그입니다. 이 클라이언트를 사용하면 기기에서 애플리케이션을 쉽게 검색, 설치 및 업데이트할 수 있습니다. F-Droid를 통한 업데이트는 다른 앱 스토어보다 속도가 느릴 수 있다는 점을 언급할 필요가 있습니다. 이는 주로 앱이 기본 F-Droid 저장소를 통해 검색되는지 아니면 사용자 지정 저장소를 통해 검색되는지에 따라 달라집니다.


F-Droid를 설치하려면 휴대폰의 브라우저를 통해 해당 웹사이트로 이동한 후 다운로드를 탭하세요. 그러면 '.apk' 파일이 다운로드됩니다. 그러면 앱을 설치할 것인지 묻는 메시지가 표시됩니다.


F-Droid의 기본 저장소에 있는 애플리케이션뿐만 아니라, 많은 오픈 소스 프로젝트는 F-Droid 앱 설정에서 추가할 수 있는 자체 저장소를 호스팅하기도 합니다. 이 경우 해당 프로젝트는 웹사이트에서 이를 수행하는 데 필요한 매우 간단한 단계를 안내합니다.


![image](assets/fr/5.webp)


F-Droid 홈 화면


https://planb.network/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

### 오로라 스토어


[오로라 스토어](https://auroraoss.com/)는 구글 플레이스토어의 FOSS 버전입니다. Aurora는 기존 Play 스토어와 모양과 느낌이 매우 유사하며, 일반적으로 Google 옵션을 통해 찾을 수 있는 모든 앱을 다운로드하고 업데이트할 수 있습니다.


Aurora의 킬러 기능은 익명 로그인입니다. 즉, 구글 계정에 로그인하지 않고도 F-Droid 또는 직접 APK를 통해 사용할 수 없는 좋아하는 앱을 다운로드할 수 있습니다.


서둘러 기본 설치 옵션으로 설정하기 전에, 저희가 제거하려는 많은 애플리케이션이 Play 스토어에서 설치되었다는 점을 기억하세요. Aurora에서 액세스할 수 있다고 해서 일부 앱에 추적 기능이 내장되어 있다는 사실은 변하지 않습니다. 항상 가능한 것은 아니지만, 가능하면 Aurora를 통해 다운로드하기 전에 F-Droid를 대체할 수 있는 앱을 찾아보세요.


Aurora를 설치하려면 F-Droid에서 'Aurora Store'를 검색하면 됩니다.


또한 "익명 계정"은 실제로 Aurora에서 생성하고 제어하기 때문에 잠재적인 공격 벡터가 있습니다. 이론상으로는 악성 업데이트를 제공하거나 휴대폰에 앱을 푸시할 수 있지만, 기기에서 설치 메시지가 표시되면 사용자가 이를 수락해야 합니다. 또한 Aurora는 지역 및 디바이스 오판독으로 인해 앱이 표시되지 않는 문제가 가끔 발생합니다. 이 문제는 일반적으로 아래 단계를 통해 해결할 수 있습니다.


**최고 팁** - 가끔 오로라 스토어에서 속도 제한이 발생하여 앱을 검색하고 설치하는 기능이 제한될 수 있습니다. 이 문제를 해결하려면 **설정** > **앱** > **오로라** > **기본값으로 열기**로 이동한 다음 `play.google.com` 도메인을 추가하세요. 이제 'Play 스토어를 통해 다운로드' 링크가 있는 제품이나 서비스의 웹사이트로 이동할 때마다 해당 링크를 탭하면 해당 앱이 Aurora 내에서 열리므로 다운로드할 수 있습니다.



![image](assets/fr/6.webp)


오로라 스토어 홈 화면


https://planb.network/tutorials/computer-security/data/aurora-store-b3345da7-1ed1-407e-a9ae-a1c7f0ba9967

### APK 다운로드


Android의 앱은 '.apk' 파일을 통해 다운로드하여 설치할 수도 있습니다. 이는 타사 앱 스토어가 필요 없는 훌륭한 대안으로, 프로젝트 또는 서비스의 웹사이트나 GitHub 저장소에서 직접 파일을 다운로드하기만 하면 됩니다.


이 방법의 단점은 자동 업데이트가 제공되지 않기 때문에 새로운 릴리스에 대한 정보를 얻으려면 해당 서비스의 커뮤니케이션 채널을 모니터링해야 한다는 것입니다. 하지만 이 문제를 해결하고자 하는 Obtanium이라는 훌륭한 프로젝트가 있습니다. [Obtainium](https://github.com/ImranR98/Obtainium)을 사용하면 오픈 소스 앱의 릴리스 페이지에서 직접 설치 및 업데이트하고 새 릴리스가 제공되면 알림을 받을 수 있습니다.


![image](assets/fr/7.webp)


오타니움 미리보기


### 웹 앱


서비스를 자주 사용하지 않고 네이티브 애플리케이션을 다운로드하고 싶지 않을 때는 웹 버전으로 간편하게 액세스할 수 있습니다. 요즘에는 많은 웹사이트가 프로그레시브 웹 앱(PWA)을 지원합니다. 여기에서 특정 웹사이트(예: 트위터닷컴)를 휴대폰 홈 화면에 북마크할 수 있습니다. 그런 다음 아이콘을 탭하면 일반적인 브라우저 환경에서 발생하는 일반적인 방해 요소 없이 전체 화면 애플리케이션으로 열립니다. 아래에서 그 예시를 확인할 수 있습니다.


그래핀OS의 기본 브라우저인 바나디움에서 이 기능을 사용하려면 원하는 웹사이트로 이동하여 화면 오른쪽 상단에 있는 세로점 3개를 탭한 다음 **'홈 화면에 추가'**를 탭하면 됩니다.


이 방법의 유일한 단점은 북마크된 웹 페이지일 뿐이므로 어떤 형태의 알림도 받지 못한다는 점입니다. 하지만 이 점을 긍정적으로 보는 분들도 있습니다!


![image](assets/fr/8.webp)


트위터 PWA


### 웹 브라우저


사전 패키지 옵션인 바나듐을 사용하면 정말 나쁠 것이 없습니다. 이 앱은 제가 사용해 본 다른 모바일 브라우저와 동일하게 작동하며 호환성 문제가 단 한 번도 발생하지 않았습니다.


토르 네이티브 '.onion' 사이트에 액세스해야 하는 경우, 해당 [웹사이트](https://www.torproject.org/download/#android) 또는 F-Droid를 통해 토르 브라우저 APK를 직접 다운로드할 수 있습니다.


### VPN


스누핑하는 인터넷 서비스 제공업체(ISP)로부터 온라인 활동을 보호하려면 가상 사설망(VPN) 앱을 사용하는 것이 좋습니다. VPN은 인터넷 트래픽을 암호화된 터널을 통해 VPN 서비스 제공업체가 관리하는 공유 IP Address로 전송하여 사용자의 디바이스 활동이 사용자와 연결되지 않도록 합니다.


다음은 개인 정보를 제공하지 않고도 Bitcoin에서 서비스 비용을 결제할 수 있는 두 가지 공인 옵션입니다. 두 가지 모두 F-Droid에서 사용할 수 있습니다.


https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68

https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8


### 메시징


최근 몇 년 동안 암호화된 메시징 솔루션이 많이 출시되었습니다. 하지만 문제는 여전히 남아 있습니다. 휴대폰에 최고의 비공개 옵션을 설치할 수 있지만 이를 사용하는 연락처가 없다면 무슨 소용이 있을까요?


개인 정보 보호 공간에 관심이 없는 대부분의 사람들은 WhatsApp 또는 iMessage를 사용하고 있을 가능성이 높습니다. 전자는 Aurora Store를 통해 다운로드할 수 있지만 후자는 GrapheneOS에서 작동하지 않습니다(당연하죠!).



- [Signal](https://signal.org/)은 강력한 실적과 다양한 기능을 갖춘 가장 인기 있는 종단간 암호화(E2EE) 메신저 중 하나입니다. Signal은 가입 시 전화번호가 필요하므로 전화번호를 모르는 사람과 채팅할 계획이라면 다른 대안을 살펴보는 것도 좋습니다. Signal은 Aurora Store를 통해 다운로드해야 합니다.
- [심플렉스](https://f-droid.org/en/packages/chat.simplex.app/)는 상당히 새로운 E2EE 메신저입니다. 사용자 ID가 없고 전화번호나 개인 정보가 필요하지 않습니다. 사람들은 개인 QR 코드를 스캔하거나 고유 링크를 방문하여 사용자를 찾습니다. 또한 심플렉스는 고급 사용자가 자체 서버를 운영할 수 있어 중앙 집중식 기관에 대한 의존도를 더욱 낮출 수 있습니다. Simplex에는 데스크톱 클라이언트가 없으므로 멀티 디바이스가 우선순위 목록에 있는 경우 적합하지 않을 수 있습니다. Android용 Simplex는 F-Droid를 통해 사용할 수 있습니다.
- [Threema](https://threema.ch/en/faq/libre_installation)는 Simplex와 비슷한 경험을 제공하지만, 더 오래 사용되어 왔기 때문에 조금 더 세련된 느낌을 줍니다. Threema는 무료가 아니며 평생 라이선스는 $4.99이며 Bitcoin로 구입할 수 있습니다. Threema는 웹 클라이언트와 기본 데스크톱 애플리케이션을 제공합니다. Android 애플리케이션은 F-Droid를 통해 사용할 수 있습니다.
- [텔레그램 FOSS](https://f-droid.org/en/packages/org.telegram.messenger/)는 안드로이드용 공식 텔레그램 앱의 비공식 FOSS Fork입니다. 텔레그램에는 E2EE '비밀대화'가 있지만, 기본 옵션은 비공개가 아닙니다. 텔레그램 FOSS는 F-Droid에서 다운로드 받을 수 있습니다.


![image](assets/fr/9.webp)

왼쪽: 쓰리마, 오른쪽: Simplex


https://planb.network/tutorials/computer-security/communication/signal-8dfb5572-6962-4f1c-bfa5-3192da4e9a4e

https://planb.network/tutorials/computer-security/communication/telegram-09ab3cf3-7625-4267-97a1-24e59a9e5943

https://planb.network/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3

https://planb.network/tutorials/computer-security/communication/simplex-chat-7a1efa11-4d0a-49c4-92aa-e18bf22c22b9

https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74

### 미디어



- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/)는 프리미엄 계정이 필요 없는 크로스 플랫폼 Spotify 클라이언트입니다. Spotube는 F-Droid를 통해 사용할 수 있습니다.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/)은 YouTube 음악에서 모든 음악을 무료로 스트리밍할 수 있는 환상적인 애플리케이션입니다. ViMusic은 F-Droid에서 구입할 수 있습니다.
- [뉴파이프](https://f-droid.org/packages/org.schabi.newpipe/)는 성가신 광고와 의심스러운 권한 없이 YouTube를 시청할 수 있는 환경을 제공합니다. 뉴파이프를 사용하면 채널을 구독하고, 백그라운드에서 듣고, 다운로드하여 오프라인으로 시청할 수도 있습니다. 뉴파이프는 F-Droid를 통해 액세스할 수 있습니다.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/)는 좋아하는 모든 프로그램을 구독하고 관리할 수 있는 팟캐스트 플레이어입니다. AntennaPod는 F-Droid를 통해 이용할 수 있습니다.


![image](assets/fr/11.webp)

왼쪽: 스포튜브, 오른쪽: ViMusic


### 지도


운전 중 음성 지원을 원하고 GrapheneOS에서 지도 앱을 사용하려면 [RHVoice](https://rhvoice.org/installation/)를 설치하고 [구성](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available)을 해야 합니다.



- [매직 어스](https://www.magicearth.com/)는 턴바이턴 내비게이션, 3D 및 오프라인 지도를 지원하는 지도 대체 앱입니다. 매직 어스는 오로라 스토어에서 다운로드할 수 있습니다.
- [오가닉 맵](https://f-droid.org/en/packages/app.organicmaps/)은 크라우드 소스 오픈스트리트맵 데이터를 기반으로 한 여행자, 관광객, 등산객, 자전거 이용자를 위한 지도 대안입니다. 개인 정보 보호에 중점을 둔 Maps.me 앱(이전에는 MapsWithMe로 알려짐)의 오픈 소스 Fork입니다. 인터넷 연결 없이도 모든 기능을 100% 지원하며 F-Droid에서 다운로드할 수 있습니다.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/)는 위에서 언급한 모든 기능을 지원하는 또 다른 훌륭한 지도 대안입니다.


![image](assets/fr/13.webp)

왼쪽: 매직어스, 오른쪽: 오가닉 맵


### 이메일



- [Proton Mail](https://proton.me/mail)은 감사된 E2EE를 지원하는 무료 비공개 이메일 서비스를 제공합니다. Proton은 사용자 지정 도메인과 [별칭](https://proton.me/support/creating-aliases)을 지원하는 유료 버전도 제공합니다. Proton Mail은 직접 APK로 다운로드하거나 Aurora를 통해 다운로드할 수 있습니다.
- [투타노타](https://tutanota.com/)는 유료 서비스 옵션을 포함하여 프로톤 메일과 동일한 기능을 제공하며, 직접 APK로 다운로드하거나 F-Droid를 통해 다운로드할 수 있습니다.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/)은 기본적으로 모든 이메일 제공업체에서 작동하는 오픈 소스 이메일 클라이언트입니다. 여러 계정, 통합 받은 편지함, OpenPGP 암호화 표준을 지원합니다.


![image](assets/fr/15.webp)

왼쪽: 양성자 메일, 오른쪽: 투타노타


### 생산성



- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/)은 파일 동기화 프로그램입니다. 두 대 이상의 기기 간에 파일을 실시간으로 동기화하며, 외부의 시선으로부터 안전하게 보호합니다. 내 데이터는 내 데이터이므로 저장 위치, 제3자와의 공유 여부, 인터넷을 통한 전송 방법을 선택할 권리가 있습니다. 동기화는 F-Droid를 통해 사용할 수 있습니다.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/)를 사용하면 홈 네트워크에 연결된 모든 기기가 서로 쉽게 대화할 수 있습니다. 모든 장치에서 파일, 사진, 클립보드 데이터를 쉽게 전송할 수 있습니다(iOS에서도!). KDE Connect는 F-Droid에서 다운로드할 수 있습니다.
- [노트북](https://f-droid.org/en/packages/com.streetwriters.notesnook/)은 모든 장치에서 생각과 할 일 목록을 동기화할 수 있는 E2EE 노트 애플리케이션입니다. 무료 요금제로 대부분의 개인 사용 사례를 커버할 수 있습니다. Notesnook은 F-Droid에서 사용할 수 있습니다.
- [표준 노트](https://f-droid.org/en/packages/com.standardnotes/)는 노트북과 매우 유사하지만 기능 세트에 맞는 유료 요금제를 사용해야 합니다. 스탠다드 노트는 F-Droid를 통해 이용할 수 있습니다.
- [애니소프트 키보드](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/)는 휴대폰 타이핑 환경과 관련하여 생각할 수 있는 거의 모든 것을 사용자 지정할 수 있는 키보드 앱입니다. F-Droid를 통해 다운로드할 수 있습니다.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US)는 기본 Google 키보드 앱입니다. 제 경험상 이 앱은 최고의 타이핑 및 스와이프 경험을 제공합니다. 이 앱을 다운로드하는 경우 모든 네트워크 관련 권한을 완전히 비활성화해야 합니다. Aurora를 통해 다운로드할 수 있습니다.


![image](assets/fr/17.webp)

왼쪽: 노트북, 오른쪽: KDE Connect


### 라이프스타일



- [기하학적 날씨](https://f-droid.org/en/packages/wangdaye.com.geometricweather/)는 아름답게 디자인된 오픈 소스 날씨 앱으로, F-Droid를 통해 이용할 수 있습니다. 또한 다양한 크기의 위젯을 지원하므로 홈 화면에서 바로 선택한 위치의 날씨를 확인할 수 있습니다.
- [번역해줘](https://f-droid.org/packages/com.bnyro.translate/)는 200개 이상의 언어를 지원하는 오픈 소스 및 개인정보 보호 번역 앱입니다. 번역해줘는 F-Droid를 통해 사용할 수 있습니다.
- [프로톤 캘린더](https://proton.me/calendar/download)는 사용이 간편한 E2EE로, 프로톤 이메일 계정과 원활하게 연동됩니다. 프로톤 캘린더는 APK로 다운로드하거나 Aurora 스토어를 통해 다운로드할 수 있습니다.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/)는 탑승권, 쿠폰, 영화 티켓, 멤버십 카드 등을 표시하고 저장할 수 있는 앱입니다. 관련 `pkpass` 또는 `espass` 파일을 다운로드하고 앱으로 열기만 하면 됩니다. 패스안드로이드는 F-Droid를 통해 이용할 수 있습니다.


![image](assets/fr/19.webp)

왼쪽: 기하학적 날씨, 오른쪽: 양성자 달력


### 보안/개인 정보 보호



- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/)은 모든 디바이스에서 사용할 수 있는 무료 E2EE 크로스 플랫폼 비밀번호 관리자 솔루션을 제공합니다. 유료 서비스를 이용하면 앱에 2FA 코드를 통합할 수 있습니다. Bitwarden의 서버 쪽은 자체 호스팅이 가능하며 안드로이드 앱은 F-Droid를 통해 사용할 수 있습니다.
- [프로톤 패스](https://proton.me/pass/download)는 비트워든과 유사한 무료 서비스를 제공하지만, [프로톤 무제한](https://proton.me/pricing) 고객은 추가적인 고급 기능을 이용할 수 있습니다. 프로톤 패스는 APK 또는 Aurora를 통해 이용할 수 있습니다.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/)는 일회용 비밀번호 프로토콜을 사용하는 시스템을 위한 2단계 인증 애플리케이션입니다. QR 코드를 스캔하여 토큰을 쉽게 추가할 수 있습니다. FreeOTP는 F-Droid를 통해 사용할 수 있습니다.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/)는 온라인 서비스를 위한 2단계 인증 토큰을 관리할 수 있는 안전한 무료 안드로이드용 오픈 소스 앱입니다. Aegis는 F-Droid를 통해 사용할 수 있습니다.
- [크립토메이터](https://f-droid.org/en/packages/org.cryptomator.lite/)는 데이터를 로컬에서 암호화하여 선호하는 클라우드 서비스에 안전하게 업로드할 수 있는 유료 크로스 플랫폼 서비스입니다. 크립토메이터는 F-Droid를 통해 다운로드할 수 있습니다.


![image](assets/fr/21.webp)

왼쪽: 프로톤 패스,

맞아요: 비트워든


https://planb.network/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

https://planb.network/tutorials/computer-security/data/cryptomator-84e52c76-2253-49fe-81da-e05e90c28d0d

### 클라우드 솔루션



- [프로톤 드라이브](https://proton.me/drive/download)는 모든 파일을 백업하고 저장할 수 있는 유료 E2EE 클라우드 솔루션입니다. 이 글을 쓰는 시점에 Windows 데스크톱 클라이언트를 발표했지만, Mac과 Linux 사용자는 컴퓨터에서 동기화하려면 (현재로서는) 웹 버전을 계속 사용해야 합니다. Android 클라이언트는 APK 또는 Aurora를 통해 사용할 수 있습니다.
- [Skiff](https://skiff.com/download)는 유료 E2EE 클라우드 스토리지 및 파일 협업 도구도 제공합니다. Mac 및 Windows 데스크톱 클라이언트(웹 앱도 제공)를 제공하며, Android 클라이언트는 Aurora에서 다운로드해야 합니다.
- [넥스트클라우드](https://f-droid.org/en/packages/com.nextcloud.client/)는 협업, 장치 간 동기화 및 파일 저장을 위한 모든 기능을 갖춘 클라우드 기반 솔루션을 제공합니다. 고급 사용자는 원하는 하드웨어에서 무료 및 오픈 소스 소프트웨어를 자체 호스팅하도록 선택할 수 있습니다. 안드로이드 클라이언트는 F-Droid를 통해 다운로드할 수 있습니다.
- [크립트패드](https://cryptpad.fr/)는 Google 문서 도구의 무료 웹 기반 E2EE 대안을 제공합니다.


![image](assets/fr/23.webp)

프로톤 드라이브


https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

## 단점


여러분이 익숙하게 사용하던 대기업 애플리케이션을 대체할 수 있는 오픈 소스와 프라이버시를 보호하는 대안은 많으며, 그중 일부는 스파이웨어가 가득한 폐쇄형 소스보다 더 나은 경우가 많습니다.


하지만 GrapheneOS로 전환할 때 대안이 없어 포기해야 하는 몇 가지 편의 기능이 있습니다. 여기에는 다음이 포함됩니다:



- 애플 카플레이/안드로이드 오토** - 기존 방식인 블루투스, USB 또는 Aux를 사용해야 합니다.
- 애플/구글 페이** - 거의 모든 사람들이 Wallet를 휴대하고 다닙니다!
- 뱅킹 앱** - 전혀 작동하지 않는 것은 아닙니다. 실제로 완벽하게 작동하는 앱도 있습니다. Google Play 서비스를 활성화한 상태에서만 작동하는 앱도 있고(아래에서 자세히 알아보세요), 전혀 작동하지 않는 앱도 있습니다. 은행에 대한 보고서[여기](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/)를 읽고 현재 상태를 확인하세요. 작동하지 않는 목록에 포함되어 있어도 걱정하지 마시고 홈 화면에 웹 앱으로 URL을 저장하면 됩니다.
- 푸시 알림** - 특정 앱을 사용하지 않을 때 업데이트를 보내는 대부분의 애플리케이션은 Google Play 서비스를 통해 업데이트를 보냅니다. 이러한 앱은 GrapheneOS에 기본적으로 설치되어 있지 않으므로 친구가 이메일을 보낼 때 즉시 알림을 받지 못한다면 이 때문일 수 있습니다. 다행히 위에서 언급한 앱 중 일부는 자체 백그라운드 연결을 구현하여 주기적으로 업데이트를 확인한 다음 필요한 경우 알림을 보내도록 되어 있습니다


### 샌드박스가 적용된 Google Play


**참고: ** GrapheneOS는 호환성 Layer을 통해 표준 앱 샌드박스에서 Google Play의 공식 릴리스를 설치 및 사용할 수 있는 옵션을 제공합니다. 구글플레이는 앱 샌드박스를 우회하여 막대한 양의 권한이 있는 액세스 권한을 받는 것과는 달리, GrapheneOS에 대한 특별한 액세스 권한이나 권한을 전혀 받지 않습니다.


즐겨 찾는 앱의 푸시 알림 없이는 살 수 없거나 특정 '필수' 앱이 Play 서비스 없이는 쓸모없다면, GrapheneOS를 사용하면 완전히 샌드박스된 환경에서 이러한 서비스를 [설치](https://grapheneos.org/usage#sandboxed-google-play-installation)할 수 있습니다. 일단 설치되면 이러한 서비스는 Google 계정이 없어도 작동하며, 각 서비스의 권한을 엄격하게 제어할 수 있습니다.


첫날에 서둘러 설치하기 전에 이 기능을 사용하지 않고도 얼마나 멀리 갈 수 있는지 확인해 보세요. 앱이 없어도 정상적으로 작동하는 앱이 얼마나 많은지 알게 되면 아마 놀라실 겁니다.


설치하려면 사전 설치된 '앱' 애플리케이션을 탭한 다음 'Google Play 서비스'를 탭하면 됩니다. 사생활 보호가 필요한 앱과 함께 완전히 별도의 사용자 프로필에 설치하여 휴대전화의 나머지 부분과 Layer의 추가 분리를 제공하는 것도 좋습니다.


![image](assets/fr/24.webp)

Play 서비스 설치 화면


### 프로필


GrapheneOS를 사용하면 휴대폰 내에서 별도의 휴대폰 환경을 사용할 수 있습니다. 추가 프로필은 자체 앱과 서비스를 설치할 수 있으며 소유자 계정의 파일이나 데이터에는 액세스할 수 없습니다.

필수 앱 중 한두 개만 Play 서비스가 필요하지만 사용 빈도가 매우 낮은 앱이 있는 경우, 해당 앱을 별도의 프로필에 Play 서비스와 함께 설치하여 소유자 프로필에서 실행함으로써 사소한 개인정보 노출을 더욱 강화하는 것도 좋은 아이디어입니다.


이 사용 사례에 대한 자세한 내용은 [여기](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2)에서 확인할 수 있습니다.


사용 사례에 맞게 별도의 프로필을 추가하려는 경우 [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) 앱이 유용할 수 있습니다. Insular를 사용하면 이 가이드의 앞부분에서 설명한 기존 설치 경로를 거치지 않고도 기존 앱을 새 프로필로 쉽게 복제할 수 있습니다. 또한 Insular를 사용하면 해당 앱을 빠르게 '동결'하여 해당 앱의 모든 백그라운드 서비스가 실행되지 않도록 완전히 비활성화할 수 있습니다.


![image](assets/fr/24.webp)

사용자 프로필 관리 화면


### 전자 심즈


휴대폰 개인정보 보호 수준을 한 단계 높이고 실제 신원과 분리된 휴대폰 서비스를 이용하고 싶으시다면 eSIM이 적합할 수 있습니다. ESIM은 온라인에서 구매하여 QR 코드를 통해 휴대폰에 추가할 수 있는 가상 SIM입니다. Bitcoin로 익명으로 결제할 수 있는 이러한 서비스를 제공하는 회사로는 [Silent.Link](https://silent.link/) 및 [Bitrefill](https://www.bitrefill.com/gb/en/esims/)이 있습니다.


eSIM을 휴대폰 개인정보 보호를 위한 만병통치약으로 간주해서는 안 됩니다. 올바르게 사용하면 유용한 도구가 될 수 있지만, 완전히 '오프 그리드'로 전환하려는 의도가 있다면 모든 유형의 휴대폰 서비스 사용의 [트레이드오프](https://grapheneos.org/faq#cellular-tracking)에 대해 조사해 보세요.


샌드박스 플레이 서비스는 GrapheneOS에서 eSIM 프로비저닝을 위해 설치해야 합니다.


## 백업


새로운 탈구글 픽셀 휴대전화를 설정한 후에는 백업을 만들어 두는 것이 좋습니다. 이 백업을 통해 휴대전화를 분실하거나 도난당한 경우 동일한 상태로 복원할 수 있습니다.


백업 파일을 외부 저장 미디어에 저장하거나 Nextcloud와 같은 자체 호스팅 클라우드 솔루션에 저장할 수 있지만, 일부 사용자는 후자의 옵션에 대해 다양한 수준의 성공률을 보고합니다.


첫 번째 백업을 만들려면 다음과 같이 하세요:


1. 설정** > **시스템** > **백업**으로 이동한 다음 12단어 복구 코드를 적어 둡니다. 이 코드는 나중에 백업 파일의 암호를 해독하는 데 필요합니다. 코드를 분실하면 휴대폰 백업에 액세스할 수 없게 됩니다.

2. 다음으로 저장 위치를 선택합니다. 외장 USB 드라이브 또는 산업용 등급의 microSD 카드를 추천합니다.

3. 백업할 데이터를 선택합니다. 지정된 저장 매체에 공간이 충분하다면 모든 데이터를 선택하는 것이 좋습니다.

4. 오른쪽 상단의 점 3개를 탭하고 **지금 백업하기**를 선택합니다.


![image](assets/fr/26.webp)


백업 화면


외부 저장 매체에 오프라인 백업을 하는 경우, 최악의 상황이 발생하더라도 휴대폰의 최근 중요한 업데이트가 손실되지 않도록 이 단계를 정기적으로 완료하는 것이 좋습니다.


![video](https://www.youtube.com/embed/eyWmcItzisk)


백업 프로세스를 자세히 설명하는 동영상


## 결론


최근 몇 년 동안 GrapheneOS 소프트웨어는 크게 발전했습니다. 그 어느 때보다 안정적이고 호환성이 뛰어납니다. 여기에 번성하는 오픈 소스 및 개인 정보를 보호하는 앱 생태계가 결합되어 여러분과 같은 '평범한' 사람들에게도 GrapheneOS는 주식 Android 또는 iOS의 진정한 대안이 될 수 있습니다!


데이터 유출과 드래그넷 감시는 오늘날에는 너무 흔해서 더 이상 헤드라인을 장식하지 않습니다. 스스로를 보호하는 것은 여러분의 몫입니다. 그 과정에서 조정과 희생이 따르겠지만, 이러한 침해에 대한 노출을 줄이는 것은 생각만큼 어렵지 않습니다.


이 가이드가 여러분의 여정에 조금이나마 도움이 되길 바랍니다. 이 가이드가 유용했고 제 작업을 지원하고 싶으시다면 [기부](/팁)를 보내주세요.


기존 그래핀OS 사용자이거나 이 가이드를 통해 사용자가 되신다면, [기부](https://grapheneos.org/donate)를 통해 이들의 중요한 작업을 지원하는 것을 고려해 보세요.


### 자세히 알아보기


그래핀OS는 누구나 몇 주만 투자하면 쉽게 이해할 수 있는 토끼굴입니다. 요구 사항과 위협 모델에 맞게 환경을 조정하기 위해 배우고 수정할 수 있는 것이 너무 많습니다. 아래는 여정을 계속할 수 있는 몇 가지 링크입니다:



- [그래핀OS 공식 사용 가이드](https://grapheneos.org/usage) - 공식 웹사이트
- [그래핀OS 포럼](https://discuss.grapheneos.org/) - 공식 웹사이트
- [GrapheneOS 설정 마스터클래스](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - 'The Privacy Wayfinder'의 동영상
- [그래핀OS 일반 팟캐스트](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - '워치맨 프라이버시'의 팟캐스트


*이 튜토리얼은 [MIT 라이선스 하에 Bitcoiner.Guide의 BitcoinQnA](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md)에 게시된 원본 콘텐츠를 각색한 것으로, 최초 작성에 대한 모든 저작권은 해당 게시자에게 있습니다*