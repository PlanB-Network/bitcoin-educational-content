---
name: Lightning Smoke Machine
description: یک دستگاه دودزا را با پرداخت لایتنینگ از طریق ESP32 فعال کنید.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## مقدمه



یک دستگاه دود کلاسیک را به دستگاهی تبدیل می‌کند که در Bitcoin از طریق Lightning Network قابل پرداخت است. هر پرداخت به‌طور خودکار یک جت دود را فعال می‌کند!





- سطح: متوسط
- زمان تخمینی: ۲-۳ ساعت
- موارد استفاده: رویدادهای Bitcoin، اجراهای هنری، دموهای سریع، افکت‌های صحنه‌ای خودکار



## پیش‌نیازها



### دانش





 - الکترونیک پایه (سیم‌کشی، رله‌ها)
 - جوشکاری (یا استفاده از کانکتورهای دوپونت)
 - پیکربندی شبکه (WiFi، WebSocket)



### حساب‌ها مورد نیاز است





- سرور BTCPay: نمونه کاربردی (میزبانی‌شده توسط خود یا میزبانی‌شده)
- Blink Wallet : حساب + دسترسی API



### دسترسی





- دسترسی ادمین به سرور BTCPay
- اتصال WiFi برای ESP32



## مواد مورد نیاز



### سخت‌افزار - قطعات الکترونیکی





- ۱ میکروکنترلر - ESP32-WROOM-32


*ESP32-WROOM-32 یک میکروکنترلر WiFi/Bluetooth کم‌هزینه و جمع‌وجور است که برای اتصال دستگاه‌های الکترونیکی به اینترنت و کنترل آن‌ها از راه دور استفاده می‌شود*



![ESP32](assets/fr/1.webp)





- ماژول رله 1 کاناله - 5 ولت با اپتوکوپلر


*رله مانند یک سوئیچ است که ESP32 می‌تواند برای روشن یا خاموش کردن دستگاه دود از آن استفاده کند*



![relay](assets/fr/2.webp)





- ~10 کابل دوپونت - نر/نر و نر/ماده



![dupont-cables](assets/fr/3.webp)





- 1 منبع تغذیه برای ESP32 - 5V USB یا باتری Li-Po



![battery](assets/fr/4.webp)





- ۱ کابل میکرو USB - اتصال بین ESP32 و منبع تغذیه



![micro-usb-cables](assets/fr/5.webp)





- 1 دستگاه مه ساز 220 ولت با کنترل از راه دور باتری 12 ولت



![remote-and-smoke-machine](assets/fr/6.webp)





- ۱ بطری مایع سازگار با دستگاه دود شما



### سخت‌افزار - ابزارها





- هویه + قلع (در صورت لحیم‌کاری)
- پیچ‌گوشتی
- مولتی‌متر (توصیه‌شده)



### نرم‌افزار





- سفت‌افزار BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- مرورگر وب سازگار با WebSerial (Chrome/Edge/Brave)
- سرور BTCPay پیکربندی شد. برای اطلاعات بیشتر در مورد ایجاد یک نمونه سرور BTCPay، به این آموزش مراجعه کنید: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## معماری سیستم



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **هشدار ایمنی - قبل از ادامه مطالعه کنید** **⚠️**



این پروژه شامل یک دستگاه مه‌ساز متصل به **برق اصلی ۲۲۰ ولت** است. عملکرد نادرست می‌تواند منجر به **برق‌گرفتگی کشنده** یا **آتش‌سوزی** شود.



**قوانین غیرقابل مذاکره:**



1. **همیشه دستگاه دودزا را از برق جدا کنید** قبل از باز کردن کنترل از راه دور یا دستکاری سیم‌کشی


2. **باتری را از کنترل از راه دور خارج کنید** قبل از دست زدن (خطر اتصال کوتاه و آسیب به قطعات)


3. **اطمینان حاصل کنید که تمام اتصالات شما ایزوله شده‌اند** قبل از اینکه چیزی را دوباره وصل کنید.


4. **هرگز 220 ولت را دوباره وصل نکنید** تا زمانی که جعبه کنترل از راه دور بسته و محکم نشده باشد.



اگر با این نوع برخورد راحت نیستید، کسی را با خود ببرید که راحت باشد.



---

## بخش ۱: مونتاژ سخت‌افزار



### مرحله 1: آماده‌سازی کنترل از راه دور



هدف: رله را به دکمه روشن/خاموش روی کنترل از راه دور وصل کنید


1. کنترل از راه دور را باز کنید




    - دکمه روشن/خاموش را شناسایی کنید
    - پیچ‌های قاب را باز کنید تا کنترل از راه دور باز شود.


