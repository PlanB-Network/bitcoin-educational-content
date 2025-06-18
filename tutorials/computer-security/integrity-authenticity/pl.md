---
name: GnuPG
description: Jak zweryfikować integralność i autentyczność oprogramowania?
---
![cover](assets/cover.webp)


Podczas pobierania oprogramowania bardzo ważne jest, aby upewnić się, że nie zostało ono zmienione i rzeczywiście pochodzi z oficjalnego źródła. Jest to szczególnie ważne w przypadku oprogramowania związanego z Bitcoin, takiego jak oprogramowanie Wallet, które pozwala zabezpieczyć klucze dające dostęp do funduszy. W tym samouczku zobaczymy, jak zweryfikować integralność i autentyczność oprogramowania przed jego zainstalowaniem. Jako przykładu użyjemy Sparrow Wallet, ulubionego oprogramowania Wallet wśród bitcoinerów, ale procedura będzie taka sama dla każdego innego oprogramowania.


Weryfikacja integralności polega na upewnieniu się, że pobrany plik nie został zmodyfikowany poprzez porównanie jego cyfrowego odcisku palca (tj. Hash) z tym dostarczonym przez oficjalnego dewelopera. Jeśli oba są zgodne, oznacza to, że plik jest identyczny z oryginałem i nie został uszkodzony ani zmodyfikowany przez atakującego.


Z drugiej strony, weryfikacja autentyczności zapewnia, że plik rzeczywiście pochodzi od oficjalnego dewelopera, a nie od oszusta. Odbywa się to poprzez weryfikację podpisu cyfrowego. Podpis ten dowodzi, że oprogramowanie zostało podpisane kluczem prywatnym legalnego dewelopera.


Jeśli te kontrole nie zostaną przeprowadzone, istnieje ryzyko zainstalowania złośliwego oprogramowania, które może zawierać zmodyfikowany kod. Kod ten może wykraść informacje, takie jak klucze prywatne, lub zablokować dostęp do plików. Ten rodzaj ataku jest dość powszechny, zwłaszcza w kontekście oprogramowania open source, w którym mogą być rozpowszechniane fałszywe wersje.


Aby przeprowadzić tę weryfikację, użyjemy dwóch narzędzi: funkcji haszujących do weryfikacji integralności oraz GnuPG, narzędzia typu open source, które implementuje protokół PGP, do weryfikacji autentyczności.


## Wymagania wstępne


Jeśli korzystasz z **Linux**, GPG jest preinstalowany w większości dystrybucji. Jeśli nie, można go zainstalować za pomocą następującego polecenia:


```bash
sudo apt install gnupg
```


W przypadku **macOS**, jeśli nie zainstalowałeś jeszcze menedżera pakietów Homebrew, zrób to za pomocą poniższych poleceń:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


Następnie zainstaluj GPG za pomocą tego polecenia:


```bash
brew install gnupg
```

