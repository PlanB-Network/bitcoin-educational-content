---
name: Plan ₿ Academy 교수
description: Plan ₿ Network에서 교사 프로필을 추가하거나 수정하려면 어떻게 하나요?
---
![cover](assets/cover.webp)


새 튜토리얼이나 강좌를 작성하여 Plan ₿ Network에 기여하려는 경우 교사 프로필이 필요합니다. 이 프로필을 통해 플랫폼에 기여한 콘텐츠에 대해 적절한 크레딧을 받을 수 있습니다.


이미 Plan ₿ Network에서 교육 콘텐츠 제작에 참여한 적이 있는 분이라면 이미 교사 프로필이 있을 것입니다. GitHub 리포지토리의 `/professors` 폴더에서 찾을 수 있습니다(https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). 프로필이 이미 있는 경우 `professor.yml` 파일에서 로그인 정보를 찾으세요.


프로필을 변경하려면 이 튜토리얼 마지막에 있는 '교사 프로필 수정' 섹션으로 이동합니다.


## 소프트웨어로 새 교사 추가하기


Plan ₿ Network에서 교사 프로필을 만드는 가장 쉬운 방법은 통합된 Python 도구를 사용하는 것입니다. 사용 방법은 다음과 같습니다.


### 1 - 로컬 환경 구성


GitHub의 Plan ₿ Academy 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content)의 Fork이 있어야 합니다.


Fork의 메인 브랜치(`개발`)를 소스 리포지토리와 동기화합니다.


로컬 클론을 업데이트합니다.


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### 2 - 새 브랜치 만들기


개발자 브랜치에 있는지 확인합니다. 설명이 포함된 이름(예: `add-professor-loic-morel`)으로 새 브랜치를 만듭니다.


이 지점을 Fork 온라인에 게시하세요.


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - 교사 프로필 만들기


로컬 클론의 '스크립트/튜토리얼 관련/데이터 크리에이터/' 폴더로 이동합니다. 소프트웨어에 필요한 모든 종속성을 설치했는지, 먼저 Python을 설치했는지 확인합니다:


```bash
pip install -r requirements.txt
```


그런 다음 다음 명령을 사용하여 소프트웨어를 실행합니다:


```bash
python3 main.py
```


홈 페이지에서 리포지토리 복제본의 로컬 경로, 작성 중인 언어 및 GitHub ID를 입력합니다. 다른 사람을 위해 이 프로필을 만들고 이미 교수님의 프로필이 있는 경우 "*Plan ₿ Academy 교수님의 ID*" 필드에 교수님의 ID를 입력합니다. 자신의 프로필을 만드는 중이라면 아직 교수님의 ID가 없으므로 이 필드를 비워 두세요.


그런 다음 "*새 교수*" 버튼을 클릭합니다.


![Image](assets/fr/01.webp)


필수 정보를 입력합니다(이 모든 정보는 플랫폼과 GitHub에 공개됩니다):




- 교사 파일 이름(이름과 성 또는 가명, 소문자 사용) ;
- 이름 또는 닉네임 ;
- 웹사이트 및 프로필 X(선택 사항) ;
- 독자로부터 기부를 받을 수 있는 라이트닝 Address(선택 사항) ;
- 목록에서 태그를 2개 또는 3개 선택합니다;
- "*이미지 선택*"을 클릭하여 로컬 폴더에서 프로필 이미지를 선택합니다(이미지에는 어떤 이름과 형식도 사용할 수 있으며 소프트웨어가 자동으로 조정합니다). 이미지가 정사각형인지 확인하세요;)
- 프로필에 대한 간단한 설명을 작성합니다.


"*교수 만들기*"를 클릭하여 생성을 완료합니다. 그러면 프로필에 필요한 모든 파일이 자동으로 generate됩니다.


![Image](assets/fr/02.webp)


설명 메시지와 함께 커밋을 생성하여 로컬에 변경 사항을 저장합니다. 변경 사항을 Fork GitHub에 푸시합니다.


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


완료되면 GitHub에서 풀 리퀘스트(PR)를 만들어 수정 사항의 통합을 제안합니다. PR에 제목과 간단한 설명을 추가합니다.


