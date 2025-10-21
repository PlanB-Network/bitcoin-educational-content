---
name: افزودن یک سازنده
description: چگونه پیشنهاد اضافه کردن یک سازنده جدید در شبکه PlanB را ارائه دهیم؟
---
![project](assets/cover.webp)


ماموریت PlanB ارائه منابع آموزشی درجه یک در مورد Bitcoin به بیشترین تعداد زبان ممکن است. تمام محتوای منتشر شده در سایت منبع باز است و در GitHub میزبانی می‌شود، که به هر کسی اجازه می‌دهد در غنی‌سازی این پلتفرم مشارکت کند.


آیا می‌خواهید یک Bitcoin "سازنده" جدید به سایت شبکه PlanB اضافه کنید و به شرکت یا نرم‌افزار خود دیده‌شدن بدهید، اما نمی‌دانید چگونه؟ این آموزش برای شماست!

![project](assets/01.webp)


- ابتدا، شما نیاز به یک حساب GitHub دارید. اگر نمی‌دانید چگونه یک حساب ایجاد کنید، ما یک آموزش جامع برای راهنمایی شما تهیه کرده‌ایم.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- به [مخزن GitHub از PlanB که به داده‌ها اختصاص دارد](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) در بخش `resources/project/` بروید:

![project](assets/02.webp)


- در بالا سمت راست روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![project](assets/03.webp)


- اگر تا به حال به محتوای شبکه PlanB کمک نکرده‌اید، نیاز دارید که Fork مخزن اصلی را ایجاد کنید. فورک کردن یک مخزن به معنای ایجاد یک کپی از آن مخزن در حساب GitHub خودتان است که به شما اجازه می‌دهد روی پروژه کار کنید بدون اینکه مخزن اصلی تحت تأثیر قرار گیرد. روی دکمه `Fork this repository` کلیک کنید:

![project](assets/04.webp)


- سپس به صفحه ویرایش GitHub خواهید رسید:

![project](assets/05.webp)


- یک پوشه برای شرکت خود ایجاد کنید. برای انجام این کار، در کادر `Name your file...`، نام شرکت خود را با حروف کوچک و به جای فاصله از خط تیره استفاده کنید. به عنوان مثال، اگر شرکت شما "Bitcoin Baguette" نام دارد، باید بنویسید `Bitcoin-baguette`:

![project](assets/06.webp)


- برای تأیید ایجاد پوشه، به سادگی یک اسلش بعد از نام خود در همان کادر اضافه کنید، به عنوان مثال: `Bitcoin-baguette/`. اضافه کردن یک اسلش به طور خودکار یک پوشه ایجاد می‌کند نه یک فایل:

![project](assets/07.webp)


- در این پوشه، شما یک فایل YAML به نام `project.yml` ایجاد خواهید کرد:

![project](assets/08.webp)


- این فایل را با اطلاعات مربوط به شرکت خود با استفاده از این الگو پر کنید:


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


در اینجا چیزی است که باید برای هر کلید پر کنید:


- `name`: نام شرکت شما (الزامی)؛
- `Address` : مکان کسب‌وکار شما (اختیاری)؛
- `language` : کشورهایی که کسب‌وکار شما در آن‌ها فعالیت می‌کند یا زبان‌های پشتیبانی‌شده (اختیاری)؛
- `links` : لینک‌های رسمی مختلف کسب‌وکار شما (اختیاری)؛
- `برچسب‌ها`: ۲ اصطلاح که کسب‌وکار شما را توصیف می‌کنند (الزامی)؛
- `category` : دسته‌ای که به بهترین شکل زمینه فعالیت کسب‌وکار شما را در میان گزینه‌های زیر توصیف می‌کند:
 - `Wallet`,
 - `زیرساخت`,
 - `Exchange`,
 - `آموزش`,
 - `سرویس`,
 - `جوامع`,
 - `کنفرانس`,
 - `حریم خصوصی`,
 - `سرمایه‌گذاری`,
 - `گره`,
 - `Mining`,
 - `اخبار`,
 - `سازنده`.


به عنوان مثال، فایل YAML شما می‌تواند به این شکل باشد:


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


- پس از اتمام ایجاد تغییرات در این فایل، با کلیک بر روی دکمه `Commit changes...` آن‌ها را ذخیره کنید:

![project](assets/10.webp)


- یک عنوان برای تغییرات خود اضافه کنید، همراه با یک توضیح کوتاه:

![project](assets/11.webp)


- روی دکمه `Propose changes` Green کلیک کنید:

![project](assets/12.webp)


- سپس به صفحه‌ای خواهید رسید که خلاصه‌ای از تمام تغییرات شما را نشان می‌دهد:

![project](assets/13.webp)


- روی تصویر پروفایل GitHub خود در بالا سمت راست کلیک کنید، سپس روی `Your Repositories`:

![project](assets/14.webp)


- مخزن Fork از مخزن Plan ₿ Academy خود را انتخاب کنید:

![project](assets/15.webp)


- باید یک اعلان در بالای پنجره با شاخه جدید خود ببینید. احتمالاً به نام `patch-1` است. روی آن کلیک کنید:

![project](assets/16.webp)


- شما اکنون در شاخه کاری خود هستید (**اطمینان حاصل کنید که در همان شاخه‌ای هستید که تغییرات قبلی خود را انجام داده‌اید، این مهم است!**):

![project](assets/17.webp)


- به پوشه `resources/projects/` برگردید و پوشه کسب‌وکار خود را که در کامیت قبلی ایجاد کرده‌اید، انتخاب کنید:

