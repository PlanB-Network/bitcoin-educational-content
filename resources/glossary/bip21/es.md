---
term: BIP21

---
Propuesta escrita por Nils Schneider y Matt Corallo, basada en el BIP20 escrito por Luke Dashjr, que a su vez procede de otro documento escrito por Nils Schneider. BIP21 define cómo las direcciones de recepción deben ser codificadas en URIs (*Uniform Resource Identifier*) para facilitar los pagos. Por ejemplo, un URI Bitcoin siguiendo BIP21 en el que yo solicitaría bajo la etiqueta "*Pandul*" que me enviara 0.1 BTC tendría este aspecto:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

Esta estandarización mejora la experiencia de usuario de las transacciones Bitcoin al permitir hacer clic en un enlace o escanear un código QR para iniciar sus parámetros. El estándar BIP21 está ahora ampliamente adoptado en el software de monederos Bitcoin.