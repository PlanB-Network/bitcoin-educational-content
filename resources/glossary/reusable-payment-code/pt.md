---
term: CÓDIGO DE PAGAMENTO REUTILIZÁVEL
---

No BIP47, um código de pagamento reutilizável é um identificador estático gerado a partir de uma carteira Bitcoin que permite uma transação de notificação e a derivação de endereços únicos. Isso evita a reutilização de endereços, o que leva à perda de privacidade, sem ter que derivar e transmitir manualmente novos endereços não utilizados para cada pagamento. No BIP47, os códigos de pagamento reutilizáveis são construídos da seguinte forma:
* Byte 0 corresponde à versão;
* Byte 1 é um campo de bits para adicionar informações em caso de uso específico;
* Byte 2 indica a paridade do `y` da chave pública;
* Do byte 3 ao byte 34, você encontrará o valor `x` da chave pública;
* Do byte 35 ao byte 66, há o código da cadeia associado à chave pública;
* Do byte 67 ao byte 79, há um preenchimento de zeros.

Uma Parte Legível por Humanos (HRP, na sigla em inglês) é geralmente adicionada no início do código de pagamento e um checksum no final, e então é codificado em base58. A construção de um código de pagamento é, portanto, bastante semelhante à de uma chave estendida. Aqui está o meu próprio código de pagamento BIP47 em base58, por exemplo:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

Na implementação PayNym do BIP47, os códigos de pagamento também podem ser expressos na forma de identificadores associados à imagem de um robô. Aqui está o meu, por exemplo:

```text
+throbbingpond8B1
```

O uso de códigos de pagamento com a implementação PayNym está atualmente disponível no Sparrow Wallet no PC e no Samourai Wallet no celular.