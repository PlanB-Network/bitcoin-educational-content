---
name: Lightning Watchtower
description: Entendendo e usando um Watchtower no seu nó do Lightning
---
![cover](assets/cover.webp)



## Como é que as Torres de Vigia funcionam?



Uma parte essencial do ecossistema Lightning Network, as _Watchtowers_ fornecem um nível extra de proteção para os canais Lightning dos utilizadores. O seu papel principal é monitorizar o estado do canal e intervir se um lado do canal tentar defraudar o outro.



Como é que um Watchtower pode determinar se um canal foi comprometido? Recebe do cliente (uma das partes do canal) as informações necessárias para identificar e tratar corretamente qualquer violação. Esta informação inclui detalhes da transação mais recente, o estado atual do canal e o Elements necessário para criar transacções de penalização. Antes de transmitir estes dados ao Watchtower, o cliente pode encriptá-los para preservar a confidencialidade. Assim, mesmo que o Watchtower receba os dados, não poderá decifrá-los até que ocorra efetivamente uma violação. Este mecanismo de encriptação protege a privacidade do cliente e impede o Watchtower de obter acesso não autorizado a informações sensíveis.



Neste tutorial, veremos 3 formas de utilizar um **Watchtower** :




- em primeiro lugar, o método clássico em bruto através do LND,
- depois outra abordagem com o Olho de Satoshi,
- e, finalmente, a configuração simplificada de um Watchtower no seu nó Lightning hospedado com a Umbrel.



## 1 - Configuração de um Watchtower ou de um cliente via LND



