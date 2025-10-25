---
name: Proton Authenticator
description: 프로톤 인증기를 사용하여 2FA로 계정을 보호하려면 어떻게 해야 하나요?
---
![cover](assets/cover.webp)



2단계 인증(2FA)은 비밀번호 외에 본인만 알고 있다는 추가 증명을 요구함으로써 계정에 추가적인 보안 장벽을 추가합니다. 2FA를 활성화하면 피싱이나 데이터 유출로 인해 비밀번호가 유출되더라도 해킹의 위험이 크게 줄어듭니다. 2FA를 사용하지 않으면 공격자는 비밀번호만 있으면 계정에 액세스할 수 있지만, 2FA를 사용하면 두 번째 요소도 필요하므로 대부분의 계정 도용 시도를 차단할 수 있습니다.



다양한 유형의 2FA가 존재합니다. SMS 코드는 없는 것보다는 낫지만 SIM 스와핑 공격과 도청에 여전히 취약합니다. SMS를 기본 2FA로 사용하는 것은 권장하지 않습니다. 인증 애플리케이션(TOTP) generate 임시 코드는 디바이스에 로컬로 저장되므로 가로채기가 훨씬 더 어렵습니다. 물리적 보안 키는 최고의 보안을 제공하지만 전용 하드웨어가 필요합니다.



프로톤 인증기는 TOTP 인증기입니다. 기존 애플리케이션의 한계, 즉 많은 애플리케이션이 독점적이고 광고 추적기를 포함하며 암호화된 백업을 제공하지 않는다는 한계에 대한 Proton의 대응책입니다. 프로톤 인증기는 광고 및 트래커가 없는 오픈 소스 애플리케이션과 엔드투엔드 암호화 백업을 제공함으로써 차별화됩니다.



## 양성자 인증기 소개



프로톤 인증기는 개인정보 보호에 중점을 둔 서비스로 유명한 프로톤에서 개발한 모바일 및 데스크톱 TOTP 인증 애플리케이션입니다. 모든 Proton 제품과 마찬가지로 이 애플리케이션은 오픈 소스이며 독립적인 보안 감사를 거쳤습니다. 모든 플랫폼(Android, iOS, Windows, macOS, Linux)에서 무료로 사용할 수 있습니다.



프로톤 인증기는 다음과 같은 주요 기능을 제공합니다:





- 2FA 계정을 위한 **TOTP** 코드를 생성하며, Google 인증기, Authy 등을 사용하는 대부분의 사이트와 호환됩니다.





- 암호화된 클라우드 백업** 옵션: 애플리케이션을 Proton 계정에 연결하여 종단 간 암호화를 통해 코드를 백업하고 동기화할 수 있습니다. 기기를 분실한 경우 새 기기를 다시 연결하기만 하면 모든 코드를 복원할 수 있습니다.





- 다중 디바이스 동기화**: 앱에서 Proton에 로그인하면 종단 간 암호화를 통해 2FA 코드가 여러 디바이스 간에 자동으로 동기화됩니다. IOS에서는 iCloud를 통한 동기화도 가능합니다.





- 비밀번호 또는 생체인식**을 통한 로컬 잠금: 이 애플리케이션은 PIN 및/또는 지문/얼굴 ID 잠금을 제공합니다. 따라서 누군가가 잠금 해제된 휴대폰에 물리적으로 접근하더라도 Proton Authenticator를 열 수 없습니다.





- 데이터 수집 또는 추적기 없음**: 프로톤은 애플리케이션을 통해 어떠한 개인 데이터도 수집하지 않습니다. 숨겨진 광고나 행동 분석이 없습니다.





- 간편한 가져오기/내보내기**: 프로톤 인증기의 강점 중 하나는 기존 계정을 위한 가져오기 마법사로, 다른 애플리케이션(Google 인증기, Authy, Aegis 등)과 호환된다는 점입니다. 필요한 경우 코드를 파일로 내보낼 수도 있습니다.



간단히 말해, Proton Authenticator는 안전하고, 비공개적이며, 유연한 타협하지 않는 2FA 솔루션을 목표로 합니다.



## 설치



