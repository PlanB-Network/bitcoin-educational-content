---
name: KeePass
description: 로컬 비밀번호 관리자를 설정하는 방법은 무엇인가요?
---
![cover](assets/cover.webp)


디지털 시대에는 뱅킹, 금융 플랫폼, 이메일, 파일 저장소, 건강, 관리, 소셜 네트워크, 비디오 게임 등 일상 생활의 다양한 측면을 아우르는 수많은 온라인 계정을 관리해야 합니다.


이러한 각 계정에서 본인을 인증하기 위해 비밀번호와 함께 식별자(주로 이메일 Address)를 사용합니다. 많은 수의 고유 비밀번호를 외울 수 없는 상황에서 동일한 비밀번호를 재사용하거나 기억하기 쉽도록 일반적인 비밀번호를 약간 수정하고 싶은 유혹을 받을 수 있습니다. 하지만 이러한 방법은 계정의 보안을 심각하게 손상시킬 수 있습니다.


비밀번호에 대해 지켜야 할 첫 번째 원칙은 비밀번호를 재사용하지 않는 것입니다. 각 온라인 계정은 완전히 구별되는 고유한 비밀번호로 보호해야 합니다. 공격자가 회원님의 비밀번호 중 하나를 유출하더라도 모든 계정에 액세스할 수 없도록 하려면 이 원칙이 중요합니다. 각 계정에 고유한 비밀번호를 사용하면 잠재적인 공격을 차단하고 공격 범위를 제한할 수 있습니다. 예를 들어, 비디오 게임 플랫폼과 이메일에 동일한 비밀번호를 사용하는데 게임 플랫폼과 관련된 피싱 사이트를 통해 해당 비밀번호가 유출되면 공격자가 이메일에 쉽게 액세스하여 다른 모든 온라인 계정을 제어할 수 있습니다.


두 번째 필수 원칙은 비밀번호의 강도입니다. 무차별 대입, 즉 시행착오를 통해 추측하기 어려운 비밀번호는 강력한 비밀번호로 간주됩니다. 즉, 비밀번호는 가능한 한 무작위적이고 길어야 하며 다양한 문자(소문자, 대문자, 숫자, 기호)를 포함해야 합니다.


이 두 가지 비밀번호 보안 원칙(고유성과 견고성)을 적용하는 것은 일상 생활에서 어려울 수 있습니다. 모든 계정에 대해 독특하고 무작위적이며 강력한 비밀번호를 외우는 것은 거의 불가능하기 때문입니다. 이때 비밀번호 관리자의 역할이 중요합니다.


비밀번호 관리자는 강력한 비밀번호를 생성하고 안전하게 저장하므로, 비밀번호를 일일이 외울 필요 없이 모든 온라인 계정에 액세스할 수 있습니다. 비밀번호는 마스터 비밀번호 하나만 기억하면 되며, 이 마스터 비밀번호를 통해 비밀번호 관리자에 저장된 모든 비밀번호에 액세스할 수 있습니다. 비밀번호 관리자를 사용하면 비밀번호 재사용을 방지하고 체계적으로 임의의 비밀번호를 생성하기 때문에 온라인 보안이 강화됩니다. 또한 민감한 정보에 대한 액세스를 중앙 집중화하여 일상적인 계정 사용을 간소화할 수 있습니다.

이 튜토리얼에서는 온라인 보안을 강화하기 위해 로컬 비밀번호 관리자를 설정하고 사용하는 방법에 대해 알아보세요. 여기서는 KeePass를 소개합니다. 하지만 초보자이고 여러 디바이스에서 동기화할 수 있는 온라인 비밀번호 관리자를 원하신다면 Bitwarden의 튜토리얼을 따르는 것이 좋습니다:

https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*주의: 비밀번호 관리자는 비밀번호를 저장하는 데 유용하지만 **절대로 Bitcoin Wallet의 Mnemonic 문구를 저장해서는 안 됩니다!** Mnemonic 문구는 종이나 금속과 같은 물리적 형식에만 저장해야 한다는 점을 기억하세요*


---

## KeePass 소개


