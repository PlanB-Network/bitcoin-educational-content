---
term: ADAPTER SIGNATUR

---
Kryptografisk metode som gjør det mulig å kombinere en ekte signatur med en tilleggssignatur (kalt en "adaptorsignatur") for å avsløre en hemmelig del av dataene. Denne metoden fungerer slik at hvis man kjenner til to elementer blant den gyldige signaturen, tilpasningssignaturen og hemmeligheten, kan man utlede det tredje elementet som mangler. En av de interessante egenskapene ved denne metoden er at hvis vi kjenner motpartens adaptorsignatur og det spesifikke punktet på den elliptiske kurven som er knyttet til hemmeligheten som ble brukt til å beregne adaptorsignaturen, kan vi utlede vår egen adaptorsignatur som passer med den samme hemmeligheten, uten å ha direkte tilgang til selve hemmeligheten. I en utveksling mellom to interessenter som ikke stoler på hverandre, gjør denne teknikken det mulig å avsløre to sensitive opplysninger mellom deltakerne samtidig. Denne prosessen eliminerer behovet for tillit i øyeblikkelige transaksjoner som Coin Swap eller Atomic Swap. La oss ta et eksempel for å forstå det bedre. Alice og Bob ønsker å sende 1 BTC til hverandre, men de stoler ikke på hverandre. De vil derfor bruke adaptorsignaturer for å oppheve behovet for tillit til den andre parten i denne utvekslingen (og dermed gjøre det til en "atomisk" utveksling). De går frem på følgende måte:


- Alice initierer denne atomutvekslingen. Hun oppretter en transaksjon $m_A$ som sender 1 BTC til Bob. Hun oppretter en signatur $s_A$ som validerer denne transaksjonen ved hjelp av sin private nøkkel $p_A$ ($P_A = p_A \cdot G$), og ved hjelp av en nonce $n_A$ og en hemmelighet $t$ ($N_A = n_A \cdot G$ og $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \parallell P_A \parallell m_A) \cdot p_A$$$

&nbsp;


- Alice beregner adapter-signaturen $s_A'$ ut fra den hemmelige $t$ og sin virkelige signatur $s_A$:

$$s_A' = s_A - t$$$$

&nbsp;


- Alice sender Bob sin adaptorsignatur $s_A'$, sin usignerte transaksjon $m_A$, punktet som tilsvarer hemmeligheten $T$, og punktet som tilsvarer nonce $N_A$. Vi kaller disse informasjonsbitene for en "adaptor". Merk at Bob ikke kan gjenopprette Alices BTC med bare denne informasjonen.
- Bob kan imidlertid verifisere at Alice ikke lurer ham. For å gjøre dette kontrollerer han at Alices adapter-signatur $s_A'$ samsvarer med den lovede transaksjonen $m_A$. Hvis følgende ligning stemmer, er han overbevist om at Alices adaptorsignatur er gyldig:

$$s_A' \cdot G = N_A + H(N_A + T \parallell P_A \parallell m_A) \cdot P_A$$$

&nbsp;


- Denne verifiseringen gir Bob forsikringer fra Alice, slik at han kan fortsette atombytteprosessen med ro i sinnet. Han vil deretter opprette sin egen transaksjon $m_B$ som sender 1 BTC til Alice og sin egen adapter-signatur $s_B'$, som vil være knyttet til den samme hemmeligheten $t$ som bare Alice kjenner til for øyeblikket (Bob kjenner ikke denne verdien $t$, men bare det tilsvarende punktet $T$ som Alice har gitt ham): $$s_B' = n_B + H(N_B + T \parallell P_B \parallell m_B) \cdot p_B$$$

&nbsp;


- Bob sender sin adapter-signatur $s_B'$, sin usignerte transaksjon $m_B$, punktet som tilsvarer hemmeligheten $T$, og punktet som tilsvarer nonce $N_B$, til Alice. Alice kan nå kombinere Bobs adaptorsignatur $s_B'$ med hemmeligheten $t$, som bare hun kjenner til, for å beregne en gyldig signatur $s_B$ for transaksjonen $m_B$ som sender henne Bobs BTC:

$$s_B = s_B' + t$$$$

&nbsp;

$$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallell P_B \parallell m_B) \cdot P_B$$$

&nbsp;


- Alice sender denne signerte transaksjonen $m_B$ på Bitcoin-blokkjeden for å få tilbake BTC som Bob lovet henne. Bob får vite om denne transaksjonen på blokkjeden. Han er dermed i stand til å trekke ut signaturen $s_B = s_B' + t$. Ut fra denne informasjonen kan Bob isolere den berømte hemmeligheten $t$ han trengte:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$$$

&nbsp;


- Denne hemmeligheten $t$ var imidlertid den eneste informasjonen som manglet for at Bob skulle kunne produsere den gyldige signaturen $s_A$, fra Alices adapter-signatur $s_A'$, som vil gjøre det mulig for ham å validere transaksjonen $m_A$ som sender en BTC fra Alice til Bob. Deretter beregner han $s_A$ og sender transaksjonen $m_A$ i tur og orden: $$s_A = s_A' + t$$$$

&nbsp;

$$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallell P_A \parallell m_A) \cdot P_A$$$