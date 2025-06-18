---
term: BIP0072
---

Uzupełnia BIP70 i BIP71 poprzez zdefiniowanie rozszerzenia Bitcoin URI (BIP21) o dodatkowy parametr `r`. Ten parametr umożliwia dołączenie linku do bezpiecznego żądania płatności podpisanego certyfikatem SSL sprzedawcy. Gdy klient kliknie ten rozszerzony URI, jego Wallet skontaktuje się z serwerem sprzedawcy, aby zażądać szczegółów płatności. Szczegóły te są automatycznie wypełniane w transakcji Wallet Interface, a klient może zostać poinformowany, że płaci właścicielowi domeny odpowiadającej certyfikatowi podpisującemu (na przykład "pandul.fr"). Ponieważ to rozszerzenie jest dołączone do BIP70, nigdy nie zostało powszechnie przyjęte.