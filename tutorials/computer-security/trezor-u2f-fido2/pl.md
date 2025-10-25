---
name: "Trezor U2F & FIDO2"
description: Wzmocnij swoje bezpieczeństwo online dzięki Trezor
---
![cover](assets/cover.webp)



Urządzenia Trezor to portfele sprzętowe pierwotnie zaprojektowane w celu zabezpieczenia Bitcoin Wallet, ale posiadają również zaawansowane opcje silnego uwierzytelniania w sieci. Dzięki kompatybilności z protokołami **U2F** i **FIDO2** umożliwiają zabezpieczenie dostępu do kont internetowych bez polegania wyłącznie na hasłach.



Protokół U2F (*Universal 2nd Factor*) został wprowadzony przez Google i Yubico w 2014 roku, a następnie ustandaryzowany przez FIDO Alliance. Umożliwia on dodanie drugiego fizycznego czynnika uwierzytelniania (2FA) podczas logowania. Po aktywacji, oprócz klasycznego hasła, użytkownicy muszą zatwierdzić każdą próbę połączenia się ze swoim kontem, naciskając przycisk na Trezorze. W tym kontekście Trezor działa podobnie do Yubikey.



Metoda ta opiera się na kryptografii asymetrycznej: żadne tajne dane nie są przesyłane, dzięki czemu ataki phishingowe lub przechwytujące są nieskuteczne. U2F jest obecnie obsługiwany przez wiele usług online.



Oprócz U2F, który umożliwia uwierzytelnianie dwuskładnikowe, Trezory obsługują również FIDO2 (*Fast IDentity Online 2.0*), ewolucję U2F. Jest to ustandaryzowany protokół uwierzytelniania z 2018 roku, który rozszerza logikę U2F i ma na celu całkowite zastąpienie haseł. Opiera się na dwóch komponentach: *WebAuthn* (po stronie przeglądarki) i *CTAP2* (po stronie klucza fizycznego). FIDO2 umożliwia uwierzytelnianie "bez hasła": użytkownicy identyfikują się wyłącznie za pomocą urządzenia Trezor, które działa jako unikalny token kryptograficzny, bez dodatkowego hasła. Protokół ten jest obecnie kompatybilny z wieloma usługami online, szczególnie tymi przeznaczonymi dla przedsiębiorstw.



Oprócz funkcji "bez hasła", FIDO2 umożliwia również uwierzytelnianie dwuskładnikowe w podobny sposób jak U2F.



FIDO2 wprowadza również pojęcie rezydentnych danych uwierzytelniających, tj. identyfikatorów przechowywanych bezpośrednio w Trezorze, które zawierają zarówno klucz prywatny umożliwiający połączenie, jak i informacje identyfikacyjne użytkownika. Mechanizm ten umożliwia prawdziwie bezhasłowe uwierzytelnianie: wystarczy podłączyć Trezor i potwierdzić dostęp, bez wprowadzania identyfikatora lub hasła. I odwrotnie, poświadczenia nierezydentne, które są bardziej konwencjonalne, przechowują tylko klucz prywatny w urządzeniu; identyfikator użytkownika pozostaje przechowywany po stronie serwera i dlatego musi być wprowadzany przy każdym połączeniu. Później przyjrzymy się, jak zapisać je za pomocą Trezora.



W tym samouczku dowiemy się, jak aktywować U2F lub FIDO2 do uwierzytelniania dwuskładnikowego, a następnie jak skonfigurować FIDO2, aby uzyskać dostęp do kont bez hasła, bezpośrednio za pomocą Trezora.



**Uwaga:** U2F jest kompatybilne ze wszystkimi modelami Trezor, ale FIDO2 jest obsługiwane tylko przez Safe 3, Safe 5 i Model T, a nie Model One.



## Używanie U2F/FIDO2 do 2FA na Trezorze



Przed rozpoczęciem upewnij się, że skonfigurowałeś Bitcoin Wallet na Trezorze. Ważne jest prawidłowe zapisanie Mnemonic, ponieważ klucze używane do U2F i FIDO2 w uwierzytelnianiu dwuskładnikowym pochodzą z tego Mnemonic. Jeśli urządzenie Trezor zostanie zgubione lub uszkodzone, można odzyskać dostęp do kluczy, wprowadzając frazę Mnemonic na innym urządzeniu Trezor (należy pamiętać, że w przypadku poświadczeń FIDO2 w trybie "*bez hasła*" sam seed nie wystarczy, jak zobaczymy w następnych sekcjach).



Podłącz urządzenie Trezor do komputera i odblokuj je.



![Image](assets/fr/01.webp)



Uzyskaj dostęp do konta, które chcesz zabezpieczyć za pomocą uwierzytelniania dwuskładnikowego. Na przykład użyję konta Bitwarden. Opcję 2FA można zazwyczaj znaleźć w ustawieniach usługi, w zakładkach "*authentication*", "*security*", "*login*" lub "*password*".



