---
name: Bitcoin Keeper - Plan dziedziczenia
description: Zaplanuj transmisję bitcoinów z Bitcoin Keeper
---

![cover](assets/cover.webp)



Transfer aktywów Bitcoin jest jednym z wyzwań najbardziej niedocenianych przez posiadaczy. W przeciwieństwie do konta bankowego, gdzie instytucja finansowa może przekazać środki prawowitym spadkobiercom, Bitcoin opiera się całkowicie na posiadaniu kluczy prywatnych. Prawowity spadkobierca nigdy nie będzie w stanie uzyskać dostępu do środków bez tych kluczy, podczas gdy złośliwa osoba będąca w posiadaniu tajemnic będzie mogła je wydać bez żadnych formalności.



W tym drugim samouczku Bitcoin Keeper zbadamy funkcje premium poświęcone planowaniu nieruchomości. Aplikacja oferuje zaawansowane narzędzia do tworzenia Enhanced Vaults, z mechanizmami ochrony czasowej dzięki Miniscript, a także dokumentami towarzyszącymi, aby poprowadzić swoich bliskich.



Ten przewodnik zakłada, że opanowałeś już podstawy Bitcoin Keeper (tworzenie portfolio, klasyczny multisig, dodawanie kluczy sprzętowych), jak wyjaśniono w naszym pierwszym samouczku:



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-22cbfb8d-790f-4a6f-a92f-93a117e1e65c

