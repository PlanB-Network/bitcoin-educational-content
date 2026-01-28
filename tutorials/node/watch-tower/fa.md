---
name: Lightning Watchtower
description: درک و استفاده از Watchtower در نود لایتنینگ شما
---
![cover](assets/cover.webp)



## برج‌های دیده‌بانی چگونه کار می‌کنند؟



بخشی اساسی از اکوسیستم Lightning Network، _برج‌های مراقبت_ سطح اضافی از حفاظت را برای کانال‌های لایتنینگ کاربران فراهم می‌کنند. نقش اصلی آن‌ها نظارت بر وضعیت کانال و مداخله در صورتی است که یک طرف کانال سعی کند طرف دیگر را فریب دهد.



چگونه یک Watchtower می‌تواند تعیین کند که آیا یک کانال به خطر افتاده است؟ این سیستم از مشتری (یکی از طرفین کانال) اطلاعات لازم برای شناسایی صحیح و رسیدگی به هرگونه نقض را دریافت می‌کند. این اطلاعات شامل جزئیات آخرین تراکنش، وضعیت فعلی کانال و Elements مورد نیاز برای ایجاد تراکنش‌های جریمه است. قبل از ارسال این داده‌ها به Watchtower، مشتری می‌تواند آن‌ها را رمزگذاری کند تا محرمانگی حفظ شود. بنابراین، حتی اگر Watchtower داده‌ها را دریافت کند، قادر به رمزگشایی آن نخواهد بود تا زمانی که واقعاً نقضی رخ داده باشد. این مکانیزم رمزگذاری از حریم خصوصی مشتری محافظت می‌کند و مانع از دسترسی غیرمجاز Watchtower به اطلاعات حساس می‌شود.



در این آموزش، به ۳ روش استفاده از **Watchtower** خواهیم پرداخت:




- ابتدا، روش کلاسیک خام از طریق LND،
- سپس رویکرد دیگری با چشم Satoshi،
- و در نهایت، پیکربندی ساده‌شده‌ی یک Watchtower بر روی نود Lightning شما که با Umbrel میزبانی می‌شود.



## 1 - پیکربندی یک Watchtower یا یک کلاینت از طریق LND



*این آموزش از [مستندات رسمی LND](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md) گرفته شده است. ممکن است برخی تغییرات در نسخه اصلی اعمال شده باشد.



از نسخه v0.7.0، `LND` از اجرای یک Watchtower نوع‌دوستانه خصوصی به عنوان یک زیرسیستم کاملاً یکپارچه از `LND` پشتیبانی می‌کند. برج‌های مراقبت یک خط دفاعی دوم در برابر سناریوهای نقض مخرب یا تصادفی ارائه می‌دهند، زمانی که گره مشتری آفلاین است یا قادر به پاسخگویی در زمان نقض نیست، و درجه امنیت بیشتری برای وجوه کانال فراهم می‌کنند.



برخلاف _برج مراقبت پاداش_ که در ازای خدمات خود سهمی از وجوه کانال را می‌طلبد، _برج مراقبت نوع‌دوست_ تمام وجوه قربانی را (به‌جز هزینه‌های On-Chain) بدون دریافت کمیسیون بازمی‌گرداند. برج‌های مراقبت پاداش در نسخه‌های بعدی فعال خواهند شد؛ آن‌ها هنوز در مرحله آزمایش و بهبود قرار دارند.



علاوه بر این، `LND` اکنون می‌تواند به عنوان یک _کلاینت دیده‌بانی_ پیکربندی شود و تراکنش‌های رمزگذاری‌شده‌ی اصلاح نقض (به‌اصطلاح "تراکنش‌های عدالت") را از دیگر دیده‌بان‌های نوع‌دوست ذخیره کند. Watchtower بلوک‌های رمزگذاری‌شده با اندازه ثابت را ذخیره می‌کند و تنها پس از اینکه طرف متخلف یک حالت لغو شده‌ی Commitment را پخش کرده باشد، می‌تواند تراکنش عدالت را رمزگشایی و منتشر کند. ارتباطات مشتری ↔ Watchtower با استفاده از جفت کلیدهای موقت رمزگذاری و احراز هویت می‌شوند، که توانایی Watchtower را برای ردیابی مشتریانش از طریق اعتبارنامه‌های بلندمدت محدود می‌کند.



