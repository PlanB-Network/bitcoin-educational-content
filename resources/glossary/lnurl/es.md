---
term: LNURL
---

Protocolo de comunicación que especifica un conjunto de funcionalidades diseñadas para simplificar las interacciones entre los nodos Lightning y los clientes, así como las aplicaciones de terceros. Este protocolo se basa en HTTP y permite crear enlaces para diversas operaciones, como una solicitud de pago, una solicitud de retirada de fondos u otras funcionalidades que mejoran la experiencia del usuario. Cada LNURL es una URL codificada en bech32 con el prefijo `lnurl` que, al ser escaneada, desencadena una serie de acciones automáticas en el Wallet Lightning.


Por ejemplo, LNURL-withdraw (LUD-03) te permite retirar fondos de un servicio escaneando un código QR, sin tener que generate a Invoice manualmente. O LNURL-auth (LUD-04) te permite conectarte a servicios en línea utilizando una clave privada en tu Wallet Lightning en lugar de una contraseña.