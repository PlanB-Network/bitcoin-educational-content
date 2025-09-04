---
name: be-BOP
description: Praktyczny przewodnik po monetyzacji firmy za pomocą be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** to platforma e-commerce przeznaczona dla przedsiębiorców, którzy chcą sprzedawać online i offline, w pełnej autonomii, akceptując płatności w Bitcoin, za pośrednictwem konta bankowego i w gotówce. Rozwiązanie to jest również przydatne dla wszelkiego rodzaju organizacji, które chcą zbierać darowizny lub zarabiać na swojej działalności.



Rozwiązanie jest proste, lekkie i autonomiczne. Umożliwia stworzenie sklepu internetowego, nawet w środowisku, w którym tradycyjne usługi finansowe są ograniczone lub nieobecne. W rzeczywistości **be-BOP** został zaprojektowany tak, aby działał wydajnie z dostępem do banków lub bez niego, wykorzystując Bitcoin jako infrastrukturę płatniczą.



W tym poradniku przeprowadzimy cię krok po kroku przez:





- Stwórz swój pierwszy sklep internetowy z **be-BOP**
- Spersonalizuj swoją wizytówkę i produkty
- Konfiguracja dostępnych metod płatności
- Poznaj najlepsze praktyki skutecznej sprzedaży online z **be-BOP**



Ten samouczek nie wymaga zaawansowanych umiejętności technicznych. Jest skierowany do programistów, a także rzemieślników, kupców, spółdzielni lub przedsiębiorców, którzy chcą rozpocząć handel cyfrowy w suwerenny i odporny sposób.



## Wymagania wstępne dotyczące instalacji be-BOP na własnym serwerze



Przed rozpoczęciem instalacji be-BOP upewnij się, że posiadasz następującą infrastrukturę techniczną. Te Elements są niezbędne do prawidłowego działania platformy:



### Pamięć masowa kompatybilna z S3



be-BOP używa systemu przechowywania do zarządzania plikami (takimi jak zdjęcia produktów). Wymaga to dostępu do usługi S3, takiej jak:





- [MinIO](https://min.io/) self-hosted
- Amazon S3 (AWS)
- Scaleway Object Storage



Konieczne będzie skonfigurowanie zasobnika i podanie następujących informacji:





- S3_BUCKET**: nazwa zasobnika
- S3_ENDPOINT_URL**: link dostępu do usługi S3
- S3_KEY_ID** i S3_KEY_SECRET: kody dostępu
- S3_REGION**: region usługi S3



### Baza danych MongoDB w trybie ReplicaSet



be-BOP używa MongoDB do przechowywania danych sklepu, użytkowników, produktów i innych.



Masz dwie możliwości:





- Zainstaluj MongoDB lokalnie z włączonym trybem **ReplicaSet**
- Skorzystaj z usługi online, takiej jak **MongoDB Atlas**



Potrzebne będą następujące zmienne:





- MONGODB_URL**: połączenie z bazą danych Address
- MONGODB_DB**: nazwa bazy danych



## Środowisko Node.js



be-BOP działa z Node.js. Upewnij się, że masz **Node.js** w wersji 18 lub wyższej i **Corepack** włączony (potrzebny do zarządzania menedżerami pakietów, takimi jak pnpm). Polecenie do uruchomienia to `corepack enable`



### Zainstalowany Git LFS



Niektóre zasoby (takie jak duże obrazy) są zarządzane przez Git LFS (Large File Storage). Upewnij się, że masz zainstalowany Git LFS na swoim komputerze za pomocą polecenia `git lfs install`. Gdy te warunki wstępne zostaną spełnione, możesz przejść do następnego kroku: pobrania i skonfigurowania be-BOP.



**Uwaga:** Przewodnik techniczny dotyczący wdrażania oprogramowania jest dostępny w osobnym samouczku.



## Tworzenie konta super administratora



Przy pierwszym uruchomieniu be-BOP tworzone jest konto **Super Admin**. Konto to posiada wszystkie uprawnienia wymagane do zarządzania funkcjami back-office. Aby utworzyć konto, wykonaj następujące kroki:





- Przejdź do `yourresiteweb/admin/login`
- Utworzenie konta administratora z bezpiecznym loginem i hasłem



To konto zapewnia dostęp do wszystkich funkcji zaplecza. Po jego utworzeniu można się zalogować, wprowadzając nazwę użytkownika i hasło.



![login](assets/fr/001.webp)



## Konfiguracja i zabezpieczenia Back-Office



Przed skonfigurowaniem połączenia zaplecza Interface należy utworzyć unikalny Hash. Zapewnia to ochronę przed złośliwymi podmiotami próbującymi wykraść łącze połączenia z administratorem Interface.



Aby utworzyć Hash, przejdź do `/admin/Settings`. W sekcji poświęconej bezpieczeństwu (np. "Admin Hash") zdefiniuj unikalny ciąg znaków (Hash). Po zarejestrowaniu, adres URL zaplecza zostanie zmodyfikowany (np. `/admin-yourhash/login`), aby ograniczyć dostęp osobom nieupoważnionym.



![hash-login](assets/fr/002.webp)



2.2. Aktywuj tryb konserwacji (jeśli to konieczne)



Nadal w /admin/Settings, (Ustawienia > Ogólne poprzez grafikę Interface) sprawdź opcję "włącz tryb konserwacji" na dole strony.



![maintenance-mode](assets/fr/003.webp)



W razie potrzeby można określić listę autoryzowanych adresów IPv4 (oddzielonych przecinkami), aby umożliwić dostęp do biura głównego podczas konserwacji. Back office pozostaje dostępny dla administratorów.



![ip-bebop](assets/fr/004.webp)



## Konfiguracja łączności



Aby umożliwić be-BOP wysyłanie powiadomień (np. o zamówieniach, rejestracjach lub komunikatach systemowych), należy skonfigurować co najmniej jedną metodę komunikacji. Dostępne są dwie opcje: e-mail (SMTP) lub Nostr.



### Konfiguracja SMTP (e-mail)



be-BOP może wysyłać wiadomości e-mail za pośrednictwem serwera SMTP. Potrzebne będą prawidłowe dane uwierzytelniające SMTP, często dostarczane przez usługę poczty e-mail (np. Mailgun, Gmail itp.).



Oto, co musisz wiedzieć:



SMTP_HOST: Serwer SMTP Address (np. smtp.mailgun.org)



SMTP_PORT: port do użycia (często 587 lub 465)



SMTP_USER: nazwa użytkownika (zazwyczaj e-mail Address)



SMTP_PASSWORD: hasło lub klucz API



SMTP_FROM: e-mail Address, który pojawi się jako nadawca




### Konfiguracja Nostr



be-BOP umożliwia wysyłanie powiadomień za pośrednictwem protokołu Nostr, zdecentralizowanej infrastruktury przesyłania wiadomości. Aby to zrobić, należy użyć generate lub Supply klucza prywatnego Nostr (NSEC). Klucz ten można generate bezpośrednio przez be-BOP Interface, w sekcji poświęconej Nostr. Po prawidłowym skonfigurowaniu Elements, be-BOP będzie w stanie automatycznie wysyłać wiadomości i alerty do użytkowników.



## Kompatybilne metody płatności



be-BOP jest kompatybilny z kilkoma rozwiązaniami płatniczymi, dzięki czemu możesz zaoferować swoim klientom większą elastyczność. Oto, czego potrzebujesz, aby skonfigurować metodę płatności, która najbardziej Ci odpowiada.



### Bitcoin Onchain



be-BOP umożliwia przyjmowanie płatności Bitcoin bezpośrednio na Blockchain (On-Chain), w prosty i bezpieczny sposób.



**Kroki konfiguracji:**





- Przejdź do menu **Ustawienia płatności**
- Kliknij **Bitcoin Nodeless**, aby uzyskać dostęp do parametrów płatności On-Chain.
- Wypełnij następujące pola:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Wskazówka:** Aby uzyskać rozszerzony klucz publiczny (Zpub), można zapoznać się z zaawansowanymi ustawieniami Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter itp.). Upewnij się, że Wallet nie jest **tylko do odczytu**, jeśli zamierzasz korzystać z historii transakcji.



