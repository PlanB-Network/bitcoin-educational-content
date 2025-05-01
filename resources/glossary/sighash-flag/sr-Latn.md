---
term: SIGHASH ZASTAVICA
---

Parametar u Bitcoin transakciji koji određuje koje komponente transakcije (ulazi i izlazi) su pokrivene pridruženim potpisom, čime postaju nepromenljive. SigHash Flag je bajt dodat digitalnom potpisu svakog ulaza. Stoga, izbor SigHash Flaga direktno utiče na to koji delovi transakcije su zamrznuti potpisom i koji se još uvek mogu modifikovati nakon toga. Ovaj mehanizam osigurava da potpisi precizno i sigurno obavezuju podatke transakcije prema nameri potpisnika. Postoje tri glavna SigHash Flaga:



- `SIGHASH_ALL` (`0x01`): Potpis se odnosi na sve ulaze i izlaze transakcije, čime ih u potpunosti zaključava;



- `SIGHASH_NONE` (`0x02`): Potpis se odnosi na sve ulaze, ali ni na jedan izlaz, omogućavajući da se izlazi izmene nakon potpisivanja;



- `SIGHASH_SINGLE` (`0x03`): Potpis pokriva sve ulaze i samo jedan izlaz koji odgovara indeksu potpisanog ulaza.


Pored ova tri SigHash zastavice, modifikator `SIGHASH_ANYONECANPAY` (`0x80`) može se kombinovati sa svakim od prethodnih tipova. Kada se ovaj modifikator koristi, samo deo ulaza je potpisan, ostavljajući ostale otvorenim za modifikaciju. Ovde su postojeće kombinacije sa modifikatorom:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Potpis se odnosi na jedan ulaz dok pokriva sve izlaze transakcije;



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Potpis pokriva jedan ulaz, bez obavezivanja na bilo koji izlaz;



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Potpis se odnosi na jedan ulaz i samo na izlaz koji ima isti indeks kao ovaj ulaz.


> ► *Sinonim koji se ponekad koristi za "SigHash" je "Signature Hash Types".*