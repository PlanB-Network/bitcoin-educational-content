---
name: GitHub Desktop
description: 로컬 작업 환경을 설정하는 방법은 무엇인가요?
---
![github](assets/cover.webp)


PlanB의 사명은 Bitcoin에 대한 최고 수준의 교육 리소스를 가능한 한 많은 언어로 제공하는 것입니다. 사이트에 게시된 모든 콘텐츠는 오픈 소스이며 GitHub에서 호스팅되므로 누구나 플랫폼을 더욱 풍성하게 만드는 데 참여할 수 있습니다. 기여는 기존 텍스트의 수정 및 교정, 다른 언어로 번역, 정보 업데이트, 아직 사이트에 없는 새로운 튜토리얼 제작 등 다양한 형태로 이루어질 수 있습니다.


PlanB 네트워크에 기여하고 싶으시다면 GitHub를 사용하여 변경 사항을 제안해야 합니다. 이를 위해 두 가지 옵션이 있습니다:


- GitHub의 웹 Interface**을 통해 직접 기여하세요: 가장 간단한 방법입니다. 초보자이거나 몇 가지 작은 기여만 할 계획이라면 이 옵션이 가장 적합할 것입니다;
- Git**을 사용하여 로컬에서 기여하기: 이 방법은 PlanB 네트워크에 정기적으로 또는 상당한 규모의 기여를 계획하는 경우에 더 적합합니다. 컴퓨터에서 로컬 Git 환경을 설정하는 것이 처음에는 복잡해 보일 수 있지만, 장기적으로는 이 방법이 더 효율적입니다. 변경 사항을 보다 유연하게 관리할 수 있습니다. 이 튜토리얼에서 환경 설정의 전체 과정을 설명해드리니 걱정하지 마세요** (명령줄을 입력할 필요가 없습니다 ^^).


GitHub가 무엇인지 잘 모르거나 Git 및 GitHub와 관련된 기술 용어에 대해 자세히 알고 싶다면 소개 글을 읽고 이러한 개념을 익히는 것이 좋습니다.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c




- 시작하려면 당연히 GitHub 계정이 필요합니다. 이미 계정이 있는 경우 로그인하면 되고, 그렇지 않은 경우 튜토리얼을 사용하여 새 계정을 만들 수 있습니다.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



## 1단계: GitHub 데스크톱 설치



- Https://desktop.github.com/ 으로 이동하여 GitHub 데스크톱 소프트웨어를 다운로드하세요. 이 소프트웨어를 사용하면 터미널을 사용하지 않고도 GitHub와 쉽게 상호작용할 수 있습니다:

![github-desktop](assets/1.webp)


- 소프트웨어를 처음 실행하면 GitHub 계정을 연결하라는 메시지가 표시됩니다. 이렇게 하려면 'GitHub.com에 로그인'을 클릭합니다:

![github-desktop](assets/2.webp)


- 브라우저에 인증 페이지가 열립니다. 계정 생성 시 선택한 이메일 Address와 비밀번호를 입력한 후 '로그인' 버튼을 클릭합니다:

![github-desktop](assets/3.webp)


- '데스크톱 인증'을 클릭하여 계정과 소프트웨어 간의 연결을 확인합니다:

![github-desktop](assets/4.webp)


- GitHub 데스크톱 소프트웨어로 자동 리디렉션됩니다. '마침'을 클릭합니다: ![github-desktop](assets/5.webp)
- 방금 GitHub 계정을 만든 경우 아직 리포지토리를 만들지 않았다는 페이지로 리디렉션됩니다. 이 시점에서 GitHub 데스크톱 소프트웨어는 따로 보관해 두세요. 나중에 다시 살펴보겠습니다: ![github-desktop](assets/6.webp)


## 2단계: 옵시디언 설치


글쓰기 소프트웨어 설치로 넘어가겠습니다. 여기에는 몇 가지 옵션이 있습니다. PlanB Network는 리포지토리의 텍스트 파일에 이 형식을 사용하므로 마크다운 파일 편집을 지원하는 소프트웨어가 필요합니다.


글쓰기를 위해 특별히 설계된 Typora와 같이 마크다운 파일 편집에 특화된 소프트웨어가 많이 있습니다. 이상적이지는 않지만 Visual Studio Code(VSC) 또는 Sublime Text와 같은 코드 편집기를 선택할 수도 있습니다. 하지만 저는 글을 쓰는 사람으로서 옵시디언 소프트웨어를 선호합니다. 설치 및 시작 방법을 함께 살펴 보겠습니다.



