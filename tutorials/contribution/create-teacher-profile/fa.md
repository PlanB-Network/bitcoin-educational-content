---
name: پروفسور Plan ₿ Academy
description: چگونه می‌توانم پروفایل معلم خود را در Plan ₿ Academy اضافه یا ویرایش کنم؟
---
![cover](assets/cover.webp)


اگر قصد دارید با نوشتن یک آموزش یا دوره جدید به Plan ₿ Academy کمک کنید، به یک پروفایل معلم نیاز خواهید داشت. این پروفایل به شما امکان می‌دهد تا اعتبار مناسب برای محتوایی که به پلتفرم ارائه می‌دهید را دریافت کنید.


برای کسانی که قبلاً در ایجاد محتوای آموزشی در Plan ₿ Academy مشارکت داشته‌اند، احتمالاً پروفایل معلم دارید. می‌توانید آن را در پوشه `/professors` [در مخزن GitHub ما](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) پیدا کنید. اگر پروفایل شما قبلاً وجود دارد، ورود خود را در فایل `professor.yml` پیدا کنید.


برای ایجاد تغییرات در پروفایل خود، به بخش "ویرایش پروفایل معلم خود" در انتهای این آموزش بروید.


## یک معلم جدید با نرم‌افزار ما اضافه کنید


آسان‌ترین راه برای ایجاد پروفایل معلم خود در Plan ₿ Academy استفاده از ابزار پایتون یکپارچه ما است. در اینجا نحوه کار آن آمده است.


### ۱ - محیط محلی خود را پیکربندی کنید


شما باید Fork خود را از [مخزن Plan ₿ Academy در GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content) داشته باشید.


شاخه اصلی (`dev`) از Fork خود را با مخزن منبع همگام‌سازی کنید.


کلون محلی خود را به‌روزرسانی کنید.


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### ۲ - ایجاد یک شاخه جدید


مطمئن شوید که روی شاخه `dev` هستید. یک شاخه جدید با یک نام توصیفی ایجاد کنید (مثلاً `add-professor-loic-morel`).


این شاخه را به صورت آنلاین در Fork خود منتشر کنید.


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### ۳ - پروفایل معلم خود را ایجاد کنید


به پوشه `scripts/tutorial-related/data-creator/` در کلون محلی خود بروید. اطمینان حاصل کنید که تمام وابستگی‌های مورد نیاز برای نرم‌افزار را نصب کرده‌اید، پس از نصب پایتون:


```bash
pip install -r requirements.txt
```


سپس نرم‌افزار را با فرمان زیر اجرا کنید:


```bash
python3 main.py
```


پس از ورود به صفحه اصلی، مسیر محلی کلون مخزن خود، زبانی که در آن می‌نویسید و شناسه GitHub خود را وارد کنید. اگر این پروفایل را برای شخص دیگری ایجاد می‌کنید و قبلاً پروفایل استادی دارید، شناسه خود را در فیلد "*شناسه استاد Plan ₿ Academy*" وارد کنید. اگر در حال ایجاد پروفایل خود هستید، هنوز شناسه استادی نخواهید داشت، زیرا در حال ایجاد آن هستید، بنابراین این فیلد را خالی بگذارید.


سپس روی دکمه "*استاد جدید*" کلیک کنید.


![Image](assets/fr/01.webp)


اطلاعات مورد نیاز را پر کنید (لطفاً توجه داشته باشید که تمام این اطلاعات در پلتفرم ما و همچنین در GitHub عمومی خواهد بود):




- نام فایل معلم شما (از نام و نام خانوادگی یا یک نام مستعار خود، با حروف کوچک استفاده کنید) ;
- نام یا نام مستعار شما ؛
- وب‌سایت و پروفایل شما X (اختیاری) ؛
- یک Address Lightning برای دریافت کمک‌های مالی از خوانندگان (اختیاری) ؛
- 2 یا 3 برچسب از لیست انتخاب کنید؛
- روی "*Select Image*" کلیک کنید تا یک تصویر پروفایل از پوشه‌های محلی خود انتخاب کنید (هر نام و فرمتی می‌تواند برای تصویر استفاده شود و نرم‌افزار به‌طور خودکار آن را تطبیق می‌دهد. فقط مطمئن شوید که تصویر مربعی است)؛
- یک توضیح کوتاه از پروفایل خود بنویسید.


ایجاد را با کلیک بر روی "*ایجاد استاد*" نهایی کنید. این کار به طور خودکار تمام فایل‌های مورد نیاز برای پروفایل شما را generate خواهد کرد.


![Image](assets/fr/02.webp)


تغییرات خود را با ایجاد یک کامیت با یک پیام توضیحی به صورت محلی ذخیره کنید. تغییرات را به GitHub خود در Fork پوش کنید.


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


پس از اتمام، یک درخواست کشش (PR) در GitHub ایجاد کنید تا پیشنهاد ادغام تغییرات خود را ارائه دهید. یک عنوان و توضیح مختصر به PR اضافه کنید.


