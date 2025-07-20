---
name: KeePass
description: Jak skonfigurować lokalny menedżer haseł?
---
![cover](assets/cover.webp)


W erze cyfrowej musimy zarządzać wieloma kontami online obejmującymi różne aspekty naszego codziennego życia, w tym bankowość, platformy finansowe, e-maile, przechowywanie plików, zdrowie, administrację, sieci społecznościowe, gry wideo itp.


Aby uwierzytelnić się na każdym z tych kont, używamy identyfikatora, często adresu e-mail Address, któremu towarzyszy hasło. W obliczu niemożności zapamiętania dużej liczby unikalnych haseł, można ulec pokusie ponownego użycia tego samego hasła lub nieznacznej modyfikacji wspólnej bazy, aby ułatwić jej zapamiętanie. Jednak takie praktyki poważnie zagrażają bezpieczeństwu kont.


Pierwszą zasadą, której należy przestrzegać w przypadku haseł, jest nieużywanie ich ponownie. Każde konto online powinno być chronione unikalnym i całkowicie odrębnym hasłem. Jest to ważne, ponieważ jeśli atakującemu uda się złamać jedno z twoich haseł, nie chcesz, aby miał dostęp do wszystkich twoich kont. Posiadanie unikalnego hasła dla każdego konta izoluje potencjalne ataki i ogranicza ich zakres. Na przykład, jeśli używasz tego samego hasła do platformy gier wideo i poczty e-mail, a hasło to zostanie złamane za pośrednictwem strony phishingowej związanej z platformą gier, atakujący może łatwo uzyskać dostęp do poczty e-mail i przejąć kontrolę nad wszystkimi innymi kontami online.


Drugą istotną zasadą jest siła hasła. Hasło jest uważane za silne, jeśli jest trudne do złamania, czyli odgadnięcia metodą prób i błędów. Oznacza to, że hasła muszą być jak najbardziej losowe, długie i zawierać różnorodne znaki (małe i wielkie litery, cyfry i symbole).


Stosowanie tych dwóch zasad bezpieczeństwa haseł (unikalność i solidność) może okazać się trudne w codziennym życiu, ponieważ zapamiętanie unikalnego, losowego i silnego hasła do wszystkich naszych kont jest prawie niemożliwe. W tym miejscu do gry wkracza menedżer haseł.


Menedżer haseł generuje i bezpiecznie przechowuje silne hasła, umożliwiając dostęp do wszystkich kont online bez konieczności ich indywidualnego zapamiętywania. Wystarczy zapamiętać tylko jedno hasło, hasło główne, które zapewnia dostęp do wszystkich haseł zapisanych w menedżerze. Korzystanie z menedżera haseł zwiększa bezpieczeństwo online, ponieważ zapobiega ponownemu użyciu haseł i systematycznie generuje losowe hasła. Upraszcza również codzienne korzystanie z kont poprzez scentralizowanie dostępu do poufnych informacji.

W tym poradniku dowiemy się, jak skonfigurować i używać lokalnego menedżera haseł w celu zwiększenia bezpieczeństwa online. Tutaj przedstawię ci KeePass. Jeśli jednak jesteś początkującym użytkownikiem i chciałbyś korzystać z menedżera haseł online z możliwością synchronizacji na wielu urządzeniach, polecam zapoznać się z naszym poradnikiem na temat Bitwarden:

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*Uwaga: Menedżer haseł jest świetny do przechowywania haseł, ale **nigdy nie należy przechowywać w nim frazy Mnemonic Bitcoin Wallet!** Pamiętaj, że fraza Mnemonic powinna być zapisana wyłącznie w formacie fizycznym, takim jak kawałek papieru lub metalu*


---

## Wprowadzenie do KeePass