### Lightning Network



be-BOP może również akceptować natychmiastowe płatności Bitcoin dzięki Lightning Network. Obecnie dostępne są dwie opcje konfiguracji:



**Phoenixd**



Przejdź do menu `Ustawienia płatności` i kliknij `Phoenixd`



![phoenixd](assets/fr/006.webp)



Następnie musisz wprowadzić **hasło lub uwierzytelnienie token**, które połączy Cię z instancją Phoenixd, backendem opracowanym przez Acinq, który pozwala zarządzać płatnościami Lightning za pomocą własnego węzła, ale bez złożoności zarządzania kanałami płatności.



**Swiss Bitcoin Pay**



Jeśli nie chcesz samodzielnie zarządzać węzłem Lightning, **Swiss Bitcoin Pay** to gotowe do użycia, łatwe w konfiguracji rozwiązanie, które jest idealne do rozpoczęcia akceptowania płatności Lightning bez złożonej infrastruktury.



Kroki konfiguracji:





- W menu "Ustawienia płatności" kliknij `Swiss Bitcoin Pay`
- Zaloguj się na swoje konto Swiss Bitcoin Pay (lub utwórz je, jeśli jeszcze go nie masz).
- Wprowadź klucz API dostarczony przez Swiss Bitcoin Pay, a następnie kliknij "Zapisz"



Po skonfigurowaniu, be-BOP automatycznie generate Lightning faktury dla klientów, a otrzymasz płatności bezpośrednio na konto Swiss Bitcoin Pay. To rozwiązanie jest idealne dla użytkowników, którzy chcą uniknąć złożoności technicznej węzła osobistego, jednocześnie akceptując szybkie i tanie płatności.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Oprócz Bitcoin, be-BOP umożliwia również przyjmowanie płatności gotówkowych za pośrednictwem PayPal, dobrze znanego i szeroko stosowanego rozwiązania międzynarodowego.



Kroki konfiguracji:





- Przejdź do menu `Ustawienia płatności`
- Kliknij `PayPal
- Na swoim koncie Paypal (sekcja dla deweloperów) wprowadź `Client ID` i `Secret`
- Wybierz walutę (np. **USD**, **EUR**, **XOF** itp.)
- Kliknij `zapisz



![paypal](assets/fr/008.webp)



