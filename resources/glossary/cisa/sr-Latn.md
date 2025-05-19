---
term: CISA
---

Akronim za "Cross-Input Signature Aggregation". Ovo je tehnički predlog osmišljen da optimizuje veličinu Bitcoin transakcija smanjenjem broja potpisa potrebnih za njihovu validaciju.


Trenutno, na Bitcoin, svaki ulaz u transakciji mora imati individualni potpis pre nego što može biti iskorišćen. Ovo dokazuje da je vlasnik dotičnog UTXO odobrio transakciju. Sa CISA, cilj je kombinovati potpise svih ulaza u jednu transakciju u jedan potpis koji pokriva sve ulaze. Ovo bi omogućilo smanjenje veličine transakcija sa mnogo ulaza, a time i smanjenje njihovih troškova. Ovo bi bilo posebno korisno za one koji obavljaju coinjoin ili konsolidacije, dok bi omogućilo više transakcija da budu potvrđene na Bitcoin bez promene veličine blokova ili intervala. CISA se zasniva na Schnorr protokolu, koji omogućava linearnu agregaciju potpisa. To znači da jedan potpis može dokazati posedovanje nekoliko nezavisnih ključeva.


Međutim, implementacija CISA na Bitcoin je veoma složena, jer zahteva duboke promene u načinu na koji skripte funkcionišu. Trenutno se verifikacija skripti na Bitcoin vrši unos po unos. Prelazak na model gde se cela transakcija proverava odjednom, kao što predlaže CISA, daleko je od trivijalne promene.