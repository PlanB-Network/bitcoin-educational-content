---
name: Tox
description: Otwieranie rozmów bez pośredników na zdecentralizowanym protokole Tox
---
![cover](assets/cover.webp)



Szyfrowanie end-to-end to usługa oferowana przez wiele aplikacji do przesyłania wiadomości, takich jak WhatsApp i Telegram. Szyfrowanie oznacza tutaj, że zanim wiadomość zostanie wysłana przez nadawcę, jest ona zabezpieczona zamkiem kryptograficznym, do którego klucz ma tylko odbiorca. Dzisiaj odkryjemy całkowicie zdecentralizowaną, szyfrowaną aplikację do przesyłania wiadomości, opartą na zasadach podobnych do Blockchain, oferującą bezpieczną, szyfrowaną komunikację typu end-to-end bez pośredników: Tox Chat.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = szyfrowanie typu end-to-end*



## Co to jest Tox?



Tox to darmowy (open source), zdecentralizowany protokół komunikacyjny, który wykorzystuje technologię *Networking and Cryptography Library* (NaCl) oraz kombinacje algorytmów szyfrowania w celu zapewnienia bezpieczeństwa i poufności swoim użytkownikom. Tox umożliwia wysyłanie wiadomości tekstowych Exchange, wykonywanie połączeń audio i wideo, udostępnianie plików i udostępnianie ekranu znajomym w sposób bezpieczny, zdecentralizowany i bez pośredników.



Technologia wykorzystywana przez protokół Tox jest podobna do sieci peer-to-peer, takich jak blockchain, co sprzyja decentralizacji infrastruktury protokołu. W przeciwieństwie do sieci społecznościowych i szyfrowanych aplikacji do przesyłania wiadomości typu end-to-end, aplikacja Tox Chat jest zbudowana na zdecentralizowanym protokole, który nie ma centralnego serwera. Wszyscy użytkownicy komunikują się w wolnej od pośredników, odpornej na cenzurę sieci peer-to-peer. Aby się komunikować, każdy użytkownik jest identyfikowany przez unikalny identyfikator (ToxID) pochodzący z jego klucza publicznego, który jest przechowywany w rozproszonej tabeli Hash.



## Join Tox



