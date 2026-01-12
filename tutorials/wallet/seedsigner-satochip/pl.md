---
name: Satochip x SeedSigner
description: Jak używać Satochip z SeedSigner?
---

![cover](assets/cover.webp)



*Podziękowania dla [Crypto Guide](https://www.youtube.com/@CryptoGuide/) za fork oprogramowania SeedSigner do obsługi kart inteligentnych, którego użyjemy w tym samouczku



---

Satochip to sprzęt w formacie karty inteligentnej wallet z certyfikowanym elementem zabezpieczającym EAL6+, jednym z najwyższych standardów bezpieczeństwa. Został zaprojektowany i wyprodukowany przez belgijską firmę o tej samej nazwie: Satochip.



Wyceniony na około 25 euro, Satochip wyróżnia się na tle konkurencji doskonałym stosunkiem jakości do ceny. Dzięki bezpiecznemu chipowi oferuje odporność na ataki fizyczne. Co więcej, kod źródłowy apletu jest całkowicie open-source, na licencji *AGPLv3*.



Z drugiej strony, jego format nakłada pewne ograniczenia funkcjonalne. Główną wadą Satochip jest brak zintegrowanego ekranu: użytkownicy muszą zatem podpisywać transakcje na ślepo, polegając wyłącznie na wyświetlaczu komputera.



Aby przezwyciężyć tę słabość, szczególnie interesującą konfiguracją jest użycie go w połączeniu z SeedSigner. W tej konfiguracji komunikacja nie odbywa się już bezpośrednio między komputerem a Satochip, ale poprzez wymianę kodów QR między komputerem a SeedSigner. SeedSigner działa wtedy jako ekran zaufania: wyświetla informacje do podpisania, podczas gdy sam podpis jest wykonywany przez Satochip. W przeciwieństwie do konwencjonalnego użycia SeedSigner (lub nawet w połączeniu z Seedkeeper), seed nigdy nie jest ładowany do SeedSigner. W ten sposób SeedSigner staje się ekranem Satochip, eliminując ryzyko związane z podpisywaniem "na ślepo".



Jeśli spojrzymy na problem z innej strony, użycie SeedSigner z Satochipem wypełnia główną lukę w SeedSigner: możliwość przechowywania i używania seed w secure element.



Moim zdaniem taka konfiguracja oferuje kilka zalet w porównaniu z konwencjonalnymi portfelami sprzętowymi:




- Satochip kosztuje około 25 euro, a ponieważ aplet jest open-source, można go zainstalować samodzielnie na pustej karcie inteligentnej. Następnie należy dodać koszt komponentów SeedSigner i rozszerzenia do odczytu kart inteligentnych: w zależności od tego, gdzie kupisz ten sprzęt, łączna kwota powinna wynosić od 70 do 100 euro.
- Całe oprogramowanie zaangażowane w konfigurację jest open-source: oprogramowanie układowe SeedSigner i aplet Satochip.
- Korzystasz z certyfikowanego elementu bezpieczeństwa.
- Konfigurację można przeprowadzić całkowicie samodzielnie, bez uciekania się do sprzętu wyraźnie przeznaczonego do użytku Bitcoin, co może stanowić formę wiarygodnego zaprzeczenia i odporności na niektóre zagrożenia zewnętrzne (w tym, w zależności od kraju, naciski ze strony państwa). Jest to również interesujące rozwiązanie, jeśli dostęp do komercyjnych portfeli sprzętowych jest ograniczony lub niemożliwy w danym regionie.




## 1. Wymagane materiały



Do przeprowadzenia tej konfiguracji potrzebne będą następujące elementy:




- Zwykły sprzęt potrzebny klasycznemu SeedSignerowi:
 - raspberry Pi Zero z pinami GPIO,
 - 1.3-calowy ekran Waveshare,
 - kompatybilna kamera,
 - kartę microSD.



![Image](assets/fr/01.webp)





- Zestaw rozszerzeń SeedSigner, dostępny [w oficjalnym sklepie Satochip](https://satochip.io/product/seedsigner-extension-kit/), który umożliwia odczyt i zapis na karcie inteligentnej bezpośrednio z SeedSigner. Inną opcją jest użycie [zewnętrznego czytnika kart inteligentnych](https://satochip.io/product/chip-card-reader/), który można podłączyć kablem do portu Micro-USB w Raspberry Pi. Nie testowałem jednak tego rozwiązania osobiście;
- [A Satochip](https://satochip.io/product/satochip/) lub alternatywnie [blank smartcard](https://satochip.io/product/card-for-diy-project/), na której można zainstalować aplet Satochip (zestaw rozszerzeń sprzedawany przez Satochip zawiera już pustą kartę). Zestaw rozszerzeń Satochip obsługuje również format [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Możesz więc wybrać ten format, jeśli wolisz.



![Image](assets/fr/02.webp)



Aby uzyskać więcej informacji na temat sprzętu wymaganego do złożenia SeedSigner, zapoznaj się z częścią 1 tego samouczka:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Instalacja oprogramowania sprzętowego



Aby używać SeedSigner z Satochip, należy zainstalować alternatywne oprogramowanie układowe, inne niż oryginalne SeedSigner, w celu obsługi odczytu kart inteligentnych. W tym celu [zalecam użycie fork z "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Pobierz [najnowszą wersję obrazu](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) odpowiadającą używanemu modelowi Raspberry Pi.



![Image](assets/fr/03.webp)



Jeśli jeszcze go nie masz, pobierz oprogramowanie [Balena Etcher](https://etcher.balena.io/), a następnie wykonaj następujące czynności:




- Włóż kartę microSD do komputera;
- Launch Etcher ;
- Wybierz właśnie pobrany plik `.zip`;
- Wybierz kartę microSD jako cel;
- Kliknij na `Flash!`.



![Image](assets/fr/04.webp)



Poczekaj na zakończenie procesu: karta microSD jest teraz gotowa do użycia. Możesz teraz przejść do montażu urządzenia.



Aby uzyskać więcej informacji na temat instalacji oprogramowania układowego i weryfikacji oprogramowania (co zdecydowanie zalecam), zapoznaj się z poniższym samouczkiem:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Montaż czytnika kart inteligentnych



Zacznij od zainstalowania kamery na Raspberry Pi Zero, ostrożnie wkładając ją do bolca kamery i blokując czarną wypustką. Następnie umieść Pi na spodzie obudowy, upewniając się, że porty są wyrównane z odpowiednimi otworami.



![Image](assets/fr/05.webp)



Następnie podłącz czytnik kart inteligentnych do pinów GPIO Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Nasuń plastikową osłonę na czytnik kart inteligentnych, aż zostanie prawidłowo umieszczona.



![Image](assets/fr/07.webp)



Następnie dodaj ekran do pinów GPIO rozszerzenia.



![Image](assets/fr/08.webp)



Na koniec włóż kartę microSD zawierającą oprogramowanie sprzętowe do bocznego portu Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Możesz teraz podłączyć SeedSigner albo przez port Micro-USB Raspberry Pi Zero, albo przez port USB-C rozszerzenia. Obie opcje działają. Poczekaj kilka sekund na uruchomienie, a następnie powinien pojawić się ekran powitalny.



![Image](assets/fr/10.webp)



Aby uzyskać więcej informacji na temat początkowej konfiguracji SeedSigner, zalecamy zapoznanie się z częścią 4 poniższego samouczka:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flashowanie karty inteligentnej za pomocą apletu Satochip (opcjonalnie)



Jeśli posiadasz już Satochip, możesz pominąć ten krok i przejść od razu do kroku 4. W tej sekcji przyjrzymy się, jak zainstalować aplet Satochip na pustej karcie inteligentnej (metoda DIY). Aplet to po prostu mały program działający na karcie inteligentnej, który umożliwia nam zarządzanie określonymi funkcjami.



Aby rozpocząć, otwórz menu `Tools > Smartcard Tools` w SeedSigner.



![Image](assets/fr/11.webp)



Następnie wybierz `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Włóż kartę do czytnika SeedSigner chipem do dołu i wybierz aplet `Satochip`.



![Image](assets/fr/13.webp)



Prosimy o cierpliwość podczas instalacji: proces może potrwać kilkadziesiąt sekund.



![Image](assets/fr/14.webp)



Po pomyślnym zainstalowaniu apletu można przejść do kroku 4.



![Image](assets/fr/15.webp)




## 5. Tworzenie i zapisywanie seed



### 5.1. Wygeneruj seed



Teraz, gdy cały sprzęt i oprogramowanie działają prawidłowo, można przystąpić do tworzenia portfela Bitcoin. Aby to zrobić, podłącz swój SeedSigner, a następnie generate seed, tak jak w przypadku konwencjonalnego SeedSignera, rzucając kostką lub robiąc zdjęcie:




- Przejdź do menu `Narzędzia > Kamera / Rzuty kostką`;
- Następnie wykonaj proces generowania entropii zgodnie z wybraną metodą;
- Na koniec należy wykonać kopię zapasową seed na nośniku fizycznym i dokładnie ją sprawdzić.



![Image](assets/fr/16.webp)



Jeśli chcesz zapoznać się ze szczegółami tej procedury, postępuj zgodnie z częścią 5 tego samouczka:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Zapisywanie seed na urządzeniu Seedkeeper



Po wygenerowaniu seed jest to jedyny czas, w którym znajduje się on w pamięci RAM SeedSignera. W moim przypadku chcę zapisać go na [Seedkeeper](https://satochip.io/product/seedkeeper/), innym produkcie Satochip przeznaczonym do przechowywania sekretów. Użyję tego urządzenia w ostateczności, w przypadku utraty mojego Satochipa.



Wybrana strategia tworzenia kopii zapasowych zależy od preferencji, ale konieczne jest posiadanie co najmniej jednej kopii frazy mnemonicznej na nośniku fizycznym (papierowym lub metalowym) lub, jak tutaj, w Seedkeeper. Można również zwielokrotnić liczbę kopii zapasowych w zależności od potrzeb. Aby uzyskać więcej informacji na temat strategii tworzenia kopii zapasowych portfela, sugeruję przeczytanie tego samouczka :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Aby wykonać kopię zapasową seed na Seedkeeper, przejdź bezpośrednio do menu `Backup Seed`.



![Image](assets/fr/17.webp)



Następnie włóż swój Seedkeeper do czytnika kart inteligentnych i wybierz `To SeedKeeper`.



![Image](assets/fr/18.webp)



Wprowadź kod PIN, aby go odblokować.



![Image](assets/fr/19.webp)



Wybierz `Label`, aby łatwo zidentyfikować różne sekrety przechowywane w Seedkeeper. Możesz na przykład po prostu zachować odcisk wallet lub wyraźnie wskazać `Seed`. Wybór zależy od preferencji i ryzyka.



![Image](assets/fr/20.webp)



Jeśli twoja strategia tworzenia kopii zapasowych opiera się wyłącznie na tym Seedkeeperze, zdecydowanie zalecam przeprowadzenie teraz pustego testu odzyskiwania, a następnie porównanie odcisków palców w celu sprawdzenia, czy kopia zapasowa działa.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Kod PIN Seedkeeper powinien być tak długi i losowy, jak to możliwe, aby zapobiec próbom brutalnej siły w przypadku fizycznego naruszenia karty. Należy również zachować kopię zapasową tego kodu PIN, przechowywaną w innym miejscu niż Seedkeeper. Bez tego kodu PIN nie będzie można uzyskać dostępu do mnemonika przechowywanego w Seedkeeper, a bitcoiny zostaną trwale utracone.



### 5.3. Zapisz seed na Satochip



Teraz, gdy portfel został wygenerowany, zapisany i zweryfikowany, przeniesiemy go do Satochip. Aby to zrobić, upewnij się, że seed jest załadowany do pamięci RAM SeedSigner. Następnie przejdź do `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/21.webp)



Włóż urządzenie Satochip do czytnika kart inteligentnych, a następnie wybierz opcję `Initialise with Seed`.



![Image](assets/fr/22.webp)



Urządzenie wyświetli monit o wprowadzenie kodu PIN Satochip; ponieważ karta jest nowa i niezainicjowana, kod PIN jeszcze nie istnieje. Wprowadź dowolny kod, aby pominąć ten krok (nie jest to kod blokujący).



![Image](assets/fr/23.webp)



SeedSigner wykrywa, że Satochip nie został zainicjowany. Kliknij "Rozumiem", aby potwierdzić.



![Image](assets/fr/24.webp)



Następnie można ustawić kod PIN Satochip, od 4 do 16 znaków. Aby wzmocnić bezpieczeństwo wallet, wybierz długi, losowy kod: jest to jedyne zabezpieczenie przed fizycznym dostępem do frazy mnemonicznej.



Pamiętaj, aby zapisać ten kod PIN natychmiast po jego utworzeniu, w bezpiecznym menedżerze haseł lub na fizycznym nośniku, w zależności od osobistej strategii. W tym drugim przypadku należy pamiętać, aby nigdy nie przechowywać nośnika zawierającego PIN w tym samym miejscu co Satochip, w przeciwnym razie ochrona stanie się bezużyteczna. Ważne jest posiadanie kopii zapasowej: **Bez tego kodu PIN nie będzie można uzyskać dostępu do seed, a bitcoiny zostaną utracone na zawsze**.



![Image](assets/fr/25.webp)



Następnie SeedSigner zapyta, który seed zaimportować do Satochip. Wybierz ten, którego odcisk palca pasuje do właśnie utworzonego portfela.



![Image](assets/fr/26.webp)



Twój seed został zaimportowany do Satochip.



![Image](assets/fr/27.webp)



Możesz teraz wyłączyć SeedSigner.



Jeśli chcesz użyć passphrase BIP39, aby zwiększyć bezpieczeństwo wallet, zapoznaj się z częścią 6 tego samouczka:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Zaimportuj wallet do Sparrow



Po uruchomieniu portfela zaimportujemy jego informacje publiczne ("*keystore*") do Sparrow Wallet lub innego oprogramowania do zarządzania portfelem. Oprogramowanie to będzie używane do tworzenia, dystrybucji i śledzenia transakcji. Nie będzie jednak w stanie ich podpisać, ponieważ tylko Satochip (i wszelkie kopie zapasowe) przechowują klucze prywatne potrzebne do tej operacji.



### 6.1 Przygotowanie SeedSigner i Satochip



Włóż kartę microSD zawierającą system operacyjny, a następnie włącz SeedSigner. W tej chwili nie może on nic zrobić, ponieważ nie zna jeszcze seed. Będziesz musiał zacząć od włożenia Satochip do czytnika kart inteligentnych, ponieważ to on zawiera seed.



Z ekranu głównego przejdź do menu `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/28.webp)



Następnie kliknij `Export Xpub`.



![Image](assets/fr/29.webp)



Wybierz typ portfela. W naszym przypadku jest to pojedynczy portfel: wybierz `Single Sig`.



![Image](assets/fr/30.webp)



Następnie należy wybrać standard skryptów. Wybierz najnowszy: `Native SegWit`.



![Image](assets/fr/31.webp)



Na koniec wybierz `Coordinator`, czyli oprogramowanie do zarządzania portfelem, którego chcesz używać. Tutaj będziemy używać Sparrow Wallet.



![Image](assets/fr/32.webp)



Pojawi się komunikat ostrzegawczy: jest to całkowicie normalne. Rozszerzony klucz publiczny (`xpub`) umożliwia przeglądanie wszystkich adresów pochodzących z seed (na pierwszym koncie). Nie daje on jednak dostępu do twoich funduszy: jego ujawnienie zagroziłoby twojej prywatności, ale nie bezpieczeństwu twoich bitcoinów. Innymi słowy, pozwala na obserwowanie sald, ale nie na ich wydawanie.



Kliknij przycisk "Rozumiem".



![Image](assets/fr/33.webp)



Następnie wprowadź kod PIN urządzenia Satochip, aby je odblokować. Jest to kod zdefiniowany i zapisany w kroku 5.



![Image](assets/fr/34.webp)



Na koniec kliknij `Export Xpub`, jeśli jesteś zadowolony z wyświetlanych informacji.



![Image](assets/fr/35.webp)



Następnie SeedSigner generuje xpub w postaci dynamicznego kodu QR, zawierającego wszystkie dane potrzebne do zarządzania portfelem w Sparrow Wallet. Jasność ekranu można regulować za pomocą joysticka, aby ułatwić skanowanie kodu QR.



### 6.2 Importowanie nowego portfela do Sparrow Wallet



Upewnij się, że oprogramowanie Sparrow Wallet jest zainstalowane na komputerze. Jeśli nie wiesz, jak je pobrać, sprawdzić jego autentyczność i poprawnie zainstalować, zapoznaj się z naszym pełnym samouczkiem na ten temat:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Na komputerze otwórz Sparrow Wallet, a następnie na pasku menu kliknij `File → Import Wallet`.



![Image](assets/fr/36.webp)



Przewiń w dół do `SeedSigner`, a następnie wybierz `Scan...`. Twoja kamera internetowa zostanie aktywowana: zeskanuj dynamiczny kod QR wyświetlany na ekranie SeedSigner.



![Image](assets/fr/37.webp)



Przypisz nazwę do portfela, a następnie kliknij `Create Wallet`. Następnie Sparrow poprosi o ustawienie hasła w celu zablokowania lokalnego dostępu do tego wallet. Wybierz silne hasło: chroni ono dane w Sparrow (klucze publiczne, adresy, etykiety i historię transakcji). Hasło to nie jest jednak wymagane do przywrócenia wallet w przyszłości: wymagana będzie jedynie fraza mnemoniczna (i ewentualnie passphrase).



Zalecam zapisanie tego hasła w menedżerze haseł, aby uniknąć jego utraty.



![Image](assets/fr/38.webp)



Twój magazyn kluczy został pomyślnie zaimportowany.



![Image](assets/fr/39.webp)



Teraz sprawdź, czy `Master fingerprint` wyświetlany w Sparrow Wallet jest zgodny z tym znalezionym wcześniej na twoim SeedSignerze.



Następnie SeedSigner poprosi o zeskanowanie losowego adresu odbiorczego z Sparrow wallet w celu potwierdzenia ważności importu.



![Image](assets/fr/40.webp)



Satochip (za pośrednictwem SeedSigner) i Sparrow Wallet są teraz bezpiecznie połączone. Sparrow działa jako kompletny interfejs zarządzania, podczas gdy Satochip pozostaje jedynym urządzeniem zdolnym do podpisywania transakcji. Jesteś teraz gotowy do odbierania i wysyłania bitcoinów w całkowicie hermetycznej konfiguracji.



![Image](assets/fr/41.webp)



## 7. Odbieranie i wysyłanie bitcoinów



Satochip i Sparrow Wallet są teraz skonfigurowane do współpracy. W tej sekcji wyjaśnimy krok po kroku, jak odbierać i wysyłać bitcoiny w tym trybie.



### 7.1 Otrzymywanie bitcoinów



#### 7.1.1 Generowanie adresu odbioru



Na komputerze otwórz Sparrow Wallet i odblokuj swój `Satochip-SeedSigner` wallet za pomocą hasła. Sprawdź, czy oprogramowanie jest połączone z serwerem (wskaźnik w prawym dolnym rogu). Następnie na pasku bocznym kliknij `Receive`.



![Image](assets/fr/42.webp)



Pojawi się nowy adres Bitcoin. Znajdziesz :




- Adres w formacie tekstowym (zaczynający się od `bc1q...`, jeśli używasz P2WPKH, jak w tym przykładzie) ;
- Powiązany kod QR ;
- Pole `Label`, przydatne do śledzenia transakcji.



Zdecydowanie zalecam dodanie etykiety do każdego paragonu bitcoinów w wallet. Pomoże to łatwo zidentyfikować pochodzenie każdego UTXO i lepiej zarządzać swoją prywatnością. Aby dowiedzieć się więcej na ten ważny temat, sprawdź dedykowane szkolenie w Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Aby dodać etykietę, wystarczy wpisać nazwę w polu `Label`, a następnie potwierdzić.



Na przykład:



```txt
Label : Sale of the Raspberry Pi Zero
```



Twój adres jest teraz powiązany z tą etykietą we wszystkich sekcjach Sparrow.



![Image](assets/fr/43.webp)



#### 7.1.2 Weryfikacja Address na urządzeniu SeedSigner



Przed przekazaniem płatnikowi adresu odbiorczego należy sprawdzić, czy należy on do seed. Ten krok gwarantuje, że Satochip będzie w stanie podpisać transakcje powiązane z tym adresem. Zapobiega to również potencjalnym atakom, w których Sparrow wyświetlałby fałszywy adres. Należy pamiętać, że Sparrow działa w niezabezpieczonym środowisku (na komputerze użytkownika), którego powierzchnia ataku jest znacznie większa niż w przypadku Satochip, który jest całkowicie odizolowany. Dlatego nigdy nie należy ślepo ufać adresom wyświetlanym w Sparrow przed sprawdzeniem ich na sprzęcie wallet.



W Sparrow kliknij kod QR adresu, aby go powiększyć: zostanie on wyświetlony na pełnym ekranie.



![Image](assets/fr/44.webp)



W aplikacji SeedSigner włóż kartę Satochip do czytnika, a następnie z menu głównego wybierz `Scan`. Zeskanuj kod QR wyświetlony na komputerze, a następnie wybierz `Użyj karty Satochip`.



![Image](assets/fr/45.webp)



Następnie potwierdź typ używanego skryptu (w tym przypadku `Native SegWit`), wprowadź kod PIN Satochip, aby go odblokować i potwierdź informacje `xpub`.



![Image](assets/fr/46.webp)



Jeśli zeskanowany adres jest zgodny z adresem uzyskanym z seed, SeedSigner wyświetli komunikat: `Address Verified`.



![Image](assets/fr/47.webp)



Dzięki temu możesz mieć pewność, że adres należy do Twojego portfela.



#### 7.1.3 Otrzymanie środków



Możesz teraz przesłać ten adres w formie tekstowej lub za pomocą kodu QR do osoby lub działu, który musi wysłać Ci dane. Po rozesłaniu transakcji w sieci pojawi się ona w zakładce "Transakcje" w Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Wyślij bitcoiny



Wysyłanie bitcoinów za pomocą konfiguracji Satochip-SeedSigner obejmuje 3 kroki:




- Tworzenie transakcji w Sparrow ;
- Podpisanie tej transakcji na Satochip, za pośrednictwem SeedSigner ;
- Na koniec transakcja jest transmitowana przez sieć z Sparrow.



Wszystkie wymiany między tymi dwoma urządzeniami odbywają się wyłącznie za pośrednictwem kodów QR.



#### 7.2.1 Tworzenie transakcji w Sparrow



W Sparrow Wallet można utworzyć transakcję, klikając zakładkę `Wyślij` na lewym pasku bocznym. Ja jednak wolę korzystać z zakładki `UTXOs`, która pozwala ćwiczyć *Coin Control*. Ta metoda oferuje precyzyjną kontrolę nad wydanymi UTXO, aby ograniczyć informacje ujawniane podczas transakcji.



W zakładce `UTXOs` wybierz monety, które chcesz wydać, a następnie kliknij `Send Selected`.



![Image](assets/fr/49.webp)



Następnie wypełnij pola transakcji:




- W `Pay to` wklej adres odbiorcy lub zeskanuj jego kod QR za pomocą ikony aparatu ;
- W polu `Label` dodaj etykietę, aby śledzić ten wydatek;
- W polu `Amount` wprowadź kwotę do wysłania;
- Na koniec należy wybrać szybkość ładowania zgodnie z aktualnymi warunkami sieciowymi (szacunki są dostępne na stronie [mempool.space](https://mempool.space/)).



Po wypełnieniu wszystkich pól, dokładnie przejrzyj informacje, a następnie kliknij `Twórz transakcję >>`.



![Image](assets/fr/50.webp)



Sprawdź szczegóły transakcji po raz ostatni, a następnie kliknij `Finalizuj transakcję do podpisania`.



![Image](assets/fr/51.webp)



Transakcja jest gotowa, ale nie została jeszcze podpisana. Aby wyświetlić [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) jako kod QR, kliknij `Pokaż QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Podpisanie transakcji z Satochip



Włącz SeedSigner i włóż Satochip jak zwykle. Na ekranie głównym wybierz `Scan`, a następnie zeskanuj kod QR wyświetlony na Sparrow.



![Image](assets/fr/53.webp)



Wybierz opcję `Użyj karty Satochip`.



![Image](assets/fr/54.webp)



Wprowadź kod PIN, aby odblokować kartę.



![Image](assets/fr/55.webp)



SeedSigner wykrywa, że jest to PSBT i wyświetla podsumowanie transakcji:




   - Wysłana kwota,
   - Adresy docelowe,
   - Powiązane koszty transakcyjne.



Kliknij `Review Details` i sprawdź wszystkie informacje bezpośrednio na ekranie SeedSigner. Najważniejszymi punktami do sprawdzenia są wysłane kwoty, adresy docelowe i opłaty transakcyjne.



![Image](assets/fr/56.webp)



Jeśli wszystko jest w porządku, wybierz `Approve PSBT`, aby podpisać transakcję za pomocą Satochip.



![Image](assets/fr/57.webp)



Po zakończeniu podpisywania SeedSigner generuje nowy kod QR zawierający podpisaną transakcję, gotowy do zeskanowania przez Sparrow.



#### 7.2.3 Transmisja transakcji z Sparrow



Teraz, gdy transakcja została podpisana i zatwierdzona, pozostaje tylko rozgłosić ją w sieci Bitcoin, aby górnik mógł dołączyć ją do bloku. W Sparrow kliknij na `Scan QR`.



![Image](assets/fr/58.webp)



Przedstaw kod QR wyświetlony na urządzeniu SeedSigner (zawierający podpisaną transakcję) kamerze internetowej. Sparrow wyświetli wszystkie szczegóły transakcji. Sprawdź, czy wszystkie informacje są prawidłowe, a następnie kliknij przycisk "Broadcast Transaction", aby rozgłosić transakcję w sieci Bitcoin.



![Image](assets/fr/59.webp)



Transakcja jest teraz przesyłana do sieci. Możesz śledzić jej potwierdzenie w zakładce `Transakcje` Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Odzyskaj swój wallet



Jak widzieliśmy w poprzednich sekcjach, w zależności od strategii bezpieczeństwa, istnieje kilka sposobów tworzenia kopii zapasowych frazy odzyskiwania oprócz Satochip :




- Korzystanie z klasycznego *SeedQR* z SeedSigner ;
- Zapisując frazę mnemoniczną na nośniku fizycznym;
- Lub przechowując go na Seedkeeperze, jak wyjaśniono w sekcji 5.2.



W każdym przypadku istnieją 2 główne sytuacje, w których należy interweniować: utrata Satochip lub utrata SeedSigner. Przyjrzyjmy się, jak reagować w każdym z tych scenariuszy.



### 8.1. Odzyskaj swój wallet za pomocą Satochip



Jeśli nadal posiadasz swój Satochip, ale Twój SeedSigner jest uszkodzony lub zagubiony, sytuacja jest dość prosta do opanowania, ponieważ Twój wallet jest nadal w Satochip.



Najlepszą opcją jest polecenie niezbędnych komponentów i odbudowanie nowego SeedSignera od podstaw. Ponieważ jest to urządzenie "bezstanowe", nie ma znaczenia, czy używasz tego samego, czy innego SeedSignera: tak długo, jak możesz włożyć swój Satochip, wszystko będzie działać normalnie.



Jeśli nie chcesz go odbudowywać, możesz również użyć swojego Satochipa w klasyczny sposób, tj. bezpośrednio z komputera, bez przechodzenia przez SeedSigner. Ta metoda działa doskonale, ale znacznie zmniejsza bezpieczeństwo Bitcoin wallet: tracisz izolację "*air-gapped*" i musisz teraz podpisywać na ślepo, ponieważ SeedSigner działał jako zaufany ekran. Może to być jednak tymczasowe rozwiązanie w sytuacjach awaryjnych lub jeśli nie jesteś w stanie odbudować SeedSigner.



Aby to zrobić, potrzebna będzie karta inteligentna USB lub czytnik NFC. Otwórz wallet, który chcesz przywrócić w Sparrow, a następnie przejdź do zakładki `Ustawienia` i kliknij `Zastąp`.



![Image](assets/fr/61.webp)



Włóż Satochip do czytnika kart inteligentnych podłączonego do komputera, a następnie kliknij `Import` obok `Satochip`.



![Image](assets/fr/62.webp)



Na koniec wprowadź kod PIN karty inteligentnej, aby ją odblokować. Następnie będziesz mógł uzyskać dostęp do wallet, tworzyć transakcje i podpisywać je bezpośrednio za pomocą podłączonego Satochip.



### 8.2. Odzyskaj swoje portfolio za pomocą SeedSigner



Innym, bardziej delikatnym scenariuszem jest utrata dostępu do satochipa zawierającego seed: niezależnie od tego, czy jest on zepsuty, zgubiony, skradziony, czy też zapomniałeś kodu PIN. Jeśli Satochip został skradziony lub zgubiony, zdecydowanie zalecamy, aby po przywróceniu dostępu do środków natychmiast przenieść swoje bitcoiny na zupełnie nowy wallet, wygenerowany przy użyciu innego seed. Gwarantuje to, że potencjalny atakujący nigdy nie uzyska dostępu do twoich satochipów.



Aby odzyskać dostęp do portfela i przenieść środki, wystarczy załadować seed do SeedSigner. W zależności od używanego nośnika kopii zapasowej masz kilka opcji:





- Wprowadź ręcznie frazę mnemoniczną w menu `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Zeskanuj swój *SeedQR* klikając na przycisk `Scan` na stronie głównej.



![Image](assets/fr/64.webp)





- Można też załadować seed z Seedkeepera za pomocą menu `Seeds > From SeedKeeper` (jest to metoda, której używam w tym poradniku). Wystarczy wprowadzić kod PIN Seedkeepera i wybrać sekret, który ma być używany jako seed w SeedSigner.



![Image](assets/fr/65.webp)



Po załadowaniu seed do SeedSigner, niezależnie od używanej metody, będziesz mógł podpisać jedną lub więcej transakcji skanowania, aby przenieść swoje bitcoiny do nowego, nieskompromitowanego wallet. Aby dowiedzieć się, jak to zrobić, zobacz część 7.2 poniższego samouczka:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Teraz już wiesz, jak używać Satochip do bezpiecznego zarządzania portfelem Bitcoin w połączeniu z SeedSigner.



Jeśli ta konfiguracja cię przekonała, nie wahaj się wspierać projektów, które to umożliwiają:




- Kupując sprzęt bezpośrednio [na stronie internetowej Satochip](https://satochip.io/shop/);
- Przekazując [darowiznę na rzecz projektu SeedSigner](https://seedsigner.com/donate/);
- Subskrybując kanał YouTube [Crypto Guide](https://www.youtube.com/@CryptoGuide/), prowadzony przez osobę, która utrzymuje repozytorium GitHub zawierające zmodyfikowane oprogramowanie układowe, którego używaliśmy w tym samouczku.