- Https://obsidian.md/download 로 이동하여 소프트웨어를 다운로드하세요: ![github-desktop](assets/7.webp)
- 옵시디언을 설치하고, 소프트웨어를 실행하고, 언어를 선택한 다음 '빠른 시작'을 클릭합니다: ![github-desktop](assets/8.webp)
- 옵시디언 소프트웨어에 도착합니다. 현재 열려 있는 파일은 없습니다: ![github-desktop](assets/9.webp)


## 3단계: PlanB 네트워크 리포지토리 Fork



- 다음 Address의 PlanB 네트워크 데이터 저장소로 이동하세요: [https://github.com/PlanB-Network/Bitcoin-educational-content](https://github.com/PlanB-Network/Bitcoin-educational-content): ![github-desktop](assets/10.webp)
- 이 페이지에서 창 오른쪽 상단의 `Fork` 버튼을 클릭합니다: ![github-desktop](assets/11.webp)
- 생성 메뉴에서 기본 설정을 그대로 둘 수 있습니다. 개발 브랜치만 복사` 상자가 선택되어 있는지 확인한 다음 `Fork 생성` 버튼을 클릭합니다: ![github-desktop](assets/12.webp)
- 그러면 플랜B 네트워크 리포지토리의 Fork에 도달하게 됩니다: ![github-desktop](assets/13.webp)

이 Fork는 현재 동일한 데이터를 포함하고 있지만 원본 리포지토리와는 별도의 리포지토리를 구성합니다. 이제 이 새 리포지토리에서 작업하게 됩니다.


어떤 의미에서 우리는 PlanB 네트워크 소스 저장소의 복사본을 만들었습니다. 이제 Fork(사본)과 원본 리포지토리는 서로 독립적으로 발전할 것입니다. 원본 리포지토리에서는 다른 기여자가 새로운 데이터를 추가할 수 있고, Fork에서는 사용자가 직접 수정을 진행할 수 있습니다.

이 두 리포지토리 간의 일관성을 유지하려면 동일한 정보를 검색할 수 있도록 주기적으로 동기화해야 합니다. 소스 리포지토리로 변경 사항을 보내려면 **풀 리퀘스트**라는 것을 사용합니다. 그리고 소스 리포지토리의 변경 사항을 Fork에 통합하려면 GitHub 웹 Interface에서 **Sync Fork** 명령을 사용합니다.

![github-desktop](assets/14.webp)


## 4단계: Fork 복제



- GitHub 데스크톱 소프트웨어로 돌아갑니다. 이제 Fork가 '내 리포지토리' 섹션에 표시되어야 합니다. 바로 보이지 않는다면 이중 화살표 버튼을 사용하여 목록을 새로 고치세요. Fork가 나타나면 클릭하여 선택하세요:

![github-desktop](assets/15.webp)


- 그런 다음 파란색 버튼을 클릭합니다: '[사용자 이름]/Bitcoin-교육용 콘텐츠 복제'를 클릭합니다:

![github-desktop](assets/16.webp)


- 기본 경로를 그대로 유지합니다. 확인하려면 파란색 '복제' 버튼을 클릭합니다:

![github-desktop](assets/17.webp)


- GitHub Desktop이 Fork을 로컬로 복제하는 동안 기다리세요:

![github-desktop](assets/18.webp)


- 리포지토리를 복제한 후 소프트웨어는 두 가지 옵션을 제공합니다. 첫 번째 옵션인 '상위 프로젝트에 기여하기'를 선택해야 합니다. 이 옵션을 선택하면 향후 작업을 개인 Fork(`[사용자명]/Bitcoin-교육용 콘텐츠`)의 수정이 아닌 상위 프로젝트(`PlanB-Network/Bitcoin-교육용 콘텐츠`)에 대한 기여로 제시할 수 있습니다. 옵션을 선택한 후 `계속`을 클릭합니다:

![github-desktop](assets/19.webp)


- 이제 GitHub 데스크톱이 올바르게 구성되었습니다. 이제 소프트웨어를 백그라운드에서 열어두고 수정 사항을 따라가셔도 됩니다.

![github-desktop](assets/20.webp)

이 단계에서 달성한 것은 GitHub에서 호스팅되는 로컬 리포지토리 사본을 생성한 것입니다. 이 리포지토리는 플랜비 네트워크의 소스 리포지토리의 Fork 버전입니다. 튜토리얼 추가, 번역 또는 수정 등 이 로컬 복사본을 수정할 수 있습니다. 이러한 수정이 완료되면 **Push origin** 명령을 사용하여 로컬 수정 사항을 GitHub에 호스팅된 Fork로 전송합니다.


예를 들어 PlanB 네트워크 리포지토리와 동기화하는 동안 Fork에서 수정 사항을 검색할 수도 있습니다. 이를 위해 **Fetch origin** 명령을 사용하여 로컬 복사본(클론)에 수정 사항을 다운로드한 다음 **Pull origin** 명령을 사용하여 작업과 병합하면 됩니다. 이렇게 하면 효과적으로 기여하면서 프로젝트의 최신 개발 상황을 최신 상태로 유지할 수 있습니다.


![github-desktop](assets/21.webp)

## 5단계: 새 옵시디언 볼트 만들기



- Obsidian 소프트웨어를 열고 창 왼쪽 하단의 작은 보관함 아이콘을 클릭합니다:

![github-desktop](assets/22.webp)


- '열기' 버튼을 클릭하여 기존 폴더를 볼트로 엽니다: ![github-desktop](assets/23.webp)
- 파일 탐색기가 열립니다. 파일 중 '문서' 디렉토리에 있는 'GitHub'라는 폴더를 찾아서 선택해야 합니다. 이 경로는 4단계에서 설정한 경로와 일치합니다. 폴더를 선택한 후 선택을 확인합니다. 그러면 옵시디언에서 볼트 생성이 소프트웨어의 새 페이지에서 시작됩니다:


![github-desktop](assets/24.webp)

-> **주의**에 따르면, Obsidian에서 새 볼트를 만들 때 `Bitcoin-educational-content` 폴더를 선택하지 않는 것이 중요합니다. 대신 상위 폴더인 `GitHub`를 선택하세요. Bitcoin-educational-content` 폴더를 선택하면 로컬 Obsidian 설정이 포함된 구성 폴더 `.obsidian`이 자동으로 리포지토리에 통합됩니다. 옵시디언 구성을 PlanB 네트워크 리포지토리로 전송할 필요가 없으므로 이를 피하고 싶습니다. 다른 방법은 '.gitignore` 파일에 '.obsidian` 폴더를 추가하는 것이지만 이 방법은 소스 리포지토리의 '.gitignore` 파일도 수정하게 되므로 바람직하지 않습니다.



- 창 왼쪽에서 로컬로 복제된 여러 GitHub 리포지토리가 있는 파일 트리를 볼 수 있습니다.
- 폴더 이름 옆의 화살표를 클릭하면 해당 폴더를 확장하여 리포지토리의 하위 폴더 및 해당 문서에 액세스할 수 있습니다:

![github-desktop](assets/25.webp)


- 옵시디언을 다크 모드로 설정하는 것을 잊지 마세요: "빛은 벌레를 끌어당긴다" ;)


