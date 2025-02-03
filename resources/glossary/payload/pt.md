---
term: PAYLOAD

---
No contexto geral da computação, uma carga útil refere-se aos dados essenciais transportados num pacote de dados maior. Por exemplo, em um endereço SegWit V0 no Bitcoin, o payload corresponde ao hash da chave pública, excluindo vários metadados (o HRP, o separador, a versão SegWit e a soma de verificação). Por exemplo, no endereço `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, temos:


- `bc` : a parte legível por humanos (HRP);
- `1` : o separador;
- `q` : a versão do SegWit. Aqui, é a versão 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa` : a carga útil, neste caso, o hash da chave pública;
- `ys50gj` : a soma de controlo.