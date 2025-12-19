---
name: Phoenixd
description: راه‌اندازی نود لایتنینگ مینیمالیستی خود با Phoenixd
---

![cover](assets/cover.webp)



استقلال مالی همچنین به معنای کنترل زیرساخت لایتنینگ شماست. برای توسعه‌دهندگان و شرکت‌هایی که مایل به ادغام Bitcoin Lightning در برنامه‌های خود هستند، **Phoenixd** راه‌حل ایده‌آل را ارائه می‌دهد: یک نود لایتنینگ مینیمالیستی و تخصصی با مدیریت خودکار نقدینگی.



Phoenixd یک سرور Lightning است که توسط ACINQ توسعه یافته و به طور خاص برای ارسال و دریافت پرداخت‌های Lightning از طریق یک API HTTP طراحی شده است. برخلاف پیاده‌سازی‌های کامل مانند LND یا Core Lightning، Phoenixd تمام پیچیدگی‌های مدیریت کانال را انتزاع می‌کند و در عین حال از خود محافظت از وجوه شما را حفظ می‌کند.



در این آموزش، ما به نحوه نصب، پیکربندی و استفاده از Phoenixd برای توسعه برنامه‌های Lightning با زیرساخت خودمیزبان و یک API آسان برای استفاده خواهیم پرداخت.



## فینیکسد چیست؟



Phoenixd یک نود لایتنینگ مینیمال و تخصصی است که توسط ACINQ توسعه یافته است. این یک راه‌حل برای توسعه‌دهندگان و شرکت‌هایی است که می‌خواهند لایتنینگ را بدون پیچیدگی مدیریت Full node در برنامه‌های خود ادغام کنند.



### اصل عملکرد



**Phoenixd یک نود لایتنینگ مینیمال است که از ACINQ به عنوان LSP (ارائه‌دهنده خدمات لایتنینگ) خود برای نقدینگی خودکار استفاده می‌کند. هنگامی که پرداخت‌های لایتنینگ دریافت می‌کنید، به‌طور خودکار کانال‌هایی با نودهای ACINQ باز می‌کند تا ظرفیت ورودی لازم را تخصیص دهد. این نقدینگی "در لحظه" فوری است، اما با هزینه دقیقاً **1% + Mining fees** از مبلغ دریافت شده، محاسبه می‌شود.**



**مدیریت خودکار:** سیستم سه Elements کلیدی را مدیریت می‌کند:




- کانال‌های **Lightning**: به‌طور خودکار در صورت نیاز باز، بسته و مدیریت کنید
- ورودی/خروجی نقدینگی**: تأمین خودکار از طریق اسپلیسینگ و باز کردن کانال
- اعتبار هزینه** : پرداخت‌های کوچک که برای توجیه یک کانال کافی نیستند به عنوان پیش‌بینی برای هزینه‌های آینده ذخیره می‌شوند



### مزایای Phoenixd



**شما کلیدهای خصوصی (seed 12-کلمه‌ای) و وجوه خود را کنترل می‌کنید. Phoenixd به صورت محلی Wallet شما را تولید می‌کند بدون اینکه هرگز کلیدهای شما را به اشتراک بگذارد.



**زیرساخت شخصی:** Phoenixd بر روی سرور شما اجرا می‌شود و به شما دسترسی به گزارش‌های دقیق، پیکربندی و کنترل API می‌دهد. شما دیگر برای دسترسی به وجوه خود به خدمات شخص ثالث وابسته نیستید.



**API یکپارچه:** Phoenixd دارای یک API HTTP برای یکپارچه‌سازی با سایر خدمات، پشتیبانی بومی از LNURL و توسعه برنامه‌های سفارشی است.



**سهولت در یکپارچه‌سازی:** به لطف API ساده REST، Phoenixd می‌تواند در هر برنامه یا سرویسی که نیاز به پرداخت‌های Lightning دارد، یکپارچه شود.



