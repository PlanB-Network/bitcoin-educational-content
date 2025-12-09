---
name: Kali
description: Instalacja Kali Linux w VirtualBox, jako bootowalna pamięć USB lub jako podwójny rozruch, krok po kroku.
---

![cover-kali](assets/cover.webp)



## Wprowadzenie



### Dlaczego Kali Linux?



**Kali Linux** to dystrybucja Linuksa specjalizująca się w bezpieczeństwie IT.


Oto dlaczego używamy Kali Linux:





- Jest wstępnie skonfigurowany z szeroką gamą narzędzi do pentestingu (testy bezpieczeństwa systemu i sieci).
- Jest **open source i darmowy**, więc można go swobodnie używać i modyfikować.
- Jest **niezawodny i bezpieczny**, idealny do nauki o cyberbezpieczeństwie.
- Pozwala nauczyć się korzystać z systemu Linux w środowisku gotowym do testów.
- Można go zainstalować na różne sposoby: **VirtualBox**, **bootowalny klucz USB** lub **dual boot**.



## Instalacja i konfiguracja



### 1. Wymagania wstępne



**Wymagany sprzęt:**





- procesor 64-bitowy** (Intel lub AMD).
- co najmniej 8 GB pamięci RAM** (4 GB mogą być wystarczające dla lekkiej instalacji lub maszyny wirtualnej).
- 50 GB wolnego miejsca na dysku** do zainstalowania systemu Kali Linux.
- Połączenie internetowe** w celu pobrania obrazu ISO i aktualizacji.
- Klucz USB o pojemności co najmniej 8 GB** do utworzenia nośnika startowego (jeśli chcesz zainstalować Kali na komputerze lub przetestować go na Live USB).



Ważne jest, aby wykonać kopię zapasową danych przed instalacją na istniejącym komputerze.



### 2. Pobierz





