---
term: CÓDIGO DE PAGAMENTO REUTILIZÁVEL

---
No BIP47, um código de pagamento reutilizável é um identificador estático gerado a partir de uma carteira Bitcoin que permite uma transação de notificação e a derivação de endereços únicos. Isto evita a reutilização de endereços, que conduz a uma perda de privacidade, sem ter de derivar e transmitir manualmente novos endereços não utilizados para cada pagamento. No BIP47, os códigos de pagamento reutilizáveis são construídos da seguinte forma:


- O byte 0 corresponde à versão;
- O byte 1 é um campo de bits para acrescentar informações em caso de utilização específica;
- O byte 2 indica a paridade do `y` da chave pública;
- Do byte 3 ao byte 34, encontrará o valor `x` da chave pública;
- Do byte 35 ao byte 66, existe o código de cadeia associado à chave pública;
- Do byte 67 ao byte 79, o preenchimento é zero.

Uma parte legível por humanos (HRP) é geralmente acrescentada no início do código de pagamento e uma soma de controlo no final, sendo depois codificada em base58. A construção de um código de pagamento é, portanto, bastante semelhante à de uma chave alargada. Eis, por exemplo, o meu próprio código de pagamento BIP47 em base58:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

Na implementação PayNym do BIP47, os códigos de pagamento também podem ser expressos sob a forma de identificadores associados à imagem de um robot. Eis o meu, por exemplo:

```text
+throbbingpond8B1
```

A utilização de códigos de pagamento com a implementação PayNym está atualmente disponível na Sparrow Wallet no PC e na Samourai Wallet no telemóvel.