---
term: BIP21
---

Propuesta escrita por Nils Schneider y Matt Corallo, basada en BIP20 escrita por Luke Dashjr, que a su vez provino de otro documento escrito por Nils Schneider. BIP21 define cómo se deben codificar las direcciones de recepción en URIs (*Uniform Resource Identifier*) para facilitar los pagos. Por ejemplo, un URI de Bitcoin siguiendo BIP21 en el cual yo solicitaría bajo la etiqueta “*Pandul*” que me envíen 0.1 BTC se vería así:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

Esta estandarización mejora la experiencia del usuario en las transacciones de Bitcoin al permitir hacer clic en un enlace o escanear un código QR para iniciar sus parámetros. El estándar BIP21 ahora es ampliamente adoptado en el software de billeteras Bitcoin.