![Image](assets/fr/02.webp)



W sekcji poświęconej uwierzytelnianiu dwuskładnikowemu wybierz opcję "*Passkey*" (termin może się różnić w zależności od używanej witryny).



![Image](assets/fr/03.webp)



Często będziesz proszony o potwierdzenie aktualnego hasła.



![Image](assets/fr/04.webp)



Nadaj swojemu kluczowi bezpieczeństwa nazwę w celu łatwego rozpoznania, a następnie kliknij "*Read Key*".



![Image](assets/fr/05.webp)



Dane konta zostaną wyświetlone na ekranie urządzenia Trezor. Dotknij ekranu lub naciśnij przycisk, aby potwierdzić. Zostaniesz również poproszony o potwierdzenie kodu PIN.



![Image](assets/fr/06.webp)



Zarejestruj ten klucz bezpieczeństwa.



![Image](assets/fr/07.webp)



Od teraz, gdy chcesz połączyć się ze swoim kontem, oprócz zwykłego hasła, zostaniesz poproszony o podłączenie Trezora.



![Image](assets/fr/08.webp)



Następnie można nacisnąć ekran urządzenia Trezor, aby potwierdzić uwierzytelnienie.



![Image](assets/fr/09.webp)



Zaletą korzystania z Trezora Hardware Wallet do uwierzytelniania dwuskładnikowego jest to, że można łatwo odzyskać klucze dzięki frazie Mnemonic. Oprócz tej podstawowej kopii zapasowej można również użyć kodu awaryjnego dostarczonego przez każdą usługę, w której aktywowano 2FA. Ten kod awaryjny umożliwia połączenie się z kontem w przypadku utraty klucza bezpieczeństwa. W razie potrzeby zastępuje on zatem 2FA.



Na przykład w Bitwarden można uzyskać dostęp do tego kodu, klikając "*Wyświetl kod odzyskiwania*".



![Image](assets/fr/10.webp)



Zalecam przechowywanie tego kodu w innym miejscu niż przechowujesz swoje główne hasło, aby zapobiec ich kradzieży razem. Na przykład, jeśli hasło jest zapisane w menedżerze haseł, kod awaryjny 2FA należy przechowywać osobno na papierze.



Takie podejście oferuje dwa poziomy kopii zapasowych na wypadek utraty Trezora do uwierzytelniania 2FA: pierwsza kopia zapasowa przy użyciu frazy Mnemonic dla wszystkich kont, a druga kopia zapasowa specyficzna dla każdego konta z kodami awaryjnymi. Ważne jest jednak, aby **nie mylić roli Mnemonic z rolą kodu awaryjnego**:




- 12- lub 24-wyrazowa fraza Mnemonic zapewnia dostęp nie tylko do kluczy używanych do 2FA na wszystkich kontach, ale także do bitcoinów zabezpieczonych Trezorem;
- Kod awaryjny pozwala tymczasowo ominąć żądanie 2FA tylko na danym koncie (w tym przykładzie tylko na Bitwarden).



## Korzystanie z FIDO2 na urządzeniu Trezor



Oprócz uwierzytelniania dwuskładnikowego, FIDO2 umożliwia również uwierzytelnianie "bez hasła", tj. bez konieczności wprowadzania hasła podczas logowania do witryny. Wystarczy podłączyć urządzenie Trezor do komputera, aby uzyskać dostęp do bezpiecznego konta w ten sposób. Oto jak skonfigurować tę funkcję.



Zanim zaczniesz, upewnij się, że skonfigurowałeś Bitcoin Wallet na swoim Trezorze. Ważne jest, aby zapisać Mnemonic, ponieważ identyfikatory FIDO2 "*bez hasła*" są szyfrowane za pomocą seed (dowiemy się, jak poprawnie zapisać te identyfikatory w następnej sekcji).



Podłącz urządzenie Trezor do komputera i odblokuj je.



![Image](assets/fr/01.webp)



Uzyskaj dostęp do konta, które chcesz zabezpieczyć w trybie "*bez hasła*". Jako przykładu użyję konta Bitwarden. Opcja ta znajduje się zazwyczaj w ustawieniach usługi, często w zakładce "*authentication*", "*security*" lub "*password*".



Na przykład w Bitwarden opcja ta znajduje się w zakładce "*Master password*". Kliknij "*Włącz*", aby aktywować uwierzytelnianie przez FIDO2.



![Image](assets/fr/11.webp)



Często będziesz proszony o potwierdzenie hasła.



![Image](assets/fr/12.webp)



Dane konta zostaną wyświetlone na ekranie urządzenia Trezor. Dotknij ekranu lub naciśnij przycisk, aby potwierdzić. Konieczne będzie również potwierdzenie kodu PIN.



![Image](assets/fr/13.webp)



W witrynie dodaj nazwę, aby zapamiętać klucz bezpieczeństwa, a następnie kliknij "*Włącz*".



