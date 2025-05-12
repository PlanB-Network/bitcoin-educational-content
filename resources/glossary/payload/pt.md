---
term: CARGA ÚTIL
---

No contexto geral da computação, uma carga útil é o dado essencial transportado num pacote de dados maior. Por exemplo, num SegWit V0 sobre Bitcoin Address, o payload corresponde ao Hash da chave pública, sem os vários metadados (o HRP, o separador, a versão SegWit e a soma de controlo). Por exemplo, no Address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, temos :




- `bc`: a parte legível por humanos (HRP) ;
- `1`: o separador ;
- `q`: Versão do SegWit. Esta é a versão 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa`: a carga útil, neste caso, o Hash da chave pública ;
- `ys50gj`: soma de controlo.