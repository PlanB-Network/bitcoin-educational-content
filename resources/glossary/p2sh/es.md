---
term: P2SH
---

P2SH significa *Pay to Script Hash* (Pago a Hash de Script). Es un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO. A diferencia de los scripts P2PK y P2PKH, donde las condiciones de gasto están predefinidas, P2SH permite la integración de condiciones de gasto arbitrarias y funcionalidades adicionales dentro de un script de transacción.

Técnicamente, en una transacción P2SH, el `scriptPubKey` contiene el hash criptográfico de un `redeemScript`, en lugar de condiciones de gasto explícitas. Este hash se obtiene utilizando un hash `SHA256`. Al enviar bitcoins a una dirección P2SH, el `redeemScript` subyacente no se revela. Solo su hash se incluye en la transacción. Las direcciones P2SH están codificadas en `Base58Check` y comienzan con el número `3`. Cuando el destinatario desea gastar los bitcoins recibidos, debe proporcionar un `redeemScript` que coincida con el hash presente en el `scriptPubKey`, junto con los datos necesarios para satisfacer las condiciones de este `redeemScript`. Por ejemplo, en un script multisignatura P2SH, el script podría requerir firmas de múltiples claves privadas.

El uso de P2SH ofrece más flexibilidad, ya que permite la construcción de scripts arbitrarios sin que el remitente conozca los detalles. P2SH fue introducido en 2012 con el BIP16.