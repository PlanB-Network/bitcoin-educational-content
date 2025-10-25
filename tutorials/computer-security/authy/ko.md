---
name: Authy 2FA
description: 2단계 인증 애플리케이션은 어떻게 사용하나요?
---
![cover](assets/cover.webp)


오늘날 2단계 인증(2FA)은 무단 액세스로부터 온라인 계정의 보안을 강화하는 데 필수적인 요소가 되었습니다. 사이버 공격이 증가함에 따라 비밀번호에만 의존해 계정을 보호하는 것은 때때로 불충분할 수 있습니다. 2단계 인증은 비밀번호 외에 두 번째 인증 수단을 요구함으로써 보안을 한층 더 강화합니다. 이 인증은 SMS를 통해 전송된 코드, 전용 앱에서 생성된 동적 코드, 물리적 보안 키 사용 등 여러 가지 형태로 이루어질 수 있습니다. 2단계 인증을 사용하면 비밀번호를 도난당한 경우에도 계정이 유출될 위험이 크게 줄어듭니다.


## 인증 앱을 통한 2FA


다른 튜토리얼에서는 물리적 보안 키와 같은 다른 솔루션을 살펴볼 예정이지만, 이 튜토리얼에서는 2FA 애플리케이션에 대해 구체적으로 논의할 것을 제안합니다. 이러한 애플리케이션의 작동은 매우 간단합니다. 계정에서 2FA가 활성화되면 로그인할 때마다 일반적인 비밀번호뿐만 아니라 6자리 코드를 입력하라는 메시지가 표시됩니다. 이 코드는 2FA 애플리케이션에서 생성합니다. 이 6자리 코드의 중요한 특징은 정적 코드가 아니라 30초마다 애플리케이션에서 새 코드를 생성한다는 것입니다.

![AUTHY 2FA](assets/notext/01.webp)

30초마다 코드가 갱신되므로 공격자가 계정에 액세스하기가 매우 어렵습니다. 이 시스템은 공격자가 훔치거나 가로챈 코드를 재사용하지 못하도록 차단하며, 코드가 빠르게 만료됩니다. 따라서 공격자가 코드를 입수하더라도 새로운 코드가 필요하기 전까지 매우 짧은 시간 동안만 사용할 수 있습니다. 게다가 코드가 자주 변경되기 때문에 해커가 무차별 암호 대입을 통해 코드를 추측할 수 있는 시간이 크게 줄어듭니다.


따라서 인증 앱을 통한 2FA는 온라인 계정의 보안을 크게 향상시킬 수 있는 사용하기 쉽고 무료인 방법입니다.


2FA를 설정하는 데는 수많은 애플리케이션이 있으며, 그 중 가장 잘 알려진 것은 Google Authenticator와 Microsoft Authenticator입니다. 하지만 이 튜토리얼에서는 Authy라는 잘 알려지지 않은 또 다른 솔루션을 소개하고자 합니다. 이 모든 애플리케이션은 동일한 TOTP(*시간 기반 일회용 비밀번호*) 프로토콜을 사용하여 작동하므로 사용법이 매우 유사합니다.

Authy는 다른 대형 기술 회사의 솔루션에 비해 몇 가지 장점이 있습니다. 무엇보다도 여러 디바이스에서 2FA 토큰을 동기화할 수 있어 휴대폰 분실 또는 변경 시 유용하게 사용할 수 있습니다. 또한 Authy를 사용하면 암호화된 백업을 generate로 생성하여 온라인에 저장할 수 있으므로 기본 장치를 분실하더라도 토큰에 대한 액세스 권한을 잃을 염려가 없습니다. Interface 사용자의 관점에서 볼 때, 개인적으로 Authy가 다른 대안보다 더 쾌적하고 직관적인 경험을 제공한다고 생각합니다.


## Authy를 설치하는 방법은 무엇인가요?


스마트폰에서 앱 스토어(구글 플레이 스토어 또는 애플 스토어)로 이동하여 "*트윌리오 오티 인증기*"를 검색합니다.



- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)

![AUTHY 2FA](assets/notext/02.webp)

앱을 처음 실행할 때 계정을 만들어야 합니다. 해당 국가의 발신 코드와 전화번호를 선택한 다음 '*제출*'을 클릭합니다.

![AUTHY 2FA](assets/notext/03.webp)

코드 복구를 위해 Address 이메일을 입력하세요.

![AUTHY 2FA](assets/notext/04.webp)

Address를 확인하기 위한 이메일이 전송됩니다. 받은 6자리 숫자를 입력하여 확인합니다.

![AUTHY 2FA](assets/notext/05.webp)

사용 가능한 두 가지 방법 중 하나를 선택하여 휴대폰 번호를 인증합니다. SMS 수신을 선택하는 경우 메시지로 받은 6자리 코드를 입력하여 번호를 확인합니다.

![AUTHY 2FA](assets/notext/06.webp)

축하합니다, Authy 계정이 생성되었습니다!

![AUTHY 2FA](assets/notext/07.webp)

## Authy를 구성하는 방법은 무엇인가요?


