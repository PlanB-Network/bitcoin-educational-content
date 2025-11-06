---
name: 로컬에서 Plan ₿ Academy 플랫폼 실행 가이드
description: 로컬 환경에서 Plan ₿ Network을 실행하여 Plan ₿ Network에서 교육용 콘텐츠의 콘텐츠 기여 또는 교정/검토를 테스트하려면 어떻게 해야 하나요?
---
![github](assets/cover.webp)


## 요약


이 튜토리얼은 로컬 머신에서 Docker, 더미 키 및 사용자 지정 저장소 구성을 사용하여 Plan ₿ Network에서 Bitcoin 학습 관리 시스템을 설정하는 단계별 지침을 제공합니다.


위의 내용을 이해하지 못했더라도 걱정하지 마세요. 이 튜토리얼은 여러분을 위한 것입니다!


---

## **Bitcoin 학습 관리 시스템을 로컬에서 실행하는 방법**


이 튜토리얼에서는 플랫폼을 설정하고, 더미 키를 처리하고, 리포지토리를 사용자 지정하는 자세한 단계를 제공합니다. 아래 단계에 따라 일반적인 문제를 방지하고 로컬 환경을 올바르게 구성하세요.



**1. 전제 조건**


- 도커 및 도커 컴포즈가 설치된 Linux 시스템(윈도우에서도 작동하는 것으로 보고됨).
- 충분한 `nodejs` 버전(테스트 완료: 22.12.0)
- 시스템에 `pnpm`이 설치되어 있어야 합니다.
- 리포지토리 복제를 위해 Git을 구성했습니다.



**2. 리포지토리 복제**

리포지토리를 로컬 머신에 복제합니다:


git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-학습 관리 시스템


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. 환경 변수 설정**


1\. .env.example` 파일을 복제합니다:


```bash
cp .env.example .env
```


1. .env` 파일을 편집하여 이름에서 .example 부분을 삭제하고 이제 필수 변수에 대한 더미 키를 포함해야 합니다. 예시:


⚠️ 이 단계는 필수 단계이며 건너뛰면 일부 컨테이너 간 연결이 거부되는 등의 오류가 발생할 수 있습니다.


파일에 전용 Github PAT도 추가하는 것을 잊지 마세요



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. 설치 종속성**


적합한 nodejs 버전을 설치했는지 '반드시' 확인하세요. 2024-12 기준, v22.12.0(LTS)이 작동하는 것으로 입증되었습니다.



⚠️ 우분투 22.04 리포지토리 nodejs 버전이 12.22.9: 너무 오래되어 pnpm을 설치할 수 없습니다



Nodejs를 설치하려면 [여기](https://nodejs.org/en/download/package-manager)에서 지침을 참조하세요(예: `nvm` 설치 방법을 사용할 수 있습니다).


---

필요한 패키지의 pnpm 설치 단계를 시작하기 전에 모든 종속성이 설치되어 있는지 확인해야 하며, 다음 명령을 실행하여 이를 수행할 수 있습니다:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

./Bitcoin-learning-management-system/` 폴더에서 다음 명령을 실행하여 `pnpm`을 설치합니다


```bash
pnpm install
```


팁:__종속성과 pnpm 자체를 수시로 업데이트하는 것을 잊지 마세요



**5. 컨테이너 실행**

./Bitcoin-learning-management-system/` 폴더에서 Docker로 개발 환경을 시작합니다:


```bash
docker compose up --build -V
```

다음 명령도 이 방법으로 실행하면 터미널에 로그가 표시되지 않습니다.

```bash
docker compose up -d --build -V
```


이렇게 하면 도커에서 필요한 모든 컨테이너가 빌드되고 시작됩니다.


**6. 애플리케이션에 액세스**

컨테이너가 실행되면 다음 주소에서 프론트엔드에 액세스합니다:

<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Academy Local](assets/en/1.webp)


참고: 소스 파일을 변경하면 앱이 자동으로 다시 로드됩니다.



**7.** 데이터베이스 설정 Schema


처음 실행할 때는 DB 마이그레이션을 실행해야 합니다.


이렇게 하려면 마이그레이션 스크립트를 실행합니다: 'pnpm 실행 dev:db:마이그레이트'


```markdown
pnpm run dev:db:migrate
```


**8. 리포지토리에서 데이터 가져오기**

데이터를 데이터베이스로 가져오려면 API에 요청합니다:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. 동기화 볼륨 액세스 문제 수정**

Cdn` 및 `sync` 볼륨에 액세스 문제가 발생하면 실행하세요:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


그리고 다시


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Academy Local](assets/en/2.webp)



**10. 리포지토리 사용자 지정(선택 사항)**

Fork 또는 특정 지점을 사용해야 하는 경우:

1. .env` 파일을 편집하여 다음 변수를 업데이트합니다:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. 도커를 재시작합니다:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. 리포지토리 데이터를 다시 동기화합니다:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


이 튜토리얼은 플랫폼이 더미 키, 종속성 설치, 필요에 따라 사용자 지정한 리포지토리로 올바르게 설정되었는지 확인합니다. 설정에 행운을 빕니다!


**추가 도움말 요청**


모든 컨테이너 중지


```
docker compose down
```


기존 컨테이너와 볼륨을 모두 정리합니다


```
docker container prune -f
docker volume prune --all
```


공식 가이드에 사용된 것과 동일한 명령어로 컨테이너를 다시 생성하고 동기화 스크립트를 실행합니다:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```