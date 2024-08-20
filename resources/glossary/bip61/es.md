---
term: BIP61
---

Introdujo un mensaje de rechazo en el protocolo de comunicación entre nodos. El objetivo de BIP61 es agregar un mecanismo de retroalimentación cuando un nodo recibe una transacción o un bloque de otro nodo que considera inválido. Este mensaje de rechazo permitiría a un nodo señalar al emisor la razón por la cual fue rechazado. Este tipo de comunicación tenía la intención de mejorar la interoperabilidad entre diferentes clientes y las comunicaciones entre nodos completos y clientes SPV. Las funcionalidades aportadas por BIP61 fueron eventualmente abandonadas a partir de la versión 0.20.0 de Bitcoin Core, ya que se consideraron innecesarias mientras implicaban un aumento en las necesidades de ancho de banda.