---
name: RGB Lightning Node
description: چگونه می‌توانم یک نود لایتنینگ سازگار با RGB را با RLN راه‌اندازی کنم؟
---
![cover](assets/cover.webp)


در این آموزش گام‌به‌گام، یاد خواهید گرفت که چگونه یک نود Lightning RGB را در محیط Regtest راه‌اندازی کنید. خواهیم دید که چگونه توکن‌های RGB ایجاد کرده و آن‌ها را در کانال‌ها به گردش درآوریم.


## پروژه RLN


تیم RGB بیتفینکس از سال 2022 در حال کار برای غنی‌سازی اکوسیستم RGB با توسعه یک پشته فناوری کامل بوده است. به جای هدف‌گذاری برای یک محصول تجاری واحد، تلاش‌های آن‌ها بر روی ارائه آجرهای نرم‌افزار متن‌باز، مشارکت در مشخصات پروتکل RGB و ایجاد مراجع پیاده‌سازی متمرکز است.


در میان مشارکت‌های قابل توجه Bitfinex در اکوسیستم RGB، [کتابخانه *RGBlib*](https://github.com/RGB-Tools/RGB-lib) قرار دارد که به زبان Rust نوشته شده و از طریق بایندینگ‌ها در Kotlin و Python قابل دسترسی است. این کتابخانه با محصور کردن مکانیزم‌های پیچیده اعتبارسنجی و تعامل، توسعه برنامه‌های RGB را به‌طور قابل توجهی ساده می‌کند.


تیم Bitfinex همچنین یک RGB موبایل Wallet طراحی کرده است که "[*Iris Wallet*](https://iriswallet.com/)" نام دارد و در اندروید موجود است. این Wallet استفاده از یک سرور پروکسی RGB را برای مدیریت آسان تبادلات داده off-chain (*محموله‌ها*) برای *Client-side Validation* بر روی RGB یکپارچه می‌کند.


Bitfinex همچنین پروژه `RGB-lightning-node` (RLN) را توسعه داده است. این پروژه یک Rust daemon است که بر اساس Fork از `Rust-lightning` (LDK) ساخته شده و به گونه‌ای اصلاح شده که وجود دارایی‌های RGB در یک کانال را در نظر بگیرد. هنگامی که یک کانال باز می‌شود، می‌توان حضور توکن‌های RGB را مشخص کرد و هر بار که وضعیت کانال به‌روزرسانی می‌شود، یک State Transition ایجاد می‌شود که توزیع توکن‌ها در خروجی‌های Lightning را منعکس می‌کند. این امکان را فراهم می‌کند:




- کانال‌های لایتنینگ را در USDT باز کنید، برای مثال؛
- این توکن‌ها را از طریق شبکه مسیریابی کنید، به شرطی که مسیرهای مسیریابی نقدینگی کافی داشته باشند؛
- از منطق مجازات و قفل زمانی Lightning بدون تغییر بهره‌برداری کنید: به سادگی گذار Anchor به RGB را در یک خروجی اضافی از Commitment Transaction انجام دهید.


کد RLN هنوز در مرحله آلفا است: توصیه می‌کنیم از آن فقط در **regtest** یا روی **Testnet** استفاده کنید.


## یادآوری پروتکل RGB


RGB پروتکلی است که بر روی Bitcoin اجرا می‌شود و عملکرد و مدیریت دارایی دیجیتال Smart contract را شبیه‌سازی می‌کند، بدون اینکه Blockchain که بر اساس آن است را بارگذاری کند. برخلاف قراردادهای هوشمند معمولی On-Chain (مانند اتریوم، به عنوان مثال)، RGB به یک سیستم "*Client-side Validation*" متکی است: اکثر داده‌ها و تاریخچه‌های وضعیت به‌طور انحصاری توسط شرکت‌کنندگان درگیر مبادله و ذخیره می‌شوند، در حالی که Bitcoin Blockchain تنها تعهدات رمزنگاری کوچک را میزبانی می‌کند (از طریق مکانیزم‌هایی مانند *Tapret* یا *Opret*). در پروتکل RGB، Bitcoin Blockchain بنابراین تنها به عنوان یک سرور زمان‌سنجی و سیستم حفاظت Double-spending عمل می‌کند.


RGB Contract به‌صورت یک ماشین حالت تکاملی ساختار یافته است. این فرآیند با یک Genesis آغاز می‌شود که حالت اولیه را تعریف می‌کند (به‌عنوان مثال، Supply، تیکر یا دیگر متادیتا) بر اساس یک Schema که به‌صورت دقیق تایپ و کامپایل شده است. انتقالات حالت و در صورت لزوم، توسعه‌های حالت برای تغییر یا گسترش این حالت اعمال می‌شوند. هر عملیات، چه انتقال دارایی‌های قابل تعویض (RGB20) یا ایجاد دارایی‌های منحصر به فرد (RGB21)، شامل *مهر و موم‌های یک‌بار مصرف* است. این مهر و موم‌ها UTXOهای Bitcoin را به حالت‌های off-chain متصل می‌کنند و از دوبار خرج کردن جلوگیری می‌کنند، در حالی که محرمانگی و مقیاس‌پذیری را تضمین می‌کنند.


برای کسب اطلاعات بیشتر در مورد نحوه کار پروتکل RGB، توصیه می‌کنم این دوره آموزشی جامع را بگذرانید:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## نصب نود لایتنینگ سازگار با RGB


برای کامپایل و نصب باینری `RGB-lightning-node`، ابتدا با کلون کردن مخزن و زیرماژول‌های آن شروع می‌کنیم، سپس اجرا می‌کنیم:


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- گزینه `--recurse-submodules` همچنین زیر دستگاه‌های ضروری (از جمله نسخه اصلاح‌شده `Rust-lightning`) را نیز کلون می‌کند؛
- گزینه `--shallow-submodules` عمق کلون را محدود می‌کند تا سرعت دانلود افزایش یابد، در حالی که همچنان دسترسی به کامیت‌های ضروری را فراهم می‌کند.


از ریشه پروژه، فرمان زیر را برای کامپایل و نصب باینری اجرا کنید:


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` اطمینان حاصل می‌کند که نسخه وابستگی‌ها رعایت شود؛
- گزینه `--debug` اجباری نیست، اما می‌تواند به شما کمک کند تمرکز کنید (می‌توانید از `--release` استفاده کنید اگر ترجیح می‌دهید) ؛
- `--path .` به `cargo install` می‌گوید که از دایرکتوری فعلی نصب کند.


در پایان این دستور، یک فایل اجرایی `RGB-lightning-node` در مسیر `$CARGO_HOME/bin/` شما موجود خواهد بود. اطمینان حاصل کنید که این مسیر در `$PATH` شما قرار دارد تا بتوانید دستور را از هر دایرکتوری اجرا کنید.


## پیش‌نیازها


برای عملکرد، `RGB-lightning-node` daemon به حضور و پیکربندی نیاز دارد:




- یک گره `bitcoind`


هر نمونه RLN نیاز خواهد داشت تا با `bitcoind` ارتباط برقرار کند تا تراکنش‌های On-Chain خود را پخش و نظارت کند. احراز هویت (ورود/رمز عبور) و URL (میزبان/پورت) باید به daemon ارائه شود.




- یک **ایندکسر** (Electrum یا Esplora)


daemon باید بتواند تراکنش‌های On-Chain را فهرست کرده و بررسی کند، به‌ویژه برای یافتن UTXO که یک دارایی بر روی آن لنگر انداخته است. شما باید URL سرور Electrum یا Esplora خود را مشخص کنید.




- یک پروکسی **RGB**


سرور پروکسی یک مؤلفه (اختیاری، اما به شدت توصیه می‌شود) برای ساده‌سازی Exchange از RGB *محموله‌ها* بین همتایان Lightning است. بار دیگر، باید یک URL مشخص شود.


شناسه‌ها و URLها زمانی وارد می‌شوند که daemon از طریق API *باز شود*.


## راه‌اندازی Regtest


برای استفاده‌ی ساده، یک اسکریپت `regtest.sh` وجود دارد که به‌طور خودکار، از طریق Docker، مجموعه‌ای از سرویس‌ها را راه‌اندازی می‌کند: `bitcoind`، `electrs` (ایندکسر)، `RGB-proxy-server`.


![RLN](assets/fr/03.webp)


این به شما امکان می‌دهد یک محیط محلی، ایزوله و از پیش پیکربندی شده را راه‌اندازی کنید. این کار کانتینرها و دایرکتوری‌های داده را در هر بار راه‌اندازی مجدد ایجاد و نابود می‌کند. ما با شروع :


```bash
./regtest.sh start
```


این اسکریپت خواهد:




- یک دایرکتوری `docker/` ایجاد کنید تا ذخیره شود؛
- اجرای `bitcoind` در حالت regtest، به همراه ایندکسر `electrs` و `RGB-proxy-server` ;
- صبر کنید تا همه چیز آماده استفاده شود.


![RLN](assets/fr/04.webp)


سپس، چندین گره RLN را راه‌اندازی خواهیم کرد. در شل‌های جداگانه، به عنوان مثال اجرا کنید (برای راه‌اندازی 3 گره RLN) :


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- پارامتر `--network regtest` نشان‌دهنده استفاده از پیکربندی regtest است؛
- `--daemon-listening-port` نشان می‌دهد که نود لایتنینگ بر روی کدام پورت REST برای فراخوانی‌های API (JSON) گوش خواهد داد؛
- `--ldk-peer-listening-port` مشخص می‌کند که به کدام پورت Lightning P2P گوش دهد؛
- `dataldk0/`، `dataldk1/` مسیرهای دایرکتوری‌های ذخیره‌سازی هستند (هر گره اطلاعات خود را به‌طور جداگانه ذخیره می‌کند).


اکنون می‌توانید دستورات را بر روی گره‌های RLN خود از مرورگر اجرا کنید، به لطف API. به‌ویژه، اینجاست که می‌توانید دیمن‌ها را *باز کنید*. به سادگی یک مرورگر را بر روی همان کامپیوتری که گره‌های شما قرار دارند باز کنید و URL زیر را وارد کنید:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


برای یک نود برای باز کردن یک کانال، ابتدا باید بیت‌کوین‌ها را روی یک Address که با فرمان زیر تولید شده است، داشته باشد (برای نود شماره 1، به عنوان مثال):


```bash
curl -X POST http://localhost:3001/address
```


پاسخ به شما یک Address ارائه خواهد داد.


![RLN](assets/fr/06.webp)


در `bitcoind` Regtest، قصد داریم چند بیت‌کوین استخراج کنیم. اجرا کنید :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


ارسال وجوه به نود Address که در بالا ایجاد شده است:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


سپس یک بلاک را استخراج کنید تا تراکنش تأیید شود:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## راه‌اندازی Testnet (بدون Docker)


اگر می‌خواهید یک سناریوی واقعی‌تر را آزمایش کنید، می‌توانید به جای Regtest، گره‌های RLN را بر روی Testnet راه‌اندازی کنید و به خدمات عمومی یا خدماتی که کنترل می‌کنید اشاره کنید:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


به طور پیش‌فرض، اگر هیچ پیکربندی یافت نشود، daemon سعی خواهد کرد از :




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- `indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


با ورود :




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`


شما همچنین می‌توانید این Elements را از طریق API `init`/`unlock` سفارشی‌سازی کنید.


## صدور یک RGB token


برای صدور token، ابتدا با ایجاد UTXOهای "قابل رنگ‌آمیزی" شروع خواهیم کرد:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


البته می‌توانید ترتیب را تغییر دهید. برای تأیید تراکنش، ما یک :


```bash
./regtest.sh mine 1
```


اکنون می‌توانیم یک دارایی RGB ایجاد کنیم. فرمان بستگی به نوع دارایی که می‌خواهید ایجاد کنید و پارامترهای آن دارد. در اینجا من یک NIA (*دارایی غیرقابل تورم*) token به نام "PBN" با یک Supply به مقدار 1000 واحد ایجاد می‌کنم. `precision` به شما اجازه می‌دهد تا قابلیت تقسیم‌پذیری واحدها را تعریف کنید.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


پاسخ شامل شناسه دارایی تازه ایجاد شده است. به یاد داشته باشید که این شناسه را یادداشت کنید. در مورد من، این است:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


سپس می‌توانید آن را به On-Chain منتقل کنید یا در یک کانال Lightning تخصیص دهید. این دقیقاً همان کاری است که در بخش بعدی انجام خواهیم داد.


## باز کردن یک کانال و انتقال دارایی RGB


ابتدا باید نود خود را با استفاده از دستور `/connectpeer` به یک همتا در Lightning Network متصل کنید. در مثال من، هر دو نود را کنترل می‌کنم. بنابراین کلید عمومی نود دوم لایتنینگ خود را با این دستور بازیابی خواهم کرد:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


دستور کلید عمومی نود شماره ۲ من را برمی‌گرداند:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


سپس، کانال را با مشخص کردن دارایی مربوطه (`PBN`) باز خواهیم کرد. فرمان `/openchannel` به شما اجازه می‌دهد اندازه کانال را به ساتوشی تعریف کنید و انتخاب کنید که دارایی RGB را شامل شود. این بستگی به آنچه که می‌خواهید ایجاد کنید دارد، اما در مورد من، فرمان این است:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


بیشتر بدانید اینجا:




- `peer_pubkey_and_opt_addr`: شناسه همتایی که می‌خواهیم به آن متصل شویم (کلید عمومی که قبلاً پیدا کردیم)؛
- `capacity_sat`: ظرفیت کل کانال به ساتوشی؛
- `push_msat`: مقدار به میلی‌ساتوشی که در ابتدا هنگام باز شدن کانال به همتا منتقل می‌شود (در اینجا من بلافاصله 10,000 Sats منتقل می‌کنم تا او بتواند بعداً یک انتقال RGB انجام دهد) ;
- `asset_amount`: مقدار دارایی‌های RGB که باید به کانال اختصاص داده شود ;
- `asset_id` : شناسه منحصربه‌فرد دارایی RGB که در کانال درگیر است؛
- `عمومی`: نشان می‌دهد که آیا کانال باید برای مسیریابی در شبکه عمومی شود یا خیر.


![RLN](assets/fr/14.webp)


برای تأیید تراکنش، ۶ بلاک استخراج می‌شوند:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


کانال Lightning اکنون باز است و همچنین حاوی 500 توکن `PBN` در سمت نود شماره 1 است. اگر نود شماره 2 بخواهد توکن‌های `PBN` دریافت کند، باید generate و Invoice را انجام دهد. در اینجا نحوه انجام آن آمده است:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


با :




- `amt_msat`: مقدار Invoice به میلی‌ساتوشی (حداقل 3000 Sats) ;
- `expiry_sec` : زمان انقضا Invoice به ثانیه ;
- `asset_id` : شناسه دارایی RGB مرتبط با Invoice ;
- `asset_amount`: مقدار دارایی RGB که باید با این Invoice منتقل شود.


در پاسخ، شما یک RGB Invoice دریافت خواهید کرد:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


ما اکنون این Invoice را از اولین نود پرداخت خواهیم کرد، که پول لازم را با `PBN` token نگه می‌دارد:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


پرداخت انجام شده است. این موضوع را می‌توان با اجرای فرمان زیر تأیید کرد:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


در اینجا نحوه استقرار یک نود Lightning که برای حمل دارایی‌های RGB اصلاح شده است، آورده شده است. این نمایش بر اساس:




- یک محیط regtest (از طریق `./regtest.sh`) یا Testnet ;
- یک نود لایتنینگ (`RGB-lightning-node`) بر پایه یک `bitcoind`، یک ایندکسر و یک `RGB-proxy-server`؛
- مجموعه‌ای از APIهای JSON REST برای باز کردن/بستن کانال‌ها، صدور توکن‌ها، انتقال دارایی‌ها از طریق Lightning و غیره.


با تشکر از این فرآیند :




- تراکنش‌های نامزدی لایتنینگ شامل یک خروجی اضافی (OP_RETURN یا Taproot) با لنگر انداختن یک انتقال RGB هستند؛
- انتقالات دقیقاً به همان شیوه پرداخت‌های سنتی لایتنینگ انجام می‌شوند، اما با اضافه شدن یک RGB token؛
- می‌توان چندین گره RLN را برای مسیریابی و آزمایش با پرداخت‌ها در چندین گره متصل کرد، به شرطی که نقدینگی کافی در بیت‌کوین‌ها و دارایی RGB در مسیر وجود داشته باشد.


اگر این آموزش برای شما مفید بود، بسیار سپاسگزار خواهم بود اگر یک انگشت شست Green در زیر قرار دهید. لطفاً این مقاله را در شبکه‌های اجتماعی خود به اشتراک بگذارید. بسیار متشکرم!


من همچنین این آموزش دیگر را توصیه می‌کنم که در آن توضیح می‌دهم چگونه از ابزار RGB CLI که توسط انجمن LNP/BP توسعه یافته است برای ایجاد یک RGB Contract استفاده کنید:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4