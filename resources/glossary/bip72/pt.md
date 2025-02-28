---
term: BIP72

---
Completa o BIP70 e o BIP71, definindo a extensão do Bitcoin URI (BIP21) com um parâmetro adicional `r`. Este parâmetro permite incluir um link para um pedido de pagamento seguro assinado pelo certificado SSL do comerciante. Quando um cliente clica neste URI alargado, a sua carteira contacta o servidor do comerciante para pedir os detalhes do pagamento. Estes detalhes são automaticamente preenchidos na interface de transação da carteira, e o cliente pode ser informado de que está a pagar ao proprietário do domínio correspondente ao certificado de assinatura (por exemplo, "pandul.fr"). Uma vez que esta melhoria está associada à BIP70, nunca foi amplamente adoptada.