۲. اتصالات را پیدا کنید




 - پایانه‌های + و - را پیدا کنید.
 - تست تداوم با مولتی‌متر (اختیاری)



![smoke-machine-remote](assets/fr/8.webp)



۳. سیم‌کشی دکمه (لحیم‌کاری یا کانکتورها)




    - یک کابل سیاه را به ترمینال - دکمه لحیم کنید.
    - یک کابل قرمز را به ترمینال مشترک + لحیم کنید



![smoke-machine-remote](assets/fr/9.webp)



### مرحله 2: اتصال به ماژول رله



**یادآوری: اصطلاحات رله**




| **پایانه**         | **توضیح**           | **عملکرد**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (معمولاً باز)   | مدار به طور پیش‌فرض باز است | هنگام فعال شدن رله بسته می‌شود |
| NC (معمولاً بسته) | مدار به طور پیش‌فرض بسته است  | هنگام فعال شدن رله باز می‌شود  |
| COM (مشترک)         | پایانه مرکزی          | بین NO و NC تغییر می‌کند              |

**سیم‌کشی از کنترل از راه دور به ماژول رله:**




- سیم سیاه از دکمه روشن/خاموش **→** NO (به طور معمول باز)
- سیم قرمز (مشترک) **→** COM (مشترک)



**منطق:**


هنگامی که ESP32 رله را فعال می‌کند، COM و NO را متصل می‌کند، که دقیقاً مانند فشار دادن دکمه کنترل از راه دور است.


وقتی ESP32 رله را قطع می‌کند، COM و NO جدا می‌شوند که معادل رها کردن دکمه است.



![remote-relay](assets/fr/10.webp)



### مرحله 3: اتصال ESP32 به ماژول رله



**نمودار سیم‌کشی:**




| **ESP32** | **→** | **ماژول رله** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (ورودی)        |

**تأیید:**




- VCC و GND به خوبی متصل شده‌اند (قطبیت)
- GPIO 21 برای سیگنال کنترل استفاده می‌شود
- مدار کوتاه قابل مشاهده نیست



![relay-esp32](assets/fr/11.webp)



**سخت‌افزار چک‌پوینت**


قبل از تغییر به نرم‌افزار، بررسی کنید:




- کنترل از راه دور به درستی سیم‌کشی شده
- ماژول رله متصل به ESP32
- هیچ سیم لختی با سایر قطعات تماس نداشته باشد
- همیشه 220V قطع است



![relay-esp32](assets/fr/12.webp)





---


## بخش ۲: پیکربندی نرم‌افزار



ما از *Blink* به عنوان مثال استفاده خواهیم کرد، اما *BTCPay Server* همچنین *Strike, Breez و Boltz* را نیز ارائه می‌دهد اگر گزینه دیگری را ترجیح می‌دهید.



### مرحله 1: پلاگین‌ها، نصب *BitcoinSwitch* + *Blink



۱ - به نمونه *BTCPay Server* خود با یک حساب کاربری مدیر بروید



۲ - اولین کور خود را ایجاد کنید



۳ - در سمت چپ *BTCPay Server*، به پایین بروید و به *"Manage Plugins "* بروید.



![btcpay-plugins](assets/fr/13.webp)



۴ - ما قصد داریم افزونه‌های *BitcoinSwitch* و همچنین *Blink* را نصب کنیم.



![btcpay-plugins](assets/fr/14.webp)



5 - به لیست پلاگین‌ها پایین بروید و روی *"نصب "* کلیک کنید: *BitcoinSwitch و Blink* (یا wallet موجود به انتخاب شما)



![btcpay-plugins](assets/fr/15.webp)



۶ - پس از اتمام نصب، *BTCPay Server* را مجدداً راه‌اندازی کنید و ۱ دقیقه صبر کنید تا نمونه مجدداً راه‌اندازی شود.



![btcpay-plugins](assets/fr/16.webp)



۷ - وقتی به *"مدیریت افزونه‌ها"* بازمی‌گردید، بررسی کنید که هر دو افزونه نصب شده‌اند.



![btcpay-plugins](assets/fr/17.webp)



### مرحله 2: پشتیبان : *پیکربندی BTCPay Server + Blink*



**1 - ایجاد یک wallet *Blink***




- از https://www.blink.sv دیدن کنید
- حساب خود را ایجاد کنید. لطفاً به آموزش مراجعه کنید:



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - تولید یک کلید API *Blink***




- به رابط API دسترسی پیدا کنید: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** و با همان حسابی که برای ایجاد wallet *Blink* استفاده کردید، وارد شوید.



![blink-api](assets/fr/18.webp)





   - پس از اتصال، به برگه *API Keys* بروید



