---
term: BIP119
---

Zavádí nový operační kód pojmenovaný `OP_CHECKTEMPLATEVERIFY` (CTV). CTV by umožnilo vytváření ne-rekurzivních smluv v transakcích, aby se na určenou minci vztahovaly specifické podmínky, jak může být utracena, včetně v budoucích transakcích. Konkrétněji by to umožnilo definování podmínek na `scriptPubKey` výstupů transakce na základě `scriptPubKey` UTXO utraceného jako vstup. CheckTemplateVerify je navržen tak, aby byl jednoduchý a bez dynamického stavu. Jeho implementace si klade za cíl rozšířit schopnosti skriptování Bitcoinu, aby usnadnila různé aplikace, jako je kontrola přetížení transakcí, vytváření neinteraktivních platebních kanálů, DLCs, platebních poolů... Tento nový operační kód by byl zaveden jako náhrada za `OP_NOP4`. Tato změna by znamenala soft fork.