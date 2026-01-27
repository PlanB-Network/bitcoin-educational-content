---
name: Breez - POS
description: Breez ułatwia zbieranie płatności bitcoinowych dla Twojej firmy.
---

![cover](assets/cover.webp)



Od czasu pandemii COVID-19 zbliżeniowe płatności cyfrowe stały się powszechne, nawet w najmniejszych sklepach. W tym okresie wiele firm odkryło praktyczność rozwiązań gotówkowych Bitcoin, umożliwiając im otrzymywanie płatności z całego świata. Jednak rozwiązania te są czasami trudne w użyciu lub nieodpowiednie dla małych firm. W tym samouczku przyjrzymy się terminalowi płatniczemu Breez, rozwiązaniu, które wyróżnia się łatwością obsługi, zapewniając jednocześnie pełną kontrolę nad zarządzaniem bitcoinami.



## Zainstaluj Breez POS



Breez POS to usługa samoobsługowa świadczona przez Breez wallet. Użyteczność tej usługi polega na umożliwieniu sprzedawcom zbierania płatności za pośrednictwem Bitcoin przy zachowaniu prostego interfejsu, bardzo podobnego do różnych portfeli Lightning. Breez POS jest dostępny na platformach pobierania [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) i [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS).



![download](assets/fr/01.webp)



![setup](assets/fr/12.webp)



⚠️ Należy pamiętać, że aplikacje te są nadal w fazie rozwoju i mogą występować pewne błędy w korzystaniu z ich funkcji. Zalecamy umiarkowane korzystanie.



Dzięki tej aplikacji Breez zapewnia pełną kontrolę nad konfiguracjami sieci i ustawieniami opłat, gwarantując jednocześnie suwerenność w zarządzaniu bitcoinami.



Możesz zapoznać się z różnymi opcjami Breez wallet, postępując zgodnie z naszym samouczkiem poniżej. Ten krok pomoże ci lepiej zrozumieć ekosystem punktów sprzedaży i przyjąć najlepsze praktyki, aby skutecznie zabezpieczyć bitcoiny powiązane z seed.



https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Korzystanie z Breez POS



W tym samouczku skupimy się na sekcji "*Point-of-Sale*", aby pomóc Ci zrozumieć, jak zintegrować ją jako środek płatności w Twojej firmie.



Punkt sprzedaży jest integralną częścią portfolio Breez i opiera się głównie na Lightning Network do zbierania płatności.



W menu "*Point of Sale*" dostępny jest bezpośredni interfejs do pobierania płatności. Jest on podzielony na dwie części:



### Polecenie zapłaty



Pierwsza część to klawiatura polecenia zapłaty. Ten interfejs jest przydatny do pobierania płatności w całości, gdy znasz całkowite zakupy klienta lub gdy nie potrzebujesz stałego katalogu produktów w swojej firmie (np. usługi freelancerskie).



![keyboard](assets/fr/02.webp)



Aby skorzystać z Breez POS po raz pierwszy, należy uiścić opłatę w wysokości ponad 2500 satoshi (około 3 euro po dzisiejszym kursie wymiany). Kwota ta, płatna tylko przy pierwszej wypłacie gotówki, stanowi koszt utworzenia kanału płatności, dzięki któremu można komunikować się z innymi węzłami Lightning Network oraz wysyłać i odbierać satoshi.



![channel_fee](assets/fr/03.webp)


### Katalog produktów



Druga część to katalog produktów. Interfejs ten jest idealny w przypadku posiadania katalogu produktów z predefiniowanymi cenami. W tym miejscu można wstępnie skonfigurować produkty, a następnie użyć ich do faktur generate, aby poprawić identyfikowalność wpływów gotówkowych.



![items](assets/fr/04.webp)



Z poziomu tego interfejsu można ręcznie skonfigurować każdą pozycję, klikając przycisk "**Plus**", a następnie definiując nazwę, cenę i identyfikator dla tej pozycji.



![add_items](assets/fr/05.webp)



Następnie można go dodać i zdefiniować jego ilość, aby pobrać powiązaną płatność.



Gdy katalog jest dość duży, dodawanie produktów jeden po drugim może być skomplikowane. W tym celu w sekcji **Preferencje > Ustawienia punktu sprzedaży**, w menu "Lista artykułów", można automatycznie importować i eksportować listę artykułów z plików CSV.



![import](assets/fr/07.webp)



W tej samej sekcji można zdefiniować okres ważności faktur Lightning. Od tego momentu klienci mają `N` sekund na dokonanie płatności za wszystkie faktury, a w przeciwnym razie konieczne będzie ponowne wygenerowanie nowej faktury Lightning.



![invoice_time](assets/fr/08.webp)



Jako menedżer możesz zwiększyć bezpieczeństwo swoich bitcoinów, dodając hasło, które będzie wymagane dla wszystkich płatności wychodzących z wallet. Funkcja ta jest szczególnie przydatna, gdy nie jesteś jedyną osobą zarządzającą swoim punktem sprzedaży.



![manager](assets/fr/09.webp)



W menu **Transakcje** znajdziesz listę wszystkich pobranych płatności. Możesz również filtrować wyniki według określonego okresu, klikając przycisk **Kalendarz**.



![transactions](assets/fr/10.webp)



Możesz również wyświetlić dzienne podsumowanie sprzedaży i całkowitą zebraną kwotę, klikając przycisk **Dokument**.



![summary](assets/fr/11.webp)



Masz teraz pełną wiedzę na temat punktu sprzedaży oferowanego przez aplikację Breez w celu płynnej integracji Bitcoin z Twoją firmą. Jeśli ten samouczek okazał się przydatny, polecamy nasz samouczek na temat be-BOP, platformy e-commerce, która pozwala przyjmować płatności w bitcoinach i zarabiać na swojej działalności.



https://planb.academy/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa