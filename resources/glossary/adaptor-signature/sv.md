---
term: Adaptor signature
definition: En kryptografisk teknik som binder en signatur till en hemlighet, så att publicering av signaturen avslöjar hemligheten. Användbar för atomära byten utan en pålitlig mellanhand.
---

Kryptografisk metod som gör det möjligt att kombinera en äkta signatur med en ytterligare signatur (en s.k. "adaptorsignatur") för att avslöja en hemlig uppgift. Metoden fungerar på så sätt att om man känner till två Elements bland den giltiga signaturen, adaptersignaturen och hemligheten kan man härleda det saknade tredje elementet. En av de intressanta egenskaperna hos denna metod är att om vi känner till vår motparts adaptorsignatur och den specifika punkt på den elliptiska kurvan som är kopplad till den hemlighet som används för att beräkna denna adaptorsignatur, kan vi sedan härleda vår egen adaptorsignatur som kommer att matcha med samma hemlighet, utan att någonsin ha direkt tillgång till själva hemligheten. I en Exchange mellan två intressenter som inte litar på varandra gör den här tekniken det möjligt att samtidigt avslöja två känsliga informationsbitar mellan deltagarna. Denna process eliminerar behovet av förtroende i omedelbara transaktioner som ett Coin Swap eller ett Atomic Swap. Låt oss ta ett exempel för att förstå det bättre. Alice och Bob vill skicka 1 BTC till varandra, men de litar inte på varandra. De kommer därför att använda adaptersignaturer för att upphäva behovet av förtroende för den andra parten i denna Exchange (vilket gör den till en "atomisk" Exchange). De går tillväga på följande sätt:


- Alice initierar denna atomära Exchange. Hon skapar en transaktion $m_A$ som skickar 1 BTC till Bob. Hon skapar en signatur $s_A$ som validerar denna transaktion med hjälp av hennes privata nyckel $p_A$ ($P_A = p_A \cdot G$), och med hjälp av en Nonce $n_A$ och en hemlighet $t$ ($N_A = n_A \cdot G$ och $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \parallell P_A \parallell m_A) \cdot p_A$$$



- Alice beräknar adapterns signatur $s_A'$ utifrån hemligheten $t$ och hennes verkliga signatur $s_A$:

$$s_A' = s_A - t$$$



- Alice skickar till Bob sin adaptorsignatur $s_A'$, sin osignerade transaktion $m_A$, den punkt som motsvarar hemligheten $T$ och den punkt som motsvarar Nonce $N_A$. Vi kallar dessa informationsbitar för en "adapter". Observera att med bara denna information kan Bob inte återfå Alice:s BTC.
- Bob kan dock verifiera att Alice inte lurar honom. För att göra detta kontrollerar han att Alice:s adaptersignatur $s_A'$ matchar den utlovade transaktionen $m_A$. Om följande ekvation är korrekt är han övertygad om att Alice:s adaptersignatur är giltig:

$$s_A' \cdot G = N_A + H(N_A + T \parallell P_A \parallell m_A) \cdot P_A$$$



- Denna verifiering ger Bob försäkringar från Alice, så att han kan fortsätta atombytesprocessen med sinnesfrid. Han kommer sedan att skapa sin egen transaktion $m_B$ som skickar 1 BTC till Alice och sin egen adaptersignatur $s_B'$, som kommer att länkas med samma hemlighet $t$ som endast Alice känner till för tillfället (Bob känner inte till detta värde $t$, utan endast dess motsvarande punkt $T$ som Alice har gett honom): $$s_B' = n_B + H(N_B + T \parallell P_B \parallell m_B) \cdot p_B$$$



- Bob skickar till Alice sin adaptersignatur $s_B'$, sin osignerade transaktion $m_B$, den punkt som motsvarar hemligheten $T$ och den punkt som motsvarar Nonce $N_B$. Alice kan nu kombinera Bob:s adaptersignatur $s_B'$ med hemligheten $t$, som endast hon känner till, för att beräkna en giltig signatur $s_B$ för transaktionen $m_B$ som skickar Bob:s BTC till henne:

$$s_B = s_B' + t$$$


$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallell P_B \parallell m_B) \cdot P_B$$$



- Alice sänder denna signerade transaktion $m_B$ på Bitcoin Blockchain för att återfå BTC som Bob lovade henne. Bob får kännedom om denna transaktion på Blockchain. Han kan därmed extrahera signaturen $s_B = s_B' + t$. Från denna information kan Bob isolera den berömda hemligheten $t$ som han behövde:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$$



- Denna hemliga $t$ var dock den enda information som saknades för att Bob skulle kunna producera den giltiga signaturen $s_A$, från Alice:s adaptersignatur $s_A'$, som gör det möjligt för honom att validera transaktionen $m_A$ som skickar en BTC från Alice till Bob. Han beräknar sedan $s_A$ och sänder transaktionen $m_A$ i tur och ordning: $$s_A = s_A' + t$$$$


$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallell P_A \parallell m_A) \cdot P_A$$$