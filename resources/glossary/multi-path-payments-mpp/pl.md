---
term: PŁATNOŚCI WIELOŚCIEŻKOWE (MPP)
---

Ogólny termin określający wszystkie techniki płatności na Lightning, które umożliwiają podzielenie transakcji na kilka mniejszych części i kierowanie ich różnymi trasami. Innymi słowy, każda część płatności odbywa się inną ścieżką węzła. Umożliwia to ominięcie ograniczeń płynności w pojedynczym kanale na trasie.


Płatności wielościeżkowe oferują również niewielkie korzyści pod względem poufności, ponieważ obserwatorowi trudniej jest powiązać każdy fragment płatności z całą transakcją. Jednak w podstawowej wersji wszystkie fragmenty mają ten sam sekret dla HTLC, co może sprawić, że transakcja będzie identyfikowalna, jeśli obserwator jest obecny na kilku trasach. Co więcej, ponieważ sekret jest unikalny dla wszystkich fragmentów płatności, nie jest on atomowy. Oznacza to, że niektóre części płatności mogą zostać wykonane pomyślnie, podczas gdy inne mogą się nie powieść. Wady te są korygowane za pomocą "Atomic Multi-Path Payment".