توجه داشته باشید که ما تصمیم گرفته‌ایم در این نسخه مجموعه محدودی از ویژگی‌ها را که امنیت قابل توجهی برای کاربران `LND` فراهم می‌کنند، ارائه دهیم. بسیاری از ویژگی‌های مرتبط با Watchtower یا نزدیک به تکمیل هستند یا به خوبی پیشرفت کرده‌اند؛ ما به ارائه آن‌ها ادامه خواهیم داد، همان‌طور که آن‌ها را آزمایش می‌کنیم و به محض اینکه ایمن تشخیص داده شوند.



توجه: در حال حاضر، برج‌های دیده‌بانی فقط خروجی‌های `to_local` و `to_remote` تعهدات لغو شده را ذخیره می‌کنند؛ ذخیره خروجی HTLC در نسخه آینده پیاده‌سازی خواهد شد، زیرا پروتکل می‌تواند برای شامل کردن داده‌های امضای اضافی در بلوک‌های رمزگذاری شده گسترش یابد._



### پیکربندی یک Watchtower



برای راه‌اندازی Watchtower، کاربران خط فرمان نیاز دارند تا زیرسرور اختیاری `watchtowerrpc` را کامپایل کنند که امکان تعامل با Watchtower از طریق gRPC یا `lncli` را فراهم می‌کند. باینری‌های منتشر شده به طور پیش‌فرض شامل زیرسرور `watchtowerrpc` هستند.



حداقل پیکربندی برای فعال‌سازی Watchtower این است: `Watchtower.active=1`.



می‌توانید اطلاعات پیکربندی Watchtower خود را با `lncli tower info` بازیابی کنید:



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



مجموعه کامل گزینه‌های پیکربندی Watchtower از طریق `LND -h` در دسترس است:



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### رابط‌های شنیداری



به طور پیش‌فرض، Watchtower به `:9911` گوش می‌دهد، که معادل پورت `9911` بر روی تمامی رابط‌های موجود است. کاربران می‌توانند رابط‌های شنود خود را از طریق گزینه `--Watchtower.listen=` تعریف کنند. شما می‌توانید پیکربندی خود را در فیلد `"listeners"` از `lncli tower info` بررسی کنید. اگر در اتصال به Watchtower مشکل دارید، مطمئن شوید که `<port>` باز است یا پروکسی شما به درستی به یک Interface فعال پیکربندی شده است.



#### آدرس‌های IP خارجی



کاربران همچنین می‌توانند IP خارجی Watchtower را با `Watchtower.externalip=` مشخص کنند، که URI کامل Watchtower (pubkey@host:port) را از طریق RPC یا `lncli tower info` نمایش می‌دهد:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URIها را می‌توان با استفاده از فرمان زیر به مشتریان اعلام کرد تا متصل شوند و استفاده کنند:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



اگر مشتریان Watchtower نیاز به دسترسی از راه دور دارند، اطمینان حاصل کنید که:




- پورت 9911 (یا پورتی که از طریق `Watchtower.listen` تعریف شده است) را باز کنید.
- از یک پروکسی برای هدایت ترافیک از یک پورت باز به Watchtower به Address که در حال گوش دادن است، استفاده کنید.



#### سرویس‌های مخفی تور



برج‌های مراقبت از خدمات مخفی Tor پشتیبانی می‌کنند و می‌توانند به‌طور خودکار generate را در هنگام راه‌اندازی با گزینه‌های زیر فعال کنند:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