KeePass는 무료 오픈 소스 비밀번호 관리 프로그램으로, 로컬 관리를 위한 안전한 무료 솔루션을 원하는 분들에게 적합합니다. 플러그인을 추가하지 않고 인터넷과 통신하지 않는 PC에 설치하는 소프트웨어입니다. 이는 이전 튜토리얼에서 다룬 Bitwarden과는 근본적으로 다른 접근 방식입니다. Bitwarden은 KeePass와 달리 여러 장치에서 동기화가 가능하므로 온라인 서버에 비밀번호를 저장해야 합니다.


기본적으로 KeePass는 Bitwarden과 같은 브라우저 확장 프로그램 사용을 지원하지 않으므로 소프트웨어에서 비밀번호를 수동으로 복사하여 붙여넣어야 합니다. 이는 제약처럼 보일 수 있지만, 자동 입력 기능을 사용하는 것보다 비밀번호를 복사하여 붙여넣는 것이 온라인 보안을 위해 좋은 습관입니다.


KeePass는 높은 보안 표준을 준수하면서 가볍고 사용하기 쉽도록 설계되었습니다. 이 소프트웨어는 자격 증명을 최적으로 보호하기 위해 데이터베이스를 로컬에서 암호화합니다. 또한, KeePass는 프랑스 사이버 보안 기관인 ANSSI의 인증을 받은 유일한 비밀번호 관리자입니다.


KeePass의 주요 장점 중 하나는 유연성입니다. 컴퓨터에 설치할 필요 없이 USB 스틱 등 다양한 방법으로 사용할 수 있습니다. 또한, [플러그인 환경](https://keepass.info/plugins.html) 덕분에 보다 구체적인 요구 사항을 충족하도록 KeePass를 사용자 지정할 수 있습니다.

![KEEPASS](assets/notext/01.webp)

## 키패스는 어떻게 다운로드하나요?


KeePass의 설치 과정은 사용 중인 운영 체제에 따라 다릅니다. Windows 또는 Linux 사용자의 경우 설치가 비교적 간단합니다. 그러나 macOS를 사용하는 경우, KeePass가 .NET 플랫폼에서 개발되어 macOS에서 직접 지원되지 않기 때문에 추가 단계가 필요합니다. 따라서 Apple 디바이스에서 KeePass를 실행할 수 있도록 호환 환경을 구성해야 합니다.


데비안/우분투 사용자의 경우 터미널을 열고 다음 명령을 입력합니다:


```bash
sudo apt-get 업데이트

sudo apt-get 설치 keepass2

```

For Fedora:

```

sudo dnf 설치 키패스

```

For Arch Linux:

```

sudo pacman -S keepass

```

If you are on a Windows computer, go to the [official KeePass download page](https://keepass.info/download.html), and download the latest version of the installer:
![KEEPASS](assets/notext/02.webp)
Click on the downloaded file to run it, then follow the instructions of the setup wizard to complete the installation (see next section).

For macOS users, the installation is a bit more complex. If you wish to use the original version of KeePass as on Windows, follow the instructions below. Otherwise, you can opt for [KeePassXC](https://keepassxc.org/), an alternative version compatible with macOS, which offers a slightly different interface.

To use KeePass, you will need a runtime environment for .NET applications. I recommend installing Mono for this. Go to the [official Mono page](https://www.mono-project.com/download/stable/#download-mac) in the "*macOS*" section, and click on the link to download the installation package (`.pkg`).
![KEEPASS](assets/notext/03.webp)
Open the downloaded `.pkg` file and follow the instructions to install Mono on your Mac.
![KEEPASS](assets/notext/04.webp)
Next, go to the official KeePass website and download the latest portable version in `.zip` format.
![KEEPASS](assets/notext/05.webp)
After downloading the `.zip` file, double-click to extract it. You will get a folder containing several files, including `KeePass.exe`. Open a terminal, navigate to the KeePass folder (replace `xx` with the version number):

```

cd ~/Downloads/KeePass-2.xx

```

And finally, run KeePass with Mono:

```

mono KeePass.exe

```