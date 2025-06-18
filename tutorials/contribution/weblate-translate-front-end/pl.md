---
name: Weblate - tłumaczenie statycznego Elements
description: Jak można uczestniczyć w tłumaczeniu statycznego Elements na planb.network?
---
![cover](assets/cover.webp)


Misją Plan ₿ Network jest dostarczanie najwyższej klasy zasobów edukacyjnych na Bitcoin i tłumaczenie ich na jak największą liczbę języków. Duża część treści publikowanych na stronie jest open-source i hostowana na GitHub, dzięki czemu każdy może uczestniczyć we wzbogacaniu platformy. Wkład może przybierać różne formy: poprawianie i korekta istniejących treści, aktualizowanie informacji lub tworzenie nowych samouczków do dodania na platformę.


W tym samouczku pokażemy, jak w prosty sposób przyczynić się do tłumaczenia statycznego Elements na naszej stronie internetowej. Dane na platformie są podzielone na dwie główne kategorie:


- dane frontendowe/statyczne Elements (strony, przyciski itp.);
- treści edukacyjne (samouczki, kursy, zasoby...).


Do tłumaczenia treści edukacyjnych używamy [sztucznej inteligencji] (https://github.com/Asi0Flammeus/LLM-Translator). Następnie, aby poprawić ewentualne błędy w tych plikach, zapraszamy korektorów do udziału. Jeśli chcesz dokonać korekty niektórych treści, zapoznaj się z poniższym samouczkiem:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6

Z drugiej strony, jeśli jesteś zainteresowany tłumaczeniem statycznego Elements strony internetowej (z wyłączeniem treści edukacyjnych), jesteś we właściwym miejscu! Aby skutecznie przetłumaczyć frontend, używamy narzędzia Weblate, które jest bardzo proste w użyciu i ułatwia podejście do tłumaczenia.


Jeśli chcesz dodać zupełnie nowy język do Plan ₿ Network, skontaktuj się z zespołem Plan ₿ Network za pośrednictwem naszej grupy [Telegram](https://t.me/PlanBNetwork_ContentBuilder). Jeśli nie masz telegramu, możesz wysłać e-mail na adres mari@planb.network. Pamiętaj, aby napisać małą prezentację o tym, kim jesteś i jakimi językami mówisz.

Członkowie naszego zespołu przekażą ci szczegółowe instrukcje i otworzą powiązane "sprawy" w serwisie Github, aby koordynować twoją pracę.


Przed wykonaniem tego samouczka należy dodać nowy język do Weblate.


https://planb.network/tutorials/contribution/content/weblate-add-new-language-eef2f5c0-1aba-48a3-b8f0-a57feb761d86

Gdy będziesz gotowy do rozpoczęcia tłumaczenia, wróć do tego samouczka i zapoznaj się z poniższymi punktami.


## Zarejestruj się na Weblate



- Wejdź na stronę [self-hosted Weblate of Plan ₿ Network] (https://weblate.planb.network/):

![weblate](assets/01.webp)


- Jeśli masz już konto Weblate, kliknij `Zaloguj`:

![weblate](assets/02.webp)


- Jeśli nie masz konta, kliknij `Register`:

![weblate](assets/03.webp)


- Wprowadź swój adres e-mail Address, a także nazwę użytkownika i imię i nazwisko (możesz użyć pseudonimu), a następnie kliknij `Register`:

![weblate](assets/04.webp)


- Na swoją skrzynkę e-mail powinieneś otrzymać wiadomość z potwierdzeniem od Weblate. Kliknij łącze, aby potwierdzić rejestrację:

![weblate](assets/05.webp)


- Wybierz silne hasło, a następnie kliknij `Zmień moje hasło`:

![weblate](assets/06.webp)


- Możesz teraz wrócić do pulpitu nawigacyjnego Plan ₿ Network:

![weblate](assets/07.webp)


## Rozpocznij tłumaczenie



- Kliknij projekt `Website Elements` (nie słownik):

![weblate](assets/08.webp)


- Dojdziesz do Interface, gdzie możesz zobaczyć języki w toku:

![weblate](assets/09.webp)


- Wybierz swój język. Weźmy na przykład francuski:

![weblate](assets/10.webp)


- Aby rozpocząć tłumaczenie, wystarczy kliknąć przycisk `Translate`:

![weblate](assets/11.webp)


- Nastąpi przekierowanie do roboczego Interface:

![weblate](assets/12.webp)


- Weblate automatycznie zasugeruje zdania, akapity, a nawet słowa do przetłumaczenia w polu "język". W twoim przypadku prawdopodobnie zobaczysz główny ciąg w języku angielskim i inne pole tekstowe dla twojego języka:

![weblate](assets/13.webp)


- Twoje zadanie polega na przetłumaczeniu wskazanych ciągów znaków. Tekst należy umieścić w polu odpowiadającym wybranemu językowi. Na przykład, jeśli pracujesz nad wersją francuską, wpisz swoje tłumaczenie w polu `French`:

![weblate](assets/14.webp)


- Kliknij zakładkę `Automatyczna sugestia`:

![weblate](assets/15.webp)


- Tutaj Weblate pokazuje tłumaczenie wykonane przez sztuczną inteligencję:

![weblate](assets/16.webp)


- Jeśli sugerowane tłumaczenie wydaje ci się odpowiednie, możesz kliknąć przycisk "Klonuj do tłumaczenia":

![weblate](assets/17.webp)


- Sugestia zostanie teraz umieszczona w polu roboczym:

![weblate](assets/18.webp)


- Następnie można ręcznie zmodyfikować sugestię:

![weblate](assets/19.webp)


- Gdy tłumaczenie wyda ci się satysfakcjonujące, kliknij przycisk `Zapisz i kontynuuj`. Pamiętaj, aby odznaczyć pole "Wymaga edycji", gdy jesteś pewien swojego tłumaczenia:

![weblate](assets/20.webp)


- Proszę bardzo! Twoje tłumaczenie zostało pomyślnie zapisane. Weblate automatycznie przekieruje cię do następnego elementu do przetłumaczenia. Jeśli wrócisz do pulpitu nawigacyjnego odpowiadającego Twojemu językowi, zobaczysz, że każdy typ ciągu ma inny status tłumaczenia. Na przykład, jeśli chcesz skupić się tylko na "nieprzetłumaczonych ciągach", możesz kliknąć określoną zakładkę:

![weblate](assets/21.webp)


- Jeśli chcesz wyszukać określone słowo, czy to w swoim języku, czy w oryginalnym, kliknij "szukaj" i wprowadź je tam:

![weblate](assets/22.webp)


## Wytyczne dotyczące tłumaczeń



- Gdy znajdziesz słowa wstawione wewnątrz nawiasów klamrowych "{", nie musisz ich tłumaczyć. Na przykład w "Twoje konto zostało utworzone, {{userName}}!", przetłumaczysz całe zdanie, ale zachowasz "nazwę użytkownika" w języku angielskim.
- Jeśli w ciągu znaków znajdziesz "Plan ₿ Network", NIE tłumacz słowa "network" (uznaj Plan ₿ Network za znak towarowy). Poza tym, zawsze używaj Bitcoin's ₿!
- Jeśli znajdziesz samo słowo "sieć", możesz je przetłumaczyć.
- Nie należy tłumaczyć "B-CERT", ponieważ jest to inne stałe słowo.
- Jeśli znajdziesz ciągi kończące się spacją, możesz je opuścić.
- Niektóre ciągi mogą zawierać spację między ostatnim słowem a znakiem interpunkcyjnym: nie pozostawiaj jej w języku docelowym, chyba że wymaga tego gramatyka. Na przykład "Informacje kontaktowe:" należy poprawić na "Informacje kontaktowe:". W takim przypadku należy przetłumaczyć je w poprawny sposób. Możesz również dodać komentarz, aby poinformować administratorów o tym problemie w oryginalnej wersji angielskiej.


## Nowe funkcje


- Pracujemy nad dodaniem sekcji "wyjaśnienia" dla każdego ciągu, wraz ze zrzutem ekranu, aby pomóc ci znaleźć, gdzie konkretne zdanie / słowo pojawia się na stronie. W chwili obecnej, jeśli masz jakiekolwiek wątpliwości co do niektórych słów i chcesz znaleźć ich konkretną lokalizację na stronie, możesz zadać pytanie w sekcji "komentarze" lub zapytać koordynatora tłumaczeń na grupie Telegram wspomnianej na początku tego samouczka.

![weblate](assets/23.webp)


Z góry dziękujemy za wkład w tłumaczenie Plan ₿ Network! Jeśli masz do nas jakieś konkretne pytania lub uwagi, skontaktuj się z nami za pośrednictwem grupy [Telegram](https://t.me/PlanBNetwork_ContentBuilder).