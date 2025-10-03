---
name: 기여 - Git 튜토리얼(고급)
description: 고급 사용자를 위한 Git을 사용한 Plan ₿ Network 튜토리얼 제공 가이드
---
![cover](assets/cover.webp)


새 튜토리얼 추가에 대한 이 튜토리얼을 따라하기 전에 몇 가지 사전 단계를 완료해야 합니다. 아직 완료하지 않았다면 이 소개 튜토리얼을 먼저 살펴본 다음 여기로 돌아와 주세요:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

이미 가지고 계십니다:



- 튜토리얼의 테마를 선택합니다;
- 텔레그램 그룹](https://t.me/PlanBNetwork_ContentBuilder) 또는 paolo@planb.network 을 통해 Plan ₿ Network 팀에 문의하세요;
- 기여 도구를 선택하세요.


이 튜토리얼에서는 숙련된 Git 사용자를 위해 새로운 Plan ₿ Network 튜토리얼을 제공하기 위한 핵심 단계와 필수 지침을 간략하게 요약해 드립니다. Git 및 GitHub에 익숙하지 않다면 단계별로 안내하는 다른 두 개의 자세한 튜토리얼 중 하나를 따르는 것이 좋습니다:



- 중급(GitHub 데스크톱):


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- 초보자(웹 Interface):


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## 추천 도구


마크다운 파일 편집용:



- 옵시디언(무료, 오픈소스 아님)
- 마크 텍스트(무료, 오픈 소스)
- Zettlr(무료, 오픈 소스)
- Typora (유료, ~€15, 오픈소스 아님)


Git의 경우:



- Git(무료, 오픈소스)
- GitHub 데스크톱(무료, 오픈소스)
- 소스트리(무료, 오픈소스 아님)


YAML 파일 편집용:



- Visual Studio 코드(무료, 오픈 소스)
- 숭고한 텍스트(제한이 있는 무료, 오픈 소스 아님)


다이어그램과 시각 자료를 만들려면



- Canva(유료 옵션은 무료, 오픈소스는 아님)
- Inkscape(무료, 오픈 소스)
- 펜팟(무료, 오픈 소스)


## 워크플로


### 1 - 로컬 환경 구성



- GitHub의 Fork 리포지토리(https://github.com/PlanB-Network/Bitcoin-educational-content)의 Plan ₿ Network가 있어야 합니다.
- Fork의 메인 브랜치(`개발`)를 소스 리포지토리와 동기화합니다.
- 로컬 클론을 업데이트합니다.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - 새 브랜치 만들기



- 개발' 브랜치에 있는지 확인하세요.
- 설명이 포함된 이름(예: `tuto-Green-Wallet-loic`)으로 새 브랜치를 만듭니다.
- 이 브랜치를 온라인 Fork에 게시하세요.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - 튜토리얼 문서 추가


***참고: *** [내 Python GUI 스크립트](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation)를 사용하여 3단계와 4단계를 자동화할 수 있습니다. 로컬 클론의 해당 폴더에서 직접 실행한 다음 GUI의 필수 입력란을 채우세요. 설치 및 사용 방법에 대한 자세한 내용은 [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md)를 참조하세요.


수동으로 수행하려면 다음 단계를 따르세요:



- 로컬 저장소에서 해당 폴더를 찾습니다(예: `tutorials/Wallet`).
- 튜토리얼 전용 디렉터리를 명확한 이름(예: `Green-Wallet`)으로 만듭니다. 이 폴더 이름은 튜토리얼의 URL 경로도 결정합니다. 소문자로 작성해야 하며 하이픈을 제외한 특수 문자와 공백이 없어야 합니다.
- 이 디렉터리에 다음 항목을 추가합니다:
    - '자산'이라는 이름의 하위 폴더가 들어 있습니다:
        - 두 개의 '.webp' 이미지:
            - `logo.webp`: 튜토리얼 로고(배경이 있는 정사각형 형식)입니다. 이 로고는 제시된 소프트웨어 또는 도구를 나타내야 합니다. 튜토리얼이 특정 도구에 국한되지 않는 경우(예: Mnemonic 문구 생성에 대한 일반 가이드) 적절한 시각적 요소(예: 일반 아이콘)를 선택할 수 있습니다.
            - `cover.webp`: 튜토리얼 시작 시 표시되는 표지 이미지입니다.
        - 튜토리얼의 원래 언어 코드가 있는 하위 폴더입니다. 예를 들어 튜토리얼이 영어로 작성된 경우 이 하위 폴더의 이름은 `en'이어야 합니다. 튜토리얼의 모든 시각 자료(다이어그램, 이미지, 스크린샷 등)를 이 폴더에 넣습니다.
    - 메타데이터(작성자, 태그, 카테고리, 난이도 등)가 포함된 `tutorial.yml` 파일입니다.
    - 튜토리얼이 포함된 마크다운 파일로, 언어 코드에 따라 이름이 지정됩니다(예: `fr.md`, `en.md` 등).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - YAML 파일 채우기



- 다음과 같이 `tutorial.yml` 파일을 작성합니다:


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



- id**: 튜토리얼을 고유하게 식별하는 UUID(_유니버설 고유 식별자_)입니다. 온라인 도구](https://www.uuidgenerator.net/version4)를 사용하여 generate할 수 있습니다. 유일한 요구 사항은 플랫폼의 다른 UUID와의 충돌을 피하기 위해 이 UUID가 무작위여야 한다는 것입니다;



- project_id**: 프로젝트 목록에서](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) 튜토리얼에 제시된 도구의 배후에 있는 회사 또는 조직의 UUID입니다. 예를 들어 Green Wallet 소프트웨어에 대한 튜토리얼을 만드는 경우 다음 파일에서 이 `project_id`를 찾을 수 있습니다: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. 이 정보는 Plan ₿ Network에서 Bitcoin 또는 관련 프로젝트를 운영하는 모든 회사 및 조직의 데이터베이스를 유지 관리하기 때문에 튜토리얼의 YAML 파일에 추가됩니다. 튜토리얼에 연결된 엔티티의 `project_id`를 추가하면 두 Elements 사이에 링크가 생성됩니다;



- 태그**: 튜토리얼 콘텐츠와 관련된 관련 키워드 2개 또는 3개, [Plan ₿ Network 태그 목록에서] 독점적으로 선택(https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- 카테고리**: Plan ₿ Network 웹사이트 구조에 따라 튜토리얼 콘텐츠에 해당하는 하위 카테고리(예: 지갑의 경우 `데스크톱`, `하드웨어`, `모바일`, `백업`);



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


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

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


### 5 - 콘텐츠 작성



- 마크다운 파일 속성을 작성합니다:
    - 제목(`이름`).
    - 간단한 설명(`설명`).
- 마크다운 구문을 사용하여 튜토리얼 상단에 표지 이미지를 추가합니다("Green"을 표시된 도구 이름으로 바꿉니다):


```
![cover-green](assets/cover.webp)
```



- 마크다운으로 튜토리얼 콘텐츠를 작성합니다:
    - 잘 구조화된 제목(`##`), 목록 및 단락을 사용하세요.
    - 마크다운 구문을 사용하여 시각적 요소를 삽입합니다:


```
![nom-image](assets/en/001.webp)
```




- 해당 언어 하위 폴더의 `/assets`에 다이어그램과 이미지를 배치합니다.


### 6 - 튜토리얼 저장 및 제출



- 설명 메시지와 함께 커밋을 생성하여 변경 사항을 로컬에 저장하세요.
- 변경 사항을 GitHub Fork에 푸시합니다.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- 완료되면 GitHub에서 풀 리퀘스트(PR)를 생성하여 수정 사항의 통합을 제안합니다.
- PR에 제목과 간단한 설명을 추가합니다. 댓글에 해당 이슈 번호를 언급합니다.


### 7 - 교정 및 병합



- 관리자의 확인 또는 피드백을 기다립니다.
- 필요한 경우 수정하고 새 커밋을 푸시합니다.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- PR이 병합되면 작업 중인 브랜치를 삭제할 수 있습니다.


## 콘텐츠 제작 표준



- 플랫폼에서 서식 지정이 지원됩니다**:
    - 클래식 마크다운: 목록, 링크, 이미지, 따옴표, 굵게, 이탤릭체 등
    - LaTeX(인라인이 아닌 블록 전용): `$$`로 구분합니다.
    - 인라인 코드: 단일 백틱이 있는 구문.
    - 코드 블록: 예를 들어 백틱이 3개인 구문입니다:


```
print("Hello, Bitcoin!")
```



- 일러스트레이션 및 다이어그램**:
    - 모든 이미지는 WebP 형식이어야 합니다. 필요한 경우 이 무료 도구를 사용하여 변환하세요: [이미지 변환기](https://github.com/LoicPandul/ImagesConverter).
    - 비주얼의 이름은 2자리 또는 3자리 숫자로 지정합니다(예: `001.webp`, `002.webp`).
    - 모바일 또는 Hardware Wallet 튜토리얼의 경우 모형을 사용합니다.
    - 자체 제작하거나 로열티가 없는 비주얼만 사용하세요.
    - 관련성이 높고 품질이 우수한지 확인하세요.
- 그래픽 헌장**:
    - 글꼴: [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - 색상 Plan ₿ Network:
        - 주황색: `#FF5C00`
        - 검정: `#000000`
        - 흰색: `#FFFFFF`


튜토리얼을 제출하는 데 기술적인 문제가 있는 경우, [기고 전용 텔레그램 그룹](https://t.me/PlanBNetwork_ContentBuilder)에서 언제든지 도움을 요청해 주세요. 대단히 감사합니다!