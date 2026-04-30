---
name: هماهنگ‌کننده Coinjoin - WabiSabi
description: چگونه یک هماهنگ‌کننده کوین‌جوین را با پیروی از پروتکل WabiSabi (استفاده شده در Wasabi Wallet 2.0) راه‌اندازی و اجرا کنیم
---

![cover](assets/cover.webp)


---

## مقدمه 👋


در این راهنمای تخصصی، ما به شما کمک خواهیم کرد تا یک هماهنگ‌کننده کوین‌جوین راه‌اندازی کنید، که اساساً یک سرور است که افرادی را که می‌خواهند در هزینه‌های تراکنش صرفه‌جویی کنند یا حریم خصوصی زنجیره‌ای خود را در تراکنش‌های مشارکتی افزایش دهند، گرد هم می‌آورد. از آنجا که دیگر هماهنگ‌کننده‌ای که توسط شرکت اداره می‌شود با Wasabi Wallet همراه نیست، کاربران باید سرور هماهنگ‌کننده مورد نظر خود را پیدا و انتخاب کنند. تنها تعداد کمی از هماهنگ‌کننده‌ها درخواست کارمزد هماهنگی 0% کرده‌اند، بنابراین توسعه‌دهندگان Wasabi Wallet سخت کار کرده‌اند تا راه‌اندازی هماهنگ‌کننده جامعه خود را تا حد ممکن آسان کنند (روی سخت‌افزاری به کوچکی Raspberry Pi5!). هماهنگ‌کننده‌های فعال فعلی که درخواست کارمزد هماهنگی 0% دارند را می‌توان در [LiquiSabi](https://liquisabi.com) و مهم‌تر از همه در [nostr](https://github.com/Kukks/WasabiNostr) یافت.


## الزامات 🫴



- VPS (گره میزبانی‌شده) یا کامپیوتر/سرور (گره خودمیزبانی‌شده)
- گره هسته‌ای Bitcoin هرس‌شده/کامل (آزمایش‌شده با نسخه v29.0)


اختیاری:


- ترافیک هدایت دامنه (فرعی) به نود (مثلاً coinjoin.[yourdomain].io)


توصیه می‌شود که تجربه‌ای در کار با دستورات خط فرمان و bash داشته باشید، زیرا همه مراحل قابل خودکارسازی نیستند.


از نظر سخت‌افزاری توصیه می‌شود سیستمی با:


- ۴ هسته
- 16 گیگابایت رم
- ۲ ترابایت SSD یا NVMe (برای یک نود کامل) / ۱۲۸ گیگابایت SSD (برای یک نود pruned)


چنین نیازهایی می‌تواند توسط یک Raspberry Pi 5 با قیمت تنها 120 دلار فراهم شود، به‌جز حافظه که حدود 100 دلار برای یک استیک NVMe با ظرفیت 2 ترابایت هزینه دارد.


سرورهای خصوصی مجازی ارزان معمولاً تنها با 1 هسته و 4 گیگابایت رم ارائه می‌شوند، که به نظر من برای همگام‌سازی و تأیید کل بیت‌کوین blockchain در ارتفاع بلوک 911817 بسیار کم است.


از نظر ذخیره‌سازی، یک فول‌نود حداقل به 2 ترابایت فضای دیسک نیاز دارد، ترجیحاً از نوع SSD یا NVMe. هنگام هرس کردن blockchain، یک درایو ذخیره‌سازی بسیار کوچکتر قابل قبول است (مثلاً یک SSD 128 گیگابایتی).


اگر قصد دارید یک هماهنگ‌کننده برای کوین‌جوین‌های بزرگ (بیش از 300 ورودی) اجرا کنید، توصیه می‌شود سیستمی با هسته‌های سریع‌تر/جدیدتر و عملکرد بالاتر برای تمامی تأییدیه‌های امضا انتخاب کنید.


## نصب 🛠️


روی نودی که می‌خواهیم آخرین نسخه منتشر شده Wasabi Wallet را دانلود و نصب کنیم، که شامل یک بک‌اند و هماهنگ‌کننده به عنوان اجرایی‌های مستقل در کنار wallet است.


آخرین نسخه را پیدا کنید: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) و امضای PGP نسخه را با کلیدها تأیید کنید: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


جزئیات استقرار بسته به سخت‌افزار (معماری CPU) و انتخاب سیستم‌عامل متفاوت است، در زیر جزئیات مختلف برای Raspberry Pi (ARM-64) با Debian مبتنی بر RaspiBlitz به عنوان نقطه شروع ارائه شده است. برای استقرار سیستم‌عامل (X86-64) Ubuntu با استفاده از Nix به جلو بروید.


دستورالعمل‌های نصب را اینجا پیدا کنید: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### استقرار RaspiBlitz/Debian


برای گره‌های RaspiBlitz (آزمایش شده با v1.11) می‌توان از یک استقرار script که از کد منبع ساخته شده استفاده کرد: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### استقرار آسان