Dla **Windows**, jeśli nie masz GPG, możesz zainstalować oprogramowanie [Gpg4win](https://www.gpg4win.org/).

![GnuPG](assets/notext/01.webp)


## Pobieranie dokumentów


Aby rozpocząć, będziemy potrzebować różnych dokumentów. Odwiedź oficjalną stronę [Sparrow Wallet w sekcji "*Download*"](https://sparrowwallet.com/download/). Jeśli chcesz zweryfikować inne oprogramowanie, przejdź do jego strony internetowej.


![GnuPG](assets/notext/02.webp)


Możesz również przejść [do repozytorium GitHub projektu] (https://github.com/sparrowwallet/sparrow/releases).


![GnuPG](assets/notext/03.webp)


Pobierz instalator oprogramowania odpowiadającego Twojemu systemowi operacyjnemu.


![GnuPG](assets/notext/04.webp)


Potrzebny będzie również Hash pliku, często nazywany "*SHA256SUMS*" lub "*MANIFEST*".


![GnuPG](assets/notext/05.webp)


Pobierz również podpis PGP pliku. Jest to dokument w formacie `.asc`.


![GnuPG](assets/notext/06.webp)


Upewnij się, że wszystkie te pliki znajdują się w tym samym folderze na potrzeby kolejnych kroków.


Na koniec potrzebny będzie klucz publiczny dewelopera, którego użyjemy do weryfikacji podpisu PGP. Klucz ten jest często dostępny na stronie internetowej oprogramowania, w repozytorium GitHub projektu, czasami w mediach społecznościowych dewelopera lub na wyspecjalizowanych stronach, takich jak Keybase. W przypadku Sparrow Wallet, klucz publiczny dewelopera Craiga Raw można znaleźć [na Keybase](https://keybase.io/craigraw). Aby pobrać go bezpośrednio z terminala, wykonaj polecenie:


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## Weryfikacja podpisu


Proces weryfikacji podpisu jest taki sam w systemach **Windows**, **macOS** i **Linux**. Zwykle klucz publiczny został już zaimportowany w poprzednim kroku, ale jeśli nie, należy to zrobić za pomocą polecenia:


```bash
gpg --import [key path]
```


Zastąp `[ścieżka klucza]` lokalizacją pliku klucza publicznego dewelopera.


![GnuPG](assets/notext/08.webp)


Zweryfikuj podpis za pomocą następującego polecenia:


```bash
gpg --verify [file.asc]
```


Zastąp `[file.asc]` ścieżką do pliku podpisu. W przypadku Sparrow, plik ten nazywa się "*sparrow-2.0.0-manifest.txt.asc*" dla wersji 2.0.0.


![GnuPG](assets/notext/09.webp)


Jeśli podpis jest ważny, GPG wskaże to użytkownikowi. Możesz wtedy przejść do następnego kroku, ponieważ potwierdza to autentyczność pliku.


![GnuPG](assets/notext/10.webp)


## Weryfikacja Hash

Teraz, gdy autentyczność oprogramowania została potwierdzona, konieczne jest również zweryfikowanie jego integralności. Porównamy Hash oprogramowania z Hash dostarczonym przez dewelopera. Jeśli oba się zgadzają, gwarantuje to, że kod oprogramowania nie został zmieniony.


W systemie **Windows** otwórz terminal i wykonaj następujące polecenie:


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


Zastąp `[ścieżka pliku]` lokalizacją instalatora.


![GnuPG](assets/notext/11.webp)


Terminal zwróci Hash pobranego oprogramowania.


![GnuPG](assets/notext/12.webp)


Należy pamiętać, że w przypadku niektórych programów może być konieczne użycie innej funkcji Hash niż SHA256. W takim przypadku wystarczy zastąpić nazwę funkcji Hash w poleceniu.


Następnie porównaj wynik z odpowiednią wartością w pliku "*sparrow-2.0.0-manifest.txt*".


![GnuPG](assets/notext/13.webp)


W moim przypadku widzimy, że oba hashe idealnie do siebie pasują.


W systemach **macOS** i **Linux** proces weryfikacji Hash jest zautomatyzowany. Nie jest konieczne ręczne sprawdzanie zgodności między dwoma hashami, jak w systemie Windows.


Wystarczy wykonać to polecenie w systemie **macOS**:


```bash
shasum --check [file name] --ignore-missing
```


Zastąp `[nazwa pliku]` nazwą instalatora. Na przykład dla Sparrow Wallet:


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


Jeśli skróty są zgodne, powinny zostać wyświetlone następujące dane wyjściowe:


```bash
Sparrow-2.0.0.dmg: OK
```


W systemie **Linux** polecenie jest podobne:


```bash
sha256sum --check [file name] --ignore-missing
```


Jeśli skróty są zgodne, powinny zostać wyświetlone następujące dane wyjściowe:


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


Masz teraz pewność, że pobrane oprogramowanie jest autentyczne i nienaruszone. Możesz kontynuować jego instalację na swoim komputerze.


Jeśli ten poradnik okazał się pomocny, będę wdzięczny za kciuk w górę poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznanie się z tym innym samouczkiem na temat VeraCrypt, oprogramowania umożliwiającego szyfrowanie i odszyfrowywanie urządzeń pamięci masowej.


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5