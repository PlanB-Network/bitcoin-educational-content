---
term: INDEX (KLÍČOVÉ ČÍSLO)
---

V kontextu HD peněženky se jedná o sekvenční číslo přiřazené dětskému klíči generovanému z rodičovského klíče. Tento index se používá ve spojení s rodičovským klíčem a rodičovským řetězcovým kódem pro deterministické odvození unikátních dětských klíčů. Umožňuje strukturovanou organizaci a reprodukovatelnou generaci několika sourozeneckých párů dětských klíčů ze stejného rodičovského klíče. Jedná se o 32bitové celé číslo používané ve funkci derivace `HMAC-SHA512`. Toto číslo tak rozlišuje sourozenecké dětské klíče v rámci HD peněženky.