---
name: Public Pool
description: Wprowadzenie do basenu publicznego
---

![signup](assets/cover.webp)


**Public Pool** nie jest zwykłą pulą; jest to również tak zwana **Solo Pool**. Jeśli twój Miner odniesie sukces w Mining bloku, otrzymasz cały Block reward, który nie jest udostępniany innym uczestnikom puli ani samej puli.


**Public Pool** zapewnia wyłącznie **szablon bloku** dla Miner, dzięki czemu może on wykonywać swoje zadanie bez konieczności posiadania **węzła Bitcoin** i oprogramowania komunikującego się z Miner. Ponieważ nie łączysz swojej mocy obliczeniowej z mocą obliczeniową innych uczestników, twoje szanse na pomyślne Mining bloku są oczywiście bardzo niskie, przypominając nieco system loterii, w którym czasami szczęśliwa osoba wygrywa jackpota.


![signup](assets/1.webp)


Na **Dashboardzie** **Publicznej puli** nadal dostępne są pewne statystyki, takie jak **Łączna liczba Hashrate** puli, a także rozkład różnych typów górników, którzy są podłączeni do puli.


![signup](assets/2.webp)


W pierwszych kilku linijkach możemy zobaczyć **Bitaxe** z 1323 **Bitaxe** połączonymi dla łącznej prędkości 649TH/s. **Bitaxe** to **projekt open source**, który pozwala na proste ponowne wykorzystanie chipa z **ASIC**, takiego jak **Antminer S19**, na **opensource** płytce elektronicznej, aby stworzyć maleńki Miner o prędkości 0,5TH/s dla 15W. Jest to Miner, którego użyjemy jako przykładu w tym samouczku.


## Dodanie **Pracownika** 👷‍♂️


![signup](assets/cover.webp)


Na górze strony można skopiować pulę Address **stratum+tcp://public-pool.io:21496**.


Następnie w polu **user** wprowadź **Bitcoin** Address, którego jesteś właścicielem.


Jeśli masz wielu górników, możesz wprowadzić ten sam Address dla wszystkich z nich, aby ich **hashraty** zostały połączone i wyświetlane jako pojedynczy Miner. Można je również rozróżnić, dodając odrębną nazwę dla każdego z nich. Aby to zrobić, wystarczy dodać **.workername** po **Bitcoin** Address.


Wreszcie, w polu **hasło** należy użyć **'x'**.


Przykład: Jeśli twój **Bitcoin** Address to **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'** i chcesz nazwać swój Miner **" Brrrr "**, to wprowadzisz następujące informacje w Interface swojego Miner:



- **URL**: stratum+tcp://public-pool.io:21496
- **UŻYTKOWNIK**: **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr'**
- **Hasło**: **'x'**

Jeśli twój Miner to **Bitaxe**, pola są nieco inne, ale informacje pozostają takie same:


- **URL**: public-pool.io (tutaj należy usunąć część na początku **'stratum+tcp://'** i część na końcu **':21496'**, która zostanie zgłoszona w polu portu)
- **Port**: 21496
- **Użytkownik**: **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr'**
- **Hasło**: **'x'**


![signup](assets/3.webp)


Kilka minut po uruchomieniu Mining będziesz mógł zobaczyć swoje dane na stronie **Public Pool**, wyszukując swój Address.


## Pulpit nawigacyjny


![signup](assets/4.webp)


Po połączeniu się z **Public Pool**, możesz uzyskać dostęp do **Dashboard**, wyszukując **Bitcoin** Address, który wpisałeś w polu **User**. W naszym przypadku jest to **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'**.


Na **Dashboardzie** wyświetlane są różne informacje dotyczące zarówno danych użytkownika, jak i sieci.


![signup](assets/5.webp)


Dostępna jest **Sieć Hash Rate**, która odpowiada całkowitej mocy roboczej sieci **Bitcoin**.


**Trudność sieci** wskazuje trudność, która musi zostać osiągnięta w celu zatwierdzenia bloku.


A **Twój najlepszy poziom trudności** to najwyższy poziom trudności, jaki osiągnąłeś. Jeśli przypadkiem 🍀 osiągniesz trudność sieciową, wygrasz cały Block reward... po 100 blokach. Będziesz musiał poczekać 100 bloków, zanim będziesz mógł je wydać.


Masz również **Wysokość bloku**, która jest numerem ostatniego wydobytego bloku, a także jego wagą wyrażoną w WU, przy czym maksymalna wartość to 4 000 000.


Poniżej możesz zobaczyć wszystkie statystyki każdego z urządzeń indywidualnie, jeśli nadałeś im odrębną nazwę, dodając **.name** za **Bitcoin** Address w polu **Użytkownik**.