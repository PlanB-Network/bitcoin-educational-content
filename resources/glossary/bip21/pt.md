---
term: BIP21

---
Proposta escrita por Nils Schneider e Matt Corallo, baseada no BIP20 escrito por Luke Dashjr, que por sua vez veio de outro documento escrito por Nils Schneider. O BIP21 define como os endereços de receção devem ser codificados em URIs (*Uniform Resource Identifier*) para facilitar os pagamentos. Por exemplo, um URI Bitcoin seguindo o BIP21 no qual eu pediria sob o rótulo "*Pandul*" para me enviar 0,1 BTC seria assim:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

Esta normalização melhora a experiência do utilizador nas transacções Bitcoin, permitindo clicar numa ligação ou digitalizar um código QR para iniciar os seus parâmetros. A norma BIP21 é agora amplamente adoptada no software das carteiras Bitcoin.