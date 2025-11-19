---
name: 기여 - GitHub 웹 튜토리얼(초급)
description: GitHub 웹을 사용한 Plan ₿ Academy 튜토리얼 전체 가이드
---
![cover](assets/cover.webp)


새 튜토리얼 추가에 대한 이 튜토리얼을 따라하기 전에 몇 가지 사전 단계를 완료해야 합니다. 아직 완료하지 않았다면 이 소개 튜토리얼을 먼저 살펴본 다음 여기로 돌아와 주세요:


https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

이미 가지고 계십니다:




- 튜토리얼에 사용할 테마를 선택합니다;
- 텔레그램 그룹](https://t.me/PlanBNetwork_ContentBuilder) 또는 paolo@planb.network 을 통해 Plan ₿ Academy 팀에 문의하세요;
- 기여 도구를 선택하세요.


이 튜토리얼에서는 GitHub의 웹 버전을 사용하여 Plan ₿ Network에 튜토리얼을 추가하는 방법을 살펴봅니다. 이미 Git에 익숙하다면 이 매우 상세한 튜토리얼이 필요하지 않을 수도 있습니다. 대신 따라야 할 가이드라인과 로컬에서 변경하는 단계를 자세히 설명하는 다른 두 개의 튜토리얼 중 하나를 확인하는 것이 좋습니다:




- 숙련된 사용자**:


https://planb.academy/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410


- 중급(GitHub 데스크톱)**:


https://planb.academy/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## 전제 조건


튜토리얼을 시작하기 전에 필요한 전제 조건입니다:




- GitHub 계정](https://github.com/signup)이 있어야 합니다;
- Plan ₿ Academy 소스 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content)의 Fork가 있어야 합니다;
- Plan ₿ Network에 [교사 프로필](https://planb.academy/professors)이 있어야 합니다(전체 튜토리얼을 제공하는 경우에만 해당).


이러한 전제 조건을 충족하는 데 도움이 필요하다면 다른 튜토리얼을 참조하세요:



https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.academy/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

모든 것이 준비되고 Plan ₿ Academy 리포지토리의 Fork이 준비되면 튜토리얼 추가를 시작할 수 있습니다.


## 1 - 새 브랜치 만들기


브라우저를 열고 Plan ₿ Academy 리포지토리의 Fork 페이지로 이동합니다. 이 페이지가 GitHub에서 설정한 Fork입니다. Fork의 URL은 다음과 같아야 합니다: 'https://github.com/[사용자 이름]/Bitcoin-educational-content`:


![GITHUB](assets/fr/01.webp)


메인 `dev` 브랜치에 있는지 확인한 다음 "*Sync Fork*" 버튼을 클릭합니다. Fork가 최신 버전이 아닌 경우 GitHub에서 브랜치를 업데이트하라는 메시지가 표시됩니다. 이 업데이트를 진행하세요:


![GITHUB](assets/fr/02.webp)


'dev' 브랜치를 클릭한 다음, 대시를 사용하여 단어를 구분하여 브랜치 제목에 목적이 명확하게 반영되도록 작업 브랜치 이름을 지정합니다. 예를 들어, Green Wallet 사용에 대한 튜토리얼을 작성하는 것이 목표라면 브랜치 이름을 이렇게 지을 수 있습니다: `tuto-Green-Wallet-loic`. 적절한 이름을 입력한 후 "*브랜치 만들기*"를 클릭하여 `dev`를 기준으로 새 브랜치 생성을 확인합니다:


![GITHUB](assets/fr/03.webp)


이제 새 업무 지점에서 업무를 시작해야 합니다:


![GITHUB](assets/fr/04.webp)


즉, 변경한 내용은 해당 특정 브랜치에만 저장됩니다.


게시하려는 각 새 문서에 대해 `dev`에서 새 브랜치를 만듭니다.


Git의 브랜치는 프로젝트의 병렬 버전을 나타내므로 작업을 통합할 준비가 될 때까지 메인 브랜치에 영향을 주지 않고 수정 작업을 할 수 있습니다.


## 2 - 튜토리얼 파일 추가


이제 작업 브랜치가 생성되었으므로 새 튜토리얼을 통합할 차례입니다.


브랜치 파일 내에서 튜토리얼을 배치할 적절한 하위 폴더를 찾아야 합니다. 폴더의 구성은 Plan ₿ Academy 웹사이트의 여러 섹션을 반영합니다. 이 예에서는 Green Wallet에 튜토리얼을 추가하므로 다음 경로로 이동합니다: 웹사이트의 `Wallet` 섹션에 해당하는 `Bitcoin-educational-content\tutorials\Wallet`입니다:


![GITHUB](assets/fr/05.webp)


Wallet` 폴더에 튜토리얼 전용 디렉토리를 새로 만듭니다. 이 폴더의 이름은 하이픈을 사용하여 단어를 연결하여 튜토리얼에서 다루는 소프트웨어를 명확하게 나타내야 합니다. 이 예제에서는 폴더의 이름을 `Green-Wallet`로 지정합니다. "*파일 추가*"를 클릭한 다음 "*새 파일 만들기*"를 클릭합니다:


![GITHUB](assets/fr/06.webp)


폴더 이름 뒤에 슬래시 `/`를 입력하여 폴더로 생성되었음을 확인합니다.


![GITHUB](assets/fr/07.webp)


튜토리얼 전용의 이 새 하위 폴더에 여러 항목을 추가해야 합니다:




- 튜토리얼에 필요한 모든 일러스트를 보관할 '자산' 폴더를 만듭니다;
- 이 `assets` 폴더 안에 튜토리얼의 원래 언어 코드에 따라 이름을 지정한 하위 폴더를 만듭니다. 예를 들어 튜토리얼이 영어로 작성된 경우 이 하위 폴더의 이름은 `en`이어야 합니다. 튜토리얼의 모든 시각 자료(다이어그램, 이미지, 스크린샷 등)를 이 폴더에 넣습니다.
- 튜토리얼의 세부 정보를 기록하려면 `tutorial.yml` 파일을 만들어야 합니다;
- 튜토리얼의 실제 콘텐츠를 작성하려면 마크다운 파일을 만들어야 합니다. 이 파일은 작성된 언어의 코드에 따라 이름을 지정해야 합니다. 예를 들어 프랑스어로 작성된 튜토리얼의 경우 파일 이름은 `fr.md`여야 합니다.


요약하자면, 파일 계층 구조는 다음과 같습니다(다음 섹션에서 계속 생성하겠습니다):


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```


## 3 - YAML 파일 채우기


YAML 파일부터 시작하겠습니다. 새 파일을 만드는 상자에 `tutorial.yml`을 입력합니다:


![GITHUB](assets/fr/08.webp)


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



- id**: 튜토리얼을 고유하게 식별하는 UUID(_유니버설 고유 식별자_)입니다. 온라인 도구](https://www.uuidgenerator.net/version4)를 사용하여 generate을 생성할 수 있습니다. 유일한 요구 사항은 플랫폼의 다른 UUID와의 충돌을 피하기 위해 이 UUID가 무작위여야 한다는 것입니다;



- project_id**: 프로젝트 목록에서](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) 튜토리얼에 제시된 도구의 배후에 있는 회사 또는 조직의 UUID입니다. 예를 들어 Green Wallet 소프트웨어에 대한 튜토리얼을 만드는 경우 다음 파일에서 이 `project_id`를 찾을 수 있습니다: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. 이 정보는 Plan ₿ Network에서 Bitcoin 또는 관련 프로젝트를 운영하는 모든 회사 및 조직의 데이터베이스를 유지 관리하기 때문에 튜토리얼의 YAML 파일에 추가됩니다. 튜토리얼에 연결된 엔티티의 `project_id`를 추가하면 두 Elements 간의 링크가 생성됩니다;