프로톤 인증기는 모든 플랫폼에서 무료로 사용할 수 있습니다. 애플리케이션을 다운로드하려면 공식 페이지로 이동하세요: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*애플리케이션의 주요 기능과 Interface*을 보여주는 공식 프로톤 인증기 페이지



이 페이지에서는 모든 운영 체제에 대한 다운로드 링크를 찾을 수 있습니다: Android, iOS, Windows, macOS, Linux. 원하는 운영 체제를 클릭하고 표준 설치 단계를 따르기만 하면 됩니다.



이 튜토리얼에서는 macOS에 앱을 설치하고 구성하는 방법을 보여드리고, iOS에 앱을 설치하고 두 기기 간에 코드를 동기화하는 방법을 살펴봅니다.



### MacOS에 설치



애플리케이션을 다운로드하고 설치했으면 Proton Authenticator를 실행합니다. 처음 실행하면 애플리케이션이 몇 가지 초기 구성 화면을 안내합니다:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*"모든 코드의 보안" 메시지와 "시작하기"* 버튼이 있는 Proton Authenticator 시작 화면



### 초기 가져오기



이전에 다른 2FA 애플리케이션을 사용 중인 것을 Proton 인증서가 감지하면 가져오기 마법사가 나타날 수 있습니다. 특정 애플리케이션(Google Authenticator, 2FAS, Authy, Aegis 등)에서 직접 가져오기를 지원합니다. 또는 이 단계를 건너뛰고 나중에 수동으로 계정을 추가할 수도 있습니다.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*다른 인증 애플리케이션에서 코드 전송을 위한 가져오기 마법사*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*호환되는 가져오기 애플리케이션: 2FAS, 이지스 인증기, Authy, 비트워든 인증기, 엔테 인증 및 구글 인증기*



### 로컬 애플리케이션 보호



잠금 해제 PIN을 설정하거나 가능한 경우 생체 인식 잠금 해제(Touch ID)를 활성화합니다. 이 단계는 Mac을 사용하는 다른 사람이 2FA 코드에 무료로 액세스하는 것을 방지하는 데 매우 중요합니다.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*"데이터 보호" 메시지 및 "Touch ID 활성화"* 버튼이 있는 Touch ID 구성 화면



### 동기화 옵션



또한 이 애플리케이션을 사용하면 iCloud 동기화를 활성화하여 Apple 장치 간에 데이터를 안전하게 백업할 수 있습니다.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*"암호화된 iCloud 동기화로 데이터를 안전하게 백업"*이라는 메시지와 함께 iCloud 동기화 옵션이 표시됩니다



이 단계가 완료되면 Proton 인증기를 사용할 준비가 된 것입니다.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*"새 코드 생성" 및 "코드 가져오기"* 옵션이 있는 Interface 메인 빈 양성자 인증기



## ProtonMail로 2FA 계정 추가하기



이제 프로톤메일을 예로 들어 첫 번째 2단계 인증 코드를 추가하는 방법을 살펴보겠습니다. 이 방법은 2단계 인증을 지원하는 모든 서비스에서 동일하게 작동합니다.



### ProtonMail에서 2FA 활성화



우선, 자세한 내용은 프로톤메일 가이드를 참조하세요:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

프로톤메일 계정에 로그인하고 보안 설정으로 이동합니다. '2단계 인증' 옵션을 찾아 활성화합니다.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*'2단계 인증'* 섹션의 '인증 앱' 옵션이 있는 ProtonMail 설정 페이지로 이동합니다



버튼을 클릭하여 인증기를 활성화하면 ProtonMail에서 인증 애플리케이션을 선택하라는 메시지가 표시됩니다.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*"취소" 및 "다음"* 버튼이 있는 ProtonMail 2FA 구성 창



그러면 프로톤메일은 인증 애플리케이션으로 스캔할 수 있는 QR 코드를 표시합니다.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*인증 애플리케이션으로 스캔할 프로톤메일 QR 코드, '대신 수동으로 키 입력' 옵션* 사용 가능



