---
term: BIP0012
---

Propozycja Gavina Andresena mająca na celu zwiększenie elastyczności i prywatności skryptów transakcji Bitcoin. Ten BIP sugeruje wdrożenie nowego kodu operacyjnego skryptu o nazwie `OP_EVAL`, który pozwala na ocenę skryptu zawartego w danych `scriptSig` podczas procesu walidacji transakcji. Główną modyfikacją BIP12 jest umożliwienie włączenia jednego skryptu wewnątrz innego skryptu. Technika ta umożliwia tworzenie bardziej złożonych warunków, które można zweryfikować w momencie wydawania, bez konieczności ujawniania ich użytkownikom wysyłającym bitcoiny do używanego Address. BIP12 został później zastąpiony bezpieczniejszymi propozycjami, w szczególności BIP16 (P2SH), który oferuje inną metodę osiągnięcia tych samych celów co `OP_EVAL`.