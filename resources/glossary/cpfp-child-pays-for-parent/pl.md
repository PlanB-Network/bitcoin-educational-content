---
term: CPFP (DZIECKO PŁACI ZA RODZICA)
---

Mechanizm transakcyjny mający na celu przyspieszenie potwierdzenia transakcji Bitcoin, podobny do tego, co robi Replace-by-fee (RBF), ale od strony odbiorcy. Gdy transakcja z opłatami zbyt niskimi w porównaniu z rynkiem utknie w mempoolach węzłów i nie zostanie potwierdzona wystarczająco szybko, odbiorca może dokonać nowej transakcji, wydając bitcoiny otrzymane w zablokowanej transakcji, chociaż nie jest ona jeszcze potwierdzona. Ta druga transakcja koniecznie wymaga wydobycia pierwszej, aby została potwierdzona. Górnicy są zatem zmuszeni do uwzględnienia obu transakcji razem. Druga transakcja przydzieli znacznie więcej opłat transakcyjnych niż pierwsza, w taki sposób, że średnia opłata zachęca górników do uwzględnienia obu transakcji. Transakcja potomna (druga) płaci za transakcję nadrzędną, która utknęła (pierwsza). Właśnie dlatego jest ona określana jako "CPFP"


W ten sposób CPFP pozwala odbiorcy na szybsze uzyskanie środków pomimo niskich opłat początkowych ponoszonych przez nadawcę, w przeciwieństwie do RBF (*Replace-by-fee*), który pozwala nadawcy przejąć inicjatywę w celu przyspieszenia własnej transakcji poprzez zwiększenie opłat.