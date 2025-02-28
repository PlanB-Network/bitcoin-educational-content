---
term: P2SH

---
P2SH son las siglas de *Pay to Script Hash*. Se trata de un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO. A diferencia de los scripts P2PK y P2PKH, en los que las condiciones de gasto están predefinidas, P2SH permite la integración de condiciones de gasto arbitrarias y funcionalidades adicionales dentro de un script de transacción.

Técnicamente, en una transacción P2SH, la `scriptPubKey` contiene el hash criptográfico de un `redeemScript`, en lugar de condiciones de gasto explícitas. Este hash se obtiene utilizando un hash `SHA256`. Cuando se envían bitcoins a una dirección P2SH, el `redeemScript` subyacente no se revela. Sólo se incluye su hash en la transacción. Las direcciones P2SH están codificadas en `Base58Check` y comienzan con el número `3`. Cuando el destinatario desea gastar los bitcoins recibidos, debe proporcionar un `redeemScript` que coincida con el hash presente en el `scriptPubKey`, junto con los datos necesarios para satisfacer las condiciones de este `redeemScript`. Por ejemplo, en un script P2SH multifirma, el script podría requerir firmas de múltiples claves privadas.

El uso de P2SH ofrece más flexibilidad, ya que permite construir guiones arbitrarios sin que el remitente conozca los detalles. P2SH se introdujo en 2012 con BIP16.