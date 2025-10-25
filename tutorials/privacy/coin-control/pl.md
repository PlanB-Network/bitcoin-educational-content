---
name: Coin Control
description: Zapoznaj się z Coin Control, kluczowym narzędziem do ochrony twojej prywatności w Bitcoin
---
![cover](assets/cover.webp)


*Ten samouczek został zaimportowany z [lekcji Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Wprowadzenie



Solidność protokołu Bitcoin jest gwarantowana przez proste kluczowe koncepcje. Wśród nich wyróżnia się przejrzystość: wszystkie transakcje Bitcoina są publiczne i łatwe do zweryfikowania przez każdego. Chociaż ta cecha jest kamieniem milowym protokołu, ponieważ zapobiega oszustwom i zapewnia autentyczność środków, może również stanowić wyzwanie dla poufności. **Zastanawiałeś się, czy taka przejrzystość może zagrozić twojej prywatności?**



Powinieneś. Podczas gdy gromadzenie Satoshi non-kyc jest raczej łatwe, twoja prywatność jest najbardziej zagrożona na etapie wydawania.



### Co się stanie, gdy wydasz UTXO



Wydawanie Bitcoin nie jest po prostu przekazywaniem wartości komuś innemu.



Korzystając z jednego ze swoich UTXO, musisz w rzeczywistości spełnić warunki nałożone na przejrzystość protokołu, ponieważ masz obowiązek udowodnić, że jesteś właścicielem tych funduszy. W ten sposób stajesz się odpowiedzialny za :




- ujawnić swój klucz publiczny;
- wygenerować podpis cyfrowy.



Czas wydawania jest zatem najbardziej krytyczny: **wydawanie Bitcoin jest czynnością, którą należy wykonywać świadomie i z jak największą kontrolą**.



## Kontrola Coin



W protokole Bitcoin elementy takie jak _konto_ czy _jednostki monetarne_ nie istnieją. Koncepcja UTXO jest doskonale wyjaśniona w poniższym kursie, który gorąco polecam:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Z Bitcoin to, co gromadzisz, a później wydajesz, to małe lub duże jednostki konta mierzone w Satoshi, reprezentowane przez "niewydane wyniki transakcji", **UTXO**, zwane również "monetami". Kiedy używasz UTXO do tworzenia transakcji, są one całkowicie niszczone, a na ich miejsce tworzone są inne UTXO.



Portfele programowe są opracowywane w celu automatycznego dokonywania tego wyboru, przy użyciu "losowo" wybranych monet, przyjmując określone algorytmy dostarczone przez protokół. Jedynym kryterium, jakie spełniają te algorytmy, jest pokrycie kwoty potrzebnej do wydania.



Mogą one łączyć UTXO w różnym wieku lub faworyzować wydawanie najnowszych lub "najstarszych", w zależności od algorytmu wybranego przez programistów. Najlepsze portfele programowe planują również pozostawić użytkownikowi ważny wybór.



Instrukcja `Coin Control`, którą można również znaleźć pod nazwą `Coin Selection`, to funkcja niektórych portfeli programowych, która pozwala **ręcznie wybrać UTXO do wydania podczas tworzenia transakcji**.



Załóżmy, że mamy Wallet z 3 UTXO wynoszącymi odpowiednio 21 000, 42 000 i 63 000 Satoshi.



![img](assets/en/01.webp)



Jeśli musisz wydać 24 000 Sats i pozwolić algorytmowi na automatyczną selekcję, dobry Software Wallet może zdecydować się na połączenie UTXO 1 + UTXO 2, aby zapłacić 24 tys. opłat Sats i Miner, tworząc resztę, która wraca do wewnętrznego Address początkowego Wallet.



![img](assets/en/02.webp)



Po transakcji, nową sytuację w Wallet, licząc tylko UTXO, można podsumować następująco.



![img](assets/en/03.webp)



Mając jednak odpowiednie oprogramowanie i świadomość, można było dokonać innego, pod pewnymi względami bardziej poprawnego wyboru. Na przykład wybierając tylko UTXO2 (z 42 000 Sats).



![img](assets/en/04.webp)



Z sytuacją końcową w Wallet, na poziomie UTXO, wygląda to inaczej niż wcześniej.



![img](assets/en/05.webp)



## Dlaczego ręczny coin control?



![img](assets/en/06.webp)



W dwóch powyższych przykładach saldo jest w rzeczywistości takie samo `108,280 Sats`. Po wydaniu 24 000 Sats, bez ręcznego wyboru mielibyśmy 2 UTXO w Wallet; z ręcznym sterowaniem Coin mamy łącznie 3.



Pytanie, które moglibyśmy sobie zadać, brzmi następująco: **dlaczego robić to wszystko?** Istnieją, lub mogłyby istnieć, różne powody, dla których nie użyliśmy `UTXO1` **i wszystkie one stanowią podstawę tego, dlaczego — na etapie wydawania — aktywacja ręcznej kontroli monet jest jedną z dobrych praktyk, które należy stosować**.



Wybór UTXO pozwala faworyzować niektóre aspekty nad innymi. Wybór tak naprawdę zależy od celów, które chcesz osiągnąć.



### Prywatność



Jedną z głównych zalet, jeśli chodzi o ręczną kontrolę Coin, jest **większa prywatność wydawcy**. Weźmy zawsze nasz przykład: wydatek 24.000 Satoshi _bez ręcznego wyboru Coin_. Ponieważ Blockchain z Bitcoin jest rekordem publicznym, zewnętrzny obserwator może bez cienia wątpliwości stwierdzić, że wejścia `UTXO1 z 21.000 Sats` i `UTXO2 z 42.000 Sats`, jak również reszta, `UTXO5 z 38.280 Sats` **wszystkie trzy należą do tego samego użytkownika**.



Po ręcznym wybraniu `UTXO2`, z drugiej strony, `UTXO1` pozostaje całkowicie zarezerwowane, siedząc w zestawie UTXO i czekając na wykorzystanie w bardziej odpowiednim momencie.



UTXO1 może pochodzić ze źródła KYC, takiego jak płatność otrzymana w Exchange za towary i usługi, podczas gdy inne UTXO nie. Mieszanie UTXO-kyc z innymi, które są bardziej poufne, narusza zestaw anonimowości funduszy nie-kyc.



**Środki KYC nieuchronnie doprowadziłyby do ustalenia tożsamości płatnika. Gdyby to był twój portfel, czy chciałbyś, aby zewnętrzny obserwator mógł ustalić twoją tożsamość z tak absolutną pewnością?**



Spróbuj więc wziąć pod uwagę, że portfele, które implementują ręczny wybór UTXO, na przykład, pozwalają na **segregację jednego lub więcej UTXO**, funkcję do wykorzystania w takich sytuacjach.



Chociaż jestem przekonany, że środki KYC powinny być przechowywane w oddzielnym Wallet niż Bitcoin zakupione bez KYC, jeśli tak jest w twoim przypadku, segregacja niektórych adresów jest kluczową pomocą, z której możesz skorzystać, ucząc się ręcznie wybierać dane wejściowe do wydatków.



### Oszczędność na opłatach



Wybór właściwego UTXO do dokonania wydatku, **pozwala na optymalizację opłat**. Ponownie zaczynając od naszego początkowego przykładu, Software Wallet wybrał dwa UTXO, aby pokryć wydatki, które mają zostać poniesione. Dwa UTXO oznaczają dwa podpisy do pokazania w sieci. Wynika z tego, że transakcja ma większą "wagę" pod względem vBajtów.



Z drugiej strony, korzystając z ręcznego sterowania Coin, można wybrać tylko jeden, który jest wystarczający do pokrycia kwoty, oszczędzając opłaty poprzez zmniejszenie "wagi" transakcji.



W czasach, gdy opłaty są wysokie, ale jesteś zmuszony wydać Bitcoin On-Chain (np. aby otworzyć kanał Lightning Network), to właśnie wtedy kontrola Coin okazuje się właściwą zachętą ekonomiczną.



### Agregacja szczątków



Kiedy dokonujesz płatności i używasz Bitcoin On-Chain, możliwość otrzymania reszty prawie zawsze staje się pewna. Każda reszta jest sama w sobie niewielką utratą prywatności, ponieważ ujawnia sieci (a zwłaszcza odbiorcy płatności) twój Address, który może być powiązany z twoim wejściem źródłowym.



Biorąc pod uwagę, że najlepsze Wallet HD mają specjalne adresy generate dla pozostałości, można je łatwo rozpoznać i "posegregować" wszystkie pozostałości po różnych dokonanych transakcjach; gdy osiągną określoną kwotę, można je wybrać ręcznie i skonsolidować lub zamienić na Lightning Network (preferowana przeze mnie metoda) i przetworzyć je tak, aby odzyskać prywatność utraconą w wydatkach.



### Wydatki z Cold Wallet



Cold Wallet to instrument, za pomocą którego można rozsądnie uzyskać dobry stopień bezpieczeństwa, aby przechowywać dowolną ilość środków na bok przez długi okres czasu. Jednak nieprzewidziane wydarzenia mogą się zdarzyć, więc pojawia się potrzeba zdobycia oszczędności i pokrycia nieoczekiwanych wydatków.



Nie wiem, jak wielu może podzielać moje podejście, ale moja rada jest taka, aby **nigdy nie dokonywać wydatków bezpośrednio z Cold Wallet, aby uniknąć otrzymania zmiany między adresami tego samego**. Naucz się ręcznie wybierać UTXO potrzebne do pokrycia wydatku, przenieś je do Wallet Hot i przygotuj transakcję z tego ostatniego. Każdą zmianę można następnie odesłać z powrotem do Cold Wallet Address (jeśli kwota jest odpowiednia), wykorzystać ją na inne wydatki lub nadal segregować, jak właśnie widzieliśmy.



## Praktyczna prezentacja


Po technicznym wprowadzeniu "dlaczego", zobaczmy jak zastosować ręczne sterowanie Coin w praktyce z różnym oprogramowaniem, stacjonarnym i mobilnym. Zawsze będziemy używać tego samego Wallet BIP39, zaimportowanego do każdego z wybranych narzędzi, aby pokazać niewielkie różnice między nimi.



## Wallet Desktop



### Sparrow



Jeśli używasz Sparrow, otwórz Wallet i wybierz _UTXOs_ z menu po lewej stronie. Wyświetli się lista wszystkich UTXO powiązanych z Wallet.



Wystarczy kliknąć myszką na jednym z nich, a następnie wybrać opcję _Wyślij wybrane_. Sparrow pokazuje również łączną kwotę dostępną do wydania po dokonaniu wyboru, tuż obok polecenia. Graficznie Sparrow pokazuje wybrany UTXO podświetlając go na niebiesko.



![img](assets/en/07.webp)



Można również wybrać więcej niż jeden. Użyj klawisza _CTRL_, aby wybrać nieprzylegające UTXO na liście.



![img](assets/en/08.webp)



Po ręcznym wybraniu UTXO, możesz zacząć budować transakcję, a Sparrow pokaże ci dobrze, graficznie, jak się ona składa.



![img](assets/en/09.webp)



#### Segregacja UTXO



Segregacja środków oznacza "zablokowanie" ich w Wallet, aby nie mogły zostać użyte jako dane wejściowe do transakcji. Sparrow umożliwia tę funkcję, która jest zawsze dostępna z menu _UTXOs_: należy umieścić mysz nad UTXO, który ma zostać "zablokowany" i kliknąć prawym przyciskiem myszy. Wśród funkcji tej procedury pojawi się _Freeze UTXO_. W ten sposób będzie można segregować monety w portfelach Sparrow.



![img](assets/en/29.webp)



### Electrum



Jeśli twój pulpit Wallet to Electrum, powinieneś wiedzieć, że możesz ręcznie wybrać UTXO z menu _Adresy_ lub z menu _Koszty_. W obu menu wybór odbywa się poprzez wskazanie myszką żądanego UTXO i wybranie _Dodaj do kontroli Coin_ po kliknięciu prawym przyciskiem myszy.



![img](assets/en/10.webp)



Nawet w tym oprogramowaniu można wybrać więcej niż jeden UTXO, pomagając sobie klawiszem _CTRL_ na klawiaturze, jeśli nie sąsiadują one ze sobą.



![img](assets/en/11.webp)



Graficznie Electrum pokaże wybór, podświetlając wybrane UTXO w Green, podczas gdy na dole pojawi się pasek, podświetlony w tym samym kolorze, pokazujący dostępne saldo po kontroli Coin.



![img](assets/en/12.webp)



Po wybraniu wyjścia lub wyjść można utworzyć transakcję w zwykły sposób, korzystając z menu _Send_.



#### Segregacja UTXO



Electrum zapewnia tę funkcję, przechodząc do menu _Coins_, gdzie należy wybrać konkretny UTXO, a następnie wybierając _Freeze_ prawym przyciskiem myszy. Możesz "zamrozić" Address nawet bez środków z menu _Addresses_ lub "Coin", aby go nie wydawać.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk pozwala na ręczne wybranie UTXO z menu głównego po jego otwarciu. Uruchom Nunchuka i kliknij _Wyświetl monety_.



![img](assets/en/13.webp)



Spowoduje to otwarcie okna zawierającego wszystkie UTXO w Wallet, w którym można wybrać jedną lub więcej, aktywując znacznik wyboru obok każdej kwoty. Po dokonaniu wyboru przejdź do opcji _Create transaction_ (Utwórz transakcję).



![img](assets/en/14.webp)



Następnie można wprowadzić miejsce docelowe Address i ustawić kwotę oraz opłaty.



![img](assets/en/15.webp)



#### Segregacja UTXO



Dla kompletności, Nunchuk pozwala również na segregację jednego (lub więcej) UTXO i robi to na dwa różne sposoby. Wejdź do menu _View coins_ i ręcznie wybierz z listy monet. Następnie kliknij menu _More_ w prawym dolnym rogu: pojawi się lista opcji, z której możesz wybrać _Lock coins_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Można również kliknąć miejsce zarezerwowane dla UTXO, aby uzyskać dostęp do okna _Coin details_. W prawym górnym rogu pojawi się polecenie zablokowania/odblokowania danego UTXO.



![img](assets/en/41.webp)



### Aplikacja Blockstream



Aplikacja Blockstream App desktop, wcześniej znana jako Green, umożliwia wybór Coin po rozpoczęciu tworzenia transakcji. Dlatego otwórz Wallet i kliknij _Send_.



![img](assets/en/16.webp)



Wklej docelowy Address do odpowiedniego pola, a następnie wybierz _Ręczny wybór Coin_.



![img](assets/en/17.webp)



Otworzy się okno, w którym można wybrać jedną lub więcej monet UTXO. W poniższym przykładzie wybraliśmy dwie monety. Następnie potwierdź swój wybór, klikając _Confirm Coin Selection_.



![img](assets/en/18.webp)



Ustaw kwotę i opłaty, a następnie kontynuuj normalnie transakcję.



![img](assets/en/19.webp)



⚠️ N.B. W menu _Coins_ Green znajdują się pozycje _Lock_/_Unlock_, które zapowiadają możliwość segregacji UTXO. Ta funkcja jest aktywowana tylko na tak zwanych kontach Multisig; jest również aktywowana tylko poprzez wybranie UTXO o bardzo małej kwocie, zbliżonej do progu `Dust`.



## Wallet mobile



Portfele można również wybierać z urządzeń mobilnych, które umożliwiają ręczny wybór UTXO. Zobaczmy Blue Wallet jako pierwszy przykład.



### Niebieski Wallet



Jeśli jesteś użytkownikiem tego Wallet, otwórz go i kliknij, aby przejść do ekranów kontrolnych związanych z jednym z portfeli. Aby uzyskać dostęp do instrukcji obsługi Coin, należy wejść w fazę wydatków, a następnie kliknąć przycisk _Send_.



![img](assets/en/21.webp)



Na następnym ekranie wybierz menu oznaczone trzema kropkami w prawym górnym rogu. Otworzy się rozwijane okno z serią poleceń. Wybierz ostatnie z nich: _Coin Control_.



![img](assets/en/22.webp)



W tym momencie niebieski Wallet pokazuje wszystkie UTXO. Oprócz kwot są one rozróżniane graficznie za pomocą różnych kolorów.



![img](assets/en/27.webp)



Wybierz UTXO, a następnie wybierz _Use Coin_.



![img](assets/en/23.webp)



Blue Wallet przeniesie Cię z powrotem do okna _Send_, aby kontynuować tworzenie transakcji. Dostosuj kwotę i opłaty, a następnie wybierz _Next_.



![img](assets/en/24.webp)



W tym momencie możesz zakończyć transakcję, tak jak zwykle to robisz.



#### Segregacja UTXO



Niebieski Wallet pozwala również segregować UTXO, czyniąc je niedostępnymi do wydawania, co nie jest złą funkcją dla Wallet z urządzenia mobilnego. Dostęp do kontroli Coin uzyskuje się za pomocą procedury opisanej powyżej, a po wybraniu UTXO należy wybrać _Freeze_ zamiast _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



Mobilna wersja Nunchuka umożliwia również użytkownikowi sterowanie Coin. Jeśli używasz tej aplikacji z telefonu komórkowego, otwórz ją i przejdź do menu _Wallet_. Następnie wybierz _View coins_.



![img](assets/en/30.webp)



W oknie, w którym wyświetlana jest lista UTXO, kliknij przycisk _Select_.



![img](assets/en/38.webp)



Funkcja wyboru pojawia się obok każdego UTXO. Podobnie jak w wersji na komputery stacjonarne, ręczny wybór na Nunchuk mobile odbywa się poprzez zaznaczenie małego kwadratu obok kwoty. Ekran pokazuje liczbę wybranych UTXO i całkowitą dostępną kwotę. Po zakończeniu kliknij symbol ₿ w lewym dolnym rogu, który jest poleceniem rozpoczęcia tworzenia transakcji.



![img](assets/en/31.webp)



Teraz możesz sfinalizować transakcję, wybierając kwotę i klikając przycisk Kontynuuj.



![img](assets/en/32.webp)



Kontynuuj jak zawsze, wklejając miejsce docelowe Address, opis i dostosowując ustawienia opłat.



#### Segregacja UTXO



Możesz również segregować UTXO za pomocą mobilnego Nunchuka. Przejdź do dedykowanego okna listy monet i wybierz strzałkę obok UTXO, który chcesz posegregować.



![img](assets/en/42.webp)



Zobaczysz miejsce zarezerwowane na _Szczegóły monety_, gdzie możesz wybrać _Zablokuj tę monetę_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper jest ostatnim Wallet, który zobaczymy w tym przewodniku. Widzimy jego funkcjonalność zastosowaną do kontroli Coin z Wallet single-sig, chociaż takie zastosowanie nie jest celem tej konkretnej aplikacji. Po skonfigurowaniu Keeper na telefonie, uruchom go i otwórz Wallet zawierający pewne środki. Na środku ekranu głównego kliknij _View All Coins_.



![img](assets/en/34.webp)



Keeper wyświetla przegląd UTXO. Aby przejść do ekranu wyboru, kliknij _Select To Send_.



![img](assets/en/35.webp)



Możesz wybrać monety, zaznaczając je, klikając odpowiednie polecenie. Po zakończeniu kliknij przycisk _Wyślij_.



![img](assets/en/36.webp)



Bitcoin Keeper przenosi użytkownika bezpośrednio do menu _Send_, gdzie można utworzyć transakcję z wybranymi UTXO.



![img](assets/en/37.webp)



## Hardware Wallet



Każdy z portfeli programowych przedstawionych w tym przewodniku może być tylko zegarkiem Interface dla jednego z portfeli sprzętowych. Oznacza to, że kontrola Coin dla urządzenia podpisującego offline jest wykonywana za pomocą kroków opisanych do tej pory.



### Zalecenia ogólne



Kontrola Coin jest bardzo skuteczną praktyką wyboru danych wejściowych transakcji. Ręczny wybór jest jeszcze bardziej skuteczny, jeśli podczas kupowania/otrzymywania środków dobrze oznaczyłeś źródło swoich Satoshis. Jeśli chcesz dobrze nauczyć się tej techniki, polecam poniższy samouczek:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Rozmawialiśmy wcześniej o `segregacji pozostałości`. Jeśli chcesz zablokować resztki do późniejszego przetworzenia i odzyskać prywatność (swap na Layer 2), musisz zadbać o ich `oznakowanie` za każdym razem, gdy je otrzymasz. Spośród dotychczasowych portfeli programowych tylko Electrum graficznie koloruje resztki UTXO, aby były widoczne na pierwszy rzut oka. Inne, takie jak Sparrow, pokazują łańcuch w ścieżce wyprowadzania poszczególnych UTXO (`m/84'/0'/0'/1/11`).



Aby skutecznie stosować tę technikę, pamiętaj, aby zawsze dodawać opis do otrzymanej reszty: osoba, do której wysłałeś swoje środki (płatność, samouczek lub inne), zna Address powiązany ze zmianą i wie, że należy ona do Ciebie, ponieważ pochodzi z transakcji, którą razem wykonaliście!