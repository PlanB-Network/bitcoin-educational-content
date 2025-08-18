---
name: Picocrypt
description: Narzędzie open source do szyfrowania danych
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana BURNELA opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Wprowadzono zmiany w oryginalnej treści.*



___



## I. Prezentacja



W tym samouczku przyjrzymy się Picocrypt, prostemu, lekkiemu i skutecznemu oprogramowaniu do szyfrowania danych o wysokim poziomie bezpieczeństwa.



Nadaje się do **szyfrowania plików**, można go używać do ochrony **danych na komputerze, na pamięci USB**, ale także danych przechowywanych w chmurze. Na przykład można szyfrować dane i przechowywać je na **Microsoft OneDrive, Google Drive, iCloud lub Dropbox**, chociaż do tego celu wolę inne oprogramowanie, które zostanie przedstawione w przyszłym artykule.



Możesz go również użyć, gdy musisz **udostępnić dane osobom trzecim**: dzięki Picocrypt i kluczowi deszyfrującemu będą one w stanie odszyfrować dane na swoim komputerze. Jeśli więc Twoje konto lub komputer zostaną przejęte, Twoje dane będą chronione.



Aby śledzić projekt Picocrypt, istnieje tylko jeden Address:





- [Picocrypt na GitHub](https://github.com/Picocrypt/Picocrypt)



Całkowicie **wolny i open source**, PicoCrypt jest dostępny dla **Windows**, **Linux** i **macOS**. W systemie Windows można go zainstalować na własnym komputerze lub skorzystać z wersji przenośnej.



## II. Picocrypt, oprogramowanie szyfrujące typu open source



Oprogramowanie szyfrujące Picocrypt** przedstawia się jako **alternatywa** dla innych znanych rozwiązań, takich jak **VeraCrypt** i **Cryptomator** (*przeznaczone do szyfrowania danych w środowiskach chmurowych*), czy **AxCrypt**. Nawiasem mówiąc, na oficjalnym GitHubie Picocrypt można znaleźć porównanie z niektórymi konkurentami:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Źródło: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt jest **bardzo lekki**, waży zaledwie **3 MB** i nie wymaga instalacji: jest to **przenośna aplikacja** z tą zaletą, że nie wymaga uprawnień administratora! Nie zaniedbuje jednak bezpieczeństwa, ponieważ opiera się na **solidnych i niezawodnych algorytmach**:





- Algorytm szyfrowania XChaCha20**
- Funkcja obejścia klucza **Argon2**



Poza wymienionymi zaletami, to co naprawdę przemawia za tym rozwiązaniem to **łatwość obsługi**!



Potrzebuje tylko jednej rzeczy: **audytu kodu**, ale to jest zaplanowane, jak widać w tabeli porównawczej powyżej (ostatni wiersz). Ale ponieważ jest to oprogramowanie open source, nic nie stoi na przeszkodzie, aby przyjrzeć się jego kodowi źródłowemu.



Chociaż w powyższej tabeli jest on porównywany do BitLockera, **moim zdaniem BitLocker i Picocrypt są przeznaczone do różnych zastosowań**: BitLocker do szyfrowania całego woluminu (na przykład systemu Windows), a Picocrypt do szyfrowania struktury drzewa lub przestrzeni dyskowej typu "Dysk".



## III. Korzystanie z Picocrypt



Do tej demonstracji zostanie użyty komputer z systemem Windows 11.



### A. Szyfrowanie danych za pomocą Picocrypt



Przede wszystkim należy pobrać plik Picocrypt.exe z oficjalnego serwisu GitHub ([zobacz tę stronę](https://github.com/Picocrypt/Picocrypt/releases)).



Otwórz aplikację, aby wyświetlić minimalistyczny Interface na ekranie. Aby zaszyfrować dane, czy to **plik, kilka plików lub folder**, wystarczy **przeciągnąć i upuścić je w Interface Picocrypt**. Spowoduje to wybranie danych do zaszyfrowania.



![Image](assets/fr/020.webp)



Następnie, w przypadku szyfrowania danych, masz dostęp do kilku opcji, w tym klucza szyfrowania. Może to być **silne hasło** lub **klucz szyfrujący w postaci pliku klucza**, lub **obydwa**. Jeśli weźmiemy przykład hasła, mamy wybór między utworzeniem własnego hasła lub wygenerowaniem hasła za pomocą Picocrypt.



Hasło to musi być silne, ponieważ może zostać użyte do odszyfrowania danych. Wprowadź je w "**Hasło**" i "**Potwierdź hasło**", a następnie kliknij "**Szyfruj**", aby zaszyfrować dane! Wcześniej możesz kliknąć przycisk "**Zmień**" obok "**Zapisz dane wyjściowe jako**", aby określić katalog wyjściowy.



**Uwaga**: aby użyć klucza w formacie pliku, kliknij "**Create**" po prawej stronie "**Keyfiles**", aby utworzyć klucz. Następnie wybierz go, klikając "**Edit**" i przeciągając plik klucza do odpowiedniego obszaru.



![Image](assets/fr/019.webp)



Dwa wybrane pliki są **szyfrowane i zgrupowane razem** w pliku "**Encrypted.zip.pcv**", ponieważ **PCV** jest rozszerzeniem używanym przez Picocrypt. Ten plik ZIP jest nieczytelny dzięki szyfrowaniu. Aby zapobiec grupowaniu wybranych plików w jednym zaszyfrowanym pliku ZIP, należy zaznaczyć opcję "**Recursively**", tak aby było tyle zaszyfrowanych plików, ile jest plików do zaszyfrowania.



Aby uzyskać dostęp do naszych danych, musimy je odszyfrować za pomocą Picocrypt.



![Image](assets/fr/023.webp)



Zanim porozmawiamy o odszyfrowywaniu danych, oto kilka informacji o niektórych dostępnych opcjach:





- Tryb paranoidalny**: korzystanie z najwyższego poziomu bezpieczeństwa oferowanego przez Picocrypt. Narzędzie będzie używać kilku kaskadowych algorytmów szyfrowania (XChaCha20 i Serpent) oraz HMAC-SHA3 zamiast BLAKE2b do uwierzytelniania danych.
- Reed-Solomon**: implementacja kodów korekcji błędów *Reed-Solomon* w celu ułatwienia korekcji błędów w uszkodzonych danych. Pozwala to na obsługę poziomu uszkodzenia około 3% pliku.
- Split into chunks** lub **divide into several parts**: jeśli szyfrujesz duży plik, możesz poprosić Picocrypt o podzielenie go na kilka części. Może to ułatwić przesyłanie pliku.
- Kompresuj pliki** lub **Kompresuj pliki**: kompresuje pliki w celu zmniejszenia rozmiaru zaszyfrowanych plików.
- Usunięte pliki** lub **Fichiers supprimés**: usuń pliki źródłowe, aby zachować tylko zaszyfrowaną wersję



### B. Odszyfrowywanie danych za pomocą Picocrypt



Odszyfrowanie danych nie jest skomplikowane, podobnie jak ich zaszyfrowanie. Wystarczy otworzyć Picocrypt i **przeciągnąć i upuścić plik PCV do odszyfrowania**. Następnie wprowadź hasło i/lub wybierz plik klucza przed kliknięciem "**Decrypt**".



![Image](assets/fr/021.webp)



Niezaszyfrowana wersja archiwum ZIP "Encrypted.zip" pozwala mi teraz odzyskać moje dwa pliki w postaci czystego tekstu!



![Image](assets/fr/022.webp)



## IV. Wnioski



**Zostałeś ostrzeżony: Picocrypt jest bardzo łatwy w użyciu i działa! Chociaż Interface jest minimalistyczny, zawiera kilka bardzo przydatnych opcji dostosowywania szyfrowania! A ponieważ jest dostępny w wersji przenośnej, możesz zabrać go ze sobą, gdziekolwiek jesteś, abyś mógł odszyfrować swoje dane z pewnością**



Pamiętaj, aby używać silnych haseł do ochrony danych, a jeśli używasz pliku klucza, musisz pamiętać o utworzeniu jego kopii zapasowej, w przeciwnym razie nie będziesz już w stanie odszyfrować kontenera PCV wygenerowanego przez Picocrypt. Wreszcie, warto wiedzieć, że istnieje również [wersja CLI](https://github.com/Picocrypt/CLI) (z mniejszą liczbą funkcji), która pozwala uruchamiać Picocrypt z wiersza poleceń: tutaj ponownie Picocrypt otwiera drzwi do nowych możliwości.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5