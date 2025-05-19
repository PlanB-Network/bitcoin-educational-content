---
term: SIGHASH_ANYPREVOUT
---

Predlog za implementaciju novog SigHash Flag modifikatora u Bitcoin, uvedenog sa BIP118. `SIGHASH_ANYPREVOUT` omogućava veću fleksibilnost u upravljanju transakcijama, posebno za napredne aplikacije kao što su platni kanali na Lightning Network i Eltoo ažuriranje. `SIGHASH_ANYPREVOUT` omogućava da potpis ne bude vezan za bilo koji specifičan prethodni UTXO (*Any Previous Output*). U kombinaciji sa `SIGHASH_ALL`, omogućilo bi potpisivanje svih izlaza transakcije, ali nijednog ulaza. Ovo bi omogućilo ponovno korišćenje potpisa za različite transakcije, sve dok su ispunjeni određeni specificirani uslovi.


> ► *Ovaj SigHash modifikator SIGHASH_ANYPREVOUT potiče iz ideje SIGHASH_NOINPUT koju je prvobitno predložio Joseph Poon 2016. godine kako bi unapredio svoj koncept Lightning Network.*