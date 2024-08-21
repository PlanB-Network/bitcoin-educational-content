---
term: ELTOO
---

Üldprotokoll Bitcoin'i teise kihi jaoks, mis määratleb, kuidas ühiselt hallata UTXO omandiõigust. Eltoo töötasid välja Christian Decker, Rusty Russell ja Olaoluwa Osuntokun, eelkõige selleks, et lahendada probleeme, mis on seotud Lightning kanalite olekute läbirääkimismehhanismidega, see tähendab avamise ja sulgemise vahel. Eltoo arhitektuur lihtsustab läbirääkimisprotsessi, tutvustades lineaarset olekuhaldussüsteemi, asendades kehtestatud karistuspõhise lähenemise paindlikuma ja vähem karistava uuendusmeetodiga. See protokoll nõuab uut tüüpi SigHash'i kasutamist, mis võimaldab tehingu allkirjas kõiki sisendeid eirata. Seda SigHash'i nimetati algselt `SIGHASH_NOINPUT`, seejärel `SIGHASH_ANYPREVOUT` (*Iga Eelnev Väljund*). Selle rakendamine on planeeritud BIP118-s.

> ► *Eltood nimetatakse mõnikord ka "LN-Sümmeetriaks".*