**Uwaga:** Musisz mieć konto firmowe PayPal, aby generate te identyfikatory. Można je uzyskać za pośrednictwem portalu [deweloperskiego] (https://developer.paypal.com)



### SumUp



Oprogramowanie integruje teraz rozwiązanie płatnicze **SumUp**, umożliwiając przyjmowanie płatności kartą kredytową w prosty, bezpieczny i wydajny sposób. Aby skorzystać z tej funkcjonalności, wymagana jest wstępna konfiguracja. Oto kroki, które należy wykonać, ponumerowane w celu przejrzystego i stopniowego wdrożenia:





- Zacznij od wprowadzenia **API Key**, poufnego klucza dostarczonego przez SumUp podczas tworzenia konta programisty. Ustanawia on bezpieczne połączenie między kontem SumUp a oprogramowaniem.
- Wypełnij pole `Merchant Code` unikalnym kodem, który identyfikuje Twoją firmę na platformie SumUp. Kod ten jest niezbędny do powiązania transakcji z Twoją firmą.
- W polu `Waluta` wybierz główną walutę używaną do transakcji (np. **EUR**, **USD**, **CDF** itp.).
- Po prawidłowym wypełnieniu wszystkich pól kliknij przycisk "Zapisz", aby zapisać ustawienia. Następnie system ustanowi połączenie z kontem SumUp, a oprogramowanie będzie gotowe do przyjmowania płatności.



![payment-sumup](assets/fr/009.webp)



Po tej konfiguracji integracja **SumUp** będzie aktywna i będzie działać, umożliwiając szybkie wypłacanie gotówki i śledzenie transakcji bezpośrednio z oprogramowania.



### Pasek



be-BOP oferuje również pełną integrację z **Stripe**, jedną z najpopularniejszych platform płatności online. Stripe pozwala akceptować płatności online za pomocą karty kredytowej, cyfrowego Wallet i kilku innych metod płatności. Oto jak ją aktywować:





- Wprowadź **secret key** podany w panelu Stripe.
- Wypełnij pole **Klucz publiczny**, również dostarczone przez Stripe.
- Wybierz **walutę główną**.
- Zapisz konfigurację, a następnie kliknij `Zapisz`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Uwaga:** W celu prawidłowego skonfigurowania opcji fakturowania w **be-BOP** niezbędna jest znajomość systemu VAT mającego zastosowanie do Twojej działalności (np. sprzedaż objęta podatkiem VAT w kraju sprzedawcy, zwolnienie na podstawie uzasadnienia lub sprzedaż ze stawką VAT kraju nabywcy).



## Konfiguracja waluty



**be-BOP** oferuje zaawansowane zarządzanie walutami i jest dostosowany do środowisk wielowalutowych i specyficznych wymagań księgowych. Aby zapewnić spójność operacji finansowych i raportowania, konieczne jest prawidłowe skonfigurowanie różnych walut używanych w systemie. Oto kroki, które należy wykonać w celu tej konfiguracji:





- Wybierz **główną walutę** (`Główna waluta`)
- Wybierz `Waluta dodatkowa
- Zdefiniuj **walutę referencyjną** (`Waluta referencyjna ceny`)
- Wskazać `Waluta rozliczeniowa



Po prawidłowym skonfigurowaniu wszystkich walut, oprogramowanie zapewnia automatyczną i dokładną konwersję transakcji wielowalutowych, przy jednoczesnym zachowaniu rygorystycznej spójności księgowej.



![settings-currencies](assets/fr/011.webp)



## Konfiguracja dostępu do odzyskiwania przez e-mail lub Nostr



Nadal w `/admin/settings`, poprzez moduł **ARM**, upewnij się, że konto super-admina zawiera **email Address** lub **recovery pub**, ułatwiając w ten sposób procedurę w przypadku zapomnienia hasła.



![settings-users](assets/fr/012.webp)



## Ustawienia języka



Oprogramowanie oferuje możliwość obsługi wielu języków, aby dostosować się do międzynarodowej publiczności i poprawić komfort użytkowania. Aby aktywować funkcję wielojęzyczności, należy skonfigurować dostępne języki i zdefiniować **język domyślny**.



![settings-languages](assets/fr/13.webp)



## Konfiguracja Interface i tożsamości w be-BOP



**be-BOP** zapewnia projektantom wszystkie narzędzia potrzebne do zaprojektowania strony internetowej. Pierwszym krokiem jest otwarcie sekcji `/Admin > Merch > Layout` w ustawieniach. Zacznij od skonfigurowania **Top Bar**, **Navbar** i **Footer**.



### Le Top Bar



Konfiguracja **Top Bar** pozwala spersonalizować identyfikację wizualną oprogramowania, wyświetlając kluczowe informacje już w pierwszym wierszu Interface. Wzmacnia to rozpoznawalność marki i zapewnia jasny kontekst dla użytkowników.



#### Kroki konfiguracji:





- W polu `Nazwa marki` wprowadź nazwę swojej firmy, organizacji lub produktu. Nazwa ta pojawi się w górnej części Interface i będzie reprezentować główną identyfikację wizualną.
- Wskaż tytuł strony**: wybrany tytuł powinien podsumowywać cel platformy. Tytuł ten może pojawić się w nagłówku lub na karcie przeglądarki.
- Dodaj opis witryny**: w tym miejscu należy wprowadzić krótki opis swojej inicjatywy. Opis ten pomaga kontekstualizować narzędzie dla użytkowników i może być również wykorzystywany do celów SEO.



Po wprowadzeniu tych informacji, **Top Bar** wyświetli przejrzystą, profesjonalną i spójną prezentację Twojego rozwiązania.



#### Linki na górnym pasku



Sekcja `Links` na górnym pasku umożliwia dodawanie skrótów do ważnych stron w aplikacji lub na stronach zewnętrznych. Linki te są wyświetlane bezpośrednio na górnym pasku, oferując użytkownikom szybki, uporządkowany dostęp.



#### Kroki konfiguracji:





- Wprowadź nazwę linku (tekst)**: w polu `Text` wprowadź nazwę lub etykietę linku, tak jak będzie się ona wyświetlać (np. Strona główna, Kontakt, Pomoc...).
- Wskaż link Address (Url)**: w polu `Url` wprowadź pełny Address strony docelowej (wewnętrznej lub zewnętrznej).
- Dodaj inne linki, jeśli to konieczne**: każda linia konfiguracji pozwala dodać dodatkowy link przy użyciu pól `Text` i `Url`.
- Zapisz linki**: po wprowadzeniu wszystkich linków kliknij przycisk "Dodaj link na górnym pasku", aby je zapisać.



Taka konfiguracja pozwala zaoferować przejrzystą, płynną i dostępną nawigację po różnych sekcjach witryny lub do dodatkowych zasobów.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



Sekcja **Navbar** pozwala skonfigurować główne menu nawigacyjne be-BOP, zwykle znajdujące się z boku lub na górze Interface. To menu prowadzi użytkowników do różnych stron i funkcji aplikacji. Konfiguracja łącza jest prosta i intuicyjna. Oto jak to działa:





- Wprowadź nazwę linku (`Text`)**: w linii konfiguracji zacznij od wypełnienia pola `Text`. Odpowiada to nazwie linku wyświetlanego na pasku nawigacyjnym (przykłady: *Dashboard*, *Users*, *Settings*...).
- Wprowadź link Address (`Url`)**: obok pola `Text` znajduje się pole `Url`. W tym polu wprowadź Address strony, do której link powinien przekierowywać. Może to być trasa wewnętrzna lub link do strony zewnętrznej.
- Dodaj wiele linków w razie potrzeby**: poniżej pierwszej linii dostępne są nowe pola `Text` i `Url`, umożliwiające dodanie dowolnej liczby linków. Każda linia reprezentuje dodatkowy link nawigacyjny.
- Zapisz linki**: po wprowadzeniu wszystkich Elements, kliknij przycisk `Dodaj link paska nawigacyjnego`, aby zapisać i wyświetlić wyniki na pasku nawigacyjnym.



Taka konfiguracja pozwala na efektywną strukturę dostępu do różnych części oprogramowania, poprawiając ergonomię i wrażenia użytkownika.



![navbar](assets/fr/015.webp)



### Stopka



Sekcja **Stopka** pozwala dostosować stopkę oprogramowania, dodając przydatne informacje lub linki. Przed skonfigurowaniem linków należy rozpocząć od aktywowania określonej opcji:





- Włącz wyświetlanie etykiety "Powered by be-BOP "**: aktywuj przycisk `Wyświetl Powered by be-BOP`, aby wyświetlić tę etykietę w stopce.
- Wprowadź nazwę linku (`Text`)**: wypełnij pole `Text`, które odpowiada treści linku w stopce (przykłady: *Terms*, *Privacy*, *Contact*...).
- Wskaż link Address (`Url`)**: w polu `Url` wprowadź Address strony docelowej (wewnętrznej lub zewnętrznej).
- Dodaj więcej linków w razie potrzeby**: użyj dodatkowych linii, aby utworzyć dowolną liczbę linków.
- Zapisz linki**: kliknij przycisk "Dodaj link stopki", aby zapisać linki.



![footer](assets/fr/016.webp)



### Personalizacja wizualna



**⚠️ Nie zapomnij ustawić logo dla jasnego i ciemnego motywu, a także favicon, poprzez** `Admin > Merch > Pictures`.



Oto jak dostosować wygląd i sposób działania witryny:



#### Przejdź do sekcji Zdjęcia



Menu `Admin` > `Merch` > `Pictures`.



#### Dodaj nowy obraz



Kliknij `Nowe zdjęcie`.



#### Wybierz plik lokalny



Kliknij `Wybierz pliki`, a następnie wybierz obraz z dysku Hard.



#### Wybierz plik do zaimportowania



Kliknij dwukrotnie obraz, który ma zostać zaimportowany (jasne logo, ciemne logo lub favicon).



#### Nadawanie nazwy obrazowi



Wypełnij pole `Nazwa zdjęcia`.



#### Dodaj obraz



Kliknij `Add`, aby sfinalizować import.



![pictures](assets/fr/017.webp)



### Konfiguracja tożsamości sprzedawcy



#### Ustawienia tożsamości



Dostępna poprzez `Admin > Identity` (lub `Settings > Identity`), sekcja ta pozwala skonfigurować informacje administracyjne i prawne firmy.



#### Informacje prawne





- Nazwa firmy**: oficjalna nazwa firmy.
- Identyfikator firmy**: identyfikator prawny lub numer rejestracyjny (RCCM, SIRET...).



#### Biznes Address





- Ulica**: adres pocztowy Address (ulica, numer...).
- Kraj**: kraj.
- Stan**: prowincja lub region.
- Miasto**: miasto.
- Kod pocztowy**: kod pocztowy.



#### Informacje kontaktowe





- E-mail**: profesjonalny e-mail Address.
- Telefon**: numer telefonu firmy.



#### Konto bankowe





- Nazwa posiadacza rachunku**: nazwa posiadacza rachunku.
- Posiadacz rachunku Address**: Address posiadacza.
- IBAN**: Międzynarodowy numer rachunku bankowego.
- BIC**: Kod SWIFT/BIC.



![bank-account](assets/fr/019.webp)



#### Fakturowanie





- Kliknij `Wypełnij głównymi informacjami o sklepie`, aby wstępnie wypełnić dane.
- Very-top-right issuer information**: pole na informacje prawne/podatkowe widoczne na fakturach.
- Kliknij `Update`, aby zapisać zmiany.



**Uwaga:** można również wprowadzić dodatkowe informacje, które mają być wyświetlane na Invoice, zgodnie z potrzebami.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Sklep fizyczny Address



W przypadku sklepów fizycznych należy dodać pełny Address w `Admin > Settings > Identity` lub w dedykowanej sekcji. Umożliwi to wyświetlanie go na oficjalnych dokumentach i w stopce, jeśli zajdzie taka potrzeba.



![seller-id](assets/fr/021.webp)



## Zarządzanie produktem



### Tworzenie nowego produktu



Przejdź do `Admin > Merch > Products`, aby dodać lub zmodyfikować produkt. Wypełnij następujące pola:



#### Podstawowe informacje





- Nazwa produktu**: nazwa produktu (np. *BOP T-shirt edycja limitowana*).
- Slug**: Identyfikator URL bez spacji (np. `tshirt-bop-edition-limitee`).
- Alias** *(opcjonalnie)*: przydatny do szybkiego dodawania do koszyka za pośrednictwem dedykowanego pola.



![product-config](assets/fr/028.webp)



#### Wycena





- Cena**: cena produktu (np. `25.00`).
- Waluta ceny**: waluta (EUR, USD, BTC itp.).
- Produkty specjalne**:
  - jest to produkt bezpłatny.
  - jest to produkt typu "płać ile chcesz".



#### Opcje produktu





- Pojedynczy produkt (`standalone`)**: możliwy tylko jeden dodatek na zamówienie (np. darowizna, bilet wstępu).
- Produkt z odmianami**:
  - Nie sprawdzaj `Standalone`.
  - Zaznacz `Product has light variations (no stock difference)`.
  - Dodaj:
    - Nazwa** (np. *Rozmiar*),
    - Wartości** (np.: S, M, L, XL),
    - Różnice w cenie**, jeśli dotyczy (np.: `+2 USD` dla XL).



![product-details](assets/fr/029.webp)



## Zarządzanie zapasami



### Zaawansowane opcje podczas tworzenia produktu (zapasy, dostawa, bilety itp.)



#### Produkt o ograniczonych zapasach



Jeśli produkt nie jest dostępny w nieograniczonych ilościach, zaznacz opcję `Produkt ma ograniczone zapasy`. Aktywuje to automatyczne śledzenie pozostałych ilości. Po zaznaczeniu tego pola pojawi się pole wskazujące **dostępne zapasy**.



System zarządza:





- Zapas zarezerwowany** → produkty w koszykach, za które jeszcze nie zapłacono
- Zapasy sprzedane** → produkty już zakupione



**Czas rezerwacji koszyka**: Gdy klient dodaje produkt do koszyka, jest on "rezerwowany" na określony czas. Czas ten można zmodyfikować w: `Admin > Config > Cart reservation` (wartość w minutach)



#### Produkt do dostarczenia?



Zaznacz `Produkt ma fizyczny komponent, który zostanie wysłany do Address klienta`. Jest to przydatne w przypadku wszystkich produktów, które mają być wysyłane fizycznie (książki, koszulki itp.)



#### Inne opcje





- Bilet**: zaznacz, jeśli produkt jest biletem na wydarzenie
- Rezerwacja**: sprawdź, czy jest to slot rezerwacji (np. sesja, spotkanie)



![product-options](assets/fr/030.webp)



### Ustawienia akcji (na dole)



Ta sekcja określa **gdzie** i **jak** produkt może być oglądany i kupowany:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Zaznacz tylko te kanały, których chcesz używać.



## Tworzenie i dostosowywanie stron i widżetów CMS



### Obowiązkowe strony CMS



Przejdź do `Admin > Merch > CMS`. Zobaczysz listę istniejących stron i możesz dodać nowe za pomocą **Dodaj stronę CMS**.



Strony CMS są ważne dla:





- Informowanie odwiedzających (np. warunki użytkowania)
- Zgodność z prawem (np. polityka prywatności)
- Wyjaśnienie niektórych funkcji sklepu (np. odbiór IP, 0% VAT)



W razie potrzeby można dodać inne strony:





- O nas / Kim jesteśmy
- Wesprzyj nas / Darowizny
- FAQ
- Kontakt
- itp.



**Wskazówka: Kliknij każdy link lub ikonę, aby zmodyfikować **treść**, **tytuł** lub **widoczność** każdej strony.



### Układ i grafika Elements



Przejdź do: `Admin > Merch > Layout`. Możesz dostosować wizualny Elements swojej witryny:



![product-options](assets/fr/032.webp)



#### Górny pasek





- Modyfikowanie lub usuwanie linków (np. HOME, ABOUT US,...)
- Nawigacja między kluczowymi sekcjami witryny



#### Navbar (główny pasek nawigacyjny)





- Obecny w szarym obszarze poniżej górnego paska
- Zawiera szybki dostęp do: `Konfiguracja`, `Ustawienia płatności`, `Transakcje`, `Zarządzanie węzłami`, `Widgety` itp.
- Tylko dyrektorzy



#### Stopka





- Możliwość edycji z poziomu `Admin > Merch > Layout`
- Zawiera: informacje kontaktowe, przydatne linki, informacje prawne....



#### Dostosowywanie efektów wizualnych



Przejdź do: `Admin > Merch > Pictures`



Możesz:





- Zmień **główne logo**
- Modyfikacja lub dodanie układu **obrazów**



#### Opis strony



Również modyfikowalny w `Pictures`, pozwala na wyświetlenie **podsumowania lub sloganu** w nagłówku lub stopce, w zależności od motywu.



**Uwaga:** pozwala to na dostosowanie wyglądu do tożsamości marki (edukacyjnej, komercyjnej lub społecznościowej).



### Integracja widżetów ze stronami CMS



Widgety** wzbogacają strony CMS o dynamiczne lub wizualne Elements.



#### Tworzenie widżetów



Przejdź do: `Admin > Widgets`



Przykłady dostępnych widżetów:





- Wyzwania**: wyzwania lub misje
- Tagi**: kategorie lub słowa kluczowe
- Slidery**: karuzele obrazów
- Specyfikacje**: Tabele specyfikacji
- Formularze**: formularze (kontaktowe, opinii itp.)
- Odliczanie**: liczniki czasu
- Galerie**: galerie obrazów
- Tablice wyników**: rankingi użytkowników



![widgets](assets/fr/033.webp)



#### Integracja ze stronami CMS



Używaj **kodów skrótów** w treści stron CMS:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Aktualne parametry**:





- `slug`: unikalny identyfikator widżetu
- `display=img-1`: obraz specyficzny dla produktu
- `szerokość`, `wysokość`, `dopasowanie`: wymiary i styl obrazu
- autoplay=3000`: czas w ms pomiędzy dwoma slajdami



**Zalety**:





- Łatwe wstawianie (kopiowanie i wklejanie)
- Dynamiczny: każda modyfikacja widżetu jest automatycznie odzwierciedlana
- Deweloper nie jest wymagany



## Zarządzanie zamówieniami i raportowanie



### Śledzenie zamówień



Aby wyświetlić poprzednie zamówienia i zarządzać nimi, przejdź do: `Admin > Transaction > Orders`



Tutaj znajdziesz **pełną listę zamówień** złożonych w Twojej witrynie.



![orders](assets/fr/034.webp)



#### Wizualizacja i wyszukiwanie



Interface umożliwia wyszukiwanie i filtrowanie zleceń według kilku kryteriów:





- numer zamówienia: numer zamówienia
- alias produktu: identyfikator lub nazwa produktu
- payment Mean": używana metoda płatności (karta, kryptowaluta itp.)
- `Email`: adres e-mail klienta



Filtry te ułatwiają szybkie wyszukiwanie i ukierunkowane zarządzanie.



#### Szczegóły każdego zamówienia



Klikając na zamówienie, można uzyskać dostęp do pełnego pliku zawierającego:





- Zamówione produkty
- Informacje o kliencie
- Dostawa Address (jeśli dotyczy)
- Wszelkie notatki powiązane z zamówieniem



#### Możliwe działania dotyczące zamówienia



Możesz:





- Potwierdź zamówienie (jeśli oczekuje)
- Anulowanie zamówienia (w przypadku problemu lub żądania klienta)
- Dodaj **etykiety** (dla organizacji wewnętrznej)
- Skonsultuj / dodaj **uwagi wewnętrzne**



**Uwaga:** ta sekcja jest niezbędna dla dobrej logistyki i relacji z klientami.



### Raportowanie i eksport



Aby uzyskać dostęp do statystyk sprzedaży i płatności:


administrator > Ustawienia > Raportowanie



![reporting](assets/fr/035.webp)



Tutaj znajdziesz przegląd swojej firmy w postaci **raportów miesięcznych i rocznych**.



#### Treść raportu



Raporty są podzielone na sekcje:





- Szczegóły zamówienia**: liczba zamówień, status (potwierdzone, anulowane, oczekujące), ewolucja
- Szczegóły produktu**: sprzedane produkty, ilości, popularne produkty
- Szczegóły płatności**: zebrane kwoty w podziale na metody płatności



#### Eksport danych



Każda sekcja zawiera przycisk **Export CSV**, który umożliwia:





- Pobieranie danych w formacie CSV
- Otwórz je w programie Excel, Arkuszach Google itp.
- Archiwizacja do celów administracyjnych lub księgowych
- Używaj ich do raportów wewnętrznych



**Uwaga:** Idealny do śledzenia wydajności, księgowości i prezentacji.



## Konfiguracja Nostr Messaging (opcjonalnie)



![nostr-config](assets/fr/036.webp)



Platforma obsługuje protokół **Nostr** dla niektórych zaawansowanych funkcji:





- Zdecentralizowane powiadomienia
- Logowanie bez hasła
- Interface lekka administracja



### Generowanie i dodawanie klucza prywatnego Nostr



Przejdź do:


admin > Zarządzanie węzłami > Nostr





- Kliknij na **Utwórz nsec**, jeśli go nie posiadasz.
- System generate może to zrobić automatycznie.
- Alternatywnie można użyć istniejącego klucza (np. z Damus lub Amethyst).



Następny:





- Skopiuj klucz `nsec`
- Dodaj go do pliku `.env.local` (lub `.env`): ``env NOSTR_PRIVATE_KEY=YourNsecIciKey



### Funkcje aktywowane za pomocą Nostr



Po skonfigurowaniu dostępnych jest kilka funkcji:



**Powiadomienia przez Nostr**





- Wysyłanie powiadomień o zamówieniach, płatnościach lub zdarzeniach systemowych
- Dla administratorów lub użytkowników



**Interface lekka administracja**





- Dostęp za pośrednictwem klienta Nostr
- Umożliwia szybkie i przyjazne dla urządzeń mobilnych zarządzanie



**Połączenie bez hasła**





- Zaloguj się przez bezpieczny link (wysłany przez Nostr)
- Większe bezpieczeństwo użytkownika i płynność



## Projektowanie i dostosowywanie motywów



Aby dostosować wygląd sklepu do karty graficznej, przejdź do: `Admin > Merch > Theme`



Tutaj znajdziesz wszystkie opcje **tworzenia** i **konfiguracji** niestandardowego motywu.



### Tworzenie motywu



![theme](assets/fr/037.webp)



Podczas tworzenia lub modyfikowania motywu można zdefiniować:





- Kolory**: dla przycisków, tła, tekstu, linków itp.
- Czcionki**: wybór krojów pisma dla tytułów, akapitów, menu
- Style graficzne**: obramowania, marginesy, odstępy, kształty bloków



### Konfigurowalne sekcje



Każda część strony może być regulowana niezależnie:





- Nagłówek**: górny pasek nawigacyjny
- Body**: treść główna
- Stopka**: na dole strony



**Uwaga:** ta szczegółowość zapewnia spójność między wizualizacjami witryny a tożsamością marki.



### Aktywacja motywu



Po skonfigurowaniu motywu:





- Kliknij na **Zapisz**
- Aktywuj go jako **główny motyw** sklepu



**Uwaga:** aktywny motyw to ten, który będzie widoczny dla odwiedzających.



## Konfigurowanie szablonów wiadomości e-mail



Platforma umożliwia personalizację wiadomości e-mail wysyłanych automatycznie do użytkowników. Przejdź do: `Admin > Ustawienia > Szablony`



![emails-templates](assets/fr/038.webp)



### Tworzenie/edycja szablonów



Każda wiadomość e-mail (potwierdzenie zamówienia, zapomniane hasło itp.) ma:





- Temat**: temat wiadomości e-mail (np. "Twoje zamówienie zostało zatwierdzone")
- HTML Body**: Zawartość HTML wyświetlana w wiadomości e-mail



**Uwaga:** Możesz wstawiać tekst, obrazy, linki itp. zgodnie z wymaganiami.



### Używanie zmiennych dynamicznych



Aby wiadomości e-mail były dynamiczne, należy wstawić zmienne, takie jak:





- `{orderNumber}}`: zastąpiony przez rzeczywisty numer zamówienia
- `{invoiceLink}}`: link do Invoice
- `{websiteLink}}`: Adres URL witryny



**Uwaga:** tagi te są automatycznie zastępowane po wysłaniu.



### Zaawansowane wskazówki





- Twórz e-maile, które są **responsywne** i łatwe do odczytania na urządzeniach mobilnych
- Dodaj **przyciski akcji** (zapłać, pobierz, śledź zamówienie)
- Przetestuj swoje e-maile, wysyłając je do siebie przed publikacją



## Konfigurowanie określonych tagów i widżetów



### Zarządzanie tagami



Tagi mogą być używane do strukturyzowania i wzbogacania treści. Aby uzyskać do nich dostęp: `Admin > Widgety > Tag`



![tags-config](assets/fr/039.webp)



### Tworzenie tagu



Wypełnij następujące pola:





- Nazwa tagu**: wyświetlana nazwa tagu
- Slug**: unikalny identyfikator (bez spacji i akcentów)
- Rodzina tagów**: grupuje tagi według kategorii



![targsconfig](assets/fr/040.webp)



#### Dostępne rodziny:





- creators`: autorzy lub producenci
- sprzedawcy detaliczni: sprzedawcy lub punkty sprzedaży
- `Temporal`: okresy lub daty
- zdarzenia: zdarzenia powiązane



