---
name: RGB
description: معرفی و ایجاد دارایی در RGB
---

![cover](assets/cover.webp)


## معرفی


در ۳ ژانویه ۲۰۰۹، Satoshi ناکاموتو اولین نود Bitcoin را راه‌اندازی کرد، از آن لحظه نودهای جدیدی پیوستند و Bitcoin شروع به رفتار کرد به گونه‌ای که گویی یک شکل جدید از زندگی است، شکلی از زندگی که تکامل آن متوقف نشده است، کم‌کم به امن‌ترین شبکه در جهان تبدیل شده است به عنوان نتیجه‌ای از طراحی منحصر به فرد آن، که به خوبی توسط Satoshi اندیشیده شده است، زیرا از طریق مشوق‌های اقتصادی، کاربران که معمولاً به آنها ماینر گفته می‌شود را جذب می‌کند تا در انرژی و قدرت محاسباتی سرمایه‌گذاری کنند که به امنیت شبکه کمک می‌کند.


همان‌طور که Bitcoin به رشد و پذیرش خود ادامه می‌دهد، با مسائل مقیاس‌پذیری مواجه است. شبکه Bitcoin اجازه می‌دهد یک بلوک جدید با تراکنش‌ها در زمانی تقریبی ۱۰ دقیقه استخراج شود. با فرض اینکه ما ۱۴۴ بلوک در روز با حداکثر مقادیر ۲۷۰۰ تراکنش در هر بلوک داشته باشیم، Bitcoin تنها ۴.۵ تراکنش در ثانیه را مجاز می‌داند. Satoshi از این محدودیت آگاه بود، ما می‌توانیم این را در ایمیلی که در مارس ۲۰۱۱ به مایک هرن ارسال شده است ببینیم، جایی که او توضیح می‌دهد چگونه چیزی که امروز به عنوان یک کانال پرداخت می‌شناسیم کار می‌کند. پرداخت‌های خرد به سرعت و با اطمینان بدون انتظار برای تأییدات انجام می‌شوند. اینجاست که پروتکل‌های off-chain وارد می‌شوند.


بر اساس گفته‌های کریستین دکر، پروتکل‌های off-chain معمولاً سیستم‌هایی هستند که در آن کاربران از داده‌های یک Blockchain استفاده می‌کنند و آن را بدون دست زدن به خود Blockchain تا آخرین لحظه مدیریت می‌کنند. بر اساس این مفهوم، Lightning Network متولد شد، شبکه‌ای که از پروتکل‌های off-chain استفاده می‌کند تا پرداخت‌های Bitcoin تقریباً به صورت فوری انجام شوند و از آنجا که همه این عملیات‌ها بر روی بلاک چین نوشته نمی‌شوند، امکان انجام هزاران تراکنش در ثانیه و مقیاس‌پذیری Bitcoin را فراهم می‌کند.


تحقیق و توسعه در زمینه پروتکل‌های off-chain بر روی Bitcoin جعبه پاندورا را باز کرده است، امروز می‌دانیم که می‌توانیم بسیار بیشتر از انتقال ارزش به صورت غیرمتمرکز دست یابیم، انجمن استانداردهای LNP/BP غیرانتفاعی بر توسعه پروتکل‌های Layer 2 و 3 بر روی Bitcoin و Lightning Network تمرکز دارد، در میان این پروژه‌ها RGB برجسته است.


## RGB چیست؟


RGB از تحقیق پیتر تاد3 درباره مهر و موم‌های یکبار مصرف و اعتبارسنجی سمت مشتری پدیدار شد، که در سال‌های 2016-2019 توسط جیاکومو زوکو و جامعه به یک پروتکل دارایی بهتر برای Bitcoin و Lightning Network تبدیل شد. تکامل بیشتر این ایده‌ها منجر به توسعه RGB به یک سیستم کامل Smart contract توسط ماکسیم اورلوفسکی شد، که از سال 2019 با مشارکت جامعه رهبری اجرای آن را بر عهده دارد.


