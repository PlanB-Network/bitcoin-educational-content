---
name: PlanB 네트워크에 이벤트 추가
description: 플랜비 네트워크에 새 이벤트를 추가하려면 어떻게 해야 하나요?
---
![event](assets/cover.webp)


PlanB의 사명은 Bitcoin에 대한 최고 수준의 교육 리소스를 가능한 한 많은 언어로 제공하는 것입니다. 이 사이트에 게시된 모든 콘텐츠는 오픈 소스이며 GitHub에서 호스팅되어 누구나 플랫폼 강화에 기여할 수 있는 기회를 제공합니다.


플랜비 네트워크 사이트에 Bitcoin 컨퍼런스를 추가하고 이벤트의 가시성을 높이고 싶지만 방법을 모르시나요? 이 튜토리얼은 여러분을 위한 것입니다!

![event](assets/01.webp)


- 먼저 GitHub에 계정이 있어야 합니다. 계정을 만드는 방법을 모르는 경우 자세한 튜토리얼을 만들어 안내해 드립니다.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 리소스/회의/` 섹션의 [데이터 전용 PlanB의 GitHub 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference)로 이동합니다:

![event](assets/02.webp)


- 오른쪽 상단의 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![event](assets/03.webp)


- 플랜비 네트워크의 콘텐츠에 기여한 적이 없는 경우, 원본 리포지토리의 Fork를 만들어야 합니다. 리포지토리를 포크한다는 것은 자신의 GitHub 계정에 해당 리포지토리의 복사본을 생성하여 원본 리포지토리에 영향을 주지 않고 프로젝트 작업을 할 수 있도록 하는 것을 의미합니다. '이 리포지토리 Fork' 버튼을 클릭합니다:

![event](assets/04.webp)


- 그러면 GitHub 편집 페이지로 이동합니다:

![event](assets/05.webp)


- 회의를 위한 폴더를 만듭니다. 이렇게 하려면 '파일 이름...` 상자에 공백 대신 대시를 사용하여 소문자로 회의 이름을 입력합니다. 예를 들어, 컨퍼런스의 이름이 '파리 Bitcoin 컨퍼런스'인 경우 '파리-Bitcoin-conference'라고 적어야 합니다. 또한 회의의 연도를 추가합니다(예: `paris-Bitcoin-conference-2024`):

![event](assets/06.webp)


- 폴더 생성을 확인하려면 같은 상자에 이름 뒤에 슬래시를 추가하면 됩니다(예: `paris-Bitcoin-conference-2024/`). 슬래시를 추가하면 파일이 아닌 폴더가 자동으로 생성됩니다:

![event](assets/07.webp)


- 이 폴더에 `events.yml`이라는 이름의 첫 번째 YAML 파일을 만듭니다:

![event](assets/08.webp)


- 이 템플릿을 사용하여 회의에 대한 정보로 이 파일을 채우세요:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
project:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language:
-
links:
website:
replay_url:
live_url :
tags:
-
```


예를 들어 YAML 파일은 다음과 같이 보일 수 있습니다:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

아직 조직의 "*프로젝트*" 식별자가 없는 경우 이 다른 튜토리얼을 따라 추가할 수 있습니다.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- 이 파일에 대한 변경이 완료되면 `변경사항 커밋...` 버튼을 클릭하여 저장합니다:

![event](assets/10.webp)


- 변경 내용에 대한 제목과 간단한 설명을 추가합니다:

![event](assets/11.webp)


- Green `변경 제안` 버튼을 클릭합니다:

![event](assets/12.webp)


- 그러면 모든 변경 사항을 요약한 페이지가 표시됩니다:

![event](assets/13.webp)


- 오른쪽 상단의 GitHub 프로필 사진을 클릭한 다음 '내 리포지토리'를 클릭합니다:

![event](assets/14.webp)


- PlanB 네트워크 리포지토리에서 Fork을 선택합니다:

![event](assets/15.webp)


- 창 상단에 새 브랜치에 대한 알림이 표시될 것입니다. 아마도 '패치-1'이라는 이름으로 표시될 것입니다. 그것을 클릭하세요:

![event](assets/16.webp)


- 이제 작업 중인 브랜치에 도착했습니다:

![event](assets/17.webp)


- Resources/conference/` 폴더로 돌아가서 이전 커밋에서 방금 만든 회의의 폴더를 선택합니다:

