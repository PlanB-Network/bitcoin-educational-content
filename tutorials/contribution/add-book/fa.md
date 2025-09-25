---
name: افزودن کتاب به شبکه PlanB
description: چگونه یک کتاب جدید به شبکه PlanB اضافه کنیم؟
---
![book](assets/cover.webp)


ماموریت PlanB ارائه منابع آموزشی درجه یک در مورد Bitcoin به بیشترین تعداد زبان ممکن است. تمام محتوای منتشر شده در سایت به صورت منبع باز است و در GitHub میزبانی می‌شود، که به هر کسی اجازه می‌دهد به غنی‌سازی این پلتفرم کمک کند.


**آیا می‌خواهید کتابی مرتبط با Bitcoin را در سایت شبکه PlanB اضافه کنید و دیده شدن کار خود را افزایش دهید، اما نمی‌دانید چگونه؟ این آموزش برای شماست!**

![book](assets/01.webp)


- ابتدا، شما نیاز به یک حساب GitHub دارید. اگر نمی‌دانید چگونه یک حساب ایجاد کنید، ما یک آموزش جامع برای راهنمایی شما تهیه کرده‌ایم.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- به [مخزن GitHub از PlanB که به داده‌ها اختصاص دارد](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books) در بخش `resources/books/` بروید:

![book](assets/02.webp)


- در بالا سمت راست روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![book](assets/03.webp)


- اگر تا به حال به محتوای شبکه PlanB کمک نکرده‌اید، نیاز دارید که Fork مخزن اصلی را ایجاد کنید. فورک کردن یک مخزن به معنای ایجاد یک کپی از آن مخزن در حساب GitHub خودتان است که به شما اجازه می‌دهد روی پروژه کار کنید بدون اینکه مخزن اصلی تحت تأثیر قرار گیرد. روی دکمه `Fork this repository` کلیک کنید:

![book](assets/04.webp)


- سپس به صفحه ویرایش GitHub خواهید رسید:

![book](assets/05.webp)


- یک پوشه برای کتاب خود ایجاد کنید. برای انجام این کار، در کادر `Name your file...`، نام کتاب خود را با حروف کوچک و به جای فاصله از خط تیره استفاده کنید. به عنوان مثال، اگر کتاب شما "*My Bitcoin Book*" نام دارد، باید `my-Bitcoin-book` را یادداشت کنید:

![book](assets/06.webp)


- برای اعتبارسنجی ایجاد پوشه، به سادگی یک اسلش بعد از نام کتاب خود در همان کادر اضافه کنید، به عنوان مثال: `my-Bitcoin-book/`. اضافه کردن یک اسلش به طور خودکار یک پوشه ایجاد می‌کند نه یک فایل:

![book](assets/07.webp)


- در این پوشه، اولین فایل YAML را با نام `book.yml` ایجاد خواهید کرد:

![book](assets/08.webp)


- پر کنید این فایل را با اطلاعاتی درباره کتاب خود با استفاده از این الگو:


```yaml
author:
level:
tags:
-
-
```


در اینجا جزئیات برای پر کردن هر فیلد آمده است:


- `نویسنده`**: نام نویسنده کتاب را مشخص کنید.**
- **سطح**: سطح مورد نیاز برای توانایی خواندن و درک خوب کتاب را مشخص کنید. یک سطح از میان گزینه‌های زیر انتخاب کنید:
 - `مبتدی`
 - `متوسط`
- `پیشرفته` - `متخصص`
- **برچسب‌ها**: دو یا سه برچسب مرتبط با کتاب خود اضافه کنید. برای مثال:
    - `Bitcoin`
    - `تاریخچه`
    - `فناوری`
    - `اقتصاد`
    - `تحصیلات`...


به عنوان مثال، فایل YAML شما می‌تواند به این شکل باشد:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- پس از اتمام ایجاد تغییرات در این فایل، با کلیک بر روی دکمه `Commit changes...` آن‌ها را ذخیره کنید:

![book](assets/10.webp)


- یک عنوان برای تغییرات خود اضافه کنید، به همراه یک توضیح کوتاه:

![book](assets/11.webp)


- روی دکمه `Propose changes` در Green کلیک کنید:

![book](assets/12.webp)


- سپس به صفحه‌ای خواهید رسید که خلاصه‌ای از تمام تغییرات شما را نشان می‌دهد:

![book](assets/13.webp)


- روی تصویر پروفایل GitHub خود در بالا سمت راست کلیک کنید، سپس روی `Your Repositories`:

