---
term: RGB
---

Sistema Smart contract descentralizado e confidencial concebido para funcionar com o Bitcoin e o Lightning Network. O RGB funciona num modelo Client-side Validation e separa o armazenamento do Contract State do Blockchain, de modo a que apenas os compromissos criptográficos sejam mantidos nele. Desta forma, o histórico completo do estado é mantido fora da cadeia, permitindo maior escalabilidade e confidencialidade. O RGB permite assim a criação de contratos complexos para armazenar tokens, NFTs, identidades descentralizadas ou soluções DeFi, diretamente sobre o Bitcoin.


No RGB, a resistência ao Double-spending é garantida pela utilização do Single-Use Seal, um mecanismo criptográfico que tira partido do facto de os UTXOs no Bitcoin só poderem ser utilizados uma vez. Quanto à autenticidade do token, esta é garantida pela verificação do lado do cliente do histórico do estado, desde a criação do Contract até ao seu estado mais recente.