ما می‌توانیم RGB را به عنوان مجموعه‌ای از پروتکل‌های متن‌باز تعریف کنیم که به ما اجازه می‌دهد قراردادهای هوشمند پیچیده را به صورت مقیاس‌پذیر و محرمانه اجرا کنیم. این یک شبکه خاص نیست (مانند Bitcoin یا Lightning)؛ هر Smart contract فقط مجموعه‌ای از شرکت‌کنندگان Contract است که می‌توانند با استفاده از کانال‌های ارتباطی مختلف (به طور پیش‌فرض Lightning Network) تعامل داشته باشند. RGB از Bitcoin Blockchain به عنوان Layer حالت Commitment استفاده می‌کند و کد Smart contract و داده‌های off-chain را حفظ می‌کند، که این امر آن را مقیاس‌پذیر می‌سازد و از تراکنش‌های Bitcoin (و Script) به عنوان سیستم کنترل Ownership برای قراردادهای هوشمند بهره می‌برد؛ در حالی که تکامل Smart contract توسط یک طرح off-chain تعریف می‌شود، در نهایت مهم است که توجه داشته باشید که همه چیز در سمت مشتری تأیید می‌شود.


به زبان ساده، RGB سیستمی است که به کاربر اجازه می‌دهد تا یک Smart contract را ممیزی کند، آن را اجرا کند و به صورت فردی در هر زمان بدون هزینه اضافی تأیید کند زیرا برای این کار از Blockchain مانند سیستم‌های "سنتی" استفاده نمی‌کند. سیستم‌های قرارداد هوشمند پیچیده توسط اتریوم پیشگام شدند اما به دلیل اینکه کاربر باید برای هر عملیات مقدار قابل توجهی گاز مصرف کند، هرگز به مقیاس‌پذیری که وعده داده بودند نرسیدند و در نتیجه هرگز گزینه‌ای برای بانک کردن کاربرانی که از سیستم مالی فعلی محروم شده‌اند نبودند.


در حال حاضر، صنعت Blockchain ترویج می‌کند که هم کد قراردادهای هوشمند و هم داده‌ها باید در Blockchain ذخیره شوند و توسط هر گره شبکه اجرا شوند، بدون توجه به افزایش بیش از حد اندازه یا سوء استفاده از منابع محاسباتی. طرح پیشنهادی توسط RGB بسیار هوشمندانه‌تر و کارآمدتر است زیرا با جدا کردن قراردادهای هوشمند و داده‌ها از Blockchain، از اشباع شبکه که در سایر پلتفرم‌ها دیده می‌شود جلوگیری می‌کند و در عین حال هر گره را مجبور به اجرای هر Contract نمی‌کند بلکه طرف‌های درگیر را مجبور می‌کند که به سطحی از محرمانگی برسند که قبلاً هرگز دیده نشده است.


![RGB vs Ethereum](assets/1.webp)


## قراردادهای هوشمند در RGB


در RGB توسعه‌دهنده Smart contract یک طرح تعریف می‌کند که قوانین چگونگی تکامل Contract را در طول زمان مشخص می‌کند. این طرح استانداردی برای ساخت قراردادهای هوشمند در RGB است و هم صادرکننده هنگام تعریف یک Contract برای صدور و هم Wallet یا Exchange باید به یک طرح خاص پایبند باشند که بر اساس آن باید Contract را اعتبارسنجی کنند. تنها در صورتی که اعتبارسنجی صحیح باشد، هر طرف می‌تواند درخواست‌ها را بپذیرد و با دارایی کار کند.


یک Smart contract در RGB یک Directed Acyclic Graph (DAG) از تغییرات حالت است، جایی که تنها بخشی از گراف همیشه شناخته شده است و دسترسی به بقیه وجود ندارد. طرح RGB یک مجموعه اصلی از قوانین برای تکامل این گراف است که Smart contract با آن شروع می‌شود. هر Contract Participant ممکن است به آن قوانین اضافه کند (اگر این توسط Schema مجاز باشد) و گراف حاصل از کاربرد تکراری آن قوانین ساخته می‌شود.


## دارایی‌های قابل تعویض


دارایی‌های قابل تعویض در RGB از مشخصات LNPBP RGB-20 پیروی می‌کنند، زمانی که یک RGB-20 تعریف می‌شود، داده‌های دارایی که به عنوان "داده‌های Genesis" شناخته می‌شوند، از طریق Lightning Network توزیع می‌شوند، که شامل آنچه برای استفاده از دارایی لازم است می‌باشد. ابتدایی‌ترین شکل دارایی‌ها اجازه صدور ثانویه، سوزاندن token، تغییر نام یا جایگزینی را نمی‌دهند.


