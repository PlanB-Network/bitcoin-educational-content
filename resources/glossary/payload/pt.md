---
term: PAYLOAD
---

No contexto geral da computação, payload refere-se aos dados essenciais transportados dentro de um pacote de dados maior. Por exemplo, em um endereço SegWit V0 no Bitcoin, o payload corresponde ao hash da chave pública, excluindo vários metadados (o HRP, o separador, a versão SegWit e o checksum). Por exemplo, no endereço `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, temos:
* `bc` : a parte legível por humanos (HRP);
* `1` : o separador;
* `q` : a versão SegWit. Aqui, é a versão 0;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : o payload, aqui, o hash da chave pública;
* `ys50gj` : o checksum.