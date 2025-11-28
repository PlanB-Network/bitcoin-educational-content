---
name: Macadâmia Wallet
description: Cashu mobile wallet para pagamentos BTC anónimos e instantâneos
---

![cover](assets/cover.webp)



O Macadamia Wallet é um wallet móvel iOS que implementa o protocolo Cashu, um sistema de ecash Chaumian que permite pagamentos Bitcoin totalmente anónimos. Graças às assinaturas cegas, nenhum observador pode associar os seus depósitos às suas despesas, oferecendo uma confidencialidade semelhante à do dinheiro físico.



Neste tutorial, veremos como instalar e configurar o Macadamia, realizar as suas primeiras transacções Cashu (Mint, Send, Receive, Melt) e gerir vários mints para garantir os seus fundos.



## O que é a Macadâmia Wallet?



### O protocolo Cashu



A Cashu utiliza assinaturas cegas inventadas por David Chaum: o utilizador deposita bitcoins num servidor "mint", que emite tokens equivalentes em satoshis. A casa da moeda assina estes tokens sem ver o seu conteúdo, tornando impossível associar um token a um utilizador. As trocas são off-chain, peer-to-peer, e totalmente opacas - nem mesmo a casa da moeda consegue saber quem está a pagar a quem.



Macadamia é um wallet iOS de código aberto desenvolvido em Swift/SwiftUI. Funciona sem conta ou KYC, os seus tokens são armazenados localmente e protegidos por uma frase seed. O código é auditável no GitHub e os tokens são interoperáveis com outras carteiras Cashu (Minibits, Cashu.me).



### Modelo de custódia e compromisso



**Importante**: A Cashu opera num modelo de custódia. As fichas são promessas de pagamento (IOUs) apoiadas pelas reservas Bitcoin da casa da moeda. Se a casa da moeda desaparecer, os seus tokens perdem o seu valor. Este é o compromisso para a máxima confidencialidade.



Utilizar a Macadâmia como um wallet físico: apenas pequenas quantidades. Distribua os seus fundos por várias casas da moeda para diluir o risco.



## Principais caraterísticas



Macadamia implementa as quatro operações fundamentais do protocolo Cashu. **Mint** converte os seus satoshis em tokens através de uma fatura Lightning. **Enviar** permite-lhe enviar tokens gratuitamente através de código QR ou link, completamente off-chain. **Receber** permite-lhe receber tokens ou generate uma fatura Lightning. **Derreter paga uma fatura relâmpago destruindo os seus tokens.



O wallet suporta a gestão de várias casas da moeda em simultâneo. É possível trocar tokens entre diferentes casas da moeda via Lightning.



## Plataformas suportadas



A Macadamia está disponível apenas no iOS 17 ou superior para iPhone e iPad. A aplicação nativa Swift/SwiftUI oferece uma integração óptima com o ecossistema Apple.



O protocolo Cashu garante a interoperabilidade entre as carteiras. Pode restaurar a sua frase seed noutras aplicações, como o Minibits no Android ou o Nutstash no computador.



A versão atual é distribuída através do TestFlight. Utilize apenas pequenas quantidades com esta versão beta.



## Instalação



O Macadamia está atualmente disponível através do TestFlight, o programa de testes beta da Apple. Veja como instalá-lo:



### Instalação através do TestFlight



**Passo 1: Descarregar o TestFlight



Se ainda não tiver a aplicação TestFlight no seu dispositivo, procure por "TestFlight" na App Store e instale-a. O TestFlight é a aplicação oficial da Apple para testar versões beta de aplicações iOS.



**Passo 2: aderir ao programa Macadamia beta** (em francês)



Quando o TestFlight estiver instalado, siga esta ligação de convite a partir do seu iPhone ou iPad: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



A ligação abrirá automaticamente o TestFlight e propor-lhe-á a instalação do Macadamia Wallet. Toque em "Aceitar" e depois em "Instalar" para iniciar a transferência. A aplicação pesa cerca de dez megabytes e demora apenas alguns segundos a instalar.