گاهی اوقات صادرکننده نیاز خواهد داشت که در آینده توکن‌های بیشتری صادر کند، به عنوان مثال استیبل‌کوین‌هایی مانند USDT، که ارزش هر token را به ارزش یک ارز تورمی مانند USD متصل نگه می‌دارد. برای دستیابی به این هدف، طرح‌های پیچیده‌تر RGB-20 وجود دارد و علاوه بر داده‌های Genesis، آنها از صادرکننده می‌خواهند که محموله‌هایی تولید کند که در Lightning Network نیز در گردش خواهند بود؛ با این اطلاعات می‌توانیم کل Supply در گردش دارایی را بدانیم. همین امر برای سوزاندن دارایی‌ها یا تغییر نام آن‌ها نیز صدق می‌کند.


اطلاعات مربوط به دارایی می‌تواند عمومی یا خصوصی باشد: اگر صادرکننده نیاز به محرمانگی داشته باشد، می‌تواند انتخاب کند که اطلاعات مربوط به token را به اشتراک نگذارد و عملیات را در حریم خصوصی کامل انجام دهد، اما ما همچنین حالت مخالفی داریم که در آن صادرکننده و دارندگان نیاز دارند که کل فرآیند شفاف باشد. این با به اشتراک‌گذاری داده‌های token محقق می‌شود.


## رویه‌های RGB-20


فرآیند سوزاندن توکن‌ها را غیرفعال می‌کند، توکن‌های سوزانده‌شده دیگر قابل استفاده نیستند.


فرآیند جایگزینی زمانی اتفاق می‌افتد که توکن‌ها سوزانده می‌شوند و مقدار جدیدی از همان token ایجاد می‌شود. این کار به کاهش اندازه داده‌های تاریخی دارایی کمک می‌کند، که برای حفظ سرعت دارایی مهم است.


برای پشتیبانی از مورد استفاده‌ای که در آن امکان سوزاندن دارایی‌ها بدون نیاز به جایگزینی آن‌ها وجود دارد، از زیرطرح RGB-20 استفاده می‌شود که فقط اجازه سوزاندن دارایی‌ها را می‌دهد.


## دارایی‌های غیرقابل تعویض


دارایی‌های غیرقابل تعویض در RGB از مشخصات LNPBP RGB-21 پیروی می‌کنند. هنگامی که با NFTها کار می‌کنیم، یک طرح اصلی و یک زیرطرح داریم. این طرح‌ها دارای یک روش حکاکی هستند که به ما اجازه می‌دهد داده‌های سفارشی را توسط مالک token پیوست کنیم. رایج‌ترین مثالی که امروزه در NFTها می‌بینیم، هنر دیجیتالی است که به token متصل است. صادرکننده token می‌تواند با استفاده از زیرطرح RGB-21 این حکاکی داده‌ها را ممنوع کند. برخلاف سایر سیستم‌های NFT Blockchain، RGB اجازه می‌دهد داده‌های رسانه‌ای token با اندازه بزرگ به صورت کاملاً غیرمتمرکز و مقاوم در برابر سانسور توزیع شوند، با استفاده از افزونه‌ای به شبکه Lightning P2P به نام Bifrost، که همچنین برای ساخت بسیاری از اشکال دیگر از قابلیت‌های خاص RGB Smart contract استفاده می‌شود.


علاوه بر دارایی‌های قابل تعویض و NFTها، RGB و Bifrost می‌توانند برای تولید اشکال دیگر قراردادهای هوشمند، از جمله DEXها، استخرهای نقدینگی، استیبل کوین‌های الگوریتمی و غیره استفاده شوند که در مقالات آینده به آن‌ها خواهیم پرداخت.


## ‏NFT از RGB در مقابل NFT از پلتفرم‌های دیگر



- نیازی به ذخیره‌سازی گران‌قیمت Blockchain نیست
- نیازی به IPFS نیست، به جای آن از یک افزونه Lightning Network (به نام Bifrost) استفاده می‌شود (و این افزونه به طور کامل از مبدا تا مقصد رمزگذاری شده است)
- نیازی به یک راه‌حل مدیریت داده خاص نیست – باز هم، بیفراست این نقش را بر عهده می‌گیرد
- نیازی به اعتماد به وب‌سایت‌ها برای نگهداری داده‌ها برای توکن‌های NFT یا درباره دارایی‌های مسائل / Contract ABI‌ها نیست.
- رمزگذاری DRM داخلی و مدیریت Ownership
- زیرساخت برای پشتیبان‌گیری با استفاده از Lightning Network (Bifrost)
- راه‌های کسب درآمد از محتوا (نه فقط فروش خود NFT، بلکه دسترسی به محتوا، چندین بار)


