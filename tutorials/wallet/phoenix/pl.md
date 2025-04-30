---
name: Phoenix
description: Instalacja i korzystanie z Phoenix Wallet
---
![cover](assets/cover.webp)


Phoenix to samodzielny portfel Lightning Wallet i węzeł opracowany przez ACINQ, francuską firmę specjalizującą się w rozwiązaniach programowych opartych na Lightning. W przeciwieństwie do portfeli Lightning typu custodial, takich jak Wallet lub Satoshi, w których bitcoiny są przechowywane przez stronę trzecią, Phoenix umożliwia użytkownikom zachowanie pełnej kontroli nad ich kluczami prywatnymi.


Phoenix działa jako prawdziwy węzeł Lightning osadzony w telefonie, automatycznie otwierając kanał z węzłem Lightning ACINQ. Aplikacja oparta jest na Lightning-KMP, wieloplatformowej implementacji Lightning Network w Kotlinie, zoptymalizowanej pod kątem portfeli mobilnych. W przeciwieństwie do innych rozwiązań węzła Lightning, Phoenix znacznie upraszcza zarządzanie. Użytkownik nie musi obsługiwać otwierania i zamykania kanałów, uruchamiać węzła Bitcoin ani zarządzać płynnością na Lightning Network. Phoenix zajmuje się wszystkimi tymi operacjami technicznymi w tle.


Aplikacja ta łączy w sobie łatwość obsługi i wygodę mobilnych portfeli Lightning z bezpieczeństwem i suwerennością prawdziwego osobistego węzła Lightning. Phoenix umożliwia bezpieczne, wydajne i autonomiczne korzystanie z Lightning Network, jednocześnie ciesząc się płynnym, intuicyjnym doświadczeniem użytkownika.


W zamian obowiązują pewne opłaty:




- Wysyłanie za pomocą Lightning kosztuje 0,4% kwoty plus 4 Sats ;
- Jeśli do odbioru za pośrednictwem usługi Lightning potrzebna jest gotówka, naliczana jest opłata w wysokości 1% kwoty;
- Otwarcie każdego kanału kosztuje 1000 Sats.


Moim zdaniem Phoenix stanowi doskonałe rozwiązanie pośrednie między portfelami Lightning a ręcznym zarządzaniem węzłem Lightning. Aplikacja ta jest odpowiednia zarówno dla początkujących, jak i zaawansowanych użytkowników, którzy wolą nie zajmować się szczegółami zarządzania własnym LND lub Core Lightning. Dowiedzmy się, jak z niej korzystać!


![Image](assets/fr/01.webp)


## Zainstaluj aplikację


Przejdź do sklepu z aplikacjami i zainstaluj Phoenix :




