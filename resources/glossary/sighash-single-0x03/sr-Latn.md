---
term: SIGHASH_SINGLE (0X03)
---

Tip zastavice SigHash korišćene u Bitcoin potpisima transakcija da označi da se potpis odnosi na sve ulaze transakcije i samo na jedan izlaz, koji odgovara indeksu istog potpisanog ulaza. Dakle, svaki ulaz potpisan sa `SIGHASH_SINGLE` je specifično povezan sa određenim izlazom. Ostali izlazi nisu obuhvaćeni potpisom i stoga se mogu kasnije menjati. Ovaj tip potpisa je koristan u složenim transakcijama, gde učesnici žele da povežu određene ulaze sa specifičnim izlazima, dok ostavljaju fleksibilnost za ostale izlaze transakcije.