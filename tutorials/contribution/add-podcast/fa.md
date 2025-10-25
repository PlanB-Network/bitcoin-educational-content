---
name: افزودن یک پادکست به شبکه PlanB
description: چگونه یک پادکست جدید به شبکه PlanB اضافه کنیم؟
---
![podcast](assets/cover.webp)


ماموریت PlanB ارائه منابع آموزشی درجه یک در مورد Bitcoin به بیشترین تعداد زبان ممکن است. تمام محتوای منتشر شده در سایت به صورت منبع باز است و در GitHub میزبانی می‌شود، که به هر کسی اجازه می‌دهد در غنی‌سازی این پلتفرم مشارکت کند.


آیا به دنبال اضافه کردن یک پادکست Bitcoin به سایت شبکه PlanB و افزایش دیده شدن برنامه خود هستید، اما نمی‌دانید چگونه؟ این آموزش برای شماست!

![podcast](assets/01.webp)


- ابتدا، شما نیاز به یک حساب GitHub دارید. اگر نمی‌دانید چگونه یکی بسازید، ما یک آموزش جامع برای راهنمایی شما تهیه کرده‌ایم.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- به [مخزن GitHub از PlanB که به داده‌ها اختصاص دارد](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts) در بخش `resources/podcasts/` بروید:

![podcast](assets/02.webp)


- در بالا سمت راست روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![podcast](assets/03.webp)


- اگر تا به حال به محتوای شبکه PlanB کمک نکرده‌اید، نیاز دارید که Fork مخزن اصلی را ایجاد کنید. فورک کردن یک مخزن به معنای ایجاد یک کپی از آن مخزن در حساب GitHub خودتان است که به شما اجازه می‌دهد روی پروژه کار کنید بدون اینکه مخزن اصلی تحت تأثیر قرار گیرد. روی دکمه `Fork this repository` کلیک کنید:

![podcast](assets/04.webp)


- سپس به صفحه ویرایش GitHub خواهید رسید:

![podcast](assets/05.webp)


- یک پوشه برای پادکست خود ایجاد کنید. برای این کار، در کادر `نام فایل خود را بنویسید...`، نام پادکست خود را با حروف کوچک و به جای فاصله از خط تیره استفاده کنید. به عنوان مثال، اگر برنامه شما "Super Podcast Bitcoin" نام دارد، باید بنویسید `super-podcast-Bitcoin`:

![podcast](assets/06.webp)


- برای اعتبارسنجی ایجاد پوشه، به‌سادگی یک اسلش بعد از نام پادکست خود در همان کادر اضافه کنید، به‌عنوان مثال: `super-podcast-Bitcoin/`. اضافه کردن یک اسلش به‌طور خودکار یک پوشه ایجاد می‌کند نه یک فایل:

![podcast](assets/07.webp)


- در این پوشه، شما یک فایل YAML به نام `podcast.yml` ایجاد خواهید کرد:

![podcast](assets/08.webp)


- این فایل را با اطلاعات مربوط به پادکست خود با استفاده از این الگو پر کنید:


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


در اینجا جزئیات برای پر کردن هر فیلد آمده است:



- **نام**: نام پادکست خود را مشخص کنید.
- **میزبان**: نام‌ها یا نام‌های مستعار سخنرانان یا میزبان پادکست را فهرست کنید. هر نام باید با کاما جدا شود.
- `language`: کد زبان زبانی را که در پادکست شما صحبت می‌شود مشخص کنید. به عنوان مثال، برای انگلیسی، `en` و برای ایتالیایی `it` را یادداشت کنید...



- **لینک‌ها**: لینک‌های محتوای خود را ارائه دهید. شما دو گزینه دارید:
 - `پادکست`: لینک به پادکست شما،
 - `twitter`: لینک پروفایل توییتر پادکست یا سازمان تولیدکننده آن،
 - `website`: لینک به وب‌سایت پادکست یا سازمان تولیدکننده آن.



- `description`: یک پاراگراف کوتاه اضافه کنید که پادکست شما را توصیف کند. توضیحات باید به همان زبانی باشد که در قسمت `language:` مشخص شده است.



- **برچسب‌ها**: دو برچسب مرتبط با پادکست خود اضافه کنید. مثال‌ها:
    - `Bitcoin`
    - `فناوری`
    - `اقتصاد`
    - `آموزش`...



- **مشارکت‌کنندگان**: در صورت داشتن، شناسه مشارکت‌کننده خود را ذکر کنید.


به عنوان مثال، فایل YAML شما می‌تواند به این شکل باشد:


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



- پس از اتمام ایجاد تغییرات در این فایل، آن‌ها را با کلیک بر روی دکمه `Commit changes...` ذخیره کنید:

![podcast](assets/10.webp)


- یک عنوان برای تغییرات خود اضافه کنید، همچنین یک توضیح کوتاه:

