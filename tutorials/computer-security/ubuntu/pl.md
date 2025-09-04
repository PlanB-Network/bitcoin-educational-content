---
name: Ubuntu
description: Kompletny przewodnik po instalacji i używaniu Ubuntu jako alternatywy dla systemu Windows
---
![cover](assets/cover.webp)


## Wprowadzenie


System operacyjny (OS) to główne oprogramowanie, które zarządza wszystkimi zasobami komputera. Wybór alternatywnego systemu operacyjnego, takiego jak Ubuntu, może oferować wiele korzyści pod względem bezpieczeństwa, kosztów i prywatności.


### Dlaczego Ubuntu?




- Zwiększone bezpieczeństwo**: Dystrybucje Linuksa są znane ze swojego bezpieczeństwa i solidności
- Zero kosztów**: Ubuntu i większość dystrybucji Linuksa są bezpłatne
- Duża społeczność**: Społeczność użytkowników gotowych do pomocy za pośrednictwem forów i samouczków
- Poszanowanie prywatności**: System open source zapewniający większą przejrzystość
- Prostota**: Przyjazny dla użytkownika Interface i łatwość użytkowania
- Bogaty ekosystem**: Obszerny katalog oprogramowania open source
- Regularne wsparcie**: Bezpieczne aktualizacje od Canonical


## Instalacja i konfiguracja


### 1. Wymagania wstępne


**Wymagany sprzęt:**




- Klucz USB o pojemności co najmniej 12 GB
- Komputer z co najmniej 25 GB dostępnej pamięci


### 2. Pobierz




