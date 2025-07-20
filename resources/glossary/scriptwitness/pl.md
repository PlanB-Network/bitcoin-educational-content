---
term: SCRIPTWITNESS
---

Element we wpisach transakcji SegWit, który zawiera podpisy i klucze publiczne niezbędne do odblokowania bitcoinów wysłanych w transakcji. Podobnie jak `scriptSig` w transakcjach Legacy, `scriptWitness` nie jest jednak umieszczany w tym samym miejscu. W rzeczywistości to właśnie ta część, określana jako "świadek" (`*witness*` w języku angielskim), jest przenoszona do oddzielnej bazy danych w celu rozwiązania problemu podatności transakcji na modyfikacje. Każde wejście SegWit ma swój własny `scriptWitness`, a wszystkie `scriptWitness` Elements razem tworzą pole `Witness` transakcji.


> należy uważać, aby nie pomylić `scriptWitness` z `witnessScript`. Podczas gdy `scriptWitness` zawiera dane świadka dla dowolnego wejścia SegWit, `witnessScript` definiuje warunki wydawania P2WSH lub P2SH-P2WSH UTXO i stanowi skrypt sam w sobie, podobny do `redeemscript` dla wyjścia P2SH