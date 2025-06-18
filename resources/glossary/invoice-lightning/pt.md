---
term: Invoice ILUMINAÇÃO
---

Pedido de pagamento relâmpago gerado pelo destinatário, contendo todas as informações necessárias para completar a transação.


Um Lightning Invoice contém o destino do pagamento sob a forma da chave pública do nó destinatário, mas também um prefixo `LN`, o montante, um prazo de validade, o Hash do segredo utilizado nos HTLCs e outros metadados, alguns dos quais são opcionais, como as opções de encaminhamento. Estas facturas são definidas pela norma BOLT11. Uma vez paga, uma fatura Invoice Lightning não pode ser reutilizada.


> ► *Em francês, poderíamos traduzir "Invoice" por "facture", mas geralmente utilizamos o termo inglês mesmo em francês.*