---
name: Tiankii
description: Pakiet narzędzi Lightning dla sprzedawców detalicznych i konsumentów
---

![cover](assets/cover.webp)



W ekosystemie Bitcoin przyjmowanie płatności w czasie rzeczywistym pozostaje głównym wyzwaniem dla firm i osób fizycznych. Tradycyjne rozwiązania często wymagają zaawansowanej wiedzy technicznej, złożonej infrastruktury do utrzymania lub wymagają przechowywania środków przez pośredników. Sytuacja ta powstrzymuje masowe przyjęcie Bitcoin jako codziennej waluty, pomimo obietnicy postępu technologicznego Lightning Network.



Tiankii, salwadorska firma założona w 2021 roku, odpowiada na ten problem, oferując dostępną, modułową infrastrukturę Bitcoin. Zamiast wymuszać przyjęcie zamkniętego ekosystemu, Tiankii oferuje zestaw wzajemnie połączonych narzędzi umożliwiających każdemu integrację Bitcoin Lightning z ich działalnością bez poświęcania kontroli nad swoimi funduszami.



## Czym jest Tiankii?



### Pochodzenie i filozofia



Tiankii - termin z języka nahuatl oznaczający "rynek na świeżym powietrzu dostępny dla wszystkich" - to pierwszy w Salwadorze start-up w 100% wykorzystujący Bitcoin. Założona przez Darvina Otero po przyjęciu Bitcoin jako prawnego środka płatniczego w kraju, firma ma na celu przekształcenie Bitcoin z magazynu wartości w walutę transakcyjną do codziennych zakupów. W przeciwieństwie do platform powierniczych, Tiankii przyjmuje podejście niepowiernicze, w którym użytkownicy zachowują kontrolę nad swoimi środkami, a infrastruktura służy jedynie jako pośrednik techniczny.



### Architektura techniczna



Tiankii jest dostawcą infrastruktury Bitcoin-as-a-Service opartej na Lightning Network. Ta technologia drugiej warstwy umożliwia niemal natychmiastowe transakcje przy znikomych kosztach, umożliwiając mikropłatności i codzienne zakupy.



Architektura opiera się na trzech filarach:



**Najpierw Lightning**: Systematyczne faworyzowanie sieci Lightning ze względu na jej szybkość i niższe koszty, przy jednoczesnym zachowaniu obsługi transakcji on-chain dla dużych kwot.



**Otwarte standardy**: Wykorzystanie LNURL do automatyzacji żądań płatności, Lightning Address do czytelnych identyfikatorów e-mail oraz Bolt Card do interoperacyjnych płatności NFC.



** Modułowość niezależna od wallet**: Możliwość podłączenia różnych portfeli Lightning (LNbits, Blink, BlueWallet) lub własnego węzła, oferując maksymalną elastyczność w zależności od wymaganego poziomu wiedzy i autonomii.



## Narzędzia ekosystemu Tiankii



### Bitcoin POS - sklepowy terminal płatniczy



Aplikacja zamienia smartfon lub tablet w terminal Lightning. Sprzedawca wprowadza kwotę w lokalnej walucie, a aplikacja generuje kod QR Lightning lub akceptuje kartę Bolt. Transakcje są natychmiast uznawane bez prowizji, z automatycznym przeliczaniem w ponad 150 walutach, zarządzaniem napiwkami i historią sprzedaży.



### Merchant Dashboard - ujednolicone zarządzanie sprzedażą



Interface web scentralizowany do łączenia wallet Lightning, śledzenia transakcji w czasie rzeczywistym, wystawiania faktur i generate raportów księgowych. Platforma agreguje wszystkie kanały: płatności w sklepie (POS), sprzedaż online (wtyczki e-commerce) lub integracje API. Płatności są zbieżne na wybranym wallet.



### Karta zbliżeniowa Bitcoin (karta Bolt)