수동으로 키를 입력하려면 '대신 수동으로 키 입력'을 클릭하여 비밀 키를 확인하세요.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*2단계 인증 정보를 수동으로 입력합니다: 키, 간격(30) 및 숫자(6)**



### 프로톤 인증기로 QR 코드 스캔하기



MacOS의 Proton 인증기에서 "새 코드 만들기"를 클릭합니다. 이 애플리케이션은 몇 가지 옵션을 제공합니다: **QR 코드 스캔** 또는 **키를 수동으로 입력**.



Mac의 카메라를 사용하여 ProtonMail 화면에 표시된 QR 코드를 스캔합니다. QR 코드를 스캔하면 새 코드 구성 화면으로 이동합니다.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*제목(프로톤메일), 비밀, 발신자(프로톤), 숫자 매개변수 및 간격 필드가 포함된 새로운 항목 생성 창*이 추가되었습니다



프로톤 인증기가 자동으로 정보를 입력합니다. 원하는 경우 이름을 사용자 지정한 다음 "저장"을 클릭할 수 있습니다.



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*남은 시간이 표시된 ProtonMail(848 812)에 대해 생성된 TOTP 코드*입니다



### 구성 유효성 검사



프로톤 메일은 2FA가 올바르게 작동하는지 확인하기 위해 프로톤 인증기에서 생성한 6자리 코드를 입력하라는 메시지를 표시합니다.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*6자리 코드(848812)*를 입력하라는 ProtonMail 유효성 검사 화면이 표시됩니다



애플리케이션에서 코드를 복사하여(클릭하여) ProtonMail에 붙여넣어 활성화를 완료합니다.



확인이 완료되면 ProtonMail에서 복구 코드를 다운로드하라는 메시지가 표시됩니다. 신중하게 저장하는 것이 중요합니다.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*구조 코드 목록과 "다운로드"* 버튼이 있는 ProtonMail 복구 코드 화면



### 긴급 코드



계정을 추가할 때 서비스에서 제공한 복구 코드를 보관하세요. 대부분의 사이트는 안전한 곳에 보관할 수 있는 정적 일회용 복구 코드를 제공합니다. 이러한 백업 코드는 2FA 애플리케이션에 액세스할 수 없는 경우 계정에 액세스할 수 있도록 Proton Authenticator 외부에 보관하세요.



## IOS 설치 및 코드 가져오기



이제 macOS에서 프로톤 인증기를 설정했으니 iPhone 또는 iPad에서도 사용할 수 있습니다. 여러 디바이스에서 2단계 인증 코드를 받는 방법은 다음과 같습니다.



### IOS에서 애플리케이션 다운로드



App Store로 이동하여 "양성자 인증기"를 검색합니다. IOS 디바이스에 애플리케이션을 다운로드하여 설치합니다.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*IOS의 설치 과정: 시작 화면, 가져오기 마법사, 호환 가능한 애플리케이션 선택, 마지막 "Proton Authenticator에서 코드 가져오기"* 화면



### 방법 1: JSON 파일을 통한 내보내기/가져오기



자동 동기화(iCloud 또는 Proton 계정)를 사용하지 않는 경우 Mac에서 iPhone으로 코드를 수동으로 전송해야 합니다:



**1단계 - macOS에서 내보내기** :



Mac에서 프로톤 인증기를 열고 설정(톱니바퀴 아이콘)으로 이동합니다. 메뉴에서 '내보내기'를 클릭합니다.



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*"내보내기" 옵션이 표시된 macOS의 Proton 인증자 설정 메뉴*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*파일 이름 "Proton_Authenticator_backup_2025" 및 "저장"* 버튼으로 내보내기 창 열기



Mac에 JSON 파일을 저장합니다. 보안 이메일로 보내거나 iCloud 드라이브에 저장하여 iPhone에서 액세스할 수 있습니다.



**2단계 - iOS에서 가져오기** :



IPhone에서 프로톤 인증기를 설치하고 구성하는 동안 코드 가져오기를 선택합니다. 목록에서 '양성자 인증기'를 선택하고 JSON 파일을 가져옵니다.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*IOS에서 가져오기 프로세스: JSON 파일 현지화, 가져오기 확인 및 Face ID 및 iCloud 옵션*을 사용한 구성 화면



