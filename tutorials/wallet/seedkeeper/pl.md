---
name: Seedkeeper
description: Jak wykonać kopię zapasową Wallet Bitcoin za pomocą karty inteligentnej Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper to inteligentna karta opracowana przez Satochip, belgijską firmę specjalizującą się w rozwiązaniach sprzętowych do zarządzania i ochrony tajemnic cyfrowych. Znana ze swojej gamy kart elektronicznych dla ekosystemu Bitcoin, firma Satochip zaprojektowała Seedkeeper jako alternatywę dla tradycyjnych metod przechowywania fraz Mnemonic.



Mówiąc konkretnie, Seedkeeper ma postać wielofunkcyjnej karty inteligentnej z certyfikatem EAL6 z bezpiecznym procesorem i odporną na manipulacje pamięcią (tj. "secure element*"). Jak sama nazwa wskazuje, jego rolą jest przechowywanie fraz i haseł Bitcoin Mnemonic w zaszyfrowany i chroniony sposób. Dzięki Seedkeeper możesz generate, importować, organizować i zapisywać swoje sekrety bezpośrednio w bezpiecznym komponencie karty.



Moim zdaniem Seedkeeper ma dwa główne zastosowania, które omówimy w 2 osobnych poradnikach:




- Przechowywanie fraz Bitcoin** Mnemonic: zamiast zapisywać 12 lub 24 słowa na papierze, można zaimportować je na kartę inteligentną i zabezpieczyć kodem PIN.
- Zarządzanie hasłami**: za pośrednictwem aplikacji Seedkeeper można utworzyć 10 silnych haseł i przechowywać je bezpośrednio na karcie inteligentnej, uzyskując wygodny, łatwy w użyciu menedżer haseł offline.