Karta NFC Bolt stanowi główną innowację Tiankii w demokratyzacji Bitcoin dla ogółu społeczeństwa. Działa jak zbliżeniowa karta bankowa i pozwala płacić za zakupy Bitcoin Lightning po prostu dotykając kompatybilnego terminala.



W przeciwieństwie do tradycyjnych rozwiązań powierniczych, karta ta jest zgodna z otwartym standardem gwarantującym interoperacyjność. Użytkownicy mogą połączyć ją z własnym wallet za pośrednictwem aplikacji IBI, zachowując w ten sposób swoje klucze prywatne i pełną kontrolę nad powiązanymi środkami. Płatność trwa zaledwie sekundę, bez konieczności wyjmowania smartfona lub posiadania aktywnego połączenia internetowego w momencie płatności.



Rozwiązanie to jest szczególnie przyjazne dla osób niezaznajomionych ze smartfonami, oferując przystępną bramę do gospodarki Bitcoin.



### Aplikacja IBI - Interface indywidualny Bitcoin



Aplikacja IBI (Individual Bitcoin Interface) jest przeznaczona dla osób, które chcą korzystać z Bitcoin Lightning na co dzień. Jej główną zaletą jest generowanie spersonalizowanego Address Lightning, identyfikatora płatności czytelnego w formacie e-mail (przykład: alice@ibi.me).



Identyfikator ten drastycznie upraszcza otrzymywanie płatności: nie ma potrzeby wystawiania nowej faktury generate dla każdej transakcji, nadawca może po prostu wprowadzić adres Lightning. Interfejs pozwala również zarządzać kartą Bolt (aktywacja, dezaktywacja, limity wydatków), łączyć różne portfele Lightning i dokonywać płatności poprzez skanowanie kodów QR.



### Wtyczki e-commerce



Gotowe do użycia integracje dla WooCommerce, Shopify i Cloudbeds. Instaluje się w ciągu kilku minut, aby dodać Bitcoin Lightning do kasy. Korzyści: zerowa prowizja (w porównaniu z kartami kredytowymi 2-3%), natychmiastowe rozliczenie, dostęp na całym świecie, eliminacja obciążeń zwrotnych. Płatności docierają bezpośrednio do połączonego wallet sprzedawcy.



### Bitcoin API i narzędzia deweloperskie



Tiankii SDK umożliwia integrację Bitcoin Lightning z istniejącymi aplikacjami bez konieczności utrzymywania własnego węzła. API obsługuje tworzenie faktur, weryfikację płatności i masowe wysyłki za pośrednictwem solidnej infrastruktury hostowanej w Google Cloud. Command Center uzupełnia ofertę dla organizacji z Address Lightning w niestandardowych domenach, płatnościach masowych i scentralizowanym zarządzaniu terminalami i kartami NFC.



## Instalacja i pierwsze kroki



### Niezbędne warunki wstępne



Korzystanie z Tiankii nie wymaga skomplikowanych warunków technicznych. Aplikacje działają za pośrednictwem przeglądarki internetowej na smartfonie, tablecie lub komputerze. Nie jest wymagana instalacja natywnej aplikacji: wszystko, czego potrzebujesz, to dostęp do Internetu i najnowsza przeglądarka, aby uzyskać dostęp do IBI lub Merchant Dashboard.



**Dla użytkowników prywatnych (aplikacja IBI)**: Nie jest wymagane wcześniejsze posiadanie wallet Lightning. Po utworzeniu konta Tiankii automatycznie konfiguruje działający Address Lightning za pośrednictwem [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), bezwęzłowej implementacji, która wykorzystuje sieć Liquid w tle. Możesz natychmiast otrzymywać i wysyłać płatności bez żadnej konfiguracji technicznej. To rozwiązanie drastycznie upraszcza dostęp dla początkujących, pozostając jednocześnie samowystarczalnym.



