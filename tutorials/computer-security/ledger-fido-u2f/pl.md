---
name: "Ledger U2F & FIDO2"
description: Zwiększ swoje bezpieczeństwo online dzięki Ledger
---
![cover](assets/cover.webp)



Urządzenia Ledger to portfele sprzętowe pierwotnie zaprojektowane w celu zabezpieczenia Bitcoin Wallet, ale posiadają również zaawansowane opcje silnego uwierzytelniania w sieci. Dzięki kompatybilności z protokołami **U2F** i **FIDO2** umożliwiają one zabezpieczenie dostępu do kont internetowych poprzez ustawienie drugiego czynnika uwierzytelniania.



Protokół U2F (Universal 2nd Factor) został wprowadzony przez Google i Yubico w 2014 roku, a następnie ustandaryzowany przez FIDO Alliance. Umożliwia on dodanie drugiego fizycznego czynnika uwierzytelniania (2FA) podczas logowania. Po aktywacji, oprócz klasycznego hasła, użytkownicy muszą zatwierdzić każdą próbę połączenia się ze swoim kontem, naciskając przycisk na Ledger. W tym kontekście Ledger działa podobnie do Yubikey. U2F jest w rzeczywistości podkomponentem standardu FIDO2, obejmując go, a jednocześnie wprowadzając znaczące ulepszenia, w tym natywną obsługę nowoczesnych przeglądarek i większą elastyczność w zarządzaniu kluczami uwierzytelniania.



Metody te opierają się na kryptografii asymetrycznej: żadne tajne dane nie są przesyłane, dzięki czemu ataki phishingowe lub przechwytujące są nieskuteczne. U2F i FIDO2 są obecnie obsługiwane przez wiele usług online.



W tym samouczku pokażemy, jak aktywować U2F i FIDO2 w celu uwierzytelniania dwuskładnikowego za pomocą Ledger.



**Uwaga:** U2F i FIDO2 są obsługiwane na wszystkich urządzeniach Ledger wyposażonych w najnowsze oprogramowanie sprzętowe: od wersji 2.1.0 dla Nano X i Nano S classic oraz od wersji 1.1.0 dla Nano S Plus. Modele Stax i Flex są natywnie kompatybilne.



## Zainstaluj aplikację Ledger Security Key



Jeśli korzystasz z urządzenia Ledger, prawdopodobnie wiesz, że samo oprogramowanie układowe nie zawiera wszystkich funkcji potrzebnych do zarządzania portfelami kryptograficznymi. Na przykład, aby korzystać z Bitcoin Wallet, należy zainstalować aplikację "*Bitcoin*". Podobnie, aby zarządzać kluczami MFA, należy zainstalować aplikację "*Security Key*".



Przed rozpoczęciem upewnij się, że skonfigurowałeś Bitcoin Wallet na Ledger. Ważne jest prawidłowe zapisanie Mnemonic, ponieważ klucze używane do 2FA pochodzą z tego Mnemonic. Jeśli urządzenie Ledger zostanie zgubione lub uszkodzone, można odzyskać dostęp do kluczy, wprowadzając frazę Mnemonic na innym urządzeniu Ledger (na razie identyfikatory FIDO2 w trybie "*bez hasła*" nie są jeszcze obsługiwane przez Ledgers, więc nie ma identyfikatorów rezydentnych).



Podłącz Ledger do komputera i odblokuj go.



![Image](assets/fr/01.webp)