## نتیجه‌گیری‌ها


از زمان راه‌اندازی Bitcoin، تقریباً ۱۳ سال پیش، تحقیقات و آزمایش‌های زیادی در این زمینه انجام شده است. هم موفقیت‌ها و هم اشتباهات به ما اجازه داده‌اند تا کمی بیشتر بفهمیم که سیستم‌های غیرمتمرکز در عمل چگونه رفتار می‌کنند، چه چیزی آن‌ها را واقعاً غیرمتمرکز می‌کند و چه اقداماتی تمایل به هدایت آن‌ها به سمت تمرکز دارند. همه این‌ها ما را به این نتیجه رسانده است که غیرمتمرکزسازی واقعی یک پدیده نادر و دشوار برای دستیابی است. غیرمتمرکزسازی واقعی تنها توسط Bitcoin به دست آمده است و به همین دلیل است که ما تلاش‌های خود را متمرکز بر ساخت بر روی آن کرده‌ایم.


RGB سوراخ خرگوش خود را درون سوراخ خرگوش Bitcoin دارد، در حالی که من در حال سقوط از طریق آنها هستم، آنچه را که آموخته‌ام ارسال خواهم کرد، در مقاله بعدی مقدمه‌ای بر گره‌های LNP و RGB و نحوه استفاده از آنها خواهیم داشت.



- متاسفانه نمی‌توانم محتوای وب‌سایت‌ها یا لینک‌های خارجی را مشاهده یا ترجمه کنم. اگر متنی دارید که می‌خواهید ترجمه شود، لطفاً آن را اینجا قرار دهید.
- ۲ https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- ۳ https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- ۴ https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- ۵ https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# آموزش RGB-node


## معرفی


در این آموزش، نحوه استفاده از RGB-node برای ایجاد یک token قابل تعویض و نحوه انتقال آن را توضیح می‌دهیم. این سند بر اساس دموی RGB-node است و تفاوت آن در این است که این آموزش از داده‌های واقعی Testnet استفاده می‌کند و برای این منظور، باید از این پس Partially Signed Bitcoin Transaction و PSBT خود را بسازیم.


## الزامات


استفاده از یک توزیع لینوکس توصیه می‌شود، این آموزش با استفاده از Pop!OS نوشته شده است که بر پایه اوبونتو است و شما به موارد زیر نیاز خواهید داشت:



- بارگیری
- Bitcoin هسته
- گیت


توجه: این آموزش اجرای دستورات در یک ترمینال لینوکس را نشان می‌دهد، برای تمایز بین آنچه کاربر می‌نویسد و پاسخی که در ترمینال دریافت می‌کند، ما از نماد $ برای نشان دادن پرامپت بش استفاده می‌کنیم.


شما نیاز خواهید داشت تا برخی وابستگی‌ها را نصب کنید:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


ساخت و اجرا


گره RGB در حال پیشرفت (WIP) است، به همین دلیل باید خود را در یک کامیت خاص (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) قرار دهیم تا بتوانیم آن را به درستی کامپایل و استفاده کنیم، برای این کار دستورات زیر را اجرا می‌کنیم.


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


اکنون آن را کامپایل می‌کنیم، فراموش نکنید که از پرچم --locked استفاده کنید زیرا یک تغییر شکننده در نسخه‌ای از clap معرفی شده است.


```
$ cargo install --path . --all-features --locked

....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```


همانطور که کامپایلر Rust به ما می‌گوید، فایل‌های باینری به دایرکتوری $HOME/.cargo/bin کپی شده‌اند، اگر کامپایلر شما آنها را به مکان دیگری کپی کرده است، باید مطمئن شوید که آن دایرکتوری در $PATH گنجانده شده است.


در میان باینری‌های نصب شده، می‌توانیم سه دیمن یا سرویس (فایل‌هایی که به d ختم می‌شوند) و یک CLI (خط فرمان Interface) را ببینیم. CLI به ما اجازه می‌دهد تا با rgbd اصلی daemon تعامل داشته باشیم. همانطور که در این آموزش قصد داریم دو نود را اجرا کنیم، به دو کلاینت نیز نیاز خواهیم داشت، هر کدام باید به نود خود متصل شوند، برای این کار دو نام مستعار ایجاد می‌کنیم.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


