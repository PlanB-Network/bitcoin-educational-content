---
name: 교육 도구 추가
description: PlanB 네트워크에 새로운 교육 자료를 추가하는 방법은 무엇인가요?
---
![event](assets/cover.webp)


PlanB의 사명은 Bitcoin에 대한 선도적인 교육 리소스를 가능한 한 많은 언어로 제공하는 것입니다. 이 사이트에 게시된 모든 콘텐츠는 오픈 소스이며 GitHub에서 호스팅되므로 누구나 플랫폼을 더욱 풍성하게 만드는 데 참여할 수 있습니다.


튜토리얼과 교육 외에도 플랜비 네트워크는 누구나 이용할 수 있는 Bitcoin에 대한 다양한 교육 콘텐츠의 방대한 라이브러리를 "BET"(_비트코인 교육 툴킷_) 섹션에서 제공합니다(https://planb.academy/resources/bet). 이 데이터베이스에는 교육용 포스터, 밈, 유머러스한 선전 포스터, 기술 도표, 로고 및 사용자를 위한 기타 도구가 포함되어 있습니다. 이 이니셔티브의 목표는 전 세계에서 Bitcoin을 가르치는 개인과 커뮤니티에 필요한 시각 자료를 제공함으로써 이들을 지원하는 것입니다.


이 데이터베이스를 보강하는 데 참여하고 싶지만 방법을 모르시나요? 이 튜토리얼은 여러분을 위한 것입니다!


*사이트에 통합된 모든 콘텐츠는 저작권이 없거나 소스 파일의 라이선스를 준수해야 합니다. 또한 플랜비 네트워크에 게시된 모든 영상은 [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) 라이선스*에 따라 제공됩니다

![event](assets/01.webp)


- 먼저 GitHub에 계정이 있어야 합니다. 계정을 만드는 방법을 모르는 경우 자세한 튜토리얼을 만들어 안내해 드립니다.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 'resources/bet/' 섹션의 [데이터 전용 PlanB의 GitHub 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet)로 이동합니다:

![event](assets/02.webp)


- 오른쪽 상단의 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![event](assets/03.webp)


- 이전에 PlanB Network의 콘텐츠에 기여한 적이 없는 경우, 원본 리포지토리의 Fork를 만들어야 합니다. 리포지토리를 포크한다는 것은 자신의 GitHub 계정에 해당 리포지토리의 복사본을 생성하여 원본 리포지토리에 영향을 주지 않고 프로젝트 작업을 할 수 있도록 하는 것을 의미합니다. '이 리포지토리 Fork' 버튼을 클릭합니다:

![event](assets/04.webp)


- 그러면 GitHub 편집 페이지로 이동합니다:

![event](assets/05.webp)


- 콘텐츠를 위한 폴더를 만듭니다. 이렇게 하려면 '파일 이름...` 상자에 콘텐츠의 이름을 공백 대신 대시를 사용하여 소문자로 작성합니다. 이 예제에서는 2048단어 BIP39 목록의 PDF 시각 자료를 추가한다고 가정해 보겠습니다. 따라서 내 폴더를 `bip39-wordlist`: ![event](assets/06.webp)라고 부릅니다
- 폴더 생성을 확인하려면 같은 상자의 이름 뒤에 슬래시를 추가하면 됩니다(예: `bip39-wordlist/`). 슬래시를 추가하면 파일이 아닌 폴더가 자동으로 생성됩니다:

![event](assets/07.webp)


- 이 폴더에 `bet.yml`이라는 이름의 첫 번째 YAML 파일을 만듭니다:

![event](assets/08.webp)


- 이 템플릿을 사용하여 콘텐츠와 관련된 정보로 이 파일을 채우세요:


```yaml
project:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


각 필드에 입력해야 할 세부 정보는 다음과 같습니다:



- 프로젝트`**: PlanB 네트워크에서 조직의 식별자를 표시합니다. 아직 회사의 '프로젝트' 식별자가 없는 경우 이 튜토리얼을 따라 생성할 수 있습니다.


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

프로젝트 프로필이 없는 경우 프로젝트 프로필을 만들지 않고도 이름, 가명 또는 회사 이름을 사용할 수 있습니다.



- 유형`**을 입력합니다: 다음 두 가지 옵션 중에서 콘텐츠의 성격을 선택합니다:
 - 교육용 콘텐츠의 경우 '교육용 콘텐츠'를 클릭합니다.
 - 다른 유형의 다양한 콘텐츠를 보려면 '시각적 콘텐츠'를 클릭하세요.



- 링크`**: 콘텐츠에 대한 링크를 제공합니다. 두 가지 옵션이 있습니다:
 - PlanB의 GitHub에서 콘텐츠를 직접 호스팅하기로 선택한 경우 다음 단계에서 이 파일에 대한 링크를 추가해야 합니다.
 - 콘텐츠가 개인 웹사이트 등 다른 곳에서 호스팅되는 경우 여기에 해당 링크를 표시하세요:
     - 다운로드`: 콘텐츠를 다운로드할 수 있는 링크입니다.
     - '보기': 콘텐츠를 볼 수 있는 링크(다운로드 링크와 동일할 수 있음). 콘텐츠가 여러 언어로 제공되는 경우 각 언어에 대한 링크를 추가합니다.



- 태그`**: 콘텐츠와 관련된 두 개의 태그를 추가합니다. 예시:
 - Bitcoin
 - 기술
 - 경제
 - 교육
 - 밈...



- 기여자`**: 기여자 식별자가 있는 경우 이를 언급하세요.


예를 들어 YAML 파일은 다음과 같이 보일 수 있습니다:


```yaml
project: Plan ₿ Academy
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the Plan ₿ Academy repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the Plan ₿ Academy site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
Mnemonic 문구를 인코딩하는 데 사용되는 BIP39 사전의 2048 영어 단어의 전체 및 번호가 매겨진 목록입니다. 이 문서는 한 페이지로 인쇄할 수 있습니다.

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```