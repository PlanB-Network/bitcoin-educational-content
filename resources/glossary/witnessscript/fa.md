---
term: Witnessscript
definition: اسکریپتی که شرایط خرج کردن را برای UTXOهای P2WSH یا P2SH-P2WSH تعریف می‌کند، معادل SegWit برای redeemScript.
---

اسکریپتی که شرایطی را مشخص می‌کند که تحت آن بیت‌کوین‌ها می‌توانند از P2WSH یا P2SH-P2WSH UTXOها خرج شوند. به طور معمول، `witnessScript` شرایط یک امضای چندگانه Wallet را تحت استاندارد SegWit تعیین می‌کند. در این استانداردهای اسکریپت، `scriptPubKey` از UTXO (خروجی) حاوی یک Hash از `witnessScript` است. برای استفاده از این UTXO به عنوان ورودی در یک تراکنش جدید، دارنده باید `witnessScript` اصلی را فاش کند تا تطابق آن با اثر انگشت در `scriptPubKey` را اثبات کند. سپس `witnessScript` باید در `scriptWitness` تراکنش گنجانده شود، که همچنین شامل Elements لازم برای اعتبارسنجی اسکریپت، مانند امضاها است. بنابراین، `witnessScript` معادل SegWit از `redeemscript` در یک تراکنش P2SH است، با این تفاوت که در شاهد تراکنش قرار می‌گیرد و نه در `scriptSig`.


> ► *احتیاط، `witnessScript` نباید با `scriptWitness` اشتباه گرفته شود. در حالی که `witnessScript` شرایط خرج کردن یک P2WSH یا P2SH-P2WSH UTXO را تعریف می‌کند و به خودی خود یک اسکریپت محسوب می‌شود، `scriptWitness` شامل داده‌های شاهد هر ورودی SegWit است.*