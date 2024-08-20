---
termo: BIP21
---

Proposta escrita por Nils Schneider e Matt Corallo, baseada no BIP20 escrito por Luke Dashjr, que por sua vez veio de outro documento escrito por Nils Schneider. O BIP21 define como os endereços de recebimento devem ser codificados em URIs (*Uniform Resource Identifier*) para facilitar pagamentos. Por exemplo, um URI Bitcoin seguindo o BIP21 no qual eu solicitaria sob o rótulo “*Pandul*” para me enviar 0.1 BTC teria esta aparência:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

Esta padronização melhora a experiência do usuário em transações Bitcoin ao permitir clicar em um link ou escanear um código QR para iniciar seus parâmetros. O padrão BIP21 agora é amplamente adotado em softwares de carteira Bitcoin.