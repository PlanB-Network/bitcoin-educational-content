---
name: 기여 - GitHub 데스크톱 튜토리얼(중급)
description: GitHub Desktop을 사용하여 Plan ₿ Network에 대한 튜토리얼을 제안하는 전체 가이드
---
![cover](assets/cover.webp)


새 튜토리얼 추가에 대한 이 튜토리얼을 따라하기 전에 몇 가지 사전 단계를 완료해야 합니다. 아직 완료하지 않았다면 먼저 이 소개 튜토리얼을 참조한 다음 여기로 돌아와 주시기 바랍니다:


https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

이미 하셨습니다:


- 튜토리얼의 테마를 선택합니다;
- 텔레그램 그룹](https://t.me/PlanBNetwork_ContentBuilder) 또는 paolo@planb.network 을 통해 Plan ₿ Academy 팀에 문의하세요;
- 기여 도구를 선택했습니다.


이 튜토리얼에서는 GitHub 데스크톱으로 로컬 환경을 설정하여 Plan ₿ Network에 튜토리얼을 추가하는 방법을 살펴봅니다. 이미 Git에 능숙하다면 이 매우 상세한 튜토리얼이 필요하지 않을 수도 있습니다. 자세한 단계별 안내 없이 주요 가이드라인만 제시하는 다른 튜토리얼을 참조하는 것이 좋습니다:



- 숙련된 사용자**:


https://planb.academy/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

로컬 환경을 설정하고 싶지 않다면 초보자를 위해 설계된 다른 튜토리얼을 따라 GitHub의 웹 Interface을 통해 직접 변경하세요:



- 초보자(웹 Interface)**:


https://planb.academy/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## 전제 조건


이 튜토리얼을 따르는 데 필요한 소프트웨어입니다:



- [깃허브 데스크톱](https://desktop.github.com/);
- 옵시디언](https://obsidian.md/)과 같은 마크다운 파일 편집기;
- 코드 편집기([VSC](https://code.visualstudio.com/) 또는 [숭고한 텍스트](https://www.sublimetext.com/)).


![TUTO](assets/fr/01.webp)


튜토리얼을 시작하기 전에 필요한 전제 조건입니다:



- GitHub 계정](https://github.com/signup)이 있어야 합니다;
- Plan ₿ Academy 소스 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content)의 Fork이 있어야 합니다;
- Plan ₿ Network에 [교수 프로필](https://planb.academy/professors)이 있어야 합니다(전체 튜토리얼을 제안하는 경우에만 해당).


이러한 필수 요건을 충족하는 데 도움이 필요하다면 다른 튜토리얼을 참조하세요:



모든 것이 준비되고 로컬 환경이 Plan ₿ Network의 Fork으로 올바르게 설정되면 튜토리얼 추가를 시작할 수 있습니다.


## 1 - 새 브랜치 만들기


브라우저를 열고 Plan ₿ Academy 리포지토리의 Fork 페이지로 이동합니다. 이것이 GitHub에서 설정한 Fork입니다. Fork의 URL은 다음과 같아야 합니다: 'https://github.com/[사용자 아이디]/Bitcoin-educational-content`:


![TUTO](assets/fr/03.webp)


메인 브랜치 'dev'에 있는지 확인한 다음 'Fork 동기화' 버튼을 클릭합니다. Fork가 최신 버전이 아닌 경우 GitHub에서 브랜치 업데이트를 제안합니다. 이 업데이트를 진행하세요. 반대로 브랜치가 이미 최신 상태인 경우 GitHub에서 알려줍니다:


![TUTO](assets/fr/04.webp)


GitHub 데스크톱 소프트웨어를 열고 창의 왼쪽 상단 모서리에서 Fork가 올바르게 선택되었는지 확인합니다:


![TUTO](assets/fr/05.webp)


'원본 가져오기' 버튼을 클릭합니다. 로컬 리포지토리가 이미 최신 상태인 경우 GitHub Desktop은 추가 작업을 제안하지 않습니다. 그렇지 않으면 `원점 가져오기` 옵션이 나타납니다. 이 버튼을 클릭하여 로컬 리포지토리를 업데이트하세요:


![TUTO](assets/fr/06.webp)


실제로 메인 브랜치 `dev`에 있는지 확인합니다:


![TUTO](assets/fr/07.webp)


이 지점을 클릭한 다음 '새 지점' 버튼을 클릭합니다:


![TUTO](assets/fr/08.webp)


새 브랜치가 소스 리포지토리, 즉 `Plan ₿ Academy/Bitcoin-educational-content`를 기반으로 하는지 확인하세요.


대시를 사용하여 각 단어를 구분하여 제목의 목적을 명확하게 알 수 있도록 브랜치 이름을 정합니다. 예를 들어 Sparrow wallet 소프트웨어 사용에 대한 튜토리얼을 작성하는 것이 목표라고 가정해 봅시다. 이 경우 이 튜토리얼을 작성하기 위한 작업 브랜치의 이름은 `tuto-Sparrow-Wallet-loic`으로 지정할 수 있습니다. 적절한 이름을 입력한 후 '브랜치 생성'을 클릭하여 브랜치 생성을 확인합니다:


![TUTO](assets/fr/09.webp)


이제 '브랜치 게시' 버튼을 클릭하여 새 작업 브랜치를 GitHub의 온라인 Fork에 저장합니다:

![TUTORIAL](assets/fr/10.webp)

이제 GitHub 데스크톱에서 새 브랜치를 찾을 수 있습니다. 즉, 컴퓨터에서 로컬로 변경한 모든 내용은 이 특정 브랜치에만 저장됩니다. 또한 이 브랜치가 GitHub Desktop에서 선택된 상태로 유지되는 한, 컴퓨터에서 로컬로 표시되는 파일은 메인 브랜치(`dev`)가 아닌 이 브랜치(`tuto-Sparrow-Wallet-loic`)의 파일에 해당합니다.


![TUTORIAL](assets/fr/11.webp)


게시하려는 각 새 문서에 대해 `dev`에서 새 브랜치를 만들어야 합니다. Git의 브랜치는 프로젝트의 병렬 버전으로, 작업을 병합할 준비가 될 때까지 메인 브랜치에 영향을 주지 않고 변경할 수 있습니다.


## 2 - 튜토리얼 파일 추가하기


이제 작업 브랜치가 만들어졌으니 새 튜토리얼을 통합할 차례입니다. 두 가지 옵션이 있습니다. 필요한 문서 생성을 자동화하는 Python 스크립트를 사용하거나 각 파일을 수동으로 만드는 것입니다. 각 옵션에 대해 따라야 할 단계를 살펴보겠습니다.


### 파이썬 스크립트 사용


컴퓨터에 설치해야 합니다:


- Python 3.8 이상.


스크립트를 사용하려면 스크립트가 저장된 폴더로 이동합니다. 스크립트는 Plan ₿ Academy 데이터 리포지토리의 경로에 있습니다: 'Bitcoin-교육용 콘텐츠/스크립트/튜토리얼 관련/데이터 크리에이터'에 있습니다.


폴더에 들어가면 종속성을 설치합니다:


```
pip install -r requirements.txt
```


그런 다음 다음 명령을 사용하여 소프트웨어를 실행합니다:


```
python3 main.py
```


그래픽 사용자 Interface(GUI)가 열립니다. 처음 사용할 때는 필요한 모든 정보를 입력해야 하지만 이후 사용 시에는 스크립트가 개인 정보를 기억하므로 다시 입력할 필요가 없습니다.


![DATA-CREATOR-PY](assets/fr/37.webp)


먼저 복제된 리포지토리에 있는 `/tutorials` 폴더의 로컬 경로(`.../Bitcoin-educational-content/tutorials/`)를 입력합니다. 직접 입력하거나 '찾아보기' 버튼을 클릭하여 파일 탐색기를 사용하여 탐색할 수 있습니다.


![DATA-CREATOR-PY](assets/fr/38.webp)


튜토리얼을 작성할 언어를 선택합니다.


![DATA-CREATOR-PY](assets/fr/39.webp)


"기여자의 GitHub ID" 필드에 GitHub 사용자명을 입력합니다.


![DATA-CREATOR-PY](assets/fr/40.webp)


다음으로 교수자 프로필을 작성해야 합니다. 몇 가지 옵션을 사용할 수 있습니다:


- "교수 이름" 필드에 이름 첫 글자를 입력합니다. 그러면 아래의 "교수 제안" 드롭다운 목록에 이름이 표시됩니다. 클릭하여 선택합니다;
- 또는 '교수 제안' 드롭다운 목록을 직접 클릭하고 교수 이름을 선택할 수도 있습니다.


이 작업을 수행하면 해당 필드에 교수자 UUID가 자동으로 채워집니다.



![DATA-CREATOR-PY](assets/fr/41.webp)


아직 교수자 프로필이 없는 경우 이 튜토리얼을 확인하세요:


https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

그런 다음 '새 튜토리얼' 버튼을 클릭합니다.


![DATA-CREATOR-PY](assets/fr/42.webp)


튜토리얼의 메인 카테고리를 선택합니다. 그런 다음 선택한 기본 카테고리에 따라 관련 하위 카테고리를 선택합니다.


![DATA-CREATOR-PY](assets/fr/43.webp)


튜토리얼의 난이도를 결정합니다.


![DATA-CREATOR-PY](assets/fr/44.webp)


튜토리얼을 위해 특별히 생성된 디렉터리의 이름을 선택합니다. 이 폴더의 이름은 튜토리얼에서 다루는 소프트웨어를 반영해야 하며, 하이픈을 사용하여 단어를 구분해야 합니다. 예를 들어 폴더 이름은 `red-Wallet`로 지정할 수 있습니다:


![DATA-CREATOR-PY](assets/fr/45.webp)


프로젝트_id`는 튜토리얼에서 다루는 도구를 만든 회사 또는 조직의 UUID로, [프로젝트 목록](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects)에서 확인할 수 있습니다. 예를 들어 Sparrow wallet에 대한 튜토리얼의 경우 파일에서 `project_id`를 찾을 수 있습니다: `Bitcoin-educational-content/resources/projects/Sparrow/project.yml`입니다. 이 정보가 튜토리얼의 YAML 파일에 추가되는 이유는 Plan ₿ Network에서 Bitcoin 또는 관련 프로젝트에서 활동하는 회사 및 조직의 데이터베이스를 관리하기 때문입니다. 연결된 `project_id`를 추가하면 콘텐츠를 관련 엔티티에 연결할 수 있습니다.


***업데이트: *** 새 버전의 스크립트에서는 더 이상 `project_id`를 수동으로 입력할 필요가 없습니다. 이름으로 프로젝트를 찾고 해당 `project_id`를 자동으로 검색하는 검색 기능이 추가되었습니다. 검색하려면 '프로젝트 이름' 필드에 프로젝트 이름의 앞부분을 입력한 후 드롭다운 메뉴에서 원하는 회사를 선택하세요. 아래 필드에 `project_id`가 자동으로 채워집니다. 필요한 경우 수동으로 입력할 수도 있습니다.


![DATA-CREATOR-PY](assets/fr/46.webp)


태그의 경우 [Plan ₿ Academy 태그 목록](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md)에서 튜토리얼 콘텐츠와 관련된 관련 키워드를 2개 또는 3개 선택합니다. 이 소프트웨어는 드롭다운 목록을 통한 키워드 검색 기능도 제공합니다.


![DATA-CREATOR-PY](assets/fr/47.webp)


모든 정보를 입력하고 확인했으면 '튜토리얼 만들기'를 클릭하여 튜토리얼 파일 생성을 확인합니다. 그러면 튜토리얼 폴더와 선택한 카테고리의 모든 필요한 파일이 로컬로 generate 생성됩니다.


![DATA-CREATOR-PY](assets/fr/48.webp)


이제 스크립트에서 이미 이러한 작업을 완료했으므로 '내 Python 스크립트 없이'라는 하위 섹션과 3단계인 'YAML 파일 채우기'를 건너뛸 수 있습니다. 4단계로 바로 진행하여 튜토리얼 작성을 시작하세요.


이 Python 스크립트에 대한 자세한 내용은 [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md)에서도 확인할 수 있습니다.


### 파이썬 스크립트 없이


파일 관리자를 열고 리포지토리의 로컬 복제본이 있는 `Bitcoin-educational-content` 폴더로 이동합니다. 일반적으로 `Documents\GitHub\Bitcoin-educational-content`에서 찾을 수 있습니다.


이 디렉토리 내에서 튜토리얼을 배치할 적절한 하위 폴더를 찾아야 합니다. 폴더 구성은 Plan ₿ Academy 웹사이트의 여러 섹션을 반영합니다. 이 예에서는 Sparrow wallet에 대한 튜토리얼을 추가하려고 하므로 다음 경로로 이동해야 합니다: 웹사이트의 `Wallet` 섹션에 해당하는 `Bitcoin-educational-content\tutorials\Wallet`입니다:


![TUTO](assets/fr/12.webp)


Wallet` 폴더 안에 튜토리얼 전용 디렉토리를 새로 만들어야 합니다. 이 폴더의 이름은 튜토리얼에서 다루는 소프트웨어를 연상시킬 수 있어야 하며, 대시로 단어를 연결해야 합니다. 이 예제에서는 폴더의 제목을 `Sparrow-Wallet`로 지정합니다:


![TUTO](assets/fr/13.webp)


튜토리얼 전용의 이 새 하위 폴더에는 여러 개의 Elements을 추가해야 합니다:


- 튜토리얼에 필요한 모든 일러스트를 받을 수 있는 '자산' 폴더를 만듭니다;
- 이 `assets` 폴더 안에 튜토리얼의 원래 언어 코드에 따라 이름을 지정한 하위 폴더를 만들어야 합니다. 예를 들어 튜토리얼이 영어로 작성된 경우 이 하위 폴더의 이름은 `en`이어야 합니다. 튜토리얼의 모든 시각 자료(다이어그램, 이미지, 스크린샷 등)를 여기에 넣습니다.
- 튜토리얼과 관련된 세부 정보를 기록하려면 `tutorial.yml` 파일을 만들어야 합니다;
- 튜토리얼의 실제 콘텐츠를 작성하기 위해 마크다운 형식의 파일을 만들어야 합니다. 이 파일의 제목은 작성 언어 코드에 따라 지정해야 합니다. 예를 들어 프랑스어로 작성된 튜토리얼의 경우 파일 이름은 'fr.md'여야 합니다.


![TUTO](assets/fr/14.webp)


요약하면, 생성할 파일의 계층 구조는 다음과 같습니다:


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```


## 3 - YAML 파일 채우기


다음 템플릿을 복사하여 `tutorial.yml` 파일을 작성합니다:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


필수 입력란은 다음과 같습니다:



- id**: 튜토리얼을 고유하게 식별하는 UUID(_유니버설 고유 식별자_)입니다. 온라인 도구](https://www.uuidgenerator.net/version4)를 사용하여 generate를 생성할 수 있습니다. 유일한 요구 사항은 플랫폼의 다른 UUID와의 충돌을 피하기 위해 이 UUID가 무작위여야 한다는 것입니다;



- project_id**: 프로젝트 목록에서](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) 튜토리얼에 제시된 도구의 배후에 있는 회사 또는 조직의 UUID입니다. 예를 들어 Green Wallet 소프트웨어에 대한 튜토리얼을 만드는 경우 다음 파일에서 이 `project_id`를 찾을 수 있습니다: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. 이 정보는 Plan ₿ Network에서 Bitcoin 또는 관련 프로젝트를 운영하는 모든 회사 및 조직의 데이터베이스를 유지 관리하기 때문에 튜토리얼의 YAML 파일에 추가됩니다. 튜토리얼에 연결된 엔티티의 `project_id`를 추가하면 두 Elements 사이에 링크가 생성됩니다;



- 태그**: 튜토리얼 콘텐츠와 관련된 관련 키워드 2개 또는 3개, [Plan ₿ Academy 태그 목록에서] 독점적으로 선택(https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- 카테고리**: Plan ₿ Academy 웹사이트 구조에 따라 튜토리얼 콘텐츠에 해당하는 하위 카테고리(예: 지갑의 경우 `데스크톱`, `하드웨어`, `모바일`, `백업`);



- 레벨**: 튜토리얼의 난이도(선택): 튜토리얼의 난이도입니다:
    - '초보자'
    - `중급`
    - `고급`
    - `전문가`



- 교수자_ID**: 교수자 프로필](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors)에 표시된 `교수자_id`(UUID)입니다;



- original_language**: 튜토리얼의 원래 언어(예: `fr`, `en` 등);



- 교정**: 교정 과정에 대한 정보입니다. 튜토리얼을 직접 교정하는 것은 첫 번째 검증으로 간주되므로 첫 번째 부분을 완료하세요:
    - 언어**: 교정의 언어 코드(예: `fr`, `en` 등).
    - 마지막_기여_날짜**: 오늘의 날짜입니다.
    - 긴급성**: 1
    - 기여자_이름**: GitHub ID.
    - 보상**: 0


교사 ID에 대한 자세한 내용은 해당 튜토리얼을 참조하세요:


https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


튜토리얼.yml` 파일 수정이 완료되면 `파일 > 저장`을 클릭하여 문서를 저장합니다:


![TUTO](assets/fr/16.webp)


이제 코드 편집기를 닫을 수 있습니다.


## 4 - 마크다운 파일 작성


이제 튜토리얼을 호스팅할 파일(예: `fr.md`와 같은 언어 코드로 명명된 파일)을 열 수 있습니다. 창 왼쪽의 흑요석으로 이동하여 폴더 트리를 스크롤하여 튜토리얼의 폴더와 찾고 있는 파일을 찾습니다:


![TUTO](assets/fr/18.webp)


파일을 클릭하여 엽니다:


![TUTO](assets/fr/19.webp)


문서 상단의 '속성' 섹션을 작성하는 것부터 시작하겠습니다.


![TUTO](assets/fr/20.webp)


다음 코드 블록을 수동으로 추가하고 채웁니다:


```
---
name: [Title]
description: [Description]
---
```


![TUTO](assets/fr/21.webp)


튜토리얼의 이름과 간단한 설명을 입력합니다:


![TUTO](assets/fr/22.webp)


그런 다음 튜토리얼의 시작 부분에 표지 이미지의 경로를 추가합니다. 이렇게 하려면 참고하세요:


```
![cover-sparrow](assets/cover.webp)
```


이 구문은 튜토리얼에 이미지를 추가해야 할 때마다 유용합니다. 느낌표는 이미지임을 나타내며 괄호 사이에 대체 텍스트(alt)를 지정합니다. 이미지 경로는 괄호 사이에 표시됩니다:


![TUTO](assets/fr/23.webp)


## 5 - 로고 및 표지 추가


자산` 폴더 내에 글의 썸네일 역할을 할 `logo.webp`라는 파일을 추가해야 합니다. 이 이미지는 `.webp` 형식이어야 하며 사용자 Interface와 조화를 이루기 위해 정사각형 크기를 준수해야 합니다. 튜토리얼에서 다루는 소프트웨어의 로고나 기타 관련 이미지는 저작권이 없는 경우 자유롭게 선택할 수 있습니다. 또한 같은 위치에 'cover.webp'라는 제목의 이미지도 추가합니다. 이 이미지는 튜토리얼 상단에 표시됩니다. 이 이미지는 로고와 마찬가지로 사용 권한을 준수하고 튜토리얼의 맥락에 적합한지 확인하세요:

## 6 - 튜토리얼 작성 및 시각 자료 추가하기


콘텐츠 초안을 작성하여 튜토리얼을 계속 작성합니다. 자막을 통합하려면 텍스트 앞에 `##`를 붙여 적절한 마크다운 서식을 적용하세요:


![TUTO](assets/fr/24.webp)


'자산' 폴더의 언어 하위 폴더는 튜토리얼과 함께 제공되는 도표와 시각 자료를 저장하는 데 사용됩니다. 전 세계 사람들이 콘텐츠에 액세스할 수 있도록 가급적 이미지에 텍스트를 포함하지 마세요. 물론 소개하는 소프트웨어에는 텍스트가 포함되지만 소프트웨어 스크린샷에 다이어그램이나 추가 표시를 추가하는 경우에는 텍스트 없이 추가하거나 꼭 필요한 경우 영어를 사용하세요.


![TUTO](assets/fr/25.webp)


이미지 이름을 지정하려면 튜토리얼에 표시되는 순서에 해당하는 숫자를 두 자리 형식(이미지가 99개 이상인 경우 세 자리 형식)으로 지정하면 됩니다. 예를 들어 첫 번째 이미지의 이름은 `01.webp`, 두 번째 이미지의 이름은 `02.webp`로 지정합니다.


이미지는 '.webp' 형식만 사용해야 합니다. 필요한 경우 [내 이미지 변환 소프트웨어](https://github.com/LoicPandul/ImagesConverter)를 사용할 수 있습니다.


![TUTO](assets/fr/26.webp)


문서에 다이어그램을 삽입하려면 다음 마크다운 명령을 사용하여 적절한 대체 텍스트와 이미지의 올바른 경로를 지정하세요:


```
![sparrow](assets/fr/01.webp)
```


시작 부분의 느낌표는 이미지임을 나타냅니다. 접근성 및 SEO에 도움이 되는 대체 텍스트는 괄호 사이에 배치됩니다. 마지막으로 괄호 사이에 이미지의 경로가 표시됩니다.


자신만의 다이어그램을 만들려면 시각적 일관성을 보장하기 위해 Plan ₿ Network의 그래픽 헌장을 준수해야 합니다:


- Font**: IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans) 사용;
- 색상**:
 - 오렌지: 주황색: #FF5C00
 - Black: #000000
 - 흰색: 흰색: #FFFFFF


**튜토리얼에 포함된 모든 시각 자료는 저작권이 없거나 소스 파일의 라이선스를 준수해야 합니다**. 또한 Plan ₿ Network에 게시된 모든 다이어그램은 텍스트와 동일한 방식으로 CC-BY-SA 라이선스에 따라 제공됩니다.

**-> 팁: 이미지와 같은 파일을 공개적으로 공유할 때는 불필요한 메타데이터를 제거하는 것이 중요합니다. 여기에는 위치 데이터, 생성 날짜 또는 작성자에 대한 세부 정보와 같은 민감한 정보가 포함될 수 있습니다. 개인정보를 보호하려면 이러한 메타데이터를 삭제하는 것이 좋습니다. 이 과정을 간소화하기 위해 간단한 드래그 앤 드롭으로 문서의 메타데이터를 정리할 수 있는 [Exif Cleaner](https://exifcleaner.com/)와 같은 전문 도구를 사용할 수 있습니다.

## 7 - 튜토리얼 저장 및 제출


원하는 언어로 튜토리얼 작성을 완료했다면 다음 단계는 **풀 요청**을 제출하는 것입니다. 그러면 관리자가 사람이 검토하는 자동 번역 방식을 통해 튜토리얼에 누락된 번역을 추가해 드립니다.


풀 리퀘스트를 진행하려면 GitHub 데스크톱 소프트웨어를 엽니다. 소프트웨어가 원래 리포지토리와 비교하여 브랜치에서 로컬로 변경한 내용을 자동으로 감지합니다. 계속하기 전에 Interface의 왼쪽에서 이러한 변경 사항이 예상한 것과 일치하는지 주의 깊게 확인하세요:


![TUTO](assets/fr/28.webp)


커밋 제목을 추가한 다음 파란색 '[내 브랜치에 커밋]` 버튼을 클릭하여 변경 사항을 확인합니다:


![TUTO](assets/fr/29.webp)


커밋은 설명 메시지와 함께 브랜치에 변경된 내용을 저장하는 것으로, 시간이 지남에 따라 프로젝트의 진화를 추적할 수 있습니다. 일종의 중간 체크포인트입니다.


그런 다음 '푸시 오리진' 버튼을 클릭합니다. 그러면 커밋이 Fork로 전송됩니다:


![TUTO](assets/fr/30.webp)


튜토리얼을 완료하지 못했다면 나중에 다시 돌아와서 새로운 커밋을 할 수 있습니다. 이 브랜치에 대한 변경을 완료했다면 지금 '풀 리퀘스트 미리 보기' 버튼을 클릭하세요:


![TUTO](assets/fr/31.webp)


수정한 내용이 올바른지 다시 한 번 확인한 다음 '풀 리퀘스트 만들기' 버튼을 클릭할 수 있습니다:


![TUTO](assets/fr/32.webp)


풀 리퀘스트는 브랜치에서 Plan ₿ Academy 리포지토리의 메인 브랜치로 변경 사항을 통합하기 위한 요청으로, 변경 사항을 병합하기 전에 검토하고 논의할 수 있습니다.


GitHub의 브라우저에서 풀 리퀘스트의 준비 페이지로 자동 리디렉션됩니다:


![TUTO](assets/fr/33.webp)

소스 리포지토리와 병합하려는 변경 사항을 간략하게 요약하는 제목을 표시합니다. 변경 사항을 설명하는 간단한 코멘트를 추가한 다음(튜토리얼 생성과 관련된 이슈 번호가 있는 경우 '#{이슈 번호}를 닫습니다'라는 코멘트를 잊지 마세요) Green '풀 리퀘스트 만들기' 버튼을 클릭하여 병합 요청을 확인합니다:

![TUTO](assets/fr/34.webp)


그러면 메인 Plan ₿ Academy 리포지토리의 '풀 리퀘스트' 탭에서 PR을 볼 수 있습니다. 관리자가 기여의 병합을 확인하거나 추가 수정을 요청하기 위해 연락이 올 때까지 기다리기만 하면 됩니다.


![TUTO](assets/fr/35.webp)


PR이 메인 브랜치에 병합된 후에는 작업 브랜치(`tuto-Sparrow-Wallet`)를 삭제하여 Fork의 기록을 깨끗하게 유지하는 것이 좋습니다. GitHub는 PR 페이지에서 이 옵션을 자동으로 제공합니다:


![TUTO](assets/fr/36.webp)


GitHub 데스크톱 소프트웨어에서 Fork의 메인 브랜치(`dev`)로 다시 전환할 수 있습니다.


![TUTO](assets/fr/07.webp)


이미 PR을 제출한 후 기여 내용을 변경하려는 경우, 절차는 PR의 현재 상태에 따라 다릅니다:


- PR이 아직 열려 있고 아직 병합되지 않은 경우, 같은 브랜치에 유지하면서 로컬에서 변경을 수행합니다. 수정이 완료되면 `원점 푸시` 버튼을 사용하여 아직 열려 있는 PR에 새 커밋을 추가합니다;
- PR이 이미 메인 브랜치에 병합된 경우 새 브랜치를 만든 다음 새 PR을 제출하여 프로세스를 다시 시작해야 합니다. 계속 진행하기 전에 로컬 리포지토리가 Plan ₿ Academy 소스 리포지토리와 동기화되었는지 확인하세요.


튜토리얼을 제출하는 데 기술적인 문제가 발생하면 언제든지 [기고 전용 텔레그램 그룹](https://t.me/PlanBNetwork_ContentBuilder)에서 도움을 요청하세요. 감사합니다!