سپس .onion Address در فیلد `"uris"` در طول یک پرس و جو `lncli tower info` ظاهر می‌شود:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



توجه: کلید عمومی Watchtower با کلید عمومی گره `LND` متفاوت است. در حال حاضر، به عنوان "لیست سفید Soft" عمل می‌کند، زیرا مشتریان برای استفاده از آن به عنوان پشتیبان، نیاز به دانستن کلید عمومی Watchtower دارند، تا زمانی که مکانیزم‌های پیشرفته‌تر لیست سفید ارائه شوند. ما توصیه می‌کنیم این کلید عمومی را به‌طور علنی فاش نکنید، مگر اینکه آماده باشید Watchtower خود را در معرض کل اینترنت قرار دهید._



#### دایرکتوری پایگاه داده Watchtower



می‌توان پایگاه داده Watchtower را با استفاده از گزینه `Watchtower.towerdir=` جابجا کرد. توجه داشته باشید که یک پسوند `/Bitcoin/Mainnet/Watchtower.db` به مسیر انتخابی اضافه خواهد شد تا پایگاه‌های داده را با رشته جدا کند. بنابراین، تنظیم `Watchtower.towerdir=/path/to/towerdir` یک پایگاه داده در مسیر `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db` ایجاد خواهد کرد.



در لینوکس، به عنوان مثال، پایگاه داده پیش‌فرض Watchtower در اینجا قرار دارد:


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### پیکربندی یک مشتری Watchtower



برای پیکربندی یک مشتری Watchtower، به دو مورد نیاز دارید:





- مشتری Watchtower را با گزینه `--wtclient.active` فعال کنید.



```shell
$  lnd --wtclient.active
```





- URI یک Watchtower فعال.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



می‌توانید چندین برج دیده‌بانی را به این روش پیکربندی کنید.



#### نرخ‌های هزینه برای معاملات قانونی



کاربران می‌توانند به‌صورت اختیاری نرخ کارمزد برای تراکنش‌های عدالت را از طریق گزینه `wtclient.sweep-fee-rate` تنظیم کنند، که مقادیر را به صورت ساتوشی/بایت می‌پذیرد. مقدار پیش‌فرض ۱۰ ساتوشی/بایت است، اما می‌توان برای دستیابی به اولویت بالاتر در زمان اوج بار، به نرخ‌های بالاتر هدف‌گذاری کرد. تغییر `sweep-fee-rate` به تمام به‌روزرسانی‌های جدید پس از راه‌اندازی مجدد daemon اعمال می‌شود.



#### نظارت



با استفاده از دستور `lncli wtclient`، کاربران اکنون می‌توانند به‌طور مستقیم با کلاینت Watchtower تعامل داشته باشند تا اطلاعات مربوط به تمامی برج‌های مراقبت ثبت‌شده را به‌دست آورند یا تغییر دهند.



