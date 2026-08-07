---
term: BTCPay Server
definition: Procesor płatności o otwartym kodzie źródłowym, umożliwiający przyjmowanie płatności w bitcoinach bez pośredników.
---

⚠️ **Krytyczny alert bezpieczeństwa (7 sierpnia 2026):** krytyczna podatność dotycząca BTCPay Server jest aktywnie wykorzystywana i może prowadzić do utraty środków. Natychmiast zaktualizuj swoją instancję do **wersji 2.4.2** przez `Admin Dashboard > Server > Maintenance > Update`, a następnie sprawdź, czy w stopce wyświetla się `2.4.2`. Jeśli nie możesz zaktualizować od razu, wyłącz swój BTCPay Server. Po aktualizacji musisz również całkowicie odświeżyć swoje macaroons oraz plik `macaroons.db`, całkowicie odświeżyć ciągi uwierzytelniające wszelkich innych backendów Lightning, a jeśli wygenerowałeś gorący portfel on-chain wewnątrz BTCPay Server — przenieś te środki i utwórz portfel od nowa. Integratorzy powinni dodatkowo zaktualizować NBXplorer do wersji 2.6.10. Źródło: [Informacje o wydaniu BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b

BTCPay Server to procesor płatności typu open-source, który umożliwia sprzedawcom i użytkownikom akceptowanie płatności Bitcoin bez polegania na stronie trzeciej w zakresie przetwarzania transakcji. Uruchomiony w 2017 roku BTCPay Server zapewnia rozwiązanie do integracji płatności Bitcoin dla witryn e-commerce, z zaawansowanymi funkcjami, takimi jak obsługa portfeli sprzętowych, narzędzia rozliczeniowe i księgowe, a także kompatybilność z Lightning Network. Jego rozwój został zainicjowany przez Nicolasa Doriera w odpowiedzi na działania Bitpay, który według niego wprowadził w błąd swoich użytkowników, popychając ich do przyjęcia SegWit2x, który firma błędnie uważała za "prawdziwy" Bitcoin. Sprzeciw ten został zawarty w słynnym już tweecie Nicolasa Doriera z sierpnia 2017 roku:


> "_To kłamstwa, moje zaufanie do ciebie zostało złamane, uczynię cię przestarzałym_".

