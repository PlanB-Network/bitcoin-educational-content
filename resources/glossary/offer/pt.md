---
term: Offer
definition: Códigos QR estáticos reutilizáveis para receber múltiplos pagamentos no Lightning (BOLT12).
---

No BOLT12, as *ofertas* são códigos QR estáticos que permitem efetuar vários pagamentos no Lightning Network. Ao contrário das facturas convencionais, as *ofertas* podem ser reutilizadas. Podem ser utilizadas para vários pedidos generate e Invoice. Quando um utilizador digitaliza um código QR que contém uma *oferta*, envia uma mensagem a solicitar um novo Invoice ao nó Lightning associado. O nó responde com um Invoice que o pagador pode utilizar. As *ofertas* fornecem assim um identificador único para receber vários pagamentos de diferentes utilizadores no Lightning.