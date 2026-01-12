---
name: 회의 다시보기 추가하기
description: PlanB 네트워크에서 회의 리플레이를 추가하는 방법은 무엇인가요?
---
![conference](assets/cover.webp)


PlanB의 사명은 Bitcoin에 대한 최고 수준의 교육 리소스를 가능한 한 많은 언어로 제공하는 것입니다. 이 사이트에 게시된 모든 콘텐츠는 오픈 소스이며 GitHub에서 호스팅되므로 누구나 플랫폼 강화에 기여할 수 있습니다.


PlanB 네트워크 사이트에 Bitcoin 회의의 리플레이를 추가하고 이 이벤트에 대한 가시성을 제공하고 싶지만 방법을 모르시나요? 이 튜토리얼은 여러분을 위한 것입니다!


하지만 앞으로 열릴 회의를 추가하려면 사이트에 새 이벤트를 추가하는 방법을 설명하는 이 다른 튜토리얼을 읽어보시기 바랍니다.


https://planb.academy/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- 먼저 GitHub에 계정이 있어야 합니다. 계정을 만드는 방법을 모르는 경우 자세한 튜토리얼을 만들어 안내해 드립니다.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 리소스/회의/` 섹션의 [데이터 전용 PlanB의 GitHub 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference)로 이동합니다:

![conference](assets/02.webp)


- 오른쪽 상단의 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![conference](assets/03.webp)


- 이전에 PlanB Network의 콘텐츠에 기여한 적이 없는 경우, 원본 리포지토리의 Fork를 만들어야 합니다. 리포지토리를 포크한다는 것은 자신의 GitHub 계정에 해당 리포지토리의 복사본을 생성하여 원본 리포지토리에 영향을 주지 않고 프로젝트 작업을 할 수 있도록 하는 것을 의미합니다. '이 리포지토리 Fork' 버튼을 클릭합니다:

![conference](assets/04.webp)


- 그러면 GitHub 편집 페이지로 이동합니다:

![conference](assets/05.webp)


- 회의를 위한 폴더를 만듭니다. 이렇게 하려면 '파일 이름...` 상자에 공백 대신 대시를 사용하여 소문자로 회의 이름을 입력합니다. 예를 들어, 컨퍼런스의 이름이 '파리 Bitcoin 컨퍼런스'인 경우 '파리-Bitcoin-conference'라고 적어야 합니다. 또한 회의의 연도를 추가합니다(예: `paris-Bitcoin-conference-2024`):

![conference](assets/06.webp)


- 폴더 생성을 확인하려면 같은 상자에 이름 뒤에 슬래시를 추가하면 됩니다(예: `paris-Bitcoin-conference-2024/`). 슬래시를 추가하면 파일이 아닌 폴더가 자동으로 생성됩니다:

![conference](assets/07.webp)


- 이 폴더에 `conference.yml`이라는 이름의 첫 번째 YAML 파일을 만듭니다:

![conference](assets/08.webp)

이 템플릿을 사용하여 회의와 관련된 정보로 이 파일을 채우세요:

```yaml
year:
name:
project:
location:
language:
-
links:
website:
twitter:
tags:
-
-
```


예를 들어 YAML 파일은 다음과 같이 보일 수 있습니다:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


아직 조직의 "*프로젝트*" 식별자가 없는 경우 이 다른 튜토리얼을 따라 추가할 수 있습니다.


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- 이 파일에 대한 변경이 완료되면 `변경사항 커밋...` 버튼을 클릭하여 저장합니다:

![conference](assets/10.webp)


- 변경 내용에 대한 제목과 간단한 설명을 추가합니다:

![conference](assets/11.webp)


- Green `변경 제안` 버튼을 클릭합니다:

![conference](assets/12.webp)


- 그러면 모든 변경 사항을 요약한 페이지가 표시됩니다:

![conference](assets/13.webp)


- 오른쪽 상단의 GitHub 프로필 사진을 클릭한 다음 '내 리포지토리'를 클릭합니다:

![conference](assets/14.webp)


- PlanB 네트워크 리포지토리에서 Fork을 선택합니다:

![conference](assets/15.webp)


- 창 상단에 새 브랜치에 대한 알림이 표시될 것입니다. 아마도 '패치-1'이라고 할 것입니다. 그것을 클릭하세요:

![conference](assets/16.webp)


- 이제 작업 중인 브랜치에 도착했습니다:

![conference](assets/17.webp)


- Resources/conference/` 폴더로 돌아가서 이전 커밋에서 방금 만든 회의의 폴더를 선택합니다:

![conference](assets/18.webp)


- 회의 폴더에서 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![conference](assets/19.webp)


- 이 새 폴더의 이름을 `자산`으로 지정하고 끝에 슬래시 `/`를 넣어 생성을 확인합니다:

![conference](assets/20.webp)


- 이 `assets` 폴더에 '.gitkeep'이라는 파일을 만듭니다:

![conference](assets/21.webp)


- '변경사항 커밋...' 버튼을 클릭합니다:

![conference](assets/22.webp)


- 커밋 제목은 기본값으로 두고 '패치 1 브랜치에 직접 커밋' 상자가 선택되어 있는지 확인한 다음 '변경 사항 커밋'을 클릭합니다:

![conference](assets/23.webp)


- 자산` 폴더로 돌아갑니다:

![conference](assets/24.webp)