시작하려면 화면 오른쪽 상단에 있는 작은 점 3개를 클릭하여 앱 설정으로 이동합니다.

![AUTHY 2FA](assets/notext/08.webp)

그런 다음 "*설정*"을 클릭합니다.

![AUTHY 2FA](assets/notext/09.webp)

"*내 계정*" 탭에서 계정을 수정할 수 있는 옵션이 있습니다. "*앱 보호*"를 선택해 앱에 PIN 코드를 추가하는 것이 좋습니다. 이렇게 하면 애플리케이션에 액세스하기 위한 보안이 5단계 더 강화됩니다.

![AUTHY 2FA](assets/notext/10.webp)

"*계정*" 탭에서 토큰에 대한 백업을 설정할 수 있습니다. 이 백업을 통해 문제 발생 시 코드를 복구할 수 있습니다. 이 백업은 사용자가 정의해야 하는 비밀번호를 사용하여 암호화됩니다. 이 비밀번호는 강력하고 안전한 곳에 보관하는 것이 중요합니다. 예를 들어 동일한 Authy 계정을 사용하는 두 번째 장치와 같은 다른 복구 방법이 있는 경우 이 백업을 설정하는 것이 반드시 필요한 것은 아닙니다.

![AUTHY 2FA](assets/notext/11.webp)In the "*Devices*" tab, you can see all the devices synchronized with your Authy account. You have the option to disable the use of multiple devices, which restricts access to your account to that device only. If you use only one device, this can increase the security of your account, but make sure you have another backup method in case you lose that device.


다른 디바이스의 추가를 허용하려면 새 디바이스를 추가하기 전에 현재 인증된 디바이스의 확인이 필요한 옵션을 Authy 계정에서 활성화하는 것이 좋습니다.

![AUTHY 2FA](assets/notext/12.webp)

새 디바이스를 추가하려면 동일한 자격 증명을 사용하여 이전 부분에서 설명한 설치 프로세스를 반복하면 됩니다. 그러면 기본 장치에서 이 새 액세스를 확인하라는 메시지가 표시됩니다.


## 계정에서 2FA를 설정하는 방법은 무엇인가요?


계정에서 Authy와 같은 앱을 통해 2FA 인증 코드를 설정하려면 해당 계정이 이 기능을 지원해야 합니다. 요즘에는 대부분의 온라인 서비스에서 이 2단계 인증 옵션을 제공하지만 항상 그런 것은 아닙니다. 다른 튜토리얼에서 소개한 Proton 메일 계정을 예로 들어 보겠습니다:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![AUTHY 2FA](assets/notext/13.webp)

이 2단계 인증 옵션은 일반적으로 계정 설정에서 '*비밀번호*' 또는 '*보안*' 섹션 아래에서 찾을 수 있습니다.

![AUTHY 2FA](assets/notext/14.webp)

Proton 메일 계정에서 이 옵션을 활성화하면 QR 코드가 표시됩니다. 그런 다음 Authy 앱으로 이 QR 코드를 스캔해야 합니다.

![AUTHY 2FA](assets/notext/15.webp)

인증에서 '*+*' 버튼을 클릭합니다.

![AUTHY 2FA](assets/notext/16.webp)

"*QR 코드 스캔*"을 클릭합니다. 그런 다음 웹사이트에서 QR 코드를 스캔합니다.

![AUTHY 2FA](assets/notext/17.webp)

필요한 경우 사용자 아이디를 조정할 수도 있습니다. 변경한 후 "*저장*" 버튼을 클릭합니다.

![AUTHY 2FA](assets/notext/18.webp)

그러면 Authy에서 30초마다 새로 고쳐지는 해당 계정에 고유한 6자리 동적 코드를 표시합니다.

![AUTHY 2FA](assets/notext/19.webp)

웹사이트에 이 코드를 입력하여 2FA 설정을 완료합니다.

![AUTHY 2FA](assets/notext/20.webp)

일부 사이트에서는 2FA를 활성화한 후 복구 코드를 제공하기도 합니다. 이 코드를 사용하면 Authy 앱에 액세스할 수 없는 경우 계정에 액세스할 수 있습니다. 안전한 곳에 저장해 두는 것이 좋습니다.

![AUTHY 2FA](assets/notext/21.webp)Your account is now secured with two-factor authentication via the Authy app.

![AUTHY 2FA](assets/notext/22.webp)

계정에 로그인할 때마다 Authy에서 생성한 동적 코드를 제공해야 합니다. 이제 모든 계정을 이 2단계 인증 방법과 호환되는 방식으로 보호할 수 있습니다. Authy에서 새 계정을 추가하려면 앱 오른쪽 상단에 있는 작은 점 3개를 클릭합니다.

![AUTHY 2FA](assets/notext/23.webp)

그런 다음 "*계정 추가*"를 클릭합니다.

![AUTHY 2FA](assets/notext/24.webp)

첫 번째 계정에 사용한 것과 동일한 단계를 따릅니다. 다양한 동적 코드가 Authy 홈 페이지에 표시됩니다.