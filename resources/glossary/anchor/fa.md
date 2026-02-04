---
term: Anchor
definition: در پروتکل RGB، مجموعه‌ای از داده‌ها که اثبات کند یک التزام در یک معاملهٔ بیتکوین گنجانده شده است، بدون افشای علنی محتوای آن.
---

در پروتکل RGB، یک Anchor مجموعه‌ای از داده‌های سمت کلاینت است که برای اثبات گنجاندن یک Commitment در یک تراکنش استفاده می‌شود. در پروتکل RGB، یک Anchor از Elementsهای زیر تشکیل شده است:




- transaction ID Bitcoin (txid) از Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- اثبات تراکنش اضافی (ETP) در صورت استفاده از مکانیزم Tapret Commitment.


بنابراین، یک Anchor برای ایجاد یک پیوند قابل تأیید بین یک تراکنش خاص Bitcoin و داده‌های خصوصی که توسط پروتکل RGB تأیید شده‌اند، خدمت می‌کند. این تضمین می‌کند که این داده‌ها واقعاً در Blockchain گنجانده شده‌اند، بدون اینکه محتوای دقیق آن‌ها عمومی شود.