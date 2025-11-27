---
name: Alias Vault
description: Potężne narzędzie do zarządzania hasłami, uwierzytelnianiem dwuskładnikowym i aliasami (z wbudowanym serwerem poczty e-mail) - również hostowane samodzielnie!
---

![cover](assets/cover.webp)



Prywatność i bezpieczeństwo online to temat, na który każdy, niezależnie od prowadzonej działalności, powinien zwrócić szczególną uwagę.



Kwestie te są ponadto częścią świata w ciągłym zamieszaniu: coraz więcej deweloperów uczestniczy w temacie, wprowadzając implementacje do ustalonych rozwiązań i nowych produktów.



Tak jest w przypadku **Leenderta de Borst** i jego `Alias Vault`, rewolucyjnego narzędzia (pierwszego w swoim rodzaju), które pozwala zarządzać i przechowywać hasła, używać rekordów haseł do uwierzytelniania w usługach internetowych, administrować uwierzytelnianiem dwuskładnikowym, ale co najważniejsze generate prawdziwe _aliasy_, wszystko w jednym Interface.



**Ale Alias Vault na tym się nie kończy.



## Kluczowe cechy



Alias Vault działa w chmurze na serwerach dewelopera lub samodzielnie we własnej infrastrukturze, dla której dostępne są pliki Docker i obraz do zainstalowania za pomocą scipt. Oprócz webowego Interface, dostępne są rozszerzenia dla wszystkich popularnych przeglądarek, a także aplikacje mobilne dla iOS i Androida; te ostatnie można również pobrać z F-Droid, omijając oficjalny sklep Google.



W jednym Interface Alias Vault jest:




- Darmowe i otwarte źródło**
- Menedżer haseł**, do przechowywania wszystkich złożonych haseł. Korzystając z rozszerzenia przeglądarki, menedżer haseł uzupełnia loginy do stron internetowych
- 2FA**, do obsługi uwierzytelniania dwuskładnikowego
- Menedżer aliasów z wbudowanym serwerem poczty e-mail**: Alias Vault nie tworzy aliasów, które przekazują wiadomości e-mail do skrzynki pocztowej użytkownika; raczej tworzy rzeczywiste alter-ego, wraz z imieniem, nazwiskiem, płcią, nazwą użytkownika, hasłem i datą urodzin (jeśli te informacje są wymagane).



Częścią pakietu jest obszerna i dokładna dokumentacja, która będzie towarzyszyć nowicjuszom w odkrywaniu tego potężnego narzędzia.



## Brak danych osobowych!



Zaczyna się, jak zawsze, od strony internetowej [aliasvault.net](aliasvault.net). Jak wspomniano, Alias Vault może być używany na własnym serwerze lub z chmury dewelopera, aby zapoznać się z nim przed przejściem na rozwiązanie hostowane samodzielnie.



Witryna ma naprawdę przyciągającą wzrok i dobrze utrzymaną grafikę, ale dobre rzeczy pojawiają się, gdy zaczynasz brać się w garść: **załóż konto**.



![img](assets/en/01.webp)



Ku ogromnemu zaskoczeniu okaże się, że Alias Vault nie prosi o podanie danych osobowych: wszystko, czego potrzebujesz, aby utworzyć konto, to dowolny pseudonim, znane Ci słowo, o ile jest dostępne. Zaakceptuj warunki korzystania z usługi, wybierz słowo i kontynuuj.



![img](assets/en/02.webp)



