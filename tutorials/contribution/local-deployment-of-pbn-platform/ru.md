---
name: Руководство по локальному запуску платформы Plan ₿ Network
description: Как можно запустить Plan ₿ Network в локальной среде, чтобы проверить мой вклад в контент или корректуру/рецензирование образовательного контента на Plan ₿ Network?
---
![github](assets/cover.webp)

## В кратком изложении

Это руководство содержит пошаговые инструкции по настройке системы управления обучением Bitcoin из Plan ₿ Network на локальной машине с помощью Docker, фиктивных ключей и пользовательских конфигураций репозиториев.

Если вы не поняли, что написано выше, не волнуйтесь - этот урок для вас!

---
## **Как запустить систему управления обучением Bitcoin локально**

В этом руководстве подробно описаны шаги по настройке платформы, работе с фиктивными ключами и настройке репозиториев. Следуйте приведенным ниже шагам, чтобы избежать распространенных проблем и правильно настроить локальную среду.

**1. Пререквизиты**


- Linux-машина с установленными Docker и Docker Compose (сообщалось, что они работают и на Windows).
- достаточная версия `nodejs` (проверено: 22.12.0)
- в вашей системе установлен `pnpm`.
- Git настроен для клонирования репозиториев.

**2. Клонирование репозитория**

Клонируйте репозиторий на свой локальный компьютер:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Настройка переменных окружения**

1\. Дублируйте файл `.env.example`:

```bash
cp .env.example .env
```

1. Отредактируйте файл `.env`, удалив часть имени .example, теперь вам нужно включить фиктивные ключи для необходимых переменных. Пример:

⚠️ Это обязательный шаг, его пропуск приведет к ошибкам, таким как отказ в соединении между некоторыми контейнерами.

Не забудьте также добавить в файл свой выделенный PAT на Github

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Установите зависимости**

убедитесь, что установлена подходящая версия nodejs. По состоянию на 2024-12 была доказана работоспособность версии 22.12.0 (LTS).

⚠️ Версия nodejs в репозитории Ubuntu 22.04 - 12.22.9: слишком старая, чтобы позволить вам установить pnpm

Чтобы установить nodejs, найдите инструкции [здесь](https://nodejs.org/en/download/package-manager); например, вы можете использовать метод установки `nvm`.

---
Перед началом этапа установки необходимых пакетов pnpm убедитесь, что все зависимости установлены, для этого выполните следующую команду:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Внутри папки `../Bitcoin-learning-management-system/` выполните следующую команду для установки `pnpm`

```bash
pnpm install
```

__TIP:__ Не забывайте время от времени обновлять как зависимости, так и сам pnpm

**5. Запустите контейнеры**

В папке `../Bitcoin-learning-management-system/` запустите среду разработки с помощью Docker:

```bash
docker compose up --build -V
```

Если вы выполните следующую команду таким образом, вы не увидите журналов в терминале.

```bash
docker compose up -d --build -V
```

Это позволит собрать и запустить все необходимые контейнеры из dockers.

**6. Доступ к приложению**

Когда контейнеры запущены, зайдите во фронтенд по адресу:

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Обратите внимание, что приложение автоматически перезагрузится, если вы измените какие-либо исходные файлы.

**7.** Настройте свою базу данных Schema

При первом запуске вам нужно будет запустить миграцию БД.

Для этого запустите скрипт миграции: `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Импорт данных из хранилища**

Чтобы импортировать данные в базу данных, сделайте запрос к API:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Устранение проблем с доступом к томам синхронизации**

Если у вас возникли проблемы с доступом к томам `cdn` и `sync`, выполните команду:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

но опять же:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Настройка репозитория (необязательно)**

Если вам нужно использовать Fork или определенную ветку:

1. Отредактируйте файл `.env`, чтобы обновить следующие переменные:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Перезапустите Docker:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Пересинхронизируйте данные хранилища:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Это руководство гарантирует, что платформа правильно настроена с фиктивными ключами, установлены зависимости и настроены репозитории по мере необходимости. 🎉 Удачи вам в настройке!

**Команды для дополнительной помощи*

остановить все контейнеры

```
docker compose down
```

обрезать все существующие контейнеры и объемы

```
docker container prune -f
docker volume prune --all
```

пересоздайте контейнеры с помощью той же команды, что использовалась в официальном руководстве, и скрипта синхронизации ланча:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
