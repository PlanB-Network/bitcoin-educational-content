---
term: ASSINATURA ADAPTADORA
---

Método criptográfico que permite combinar uma assinatura genuína com uma assinatura adicional (chamada de "assinatura adaptadora") para revelar um pedaço secreto de dados. Este método funciona de tal maneira que conhecer dois elementos entre a assinatura válida, a assinatura adaptadora e o segredo permite deduzir o terceiro elemento faltante. Uma das propriedades interessantes deste método é que, se conhecermos a assinatura adaptadora da nossa contraparte e o ponto específico na curva elíptica ligado ao segredo usado para calcular esta assinatura adaptadora, podemos então derivar nossa própria assinatura adaptadora que corresponderá com o mesmo segredo, sem nunca ter acesso direto ao segredo em si. Em uma troca entre duas partes que não confiam uma na outra, esta técnica permite a revelação simultânea de duas peças sensíveis de informação entre os participantes. Este processo elimina a necessidade de confiança em transações instantâneas como um Coin Swap ou um Atomic Swap. Vamos tomar um exemplo para entender melhor. Alice e Bob querem enviar um ao outro 1 BTC, mas eles não confiam um no outro. Eles vão, portanto, usar assinaturas adaptadoras para negar a necessidade de confiança na outra parte nesta troca (tornando-a assim uma troca "atômica"). Eles procedem da seguinte forma:
* Alice inicia esta troca atômica. Ela cria uma transação $m_A$ que envia 1 BTC para Bob. Ela cria uma assinatura $s_A$ que valida esta transação usando sua chave privada $p_A$ ($P_A = p_A \cdot G$), e usando um nonce $n_A$ e um segredo $t$ ($N_A = n_A \cdot G$ e $T = t \cdot G$): 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice calcula a assinatura adaptadora $s_A'$ a partir do segredo $t$ e sua assinatura real $s_A$:  
$$s_A' = s_A - t$$
&nbsp;
* Alice envia para Bob sua assinatura adaptadora $s_A'$, sua transação não assinada $m_A$, o ponto correspondente ao segredo $T$, e o ponto correspondente ao nonce $N_A$. Chamamos essas peças de informação de "adaptador". Note que com apenas essa informação, Bob não é capaz de recuperar os BTC de Alice.
* No entanto, Bob pode verificar que Alice não está o enganando. Para fazer isso, ele verifica se a assinatura adaptadora de Alice $s_A'$ corresponde à transação prometida $m_A$. Se a seguinte equação estiver correta, então ele está convencido de que a assinatura adaptadora de Alice é válida: 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Esta verificação fornece a Bob garantias de Alice, para que ele possa continuar o processo de troca atômica com tranquilidade. Ele então criará sua própria transação $m_B$ enviando 1 BTC para Alice e sua própria assinatura adaptadora $s_B'$, que estará ligada com o mesmo segredo $t$ que apenas Alice conhece por enquanto (Bob não conhece este valor $t$, mas apenas seu ponto correspondente $T$ que Alice forneceu a ele): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob envia para Alice sua assinatura adaptadora $s_B'$, sua transação não assinada $m_B$, o ponto correspondente ao segredo $T$ e o ponto correspondente ao nonce $N_B$. Alice agora pode combinar a assinatura adaptadora de Bob $s_B'$ com o segredo $t$, que apenas ela conhece, para calcular uma assinatura válida $s_B$ para a transação $m_B$ que envia o BTC de Bob para ela: $$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice transmite esta transação assinada $m_B$ na blockchain do Bitcoin para recuperar o BTC que Bob prometeu a ela. Bob fica sabendo desta transação na blockchain. Assim, ele consegue extrair a assinatura $s_B = s_B' + t$. Com essa informação, Bob pode isolar o famoso segredo $t$ de que precisava:
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* No entanto, esse segredo $t$ era a única informação que faltava para Bob produzir a assinatura válida $s_A$, a partir da assinatura adaptadora de Alice $s_A'$, que permitirá a ele validar a transação $m_A$ enviando um BTC de Alice para Bob. Ele então calcula $s_A$ e transmite a transação $m_A$ por sua vez: $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$