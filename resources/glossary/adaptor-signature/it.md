---
term: FIRMA DELL'ADATTATORE

---
Metodo crittografico che consente di combinare una firma autentica con una firma aggiuntiva (chiamata "firma adattatore") per rivelare un dato segreto. Questo metodo funziona in modo tale che, conoscendo due elementi tra la firma valida, la firma adattatore e il segreto, è possibile dedurre il terzo elemento mancante. Una delle proprietà interessanti di questo metodo è che se conosciamo la firma dell'adattatore della nostra controparte e il punto specifico della curva ellittica collegato al segreto usato per calcolare questa firma dell'adattatore, possiamo ricavare la nostra firma dell'adattatore che corrisponderà allo stesso segreto, senza avere accesso diretto al segreto stesso. In uno scambio tra due parti interessate che non si fidano l'una dell'altra, questa tecnica consente di svelare simultaneamente due informazioni sensibili tra i partecipanti. Questo processo elimina la necessità di fiducia nelle transazioni istantanee come un Coin Swap o un Atomic Swap. Facciamo un esempio per capire meglio. Alice e Bob vogliono inviarsi 1 BTC, ma non si fidano l'uno dell'altro. Utilizzeranno quindi le firme adattatore per annullare la necessità di fiducia nell'altra parte in questo scambio (rendendolo così uno scambio "atomico"). Procedono come segue:


- Alice avvia questo scambio atomico. Crea una transazione $m_A$ che invia 1 BTC a Bob. Crea una firma $s_A$ che convalida questa transazione usando la sua chiave privata $p_A$ ($P_A = p_A \cdot G$) e usando un nonce $n_A$ e un segreto $t$ ($N_A = n_A \cdot G$ e $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \parallelo P_A \parallelo m_A) \cdot p_A$$

&nbsp;


- Alice calcola la firma dell'adattatore $s_A'$ a partire dal segreto $t$ e dalla sua firma reale $s_A$:

$$s_A' = s_A - t$$$

&nbsp;


- Alice invia a Bob il suo adattatore di firma $s_A'$, la sua transazione non firmata $m_A$, il punto corrispondente al segreto $T$ e il punto corrispondente al nonce $N_A$. Queste informazioni sono chiamate "adattatore". Si noti che con queste sole informazioni Bob non è in grado di recuperare il BTC di Alice.
- Tuttavia, Bob può verificare che Alice non lo stia ingannando. Per farlo, controlla che la firma dell'adattatore di Alice $s_A'$ corrisponda alla transazione promessa $m_A$. Se la seguente equazione è corretta, Bob è convinto che la firma dell'adattatore di Alice sia valida:

$$s_A' \cdot G = N_A + H(N_A + T \parallelo P_A \parallelo m_A) \cdot P_A$$

&nbsp;


- Questa verifica fornisce a Bob le garanzie di Alice, in modo che possa continuare il processo di scambio atomico in tutta tranquillità. Creerà quindi la propria transazione $m_B$ inviando 1 BTC ad Alice e la propria firma adattatore $s_B'$, che sarà collegata con lo stesso segreto $t$ che solo Alice conosce per ora (Bob non conosce questo valore $t$, ma solo il suo punto corrispondente $T$ che Alice gli ha fornito): $$s_B' = n_B + H(N_B + T \parallelo P_B \parallelo m_B) \cdot p_B$$

&nbsp;


- Bob invia ad Alice la sua firma adattatore $s_B'$, la sua transazione non firmata $m_B$, il punto corrispondente al segreto $T$ e il punto corrispondente al nonce $N_B$. Alice può ora combinare la firma dell'adattatore di Bob $s_B'$ con il segreto $t$, che solo lei conosce, per calcolare una firma valida $s_B$ per la transazione $m_B$ che le invia il BTC di Bob:

$$s_B = s_B' + t$$$

&nbsp;

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallelo P_B \parallelo m_B) \cdot P_B$$

&nbsp;


- Alice trasmette questa transazione firmata $m_B$ sulla blockchain Bitcoin per recuperare i BTC che Bob le ha promesso. Bob viene a conoscenza di questa transazione sulla blockchain. È quindi in grado di estrarre la firma $s_B = s_B' + t$. Da questa informazione, Bob può isolare il famoso segreto $t$ di cui aveva bisogno:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$

&nbsp;


- Tuttavia, questo segreto $t$ era l'unica informazione mancante a Bob per produrre la firma valida $s_A$, a partire dalla firma adattatore $s_A'$ di Alice, che gli permetterà di convalidare la transazione $m_A$ che invia un BTC da Alice a Bob. Egli calcola quindi $s_A$ e trasmette a sua volta la transazione $m_A$: $$s_A = s_A' + t$$

&nbsp;

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallela P_A \parallela m_A) \cdot P_A$$