## 6단계: 코드 편집기 설치


대부분의 수정 작업은 마크다운 형식('.md')의 파일에 이루어집니다. 이러한 문서를 편집하려면 앞서 설명한 소프트웨어인 옵시디언을 사용할 수 있습니다. 그러나 PlanB Network는 다른 파일 형식을 사용하므로 일부 파일 형식을 수정해야 합니다.


예를 들어 새 튜토리얼을 생성할 때 튜토리얼의 태그, 제목 및 교사 ID를 입력하기 위해 YAML('`.yml`) 파일을 생성해야 합니다. Obsidian에서는 이러한 유형의 파일을 수정할 수 있는 기능을 제공하지 않으므로 코드 편집기가 필요합니다.


이를 위해 몇 가지 옵션을 사용할 수 있습니다. 컴퓨터의 표준 메모장을 이러한 수정에 사용할 수 있지만, 이 솔루션은 깔끔한 작업에는 적합하지 않습니다. VS Code](https://code.visualstudio.com/download) 또는 [Sublime Text](https://www.sublimetext.com/download)와 같이 이 목적을 위해 특별히 설계된 소프트웨어를 선택하는 것이 좋습니다. 특히 서브라임 텍스트는 가볍기 때문에 우리의 필요에 충분할 것입니다.


- 다음 소프트웨어 프로그램 중 하나를 설치하여 나중에 수정할 수 있도록 따로 보관하세요. ![github-desktop](assets/26.webp)

축하합니다! 이제 플랜비 네트워크에 기여할 수 있는 작업 환경이 준비되었습니다. 이제 각 기여 유형(번역, 교정, 글쓰기)에 대한 다른 구체적인 튜토리얼을 살펴볼 수 있습니다.


https://planb.network/tutorials/others

..).