**توجه مهم:** نقدینگی خودکار همچنان از ACINQ به عنوان LSP (ارائه‌دهنده خدمات لایتنینگ) تأمین می‌شود. Phoenixd از همان مکانیزم Phoenix موبایل برای مدیریت خودکار کانال استفاده می‌کند.



## نصب Phoenixd



### پیش‌نیازها



فینیکسد به یک محیط لینوکس (توصیه می‌شود اوبونتو/دبیان) نیاز دارد، همراه با مهارت‌های پایه در خط فرمان. برای عملکرد بهینه، شما نیاز خواهید داشت به:





- سرور لینوکس**: VPS یا ماشین محلی با اتصال پایدار
- محیط اجرای جاوا : OpenJDK 21**
- اتصال اینترنت پایدار**: برای همگام‌سازی با Lightning Network
- نام دامنه** (اختیاری): برای دسترسی امن HTTPS به API



### دانلود و نصب



**1. دانلود Phoenixd**



به صفحه [انتشارهای GitHub](https://github.com/ACINQ/phoenixd/releases) بروید و آخرین نسخه مناسب برای معماری خود را دانلود کنید:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. اولین راه‌اندازی**



شروع Phoenixd برای راه‌اندازی:



```bash
./phoenixd
```



در اولین اجرا، از شما خواسته می‌شود تا با تایپ "متوجه شدم" دو مرحله مهم را تأیید کنید:



**پیام 1 - پشتیبان‌گیری:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**این ۱۲ کلمه را ذخیره کنید** - این تنها تضمین بازیابی شماست.



**پیام ۲ - نقدینگی خودکار:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



برای هر تأیید `I understand` را تایپ کنید.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd برای اولین بار راه‌اندازی می‌شود: تأییدیه‌های پشتیبان و نقدینگی خودکار*



**3. پیکربندی در حال سرویس** (فقط به زبان فرانسوی)



برای عملیات مداوم، یک systemd ایجاد کنید:



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*سرویس Phoenixd فعال و عملیاتی از طریق systemd و `auto-liquidity` در ۲ میلیون سات*



## پیکربندی و امنیت



### پرونده پیکربندی



Phoenixd به‌طور خودکار `~/.phoenix/phoenix.conf` را با پارامترهای ضروری ایجاد می‌کند:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**پارامترهای کلیدی:**




- `auto-liquidity`: اندازه کانال‌های خودکار باز شده (پیش‌فرض: 2M Sats)
- `http-password`: رمز عبور مدیر برای API (ایجاد Invoice و ارسال پرداخت)
- http-password-limited-access`: رمز عبور محدود (فقط ایجاد Invoice)



### دسترسی امن با HTTPS



به طور پیش‌فرض، API فینیکسد فقط از طریق HTTP محلی (`http://127.0.0.1:9740`) قابل دسترسی است. برای استفاده از نود خود از خارج (برنامه‌های موبایل، سرورهای دیگر، یکپارچه‌سازی‌های وب)، نیاز به پیکربندی دسترسی امن HTTPS دارید.



**اصل عملکرد پروکسی معکوس:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** به عنوان یک **پراکسی معکوس** عمل می‌کند: درخواست‌های HTTPS را از اینترنت روی پورت 443 گوش می‌دهد، آن‌ها را به صورت محلی به Phoenixd (پورت 9740) هدایت می‌کند، سپس پاسخ‌های رمزگذاری‌شده را به مشتری ارسال می‌کند.



گواهینامه **SSL/TLS** یک فایل دیجیتال است که :




- هویت سرور خود را اثبات کنید** (از حملات مرد میانی جلوگیری می‌کند)
- فعال‌سازی رمزگذاری HTTPS**: تمام داده‌ها، از جمله رمزهای عبور API شما، در حین انتقال رمزگذاری می‌شوند
- صادر شده به صورت رایگان** توسط Let's Encrypt از طریق ابزار certbot



این پیکربندی به شما اجازه می‌دهد تا:




- دسترسی امن به API از اینترنت**
- رمزگذاری گذرواژه‌های API** خود در حین انتقال (برای جلوگیری از ارسال آن‌ها به صورت متن ساده)
- ادغام Phoenixd** در برنامه‌های خارجی که نیاز به HTTPS دارند
- رعایت استانداردهای امنیتی** برای APIهای مالی



این پروکسی معکوس HTTPS را با nginx پیکربندی کنید:



**1. Nginx** پیکربندی



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**۲. گواهی‌نامه SSL**



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### تست عملکرد



بررسی کنید که Phoenixd به درستی کار می‌کند:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



این دستورات باید اطلاعات JSON در مورد وضعیت و موجودی نود (در ابتدا خالی) را برگردانند.



![Commandes CLI](assets/fr/03.webp)



*دستورات Getinfo و getbalance برای بررسی وضعیت نود*



## استفاده از API



### اولین آزمون پذیرش



**1. ایجاد یک Lightning** Invoice



از API برای ایجاد اولین Invoice خود استفاده کنید:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### درک مکانیزم نقدینگی خودکار



**اصل اساسی:** هنگامی که یک پرداخت لایتنینگ دریافت می‌کنید، Phoenixd گاهی اوقات باید یک کانال جدید باز کند تا بتواند آن را دریافت کند. باز کردن این کانال هزینه‌ای دارد که به صورت **خودکار از** مبلغ دریافت شده کسر می‌شود.



**مثال عینی با 100,000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*اولین آزمون پذیرش: Sats 100k دریافت شد، مانده نهایی Sats 75.561 پس از کسر هزینه‌های نقدینگی*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**محاسبه هزینه:**




- هزینه خدمات**: 1% از ظرفیت کانال (2,115,000 Sats) = 21,150 Sats
- هزینه‌های Mining**: ~3,289 Sats (برای تراکنش On-Chain)
- مجموع**: 24,439 Sats به‌طور خودکار کسر شد



**تأیید با دستورات CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*موجودی نهایی پس از ارسال پرداخت: ۲۵۷ Sats باقی‌مانده پس از ارسال Lightning*



**اعتبار کارمزد برای پرداخت‌های کوچک:** اگر پرداخت‌هایی دریافت کنید که برای باز کردن یک کانال توجیه‌پذیر نیستند (< تقریباً 25k Sats)، آن‌ها در یک "اعتبار کارمزد" غیرقابل استرداد ذخیره می‌شوند. این اعتبار برای پرداخت کارمزدهای کانال در آینده زمانی که مبلغ کافی دریافت کنید، استفاده خواهد شد.



**2. دنبال کردن باز شدن کانال**



مشاهده گزارش‌های Phoenixd:



```bash
journalctl -u phoenixd -f
```



شما افتتاح کانال و کسر خودکار هزینه‌های نقدینگی را مشاهده خواهید کرد. هزینه‌ها بسته به شرایط Mempool و Bitcoin متفاوت است، اما همیشه شامل ۱٪ هزینه خدمات به علاوه هزینه فعلی Mining می‌شود.



**3. کانال را بررسی کنید**



```bash
./phoenix-cli listchannels
```



این دستور کانال‌های فعال شما را با وضعیت و موجودی آن‌ها نمایش می‌دهد.



### عملیات کامل API



Phoenixd یک API REST را روی پورت 9740 فعال می‌کند که امکان‌پذیر می‌سازد:



**عملیات پایه:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**مهم در مورد هزینه‌ها:**




- رسید**: 1% + هزینه Mining برای نقدینگی خودکار
- حمل و نقل**: 0.4% هزینه مسیریابی بر روی Lightning Network



**وب‌هوک‌ها:** وب‌هوک‌ها به Phoenixd این امکان را می‌دهند که به‌طور **خودکار به** برنامه‌های شما اطلاع دهد وقتی یک رویداد رخ می‌دهد (پرداخت دریافت شد، Invoice پرداخت شد، کانال باز شد، و غیره). به جای اینکه به‌طور مداوم از Phoenixd درخواست به‌روزرسانی کنید، برنامه شما یک اعلان HTTP فوری دریافت می‌کند.



**فروشگاه آنلاین شما به‌طور خودکار هنگامی که مشتری برای یک سفارش پرداخت می‌کند، یک اعلان دریافت می‌کند و این امکان را فراهم می‌کند که تراکنش به‌صورت فوری اعتبارسنجی شود.



پیکربندی در `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## برنامه‌های پیشرفته



### ادغام‌های LNURL



Phoenixd به‌طور بومی از پروتکل‌های LNURL برای یکپارچه‌سازی پیشرفته پشتیبانی می‌کند:



**LNURL-Pay:** پرداخت برای خدمات سازگار با LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** بازیابی وجوه از خدمات LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** احراز هویت از طریق لایتنینگ برای دسترسی به خدمات


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### ادغام با LNbits



طبق [مستندات رسمی](https://docs.lnbits.org/guide/wallets.html)، LNbits می‌تواند از Phoenixd به عنوان منبع تأمین مالی استفاده کند:



**پیکربندی LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



این یکپارچه‌سازی به شما اجازه می‌دهد تا زیرحساب‌های LNbits را که توسط نود Phoenixd شما پشتیبانی می‌شوند، ایجاد کنید و یک Interface مبتنی بر وب برای مدیریت چندین کیف پول Lightning فراهم می‌کند.



### برنامه‌های سفارشی



با تشکر از API جامع REST آن، می‌توانید توسعه دهید:



**تجارت الکترونیک:** ادغام مستقیم پرداخت‌های Lightning در فروشگاه شما


**خدمات اهدا:** سیستم‌های اهدا با فاکتورها و وب‌هوک‌های خودکار


**ربات‌های شبکه‌های اجتماعی:** ربات‌های تلگرام/دیسکورد با قابلیت انعام‌دهی


**پرداخت با لایتنینگ:** محتوای ویژه با پرداخت هزینه لایتنینگ در دسترس است



## ایمنی و بهترین روش‌ها



### محافظت از دسترسی



**رمزهای عبور API:** رمزهای عبور تولید شده به صورت خودکار کلیدهای خزانه لایتنینگ شما هستند. هرگز آنها را به اشتراک نگذارید و در صورت تردید آنها را تغییر دهید.



**فایروال:** هرگز پورت 9740 را مستقیماً به اینترنت باز نگذارید. همیشه از nginx با HTTPS استفاده کنید.



**احراز هویت پیشرفته:** استفاده از VPN یا Tailscale را برای محدود کردن دسترسی به سرور خود به دستگاه‌های مجاز در نظر بگیرید.



### پشتیبان‌گیری‌های ضروری



**بازیابی seed:** 12 کلمه خود را در مکانی امن و خارج از سرور ذخیره کنید. این تنها تضمین شما برای بازیابی است.



*~/.phoenix directory:** این پوشه را به طور منظم پشتیبان‌گیری کنید (پس از خاموش شدن Phoenixd) تا وضعیت کانال را حفظ کرده و روند بازیابی را تسریع کنید.



**کدهای بازیابی سرویس:** همچنین کدهای پشتیبان را برای تمامی سرویس‌هایی که در آن‌ها 2FA را با Phoenix خود فعال می‌کنید، نگه دارید.



### نظارت و نگهداری



**نظارت بر گزارش‌ها:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**به‌روزرسانی‌ها:** برای نسخه‌های جدید به [انتشارهای GitHub](https://github.com/ACINQ/phoenixd/releases) مراجعه کنید. به‌روزرسانی به سادگی جایگزینی فایل باینری و راه‌اندازی مجدد سرویس است.



## مقایسه با گزینه‌های جایگزین



### Phoenixd در مقابل Phoenix استاندارد



**استاندارد فونیکس (موبایل) :**




- ✅ نصب فوری، بدون نیاز به پیکربندی
- ✅ Interface موبایل شهودی
- ✅ همان ذخیره‌سازی خودکار به سبک Phoenixd
- ❌ بدون API برای توسعه‌دهندگان
- ❌ دسترسی به گزارش‌های دقیق وجود ندارد



**Phoenixd (سرور) :**




- ✅ API HTTP برای یکپارچه‌سازی‌ها
- ✅ دسترسی کامل به لاگ‌ها
- ✅ زیرساخت شخصی
- ❌ نیاز به مهارت‌های فنی دارد
- ❌ نیاز به تعمیر و نگهداری سرور



**هر دو از ACINQ به عنوان LSP خود برای نقدینگی خودکار استفاده می‌کنند.



### Phoenixd در مقابل LND/Core Lightning



**LND/هسته رعد و برق :**




- ✅ کنترل کامل، پروتکل کامل لایتنینگ
- ✅ جامعه بزرگ، اکوسیستم بالغ
- ❌ مدیریت نقدینگی پیچیده دستی
- ❌ منحنی یادگیری بزرگ



**فینیکسد :**




- ✅ مدیریت خودکار نقدینگی (مانند Phoenix mobile)
- ✅ API برای توسعه‌دهندگان
- ✅ پیکربندی ساده شده
- ❌ از ACINQ به عنوان LSP استفاده می‌کند (بدون مسیریابی مستقل)
- ❌ کمتر انعطاف‌پذیر از نودهای کامل



## حل مشکلات رایج



### مشکلات دسترسی به API



**خطای "احراز هویت ناموفق":**


۱. رمز عبور را در فایل `~/.phoenix/phoenix.conf` بررسی کنید.


۲. قالب احراز هویت را بررسی کنید `-u:password`


۳. مطمئن شوید که Phoenixd در حال اجرا است (`./phoenix-CLI getinfo`)



**مهلت‌های اتصال:**




- بررسی کنید که Phoenixd در پورت صحیح (9740) در حال گوش دادن است.
- دسترسی محلی را قبل از پیکربندی HTTPS آزمایش کنید
- بررسی لاگ‌ها: `journalctl -u phoenixd -f`



### مشکلات نقدینگی



**پرداخت‌ها نرسیده‌اند :**


1. بررسی کنید که مقدار از حداقل آستانه (~30k Sats) بیشتر باشد.


۲. برای شناسایی خطاهای کانال، لاگ‌ها را بررسی کنید


۳. در صورت لزوم Phoenixd را مجدداً راه‌اندازی کنید



**موجودی در "اعتبار هزینه":**


پرداخت‌های کوچک به عنوان یک پیش‌بینی ذخیره می‌شوند. مبلغ بزرگتری دریافت کنید تا باز شدن کانال را فعال کرده و این وجوه را آزاد کنید.



## نتیجه‌گیری



Phoenixd نمایانگر یک مصالحه عالی بین سهولت استفاده و حاکمیت فنی برای توسعه‌دهندگان است. این ابزار یک API لایتنینگ ساده اما قدرتمند با مدیریت خودکار نقدینگی ارائه می‌دهد و پیچیدگی نودهای سنتی لایتنینگ را از بین می‌برد.



این راه‌حل به‌ویژه برای توسعه‌دهندگان و شرکت‌هایی که مایلند:




- ادغام Bitcoin Lightning در برنامه‌های خود
- از پیچیدگی مدیریت کانال لایتنینگ اجتناب کنید
- از زیرساخت میزبانی‌شده خود بهره‌مند شوید
- یک API ساده و قابل اعتماد



با Phoenixd، شما زیرساخت خصوصی Lightning خود را با یک API مدرن REST و مدیریت خودکار جنبه‌های فنی می‌سازید. این راه‌حل ایده‌آلی برای دموکراتیزه کردن یکپارچه‌سازی Lightning در پروژه‌های شماست.



## منابع مفید



### مستندات رسمی




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - کد منبع و نسخه‌ها
- سرور Phoenix** سایت: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - مستندات کامل
- پرسش‌های متداول Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - پرسش‌های متداول



### پشتیبانی جامعه




- مشکلات GitHub** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - پشتیبانی فنی
- توییتر ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - اخبار و اطلاعیه‌ها