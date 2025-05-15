---
term: POTPIS ADAPTORA
---

Kriptografski metod koji omogućava kombinovanje originalnog potpisa sa dodatnim potpisom (nazvanim "adaptor potpis") kako bi se otkrio tajni deo podataka. Ovaj metod funkcioniše na takav način da poznavanje dva Elements među važećim potpisom, adaptor potpisom i tajnom omogućava izvođenje trećeg nedostajućeg elementa. Jedna od zanimljivih osobina ovog metoda je da ako znamo adaptor potpis našeg partnera i specifičnu tačku na eliptičnoj krivi povezanu sa tajnom korišćenom za izračunavanje ovog adaptor potpisa, možemo zatim izvesti sopstveni adaptor potpis koji će se poklapati sa istom tajnom, bez ikakvog direktnog pristupa samoj tajni. U Exchange između dva učesnika koji ne veruju jedan drugom, ova tehnika omogućava simultano otkrivanje dva osetljiva dela informacija između učesnika. Ovaj proces eliminiše potrebu za poverenjem u trenutnim transakcijama kao što su Coin Swap ili Atomic Swap. Uzmimo primer da bismo to bolje razumeli. Alisa i Bob žele da pošalju jedno drugom 1 BTC, ali ne veruju jedno drugom. Stoga će koristiti adaptor potpise kako bi negirali potrebu za poverenjem u drugu stranu u ovom Exchange (čime ga čine "atomskim" Exchange). Oni postupaju na sledeći način:


- Alice inicira ovaj atomski Exchange. Ona kreira transakciju $m_A$ koja šalje 1 BTC Bobu. Ona kreira potpis $s_A$ koji validira ovu transakciju koristeći njen privatni ključ $p_A$ ($P_A = p_A \cdot G$), i koristeći Nonce $n_A$ i tajnu $t$ ($N_A = n_A \cdot G$ i $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$



- Alisa izračunava potpis adaptera $s_A'$ iz tajne $t$ i njenog pravog potpisa $s_A$:

$$s_A' = s_A - t$$



- Alis šalje Bobu svoj adaptor potpis $s_A'$, svoju nepotpisanu transakciju $m_A$, tačku koja odgovara tajni $T$, i tačku koja odgovara Nonce $N_A$. Ove informacije nazivamo "adaptor". Napomena: sa samo ovim informacijama, Bob nije u mogućnosti da povrati Alisin BTC.
- Međutim, Bob može proveriti da ga Alice ne obmanjuje. Da bi to uradio, proverava da li se Alicein adaptor potpis $s_A'$ poklapa sa obećanom transakcijom $m_A$. Ako je sledeća jednačina tačna, onda je uveren da je Alicein adaptor potpis validan:

$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$



- Ova verifikacija pruža Bobu uverenja od Alice, kako bi mogao da nastavi proces atomskog zamene sa spokojem. On će zatim kreirati svoju sopstvenu transakciju $m_B$ šaljući 1 BTC Alice i svoj sopstveni adaptor potpis $s_B'$, koji će biti povezan sa istom tajnom $t$ koju za sada samo Alice zna (Bob ne zna ovu vrednost $t$, već samo njenu odgovarajuću tačku $T$ koju mu je Alice obezbedila): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$



- Bob šalje Alisi svoj adaptor potpis $s_B'$, svoju nepotpisanu transakciju $m_B$, tačku koja odgovara tajni $T$, i tačku koja odgovara Nonce $N_B$. Alisa sada može kombinovati Bobov adaptor potpis $s_B'$ sa tajnom $t$, koju samo ona zna, kako bi izračunala važeći potpis $s_B$ za transakciju $m_B$ koja joj šalje Bobov BTC:

$$s_B = s_B' + t$$


$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$



- Alisa emituje ovu potpisanu transakciju $m_B$ na Bitcoin Blockchain kako bi povratila BTC koji joj je Bob obećao. Bob saznaje za ovu transakciju na Blockchain. Tako je u mogućnosti da izdvoji potpis $s_B = s_B' + t$. Iz ovih informacija, Bob može izolovati čuvenu tajnu $t$ koja mu je bila potrebna:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$



- Međutim, ova tajna $t$ je bila jedina nedostajuća informacija koju je Bobu trebala da proizvede važeći potpis $s_A$, iz Alisinog adapter potpisa $s_A'$, što će mu omogućiti da validira transakciju $m_A$ slanjem BTC-a od Alise ka Bobu. On zatim izračunava $s_A$ i emituje transakciju $m_A$ zauzvrat: $$s_A = s_A' + t$$


$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$