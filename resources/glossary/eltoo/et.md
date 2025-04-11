---
term: ELTOO

---
Bitcoini teise kihi üldine protokoll, mis määratleb, kuidas ühiselt hallata UTXO omandiõigust. Eltoo töötasid välja Christian Decker, Rusty Russell ja Olaoluwa Osuntokun, eelkõige selleks, et lahendada probleemid, mis on seotud Lightning-kanali olekute läbirääkimiste mehhanismidega, st avamise ja sulgemise vahel. Eltoo arhitektuur lihtsustab läbirääkimisprotsessi, võttes kasutusele lineaarse oleku haldamise süsteemi, asendades väljakujunenud karistuspõhise lähenemisviisi paindlikuma ja vähem karistusliku uuendamismeetodiga. See protokoll nõuab uut tüüpi SigHashi kasutamist, mis võimaldab ignoreerida kõiki tehingu allkirja sisendeid. Seda SigHashi nimetati algselt `SIGHASH_NOINPUT`, seejärel `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Selle rakendamine on kavas BIP118-s.

> ► *Eltoo nimetatakse mõnikord ka "LN-sümmeetriaks".*