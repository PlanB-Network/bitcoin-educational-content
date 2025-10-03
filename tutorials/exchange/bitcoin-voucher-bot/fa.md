---
name: BitcoinVoucherBot
description: یک ربات تلگرام برای خرید Bitcoin به صورت محرمانه
---
![image](assets/cover.webp)


_این آموزش نوشته شده توسط_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## مقدمه


ربات BitcoinVoucherBot ابزاری است که با آن می‌توان بیت‌کوین‌ها را در Exchange با یورو خریداری کرد.


### KYC Light


اقدام به تبدیل یورو به Bitcoin اولین و اساسی‌ترین گام برای شروع مطالعه این موضوع است، اما ظاهراً این نیز دشوارترین و پیچیده‌ترین است. گزینه‌های زیادی می‌تواند وجود داشته باشد: ارائه Bitcoin از طریق صرافی‌های متمرکز، ملاقات‌های مرتبط با Bitcoin، دوستان، آشنایان و موارد دیگر. ما به جامعه بیت‌کوینر می‌پیوندیم و **ما به شدت استفاده از صرافی‌های متمرکز را توصیه می‌کنیم** تا توجه بیشتری به حفظ حریم خصوصی خود داشته باشیم.


اگرچه این انتخاب ممکن است کمتر راحت باشد، اما مهم است که درک کنیم که صرافی‌ها مقررات شناخت مشتری (KYC) را اجرا می‌کنند و به این ترتیب به هر Satoshi خریداری شده از آنها یک هویت و همچنین یک مکان فیزیکی اختصاص می‌دهند. "راحتی" برخی عوارض جانبی چشمگیر دارد.


### چگونه آن را انجام دهیم؟


در اینجا سرویس [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot) آمده است، یک ربات تلگرام که به عنوان واسطه‌ای بین انتقال‌های SEPA ما و خریدهای Sats عمل می‌کند.


### پیش‌نیازها


برای شروع استفاده از BitcoinVoucherBot، نیازی به ارائه اطلاعات حساس شخصی به کارکنان Bot نیست. **نیازی به مجوز نیست**.


تنها چیزی که لازم است، یک حساب تلگرام فعال و یک حساب بانکی است. **توجه**: حسابی که با Poste Italiane (برای مشتریان ایتالیایی) باز شده یا به طور کلی به یک کارت قابل شارژ اشاره دارد، مناسب نیست.


در چت تلگرام سفارش را آماده می‌کنیم، با انتقال بانکی هزینه آن را پرداخت می‌کنیم، و در نهایت از طریق ربات یک ووچر دریافت می‌کنیم که توسط یک شرکت ثالث صادر شده و از موضوع خرید اطلاعی ندارد.


### فعال‌سازی ربات و منو


فعال‌سازی یک عملیات ساده و یک‌باره است. در تلگرام، به دنبال _@BitcoinVoucherBot_ بگردید و به محض ورود به چت بات، یک دکمه بزرگ _Start/Start_ در پایین صفحه به چشم می‌خورد. این عملیات باعث می‌شود که بات پاسخ دهد و منویی از دستورات اصلی موجود را ارائه دهد. پیام‌های خوش‌آمدگویی اولیه نیز ظاهر می‌شوند که توصیه می‌کنیم با دقت خوانده شوند.


