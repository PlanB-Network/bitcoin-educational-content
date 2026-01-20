---
term: LOCK (.LOCK)

---
Ficheiro utilizado no Bitcoin Core para bloquear o diretório de dados. É criado quando o bitcoind ou Bitcoin-qt é iniciado para evitar que múltiplas instâncias do software acessem o mesmo diretório de dados simultaneamente. O objetivo é evitar conflitos e corrupção de dados. Se o software parar inesperadamente, o arquivo .lock pode permanecer e deve ser excluído manualmente antes de reiniciar o Bitcoin Core.