---
name: Electrum OP_RETURN
description: Zarejestruj wiadomość na Blockchain Bitcoin z Electrum
---

![cover](assets/cover.webp)




Ten samouczek krok po kroku pokazuje, jak napisać wiadomość na Blockchain Bitcoin przy użyciu Wallet Electrum. Ta operacja wykorzystuje instrukcję OP_RETURN do wstawienia tekstu do transakcji, publicznie widocznej na Blockchain. Wykonaj te proste kroki, aby pomyślnie dokonać rejestracji.



---
## Wymagania wstępne





- Komputer (Windows, macOS lub Linux).
- Połączenie internetowe.
- Kilka satoshi (Sats) lub bitcoinów (BTC) w Wallet na pokrycie kwoty transakcji i opłat.
- Konwerter tekstu na szesnastkowy (np. strona internetowa) lub dedykowane narzędzie, takie jak [ten generator skryptów OP_RETURN] (https://resources.davidcoen.it/opreturnelectrum/).



---

## Krok 1: Pobierz i zainstaluj Electrum



![image](assets/fr/01.webp)



1. Odwiedź oficjalną stronę Electrum: [electrum.org](https://electrum.org/).


2. Pobierz wersję odpowiadającą Twojemu systemowi operacyjnemu (Windows, macOS, Linux).


3. Zainstaluj Electrum zgodnie z instrukcjami instalatora.


4. Sprawdzenie integralności pobranego pliku (opcjonalne, ale zalecane ze względów bezpieczeństwa) poprzez porównanie podpisu pliku lub Hash.



→ Więcej szczegółów w samouczku Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Krok 2: Utwórz lub zaimportuj Wallet



1. Uruchom Electrum.


2. Wybierz Utwórz nowy Wallet lub Przywróć istniejący Wallet, jeśli masz już frazę seed (frazę odzyskiwania).


3. Postępuj zgodnie z instrukcjami, aby skonfigurować Wallet:




 - W przypadku nowego Wallet zanotuj swoje zdanie seed i przechowuj je w bezpiecznym miejscu (papier, sejf itp.).
 - W przypadku istniejącego Wallet wprowadź frazę seed, aby go przywrócić.


4. Ustaw hasło, aby zabezpieczyć Wallet.



→ Więcej szczegółów w samouczku Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Krok 3: Sprawdź dostępne środki



Upewnij się, że twój Wallet zawiera wystarczającą ilość bitcoinów (BTC) lub satoshis (Sats), aby :




- Kwota transakcji (na przykład 0,00001 BTC lub 1000 Sats).
- Opłaty transakcyjne, które różnią się w zależności od wielkości sieci (zazwyczaj kilka tysięcy Sats).



Sprawdź saldo w Electrum, aby sprawdzić swoje środki.



![image](assets/fr/02.webp)



W razie potrzeby przelej BTC lub Sats, aby zasilić Wallet. Aby to zrobić, przejdź do zakładki "Odbiór" i kliknij "Utwórz żądanie" :



![image](assets/fr/03.webp)



Spowoduje to wyświetlenie odbioru Address:



![image](assets/fr/04.webp)



→ Więcej szczegółów w samouczku Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Krok 4: Przygotowanie wiadomości do wpisania



Wybierz wiadomość, którą chcesz wprowadzić (np. `Dzięki Satoshi`). Uwaga: Wiadomości OP_RETURN są ograniczone do 80 bajtów, tj. około 80 znaków ASCII.



*Zastanów się przez chwilę: to, co piszesz na Blockchain Bitcoin jest wieczne i dostępne dla wszystkich, więc :*




- pozostawić piękny wyraz naszego człowieczeństwa,*
- unikaj wprowadzania treści, których możesz żałować*



*Przestrzeń Blockchain i twoje bitcoiny są cenne, używaj ich mądrze i świadomie*



Konwersja wiadomości do systemu szesnastkowego:




- Można skorzystać z [narzędzia online](https://www.rapidtables.com/convert/number/ascii-to-hex.html), ale należy uważać, aby nie przetwarzać tam danych szczególnie chronionych (chociaż zasadniczo informacje przeznaczone do publikacji w Blockchain Bitcoin za pośrednictwem OP_RETURN nie stanowią żadnych kwestii związanych z poufnością);
- Aby zapewnić większą poufność, konwersję można przeprowadzić lokalnie przy użyciu niewielkiej aplikacji Python :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Przykład: `Dzięki Satoshi` w ASCII daje `5468616e6b73205361746f736869` w systemie szesnastkowym.



Przygotuj skrypt transakcji. Oto przykład oczekiwanego formatu:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



który składa się z :





- Miejsce docelowe Address**: Ważny Bitcoin Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Może to być Twój własny Address, jeśli chcesz zwrócić przelane środki do siebie;
- Przelana kwota**: kwota transakcji, tutaj `0,00001` BTC. **Uwaga**: ponieważ jednostką używaną w Electrum jest BTC, kwota wskazana w skrypcie transakcji musi być również wyrażona w BTC, a nie w Sats;
- Skrypt OP_RETURN**: Wiadomość przekonwertowana na szesnastkowy poprzedzona script(`OP_RETURN <messsage>), 0`. Tutaj, `5468616e6b73205361746f736869` dla wiadomości w systemie szesnastkowym.



⚠️ **Uwaga**: Bardzo ważne jest wskazanie `0` po OP_RETURN, ponieważ ten kod operacyjny oznacza skrypt jako nieprawidłowy, co sprawia, że dane wyjściowe są trwale niewydajne. Węzły sieciowe usuną to wyjście ze swojego zestawu UTXO. Jeśli wprowadzisz wartość inną niż `0`, zostanie ona bezpowrotnie utracona: twoje bitcoiny zostaną uznane za spalone. Powinieneś zatem zawsze wpisywać `0` z OP_RETURN, aby zarejestrować pożądane dane, ale bez kojarzenia z nimi środków, które zostałyby utracone.



Wskazówka: Użyj narzędzia [Generator OP_RETURN] (https://resources.davidcoen.it/opreturnelectrum/), aby automatycznie utworzyć skrypt generate. Nawet jeśli to narzędzie sugeruje wprowadzenie kwoty w BTC, zachowaj jednostkę skonfigurowaną w Electrum.



![image](assets/fr/05.webp)



Aby zmienić jednostkę używaną przez Electrum, na pasku menu znajdź "Preferencje", a następnie w zakładce "Jednostki" wybierz BTC / mBTC / bity lub Sats :



![image](assets/fr/06.webp)




---

## Krok 5: Wysłanie transakcji



W Electrum przejdź do zakładki Wyślij.



![image](assets/fr/07.webp)



W polu "Zapłać do" wklej przygotowany skrypt (na przykład ten powyżej).



![image](assets/fr/08.webp)



Pole "Zapłać do" powinno zostać wyświetlone w Green, a kwota transakcji powinna pojawić się w wierszu poniżej.



Sprawdź kwotę i jej jednostkę w polu Kwota.



Kliknij "Zapłać..." i dostosuj opłaty transakcyjne do kwoty, którą chcesz zapłacić i szybkości, z jaką chcesz, aby transakcja została przetworzona przez Miner i zintegrowana z blokiem.



![image](assets/fr/09.webp)



Kliknij OK i potwierdź transakcję hasłem. Pojawi się okno potwierdzenia.




---

## Krok 6: Weryfikacja rejestracji



Po potwierdzeniu transakcji (może to potrwać kilka minut) przejdź do zakładki "Historia".



![image](assets/fr/10.webp)



Kliknij transakcję prawym przyciskiem myszy i wybierz opcję "Wyświetl w Eksploratorze", aby zobaczyć szczegóły.



Alternatywnie, skopiuj docelowy Address (na przykład `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) i wyświetl go w eksploratorze Blockchain, takim jak [Mempool.space](https://Mempool.space/) lub [blockstream.info](https://blockstream.info/).



Poszukaj pola OP_RETURN w szczegółach transakcji, aby zobaczyć swoją wiadomość.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Wskazówki i najlepsze praktyki





- Przetestuj niewielką kwotę: Zacznij od małej transakcji (np. Sats 1000), aby uniknąć kosztownych błędów.
- Upewnij się, że wyjście zawierające OP_RETURN jest równe zero, w przeciwnym razie twoje bitcoiny zostaną trwale utracone.
- Sprawdź jednostkę: Upewnij się, że wprowadzona kwota odpowiada jednostce wyświetlanej w Electrum (BTC, mBTC lub Sats).
- Opłata za transakcję: Jeśli sieć jest przeciążona, zwiększ opłatę za szybsze potwierdzenie.
- Krótka wiadomość: Wpisy OP_RETURN są ograniczone do 80 bajtów. Należy odpowiednio zaplanować wiadomość.



---

## Przydatne zasoby





- Pobierz Electrum: [electrum.org](https://electrum.org/)
- Generator skryptów OP_RETURN: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Explorers: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)