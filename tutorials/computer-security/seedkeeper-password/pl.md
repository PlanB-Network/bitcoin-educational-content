---
name: Seedkeeper - Menedżer haseł
description: Jak zapisywać hasła za pomocą karty inteligentnej Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper to inteligentna karta opracowana przez Satochip, belgijską firmę specjalizującą się w rozwiązaniach sprzętowych do zarządzania i ochrony tajemnic cyfrowych. Znana ze swojej gamy kart elektronicznych dla ekosystemu Bitcoin, firma Satochip stworzyła Seedkeeper jako alternatywę dla tradycyjnych metod przechowywania fraz mnemonicznych i innych tajemnic cyfrowych.



Mówiąc konkretnie, Seedkeeper ma postać wielofunkcyjnej karty inteligentnej z certyfikatem EAL6 z bezpiecznym procesorem i odporną na manipulacje pamięcią (tzw. "Secure Element"). Jak sama nazwa wskazuje, jego rolą jest przechowywanie mnemoników i haseł portfela Bitcoin w zaszyfrowany i chroniony sposób. Dzięki Seedkeeper możesz generate, importować, organizować i zapisywać swoje sekrety bezpośrednio w bezpiecznym elemencie karty.



Moim zdaniem Seedkeeper ma dwa główne zastosowania, które omówimy w 2 osobnych poradnikach:




- Przechowywanie fraz mnemonicznych Bitcoin**: zamiast zapisywać 12 lub 24 słowa na papierze, można zaimportować je na kartę inteligentną i zabezpieczyć kodem PIN.
- Zarządzanie hasłami**: za pomocą aplikacji Seedkeeper można utworzyć 4 silne hasła i przechowywać je bezpośrednio na karcie inteligentnej, co zapewnia wygodny i łatwy w użyciu menedżer haseł offline.



