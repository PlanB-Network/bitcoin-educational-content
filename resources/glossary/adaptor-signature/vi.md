---
term: ADAPTOR SIGNATURE

---
Cryptographic method that allows combining a genuine signature with an additional signature (called an "adaptor signature") to reveal a secret piece of data. This method works in such a way that knowing two elements among the valid signature, the adaptor signature, and the secret allows deducing the missing third element. One of the interesting properties of this method is that if we know our counterpart's adaptor signature and the specific point on the elliptical curve linked to the secret used to calculate this adaptor signature, we can then derive our own adaptor signature that will match with the same secret, without ever having direct access to the secret itself. In an exchange between two stakeholders who do not trust each other, this technique allows for the simultaneous unveiling of two sensitive pieces of information between the participants. This process eliminates the need for trust in instantaneous transactions such as a Coin Swap or an Atomic Swap. Let's take an example to understand it better. Alice and Bob want to send each other 1 BTC, but they do not trust each other. They will therefore use adaptor signatures to negate the need for trust in the other party in this exchange (thus making it an "atomic" exchange). They proceed as follows:


- Alice initiates this atomic exchange. She creates a transaction $m_A$ that sends 1 BTC to Bob. She creates a signature $s_A$ that validates this transaction using her private key $p_A$ ($P_A = p_A \cdot G$), and using a nonce $n_A$ and a secret $t$ ($N_A = n_A \cdot G$ and $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$

&nbsp;


- Alice calculates the adaptor signature $s_A'$ from the secret $t$ and her real signature $s_A$:

$$s_A' = s_A - t$$

&nbsp;


- Alice sends to Bob her adaptor signature $s_A'$, her unsigned transaction $m_A$, the point corresponding to the secret $T$, and the point corresponding to the nonce $N_A$. We call these pieces of information an "adaptor". Note that with just this information, Bob is not able to recover Alice's BTC.
- However, Bob can verify that Alice is not deceiving him. To do this, he checks that Alice's adaptor signature $s_A'$ matches the promised transaction $m_A$. If the following equation is correct, then he is convinced that Alice's adaptor signature is valid:

$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$

&nbsp;


- This verification provides Bob with assurances from Alice, so that he can continue the atomic swap process with peace of mind. He will then create his own transaction $m_B$ sending 1 BTC to Alice and his own adaptor signature $s_B'$, which will be linked with the same secret $t$ that only Alice knows for now (Bob does not know this value $t$, but only its corresponding point $T$ that Alice has provided him): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$

&nbsp;


- Bob sends to Alice his adaptor signature $s_B'$, his unsigned transaction $m_B$, the point corresponding to the secret $T$, and the point corresponding to the nonce $N_B$. Alice can now combine Bob's adaptor signature $s_B'$ with the secret $t$, which only she knows, to calculate a valid signature $s_B$ for the transaction $m_B$ that sends her Bob's BTC:

$$s_B = s_B' + t$$

&nbsp;

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$

&nbsp;


- Alice broadcasts this signed transaction $m_B$ on the Bitcoin blockchain to recover the BTC that Bob promised her. Bob learns of this transaction on the blockchain. He is thus able to extract the signature $s_B = s_B' + t$. From this information, Bob can isolate the famous secret $t$ he needed:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$

&nbsp;


- However, this secret $t$ was the only missing information for Bob to produce the valid signature $s_A$, from Alice's adaptor signature $s_A'$, which will allow him to validate the transaction $m_A$ sending a BTC from Alice to Bob. He then calculates $s_A$ and broadcasts the transaction $m_A$ in turn: $$s_A = s_A' + t$$

&nbsp;

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$