### 방법 2: 자동 동기화



**프로톤 계정을 통해(멀티 플랫폼 동기화용)** :



아직 프로톤 계정을 설정하지 않았고 다른 운영 체제 간에 동기화하려는 경우, 애플리케이션에서 프로톤 계정을 만들거나 연결하라는 메시지가 표시됩니다.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*무료 Proton 계정을 만들거나 기존 계정*에 연결하라는 장치 동기화 화면이 표시됩니다



**iCloud를 통해(Apple 에코시스템 전용)** :


Apple 기기만 사용하는 경우 애플리케이션 설정에서 iCloud 동기화를 선택할 수 있습니다. 이 방법을 사용하면 프로톤 계정 없이도 모든 Apple 기기 간에 코드를 자동으로 안전하게 동기화할 수 있습니다.



## 암호화된 백업 및 복원



프로톤 인증기의 주요 기능 중 하나는 2FA 코드의 엔드투엔드 백업 기능으로, 장치를 분실하거나 변경해도 처음부터 다시 시작해야 하는 불편함을 없애줍니다.



### 엔드투엔드 암호화



Proton 인증기를 사용한 암호화된 클라우드 백업의 경우, TOTP 비밀은 Proton 서버로 전송되기 전에 장치에서 로컬로 암호화됩니다. 암호 해독은 Proton 계정에 연결된 장치에서 사용자 본인만 가능합니다. Proton AG는 등록된 코드를 읽을 수 있는 키를 가지고 있지 않습니다.



IOS에서 Proton 계정 대신 iCloud를 선택하면 데이터가 Apple 표준에 따라 암호화됩니다. Android의 로컬 백업을 사용하면 원하는 비밀번호로 백업 파일을 암호화할 수 있습니다.



### 분실 시 복원



휴대폰을 분실, 도난당하거나 휴대폰을 변경한 경우 :



**프로톤 백업이 활성화된 경우**: 새 디바이스에 Proton 인증기를 설치합니다. 초기 설정 중에 동일한 Proton 계정으로 로그인합니다. 즉시 애플리케이션이 암호화된 백업에서 모든 2FA 코드를 동기화하고 다운로드합니다.



**iCloud 백업 사용(iOS)**: 새 iPhone/iPad를 동일한 Apple ID로 연결하고 iCloud 키체인을 활성화하세요. Proton 인증서를 설치한 후 iCloud에 연결합니다. 코드가 iCloud를 통해 동기화되고 표시되어야 합니다.



**클라우드 백업 없음**: 계정을 수동으로 가져와야 합니다. 백업 파일을 내보낸 경우, Proton 인증서의 가져오기 기능을 사용하세요. 최악의 경우, 백업이 없는 경우 각 서비스의 백업 코드를 사용하거나 지원팀에 문의해야 합니다.



프로톤 인증기를 사용하면 언제든지 계정을 암호화된 파일 또는 다중 계정 QR 코드로 내보낼 수 있습니다. 이러한 옵션을 사용하면 더욱 안심할 수 있습니다.



## 모범 사례



2FA 인증서를 사용하면 보안이 크게 향상되지만 특정 모범 사례를 준수해야 합니다:



### 비상 코드 저장



서비스에서 2FA를 활성화하면 복구 코드 목록이 제공되는 경우가 많습니다. 이 복구 코드를 종이나 암호화된 비밀번호 관리자 등에 보관하세요. 인증자를 완전히 분실한 경우 이러한 정적 코드가 도움이 됩니다.



### 비밀번호와 2FA 코드를 혼동하지 마세요



TOTP도 저장하는 비밀번호 관리자를 사용하고 싶은 유혹이 있을 수 있습니다. 하지만 비밀번호와 2FA 코드를 같은 곳에 보관하면 단일 실패 지점이 발생하고 이중 인증이 약화됩니다. 보안을 극대화하기 위해 많은 전문가들은 비밀번호는 보안 관리자에, 2FA 코드는 Proton Authenticator와 같은 별도의 애플리케이션에 보관하는 등 두 가지 요소를 분리할 것을 권장합니다. 하지만 통합 관리자를 사용하는 것이 2FA를 전혀 사용하지 않는 것보다는 여전히 낫습니다.