Z protokołu Tox można korzystać za pośrednictwem klienta wiadomości błyskawicznych, który można pobrać ze strony [Tox Chat site](https://tox.chat).



![download](assets/fr/01.webp)



W zależności od systemu operacyjnego można pobrać i zainstalować klienta Tox, który pasuje do :





- aTox: [aTox](https://github.com/evilcorpltd/aTox), klient Tox napisany w Kotlinie dostępny tylko na Androida



![aTox](assets/fr/02.webp)





- qTox: Klient Tox z [open source](https://github.com/TokTok/qTox) oparty na Qt Framework (C++) dostępny na Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) to klient Tox napisany w języku C i działający na systemach z interfejsem wiersza poleceń.



![Toxic](assets/fr/04.webp)



W tym samouczku użyjemy klientów qTox w systemie Windows i aTox do komunikacji.



## Rozpoczęcie pracy z qTox



Po pobraniu zainstaluj klienta Tox i utwórz swój profil.



![qTox-acount](assets/fr/05.webp)



Gratulacje, właśnie dołączyłeś do protokołu Tox. W oprogramowaniu qTox możesz znaleźć informacje o swoim profilu, klikając nazwę użytkownika.



![profil](assets/fr/06.webp)



W szczególności znajdziesz swój identyfikator Tox ID, który możesz zapisać jako kod QR i udostępnić osobom, które chcą się z Tobą skontaktować.



Wyeksportuj plik profilu Tox, aby mieć kopię zapasową swojego profilu i informacji kontaktowych, których możesz użyć do przywrócenia. Kliknij przycisk **Eksportuj**, a następnie wybierz ścieżkę do pliku kopii zapasowej.



![export](assets/fr/07.webp)



W menu **Więcej** możesz dodawać znajomych, importować kontakty i zarządzać otrzymywanymi zaproszeniami do znajomych.



![friends](assets/fr/08.webp)



Możesz skontaktować się ze mną na przykład za pośrednictwem tego Tox ID: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Po wysłaniu zaproszenia do grona znajomych odbiorca będzie musiał je zaakceptować lub odrzucić, zanim będzie można się z nim skontaktować.



![request](assets/fr/09.webp)



Klient Tox zawiera wszystkie opcje oferowane przez komunikatory internetowe:





- Połączenia wideo





- Połączenia głosowe





- Udostępnianie plików





- emotikony



![chat](assets/fr/10.webp)



### Grupy peer-to-peer



Klienci Tox umożliwiają również komunikację z grupą osób w całkowicie zdecentralizowany sposób: są to tzw. konferencje. W menu **Groups** utwórz nową konferencję lub sprawdź listę otrzymanych zaproszeń do dołączenia do konferencji.



![conferences](assets/fr/11.webp)



Po utworzeniu konferencji można zaprosić do niej znajomych w kliencie Tox. Na liście znajomych kliknij prawym przyciskiem myszy nazwę użytkownika znajomego, którego chcesz zaprosić. Kliknij opcję **Zaproś do konferencji**, a następnie wybierz nazwę utworzonej konferencji. Możesz również zaprosić znajomego poprzez domyślne utworzenie konferencji za pomocą opcji **Utwórz nową konferencję**.



klienty ⚠️ Tox są nadal w fazie rozwoju, więc podczas interakcji z oprogramowaniem mogą wystąpić błędy. Funkcje konferencji i połączeń wideo nie są jeszcze dostępne w kliencie Tox Android (aTox).



![invite](assets/fr/12.webp)



### Transfery plików



W menu **Przekazywanie plików** znajduje się historia wysłanych i otrzymanych plików od kontaktów.



![files](assets/fr/13.webp)



Możesz także dostosować konfiguracje udostępniania plików dla każdej prowadzonej dyskusji. Kliknij prawym przyciskiem myszy nazwę użytkownika odbiorcy i wybierz "Pokaż więcej szczegółów".



![details](assets/fr/14.webp)



W szczegółach Interface można zarządzać uprawnieniami przyznanymi odbiorcy dla :





- Automatyczna akceptacja zaproszeń na konferencje.





- Automatyczna akceptacja plików.





- Ścieżki kopii zapasowych plików dyskusji.



![permissions](assets/fr/15.webp)



### Więcej parametrów



W menu **Ustawienia** można dostosować ustawienia klienta Tox.





- W sekcji **Ogólne** zmień podstawowy język klienta Tox, zdefiniuj ścieżki kopii zapasowych plików i maksymalny rozmiar pliku, który ma być akceptowany automatycznie.



![general](assets/fr/16.webp)





- W sekcji **Użytkownik Interface** zmodyfikuj czcionki i rozmiary wiadomości. Możesz także zmienić motyw klienta Tox.



![ui](assets/fr/17.webp)





- Zakładka **Prywatność** pozwala zdefiniować efemeryczne wiadomości poprzez odznaczenie pola "Zachowaj historię czatu". Możesz także zmienić swój kod Nospam, gdy zauważysz, że jesteś spamowany zaproszeniami do znajomych, klikając przycisk "generate losowy kod NoSpam".



![privacy](assets/fr/18.webp)



### Co gwarantuje poufność na Tox?



Protokół Tox wykorzystuje rozproszoną tabelę Hash do tworzenia sieci zdecentralizowanych węzłów. Każdy klient Tox jest częścią sieci DHT i przechowuje informacje o innych węzłach. W przypadku Tox, DHT przechowuje adresy IP jako wartości powiązane z kluczami publicznymi Tox (Tox ID). Ułatwia to wyszukiwanie urządzenia klienta Tox bez konieczności odpytywania centralnego serwera.



Wyobraźmy sobie, że piszemy do naszego użytkownika `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F`, którego nazwiemy **użytkownikiem B**. Klient Tox zlokalizuje ten identyfikator w tabeli Hash Distributed i pobierze powiązany adres IP Address. Po znalezieniu adresu IP Address klient Tox utworzy bezpośredni, szyfrowany kanał komunikacyjny z maszyną naszego **użytkownika B** lub użyje innych węzłów jako przekaźników, aby dotrzeć do **użytkownika B**. Algorytmy szyfrowania zapewniają, że niezależnie od kanału komunikacji, tylko **użytkownik B** będzie w stanie odczytać treść wiadomości.



Jeśli podobało ci się odkrywanie Toxa i byłeś w stanie zrozumieć, w jaki sposób jest on przydatny do wzmocnienia twojej prywatności, prosimy o kciuki w górę. Polecamy również nasz poradnik na temat Simple Login, narzędzia, które pozwala anonimowo odbierać i wysyłać wiadomości e-mail.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41