**Dla sprzedawców (Pulpit sprzedawcy)** : Podłączenie istniejącego wallet Lightning jest obowiązkowe do korzystania z terminali w punktach sprzedaży i otrzymywania płatności. Tiankii obsługuje wiele rozwiązań: portfele mobilne (Blink, Strike), rozwiązania self-hosted (LNbits, LND/CLN node) lub portfele internetowe (Alby). Szczegółowe instrukcje połączeń są dostępne w sekcji Zasoby tego samouczka.



### Dla klientów prywatnych: IBI App



**Tworzenie konta



Przejdź na stronę accounts.ibi.me, aby utworzyć konto. Na tej stronie możesz wybrać jeden z dwóch typów kont: "Personal Use" do użytku indywidualnego lub "Business Use" do użytku komercyjnego. Wybierz opcję "Personal Use", aby uzyskać dostęp do narzędzi umożliwiających odbieranie i wysyłanie płatności w Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



Po wybraniu opcji "Użytek osobisty" nastąpi automatyczne przekierowanie na stronę go.ibi.me w celu dokończenia rejestracji. Można to zrobić za pośrednictwem poczty e-mail, numeru telefonu lub konta Google, Microsoft lub Twitter. Po utworzeniu konta można natychmiast uzyskać dostęp do interfejsu IBI, w którym działa już Lightning Address.



![Création du compte](assets/fr/02.webp)



**Interface main**



Interfejs IBI wyświetla saldo w satoshis i lokalnej walucie (USD). Trzy przyciski umożliwiają interakcję: "Odbierz", aby otrzymywać płatności, "Skanuj", aby zeskanować kod QR i "Wyślij", aby wysłać satoshi.



![Interface IBI](assets/fr/03.webp)



**Odbierz płatność**



Aby odebrać satoshis, naciśnij "Odbierz". Aplikacja automatycznie wygeneruje kod QR i wyświetli spersonalizowany adres Address Lightning (format nom@ibi.me). Udostępnij ten adres lub kod QR nadawcy: środki natychmiast dotrą na Twoje konto IBI.



![Réception avec Lightning Address](assets/fr/04.webp)



Po zaksięgowaniu salda możesz użyć tych satoshis do dokonywania płatności.



**Wyślij płatność**



Aby wysłać satoshis, naciśnij "Wyślij". Możesz zeskanować kod QR Lightning lub bezpośrednio wprowadzić miejsce docelowe Lightning Address.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Wprowadź żądaną kwotę w satoshis, sprawdź równowartość w lokalnej walucie, a następnie potwierdź płatność.



![Confirmation du montant](assets/fr/07.webp)



Powiadomienie o powodzeniu potwierdza wysyłkę ze szczegółami: wysłaną kwotą, opłatą transakcyjną i odbiorcą.



![Paiement réussi](assets/fr/08.webp)



**Zarządzanie kontem



W Ustawieniach można zarządzać kartami Bitcoin NFC (karty Bolt). Interfejs umożliwia aktywację, dezaktywację lub ustawienie limitów wydatków dla kart.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Dla sprzedawców: Pulpit sprzedawcy i POS



**Tworzenie konta biznesowego



Przejdź do accounts.ibi.me, aby utworzyć konto. Wybierz opcję "Business Use", aby uzyskać dostęp do narzędzi dla sprzedawców. Ten typ konta odblokowuje dostęp do pulpitu sprzedawcy i terminali w punktach sprzedaży.



Po wybraniu opcji "Business Use" nastąpi automatyczne przekierowanie do panelu sprzedawcy (pay.tiankii.com). Spowoduje to przejście do interfejsu zarządzania biznesem ze śledzeniem przychodów, transakcjami i narzędziami płatności. Aby rozpocząć przyjmowanie płatności, należy najpierw podłączyć wallet Lightning, klikając łącze u góry strony (patrz strzałka na obrazku).



![Dashboard marchand](assets/fr/11.webp)



*połączenie *wallet Lightning**



Kluczowy krok w aktywacji punktu sprzedaży: podłącz wallet Lightning, aby otrzymywać płatności. Interfejs oferuje kilka opcji połączenia. Należy pamiętać, że niektóre opcje (Bitcoin Onchain i Lightning Network) są nadal w fazie rozwoju i są wyszarzone w interfejsie.