*Este tutorial foi retirado da [documentação oficial do LND] (https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Algumas mudanças podem ter sido feitas na versão original



Desde a versão 0.7.0, o `LND` suporta a execução de um Watchtower altruísta privado como um subsistema totalmente integrado do `LND`. As torres de vigilância fornecem uma segunda linha de defesa contra cenários de violação maliciosa ou acidental quando o nó do cliente está offline ou incapaz de responder no momento da violação, oferecendo um maior grau de segurança para os fundos do canal.



Ao contrário de uma _torre de recompensa_, que exige uma parte dos fundos do canal em troca do seu serviço, uma _torre de altruísmo_ devolve todos os fundos da vítima (menos as taxas On-Chain) sem cobrar uma comissão. As torres de vigia de recompensa serão activadas numa versão posterior; ainda estão em fase de testes e melhoramentos.



Além disso, o `LND` pode agora ser configurado para funcionar como um _cliente de torre de vigia_, salvando transações criptografadas de remediação de violação (as chamadas "transações de justiça") de outras torres de vigia altruístas. O Watchtower armazena blobs encriptados de tamanho fixo e só pode desencriptar e publicar a transação de justiça depois de a parte infratora ter transmitido um estado revogado do Commitment. As comunicações Cliente ↔ Watchtower são encriptadas e autenticadas usando pares de chaves efémeras, o que limita a capacidade do Watchtower de localizar os seus clientes através de credenciais de longo prazo.



Observe que optamos por implantar nesta versão um conjunto limitado de recursos que já fornecem segurança significativa para os usuários do `LND`. Muitos outros recursos relacionados ao Watchtower estão próximos da conclusão ou bem avançados; continuaremos a entregá-los à medida que os testarmos e assim que forem considerados seguros.



nota: por enquanto, as torres de vigia apenas guardam a saída `to_local` e `to_remote` dos compromissos revogados; guardar a saída HTLC será implementado numa versão futura, uma vez que o protocolo pode ser alargado para incluir dados de assinatura adicionais em blobs encriptados._



### Configuração de um Watchtower



Para configurar um Watchtower, os utilizadores de linha de comandos precisam de compilar o sub-servidor opcional `watchtowerrpc`, que permite a interação com o Watchtower via gRPC ou `lncli`. Os binários publicados incluem o sub-servidor `watchtowerrpc` por padrão.



A configuração mínima para ativar o Watchtower é `Watchtower.active=1`.



Pode obter as informações de configuração do Watchtower com `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



O conjunto completo de opções de configuração do Watchtower está disponível via `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Interfaces de escuta



Por padrão, o Watchtower escuta em `:9911`, que corresponde à porta `9911` em todas as interfaces disponíveis. Usuários podem definir suas próprias interfaces de escuta através da opção `--Watchtower.listen=`. Você pode verificar sua configuração no campo `"listeners"` do `lncli tower info`. Se você tiver problemas para se conectar ao seu Watchtower, certifique-se de que a `<port>` está aberta ou que seu proxy está corretamente configurado para um Interface ativo.



#### Endereços IP externos



Os utilizadores podem também especificar o IP externo do Watchtower com `Watchtower.externalip=`, que expõe o URI completo do Watchtower (pubkey@host:port) via RPC ou `lncli tower info` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Os URIs Watchtower podem ser comunicados aos clientes para ligação e utilização com o seguinte comando:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Se os clientes do Watchtower necessitarem de aceder remotamente, certifique-se de que :




- Abre a porta 9911 (ou uma porta definida via `Watchtower.listen`).
- Utilize um proxy para redirecionar o tráfego de uma porta aberta para o Watchtower que está a ouvir o Address.



#### Serviços ocultos Tor



As torres de vigia suportam os serviços ocultos do Tor e podem automaticamente generate um no arranque com as seguintes opções:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



O .onion Address aparece então no campo `"uris"` durante uma consulta `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



nota: a chave pública do Watchtower é distinta da chave pública do nó `LND`. De momento, funciona como uma "whitelist do Soft", uma vez que os clientes precisam de conhecer a chave pública do Watchtower para o utilizar como backup, enquanto aguardam mecanismos de whitelisting mais avançados. Recomendamos que NÃO divulgue esta chave pública abertamente, a menos que esteja preparado para expor o seu Watchtower a toda a Internet



#### Diretório da base de dados Watchtower



A base de dados Watchtower pode ser movida utilizando a opção `Watchtower.towerdir=`. Note que um sufixo `/Bitcoin/Mainnet/Watchtower.db` será adicionado ao caminho escolhido para isolar as bases de dados por string. Assim, definindo `Watchtower.towerdir=/path/to/towerdir` produzirá uma base de dados em `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



No Linux, por exemplo, o banco de dados padrão do Watchtower está localizado em :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Configuração de um cliente Watchtower



Para configurar um cliente Watchtower, são necessários dois itens:





- Ativar o cliente Watchtower com a opção `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- O URI de um Watchtower ativo.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



É possível configurar várias torres de vigia desta forma.



#### Taxas de honorários para transacções legais



Os utilizadores podem opcionalmente definir a taxa para transacções de justiça através da opção `wtclient.sweep-fee-rate`, que aceita valores em sat/byte. O valor padrão é de 10 sat/byte, mas é possível tentar obter taxas mais altas para obter maior prioridade durante os picos de carga. A alteração de `sweep-fee-rate` se aplica a todas as novas atualizações após a reinicialização do daemon.



#### Supervisão



Com o comando `lncli wtclient`, os utilizadores podem agora interagir diretamente com o cliente Watchtower para obter ou modificar informações sobre todas as torres de vigia registadas.



Por exemplo, com `lncli wtclient tower`, pode descobrir o número de sessões atualmente negociadas com o Watchtower adicionado acima e determinar se está a ser utilizado para backups graças ao campo `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Para obter informações sobre as sessões do Watchtower, utilize a opção `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Todas as opções de configuração do cliente Watchtower estão disponíveis via `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Instalar o seu próprio olho de Satoshi



*Este tutorial foi parcialmente extraído de um artigo no [Summer of Bitcoin Blog] (https://blog.summerofbitcoin.org/). Foram efectuadas modificações à versão original*



O Olho de Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) é um relâmpago Watchtower não-depositário, em conformidade com [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). É constituído por dois componentes principais:





- teos**: inclui um Interface de linha de comando (CLI) e as caraterísticas essenciais de servidor do Watchtower. Dois binários - **teosd** e **teos-CLI** - são produzidos quando este _crate_ é compilado.





- teos-common**: inclui funcionalidades partilhadas do lado do servidor e do lado do cliente (útil para criar um cliente).



Para executar o Watchtower corretamente, é necessário executar o **bitcoind** antes de lançar o Watchtower com o comando **teosd**. Antes de executar estes dois comandos, é necessário configurar o ficheiro **Bitcoin.conf**. Aqui está como fazer isso:





- Instalar o Bitcoin core a partir da fonte ou fazer o download. Após o download, coloque o arquivo **Bitcoin.conf** no diretório do usuário do Bitcoin core. Consulte este link para obter mais informações sobre onde colocar o arquivo, pois isso depende do sistema operacional usado.





- Uma vez identificada a localização, adicione as seguintes opções:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- servidor**: para pedidos RPC





- rpcuser** e **rpcpassword**: autenticam os clientes RPC no servidor





- regtest**: não é necessário, mas é útil se estiver a planear o desenvolvimento.



Os valores para **rpcuser** e **rpcpassword** devem ser escolhidos pelo utilizador. Devem ser escritos sem aspas. Por exemplo:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Agora, se executar **bitcoind**, o nó deve iniciar.





- Para a parte do Watchtower, é necessário instalar primeiro o **teos** a partir da fonte. Siga as instruções fornecidas neste link.





- Depois de ter instalado com sucesso o **teos** no seu sistema e executado os testes, pode passar ao passo final: configurar o ficheiro **teos.toml** no diretório de utilizador do teos. O ficheiro deve ser colocado numa pasta chamada **.teos** (note o ponto) no seu diretório home. Por exemplo, **/home//.teos** no Linux. Quando a localização tiver sido encontrada, crie um ficheiro **teos.toml** e defina estas opções de acordo com as alterações efectuadas em **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Note que aqui, o nome de utilizador e a palavra-passe devem ser escritos **entre aspas**. Usando o exemplo anterior :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Uma vez que isso tenha sido feito, você deve estar pronto para lançar o Watchtower. Como estamos a correr em **regtest**, é provável que nenhum bloco tenha sido minerado na nossa rede de teste Bitcoin quando o Watchtower se ligou pela primeira vez (se foi, algo está errado). O Watchtower constrói um cache interno dos últimos 100 blocos do **bitcoind**; assim, na primeira inicialização, você pode receber o seguinte erro:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Como estamos a usar o **regtest**, podemos bloquear o Miner emitindo um comando RPC, sem ter que esperar pelo atraso médio de 10 minutos visto noutras redes (como o Mainnet ou Testnet). Veja a ajuda do **bitcoin-cli** para detalhes de como fazer blocos Miner.



![Image](assets/fr/01.webp)



É tudo: executou com êxito o Watchtower. Parabéns. 🎉




## 3 - Configurando um Watchtower na Umbrel



Na Umbrel, a ligação a um Watchtower para proteger o seu nó Lightning é extremamente simples, pois tudo é feito através do Interface gráfico. Depois de se ligar remotamente ao seu nó, abra a aplicação "**Lightning Node**".



![Image](assets/fr/02.webp)



Clique nos três pequenos pontos no canto superior direito do Interface e, em seguida, selecione "**Configurações avançadas**".



![Image](assets/fr/03.webp)



No menu "**Watchtower**", estão disponíveis duas opções:





- Serviço Watchtower**: esta opção permite-lhe operar um Watchtower, ou seja, um serviço que monitoriza os canais de outros nós para detetar qualquer tentativa de fraude. Em caso de violação, o seu Watchtower publica uma transação no Blockchain, permitindo aos utilizadores recuperar os seus fundos bloqueados. Uma vez ativado, o URI do seu Watchtower aparece e pode ser comunicado a outros nós para que o possam adicionar ao seu cliente Watchtower;





- Cliente Watchtower**: esta opção permite-lhe ligar-se a torres de vigilância externas para proteger os seus próprios canais. Uma vez activada, pode adicionar serviços Watchtower aos quais o seu nó transmitirá as informações necessárias sobre os seus canais. Estas torres de vigilância vigiarão o seu estado e intervirão em caso de tentativa de fraude.



A sua prioridade é, obviamente, ativar o *Watchtower Client* para proteger o seu nó, mas também recomendo que active o *Watchtower Service* para contribuir para a segurança de outros utilizadores.



![Image](assets/fr/04.webp)



Em seguida, clique no botão "**Save and Restart Node**" do Green. O LND será reiniciado.



No mesmo menu, encontrará também o URI do seu serviço Watchtower, caso o tenha ativado. Pode também adicionar o URI de um Watchtower externo para proteger os seus canais. Clique em "**ADD**" para confirmar.



![Image](assets/fr/05.webp)



Existem várias Torres de Vigia disponíveis online. Por exemplo, [LN+ e Voltage oferecem um Watchtower altruísta](https://lightningnetwork.plus/Watchtower) ao qual se pode ligar:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Outra opção é Exchange seu Watchtower URI com seus colegas bitcoiners, para que cada um proteja o nó do outro.



Recomendo também a instalação de várias torres de vigia para reduzir os riscos no caso de uma delas ficar indisponível.



Por último, pode ajustar o parâmetro "**Watchtower Client Sweep Fee Rate**". Este parâmetro define a taxa máxima que está disposto a pagar para que uma transação de punição de difusão Watchtower seja incluída num bloco. Certifique-se de que define um valor suficientemente elevado, adaptado aos montantes bloqueados nos seus canais.