### Pola opcjonalne



Pola te mogą być użyte do wzbogacenia tagu tak, jakby był stroną z treścią:





- Tytuł
- Podtytuł
- Krótka** treść
- Pełna treść** (w języku francuskim)
- CTA** (przyciski akcji)



### Korzystanie z tagów



Tagi mogą być:





- Przydzielone do produktów
- Zintegrowany ze stronami CMS za pomocą tagu: [Tag=slug?display=var-1]



## Konfiguracja plików do pobrania



Aby zaoferować klientom dokumenty do pobrania: `Admin > Merch > Files`



### Dodawanie pliku



1. Kliknij na **Nowy plik**


2. Inform:




   - Nazwa pliku** (np. *Podręcznik instalacji*)
   - Plik do przesłania** (PDF, obraz, Word...)



**Uwaga:** po dodaniu, platforma automatycznie wygeneruje **stały link**.



### Korzystanie z łącza



Link ten można następnie wstawić do:





- Strona CMS** (jako link tekstowy lub przycisk)
- Klient **e-mail** (za pośrednictwem szablonu)
- **arkusz produktu** (np. pobrana instrukcja obsługi)



Jest to idealne rozwiązanie do dostarczania *podręczników użytkownika, przewodników technicznych, kart produktów...* bez konieczności korzystania z zewnętrznego hostingu.