![Options de connexion wallet](assets/fr/12.webp)



W tym samouczku używamy połączenia Lightning Address, kompatybilnego z Chivo, Blink Wallet i Strike. Wprowadź swój Lightning Address (format nom@domaine.com), na przykład od LN Markets, Alby lub innego kompatybilnego dostawcy.



![Saisie de la Lightning Address](assets/fr/13.webp)



Po zalogowaniu konto jest gotowe do działania. Możesz teraz uzyskać dostęp do POS lub powrócić do pulpitu nawigacyjnego, aby skonfigurować inne ustawienia.



![Connexion réussie](assets/fr/14.webp)



*linki do płatności** * Linki do płatności



Menu "Narzędzia płatności" zapewnia dostęp do opcji "Żądanie płatności", która umożliwia tworzenie linków do płatności i zarządzanie nimi. Ta funkcja jest przydatna do generowania spersonalizowanych linków do płatności wysyłanych pocztą elektroniczną lub wiadomością: darowizn, pojedynczych płatności, wielu płatności, a nawet paywalli w celu ochrony treści. Możesz tworzyć różne rodzaje linków, aby dopasować je do swoich potrzeb biznesowych.



![Liens de paiement](assets/fr/15.webp)



**Konfiguracja terminala sprzedaży**



Aby akceptować płatności w sklepie, przejdź do menu "Terminal sprzedaży" w "Narzędziach płatności". Ta sekcja umożliwia tworzenie terminali POS i zarządzanie nimi (liczba terminali zależy od planu, patrz plany Freemium vs. Business poniżej). Kliknij "Otwórz", aby otworzyć interfejs POS w przeglądarce.



![Gestion des terminaux](assets/fr/16.webp)




**Generowanie sprzedaży**



Terminal POS wyświetla klawiaturę numeryczną do wprowadzania kwoty sprzedaży. Wprowadź kwotę w lokalnej walucie (np. 500 sats odpowiada 630,74 ARS), a następnie naciśnij "OK", aby potwierdzić.



![Saisie du montant](assets/fr/17.webp)



Aplikacja natychmiast generuje kod Lightning QR i kartę Lightning Address do płatności. Klienci mogą zeskanować kod QR za pomocą wallet lub użyć karty Bolt na terminalu NFC.



![QR code de paiement](assets/fr/18.webp)



Po otrzymaniu płatności pojawi się ekran potwierdzenia, pokazujący otrzymaną kwotę w lokalnej walucie i satoshis. Możesz wysłać potwierdzenie e-mailem, wydrukować bilet lub natychmiast rozpocząć nową sprzedaż.



![Paiement encaissé](assets/fr/19.webp)



**Monitorowanie i zarządzanie**



Wszystkie transakcje są rejestrowane w panelu sprzedawcy. Masz możliwość pełnego śledzenia przychodów według okresu, całkowitej liczby sprzedaży i szczegółowej historii księgowości.



Interfejs ustawień oferuje kilka zakładek konfiguracyjnych. Zakładka "Ustawienia ogólne" umożliwia zarządzanie profilem sprzedawcy i powiadomieniami. Zakładka "Użytkownicy" umożliwia dodawanie i zarządzanie dostępem do panelu sprzedawcy dla zespołu (zarządzanie wieloma użytkownikami zgodnie z planem). Zakładka "Development Workspace" daje dostęp do kluczy API dla zaawansowanych integracji, a "Subscription" pozwala zarządzać subskrypcją.



![Paramètres du compte marchand](assets/fr/20.webp)



**Plany freemium a plany biznesowe



