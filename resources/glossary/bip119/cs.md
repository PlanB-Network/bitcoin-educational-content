---
term: BIP119

---
Zavádí nový opkód s názvem `OP_CHECKTEMPLATEVERIFY` (CTV). CTV by umožnil vytvářet v transakcích nevratné dohody, aby bylo možné stanovit konkrétní podmínky, jak lze danou minci utratit, a to i v budoucích transakcích. Konkrétně by umožňoval definovat podmínky pro `scriptPubKey` výstupů transakce na základě `scriptPubKey` UTXO utraceného jako vstup. CheckTemplateVerify je navržen tak, aby byl jednoduchý a bez dynamického stavu. Jeho implementace má za cíl rozšířit možnosti skriptování Bitcoinu a usnadnit tak různé aplikace, jako je kontrola přetížení transakcí, vytváření neinteraktivních platebních kanálů, DLC, platebních poolů... Tento nový opkód by byl zaveden jako náhrada za `OP_NOP4`. Tato změna by znamenala měkký fork.