ما می‌توانیم به سادگی aliasها را اجرا کنیم یا آن‌ها را به انتهای فایل $HOME/.bashrc اضافه کرده و دستور source $HOME/.bashrc را اجرا کنیم.

فرضیه


گره RGB هیچ‌گونه عملکرد مرتبط با Wallet را مدیریت نمی‌کند، بلکه فقط وظایف خاص RGB را بر روی داده‌هایی که توسط یک Wallet خارجی مانند هسته Bitcoin ارائه می‌شود، انجام می‌دهد. به‌طور خاص، برای نمایش یک جریان کاری پایه با صدور و انتقال، ما نیاز خواهیم داشت:



- یک issuance_utxo که RGB-node-0 دارایی جدید صادر شده را به آن متصل خواهد کرد
- دریافت_utxo که در آن RGB-node-1 دارایی را دریافت می‌کند
- تغییر_utxo که در آن RGB-node-0 تغییر دارایی را دریافت می‌کند
- یک Partially Signed Bitcoin Transaction (tx.PSBT)، که کلید عمومی خروجی آن برای شامل کردن یک Commitment به انتقال، تغییر خواهد یافت.


ما از هسته Bitcoin به CLI استفاده خواهیم کرد، نیاز داریم که bitcoind و daemon بر روی Testnet اجرا شوند، این به ما قابلیت همکاری می‌دهد و در نهایت قادر خواهیم بود دارایی‌های خود را به کاربر دیگر RGB که این آموزش را دنبال کرده است، ارسال کنیم.


برای سادگی، این نام مستعار را در انتهای فایل ~/.bashrc خود اضافه خواهیم کرد.


```
alias bcli="bitcoin-cli -testnet"
```


بیایید تراکنش‌های خروجی خرج‌نشده خود را فهرست کنیم و دو مورد را انتخاب کنیم، یکی به عنوان issuance_utxo و دیگری به عنوان change_utxo خواهد بود، مهم نیست کدام به کدام است، نکته مهم این است که صادرکننده کنترل این دو را دارد UTXO.


```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```


قبل از اینکه جلوتر برویم، باید درباره‌ی outpoints صحبت کنیم. یک تراکنش می‌تواند شامل چندین خروجی باشد، outpoint شامل یک txid با اندازه‌ی 32 بایت و یک شماره‌ی شاخص خروجی 4 بایتی (vout) است که برای اشاره به خروجی خاصی با یک دونقطه : جدا شده‌اند. در خروجی listunspent ما می‌توانیم دو UTXO پیدا کنیم، در هر کدام می‌توانیم txid و vout را ببینیم، این‌ها outpoints مربوط به issuance_utxo و change_utxo هستند.


receive_utxo یک UTXO است که توسط گیرنده کنترل می‌شود، در این مورد ما از e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 استفاده خواهیم کرد که یک outpoint از یک Wallet دیگر است.



- صدور_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- دریافت_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


ما اکنون قصد داریم یک تراکنش نیمه امضا شده (tx.PSBT) ایجاد کنیم که خروجی آن برای شامل کردن یک تعهد به انتقال تغییر خواهد کرد. به یاد داشته باشید که txid و vout را با موارد خودتان جایگزین کنید. مقصد Address واقعاً مهم نیست، می‌تواند متعلق به شما باشد یا از شخص دیگری باشد، مهم نیست که این Sats به کجا می‌رود، آنچه مهم است این است که ما از issuance_utxo استفاده می‌کنیم.


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


خروجی به ما یک PSBT در کدگذاری base64 داد که از آن برای ایجاد tx.PSBT استفاده خواهیم کرد.


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


بیایید یک دایرکتوری جدید به نام rgbdata ایجاد کنیم که در آن دایرکتوری داده‌های هر گره ذخیره می‌شود.


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


در حال حاضر در $HOME/rgbdata قرار دارد، ما هر گره را در ترمینال‌های مختلف شروع می‌کنیم، جایی که ~/.cargo/bin دایرکتوری است که cargo تمام باینری‌ها را پس از نصب RGB-node کپی کرده است.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## صدور


