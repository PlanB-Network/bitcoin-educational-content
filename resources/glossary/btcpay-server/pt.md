---
term: BTCPay Server

definition: Processador de pagamentos de código aberto que permite aceitar pagamentos em bitcoins sem intermediários.
---

⚠️ **Alerta crítico de segurança (7 de agosto de 2026):** uma vulnerabilidade crítica que afeta o BTCPay Server está a ser explorada ativamente e pode levar à perda de fundos. Atualize a sua instância para a **versão 2.4.2** imediatamente através de `Admin Dashboard > Server > Maintenance > Update` e, em seguida, verifique se o rodapé apresenta `2.4.2`. Se não conseguir atualizar de imediato, desligue o seu BTCPay Server. Depois de atualizar, deve também renovar completamente os seus macaroons e o seu `macaroons.db`, renovar completamente as cadeias de autenticação de qualquer outro backend Lightning e, caso tenha gerado uma carteira quente on-chain dentro do BTCPay Server, mover esses fundos e recriar a carteira. Os integradores devem igualmente atualizar o NBXplorer para a versão 2.6.10. Fonte: [notas de lançamento do BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
O BTCPay Server é um processador de pagamentos de código aberto que permite aos comerciantes e utilizadores aceitarem pagamentos em Bitcoin sem dependerem de terceiros para o processamento de transacções. Lançado em 2017, o BTCPay Server fornece uma solução de integração de pagamentos Bitcoin para sites de comércio eletrónico, com funcionalidades avançadas, como suporte para carteiras de hardware, ferramentas de faturação e contabilidade, bem como compatibilidade com a Lightning Network. O seu desenvolvimento foi iniciado por Nicolas Dorier, em resposta às acções da Bitpay que, segundo ele, tinha enganado os seus utilizadores, empurrando-os para a adoção do SegWit2x, que a empresa considerava erradamente como a "verdadeira" Bitcoin. Esta oposição foi resumida num tweet agora famoso de Nicolas Dorier em agosto de 2017:

> "_Isto é mentira, a minha confiança em ti está quebrada, vou tornar-te obsoleto_".