Technicznie rzecz biorąc, Seedkeeper ma pojemność 8192 bajtów, co pozwala na przechowywanie co najmniej 50 oddzielnych sekretów (dokładna liczba będzie zależeć od ich rozmiaru i metadanych powiązanych z każdym z nich). Dostęp do Seedkeepera można uzyskać zarówno [za pośrednictwem czytnika kart inteligentnych podłączonego](https://satochip.io/accessories/) do komputera, jak i za pośrednictwem aplikacji mobilnej z połączeniem NFC. Cały system działa w trybie offline, bez połączenia z Internetem, gwarantując ograniczoną powierzchnię ataku.



![Image](assets/fr/001.webp)



Szczególnie interesującą funkcją jest możliwość duplikowania zawartości jednego Seedkeepera do drugiego w celu utworzenia kopii zapasowej. W tym poradniku pokażemy, jak to zrobić.



Seedkeeper jest również bardzo interesujący w połączeniu z bezstanowym Hardware Wallet, takim jak SeedSigner lub Specter DIY. W takim przypadku nie ma potrzeby korzystania z komputera lub klienta mobilnego Satochip. Seedkeeper przechowuje seed w swoim secure element i może być używany bezpośrednio z urządzeniem podpisującym, eliminując potrzebę stosowania papierowego kodu QR. Nie będę rozwijał tego konkretnego przypadku użycia w tym samouczku, ponieważ jest to temat innego dedykowanego samouczka:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Jaki przypadek użycia dla Seedkeeper?



W tym samouczku zajmę się tylko przypadkami użycia związanymi z Bitcoin, ponieważ o tym jest ten samouczek. Nie będziemy zagłębiać się w funkcjonalność zarządzania hasłami, która będzie przedmiotem innego samouczka.



W porównaniu do zwykłej papierowej kopii zapasowej frazy Mnemonic, korzystanie z Seedkeepera ma kilka zalet:





- Odporny na kradzież:** seed w Wallet nie jest dostępny w postaci czystego tekstu. Aby go wyodrębnić, należy znać kod PIN Seedkeeper. Złodziej, który wejdzie w posiadanie urządzenia, nie będzie w stanie nic z nim zrobić bez tego kodu.





- Rozłożenie ryzyka na dwa czynniki:** można podzielić bezpieczeństwo między czynnik cyfrowy i fizyczny. Na przykład, jeśli przechowujesz kod PIN Seedkeeper w menedżerze haseł, będziesz potrzebować zarówno dostępu do tego menedżera, jak i fizycznego posiadania karty elektronicznej, aby uzyskać seed (znacznie zmniejszone prawdopodobieństwo ataku).





- Scentralizowane zarządzanie:** Seedkeeper ułatwia zarządzanie wieloma nasionami z różnych portfeli.





- Łatwe tworzenie kopii zapasowych:** po prostu duplikuj zaszyfrowane kopie zapasowe do innych SeedKeeperów.



Istnieje jednak szereg wad w porównaniu z prostą papierową kopią zapasową seed:





- Cena:** choć skromna (około 25 euro), jest wciąż wyższa niż cena kartki papieru.





- Zależność od urządzenia komputerowego ogólnego przeznaczenia:** Wejście do seed i zarządzanie nim wymaga komputera lub smartfona, co oznacza, że Mnemonic przechodzi przez maszynę o znacznie szerszej powierzchni ataku niż Hardware Wallet. Może to stanowić zagrożenie, jeśli stacja robocza zostanie przejęta. Dlatego też nie zalecam używania Seedkeeper do przechowywania seed z Hardware Wallet (z wyjątkiem bezstanowego użycia bez komputera, jak w przypadku SeedSigner). Rolą Hardware Wallet jest właśnie przechowywanie seed w minimalistycznym, wysoce bezpiecznym środowisku. Ręczne wprowadzanie seed na zwykłym komputerze nie ogranicza go już do Hardware Wallet: trafia on również na maszynę ogólnego przeznaczenia, narażoną na wiele wektorów ataku. Dlatego lepiej jest używać Seedkeeper dla Hot Wallet niż Cold (z wyjątkiem SeedSigner / bezstanowego Hardware Wallet).





- Ryzyko utraty związane z kodem PIN:** bezpośredni brak dostępu do seed, w przeciwieństwie do papierowej kopii zapasowej, rzeczywiście zapewnia ochronę przed fizyczną kradzieżą. Jednak jak zawsze, bezpieczeństwo to balansowanie między ryzykiem kradzieży a ryzykiem utraty. Jeśli kopia zapasowa wymaga kodu PIN, utrata tego kodu uniemożliwi odzyskanie frazy Mnemonic, a tym samym dostęp do bitcoinów.



Biorąc pod uwagę te zalety i wady, uważam, że najlepszym zastosowaniem Seedkeepera (poza jego funkcją menedżera haseł) jest, z jednej strony, przechowywanie nasion z **portfeli oprogramowania**, ponieważ znajdują się one już na telefonie lub komputerze, lub z bezekranowych portfeli sprzętowych, takich jak Satochip, a z drugiej strony, używanie go w połączeniu z bezstanowym Hardware Wallet, takim jak SeedSigner, gdzie naprawdę się sprawdza.



Innym szczególnie interesującym przypadkiem użycia Seedkeeper jest możliwość bezpiecznego i niezawodnego tworzenia kopii zapasowych *Deskryptorów* portfeli.



## 2. Jak zdobyć Seedkeepera?



Istnieją dwa główne sposoby na zdobycie Seedkeepera. Możesz [kupić go bezpośrednio z oficjalnego sklepu Satochip](https://satochip.io/product/seedkeeper/) lub od autoryzowanego sprzedawcy. Ale ponieważ [aplet Seedkeeper jest open-source](https://github.com/Toporin/Seedkeeper-Applet), masz również możliwość zainstalowania go samodzielnie na [pustej karcie inteligentnej](https://satochip.io/product/blank-javacard-for-diy-project/).



Jeśli chcesz korzystać z funkcji tworzenia kopii zapasowych Seedkeeper, musisz oczywiście kupić dwie karty inteligentne.



## 3. Instalacja klienta Seedkeeper



W tym samouczku wykonamy kopię zapasową naszego portfela seed na naszym Seedkeeper. Pierwszym krokiem jest zainstalowanie oprogramowania na komputerze lub smartfonie. Na komputerze PC należy [pobrać najnowszą wersję Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Na urządzeniach mobilnych aplikacja Seedkeeper jest dostępna w [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper), a także w [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Inicjalizacja Seedkeepera



Uruchom aplikację i kliknij przycisk "*Kliknij i skanuj*".



![Image](assets/fr/003.webp)



Zostaniesz poproszony o podanie kodu PIN dla Seedkeeper. Ponieważ jest to nowa karta, kod PIN nie został jeszcze zdefiniowany. Wprowadź dowolny kod, aby pominąć ten krok, a następnie kliknij "*Next*".



![Image](assets/fr/004.webp)



Następnie umieść kartę z tyłu smartfona. Aplikacja wykryje, że Seedkeeper nie został jeszcze zainicjowany i wyświetli monit o ustawienie kodu PIN karty inteligentnej o długości od 4 do 16 znaków. Aby zapewnić optymalne bezpieczeństwo, należy wybrać silne hasło, które jest tak długie, jak to możliwe, losowe i składa się z wielu różnych znaków. Ten kod PIN jest jedyną barierą przed fizycznym dostępem do frazy odzyskiwania.



**Pamiętaj również o zapisaniu tego kodu PIN teraz**, na przykład w menedżerze haseł lub na oddzielnym nośniku fizycznym. W tym drugim przypadku nigdy nie przechowuj nośnika zawierającego PIN w tym samym miejscu co Seedkeeper, w przeciwnym razie zabezpieczenie stanie się bezużyteczne. Ważne jest, aby mieć niezawodną kopię zapasową: bez kodu PIN nie będzie można odzyskać sekretów przechowywanych w Seedkeeper.



![Image](assets/fr/005.webp)



Potwierdź kod PIN po raz drugi.



![Image](assets/fr/006.webp)



Urządzenie Seedkeeper zostało zainicjowane. Możesz go odblokować, wprowadzając właśnie ustawiony kod PIN.



![Image](assets/fr/007.webp)



Nastąpi przejście do strony zarządzania kartami inteligentnymi.



![Image](assets/fr/008.webp)



## 5. Zarejestruj seed na Seedkeeper



Po odblokowaniu Seedkeepera kliknij przycisk "*+*".



![Image](assets/fr/009.webp)



Wybierz opcję "Import secret*". Opcja "*generate secret*" umożliwia utworzenie nowej frazy Mnemonic bezpośrednio z poziomu aplikacji.



![Image](assets/fr/010.webp)



W naszym przypadku chcemy zapisać seed w naszym portfolio. Kliknij na "*Mnemonic*".



![Image](assets/fr/011.webp)



Przypisz "*Label*" do tego sekretu, aby można go było łatwo zidentyfikować, jeśli przechowujesz kilka informacji w Seedkeeper.



![Image](assets/fr/012.webp)



Następnie wprowadź frazę odzyskiwania w odpowiednim polu. Jeśli chcesz, możesz również dodać passphrase BIP39 lub *Deskryptory*. Następnie kliknij "Import*".



![Image](assets/fr/013.webp)



*Mnemonic wyświetlany na tym zdjęciu jest fikcyjny i nie należy do nikogo. To tylko przykład. Nigdy nie ujawniaj nikomu swojego własnego Mnemonic, w przeciwnym razie twoje bitcoiny zostaną skradzione



Umieść Seedkeeper z tyłu smartfona.



![Image](assets/fr/014.webp)



Twój seed został zarejestrowany.



![Image](assets/fr/015.webp)



## 6. Dostęp do seed na Seedkeeper



Jeśli chcesz sprawdzić swoją frazę Mnemonic, podnieś Seedkeeper i kliknij przycisk "*Click & Scan*".



![Image](assets/fr/016.webp)



Wprowadź kod PIN, a następnie naciśnij "*Next*".



![Image](assets/fr/017.webp)



Umieść Seedkeeper z tyłu smartfona.



![Image](assets/fr/018.webp)



Spowoduje to wyświetlenie listy wszystkich zarejestrowanych wpisów tajnych. W tym przykładzie chcę wyświetlić seed w moim portfolio "*BLOCKSTREAM App*", więc klikam na niego.



![Image](assets/fr/019.webp)



Naciśnij przycisk "*Reveal*".



![Image](assets/fr/020.webp)



Ponownie przeskanuj swój Seedkeeper.



![Image](assets/fr/021.webp)



Poprzednio nagrana fraza Mnemonic jest teraz wyświetlana na ekranie.



![Image](assets/fr/022.webp)



## 7. Tworzenie kopii zapasowej Seedkeeper



Wykonamy teraz kopię zapasową mojego Seedkeepera na drugim Seedkeeperze, aby mieć dwie kopie. Ta redundancja może być częścią strategii zabezpieczania bitcoinów: na przykład przechowywanie frazy w dwóch oddzielnych lokalizacjach w celu ograniczenia ryzyka fizycznego lub powierzenie kopii zaufanemu krewnemu w ramach planu dziedziczenia.



Aby to zrobić, zabierz ze sobą drugi Seedkeeper (pamiętaj, aby zidentyfikować jeden z dwóch za pomocą znaku na nim, aby uniknąć pomyłki). Zacznij od zainicjowania go, jak opisano w kroku 4 tego samouczka. Ponownie wybierz silne hasło. W zależności od strategii, możesz wybrać inne hasło lub zachować to samo.



![Image](assets/fr/023.webp)



Otwórz aplikację, kliknij "*Click & Scan*", wprowadź hasło Seedkeeper n°1 (źródło), a następnie zeskanuj je.



![Image](assets/fr/024.webp)



Spowoduje to przejście do strony głównej z listą sekretów. Kliknij trzy małe kropki w prawym górnym rogu Interface.



![Image](assets/fr/025.webp)



Wybierz "*Make a backup*", a następnie naciśnij "*Start*".



![Image](assets/fr/026.webp)



Wprowadź kod PIN karty zapasowej (Seedkeeper nr 2).



![Image](assets/fr/027.webp)



Następnie zeskanuj kartę.



![Image](assets/fr/028.webp)



Zrób to samo z główną kartą (Seedkeeper n°1), a następnie kliknij "*Make a backup*".



![Image](assets/fr/029.webp)



Seedkeeper n°2 zawiera teraz wszystkie sekrety przechowywane na Seedkeeper n°1.



![Image](assets/fr/030.webp)



Możesz zeskanować Seedkeeper n°2, aby sprawdzić, czy sekrety zostały skopiowane.



![Image](assets/fr/031.webp)



To już wszystko! Teraz już wiesz, jak używać Seedkeeper do przechowywania frazy Mnemonic Bitcoin Wallet. W przyszłym samouczku przyjrzymy się, jak używać Seedkeeper do przechowywania haseł. Zapraszam również do odkrycia jego połączonego zastosowania z SeedSigner :



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.network/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

W tym samouczku kilkakrotnie wspominaliśmy o ***Deskryptorach*** w portfolio Bitcoin. Nie wiesz, czym one są? W takim razie zalecamy skorzystanie z naszego bezpłatnego szkolenia CYP 201, które szczegółowo omawia wszystkie mechanizmy związane z obsługą portfeli HD!



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f