![Installation TestFlight](assets/fr/01.webp)



### Informações importantes sobre as versões beta



O Macadamia ainda se encontra em fase de desenvolvimento ativo. As versões TestFlight são actualizadas frequentemente e podem introduzir novas funcionalidades ou corrigir erros. No entanto, como em qualquer versão beta, podem ocorrer problemas de funcionamento. **Recomendamos vivamente que utilize apenas pequenas quantidades**, que aceita poderem ser perdidas no caso de um problema técnico.



O Macadamia não recolhe quaisquer dados do utilizador de acordo com a política de privacidade apresentada. Certifique-se de que o programador é cypherbase UG aquando da instalação.



## Configuração inicial



No primeiro lançamento, o Macadamia gera uma frase BIP-39 com 12 palavras. Anote-as num local seguro - nunca como uma captura de ecrã. Estas palavras permitem-lhe recriar o seu wallet e gastar os seus tokens.



![Configuration initiale](assets/fr/02.webp)



Siga as quatro etapas: boas-vindas, aceitar as condições, guardar a frase seed e confirmação final.



![Interface principale](assets/fr/03.webp)



Uma vez concluída a configuração, o Macadamia apresenta três separadores principais. **Wallet** mostra o seu saldo e o histórico de transacções. **Mints** permite-lhe gerir os seus servidores Cashu. **Configurações** dá acesso às configurações e à sua frase seed.



