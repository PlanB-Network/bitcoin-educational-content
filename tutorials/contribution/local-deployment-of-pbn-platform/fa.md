---
name: راهنمای اجرای محلی پلتفرم Plan ₿ Academy
description: چگونه می‌توان Plan ₿ Academy را در یک محیط محلی اجرا کرد تا مشارکت محتوایی یا ویرایش/بازبینی محتوای آموزشی خود را بر روی Plan ₿ Academy آزمایش کنم؟
---
![github](assets/cover.webp)


## به طور خلاصه


این آموزش دستورالعمل‌های گام‌به‌گام برای راه‌اندازی سیستم مدیریت یادگیری Bitcoin از Plan ₿ Academy بر روی ماشین محلی شما با استفاده از Docker، کلیدهای ساختگی و پیکربندی‌های مخزن سفارشی را ارائه می‌دهد.


اگر بخش بالا را متوجه نشدید، نگران نباشید—این آموزش برای شماست!


---

## **چگونه سیستم مدیریت یادگیری Bitcoin را به صورت محلی اجرا کنیم**


این آموزش مراحل دقیقی برای راه‌اندازی پلتفرم، مدیریت کلیدهای ساختگی، و سفارشی‌سازی مخازن ارائه می‌دهد. مراحل زیر را دنبال کنید تا از مشکلات رایج جلوگیری کرده و محیط محلی خود را به درستی پیکربندی کنید.



**1. پیش‌نیازها**


- ماشین لینوکس با Docker و Docker Compose نصب شده (گزارش شده که روی ویندوز هم کار می‌کند).
- نسخه `nodejs` کافی (آزمایش شده: 22.12.0)
- `pnpm` بر روی سیستم شما نصب شده است.
- گیت برای کلون کردن مخازن پیکربندی شده است.



**۲. مخزن را کلون کنید**

مخزن را به دستگاه محلی خود کلون کنید:


git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. تنظیم متغیرهای محیطی**


۱. فایل `.env.example` را کپی کنید:


```bash
cp .env.example .env
```


۱. فایل `.env` را ویرایش کنید و قسمت .example را از نام حذف کنید، اکنون باید کلیدهای ساختگی برای متغیرهای مورد نیاز وارد کنید. مثال:


⚠️ این یک مرحله اجباری است، رد کردن آن منجر به خطاهایی مانند رد اتصال بین برخی از کانتینرها خواهد شد.


فراموش نکنید که PAT اختصاصی Github خود را نیز به فایل اضافه کنید.



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**۴. وابستگی‌ها را نصب کنید**


`مطمئن شوید` که یک نسخه مناسب از nodejs نصب کرده‌اید. از 2024-12، نسخه v22.12.0 (LTS) اثبات شده که کار می‌کند.



⚠️ نسخه nodejs در مخزن Ubuntu 22.04 برابر با 12.22.9 است: برای نصب pnpm بسیار قدیمی است.



برای نصب nodejs، دستورالعمل‌ها را [اینجا](https://nodejs.org/en/download/package-manager) پیدا کنید؛ به عنوان مثال، ممکن است بخواهید از روش نصب `nvm` استفاده کنید.


---

قبل از شروع مرحله نصب pnpm برای بسته‌های ضروری، مطمئن شوید که همه وابستگی‌ها نصب شده‌اند، می‌توانید این کار را با اجرای دستور زیر انجام دهید:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

داخل پوشه `../Bitcoin-learning-management-system/` خود، فرمان زیر را برای نصب `pnpm` اجرا کنید.


```bash
pnpm install
```


__نکته:__ به یاد داشته باشید که هم وابستگی‌ها و هم خود pnpm را هر از گاهی به‌روزرسانی کنید



**5. اجرای کانتینرها**

داخل پوشه `../Bitcoin-learning-management-system/` خود، محیط توسعه را با Docker شروع کنید:


```bash
docker compose up --build -V
```

شما همچنین این فرمان بعدی را به این صورت اجرا کنید، لاگ‌ها را در ترمینال خود نخواهید دید.

```bash
docker compose up -d --build -V
```


این تمام کانتینرهای لازم را از داکرها ساخته و راه‌اندازی خواهد کرد.


**6. به برنامه دسترسی پیدا کنید**

پس از اجرای کانتینرها، به فرانت‌اند در اینجا دسترسی پیدا کنید:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Academy Local](assets/en/1.webp)


توجه: اگر هر یک از فایل‌های منبع را تغییر دهید، برنامه به‌طور خودکار بارگذاری مجدد خواهد شد.



**7.** پایگاه داده خود را Schema تنظیم کنید


در اولین اجرا، نیاز خواهید داشت که مهاجرت‌های DB را اجرا کنید.


برای انجام این کار، اسکریپت مهاجرت را اجرا کنید: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**۸. وارد کردن داده‌ها از مخزن**

برای وارد کردن داده‌ها به پایگاه داده، یک درخواست به API ارسال کنید:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. رفع مشکلات دسترسی به حجم همگام‌سازی**

اگر با مشکلات دسترسی به حجم‌های `cdn` و `sync` مواجه شدید، اجرا کنید:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


سپس دوباره:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Academy Local](assets/en/2.webp)



**10. سفارشی‌سازی مخزن (اختیاری)**

اگر نیاز به استفاده از Fork یا یک شاخه خاص دارید:

1. فایل `.env` را ویرایش کنید تا متغیرهای زیر را به‌روزرسانی کنید:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


۲. داکر را مجدداً راه‌اندازی کنید:


```markdown
docker compose down -v
docker compose up --build -V
```


۳. داده‌های مخزن را دوباره همگام‌سازی کنید:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


این آموزش اطمینان حاصل می‌کند که پلتفرم به درستی با کلیدهای آزمایشی تنظیم شده، وابستگی‌ها نصب شده و مخازن به صورت دلخواه سفارشی شده‌اند. 🎉 موفق باشید با تنظیمات خود!


**دستورات برای کمک اضافی**


تمام کانتینرها را متوقف کن


```
docker compose down
```


همه کانتینرها و حجم‌های موجود را هرس کنید


```
docker container prune -f
docker volume prune --all
```


بازسازی کانتینرها با استفاده از همان دستوری که در راهنمای رسمی استفاده شده و اجرای اسکریپت همگام‌سازی:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```