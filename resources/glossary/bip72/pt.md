---
termo: BIP72
---

Completa o BIP70 e o BIP71 definindo a extensão do URI do Bitcoin (BIP21) com um parâmetro adicional `r`. Esse parâmetro permite incluir um link para um pedido de pagamento seguro assinado pelo certificado SSL do comerciante. Quando um cliente clica neste URI estendido, sua carteira contata o servidor do comerciante para solicitar os detalhes do pagamento. Esses detalhes são automaticamente preenchidos na interface de transação da carteira, e o cliente pode ser informado de que está pagando ao dono do domínio correspondente ao certificado de assinatura (por exemplo, "pandul.fr"). Como essa melhoria está agrupada com o BIP70, ela nunca foi amplamente adotada.