![Ajout d'un mint](assets/fr/04.webp)



Agora precisas de configurar um mint, ou seja, um servidor Cashu que irá emitir os teus tokens. Vá para o separador "Mints" (Casas da Moeda), toque em "Add new Mint URL" (Adicionar novo URL da Casa da Moeda) e introduza o endereço da casa da moeda escolhida (por exemplo, mint.cubabitcoin.org). Consulte bitcoinmints.com ou cashu.space para conhecer as casas da moeda públicas com boa reputação. Valide apenas as casas da moeda cuja reputação tenha verificado, uma vez que elas terão a custódia dos seus satoshis.



## Utilização diária



### Criação de novos tokens (Mint)



Para alimentar o seu wallet Macadamia com ecash, é necessário efetuar uma operação "Mint" (para criar fichas). Toque em "Receber" e escolha a opção "Relâmpago". Introduza o montante pretendido (por exemplo, 1000 sats), selecione a moeda a utilizar e, em seguida, generate a fatura Lightning.



![Opération Mint](assets/fr/05.webp)



Pague a fatura relâmpago gerada com o seu wallet habitual (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Os tokens Cashu aparecem instantaneamente no seu saldo após o pagamento.



### Enviar tokens



Para enviar fichas Cashu a outro utilizador, toque no botão "Enviar" no ecrã principal e selecione "Ecash". Introduza o montante a enviar (por exemplo, 50 sats) e acrescente uma nota descritiva, se necessário.



![Envoi Ecash](assets/fr/07.webp)



Partilhe o código QR ou o texto gerado através do iMessage, Signal ou Telegram. O destinatário recebe os fundos de forma instantânea e gratuita.



### Receber fichas



Para receber tokens Cashu enviados por outro utilizador, toque em "Receber" e selecione "Ecash". Digitalize o código QR do token ou cole a hiperligação do token que recebeu.



![Réception Ecash](assets/fr/08.webp)



Toque em "Redeem" para reivindicar token.



### Pagamentos relâmpago (derreter)



Para pagar uma fatura Lightning com os seus tokens Cashu, toque em "Enviar" e selecione "Lightning". Cole a fatura BOLT11 que deseja pagar.



![Paiement Lightning](assets/fr/11.webp)



A casa da moeda destrói os seus tokens e executa o pagamento Lightning. Assim, pode pagar por qualquer serviço Lightning preservando o seu anonimato.



### Trocar entre balas



Quando recebe tokens de uma casa da moeda que não configurou, o Macadamia oferece-lhe várias opções para gerir esses tokens.



![Swap inter-mints](assets/fr/09.webp)



Adicione a nova casa da moeda ou troque os tokens por uma casa da moeda existente. A troca utiliza o Lightning como ponte para transferir os seus fundos de forma anónima.



### Gestão avançada de várias moedas



A Macadamia oferece ferramentas sofisticadas para gerir várias casas da moeda em simultâneo e afetar estrategicamente os seus fundos.



![Gestion multi-mints](assets/fr/10.webp)



"Distribuir fundos" distribui automaticamente o seu saldo de acordo com percentagens (por exemplo, 50/50). "Transferir" permite transferências manuais entre casas da moeda para diversificar os seus riscos.



## Vantagens e limitações



**Destaques** :





- Máxima confidencialidade**: Transacções não rastreáveis, mesmo pela casa da moeda. Sem metadados de blockchain, trocas peer-to-peer sem rasto.
- Rápido e gratuito**: Transferências instantâneas gratuitas dentro de uma casa da moeda, ideais para micropagamentos.
- Interoperabilidade**: tokens Cashu padronizados para uso com outras carteiras compatíveis (Minibits, Nutstash).
- Simplicidade**: O Interface iOS nativo é acessível a principiantes, mantendo-se auditável (código aberto).



**Restrições** :





- Modelo de custódia**: é necessária a confiança da casa da moeda. Se uma casa da moeda desaparecer, as suas fichas perdem o seu valor.
- apenas iOS**: Não há versão para Android/desktop. A interoperabilidade Cashu permite o acesso através de outras carteiras, mas a experiência ideal continua a ser iOS.
- Dependência da Mint**: Mint offline = incapaz de efetuar transacções que exijam a sua intervenção (Mint, Melt).
- Tecnologia emergente** : Desenvolvimento ativo, possíveis erros, normas em evolução.



## Melhores práticas





- Diversifique as suas moedas**: Distribua as suas fichas por várias casas da moeda com boa reputação para diluir o risco.
- Limite de montantes**: Utilize o Macadamia como um wallet físico para pagamentos diários e não como um cofre.
- Proteja o seu seed**: Guarde a sua frase de 12 palavras num papel e num local seguro. Teste a restauração ocasionalmente.
- Verificar os rebuçados**: Consulte cashu.space e os fóruns da comunidade antes de adicionar um mint. Escolha aqueles com um bom tempo de atividade e uma reputação sólida.
- VPN ou Tor**: Oculte o seu IP com VPN/Tor para maximizar a privacidade da rede.
- Junta-te à comunidade**: Grupos Cashu do Telegram/Discord para actualizações, recomendações de hortelã e melhores práticas.



## Conclusão



O Macadamia Wallet traz as propriedades do dinheiro físico para o Bitcoin digital. Ao combinar as assinaturas cegas Chaum e Lightning, oferece uma solução elegante para a confidencialidade das transacções. A sua interface nativa para iOS torna acessível a tecnologia criptográfica sofisticada, mantendo-se em código aberto e interoperável com o ecossistema Cashu.



O modelo de custódia exige vigilância e boas práticas de segurança. Utilizada corretamente, a Macadamia torna-se uma ferramenta valiosa para pagamentos quotidianos que exijam anonimato, complementando as carteiras de poupança sem custódia.



## Recursos



### Documentação oficial




- Sítio Web oficial: [macadamia.cash](https://macadamia.cash)
- Perguntas frequentes sobre a macadâmia: [macadamia.cash/faq](https://macadamia.cash/faq)
- Código-fonte do GitHub: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Documentação Cashu




- Documentação técnica: [docs.cashu.space](https://docs.cashu.space)
- Lista de casas da moeda públicas: [bitcoinmints.com](https://bitcoinmints.com)
- Sítio Web oficial do protocolo: [cashu.space](https://cashu.space)



### Comunidade




- Telegrama do grupo Cashu: [t.me/cashu_ecash](https://t.me/cashu_ecash)