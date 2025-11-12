---
name: Nunchuk
description: Wallet mobile odpowiedni dla wszystkich
---
![cover](assets/cover.webp)



## Potężny Wallet


Nunchuk pojawił się pod koniec 2020 roku z jasną filozofią: uczynić multi-signature standardem. Dlatego też został zaprojektowany do wykonywania bardzo zaawansowanych funkcji, z cennym wyborem zbudowania projektu bezpośrednio na Bitcoin Core, oprogramowaniu referencyjnym dla ekosystemu Bitcoin.



Po ponad 4 latach rozwoju i użytkowania jest gotowy do wypróbowania na dużą skalę. Jeśli jesteś początkującym użytkownikiem i nie znasz Nunchuka, ten poradnik pomoże ci postawić pierwsze kroki i odkryć to oprogramowanie, którego zaawansowane funkcje będziesz mógł poznać po przejściu przez pierwsze uderzenie. Sam poradnik dedykowany jest średnio-zaawansowanym użytkownikom, którzy posiadają umiejętności niezbędne do wykonania wszystkich kroków, ale może być inspiracją dla każdego, kto chce dowiedzieć się, jak zwiększyć swoje umiejętności. Zaczniemy od wersji mobilnej, a to zaznaczenie jest konieczne, gdyż Nunchuk posiada oprogramowanie działające również na komputerach.



## Pobierz