## Nostr-bot



Platforma oferuje zaawansowaną integrację z protokołem **Nostr** za pośrednictwem automatycznego bota.



Przejdź do: Zarządzanie węzłami > Nostr



### Główne cechy



#### Zarządzanie przekaźnikami





- Dodawanie lub usuwanie **przekaźników** używanych przez bota
- Optymalizacja **zasięgu** i **niezawodności** wysyłanych wiadomości



#### Automatyczna wiadomość wprowadzająca





- Aktywuj automatyczną wiadomość przy **pierwszej interakcji użytkownika**
- Idealny dla:
  - Prezentacja usługi
  - Wyślij przydatny link (np. FAQ, kontakt, zamówienie)



#### Certyfikacja twojego `npub





- Dodaj **logo** i **nazwę publiczną**
- Link do **zweryfikowanej domeny internetowej**
- Zwiększa wiarygodność i rozpoznawalność tożsamości Nostr



### Przypadki użycia Nostr-bota





- Wysyłanie **potwierdzeń zamówień** do Ciebie
- Automatyczna reakcja na **zdarzenia (np. nowe zamówienie)**
- Tworzenie **zdecentralizowanej interakcji z klientem**



## Przeciążanie etykiet tłumaczeń



be-BOP jest wielojęzyczny (FR, EN, ES...), ale możesz dostosować tłumaczenia do swoich potrzeb.



