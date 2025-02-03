---
term: ASSINATURA DO ADAPTADOR

---
Método criptográfico que permite combinar uma assinatura genuína com uma assinatura adicional (denominada "assinatura adaptadora") para revelar um dado secreto. Este método funciona de tal forma que o conhecimento de dois elementos entre a assinatura válida, a assinatura adaptadora e o segredo permite deduzir o terceiro elemento em falta. Uma das propriedades interessantes deste método é que, se conhecermos a assinatura do adaptador da nossa contraparte e o ponto específico da curva elíptica ligado ao segredo utilizado para calcular esta assinatura do adaptador, podemos então derivar a nossa própria assinatura do adaptador que corresponderá ao mesmo segredo, sem nunca ter acesso direto ao próprio segredo. Numa troca entre duas partes interessadas que não confiam uma na outra, esta técnica permite a revelação simultânea de duas informações sensíveis entre os participantes. Este processo elimina a necessidade de confiança em transacções instantâneas, como uma troca de moedas ou uma troca atómica. Vejamos um exemplo para o compreender melhor. Alice e Bob querem enviar um ao outro 1 BTC, mas não confiam um no outro. Por conseguinte, utilizarão assinaturas de adaptadores para anular a necessidade de confiança na outra parte nesta troca (tornando-a assim uma troca "atómica"). Procedem da seguinte forma:


- Alice inicia esta troca atómica. Cria uma transação $m_A$ que envia 1 BTC ao Bob. Cria uma assinatura $s_A$ que valida esta transação utilizando a sua chave privada $p_A$ ($P_A = p_A \cdot G$), e utilizando um nonce $n_A$ e um segredo $t$ ($N_A = n_A \cdot G$ e $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \paralelo P_A \paralelo m_A) \cdot p_A$$

&nbsp;


- Alice calcula a assinatura do adaptador $s_A'$ a partir do segredo $t$ e da sua assinatura real $s_A$:

$$s_A' = s_A - t$$

&nbsp;


- Alice envia a Bob a sua assinatura adaptadora $s_A'$, a sua transação não assinada $m_A$, o ponto correspondente ao segredo $T$ e o ponto correspondente ao nonce $N_A$. Chamamos a estas peças de informação um "adaptador". Note-se que, apenas com esta informação, Bob não é capaz de recuperar as BTC de Alice.
- No entanto, Bob pode verificar que Alice não o está a enganar. Para isso, ele verifica se a assinatura do adaptador de Alice $s_A'$ corresponde à transação prometida $m_A$. Se a seguinte equação estiver correta, então ele está convencido de que a assinatura do adaptador de Alice é válida:

$$s_A' \cdot G = N_A + H(N_A + T \paralelo P_A \paralelo m_A) \cdot P_A$$

&nbsp;


- Esta verificação dá a Bob garantias de Alice, para que possa continuar o processo de troca atómica com tranquilidade. Criará então a sua própria transação $m_B$ enviando 1 BTC a Alice e a sua própria assinatura adaptadora $s_B'$, que será associada ao mesmo segredo $t$ que só Alice conhece por agora (Bob não conhece este valor $t$, mas apenas o seu ponto correspondente $T$ que Alice lhe forneceu): $$s_B' = n_B + H(N_B + T \paralelo P_B \paralelo m_B) \cdot p_B$$

&nbsp;


- Bob envia a Alice a sua assinatura adaptadora $s_B'$, a sua transação não assinada $m_B$, o ponto correspondente ao segredo $T$ e o ponto correspondente ao nonce $N_B$. Alice pode agora combinar a assinatura adaptadora de Bob $s_B'$ com o segredo $t$, que só ela conhece, para calcular uma assinatura válida $s_B$ para a transação $m_B$ que lhe envia o BTC de Bob:

$$s_B = s_B' + t$$

&nbsp;

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \paralelo P_B \paralelo m_B) \cdot P_B$$

&nbsp;


- Alice transmite esta transação assinada $m_B$ na blockchain da Bitcoin para recuperar as BTC que Bob lhe prometeu. Bob toma conhecimento desta transação na cadeia de blocos. Assim, consegue extrair a assinatura $s_B = s_B' + t$. A partir desta informação, Bob pode isolar o famoso segredo $t$ de que precisava:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$

&nbsp;


- No entanto, este segredo $t$ era a única informação que faltava para Bob produzir a assinatura válida $s_A$, a partir da assinatura adaptadora de Alice $s_A'$, que lhe permitirá validar a transação $m_A$ enviando um BTC de Alice para Bob. Calcula então $s_A$ e transmite a transação $m_A$ por sua vez: $$s_A = s_A' + t$$

&nbsp;

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \paralelo P_A \paralelo m_A) \cdot P_A$$