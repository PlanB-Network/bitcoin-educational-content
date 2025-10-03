---
name: LNbits

description: پلتفرم حسابداری بازرگان
---

![presentation](assets/lnbits-intro.webp)

# سیستم حسابداری


LNbits دارای ابزارهای زیادی برای کنترل و هدایت وجوه ورودی و خروجی شما است، اتصال فروشگاه وب یا حتی دستگاه‌هایی مانند Hardware Wallet یا یک دستگاه خودپرداز که خودتان ساخته‌اید. انواع کاربران شامل:


- صاحبان Wallet که می‌خواهند از LNbits به عنوان Interface برای مدیریت وجوه خود و همچنین ویژگی‌های اضافی آن استفاده کنند.
- فروشندگان آنلاین و آفلاین یا ارائه‌دهندگان خدماتی که می‌خواهند پرداخت‌های Bitcoin روی زنجیره و Lightning Network را بپذیرند.
- توسعه‌دهندگانی که می‌خواهند برنامه‌های Lightning Network بسازند.
- اپراتورهای نود که می‌خواهند نود خود را برای اهداف حسابداری با سیستم LNbits یکپارچه کنند.
- همه آن‌ها نیازهای متفاوتی دارند. ما LNbits را به صورت ماژولار ساخته‌ایم تا هر کاربر بتواند از ویژگی‌های ما به روشی که برای او بهترین است استفاده کند.


# مدیر Wallet


LNbits یک سیستم حسابداری رایگان و متن‌باز است - نه یک مدیر نود. مدیریت کانال حوزه‌ی نود لایتنینگی است که به عنوان منبع تأمین مالی به LNbits متصل شده است، مانند LND یا c-lightning. کاربران سوپر یوزر یا ادمین در سیستم LNbits مسئول مدیریت دسترسی کلی و پیکربندی ویژگی‌های حسابداری و افزونه‌های داخلی هستند.


LNbits به عنوان یک Interface بین کاربر و نود Lightning عمل می‌کند و روشی ساده و کاربرپسند برای مدیریت و تعامل با شبکه پرداخت فراهم می‌کند.


LNbits را مانند یک "چارچوب مدولار وردپرس" برای نود خود تصور کنید. یک پلتفرم آسان برای مدیریت، بر اساس افزونه‌هایی که می‌توانید برای موارد استفاده متعدد ترکیب کنید.


LNbits را به عنوان نرم‌افزار مدیریت مالی بانک خود در نظر بگیرید. نود شما کانال‌هایی برای پرداخت ارائه می‌دهد و LNbits نود شما را گسترش می‌دهد تا بتوانید بیش از یک Wallet لایتنینگ که نود شما با آن می‌آید را اجرا کنید. این کیف پول‌ها لزوماً نیازی به متعلق بودن به خودتان ندارند. فرض کنید شما، به عنوان اجراکننده نود LN، قبلاً به اندازه کافی نقدینگی کانال و وجوه دارید و اکنون می‌خواهید برخی خدمات بانکی Bitcoin را به دوستان، خانواده، فروشگاه خود یا سایر بازرگانان معمولی ارائه دهید.


شما یک روش ساده به آن‌ها ارائه خواهید داد تا یک "حساب بانکی" در نود شما باز کنند بدون اینکه به کیف‌پول‌های دیگر در نود شما و به تمام نقدینگی نود شما دسترسی داشته باشند، بلکه فقط به بخش خودشان. نود شما (بانک) فقط به عنوان یک ارائه‌دهنده حمل و نقل برای پرداخت‌های آن‌ها (ورودی/خروجی) عمل می‌کند.


توجه: تمام وجوهی که "مشتریان" شما به حساب‌های بانکی LNbits خود در نود شما واریز می‌کنند، مستقیماً به کانال‌های نود LN شما منتقل خواهند شد. این بدان معناست که شما در واقع مالک واقعی آن وجوه هستید. شما مسئولیت بزرگی برای وجوه آنها خواهید داشت. شرور نباشید و با وجوه فرار نکنید، شرور نباشید و کارمزدهای بالا دریافت نکنید. ما می‌خواهیم بانکداران فیات را شکست دهیم، نه اینکه به یکدیگر (کاربران Bitcoin) آسیب برسانیم.


# پلتفرم دمو


