---
term: BIP61

---
Se introduce un mensaje de rechazo en el protocolo de comunicación entre nodos. El objetivo de BIP61 es añadir un mecanismo de retroalimentación cuando un nodo recibe una transacción o un bloque de otro nodo que considera inválido. Este mensaje de rechazo permitiría a un nodo señalar al remitente la razón por la que ha sido rechazado. Con este tipo de comunicación se pretendía mejorar la interoperabilidad entre distintos clientes y las comunicaciones entre nodos completos y clientes SPV. Las funcionalidades aportadas por BIP61 fueron finalmente abandonadas a partir de la versión 0.20.0 de Bitcoin Core, ya que se consideraron innecesarias al implicar mayores necesidades de ancho de banda.