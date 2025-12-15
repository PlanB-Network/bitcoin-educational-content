---
name: Ръководство за управление на платформата Plan ₿ Academy на местно ниво
description: Как можете да стартирате Академията на Plan ₿ в локална среда, за да тествате моя принос към съдържанието или корекция/преглед на образователното съдържание в Академията на Plan ₿?
---
![github](assets/cover.webp)


## В резюме


Това ръководство предоставя инструкции стъпка по стъпка за настройка на системата за управление на обучение Bitcoin от Plan ₿ Academy на вашата локална машина с помощта на Docker, фиктивни ключове и персонализирани конфигурации на хранилището.


Ако не сте разбрали горната част, не се притеснявайте - този урок е за вас!


---

## **Как да стартирате локално системата за управление на обучение Bitcoin**


Този урок съдържа подробни стъпки за настройка на платформата, работа с фиктивни ключове и персонализиране на хранилищата. Следвайте стъпките по-долу, за да избегнете често срещани проблеми и да конфигурирате правилно локалната си среда.



**1. Предварителни условия**


- Linux машина с инсталирани Docker и Docker Compose (съобщава се, че работи и под Windows).
- достатъчна версия на `nodejs` (тествана: 22.12.0)
- `pnpm`, инсталиран на вашата система.
- Git е конфигуриран за клониране на хранилища.



**2. Клониране на хранилището**

Клонирайте хранилището на локалната си машина:


git clone [https://github.com/PlanB-Network/bitcoin-learning-management-system](https://github.com/PlanB-Network/bitcoin-learning-management-system￼cd)

[CD](https://github.com/PlanB-Network/bitcoin-learning-management-system￼cd) bitcoin-learning-management-system


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. Настройка на променливите на средата**


1\. Дублирайте файла `.env.example`:


```bash
cp .env.example .env
```


1. Редактирайте файла `.env`, като изтриете частта .example от името, сега трябва да включите фиктивни ключове за необходимите променливи. Пример:


⚠️ Това е задължителна стъпка, пропускането ѝ ще доведе до грешки, като например отказ на връзка между някои от контейнерите.


Не забравяйте да добавите и своя специален Github PAT във файла



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. Инсталиране на зависимости**


уверете се, че сте инсталирали подходяща версия на nodejs. Към 2024-12 е доказано, че v22.12.0 (LTS) работи.



⚠️ Ubuntu 22.04 хранилище версията на nodejs е 12.22.9: твърде стара, за да ви позволи да инсталирате pnpm



За да инсталирате nodejs, намерете инструкции [тук](https://nodejs.org/en/download/package-manager); например можете да изберете да използвате метода за инсталиране `nvm`.


---

Преди да стартирате фазата на инсталиране на необходимите пакети, уверете се, че всички зависимости са инсталирани, което можете да постигнете, като изпълните следната команда:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

Вътре в папката `../bitcoin-learning-management-system/` изпълнете следната команда, за да инсталирате `pnpm`


```bash
pnpm install
```


__TIP:__Не забравяйте да актуализирате от време на време както зависимостите, така и самия pnpm



**5. Изпълнение на контейнерите**

В папката си `../bitcoin-learning-management-system/` стартирайте средата за разработка с Docker:


```bash
docker compose up --build -V
```

Изпълнявайте и тази следваща команда по този начин, но няма да виждате дневниците в терминала си.

```bash
docker compose up -d --build -V
```


Това ще изгради и стартира всички необходими контейнери от dockers.


**6. Достъп до приложението**

След като контейнерите са стартирани, осъществете достъп до фронтенда на адрес:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Academy Local](assets/en/1.webp)


Обърнете внимание, че приложението ще се презареди автоматично, ако промените изходните файлове.



**7.** Създаване на схема на базата данни


При първото стартиране ще трябва да стартирате миграциите на БД.


За целта стартирайте скрипта за миграция: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. Импортиране на данни от хранилището**

За да импортирате данни в базата данни, направете заявка в API:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. Отстраняване на проблеми с достъпа до обема на синхронизация**

Ако срещнете проблеми с достъпа до томовете `cdn` и `sync`, изпълнете:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


след това отново:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Academy Local](assets/en/2.webp)



**10. Персонализиране на хранилището (по избор)**

Ако трябва да използвате fork или конкретен клон:

1. Редактирайте файла `.env`, за да актуализирате следните променливи:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Рестартирайте Docker:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. Синхронизирайте отново данните в хранилището:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


Този урок гарантира, че платформата е правилно настроена с фиктивни ключове, инсталирани са зависимости и хранилищата са персонализирани според нуждите. 🎉 Успех с настройката!


**Команди за допълнителна помощ**


спиране на всички контейнери


```
docker compose down
```


изрязване на всички съществуващи контейнери и обеми


```
docker container prune -f
docker volume prune --all
```


пресъздайте контейнерите със същата команда, използвана в официалното ръководство, и стартирайте скрипта за синхронизация:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```