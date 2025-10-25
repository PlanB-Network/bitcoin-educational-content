---
name: PlanB 네트워크에 책 추가하기
description: PlanB 네트워크에 새 책을 추가하는 방법은 무엇인가요?
---
![book](assets/cover.webp)


PlanB의 사명은 Bitcoin에 대한 최고 수준의 교육 리소스를 가능한 한 많은 언어로 제공하는 것입니다. 이 사이트에 게시된 모든 콘텐츠는 오픈 소스이며 GitHub에서 호스팅되므로 누구나 플랫폼 강화에 기여할 수 있습니다.


**플랜비 네트워크 사이트에 Bitcoin과 관련된 책을 추가하고 작업의 가시성을 높이고 싶지만 방법을 모르시나요? 이 튜토리얼은 여러분을 위한 것입니다!

![book](assets/01.webp)


- 먼저 GitHub 계정이 있어야 합니다. 계정을 만드는 방법을 모르는 경우 자세한 튜토리얼을 만들어 안내해 드리고 있습니다.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- 'resources/books/' 섹션의 [데이터 전용 PlanB의 GitHub 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books)로 이동합니다:

![book](assets/02.webp)


- 오른쪽 상단의 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![book](assets/03.webp)


- 플랜비 네트워크의 콘텐츠에 기여한 적이 없는 경우, 원본 리포지토리의 Fork를 만들어야 합니다. 리포지토리를 포크한다는 것은 자신의 GitHub 계정에 해당 리포지토리의 복사본을 생성하여 원본 리포지토리에 영향을 주지 않고 프로젝트 작업을 할 수 있도록 하는 것을 의미합니다. '이 리포지토리 Fork' 버튼을 클릭합니다:

![book](assets/04.webp)


- 그러면 GitHub 편집 페이지로 이동합니다:

![book](assets/05.webp)


- 책을 위한 폴더를 만듭니다. 이렇게 하려면 '파일 이름...` 상자에 공백 대신 대시를 사용하여 소문자로 책 이름을 입력합니다. 예를 들어, 책의 이름이 "*내 Bitcoin 책*"인 경우 `my-Bitcoin-book`이라고 적어야 합니다:

![book](assets/06.webp)


- 폴더 생성을 확인하려면 같은 상자에 책 이름 뒤에 슬래시를 추가하면 됩니다(예: `my-Bitcoin-book/`). 슬래시를 추가하면 파일이 아닌 폴더가 자동으로 생성됩니다:

![book](assets/07.webp)


- 이 폴더에 `book.yml`이라는 이름의 첫 번째 YAML 파일을 만듭니다:

![book](assets/08.webp)


- 이 템플릿을 사용하여 책에 대한 정보로 이 파일을 채우세요:


```yaml
author:
level:
tags:
-
-
```


각 필드에 입력해야 할 세부 정보는 다음과 같습니다:


- 저자`**: 책의 저자 이름을 표시합니다.
- 레벨`**: 책을 잘 읽고 이해하는 데 필요한 수준을 표시합니다. 다음 중에서 레벨을 선택하세요:
 - '초보자'
 - `중급`
- 고급` - `전문가`
- 태그`**: 책과 관련된 태그를 두세 개 추가합니다. 예를 들어
    - `Bitcoin`
    - `역사`
    - '기술'
    - `경제`
    - '교육'...


예를 들어 YAML 파일은 다음과 같이 보일 수 있습니다:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- 이 파일에 대한 변경이 완료되면 `변경사항 커밋...` 버튼을 클릭하여 저장합니다:

![book](assets/10.webp)


- 변경 내용에 대한 제목과 간단한 설명을 추가합니다:

![book](assets/11.webp)


- Green `변경 제안` 버튼을 클릭합니다:

![book](assets/12.webp)


- 그러면 모든 변경 사항을 요약한 페이지가 표시됩니다:

![book](assets/13.webp)


- 오른쪽 상단의 GitHub 프로필 사진을 클릭한 다음 '내 리포지토리'를 클릭합니다:

![book](assets/14.webp)


