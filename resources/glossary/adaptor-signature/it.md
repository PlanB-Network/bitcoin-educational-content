---
termine: ADAPTOR SIGNATURE
---

Metodo crittografico che consente di combinare una firma autentica con una firma aggiuntiva (denominata "adaptor signature") per rivelare un pezzo di dati segreto. Questo metodo funziona in modo tale che conoscere due elementi tra la firma valida, la firma adattatore e il segreto permette di dedurre il terzo elemento mancante. Una delle proprietà interessanti di questo metodo è che, se conosciamo la firma adattatore della nostra controparte e il punto specifico sulla curva ellittica collegato al segreto usato per calcolare questa firma adattatore, possiamo quindi derivare la nostra propria firma adattatore che corrisponderà allo stesso segreto, senza mai avere accesso diretto al segreto stesso. In uno scambio tra due parti che non si fidano l'una dell'altra, questa tecnica consente la rivelazione simultanea di due pezzi di informazioni sensibili tra i partecipanti. Questo processo elimina la necessità di fiducia in transazioni istantanee come uno scambio di monete (Coin Swap) o uno scambio atomico (Atomic Swap). Prendiamo un esempio per capirlo meglio. Alice e Bob vogliono inviarsi reciprocamente 1 BTC, ma non si fidano l'uno dell'altro. Useranno quindi le firme adattatore per negare la necessità di fidarsi dell'altra parte in questo scambio (rendendolo così uno scambio "atomico"). Procedono come segue:
* Alice inizia questo scambio atomico. Crea una transazione $m_A$ che invia 1 BTC a Bob. Crea una firma $s_A$ che valida questa transazione usando la sua chiave privata $p_A$ ($P_A = p_A \cdot G$), e usando un nonce $n_A$ e un segreto $t$ ($N_A = n_A \cdot G$ e $T = t \cdot G$): 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice calcola la firma adattatore $s_A'$ dal segreto $t$ e dalla sua vera firma $s_A$:  
$$s_A' = s_A - t$$
&nbsp;
* Alice invia a Bob la sua firma adattatore $s_A'$, la sua transazione non firmata $m_A$, il punto corrispondente al segreto $T$, e il punto corrispondente al nonce $N_A$. Chiamiamo queste informazioni un "adattatore". Nota che con solo queste informazioni, Bob non è in grado di recuperare i BTC di Alice.
* Tuttavia, Bob può verificare che Alice non lo stia ingannando. Per fare ciò, controlla che la firma adattatore di Alice $s_A'$ corrisponda alla transazione promessa $m_A$. Se la seguente equazione è corretta, allora è convinto che la firma adattatore di Alice sia valida: 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Questa verifica fornisce a Bob delle rassicurazioni da parte di Alice, così che possa continuare il processo di scambio atomico con tranquillità. Creerà quindi la sua propria transazione $m_B$ inviando 1 BTC ad Alice e la sua propria firma adattatore $s_B'$, che sarà collegata con lo stesso segreto $t$ che solo Alice conosce per ora (Bob non conosce questo valore $t$, ma solo il suo punto corrispondente $T$ che Alice gli ha fornito): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob invia ad Alice la sua firma adattatore $s_B'$, la sua transazione non firmata $m_B$, il punto corrispondente al segreto $T$ e il punto corrispondente al nonce $N_B$. Alice può ora combinare la firma adattatore di Bob $s_B'$ con il segreto $t$, che solo lei conosce, per calcolare una firma valida $s_B$ per la transazione $m_B$ che le invia i BTC di Bob: $$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice trasmette questa transazione firmata $m_B$ sulla blockchain di Bitcoin per recuperare i BTC che Bob le aveva promesso. Bob apprende di questa transazione sulla blockchain. Così facendo, è in grado di estrarre la firma $s_B = s_B' + t$. Da queste informazioni, Bob può isolare il famoso segreto $t$ di cui aveva bisogno:
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Tuttavia, questo segreto $t$ era l'unica informazione mancante affinché Bob potesse produrre la firma valida $s_A$, a partire dalla firma adattatore di Alice $s_A'$, che gli permetterà di convalidare la transazione $m_A$ che invia un BTC da Alice a Bob. Calcola quindi $s_A$ e trasmette a sua volta la transazione $m_A$: $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$