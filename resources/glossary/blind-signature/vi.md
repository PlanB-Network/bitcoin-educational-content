---
term: BLIND SIGNATURE

---
Chaum's blind signatures are a form of digital signature where the issuer of the signature does not know the content of the message they are signing. However, the signature can later be verified with the original message. This technique was developed by cryptographer David Chaum in 1983.

Consider the example of a company wanting to authenticate a confidential document, such as a contract, without revealing its content. The company applies a masking process that cryptographically transforms the original document in a reversible manner. This modified document is sent to a certification authority that applies a blind signature without knowing the underlying content. After receiving the masked signed document, the company un-masks the signature. The result is an original document authenticated by the authority's signature, without the authority ever having seen the original content.

Thus, Chaum's blind signatures allow for the certification of a document's authenticity without knowing its content, ensuring both the confidentiality of the user's data and the integrity of the signed document.

In Bitcoin, this protocol is used in systems of Chaumian banks as an overlay (Cashu, Fedimint, etc.), but especially in Chaumian coinjoin protocols, to ensure that the coordinator is not able to link an input to an output.