---
term: HANDTEKENING ADAPTER
---

Cryptografische methode die het mogelijk maakt om een echte handtekening te combineren met een extra handtekening (een "adaptor handtekening" genoemd) om een geheim stuk data te onthullen. Deze methode werkt op zo'n manier dat als we twee Elements van de geldige handtekening, de aangepaste handtekening en het geheim kennen, we het ontbrekende derde element kunnen afleiden. Een van de interessante eigenschappen van deze methode is dat als we de adaptorhandtekening van onze tegenhanger kennen en het specifieke punt op de elliptische curve dat gekoppeld is aan het geheim dat gebruikt is om deze adaptorhandtekening te berekenen, we vervolgens onze eigen adaptorhandtekening kunnen afleiden die overeenkomt met hetzelfde geheim, zonder ooit directe toegang te hebben tot het geheim zelf. In een Exchange tussen twee belanghebbenden die elkaar niet vertrouwen, maakt deze techniek de gelijktijdige onthulling van twee gevoelige stukjes informatie tussen de deelnemers mogelijk. Dit proces elimineert de noodzaak voor vertrouwen in ogenblikkelijke transacties zoals een Coin Swap of een Atomic Swap. Laten we een voorbeeld nemen om het beter te begrijpen. Alice en Bob willen elkaar 1 BTC sturen, maar ze vertrouwen elkaar niet. Ze zullen daarom adaptorhandtekeningen gebruiken om de noodzaak voor vertrouwen in de andere partij in deze Exchange te negeren (waardoor het een "atomaire" Exchange wordt). Ze gaan als volgt te werk:


- Alice initieert deze atomaire Exchange. Ze creëert een transactie $m_A$ die 1 BTC naar Bob stuurt. Ze creëert een handtekening $s_A$ die deze transactie valideert met behulp van haar private sleutel $p_A$ ($P_A = p_A \cdot G$), en met behulp van een Nonce $n_A$ en een geheim $t$ ($N_A = n_A \cdot G$ en $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$



- Alice berekent de adaptorhandtekening $s_A'$ uit het geheim $t$ en haar echte handtekening $s_A$:

$$s_A' = s_A - t$$



- Alice stuurt naar Bob haar adaptorhandtekening $s_A'$, haar niet-ondertekende transactie $m_A$, het punt dat overeenkomt met het geheim $T$, en het punt dat overeenkomt met de Nonce $N_A$. We noemen deze stukjes informatie een "adaptor". Merk op dat met alleen deze informatie, Bob niet in staat is om Alice's BTC terug te krijgen.
- Bob kan echter controleren of Alice hem niet misleidt. Hiervoor controleert hij of Alice's adaptorhandtekening $s_A'$ overeenkomt met de beloofde transactie $m_A$. Als de volgende vergelijking klopt, dan is hij ervan overtuigd dat de adaptorhandtekening van Alice geldig is:

$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$



- Deze verificatie geeft Bob garanties van Alice, zodat hij met een gerust hart verder kan gaan met het atomaire swap-proces. Hij maakt dan zijn eigen transactie $m_B$ aan, waarbij hij 1 BTC naar Alice stuurt en zijn eigen adaptorhandtekening $s_B'$, die wordt gekoppeld aan hetzelfde geheim $t$ dat voorlopig alleen Alice kent (Bob kent deze waarde $t$ niet, maar alleen het bijbehorende punt $T$ dat Alice hem heeft verstrekt): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$



- Bob stuurt naar Alice zijn adaptorhandtekening $s_B'$, zijn niet-ondertekende transactie $m_B$, het punt dat overeenkomt met het geheim $T$ en het punt dat overeenkomt met de Nonce $N_B$. Alice kan nu Bob's adaptorhandtekening $s_B'$ combineren met het geheim $t$, dat alleen zij kent, om een geldige handtekening $s_B$ te berekenen voor de transactie $m_B$ die haar Bob's BTC stuurt:

$$s_B = s_B' + t$$


$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$



- Alice zendt deze ondertekende transactie $m_B$ uit op Bitcoin Blockchain om de BTC terug te krijgen die Bob haar beloofd heeft. Bob verneemt van deze transactie op de Blockchain. Hij is dus in staat om de handtekening $s_B = s_B' + t$ te extraheren. Uit deze informatie kan Bob het beroemde geheim $t$ isoleren dat hij nodig had:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$



- Deze geheime $t$ was echter de enige ontbrekende informatie voor Bob om de geldige handtekening $s_A$ te produceren, uit Alice's adaptorhandtekening $s_A'$, waarmee hij de transactie $m_A$ kan valideren waarbij een BTC van Alice naar Bob wordt gestuurd. Hij berekent dan $s_A$ en zendt de transactie $m_A$ op zijn beurt uit: $$s_A = s_A' + t$$


$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$