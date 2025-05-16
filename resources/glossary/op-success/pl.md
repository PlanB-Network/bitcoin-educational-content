---
term: OP_SUCCESS
---

`OP_SUCCESS` reprezentuje serię kodów operacyjnych, które zostały wyłączone w przeszłości i są teraz zarezerwowane do przyszłego użytku w Tapscript. Ich ostatecznym celem jest ułatwienie aktualizacji i rozszerzeń języka skryptowego, poprzez umożliwienie wprowadzenia nowych funkcji za pomocą Soft forków. Gdy jeden z tych kodów operacyjnych zostanie napotkany w skrypcie, oznacza to automatyczne powodzenie tej części skryptu, niezależnie od obecnych danych lub warunków. Oznacza to, że skrypt kontynuuje wykonywanie bez niepowodzenia, niezależnie od poprzednich operacji.


Tak więc, gdy nowy kod operacyjny jest dodawany do `OP_SUCCESS`, z konieczności reprezentuje on dodanie bardziej restrykcyjnej reguły niż poprzednia. Zaktualizowane węzły mogą następnie zweryfikować zgodność z tą regułą, a węzły niezaktualizowane nie odrzucą powiązanych transakcji i bloków, które je zawierają, ponieważ `OP_SUCCESS` zatwierdza tę część skryptu. Dlatego nie ma Hard Fork.


Dla porównania, `OP_NOP` (*Brak operacji*) również służą jako symbole zastępcze w skrypcie, ale nie mają żadnego wpływu na wykonanie skryptu. Po napotkaniu `OP_NOP`, skrypt jest po prostu kontynuowany bez zmiany stanu stosu lub postępu skryptu. Kluczową różnicą jest zatem ich wpływ na wykonanie: `OP_SUCCESS` gwarantuje pomyślne przejście przez tę część skryptu, podczas gdy `OP_NOP` jest neutralny i nie wpływa ani na stos, ani na przepływ skryptu. Te kody operacyjne są oznaczone przez `OP_SUCCESSN`, gdzie `N` jest liczbą używaną do rozróżnienia `OP_SUCCESS`.