![blink-api](assets/fr/19.webp)





   - برای دسترسی به پیکربندی کلید API خود، روی *" + "* در گوشه بالا سمت راست کلیک کنید.



![blink-api](assets/fr/20.webp)





   - به کلید API خود یک نام بدهید و تنظیمات پیش‌فرض را حفظ کنید. سپس، در مرحله سوم، کلید API خود را یادداشت کنید - شما فقط یک بار آن را خواهید دید: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - پس از ایجاد، باید در لیست کلیدهای فعال API شما ظاهر شود.



![blink-api](assets/fr/22.webp)



**3 - اتصال *Blink* به *BTCPay Server***




- *سرور BTCPay* خود را باز کنید
- به : *Wallet* **→** *Lightning* بروید



![btcpay-server](assets/fr/23.webp)





- روی *استفاده از نود سفارشی* کلیک کنید
- رشته اتصال زیر را جای‌گذاری کنید:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **مهم** :




- type=blink;server=https://api.blink.sv/graphql;
- فقط جایگزین کنید:
    - api-key= *توسط کلید API Blink شما*
    - wallet-id= *توسط wallet شما Blink* ID
- سپس روی *Test connection* کلیک کنید، سپس *Save*



![btcpay-server](assets/fr/24.webp)





 - بررسی کنید که اتصال برقرار شده است (وضعیت سبز)



![btcpay-server](assets/fr/25.webp)



**۴ - ایجاد یک نقطه فروش (PoS)**




- در سرور BTCPay، به برگه *افزونه‌ها* بروید و روی *نقطه فروش* کلیک کنید.



![btcpay-server](assets/fr/26.webp)





- به PoS خود یک نام بدهید و روی *ایجاد* کلیک کنید



![btcpay-server](assets/fr/27.webp)





- پیکربندی PoS :
    - یک سبک نقطه فروش را انتخاب کنید = *نمایش چاپ*
    - ارز = *SATS*
    - روی *ذخیره* کلیک کنید



![btcpay-server](assets/fr/28.webp)





- پیکربندی محصول :
    - حذف همه محصولات پیش‌فرض
    - سپس روی *افزودن آیتم* کلیک کنید



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- محصول را پیکربندی کنید:
    - عنوان: *دستگاه دود*
    - قیمت: *10 sats*
    - Bitcoin GPIO سوئیچ : 21
    - مدت زمان سوئیچ Bitcoin (به میلی‌ثانیه): 5000
    - روی *بستن* و سپس *ذخیره* کلیک کنید تا محصول جدید ذخیره شود



![btcpay-server](assets/fr/31.webp)



### مرحله 3: سیستم‌افزار: فلش کردن ESP32



**1 - به سایت فلش بروید




- به این آدرس بروید: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash سیستم‌عامل BitcoinSwitch**




- ESP32 را با کابل USB/Micro-USB به کامپیوتر خود وصل کنید
- سپس روی *اتصال به دستگاه* کلیک کنید
- یک پنجره باز می‌شود، پورت USB روی ESP32 خود را انتخاب کنید، سپس روی *Connect* کلیک کنید.



![bitcoinswitch-lnbits](assets/fr/33.webp)





- هنگامی که ESP32 شما متصل شد، ما فریمور BitcoinSwitch را فلش خواهیم کرد. در بخش *T-Display*، بر روی *Upload Firmware* برای آخرین نسخه موجود کلیک کنید (در حال حاضر: *bitcoinSwitch T-Display v1.0.1*).



![bitcoinswitch-lnbits](assets/fr/34.webp)





- منتظر آپلود بمانید، فرآیند زمانی کامل می‌شود که لاگ‌ها نشان دهند *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- اتصال ESP32 را قطع کنید



**3 - بررسی نصب سیستم‌عامل BitcoinSwitch




- بارگذاری مجدد صفحه: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- ESP32 را با کابل USB/Micro-USB به کامپیوتر خود مجدداً متصل کنید
- سپس روی *اتصال به دستگاه کلیک کنید
- پورت USB را روی ESP32 خود انتخاب کنید، سپس روی *اتصال* کلیک کنید همانطور که در بالا توضیح داده شد.
- پس از اتصال، دکمه **RESET** را روی ESP32 فشار دهید.
- بررسی کنید که خطوط آخر در گزارش‌ها نشان می‌دهند:



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(این طبیعی است، به این معنی که هنوز تنظیماتی وجود ندارد، اما فریمور نصب شده است)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - تولید WebSocket LNURL** URL



فرمت نهایی مورد انتظار :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



مراحل تولید :




- سرور BTCPay خود را باز کنید، سپس به PoS که بعداً ایجاد کردیم بروید.
- سپس روی "View" کلیک کنید تا PoS خود را در مرورگر باز کنید