![podcast](assets/11.webp)


- روی دکمه `Propose changes` در Green کلیک کنید:

![podcast](assets/12.webp)


- سپس به صفحه‌ای خواهید رسید که تمام تغییرات شما را خلاصه می‌کند:

![podcast](assets/13.webp)


- روی تصویر پروفایل GitHub خود در بالا سمت راست کلیک کنید، سپس روی `Your Repositories`:

![podcast](assets/14.webp)


- مخزن Fork شبکه PlanB خود را انتخاب کنید:

![podcast](assets/15.webp)


- باید یک اعلان در بالای پنجره با شاخه جدید خود ببینید. احتمالاً به نام `patch-1` است. روی آن کلیک کنید:

![podcast](assets/16.webp)


- شما اکنون در شاخه کاری خود هستید:

![podcast](assets/17.webp)


- به پوشه `resources/podcast/` برگردید و پوشه پادکستی که در کامیت قبلی ایجاد کرده‌اید را انتخاب کنید: ![podcast](assets/18.webp)
- در پوشه پادکست خود، روی دکمه `افزودن فایل` کلیک کنید، سپس روی `ایجاد فایل جدید`:

![podcast](assets/19.webp)


- نام این پوشه جدید را `assets` بگذارید و با اضافه کردن یک اسلش `/` در انتها، ایجاد آن را تأیید کنید:

![podcast](assets/20.webp)


- در این پوشه `assets`، فایلی به نام `.gitkeep` ایجاد کنید:

![podcast](assets/21.webp)


- روی دکمه `Commit changes...` کلیک کنید:

![podcast](assets/22.webp)


- عنوان کامیت را به صورت پیش‌فرض بگذارید و مطمئن شوید که گزینه `Commit directly to the patch-1 branch` تیک خورده است، سپس روی `Commit changes` کلیک کنید:

![podcast](assets/23.webp)


- به پوشه `assets` بازگردید:

![podcast](assets/24.webp)


- روی دکمه `Add file` کلیک کنید، سپس روی `Upload files`:

![podcast](assets/25.webp)


- صفحه جدیدی باز خواهد شد. لوگوی پادکست خود را به ناحیه مورد نظر بکشید و رها کنید. این تصویر در سایت شبکه PlanB نمایش داده خواهد شد:

![podcast](assets/26.webp)


- مراقب باشید، تصویر باید مربع باشد تا بهترین تناسب را با وب‌سایت ما داشته باشد:

![podcast](assets/27.webp)


- پس از بارگذاری تصویر، اطمینان حاصل کنید که گزینه `Commit directly to the patch-1 branch` علامت‌دار شده است، سپس روی `Commit changes` کلیک کنید:

![podcast](assets/28.webp)


- مراقب باشید، تصویر شما باید با نام `logo` و در فرمت `.webp` باشد. بنابراین نام کامل فایل باید به این صورت باشد: `logo.webp`:

![podcast](assets/29.webp)


- به پوشه `assets` خود بازگردید و روی فایل واسطه `.gitkeep` کلیک کنید:

![podcast](assets/30.webp)


- پس از باز کردن فایل، روی سه نقطه کوچک در بالا سمت راست کلیک کنید و سپس روی `Delete file`:

![podcast](assets/31.webp)


- تأیید کنید که هنوز در همان شاخه کاری هستید، سپس روی دکمه `Commit changes` کلیک کنید:

![podcast](assets/32.webp)


- به تعهد خود عنوان و توضیح اضافه کنید، سپس روی `Commit changes` کلیک کنید:

![podcast](assets/33.webp)


- به ریشه مخزن خود برگردید:

![podcast](assets/34.webp)


- باید پیامی ببینید که نشان می‌دهد شاخه شما تغییراتی داشته است. روی دکمه `Compare & pull request` کلیک کنید:

![podcast](assets/35.webp)


- یک عنوان و توضیح واضح به درخواست ادغام خود اضافه کنید:

![podcast](assets/36.webp)


- روی دکمه `Create pull request` کلیک کنید:

![podcast](assets/37.webp)

تبریک می‌گوییم! درخواست شما با موفقیت ایجاد شد. اکنون یک مدیر آن را بررسی خواهد کرد و در صورت درست بودن همه چیز، آن را به مخزن اصلی شبکه PlanB ادغام خواهد کرد. شما باید پادکست خود را چند روز بعد در وب‌سایت مشاهده کنید.


لطفاً مطمئن شوید که پیشرفت PR خود را دنبال می‌کنید. ممکن است یک مدیر نظر بگذارد و اطلاعات بیشتری بخواهد. تا زمانی که PR شما تأیید نشده است، می‌توانید آن را در زبانه `Pull requests` در مخزن GitHub شبکه PlanB مشاهده کنید:

![podcast](assets/38.webp)

خیلی ممنون بابت مشارکت ارزشمندتان! :)