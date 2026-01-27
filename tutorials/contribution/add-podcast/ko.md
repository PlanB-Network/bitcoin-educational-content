---
name: PlanB 네트워크에 팟캐스트 추가하기
description: PlanB 네트워크에 새 팟캐스트를 추가하는 방법은 무엇인가요?
---
![podcast](assets/cover.webp)


PlanB의 사명은 Bitcoin에 대한 최고 수준의 교육 리소스를 가능한 한 많은 언어로 제공하는 것입니다. 이 사이트에 게시된 모든 콘텐츠는 오픈 소스이며 GitHub에서 호스팅되므로 누구나 플랫폼을 더욱 풍성하게 만드는 데 참여할 수 있습니다.


플랜비 네트워크 사이트에 Bitcoin 팟캐스트를 추가하여 쇼의 가시성을 높이고 싶지만 방법을 모르시나요? 이 튜토리얼은 여러분을 위한 것입니다!

![podcast](assets/01.webp)


- 먼저 GitHub 계정이 있어야 합니다. 계정을 만드는 방법을 모르는 경우 자세한 튜토리얼을 만들어 안내해 드립니다.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- '자료/팟캐스트/' 섹션의 [데이터 전용 PlanB의 GitHub 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts)로 이동합니다:

![podcast](assets/02.webp)


- 오른쪽 상단의 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![podcast](assets/03.webp)


- 이전에 PlanB Network의 콘텐츠에 기여한 적이 없는 경우, 원본 리포지토리의 Fork를 만들어야 합니다. 리포지토리를 포크한다는 것은 자신의 GitHub 계정에 해당 리포지토리의 복사본을 생성하여 원본 리포지토리에 영향을 주지 않고 프로젝트 작업을 할 수 있도록 하는 것을 의미합니다. '이 리포지토리 Fork' 버튼을 클릭합니다:

![podcast](assets/04.webp)


- 그러면 GitHub 편집 페이지로 이동합니다:

![podcast](assets/05.webp)


- 팟캐스트를 위한 폴더를 만듭니다. 이렇게 하려면 `파일 이름...` 상자에 공백 대신 대시를 사용하여 소문자로 팟캐스트의 이름을 입력합니다. 예를 들어, 프로그램 이름이 "슈퍼 팟캐스트 Bitcoin"인 경우 `super-podcast-Bitcoin`라고 작성해야 합니다:

![podcast](assets/06.webp)


- 폴더 생성을 확인하려면 같은 상자에 팟캐스트 이름 뒤에 슬래시를 추가하면 됩니다(예: `super-podcast-Bitcoin/`). 슬래시를 추가하면 파일이 아닌 폴더가 자동으로 생성됩니다:

![podcast](assets/07.webp)


- 이 폴더에 'podcast.yml'이라는 이름의 첫 번째 YAML 파일을 만듭니다:

![podcast](assets/08.webp)


- 이 템플릿을 사용하여 팟캐스트에 대한 정보를 이 파일에 입력하세요:


```yaml
name:
host:
language:
links:
podcast:
twitter:
website:
description: |

tags:
-
-
contributors:
-
```


각 필드에 입력해야 할 세부 정보는 다음과 같습니다:



- 이름`**: 팟캐스트의 이름을 표시합니다.
- 호스트`**: 팟캐스트의 화자 또는 호스트의 이름 또는 가명을 나열합니다. 각 이름은 쉼표로 구분해야 합니다.
- 언어`**: 팟캐스트에서 사용하는 언어의 언어 코드를 표시합니다. 예를 들어 영어의 경우 `en`, 이탈리아어의 경우 `it`...을 표시합니다.



- 링크`**: 콘텐츠에 대한 링크를 제공합니다. 두 가지 옵션이 있습니다:
 - '팟캐스트': 팟캐스트 링크입니다,
 - 트위터`: 팟캐스트 또는 팟캐스트를 제작하는 조직의 트위터 프로필 링크입니다,
 - '웹사이트': 팟캐스트 또는 팟캐스트를 제작하는 단체의 웹사이트 링크입니다.



- 설명`**: 팟캐스트를 설명하는 짧은 문단을 추가합니다. 설명은 `언어:` 필드에 표시된 것과 동일한 언어로 작성해야 합니다.



- 태그`**: 팟캐스트와 관련된 두 개의 태그를 추가합니다. 예시:
    - `Bitcoin`
    - '기술'
    - `경제`
    - '교육'...



- 기여자`**: 기여자 ID가 있는 경우 이를 언급하세요.


예를 들어 YAML 파일은 다음과 같이 보일 수 있습니다:


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- 이 파일에 대한 변경이 완료되면 `변경사항 커밋...` 버튼을 클릭하여 저장합니다:

