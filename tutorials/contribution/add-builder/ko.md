---
name: 프로젝트 추가
description: 플랜비 네트워크에 새 프로젝트 추가를 제안하는 방법은 무엇인가요?
---
![project](assets/cover.webp)


PlanB의 사명은 Bitcoin에 대한 최고 수준의 교육 리소스를 가능한 한 많은 언어로 제공하는 것입니다. 이 사이트에 게시된 모든 콘텐츠는 오픈 소스이며 GitHub에서 호스팅되므로 누구나 플랫폼을 더욱 풍성하게 만드는 데 참여할 수 있습니다.


플랜비 네트워크 사이트에 새로운 Bitcoin "프로젝트"를 추가하여 회사 또는 소프트웨어에 가시성을 부여하고 싶지만 방법을 모르시나요? 이 튜토리얼은 여러분을 위한 것입니다!

![project](assets/01.webp)


- 먼저 GitHub 계정이 있어야 합니다. 계정을 만드는 방법을 모르는 경우 자세한 튜토리얼을 만들어 안내해 드리고 있습니다.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- '리소스/프로젝트/' 섹션의 [데이터 전용 PlanB의 GitHub 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects)로 이동합니다:

![project](assets/02.webp)


- 오른쪽 상단의 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![project](assets/03.webp)


- 이전에 PlanB Network의 콘텐츠에 기여한 적이 없는 경우, 원본 리포지토리의 Fork를 만들어야 합니다. 리포지토리를 포크한다는 것은 자신의 GitHub 계정에 해당 리포지토리의 복사본을 생성하여 원본 리포지토리에 영향을 주지 않고 프로젝트 작업을 할 수 있도록 하는 것을 의미합니다. '이 리포지토리 Fork' 버튼을 클릭합니다:

![project](assets/04.webp)


- 그러면 GitHub 편집 페이지로 이동합니다:

![project](assets/05.webp)


- 회사를 위한 폴더를 만듭니다. 이렇게 하려면 '파일 이름...` 상자에 회사 이름을 공백 대신 대시를 사용하여 소문자로 입력합니다. 예를 들어, 회사 이름이 'Bitcoin 바게트'인 경우 `Bitcoin-baguette`라고 적어야 합니다:

![project](assets/06.webp)


- 폴더 생성을 확인하려면 같은 상자에서 이름 뒤에 슬래시를 추가하면 됩니다(예: `Bitcoin-baguette/`). 슬래시를 추가하면 파일이 아닌 폴더가 자동으로 생성됩니다:

![project](assets/07.webp)


- 이 폴더에 'project.yml'이라는 이름의 첫 번째 YAML 파일을 생성합니다:

![project](assets/08.webp)


- 이 템플릿을 사용하여 회사에 대한 정보로 이 파일을 채우세요:


```yaml
name:

address_line_1:
address_line_2:
address_line_3:

language:
-

links:
website:
twitter:
Github:
youtube:
nostr:

tags:
-
-

category:
```


각 키에 입력할 내용은 다음과 같습니다:


- 이름`: 회사 이름(필수);
- `Address`: 사업장 위치(선택 사항);
- '언어': 비즈니스가 운영되는 국가 또는 지원되는 언어(선택 사항);
- '링크': 비즈니스의 다양한 공식 링크(선택 사항);
- '태그': 비즈니스를 인증하는 용어 2개(필수);
- 카테고리` : 다음 선택 항목 중 비즈니스가 운영되는 분야를 가장 잘 설명하는 카테고리입니다:
 - `Wallet`,
 - '인프라',
 - `Exchange`,
 - '교육',
 - 서비스`,
 - 커뮤니티`,
 - '회의',
 - '개인정보',
 - '투자',
 - 노드`,
 - `Mining`,
 - 뉴스`,
 - 제조업체`.


예를 들어 YAML 파일은 다음과 같이 보일 수 있습니다:


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![project](assets/09.webp)


- 이 파일에 대한 변경이 완료되면 `변경사항 커밋...` 버튼을 클릭하여 저장합니다:

![project](assets/10.webp)


- 간단한 설명과 함께 변경 사항의 제목을 추가합니다:

![project](assets/11.webp)


- Green `변경 제안` 버튼을 클릭합니다:

![project](assets/12.webp)


- 그러면 모든 변경 사항을 요약한 페이지가 표시됩니다:

![project](assets/13.webp)


- 오른쪽 상단의 GitHub 프로필 사진을 클릭한 다음 '내 리포지토리'를 클릭합니다:

![project](assets/14.webp)


- PlanB 네트워크 리포지토리에서 Fork을 선택합니다:

![project](assets/15.webp)


- 창 상단에 새 브랜치에 대한 알림이 표시될 것입니다. 아마도 '패치-1'이라는 이름으로 표시될 것입니다. 그것을 클릭하세요:

![project](assets/16.webp)


- 이제 작업 브랜치에 들어왔습니다(**이전 수정 사항과 동일한 브랜치에 있는지 확인하세요. 이것은 중요합니다!**):

![project](assets/17.webp)


- Resources/projects/` 폴더로 돌아가서 이전 커밋에서 방금 만든 비즈니스 폴더를 선택합니다:

![project](assets/18.webp)