- Przejdź do [ubuntu.com/download](https://ubuntu.com/download)
- Wybierz wersję stabilną (zalecana LTS)
- Pobierz obraz ISO


![Page de téléchargement Ubuntu](assets/fr/01.webp)


![Sélection de la version Ubuntu](assets/fr/02.webp)


### 3. Utwórz bootowalny klucz USB


Możesz użyć kilku narzędzi, takich jak Balena Etcher:




- Pobierz i zainstaluj [Balena Etcher](https://etcher.balena.io/)


![Page de téléchargement Balena Etcher](assets/fr/03.webp)


![Installation de Balena Etcher](assets/fr/04.webp)




- Otwórz Balena Etcher, a następnie wybierz obraz ISO Ubuntu
- Wybierz klucz USB jako nośnik docelowy
- Kliknij Flash i poczekaj na zakończenie procesu


![Utilisation de Balena Etcher](assets/fr/05.webp)


### 4. Instalacja i zabezpieczanie Ubuntu


**4.1 Uruchamianie z pamięci USB** (w języku francuskim)




- Wyłącz komputer
- Podłącz klucz USB (zawierający Ubuntu)
- Włącz komputer. Na najnowszych komputerach system powinien automatycznie rozpoznać klucz rozruchowy USB. Jeśli tak się nie stanie, uruchom ponownie komputer, przytrzymując klawisz dostępu do BIOS/UEFI (zwykle F2, F12 lub Delete, w zależności od marki)
 - W menu BIOS/UEFI wybierz klucz USB jako urządzenie rozruchowe
 - Zapisz i uruchom ponownie


**4.2 Uruchamianie instalacji** (w języku francuskim)


**Ekran startowy**


Podczas uruchamiania z klucza USB zobaczysz ten ekran, który umożliwia uruchomienie Ubuntu.


![Écran de démarrage Ubuntu](assets/fr/06.webp)


**Wybór języka


Wybierz preferowany język instalacji i systemu.


![Sélection de la langue](assets/fr/07.webp)


**Opcje dostępności


W razie potrzeby skonfiguruj opcje dostępności (czytnik ekranu, wysoki kontrast itp.).


![Options d'accessibilité](assets/fr/08.webp)


**Konfiguracja klawiatury


Wybierz układ klawiatury. Dostępne jest pole testowe umożliwiające sprawdzenie, czy klawisze odpowiadają konfiguracji użytkownika.


![Configuration du clavier](assets/fr/09.webp)


**Połączenie sieciowe**


Połącz się z siecią Wi-Fi lub przewodową, aby pobrać aktualizacje podczas instalacji.


![Configuration réseau](assets/fr/10.webp)


**Typ instalacji


Wybierz pomiędzy "Wypróbuj Ubuntu" (aby przetestować bez instalacji) lub "Zainstaluj Ubuntu".


![Choix du type d'installation](assets/fr/11.webp)


**Metoda instalacji


Wybierz instalację interaktywną.


![Mode d'installation](assets/fr/12.webp)


**Wybór aplikacji


Wybierz pomiędzy domyślną instalacją lub rozszerzonym wyborem aplikacji.


![Sélection des applications](assets/fr/13.webp)


**Aplikacje innych firm


Zdecyduj, czy chcesz zainstalować dodatkowe sterowniki i zastrzeżone oprogramowanie.


![Installation applications tierces](assets/fr/14.webp)


**Typ podziału


Dostępne są dwie główne opcje:




- "Wymaż dysk i zainstaluj Ubuntu": używa całego dysku dla Ubuntu
- "Instalacja ręczna: utwórz podwójny rozruch z systemem Windows lub dostosuj partycje


![Choix du partitionnement](assets/fr/15.webp)


**Tworzenie konta użytkownika


Ustaw nazwę użytkownika i hasło do konta Ubuntu.


![Création du compte](assets/fr/16.webp)


**Strefa czasowa


Wybierz obszar geograficzny, aby ustawić czas systemowy.


![Sélection du fuseau horaire](assets/fr/17.webp)


**Podsumowanie instalacji**


Sprawdź wszystkie opcje przed rozpoczęciem ostatecznej instalacji. Po kliknięciu przycisku "Zainstaluj" rozpocznie się proces instalacji.


![Résumé de l'installation](assets/fr/18.webp)


**4.3 Aktualizacja Ubuntu po instalacji** (w języku francuskim)


Aktualizacja systemu jest ważnym krokiem po nowej instalacji. Dostępne są dwie opcje:


**Opcja 1: Za pośrednictwem graficznego użytkownika Interface**




- Wyszukaj "Oprogramowanie i aktualizacje" w menu aplikacji
- Aplikacja automatycznie sprawdzi dostępność aktualizacji
- Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby zainstalować aktualizacje


**Opcja 2: Przez terminal




- Otwórz terminal (Ctrl + Alt + T)
- Wpisz następujące polecenie, aby sprawdzić dostępność aktualizacji:


```bash
sudo apt update
```




- Po wyświetleniu monitu wprowadź hasło
- Aby zainstalować aktualizacje, wpisz:


```bash
sudo apt upgrade
```




- Potwierdź instalację, wpisując "Y", a następnie Enter


### 5. Odkrywanie podstawowych zadań


**5.1 Przeglądanie Internetu


Domyślnie Firefox często znajduje się na pasku uruchamiania.


Uruchom przeglądarkę Firefox i rozpocznij przeglądanie.


Inne przeglądarki (Chrome, Brave itp.) można zainstalować za pomocą Menedżera oprogramowania lub pakietów .deb.


**5.2 Przetwarzanie tekstu


Ubuntu jest dostarczane z pakietem LibreOffice (Writer do edycji tekstu).


Aby go otworzyć: Działania > Wyszukaj "LibreOffice Writer" lub kliknij ikonę, jeśli pojawi się na pasku.


Możesz tworzyć, edytować i zapisywać dokumenty w różnych formatach (w tym .docx).


**5.3 Instalowanie aplikacji


Menedżer oprogramowania (nazywany "Ubuntu Software"): graficzny Interface do wyszukiwania i instalowania aplikacji.


W terminalu użyj polecenia:


```bash
sudo apt install nom-du-paquet
```


Przykład:


```bash
sudo apt install vlc
```


### 6. Wnioski i dodatkowe zasoby


Teraz jesteś gotowy do codziennego korzystania z Ubuntu: zabezpiecz swój system, przeglądaj strony, wykonuj prace biurowe, instaluj oprogramowanie i aktualizuj swój system operacyjny!


Aby zwiększyć bezpieczeństwo swojego cyfrowego życia, zalecamy zapoznanie się z naszą usługą szyfrowanych wiadomości, która doskonale nadaje się do ochrony prywatności i uzupełnia instalację Ubuntu:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2