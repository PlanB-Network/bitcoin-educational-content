---
name: BitcoinVoucherBot P2P
description: Jak kupować i sprzedawać Bitcoin P2P za pomocą BitcoinVoucherBot
---

![image](assets/cover.webp)



Wciąż słyszymy o BitcoinVoucherBot, bocie Telegram stworzonym do zakupu Bitcoin bez [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) za pośrednictwem przelewu bankowego SEPA. Niestety, od listopada 2025 r. BitcoinVoucherBot w swojej scentralizowanej formie nie jest już dostępny jako usługa bez KYC.



W tym przewodniku przyjrzymy się, jak działa nowa implementacja, która pozwala użytkownikom kupować i sprzedawać Bitcoin bezpośrednio na nowym rynku P2P (Peer-To-Peer), a więc bez KYC. Aby przeciwdziałać nowym ograniczeniom, które coraz bardziej zagrażają cyfrowej wolności i prywatności, deweloperzy stworzyli to rozszerzenie, dając użytkownikom możliwość kupowania i sprzedawania Bitcoin z wysokim stopniem anonimowości za pośrednictwem P2P (Peer-To-Peer). Zobaczmy razem, jak działa ta nowa metoda wymiany.



Aby korzystać z usługi, będziesz musiał dokonywać przelewów za pośrednictwem Lightning Network. Upewnij się więc, że posiadasz wallet, który obsługuje ten protokół i umożliwia korzystanie z "LNURL" lub "Lightning Address" do odbierania i wysyłania środków.



