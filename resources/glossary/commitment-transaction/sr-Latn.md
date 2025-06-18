---
term: Commitment Transaction
---

U kontekstu dvosmernog kanala unutar Lightning mreže, Commitment Transaction je transakcija koju obe strane kreiraju i potpisuju, bez objavljivanja na glavnom lancu. Ona predstavlja trenutno stanje raspodele sredstava između strana u kanalu, pri čemu svaka Lightning uplata rezultira novim Commitment Transaction. Ove transakcije su validne, ali se emituju samo kada se kanal jednostrano zatvori. Sadrže izlaze za svaku stranu, odražavajući raspodelu sredstava prema Lightning uplatama izvršenim od otvaranja kanala. Mehanizmi kazne su povezani kako bi odvratili strane od emitovanja zastarelih stanja kanala, odnosno starih Commitment transakcija koje odražavaju netačnu raspodelu sredstava.