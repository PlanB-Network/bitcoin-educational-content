---
term: Invoice LUZ
---

Solicitud de pago relámpago generada por el destinatario, que contiene toda la información necesaria para completar la transacción.


Un Invoice Lightning contiene el destino del pago en forma de clave pública del nodo receptor, pero también un prefijo `LN`, el importe, un tiempo hasta el vencimiento, el Hash del secreto utilizado en las HTLC y otros metadatos, algunos de los cuales son opcionales, como las opciones de enrutamiento. Estas facturas están definidas por la norma BOLT11. Una vez pagada, una Invoice Lightning no puede reutilizarse.


> ► *En francés, podríamos traducir "Invoice" por "facture", pero generalmente utilizamos el término inglés incluso en francés.*