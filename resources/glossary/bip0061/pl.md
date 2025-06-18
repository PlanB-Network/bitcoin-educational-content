---
term: BIP0061
---

Wprowadzono komunikat odrzucenia w protokole komunikacji między węzłami. Celem BIP61 jest dodanie mechanizmu informacji zwrotnej, gdy węzeł otrzyma transakcję lub blok od innego węzła, który uzna za nieważny. Ten komunikat odrzucenia pozwoliłby węzłowi zasygnalizować nadawcy powód, dla którego został odrzucony. Ten rodzaj komunikacji miał na celu poprawę interoperacyjności między różnymi klientami i komunikacji między pełnymi węzłami a klientami SPV. Funkcjonalności wprowadzone przez BIP61 zostały ostatecznie porzucone, począwszy od wersji 0.20.0 Bitcoin Core, ponieważ uznano je za niepotrzebne, ponieważ wiązały się ze zwiększonym zapotrzebowaniem na przepustowość.