Ustaw teraz **` hasło główne**, które jest najważniejszą informacją w całym nowym systemie. Z tym jednym hasłem będziesz jedyną osobą, która może uzyskać dostęp/odzyskać konto, ponieważ będzie ono szyfrować twój `vault` na serwerze, który będzie hostował twoje informacje.



![img](assets/en/03.webp)



Fakt: Stworzyłeś własny menedżer haseł i aliasów, ale bez podania swojego działającego, prywatnego adresu e-mail Address.



![img](assets/en/04.webp)



Alias Vault wita cię w bezpiecznej, nowej, osobistej, ale też pustej przestrzeni. A teraz zaczynamy ją trochę zaludniać.



Jeśli masz już menedżera haseł, możesz zaimportować plik z tego, którego używasz, aby ocenić różnice z innym dostawcą, lub być może wyeliminować menedżera aliasów, aby móc zarządzać wszystkim w jednej aplikacji.



![img](assets/en/05.webp)



Alias Vault jest niezwykle prosty: masz jedną stronę główną, która jest `Home`, z dwoma menu:




- `Credentials`: pozwala na tworzenie i zarządzanie tożsamościami i aliasami
- `Email`: skrzynka odbiorcza, w której można sprawdzać przychodzące wiadomości dla wygenerowanych aliasów.



![img](assets/en/06.webp)



Interesuje nas utworzenie pierwszego aliasu, więc przejdź do prawego górnego rogu strony i kliknij _+New Alias_.



![img](assets/en/07.webp)



Początkowo menu wygląda minimalistycznie, zgodnie z filozofią Alias Vault. Aby odkryć możliwości tej funkcji, kliknij _Create via advanced mode_.



![img](assets/en/08.webp)



W górnej części pierwszego ekranu możesz użyć go do zaimportowania poświadczeń hasła, których już używasz w usługach, w których masz subskrypcję lub z których najczęściej korzystasz online.



Jeśli włączyłeś uwierzytelnianie dwuskładnikowe w dowolnej (lub wszystkich) z powyższych usług, w Alias Vault możesz również zarządzać tym dodatkowym Layer bezpieczeństwa, importując `secret key`. Alias Vault utworzy `TOTP` wymagany do uzyskania dostępu.



![img](assets/en/09.webp)



**Uwaga**: W miejscu zarezerwowanym dla adresu e-mail Address, Alias Vault domyślnie proponuje własną domenę; aby użyć poprawnego Address, z którym wcześniej utworzono konta, kliknij _Enter custom domain_, aby ustawić poprawną domenę po `@`.



![img](assets/en/14.webp)



Dolna część tego ekranu jest najbardziej zabawna. Kliknij _Generate Random Alias_, a Alias Vault utworzy dla ciebie osobne tożsamości dla różnych potrzeb, każda z własną skrzynką pocztową, bardzo solidnymi hasłami poziomu, uzupełnionymi o inne szczegóły, takie jak płeć, data urodzenia i odpowiedni pseudonim.



![img](assets/en/10.webp)



Z odpowiedniego menu można zmienić ustawienia, które wpływają na generowanie hasła, takie jak wybór tylko małych liter i wyeliminowanie znaków, które mogą być niejednoznaczne.



![img](assets/en/11.webp)



Możesz użyć aliasu e-mail sugerowanego przez Alias Vault lub zmienić domeny, klikając odpowiednie menu rozwijane.



![img](assets/en/12.webp)



Przed użyciem tej wiadomości e-mail do usługi logowania można przetestować jej funkcjonalność, wysyłając wiadomość z własnego Address do nowo utworzonej skrzynki pocztowej.



![img](assets/en/13.webp)



**⚠️ OSTRZEŻENIE**: Odbieranie wiadomości e-mail jest możliwe dzięki wbudowanemu serwerowi Alias Vault, ale pozwala to tylko na odbieranie wiadomości e-mail, a nie na odpowiadanie na nie lub korzystanie ze skrzynki e-mail z "konwencjonalnymi" funkcjami usługi `alias`. Różni się więc znacznie od Simple Login, Addy i innych platform dedykowanych wyłącznie tego typu usługom. Przykład Simple Login można znaleźć w dedykowanym samouczku:



https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Aby usunąć alias utworzony jako test, wystarczy zalogować się do `Home`, następnie `Credentials` i kliknąć na tożsamość, którą chcesz usunąć. Polecenie _Delete_ pojawi się w prawym górnym rogu, aby kontynuować.



![img](assets/en/16.webp)



## Rozszerzenie przeglądarki



W zależności od potrzeb można skorzystać z rozszerzenia przeglądarki, które można znaleźć w najczęściej używanych przeglądarkach.



![img](assets/en/15.webp)



Instaluje się tak samo, jak w przypadku wszystkich innych rozszerzeń, więc nie będę się rozwodził nad tym szczegółem.



Rozszerzenie przeglądarki ma na celu ułatwienie logowania się do usług online lub tworzenie nowych aliasów w razie potrzeby: jeśli usługa jest przechowywana wśród rekordów Alias Vault, automatyczne wypełnianie robi to, co jest potrzebne.



![img](assets/en/17.webp)



Jedyną ostrożnością jest sprawdzenie, czy Alias Vault jest aktywny. W rzeczywistości aplikacja ma domyślne ustawienie, zgodnie z którym zatrzymuje się po okresie bezczynności. Jest to bardzo przydatna funkcja, **gdy na przykład musisz odejść od komputera i uniemożliwić komuś innemu dostęp do twoich kont**. Uproszczona procedura pozwoli ci zalogować się ponownie, wprowadzając `hasło główne`, jeśli poprzednia sesja jest nadal w pamięci podręcznej. Czas wylogowania jest jednym z parametrów, które można dostosować, skracając lub wydłużając go zgodnie z własnymi preferencjami.



## Aplikacja mobilna



Podobnie jak wszystkie szanujące się aplikacje tego typu, Alias Vault ma wersję na urządzenia mobilne, zarówno w środowisku Android, jak i iOS. W przypadku systemu Android aplikację można pobrać ze strony [F-Droid](https://f-droid.org/packages/net.aliasvault.app/).



W chwili pisania tego tekstu (pod koniec sierpnia 2025 r.) aplikacja mobilna uważa "automatyczne wypełnianie" za funkcję eksperymentalną, która nie działa z wyjątkiem bardzo niewielu witryn. Dopóki nie zostanie w pełni zaimplementowana, korzystanie z Alias Vault na urządzeniach mobilnych wymaga kopiowania/wklejania danych.



Po pobraniu aplikacji ze sklepu, aby się zalogować, wystarczy wprowadzić użytkownika i `hasło główne` utworzone w aplikacji internetowej.



![img](assets/en/18.webp)



Podczas otwierania `vault` zostaniesz zapytany, czy chcesz włączyć biometrycznie kontrolowany dostęp, dodatkowy Layer bezpieczeństwa, aby uniemożliwić komuś innemu dostęp do twoich haseł, jeśli zdarzy się, że trzyma twój telefon.



![img](assets/en/19.webp)



Jeśli zdecydujesz się skonfigurować sprawdzanie biometryczne, kontynuuj. Jeśli pominiesz ten krok i zmienisz zdanie, możesz również skonfigurować go później z menu _Settings_.



Po zakończeniu logowania dane, które zostały już utworzone, zostaną ponownie zsynchronizowane.



![img](assets/en/20.webp)



Aplikacja mobilna może zostać przekierowana do linku do `vault` hostowanego na własnym serwerze.



![img](assets/en/22.webp)



I to właśnie wersję self-hosted przedstawimy pokrótce w Address w następnej sekcji.



## Self-Hosting: pełna kontrola nad danymi



Alias Vault, aby być uczciwym, nie jest pierwszym "menedżerem haseł", który pozwala na wdrożenie usługi w infrastrukturze. Istnieją inne, ale niektóre z nich mają ograniczenia lub są częściowo zamknięte.



Okazja jest wyjątkowa: **zakończyć zależność od zewnętrznych dostawców usług lub chmur, ale użyć własnego lokalnego serwera do ochrony i zarządzania hasłami, aliasami i niezwykle wrażliwymi informacjami związanymi z tym wszystkim**. Dzięki Alias Vault możesz również skierować usługę poczty e-mail na swój własny serwer poczty e-mail, aby zwiększyć poufność.



Nadszedł czas, aby przejść do [dokumentacji] (https://docs.aliasvault.net/installation/), aby dowiedzieć się, jak przejść do samodzielnego hostowania Alias Vault.



![img](assets/en/23.webp)



Alias Vault działa na Docker Compose, więc wymagane jest minimalne doświadczenie z Linuksem i Dockerem. Możesz zacząć od podstawowej instalacji, a następnie uzupełnić ją o bardziej zaawansowane rozwiązania.



Serwer musi być uruchomiony na 64-bitowej maszynie z dystrybucją Linuksa, 1 GB pamięci RAM i co najmniej 16 GB pamięci masowej; wersja Dockera (CE) musi być co najmniej 20.10 lub wyższa, podczas gdy Docker Compose wymaga wydania od 2.0 wzwyż.



Postanowiłem wypróbować Alias Vault z cienkim klientem, na którym DietPi jest zainstalowany jako dystrybucja, baza Debiana Bookworm, zoptymalizowana do niezbędnych elementów i już działająca `Docker` i `Docker Compose`.



Po pierwsze, aby zachować porządek, utwórz katalog w swoim domu, otwórz `terminal` i wklej polecenie, aby uruchomić skrypt instalacyjny.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Po zakończeniu instalacji znajdziesz swoje poświadczenia dostępu:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Sprawdź zawartość katalogu po instalacji.



![img](assets/en/29.webp)



Aby uruchomić Alias Vault należy użyć polecenia:



`` Launch-Alias-Vault


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Rozważania na temat szyfrowania i bezpieczeństwa



![img](assets/en/32.webp)



Zgodnie z tym, co Lanedirt podaje na stronie, w dokumentacji i na Githubie, z Alias Vault **wszystkie informacje (komponenty), które umieszczasz w Alias Vault, pozostają ściśle związane z urządzeniem, zaszyfrowane i niedostępne dla każdego, kto nie zna `hasła głównego`**.



"Hasło główne" jest zatem podstawowym elementem całego "sejfu". Po jego wprowadzeniu jest ono przetwarzane za pomocą algorytmu `Argon2id`, funkcji wyprowadzania klucza z pamięci Hard, aby zapobiec opuszczeniu urządzenia przez sekret.



Wszystko pozostaje ukryte nawet przed menedżerem chmury lub usług hostingowych. W rzeczywistości z panelu administracyjnego nie można uzyskać dostępu do danych użytkownika, można jedynie dowiedzieć się, czy utworzyli aliasy, otrzymali e-maile i niewiele więcej.



Cała przechowywana zawartość jest szyfrowana i odszyfrowywana za pomocą kluczy kryptograficznych pochodzących z `hasła głównego`. **Na serwerze przechowywane są tylko zaszyfrowane dane, nic nie pojawia się w postaci zwykłego tekstu**. Jeśli użytkownik zapomni lub zgubi swoje `hasło główne`, powiązane z nim konto zostanie nieodwracalnie utracone, ponieważ serwer nie może uzyskać dostępu do zawartości w postaci zwykłego tekstu.



Dla wersji self-hosted istnieje skrypt resetujący "hasło główne", ale nie zapobiega to utracie danych.



![img](assets/en/33.webp)



Ponieważ Alias Vault znajduje się w fazie _Beta_, możesz mieć trudności z dostępem do niego, jeśli zmienisz / zaktualizujesz hasło główne. Zalecam wybranie solidnego i złożonego hasła od samego początku, abyś mógł eksperymentować z usługą i ostatecznie zdecydować, czy chcesz z niej korzystać. W przypadku trudności z dostępem do chmury po aktualizacji hasła należy skontaktować się z pomocą techniczną Alias Vault.



Aby uzyskać pełne zrozumienie architektury i zabezpieczeń przyjętych przez Alias Vault, zdecydowanie zalecam zapoznanie się z [tą stroną] (https://docs.aliasvault.net/architecture/), która zawiera szczegółowe informacje na temat kryptografii leżącej u podstaw jego działania.



## Mapa drogowa


Deweloperzy zamierzają uczynić Alias Vault dojrzałym i stabilnym do końca 2025 roku, aby zdefiniować jego przyszłe cechy użytkowe.



Alias Vault jest i zawsze pozostanie open source i darmowy, ale prawdopodobnie nie bez ograniczeń, jak w wersji beta. Niektóre płatne funkcje są w trakcie wdrażania, co zostało już ogłoszone.



Dostępne są plany zespołowe/rodzinne i wsparcie dla kluczy sprzętowych, te ostatnie do uwierzytelniania za pomocą FIDO2 lub WebAuth.



## Kto potrzebuje Alias Vault?



**Narzędzie takie jak to jest idealne dla każdego, kto stawia prywatność online na pierwszym miejscu**.



Twoja tożsamość jest najprawdopodobniej podstawą działalności, którą prowadzisz online i musi być chroniona na wszelkie sposoby, aby **te** dane były z dala od usług, firm i brokerów gotowych zrobić wszystko, aby dostać w swoje ręce twoje zachowanie online.



Alias Vault zapewnia pełną kontrolę nad danymi uwierzytelniającymi, ograniczając lub całkowicie eliminując potrzebę polegania na firmach trzecich w celu ochrony i szyfrowania najbardziej wrażliwych danych.



Architektura i funkcje kryptograficzne Alias Vault są idealne dla niezależnych osób, małych i średnich firm, zespołów programistycznych i wszystkich entuzjastów aplikacji **open source**. Jeśli należysz do którejkolwiek z tych kategorii: baw się dobrze odkrywając Alias Vault.