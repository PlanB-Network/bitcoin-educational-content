---
term: Hrp (human readable part)
definition: پیشوند خواندنی آدرس‌های bech32 که امکان شناسایی نوع آدرس Bitcoin را فراهم می‌کند.
---

HRP، که مخفف "Human Readable Part" به معنای "بخش قابل خواندن توسط انسان" است، یک جزء از آدرس‌های دریافت‌کننده bech32 و bech32m (SegWit v0 و SegWit v1) می‌باشد. HRP به بخشی از Address اشاره دارد که به طور خاص برای خواندن و تفسیر آسان توسط انسان‌ها قالب‌بندی شده است. به عنوان مثال، یک bech32 Bitcoin Address:


```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```


در این Address، `bc` اولیه نشان‌دهنده HRP است. این پیشوند به فرد اجازه می‌دهد تا به سرعت تشخیص دهد که رشته کاراکترهای ارائه شده یک Bitcoin Address است و نه چیز دیگری.