Aby to zrobić, przejdź do: `Ustawienia > Język`



### Ładowanie i edycja



Pliki tłumaczeń są w formacie JSON. Można:





- Pobierz** pliki językowe
- Modyfikowanie** istniejących tekstów
- Dodaj** własne tłumaczenia



Link do oryginalnych plików:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Przykład:** zamień `Add to cart` na `Ajouter au panier` lub `Acheter`.



## Praca zespołowa i punkt sprzedaży (POS)



### Zarządzanie użytkownikami i prawami dostępu



#### Tworzenie ról



Przejdź do: `Admin > Settings > ARM`



Kliknij na **Utwórz rolę**, aby utworzyć rolę (np. `Super Admin`, `POS`, `Ticket checker`).



Każda rola zawiera:





- dostęp do zapisu**: dostęp do zapisu
- dostęp do odczytu**: dostęp do odczytu
- dostęp wzbroniony**: sekcje pośrednie



#### Tworzenie użytkownika



W tym samym menu `Admin > Settings > ARM`, dodaj użytkownika z:





- login
- alias
- odzyskiwanie poczty e-mail
- (opcjonalnie) `recovery npub` dla połączenia przez Nostr



Przypisanie wcześniej zdefiniowanej roli.



![pos-users](assets/fr/045.webp)



