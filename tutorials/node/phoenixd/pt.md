---
name: Phoenixd
description: Implante seu próprio nó Lightning minimalista com o Phoenixd
---

![cover](assets/cover.webp)



Autonomia financeira significa também controlar a sua infraestrutura Lightning. Para os programadores e as empresas que desejam integrar o Bitcoin Lightning nas suas aplicações, o **Phoenixd** representa a solução ideal: um nó Lightning minimalista e especializado com gestão automática da liquidez.



O Phoenixd é um servidor Lightning desenvolvido pela ACINQ, projetado especificamente para enviar e receber pagamentos Lightning por meio de uma API HTTP. Ao contrário das implementações completas, como o LND ou o Core Lightning, o Phoenixd abstrai toda a complexidade do gerenciamento de canais, preservando a autoproteção de seus fundos.



Neste tutorial, veremos como instalar, configurar e usar o Phoenixd para desenvolver aplicativos Lightning com uma infraestrutura auto-hospedada e uma API fácil de usar.



## O que é o Phoenixd?



O Phoenixd é um nó Lightning mínimo e especializado desenvolvido pela ACINQ. É uma solução concebida para programadores e empresas que pretendem integrar o Lightning nas suas aplicações sem a complexidade de gestão de um Full node.



### Princípio de funcionamento



**O Phoenixd é um nó Lightning mínimo que utiliza o ACINQ como seu LSP (Lightning Service Provider) para liquidez automática. Quando recebe pagamentos Lightning, abre automaticamente canais com nós ACINQ para atribuir a capacidade de entrada necessária. Esta liquidez "on-the-fly" é instantânea, mas cobrada exatamente a **1% + taxas Mining** do montante recebido.



**Gestão automatizada:** O sistema gere três Elements principais:




- Canais Lightning**: Abrir, fechar e gerir automaticamente conforme necessário
- Liquidez de entrada/saída**: Aprovisionamento automático através de splicing e abertura de canais
- Crédito de taxas** : Os pequenos pagamentos insuficientes para justificar um canal são armazenados como uma provisão para encargos futuros



### Benefícios da Phoenixd



**Você controla as suas chaves privadas (seed de 12 palavras) e os seus fundos. Phoenixd gera seu Wallet localmente sem nunca compartilhar suas chaves.



**Infraestrutura pessoal:** O Phoenixd funciona no seu servidor, dando-lhe acesso a registos detalhados, configuração e controlo da API. Você não depende mais de um serviço de terceiros para ter acesso aos seus fundos.



**API integrada:** O Phoenixd dispõe de uma API HTTP para integração com outros serviços, suporte nativo de LNURL e desenvolvimento de aplicações personalizadas.



**Facilidade de integração:** Graças à sua API REST simples, o Phoenixd pode ser integrado em qualquer aplicação ou serviço que exija pagamentos Lightning.



**Nota importante:** A liquidez automática continua a provir do ACINQ como LSP (Lightning Service Provider). O Phoenixd utiliza o mesmo mecanismo que o Phoenix mobile para a gestão automática dos canais.



## Instalar o Phoenixd



### Pré-requisitos



O Phoenixd requer um ambiente Linux (recomenda-se o Ubuntu/Debian), com alguns conhecimentos básicos de linha de comandos. Para um desempenho ideal, você precisará do :





- Servidor Linux**: VPS ou máquina local com ligação estável
- OpenJDK 21** : Ambiente de tempo de execução Java
- Ligação estável à Internet**: Para sincronização com o Lightning Network
- Nome do domínio** (opcional) : Para acesso HTTPS seguro à API



### Descarregamento e instalação



**1. Descarregar o Phoenixd**



