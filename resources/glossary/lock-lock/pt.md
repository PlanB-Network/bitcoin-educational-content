---
term: LOCK (.LOCK)
---

Arquivo usado no Bitcoin Core para bloquear o diretório de dados. É criado quando o bitcoind ou o Bitcoin-qt são iniciados para impedir que múltiplas instâncias do software acessem o mesmo diretório de dados simultaneamente. O objetivo é prevenir conflitos e corrupção de dados. Se o software parar inesperadamente, o arquivo .lock pode permanecer e deve ser manualmente deletado antes de reiniciar o Bitcoin Core.