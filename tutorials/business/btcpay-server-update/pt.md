---
name: Atualizando o BTCPay Server
description: Aplique uma atualização de segurança à sua instância do BTCPay Server e rotacione as credenciais que importam
---

![cover](assets/cover.webp)

Executar seu próprio processador de pagamentos significa que você também é sua própria equipe de segurança. Quando os mantenedores do BTCPay Server publicam uma versão de segurança, ninguém vai corrigir sua instância por você: a atualização, a verificação e a rotação de credenciais que se seguem são tarefas suas.

Este tutorial percorre todo o procedimento, qualquer que seja a forma como você implantou o BTCPay Server: verifique a versão em execução, aplique a atualização no seu tipo de implantação, verifique se ela realmente entrou em vigor e rotacione os segredos que um atacante possa ter capturado enquanto sua instância estava vulnerável.

Se você ainda não implantou o BTCPay Server, comece pelo guia de instalação:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## A vulnerabilidade crítica de agosto de 2026

⚠️ **Alerta crítico de segurança (7 de agosto de 2026):** uma vulnerabilidade crítica que afeta o BTCPay Server está sendo ativamente explorada e pode levar à perda de fundos. Atualize sua instância imediatamente para a **versão 2.4.2** via `Admin Dashboard > Server > Maintenance > Update`, depois verifique se o rodapé exibe `2.4.2`. Se você não puder atualizar imediatamente, desligue seu BTCPay Server. Depois de atualizar, você também deve renovar completamente seus macaroons e seu `macaroons.db`, renovar completamente as strings de autenticação de qualquer outro backend Lightning e, caso tenha gerado uma carteira on-chain quente dentro do BTCPay Server, mover esses fundos e recriar a carteira. Integradores também devem atualizar o NBXplorer para a versão 2.6.10. Fonte: [notas de lançamento do BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

A versão 2.4.2 foi publicada em 7 de agosto de 2026. As notas de lançamento afirmam que ela corrige uma vulnerabilidade crítica que já estava sendo explorada em produção, reportada por `brunoerg` e `benthecarman` através do esforço Bitcoin Red Team. A mesma versão também corrige um contorno da autenticação de dois fatores TOTP através da autenticação Basic do Greenfield, e desativa a autenticação Basic do Greenfield por padrão cinco minutos após a criação da conta.

Duas consequências decorrem de "ativamente explorada":

- **Atualizar não é opcional nem algo a agendar para a próxima semana.** Uma instância não corrigida e acessível pela internet deve ser atualizada ou desligada.
- **Atualizar não basta por si só.** Se sua instância foi comprometida antes de você corrigi-la, o atacante pode já possuir cópias das suas credenciais Lightning e de qualquer material de chave de carteira quente que o BTCPay Server tenha gerado para você. Esses segredos permanecem válidos após a atualização até que você os rotacione. A seção de rotação abaixo é a parte que as pessoas costumam pular, e é a parte que de fato protege seus fundos.

## Passo 1 — Descubra qual versão você está executando

Faça login no seu BTCPay Server e observe o **rodapé de qualquer página**: a string de versão é exibida ali. Você também pode abrir `Admin Dashboard > Server > Maintenance`, que mostra a versão atual e os controles de atualização.

Se sua instância expõe a API Greenfield, `GET /api/v1/server/info` também retorna a versão.

Qualquer versão abaixo de `2.4.2` é vulnerável.

## Passo 2 — Atualize

### Implantação Docker self-hosted (a instalação padrão)

Isso cobre a implantação Docker oficial, que é o que você obtém pela documentação do BTCPay Server, pelo lançador de um clique da LunaNode e pela maioria das instalações em VPS.

O caminho mais simples é a interface web:

1. Vá para `Admin Dashboard > Server > Maintenance`.
2. Clique em **Update**.
3. Aguarde os contêineres serem baixados e reiniciados. A interface ficará indisponível por alguns minutos.

Se a interface web estiver inacessível, ou se você preferir ver os logs, faça-o via SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Em uma instalação padrão, `$BTCPAY_BASE_DIRECTORY` é `/root`, então o diretório é `/root/btcpayserver-docker`. O script baixa as imagens mais recentes, recria os contêineres e imprime as versões resultantes.

A implantação Docker distribui o NBXplorer junto com o BTCPay Server, então uma atualização padrão também leva o NBXplorer para a versão recomendada `2.6.10`. Se você executa o NBXplorer separadamente — típico para integradores e para stacks personalizadas — atualize-o explicitamente.

### Umbrel

Abra o painel do Umbrel, vá até a **App Store**, encontre o BTCPay Server e aplique a atualização, se houver uma disponível.

⚠️ **Importante:** os pacotes da app store são reempacotados pela equipe do Umbrel e podem ficar horas ou dias atrás do upstream. Verifique a versão no rodapé do BTCPay Server após atualizar. Se ainda estiver abaixo de `2.4.2`, **pare o aplicativo** no painel do Umbrel e aguarde a versão empacotada, em vez de deixar uma instância vulnerável em execução.

O guia dedicado do Umbrel cobre o aplicativo em si:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Mesma lógica: atualize o BTCPay Server pelo marketplace do StartOS, depois verifique a versão no rodapé. Se a versão empacotada ainda não for `2.4.2`, pare o serviço até que esteja.

### Hospedagem gerenciada e de terceiros

Se outra pessoa opera sua instância (um provedor de hospedagem, uma associação, o servidor de um amigo), você ainda precisa da confirmação. Peça ao operador a string de versão exibida no rodapé, e pergunte explicitamente se a rotação de credenciais pós-atualização descrita abaixo foi realizada. "Atualizamos" não é a mesma resposta que "rotacionamos seus macaroons".

## Passo 3 — Verifique se a atualização realmente entrou em vigor

Recarregue a interface do BTCPay Server e leia a versão no rodapé. Ela deve mostrar `2.4.2` ou superior.

Não confie apenas no comando de atualização terminar sem erro: em máquinas com recursos limitados, um download de imagem pode falhar silenciosamente e deixar o contêiner anterior em execução. Leia a versão, sempre.

## Passo 4 — Rotacione suas credenciais

Este é o passo que transforma "corrigido" em "seguro". Como a vulnerabilidade estava sendo explorada antes do lançamento da correção, trate todo segredo que sua instância possuía como potencialmente conhecido por um atacante.

### Lightning: LND

Regenere os macaroons **e** o arquivo `macaroons.db`. Apagar apenas os arquivos de macaroon não é suficiente — o LND deriva os macaroons a partir da chave raiz armazenada em `macaroons.db`, então um atacante que possua uma cópia de um macaroon antigo mantém acesso até que esse banco de dados seja recriado.

O procedimento é: pare o LND, remova `macaroons.db` e os arquivos `*.macaroon` do diretório de rede (para mainnet, `data/chain/bitcoin/mainnet/` dentro do diretório de dados do LND), depois reinicie e desbloqueie o LND, que os recriará. Faça backup do diretório antes, e reconecte todas as aplicações que usavam os macaroons antigos — o próprio BTCPay Server, Zeus, Thunderhub, RTL, Alby e qualquer script que você tenha escrito.

Se você também expõe o LND pela internet, revise ao mesmo tempo o certificado TLS e quaisquer credenciais do `lnd.conf`.

### Lightning: outros backends

Tudo que autentica no seu nó com uma string precisa de uma nova string:

- **Core Lightning**: regenere a rune ou as credenciais de acesso usadas pela conexão.
- **Phoenixd**: rotacione a senha HTTP.
- **LNbits e similares**: revogue e reemita as chaves de admin e de invoice.
- **Strings de conexão de nó remoto** armazenadas nas configurações da loja no BTCPay Server: reescreva-as com os novos segredos.

### Carteira on-chain quente gerada dentro do BTCPay Server

Se você deixou o BTCPay Server gerar uma carteira on-chain para você — em vez de conectar uma carteira de hardware ou importar uma xpub cujas chaves nunca tocaram o servidor — essa seed viveu na máquina.

Considere-a queimada:

1. Crie uma nova carteira, idealmente com uma carteira de hardware, para que as chaves nunca fiquem novamente no servidor.
2. Transfira os fundos da carteira antiga para a nova.
3. Substitua o esquema de derivação nas configurações da loja pela nova carteira.
4. Nunca reutilize a seed antiga.

Configurações somente-visualização (xpub ou carteira de hardware) não precisam disso: as chaves privadas nunca estiveram no servidor. É exatamente por isso que o guia de instalação as recomenda.

### Contas do BTCPay Server e chaves de API

Aproveite e:

- Altere as senhas de todas as contas de usuário na instância.
- Revogue e reemita todas as **chaves de API** Greenfield.
- Reinscreva a autenticação de dois fatores, já que a 2.4.2 corrige um contorno de 2FA.
- Abra `Admin Dashboard > Server > Users` e verifique que não existe nenhuma conta inesperada.
- Revise os **payouts**, **pull payments** e **reembolsos** recentes em busca de entradas que você não criou.
- Revise seus webhooks e seus segredos.

## Passo 5 — Mantenha-se informado para a próxima vez

Versões de segurança só ajudam os operadores que ficam sabendo delas:

- Acompanhe os [lançamentos do BTCPay Server no GitHub](https://github.com/btcpayserver/btcpayserver/releases) — o GitHub pode enviar um e-mail a cada novo lançamento de um repositório.
- Siga os canais de anúncios do projeto e o [blog oficial](https://blog.btcpayserver.org/).
- Mantenha sua instância em uma versão que você consiga atualizar rapidamente: quanto mais atrasado você estiver, mais dolorosa se torna uma atualização de emergência.

Fazer self-hosting lhe dá soberania sobre seus pagamentos. O custo dessa soberania é exatamente este: ler notas de lançamento e ser você quem aplica as correções.