Użytkownicy tylko do odczytu** będą widzieć menu w formacie *italic* i nie będą mogli modyfikować zawartości.



## Konfiguracja punktu sprzedaży (POS)



### Przypisywanie roli POS



Aby dać użytkownikowi dostęp do POS, przypisz rolę `Point of Sale (POS)` w: `Admin > Config > ARM`



Może on połączyć się za pośrednictwem bezpiecznego adresu URL: `/pos` lub `/pos/touch`



### Funkcje specyficzne dla POS



Be-BOP oferuje Interface dedykowany sprzedaży fizycznej (sklep, wydarzenie itp.).



#### Szybkie dodawanie za pomocą aliasu



W `/cart`, pole pozwala na dodanie produktu:





- Skanując **kod kreskowy** (ISBN, EAN13)
- Wprowadzając **alias produktu** ręcznie



**Uwaga:** produkt jest automatycznie dodawany do koszyka.



#### Środki płatności



POS obsługuje:





- Gatunek
- Karta kredytowa
- Lightning Network (kryptowaluta)
- Inne w zależności od konfiguracji



Dostępne są dwie opcje zaawansowane:





- Zwolnienie z VAT**: dotyczy uzasadnienia (organizacje pozarządowe, cudzoziemcy...)
- Zniżka na prezent**: wyjątkowa zniżka z obowiązkowym komentarzem



#### Wyświetlanie po stronie klienta



Adres URL `/pos/session` jest przeznaczony dla **dodatkowego ekranu** (HDMI, tablet...):



Plakat:





- Produkty w toku
- Całkowita kwota
- Metoda płatności
- Zastosowane rabaty



**Uwaga:** klient śledzi zamówienie na żywo, podczas gdy sprzedawca zapisuje je na `/pos`.



### Podsumowanie punktów sprzedaży



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Dziękujemy za uważne śledzenie tego samouczka.