![video](https://youtu.be/tCld_-n2d30)



## Plany subskrypcji Bitcoin Keeper



Bitcoin Keeper działa w modelu freemium z trzema poziomami subskrypcji oferującymi progresywną funkcjonalność. Aby uzyskać dostęp do planów, przejdź do zakładki **Więcej**, a następnie dotknij bieżącego planu (domyślnie "Pleb"), aby otworzyć ekran **Zarządzaj subskrypcją**.



![Plans d'abonnement](assets/fr/01.webp)



Plan **Pleb** (bezpłatny) zapewnia dostęp do podstawowych funkcji: nieograniczone tworzenie portfeli z jednym i wieloma kluczami, kompatybilność ze wszystkimi głównymi portfelami sprzętowymi (Coldcard, Trezor, Ledger, Jade, Tapsigner...), kontrolę monet, etykietowanie i połączenie z osobistym serwerem Electrum. Ten plan jest wystarczający do standardowego użytku, a nawet do klasycznych konfiguracji multi-sig.



Plan **Hodler** (9,99 €/miesiąc, z 1 miesiącem za darmo przy płatności rocznej) obejmuje wszystkie funkcje Pleb i dodaje szyfrowane kopie zapasowe w chmurze (iCloud lub Google Drive), aby przywrócić sejfy na dowolnym urządzeniu, Server Key, aby dodać automatyczne zasady wydatków i 2FA powyżej określonego progu, oraz Canary Wallets, aby wykryć nieautoryzowany dostęp do kluczy.



Plan **Diamond Hands** (29,99 €/miesiąc, z 1 miesiącem gratis przy płatności rocznej) to kompletny pakiet do planowania spadkowego. Obejmuje on cały plan Hodlera i odblokowuje klucz spadkowy (odroczona aktywacja), klucz awaryjny (klucz awaryjny do odzyskania w przypadku utraty), narzędzia i dokumenty planowania spadkowego oraz rozmowę telefoniczną z zespołem Concierge w celu zatwierdzenia konfiguracji. Jest to oferta dla bitcoinerów, którzy chcą przekazać swoje dziedzictwo kilku pokoleniom.



Ważna uwaga: utworzone skarbce pozostaną dostępne nawet po powrocie do planu bezpłatnego. Konfiguracje są oparte na otwartych standardach (BSMS, Miniscript) i działają niezależnie od subskrypcji.



## Dokumenty spadkowe



Po aktywowaniu subskrypcji Diamond Hands należy przejść do sekcji **Dokumenty spadkowe** w zakładce Więcej. Bitcoin Keeper zawiera pięć przykładowych dokumentów do struktury planu spadkowego, a także sekcję ze wskazówkami:



![Documents d'héritage](assets/fr/02.webp)





- Seed Words Template**: szablon do uporządkowanego zapisywania fraz odzyskiwania
- Zaufane kontakty**: szablon listy danych kontaktowych zaufanych osób zaangażowanych w plan (notariusz, prawnik, spadkobiercy, opiekunowie kluczy)
- Dodatkowy klucz współdzielony**: dokument zawierający szczegółowe informacje techniczne dla każdego klucza: Kod PIN, ścieżka derywacji, fizyczna lokalizacja, typ urządzenia i wszelkie inne informacje przydatne do identyfikacji i używania klucza
- Instrukcje odzyskiwania środków**: instrukcje krok po kroku dla spadkobiercy lub beneficjenta dotyczące odzyskiwania środków
- List do pełnomocnika**: wstępnie wypełniony list, który można dostosować do potrzeb prawnika lub notariusza



Sekcja **Porady spadkowe** oferuje praktyczne porady dotyczące zabezpieczania kluczy dla spadkobierców i optymalizacji planu spadkowego.



Dostosuj te dokumenty do swojej sytuacji i przechowuj je w bezpiecznym miejscu, oddzielnie od samych kluczy.



## Konfigurowanie kopii zapasowej w chmurze



Przed utworzeniem starszego skarbca należy aktywować kopię zapasową w chmurze, aby chronić pliki konfiguracyjne. W zakładce Więcej naciśnij **Personal Cloud Backup**.



![Configuration Cloud Backup](assets/fr/03.webp)



Wybierz silne hasło do szyfrowania kopii zapasowych. Hasło to chroni tylko pliki konfiguracyjne wallet (nie klucze prywatne). Potwierdź hasło i naciśnij **Confirm**. Kopie zapasowe będą przechowywane w iCloud lub Google Drive, w zależności od urządzenia. Naciśnij **Backup Now**, aby uruchomić pierwszą kopię zapasową.



## Import kluczy sprzętowych



W naszym przykładzie utworzymy sejf 2 na 3 z dwoma dodatkowymi kluczami (Dziedziczenie i Awaryjny). Zacznijmy od zaimportowania wszystkich niezbędnych kluczy do zakładki **Keys**.



![Import des clés hardware](assets/fr/04.webp)



Naciśnij **Add key**, a następnie wybierz **Add key from a hardware**, aby podłączyć sprzętowy wallet. Bitcoin Keeper obsługuje wiele urządzeń: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner i Specter Solutions.



W naszej konfiguracji importujemy :




- 2 klucze **Coldcard** (MK4SP i MK4)
- 2 klawisze **Tapsigner** (Metro i Genesis)



Aby dodać kartę Coldcard, wybierz ją z listy i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby wyeksportować klucz publiczny za pomocą kodu QR, pliku, USB lub NFC. Aby uzyskać więcej informacji na temat korzystania z karty Coldcard lub Tapsigner, zapoznaj się z naszymi dedykowanymi samouczkami:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Po zaimportowaniu wszystkich kluczy znajdziesz je w zakładce Klucze z ich niestandardowymi nazwami.



## Tworzenie starszego wallet



Przejdźmy teraz do tworzenia bagażnika. W zakładce **Wallets** naciśnij **Add Wallet**, wybierz **Bitcoin Wallet**, a następnie **Create Wallet**.



![Création du wallet](assets/fr/05.webp)



Wybierz typ wallet. W przypadku naszego starszego planu wybierz **2 z 3 kluczy wieloklawiszowych**. W dolnej części ekranu aktywuj **Enhanced Security Options**, a następnie naciśnij **Proceed**.



![Options de sécurité avancées](assets/fr/06.webp)



W wyskakującym okienku Enhanced Security Options zaznacz :




- Klucz dziedziczenia**: dodatkowy klucz, który zostanie dodany do kworum po określonym czasie
- Klucz awaryjny**: klucz z odroczoną całkowitą kontrolą w celu odzyskania środków w przypadku utraty klucza



Naciśnij **Zapisz zmiany**. Następnie wybierz 3 klucze, które utworzą wallet z zaimportowanych (np. Seed Key, Coldcard MK4SP i Tapsigner Metro).



## Ustalanie specjalnych kluczowych terminów



Następny ekran umożliwia skonfigurowanie klucza awaryjnego i klucza dziedziczenia. W tym miejscu definiuje się opóźnienia regulujące aktywację tych specjalnych kluczy.



![Configuration des délais](assets/fr/07.webp)



Dla **Klucza awaryjnego** wybierz klucz sprzętowy, który będzie służył jako ostateczna kopia zapasowa (tutaj Coldcard MK4) i wybierz opóźnienie aktywacji (w naszym przykładzie: 2 lata). W przeciwieństwie do klucza dziedziczenia, klucz awaryjny nie dodaje się do kworum: pozwala **całkowicie ominąć multisig** i daje całkowitą kontrolę nad środkami po upływie limitu czasu. Jest to rozwiązanie ostateczne: jeśli kilka kluczy zostanie utraconych lub zniszczonych, ten pojedynczy klucz pozwala odzyskać wszystko. Dlatego musi być chroniony z najwyższą starannością.



Dla **Klucza dziedziczenia** wybierz klucz przeznaczony dla spadkobiercy (tutaj Coldcard MK4SP) i wybierz opóźnienie (w naszym przykładzie: 1 rok). Po roku bez ruchu, klucz ten **zostanie dodany do kworum podpisu**. W praktyce klucz wallet 2-of-3 stanie się kluczem wallet 2-of-4 po upływie tego okresu, umożliwiając spadkobiercy uczestnictwo w podpisie wraz z istniejącymi kluczami.



### Jak działają zegary sterujące?



Bitcoin Keeper wykorzystuje **absolutne blokady czasowe** (CLTV - CheckLockTimeVerify), możliwe dzięki Miniscript. W przeciwieństwie do względnych blokad czasowych (CSV), które rozpoczynają się po otrzymaniu każdego UTXO, bezwzględne blokady czasowe działają z **ustaloną datą wygaśnięcia** zdefiniowaną podczas tworzenia wallet.



Mówiąc konkretnie, jeśli utworzysz wallet dzisiaj z rocznym kluczem spadkowym, datą aktywacji będzie "dzisiaj + 1 rok". Wszystkie środki zdeponowane w tym wallet, niezależnie od daty ich zdeponowania, będą dostępne za pośrednictwem klucza dziedziczenia w tym samym dniu.



Zaletą bezwzględnych zegarów jest to, że pozwalają one na czasy realizacji przekraczające 15 miesięcy (limit względnych zegarów CSV), co wyjaśnia, dlaczego Bitcoin Keeper może oferować opcje takie jak 2 lata.



### Mechanizm odświeżania



Aby zapobiec aktywacji kluczy specjalnych w trakcie życia użytkownika, należy okresowo "odświeżać" wallet. W przypadku bezwzględnych blokad czasowych polega to na **odtworzeniu wallet z nową datą wygaśnięcia** przesuniętą w przyszłość, a następnie przeniesieniu środków na ten nowy wallet.



Bitcoin Keeper upraszcza ten proces dzięki zintegrowanej funkcji odświeżania. Aplikacja automatycznie obsługuje złożoność w tle: wystarczy postępować zgodnie z instrukcjami, bez konieczności ręcznego tworzenia nowego wallet lub samodzielnego przesyłania środków. Zaplanuj tę operację regularnie, z dużym wyprzedzeniem przed upływem najkrótszego skonfigurowanego okresu. Na przykład, w przypadku klucza dziedziczenia na 1 rok, odświeżaj co 9-10 miesięcy, aby zachować margines bezpieczeństwa.



## Zapisywanie i eksportowanie konfiguracji



Po utworzeniu wallet aplikacja przypomina o zapisaniu pliku konfiguracyjnego. **Ten krok jest krytyczny**: bez tego pliku spadkobiercy nie będą mogli odtworzyć wallet multisig.



![Export de la configuration](assets/fr/08.webp)



Naciśnij **Backup Wallet Recovery File**. Dostępnych jest kilka opcji eksportu:




- Eksport PDF**: generuje kompletny dokument zawierający wszystkie informacje wallet
- Pokaż QR**: wyświetla kod QR w celu zaimportowania konfiguracji na inne urządzenie
- Airdrop / File Export**: eksportuje plik za pośrednictwem opcji udostępniania
- NFC**: udostępnianie przez NFC za pomocą kompatybilnego urządzenia



Pomnóż kopie: jedna u notariusza, jedna w sejfie bankowym, jedna zaszyfrowana wersja cyfrowa. Twój nowy wallet pojawi się teraz w zakładce Portfele z tagami "Multi-key", "2 of 3", "Inheritance key" i "Emergency key".



## Utwórz kanarka Wallet



Canary Wallet to system wczesnego ostrzegania. Idea: każdy klucz używany w wallet multi-key może być również używany w oddzielnym wallet single-key. Poprzez zdeponowanie niewielkiej kwoty na "kanarku" wallet, każdy nieautoryzowany ruch sygnalizuje naruszenie klucza.



![Canary Wallets](assets/fr/09.webp)



Istnieją dwa sposoby konfiguracji Wallet Canary. W zakładce **Więcej** naciśnij **Portfele kanarka** w sekcji "Klucze i portfele". Ekran wyjaśnia zasadę: jeśli ktoś uzyska dostęp do jednego z twoich kluczy i znajdzie środki w powiązanym pojedynczym kluczu wallet, spróbuje je usunąć, co spowoduje ostrzeżenie.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Można również skonfigurować Canary bezpośrednio z klucza. W zakładce **Klucze** wybierz klucz (np. Tapsigner Genesis), naciśnij ikonę **Ustawienia** (koło zębate), a następnie **Kanarek Wallet**. Otworzy się powiązany kanarek wallet, gotowy do odebrania niektórych satelitów nadzoru.



Zdeponuj niewielką sumę (kilka tysięcy satoshi) na każdym Canary Wallet. Jeśli te fundusze zostaną przeniesione bez twojej zgody, natychmiast usuń zainfekowany klucz z sejfów multisig.



## Najlepsze praktyki



**Przetestuj swoją konfigurację** z niewielką kwotą pieniędzy, zanim wpłacisz do niej dużą sumę. Wyślij kilka tysięcy satoshi do skarbca, a następnie spróbuj wydać wychodzące, aby sprawdzić, czy opanowałeś proces podpisywania na każdym urządzeniu. Przetestuj również importowanie pliku konfiguracyjnego na innym telefonie, aby upewnić się, że kopia zapasowa działa.



**Inteligentna dystrybucja kluczy**. W przypadku Tapsignerów należy przekazać je w zapieczętowanej kopercie z kodem PIN przekazanym osobno (np. w liście z instrukcjami odzyskiwania przechowywanym w innym miejscu). W przypadku klasycznych portfeli sprzętowych przechowuj urządzenie u zaufanej osoby trzeciej, a seed na papierze lub metalu u siebie lub innej osoby trzeciej. Zanotuj odcisk palca każdego klucza i jego nazwę w pliku konfiguracyjnym, aby uniknąć pomyłek.



**Zaplanuj okresowe testy** (ćwiczenia przeciwpożarowe). Co roku sprawdzaj, czy możesz odtworzyć sejf z kopii zapasowych na pustym telefonie. Przetestuj alerty Canary, sprawdzając salda. Symuluj scenariusze utraty ("co jeśli zgubię kartę Coldcard?"), aby potwierdzić, że pozostałe kombinacje kluczy są wystarczające.



**Nie zapomnij o odświeżaniu**. Jeśli ustawiłeś klucz dziedziczenia na 1 rok, odświeżaj go co 9-10 miesięcy. Jest to cena za automatyczną transmisję bez interwencji osób trzecich.



**Dbaj o aktualność planu**. Każda zmiana (wymiana klucza, modyfikacja spadkobierców, zmiana terminu) musi być odzwierciedlona we wszystkich kopiach zapasowych i dokumentach. Regeneruj pliki PDF po każdej modyfikacji i redystrybuuj nowe wersje.



## Ograniczenia i rozważania



Pomimo mocy tych narzędzi, ważne jest, aby rozpoznać ich ograniczenia, aby zarządzać nimi tak skutecznie, jak to tylko możliwe.



**Złożoność** sejfu multisig z timelockami może być ryzykiem samym w sobie: błędna konfiguracja, niezrozumienie przez spadkobierców, utrata krytycznego elementu wśród wielu komponentów. Bitcoin Keeper upraszcza to doświadczenie tak bardzo, jak to możliwe, ale pozostaje operacją techniczną. Wdrażaj ten plan tylko wtedy, gdy uzasadnia to kwota, która ma być chroniona. W przypadku niewielkich kwot może wystarczyć prostszy plan.



Warto zastanowić się nad **zależnością od aplikacji**. Chociaż kod jest open source i opiera się na otwartych standardach (Miniscript, BSMS), niektóre funkcje zależą od ekosystemu Keeper. Zachowaj kopię aplikacji (Android APK lub iOS IPA) i udokumentuj w listach do spadkobierców możliwość korzystania z innych portfeli kompatybilnych z Miniscript (takich jak Liana) w celu odzyskania środków.



Zaufani brokerzy** wprowadzają ryzyko ludzkie. Co się stanie, jeśli krewny o złych intencjach użyje powierzonego mu klucza przed upływem terminu? Albo jeśli prawnik zgubi dokumenty? Wybierz te osoby ostrożnie, wyjaśnij jasno ich obowiązki i miej plan B. Portfele Canary, nadmiarowe kopie zapasowe i sama struktura multisig pozostają najlepszą ochroną przed tymi zagrożeniami.



## Wnioski



Bitcoin Keeper, dzięki planowi Diamond Hands, oferuje kompletny zestaw narzędzi do planowania nieruchomości: Ulepszone skarbce z kluczami czasowymi, dokumenty towarzyszące, portfele Canary i spersonalizowane wsparcie.



To coś więcej niż tylko kwestia techniczna: to kwestia zaprojektowania architektury twojego majątku, inteligentnej dystrybucji kluczy i wiedzy oraz regularnego testowania systemu. Dobrze zaprojektowany plan dziedziczenia Bitcoin przekształca twoje satoshis w prawdziwe, zbywalne dziedzictwo.