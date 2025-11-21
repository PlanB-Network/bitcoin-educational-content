---
term: PLASTYCZNOŚĆ (TRANSAKCJA)
---

Odnosi się do możliwości nieznacznej modyfikacji struktury transakcji Bitcoin, bez zmiany jej efektu, ale przy jednoczesnej zmianie identyfikatora transakcji (*txid*). Właściwość ta może zostać wykorzystana w złośliwy sposób, aby wprowadzić w błąd zainteresowane strony co do statusu transakcji, powodując w ten sposób takie problemy, jak podwójne wydatki. Złośliwość była możliwa dzięki elastyczności zastosowanego podpisu cyfrowego. SegWit Soft Fork został w szczególności wprowadzony, aby zapobiec tej złośliwości transakcji Bitcoin, co skomplikowało implementację Lightning Network. Osiąga się to poprzez usunięcie możliwych do zmodyfikowania danych z transakcji z obliczeń txid.


> chociaż rzadko, termin "mutowalność" jest czasami używany w odniesieniu do tego samego pojęcia