- 태그**: 튜토리얼 콘텐츠와 관련된 2~3개의 관련 키워드로, [Plan ₿ Academy 태그 목록에서] 독점적으로 선택(https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md)합니다;



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


튜토리얼.yml` 파일 수정을 마치면 "*변경 사항 커밋...*" 버튼을 클릭하여 문서를 저장합니다:


![GITHUB](assets/fr/09.webp)


제목과 설명을 추가하고 이 튜토리얼을 시작할 때 만든 브랜치에 커밋이 되었는지 확인합니다. 그런 다음 "*변경사항 커밋*"을 클릭하여 확인합니다.


![GITHUB](assets/fr/10.webp)


## 4 - 이미지용 하위 폴더 만들기


"*파일 추가*"를 다시 클릭한 다음 "*새 파일 만들기*"를 클릭합니다:


![GITHUB](assets/fr/11.webp)


자산`을 입력한 다음 슬래시 `/`를 입력하여 폴더를 만듭니다:


![GITHUB](assets/fr/12.webp)


자산` 폴더에서 이 단계를 반복하여 언어 하위 폴더(예: 튜토리얼이 프랑스어로 된 경우 `fr`)를 만듭니다:


![GITHUB](assets/fr/13.webp)


이 폴더에 더미 파일을 만들어 GitHub가 폴더를 유지하도록 합니다(그렇지 않으면 비어 있을 것입니다). 이 파일의 이름을 `.gitkeep`으로 지정합니다. 그런 다음 "*변경사항 커밋...*"을 클릭합니다.


![GITHUB](assets/fr/14.webp)


올바른 브랜치에 있는지 다시 확인한 다음 "*변경사항 커밋*"을 클릭합니다.


![GITHUB](assets/fr/15.webp)


## 5 - 마크다운 파일 만들기


이제 튜토리얼을 호스팅할 파일을 만들고 언어 코드에 따라 이름을 지정합니다(예: 프랑스어로 작성하는 경우 `fr.md`). 튜토리얼 폴더로 이동합니다:


![GITHUB](assets/fr/16.webp)


"파일 추가*"를 클릭한 다음 "새 파일 만들기*"를 클릭합니다.


![GITHUB](assets/fr/17.webp)


언어 코드를 사용하여 파일 이름을 지정합니다. 제 경우에는 튜토리얼이 프랑스어로 작성되었으므로 파일 이름을 `fr.md`로 지정했습니다. 확장자 `.md`는 파일이 마크다운 형식임을 나타냅니다.


![GITHUB](assets/fr/18.webp)


문서 상단의 '속성' 섹션을 채우는 것부터 시작합니다. 다음 코드 블록을 수동으로 추가하고 채웁니다(`name:` 및 `description:` 키는 영문으로 유지하되 해당 값은 튜토리얼에 사용되는 언어로 작성해야 합니다):


```
---
name: [Titre]
description: [Description]
---
```


![GITHUB](assets/fr/19.webp)


튜토리얼의 이름과 간단한 설명을 입력합니다:


![GITHUB](assets/fr/20.webp)


그런 다음 튜토리얼의 시작 부분에 표지 이미지에 경로를 추가합니다. 이렇게 하려면 참고하세요:


```
![cover-green](assets/cover.webp)
```


이 구문은 튜토리얼에 이미지를 추가해야 할 때마다 유용하게 사용할 수 있습니다. 느낌표는 대괄호 사이에 대체 텍스트(alt)가 지정되어 있는 이미지를 나타냅니다. 이미지의 경로는 대괄호 사이에 표시됩니다:


![GITHUB](assets/fr/21.webp)


"*변경사항 커밋...*" 버튼을 클릭하여 이 파일을 저장합니다.


![GITHUB](assets/fr/22.webp)


올바른 브랜치에 있는지 확인한 다음 커밋을 확인합니다.


![GITHUB](assets/fr/23.webp)


이제 언어 코드에 따라 튜토리얼 폴더가 다음과 같이 표시되어야 합니다:


![GITHUB](assets/fr/24.webp)


## 6 - 로고 및 표지 추가


Assets` 폴더에 글의 썸네일 역할을 할 `logo.webp`라는 파일을 추가해야 합니다. 이 이미지는 `.webp` 형식이어야 하며 사용자 Interface과 일치하도록 크기가 정사각형이어야 합니다.