برای صدور یک دارایی، ما rgb0-CLI را با زیرفرمان‌های صدور قابل تعویض اجرا می‌کنیم، سپس آرگومان‌ها، نماد USDT، نام "USD Tether" و در تخصیص، مقدار صدور و issuance_utxo را مانند زیر استفاده خواهیم کرد:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


دارایی با موفقیت صادر شد. از این اطلاعات برای به اشتراک‌گذاری استفاده کنید:

اطلاعات دارایی:


```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"


genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```


ما assetId را دریافت می‌کنیم، به آن نیاز داریم تا دارایی را انتقال دهیم.


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## generate blinded UTXO


برای دریافت USDT جدید، RGB-node-1 نیاز دارد تا یک blinded UTXO مربوط به receive_utxo را generate کند تا دارایی را نگه دارد.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


برای اینکه بتوانیم انتقالات مربوط به این UTXO را بپذیریم، به receive_utxo اصلی و blinding_factor نیاز خواهیم داشت.


## انتقال


برای انتقال مقداری از دارایی به RGB-node-1، باید آن را به blinded UTXO ارسال کنیم، RGB-node-0 نیاز دارد که یک Consignment و یک افشاگری ایجاد کند و آن را در یک تراکنش Bitcoin متعهد کند. سپس به یک PSBT نیاز خواهیم داشت که آن را اصلاح کنیم تا تعهد را شامل شود. علاوه بر این، گزینه‌های -i و -a به ما اجازه می‌دهند که یک نقطه خروجی ورودی که منشاء دارایی خواهد بود و تخصیصی که در آن تغییر را دریافت خواهیم کرد، ارائه دهیم، باید آن را به صورت زیر مشخص کنیم @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


این سه فایل جدید، Consignment، افشا و PSBT شامل تغییرات را خواهد نوشت، این PSBT به نام Witness Transaction خوانده می‌شود، Consignment به RGB-node-1 ارسال می‌شود.


## شاهد


Witness Transaction باید امضا و پخش شود، برای این کار باید آن را به base64 رمزگذاری کنیم.


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


با استفاده از زیر فرمان walletprocesspsbt آن را امضا کنید.


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


اکنون آن را نهایی کنید و هگز را دریافت کنید.


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## پخش زنده


با استفاده از زیر فرمان sendrawtransaction آن را پخش کنید تا در Blockchain تأیید شود.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## پذیرفتن


برای پذیرش یک انتقال ورودی، RGB-node-1 باید فایل Consignment را از RGB-node-0 دریافت کرده باشد، receive_utxo و blinding_factor مربوطه که در طول تولید blinding UTXO تولید شده‌اند را داشته باشد.


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


اکنون می‌توانیم (در فیلد knownAllocations) تخصیص جدید ۱۰۰ واحد دارایی در <receive_utxo> را با اجرای: مشاهده کنیم.


```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```


از آنجایی که receive_utxo در زمان انتقال blinded بود، پرداخت‌کننده RGB-node-0 اطلاعاتی درباره اینکه 100 USDT به کجا ارسال شده است ندارد، بنابراین مکان در knownAllocations نشان داده نمی‌شود.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```


اما همانطور که می‌بینید، RGB-node-0 نمی‌تواند تغییر دارایی 900 را که با آرگومان -a به فرمان انتقال ارائه کردیم، ببیند. برای ثبت تغییر، RGB-node-0 نیاز دارد که افشا را بپذیرد.


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


اگر RGB-node-0 موفق بود، می‌توانید تغییر را با فهرست کردن دارایی مشاهده کنید.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```


## نتیجه‌گیری‌ها


ما توانسته‌ایم یک دارایی قابل تعویض ایجاد کنیم و آن را به صورت خصوصی از یک تراکنش به تراکنش دیگر منتقل کنیم، اگر تراکنش تأیید شده در یک Block explorer را بررسی کنیم، تفاوتی با تراکنش‌های معمولی پیدا نخواهیم کرد، این به دلیل این است که RGB از مهرهای یک‌بار مصرف برای تغییر تراکنش‌ها استفاده می‌کند. در این پست، مقدمه‌ای بر نحوه کار RGB ارائه می‌دهم.


این پست ممکن است دارای اشکالاتی باشد، اگر چیزی پیدا کردید لطفاً به من اطلاع دهید تا این راهنما را بهبود بخشم، پیشنهادات و انتقادات نیز خوش‌آمد هستند، هکینگ خوش! 🖖