![project](assets/18.webp)


- در پوشه کسب‌وکار خود، روی دکمه `افزودن فایل` کلیک کنید، سپس روی `ایجاد فایل جدید`:

![project](assets/19.webp)


- این پوشه جدید را `assets` نام‌گذاری کنید و با قرار دادن یک اسلش `/` در انتها، ایجاد آن را تأیید کنید:

![project](assets/20.webp)


- در این پوشه `assets`، فایلی به نام `.gitkeep` ایجاد کنید:

![project](assets/21.webp)


- روی دکمه `Commit changes...` کلیک کنید:

![project](assets/22.webp)


- عنوان کامیت را به صورت پیش‌فرض بگذارید و مطمئن شوید که گزینه `Commit directly to the patch-1 branch` تیک خورده است، سپس روی `Commit changes` کلیک کنید: ![project](assets/23.webp)
- به پوشه `assets` برگردید:

![project](assets/24.webp)


- روی دکمه `Add file` کلیک کنید، سپس روی `Upload files`:

![project](assets/25.webp)


- صفحه جدیدی باز خواهد شد. تصویر شرکت یا نرم‌افزار خود را به این ناحیه بکشید و رها کنید. این تصویر در سایت Plan ₿ Academy نمایش داده خواهد شد:

![project](assets/26.webp)


- می‌تواند لوگو یا یک آیکون باشد:

![project](assets/27.webp)


- پس از بارگذاری تصویر، اطمینان حاصل کنید که کادر `Commit directly to the patch-1 branch` علامت‌گذاری شده است، سپس روی `Commit changes` کلیک کنید:

![project](assets/28.webp)


- مراقب باشید، تصویر شما باید مربع باشد، باید به نام `logo` باشد و باید در فرمت `.webp` باشد. بنابراین نام کامل فایل باید به این صورت باشد: `logo.webp`:

![project](assets/29.webp)


- به پوشه `assets` خود برگردید و روی فایل میانی `.gitkeep` کلیک کنید:

![project](assets/30.webp)


- پس از باز کردن فایل، روی سه نقطه کوچک در بالا سمت راست کلیک کنید و سپس روی `Delete file`:

![project](assets/31.webp)


- تأیید کنید که هنوز در همان شاخه کاری هستید، سپس روی دکمه `Commit changes` کلیک کنید:

![project](assets/32.webp)


- به تغییرات خود یک عنوان و توضیح اضافه کنید، سپس روی `Commit changes` کلیک کنید:

![project](assets/33.webp)


- به پوشه شرکت خود برگردید:

![project](assets/34.webp)


- روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![project](assets/35.webp)


- یک فایل YAML جدید ایجاد کنید و آن را با نشانگر زبان مادری خود نام‌گذاری کنید. این فایل برای توضیحات سازنده استفاده خواهد شد. به عنوان مثال، اگر بخواهم توضیحات خود را به انگلیسی بنویسم، این فایل را `fa.yml` نام‌گذاری خواهم کرد:

![project](assets/36.webp)


- لطفاً قالب YAML را ارائه دهید تا بتوانم آن را برای شما پر کنم.

```yaml
description: |

contributors:
-
```



- برای کلید `contributors`، می‌توانید شناسه مشارکت‌کننده خود را به Plan ₿ Academy اضافه کنید اگر یکی دارید. اگر ندارید، این فیلد را خالی بگذارید.
- برای کلید `description`، تنها کافی است یک پاراگراف کوتاه اضافه کنید که شرکت یا نرم‌افزار شما را توصیف کند. توضیحات باید به همان زبانی باشد که نام فایل است. نیازی نیست که این توضیحات را به تمام زبان‌های پشتیبانی شده در سایت ترجمه کنید، زیرا تیم‌های PlanB این کار را با استفاده از مدل خود انجام خواهند داد. به عنوان مثال، فایل شما می‌تواند به این شکل باشد:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![project](assets/37.webp)


- روی دکمه `Commit changes` کلیک کنید:

![project](assets/38.webp)


- اطمینان حاصل کنید که کادر `Commit directly to the patch-1 branch` علامت‌دار است، یک عنوان اضافه کنید، سپس روی `Commit changes` کلیک کنید:

![project](assets/39.webp)


- پوشه شرکت شما اکنون باید به این شکل باشد:

![project](assets/40.webp)


- اگر همه چیز رضایت‌بخش است، به ریشه Fork خود بازگردید:

![project](assets/41.webp)


- شما باید پیامی ببینید که نشان می‌دهد شاخه شما تغییراتی داشته است. روی دکمه `Compare & pull request` کلیک کنید:

![project](assets/42.webp)


- یک عنوان و توضیح واضح به درخواست ادغام خود اضافه کنید:

![project](assets/43.webp)


- روی دکمه `Create pull request` کلیک کنید:

![project](assets/44.webp)

تبریک می‌گوییم! درخواست شما با موفقیت ایجاد شد. اکنون یک مدیر آن را بررسی خواهد کرد و در صورت صحت، آن را در مخزن اصلی شبکه PlanB ادغام خواهد کرد. شما باید پروفایل سازنده خود را چند روز بعد در وب‌سایت مشاهده کنید.


حتماً پیشرفت PR خود را دنبال کنید. ممکن است یک مدیر نظر بگذارد و اطلاعات بیشتری بخواهد. تا زمانی که PR شما تأیید نشده است، می‌توانید آن را در زبانه `Pull requests` در مخزن GitHub شبکه PlanB مشاهده کنید:

![project](assets/45.webp)

خیلی ممنون از مشارکت ارزشمند شما! :)
