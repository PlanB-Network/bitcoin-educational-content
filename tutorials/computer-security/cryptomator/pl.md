---
name: Cryptomator
description: Szyfrowanie plików w chmurze
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana BURNELA opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany.*



___



## I. Prezentacja



W tym poradniku użyjemy aplikacji Cryptomator do szyfrowania danych przechowywanych w chmurze, czy to na Microsoft OneDrive, Google Drive, Dropbox, Box, czy nawet iCloud.



Szyfrowanie danych przechowywanych w rozwiązaniach pamięci masowej online, takich jak Drive, to najlepszy sposób na ochronę plików i prywatności. Dzięki szyfrowaniu tylko Ty możesz odszyfrować i odczytać swoje dane, nawet jeśli są one przechowywane na serwerze w USA lub innym kraju na całym świecie.



W tej demonstracji zostanie użyty komputer z systemem Windows 11 22H2 i usługą OneDrive, ale procedura jest identyczna w przypadku innych wersji systemu Windows i innych usług pamięci masowej. Wystarczy zainstalować klienta synchronizacji i dodać swoje konto. Umożliwi to Cryptomatorowi przechowywanie danych w skarbcu.



![Image](assets/fr/020.webp)



Cryptomator jest alternatywą dla innych aplikacji, w szczególności Picocrypt przedstawionego w innym artykule, który wygląda inaczej, ale jest równie prosty w użyciu. Cryptomator jest również **open source**, zgodny z RGPD i **szyfruje dane za pomocą algorytmu szyfrowania AES-256 bitów**. Z kolei Picocrypt opiera się na szybszym algorytmie XChaCha20 (również 256-bitowym).



https://planb.network/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Aplikacja Cryptomator jest dostępna na **Windows** (exe / msi), **Linux**, **macOS,** ale także **Android** i **iOS**. Nawiasem mówiąc, wszystkie aplikacje są bezpłatne, z wyjątkiem aplikacji na Androida, za którą trzeba zapłacić (14,99 euro).



Na komputerze użytkownika **Cryptomator utworzy folder, w którym utworzy sejf**. W sejfie, który może być przechowywany na dysku OneDrive, Google Drive lub podobnym, dane zostaną zaszyfrowane. Tak więc, jeśli przechowujesz wszystkie swoje dane w sejfie hostowanym na Dysku, będą one chronione (ponieważ są zaszyfrowane).



**Uwaga**: w tym artykule usługi przechowywania danych online są używane jako przykład, ale Cryptomator może być używany do szyfrowania danych na dysku lokalnym, dysku zewnętrznym, a nawet NAS. W rzeczywistości nie ma żadnych ograniczeń.



## II. Instalacja programu Cryptomator



Aby rozpocząć, należy **pobrać** i **zainstalować** **Cryptomator**. Po zakończeniu pobierania wystarczy kilka kliknięć, aby zakończyć instalację. Podobnie jak [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), Cryptomator będzie polegał na WinFsp, aby **zamontować wirtualny dysk na komputerze z systemem Windows**.





