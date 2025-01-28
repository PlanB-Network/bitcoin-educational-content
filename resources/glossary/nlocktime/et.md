---
term: NLOCKTIME

---
Tehingutes olev varjatud väli, mis seab ajapõhise tingimuse, enne mida tehingut ei saa lisada kehtivasse plokki. See parameeter võimaldab määrata täpse aja (Unixi ajatempel) või konkreetse arvu plokke tingimusena, et tehingut saaks pidada kehtivaks. Seega on tegemist absoluutse (mitte suhtelise) ajalokiga. `nLockTime` mõjutab kogu tehingut ja võimaldab tegelikult aja kontrollimist, samas kui opkood `OP_CHECKLOCKTIMEVERIFY` võimaldab võrrelda ainult virna ülemist väärtust `nLockTime` väärtusega.