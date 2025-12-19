---
name: GnuPG
description: 소프트웨어의 무결성과 신뢰성을 확인하는 방법은 무엇인가요?
---
![cover](assets/cover.webp)


소프트웨어를 다운로드할 때는 변경되지 않았는지, 실제로 공식 출처에서 제공한 것인지 확인하는 것이 매우 중요합니다. 특히 자금에 액세스할 수 있는 키를 보호하는 Wallet 소프트웨어와 같이 Bitcoin과 관련된 소프트웨어의 경우 더욱 그렇습니다. 이 튜토리얼에서는 소프트웨어를 설치하기 전에 소프트웨어의 무결성과 진위 여부를 확인하는 방법을 살펴보겠습니다. 비트코인 사용자들이 가장 선호하는 Wallet 소프트웨어인 Sparrow wallet을 예로 사용하지만, 다른 소프트웨어에 대해서도 절차는 동일합니다.


무결성 검증은 다운로드한 파일의 디지털 지문(즉, Hash)을 공식 개발자가 제공한 지문과 비교하여 파일이 수정되지 않았는지 확인하는 것입니다. 두 지문이 일치하면 파일이 원본과 동일하며 공격자에 의해 손상되거나 수정되지 않았음을 의미합니다.


반면에 진위 확인은 파일이 실제로 사기꾼이 아닌 공식 개발자가 제공한 파일인지 확인하는 것입니다. 이는 디지털 서명을 확인하여 이루어집니다. 이 서명은 소프트웨어가 합법적인 개발자의 개인 키로 서명되었음을 증명합니다.


이러한 검사를 수행하지 않으면 수정된 코드를 포함할 수 있는 멀웨어가 설치될 위험이 있습니다. 이 코드는 개인 키와 같은 정보를 훔치거나 파일에 대한 액세스를 차단할 수 있습니다. 이러한 유형의 공격은 특히 위조 버전이 배포될 수 있는 오픈 소스 소프트웨어의 맥락에서 매우 흔합니다.


이 검증을 수행하기 위해 무결성을 검증하는 해싱 기능과 PGP 프로토콜을 구현하는 오픈소스 도구인 GnuPG를 사용하여 진위 여부를 확인합니다.


## 전제 조건


Linux**를 사용하는 경우 대부분의 배포판에는 GPG가 사전 설치되어 있습니다. 그렇지 않은 경우 다음 명령을 사용하여 설치할 수 있습니다:


```bash
sudo apt install gnupg
```


MacOS**의 경우, 아직 홈브루 패키지 관리자를 설치하지 않았다면 다음 명령어를 사용하여 설치하세요:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


그런 다음 이 명령어로 GPG를 설치합니다:


```bash
brew install gnupg
```