![podcast](assets/10.webp)


- 변경 내용에 대한 제목과 간단한 설명을 추가합니다:

![podcast](assets/11.webp)


- Green `변경 제안` 버튼을 클릭합니다:

![podcast](assets/12.webp)


- 그러면 모든 변경 사항이 요약된 페이지로 이동합니다:

![podcast](assets/13.webp)


- 오른쪽 상단의 GitHub 프로필 사진을 클릭한 다음 '내 리포지토리'를 클릭합니다:

![podcast](assets/14.webp)


- PlanB 네트워크 리포지토리에서 Fork을 선택합니다:

![podcast](assets/15.webp)


- 창 상단에 새 브랜치에 대한 알림이 표시될 것입니다. 아마도 '패치-1'이라는 이름으로 표시될 것입니다. 그것을 클릭하세요:

![podcast](assets/16.webp)


- 이제 작업 중인 브랜치에 도착했습니다:

![podcast](assets/17.webp)


- Resources/podcast/` 폴더로 돌아가서 이전 커밋에서 방금 만든 팟캐스트 폴더인 ![podcast](assets/18.webp)를 선택합니다
- 팟캐스트 폴더에서 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![podcast](assets/19.webp)


- 이 새 폴더의 이름을 `자산`으로 지정하고 끝에 슬래시 `/`를 추가하여 생성을 확인합니다:

![podcast](assets/20.webp)


- 이 `assets` 폴더에 '.gitkeep'이라는 파일을 만듭니다:

![podcast](assets/21.webp)


- '변경사항 커밋...' 버튼을 클릭합니다:

![podcast](assets/22.webp)


- 커밋 제목은 기본값으로 두고 '패치 1 브랜치에 직접 커밋' 상자가 선택되어 있는지 확인한 다음 '변경 사항 커밋'을 클릭합니다:

![podcast](assets/23.webp)


- 자산` 폴더로 돌아갑니다:

![podcast](assets/24.webp)


- 파일 추가` 버튼을 클릭한 다음 `파일 업로드`를 클릭합니다:

![podcast](assets/25.webp)


- 새 페이지가 열립니다. 팟캐스트 로고를 해당 영역으로 끌어다 놓습니다. 이 이미지가 PlanB 네트워크 사이트에 표시됩니다:

![podcast](assets/26.webp)


- 웹사이트에 가장 잘 맞도록 이미지가 정사각형이어야 한다는 점에 유의하세요:

![podcast](assets/27.webp)


- 이미지가 업로드되면 '패치 1 브랜치에 직접 커밋' 상자가 체크되어 있는지 확인한 다음 '변경 사항 커밋'을 클릭합니다:

![podcast](assets/28.webp)


- 이미지의 이름은 '로고'여야 하며 '.webp' 형식이어야 한다는 점에 유의하세요. 따라서 전체 파일 이름은 다음과 같아야 합니다: 로고.webp`여야 합니다:

![podcast](assets/29.webp)


- 자산` 폴더로 돌아가서 중개 파일인 `.gitkeep`을 클릭합니다:

![podcast](assets/30.webp)


- 파일에서 오른쪽 상단의 작은 점 세 개를 클릭한 다음 '파일 삭제'를 클릭합니다:

![podcast](assets/31.webp)


- 여전히 동일한 작업 브랜치에 있는지 확인한 다음 '변경사항 커밋' 버튼을 클릭합니다:

![podcast](assets/32.webp)


- 커밋에 제목과 설명을 추가한 다음 '변경 사항 커밋'을 클릭합니다:

![podcast](assets/33.webp)


- 리포지토리의 루트로 돌아갑니다:

![podcast](assets/34.webp)


- 브랜치가 변경되었다는 메시지가 표시될 것입니다. '비교 및 풀 리퀘스트' 버튼을 클릭합니다:

![podcast](assets/35.webp)


- PR에 명확한 제목과 설명을 추가하세요:

![podcast](assets/36.webp)


- '풀 리퀘스트 만들기' 버튼을 클릭합니다:

![podcast](assets/37.webp)

축하합니다! PR이 성공적으로 생성되었습니다. 이제 관리자가 검토하고 모든 것이 정상이면 PlanB Network의 메인 리포지토리에 병합합니다. 며칠 후 웹사이트에 팟캐스트가 표시될 것입니다.


PR 진행 상황을 꼭 확인하세요. 관리자가 추가 정보를 요청하는 댓글을 남길 수 있습니다. PR의 유효성이 검사되지 않은 경우, 플랜비 네트워크 깃허브 리포지토리의 '풀 리퀘스트' 탭에서 확인할 수 있습니다:

![podcast](assets/38.webp)

소중한 의견을 보내주셔서 감사합니다! :)