![Image](assets/fr/14.webp)



Następnie zostaniesz poproszony o podanie swojej tożsamości w celu sprawdzenia, czy klucz działa prawidłowo.



![Image](assets/fr/15.webp)



Od teraz logowanie do konta nie będzie już wymagało podawania adresu e-mail Address lub loginu. Wystarczy kliknąć przycisk, aby uwierzytelnić się za pomocą klucza fizycznego w formularzu logowania.



![Image](assets/fr/16.webp)



Potwierdź połączenie z urządzeniem Trezor, wprowadzając kod PIN Hardware Wallet.



![Image](assets/fr/17.webp)



Zostaniesz połączony ze swoim kontem bez konieczności podawania hasła.



![Image](assets/fr/18.webp)



**Należy pamiętać, że nawet w przypadku aktywacji uwierzytelniania "*bez hasła*" za pośrednictwem FIDO2 na urządzeniu Trezor, główne hasło do konta online będzie nadal ważne do celów logowania**



## Zapisz swoje poświadczenia FIDO2 (mieszkańcy poświadczeń)



Jeśli używasz FIDO2 lub U2F do uwierzytelniania dwuskładnikowego, tj. do logowania się do kont, które wymagają hasła oprócz walidacji 2FA za pośrednictwem Trezora, wówczas sama fraza Mnemonic odzyska dostęp do kluczy. Jeśli jednak korzystasz z FIDO2 w trybie "*bez hasła*", jak opisano w poprzedniej sekcji, konieczne będzie wykonanie kopii poświadczeń FIDO oprócz utworzenia kopii zapasowej frazy Mnemonic, która szyfruje te poświadczenia.



Aby to zrobić, potrzebny będzie komputer z zainstalowanym Pythonem. Otwórz terminal i uruchom poniższe polecenie, aby zainstalować niezbędne oprogramowanie Trezor:



```shell
pip3 install --upgrade trezor
```



Podłącz urządzenie Trezor do komputera przez USB i odblokuj je za pomocą kodu PIN.



![Image](assets/fr/01.webp)



Aby pobrać listę identyfikatorów FIDO2 przechowywanych w urządzeniu Trezor, uruchom następujące polecenie:



```shell
trezorctl fido credentials list
```



Potwierdź eksport na urządzeniu Trezor.



![Image](assets/fr/19.webp)



Informacje logowania FIDO2 zostaną wyświetlone na terminalu. Na przykład dla mojego konta Bitwarden otrzymałem następujące informacje:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Skopiuj i zapisz wszystkie te informacje w pliku tekstowym. Nie ma znaczącego ryzyka związanego z tą kopią zapasową, poza ujawnieniem, że korzystasz z tych usług za pomocą FIDO2. Identyfikator "*Credential ID*" jest zaszyfrowany przy użyciu seed w Wallet, co oznacza, że osoba atakująca, która uzyska tę kopię zapasową, nie będzie w stanie połączyć się z Twoimi kontami, a jedynie zauważy, że korzystasz z tych kont. Aby odszyfrować te identyfikatory, potrzebujesz seed w Wallet.



Można zatem utworzyć kilka kopii tego pliku tekstowego i przechowywać je w różnych miejscach, na przykład lokalnie na komputerze, w usłudze hostingu plików i na nośnikach zewnętrznych, takich jak pamięć USB. Należy jednak pamiętać, że ta kopia zapasowa nie jest automatycznie aktualizowana, więc trzeba będzie ją odnawiać za każdym razem, gdy skonfigurujesz nowe połączenie "*bez hasła*" z Trezorem.



Wyobraźmy sobie, że urządzenie Trezor uległo uszkodzeniu. Aby odzyskać poświadczenia FIDO2, musisz najpierw odzyskać Wallet przy użyciu frazy Mnemonic na nowym urządzeniu Trezor kompatybilnym z FIDO2.



Po zakończeniu odzyskiwania, aby zaimportować identyfikatory FIDO2 na nowym urządzeniu, uruchom następujące polecenie w terminalu:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Wystarczy zastąpić `<CREDENTIAL_ID>` jednym z identyfikatorów. Na przykład w moim przypadku dałoby to:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor wyświetli monit o zaimportowanie identyfikatora FIDO2. Potwierdź, naciskając przycisk na ekranie.



![Image](assets/fr/20.webp)



Logowanie FIDO2 działa teraz na urządzeniu Trezor. Powtórz tę procedurę dla każdego identyfikatora.



Gratulacje, jesteś teraz na bieżąco z używaniem Trezora z U2F i FIDO2! Jeśli ten poradnik okazał się przydatny, będę bardzo wdzięczny, jeśli zostawisz poniżej kciuk Green. Zachęcam również do udostępnienia tego poradnika w sieciach społecznościowych. Dziękuję bardzo!



Polecam również ten samouczek, w którym przyglądamy się innemu rozwiązaniu do uwierzytelniania U2F i FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e