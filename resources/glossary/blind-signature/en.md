---
term: BLIND SIGNATURE
---

Chaum's blind signatures are a form of digital signature in which the signer does not know the content of the message being signed. However, the resulting signature can still be verified against the original message. This technique was developed by cryptographer David Chaum in 1983.

For example, consider a company that wants to have a confidential document, such as a contract, authenticated without revealing its contents. The company applies a cryptographic masking process that transforms the original document in a reversible way. This masked document is sent to a certification authority, which applies a blind signature without seeing the underlying content. After receiving the masked signed document, the company un-masks the signature. The result is an original document authenticated by the authority’s signature, without the authority ever knowing its contents.

Thus, Chaum's blind signatures allow documents to be authenticated without revealing their content, thus ensuring both data confidentiality and document integrity.

In Bitcoin, blind signature schemes are used in Chaumian bank overlays (Cashu, Fedimint, etc.), and especially in Chaumian coinjoin protocols, to ensure that the coordinator is not able to link an input to an output.
