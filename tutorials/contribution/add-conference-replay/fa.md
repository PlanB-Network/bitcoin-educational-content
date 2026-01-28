---
name: افزودن بازپخش کنفرانس
description: چگونه یک بازپخش کنفرانس را به شبکه PlanB اضافه کنیم؟
---
![conference](assets/cover.webp)


ماموریت PlanB ارائه منابع آموزشی درجه یک درباره Bitcoin به بیشترین زبان‌های ممکن است. تمام محتوای منتشر شده در سایت به صورت منبع باز است و در GitHub میزبانی می‌شود، که به هر کسی اجازه می‌دهد به غنی‌سازی این پلتفرم کمک کند.


آیا می‌خواهید بازپخش کنفرانس Bitcoin خود را در سایت شبکه PlanB اضافه کنید و به این رویداد دیده‌شدن بدهید، اما نمی‌دانید چگونه؟ این آموزش برای شماست!


با این حال، اگر می‌خواهید کنفرانسی را که در آینده برگزار خواهد شد اضافه کنید، به شما توصیه می‌کنم این آموزش دیگر را بخوانید که در آن توضیح می‌دهیم چگونه یک رویداد جدید به سایت اضافه کنید.


https://planb.academy/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- اول، شما نیاز دارید که یک حساب کاربری در GitHub داشته باشید. اگر نمی‌دانید چگونه یک حساب کاربری ایجاد کنید، ما یک آموزش جامع برای راهنمایی شما تهیه کرده‌ایم.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- به [مخزن GitHub مربوط به PlanB که به داده‌ها اختصاص دارد](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) در بخش `resources/conference/` بروید:

![conference](assets/02.webp)


- در بالا سمت راست روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![conference](assets/03.webp)


- اگر تا به حال به محتوای شبکه PlanB کمک نکرده‌اید، نیاز دارید که Fork مخزن اصلی را ایجاد کنید. فورک کردن یک مخزن به معنای ایجاد یک کپی از آن مخزن در حساب GitHub خودتان است که به شما اجازه می‌دهد روی پروژه کار کنید بدون اینکه مخزن اصلی تحت تأثیر قرار گیرد. روی دکمه `Fork this repository` کلیک کنید:

![conference](assets/04.webp)


- سپس به صفحه ویرایش GitHub خواهید رسید:

![conference](assets/05.webp)


- پوشه‌ای برای کنفرانس خود ایجاد کنید. برای این کار، در کادر `Name your file...`، نام کنفرانس خود را با حروف کوچک و به جای فاصله از خط تیره استفاده کنید. برای مثال، اگر کنفرانس شما "Paris Bitcoin Conference" نام دارد، باید `paris-Bitcoin-conference` را یادداشت کنید. همچنین سال کنفرانس خود را اضافه کنید، برای مثال: `paris-Bitcoin-conference-2024`:

![conference](assets/06.webp)


- برای تأیید ایجاد پوشه، به سادگی یک اسلش بعد از نام خود در همان کادر یادداشت کنید، به عنوان مثال: `paris-Bitcoin-conference-2024/`. افزودن یک اسلش به طور خودکار یک پوشه ایجاد می‌کند نه یک فایل:

![conference](assets/07.webp)


- در این پوشه، شما یک فایل YAML به نام `conference.yml` ایجاد خواهید کرد:

![conference](assets/08.webp)

این فایل را با اطلاعات مربوط به کنفرانس خود با استفاده از این الگو پر کنید:

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


به عنوان مثال، فایل YAML شما می‌تواند به این شکل باشد:


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


اگر هنوز شناسه "*سازنده*" برای سازمان خود ندارید، می‌توانید با دنبال کردن این آموزش دیگر آن را اضافه کنید.


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- پس از اتمام ایجاد تغییرات در این فایل، آن‌ها را با کلیک بر روی دکمه `Commit changes...` ذخیره کنید:

![conference](assets/10.webp)


- یک عنوان برای تغییرات خود اضافه کنید، به همراه یک توضیح کوتاه:

![conference](assets/11.webp)


- روی دکمه `Propose changes` در Green کلیک کنید:

