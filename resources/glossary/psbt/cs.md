---
term: PSBT
---

Akronym pro "Partially Signed Bitcoin Transaction" (Částečně podepsaná bitcoinová transakce). Jedná se o specifikaci zavedenou s BIP174, která standardizuje způsob, jakým jsou neúplné transakce konstruovány v softwaru souvisejícím s Bitcoinem, jako je například software peněženky. PSBT obaluje transakci, ve které nemusí být vstupy plně podepsány. Obsahuje veškeré nezbytné informace pro účastníka k podepsání transakce bez nutnosti dalších dat. Tím pádem může PSBT nabývat 3 různých forem:
* Plně sestavená transakce, ale ještě nepodepsaná;
* Částečně podepsaná transakce, kde jsou některé vstupy podepsané, zatímco jiné ještě ne;
* Nebo plně podepsaná bitcoinová transakce, která může být převedena do stavu připraveného k vysílání v síti.

Formát PSBT usnadňuje interoperabilitu mezi různým softwarem peněženek a zařízeními pro podpis (hardware peněženky). V současné době se používá verze 0 PSBT, jak je definováno v BIP174, ale verze 2 je navrhována prostřednictvím BIP370.

> ► *Verze 1 PSBT neexistuje. Jelikož verze 0 byla první verzí, druhá verze byla neformálně nazvána verze 2. Ava Chow, která je autorkou BIP370, se tedy rozhodla přiřadit této nové verzi číslo 2, aby se předešlo jakékoli záměně.*