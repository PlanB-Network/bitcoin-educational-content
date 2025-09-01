---
name: F-Cold
description: Katalog darmowych i otwartych aplikacji.
---

![cover](assets/cover.webp)



W erze cyfrowej duże korporacje i instytucje pracują nad tym, aby Internet stał się bardziej scentralizowany, oddając kontrolę nad nim w swoje ręce, a tym samym ograniczając prywatność i wolność wszystkich użytkowników. To nie jest utopia, to już się dzieje. Jako bitcoiner, decentralizacja, poszanowanie prywatności i wolności jednostki to zasady, które są ci drogie, zwłaszcza w narzędziach, z których korzystasz na co dzień. Android, w przeciwieństwie do iOS, od lat pozwala na współistnienie kilku sklepów z aplikacjami w swoim ekosystemie, dając ci swobodę wyszukiwania i instalowania aplikacji z ulubionych źródeł.



W tym samouczku przyjrzymy się F-droid, katalogowi aplikacji, który stanowi alternatywę dla sklepów z aplikacjami, takich jak Google Play Store i Microsoft Store.



## Rozpoczęcie pracy z F-Droid



F-Droid to sklep z aplikacjami i narzędziami, który umożliwia instalowanie bezpłatnych aplikacji typu open source na platformie Android. Sam F-droid jest projektem open source zapoczątkowanym w 2010 roku przez Ciarana Gultnieksa i kilku innych współpracowników. Głównym celem projektu jest udostępnienie aplikacji open source i umożliwienie inicjatorom projektów open source znalezienia platformy, na której mogą publikować swoje narzędzia bez konieczności odwoływania się do sklepu Google Play.



Niestety, F-Droid nie jest aplikacją dostępną na iOS i zawiera wiele narzędzi zaprojektowanych dla systemów Android.



Możesz pobrać F-droid z [oficjalnej strony] (https://f-droid.org/) w formacie APK i zainstalować go ręcznie na swoim telefonie z Androidem.



![download](assets/fr/02.webp)



W systemie Android upewnij się, że przyznałeś uprawnienia do instalacji dla przeglądarki, z której pobrałeś F-Droid.



Po zakończeniu instalacji F-Droid uruchomi aktualizację katalogów aplikacji Open Source, aby wzbogacić aplikacje w sklepie.



![repositories](assets/fr/03.webp)



Aplikacje można teraz instalować na telefonie bez konieczności przechodzenia przez Sklep Google Play.



## Księgarnia F-Droid



W sklepie z aplikacjami znajdziesz kilka kategorii aplikacji dostosowanych do Twoich potrzeb. W zakładce **Kategorie** znajdziesz ponad 20 rodzajów aplikacji, od przeglądarek po darmowe edytory tekstu, a wszystkie wymagają jak najmniejszej ilości informacji z twojej strony.



Chcesz zainstalować konkretną aplikację? Kliknij przycisk **Szukaj**, a następnie wprowadź nazwę aplikacji, której szukasz.



![search](assets/fr/04.webp)



F-Droid dostarcza wyczerpujących informacji na temat każdej aplikacji, którą chcesz zainstalować.



Klikając na aplikację, znajdziesz między innymi:




- Funkcje i zmiany dodane w najnowszej dostępnej wersji
- Szczegółowy opis aplikacji, jej funkcji, powodów korzystania z niej oraz społeczności Open Source stojącej za projektem.



![features](assets/fr/05.webp)





- Licencja używana przez projekt, odnośniki do kodu źródłowego i problemów napotkanych podczas korzystania z aplikacji
- Uprawnienia wymagane przez aplikację



![permissions](assets/fr/06.webp)



Dowiedz się więcej w naszym samouczku Thunderbird:



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid zapewnia wszystkie informacje potrzebne do podjęcia decyzji, czy korzystanie z aplikacji chroni dane i zwiększa prywatność. Zeskanuj wszystkie aplikacje, których chcesz używać, a następnie kliknij przycisk **Install**, aby pobrać i zainstalować aplikację.


Przyznaj uprawnienia do instalacji F-Droid, włączając tę opcję w ustawieniach.



![settings](assets/fr/07.webp)



## Exchange Twoje aplikacje



F-Droid zachęca do praktyki open source i wkładu społeczności, w szczególności poprzez opcję **Near By** Exchange. Połącz się z użytkownikami wokół ciebie przez:




- Wykrywanie Bluetooth;
- Ta sama sieć Wi-Fi;
- Kod QR lub IP:PORT Address do wprowadzenia w przeglądarce.



Dzięki tej opcji możesz udostępniać i odbierać aplikacje zainstalowane na telefonie z Androidem znajomym i rodzinie w zaledwie kilku krokach.



![swap](assets/fr/08.webp)



## Aktualizacje



W zakładce **Update** zapoznaj się z listą dostępnych aktualizacji i upewnij się, że przeczytałeś również informacje o nowych wersjach każdej aplikacji, aby dowiedzieć się o wszelkich istotnych zmianach w używanej wersji.



![updates](assets/fr/09.webp)



Listę dostępnych aplikacji można również zaktualizować, odświeżając stronę (przewijając ją w dół).



## Dodawanie własnych aplikacji



F-Droid to projekt Open Source, który zachęca do tworzenia aplikacji, które priorytetowo traktują prywatność użytkowników. Możesz dodać własną aplikację mobilną na Androida do sklepu poprzez wkład do kodu źródłowego F-Droid GitLab.



Twoja aplikacja musi być open source, z kodem źródłowym publicznie dostępnym na przykład na GitHub lub GitLab.


Następnie należy przygotować plik YAML (metadane) opisujący aplikację, w tym wszystkie informacje i uprawnienia wymagane do jej używania, zgodnie z szablonem [metadata template](https://f-droid.org/docs/Build_Metadata_Reference/) zaproponowanym przez F-Droid.



W sekcji **Developers** [dokumentacji](https://f-droid.org/en/docs/) znajdziesz wszystkie zasoby potrzebne do publikowania i utrzymywania aplikacji na F-Droid.



### Integralność i bezpieczeństwo



Umieszczenie aplikacji w otwartym kodzie źródłowym jest często równoznaczne ze zwiększonym bezpieczeństwem, ale także ze znacznym ryzykiem. Jak upewnić się, że w kodzie źródłowym aplikacji dostępnej na F-Droid nie ma złośliwych zmian?



F-Droid kompiluje aplikacje na własnych serwerach, w oparciu o oficjalny kod źródłowy i instrukcje kompilacji. Każda opublikowana aplikacja jest przebudowywana i weryfikowana, aby upewnić się, że nie została naruszona. Gwarantuje to, że oferowany APK jest wierny kodowi źródłowemu opublikowanemu przez deweloperów. Co więcej, każda aplikacja instalowana za pośrednictwem F-Droid jest podpisywana cyfrowo, a następnie odcisk palca podpisu jest porównywany z tym ogłoszonym przez twórców aplikacji na oficjalnej stronie internetowej lub w repozytorium Git.



Jeśli spodobał Ci się ten poradnik, dowiedz się więcej o naszym kursie dotyczącym bezpieczeństwa IT i zarządzania danymi:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1