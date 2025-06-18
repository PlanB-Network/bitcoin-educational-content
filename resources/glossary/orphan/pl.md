---
term: ORPHAN
---

Teoretycznie Orphan block odnosi się do ważnego bloku otrzymanego przez węzeł, który jeszcze nie przejął bloku nadrzędnego, czyli poprzedniego w łańcuchu. Mimo że jest on ważny, blok ten pozostaje odizolowany lokalnie jako sierota.


Jednak w powszechnym użyciu termin "Orphan block" często odnosi się do bloku bez dziecka: ważnego bloku, ale nie zachowanego w głównym łańcuchu Bitcoin. Dzieje się tak, gdy dwóch górników znajdzie ważny blok na tej samej wysokości łańcucha w krótkim czasie i rozgłosi go w sieci. Węzły ostatecznie wybierają tylko jeden blok do włączenia do łańcucha, w oparciu o zasadę łańcucha z największą ilością zgromadzonej pracy, czyniąc drugi "sierotą"


![](../../dictionnaire/assets/9.webp)


> osobiście wolę używać terminu "Orphan block", aby mówić o bloku bez rodzica i terminu "nieaktualny blok", aby odnieść się do bloku, który nie ma dziecka. Uważam, że jest to bardziej logiczne i zrozumiałe, chociaż większość bitcoinerów nie stosuje takiego podejścia