### 여러 2FA 방법 활성화



중요한 계정에는 두 개 이상의 2차 요소를 사용하는 것이 가장 이상적입니다. 서비스에서 허용하는 경우 주저하지 말고 물리적 보안 키를 추가하세요. 자세한 내용은 Yubikey 물리적 키에 대한 튜토리얼을 참조하세요:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

마찬가지로 인쇄된 비상 코드를 잘 보관하세요.



### 신중함을 유지하며 디바이스 보호



다른 사람이 잠금 해제된 휴대폰을 검색하지 못하도록 하세요. Proton 인증기를 사용하면 PIN/생체 인식으로 코드가 보호되므로 이 PIN을 알려주지 마세요. 마찬가지로 2FA를 사용하더라도 실시간으로 사기성 사이트에 코드를 제공하면 공격자가 이를 사용할 수 있으므로 피싱에 주의하세요.



### 업데이트 및 감사



Proton 인증서를 최신 상태로 유지합니다(업데이트를 통해 가능한 결함을 수정합니다). 코드가 공개되어 있으므로 커뮤니티에서 비공식 감사를 수행하고 Proton은 공식 감사 결과를 게시합니다.



## 다른 애플리케이션과의 비교



프로톤 인증기는 다른 인증 애플리케이션과 어떻게 비교하나요? 다음은 비교 요약입니다:



**양성자 인증기**: 오픈 소스, E2EE 암호화 클라우드 백업(옵션), 다중 장치 동기화, 로컬 잠금, 추적 금지, 모바일 및 데스크톱에서 사용 가능.



**구글 인증**: 독점, 2023년부터 Google 계정을 통한 백업, 종단 간 암호화 없음(키는 Google에서 볼 수 있음), 2023년에 다중 장치 동기화 추가, 기본적으로 애플리케이션 잠금 없음, Google 추적기 포함.



**이지스 인증기**: 오픈 소스, 로컬 백업 전용, 클라우드 동기화 없음, 코드/생체 인식 잠금, 추적 없음, Android 전용.



**인증**: 비밀번호로 암호화된 독점 클라우드 백업, 비공개 코드, 다중 장치 동기화, PIN 잠금/지문, 전화번호 수집, 데스크톱 애플리케이션 2024년 3월에 중단됨.



아래에서 Authy에 대한 가이드를 확인할 수 있습니다:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

프로톤 인증기는 오픈 소스, 다중 장치 암호화 동기화, 상업적 후속 조치 없음 등 가장 포괄적이고 안전한 솔루션 중 하나입니다.



## 리소스 및 지원



### 공식 문서




- 공식 웹사이트**: [proton.me/authenticator](https://proton.me/authenticator) - 제품 소개 및 다운로드
- 다운로드 페이지**: [proton.me/ko/authenticator/download](https://proton.me/fr/authenticator/download) - 모든 OS용 링크
- 프로톤 지원**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - 공식 2FA 활성화 가이드
- 프로톤 블로그**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - 공지사항 및 세부 기능 안내



### 소스 코드 및 투명성




- 깃허브 양성자 인증기**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - 오픈 소스 코드
- 보안 감사**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - 독립 감사 보고서



### 권장 안전 테스트


구성이 완료되면 설정을 테스트합니다:




- [내가 도용당했나요](https://haveibeenpwned.com/) - 계정이 도용당했는지 확인하세요
- [2FA 디렉토리](https://2fa.directory/) - 2FA를 지원하는 서비스 목록



### 커뮤니티 및 토론




- 레딧 r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - 공식 양성자 커뮤니티
- 개인정보 보호 가이드 포럼**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - 개인정보 보호 문제에 대한 기술적 논의
- 레딧 r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - 일반적인 개인정보 보호 팁



### 기타




- [내가 도용당했나요](https://haveibeenpwned.com/) - 계정이 도용당했는지 확인하세요
- [2FA 디렉토리](https://2fa.directory/) - 2FA를 지원하는 서비스 목록