튜토리얼에 사용된 소프트웨어 로고나 기타 관련 이미지는 로열티가 없는 한 자유롭게 선택할 수 있습니다. 또한 같은 위치에 'cover.webp'라는 제목의 이미지를 추가합니다. 이 이미지는 튜토리얼 상단에 표시됩니다. 로고와 마찬가지로 이 이미지도 사용 권한을 준수하고 튜토리얼의 맥락에 적합한 이미지인지 확인하세요.


Assets` 폴더에 이미지를 추가하려면 로컬 파일에서 이미지를 끌어다 놓으면 됩니다. Assets` 폴더에 있고 올바른 브랜치에 있는지 확인한 다음 "*변경사항 커밋*"을 클릭합니다.


![GITHUB](assets/fr/26.webp)


이제 폴더에 이미지가 표시되는 것을 볼 수 있습니다.


![GITHUB](assets/fr/27.webp)


## 7 - 튜토리얼 작성하기


마크다운 파일에 언어 코드(제 예에서는 프랑스어로 `fr.md` 파일)와 함께 콘텐츠를 메모하여 튜토리얼을 계속 작성합니다. 파일로 이동하여 연필 아이콘을 클릭합니다:


![GITHUB](assets/fr/28.webp)


튜토리얼 작성을 시작합니다. 자막을 추가할 때는 텍스트 앞에 `##`를 붙여 적절한 마크다운 서식을 사용하세요:


