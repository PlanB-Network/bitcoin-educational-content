---
name: Lipa
description: Konfiguracja i korzystanie z Lipa lightning mobile Wallet
---
![cover](assets/cover.webp)


Bitcoin Lightning Wallet to aplikacja mobilna, która umożliwia natychmiastowe, tanie transakcje na Bitcoin Lightning Network. W przeciwieństwie do transakcji na głównym Blockchain (On-Chain), płatności Lightning są niemal natychmiastowe i wymagają minimalnych opłat, dzięki czemu są szczególnie odpowiednie dla małych, codziennych płatności.


Portfele Lightning, podobnie jak wszystkie portfele mobilne, są uważane za portfele "Hot", ponieważ są połączone z Internetem. Dlatego też są one przeznaczone głównie do zarządzania niewielkimi kwotami pieniędzy na codzienne wydatki. W przypadku większych kwot lepiej jest korzystać z bezpieczniejszych rozwiązań do przechowywania, takich jak portfele sprzętowe.


Jeśli chcesz dowiedzieć się więcej o Lightning Network i zrozumieć, jak działa on od strony technicznej, polecam ci udział w tym kursie:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

W tym samouczku przyjrzymy się **Lipa**, prostemu i skutecznemu Lightning Wallet opracowanemu w Szwajcarii.


## Przedstawiamy Lipę


Lipa to bezobsługowy Lightning Wallet wyróżniający się prostotą użytkowania i nieskomplikowanym Interface. Opracowany przez szwajcarski zespół, kładzie nacisk na poufność i łatwość obsługi dla początkujących.


Kluczowe funkcje obejmują:




- Intuicyjny użytkownik Interface
- Autonomiczne zarządzanie kanałem Lightning
- Obsługa protokołu LNURL
- Możliwość zakupu bitcoinów bezpośrednio w aplikacji


## Instalacja i konfiguracja aplikacji Lipa


Pierwszym krokiem jest pobranie aplikacji Lipa. Na razie jest ona dostępna tylko na iOS :




