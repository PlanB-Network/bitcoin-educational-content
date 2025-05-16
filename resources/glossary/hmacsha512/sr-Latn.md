---
term: HMAC-SHA512
---

`HMAC-SHA512` označava "Hash-based Message Authentication Code - Secure Hash Algorithm 512". To je kriptografski algoritam koji se koristi za verifikaciju integriteta i autentičnosti poruka razmenjenih između dve strane. Kombinuje kriptografsku Hash funkciju `SHA512` sa deljenim tajnim ključem da generate jedinstveni Kod za Autentifikaciju Poruke (MAC) za svaku poruku.


U kontekstu Bitcoin, prirodna upotreba `HMAC-SHA512` je blago izmenjena. Ovaj algoritam se koristi u determinističkom i hijerarhijskom procesu izvođenja kriptografskog ključa stabla Wallet. `HMAC-SHA512` se posebno koristi za prelazak sa seed na glavni ključ, a zatim za svako izvođenje iz roditeljskog para u parove dece. Ovaj algoritam se takođe nalazi unutar drugog algoritma izvođenja nazvanog `PBKDF2`, koji se koristi za prelazak sa fraze za oporavak i passphrase na seed.