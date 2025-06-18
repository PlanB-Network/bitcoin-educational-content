---
term: ODŁAMKI (BŁYSKAWICA)
---

W kontekście *Multi-Path Payments (MPP)* lub *Atomic Multi-Path Payments (AMP)*, Shard jest ułamkiem płatności globalnej. Każdy Shard reprezentuje część całkowitej płatności, która jest kierowana oddzielnie przez inną trasę w Lightning.


W MPP wszystkie odłamki mają ten sam sekret, podczas gdy w AMP każdy Shard ma unikalny częściowy sekret. Odbiorca grupuje odłamki w celu odtworzenia i sfinalizowania pełnej płatności. Mechanizm ten omija ograniczenia płynności na pojedynczym kanale.