![conference](assets/12.webp)


- سپس به صفحه‌ای خواهید رسید که خلاصه‌ای از تمام تغییرات شما را نشان می‌دهد:

![conference](assets/13.webp)


- روی تصویر پروفایل GitHub خود در بالا سمت راست کلیک کنید، سپس روی `Your Repositories`:

![conference](assets/14.webp)


- Fork خود را از مخزن Plan ₿ Academy انتخاب کنید:

![conference](assets/15.webp)


- باید یک اعلان در بالای پنجره با شاخه جدید خود ببینید. احتمالاً به نام `patch-1` است. روی آن کلیک کنید:

![conference](assets/16.webp)


- شما اکنون در شاخه کاری خود هستید:

![conference](assets/17.webp)


- به پوشه `resources/conference/` بازگردید و پوشه کنفرانسی را که در تعهد قبلی خود ایجاد کرده‌اید، انتخاب کنید:

![conference](assets/18.webp)


- در پوشه کنفرانس خود، روی دکمه `Add file` کلیک کنید، سپس روی `Create new file` کلیک کنید:

![conference](assets/19.webp)


- نام این پوشه جدید را `assets` بگذارید و با گذاشتن یک اسلش `/` در انتها، ایجاد آن را تأیید کنید:

![conference](assets/20.webp)


- در این پوشه `assets`، فایلی با نام `.gitkeep` ایجاد کنید:

![conference](assets/21.webp)


- روی دکمه `Commit changes...` کلیک کنید:

![conference](assets/22.webp)


- عنوان کامیت را به صورت پیش‌فرض بگذارید و مطمئن شوید که گزینه `Commit directly to the patch-1 branch` تیک خورده است، سپس روی `Commit changes` کلیک کنید:

![conference](assets/23.webp)


- بازگشت به پوشه `assets`:

![conference](assets/24.webp)


- روی دکمه `افزودن فایل` کلیک کنید، سپس روی `بارگذاری فایل‌ها`:

![conference](assets/25.webp)


- صفحه جدیدی باز خواهد شد. تصویری را که نمایانگر کنفرانس شماست بکشید و رها کنید و در سایت شبکه PlanB نمایش داده خواهد شد: ![conference](assets/26.webp)
- می‌تواند یک لوگو، یک تصویر بندانگشتی، یا حتی یک پوستر باشد:

![conference](assets/27.webp)


- هنگامی که تصویر بارگذاری شد، بررسی کنید که گزینه `Commit directly to the patch-1 branch` علامت‌گذاری شده باشد، سپس روی `Commit changes` کلیک کنید:

![conference](assets/28.webp)


- مراقب باشید، تصویر شما باید با نام `thumbnail` و در قالب `.webp` باشد. بنابراین نام کامل فایل باید به این صورت باشد: `thumbnail.webp`:

![conference](assets/29.webp)


- به پوشه `assets` خود بازگردید و روی فایل واسطه `.gitkeep` کلیک کنید:

![conference](assets/30.webp)


- پس از باز کردن فایل، روی ۳ نقطه کوچک در گوشه بالا سمت راست کلیک کنید و سپس روی `Delete file`:

![conference](assets/31.webp)


- تأیید کنید که هنوز در همان شاخه کاری هستید، سپس روی دکمه `Commit changes` کلیک کنید:

![conference](assets/32.webp)


- به تعهد خود عنوان و توضیح اضافه کنید، سپس روی `Commit changes` کلیک کنید:

![conference](assets/33.webp)


- به پوشه کنفرانس خود برگردید:

![conference](assets/34.webp)


- روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![conference](assets/35.webp)


- یک فایل جدید مارک‌داون (.md) ایجاد کنید و آن را با نشانگر زبان مادری خود نام‌گذاری کنید. این فایل برای بازپخش‌های کنفرانس شما استفاده خواهد شد. به عنوان مثال، اگر بخواهم توضیحات کنفرانس‌ها را به انگلیسی بنویسم، این فایل را en.md نام‌گذاری خواهم کرد.

![conference](assets/36.webp)


