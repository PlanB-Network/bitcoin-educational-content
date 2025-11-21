---
term: OFERTA
---

En BOLT12, las *ofertas* son códigos QR estáticos para realizar múltiples pagos en Lightning Network. A diferencia de las facturas convencionales, las *ofertas* pueden reutilizarse. Pueden utilizarse para generate múltiples solicitudes de Invoice. Cuando un usuario escanea un código QR que contiene una *oferta*, envía un mensaje solicitando una nueva Invoice al nodo Lightning asociado. El nodo responde con una Invoice que el pagador puede utilizar. Las *ofertas* proporcionan así un identificador único para recibir múltiples pagos de diferentes usuarios en Lightning.