Technicznie rzecz biorąc, Seedkeeper ma pojemność 8192 bajtów, co pozwala na przechowywanie co najmniej 50 oddzielnych sekretów (dokładna liczba będzie zależeć od ich rozmiaru i metadanych powiązanych z każdym z nich). Dostęp do Seedkeepera można uzyskać zarówno [za pośrednictwem czytnika kart inteligentnych podłączonego](https://satochip.io/accessories/) do komputera, jak i za pośrednictwem aplikacji mobilnej z połączeniem NFC. Cały system działa w trybie offline, bez połączenia z Internetem, gwarantując ograniczoną powierzchnię ataku.



![Image](assets/fr/001.webp)



Szczególnie interesującą funkcją jest możliwość duplikowania zawartości jednego Seedkeepera do drugiego w celu utworzenia kopii zapasowej. W tym poradniku pokażemy, jak to zrobić.



W tym samouczku omówimy tylko użycie SeedKeepera do tradycyjnych haseł, w sposób menedżera haseł. Jeśli chcesz użyć SeedKeeper do zapisywania fraz mnemonicznych Bitcoin wallet, zapoznaj się z tym innym samouczkiem:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Jak zdobyć Seedkeepera?



Istnieją dwa główne sposoby na zdobycie Seedkeepera. Możesz [kupić go bezpośrednio z oficjalnego sklepu Satochip](https://satochip.io/product/seedkeeper/) lub od autoryzowanego sprzedawcy. Ale ponieważ [aplet Seedkeeper jest open-source](https://github.com/Toporin/Seedkeeper-Applet), masz również możliwość zainstalowania go samodzielnie na [pustej karcie inteligentnej](https://satochip.io/product/blank-javacard-for-diy-project/).



Jeśli chcesz korzystać z funkcji tworzenia kopii zapasowych Seedkeeper, musisz oczywiście kupić dwie karty inteligentne.



## 2. Instalacja klienta Seedkeeper



Pierwszym krokiem jest zainstalowanie oprogramowania na komputerze lub smartfonie. Na komputerze PC należy [pobrać najnowszą wersję Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Na telefonach komórkowych aplikacja Seedkeeper jest dostępna w [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) i [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Inicjalizacja Seedkeepera



Uruchom aplikację i kliknij przycisk "*Kliknij i skanuj*".



![Image](assets/fr/003.webp)



Zostaniesz poproszony o podanie kodu PIN dla Seedkeeper. Ponieważ jest to nowa karta, kod PIN nie został jeszcze zdefiniowany. Wprowadź dowolny kod, aby pominąć ten krok, a następnie kliknij "*Next*".



![Image](assets/fr/004.webp)



Następnie umieść kartę z tyłu smartfona. Aplikacja wykryje, że Seedkeeper nie został jeszcze zainicjowany i wyświetli monit o ustawienie kodu PIN karty inteligentnej o długości od 4 do 16 znaków. Aby zapewnić optymalne bezpieczeństwo, należy wybrać solidny kod PIN, który jest jak najdłuższy, losowy i składa się z wielu różnych znaków. Ten kod PIN stanowi jedyną barierę przed fizycznym dostępem do haseł.



**Pamiętaj również o zapisaniu tego kodu PIN teraz**, na przykład w menedżerze haseł lub na oddzielnym nośniku fizycznym. W tym drugim przypadku nigdy nie przechowuj nośnika zawierającego PIN w tym samym miejscu co Seedkeeper, w przeciwnym razie zabezpieczenie stanie się bezużyteczne. Ważne jest, aby mieć niezawodną kopię zapasową: bez kodu PIN nie będzie można odzyskać sekretów przechowywanych w Seedkeeper.



![Image](assets/fr/005.webp)



Potwierdź kod PIN po raz drugi.



![Image](assets/fr/006.webp)



Urządzenie Seedkeeper zostało zainicjowane. Możesz go odblokować, wprowadzając właśnie ustawiony kod PIN.



![Image](assets/fr/007.webp)



Nastąpi przejście do strony zarządzania kartami inteligentnymi.



![Image](assets/fr/008.webp)



## 4. Zapisywanie haseł w Seedkeeper



Po odblokowaniu Seedkeepera kliknij przycisk "*+*".



![Image](assets/fr/009.webp)



Wybierz opcję "Generate secret*". Opcja "*Import a secret*" umożliwia zapisanie istniejącego hasła (na przykład hasła utworzonego w przeszłości).



![Image](assets/fr/010.webp)



W naszym przypadku chcemy zapisać hasło. Kliknij na "*Password*".



![Image](assets/fr/011.webp)



Przypisz "*Label*" do tego sekretu, aby można go było łatwo zidentyfikować, jeśli przechowujesz kilka informacji w Seedkeeper. Możesz również dodać identyfikator powiązany z hasłem i adresem URL witryny.



![Image](assets/fr/012.webp)



Wybierz długość i parametry hasła, a następnie kliknij "*Generate*", a następnie "*Import*".



![Image](assets/fr/013.webp)



Umieść Seedkeeper z tyłu smartfona.



![Image](assets/fr/014.webp)



Twoje hasło zostało zarejestrowane.



![Image](assets/fr/015.webp)



## 5. Uzyskaj dostęp do hasła Seedkeeper



Jeśli chcesz sprawdzić swoje hasło, weź Seedkeeper i kliknij przycisk "*Click & Scan*".



![Image](assets/fr/016.webp)



Wprowadź kod PIN, a następnie naciśnij "*Next*".



![Image](assets/fr/017.webp)



Umieść Seedkeeper z tyłu smartfona.



![Image](assets/fr/018.webp)



Spowoduje to wyświetlenie listy wszystkich zarejestrowanych haseł. W tym przykładzie chcę wyświetlić hasło do mojego konta Plan ₿ Academy, więc klikam na nie.



![Image](assets/fr/019.webp)



Naciśnij przycisk "*Reveal*".



![Image](assets/fr/020.webp)



Ponownie przeskanuj swój Seedkeeper.



![Image](assets/fr/021.webp)



Na ekranie pojawi się zapisane wcześniej hasło. Można je skopiować i użyć na odpowiedniej stronie internetowej.



![Image](assets/fr/022.webp)



## 6. Tworzenie kopii zapasowej Seedkeeper



Utworzymy teraz kopię zapasową mojego Seedkeepera na drugim Seedkeeperze, aby mieć dwie kopie. Ta redundancja może być częścią strategii zabezpieczania najważniejszych haseł: na przykład przechowywanie Seedkeeperów w 2 oddzielnych lokalizacjach w celu ograniczenia ryzyka fizycznego lub powierzenie kopii zaufanemu krewnemu.



Aby to zrobić, zabierz ze sobą drugi Seedkeeper (pamiętaj, aby zidentyfikować jeden z dwóch za pomocą znaku na nim, aby uniknąć pomyłki). Zacznij od zainicjowania go, jak opisano w kroku 3 tego samouczka. Ponownie wybierz silny kod PIN. W zależności od strategii możesz wybrać inny kod PIN lub zachować ten sam.



![Image](assets/fr/023.webp)



Otwórz aplikację, kliknij "*Click & Scan*", wprowadź kod PIN Seedkeeper n°1 (źródło), a następnie zeskanuj go.



![Image](assets/fr/024.webp)



Spowoduje to przejście do strony głównej z listą sekretów. Kliknij trzy małe kropki w prawym górnym rogu interfejsu.



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



To już wszystko! Teraz już wiesz, jak używać Seedkeeper do przechowywania haseł. W przyszłym samouczku przyjrzymy się, jak używać Seedkeeper do tworzenia kopii zapasowych Bitcoin wallet. Zapraszam również do odkrycia jego połączonego zastosowania z SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356