- 비즈니스 폴더에서 '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![project](assets/19.webp)


- 이 새 폴더의 이름을 `자산`으로 지정하고 끝에 슬래시 `/`를 넣어 생성을 확인합니다:

![project](assets/20.webp)


- 이 `assets` 폴더에 '.gitkeep'이라는 파일을 만듭니다:

![project](assets/21.webp)


- '변경사항 커밋...' 버튼을 클릭합니다:

![project](assets/22.webp)


- 커밋 제목은 기본값으로 두고 `패치-1 브랜치에 직접 커밋` 상자가 선택되어 있는지 확인한 다음 `변경 사항 커밋`: ![프로젝트](assets/23.webp)을 클릭합니다
- 자산` 폴더로 돌아갑니다:

![project](assets/24.webp)


- 파일 추가` 버튼을 클릭한 다음 `파일 업로드`를 클릭합니다:

![project](assets/25.webp)


- 새 페이지가 열립니다. 회사 또는 소프트웨어의 이미지를 해당 영역으로 끌어다 놓습니다. 이 이미지는 플랜비 네트워크 사이트에 표시됩니다:

![project](assets/26.webp)


- 로고 또는 아이콘이 될 수 있습니다:

![project](assets/27.webp)


- 이미지가 업로드되면 '패치 1 브랜치에 직접 커밋' 상자가 체크되어 있는지 확인한 다음 '변경 사항 커밋'을 클릭합니다:

![project](assets/28.webp)


- 주의: 이미지는 정사각형이어야 하고, 이름은 '로고'여야 하며, 형식은 '.webp'여야 합니다. 따라서 전체 파일 이름은 다음과 같아야 합니다: 로고.webp`여야 합니다:

![project](assets/29.webp)


- 자산` 폴더로 돌아가서 '.gitkeep' 중간 파일을 클릭합니다:

![project](assets/30.webp)


- 파일에서 오른쪽 상단의 작은 점 세 개를 클릭한 다음 '파일 삭제'를 클릭합니다:

![project](assets/31.webp)


- 여전히 동일한 작업 브랜치에 있는지 확인한 다음 '변경사항 커밋' 버튼을 클릭합니다:

![project](assets/32.webp)


- 커밋에 제목과 설명을 추가한 다음 '변경 사항 커밋'을 클릭합니다:

![project](assets/33.webp)


- 회사 폴더로 돌아갑니다:

![project](assets/34.webp)


- '파일 추가' 버튼을 클릭한 다음 '새 파일 만들기'를 클릭합니다:

![project](assets/35.webp)


- 모국어 표시기로 이름을 지정하여 새 YAML 파일을 만듭니다. 이 파일은 프로젝트 설명에 사용됩니다. 예를 들어 영어로 설명을 작성하려면 이 파일의 이름을 `en.yml`로 지정합니다:

![project](assets/36.webp)


- 이 템플릿을 사용하여 이 YAML 파일을 작성하세요:

```yaml
description: |

contributors:
-
```



- '기여자' 키의 경우 기여자 식별자가 있는 경우 PlanB 네트워크에 기여자 식별자를 추가할 수 있습니다. 없는 경우 이 필드를 비워두세요.
- 설명` 키의 경우 회사 또는 소프트웨어를 설명하는 짧은 단락을 추가하기만 하면 됩니다. 설명은 파일 이름과 같은 언어로 작성해야 합니다. 이 설명을 사이트에서 지원되는 모든 언어로 번역할 필요는 없으며, PlanB 팀에서 모델을 사용하여 번역할 것입니다. 예를 들어 파일은 다음과 같이 표시될 수 있습니다:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![project](assets/37.webp)


- '변경 사항 커밋' 버튼을 클릭합니다:

![project](assets/38.webp)


- 패치 1 브랜치에 직접 커밋` 상자가 선택되어 있는지 확인하고 제목을 추가한 다음 `변경 사항 커밋`을 클릭합니다:

![project](assets/39.webp)


- 이제 회사 폴더가 다음과 같이 표시되어야 합니다:

![project](assets/40.webp)


- 모든 것이 만족스럽다면 Fork의 루트로 돌아가세요:

![project](assets/41.webp)


- 브랜치가 변경되었다는 메시지가 표시될 것입니다. '비교 및 풀 리퀘스트' 버튼을 클릭합니다:

![project](assets/42.webp)


- PR에 명확한 제목과 설명을 추가하세요:

![project](assets/43.webp)


- '풀 리퀘스트 만들기' 버튼을 클릭합니다:

![project](assets/44.webp)

축하합니다! PR이 성공적으로 생성되었습니다. 이제 관리자가 검토하고 모든 것이 정상이면 PlanB Network의 메인 리포지토리에 통합합니다. 며칠 후 웹사이트에 프로젝트 프로필이 표시될 것입니다.


PR의 진행 상황을 반드시 확인하세요. 관리자가 추가 정보를 요청하는 댓글을 남길 수 있습니다. PR이 검증되지 않은 경우, Plan ₿ Academy GitHub 리포지토리의 '풀 리퀘스트' 탭에서 확인할 수 있습니다:

![project](assets/45.webp)

소중한 의견을 보내주셔서 감사합니다! :)