دمو را می‌توانید در [https://legend.lnbits.com](https://legend.lnbits.com) پیدا کنید. این دمو کاملاً کاربردی است و می‌توان از آن برای یادگیری درباره Lightning Network و ویژگی‌های LNbits و LNURL به طور کلی استفاده کرد. اگرچه نمی‌توانیم شما را از استفاده آن منع کنیم، اما از شما می‌خواهیم که از آن برای تنظیمات تولیدی خود استفاده نکنید. نه تنها ما اغلب روی سرورها کار می‌کنیم تا ویژگی‌های جدید را آزمایش کنیم، بلکه می‌خواهیم شما را تشویق کنیم که نود و LNbits خود را به صورت مستقل اجرا کنید. اگر فکر می‌کنید اجرای یک نود در حال حاضر بیش از حد درخواست شده است، می‌توانید LNbits را به یک سرویس تأمین مالی نگهبانی در ابر مانند Opennode، Luna یا Votage یا به Lightning Tipbot در تلگرام متصل کنید، فقط برای نام بردن از برخی.


# بروشور LNbits


می‌خواهید برخی اطلاعات پایه را به یک تاجر یا دوست سازنده خود بدهید؟ ما بسیار خوشحالیم که اولین بروشور خود را برای استفاده همگان اعلام کنیم. اندازه آن یک فرمت بروشور جهانی معمولی با ۶ صفحه (۲ تا خوردگی) و عرض ۳۵۰۸ و ارتفاع ۲۴۸۰ پیکسل است.


LNbits برای بازرگانان: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


LNbits برای سازندگان: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# برخی اصول اولیه


LNbits بر اساس پروتکل LNURL کار می‌کند که به این معنی است که درخواست‌ها به دو صورت معتبر هستند: یا به صورت لینک https:// clearnet (گواهی‌های خودامضا مجاز نیستند) یا به صورت لینک http:// v2/v3 onion. برای ارائه خدمات LNbits مانند کدهای QR LNURLp/w یا کارت‌های NFC که می‌توانند به صورت عمومی استفاده شوند، نیاز خواهید داشت که LNbits را به clearnet (https) باز کنید.


قبل از نصب LNbits مطمئن شوید که راهنماهای عمومی زیر را درباره اینکه LNbits چیست و چه امکاناتی را برای شما فراهم می‌کند، خوانده و درک کرده‌اید.



- [راهنمای LND](https://docs.lightning.engineering/) | نصب LND
- [مثال پیکربندی LND](https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | تنظیمات LND
- [راهنمای CLN](https://docs.corelightning.org/docs/installation) | نصب CLN
- [LUDs](https://github.com/lnurl/luds) مشخصات LNURL | [NIPs](https://github.com/nostr-protocol/nips) مشخصات Nostr
- [اجرای Watchtower](https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | بسیار مهم!


راهنماهای دقیق‌تر برای استفاده از LNbits در سناریوهای خاص استفاده در اینجا:



- [شروع به کار با LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | راهنمای Substack
- [کارهایی که برای ایمنی با LNbits باید انجام دهید](https://youtu.be/i5FQf96e6zg) | ویدئوی یوتیوب
- [بانک‌های خصوصی در Lightning Network](https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | راهنمای Substack
- [کیف پول‌های امانی را برای دوستان و خانواده خود اجرا کنید](https://darthcoin.substack.com/p/the-bank-of-lnbits) | راهنمای Substack
- [LNbits برای یک رستوران / هتل کوچک](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | راهنمای Substack
- [استفاده از LNbits Streamer copilot](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | راهنمای Substack
- [بازار NOSTR خود را با LNbits شروع کنید](https://darthcoin.substack.com/p/lnbits-nostr-market) | راهنمای Substack
- [استفاده از LNbits برای پروژه‌های مدارس یا رویدادهای جشنواره](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) راهنمای Substack



# نصب LNbits


## راهنمای نصب اولیه


LNbits را می‌توان بر روی هر ماشین با سیستم‌عامل لینوکس نصب کرد. این برنامه به یک ماشین یا سرور قدرتمند نیاز ندارد، فقط به اندازه کافی حافظه RAM و مقداری فضای دیسک برای پایگاه داده نیاز دارد. می‌توان آن را به صورت جداگانه از یک نود BTC/LN (کامپیوتر محلی یا VPS از راه دور) اجرا کرد یا بر روی همان ماشین با نود یا در یک ماشین نرم‌افزاری نود بسته‌بندی شده از قبل نصب شده اجرا کرد.


شما می‌توانید بین مدیران بسته‌بندی رایج مانند poetry و nix انتخاب کنید. به‌طور پیش‌فرض، LNbits از SQLite به عنوان پایگاه داده خود استفاده خواهد کرد. همچنین می‌توانید از PostgreSQL استفاده کنید که برای برنامه‌های با بار بالا توصیه می‌شود. [در اینجا یک راهنما برای نصب پایه با استفاده از poetry یا nix آمده است](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


برای همه کسانی که در این زمینه تازه‌کار هستند، راهنماهای گام‌به‌گام و دقیق‌تری برای راه‌اندازی LNbits در محیط‌های خاص پیدا خواهید کرد:


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) توسط Axel
- [LNbits روی یک VPS](https://github.com/TrezorHannes/vps-lnbits) توسط Hannes
- [LNbits روی cloudflare](https://www.nodeacademy.org/lnbits) توسط لئو


شما همچنین می‌توانید ویدئویی درباره [راه‌اندازی داکریزه شده روی یک VPS با PostgreSQ، LightningTipBot به عنوان منبع تأمین مالی با استفاده از nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/) پیدا کنید.


[سناریوهای نصب بیشتر اینجا](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).


برای نودهای نرم‌افزاری باندل، لطفاً به مستندات خاص آن‌ها درباره LNbits مراجعه کنید: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


وقتی به مسائل فنی علاقه‌مند نیستید و نمی‌خواهید منبع تأمین مالی یا lnbits خود را میزبانی کنید، یک [نسخه SaaS از LNbits](https://saas.lnbits.com) (نرم‌افزار به‌عنوان سرویس) وجود دارد که می‌توانید از آن استفاده کنید. این اساساً مانند LNbits در یک ابر است، اما شما می‌توانید منبع تأمین مالی (مثلاً نود خود، یک LNbits Wallet، LNtipbot، fakewallet و غیره) و متغیرهای محیطی را خودتان تعریف کنید - که در اکثر راه‌حل‌های ابری دیگر این‌گونه نیست.


[در اینجا یک راهنمای دقیق برای استفاده از LNbits SaaS برای موارد استفاده خاص ارائه شده است](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


## منابع تأمین مالی


LNbits یک نرم‌افزار مدیریت نود نیست بلکه یک سیستم حسابداری متمرکز بر LN است که بر روی یک منبع تأمین مالی LND یا CLN قرار دارد. پس از اولین نصب می‌توانید به LNbits خود در http://localhost:5000/ مراجعه کنید.


برای تغییر منبع تأمین مالی به URL سوپر-کاربر خود بروید و یک منبع تأمین مالی را در بخش "مدیریت سرور" انتخاب کنید یا فایل .env را با تغییر `LNBITS_BACKEND_WALLET_CLASS` به منبع مورد نیاز خود ویرایش کنید اگر `adminUI=TRUE` را در `.env` تنظیم کرده‌اید.


شما فایل .env را در پوشه lnbits/ یا lnbits/apps/data پیدا خواهید کرد با گسترش دستور برای لیست کردن فایل‌ها در دایرکتوری خود با `ls -a`.


ممکن است نیاز داشته باشید بسته‌های اضافی نصب کنید یا مراحل تنظیمات اضافی را انجام دهید و منبع تأمین مالی مورد نظر را انتخاب کنید. پس از راه‌اندازی مجدد، تنظیمات جدید شما فعال خواهد بود.


از کدام منابع تأمین مالی می‌توانم برای LNbits استفاده کنم؟


LNbits می‌تواند بر روی بسیاری از منابع تأمین مالی شبکه لایتنینگ اجرا شود. در حال حاضر از CoreLightning، LND، LNbits، LNPay، OpenNode پشتیبانی می‌شود و به‌طور منظم موارد بیشتری اضافه می‌شوند.

مهم است که منبعی را انتخاب کنید که نقدینگی خوبی داشته باشد و با همتایان خوبی متصل باشد. اگر از LNbits برای خدمات عمومی استفاده کنید، پرداخت‌های کاربران شما تنها در این صورت می‌توانند به راحتی در هر دو جهت جریان یابند.


یک Wallet بک‌اند (منبع تأمین مالی) می‌تواند با استفاده از متغیرهای محیطی LNbits در فایل `.env` یا در حساب کاربری سوپریوزر شما در بخش مدیریت سرور پیکربندی شود.

اگر می‌خواهید از نسخه .env استفاده کنید، می‌توانید پارامترها را اینجا پیدا کنید:



### کورلایتنینگ


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-RPC
- اسپارک (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon یا Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: پورت
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon یا Bech64/Hex

شما همچنین می‌توانید به جای آن از یک ماکارون رمزگذاری‌شده با AES (اطلاعات بیشتر) استفاده کنید با استفاده از


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

برای رمزگذاری ماکارون خود، `./venv/bin/python lnbits/wallets/macaroon/macaroon.py` را اجرا کنید.


### LNbits (نمونه دیگری از LNbits)



- نمونه LNbits میزبانی شده بر روی یک سرور ابری یا سرور خانگی خودتان
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! از این سرور برای مقاصد تولیدی / تجاری استفاده نکنید، فقط برای آزمایش !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### لایتنینگ تیپ‌بات


برای اتصال [Lightning Tipbot](https://t.me/LightningTipBot) خود از تلگرام، باید پارامتر زیر را تنظیم کنید:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://LN.tips
  - `LNBITS_KEY`: برای دریافت کلید، باید یک بار /api را در یک چت خصوصی با LightningTipbot در تلگرام اجرا کنید.


همچنین این آموزش را ببینید که چگونه [LNbits با LightningTipBot از طریق vps نصب کنید](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


### هاب آیبکس


[اینجا](https://ibexpay.ibexmercado.com/onboard) ثبت‌نام کنید سپس کلیدها/توکن‌های خود را از آنجا دریافت کنید، نقطه پایانی https://ibexpay-api.ibexmercado.com است.

برای اطلاعات بیشتر به [مستندات API آی‌بکس](https://ibexpay-api.readme.io/reference/getting-started-with-your-api) مراجعه کنید.


### LNPay

برای کارکرد شنونده Invoice، شما باید یک URL عمومی در LNbits خود داشته باشید و یک [وب‌هوک LNPay](https://dashboard.lnpay.co/webhook/) تنظیم کنید که به `<your LNbits host>/Wallet/webhook` با رویداد "Wallet Receive" و بدون ارائه رمز اشاره کند. تنظیم `https://mylnbits/Wallet/webhook` به عنوان آدرس پایانی خواهد بود که درباره هر پرداختی اطلاع‌رسانی می‌شود.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


### اوپن‌نود

برای کار کردن Invoice، شما نیاز دارید که یک URL عمومی قابل دسترسی در LNbits خود داشته باشید. تنظیمات webhook اختیاری است.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### آلبی


Alby یک افزونه مرورگر با قابلیت‌های LN Wallet و حساب LNDHUB است که می‌تواند به عنوان منبع تأمین مالی برای LNbits استفاده شود. [جزئیات بیشتر اینجا](https://getalby.com/).


برای کار کردن Invoice باید یک URL عمومی در LNbits خود داشته باشید. نیازی به تنظیم دستی webhook نیست. می‌توانید generate یک دسترسی Alby token را اینجا انجام دهید: https://getalby.com/developer/access_tokens/new



- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken


## راهنماهای اضافی / عیب‌یابی


در اینجا چند دستورالعمل اضافی وجود دارد در صورتی که به آنها نیاز داشته باشید. برای گسترش توضیحات روی فلش کلیک کنید.


### کل‌سوئیچ 🚨


اخیراً باگ‌های خطرناک زیادی نه تنها در کل فضا بلکه در LNbits وجود داشته است که تصمیم گرفتیم کاری در این مورد انجام دهیم. اکنون می‌توانید برای هشدارها و/یا اقدام مستقیم، زمانی که یک آسیب‌پذیری یا باگی که می‌تواند منجر به از دست رفتن وجوه شود دوباره رخ دهد، ثبت‌نام کنید.


![killswitchn](assets/lnbits-killswitch.webp)


اگر به void-Wallet تغییر داده شود، همه نوع کاربران در این نمونه یک بنر زرد خواهند دید که معمولاً در کنار ناحیه تم/زبان در بالا سمت راست، جایی که اعلان "LNbits در نسخه بتا است" قرار دارد، ظاهر می‌شود - و این واضح‌ترین نشانه است که چیزی اتفاق افتاده است. به تب سرور جدید خود که در Green در قسمت چپ پنجره برجسته شده است، نگاهی بیندازید.


چگونه کار می‌کند؟ وقتی که کلید قطع فعال می‌شود، یک مخزن مخفی گیت‌هاب که فقط برای تیم اصلی LNbits در دسترس است، در بازه‌های زمانی X دقیقه (که می‌تواند مشخص شود) بررسی می‌شود. اگر یک باگ آسیب‌پذیر در این مخزن منتشر شود، به عنوان سیگنالی عمل می‌کند که کلید قطع را در تمام نصب‌هایی که مشترک شده‌اند فعال می‌کند و نمونه lnbits شما را به استفاده از void Wallet منتقل می‌کند. اگر ابرها برطرف شده‌اند و شما به‌روزرسانی امنیتی را نصب کرده‌اید، می‌توانید منبع تأمین مالی خود را به نود خود، Wallet یا هر چیزی که دوباره استفاده می‌کنید، از طریق بخش مدیریت سرور تنظیم کنید. این ویکی بخشی درباره تغییر منابع تأمین مالی دارد اگر نمی‌دانید چه چیزی را پیکربندی کنید.



### تفاوت بین مدیر و سوپریوزر


رابط کاربری مدیریت LNbits به شما اجازه می‌دهد تنظیمات LNbits را از طریق رابط کاربری LNbits تغییر دهید. این ویژگی به‌طور پیش‌فرض غیرفعال است و اولین باری که متغیر محیطی `LNBITS_ADMIN_UI=true` را در فایل `.env` تنظیم می‌کنید، تنظیمات اولیه‌سازی شده و مورد استفاده قرار می‌گیرند. از آن به بعد، تنظیمات مربوطه از پایگاه داده به جای تنظیمات فایل .env استفاده می‌شوند.


### سوپر یوزر


با رابط کاربری مدیریت، ما کاربر فوق‌العاده‌ای معرفی کردیم که به سرور دسترسی دارد و می‌تواند تنظیماتی را تغییر دهد که ممکن است سرور را خراب کند یا از طریق رابط کاربری و API غیرقابل پاسخ کند، مانند تغییر منبع تأمین مالی. کاربر فوق‌العاده فقط در جدول تنظیمات پایگاه داده ذخیره می‌شود. پس از اینکه تنظیمات "به حالت پیش‌فرض بازنشانی" و مجدداً راه‌اندازی شدند، یک کاربر فوق‌العاده جدید ایجاد می‌شود. ما همچنین یک دکوراتور برای مسیرهای API اضافه کردیم تا وجود یک کاربر فوق‌العاده را بررسی کند. شناسه آن هرگز از طریق API و رابط کاربری ارسال نمی‌شود و فقط یک مقدار بولی (بله/خیر) دریافت می‌کند که آیا شما کاربر فوق‌العاده هستید یا خیر.


فقط کاربر ارشد مجاز است ساتوشی‌ها را از طریق بخش "افزایش موجودی" به کیف‌پول‌های مختلف منتقل کند.


شما همچنین می‌توانید کاربر ارشد را از طریق وب‌هوک به سرویس دیگری ارسال کنید وقتی که ایجاد می‌شود. اطلاعات بیشتر در اینجا https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`


در بخش فرانت‌اند، شما همچنین امکان تغییر تصویر فروشگاه که در صفحه "ایجاد Wallet" نمایش داده می‌شود را با باز کردن بخش مدیریت سرور و انتخاب تم -> لوگوی سفارشی خواهید یافت.


### کاربران مدیر


متغیر محیطی: `LNBITS_ADMIN_USERS`، لیستی از شناسه‌های کاربری که با کاما جدا شده‌اند. کاربران ادمین می‌توانند تنظیمات را در رابط کاربری ادمین تغییر دهند - به جز تنظیمات منبع تأمین مالی، زیرا این کار نیاز به راه‌اندازی مجدد سرور دارد و ممکن است سرور را غیرقابل دسترس کند. همچنین آنها به تمام افزونه‌هایی که در `LNBITS_ADMIN_EXTENSIONS` به آنها اختصاص داده شده است دسترسی دارند.


### کاربران مجاز


متغیر محیطی: `LNBITS_ALLOWED_USERS`، لیستی از شناسه‌های کاربری که با کاما جدا شده‌اند. با تعریف این کاربران، LNbits دیگر برای عموم قابل استفاده نخواهد بود. تنها کاربران تعریف‌شده و مدیران می‌توانند به رابط کاربری LNbits دسترسی داشته باشند.




#### به‌روزرسانی LNbits

به‌روزرسانی عادی نمونه محلی LNbits شما به سادگی با کپی و پیست کردن دستورات CLI زیر انجام می‌شود:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


اگر از Raspiblitz یا MyNode استفاده می‌کنید، ممکن است به یک

```
sudo systemctl restart lnbits
```

در نهایت، زیرا LNbits را به عنوان یک سرویس اجرا می‌کند.


در Umbrel/Citadel دستورات به صورت زیر خواهند بود

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### مهاجرت از SQLite به PostgreSQL


اگر قبلاً LNbits را نصب کرده‌اید و بر روی یک پایگاه داده SQLite اجرا می‌کنید، به شدت توصیه می‌کنیم که اگر قصد دارید LNbits را در مقیاس بزرگ اجرا کنید، به postgres مهاجرت کنید.


یک اسکریپت گنجانده شده است که می‌تواند مهاجرت را به‌راحتی انجام دهد. شما باید Postgres را از قبل نصب کرده باشید و باید برای کاربر یک رمز عبور وجود داشته باشد (راهنمای نصب Postgres را در بالا ببینید). علاوه بر این، نمونه LNbits شما باید یک بار بر روی Postgres اجرا شود تا پایگاه داده Schema را قبل از اینکه مهاجرت کار کند، پیاده‌سازی کند:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

امیدوارم اکنون همه چیز کار کند و منتقل شود... دوباره LNbits را راه‌اندازی کنید و بررسی کنید که آیا همه چیز به درستی کار می‌کند.



#### پشتیبان‌گیری و بازیابی پایگاه داده


لطفاً به [این راهنمای بسیار دقیق درباره فرآیند پشتیبان‌گیری و بازیابی](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore) مراجعه کنید.



#### تأمین مالی LNbits Wallet من از نودم کار نمی‌کند


اگر می‌خواهید Sats را از همان نودی که منبع تأمین مالی LNbits شماست ارسال کنید، باید فایل LND.conf را ویرایش کنید.


پارامترهایی که باید گنجانده شوند عبارتند از: `allow-circular-route=1`


لطفاً این کار را در بخش گزینه‌های برنامه فایل LND.conf خود انجام دهید. در غیر این صورت، در برخی از نودهای باندل ممکن است شروع LND با شکست مواجه شود.


توجه: توصیه می‌شود به جای آن از افزونه جدید adminUI با گزینه "TopUp" برای افزودن وجه به حساب LNbits استفاده کنید.


#### خطای ۴۲۶

خطا دریافت شد: "lnurl باید از طریق دامنه https عمومی قابل دسترسی یا تور ارائه شود. 426 ارتقاء لازم است"


این خطا معمولاً به این دلیل است که LNbits شما که پشت یک تونل ngnix قرار دارد، LNURL Address را به درستی ارسال نمی‌کند. LNbits خود را متوقف کرده و فایل .env را ویرایش کنید و این خط را اضافه کنید:

`FORWARDED_ALLOW_IPS=*`


همچنین اگر از تنظیمات ngnix استفاده می‌کنید، مطمئن شوید که این هدرها در پیکربندی ngnix وجود دارند:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### خطای شبکه

هنگام اسکن یک QR با خطای "https error"، "network error" یا خطاهای دیگر مواجه شدم.


خبر بد، این یک خطای مسیریابی است که ممکن است دلایل زیادی داشته باشد. ابتدا با استفاده از [Lightning Decoder](https://lightningdecoder.com/) کد LNURL مربوط به QR را بررسی کنید تا ببینید آیا چیز عجیبی در آن وجود دارد یا خیر. بیایید چند مورد از محتمل‌ترین مشکلات و راه‌حل‌های آن‌ها را امتحان کنیم.


LNbits فقط از طریق Tor اجرا می‌شود و نمی‌توانید آن را روی دامنه عمومی مانند lnbits.yourdomain.com باز کنید.



- با توجه به اینکه می‌خواهید تنظیمات شما به این شکل باقی بماند، LNbits Wallet خود را با استفاده از URI .onion باز کنید و دوباره آن را ایجاد کنید. به این ترتیب، QR به گونه‌ای تولید می‌شود که از طریق این URI .onion قابل دسترسی باشد، بنابراین فقط از طریق تور. QR را از یک URI .local generate نکنید، زیرا از طریق اینترنت قابل دسترسی نخواهد بود - فقط از داخل شبکه خانگی شما.
- برنامه LN Wallet خود را که برای اسکن آن QR استفاده کردید، باز کنید و این بار با استفاده از تور (به تنظیمات برنامه Wallet مراجعه کنید). اگر برنامه تور ارائه نمی‌دهد، می‌توانید به جای آن از Orbot (اندروید) استفاده کنید. برای دستورالعمل‌های دقیق در مورد چگونگی باز کردن LNbits خود برای clearnet/https به بخش نصب مراجعه کنید.



#### جلوگیری از ایجاد کیف پول توسط دیگران در LNbits من


وقتی LNbits خود را در clearnet اجرا می‌کنید، اساساً هر کسی می‌تواند generate را روی آن Wallet کند. از آنجا که وجوه نود شما به این کیف‌پول‌ها متصل است، ممکن است بخواهید از این کار جلوگیری کنید. دو راه برای انجام این کار وجود دارد:


پیکربندی کاربران و افزونه‌های مجاز در فایل `.env` ([نمونه env را اینجا ببینید](https://github.com/lnbits/lnbits/blob/main/.env.example)). این تنها در صورتی کار می‌کند که از تنظیم `adminUI=FALSE` در .env استفاده کنید، در غیر این صورت باید این کار را در بخش مدیریت سرور -> کاربران -> کاربران مجاز انجام دهید. سایر افراد پس از آن مجاز نخواهند بود.




#### سفارشی‌سازی بازه زمانی انقضای Invoice


اکنون می‌توانید فاکتورهای generate را با تاریخ انقضای سفارشی ایجاد کنید. تا کنون با بک‌اندهای زیر سازگار است: LndRestWallet، LndWallet، CoreLightningWallet، EclairWallet، LnbitsWallet، SparkWallet!


می‌توانید `LIGHTNING_INVOICE_EXPIRY` را در فایل .env خود تنظیم کنید یا از AdminUI برای تغییر مقدار پیش‌فرض برای همه فاکتورها استفاده کنید. همچنین یک فیلد جدید در نقطه پایانی /api/v1/payments وجود دارد که می‌توانید انقضا را در داده‌های JSON تنظیم کنید.




## Wallet-URL حذف شد


### Wallet روی سرور دمو legend.lnbits


همیشه یک نسخه از Wallet-URL، Export2phone-QR یا LNDhub خود را برای کیف پول‌های شخصی‌تان در مکانی امن ذخیره کنید. LNbits نمی‌تواند به شما در بازیابی آنها در صورت گم شدن کمک کند.


### Wallet بر روی منبع/گره تأمین مالی خودتان

همیشه یک نسخه از Wallet-URL، Export2phone-QR یا LNDhub کیف پول‌های خود را در مکانی امن ذخیره کنید. شما می‌توانید تمام کاربران LNbits و Wallet-IDها را در افزونه مدیریت کاربر LNbits یا در پایگاه داده sqlite خود پیدا کنید. برای ویرایش یا خواندن پایگاه داده LNbits، به پوشه LNbits /data بروید و به دنبال فایلی به نام sqlite.db بگردید. می‌توانید آن را با اکسل یا با یک ویرایشگر SQL اختصاصی مانند [SQLite browser](https://sqlitebrowser.org/) باز و ویرایش کنید.


همچنین می‌توانید کیف پول‌ها را از طریق CLI تخلیه کرده و هر Wallet را در پایگاه داده خود مشاهده کنید.


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


خروجی چیزی شبیه به این خواهد بود


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

و می‌خواهید این مقادیر را به یک URL مانند این قرار دهید


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


که در آن شما f8a43fc363ea428db5c53b3559935f1f را با مقداری که قبل از نام می‌آید جایگزین می‌کنید (در مثال ما f8a43fc363ea428db5c53b3559935f1f) و 1280ff5910a9c485a782a2376f338b6c کاربر شما است و باید به مقداری که بعد از نام نشان داده می‌شود تبدیل شود. برای خروج از sqlite3 وارد کنید


```
.quit
```

#### LNURL برای یک lightning-Address برعکس


این [رمزگذار](https://lnurl-codec.netlify.app/) از fiatjaf یا [این یکی](https://lightningdecoder.com/) را امتحان کنید. برای پرداخت یا بررسی یک LNURLp می‌توانید از [LNurlpay](https://wwww.lnurlpay.com/) نیز استفاده کنید. باید HTTPS باشد نه HTTP.



#### پیکربندی یک نظر که افراد هنگام پرداخت به QR LNURLp من مشاهده می‌کنند.

هنگامی که یک LNURL-p ایجاد می‌کنید، به طور پیش‌فرض کادر نظر پر نشده است. این بدان معناست که نظرات نمی‌توانند به پرداخت‌ها پیوست شوند.


برای فعال‌سازی نظرات، طول کاراکترهای جعبه را از 1 تا 250 اضافه کنید. هنگامی که عددی را در آنجا قرار دهید، جعبه نظر در فرآیند پرداخت نمایش داده خواهد شد. همچنین می‌توانید یک LNURL-p از قبل ایجاد شده را ویرایش کرده و آن عدد را اضافه کنید.


![lnbits comments](assets/lnbits-comments.webp)


#### واریز BTC زنجیره‌ای به LNbits

دو راه برای Exchange Sats از BTC زنجیره‌ای به LN BTC (به ترتیب به LNbits) وجود دارد.


##### از طریق یک سرویس مبادله خارجی.


کاربران دیگری که به LNb شما دسترسی ندارند می‌توانند از یک سرویس مبادله مانند [Boltz](https://boltz.Exchange/)، [FixedFloat](https://fixedfloat.com/)، [DiamondHands](https://swap.diamondhands.technology/) یا [ZigZag](https://zigzag.io/) استفاده کنند. این مفید است اگر شما فقط فاکتورهای LNURL/LN را از نمونه LNbits خود ارائه دهید، اما پرداخت‌کننده فقط Sats زنجیره‌ای دارد، بنابراین ابتدا باید آن Sats را در سمت خود مبادله کنند. روش ساده است: کاربر بیت‌کوین زنجیره‌ای را به سرویس مبادله ارسال می‌کند و LNURL / LN Invoice از LNbits را به عنوان مقصد مبادله ارائه می‌دهد.


##### استفاده از افزونه Onchain و Boltz LNbits.


به خاطر داشته باشید که این یک Wallet جداگانه است، نه LN btc که توسط LNbits به عنوان "Wallet شما" بر اساس منبع تأمین مالی LN شما نشان داده می‌شود. این Wallet زنجیره‌ای می‌تواند برای تبدیل LN btc به (مثلاً کیف پول سخت‌افزاری شما) با استفاده از افزونه LNbits Boltz یا Deezy نیز استفاده شود. اگر یک فروشگاه آنلاین دارید که به LNbits شما برای پرداخت‌های LN متصل است، بسیار مفید است که به طور منظم تمام Sats را از LN به زنجیره منتقل کنید. این کار فضای بیشتری در کانال‌های LN شما ایجاد می‌کند تا بتوانید Sats جدید و تازه دریافت کنید.


رویه برای کسانی که Bitcoin Hardware Wallet ندارند:



- از Electrum یا Sparrow wallet برای ایجاد یک Wallet جدید در زنجیره استفاده کنید و نسخه پشتیبان seed را در مکانی امن ذخیره کنید.
- به اطلاعات Wallet بروید و xpub را کپی کنید.
- به LNbits - افزونه Onchain بروید و یک Watch-only wallet جدید با آن xpub ایجاد کنید.
- به افزونه LNbits - Tipjar بروید و یک Tipjar جدید ایجاد کنید. همچنین گزینه onchain را در کنار LN Wallet انتخاب کنید.
- اختیاری - به LNbits - افزونه SatsPay بروید و یک شارژ جدید برای بیت‌کوین زنجیره‌ای ایجاد کنید. می‌توانید بین زنجیره‌ای و LN یا هر دو انتخاب کنید. سپس یک Invoice ایجاد می‌کند که می‌توان آن را به اشتراک گذاشت.
- اختیاری - اگر از LNbits خود که به صفحه Wordpress + Woocommerce متصل است استفاده کنید، پس از ایجاد/اتصال یک Watch-only wallet به فروشگاه بیت‌کوین LN خود Wallet، مشتری هر دو گزینه پرداخت را در همان صفحه خواهد داشت.


هنگامی که پرداختی را در LNbits دریافت می‌کنید، گزارش تراکنش تنها نوع خلاصه‌شده‌ای از تراکنش را نمایش خواهد داد.


![lnbits payment details](assets/lnbits-payment-details.webp)


در نمای کلی تراکنش خود، یک فلش کوچک Green برای دریافت و یک فلش قرمز برای وجوهی که ارسال شده‌اند، خواهید یافت.


اگر روی آن فلش‌ها کلیک کنید، یک پنجره جزئیات پیام‌های پیوست شده و همچنین نام فرستنده را در صورت وجود نشان می‌دهد.


برای پیکربندی یک نام که در پرداخت‌ها ظاهر شود، در LNbits در حال حاضر امکان‌پذیر نیست - اما برای دریافت. این تنها در صورتی ممکن است که LN Wallet فرستنده از [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) پشتیبانی کند مانند [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).


سپس یک نام مستعار/تخلص را در بخش جزئیات تراکنش‌های LNbits خود مشاهده خواهید کرد (روی فلش‌ها کلیک کنید). توجه داشته باشید که می‌توانید هر نامی را در آنجا وارد کنید و ممکن است به نام واقعی فرستنده مرتبط نباشد اگر چنین چیزی دریافت کنید.


![lnbits namedesc](assets/lnbits-namedesc.webp)


برای وارد کردن حساب LNbits خود در برنامه Wallet، حساب LNbits خود را با حساب / Wallet که می‌خواهید استفاده کنید باز کنید، به "مدیریت افزونه‌ها" بروید و افزونه LNDHUB را فعال کنید. افزونه LNDHUB را باز کنید، Wallet مورد نظر خود را انتخاب کنید و بسته به سطح امنیتی که برای آن Wallet می‌خواهید، یا QR "admin" یا "Invoice only" را اسکن کنید.


شما می‌توانید از [Zeus](https://zeusln.app/) یا [Bluewallet](https://bluewallet.io/) به عنوان اپلیکیشن‌های Wallet برای یک حساب lndhub استفاده کنید که در این میان BW از بیش از یک Wallet پشتیبانی می‌کند.


هنگام انجام این کار، توصیه می‌کنیم که URI شبکه LN را به URI نود خودتان تنظیم کنید. اگر نمونه LNbits شما فقط از طریق تور قابل دسترسی است، باید از آن برنامه‌ها با تور فعال استفاده کنید. همچنین در این حالت، نیاز دارید که صفحه LNbits را از طریق تور .onion Address خود باز کنید.


اگر با خطای "unsupported Hash type" هنگام استفاده از ypub در افزونه On-Chain مواجه شدید، بررسی کنید که آیا نمونه LNbits شما از پایتون 3.10 استفاده می‌کند یا خیر، ممکن است تحت تأثیر [این مشکل](https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python) قرار گرفته باشد. فایل openssl.cnf را همانطور که در پاسخ stackoverflow توضیح داده شده ویرایش کنید و LNbits خود را مجدداً راه‌اندازی کنید.



## ابزارسازی و ساخت با LNbits


LNbits دارای انواع [APIهای باز](https://legend.lnbits.com/docs) و ابزارهایی است که می‌توانند برای برنامه‌ریزی و اتصال به بسیاری از دستگاه‌های مختلف برای تعداد زیادی از موارد استفاده به کار روند.


وقتی در ساختن تازه‌کار هستید، با این [ارائه‌های MakerBits](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) از بن آرک درباره ساخت ابزارهایی بر اساس LNbits شروع کنید.


### مهم:


- LNbits بر اساس پروتکل LNURL کار می‌کند که درخواست‌ها به دو صورت معتبر هستند: یا به صورت لینک https:// در شبکه clearnet (بدون مجوز به گواهی‌های خودامضا) یا به صورت لینک http:// v2/v3 در شبکه onion. برای ارائه خدمات LNbits مانند کدهای QR LNURLp/w یا کارت‌های NFC که می‌توانند در محیط‌های عمومی استفاده شوند، نیاز دارید که LNbits را به شبکه clearnet (https) باز کنید.
- فقط از کابل‌های DATA برای تأمین برق esp32 خود استفاده کنید. همه کابل‌ها علاوه بر تأمین برق، از داده نیز پشتیبانی نمی‌کنند. اگر کابلی که همراه با esp آمده است فقط برای برق باشد، شما اولین نفر نخواهید بود.
- مطمئن شوید که از یک هاب USB با دستگاه‌های دیگر متصل استفاده نکنید. این می‌تواند به اثرات عجیبی منجر شود که رفع اشکال آن‌ها Hard است (مثلاً شروع یا توقف نکردن).
- برای اجرای پروژه‌های ESP با MacOS به یک درایور UART Bridge نیاز خواهید داشت. اگر با درایور در سیستم‌های Mac یا Linux مشکل دارید، می‌توانید آن‌ها را اینجا پیدا کنید یا اگر یک نمایشگر TTGO درگیر است، این یکی را امتحان کنید. اگر از ویندوز استفاده می‌کنید و در اتصال مشکل دارید، مطمئن شوید که نسخه قدیمی 11.1.0 را دانلود کنید زیرا نسخه جدیدتر کار نمی‌کند! همچنین می‌توانید یک ترمینال سریال را اینجا پیدا کنید تا اتصال خود را بررسی کنید - تنظیم شده به نرخ باود 115200.
- اگرچه استفاده از Platform.io بسیار راحت‌تر است (به عنوان مثال، وابستگی‌ها به‌طور خودکار نصب می‌شوند)، ما توصیه می‌کنیم که برای همه‌ی کسانی که تازه شروع به ساختن کرده‌اند، از Arduino استفاده کنند.
- TT-Go Display S3: رنگ برچسب فیلم محافظ صفحه نمایش به شما می‌گوید که دقیقاً از کدام کنترلر (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) برای ساخت آن استفاده شده است. آن را نگه دارید تا در صورتی که خودتان برنامه‌نویسی می‌کنید و صفحه نمایش به درستی گرافیک‌ها را نمایش نمی‌دهد، مانند رنگ‌های اشتباه، تصاویر معکوس، یا پیکسل‌های پراکنده در لبه‌ها، بتوانید اشکال‌زدایی کنید. اگر نیاز به انجام این کار داشتید، یک راهنمای فوق‌العاده برای تنظیم نمایشگرهای مختلف وجود دارد.
- همیشه از lnurl239xx با حروف کوچک به جای LNURLl239xx استفاده کنید.
- افزودن lightning:lnurl1234xyz یک کد QR ایجاد می‌کند که درخواست می‌کند Wallet کاربران برای این Invoice در اسکن باز شود (آخرین برنامه نصب شده لایتنینگ در iOS، تنظیم در Android)
- اگر در حال فلش کردن یک esp32 از طریق وب هستید، این کار فقط با این مرورگرها کار خواهد کرد (TL:DR Chrome, Edge & Opera).
- لطفاً به این مرجع PIN-OUT برای esp توجه کنید.
- وقتی از FOSSoftware یا FOSGuides استفاده می‌کنید، لطفاً همیشه به نویسنده لینک دهید. همه دوست دارند رشد اثر خود را ببینند و این کار همچنین زنجیره‌ای از ساخت و ساز را آغاز می‌کند که تماشای آن واقعاً شگفت‌انگیز است:)


اگر برای پروژه‌ای به کمک نیاز دارید، به [گروه تلگرام Makerbits](https://t.me/makerbits) بیایید - ما هوای شما را داریم!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


در اینجا چند دسته پروژه وجود دارد که می‌توانید با LNbits بسازید:



- [دستگاه امضای Nostr](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [دستگاه آرکید](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [چراغ Nostr Zap](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [دستگاه فروش خودکار](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [شبکه‌سازی لورا و مش](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [HELPERS & RESOURCES](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [نمونه‌های بیشتری از پروژه‌های "توسط LNbits پشتیبانی می‌شود" اینجا](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [موارد استفاده از LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)