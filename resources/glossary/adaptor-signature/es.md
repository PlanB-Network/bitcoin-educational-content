---
term: ADAPTOR SIGNATURE
---

Método criptográfico que permite combinar una firma genuina con una firma adicional (llamada "firma adaptadora") para revelar un dato secreto. Este método funciona de tal manera que conocer dos elementos entre la firma válida, la firma adaptadora y el secreto permite deducir el tercer elemento faltante. Una de las propiedades interesantes de este método es que si conocemos la firma adaptadora de nuestra contraparte y el punto específico en la curva elíptica vinculado al secreto utilizado para calcular esta firma adaptadora, podemos entonces derivar nuestra propia firma adaptadora que coincidirá con el mismo secreto, sin tener nunca acceso directo al secreto en sí. En un intercambio entre dos partes que no confían entre sí, esta técnica permite la revelación simultánea de dos piezas de información sensible entre los participantes. Este proceso elimina la necesidad de confianza en transacciones instantáneas como un Coin Swap o un Atomic Swap. Tomemos un ejemplo para entenderlo mejor. Alice y Bob quieren enviarse mutuamente 1 BTC, pero no confían el uno en el otro. Por lo tanto, utilizarán firmas adaptadoras para negar la necesidad de confianza en la otra parte en este intercambio (haciéndolo así un intercambio "atómico"). Proceden de la siguiente manera:
* Alice inicia este intercambio atómico. Ella crea una transacción $m_A$ que envía 1 BTC a Bob. Ella crea una firma $s_A$ que valida esta transacción usando su clave privada $p_A$ ($P_A = p_A \cdot G$), y usando un nonce $n_A$ y un secreto $t$ ($N_A = n_A \cdot G$ y $T = t \cdot G$): 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice calcula la firma adaptadora $s_A'$ a partir del secreto $t$ y su firma real $s_A$:  
$$s_A' = s_A - t$$
&nbsp;
* Alice envía a Bob su firma adaptadora $s_A'$, su transacción sin firmar $m_A$, el punto correspondiente al secreto $T$, y el punto correspondiente al nonce $N_A$. Llamamos a estas piezas de información un "adaptador". Note que con solo esta información, Bob no es capaz de recuperar los BTC de Alice.
* Sin embargo, Bob puede verificar que Alice no lo está engañando. Para hacer esto, él verifica que la firma adaptadora de Alice $s_A'$ coincide con la transacción prometida $m_A$. Si la siguiente ecuación es correcta, entonces él está convencido de que la firma adaptadora de Alice es válida: 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Esta verificación proporciona a Bob garantías de Alice, para que pueda continuar el proceso de intercambio atómico con tranquilidad. Luego, él creará su propia transacción $m_B$ enviando 1 BTC a Alice y su propia firma adaptadora $s_B'$, que estará vinculada con el mismo secreto $t$ que solo Alice conoce por ahora (Bob no conoce este valor $t$, pero solo su punto correspondiente $T$ que Alice le ha proporcionado): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob le envía a Alice su firma adaptadora $s_B'$, su transacción sin firmar $m_B$, el punto correspondiente al secreto $T$ y el punto correspondiente al nonce $N_B$. Alice ahora puede combinar la firma adaptadora de Bob $s_B'$ con el secreto $t$, que solo ella conoce, para calcular una firma válida $s_B$ para la transacción $m_B$ que le envía los BTC de Bob: $$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice transmite esta transacción firmada $m_B$ en la blockchain de Bitcoin para recuperar los BTC que Bob le prometió. Bob se entera de esta transacción en la blockchain. Así, es capaz de extraer la firma $s_B = s_B' + t$. A partir de esta información, Bob puede aislar el famoso secreto $t$ que necesitaba:
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Sin embargo, este secreto $t$ era la única información que faltaba para que Bob produjera la firma válida $s_A$, a partir de la firma adaptadora de Alice $s_A'$, lo que le permitirá validar la transacción $m_A$ enviando un BTC de Alice a Bob. Luego calcula $s_A$ y transmite la transacción $m_A$ a su vez: $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$