### ۴ - ویرایش و ادغام


منتظر اعتبارسنجی یا بازخورد از یک مدیر باشید. در صورت لزوم، اصلاحات را انجام داده و کامیت‌های جدید را ارسال کنید.


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


پس از ادغام PR، می‌توانید شاخه کاری خود را حذف کنید.


## پروفایل معلم خود را ویرایش کنید


اگر به استفاده از Git تسلط دارید، پروفایل معلم خود را با ایجاد یک شاخه جدید و ویرایش فایل مربوطه به طور مستقیم در پوشه موجود خود تغییر دهید. تغییرات می‌توانند یا در فایل `professor.yml` یا در فایل markdown انجام شوند، بسته به اطلاعاتی که باید تصحیح شوند. پس از اعمال تغییرات به صورت محلی، آن‌ها را به Fork خود پوش کنید و یک PR ارسال کنید.


برای مبتدیان، توصیه می‌کنم تغییرات را مستقیماً از طریق وب Interface گیت‌هاب انجام دهید. مطمئن شوید که یک حساب گیت‌هاب دارید. اگر نمی‌دانید چگونه یکی بسازید، این آموزش را دنبال کنید:


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
به [مخزن GitHub Plan ₿ Academy اختصاص داده شده به داده‌ها](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors) بروید.


![Image](assets/fr/03.webp)


روی پوشه "*professors*" کلیک کنید، سپس به پوشه شخصی خود بروید.


![Image](assets/fr/04.webp)


برای تغییر فراداده پروفایل خود، مانند Lightning Address، نام یا لینک‌ها، فایل "*professor.yml*" را انتخاب کنید. برای تغییر توضیحات خود، روی فایل YAML برای زبان خود کلیک کنید (مثلاً "*en.yml*" یا "*fr.yml*").


اگر توضیحات خود را تغییر دهید، به یاد داشته باشید که تمام ترجمه‌های منسوخ را حذف کنید. سپس می‌توانید با کمک یک LLM توضیحات خود را به زبان‌های دیگر ترجمه کنید، یا فقط توضیحات را به زبان مادری خود بگذارید و در درخواست Pull خود ذکر کنید که توضیحات شما نیاز به ترجمه توسط تیم ما دارد.


![Image](assets/fr/05.webp)


پس از باز کردن فایلی که می‌خواهید ویرایش کنید، روی آیکون مداد کلیک کنید.


![Image](assets/fr/06.webp)


اگر هنوز یک Fork از مخزن Plan ₿ Academy ندارید، GitHub پیشنهاد می‌کند که یکی ایجاد کنید. روی "*Fork این مخزن*" کلیک کنید.


![Image](assets/fr/07.webp)


تغییرات مورد نظر را در فایل اعمال کنید. پس از اتمام، روی "*Commit changes*" کلیک کنید.


![Image](assets/fr/08.webp)


پیامی را که تغییر خود را توصیف می‌کند وارد کنید، سپس "*پیشنهاد تغییرات*" را انتخاب کنید.


![Image](assets/fr/09.webp)


خلاصه‌ای از تغییرات شما نمایش داده خواهد شد. اگر مایل به ایجاد تغییرات بیشتری در پروفایل خود هستید، می‌توانید به پوشه‌ها بازگردید و تعهدات بیشتری انجام دهید. وقتی کارتان تمام شد، روی "*ایجاد درخواست کشش*" کلیک کنید.


یک درخواست Pull Request درخواستی است برای ادغام تغییرات از شاخه شما به شاخه اصلی مخزن Plan ₿ Academy، که امکان بررسی و بحث در مورد تغییرات را قبل از ادغام فراهم می‌کند.


![Image](assets/fr/10.webp)


مطمئن شوید که در بالای Interface، شاخه کاری شما با شاخه `dev` مخزن Plan ₿ Academy (که شاخه اصلی است) ادغام شده است.


عنوانی وارد کنید که به طور خلاصه تغییراتی که می‌خواهید با مخزن منبع ادغام کنید را خلاصه کند. یک نظر کوتاه اضافه کنید که این تغییرات را توصیف کند، سپس روی دکمه Green "*ایجاد درخواست کشش*" کلیک کنید تا درخواست کشش را تأیید کنید:


![Image](assets/fr/11.webp)


در این صورت، درخواست کشش شما در زبانه "*Pull Request*" مخزن اصلی Plan ₿ Academy قابل مشاهده خواهد بود. اکنون تنها کاری که باید انجام دهید این است که منتظر بمانید تا یک مدیر تغییرات شما را ادغام کند.


![Image](assets/fr/12.webp)


اگر در ارسال تغییرات خود با هرگونه مشکل فنی مواجه شدید، لطفاً در درخواست کمک از [گروه تلگرام ما که به مشارکت‌ها اختصاص دارد](https://t.me/PlanBNetwork_ContentBuilder) تردید نکنید. بسیار متشکریم!