Pierwszym krokiem jest zdecydowanie, skąd pobrać aplikację. Przejdź do [oficjalnej strony] (https://nunchuk.io/), gdzie znajdziesz dokumentację (niewiele, ale to początek), prezentację funkcji, a także, na końcu strony, wszystkie linki do pobrania.



w tym samouczku postanowiłem pokazać, jak pobrać Software Wallet z repozytorium Github i jak zweryfikować wydanie przed zainstalowaniem go na telefonie komórkowym. **Poniższą procedurę można wykonać tylko z komputera**, więc zalecam wykonanie wszystkich tych kroków z komputera stacjonarnego lub laptopa i - po wszystkich weryfikacjach - przesłanie pliku `.apk` do telefonu komórkowego.



![image](assets/en/01.webp)



Jeśli twoje umiejętności nie są zbyt zaawansowane, możesz zdecydować się na pobranie pliku `.apk` z oficjalnych sklepów i przejść bezpośrednio do części konfiguracyjnej tego samouczka. Jeśli natomiast chcesz wykonać skok, postępuj krok po kroku.



Z komputera stacjonarnego kliknij _Visit our open source repository_



Link przeniesie cię na stronę Github Nunchuka, gdzie znajdziesz kilka repozytoriów. My skupimy się na repozytorium _nunchuk-android_



![image](assets/en/02.webp)



Na następnym ekranie znajdź po prawej stronie sekcję _Releases_ i wybierz _Latest_



![image](assets/en/03.webp)



W sekcji _Assets_ pobierz wersję (w tym przykładzie 1.67.apk) wraz z plikiem SHA256SUMS i SHA256SUMS.asc.



![image](assets/en/04.webp)



Aby znaleźć klucz GPG dewelopera, wróć do sekcji _Releases_ repozytorium i poszukaj wersji 1.9.53 (lub wcześniejszej), która zawiera link do uzyskania i pobrania _GPG Key_



![image](assets/en/05.webp)



Weryfikację przeprowadzimy za pomocą wygodnego narzędzia oferowanego przez Sparrow wallet, które posiada dedykowane do tego celu okno i obsługuje podpisy PGP oraz manifesty SHA256.



Następnie uruchom Sparrow i z menu _Tools_ wybierz _Verify Download_.



![image](assets/en/06.webp)



W oknie, które się pojawi, znajdziesz pola do "wypełnienia": wybierz przycisk _Browse_ po prawej stronie i wybierz dla każdego pola odpowiednie pliki, które właśnie pobrałeś z Github. Po wykonaniu wszystkich kroków okno będzie wyglądać następująco, z zaznaczeniami Green i potwierdzeniem manifestu Hash.



![image](assets/en/07.webp)


**Uwaga: zrzut ekranu pochodzi z komputera z systemem Windows, ta sama praktyka może być zastosowana dla dowolnego systemu operacyjnego na komputerze, wystarczy mieć zainstalowany Sparrow wallet. I zweryfikowane!**



Możesz znaleźć przewodnik do Sparrow wallet, aby pobrać ten Software Wallet


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Następnie można przenieść plik `.apk` z komputera na telefon



![image](assets/en/08.webp)



i zainstaluj Nunchuk



![image](assets/en/09.webp)



Przed uruchomieniem Nunchuka na telefonie otwórz Orbota i umieść nowość na liście aplikacji, które mają być kierowane pod Tora.



![image](assets/en/11.webp)



Teraz uruchom Nunchuka. W przypadku funkcji projektu - które nie są przedmiotem tego samouczka - Nunchuk po otwarciu zaprosi cię do zalogowania się za pośrednictwem adresu e-mail lub profilu Google. Dopóki nie planujesz skorzystać z zaawansowanych planów Nunchuk Inc, **uniknij logowania** i kontynuuj, wybierając opcję _Kontynuuj jako gość_.



![image](assets/en/12.webp)



## Ustawienia


Nunchuk prezentuje się w oknie prezentacji _Home_, w którym łatwo jest zrozumieć jego filozofię działania i którą omówimy za chwilę.



Na dole znajduje się menu, a w pierwszym kroku należy wybrać _Profile_, aby uzyskać dostęp do ustawień.



![image](assets/en/10.webp)



Następnie wybierz _Ustawienia wyświetlania_, nadal ignorując zaproszenie do utworzenia konta.



![image](assets/en/14.webp)



Na poniższym ekranie możesz sprawdzić, czy Wallet jest online i czy możesz podłączyć swój serwer, zwracając szczególną uwagę na instrukcje w linku, który jest oferowany po kliknięciu _tego przewodnika_.



![image](assets/en/15.webp)



Zapisz ustawienia za pomocą polecenia _Zapisz ustawienia sieciowe_, wróć do menu _Profile_ (Profil) i wybierz opcję _Security settings_ (Ustawienia zabezpieczeń).



![image](assets/en/16.webp)



W tym menu można ustawić sposób ochrony przed otwarciem aplikacji. Aby zapobiec niepożądanemu dostępowi, możesz zabezpieczyć Nunchuka za pomocą danych biometrycznych telefonu i/lub dodać zabezpieczający kod PIN.



![image](assets/en/17.webp)



Zapoznaj się również z menu _About_, które zawsze znajdziesz w oknie _Profile_



![image](assets/en/18.webp)



co pozwoli ci sprawdzić wersję aplikacji lub skontaktować się z twórcami, jeśli zajdzie taka potrzeba.



![image](assets/en/19.webp)



## Generowanie kluczy i Wallet


Jak łatwo się domyślić z filozofii Nunchuka, oprogramowanie ma być użytecznym narzędziem do zarządzania portfelami z wieloma podpisami. Aby wykonać tę funkcję, Nunchuk umożliwia tworzenie Wallet poprzez oddzielenie ich od kluczy potrzebnych do złożenia podpisów cyfrowych.



W rzeczywistości idealne działanie Nunchuka obejmuje tworzenie portfeli, które można oglądać, zależnych od kluczy, które można "przeziębić"



Na poprzednich ekranach mogłeś zauważyć, że na dole znajduje się menu o nazwie _Keys_. Jeśli właśnie pobrałeś Nunchuka, zarówno w _Home_, jak i _Keys_ zobaczysz duży przycisk zapraszający do dodania klucza, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Tak właśnie działa Nunchuk:** najpierw generate/importujesz klucze, a następnie tworzysz Wallet, konfigurując go tak, aby wybierał, które klucze będą autoryzować odblokowanie przechowywanych na nim środków.



Nawet w przypadku Wallet singlesig, najpierw tworzysz klucz, a dopiero potem Wallet. I dokładnie to zrobimy teraz, zaczynając od Wallet singlesig, aby przełamać lody i odkryć funkcje Nunchuka.



Kliknij przycisk _Add Key_ (Dodaj klucz)



![image](assets/en/22.webp)



Nunchuk pokazuje szereg obsługiwanych urządzeń z podpisami, ale aby rozpocząć, wybierz _Software_.



![image](assets/en/23.webp)



Nunchuk będzie generate a Mnemonic, który będzie przechowywany na urządzeniu. Następnie musisz zapisać sekwencję słów dla kopii zapasowej, tworząc najlepsze warunki środowiskowe i upewniając się, że masz czas, aby zrobić to dobrze i cicho. Oprogramowanie wyświetla Mnemonic tylko raz, niezależnie od tego, czy chcesz go wyświetlić teraz, czy później, więc wybierz _Create and backup now_.



![image](assets/en/24.webp)



Nunchuk generuje 24-wyrazowe zdania Mnemonic, które pojawiają się natychmiast na następnym ekranie



![image](assets/en/25.webp)



a następnie przystąpił do szybkiego sprawdzenia, prosząc o wybranie poprawnego słowa z 3 opcji, odpowiadającego numerowi w sekwencji Mnemonic.


Jeśli wpisałeś Mnemonic poprawnie, przycisk _Continue_ zacznie działać. Naciśnij go, aby przejść dalej.



![image](assets/en/26.webp)



Nazwij swój klucz i naciśnij przycisk _Continue_.



![image](assets/en/27.webp)



Pod koniec tych kroków zostaniesz zapytany, czy dodać [passphrase](https://planb.academy/en/resources/glossary/passphrase-bip39) do swojej frazy Mnemonic. Jeśli nie masz niezbędnej wiedzy na temat korzystania z passphrase, organizowania jego kopii zapasowych lub jego działania, zalecam wybranie opcji _Nie potrzebuję hasła_.



![image](assets/en/28.webp)



Klucz zostanie ostatecznie utworzony i wyświetlony w menu:




- Za pomocą _Key Spec_ wskazywany jest główny odcisk palca
- Masz ustawienia, trzy kropki w prawym górnym rogu, gdzie możesz usunąć klucz lub podpisać wiadomość
- Obok nazwy klucza znajduje się ikona stalówki, której kliknięcie umożliwia edycję nazwy klucza, na przykład w celu uporządkowania kluczy w przyszłości.
- Ostatnim poleceniem jest sprawdzenie stanu zdrowia klucza: naciskając _Run health check_, aplikacja może sprawdzić, czy klucz jest zagrożony.



Po zakończeniu kliknij przycisk _Done_



![image](assets/en/29.webp)



W menu _Keys_ pojawi się pierwszy klawisz.



![image](assets/en/30.webp)



Przechodząc do menu _Home_, pojawi się opcja utworzenia Wallet. Kliknij przycisk _Utwórz nowy portfel_.



![image](assets/en/31.webp)



Nunchuk pokazuje szereg możliwości, które w większości mają związek z usługami oferowanymi przez firmę, które nie są przedmiotem tego samouczka.



W tym przewodniku utworzymy _Hot Wallet i _Custom wallet_, szczegółowo opisując szczegóły.


Zacznijmy od _Custom wallet_.



![image](assets/en/32.webp)



W prosty sposób aplikacja poprosi Cię o nazwanie tego nowego Wallet i wybranie skryptu dla adresów. Na potrzeby samouczka zdecydowałem się pozostawić domyślne ustawienie _Native segwit_. Kiedy skończysz, wybierz _Kontynuuj_



![image](assets/en/33.webp)



Konfiguracja Wallet wymaga ustawienia klucza, za pomocą którego środki tego Wallet będą odblokowywane. Jeśli istnieje wiele kluczy, zostanie wyświetlona lista, z której można wybrać. W tej chwili utworzyliśmy tylko jeden, więc zdecydowaliśmy się zaznaczyć go. W prawym dolnym rogu możesz zobaczyć, jak Nunchuk poprosi Cię o skonfigurowanie wielu podpisów Wallet w przyszłości, zwiększając liczbę _wymaganych kluczy_.



![image](assets/en/34.webp)



Ponieważ tworzymy singlesig, zostawiamy `1` i klikamy _Continue_.



Na koniec pojawi się ekran weryfikacji, na którym można sprawdzić funkcje Wallet:




- nazwa
- tage `1/1 Multisig`, tak właśnie Nunchuk nazywa Wallet singlesig
- typ skryptu, `Native SegWit`
- klucz `Keys` z jego odciskiem palca i ścieżką wyprowadzania



Po zakończeniu naciśnij przycisk _Twórz portfel_



![image](assets/en/35.webp)



Wallet został utworzony i można pobrać plik [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) jako kopię zapasową. Aby powrócić do menu głównego, kliknij strzałkę w lewym górnym rogu.



![image](assets/en/36.webp)



Znajdujesz się w _Home_, gdzie wyświetlany jest nowo utworzony Wallet raportujący saldo i status połączenia. Klikając w niebieskie pole, można uzyskać dostęp do głównych funkcji Wallet.



![image](assets/en/37.webp)





- Ikona soczewki w prawym górnym rogu umożliwia wyszukiwanie transakcji;
- `View Wallet config` daje dostęp do menu konfiguracji, gdzie można edytować nazwę Wallet i włączyć zaawansowane opcje, w prawym górnym rogu (z których nie można uzyskać zrzutów ekranu). Tutaj można wyeksportować konfigurację Wallet, etykiety, zastąpić klawisze, zmienić [limit odstępu] (https://planb.academy/en/resources/glossary/gap-limit) i nie tylko.



## Transakcje z użyciem Nunchuka



Nagrody _Odbierz_



![image](assets/en/38.webp)



Aplikacja jest zaprogramowana do wyświetlania kodu QR Address lub kopiowania/udostępniania klucza scriptPubKey w celu otrzymania środków onchain.



![image](assets/en/39.webp)



Mieliśmy UTXO, który przybył na ten pierwszy Address,



![image](assets/en/40.webp)



ale nadal klikamy _Receive_, aby otrzymać kolejny.



![image](assets/en/41.webp)



Celem jest odkrycie, że Nunchuk zgłasza ten nowy Address jako _Nieużywany adres_, ale także pokazuje, że masz _Używane adresy_ i ich liczbę.



### Wydawanie transakcji z kontrolą monet



Gdy drugi UTXO również dotrze, wróć do ekranu głównego Wallet, aby sprawdzić status dwóch przychodzących transakcji i, co najważniejsze, kliknij opcję _View coins_ (Wyświetl monety)



![image](assets/en/42.webp)



gdzie zostaną wyświetlone poszczególne UTXO. Tutaj możesz wybrać, aby wyświetlić jedną konkretną kwotę, klikając małą strzałkę obok kwoty



![image](assets/en/43.webp)



i sprawdzić, kiedy dotarł, opis, blok UTXO, aby nie został wydany i więcej.



![image](assets/en/44.webp)



Jeśli jednak wrócisz do menu _Coins_, klikając strzałkę w prawym górnym rogu, możesz włączyć "Coin Control", aby wydawać swoje UTXO w bardziej kontrolowany sposób.



W poniższym przykładzie wybrałem UTXO z 21 000 Sats, a następnie kliknąłem symbol w lewym dolnym rogu.



![image](assets/en/45.webp)



Nunchuk automatycznie otworzy okno _Nowa transakcja_, aby wydać UTXO. W transakcji wydawania należy najpierw ustawić kwotę ręcznie lub wybierając opcję _Wyślij wszystkie wybrane_, aby wysłać całe saldo kontrolne monet, bez generowania reszt. Po ustawieniu kwoty wybierz opcję _Kontynuuj_



![image](assets/en/46.webp)



Teraz Nunchuk pokazuje, gdzie wkleić Address, do którego przelać te środki, wyszczególnić opis i sfinalizować transakcję.



![image](assets/en/47.webp)



Wybór opcji _Create transaction_ deleguje automatyczne zarządzanie opłatami i transakcjami do aplikacji. Zalecam wybranie opcji _Custom transaction_ w celu uzyskania większej kontroli.



Na tym nowym ekranie należy wybrać




- _Odejmij opłatę od wysyłanej kwoty_, aby zapobiec płaceniu opłat przez inny UTXO obecny w Wallet, wydawaniu ich i generowaniu reszty (co jest możliwą do uniknięcia utratą prywatności);
- a następnie ustawić opłaty ręcznie po sprawdzeniu w eksploratorze.



Po wykonaniu wszystkich tych czynności kliknij przycisk _Continue_



![image](assets/en/48.webp)



Następny ekran to pełne podsumowanie transakcji. Jeśli wszystko jest w porządku, potwierdź, wybierając _Confirm and create transaction_.



![image](assets/en/49.webp)



Dzięki funkcji _Oczekujące podpisy_ Nunchuk ostrzega, że transakcja oczekuje na Twój podpis w celu zatwierdzenia wydatku, który składasz klikając _Podpisz_.



![image](assets/en/50.webp)



Polecenie _Broadcast_ pojawia się na dole, aby propagować sfinalizowaną i podpisaną transakcję.



![image](assets/en/51.webp)



### Wydawanie transakcji z menu _Wyślij_



Podczas gdy na stronie głównej Wallet widzimy transakcję wychodzącą i czekającą na potwierdzenie, używamy menu _Wyślij_, aby zasymulować codzienny wydatek.



![image](assets/en/52.webp)



Kliknięcie przycisku _Send_ w rzeczywistości powoduje wyświetlenie ekranu wysyłania transakcji, który jest taki sam, jak ten widziany przed chwilą, ale bez przechodzenia przez kontrolę monet.



Również w tym drugim przykładzie zdecydowałem się wybrać opcję _Custom transaction_ i wysłać całą kwotę, ale mogłem ustawić ją ręcznie. Po wybraniu kwoty do wysłania należy nacisnąć przycisk _Kontynuuj_.



![image](assets/en/53.webp)



Następnie zawsze należy wybrać, czy opłaty mają być odejmowane od danego UTXO (w tym przykładzie wybór jest wymuszony, ponieważ jest tylko jeden), ręcznie dostosować opłaty zgodnie z sytuacją w danym momencie w Mempool i nacisnąć przycisk _Kontynuuj_.



![image](assets/en/54.webp)



Jeśli ekran podsumowania jest zadowalający, wybierz opcję _Potwierdź i utwórz transakcję_.



![image](assets/en/55.webp)



Podpisz transakcję za pomocą _Sign_



![image](assets/en/56.webp)



i rozpropagować ją w sieci.



![image](assets/en/57.webp)



Wallet jest w tym momencie z zerowym saldem i aktualizowaną historią.



![image](assets/en/58.webp)



## Utworzenie "Hot Wallet"



Na koniec, aby nie pominąć niczego z początkowych etapów mobilnego Nunchuka, zobaczmy, jak tworzy to, co aplikacja nazywa "Hot Wallet"



W menu _Home_ Nunchuka, gdzie pojawia się lista portfeli, kliknij `+` w prawym górnym rogu.



![image](assets/en/59.webp)



Wybierz _Hot wallet_ spośród dostępnych opcji



![image](assets/en/60.webp)



Nunchuk udziela kilku porad dotyczących obsługi portfeli Hot na stronie prezentacji, na której należy wybrać opcję _Kontynuuj_, aby kontynuować.



![image](assets/en/61.webp)



Po kilku chwilach Wallet zostanie utworzony i pojawi się na liście w kolorze brązowym. Jest to kolor, którym Nunchuk ostrzega, że kopia zapasowa Wallet nie została jeszcze utworzona.



![image](assets/en/62.webp)



Kliknij nazwę Wallet, aby uzyskać dostęp do jego konfiguracji i możesz zauważyć zaproszenie do natychmiastowego utworzenia kopii zapasowej frazy Mnemonic.



![image](assets/en/63.webp)



Procedura jest taka sama, jak widzieliśmy wcześniej, więc nie będziemy jej powtarzać. Po zakończeniu Nunchuk przeniesie cię do odpowiedniej strony klucza, którą możesz edytować jako tę, którą utworzyłeś za pomocą procedury _Custom_.



![image](assets/en/64.webp)



Spróbuj również _Run health check_



![image](assets/en/65.webp)



lub zobaczyć, jak wyświetlić wszystkie portfele w _Home_ aplikacji.



![image](assets/en/66.webp)



## Należy pamiętać, aby kontynuować niezależnie


Podobnie jak w przypadku kolejności tworzenia, czyli najpierw generowania kluczy, a następnie Wallet, należy zachować odwrotną kolejność usuwania tych elementów z aplikacji.



Jeśli zajdzie potrzeba usunięcia jednego z kluczy, należy najpierw usunąć Wallet lub portfele, które wykorzystują jeden z kluczy podpisu do transakcji: najpierw usuwamy portfele, a dopiero potem klucze. Jeśli nie zastosujesz się do tej kolejności, nie będziesz w stanie usunąć klucza.



Teraz, gdy już wiesz, jak zacząć korzystać z Nunchuka, możesz kontynuować naukę tej aplikacji i odkrywać jej sekrety. W tym samouczku zrobiliśmy tylko pierwsze kroki, ale istnieją bardziej wyrafinowane aplikacje i zaawansowane potrzeby, które Software Wallet może pomóc spełnić.