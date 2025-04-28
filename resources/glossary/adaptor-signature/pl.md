---
term: SYGNATURA ADAPTERA
---

Metoda kryptograficzna, która umożliwia połączenie prawdziwego podpisu z dodatkowym podpisem (zwanym "podpisem adaptacyjnym") w celu ujawnienia tajnego fragmentu danych. Metoda ta działa w taki sposób, że znajomość dwóch Elements spośród prawidłowego podpisu, podpisu adaptacyjnego i sekretu pozwala wydedukować brakujący trzeci element. Jedną z interesujących właściwości tej metody jest to, że jeśli znamy podpis adaptacyjny naszego odpowiednika i konkretny punkt na krzywej eliptycznej powiązany z sekretem użytym do obliczenia tego podpisu adaptacyjnego, możemy następnie wyprowadzić własny podpis adaptacyjny, który będzie pasował do tego samego sekretu, bez bezpośredniego dostępu do samego sekretu. W Exchange między dwoma interesariuszami, którzy sobie nie ufają, technika ta pozwala na jednoczesne ujawnienie dwóch wrażliwych informacji między uczestnikami. Proces ten eliminuje potrzebę zaufania w transakcjach natychmiastowych, takich jak Coin Swap lub Atomic Swap. Weźmy przykład, aby lepiej to zrozumieć. Alice i Bob chcą wysłać sobie 1 BTC, ale nie ufają sobie nawzajem. Dlatego użyją podpisów adaptacyjnych, aby zanegować potrzebę zaufania do drugiej strony w tym Exchange (czyniąc go w ten sposób "atomowym" Exchange). Postępują w następujący sposób:


- Alice inicjuje ten atomowy Exchange. Tworzy transakcję $m_A$, która wysyła 1 BTC do Boba. Tworzy podpis $s_A$, który zatwierdza tę transakcję przy użyciu jej klucza prywatnego $p_A$ ($P_A = p_A \cdot G$) oraz przy użyciu Nonce $n_A$ i sekretu $t$ ($N_A = n_A \cdot G$ i $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$



- Alicja oblicza sygnaturę adaptera $s_A'$ na podstawie sekretu $t$ i swojej prawdziwej sygnatury $s_A$:

$$s_A' = s_A - t$$



- Alicja wysyła do Boba swój podpis adaptera $s_A'$, swoją niepodpisaną transakcję $m_A$, punkt odpowiadający sekretowi $T$ oraz punkt odpowiadający Nonce $N_A$. Nazywamy te informacje "adapterem". Zauważ, że mając tylko te informacje, Bob nie jest w stanie odzyskać BTC Alicji.
- Bob może jednak sprawdzić, czy Alicja go nie oszukuje. W tym celu sprawdza, czy podpis adaptera $s_A'$ Alicji jest zgodny z obiecaną transakcją $m_A$. Jeśli poniższe równanie jest poprawne, to jest przekonany, że podpis adaptera Alicji jest prawidłowy:

$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$



- Weryfikacja ta daje Bobowi zapewnienie od Alicji, dzięki czemu może on spokojnie kontynuować proces atomic swap. Następnie utworzy własną transakcję $m_B$ wysyłającą 1 BTC do Alicji i własną sygnaturę adaptera $s_B'$, która zostanie powiązana z tym samym sekretem $t$, który na razie zna tylko Alicja (Bob nie zna tej wartości $t$, a jedynie odpowiadający jej punkt $T$, który dostarczyła mu Alicja): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$



- Bob wysyła do Alicji swój podpis adaptacyjny $s_B'$, swoją niepodpisaną transakcję $m_B$, punkt odpowiadający sekretowi $T$ oraz punkt odpowiadający Nonce $N_B$. Alicja może teraz połączyć podpis adaptacyjny Boba $s_B'$ z sekretem $t$, który zna tylko ona, aby obliczyć prawidłowy podpis $s_B$ dla transakcji $m_B$, która wysyła jej BTC Boba:

$$s_B = s_B' + t$$


$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$



- Alicja transmituje tę podpisaną transakcję $m_B$ na Bitcoin Blockchain, aby odzyskać BTC, które obiecał jej Bob. Bob dowiaduje się o tej transakcji na Blockchain. W ten sposób jest w stanie wyodrębnić podpis $s_B = s_B' + t$. Na podstawie tych informacji Bob może wyodrębnić słynny sekret $t$, którego potrzebował:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$



- Tajemnica $t$ była jednak jedyną brakującą informacją dla Boba, aby stworzyć ważny podpis $s_A$, z podpisu adaptacyjnego $s_A'$ Alicji, który pozwoli mu zweryfikować transakcję $m_A$ wysyłającą BTC od Alicji do Boba. Następnie oblicza $s_A$ i transmituje transakcję $m_A$ po kolei: $$s_A = s_A' + t$$


$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$