Aby zainstalować aplikację, otwórz oprogramowanie [Ledger Live] (https://www.Ledger.com/Ledger-live), a następnie przejdź do zakładki "*My Ledger*". Znajdź aplikację "*Security Key*" i zainstaluj ją na swoim urządzeniu.



![Image](assets/fr/02.webp)



Aplikacja "*Security Key*" powinna teraz pojawić się obok innych aplikacji zainstalowanych na Ledger.



![Image](assets/fr/03.webp)



Kliknij aplikację, aby pozostawić ją otwartą do następnych kroków samouczka.



![Image](assets/fr/04.webp)



## Używanie U2F/FIDO2 do 2FA z Ledger



Uzyskaj dostęp do konta, które chcesz zabezpieczyć za pomocą uwierzytelniania dwuskładnikowego. Na przykład użyję konta Bitwarden. Opcję 2FA można zazwyczaj znaleźć w ustawieniach usługi, w zakładkach "*authentication*", "*security*", "*login*" lub "*password*".



![Image](assets/fr/05.webp)



W sekcji poświęconej uwierzytelnianiu dwuskładnikowemu wybierz opcję "*Passkey*" (termin może się różnić w zależności od używanej witryny).



![Image](assets/fr/06.webp)



Często będziesz proszony o potwierdzenie aktualnego hasła.



![Image](assets/fr/07.webp)



Nadaj swojemu kluczowi bezpieczeństwa nazwę w celu łatwego rozpoznania, a następnie kliknij "*Read Key*".



![Image](assets/fr/08.webp)



Dane konta pojawią się na wyświetlaczu Ledger. Naciśnij przycisk "*Register*", aby potwierdzić (lub oba przyciski jednocześnie, w zależności od używanego modelu).



![Image](assets/fr/09.webp)



Klucz dostępu został pomyślnie zarejestrowany.



![Image](assets/fr/10.webp)



Zarejestruj ten klucz bezpieczeństwa.



![Image](assets/fr/11.webp)



Od teraz podczas logowania się do konta, oprócz zwykłego hasła, zostaniesz poproszony o podłączenie Ledger.



![Image](assets/fr/12.webp)



Następnie można nacisnąć przycisk "*Log in*" na wyświetlaczu Ledger, aby potwierdzić uwierzytelnienie (lub oba przyciski jednocześnie, w zależności od używanego modelu).



![Image](assets/fr/13.webp)



Zaletą korzystania z Hardware Wallet Ledger do uwierzytelniania dwuskładnikowego jest to, że można łatwo odzyskać klucze dzięki frazie Mnemonic. Oprócz tej podstawowej kopii zapasowej można również użyć kodu awaryjnego dostarczonego przez każdą usługę, w której aktywowano 2FA. Ten kod awaryjny umożliwia połączenie się z kontem w przypadku utraty klucza bezpieczeństwa. W razie potrzeby zastępuje on zatem 2FA.



Na przykład w Bitwarden można uzyskać dostęp do tego kodu, klikając "*Wyświetl kod odzyskiwania*".



![Image](assets/fr/14.webp)



Zalecam przechowywanie tego kodu w innym miejscu niż przechowujesz swoje główne hasło, aby zapobiec ich kradzieży razem. Na przykład, jeśli hasło jest zapisane w menedżerze haseł, kod awaryjny 2FA należy przechowywać osobno na papierze.



Takie podejście oferuje dwa poziomy kopii zapasowych na wypadek utraty Ledger do uwierzytelniania 2FA: pierwsza kopia zapasowa przy użyciu frazy Mnemonic dla wszystkich kont, a druga kopia zapasowa dla poszczególnych kont przy użyciu kodów awaryjnych. Ważne jest jednak, aby **nie mylić roli Mnemonic z rolą kodu awaryjnego**:




- 12- lub 24-wyrazowa fraza Mnemonic zapewnia dostęp nie tylko do kluczy używanych do 2FA na wszystkich kontach, ale także do bitcoinów zabezpieczonych za pomocą Ledger ;
- Kod awaryjny pozwala tymczasowo ominąć żądanie 2FA tylko na danym koncie (w tym przykładzie tylko na Bitwarden).



Gratulacje, jesteś teraz na bieżąco z używaniem Ledger do MFA! Jeśli ten poradnik okazał się przydatny, będę bardzo wdzięczny, jeśli zostawisz poniżej kciuk Green. Zachęcam również do udostępnienia tego poradnika w sieciach społecznościowych. Dziękuję bardzo!



Polecam również ten samouczek, w którym przyglądamy się innemu rozwiązaniu do uwierzytelniania U2F i FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e