![btcpay-server-https](assets/fr/37.webp)





- URL صفحه را کپی کنید، برای مثال :



![btcpay-server-https](assets/fr/38.webp)



بیایید این URL را باز کنیم:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → دامنه نمونه BTCPay Server شما
- `46XXXXXXXXXXXXXXXXXXXXwFB` → شناسه منحصر به فرد PoS شما
- `/pos` → نشان‌دهنده یک نقطه فروش است



تبدیلش کن:




- جایگزین کردن `https://` با `wss://`
- `/bitcoinswitch` را به انتها اضافه کنید



نتیجه:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



این URL را برای پیکربندی آینده نگه دارید، زیرا به ESP32 شما امکان می‌دهد تا به صورت لحظه‌ای با سرور BTCPay ارتباط برقرار کند. پروتکل WebSocket (`wss://`) یک اتصال دائمی بین این دو برقرار می‌کند: به محض اینکه یک پرداخت Lightning در PoS شما تأیید شود، BTCPay بلافاصله اطلاعات را به ESP32 ارسال می‌کند که سپس می‌تواند ماشین دود شما را فعال کند.



**5 - پیکربندی WiFi و WebSocket




- به صفحه بازگردید: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) با ESP32 خود متصل شده
- به *Configure Device* → *Wifi Settings* بروید



اطلاع دادن :




- SSID وای‌فای: نام شبکه وای‌فای شما
- رمز عبور وای‌فای: your WiFi password



![bitcoinswitch-lnbits](assets/fr/39.webp)





- در بخش *LNbits Device URL*، URL وب‌سوکت ایجاد شده در مرحله قبلی را جای‌گذاری کنید.
- روی *بارگذاری پیکربندی* کلیک کنید



![bitcoinswitch-lnbits](assets/fr/40.webp)





- منتظر بمانید تا بارگذاری کامل شود؛ لاگ‌ها باید پارامترهایی که به‌تازگی وارد کرده‌اید (SSID، رمز عبور و URL وب‌سوکت) را نمایش دهند.



![bitcoinswitch-lnbits](assets/fr/41.webp)





- صبر کنید تا ESP32 اتصال WebSocket را برقرار کند. شما باید ببینید:



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- اکنون می‌توانید ESP32 را قطع کنید



---
## چک‌پوینت سافت‌ور



قبل از آزمون نهایی، بررسی کنید:





- Blink متصل به BTCPay
- ایجاد PoS با حداقل 1 آیتم
- ESP32 با BitcoinSwitch فلش شده است
- وای‌فای پیکربندی شده بر روی ESP32
- آدرس URL وب‌سوکت صحیح
- گزارش‌های بدون خطای ESP32



---

## آزمایش و اشکال‌زدایی



### تکمیل آزمون نهایی



1. دستگاه دودزا را به برق وصل کنید (220 ولت) و آن را روشن کنید


۲. ESP32 را روشن کنید (باتری یا USB)


۳. BTCPay PoS خود را در مرورگر خود باز کنید


4. اسکن آیتم "smoke-machine"


۵. پرداخت با wallet Lightning (Blink یا سایر wallet)


۶. مشاهده کنید:




 - کلیک‌های رله (صدای قابل شنیدن و روشن شدن LED رله)
 - دستگاه دود فعال شده است
 - دود تولید شد!



### مشکلات و راه‌حل‌های انصاف




| **مشکل**                        | **علت احتمالی**              | **راه حل**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 متصل نمی شود            | درایور USB مفقود             | نصب [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| رله کلیک نمی کند                | سیم کشی GPIO غلط            | بررسی GPIO 21 → IN                                                                        |
| دستگاه دود پاسخ نمی دهد         | کنترل از راه دور نادرست سیم کشی شده         | بررسی NO/NC/COM                                                                           |
| زمان انتظار WebSocket                   | URL نادرست                  | بررسی wss:// و /bitcoinswitch                                                            |
| WiFi متصل نمی شود             | SSID/Password نادرست            | دوباره فلش کردن پیکربندی WiFi                                                                    |
| پرداخت دریافت شد اما هیچ اتفاقی نمی افتد | ESP32 به WebSocket متصل نیست | بررسی لاگ های RESET                                                                      |

## منابع



### لینک‌های مفید





- سفت‌افزار BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Server Docs : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- پین اوت ESP32 : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### انجمن و پشتیبانی





- سرور BTCPay** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Mattermost رسمی
- سرور BTCPay Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Telegram رسمی، جامعه فعال
- بیت‌کوین‌سوئیچ (اشکالات فریم‌ور)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### کد منبع





- کد منبع فریمور BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** پشته sats، دود کنید، لذت ببرید، فروتن بمانید! **⚡**