- Przejdź do [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Wybierz obraz ISO dla swojej aplikacji:
  - Obraz instalacyjny** : do instalacji na komputerze PC.
  - Wirtualny obraz**: aby zainstalować Kali na VirtualBox lub VMware.
- Pobierz obraz ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Utwórz bootowalny klucz USB



Możesz użyć kilku narzędzi, takich jak Balena Etcher :





- Pobierz i zainstaluj [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Otwórz Balena Etcher, a następnie wybierz obraz ISO Kali.
- Wybierz klucz USB jako nośnik docelowy.
- Kliknij przycisk Flash i poczekaj na zakończenie procesu.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Instalowanie i zabezpieczanie systemu Kali Linux



#### 4.1 Uruchamianie z klucza USB





- Wyłącz komputer.
- Podłącz klucz USB (zawierający system Kali Linux).
- Włącz komputer. Na najnowszych komputerach system powinien automatycznie rozpoznać klucz rozruchowy USB. Jeśli tak się nie stanie, uruchom ponownie komputer, przytrzymując klawisz dostępu do BIOS/UEFI (zwykle F2, F12 lub Delete, w zależności od marki).
  - W menu BIOS/UEFI wybierz klucz USB jako urządzenie rozruchowe.
  - Zapisz i uruchom ponownie.



#### 4.2 Uruchomienie instalacji



##### Ekran startowy



Podczas uruchamiania z pamięci USB powinien pojawić się ekran startowy Kali Linux. Wybierz pomiędzy **instalacją graficzną** i **instalacją tekstową**. W tym przykładzie wybraliśmy instalację graficzną.



![capture](assets/fr/06.webp)



Jeśli użyjesz obrazu **Live**, zobaczysz inny tryb, **Live**, który jest również domyślną opcją uruchamiania.



![Mode Live](assets/fr/07.webp)



##### Wybór języka



Wybierz preferowany język instalacji i systemu.



![Sélection de la langue](assets/fr/08.webp)



Podaj swoją lokalizację geograficzną.



![Options d'accessibilité](assets/fr/09.webp)



##### Konfiguracja klawiatury



Wybierz układ klawiatury. Dostępne jest pole testowe umożliwiające sprawdzenie, czy klawisze odpowiadają konfiguracji użytkownika.



![Configuration du clavier](assets/fr/10.webp)



##### Połączenie sieciowe



Instalacja przeskanuje teraz interfejsy sieciowe, wyszuka usługę DHCP, a następnie wyświetli monit o wprowadzenie nazwy hosta dla systemu. W poniższym przykładzie wprowadziliśmy **"kali "** jako nazwę hosta.



![Configuration réseau](assets/fr/11.webp)



Opcjonalnie można podać domyślną nazwę domeny, która będzie używana przez ten system (wartości mogą być pobierane z DHCP lub jeśli istnieje wcześniej istniejący system operacyjny).



![Choix du type d'installation](assets/fr/12.webp)



##### Konta użytkowników



Następnie utwórz konto użytkownika dla systemu (pełna nazwa, nazwa użytkownika i silne hasło).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Strefa czasowa



Wybierz obszar geograficzny, aby ustawić czas systemowy.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Typ partycjonowania



Następnie instalator skanuje dyski i wyświetla kilka opcji w zależności od konfiguracji.



W tym przewodniku zaczynamy od **pustego dysku**, co daje **cztery możliwe wybory**.


Wybierzemy **Guided - użyj całego dysku**, ponieważ tutaj wykonujemy jednorazową instalację Kali Linux (pojedynczy rozruch). Oznacza to, że żaden inny system operacyjny nie zostanie zachowany, a cały dysk może zostać usunięty.



Jeśli dysk zawiera już dane, może zostać wyświetlona dodatkowa opcja **Guided - use largest contiguous free space**.



Ta alternatywa pozwala zainstalować Kali Linux bez usuwania istniejących danych, dzięki czemu idealnie nadaje się do podwójnego rozruchu z innym systemem.



W naszym przypadku dysk jest pusty, więc ta opcja się nie pojawia.



![Choix du partitionnement](assets/fr/17.webp)



Wybierz dysk, który ma zostać podzielony na partycje.



![capture](assets/fr/18.webp)



W zależności od potrzeb można wybrać przechowywanie wszystkich plików na jednej partycji (zachowanie domyślne) lub mieć oddzielne partycje dla jednego lub więcej katalogów najwyższego poziomu.



Jeśli nie jesteś pewien, czego chcesz, wybierz opcję **Wszystkie pliki na jednej partycji**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Będziesz miał wtedy ostatnią możliwość sprawdzenia konfiguracji dysku, zanim program instalacyjny wprowadzi jakiekolwiek nieodwracalne zmiany. Po kliknięciu na _Continue_, program instalacyjny uruchomi się i instalacja będzie prawie zakończona.



![capture](assets/fr/21.webp)



##### Szyfrowane LVM



Jeśli ta opcja została włączona w poprzednim kroku, Kali Linux wykona teraz bezpieczne wymazanie dysku twardego przed zapytaniem o hasło LVM.



Należy użyć silnego hasła, w przeciwnym razie zostanie wyświetlone ostrzeżenie o słabym haśle passphrase.



##### Informacje o pełnomocniku



Kali Linux używa repozytoriów do dystrybucji aplikacji. Będziesz musiał wprowadzić niezbędne informacje o serwerze proxy, jeśli twoje środowisko go używa.



Jeśli **nie jesteś pewien**, czy użyć proxy, **pozostaw puste**. Wprowadzenie fałszywych informacji uniemożliwi połączenie z repozytoriami.



![capture](assets/fr/22.webp)



##### Metapety



Jeśli dostęp do sieci nie został skonfigurowany, konieczna będzie **dalsza konfiguracja** po wyświetleniu monitu.



Jeśli używasz obrazu **Live**, następny krok nie zostanie wyświetlony.



Następnie możesz wybrać [metapakiety](https://www.kali.org/docs/general-use/metapackages/), które chcesz zainstalować. Domyślne opcje zainstalują standardowy system Kali Linux, więc nie będziesz musiał niczego modyfikować.



![capture](assets/fr/23.webp)



#### Informacje o uruchomieniu



Następnie potwierdź instalację programu ładującego GRUB.



![capture](assets/fr/24.webp)



##### Restart



Na koniec kliknij Kontynuuj, aby ponownie uruchomić nową instalację Kali Linux.



![capture](assets/fr/25.webp)



#### 4.3 Aktualizacja i konfiguracja Kali Linux po instalacji



Aktualizacja systemu jest ważnym krokiem po nowej instalacji. Dostępne są dwie opcje:



##### Opcja 1: Graficzny interfejs użytkownika (GUI)



Kali, podobnie jak Debian/Ubuntu, oferuje zintegrowany graficzny menedżer aktualizacji.



1. Kliknij na **menu główne** (w lewym górnym rogu lub na dole, w zależności od pulpitu).


2. Otwórz **"Software Updater "**.


3. Narzędzie to :




    - Sprawdź pakiety, które mają zostać zaktualizowane.
    - Wyświetli się lista (z rozmiarami i wersjami).
    - Umożliwia uruchomienie aktualizacji jednym kliknięciem.


4. Po wyświetleniu monitu wprowadź hasło administratora (`sudo`).


5. Pozwól mu się zainstalować i w razie potrzeby uruchom ponownie.



##### Opcja 2: Przez terminal



Otwórz terminal i uruchom :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Nie zaleca się używania konta **root** do codziennej pracy; zamiast tego należy utworzyć użytkownika innego niż root.



W terminalu wpisz następujące polecenia:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Wyloguj się i zaloguj ponownie jako nowy użytkownik.



Podsumujmy kilka podstawowych zadań Kali Linux w tabeli.



### Podstawowe zadania w systemie Kali Linux



| **Catégorie**              | **Tâche de base**                      | **Description / Objectif**                                 | **Méthode principale**                                       |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigation système**     | Ouvrir le terminal                     | Accéder à la ligne de commande principale de Kali          | Cliquez sur l’icône du terminal ou utilisez `Ctrl + Alt + T` |
|                            | Parcourir les dossiers                 | Se déplacer dans l’arborescence du système                 | `cd /chemin/du/dossier`, `ls` pour lister les fichiers       |
|                            | Créer / supprimer un dossier           | Organiser les fichiers                                     | `mkdir nom_dossier`, `rm -r nom_dossier`                     |
| **Gestion des fichiers**   | Copier / déplacer un fichier           | Manipuler des fichiers dans le terminal                    | `cp fichier destination`, `mv fichier destination`           |
|                            | Supprimer un fichier                   | Libérer de l’espace disque                                 | `rm nom_du_fichier`                                          |
|                            | Afficher le contenu d’un fichier texte | Lire rapidement un fichier                                 | `cat fichier.txt`, `less fichier.txt`                        |
| **Gestion du système**     | Mettre à jour Kali Linux               | Installer les dernières versions et correctifs de sécurité | `sudo apt update && sudo apt full-upgrade -y`                |
|                            | Installer un logiciel                  | Ajouter un nouvel outil ou utilitaire                      | `sudo apt install nom_du_paquet`                             |
|                            | Supprimer un logiciel                  | Nettoyer le système                                        | `sudo apt remove nom_du_paquet`                              |
|                            | Nettoyer les dépendances inutiles      | Gagner de l’espace disque                                  | `sudo apt autoremove`                                        |
| **Réseau et Internet**     | Vérifier la connexion réseau           | Tester l’accès à Internet                                  | `ping google.com`                                            |
|                            | Identifier l’adresse IP                | Connaître sa configuration réseau                          | `ip a` ou `ifconfig`                                         |
|                            | Changer de réseau Wi-Fi                | Se connecter à un autre point d’accès                      | Icône réseau → Sélectionner le Wi-Fi voulu                   |
| **Comptes et permissions** | Exécuter une commande administrateur   | Obtenir les droits root temporairement                     | `sudo commande`                                              |
|                            | Créer un nouvel utilisateur            | Ajouter un compte local                                    | `sudo adduser nom_utilisateur`                               |
|                            | Modifier un mot de passe               | Sécuriser un compte                                        | `passwd`                                                     |
| **Apparence et confort**   | Changer le fond d’écran                | Personnaliser le bureau                                    | Clic droit sur le bureau → **Paramètres du bureau**          |
|                            | Modifier le thème / icônes             | Améliorer la lisibilité et l’esthétique                    | Paramètres → Apparence / Thèmes                              |
| **Outils Kali**            | Ouvrir le menu des outils              | Explorer les outils de test et de sécurité                 | Menu **Applications → Kali Linux**                           |
|                            | Lancer un outil (ex : nmap, wireshark) | Découverte pratique des utilitaires de sécurité            | `sudo nmap`, `wireshark`, etc.                               |
| **Aide et documentation**  | Obtenir de l’aide sur une commande     | Comprendre une commande avant de l’utiliser                | `man commande` ou `commande --help`                          |

## Wnioski



Instalacja Kali Linux to tylko pierwszy krok w odkrywaniu tego potężnego środowiska dedykowanego cyberbezpieczeństwu. Opanowując podstawowe zadania i zarządzanie systemem, każdy może zacząć odkrywać wbudowane narzędzia i zrozumieć wewnętrzne działanie systemu Linux. Kali oferuje doskonałą platformę edukacyjną, zarówno do wzmacniania umiejętności technicznych, jak i rozwijania prawdziwej kultury bezpieczeństwa IT.