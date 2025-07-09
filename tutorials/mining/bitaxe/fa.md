---
name: راه‌اندازی یک BitAxe
description: چگونه یک BitAxe راه‌اندازی کنیم؟
---
![video](https://youtu.be/tvLSK8v0MK8)


### مقدمه


BitAxe یک پروژه متن‌باز است که توسط Skot ایجاد شده و [در GitHub موجود است](https://github.com/skot/bitaxe) و امکان آزمایش Mining با هزینه کم را فراهم می‌کند.


این دستگاه عملکردهای معروف Antminer S19 توسط Bitmain، پیشرو بازار در ASIC‌ها، ماشین‌های تخصصی برای Bitcoin Mining را مهندسی معکوس کرده است. اکنون، امکان استفاده از این چیپ‌های قدرتمند در پروژه‌های جدید متن‌باز وجود دارد. برخلاف Nerdminer، BitAxe قدرت محاسباتی کافی برای اتصال به Mining pool را دارد، که به شما اجازه می‌دهد به طور منظم مقداری ساتوشی کسب کنید. از سوی دیگر، Nerdminer فقط می‌تواند به چیزی که به آن solopool گفته می‌شود متصل شود، که مانند یک بلیط بخت‌آزمایی عمل می‌کند: شما شانس کمی برای برنده شدن کامل Block reward دارید.


نسخه‌های مختلفی از BitAxe وجود دارد که دارای تراشه‌ها و عملکردهای متفاوتی هستند:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

در این آموزش، ما از یک BitAxe Ultra 204 مجهز به چیپ BM1366 استفاده خواهیم کرد که برای Antminer S19XP استفاده می‌شود. این دستگاه قبلاً توسط فروشنده مونتاژ و فلش شده است.


### [فهرست خرده‌فروشان در این صفحه موجود است](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


به طور کلی، قدرت Supply به همراه آن فروخته می‌شود. در غیر این صورت، شما نیاز خواهید داشت که یک قدرت Supply با کابل جک 5V و حداقل 4A خریداری کنید.


![signup](assets/1.webp)


### پیکربندی

هنگامی که برای اولین بار BitAxe خود را وصل می‌کنید، به طور پیش‌فرض تلاش می‌کند به یک شبکه Wi-Fi متصل شود. پس از پنج تلاش، نام شبکه Wi-Fi خود را نمایش می‌دهد تا بتوانید به آن متصل شده و آن را پیکربندی کنید.

برای انجام این کار، می‌توانید از هر کامپیوتر یا گوشی هوشمندی استفاده کنید. به تنظیمات Wi-Fi خود بروید، به دنبال شبکه‌های جدید بگردید و یک Wi-Fi به نام Bitaxe_XXXX را خواهید دید. در اینجا، `Bitaxe_A859` است. به این شبکه Wi-Fi متصل شوید و یک پنجره به‌طور خودکار باز خواهد شد.


![signup](assets/3.webp)


در این پنجره، روی سه نوار افقی کوچک در بالا سمت چپ کلیک کنید، سپس روی `Settings` کلیک کنید.


![signup](assets/4.webp)


شما باید اطلاعات شبکه Wi-Fi خود را به صورت دستی وارد کنید، زیرا سیستم کشف خودکار وجود ندارد.


![signup](assets/5.webp)


بنابراین، SSID وای‌فای، یعنی نام شبکه خود، رمز عبور، و همچنین اطلاعات Mining pool که انتخاب کرده‌اید را مشخص کنید. دقت کنید، در اینجا URL استخر به همان صورت ارائه نمی‌شود. به عنوان مثال، برای Braiins، URL استخر ارائه شده به این صورت است: `stratum+tcp://eu.stratum.braiins.com:3333`.


![signup](assets/6.webp)


همانطور که روی صفحه می‌بینید، باید قسمت‌های `stratum+tcp://` و `:3333` را حذف کنید و تنها `eu.stratum.braiins.com` را باقی بگذارید. سپس، در فیلد `Port`، ۴ رقم انتهای URL داده شده توسط استخر را وارد کنید، اما بدون `:`. در اینجا، بنابراین `3333` است.


در این آموزش، ما از Braiins Mining pool استفاده می‌کنیم، اما شما آزاد هستید که یکی دیگر را انتخاب کنید. می‌توانید آموزش‌های ما در مورد استخرهای Mining را [در وب‌سایت PlanB Network](https://planb.network/en/tutorials/Mining) پیدا کنید.


سپس، در قسمت `User`، شناسه خود را وارد کنید و سپس `Password` را وارد کنید، معمولاً این مقدار `"x"` یا `"Anything123"` است.


تنظیم `Core Voltage` باید به طور پیش‌فرض روی `1200` باقی بماند و برای `Frequency` نیز ابتدا مقدار پیش‌فرض را نگه دارید. امکان تنظیم این مقدار در آینده برای دستیابی به قدرت محاسباتی بیشتر وجود خواهد داشت. با این حال، مهم است که اطمینان حاصل کنید دمای چیپ از 65-70°C تجاوز نکند، زیرا BitAxe سیستمی برای کاهش عملکرد در صورت گرمای بیش از حد ندارد. اگر دما بیش از حد از 65°C تجاوز کند، ممکن است به BitAxe شما آسیب برساند.


![signup](assets/7.webp)


پس از وارد کردن صحیح تمام تنظیمات، روی دکمه `ذخیره` در پایین کلیک کنید، سپس BitAxe خود را به سادگی با جدا کردن و دوباره وصل کردن آن، راه‌اندازی مجدد کنید.

اگر اطلاعات خود را به درستی وارد کرده باشید، دستگاه باید به سرعت به وای‌فای شما و سپس به Mining pool متصل شود و شروع به نمایش برخی اطلاعات بر روی صفحه نمایش کوچک خود کند. احتمالاً چند دقیقه طول می‌کشد تا این اطلاعات بر روی داشبورد Mining pool ظاهر شود.

### داشبورد و صفحه نمایش


سه نمایشگر مختلف پیمایش خواهند کرد. در صفحه سوم، اطلاعات `IP` را خواهید دید که IP Address است و به شما امکان اتصال به داشبورد را می‌دهد. در اینجا، Address برابر است با `192.168.1.19`.


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


برای دسترسی به داشبورد، به سادگی این Address را در مرورگر اینترنت خود وارد کنید.


روی داشبورد، تمام اطلاعاتی که روی صفحه نمایش کوچک نمایش داده می‌شود را خواهید یافت، که اکنون به طور دقیق به آن خواهیم پرداخت.


![signup](assets/11.webp)


| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |

شما می‌توانید تنظیمات وای‌فای یا استخر را در هر زمان بدون هیچ مشکلی تغییر دهید.

بسته به تهویه و دمای اتاق شما، ممکن است نیاز داشته باشید عملکرد را افزایش دهید یا کاهش دهید تا دما از 65°C تجاوز نکند. اگر عملکرد را افزایش دهید، ساتوشی‌های بیشتری کسب خواهید کرد، اما BitAxe شما نیز برق بیشتری مصرف خواهد کرد!