Wśród obsługiwanych portfeli możemy znaleźć:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Custodial z zamianą na Non-Custodial)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Lub dowolny wallet, który ma "Lightning Address" i generuje fakturę Bolt11. portfele, które generate fakturę Bolt12 nie są obecnie obsługiwane. Więcej informacji można znaleźć w definicji [Bolt](https://planb.academy/resources/glossary/bolt).



W tym samouczku, biorąc pod uwagę łatwość natychmiastowego użycia, użyjemy Wallet of Satoshi.



**Uwaga**: Wallet of Satoshi, choć popularny wśród początkujących, jest trybem powierniczym, z ograniczoną kontrolą nad funduszami; używaj go tylko tymczasowo, przenosząc się natychmiast do trybu innego niż powierniczy, aby uzyskać pełną suwerenność. Od października 2025 r. zawiera stabilny tryb self-custodial na całym świecie na iOS/Android (zaktualizuj aplikację), z autonomicznymi kluczami prywatnymi, przełączaniem między trybami, niestandardowymi adresami Lightning i 12-słowną kopią zapasową seed. Pozostaje jednak rozwiązaniem tymczasowym do czasu konsolidacji, preferując dojrzałość bez nadzoru wallet do długoterminowego zarządzania.



Bardzo dobrze! Teraz możemy rozpocząć naszą podróż, która poprowadzi Cię krok po kroku w tworzeniu konta, zarządzaniu zakupami i sprzedażą oraz korzystaniu z obszaru zastrzeżonego.



## Wallet i zapisy



Po pierwsze, jeśli nie masz jeszcze zainstalowanej aplikacji na swoim smartfonie, pobierz Wallet of Satoshi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Jeśli nigdy nie korzystałeś z Wallet of Satoshi i chcesz zrozumieć, jak to działa, sugeruję, abyś postępował zgodnie z tym samouczkiem, abyś mógł go poprawnie aktywować i bezpiecznie wykonać kopię zapasową.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Teraz, gdy twój wallet jest gotowy, możesz zacząć wysyłać niewielką ilość sats. Pamiętaj, że aby ukończyć rejestrację na platformie P2P (Peer-To-Peer), będziesz musiał wysłać 1000 sats jako środek kontrolny: ma to na celu stworzenie bariery przed atakami typu phantom match (oszustwo), uniemożliwiając każdemu zarejestrowanie się bez filtra antyspamowego.



![image](assets/it/02.webp)



Możemy teraz otworzyć platformę P2P (Peer-To-Peer), aby kontynuować rejestrację. Możesz zalogować się z komputerów stacjonarnych lub przeglądarek na smartfonach, za pośrednictwem Telegram BitcoinVoucherBot lub za pośrednictwem linków .onion, aby zapewnić jeszcze wyższy poziom prywatności.



jeśli zdecydujesz się użyć łącza Tor .onion, polecam również "Tor Browser". Jeśli jeszcze go nie znasz, możesz dowiedzieć się więcej na jego temat pod tym linkiem:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Teraz wybierz sposób dotarcia do platformy.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Nastąpi przekierowanie do strony głównej.



naciśnij "Get Starter", aby rozpocząć od razu



![image](assets/it/03.webp)



Na następnym ekranie należy wybrać hasło i wprowadzić je (pole A), a następnie powtórzyć (pole B). Zalecam natychmiastowe zapisanie tego hasła na nośniku kopii zapasowej, który może znajdować się na bezpiecznym urządzeniu cyfrowym, takim jak "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

lub zapisać hasło na nośniku papierowym (**ostrzeżenie**: nie jest to dobre rozwiązanie, ale jest w porządku, jeśli ma być rozwiązaniem tymczasowym).



Zaznacz pole weryfikacji, w którym oświadczasz, że nie jesteś robotem (pole C). Uwaga: Nie włączaj szyfrowania RSA, jeśli nie wiesz dokładnie, co to jest i jak działa. Na tym etapie nie musisz nic robić. Kliknij "Generate Avatar" ("Wygeneruj awatar") (pole D).



![image](assets/it/04.webp)



Teraz musisz zapłacić 1000 sats, aby zakończyć rejestrację.



1. Zaczynając od góry, najpierw zobacz swój losowo wygenerowany i niezwykle ważny "Avatar ID" Zapisz go ostrożnie, tak jak radziłem zrobić to z hasłem.


2. Następnie należy wpisać "Lightning Address" w polu poniżej. Umożliwi to otrzymywanie płatności w przypadku zakupu Bitcoin lub otrzymywanie zwrotów. Jeśli korzystasz z Wallet lub Satoshi, będziesz mógł skopiować swój Address, klikając otrzymaj.


3. Zaznacz pole weryfikacji, w którym oświadczasz, że nie jesteś robotem.


4. Dokonaj płatności w wysokości 1000 sats, aby uzyskać dostęp do strefy zastrzeżonej. Jeśli nie możesz go obramować, kliknij go myszą (na komputerze) lub dotknij go palcem (w przeglądarce / smartfonach Telegram), aby skopiować adres, który należy wkleić do Wallet of Satoshi i dokończyć płatność faktury.



![image](assets/it/05.webp)



To jest twój LNURL Address.



![image](assets/it/06.webp)



Gratulacje!!! Utworzyłeś swój awatar na stałe i możesz zobaczyć podsumowanie tutaj. Jeszcze raz zalecam uważne zapisanie zarówno awatara, jak i hasła, jak sugerowałem wcześniej.



Kliknij `Zapisałem swoje dane uwierzytelniające, kontynuuj` (przetłumaczone jako: "Zapisałem swoje dane uwierzytelniające, kontynuuj")



![image](assets/it/07.webp)



Znajdujesz się teraz w samym sercu platformy, gdzie możesz przeglądać wszystkie mecze handlowe wraz z ich szczegółami. Aby uzyskać wyraźniejszy widok, poniżej zobaczysz obrazy nieodłącznie związane z witryną z komputerów stacjonarnych.





- "Typ" ("Type") określa, czy jest to sprzedaż ("sell"), czy zakup ("buy")
- "Ilość" ("Amount"): wskazuje, ile sats użytkownik sprzedaje, jeśli dopasowanie jest typu "Sprzedaj" ("Sell"), lub ile Bitcoin użytkownik chce kupić, jeśli dopasowanie jest typu "Kup" ("Buy").
- "Cena BTC z marżą" ("BTC Price with Margin"): pokazuje cenę uwzględniającą marżę zastosowaną powyżej zaznaczonej wartości.
- "Marża" ("Margin") to wartość procentowa, która jest stosowana do ceny rynkowej, ze znakiem minus (-) otrzymujesz zniżkę od ceny rynkowej, ze znakiem plus (+) premia jest stosowana do ceny rynkowej.
- "Metoda" ("Method") wskazuje, jaką metodę płatności preferuje użytkownik.
- "Twórca" to unikalny awatar używany przez użytkownika na platformie.
- "Rep" (Reputacja) Poziom reputacji użytkownika waha się od -5 niewiarygodny do +5 wyjątkowo wiarygodny.
- "Status" ("Status"): wskazuje status meczu. Na przykładowym zrzucie ekranu wszystkie mecze mają status "Open" ("Otwarte").
- "Expiration" ("Wygaśnięcie"): pokazuje, ile czasu pozostało do wygaśnięcia meczu i jego anulowania, jeśli nie został wybrany przez nikogo.



![image](assets/it/08.webp)



W prawym górnym rogu kliknij swój awatar, aby uzyskać dostęp do swojego profilu.



![image](assets/it/09.webp)



Tutaj możesz zobaczyć nazwę swojego awatara, identyfikator użytkownika, datę utworzenia i reputację, która będzie pozytywnie lub negatywnie odzwierciedlać twoje zachowanie w negocjacjach.



![image](assets/it/10.webp)



W sekcji Ustawienia można wyświetlić swój "Lightning Address" wprowadzony podczas rejestracji i zmienić go w razie potrzeby. Masz również możliwość utworzenia klucza publicznego, który, jak wspomniano, należy skonfigurować tylko wtedy, gdy posiadasz odpowiednie umiejętności. Służy on do szyfrowania wiadomości, które będziesz wymieniać ze swoim odpowiednikiem bezpośrednio z komputera.



Funkcja powiadomień Telegram jest wysoce zalecana. Po jej aktywacji pojawi się kod QR, który należy umieścić w ramce aplikacji Telegram: w ten sposób będziesz otrzymywać powiadomienia w czasie rzeczywistym o wszystkich działaniach związanych z Twoimi meczami, bezpośrednio na czacie bota w Telegram.



![image](assets/it/11.webp)



Na końcu znajduje się sekcja poleconych, z zarobkami wygenerowanymi przez zaproszonych użytkowników. Z tego miejsca możesz użyć przycisku, aby udostępnić swój link lub kod QR, a nieco dalej wyświetlić listę dopasowań, aby śledzić swoją reputację wraz z odpowiednim wynikiem.



![image](assets/it/12.webp)



## Utwórz zamówienie na zakup Bitcoin



Wejdź do Marketplace: na głównym pasku nawigacyjnym kliknij symbol koszyka "Marketplace" ("Marketplace"), aby otworzyć księgę zamówień. Następnie rozpocznij nowe zamówienie: naciśnij przycisk "New Order" ("Nowe zamówienie"), aby rozpocząć proces.



![image](assets/it/13.webp)





- Ustaw szczegóły zamówienia:
- Wybierz opcję "Kup Bitcoin" ("Buy Bitcoin").
- Wprowadź żądaną ilość sats.
- Zdefiniuj marżę cenową (od -20% do +20% od wartości rynkowej).
- Wybierz metodę płatności (Instant SEPA itp.).
- Wskazuje preferowaną walutę.
- Potwierdź zamówienie: kliknij "Utwórz zamówienie" ("Confirm Order"), aby przejść do etapu składania zamówienia.



![image](assets/it/14.webp)



Wymagany depozyt: do aktywacji zamówienia wymagany jest depozyt w wysokości 10% całkowitej kwoty plus opłata za usługę.




- Wpłata depozytu: po utworzeniu zamówienia system automatycznie generuje fakturę Lightning. Depozyt ma charakter tymczasowy i jest zwracany po zakończeniu zamówienia.
- Główne cechy:
- Kaucja: 10% wartości zamówienia.
- Opłata za usługę: koszt korzystania z platformy.
- Limit czasu: Masz 5 minut na dokonanie płatności, w przeciwnym razie transakcja wygaśnie.



![image](assets/it/15.webp)



Po pomyślnym dokonaniu płatności, zlecenie pojawi się w księdze i będzie widoczne dla wszystkich użytkowników, którzy mogą je wybrać i zaakceptować. Aby utworzyć zlecenie sprzedaży, wystarczy kliknąć "Sell Bitcoin" ("Sprzedaj Bitcoin"), wprowadzić ilość satoshi, którą chcesz sprzedać, ustawić marżę, wybrać metodę płatności i walutę, a następnie dokonać wpłaty 10% jako depozytu zabezpieczającego. Po zakończeniu dopasowanie będzie widoczne na liście.



![image](assets/it/16.webp)



## Jak przyjąć zamówienie



1. Sprzedawcy mogą zobaczyć listę wszystkich dostępnych zamówień w książce.


2. Sprawdź szczegóły: każde zamówienie zawiera informacje takie jak:




  - Ilość Bitcoin,
  - Marża od ceny,
  - Metoda płatności,
  - Reputacja użytkownika.



![image](assets/it/17.webp)



3. Kliknij zamówienie, aby otworzyć pełny arkusz ze wszystkimi informacjami.


4. Naciśnij "Sell Bitcoin" ("Sprzedaj Bitcoin"), aby zaakceptować propozycję.



![image](assets/it/18.webp)



## Kaucja wymagana przez sprzedawcę



Po zaakceptowaniu zamówienia system generuje fakturę do zapłaty. Wpłata obejmuje:



- Całkowita kwota zamówienia,



- komisja serwisowa.



Wpłaty depozytu należy dokonać w określonym terminie, w przeciwnym razie transakcja nie zostanie potwierdzona.



![image](assets/it/19.webp)



## Wysyłanie instrukcji płatności



Po dokonaniu wpłaty transakcja pojawi się w osobistym panelu sprzedawcy, który musi podać szczegóły kupującemu, aby sfinalizować płatność w walucie fiducjarnej.



1. Sprzedawca wyświetla aktywną transakcję w swoim panelu.


2. Kliknij "Prześlij instrukcje dotyczące płatności"


3. Wprowadź wszystkie niezbędne informacje dotyczące płatności fiat (IBAN, odbiorca, adres, powód płatności itp.).


4. Kliknij "Send Message" ("Wyślij wiadomość"), aby przesłać dane do kupującego.



![image](assets/it/20.webp)



## Procedura płatności



Kupujący otrzymuje na czacie platformy wiadomość ze wszystkimi danymi niezbędnymi do dokonania płatności w walucie fiducjarnej:




- Dane banku: IBAN z nazwą i adresem posiadacza rachunku sprzedawcy.
- Dokładna kwota: dokładna kwota fiat, która ma zostać przelana.
- Przyczyna/opis: tekst, który ma być zawarty w transakcji.
- Termin: termin, w którym należy dokonać płatności.



Przelew odbywa się poza systemem P2P i musi być wykonany za pośrednictwem instytucji bankowej.



⚠️ **Important note:** potwierdzenie na platformie powinno być dokonane dopiero po faktycznym zorganizowaniu przelewu lub płatności fiat za pośrednictwem banku.



![image](assets/it/21.webp)



## Potwierdzenie płatności fiat



Ten krok jest kluczowy dla kupującego i powinien być wykonany dopiero po sprawdzeniu, czy płatność została faktycznie wysłana.



1. Otrzymanie danych: kupujący otrzymał instrukcje dotyczące płatności od sprzedającego.


2. Realizacja płatności: przelew fiat jest realizowany z konta bankowego.


3. Weryfikacja: sprawdzenie, czy operacja została wykonana poprawnie.


4. Potwierdź na platformie: kliknij "Potwierdź płatność fiat" ("Confirm fiat payment") na stronie transakcji.


Przycisk "Potwierdź płatność fiat" pojawia się w sekcji transakcji i powinien być używany tylko po sprawdzeniu, czy płatność została rzeczywiście wysłana.



![image](assets/it/22.webp)



Ostatnim krokiem w tym procesie jest potwierdzenie przez sprzedającego otrzymania płatności fiat, po czym satelity są wydawane kupującemu.



![image](assets/it/23.webp)



## Wnioski



Mamy nadzieję, że ten samouczek pomoże ci skorzystać z nowej metody handlu Bitcoinami lub nawet po prostu je kupić, zarówno dla własnego magazynu wartości, jak i w celu ożywienia codziennych płatności. Wciąż jednak pozostaje furtką do zbadania, aby poradzić sobie z tym, co wkrótce wydarzy się w naszym cyfrowym świecie.



Pętla prowadzona przez organy, które nas kontrolują, zaciska się, dając początek coraz bardziej kontrolowanemu Internetowi. Kupując P2P, zachowujesz całkowitą anonimowość, nie pozostawiając śladów i nie narażając się na reperkusje ze strony osób trzecich.