### 4 - 교정 및 병합


관리자의 확인 또는 피드백을 기다립니다. 필요한 경우 수정하고 새 커밋을 푸시합니다.


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


PR이 병합되면 작업 중인 브랜치를 삭제할 수 있습니다.


## 교사 프로필 수정하기


Git 사용법을 익혔다면 새 브랜치를 만들고 기존 폴더에서 직접 관련 파일을 수정하여 교사 프로필을 수정합니다. 수정할 정보에 따라 `professor.yml` 파일 또는 마크다운 파일에서 변경할 수 있습니다. 로컬에서 변경한 후에는 Fork에 푸시하고 PR을 제출합니다.


초보자의 경우 GitHub의 Interface 웹을 통해 직접 수정하는 것을 권장합니다. GitHub 계정이 있는지 확인하세요. 계정을 만드는 방법을 모른다면 이 튜토리얼을 참조하세요:


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
데이터 전용 Plan ₿ Academy GitHub 리포지토리](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors)로 이동합니다.


![Image](assets/fr/03.webp)


"*교수*" 폴더를 클릭한 다음 개인 폴더로 이동합니다.


![Image](assets/fr/04.webp)


프로필 메타데이터(예: Lightning Address, 이름 또는 링크)를 변경하려면 "*professor.yml*" 파일을 선택합니다. 설명을 변경하려면 해당 언어의 YAML 파일(예: "*en.yml*" 또는 "*fr.yml*")을 클릭합니다.


설명을 수정하는 경우 더 이상 사용되지 않는 번역을 모두 제거해야 한다는 점을 잊지 마세요. 그런 다음 언어 번역가의 도움을 받아 설명을 다른 언어로 번역하거나, 모국어로 된 설명만 남겨두고 풀 리퀘스트에 번역이 필요하다는 점을 언급하세요.


![Image](assets/fr/05.webp)


수정하려는 파일에서 연필 아이콘을 클릭합니다.


![Image](assets/fr/06.webp)


Plan ₿ Academy 리포지토리에서 Fork을 아직 만들지 않았다면 GitHub에서 만들 것을 제안합니다. "*이 리포지토리에서 Fork 만들기*"를 클릭합니다.


![Image](assets/fr/07.webp)


파일을 원하는 대로 변경합니다. 완료되면 "*변경 사항 커밋*"을 클릭합니다.


![Image](assets/fr/08.webp)


변경 내용을 설명하는 메시지를 입력한 다음 "*변경 제안*"을 선택합니다.


![Image](assets/fr/09.webp)


변경사항에 대한 요약이 표시됩니다. 프로필을 더 변경하고 싶은 경우 폴더로 돌아가서 추가 커밋을 할 수 있습니다. 완료했으면 "*풀 리퀘스트 만들기*"를 클릭합니다.


풀 리퀘스트는 브랜치의 변경 사항을 Plan ₿ Academy 리포지토리의 메인 브랜치에 통합하기 위한 요청으로, 변경 사항이 병합되기 전에 검토하고 논의할 수 있습니다.


![Image](assets/fr/10.webp)


Interface의 상단에서 작업 브랜치가 Plan ₿ Academy 리포지토리(메인 브랜치)의 `dev` 브랜치와 병합되었는지 확인하세요.


소스 리포지토리와 병합하려는 변경 사항을 간략하게 요약하는 제목을 입력합니다. 이러한 변경 사항을 설명하는 간단한 코멘트를 추가한 다음 Green "*풀 리퀘스트 만들기*" 버튼을 클릭하여 풀 리퀘스트를 확인합니다:


![Image](assets/fr/11.webp)


그러면 메인 Plan ₿ Academy 리포지토리의 "*풀 리퀘스트*" 탭에서 PR을 볼 수 있습니다. 이제 관리자가 수정 사항을 병합할 때까지 기다리기만 하면 됩니다.


![Image](assets/fr/12.webp)


변경 사항을 제출하는 데 기술적인 문제가 발생하면 언제든지 [기여 전용 텔레그램 그룹](https://t.me/PlanBNetwork_ContentBuilder)에서 도움을 요청해 주세요. 대단히 감사합니다!