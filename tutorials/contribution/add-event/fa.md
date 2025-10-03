---
name: یک رویداد به شبکه PlanB اضافه کنید
description: چگونه می‌توانم پیشنهاد اضافه کردن یک رویداد جدید در شبکه PlanB را بدهم؟
---
![event](assets/cover.webp)


ماموریت PlanB ارائه منابع آموزشی درجه یک در مورد Bitcoin به بیشترین تعداد زبان ممکن است. تمام محتوای منتشر شده در سایت به صورت منبع باز است و در GitHub میزبانی می‌شود، که به هر کسی فرصت مشارکت در غنی‌سازی این پلتفرم را می‌دهد.


اگر می‌خواهید یک کنفرانس Bitcoin را به سایت شبکه PlanB اضافه کنید و دید رویداد خود را افزایش دهید، اما نمی‌دانید چگونه؟ این آموزش برای شماست!

![event](assets/01.webp)


- ابتدا، شما نیاز به داشتن یک حساب کاربری در GitHub دارید. اگر نمی‌دانید چگونه یک حساب کاربری ایجاد کنید، ما یک آموزش جامع برای راهنمایی شما تهیه کرده‌ایم.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- به [مخزن GitHub مربوط به PlanB که به داده‌ها اختصاص دارد](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) در بخش `resources/conference/` بروید:

![event](assets/02.webp)


- در بالا سمت راست روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![event](assets/03.webp)


- اگر تا به حال به محتوای شبکه PlanB کمک نکرده‌اید، نیاز دارید که Fork مخزن اصلی را ایجاد کنید. فورک کردن یک مخزن به معنای ایجاد یک کپی از آن مخزن در حساب GitHub خودتان است که به شما اجازه می‌دهد روی پروژه کار کنید بدون اینکه مخزن اصلی تحت تأثیر قرار گیرد. روی دکمه `Fork this repository` کلیک کنید:

![event](assets/04.webp)


- سپس به صفحه ویرایش GitHub خواهید رسید:

![event](assets/05.webp)


- پوشه‌ای برای کنفرانس خود ایجاد کنید. برای این کار، در کادر `Name your file...`، نام کنفرانس خود را با حروف کوچک و به جای فاصله از خط تیره استفاده کنید. به عنوان مثال، اگر کنفرانس شما "Paris Bitcoin Conference" نام دارد، باید `paris-Bitcoin-conference` را یادداشت کنید. همچنین سال کنفرانس خود را اضافه کنید، به عنوان مثال: `paris-Bitcoin-conference-2024`:

![event](assets/06.webp)


- برای تأیید ایجاد پوشه، به سادگی یک اسلش بعد از نام خود در همان کادر یادداشت کنید، به عنوان مثال: `paris-Bitcoin-conference-2024/`. اضافه کردن یک اسلش به طور خودکار یک پوشه ایجاد می‌کند نه یک فایل:

![event](assets/07.webp)


- در این پوشه، اولین فایل YAML را با نام `events.yml` ایجاد خواهید کرد:

![event](assets/08.webp)