- PlanB 네트워크 리포지토리에서 Fork을 선택합니다:

![book](assets/15.webp)


- 창 상단에 새 브랜치에 대한 알림이 표시될 것입니다. 아마도 '패치-1'이라는 이름으로 표시될 것입니다. 그것을 클릭하세요:

![book](assets/16.webp)


- 이제 작업 중인 브랜치에 도착했습니다:

![book](assets/17.webp)


- Resources/books/` 폴더로 돌아가서 이전 커밋에서 방금 만든 책의 폴더를 선택합니다:

![book](assets/18.webp)


- 책의 폴더에서 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![book](assets/19.webp)


- 이 새 폴더의 이름을 `자산`으로 지정하고 끝에 슬래시 `/`를 넣어 생성을 확인합니다:

![book](assets/20.webp)


- 이 `assets` 폴더에 '.gitkeep'이라는 파일을 만듭니다:

![book](assets/21.webp)


- '변경사항 커밋...' 버튼을 클릭합니다:

![book](assets/22.webp)


- 커밋 제목은 기본값으로 두고 '패치 1 브랜치에 직접 커밋' 상자가 선택되어 있는지 확인한 다음 '변경 사항 커밋'을 클릭합니다:

![book](assets/23.webp)


- 자산` 폴더로 돌아갑니다:

![book](assets/24.webp)


- 파일 추가` 버튼을 클릭한 다음 `파일 업로드`를 클릭합니다:

![book](assets/25.webp)


- 새 페이지가 열립니다. 책의 표지 이미지를 해당 영역으로 끌어다 놓습니다. 이 이미지는 PlanB 네트워크 사이트에 표시됩니다:

![book](assets/26.webp)


- 예를 들어, 이미지가 책 형식이어야 웹사이트에 가장 잘 어울린다는 점에 유의하세요:

![book](assets/27.webp)


- 이미지가 업로드되면 '패치 1 브랜치에 직접 커밋' 상자가 선택되어 있는지 확인한 다음 '변경 사항 커밋'을 클릭합니다:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- 자산` 폴더로 돌아가서 '.gitkeep' 중개 파일을 클릭합니다:

![book](assets/30.webp)


- 파일에서 오른쪽 상단에 있는 작은 점 3개를 클릭한 다음 '파일 삭제'를 클릭합니다:

![book](assets/31.webp)


- 여전히 동일한 작업 브랜치에 있는지 확인한 다음 `변경사항 커밋...` 버튼을 클릭합니다:

![book](assets/32.webp)


- 커밋에 제목과 설명을 추가한 다음 '변경 사항 커밋'을 클릭합니다:

![book](assets/33.webp)


- 책의 폴더로 돌아갑니다:

![book](assets/34.webp)


- '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![book](assets/35.webp)


- 책의 언어 표시기로 이름을 지정하여 새 YAML 파일을 만듭니다. 이 파일은 책의 설명에 사용됩니다. 예를 들어 영어로 설명을 작성하려면 이 파일의 이름을 `en.yml`로 지정합니다:

![book](assets/36.webp)


- 이 템플릿을 사용하여 이 YAML 파일을 작성하세요:

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


각 필드에 입력해야 할 세부 정보는 다음과 같습니다:


- 제목`**: 책 이름을 따옴표로 묶어 표시합니다.
- 출판 연도`**: 책이 출판된 연도를 표시합니다.
- 커버`**: 현재 편집 중인 YAML 파일의 언어에 따라 표지 이미지에 해당하는 파일 이름을 표시합니다. 예를 들어 `en.yml` 파일을 편집 중이고 이전에 `cover_en.webp`라는 제목의 영문 표지 이미지를 추가한 경우 이 필드에 `cover_en.webp`라고 표시하면 됩니다.
- 설명`**: 책을 설명하는 짧은 단락을 추가합니다. 설명은 YAML 파일 제목에 표시된 것과 동일한 언어로 작성해야 합니다.
- 기여자`**: 기여자 ID가 있는 경우 추가합니다.


예를 들어 YAML 파일은 다음과 같이 보일 수 있습니다:


```yaml