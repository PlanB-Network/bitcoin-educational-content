---
term: MACAROON
---

Un mecanismo de autenticación diseñado para asegurar el acceso a servicios en sistemas distribuidos. Los macaroons son notablemente utilizados en Lightning para autenticar usuarios cuando acceden a servicios delegados. Por ejemplo, con un nodo de Lightning, es posible generar un macaroon que autoriza la ejecución de transacciones desde tu smartphone a través de tu nodo remoto. A diferencia de las cookies, los macaroons tienen la ventaja de ser validados criptográficamente por el emisor o ser delegados para su verificación.