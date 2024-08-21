---
term: STACK
---

V kontextu skriptovacího jazyka používaného pro aplikaci podmínek utrácení na Bitcoin UTXO, stack je datová struktura typu "LIFO" (*Last In, First Out* - poslední přidaný, první odebraný), která slouží k dočasnému ukládání prvků během vykonávání skriptu. Každá operace ve skriptu manipuluje s těmito zásobníky, kde mohou být prvky přidávány (*push*) nebo odebírány (*pop*). Skripty používají zásobníky k vyhodnocení výrazů, ukládání dočasných proměnných a řízení podmínek.

Během vykonávání Bitcoin skriptu mohou být použity 2 zásobníky: hlavní zásobník a alternativní zásobník (alt stack). Hlavní zásobník je používán pro většinu operací skriptu. Na tomto zásobníku operace skriptu přidávají, odebírají nebo manipulují s daty. Alternativní zásobník na druhou stranu slouží k dočasnému ukládání dat během vykonávání skriptu. Specifické operace, jako `OP_TOALTSTACK` a `OP_FROMALTSTACK`, umožňují přenos prvků z hlavního zásobníku do alternativního a naopak.

Například během validace transakce jsou podpisy a veřejné klíče vloženy na hlavní zásobník a zpracovány následujícími operacemi k ověření, že podpisy odpovídají klíčům a datům transakce.

> ► *V angličtině se překlad slova « pile » uvádí jako « stack ». Anglický termín se obecně používá i ve francouzštině během technických diskusí.*