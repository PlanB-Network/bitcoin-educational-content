---
name: Picocrypt
description: 데이터 암호화를 위한 오픈 소스 도구
---
![cover](assets/cover.webp)



___



*이 튜토리얼은 [IT-Connect](https://www.it-connect.fr/)에 게시된 플로리안 버넬의 오리지널 콘텐츠를 기반으로 합니다. 라이선스 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). 원본 콘텐츠가 변경되었습니다*



___



## I. 프레젠테이션



이 튜토리얼에서는 높은 수준의 보안으로 데이터를 암호화하는 간단하고 가볍고 효과적인 암호화 소프트웨어인 Picocrypt에 대해 살펴보겠습니다.



파일 암호화**에 적합하며, 컴퓨터, USB 스틱**의 **데이터뿐만 아니라 클라우드에 저장된 데이터도 보호하는 데 사용할 수 있습니다. 예를 들어, 데이터를 암호화하여 **Microsoft OneDrive, Google Drive, iCloud 또는 Dropbox**에 저장할 수 있지만, 이 목적을 위해 향후 기사에서 소개할 다른 소프트웨어를 선호합니다.



제3자와 데이터를 **공유**해야 할 때에도 사용할 수 있습니다. Picocrypt와 암호 해독 키 덕분에 제3자는 자신의 컴퓨터에서 데이터를 해독할 수 있습니다. 따라서 계정이나 컴퓨터가 해킹당하더라도 데이터는 안전하게 보호됩니다.



피코크립트 프로젝트를 따르려면 Address은 하나뿐입니다:





- [깃허브의 Picocrypt](https://github.com/Picocrypt/Picocrypt)



완전 **무료 오픈 소스**인 PicoCrypt는 **윈도우, **리눅스**, **macOS**에서 사용할 수 있습니다. Windows에서는 직접 컴퓨터에 설치하거나 휴대용 버전을 사용할 수 있습니다.



## II. Picocrypt, 오픈 소스 암호화 소프트웨어



**피코크립트** 암호화 소프트웨어는 **VeraCrypt** 및 **크립토메이터**(*클라우드 환경의 데이터를 암호화하도록 설계됨*) 또는 **AxCrypt**와 같은 다른 잘 알려진 솔루션에 대한 **대안**으로 제시됩니다. 참고로 Picocrypt의 공식 GitHub에서 일부 경쟁사와의 비교를 확인할 수 있습니다:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

출처: [깃허브닷컴](https://github.com/Picocrypt/Picocrypt)



Picocrypt는 **3MB**에 불과한 **매우 가볍고**, 설치가 필요 없는 **휴대용 애플리케이션**으로, 관리자 권한이 필요하지 않다는 장점이 있습니다! 하지만 **강력하고 신뢰할 수 있는 알고리즘**에 의존하기 때문에 보안을 소홀히 하지 않습니다:





- XChaCha20** 암호화 알고리즘
- 키 바이패스 기능 **Argon2**



방금 언급한 장점 외에도 정말 매력적인 것은 **사용 편의성**입니다!



단 한 가지가 필요합니다: *위의 비교표(마지막 줄)에서 볼 수 있듯이 *코드 감사**가 필요하지만, 이는 계획되어 있습니다. 하지만 오픈 소스이기 때문에 소스 코드를 살펴보는 것을 막을 수는 없습니다.



위 표에서 BitLocker와 비교되었지만, **제 생각에 BitLocker와 Picocrypt는 서로 다른 용도로 사용됩니다**: 전체 볼륨(예: Windows의 볼륨)을 암호화하는 데는 BitLocker가, 트리 구조 또는 '드라이브' 유형의 저장 공간을 암호화하는 데는 Picocrypt가 사용됩니다.



## III. Picocrypt 사용



이 데모에서는 Windows 11 머신이 사용됩니다.



### A. Picocrypt로 데이터 암호화하기



먼저 공식 GitHub([이 페이지 참조](https://github.com/Picocrypt/Picocrypt/releases))에서 Picocrypt.exe를 다운로드해야 합니다.



애플리케이션을 열면 미니멀한 Interface이 화면에 표시됩니다. 한 파일, 여러 파일 또는 폴더** 등 데이터를 암호화하려면 Picocrypt의 Interface로 **드래그 앤 드롭**하기만 하면 됩니다. 그러면 암호화할 데이터가 선택됩니다.



![Image](assets/fr/020.webp)



그런 다음 데이터 암호화를 위해 암호화 키를 포함한 여러 옵션에 액세스할 수 있습니다. 강력한 비밀번호** 또는 **키 파일 형식의 암호화 키** 또는 **둘 다**가 될 수 있습니다. 비밀번호를 예로 들면, 직접 비밀번호를 만들거나 Picocrypt로 비밀번호를 생성하는 것 중에서 선택할 수 있습니다.



이 비밀번호는 데이터를 해독하는 데 사용될 수 있으므로 강력해야 합니다. "**비밀번호**" 및 "**비밀번호 확인**" 아래에 비밀번호를 입력한 다음 "**암호화**"를 클릭하여 데이터를 암호화하세요! 그 전에 "**출력을 다른 이름으로 저장**" 옆의 "**변경**" 버튼을 클릭하여 출력 디렉터리를 지정할 수 있습니다.



**참고**: 파일 형식으로 키를 사용하려면 '**키파일**' 오른쪽에 있는 '**만들기**'를 클릭하여 키를 만드세요. 그런 다음 "**수정**"을 클릭하고 키 파일을 해당 영역에 끌어다 놓아 선택합니다.



![Image](assets/fr/019.webp)



선택한 두 파일은 **PCV**가 Picocrypt에서 사용하는 확장자이므로 **암호화되어 **함께 그룹화**된 "**Encrypted.zip.pcv**" 파일에 저장됩니다. 이 ZIP 파일은 암호화되어 읽을 수 없습니다. 선택한 파일이 하나의 암호화된 ZIP 파일로 그룹화되는 것을 방지하려면 "**재귀적으로**" 옵션을 체크하여 암호화할 파일 수만큼 암호화된 파일이 있도록 해야 합니다.



데이터에 액세스하려면 Picocrypt를 사용하여 암호를 해독해야 합니다.



![Image](assets/fr/023.webp)



데이터 암호 해독에 대해 설명하기 전에 사용 가능한 몇 가지 옵션에 대한 몇 가지 정보를 알려드립니다:





- 편집증 모드**: Picocrypt에서 제공하는 가장 높은 보안 수준을 사용합니다. 이 도구는 데이터 인증에 BLAKE2b 대신 여러 계단식 암호화 알고리즘(XChaCha20 및 Serpent)과 HMAC-SHA3를 사용합니다.
- 리드-솔로몬**: 손상된 데이터의 오류 수정을 용이하게 하기 위해 *Reed-Solomon* 오류 수정 코드를 구현합니다. 이를 통해 파일의 약 3%의 손상 수준을 지원할 수 있습니다.
- 청크로 분할** 또는 **여러 부분으로 나누기**: 대용량 파일을 암호화하는 경우, Picocrypt에 여러 부분으로 분할하도록 요청할 수 있습니다. 이렇게 하면 파일을 더 쉽게 전송할 수 있습니다.
- 파일 압축** 또는 **파일 압축**: 파일을 압축하여 암호화된 파일의 크기를 줄입니다.
- 삭제된 파일** 또는 **보관된 파일**: 소스 파일을 삭제하여 암호화된 버전만 보관합니다



### B. Picocrypt로 데이터 복호화



데이터를 해독해야 하는 경우, 암호화하는 것보다 더 복잡하지 않습니다. Picocrypt를 열고 해독할 PCV 파일을 **드래그 앤 드롭**하기만 하면 됩니다. 그런 다음 비밀번호를 입력하거나 키 파일을 선택한 다음 "**해독**"을 클릭하세요.



![Image](assets/fr/021.webp)



이제 암호화되지 않은 버전의 "Encrypted.zip" ZIP 아카이브를 통해 두 파일을 일반 텍스트로 복구할 수 있습니다!



![Image](assets/fr/022.webp)



## IV. 결론



**경고를 받았습니다: Picocrypt는 사용하기 매우 쉽고 작동합니다! Interface는 미니멀하지만, 암호화를 사용자 지정하는 데 매우 유용한 옵션이 포함되어 있습니다! 또한 휴대용 버전으로 제공되므로 어디든 가지고 다닐 수 있으므로 안심하고 데이터를 해독할 수 있습니다**



강력한 비밀번호를 사용하여 데이터를 보호하고 키 파일을 사용하는 경우 백업하는 것을 잊지 마세요. 그렇지 않으면 Picocrypt에서 생성한 PCV 컨테이너를 더 이상 해독할 수 없습니다. 마지막으로, 명령줄에서 Picocrypt를 실행할 수 있는 [CLI 버전](https://github.com/Picocrypt/CLI)도 있다는 것을 알아두세요: 여기서도 Picocrypt는 새로운 가능성의 문을 열어줍니다.



https://planb.academy/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5