به عنوان مثال، با استفاده از `lncli wtclient tower`، می‌توانید تعداد جلسات مذاکره شده فعلی با Watchtower که در بالا اضافه شده است را پیدا کنید و تعیین کنید که آیا از آن برای پشتیبان‌گیری استفاده می‌شود یا خیر، به لطف فیلد `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



برای به‌دست‌آوردن اطلاعات در مورد جلسات Watchtower، از گزینه `--include_sessions` استفاده کنید.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



تمام گزینه‌های پیکربندی مشتری Watchtower از طریق `lncli wtclient -h` در دسترس هستند:



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## ۲ - نصب چشم Satoshi خودتان



*این آموزش تا حدی از مقاله‌ای در [وبلاگ Summer of Bitcoin](https://blog.summerofbitcoin.org/) استخراج شده است. تغییراتی در نسخه اصلی اعمال شده است*



چشم Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) یک Watchtower Lightning غیرسپرده‌ای است که با [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org) مطابقت دارد. این شامل دو جزء اصلی است:





- teos**: شامل یک خط فرمان Interface (CLI) و ویژگی‌های سرور ضروری Watchtower است. دو فایل باینری - **teosd** و **teos-CLI** - زمانی که این _crate_ کامپایل می‌شود تولید می‌شوند.





- teos-common**: شامل عملکرد مشترک سمت سرور و سمت مشتری (مفید برای ایجاد یک مشتری).



برای اجرای صحیح Watchtower، باید قبل از راه‌اندازی Watchtower با دستور **teosd**، **bitcoind** را اجرا کنید. قبل از اجرای این دو دستور، باید فایل **Bitcoin.conf** خود را پیکربندی کنید. در اینجا نحوه انجام آن آمده است:





- نصب Bitcoin core از منبع یا دانلود آن. پس از دانلود، فایل **Bitcoin.conf** را در دایرکتوری کاربری Bitcoin core قرار دهید. برای اطلاعات بیشتر در مورد محل قرار دادن فایل، به این لینک مراجعه کنید، زیرا این موضوع به سیستم عامل مورد استفاده بستگی دارد.





- پس از شناسایی مکان، گزینه‌های زیر را اضافه کنید:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- سرور**: برای درخواست‌های RPC





- rpcuser** و **rpcpassword**: احراز هویت مشتریان RPC به سرور





- regtest**: الزامی نیست، اما اگر قصد توسعه دارید مفید است.



مقادیر **rpcuser** و **rpcpassword** باید توسط شما انتخاب شوند. آنها باید بدون علامت نقل قول نوشته شوند. برای مثال:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



اکنون، اگر **bitcoind** را اجرا کنید، نود باید شروع به کار کند.





- برای قسمت Watchtower، ابتدا باید **teos** را از منبع نصب کنید. دستورالعمل‌های داده شده در این لینک را دنبال کنید.





- پس از اینکه **teos** را با موفقیت روی سیستم خود نصب کردید و تست‌ها را اجرا کردید، می‌توانید به مرحله نهایی بروید: تنظیم فایل **teos.toml** در دایرکتوری کاربر teos. فایل باید در پوشه‌ای به نام **.teos** (به نقطه توجه کنید) زیر دایرکتوری خانگی شما قرار گیرد. برای مثال، **/home//.teos** در لینوکس. پس از یافتن مکان، یک فایل **teos.toml** ایجاد کنید و این گزینه‌ها را مطابق با تغییرات انجام شده در **bitcoind** تنظیم کنید:



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



توجه داشته باشید که در اینجا، نام کاربری و رمز عبور باید **در داخل علامت نقل قول** نوشته شوند. با استفاده از مثال قبلی:



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



پس از انجام این کار، باید آماده راه‌اندازی Watchtower باشید. از آنجا که ما روی **regtest** اجرا می‌کنیم، احتمالاً هیچ بلوکی در شبکه آزمایشی Bitcoin ما استخراج نشده است وقتی که Watchtower برای اولین بار متصل شد (اگر استخراج شده باشد، مشکلی وجود دارد). Watchtower یک حافظه داخلی از 100 بلوک آخر **bitcoind** می‌سازد؛ بنابراین، در اولین راه‌اندازی، ممکن است با خطای زیر مواجه شوید:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



از آنجایی که ما از **regtest** استفاده می‌کنیم، می‌توانیم با صدور فرمان RPC، بلوک‌های Miner را ایجاد کنیم، بدون اینکه نیاز به انتظار برای تأخیر متوسط 10 دقیقه‌ای که در شبکه‌های دیگر (مانند Mainnet یا Testnet) دیده می‌شود، داشته باشیم. برای جزئیات نحوه ایجاد بلوک‌های Miner به راهنمای **bitcoin-cli** مراجعه کنید.



![Image](assets/fr/01.webp)



همین است: شما با موفقیت Watchtower را اجرا کرده‌اید. تبریک می‌گویم. 🎉




## ۳ - پیکربندی Watchtower روی Umbrel



در Umbrel، اتصال به Watchtower برای محافظت از نود Lightning شما بسیار ساده است، زیرا همه چیز از طریق Interface گرافیکی انجام می‌شود. پس از اتصال از راه دور به نود خود، برنامه "**Lightning Node**" را باز کنید.



![Image](assets/fr/02.webp)



روی سه نقطه کوچک در بالای سمت راست Interface کلیک کنید، سپس "**Advanced Settings**" را انتخاب کنید.



![Image](assets/fr/03.webp)



در منوی "**Watchtower**"، دو گزینه در دسترس است:





- سرویس Watchtower**: این گزینه به شما اجازه می‌دهد تا یک Watchtower را راه‌اندازی کنید، یعنی سرویسی که کانال‌های نودهای دیگر را برای شناسایی هرگونه تلاش برای تقلب نظارت می‌کند. در صورت وقوع نقض، Watchtower شما یک تراکنش را بر روی Blockchain منتشر می‌کند و به کاربران امکان بازیابی وجوه قفل‌شده‌شان را می‌دهد. پس از فعال‌سازی، URI مربوط به Watchtower شما ظاهر می‌شود و می‌تواند به نودهای دیگر اعلام شود تا بتوانند آن را به کلاینت Watchtower خود اضافه کنند؛





- Watchtower Client**: این گزینه به شما اجازه می‌دهد تا به برج‌های مراقبت خارجی متصل شوید تا از کانال‌های خود محافظت کنید. پس از فعال‌سازی، می‌توانید خدمات Watchtower را اضافه کنید که نود شما اطلاعات لازم درباره کانال‌هایش را به آن‌ها منتقل خواهد کرد. سپس این برج‌های مراقبت وضعیت آن‌ها را نظارت کرده و در صورت تلاش برای تقلب مداخله خواهند کرد.



اولویت شما البته فعال‌سازی *Watchtower Client* برای محافظت از نود خودتان است، اما همچنین توصیه می‌کنم که *Watchtower Service* را فعال کنید تا در مقابل امنیت سایر کاربران نیز سهمی داشته باشید.



![Image](assets/fr/04.webp)



سپس روی دکمه Green "**ذخیره و راه‌اندازی مجدد نود**" کلیک کنید. LND شما راه‌اندازی مجدد خواهد شد.



در همان منو، اگر سرویس Watchtower خود را فعال کرده‌اید، URI آن را نیز خواهید یافت. همچنین می‌توانید URI یک Watchtower خارجی را برای محافظت از کانال‌های خود اضافه کنید. برای تأیید روی "**ADD**" کلیک کنید.



![Image](assets/fr/05.webp)



برج‌های مراقبت متعددی به صورت آنلاین در دسترس هستند. به عنوان مثال، [LN+ و Voltage یک Watchtower نوع‌دوستانه](https://lightningnetwork.plus/Watchtower) ارائه می‌دهند که می‌توانید به آن متصل شوید:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



گزینه دیگر این است که Exchange خود را با Watchtower URI خود با سایر بیت‌کوینرها به اشتراک بگذارید، به‌طوری‌که هر کدام از نود دیگری محافظت کند.



من همچنین توصیه می‌کنم که چندین برج دیده‌بانی راه‌اندازی کنید تا در صورت عدم دسترسی به یکی از آن‌ها، ریسک‌ها کاهش یابد.



در نهایت، می‌توانید پارامتر "**Watchtower Client Sweep Fee Rate**" را تنظیم کنید. این پارامتر حداکثر نرخ کارمزدی را که مایلید برای یک تراکنش جریمه پخش Watchtower بپردازید تا در یک بلاک گنجانده شود، تعریف می‌کند. اطمینان حاصل کنید که مقدار کافی بالا را تنظیم کرده‌اید که با مقادیر قفل شده در کانال‌های شما سازگار باشد.