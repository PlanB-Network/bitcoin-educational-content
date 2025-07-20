---
term: ATOMOWE PŁATNOŚCI WIELOŚCIEŻKOWE
---

Ulepszona wersja MPP (*Multi-Path Payments*), w której każdy fragment płatności ma odrębny częściowy sekret, zapewniając, że transakcja jest rozliczana atomowo, tj. w całości lub wcale.


MPP to techniki płatności w Lightning, które umożliwiają podzielenie transakcji na kilka mniejszych części i kierowanie ich różnymi trasami. Innymi słowy, każda część płatności odbywa się inną ścieżką węzła. Pozwala to obejść ograniczenia płynności na pojedynczym kanale w trasie. W podstawowych MPP każda frakcja płatności dzieli ten sam sekret, a zatem ten sam Hash w HTLC. Może to sprawić, że transakcja będzie identyfikowalna, jeśli obserwator jest obecny na kilku trasach, ponieważ może połączyć wszystkie te identyczne sekrety. Co więcej, ponieważ sekret jest unikalny dla wszystkich części płatności, nie jest atomowy. Oznacza to, że niektóre części płatności mogą zostać wykonane pomyślnie, podczas gdy inne mogą się nie powieść.


W AMP unikalne sekrety częściowe są używane dla każdej frakcji. Po otrzymaniu wszystkich fragmentów umożliwiają one odbiorcy odtworzenie oryginalnego ogólnego sekretu i zażądanie pełnej płatności. Metoda ta uniemożliwia częściowe rozliczenie płatności, ponieważ posiadanie wszystkich częściowych sekretów jest wymagane do odblokowania pełnej płatności. Zapewnia to, że płatność jest w pełni udana lub w pełni nieudana (tj. atomowa). AMP poprawia również poufność, ponieważ nie ma już żadnych widocznych powiązań między różnymi trasami.


Jedną z zalet AMP jest to, że działają one nawet wtedy, gdy tylko odbiorca i nadawca wdrożyli tę metodę. Węzły pośredniczące przetwarzają te płatności jako konwencjonalne transakcje przy użyciu HTLC, nie zdając sobie sprawy, że przetwarzają ułamki większej płatności.