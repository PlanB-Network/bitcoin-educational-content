---
name: Proste logowanie
description: Tożsamość chroniona aliasami
---
![cover](assets/cover.webp)

## Login = e-mail = utrata prywatności


W cyfrowym świecie standardową praktyką stało się posiadanie konta na każdej platformie, do której chce się uzyskać dostęp.

Każda z tych usług wymaga logowania, zwykle powiązanego z parą _username_ i _password_. Często nazwą użytkownika jest osobisty adres e-mail użytkownika.


Używając osobistego adresu e-mail Address do każdego logowania, łatwo wyobrazić sobie pierwszą konsekwencję: utratę poufności, która staje się poważna, jeśli Address składa się z _name.surname@serviceemail.com_.


Deweloperzy narzędzi open-source stworzyli serię pakietów aplikacji, stworzonych właśnie po to, aby użytkownicy odzyskali odrobinę prywatności: nadal będą się logować, ale używając aliasu zamiast narzędzia, które ujawnia ich prywatną tożsamość.


Najprostszym z tych, które osobiście wypróbowałem i wciąż testuję, jest [Simple Login](https://simplelogin.io/).


## Alias


Alias e-mail po prostu zastępuje część _name.surname_ adresu e-mail Address fikcyjną nazwą. Dla użytkownika nic się nie zmienia; usługa aliasu przekazuje wiadomości e-mail do i od zwykłego Address w normalny sposób. Każdy może nadal korzystać ze swojej skrzynki odbiorczej tak jak zawsze, ale zamiast wyświetlać swoje prawdziwe imię i nazwisko, pokaże nierozpoznawalnego użytkownika. Ta usługa musi być wydajna i jak dotąd Simple Login udowodniło, że tak właśnie jest.


Odwiedzając witrynę Simple Login po raz pierwszy, należy utworzyć konto (również tutaj!), korzystając z "oficjalnego" adresu e-mail Address. Tutaj należy wprowadzić adres e-mail, hasło i rozwiązać captcha.


![image](assets/it/02.webp)


Simple Login wysyła wiadomość weryfikacyjną na wskazany adres e-mail Address. Zamiast klikać przycisk weryfikacji, zaleca się skopiowanie linku i wklejenie go do paska Address.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Pulpit nawigacyjny Simple Login otwiera się natychmiast, z krótkim samouczkiem dotyczącym nawigacji.


![image](assets/it/05.webp)


Należy zauważyć, że Simple Login automatycznie aktywuje subskrypcję newslettera, którą można dezaktywować z poziomu odpowiedniego polecenia.


![image](assets/it/06.webp)


## Ustawienia


Możesz od razu rzucić okiem na _Settings_, aby odkryć funkcje usługi. Simple Login uruchamia się z aktywnymi wszystkimi opcjami, w tym _Premium_, które pozostają użyteczne przez 10 dni. Po zakończeniu okresu próbnego będziesz mieć możliwość utworzenia 10 aliasów z tym profilem i możesz bezpośrednio połączyć swój adres e-mail Proton, ponieważ Simple Login został przejęty przez szwajcarskiego dostawcę poczty e-mail.


![image](assets/it/07.webp)


Możesz ustawić szereg parametrów lub sprawdzić, czy Twoja poczta e-mail została już naruszona pod względem prywatności.


![image](assets/it/08.webp)


Na koniec możesz wyeksportować kopię zapasową swojego profilu lub zaimportować ją od innego dostawcy.


![image](assets/it/09.webp)


### E-mail służbowy


Ci, którzy używają poczty e-mail z domeną osobistą jako służbowej poczty e-mail, mogą skonfigurować swoją prywatną domenę.


![image](assets/it/10.webp)


Z głównego panelu, wybierając _Mailboxes_, można nawet dodać inne adresy e-mail, a także użyć aliasów, które zostaną odpowiednio utworzone. Na przykład w tym samouczku zdecydowałem się utworzyć profil ze skrzynką pocztową _gmail.com_, a następnie powiązać _proton.me_ Address.


![image](assets/it/11.webp)


Dodając nowy Address, zwłaszcza jeśli należy on do dostawcy Proton, procedura z przewodnikiem pokazuje możliwość wejścia w tryb _sudo_, superużytkownika. Simple Login poprosi o wprowadzenie hasła tej skrzynki pocztowej, aby udowodnić legalność Ownership.


⚠️ ** Osobiście odradzam robienie tego**. ⚠️


![image](assets/it/12.webp)


**Lepiej jest uzyskać dostęp do skrzynki e-mail -> skopiować link do weryfikacji i wkleić go w pasku adresu URL -> i uzyskać weryfikację bez ujawniania hasła **


![image](assets/it/13.webp)


Z dwóch wprowadzonych adresów jeden staje się domyślny, a drugi drugorzędny, ale można je łatwo przełączać, a ustawienie jest łatwe do zidentyfikowania na pulpicie nawigacyjnym.


![image](assets/it/14.webp)


Po dodaniu drugiego e-maila Address (opcjonalnie), zobaczmy, co możemy zrobić z Simple Login.


## Tworzenie aliasów


W panelu pierwsza opcja menu jest oznaczona jako _Alias_, gdzie można je tworzyć. Masz możliwość losowego tworzenia aliasów generate, klikając przycisk Losowy alias, który jest przyciskiem Green pokazanym na następnym zdjęciu. Ta funkcja tworzy unikalny i intrygujący adres e-mail Address.


![image](assets/it/24.webp)


Jeśli jednak chcesz rozróżnić usługi, nadając im różne nazwy, musisz wybrać opcję _New Custom Alias_. W ten sposób możesz nadać aliasowi nazwę usługi, do której chcesz uzyskać dostęp (media społecznościowe, usługodawcy, wydarzenia online, przypadkowo spotkani nieznajomi itp.) Resztą zajmie się Simple Login.

Dla zabawy (ale nie do końca, prawdę mówiąc) postanowiłem stworzyć alias dla banku i nazwałem go `BANK`. Nawet jeśli prawdą jest, że mój bank wie o mnie wszystko, uważam za zabawne komunikowanie się z nimi za pomocą niezrozumiałego dla nich e-maila Address. Simple Login rzeczywiście generuje losową nazwę, która jest oddzielona od tej wybranej przez nas znakiem `.`


Tutaj nowy e-mail Address może się stać:


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- i tak dalej


Można wybrać więcej niż jedną domenę: publiczne są dostępne z darmowym planem, podczas gdy inne, oznaczone jako prywatne (w tym _@simplelogin.com_), rozszerzają wybór dla użytkowników, którzy zdecydują się na subskrypcję płatnego planu.


![image](assets/it/15.webp)


Po wybraniu losowego sufiksu i domeny można ustawić, czy ten nowy (i dziwaczny) Address ma służyć jako alias tylko dla jednej z osobistych skrzynek e-mail, czy dla wszystkich. Alias staje się gotowy i aktywny po kliknięciu na _Create_


![image](assets/it/16.webp)


Nowy e-mail Address został utworzony i jest teraz widoczny, gotowy do wysłania (do banku!) po prostu przez skopiowanie go.


![image](assets/it/18.webp)


W tym momencie możesz skupić się na utworzeniu aliasu dla każdej usługi lub platformy, do której chcesz uzyskać dostęp i gdzie e-mail jest wymagany jako niezbędny parametr do utworzenia konta.


![image](assets/it/19.webp)


Dla entuzjastów prywatności dostępna jest również opcja generate e-mail Address oparta na protokole UUID (nie na możliwych do zidentyfikowania nazwach), który tworzy unikalny 128-bitowy identyfikator, który nie jest kontrolowany przez scentralizowane podmioty. Funkcja ta, przydatna w przypadku wrażliwych kont, znajduje się w menu _Random Alias_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Jak widać, jest to e-mail Address, który wymaga odpowiedniego zarządzania.


Jeśli zmienisz zdanie i nie chcesz już używać aliasu, po prostu kliknij polecenie _More_ każdego aliasu i wybierz _Delete_.


![image](assets/it/23.webp)


## Zarządzanie aliasami


Tworzenie aliasów jest proste, podobnie jak zarządzanie nimi, które wymaga jedynie odrobiny ostrożności i dyscypliny. W rzeczywistości cały ruch będzie nadal przechodził przez skrzynkę e-mail, którą zdefiniowaliśmy na początku jako oficjalną. Powiadomienia i ważne komunikaty z platform będą nadal docierać do Gmaila, Proton lub innego dostawcy poczty e-mail.


Rezultat jest jednak taki, że zachowaliśmy główny Address, który od momentu utworzenia aliasu możemy swobodnie decydować, komu go ujawnić, a komu nie.


Pseudonim działa zarówno w przypadku odbierania, jak i wysyłania: inny użytkownik rzeczywiście otrzyma odpowiedź od alias.preoccupy789@8shield.net, jeśli jest to pseudonim wybrany dla tego konkretnego odbiorcy.


## Plusy


Ogólnie rzecz biorąc, korzystanie z aliasów jest skutecznym sposobem ochrony tożsamości i prywatności. Adresy e-mail są często gromadzone przez brokerów danych i strony internetowe w celu śledzenia nawyków i zachowań użytkowników. Chociaż alias nie czyni cię całkowicie niemożliwym do wyśledzenia, konsekwentne korzystanie z niego jest pozytywnym krokiem w kierunku ochrony twoich informacji. Co więcej, w naszej "globalnej cyfrowej wiosce", w której hakowanie, sprzedaż danych i naruszenia bezpieczeństwa są zbyt powszechne, jest wysoce prawdopodobne, że adres e-mail używany do rejestracji na różnych stronach internetowych został już naruszony lub stał się celem ataku.


Unikalny pseudonim, używany przy każdym logowaniu, **natychmiast pozwala nam zrozumieć, która platforma wysyła spam (lub gorzej) do naszej skrzynki pocztowej, ponieważ wiadomość e-mail jest identyfikowana przez powiązany z nią alias**. Nie masz pojęcia, ile spamu i phishingu pochodzi z tak zwanych wiarygodnych kanałów, ponieważ są one instytucjonalne, dopóki nie zaczniesz używać aliasu dla banków, jednego dla usług pocztowych lub konkretnego dla niektórych obowiązkowych usług rządowych. Po zidentyfikowaniu nadawcy spamu (lub gorzej), będziesz wiedział, że witryna została naruszona, podejmując wszelkie środki ostrożności, aby chronić wszystkie dane dostarczone (pomyśl o kartach kredytowych!) do tej konkretnej witryny, która może zdać sobie sprawę z naruszenia kilka tygodni później.


Jeśli chodzi o Simple Login, narzędzie to posiada następujące funkcje:



- aplikacja mobilna (również od F-Droid) i rozszerzenie przeglądarki, do zarządzania aliasami w każdej sytuacji;
- uwierzytelnianie dwuskładnikowe dla każdego nowego pseudonimu, co zwiększa stopień niezależności od samej usługi;
- Obsługa PGP (dla użytkowników _Premium);
- proste tworzenie każdego typu aliasu (niestandardowego, losowego i UUID);
- wśród darmowych planów w tym sektorze, możliwość korzystania z aliasów z większą liczbą "oficjalnych" skrzynek e-mail. Inni konkurenci ograniczają się do jednej.


## Wady


- 10 aliasów może nie wystarczyć, jeśli planujesz intensywnie korzystać z Simple Login. W takim przypadku płatny plan, który jest dość przystępny cenowo, jest przydatny do zwiększenia liczby dostępnych aliasów.
- Nie jest możliwe utworzenie aliasu z określoną nazwą i domeną. Losowy sufiks, dodany po wybranej przez nas nazwie, generuje Address, który można opisać jako dziwaczny w najlepszym przypadku. Tradycyjne media społecznościowe zwykle odmawiają przyznania kont utworzonych przy użyciu tego typu adresów e-mail. Nostr to naprawia!
- Jeśli używasz pseudonimu do wysyłania wiadomości do kogoś, łatwo jest skończyć w folderze spamu odbiorcy. Pierwszym krokiem jest użycie pseudonimu do odbierania wiadomości, podobnie jak w przypadku zakładania konta, zapisywania się na listę mailingową itp.