Windows**의 경우, GPG가 없는 경우 [Gpg4win](https://www.gpg4win.org/) 소프트웨어를 설치할 수 있습니다.

![GnuPG](assets/notext/01.webp)


## 문서 다운로드


시작하려면 다양한 서류가 필요합니다. "*다운로드*" 섹션의 Sparrow wallet](https://sparrowwallet.com/download/)의 공식 사이트를 방문하세요. 다른 소프트웨어를 확인하려면 해당 소프트웨어의 웹사이트로 이동하세요.


![GnuPG](assets/notext/02.webp)


프로젝트의 GitHub 리포지토리(https://github.com/sparrowwallet/Sparrow/releases)로 이동할 수도 있습니다.


![GnuPG](assets/notext/03.webp)


운영 체제에 해당하는 소프트웨어의 설치 프로그램을 다운로드합니다.


![GnuPG](assets/notext/04.webp)


또한 "*SHA256SUMS*" 또는 "*MANIFEST*"라고 하는 파일의 Hash이 필요합니다.


![GnuPG](assets/notext/05.webp)


파일의 PGP 서명도 다운로드합니다. 이 파일은 '.asc' 형식의 문서입니다.


![GnuPG](assets/notext/06.webp)


다음 단계를 위해 이 모든 파일을 같은 폴더에 넣어야 합니다.


마지막으로 PGP 서명을 확인하는 데 사용할 개발자의 공개키가 필요합니다. 이 키는 소프트웨어 웹사이트, 프로젝트의 GitHub 저장소, 때로는 개발자의 소셜 미디어 또는 Keybase와 같은 전문 사이트에서 구할 수 있습니다. Sparrow wallet의 경우 개발자 Craig Raw의 공개 키는 Keybase(https://keybase.io/craigraw)에서 찾을 수 있습니다. 터미널에서 직접 다운로드하려면 다음 명령을 실행하세요:


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## 서명 확인


서명을 확인하는 과정은 **Windows**, **macOS**, **Linux**에서 동일합니다. 일반적으로는 이전 단계에서 이미 공개 키를 가져왔을 것이지만, 그렇지 않은 경우 다음 명령으로 가져옵니다:


```bash
gpg --import [key path]
```


키 경로`를 개발자의 공개 키 파일 위치로 바꿉니다.


![GnuPG](assets/notext/08.webp)


다음 명령으로 서명을 확인합니다:


```bash
gpg --verify [file.asc]
```


File.asc]`를 서명 파일의 경로로 바꿉니다. Sparrow의 경우 이 파일은 버전 2.0.0의 경우 "*Sparrow-2.0.0-manifest.txt.asc*"라고 합니다.


![GnuPG](assets/notext/09.webp)


서명이 유효하면 GPG가 이를 표시합니다. 그러면 파일의 진위 여부가 확인되므로 다음 단계로 넘어갈 수 있습니다.


![GnuPG](assets/notext/10.webp)


## Hash 확인

이제 소프트웨어의 진위 여부가 확인되었으므로 무결성을 검증해야 합니다. 소프트웨어의 Hash과 개발자가 제공한 Hash을 비교합니다. 두 개가 일치하면 소프트웨어 코드가 변경되지 않았음을 보장합니다.


Windows**에서 터미널을 열고 다음 명령을 실행합니다:


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


파일 경로]`를 설치 프로그램의 위치로 바꿉니다.


![GnuPG](assets/notext/11.webp)


단말기는 다운로드한 소프트웨어의 Hash을 반환합니다.


![GnuPG](assets/notext/12.webp)


일부 소프트웨어의 경우 SHA256이 아닌 다른 Hash 함수를 사용해야 할 수도 있다는 점에 유의하세요. 이 경우 명령에서 Hash 함수의 이름을 바꾸기만 하면 됩니다.


그런 다음 결과를 "*Sparrow-2.0.0-manifest.txt*" 파일에 있는 해당 값과 비교합니다.


![GnuPG](assets/notext/13.webp)


제 경우에는 두 해시가 완벽하게 일치하는 것을 확인할 수 있습니다.


MacOS** 및 **Linux**에서는 Hash 확인 프로세스가 자동화되어 있습니다. Windows에서와 같이 두 해시의 일치 여부를 수동으로 확인할 필요가 없습니다.


MacOS**에서 이 명령을 실행하기만 하면 됩니다:


```bash
shasum --check [file name] --ignore-missing
```


파일 이름]을 설치 프로그램의 이름으로 바꿉니다. 예를 들어, Sparrow wallet의 경우:


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


해시가 일치하면 다음과 같은 출력이 표시됩니다:


```bash
Sparrow-2.0.0.dmg: OK
```


Linux**에서도 명령은 비슷합니다:


```bash
sha256sum --check [file name] --ignore-missing
```


해시가 일치하면 다음과 같은 출력이 표시됩니다:


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


이제 다운로드한 소프트웨어가 정품이며 손상되지 않았음을 확신할 수 있습니다. 이제 컴퓨터에 설치를 진행해도 됩니다.


이 튜토리얼이 도움이 되었다면 아래에 엄지 손가락을 올려주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


저장 장치를 암호화하고 해독할 수 있는 소프트웨어인 VeraCrypt에 대한 다른 튜토리얼도 확인해 보시기 바랍니다.


https://planb.academy/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5