**توجه**: چندین کلاهبردار وجود دارند که خود را به جای VoucherBot اصلی جا می‌زنند. اگر در جستجو از طریق تلگرام مطمئن نیستید، به لینک BitcoinVoucherBot از [وب‌سایت رسمی](https://www.bitcoinvoucherbot.com/) مراجعه کنید


![image](assets/it/01.webp)


گزینه‌ها با کلیک بر روی دکمه _Menu_ در گوشه پایین سمت چپ ظاهر می‌شوند: شما می‌توانید بر روی کلمه‌ای که با فرمان مطابقت دارد کلیک کنید، یا در کادر پیام، اسلش `/` را به همراه فرمان تایپ شده وارد کنید.


![image](assets/it/02.webp)


عملیات عمده شامل:




- _/purchase_: روند واقعی خرید است. هنگامی که تراکنش تکمیل شد، کد QR به‌طور خودکار توسط ربات تولید می‌شود و آماده‌ی استفاده است.
- _/refill_: در زمان نوشتن این آموزش در دسترس است، اما به دلایل فنی این گزینه ممکن است بعداً حذف شود، بنابراین آن را پوشش نخواهیم داد.
- _/swap_: فرایند تعویض را باز می‌کند، که هم از طریق یک ربات تلگرام راحت و هم از طریق وب در دسترس است.
- _/ap_: طرح انباشت، که به شما اجازه می‌دهد یک **طرح انباشت ثابت (CAP)** تنظیم کنید.
- _/lnaddress_: که از ما خواسته شده است یک LN Address خود را برای یک فرآیند خاص که بعداً خواهیم دید، لینک کنیم.
- _/credits_: برای بررسی میزان اعتبار باقی‌مانده در کوپن‌های generate.
- _/myorders_: سفارش‌های ثبت‌شده با ربات را نشان می‌دهد (**هشدار** سیستم فقط ۱۰ سفارش آخر را پیگیری می‌کند و نه کل تاریخچه).
- _/fees_: a command to check network fees. To evaluate them, it is always best to rely on Mempool.space.
- _/support_: in case of need, pops up contacts to report issues to the support team.


## روند خرید بیت‌کوین


### آماده‌سازی سفارش


Click _/purchase_ in the command menu


![image](assets/it/03.webp)


A number of opportunities appear, but we choose _BTC Vouchers_


![image](assets/it/04.webp)


BitcoinVoucherBot allows you to purchase Bitcoin onchain, Lightning and Liquid.


At this stage choose _Onchain & Lightning 🔗⚡️_


![image](assets/it/05.webp)


The screen changes quickly and VoucherBot proposes purchase denominations. They start from a minimum of €100.00 up to €900.00.


In case of a first purchase, only the 100.00 €, Onchain and Lightning denominations are offered. To increase privacy, we suggest choosing _Lightning ⚡️_


![image](assets/it/06.webp)


The VoucherBot alerts us that a first choice has been made and that, to confirm it, we need to choose _Proceed_


![image](assets/it/07.webp)


It is now a matter of choosing the payment method. The transfer is made by wire transfer **(accepted only SEPA)**. VoucherBot proposes as a receiver a company that provides two bank accounts, one in U.K and the other in Switzerland. The Swiss bank was chosen to carry out this tutorial


![image](assets/it/08.webp)


At this point we are asked to enter our IBAN, the one from which the transfer to the chosen bank will start. This information goes to make up a puzzle that will allow the bot, i.e., a machine, to put together some information to make the purchase process flow without the need for human intervention.


The IBAN must be written in the message bar, checked, and sent to the bot.


![image](assets/it/09.webp)


A control message now appears in the chat with VoucherBot.


If everything is correct, continue by clicking _Proceed_.


![image](assets/it/10.webp)


### پرداخت


After a few moments, necessary to process the data, VoucherBot replies with a message containing all the details necessary to complete the order. Depending on what your bank requires, the relevant information is:




- `IBAN`, which is essential for the deposit, as well as the recipient`s Address;
- `the amount chosen` previously through the cutoff, which must be met to allow VoucherBot to recognize the order when payment is received;
- `Payment reason`, which is the reason for the payment. **Must be copied and pasted without removing or adding anything in the appropriate field of your transfer. Any "." or "-" present in the payment reason, may be replaced by `white space'**.
- a unique `OrderID` to refer to when requesting any assistance.


You can then proceed with the payment, via your app or bank. When the payment has been accepted by the bank, it is important to remember to press _Notify payment_ in the chat with VoucherBot. This simple operation alerts you that a payment is on its way.


![image](assets/it/11.webp)


VoucherBot responds with a message that contains a very important warning: **don't delete the chat**, at least until the voucher is received, because it is the only means of reconstructing the order and keeping it going.


![image](assets/it/12.webp)


---
Please note:




- only SEPA wire transfers are accepted;
- wait times are solely related to how the banks (which do not work 24/7/365 like Bitcoin) process the voucher. It may take from a few hours up to 3 working days to receive the voucher;
- for any needs, Bitcoin VoucherBot has an excellent [support](https://t.me/BitcoinVoucherGroup) service on Telegram.


---
### بازخرید


As soon as the payment is successful, Bitcoin VoucherBot sends the voucher directly into the chat. The lightning voucher is in the form of a QR code, printed on an orange background.


![image](assets/it/31.webp)


There is all the data needed to cash it in:




- the amount in Sats, equivalent to that sent by wire transfer, excluding service fees and network fees;
- a reference ID of the voucher;
- the date by which the voucher must be redeemed or else funds will be lost, i.e., 25 days after issuance.


You can cash in the voucher by framing the QR code with the scan function of a compatible Wallet Lightning Network, or via LNURL, also shown below the QR code.


برای این آموزش ما از Wallet Of Satoshi استفاده کردیم و از عملکرد اسکن که با دکمه _Send_ فعال می‌شود بهره بردیم.


![image](assets/it/32.webp)


With the cell phone camera activated, frame the QR code in the chat, opening Telegram from PC


![image](assets/it/34.webp)


پیش از ادامه، Wallet Of Satoshi صفحه‌ای برای بررسی نمایش می‌دهد که شامل مبلغی است که دقیقاً با مبلغ درج‌شده روی ووچر مطابقت دارد و به‌عنوان توضیح، BitcoinVoucherBot ذکر شده است. برای نقد کردن ووچر کافی است روی _Receive_ کلیک کنید.


![image](assets/it/35.webp)


Wallet Of Satoshi برای چند لحظه پردازش می‌کند.


![image](assets/it/36.webp)


and finally the collection is reported and immediately available in the Wallet balance.


**Wallet of Satoshi یک اپلیکیشن امانی است: بلافاصله پس از نقد کردن ووچر توصیه می‌شود ساتس‌ها را به کیف پول غیرامانی منتقل کنید.**


![image](assets/it/37.webp)


### How to cash in an onchain voucher


As we saw in the order preparation, VoucherBot allows Sats to be purchased directly onchain, with the choice of the eponymous voucher.


**Note**: Order preparation and payment do not change, they are always the same. What does change is how an onchain voucher is cashed.


After completing the order, making the payment, pressing _Notify payment_ and waiting for the banks' technical time to transfer the transfer, VoucherBot will respond by sending the voucher directly into the chat.


This voucher is also in the form of a QR code, but the main color is canary yellow and-most importantly-in the description it is well explained that it is an onchain voucher, which you cash directly on your Wallet onchain and, to start the cash-out procedure, you have to click on _Redeem on Telegram_. The onchain voucher also contains the information already seen for the lightning one:




- the amount in Sats, equivalent to that sent by wire transfer, excluding service fees and network fees;
- a voucher code;
- a reference ID of the voucher;
- the date by which the voucher must be redeemed or else funds will be lost, i.e., 25 days after issuance.


![image](assets/it/22.webp)


**WARNING ⚠️:** clicked as explained, pop-up of another bot opens: **Voucher RedeemBot.**


Voucher RedeemBot is the tool made available for this purpose. Whether this is the first use or there are previous orders, each time a new redemption is made it is always necessary to click _START_.


![image](assets/it/23.webp)


At this point RedeemBot loads the onchain voucher, easily recognized by Voucher Code and reference ID. It also unlocks the bar to write messages and start chatting with the bot, which in fact invites us to tell it an onchain Address of our Wallet.


**Note**: This Address must be of type SegWit.


![image](assets/it/24.webp)


We open our Wallet at this point and generate a SegWit Address


![image](assets/it/25.webp)


we copy it


![image](assets/it/26.webp)


and paste it into the chat with RedeemBot


![image](assets/it/27.webp)


We now have a check screen, to verify the voucher code is correct, as well as the Address we have communicated to RedeemBot. Let's check it well because, by clicking _Proceed_, the transaction starts and there will be no way to find it again if we have, for example, communicated the wrong Address.


![image](assets/it/28.webp)


The transaction has started and the Redeem procedure of the onchain voucher thus ends.


![image](assets/it/29.webp)


while the amount can be seen coming in the history of our Wallet.


![image](assets/it/30.webp)