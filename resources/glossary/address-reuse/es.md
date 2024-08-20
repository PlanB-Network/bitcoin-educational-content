---
term: REUTILIZACIÓN DE DIRECCIONES
---

La reutilización de direcciones se refiere a la práctica de usar la misma dirección de recepción para bloquear múltiples UTXOs, a veces dentro de varias transacciones diferentes. Los bitcoins generalmente están bloqueados usando un par de claves criptográficas que corresponden a una dirección única. Dado que la blockchain es pública, es fácil ver qué direcciones están asociadas con cuántos bitcoins. En el caso de reutilizar la misma dirección para múltiples pagos, es razonable imaginar que todos los UTXOs asociados pertenecen a la misma entidad. Por lo tanto, la reutilización de direcciones plantea un problema para la privacidad del usuario. Permite enlaces determinísticos entre múltiples transacciones y UTXOs, así como la perpetuación del seguimiento de fondos en la cadena. Satoshi Nakamoto ya mencionó este problema en su Libro Blanco:

> "*Como un cortafuegos adicional, un nuevo par de claves podría ser utilizado para cada transacción para evitar que sean vinculadas a un propietario común.*" - Nakamoto, S. (2008). "Bitcoin: Un Sistema de Efectivo Electrónico Entre Pares". Consultado en https://bitcoin.org/bitcoin.pdf.

Para preservar la privacidad como mínimo, se recomienda encarecidamente usar cada dirección de recepción solo una vez. Para cada nuevo pago, es apropiado generar una nueva dirección. Para las salidas de cambio, también se debe usar una dirección fresca. Afortunadamente, gracias a las carteras deterministas y jerárquicas, se ha vuelto muy fácil usar una multitud de direcciones. Todos los pares de claves asociados con una cartera pueden ser fácilmente regenerados desde la semilla. Esta es también la razón por la cual el software de cartera siempre genera una nueva dirección diferente cuando haces clic en el botón de “Recibir”.

> ► *En inglés, se llama "Address Reuse".*