- 파일 추가` 버튼을 클릭한 다음 `파일 업로드`를 클릭합니다:

![conference](assets/25.webp)


- 새 페이지가 열립니다. 회의를 나타내는 이미지를 끌어다 놓으면 PlanB 네트워크 사이트에 표시됩니다: ![conference](assets/26.webp)
- 로고, 썸네일 또는 포스터가 될 수 있습니다:

![conference](assets/27.webp)


- 이미지가 업로드되면 '패치 1 브랜치에 직접 커밋' 상자가 선택되어 있는지 확인한 다음 '변경 사항 커밋'을 클릭합니다:

![conference](assets/28.webp)


- 이미지의 이름은 `썸네일`이어야 하며 형식은 `.webp`여야 합니다. 따라서 전체 파일 이름은 다음과 같아야 합니다: 썸네일.webp`여야 합니다:

![conference](assets/29.webp)


- 자산` 폴더로 돌아가서 '.gitkeep' 중개 파일을 클릭합니다:

![conference](assets/30.webp)


- 파일에서 오른쪽 상단에 있는 작은 점 3개를 클릭한 다음 '파일 삭제'를 클릭합니다:

![conference](assets/31.webp)


- 여전히 동일한 작업 브랜치에 있는지 확인한 다음 '변경사항 커밋' 버튼을 클릭합니다:

![conference](assets/32.webp)


- 커밋에 제목과 설명을 추가한 다음 '변경 사항 커밋'을 클릭합니다:

![conference](assets/33.webp)


- 회의 폴더로 돌아갑니다:

![conference](assets/34.webp)


- '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![conference](assets/35.webp)


- 모국어 표시를 사용하여 이름을 지정하여 새 마크다운(.md) 파일을 만듭니다. 이 파일은 회의의 리플레이에 사용됩니다. 예를 들어 회의에 대한 설명을 영어로 작성하려면 이 파일의 이름을 en.md로 지정합니다:

![conference](assets/36.webp)


- 회의 구성에 맞게 조정할 수 있는 이 템플릿을 사용하여 이 마크다운 파일을 작성하세요:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- 문서 시작 부분의 '머리말'에 `이름:` 필드에 회의 이름과 리플레이 연도를 입력합니다. 설명:` 필드에 파일 언어로 이벤트에 대한 간단한 설명을 작성합니다. 예를 들어, 파일 이름이 `en.md`인 경우, 설명은 영어로 작성해야 합니다. 플랜비 네트워크 팀이 자체 모델을 사용하여 설명을 번역해 드립니다.
- '#'으로 표시된 1단계 제목은 컨퍼런스를 장면별로 구성하는 데 사용됩니다. 예를 들어 메인 스테이지에는 '# 메인 스테이지', 워크숍 전용 무대에는 '# 워크숍 룸'으로 표시합니다.



- 이중 `##`으로 표시된 두 번째 레벨 제목은 서로 다른 다시보기 동영상을 구분하는 데 사용됩니다. 컨퍼런스가 반나절 동안 연속으로 촬영된 경우 예를 들어 '### 금요일 오전'과 같이 표시합니다. 컨퍼런스를 개별적으로 촬영하여 방송한 경우에는 두 번째 수준의 제목을 사용하여 컨퍼런스의 이름을 직접 지정합니다.



- 각 2단계 제목 아래에 해당 재생 동영상으로 연결되는 링크를 삽입합니다. 구문은 다음과 같아야 합니다: '![동영상](https://youtu.be/XXXXXXXXXXXX)` 구문으로, `XXXXXXXXXX`를 실제 동영상 링크로 대체합니다.



- 형식이 허용하는 경우(개별 회의) 발표자의 이름을 추가할 수 있습니다. 이렇게 하려면 비디오 링크 아래에 '발표자:` 필드 다음에 발표자의 이름 또는 가명을 추가합니다. 발표자가 여러 명인 경우에는 쉼표로 각 이름을 구분합니다(예: '발표자'): 나카모토 나카모토, 나카모토 나카모토, 나카모토 나카모토, 나카모토 나카모토`와 같이 쉼표로 구분합니다.


---


- 이 파일에 대한 수정이 완료되면 `변경사항 커밋...` 버튼을 클릭하여 저장합니다:

![conference](assets/38.webp)


- 수정한 내용에 대한 제목과 간단한 설명을 추가합니다:

![conference](assets/39.webp)


- '변경 사항 커밋'을 클릭합니다:

![conference](assets/40.webp)


- 이제 회의 폴더가 다음과 같이 보일 것입니다:

![conference](assets/41.webp)


- 모든 것이 만족스럽다면 Fork의 루트로 돌아가세요:

![conference](assets/42.webp)


- 브랜치가 수정되었음을 알리는 메시지가 표시됩니다. '비교 및 풀 리퀘스트' 버튼을 클릭합니다:

![conference](assets/43.webp)


- PR의 명확한 제목과 설명을 추가하세요:

![conference](assets/44.webp)


- '풀 리퀘스트 만들기' 버튼을 클릭합니다:

![conference](assets/45.webp)

축하합니다! PR이 성공적으로 생성되었습니다. 이제 관리자가 검토하고 모든 것이 정상이면 PlanB Network의 메인 리포지토리에 병합합니다. 며칠 후 웹사이트에 회의 리플레이가 표시될 것입니다.


PR 진행 상황을 꼭 확인하세요. 관리자가 추가 정보를 요청하는 댓글을 남길 수 있습니다. PR의 유효성이 검사되지 않은 경우, 플랜비 네트워크의 깃허브 리포지토리의 '풀 리퀘스트' 탭에서 확인할 수 있습니다:

![conference](assets/46.webp)


소중한 의견을 보내주셔서 감사합니다! :)