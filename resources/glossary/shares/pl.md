---
term: AKCJE
---

W kontekście puli Mining udział jest wskaźnikiem wykorzystywanym do ilościowego określenia wkładu indywidualnego Miner w ramach puli. Miara ta służy jako podstawa do obliczenia nagrody, którą pula redystrybuuje do każdego Miner. Każdy udział odpowiada Hash, który spełnia cel trudności niższy niż w sieci Bitcoin.


Aby wyjaśnić to za pomocą analogii, rozważmy 20-stronną kość. Na Bitcoin załóżmy, że Proof of Work wymaga wyrzucenia liczby niższej niż 3 w celu zatwierdzenia bloku (czyli uzyskania wyniku 1 lub 2). Wyobraźmy sobie teraz, że w ramach Mining pool docelowy poziom trudności akcji wynosi 10. W związku z tym, dla indywidualnego Miner w puli, każdy rzut kostką, który daje liczbę niższą niż 10, liczy się jako ważny udział. Te akcje są następnie przekazywane do puli przez Miner, aby odebrać nagrodę, nawet jeśli nie odpowiadają one prawidłowemu wynikowi dla bloku na Bitcoin.


Dla każdego obliczonego Hash, indywidualny Miner w puli może napotkać trzy różne scenariusze:


- Jeśli wartość Hash jest większa lub równa ustawionemu celowi trudności puli dla akcji, to ten Hash jest bezużyteczny. Następnie Miner zmienia swój Nonce, aby spróbować nowego Hash: `Hash > udział > blok`.
- Jeśli Hash jest niższy niż docelowy poziom trudności udziału, ale większy lub równy docelowemu poziomowi trudności Bitcoin, wówczas ten Hash stanowi ważny udział, który nie jest jednak wystarczający do zatwierdzenia bloku. Miner może wysłać ten Hash do swojej puli, aby odebrać nagrodę związaną z akcją: `udział > Hash > blok`.
- Jeśli Hash jest niższy niż docelowy poziom trudności sieci Bitcoin, jest on uważany zarówno za prawidłowy udział, jak i prawidłowy blok. Miner przesyła ten Hash do swojej puli, która pospiesznie rozgłasza go w sieci Bitcoin. Ten Hash jest również liczony jako ważny udział dla Miner: `udział > blok > Hash`.


![](../../dictionnaire/assets/32.webp)


Ten system udziału jest wykorzystywany do szacowania pracy wykonanej przez każdy indywidualny Miner w puli, bez konieczności indywidualnego przeliczania wszystkich skrótów generowanych przez Miner, co byłoby całkowicie nieefektywne dla puli.


Pule Mining dostosowują trudność akcji, aby zrównoważyć obciążenie weryfikacyjne i zapewnić, że każdy Miner, niezależnie od tego, czy jest mały, czy duży, przesyła akcje mniej więcej co kilka sekund. Pozwala to na dokładne obliczenie Hashrate każdego Miner i dystrybucję nagród zgodnie z wybraną metodą obliczania rekompensaty (PPS, PPLNS, TIDES...).


> w języku francuskim "udziały" można przetłumaczyć jako "część"