Aceda à página [GitHub releases] (https://github.com/ACINQ/phoenixd/releases) e transfira a versão mais recente para a sua arquitetura:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Primeiro arranque



Iniciar o Phoenixd para inicialização:



```bash
./phoenixd
```



No primeiro lançamento, ser-lhe-á pedido que confirme dois passos importantes escrevendo "I understand" :



**Mensagem 1 - Backup:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Guardem estas 12 palavras** - são a vossa única garantia de recuperação.



**Mensagem 2 - Liquidez automática:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Escreva "Compreendo" para cada confirmação.



![Premier démarrage](assets/fr/01.webp)



*O Phoenixd arranca pela primeira vez: confirmações de segurança e liquidez automática*



**3. Configuração em serviço** (apenas em francês)



Para operação contínua, crie um arquivo systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Serviço Phoenixd ativo e operacional via systemd e `auto-liquidez` a 2m sat*



## Configuração e segurança



### Ficheiro de configuração



O Phoenixd cria automaticamente `~/.phoenix/phoenix.conf` com os parâmetros essenciais:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Parâmetros-chave




- `auto-liquidez`: Tamanho dos canais abertos automaticamente (predefinição: 2M Sats)
- http-password`: Palavra-passe de administrador para a API (criação de Invoice E envio de pagamentos)
- http-password-limited-access`: Palavra-passe restrita (apenas para a criação do Invoice)



### Acesso seguro com HTTPS



Por padrão, a API do Phoenixd só é acessível via HTTP local (`http://127.0.0.1:9740`). Para utilizar o seu nó a partir do exterior (aplicações móveis, outros servidores, integrações web), é necessário configurar um acesso HTTPS seguro.



**Princípio do proxy inverso:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



*o *Nginx** actua como um **proxy inverso**: ouve os pedidos HTTPS da Internet no porto 443, redirecciona-os para o Phoenixd localmente (porto 9740) e envia as respostas encriptadas de volta ao cliente.



**O certificado SSL/TLS** é um ficheiro digital que :




- Provar a identidade do seu servidor** (evita ataques man-in-the-middle)
- Permite a encriptação HTTPS**: todos os dados, incluindo as suas palavras-passe API, são encriptados durante o transporte
- Emitido gratuitamente** pela Let's Encrypt através da ferramenta certbot



Esta configuração permite-lhe :




- Acesso seguro à API a partir da Internet**
- Encriptar as suas palavras-passe API** durante o transporte (para evitar que sejam transmitidas em texto claro)
- Integrar o Phoenixd** em aplicações externas que requerem HTTPS
- Conformidade com as normas de segurança** para APIs financeiras



Configurar este proxy inverso HTTPS com o nginx :



**1. Configuração do Nginx**



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. Certificado SSL



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Teste de funcionamento



Verifique se o Phoenixd está a funcionar corretamente:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Estes comandos devem devolver informações JSON sobre o estado e o saldo do nó (inicialmente vazio).



![Commandes CLI](assets/fr/03.webp)



*Comandos getinfo e getbalance para verificar o estado do nó*



## Utilizar a API



### Primeiro teste de receção



**1. Criar um Raio** Invoice



Utilize a API para criar o seu primeiro Invoice:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Compreender o mecanismo automático de liquidez



**Princípio fundamental:** Quando recebe um pagamento Lightning, a Phoenixd tem por vezes de abrir um novo canal para o poder receber. Esta abertura de canal custa uma taxa que é **deduzida automaticamente** do valor recebido.



**Exemplo concreto com 100 000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Primeiro teste de aceitação: Sats 100k recebido, saldo final do Sats 75.561 após dedução dos custos de liquidez*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Cálculo da taxa:**




- Taxa de serviço**: 1% da capacidade do canal (2.115.000 Sats) = 21.150 Sats
- Taxas Mining**: ~3,289 Sats (para transação On-Chain)
- Total**: 24,439 Sats deduzido automaticamente



**Verificação com os comandos CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Saldo final após o envio do pagamento: 257 Sats restantes após a expedição do relâmpago*



**Crédito de taxa para pagamentos pequenos:** Se receber pagamentos demasiado pequenos para justificar a abertura de um canal (< aprox. 25k Sats), estes são guardados num "crédito de taxa" não reembolsável. Este crédito será usado para pagar futuras taxas de canal quando receberes uma quantia suficiente.



**2. Seguir a abertura do canal**



Ver os registos do Phoenixd:



```bash
journalctl -u phoenixd -f
```



Verá a abertura do canal e a dedução automática das comissões de liquidez. As comissões variam de acordo com as condições Mempool Bitcoin, mas incluem sempre 1% de taxa de serviço mais a taxa Mining atual.



**3. Verificar o canal**



```bash
./phoenix-cli listchannels
```



Este comando apresenta os seus canais activos com o respetivo estado e saldo.



### Operações API completas



O Phoenixd expõe uma API REST na porta 9740 que permite :



**Operações básicas


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Importante para os custos




- Receção**: 1% + taxa Mining para liquidez automática
- Envio**: 0.4% de taxa de encaminhamento no Lightning Network



**Webhooks:** Os webhooks permitem que o Phoenixd **notifique automaticamente** seus aplicativos quando um evento ocorre (pagamento recebido, Invoice pago, canal aberto, etc.). Em vez de solicitar constantemente atualizações ao Phoenixd, seu aplicativo recebe uma notificação HTTP instantânea.



**A sua loja online recebe automaticamente uma notificação quando um cliente paga uma encomenda, permitindo a validação instantânea da transação.



Configuração em `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Aplicações avançadas



### Integrações LNURL



O Phoenixd suporta nativamente protocolos LNURL para integração avançada:



**LNURL-Pay:** Pagar por serviços compatíveis com LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Recuperar fundos dos serviços LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Autenticação via Lightning para aceder aos serviços


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integração com LNbits



A LNbits pode utilizar o Phoenixd como fonte de financiamento, de acordo com a sua [documentação oficial] (https://docs.lnbits.org/guide/wallets.html):



**Configuração de LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Esta integração permite-lhe criar subcontas LNbits alimentadas pelo seu nó Phoenixd, fornecendo um Interface baseado na Web para gerir várias carteiras Lightning.



### Aplicações personalizadas



Graças à sua API REST abrangente, pode desenvolver aplicações :



**Comércio eletrónico:** Integração direta de pagamentos Lightning na sua loja


**Serviços de donativos:** Sistemas de donativos com facturas e webhooks automáticos


**Bots de redes sociais:** Bots do Telegram/Discord com funções de dicas


**Paywall Lightning:** Conteúdo premium disponível por uma taxa Lightning



## Segurança e boas práticas



### Proteção do acesso



**Senhas de API:** As senhas geradas automaticamente são as chaves do seu tesouro Lightning. Nunca as compartilhe e altere-as em caso de dúvida.



**Firewall:** Nunca deixe a porta 9740 aberta diretamente para a Internet. Utilizar sempre o nginx com HTTPS.



**Autenticação melhorada:** Considere uma VPN ou Tailscale para restringir o acesso ao seu servidor apenas a dispositivos autorizados.



### Cópias de segurança essenciais



**Recuperação do seed:** Guarde as suas 12 palavras num local seguro, fora do servidor. Esta é a sua única garantia de recuperação.



*diretório ~/.phoenix:** Faça backup desta pasta regularmente (após o Phoenixd ter sido desligado) para preservar o status do canal e acelerar a restauração.



**Códigos de recuperação de serviços:** Guarde também os códigos de segurança de todos os serviços em que activou a 2FA com o seu Phoenix.



### Controlo e manutenção



**Registos de controlo:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Actualizações:** Ver [GitHub releases](https://github.com/ACINQ/phoenixd/releases) para novas versões. A atualização é tão simples como substituir o binário e reiniciar o serviço.



## Comparação com alternativas



### Phoenixd vs Phoenix standard



**Norma Fénix (móvel) :**




- instalação imediata, configuração zero
- ✅ Interface móvel intuitivo
- a mesma gravação automática do Phoenixd
- sem API para programadores
- sem acesso a registos detalhados



**Phoenixd (servidor) :**




- aPI HTTP para integrações
- acesso total aos registos
- infra-estruturas pessoais
- requer competências técnicas
- necessidade de manutenção do servidor



**Ambos utilizam o ACINQ como seu LSP para liquidez automática.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- controlo total, protocolo Lightning completo
- grande comunidade, ecossistema maduro
- gestão manual complexa da liquidez
- grande curva de aprendizagem



**Phoenixd :**




- gestão automática da liquidez (como a Phoenix mobile)
- aPI para programadores
- configuração simplificada
- utiliza o ACINQ como LSP (sem encaminhamento independente)
- menos flexível do que os nós completos



## Resolução de problemas comuns



### Problemas de acesso à API



**A autenticação falhou" erro:**


1. Verifique a palavra-passe no ficheiro `~/.phoenix/phoenix.conf`


2. Verificar o formato de autenticação `-u:password`


3. Certifique-se de que o Phoenixd está em execução (`./phoenix-CLI getinfo`)



**Tempo limite de ligação:**




- Verifique se o Phoenixd está escutando na porta correta (9740)
- Teste o acesso local antes de configurar o HTTPS
- Verificar os registos: `journalctl -u phoenixd -f`



### Problemas de liquidez



**Os pagamentos não estão a chegar :**


1. Verificar se o montante excede o limiar mínimo (~30k Sats)


2. Consultar os registos para identificar erros de canal


3. Reiniciar o Phoenixd, se necessário



**Saldo em "crédito de despesas":**


Os pagamentos pequenos são armazenados como uma provisão. Receba uma quantia maior para ativar a abertura do canal e libertar estes fundos.



## Conclusão



O Phoenixd representa um excelente compromisso entre a facilidade de utilização e a soberania técnica para os programadores. Ele oferece uma API Lightning simples, mas poderosa, com gerenciamento automático de liquidez, eliminando a complexidade dos nós Lightning tradicionais.



Esta solução é particularmente adequada para programadores e empresas que pretendam :




- Integrar o Bitcoin Lightning nas suas aplicações
- Evitar a complexidade da gestão de canais Lightning
- Beneficiar de uma infraestrutura auto-hospedada
- Uma API simples e fiável



Com o Phoenixd, você constrói sua própria infraestrutura privada do Lightning com uma API REST moderna e gerenciamento automático de aspectos técnicos. É a solução ideal para democratizar a integração do Lightning em seus projetos.



## Recursos úteis



### Documentação oficial




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Código-fonte e versões
- Site do Servidor Phoenix**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Documentação completa
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Perguntas mais frequentes



### Apoio comunitário




- Problemas no GitHub** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Suporte técnico
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Notícias e anúncios