![GITHUB](assets/fr/29.webp)


"*편집*"과 "*미리보기*" 보기를 번갈아 가며 렌더링을 더 잘 시각화할 수 있습니다.


![GITHUB](assets/fr/30.webp)


작업을 저장하려면 "*변경사항 커밋...*"을 클릭하고 올바른 브랜치에 있는지 확인한 다음 "*변경사항 커밋*"을 다시 클릭하여 확인합니다.


![GITHUB](assets/fr/31.webp)


## 8 - 비주얼 추가


자산` 폴더의 언어 하위 폴더(예: `/assets/en`)는 튜토리얼과 함께 제공되는 도표와 시각 자료를 저장하는 데 사용됩니다. 전 세계 사람들이 콘텐츠에 액세스할 수 있도록 가급적 이미지에 텍스트를 포함하지 마세요. 물론 제공되는 소프트웨어에는 텍스트가 포함되지만 소프트웨어 스크린샷에 회로도나 추가 표시를 추가하는 경우에는 텍스트 없이 하거나 꼭 필요한 경우 영문으로 작성하세요.


이미지 이름을 지정하려면 튜토리얼에 표시되는 순서에 해당하는 숫자를 두 자리 형식(이미지가 99개 이상인 경우 세 자리 형식)으로 지정하면 됩니다. 예를 들어 첫 번째 이미지의 이름은 `01.webp`, 두 번째 이미지의 이름은 `02.webp`로 지정합니다.


이미지는 '.webp' 형식이어야 합니다. 필요한 경우 [내 이미지 변환 소프트웨어](https://github.com/LoicPandul/ImagesConverter)를 사용할 수 있습니다.


![GITHUB](assets/fr/32.webp)


이제 하위 폴더에 이미지를 추가했으므로 더미 파일 '.gitkeep'을 삭제할 수 있습니다. 이 파일을 열고 오른쪽 상단에 있는 작은 점 3개를 클릭한 다음 "*파일 삭제*"를 클릭합니다.


![GITHUB](assets/fr/33.webp)


"*변경 사항 커밋...*"을 클릭하여 변경 사항을 저장합니다.


![GITHUB](assets/fr/34.webp)


하위 폴더의 다이어그램을 편집 문서에 삽입하려면 다음 마크다운 명령을 사용하여 해당 언어에 맞는 적절한 대체 텍스트와 올바른 이미지 경로를 지정하세요:


```
![green](assets/fr/01.webp)
```


시작 부분의 느낌표는 이미지를 나타냅니다. 접근성 및 참조에 도움이 되는 대체 텍스트는 대괄호 사이에 배치됩니다. 마지막으로 대괄호 사이에 이미지의 경로가 표시됩니다.


![GITHUB](assets/fr/35.webp)


자신만의 도식을 만들려면 시각적 일관성을 보장하기 위해 Plan ₿ Academy 그래픽 가이드라인을 따르세요:




- Font**: IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans) 사용;
- 색상**:
 - 오렌지: 주황색: #FF5C00
 - Black: #000000
 - 흰색: 흰색: #FFFFFF


**튜토리얼에 포함된 모든 시각 자료는 저작권이 없거나 소스 파일 라이선스를 준수해야 합니다**. 따라서 Plan ₿ Network에 게시된 모든 다이어그램은 텍스트와 동일한 방식으로 CC-BY-SA 라이선스에 따라 제공됩니다.


**-> 팁: 이미지와 같은 파일을 공개적으로 공유할 때는 불필요한 메타데이터를 제거하는 것이 중요합니다. 여기에는 위치 데이터, 생성 날짜, 작성자 세부 정보 등 민감한 정보가 포함될 수 있습니다. 개인정보를 보호하려면 이러한 메타데이터를 제거하는 것이 좋습니다. 간단한 드래그 앤 드롭으로 문서의 메타데이터를 정리할 수 있는 [Exif Cleaner](https://exifcleaner.com/)와 같은 전문 도구를 사용하면 이 작업을 간소화할 수 있습니다.


## 9 - 튜토리얼 제안


원하는 언어로 튜토리얼 작성을 완료했다면 다음 단계는 **풀 요청**을 제출하는 것입니다. 그러면 관리자가 사람의 교정이 포함된 자동 번역 방법을 사용하여 누락된 번역을 튜토리얼에 추가합니다.


풀 리퀘스트를 진행하려면 모든 변경 사항을 저장한 후 "*기여*" 버튼을 클릭한 다음 "*풀 리퀘스트 열기*"를 클릭합니다:


![GITHUB](assets/fr/36.webp)


풀 리퀘스트는 브랜치의 변경 사항을 Plan ₿ Academy 리포지토리의 메인 브랜치에 통합하기 위한 요청으로, 변경 사항이 병합되기 전에 검토하고 논의할 수 있습니다.


계속하기 전에 Interface의 하단에서 이러한 변경 사항이 예상한 것과 일치하는지 주의 깊게 확인하세요:


![GITHUB](assets/fr/37.webp)


Interface의 상단에서 작업 브랜치가 Plan ₿ Academy 리포지토리(메인 브랜치)의 `dev` 브랜치에 병합되었는지 확인하세요.


소스 리포지토리와 병합하려는 변경 사항을 간략하게 요약하는 제목을 입력합니다. 변경 사항을 설명하는 간단한 코멘트를 추가한 다음(튜토리얼 작성과 관련된 이슈 번호가 있는 경우 '#{이슈 번호}를 닫습니다'를 코멘트로 기록하세요) Green "*풀 리퀘스트 만들기*" 버튼을 클릭하여 병합 요청을 확인합니다:


![GITHUB](assets/fr/38.webp)


그러면 메인 Plan ₿ Academy 리포지토리의 "*풀 리퀘스트*" 탭에서 PR을 볼 수 있습니다. 이제 관리자가 연락하여 기여가 병합되었는지 확인하거나 추가 수정을 요청할 때까지 기다리기만 하면 됩니다.


![GITHUB](assets/fr/39.webp)


PR을 메인 브랜치와 병합한 후에는 작업 브랜치(예: `tuto-Green-Wallet`)를 삭제하여 Fork의 기록을 깔끔하게 유지하는 것이 좋습니다. GitHub는 자동으로 PR 페이지에서 이 옵션을 제공합니다:


![GITHUB](assets/fr/40.webp)


이미 PR을 제출한 후 기여 내용을 변경하려는 경우 따라야 할 단계는 PR의 현재 상태에 따라 다릅니다:




- PR이 아직 열려 있고 아직 병합되지 않은 경우 동일한 워크브랜치에서 변경을 수행합니다. 커밋 변경 사항이 아직 열려 있는 PR에 추가됩니다;
- PR이 이미 메인 브랜치에 병합된 경우 새 브랜치를 만든 다음 새 PR을 제출하여 프로세스를 처음부터 다시 수행해야 합니다. 계속 진행하기 전에 Fork가 `dev` 브랜치의 Plan ₿ Academy 소스 리포지토리와 동기화되었는지 확인하세요.


튜토리얼을 제출하는 데 기술적인 문제가 있는 경우, [기고 전용 텔레그램 그룹](https://t.me/PlanBNetwork_ContentBuilder)에서 언제든지 도움을 요청해 주세요. 대단히 감사합니다!