---
name: مشارکت - آموزش Git (پیشرفته)
description: راهنمای کاربران پیشرفته برای ارائه یک آموزش در مورد Plan ₿ Network با Git
---
![cover](assets/cover.webp)


قبل از دنبال کردن این آموزش در مورد اضافه کردن یک آموزش جدید، باید چند مرحله مقدماتی را تکمیل کرده باشید. اگر هنوز این کار را انجام نداده‌اید، لطفاً ابتدا به این آموزش مقدماتی نگاهی بیندازید و سپس به اینجا برگردید:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

شما قبلاً دارید:



- یک موضوع برای آموزش خود انتخاب کنید؛
- از طریق [گروه تلگرام](https://t.me/PlanBNetwork_ContentBuilder) یا paolo@planb.network با تیم Plan ₿ Network تماس گرفته شد؛
- ابزارهای مشارکت خود را انتخاب کنید.


در این آموزش برای کاربران با تجربه Git، ما به طور خلاصه مراحل کلیدی و دستورالعمل‌های اساسی برای ارائه یک آموزش جدید Plan ₿ Network را خلاصه خواهیم کرد. اگر با Git و GitHub آشنا نیستید، توصیه می‌کنم به جای آن یکی از این ۲ آموزش مفصل‌تر را دنبال کنید که شما را مرحله به مرحله راهنمایی می‌کند:



- متوسط (GitHub Desktop):


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- مبتدیان (وب Interface):


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## ابزارهای پیشنهادی


برای ویرایش فایل‌های Markdown:



- ابسیدین (رایگان، متن‌بسته)
- مارک تکست (رایگان، متن‌باز)
- Zettlr (رایگان، متن‌باز)
- Typora (نرم‌افزار پولی، ~€15، متن‌باز نیست)


برای گیت:



- گیت (رایگان، متن‌باز)
- GitHub Desktop (رایگان، متن‌باز)
- Sourcetree (رایگان، متن‌بسته)


برای ویرایش فایل‌های YAML:



- ویژوال استودیو کد (رایگان، متن‌باز)
- Sublime Text (رایگان با محدودیت‌ها، متن‌باز نیست)


برای ایجاد نمودارها و تصاویر:



- Canva (رایگان با گزینه‌های پولی، متن‌باز نیست)
- اینک‌اسکیپ (رایگان، متن‌باز)
- پنپات (رایگان، متن‌باز)


## گردش‌کارها


### ۱ - محیط محلی خود را پیکربندی کنید



- شما باید Fork خود را از [مخزن Plan ₿ Network در GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content) داشته باشید.
- شاخه اصلی (`dev`) از Fork خود را با مخزن منبع همگام‌سازی کنید.
- کلون محلی خود را به‌روزرسانی کنید.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### ۲ - ایجاد یک شاخه جدید



- مطمئن شوید که روی شاخه `dev` هستید.
- یک شاخه جدید با یک نام توصیفی ایجاد کنید (مثلاً `tuto-Green-Wallet-loic`).
- این شاخه را در Fork آنلاین خود منتشر کنید.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### ۳ - اسناد آموزشی را اضافه کنید


***توجه:*** شما می‌توانید مراحل ۳ و ۴ را با استفاده از [اسکریپت GUI پایتون من](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation) خودکار کنید. آن را مستقیماً از پوشه‌اش در کلون محلی خود اجرا کنید، سپس فیلدهای مورد نیاز را در GUI پر کنید. برای اطلاعات بیشتر در مورد نحوه نصب و استفاده از آن، به [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md) مراجعه کنید.


اگر ترجیح می‌دهید به صورت دستی انجام دهید، این مراحل را دنبال کنید:



- پوشه مناسب را در مخزن محلی پیدا کنید (مثلاً `tutorials/Wallet`).
- یک دایرکتوری اختصاصی برای آموزش با یک نام واضح ایجاد کنید (مثلاً `gw-14-gw-13`). این نام پوشه همچنین مسیر URL آموزش را تعیین خواهد کرد. باید به حروف کوچک، بدون کاراکترهای ویژه (به جز خط تیره) و بدون فاصله باشد.
- موارد زیر را به این فهرست اضافه کنید:
    - یک زیرپوشه به نام `assets` که شامل:
        - دو تصویر `.webp`:
            - `logo.webp`: لوگوی آموزش (فرمت مربعی با پس‌زمینه). این لوگو باید نمایانگر نرم‌افزار یا ابزاری باشد که ارائه می‌شود. اگر آموزش به ابزار خاصی مربوط نیست (مثلاً: راهنمای کلی برای تولید عبارت Mnemonic)، می‌توانید یک تصویر مناسب انتخاب کنید (مثلاً: یک آیکون عمومی).
            - `cover.webp`: تصویری از جلد که در ابتدای آموزش نمایش داده می‌شود.
        - یک زیرپوشه با کد زبان اصلی آموزش. به عنوان مثال، اگر آموزش به زبان انگلیسی نوشته شده باشد، این زیرپوشه باید `en` نامگذاری شود. تمام تصاویر آموزشی (نمودارها، تصاویر، اسکرین‌شات‌ها، و غیره) را در این پوشه قرار دهید.
    - یک فایل `tutorial.yml` که شامل متادیتا (نویسنده، برچسب‌ها، دسته‌بندی، سطح دشواری و غیره) است.
    - فایلی با فرمت Markdown که حاوی آموزش است و بر اساس کد زبان نام‌گذاری شده است (مثلاً `fr.md`، `en.md`، و غیره).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### ۴ - فایل YAML را پر کنید



- فایل `tutorial.yml` را به صورت زیر تکمیل کنید:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


در اینجا فیلدهای مورد نیاز آمده است:



- شناسه**: یک UUID (_شناسه منحصربه‌فرد جهانی_) که به‌طور منحصربه‌فرد آموزش را شناسایی می‌کند. می‌توانید آن را با استفاده از [یک ابزار آنلاین](https://www.uuidgenerator.net/version4) به generate تبدیل کنید. تنها شرط این است که این UUID تصادفی باشد تا از تداخل با UUID دیگری در پلتفرم جلوگیری شود؛



- project_id**: شناسه UUID شرکت یا سازمان پشت ابزار ارائه‌شده در آموزش [از لیست پروژه‌ها](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). به عنوان مثال، اگر در حال ایجاد یک آموزش درباره نرم‌افزار Green Wallet هستید، می‌توانید این `project_id` را در فایل زیر پیدا کنید: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. این اطلاعات به فایل YAML آموزش شما اضافه می‌شود زیرا Plan ₿ Network یک پایگاه داده از تمام شرکت‌ها و سازمان‌هایی که بر روی Bitcoin یا پروژه‌های مرتبط فعالیت می‌کنند، نگهداری می‌کند. با افزودن `project_id` موجودیت مرتبط با آموزش شما، یک پیوند بین دو Elements ایجاد می‌کنید؛



- برچسب‌ها**: 2 یا 3 کلمه کلیدی مرتبط با محتوای آموزش، به‌طور انحصاری انتخاب شده [از لیست برچسب‌های Plan ₿ Network](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md)؛



- دسته‌بندی**: زیرمجموعه‌ای که با محتوای آموزشی مطابقت دارد، بر اساس ساختار وب‌سایت Plan ₿ Network (برای مثال، برای کیف پول‌ها: `desktop`, `hardware`, `mobile`, `backup`);



- سطح**: سطح دشواری آموزش، انتخاب شده از:
    - `مبتدی`
    - `متوسط`
    - `پیشرفته`
    - `کارشناس`



- professor_id**: `professor_id` (UUID) شما همانطور که در [پروفایل استاد شما](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) نمایش داده شده است؛



- زبان_اصلی**: زبان اصلی آموزش (مثلاً، `fr`، `en`، و غیره)؛



- بازخوانی**: اطلاعاتی درباره فرآیند بازخوانی. بخش اول را کامل کنید، زیرا بازخوانی آموزش خودتان به عنوان اولین اعتبارسنجی محسوب می‌شود:
    - زبان**: کد زبان برای تصحیح (مثلاً، `fr`، `en`، و غیره).
    - last_contribution_date**: تاریخ روز.
    - فوریت**: 1
    - نام‌های_مشارکت‌کننده**: شناسه GitHub شما.
    - پاداش**: 0


برای جزئیات بیشتر در مورد شناسه معلم خود، لطفاً به آموزش مربوطه مراجعه کنید:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


### ۵ - محتوا را بنویسید



- ویژگی‌های فایل Markdown را کامل کنید با:
    - عنوان (`name`).
    - توضیح کوتاه (`description`).
- تصویر جلد را در بالای آموزش با استفاده از نحو Markdown اضافه کنید (عبارت "Green" را با نام ابزار نشان داده شده جایگزین کنید):


```
![cover-green](assets/cover.webp)
```



- آموزش نوشتن محتوا در Markdown:
    - از عناوین ساختارمند (`##`)، لیست‌ها و پاراگراف‌ها به خوبی استفاده کنید.
    - تصاویر را با استفاده از نحو Markdown وارد کنید:


```
![nom-image](assets/en/001.webp)
```




- دایگرام‌ها و تصاویر را در زیرپوشه زبان مربوطه، در `/assets` قرار دهید.


### ۶ - آموزش را ذخیره و ارسال کنید



- تغییرات خود را با ایجاد یک کامیت با یک پیام توصیفی به صورت محلی ذخیره کنید.
- تغییرات را به GitHub خود Fork ارسال کنید.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- پس از اتمام، یک درخواست کشش (PR) در GitHub ایجاد کنید تا پیشنهاد ادغام تغییرات خود را ارائه دهید.
- یک عنوان و توضیح مختصر به PR اضافه کنید. شماره مسئله مربوطه را در نظرها ذکر کنید.


### ۷ - ویرایش و ادغام



- منتظر اعتبارسنجی یا بازخورد از یک مدیر باشید.
- در صورت لزوم، اصلاحات را انجام داده و کامیت‌های جدید را اعمال کنید.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- پس از ادغام PR، می‌توانید شاخه کاری خود را حذف کنید.


## استانداردهای ایجاد محتوا



- قالب‌بندی پشتیبانی شده در پلتفرم**:
    - کلاسیک مارک‌داون: لیست‌ها، لینک‌ها، تصاویر، نقل‌قول‌ها، **بولد**، *ایتالیک*، و غیره.
    - LaTeX (فقط بلوک، نه درون‌خطی): با `$$` محدود شده است.
    - کد درون‌خطی: نحو با یک بک‌تیک.
    - بلوک‌های کد: نحو با سه بک‌تیک، به عنوان مثال:


```
print("Hello, Bitcoin!")
```



- تصاویر و نمودارها**:
    - همه تصاویر باید در قالب WebP باشند. در صورت نیاز از این ابزار رایگان برای تبدیل آنها استفاده کنید: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - نام تصاویر با ۲ یا ۳ رقم (مثلاً `001.webp`, `002.webp`).
    - برای آموزش‌های موبایل یا Hardware Wallet، از ماک‌آپ‌ها استفاده کنید.
    - فقط از تصاویر ایجاد شده توسط خود یا بدون حق امتیاز استفاده کنید.
    - مطمئن شوید که آن‌ها مرتبط و با کیفیت بالا هستند.
- منشور گرافیکی**:
    - فونت: [روبیک](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - رنگ‌ها Plan ₿ Network:
        - نارنجی: `#FF5C00`
        - سیاه: `#000000`
        - سفید: `#FFFFFF`


اگر در ارسال آموزش خود با مشکلات فنی مواجه هستید، لطفاً در درخواست کمک از [گروه تلگرام اختصاصی ما برای مشارکت‌ها](https://t.me/PlanBNetwork_ContentBuilder) تردید نکنید. بسیار متشکریم!