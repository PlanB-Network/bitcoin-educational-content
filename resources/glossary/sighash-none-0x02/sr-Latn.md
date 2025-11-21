---
term: SIGHASH_NONE (0X02)
---

Tip zastavice SigHash korišćen u Bitcoin potpisima transakcija da označi da se potpis odnosi na sve ulaze transakcije, ali ni na jedan njen izlaz. Upotreba `SIGHASH_NONE` podrazumeva da potpisnik potvrđuje samo ulaze, omogućavajući da izlazi ostanu neodređeni ili promenljivi nakon potpisivanja. Ovaj tip potpisa je koristan u slučajevima kada potpisnik želi da ovlasti druge strane da odluče kako će bitkoini biti raspodeljeni u transakciji.