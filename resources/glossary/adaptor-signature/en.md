---
term: ADAPTOR SIGNATURE
---

Cryptographic method that allows combining a genuine signature with an additional signature (called an "adaptor signature") to reveal a secret piece of data. This method works so that knowing two elements among the valid signature, the adaptor signature, and the secret allows deducing the missing third element. One interesting property of this method is that if we know our peer's adaptor signature and the specific point on the elliptic curve related to the secret used to compute that adaptor signature, we can then derive our own adaptor signature that corresponds to the same secret, all without ever having direct access to the secret itself. In an exchange between two parties who do not trust each other, this technique allows for the simultaneous disclosure of two sensitive pieces of information between the participants. This process removes the need for trust in instant transactions such as a Coinswap or an Atomic Swap. Let's look at an example to better understand. Alice and Bob each want to send 1 BTC to the other, but they do not trust each other. They will therefore use adaptor signatures to eliminate the need to trust one another during the exchange (thus making it an "atomic" exchange). They proceed as follows:
*Alice initiates this atomic exchange. She creates a transaction $m_A$ that sends 1 BTC to Bob. She creates a signature $s_A$ to validates this transaction using her private key $p_A$ ($P_A = p_A \cdot G$), a nonce $n_A$, and a secret $t$ ($N_A = n_A \cdot G$ and $T = t \cdot G$):*
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$

**Alice calculates the adaptor signature $s_A'$ using the secret $t$ and her real signature $s_A$:**
$$s_A' = s_A - t$$

* Alice sends to Bob her adaptor signature $s_A'$, her unsigned transaction $m_A$, the point corresponding to the secret $T$, and the point corresponding to the nonce $N_A$. These pieces of information are referred to as an "adaptor". Note that with only this information, Bob cannot claim Alice’s BTC.
**However, Bob can verify that Alice is not deceiving him.** To do so, he checks whether Alice's adaptor signature $s_A'$ matches the promised transaction $m_A$. If the following equation is correct, then he can be confident that Alice's adaptor signature is valid:
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$

**This verification gives Bob some assurance from Alice, allowing him to safely proceed with the atomic swap process.** He then creates his own transaction $m_B$ sending 1 BTC to Alice and calculates his own adaptor signature $s_B'$, which is linked to the same secret $t$ (a value known only by Alice at this point, Bob only knows its corresponding point $T$, which Alice provided): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$

* Bob sends to Alice his adaptor signature $s_B'$, his unsigned transaction $m_B$, the point corresponding to the secret $T$, and the point corresponding to the nonce $N_B$. Alice can now combine Bob's adaptor signature $s_B'$ with the secret $t$, which only she knows, to compute a valid signature $s_B$ for the transaction $m_B$ that sends her Bob's BTC: 
$$s_B = s_B' + t$$

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$

*Alice then broadcasts the signed transaction $m_B$ to the Bitcoin blockchain in order to claim the BTC Bob promised. Once this transaction is published, Bob can observe it on the blockchain. He is thus able to extract the signature $s_B = s_B' + t$. From this information, Bob can isolate the famous secret $t$ he needed:*
$$t = (s_B' + t) - s_B' = s_B - s_B'$$

*This secret $t$ was the only missing information Bob needed to compute a valid signature $s_A$, from Alice's adaptor signature $s_A'$. With it, he can now validate transaction $m_A$ which sends 1 BTC from Alice to Bob. He then calculates $s_A$ and broadcasts the transaction $m_A$:* $$s_A = s_A' + t$$

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$