![event](assets/18.webp)


- 회의 폴더에서 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![event](assets/19.webp)


- 이 새 폴더의 이름을 `자산`으로 지정하고 끝에 슬래시 `/`를 넣어 생성을 확인합니다:

![event](assets/20.webp)


- 이 `assets` 폴더에 '.gitkeep'이라는 파일을 만듭니다:

![event](assets/21.webp)


- '변경사항 커밋...' 버튼을 클릭합니다:

![event](assets/22.webp)


- 커밋 제목은 기본값으로 두고 '패치 1 브랜치에 직접 커밋' 상자가 선택되어 있는지 확인한 다음 '변경 사항 커밋'을 클릭합니다:

![event](assets/23.webp)


- 자산` 폴더로 돌아갑니다:

![event](assets/24.webp)


- 파일 추가` 버튼을 클릭한 다음 `파일 업로드`: ![이벤트](자산/25.webp)를 클릭합니다
- 새 페이지가 열립니다. 회의를 나타내는 이미지를 끌어다 놓으면 PlanB 네트워크 사이트에 표시됩니다:

![event](assets/26.webp)


- 로고, 썸네일 또는 포스터가 될 수 있습니다:

![event](assets/27.webp)


- 이미지가 업로드되면 '패치 1 브랜치에 직접 커밋' 상자가 선택되어 있는지 확인한 다음 '변경 사항 커밋'을 클릭합니다:

![event](assets/28.webp)


- 이미지의 이름은 `썸네일`이어야 하며 형식은 `.webp`여야 합니다. 따라서 전체 파일 이름은 다음과 같아야 합니다: 썸네일.webp`여야 합니다:

![event](assets/29.webp)


- 자산` 폴더로 돌아가서 중개 파일인 `.gitkeep`을 클릭합니다:

![event](assets/30.webp)


- 파일에서 오른쪽 상단의 작은 점 3개를 클릭한 다음 '파일 삭제'를 클릭합니다:

![event](assets/31.webp)


- 여전히 동일한 작업 브랜치에 있는지 확인한 다음 '변경사항 커밋' 버튼을 클릭합니다:

![event](assets/32.webp)


- 커밋에 제목과 설명을 추가한 다음 '변경 사항 커밋'을 클릭합니다:

![event](assets/33.webp)


- 리포지토리의 루트로 돌아갑니다:

![event](assets/34.webp)


- 브랜치가 변경되었다는 메시지가 표시될 것입니다. '비교 및 풀 리퀘스트' 버튼을 클릭합니다:

![event](assets/35.webp)


- PR에 명확한 제목과 설명을 추가하세요:

![event](assets/36.webp)


- '풀 리퀘스트 만들기' 버튼을 클릭합니다:

![event](assets/37.webp)

축하합니다! PR이 성공적으로 생성되었습니다. 이제 관리자가 확인하고 모든 것이 정상이면 PlanB Network의 메인 리포지토리에 병합합니다. 며칠 후 웹사이트에 이벤트가 표시될 것입니다.


PR의 진행 상황을 반드시 확인하세요. 관리자가 추가 정보를 요청하는 댓글을 남길 수 있습니다. PR이 검증되지 않은 경우, PlanB Network GitHub 리포지토리의 '풀 리퀘스트' 탭에서 확인할 수 있습니다:

![event](assets/38.webp)

소중한 의견을 보내주셔서 감사합니다! :)