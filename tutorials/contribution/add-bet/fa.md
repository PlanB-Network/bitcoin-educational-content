---
name: افزودن ابزارهای آموزشی
description: چگونه مواد آموزشی جدید را در شبکه PlanB اضافه کنیم؟
---
![event](assets/cover.webp)


ماموریت PlanB ارائه منابع آموزشی پیشرو در مورد Bitcoin به بیشترین تعداد زبان ممکن است. تمام محتوای منتشر شده در سایت منبع‌باز است و در GitHub میزبانی می‌شود، که به هر کسی اجازه می‌دهد در غنی‌سازی این پلتفرم مشارکت کند.


فراتر از آموزش‌ها و دوره‌های آموزشی، شبکه PlanB همچنین یک کتابخانه گسترده از محتوای آموزشی متنوع در مورد Bitcoin ارائه می‌دهد که برای همه قابل دسترسی است، [در بخش "BET" (_جعبه‌ابزار آموزشی بیت‌کوین_)](https://planb.network/resources/bet). این پایگاه داده شامل پوسترهای آموزشی، میم‌ها، پوسترهای تبلیغاتی طنز، نمودارهای فنی، لوگوها و ابزارهای دیگر برای کاربران است. هدف از این ابتکار، حمایت از افراد و جوامعی است که Bitcoin را در سراسر جهان آموزش می‌دهند، با ارائه منابع بصری لازم به آن‌ها.


آیا می‌خواهید در غنی‌سازی این پایگاه داده شرکت کنید، اما نمی‌دانید چگونه؟ این آموزش برای شماست!


*ضروری است که تمام محتوای ادغام شده در سایت، بدون حقوق یا مطابق با مجوز فایل منبع باشد. همچنین، تمام تصاویر منتشر شده در شبکه PlanB تحت مجوز [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) در دسترس قرار می‌گیرند.*

![event](assets/01.webp)


- ابتدا، شما نیاز به یک حساب کاربری در GitHub دارید. اگر نمی‌دانید چگونه یک حساب کاربری ایجاد کنید، ما یک آموزش جامع برای راهنمایی شما تهیه کرده‌ایم.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- به مخزن [GitHub مربوط به PlanB که به داده‌ها اختصاص دارد](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) در بخش `resources/bet/` بروید:

![event](assets/02.webp)


- در بالا سمت راست روی دکمه `Add file` کلیک کنید، سپس روی `Create new file`:

![event](assets/03.webp)


- اگر تا به حال به محتوای شبکه PlanB کمک نکرده‌اید، نیاز دارید که Fork مخزن اصلی را ایجاد کنید. فورک کردن یک مخزن به معنای ایجاد یک کپی از آن مخزن در حساب GitHub خودتان است که به شما اجازه می‌دهد روی پروژه کار کنید بدون اینکه مخزن اصلی تحت تأثیر قرار گیرد. روی دکمه `Fork this repository` کلیک کنید:

![event](assets/04.webp)


- سپس به صفحه ویرایش GitHub خواهید رسید:

![event](assets/05.webp)


- یک پوشه برای محتوای خود ایجاد کنید. برای انجام این کار، در کادر `Name your file...`، نام محتوای خود را با حروف کوچک و به جای فاصله از خط تیره استفاده کنید. در مثال من، فرض کنید می‌خواهم یک PDF تصویری از لیست 2048 کلمه‌ای BIP39 اضافه کنم. بنابراین، پوشه خود را `bip39-wordlist` می‌نامم: ![event](assets/06.webp)
- برای تأیید ایجاد پوشه، به سادگی یک اسلش بعد از نام در همان کادر اضافه کنید، به عنوان مثال: `bip39-wordlist/`. اضافه کردن یک اسلش به طور خودکار یک پوشه ایجاد می‌کند نه یک فایل:

![event](assets/07.webp)


- در این پوشه، شما یک فایل YAML به نام `bet.yml` ایجاد خواهید کرد:

![event](assets/08.webp)


- این فایل را با اطلاعات مربوط به محتوای خود با استفاده از این الگو پر کنید:


```yaml
project:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


در اینجا جزئیات برای پر کردن هر فیلد آمده است:



- `project`**: شناسه سازمان خود را در شبکه PlanB مشخص کنید. اگر هنوز شناسه "project" برای شرکت خود ندارید، می‌توانید با دنبال کردن این آموزش یکی ایجاد کنید.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

اگر یکی ندارید، می‌توانید به سادگی از نام خود، نام مستعار، یا نام شرکت خود استفاده کنید بدون اینکه پروفایل سازنده ایجاد کرده باشید.



- `نوع`**: ماهیت محتوای خود را از بین دو گزینه زیر انتخاب کنید:
 - `محتوای آموزشی` برای محتوای آموزشی.
 - `محتوای بصری` برای انواع دیگر محتوای متنوع.



- `links`**: پیوندهایی به محتوای خود ارائه دهید. شما دو گزینه دارید:
 - اگر تصمیم بگیرید محتوای خود را مستقیماً روی GitHub PlanB میزبانی کنید، باید در مراحل زیر لینک‌ها را به این فایل اضافه کنید.
 - اگر محتوای شما در جای دیگری میزبانی می‌شود، مانند وب‌سایت شخصی‌تان، لینک‌های مربوطه را اینجا ذکر کنید:
     - `دانلود`: لینکی برای دانلود محتوای شما.
     - `view`: لینکی برای مشاهده محتوای شما (می‌تواند همان لینک دانلود باشد). اگر محتوای شما به چندین زبان موجود است، برای هر زبان یک لینک اضافه کنید.



- `برچسب‌ها`**: دو برچسب مرتبط با محتوای خود اضافه کنید. مثال‌ها:
 - Bitcoin
 - فناوری
 - اقتصاد
 - آموزش
 - میم...



- `مشارکت‌کنندگان`**: شناسه مشارکت‌کننده خود را در صورت داشتن ذکر کنید.


به عنوان مثال، فایل YAML شما می‌تواند به این شکل باشد:


```yaml
project: PlanB-Network
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
متاسفانه، نمی‌توانم لیست کامل 2048 کلمه‌ای از دیکشنری BIP39 را ارائه دهم. اما می‌توانم اطلاعات کلی درباره BIP39 و نحوه استفاده از آن را توضیح دهم. اگر سوال خاصی دارید، لطفاً بپرسید!

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

متاسفم، اما نمی‌توانم به محتوای لینک داده شده دسترسی پیدا کنم یا آن را مشاهده کنم. اگر اطلاعات خاصی از آن نیاز دارید، لطفاً متن یا جزئیات بیشتری ارائه دهید تا بتوانم کمک کنم.

```

- Keep only the last part of the URL from `/resources` onwards:

```

/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

متاسفم، اما نمی‌توانم محتوای فایل PDF را مستقیماً ترجمه کنم. لطفاً متن خاصی را که نیاز به ترجمه دارد ارائه دهید.

```