KeePass to darmowy menedżer haseł o otwartym kodzie źródłowym, idealny dla tych, którzy chcą darmowego i bezpiecznego rozwiązania do lokalnego zarządzania. Jest to oprogramowanie do zainstalowania na komputerze, które bez dodania wtyczek nie komunikuje się z Internetem. Jest to diametralnie inne podejście niż w przypadku Bitwarden, o którym pisaliśmy w poprzednim poradniku. Bitwarden, w przeciwieństwie do KeePass, umożliwia synchronizację między wieloma urządzeniami, a zatem wymaga przechowywania haseł na serwerze online.


Domyślnie KeePass nie obsługuje rozszerzeń przeglądarki, takich jak Bitwarden, w związku z czym konieczne jest ręczne kopiowanie i wklejanie haseł z oprogramowania. Chociaż może się to wydawać ograniczeniem, kopiowanie i wklejanie haseł zamiast korzystania z automatycznego wypełniania jest dobrą praktyką dla bezpieczeństwa online.


KeePass został zaprojektowany tak, aby był lekki i łatwy w użyciu, a jednocześnie spełniał wysokie standardy bezpieczeństwa. Oprogramowanie szyfruje bazę danych lokalnie, zapewniając optymalną ochronę danych uwierzytelniających. KeePass jest również jedynym menedżerem haseł zatwierdzonym przez ANSSI (francuski organ ds. cyberbezpieczeństwa).


Jedną z głównych zalet KeePass jest jego elastyczność. Można go używać na wiele różnych sposobów, np. na pamięci USB bez konieczności instalacji na komputerze. Co więcej, dzięki [środowisku wtyczek] (https://keepass.info/plugins.html), KeePass można dostosować do bardziej specyficznych potrzeb.

![KEEPASS](assets/notext/01.webp)

## Jak pobrać KeePass?


Proces instalacji KeePass różni się w zależności od używanego systemu operacyjnego. W przypadku użytkowników systemów Windows lub Linux instalacja jest stosunkowo prosta. Jeśli jednak korzystasz z systemu macOS, konieczny jest dodatkowy krok ze względu na rozwój KeePass na platformie .NET, która nie jest bezpośrednio obsługiwana przez macOS. W związku z tym konieczne będzie skonfigurowanie kompatybilnego środowiska, aby umożliwić uruchamianie KeePass na urządzeniach Apple.


Użytkownicy Debiana/Ubuntu powinni otworzyć terminal i wprowadzić następujące polecenia:


```bash
sudo apt-get update

sudo apt-get install keepass2

```

For Fedora:

```

sudo dnf install keepass

```

For Arch Linux:

```

sudo pacman -S keepass

```

If you are on a Windows computer, go to the [official KeePass download page](https://keepass.info/download.html), and download the latest version of the installer:
![KEEPASS](assets/notext/02.webp)
Click on the downloaded file to run it, then follow the instructions of the setup wizard to complete the installation (see next section).

For macOS users, the installation is a bit more complex. If you wish to use the original version of KeePass as on Windows, follow the instructions below. Otherwise, you can opt for [KeePassXC](https://keepassxc.org/), an alternative version compatible with macOS, which offers a slightly different interface.

To use KeePass, you will need a runtime environment for .NET applications. I recommend installing Mono for this. Go to the [official Mono page](https://www.mono-project.com/download/stable/#download-mac) in the "*macOS*" section, and click on the link to download the installation package (`.pkg`).
![KEEPASS](assets/notext/03.webp)
Open the downloaded `.pkg` file and follow the instructions to install Mono on your Mac.
![KEEPASS](assets/notext/04.webp)
Next, go to the official KeePass website and download the latest portable version in `.zip` format.
![KEEPASS](assets/notext/05.webp)
After downloading the `.zip` file, double-click to extract it. You will get a folder containing several files, including `KeePass.exe`. Open a terminal, navigate to the KeePass folder (replace `xx` with the version number):

```

cd ~/Downloads/KeePass-2.xx

```

And finally, run KeePass with Mono:

```

mono KeePass.exe

```