- پر کنید این فایل را با اطلاعات درباره کنفرانس خود با استفاده از این الگو:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
project:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language:
-
links:
website:
replay_url:
live_url :
tags:
-
```


به عنوان مثال، فایل YAML شما می‌تواند به این شکل باشد:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

اگر هنوز شناسه "*project*" برای سازمان خود ندارید، می‌توانید با دنبال کردن این آموزش دیگر آن را اضافه کنید.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- پس از اتمام ایجاد تغییرات در این فایل، آن‌ها را با کلیک بر روی دکمه `Commit changes...` ذخیره کنید:

![event](assets/10.webp)


- برای تغییرات خود یک عنوان و توضیح کوتاه اضافه کنید:

![event](assets/11.webp)


- روی دکمه `Propose changes` در Green کلیک کنید:

![event](assets/12.webp)


- سپس به صفحه‌ای خواهید رسید که خلاصه‌ای از تمام تغییرات شما را نشان می‌دهد:

![event](assets/13.webp)


- روی تصویر پروفایل GitHub خود در بالا سمت راست کلیک کنید، سپس روی `Your Repositories`:

![event](assets/14.webp)


- Fork خود را از مخزن PlanB Network انتخاب کنید:

![event](assets/15.webp)


- باید یک اعلان در بالای پنجره با شاخه جدید خود ببینید. احتمالاً به نام `patch-1` است. روی آن کلیک کنید:

![event](assets/16.webp)


- شما اکنون در شاخه کاری خود هستید:

![event](assets/17.webp)


- به پوشه `resources/conference/` برگردید و پوشه کنفرانسی که در کامیت قبلی ایجاد کرده‌اید را انتخاب کنید:

![event](assets/18.webp)


- در پوشه کنفرانس خود، روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![event](assets/19.webp)


- این پوشه جدید را `assets` نامگذاری کنید و با قرار دادن یک اسلش `/` در انتها، ایجاد آن را تأیید کنید:

![event](assets/20.webp)


- در این پوشه `assets`، فایلی به نام `.gitkeep` ایجاد کنید:

![event](assets/21.webp)


- روی دکمه `Commit changes...` کلیک کنید:

![event](assets/22.webp)


- عنوان کامیت را به صورت پیش‌فرض بگذارید و مطمئن شوید که گزینه `Commit directly to the patch-1 branch` تیک خورده است، سپس روی `Commit changes` کلیک کنید:

![event](assets/23.webp)


- به پوشه `assets` بازگردید:

![event](assets/24.webp)


- روی دکمه `Add file` کلیک کنید، سپس روی `Upload files`: ![event](assets/25.webp)
- صفحه جدیدی باز خواهد شد. تصویری را که نمایانگر کنفرانس شماست بکشید و رها کنید تا در سایت شبکه PlanB نمایش داده شود:

![event](assets/26.webp)


- می‌تواند لوگو، تصویر بندانگشتی یا حتی پوستر باشد:

![event](assets/27.webp)


- پس از بارگذاری تصویر، بررسی کنید که گزینه `Commit directly to the patch-1 branch` تیک خورده باشد، سپس روی `Commit changes` کلیک کنید:

![event](assets/28.webp)


- مراقب باشید، تصویر شما باید با نام `thumbnail` و در قالب `.webp` باشد. بنابراین نام کامل فایل باید به این صورت باشد: `thumbnail.webp`:

![event](assets/29.webp)


- به پوشه `assets` خود بازگردید و روی فایل واسطه `.gitkeep` کلیک کنید:

![event](assets/30.webp)


- پس از باز کردن فایل، روی ۳ نقطه کوچک در بالا سمت راست کلیک کنید و سپس روی `Delete file`:

![event](assets/31.webp)


- تأیید کنید که هنوز در همان شاخه کاری هستید، سپس روی دکمه `Commit changes` کلیک کنید:

![event](assets/32.webp)


- به تعهد خود عنوان و توضیح اضافه کنید، سپس روی `Commit changes` کلیک کنید:

![event](assets/33.webp)


- به ریشه مخزن خود برگردید:

![event](assets/34.webp)


- شما باید پیامی ببینید که نشان می‌دهد شاخه شما دچار تغییراتی شده است. روی دکمه `Compare & pull request` کلیک کنید:

![event](assets/35.webp)


- یک عنوان واضح و توضیحی به درخواست ادغام خود اضافه کنید:

![event](assets/36.webp)


- روی دکمه `Create pull request` کلیک کنید:

![event](assets/37.webp)

تبریک! درخواست شما با موفقیت ایجاد شد. اکنون یک مدیر آن را بررسی خواهد کرد و در صورت درست بودن، آن را به مخزن اصلی PlanB Network ادغام می‌کند. شما باید رویداد خود را چند روز بعد در وب‌سایت مشاهده کنید.


حتماً پیشرفت PR خود را دنبال کنید. ممکن است یک مدیر نظر بگذارد و اطلاعات بیشتری بخواهد. تا زمانی که PR شما تأیید نشده است، می‌توانید آن را در زبانه `Pull requests` در مخزن GitHub شبکه PlanB مشاهده کنید:

![event](assets/38.webp)

خیلی ممنون از مشارکت ارزشمند شما! :)