- [Dla Apple](https://apps.apple.com/app/lipa-Bitcoin-lightning/id1602180066)


Wersja na Androida jest obecnie w fazie rozwoju i będzie dostępna wkrótce.


![Installation de Lipa](assets/fr/01.webp)


Po uruchomieniu aplikacji pojawi się ekran główny, który oferuje dwie opcje:




- Utwórz nowy Wallet
- Przywracanie istniejącego Wallet z kopii zapasowej


Po wybraniu opcji aplikacja wyświetli monit o włączenie powiadomień. Ten krok jest ważny, ponieważ powiadomienia są niezbędne dla :




- Otrzymywanie powiadomień o otrzymanych płatnościach, nawet gdy aplikacja jest zamknięta
- Bądź informowany o krokach związanych z zakupem Bitcoin za pośrednictwem ich zintegrowanego rozwiązania


Następnie aplikacja prezentuje swoje główne funkcje poprzez serię ekranów wprowadzających:




- Bezproblemowy odbiór płatności**: Użytkownicy mogą otrzymywać płatności Bitcoin nawet po zamknięciu aplikacji, co gwarantuje niezawodność i wygodę.
- Adresy Lightning bez nadzoru**: Lipa obsługuje teraz niepowiernicze adresy Lightning, zwiększając prywatność i bezpieczeństwo, dając użytkownikom pełną kontrolę nad ich bitcoinami.
- Kontrola nad danymi analitycznymi** : Mając na uwadze przejrzystość i poufność, użytkownicy mogą przeglądać rodzaje gromadzonych danych i wybierać preferencje dotyczące ich udostępniania.
- Wysyłanie przez numer telefonu**: Nie potrzebujesz skomplikowanych adresów - po prostu wybierz kontakt, wprowadź kwotę i wyślij bitcoiny bezpośrednio na jego numer telefonu.


Aplikacja korzysta również z ciągłych ulepszeń w zakresie stabilności, bezpieczeństwa i niezawodności, aby zagwarantować optymalne wrażenia użytkownika.


## Nawigacja po aplikacji


Interface Lipa jest zorganizowany wokół 4 głównych zakładek dostępnych za pośrednictwem paska nawigacyjnego u dołu ekranu:


![Navigation principale](assets/fr/02.webp)




- Strona główna**: Wyświetla bieżące saldo i historię transakcji
- Skaner**: Umożliwia skanowanie kodów QR w celu dokonywania płatności
- Mapa**: Wyświetla interaktywną mapę firm akceptujących Bitcoin w Twojej okolicy
- Ustawienia**: Dostęp do ustawień aplikacji, kopii zapasowych i preferencji


Dostęp do dodatkowego menu można uzyskać, przeciągając ekran główny w dół:


![Menu supplémentaire](assets/fr/03.webp)


Ten gest ujawnia dodatkowe funkcje, takie jak :




- Kupowanie bitcoinów
- Złoże On-Chain Bitcoin
- Tworzenie faktur Lightning w celu otrzymywania bitcoinów
- Płatność Lightning Invoice


## Zapisz swój Wallet


Aby wykonać kopię zapasową Wallet, przejdź do zakładki "Ustawienia" i wybierz "Fraza odzyskiwania". Lipa używa frazy odzyskiwania, którą należy dokładnie zapisać na nośniku fizycznym (papier, metal). Fraza ta jest jedynym sposobem na odzyskanie środków w przypadku zgubienia lub kradzieży telefonu. Aby zweryfikować kopię zapasową, aplikacja poprosi o potwierdzenie 3 losowych słów z frazy.


![Backup](assets/fr/04.webp)


Aby uzyskać więcej informacji na temat prawidłowego tworzenia kopii zapasowych i zarządzania frazą odzyskiwania, zdecydowanie polecam zapoznanie się z tym innym samouczkiem, zwłaszcza jeśli jesteś początkującym:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Odbieranie bitcoinów


Aby otrzymywać bitcoiny, dostępne są dwie opcje. Aby uzyskać dostęp do tych opcji, wróć do ekranu głównego i przeciągnij ekran w dół. Następnie możesz wybrać :




- Wybierz "Transfer BTC", aby otrzymać bitcoiny On-Chain. Następnie wystarczy zeskanować kod QR za pomocą Wallet i sfinalizować transakcję.
- Wybierz "Żądanie", aby otrzymać za pośrednictwem Lightning Network i wprowadź kwotę, którą chcesz otrzymać.


W obu przypadkach będziesz musiał uiścić opłatę w wysokości 0,4% kwoty lub około 2500 Sats, jeśli aplikacja musi otworzyć nowy kanał płatności (co nieuchronnie będzie miało miejsce w przypadku pierwszej płatności).


![Recevoir des bitcoins on chain](assets/fr/05.webp)


![Recevoir des bitcoins lightning](assets/fr/06.webp)


## Wysyłanie bitcoinów


Aby wysłać bitcoiny, przejdź do ekranu głównego, przeciągnij ekran w dół i wybierz "Zapłać". Następnie wystarczy wybrać :




- wprowadź piorun LNURL Address
- zeskanuj piorunujący kod QR, aby dokonać płatności.


Możesz także przejść do drugiej zakładki w dolnej części ekranu, aby bezpośrednio zeskanować kod QR.


![Envoi de bitcoins](assets/fr/07.webp)


## Kup bitcoiny


Lipa oferuje możliwość zakupu bitcoinów bezpośrednio w aplikacji za opłatą w wysokości 1,5%. Aby dokonać zakupu, przejdź do ekranu głównego i przeciągnij w dół, aby wyświetlić menu. Następnie wybierz "Kup BTC". Trzy ekrany wprowadzające przeprowadzą użytkownika przez proces zakupu.


![Menu d'achat](assets/fr/08.webp)


Następnie wprowadź dane bankowe konta, którego będziesz używać do dokonania zakupu. Wybierz walutę i wprowadź swój adres e-mail Address.


Po ekranie ładowania znajdziesz numer referencyjny, który należy uwzględnić w przelewie, który zamierzasz wykonać, a także dane bankowe Exchange.


![Sélection du montant](assets/fr/09.webp)


Wszystko, co musisz zrobić, to użyć swojego banku, aby przelać żądaną kwotę, skonfigurować przelew, wskazując wcześniej pobrany RIB i wskazać numer referencyjny w momencie transakcji, aby Lipa mogła powiązać ten ruch bankowy z Twoim Lipa Wallet.


![Confirmation d'achat](assets/fr/10.webp)


## Zalety i wady


### Korzyści




- Intuicyjny Interface
- Prawidłowe opłaty za usługi
- Bez nadzoru
- Zintegrowane rozwiązanie zakupowe Bitcoin
- Integracja z BTCmap
- Obsługa NFC


### Wady




- Nie jest możliwe wysyłanie bitcoinów on chain
- Nieco dłuższa niż średnia płatność


Lipa to doskonały wybór na początek korzystania z Lightning Network, szczególnie odpowiedni dla użytkowników poszukujących prostego rozwiązania do codziennych płatności. Łatwość obsługi i przejrzystość Interface sprawiają, że jest to idealny Wallet dla początkujących, oferując jednocześnie podstawowe funkcje do codziennego użytku Lightning.


## Zasoby




- [Oficjalna strona Lipy](https://lipa.swiss/)
- [Wsparcie Lipa](https://getlipa.atlassian.net/servicedesk/customer/portal/1)