- [Pobierz Cryptomator z oficjalnej strony internetowej](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Korzystanie z programu Cryptomator w systemie Windows



### A. Utwórz nowy sejf



Aby utworzyć nowy sejf, kliknij przycisk "**Dodaj**" i wybierz "**Nowy sejf...**". Istniejące i znane sejfy na tej maszynie pojawią się w Interface, po lewej stronie. **Sejf utworzony na maszynie A może być otwierany i modyfikowany na maszynie B**, pod warunkiem, że jest ona wyposażona w Cryptomator (a klucz szyfrowania jest znany).



![Image](assets/fr/015.webp)



Zacznij od nadania skarbcowi nazwy, np. "**IT-Connect**". Spowoduje to utworzenie katalogu o nazwie "**IT-Connect**" w moim OneDrive.



![Image](assets/fr/011.webp)



W następnym kroku Cryptomator prawdopodobnie **wykryje "Dysk "** obecny na twoim komputerze: Dysk Google, OneDrive, Dropbox itp.... Aby umożliwić bezpośredni wybór dostawcy. Próbowałem tego na dwóch różnych komputerach z Windows 11, z kilkoma dyskami i nie został wykryty. To nie problem, wystarczy zdefiniować "**Lokalizację niestandardową**" i wybrać katalog główny przestrzeni dyskowej. Na przykład: **C:\Users\<Username>\OneDrive**.



![Image](assets/fr/018.webp)



Następnie możesz dostosować opcję w ustawieniach eksperckich.



![Image](assets/fr/021.webp)



Następnie należy zdefiniować **hasło odpowiadające kluczowi szyfrowania**. Hasło to umożliwi **odblokowanie sejfu Cryptomator** i dostęp do jego danych. **Jeśli je utracisz, stracisz dostęp do swoich danych**. Wreszcie, nadal masz możliwość **utworzenia klucza zapasowego**, zaznaczając opcję "**Tak, lepiej bezpieczniej niż żałować**", w tym samym duchu, co klucz odzyskiwania [BitLocker] (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Jest to zalecane, ale nie przechowuj tego klucza zapasowego w katalogu głównym OneDrive!



Kliknij "**Utwórz sejf**".



![Image](assets/fr/019.webp)



Skopiuj klucz odzyskiwania i zapisz go w swoim ulubionym menedżerze haseł. Kliknij "**Next**".



![Image](assets/fr/013.webp)



To wszystko, twój nowy bagażnik został utworzony i jest gotowy do użycia!



![Image](assets/fr/014.webp)



### B. Dane dotyczące dostępu



Aby uzyskać dostęp do sejfu i jego danych, w celu **odczytania istniejących danych lub dodania nowych danych**, należy go **odblokować**. Cryptomator wyświetla listę znanych sejfów: pojawia się sejf IT-Connect, więc wystarczy go wybrać i kliknąć "**Odblokuj**".



![Image](assets/fr/016.webp)



Aby odblokować sejf, należy wprowadzić hasło. Następnie kliknij "**Release drive**".



![Image](assets/fr/022.webp)



**Twój sejf jest zamontowany na komputerze z systemem Windows jako dysk wirtualny.** Ten dysk, który tutaj dziedziczy literę E, daje ci dostęp do twoich danych (w postaci zwykłego tekstu, ponieważ sejf jest odblokowany).



![Image](assets/fr/017.webp)



Po stronie OneDrive nie możemy bezpośrednio przeglądać skarbca Cryptomator. Nie widzimy danych (ani nazw plików, ani ich zawartości). Oznacza to, że nie trzeba dodawać danych do skarbca Cryptomator za pomocą zwykłego skrótu OneDrive. **Musisz dodać swoje dane za pomocą wirtualnego dysku Cryptomator.**



![Image](assets/fr/012.webp)



### C. Opcje magistrali



Ustawienia sejfu są dostępne za pośrednictwem przycisku "**Opcje zaszyfrowanego woluminu**" (po zablokowaniu) i włączają automatyczne blokowanie w przypadku braku aktywności, podobnie jak w przypadku sejfu na hasło. Opcja "**Odblokuj zaszyfrowany wolumin przy uruchomieniu**", jak sama nazwa wskazuje, odblokowuje dysk bez żadnej interwencji z twojej strony i montuje dysk wirtualny. Ze względów bezpieczeństwa najlepiej jest unikać aktywowania tej opcji.



W zakładce "**Mounting**" można również zdecydować o zamontowaniu go tylko do odczytu lub przypisaniu określonej litery.



![Image](assets/fr/024.webp)



Dodatkowo, w ustawieniach Cryptomatora można **włączyć automatyczne uruchamianie aplikacji**.



## IV. Wnioski



Dzięki **Cryptomator** możesz **stworzyć zaszyfrowany sejf** w ciągu zaledwie kilku minut, aby chronić dane, które chcesz przechowywać na OneDrive i konsorcjach. Jest bardzo łatwy w użyciu, jeśli chodzi o "parowanie" go z dyskiem: w tym celu preferuję Picocrypt.