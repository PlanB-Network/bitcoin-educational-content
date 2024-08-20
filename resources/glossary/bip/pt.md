---
termo: BIP
---

Acrônimo para "Proposta de Melhoria do Bitcoin" (Bitcoin Improvement Proposal). Uma Proposta de Melhoria do Bitcoin (BIP) é um processo formal para propor e documentar melhorias e alterações no protocolo do Bitcoin e seus padrões. Como o Bitcoin não possui uma entidade central para decidir sobre atualizações, os BIPs permitem que a comunidade sugira, discuta e implemente melhorias de maneira estruturada e transparente. Cada BIP detalha os objetivos da melhoria proposta, as justificativas, os potenciais impactos na compatibilidade, bem como as vantagens e desvantagens. BIPs podem ser escritos por qualquer membro da comunidade, mas devem ser aprovados por outros desenvolvedores e pelos editores que mantêm o banco de dados do GitHub do Bitcoin Core: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun e Ruben Somsen. No entanto, é importante entender que o papel desses indivíduos na edição dos BIPs não significa que eles controlam o Bitcoin. Se alguém propõe uma melhoria que não é aceita dentro do framework formal do BIP, ainda pode apresentá-la diretamente à comunidade do Bitcoin ou até criar um fork incluindo sua modificação. A vantagem do processo BIP reside em sua formalidade e centralização, que facilitam o debate para evitar divisão entre os usuários do Bitcoin, buscando implementar atualizações de maneira consensual. No final, é o princípio da maioria econômica que determina as dinâmicas de poder dentro do protocolo.

Os BIPs são classificados em três categorias principais:
* *BIPs de Rastreamento de Padrões*: Concernem modificações que afetam diretamente as implementações do Bitcoin, como regras de validação de transações e blocos;
* *BIPs Informativos*: Fornecem informações ou recomendações sem propor mudanças diretas no protocolo;
* *BIPs de Processo*: Descrevem mudanças nos procedimentos em torno do Bitcoin, como processos de governança.

BIPs de Rastreamento de Padrões e Informativos também são classificados por "Camada":
* *Camada de Consenso*: BIPs nesta camada dizem respeito às regras de consenso do Bitcoin, como modificações nas regras de validação de blocos ou transações. Essas propostas podem ser tanto soft forks (modificações compatíveis com versões anteriores) quanto hard forks (modificações não compatíveis com versões anteriores). Por exemplo, os BIPs para SegWit e Taproot pertencem a esta categoria;
* *Serviços Peer*: Esta camada diz respeito à operação da rede de nós do Bitcoin, isto é, como os nós encontram e se comunicam entre si na Internet.
* *API/RPC*: Os BIPs desta camada dizem respeito às Interfaces de Programação de Aplicativos (API) e Chamadas de Procedimento Remoto (RPC) que permitem que o software do Bitcoin interaja com os nós;
* *Camada de Aplicações*: Esta camada pertence a aplicações construídas em cima do Bitcoin. Os BIPs nesta categoria geralmente lidam com modificações no nível dos padrões de carteiras do Bitcoin.

O processo de submissão de um BIP começa com a conceitualização e discussão da ideia na lista de e-mails *Bitcoin-dev*. Se a ideia for promissora, o autor elabora um BIP seguindo um formato específico e o submete via Pull Request no repositório Core do GitHub. Os editores revisam esta proposta para verificar se ela atende a todos os critérios. O BIP deve ser tecnicamente viável, benéfico para o protocolo, cumprir com o formato requerido e estar de acordo com a filosofia do Bitcoin. Se o BIP atender a essas condições, é oficialmente integrado ao repositório do GitHub de BIPs. Em seguida, é atribuído um número. Esse número é geralmente decidido pelo editor, muitas vezes Luke Dashjr, e é atribuído de forma lógica: BIPs que lidam com assuntos semelhantes frequentemente recebem números consecutivos.

Os BIPs então passam por diferentes status ao longo de seu ciclo de vida. O status atual é especificado no cabeçalho de cada BIP:
* Rascunho: A proposta ainda está na fase de elaboração e debate;
* Proposto: O BIP é considerado completo e pronto para revisão pela comunidade;
* Adiado: O BIP é colocado em espera para o futuro pelo campeão ou um editor;
* Rejeitado: Um BIP é classificado como rejeitado se não apresentou atividade por 3 anos. Seu autor pode optar por retomá-lo mais tarde, o que permitiria que ele voltasse ao status de rascunho;
* Retirado: O BIP foi retirado pelo seu autor;
* Final: O BIP é aceito e amplamente implementado no Bitcoin;
* Ativo: Apenas para BIPs de processo, este status é atribuído uma vez que um certo consenso é alcançado;
* Substituído / Obsoleto: O BIP não é mais aplicável ou foi substituído por uma proposta mais recente que o torna desnecessário.

![](../../dictionnaire/assets/25.png)

> ► *BIP é a sigla para "Bitcoin Improvement Proposal" (Proposta de Melhoria do Bitcoin). No entanto, a maioria dos textos em português usa diretamente a sigla "BIP" como um substantivo comum.*