- W sklepie [Google Play Store] (https://play.google.com/store/apps/details?id=fr.acinq.phoenix.Mainnet);
- W [App Store](https://apps.apple.com/fr/app/phoenix-Wallet/id1544097028?l=en-GB).


![Image](assets/fr/02.webp)


Aplikację można również zainstalować [za pomocą pliku apk z repozytorium GitHub] (https://github.com/ACINQ/phoenix/releases).


![Image](assets/fr/03.webp)


## Tworzenie portfolio


Po uruchomieniu aplikacji kliknij przycisk "*Next*", aby pominąć prezentację, a następnie "*Start*".


![Image](assets/fr/04.webp)


Wybierz "*Twórz nowy Wallet*".


![Image](assets/fr/05.webp)


I to wszystko, twój Lightning Wallet i węzeł są teraz utworzone.


![Image](assets/fr/06.webp)


## Zapisz frazę Mnemonic


Zanim zaczniemy, musimy zapisać naszą 12-wyrazową frazę Mnemonic. Fraza ta daje pełny, nieograniczony dostęp do wszystkich bitcoinów. Każdy, kto posiada tę frazę, może ukraść twoje środki, nawet bez fizycznego dostępu do twojego telefonu.


12-wyrazowa fraza przywraca dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia telefonu. Dlatego bardzo ważne jest, aby zapisać go ostrożnie i przechowywać w bezpiecznym miejscu.


Można go zapisać na papierze lub, dla większego bezpieczeństwa, wygrawerować na stali nierdzewnej w celu ochrony przed pożarem, powodzią lub zawaleniem. Wybór nośnika dla Mnemonic będzie zależeć od strategii bezpieczeństwa, ale jeśli używasz Phoenix jako portfela wydatków zawierającego umiarkowane kwoty, papier powinien być wystarczający.


Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Kliknij komunikat wyświetlany w górnej części Interface "*Zapisz Wallet...*".


![Image](assets/fr/07.webp)


Następnie kliknij "*Zapisz mój Wallet*".


![Image](assets/fr/08.webp)


Następnie kliknij "*Wyświetl mój klucz*" i zapisz swoją frazę Mnemonic na fizycznym nośniku.


![Image](assets/fr/09.webp)


Sprawdź dwa pola u dołu Interface, aby potwierdzić, że tworzenie kopii zapasowej zostało pomyślnie zakończone.


![Image](assets/fr/10.webp)


## Konfiguracja aplikacji


Przed dokonaniem pierwszych transakcji można dostosować ustawienia, klikając ikonę koła zębatego w lewym dolnym rogu Interface.


![Image](assets/fr/11.webp)


W menu "*Display*" można wybrać motyw aplikacji, nominał używany w Bitcoin oraz lokalną walutę fiducjarną.


![Image](assets/fr/12.webp)


W sekcji "*Opcje płatności*" znajdziesz różne zaawansowane ustawienia płatności Lightning. Możesz zachować ustawienia domyślne.


![Image](assets/fr/13.webp)


W sekcji "*Zarządzanie kanałami*" ustaw maksymalną opłatę, jaką jesteś gotów zapłacić za otwarcie kanału Lightning.


![Image](assets/fr/14.webp)


W menu "*Kontrola dostępu*" zdecydowanie zalecam aktywowanie systemu uwierzytelniania w celu zabezpieczenia dostępu do aplikacji w telefonie. Uniemożliwi to każdemu, kto ma dostęp do odblokowanego telefonu, uzyskanie dostępu do Phoenix i kradzież bitcoinów.


![Image](assets/fr/15.webp)


W menu "*Serwer Electrum*", jeśli posiadasz serwer Electrs, możesz go podłączyć, aby nadawać swoje transakcje.


![Image](assets/fr/16.webp)


Aby zwiększyć poufność połączeń, włącz połączenia przez Tor w menu "*Tor*". Chociaż korzystanie z Tor może nieco spowolnić płatności i wymaga, aby aplikacja Phoenix była otwarta na pierwszym planie podczas odbierania, znacznie zwiększa to prywatność.


![Image](assets/fr/17.webp)


## Odbiór bitcoinów On-Chain


Przy pierwszym użyciu masz możliwość doładowania swojego Phoenix Wallet środkami On-Chain. Możesz również dokonać tej pierwszej wpłaty bezpośrednio z Lightning (patrz następna sekcja), ale w obu przypadkach będą obowiązywać dodatkowe opłaty za otwarcie pierwszego kanału.


Kliknij przycisk "*Odbierz*".


![Image](assets/fr/18.webp)


Przesuń kod QR w prawo, aby wyświetlić Bitcoin odbierający Address. Wyślij kwotę, którą chcesz zdeponować w Phoenix.


![Image](assets/fr/19.webp)


Kwota otrzymana przez On-Chain pojawi się najpierw jako oczekująca w saldzie portfela. Miną 3 potwierdzenia, zanim środki będą dostępne do wykorzystania.


![Image](assets/fr/20.webp)


Po otrzymaniu środków Phoenix automatycznie otworzy dla Ciebie kanał Lightning. Możesz teraz wysyłać i odbierać bitcoiny za pośrednictwem Lightning Network.


![Image](assets/fr/21.webp)


## Odbieranie bitcoinów za pośrednictwem usługi Lightning


Aby odebrać Sats za pośrednictwem Lightning Network, kliknij przycisk "*Odbierz*".


![Image](assets/fr/22.webp)


Phoenix generuje piorun Invoice. Możesz go zeskanować lub wysłać do osoby, która chce przekazać ci Sats.


![Image](assets/fr/23.webp)


Klikając przycisk "*Edytuj*", można dodać opis, który będzie widoczny dla płatnika na Invoice, oraz określić konkretną kwotę, którą płatnik musi wysłać.


![Image](assets/fr/24.webp)


Wspomniane powyżej klasyczne faktury można wykorzystać tylko raz. Aby skorzystać z opcji płatności wielokrotnego użytku, możesz użyć kodu QR wielokrotnego użytku, który jest ofertą BOLT12.


![Image](assets/fr/25.webp)


Gdy oferta Invoice lub BOLT12 zostanie rozliczona, transakcja pojawi się na koncie Lightning Wallet.


![Image](assets/fr/26.webp)


## Wysyłanie bitcoinów przez Lightning


Teraz, gdy masz już Sats na Phoenix, możesz dokonywać płatności za pośrednictwem Lightning Network. Zacznij od kliknięcia przycisku "*Wyślij*".


![Image](assets/fr/27.webp)


Dostępnych jest kilka opcji. Klikając "*Skanuj kod QR*", możesz zeskanować Lightning Invoice, ofertę BOLT12, a nawet otrzymany Address do płatności On-Chain.


![Image](assets/fr/28.webp)


Można również wprowadzić te informacje ręcznie za pomocą klawiatury w polu u góry Interface lub wprowadzić Lightning Address (BOLT12 lub LNURL). Informacje można również wkleić bezpośrednio za pomocą przycisku "*Wklej*".


![Image](assets/fr/29.webp)


W tym przykładzie zeskanowałem Invoice za 10 000 Sats. Aby dokonać płatności, wystarczy kliknąć "*Pay*".


![Image](assets/fr/30.webp)


Transakcja została zakończona.


![Image](assets/fr/31.webp)


Gratulacje, wiesz już jak skonfigurować i używać Phoenix. Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dzięki za udostępnienie!


Aby pójść o krok dalej, zapoznaj się z tym samouczkiem na temat Alby Hub, innego innowacyjnego i łatwego w użyciu rozwiązania do uruchamiania własnego węzła Lightning:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Aby dowiedzieć się więcej o technicznym działaniu Lightning Network, można znaleźć doskonałe bezpłatne szkolenie Fanisa Michalakisa na Plan ₿ Network:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb