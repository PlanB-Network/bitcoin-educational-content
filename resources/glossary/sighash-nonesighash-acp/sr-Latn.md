---
term: SIGHASH_NONE/SIGHASH_ACP
definition: SigHash kombinacija koja potpisuje samo jedan specifičan ulaz bez obavezivanja na bilo koji izlaz.
---

Tip zastavice SigHash (`0x82`) kombinovan sa modifikatorom `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) korišćen u Bitcoin potpisima transakcija. Ova kombinacija označava da se potpis odnosi samo na određeni ulaz, bez obavezivanja na bilo koji izlaz. Ovo omogućava drugim učesnicima da slobodno dodaju dodatne ulaze i modifikuju sve izlaze transakcije.