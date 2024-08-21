---
term: NLOCKTIME
---

Sisseehitatud väli tehingutes, mis seab ajapõhise tingimuse, enne mida ei saa tehingut lisada kehtivasse plokki. See parameeter võimaldab määrata täpse aja (Unixi ajatempel) või kindla arvu plokke tingimusena, mille korral tehingut peetakse kehtivaks. Seega on see absoluutne ajalukk (mitte suhteline). `nLockTime` mõjutab kogu tehingut ja võimaldab tõhusalt aja kontrollimist, samas kui operaator `OP_CHECKLOCKTIMEVERIFY` võimaldab võrrelda ainult virna tipus olevat väärtust `nLockTime` väärtusega.