Tiankii oferuje dwa pakiety dla Merchant Dashboard. Plan **Freemium** (bezpłatny) jest odpowiedni dla start-upów z ograniczeniami: pojedynczy punkt sprzedaży, pojedynczy użytkownik, miesięczny wolumen ograniczony do 1000 USD i brak dostępu do konektorów e-commerce. Plan **Business** (opłata 0,5% za transakcję) oferuje nieograniczoną liczbę terminali, nieograniczoną liczbę użytkowników, nieograniczony wolumen, dostęp do wtyczek WooCommerce/Shopify/Cloudbeds i ekskluzywne powiadomienia WhatsApp.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Korzyści i ograniczenia



### Najważniejsze wydarzenia



**Self-custodial**: Zachowujesz klucze prywatne i pełną kontrolę nad swoimi środkami. Brak ryzyka zamrożenia konta lub bankructwa platformy zewnętrznej.



**Prostota**: Lightning Address jako adres e-mail, płatności NFC za pomocą prostego dotknięcia, intuicyjny interfejs bez konieczności posiadania specjalistycznej wiedzy technicznej.



**Kompletny ekosystem**: Narzędzia dla wszystkich profili (osób fizycznych, sprzedawców detalicznych, deweloperów) z modułowymi integracjami dostosowanymi do Twoich potrzeb.



**Profesjonalna zgodność**: Bezpieczny hosting w chmurze, zgodność z PCI-DSS, zgodność z przepisami obowiązującymi w Salwadorze.



### Ograniczenia



**Błyskawiczne ograniczenia**: Wymaga stałego połączenia wallet, zarządzania płynnością dla dużych wolumenów, ryzyka awarii, jeśli odbiorca jest offline. Tiankii łagodzi te aspekty dzięki zintegrowanym LSP.



**Zależność od SaaS**: Jeśli Tiankii jest niedostępne, generowanie faktur jest tymczasowo niemożliwe (środki użytkownika pozostają bezpieczne).



**Prywatność**: Tiankii może obserwować metadane transakcji (kwoty, daty). Mniej prywatne niż rozwiązanie hostowane samodzielnie, takie jak BTCPay Server.



## Wnioski



Tiankii ilustruje, w jaki sposób dobrze zaprojektowana infrastruktura może usunąć bariery techniczne uniemożliwiające masowe przyjęcie Bitcoin jako waluty codziennego użytku. Łącząc moc Lightning Network z podejściem nie wymagającym nadzoru i dostępnymi narzędziami, ekosystem oferuje zrównoważoną ścieżkę między suwerennością finansową a łatwością użytkowania.



Dla sprzedawców Tiankii stanowi okazję do drastycznego obniżenia kosztów transakcji przy jednoczesnym uzyskaniu dostępu do nowej bazy klientów. Dla konsumentów, karty Lightning Address i NFC przekształcają Bitcoin w praktyczną walutę, bez technicznych komplikacji.



Chociaż powszechne przyjęcie Bitcoin pozostaje wyzwaniem wymagającym edukacji i czasu, infrastruktury takie jak Tiankii pokazują, że narzędzia techniczne już istnieją. Misja uproszczenia płatności Bitcoin nie jest już odległą wizją, ale rzeczywistością dostępną dla każdego, kto chce podjąć wyzwanie.



## Zasoby



### Oficjalna dokumentacja




- [Oficjalna strona Tiankii](https://tiankii.com)
- [Centrum pomocy Tiankii](https://help.tiankii.com)
- [aplikacja IBI](https://go.ibi.me)
- [Panel sprzedawcy](https://pay.tiankii.com)
- [Centrum dowodzenia](https://cc.ibi.me)



### Prowadnice połączeniowe Wallet




- [Connect LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Wspólnota




- [Lightning Network Plus](https://lightningnetwork.plus) - Błyskawiczne zasoby edukacyjne
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salwadorska inicjatywa gospodarki o obiegu zamkniętym Bitcoin



### Powiązane narzędzia




- [Blink Wallet](https://blink.sv) - zalecana kompatybilność z Wallet Lightning
- [LNbits](https://lnbits.com) - Samodzielnie hostowane rozwiązanie wallet
- [Standardowa karta Bolt](https://github.com/boltcard) - Specyfikacje techniczne kart NFC