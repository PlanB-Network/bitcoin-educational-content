---
term: BIP0031
---

Propozycja mająca na celu poprawę mechanizmów zarządzania siecią przez węzły Bitcoin. Przed BIP31 węzły Bitcoin nie miały bezpośredniego sposobu na sprawdzenie, czy ich peery są nadal połączone, działają i nie są przeciążone. BIP31 wprowadził użycie wiadomości `pong` w odpowiedzi na wiadomość `ping`, która pozwala na aktywne sprawdzanie łączności między węzłami.