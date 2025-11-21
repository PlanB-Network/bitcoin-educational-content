---
term: HTLC
---

Significa "*Hashed Timelock Contract*". Se trata de un mecanismo Smart contract utilizado principalmente en Lightning. También se encuentra a veces en los swaps atómicos. Básicamente, HTLC condiciona una transferencia de dinero a la revelación de un secreto, y también incluye una condición temporal para proteger el dinero del remitente en caso de transacción fallida.


En Lightning, HTLC permite enviar bitcoins a un nodo con el que no se tiene un canal directo, pasando por varios canales, sin necesidad de confianza por el camino. El pago entre cada nodo está condicionado a la provisión de una pre-imagen (el secreto que, una vez hasheado, corresponde a un valor acordado). Si el destinatario final proporciona esta imagen previa, puede reclamar los fondos, y necesariamente permite a cada nodo intermedio reclamar los fondos en cascada.


Por ejemplo, si Alicia quiere enviar 1 BTC a David, pero no tiene un canal directo con él, tiene que pasar por Bob y Carol, que tienen canales de pago entre sí. Así es como funciona la transacción:




- David entrega a Alice un Invoice Lightning. Éste contiene el Hash $h$ de un secreto $s$ (la pre-imagen) que sólo David conoce. Así que tenemos: $h = \text{Hash}(s)$ ;
- Alice crea una HTLC con Bob, que se ofrece a enviarle 1 BTC a condición de que Bob le proporcione un secreto $s$ (la imagen previa) que corresponde a la Hash $h$ ;
- Bob crea un HTLC con Carol, que le ofrece enviarle 1 BTC a condición de que ella le proporcione el mismo secreto $s$ ;
- Carol crea un HTLC con David, que le ofrece otro 1 BTC si revela la preimagen $s$;
- David revela $s$ (que sólo él conocía) a Carol para recibir 1 BTC. Carol puede ahora utilizar $s$ para obtener el BTC de Bob. Y Bob, que ahora conoce $s$, hace lo mismo con Alice.


Por último, Alice envió 1 BTC a David a través de Bob y Carol (una acción neutral para esta última), sin que nadie tuviera que confiar en los demás, ya que todo está asegurado en cascada por las condiciones de las HTLC.


Las HTLC permiten así los denominados intercambios "atómicos": o bien la transferencia se realiza con total éxito, o bien fracasa, y los fondos se devuelven. Esto garantiza la seguridad de las transacciones, incluso entre múltiples participantes sin necesidad de confianza.