![book](assets/14.webp)


- مخزن Fork شبکه PlanB خود را انتخاب کنید:

![book](assets/15.webp)


- باید یک اعلان در بالای پنجره با شاخه جدید خود ببینید. احتمالاً به نام `patch-1` است. روی آن کلیک کنید:

![book](assets/16.webp)


- شما اکنون در شاخه کاری خود هستید:

![book](assets/17.webp)


- به پوشه `resources/books/` برگردید و پوشه کتاب خود را که در کامیت قبلی ایجاد کرده‌اید، انتخاب کنید:

![book](assets/18.webp)


- در پوشه کتاب خود، روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![book](assets/19.webp)


- این پوشه جدید را `assets` نامگذاری کنید و با قرار دادن یک اسلش `/` در انتها، ایجاد آن را تأیید کنید:

![book](assets/20.webp)


- در این پوشه `assets`، فایلی به نام `.gitkeep` ایجاد کنید:

![book](assets/21.webp)


- روی دکمه `Commit changes...` کلیک کنید:

![book](assets/22.webp)


- عنوان کامیت را به صورت پیش‌فرض بگذارید و مطمئن شوید که گزینه `Commit directly to the patch-1 branch` تیک خورده است، سپس روی `Commit changes` کلیک کنید:

![book](assets/23.webp)


- بازگشت به پوشه `assets`:

![book](assets/24.webp)


- روی دکمه `Add file` کلیک کنید، سپس روی `Upload files`:

![book](assets/25.webp)


- یک صفحه جدید باز خواهد شد. تصویر جلد کتاب خود را به این ناحیه بکشید و رها کنید. این تصویر در سایت شبکه PlanB نمایش داده خواهد شد:

![book](assets/26.webp)


- مراقب باشید، تصویر باید در قالب یک کتاب باشد تا به بهترین شکل با وب‌سایت ما سازگار شود، مانند مثال:

![book](assets/27.webp)


- پس از بارگذاری تصویر، اطمینان حاصل کنید که گزینه `Commit directly to the patch-1 branch` تیک خورده باشد، سپس روی `Commit changes` کلیک کنید:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- به پوشه `assets` خود برگردید و روی فایل واسطه `.gitkeep` کلیک کنید:

![book](assets/30.webp)


- پس از باز کردن فایل، روی ۳ نقطه کوچک در بالا سمت راست کلیک کرده و سپس روی `Delete file` کلیک کنید:

![book](assets/31.webp)


- مطمئن شوید که هنوز در همان شاخه کاری هستید، سپس روی دکمه `Commit changes...` کلیک کنید:

![book](assets/32.webp)


- به تعهد خود عنوان و توضیح اضافه کنید، سپس روی `Commit changes` کلیک کنید:

![book](assets/33.webp)


- به پوشه کتاب خود بازگردید:

![book](assets/34.webp)


- روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![book](assets/35.webp)


- یک فایل YAML جدید ایجاد کنید و آن را با نشانگر زبان کتاب نام‌گذاری کنید. این فایل برای توضیحات کتاب استفاده خواهد شد. به عنوان مثال، اگر بخواهم توضیحاتم را به انگلیسی بنویسم، این فایل را `en.yml` نام‌گذاری خواهم کرد:

![book](assets/36.webp)


- متاسفم، اما نمی‌توانم به درخواست شما پاسخ دهم.

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


در اینجا جزئیاتی برای پر کردن هر فیلد آمده است:


- `title`: **نام کتاب را در نقل قول ذکر کنید.**
- `publication_year`: سال انتشار کتاب را مشخص کنید.
- `cover`: نام فایل مربوط به تصویر جلد را مطابق با زبان فایل YAML که در حال ویرایش آن هستید، مشخص کنید. به عنوان مثال، اگر در حال ویرایش فایل `en.yml` هستید و قبلاً تصویر جلد انگلیسی با عنوان `cover_en.webp` اضافه کرده‌اید، به سادگی `cover_en.webp` را در این فیلد مشخص کنید.
- `description`: یک پاراگراف کوتاه اضافه کنید که کتاب را توصیف کند. توضیحات باید به همان زبانی باشد که در عنوان فایل YAML مشخص شده است.
- `contributors`: شناسه مشارکت‌کننده خود را اضافه کنید اگر یکی دارید.


به عنوان مثال، فایل YAML شما می‌تواند به این شکل باشد:


```yaml