- این فایل مارک‌داون را با استفاده از این قالب که می‌توانید برای تنظیمات کنفرانس خود تطبیق دهید، پر کنید:


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


- در ابتدای سند خود، در بخش "اطلاعات اولیه"، فیلد `name:` را با نام کنفرانس و سال بازپخش‌ها پر کنید. در فیلد `description:`، توضیح کوتاهی از رویداد خود به زبان فایل بنویسید. به عنوان مثال، برای فایلی با نام `en.md`، توضیحات باید به زبان انگلیسی باشد. تیم شبکه PlanB مسئولیت ترجمه توضیحات شما را با استفاده از مدل خود بر عهده خواهد داشت.
- عناوین سطح اول، که با `#` مشخص شده‌اند، برای سازماندهی کنفرانس بر اساس صحنه‌ها استفاده می‌شوند. به عنوان مثال، `# Main Stage` برای صحنه اصلی و `# Workshop Room` برای صحنه‌ای که به کارگاه‌ها اختصاص داده شده است.



- عناوین سطح دوم، که با دو `##` مشخص شده‌اند، برای جدا کردن ویدیوهای بازپخش مختلف استفاده می‌شوند. اگر کنفرانس‌ها به‌طور پیوسته در طول نیم‌روز فیلم‌برداری شده‌اند، به‌عنوان مثال، `## صبح جمعه` را نشان دهید. اگر کنفرانس‌ها به‌صورت جداگانه فیلم‌برداری و پخش شده‌اند، نام کنفرانس را مستقیماً با عنوان سطح دوم ذکر کنید.



- زیر هر عنوان سطح دوم، لینکی به ویدئوی بازپخش مربوطه قرار دهید. نحو باید به این صورت باشد: `![video](https://youtu.be/XXXXXXXXXXXX)`، که در آن `XXXXXXXXXXXX` با لینک واقعی ویدئو جایگزین شود.



- اگر قالب اجازه می‌دهد (کنفرانس‌های فردی)، می‌توانید نام سخنرانان را اضافه کنید. برای این کار، فیلد `Speaker:` را به همراه نام یا نام مستعار سخنران زیر لینک ویدیو اضافه کنید. در صورت وجود چندین سخنران، هر نام را با کاما جدا کنید، به عنوان مثال: `Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- پس از اتمام تغییرات خود در این فایل، آن‌ها را با کلیک بر روی دکمه `Commit changes...` ذخیره کنید:

![conference](assets/38.webp)


- برای تغییرات خود یک عنوان اضافه کنید، همچنین یک توضیح کوتاه:

![conference](assets/39.webp)


- روی `Commit changes` کلیک کنید:

![conference](assets/40.webp)


- پوشه کنفرانس شما اکنون باید به این شکل باشد:

![conference](assets/41.webp)


- اگر همه چیز رضایت‌بخش است، به ریشه Fork خود بازگردید:

![conference](assets/42.webp)


- شما باید پیامی ببینید که نشان می‌دهد شاخه شما دستخوش تغییراتی شده است. روی دکمه `Compare & pull request` کلیک کنید:

![conference](assets/43.webp)


- یک عنوان و توضیح واضح برای PR خود اضافه کنید:

![conference](assets/44.webp)


- روی دکمه `Create pull request` کلیک کنید:

![conference](assets/45.webp)

تبریک می‌گوییم! درخواست شما با موفقیت ایجاد شد. اکنون یک مدیر آن را بررسی خواهد کرد و در صورت صحیح بودن، آن را در مخزن اصلی شبکه PlanB ادغام خواهد کرد. شما باید چند روز بعد بازپخش‌های کنفرانس خود را در وب‌سایت مشاهده کنید.


لطفاً مطمئن شوید که پیشرفت PR خود را دنبال می‌کنید. ممکن است یک مدیر نظر بگذارد و اطلاعات بیشتری بخواهد. تا زمانی که PR شما تأیید نشده است، می‌توانید آن را تحت زبانه `Pull requests` در مخزن GitHub شبکه PlanB مشاهده کنید:

![conference](assets/46.webp)


خیلی ممنون از مشارکت ارزشمند شما! :)
