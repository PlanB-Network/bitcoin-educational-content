---
term: PIF

---
Acrónimo de "Bitcoin Improvement Proposal" Uma Proposta de Melhoria do Bitcoin (BIP) é um processo formal para propor e documentar melhorias e mudanças no protocolo Bitcoin e seus padrões. Uma vez que a Bitcoin não tem uma entidade central para decidir sobre as actualizações, as BIPs permitem que a comunidade sugira, discuta e implemente melhorias de uma forma estruturada e transparente. Cada BIP detalha os objectivos da melhoria proposta, as justificações, os potenciais impactos na compatibilidade, bem como as vantagens e desvantagens. Os BIPs podem ser escritos por qualquer membro da comunidade, mas devem ser aprovados por outros desenvolvedores e pelos editores que mantêm o banco de dados do Bitcoin Core GitHub: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun e Ruben Somsen. No entanto, é importante compreender que o papel destes indivíduos na edição de PIFs não significa que controlam o Bitcoin. Se alguém propuser uma melhoria que não seja aceite no âmbito do quadro formal das PIF, pode ainda assim apresentá-la diretamente à comunidade Bitcoin ou mesmo criar um fork que inclua a sua modificação. A vantagem do processo BIP reside na sua formalidade e centralização, que facilitam o debate para evitar divisões entre os utilizadores de Bitcoin, procurando implementar actualizações de forma consensual. No final, é o princípio da maioria económica que determina a dinâmica de poder dentro do protocolo.

Os PIF são classificados em três categorias principais:


- BIPs* da trilha de padrões: Dizem respeito a modificações que afectam diretamente as implementações Bitcoin, tais como regras de validação de transacções e blocos;
- PIFs informativos*: Fornecem informações ou recomendações sem propor alterações diretas ao protocolo;
- Processar BIPs*: Descrever as alterações nos procedimentos que envolvem a Bitcoin, tais como os processos de governação.

As PIF da faixa de normas e as PIF informativas também são classificadas por "Camada":


- Camada de consenso*: As BIPs nesta camada dizem respeito às regras de consenso da Bitcoin, tais como modificações nas regras de validação de blocos ou transacções. Estas propostas podem ser soft forks (modificações compatíveis com as versões anteriores) ou hard forks (modificações não compatíveis com as versões anteriores). Por exemplo, os BIPs para SegWit e Taproot pertencem a esta categoria;
- Serviços de Pares*: Esta camada diz respeito à operação da rede de nós do Bitcoin, ou seja, como os nós se encontram e se comunicam uns com os outros na Internet.
- API/RPC*: As BIPs desta camada dizem respeito às interfaces de programação de aplicações (API) e às chamadas de procedimento remoto (RPC) que permitem ao software Bitcoin interagir com os nós;
- Camada de aplicações*: Esta camada diz respeito a aplicações construídas em cima da Bitcoin. As PIFs nesta categoria normalmente lidam com modificações no nível dos padrões da carteira Bitcoin.

O processo de submissão de um BIP começa com a concetualização e discussão da ideia na lista de discussão *Bitcoin-dev*. Se a ideia for promissora, o autor redige um PIF seguindo um formato específico e submete-o através de um Pull Request no repositório Core GitHub. Os editores analisam esta proposta para verificar se cumpre todos os critérios. O BIP deve ser tecnicamente viável, benéfico para o protocolo, cumprir a formatação exigida e estar de acordo com a filosofia do Bitcoin. Se a PIF cumprir estas condições, é oficialmente integrada no repositório de PIFs do GitHub. É-lhe então atribuído um número. Este número é geralmente decidido pelo editor, muitas vezes Luke Dashjr, e é atribuído de forma lógica: As PIFs que tratam de assuntos semelhantes recebem frequentemente números consecutivos.

As PIF passam então por diferentes estados ao longo do seu ciclo de vida. O estado atual é especificado no cabeçalho de cada PIF:


- Projeto: A proposta está ainda em fase de redação e debate;
- Proposta: O PIF é considerado completo e está pronto para ser revisto pela comunidade;
- Adiado: A PIF é colocada em espera para mais tarde pelo defensor ou por um editor;
- Rejeitado: Um PIF é classificado como rejeitado se não tiver apresentado qualquer atividade durante 3 anos. O seu autor pode optar por retomá-lo mais tarde, o que lhe permitiria voltar ao estatuto de projeto;
- Retirado: O PIF foi retirado pelo seu autor;
- Final: O BIP é aceite e amplamente implementado na Bitcoin;
- Ativo: Apenas para os PIF de processo, este estatuto é atribuído quando se atinge um determinado consenso;
- Substituído / Obsoleto: O PIF já não é aplicável ou foi substituído por uma proposta mais recente que o torna desnecessário.

![](../../dictionnaire/assets/25.webp)

> ► *BIP é o acrónimo de "Bitcoin Improvement Proposal". Em francês, pode ser traduzido como "Proposition d'amélioration de Bitcoin". No entanto, a maioria dos textos franceses utiliza diretamente a sigla "BIP" como um substantivo comum, por vezes feminino, por vezes masculino*