برای یک استقرار حداقلی، شما فقط می‌خواهید فایل‌های اجرایی مربوط به پلتفرم خود را در یک پوشه استخراج کنید.

نمونه کدهای خط فرمان برای Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


این باید منجر به پیام امضای معتبر زیر شود:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


و می‌توانید بسته دانلود شده را نصب کنید:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## پیکربندی 🧾


قبل از اجرای هماهنگ‌کننده، باید فایل Config.json را با موارد زیر ویرایش کنید:


- اعتبارنامه‌های Bitcoin RPC
- پارامترهای دور ترجیحی
- کلید عمومی توسعه‌یافته هماهنگ‌کننده (ایجاد یک SegWit wallet جدید برای دریافت گرد و غبار جمع‌آوری‌شده)

**هشدار**: Taproot wallet منجر به غیرقابل‌مصرف شدن UTXO‌ها خواهد شد! از یک Native Segwit wallet در اینجا استفاده کنید.


- انواع آدرس‌های ورودی و خروجی مجاز
- پیکربندی اعلام‌کننده برای انتشار از طریق نوستر (نام، توضیحات، Uri، حداقل ورودی‌ها، رله نوستر، کلید خصوصی نوستر)


می‌توانید هماهنگ‌کننده را که فقط از طریق آدرس .onion قابل دسترسی است اجرا کنید، یا از دامنه clearnet سفارشی خود استفاده کنید.


فایل پیکربندی را در این مسیر پیدا کنید یا ایجاد کنید:


`~/.walletwasabi/coordinator/Config.json`


متن را با دستور ویرایش کنید:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


این مثال Config.json را ببینید:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### پیکربندی تور 🧅


برای پر کردن OnionServicePrivateKey خود احتمالاً ابتدا باید یکی ایجاد کنید.


Wasabi Wallet در صورتی که برای اولین بار با تنظیم ```"PublishAsOnionService": true,``` در فایل Config.json اجرا شود، یک کلید خصوصی برای شما تولید خواهد کرد.


هماهنگ‌کننده را یک بار با دستور زیر اجرا کنید:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


برای مشاهده آدرس سرویس مخفی Onion خود، یا لاگ‌های هماهنگ‌کننده را بررسی کنید با:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


و چیزی شبیه به این پیدا خواهید کرد:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


آدرس طولانی URL که به .onion ختم می‌شود، آدرس سرویس مخفی یا CoordinatorUri شما است.


یا فایل پیکربندی هماهنگ‌کننده خود را دوباره بررسی کنید با:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


که اکنون باید به‌طور خودکار پر شود.


## در حال اجرا ⚡


پس از تنظیم تمام پارامترهای پیکربندی، می‌توانید سرویس هماهنگ‌کننده را اجرا کرده و اولین دور خود را اعلام کنید 🕶️


به سادگی هماهنگ‌کننده را با دستور زیر شروع کنید:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


می‌توانید با بررسی (در مرورگر Tor برای .onion) دور فعلی و تعداد UTXO/سکه‌های ثبت‌شده را نظارت کنید:


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### اختیاری: اشکال‌زدایی سرور هماهنگ‌کننده


می‌توانید برای هرگونه مشکل یا خطا در فایل لاگ در مسیر ```~/.walletwasabi/backend/Logs.txt``` نظارت کنید.


مشکلات معمول شامل مشکلات اتصال RPC است، این باید در ```~/.bitcoin/bitcoin.conf``` با: فعال شود.


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### اختیاری: اجرای سرور بک‌اند


همراه با هماهنگ‌کننده، شما می‌توانید یک سرور بک‌اند برای کاربرانی که نود بیت‌کوین خود را ندارند فراهم کنید تا برای تخمین هزینه‌ها و فیلترهای بلاک به آن متصل شوند.


این سرویس را با فرمان زیر شروع کنید:


```
wbackend
```


## دعوت کاربران Wasabi به هماهنگ‌کننده شما 🫂


برای اینکه کاربران دیگر بتوانند سرویس شما را پیدا کنند، می‌توانید به اعلام‌کننده nostr تکیه کنید، یا یک لینک جادویی با دامنه خود (clearnet) یا سرویس مخفی (.onion link) و پارامترهای گرد مانند این به اشتراک بگذارید:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


وقتی کاربر لینک جادویی را کپی کرده و Wasabi Wallet خود را باز می‌کند، نرم‌افزار به‌طور خودکار دیالوگ هماهنگ‌کننده را با دامنه و پارامترهای شما نشان می‌دهد.


![detected](assets/en/02.webp)


💚🍣 تبریک به خاطر غیرمتمرکز کردن حریم خصوصی بیت‌کوین 🕶️


به یاد داشته باشید آموزش خود را [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika)، Wasabi Wallet فقط برای دفاع است 🛡️