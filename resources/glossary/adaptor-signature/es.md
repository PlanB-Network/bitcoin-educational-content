---
term: FIRMA DEL ADAPTADOR

---
Método criptográfico que permite combinar una firma auténtica con una firma adicional (denominada "firma adaptadora") para revelar un dato secreto. Este método funciona de tal manera que conocer dos elementos entre la firma válida, la firma adaptadora y el secreto permite deducir el tercer elemento que falta. Una de las propiedades interesantes de este método es que si conocemos la firma del adaptador de nuestra contraparte y el punto específico de la curva elíptica vinculado al secreto utilizado para calcular esta firma del adaptador, podemos deducir nuestra propia firma del adaptador que coincidirá con el mismo secreto, sin tener nunca acceso directo al propio secreto. En un intercambio entre dos partes interesadas que no confían la una en la otra, esta técnica permite desvelar simultáneamente dos informaciones sensibles entre los participantes. Este proceso elimina la necesidad de confianza en transacciones instantáneas como un intercambio de monedas o un intercambio atómico. Pongamos un ejemplo para entenderlo mejor. Alice y Bob quieren enviarse mutuamente 1 BTC, pero no confían el uno en el otro. Por lo tanto, utilizarán firmas adaptadoras para anular la necesidad de confiar en la otra parte en este intercambio (convirtiéndolo así en un intercambio "atómico"). Proceden de la siguiente manera:


- Alice inicia este intercambio atómico. Crea una transacción $m_A$ que envía 1 BTC a Bob. Crea una firma $s_A$ que valida esta transacción usando su clave privada $p_A$ ($P_A = p_A \cdot G$), y usando un nonce $n_A$ y un secreto $t$ ($N_A = n_A \cdot G$ y $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \paralelo P_A \paralelo m_A) \cdot p_A$$

&nbsp;


- Alice calcula la firma del adaptador $s_A'$ a partir del secreto $t$ y su firma real $s_A$:

$$s_A' = s_A - t$$

&nbsp;


- Alice envía a Bob su firma adaptadora $s_A'$, su transacción sin firma $m_A$, el punto correspondiente al secreto $T$, y el punto correspondiente al nonce $N_A$. A estas piezas de información las llamamos "adaptador". Ten en cuenta que sólo con esta información, Bob no es capaz de recuperar el BTC de Alice.
- Sin embargo, Bob puede verificar que Alice no le está engañando. Para ello, comprueba que la firma $s_A'$ del adaptador de Alice coincide con la transacción prometida $m_A$. Si la siguiente ecuación es correcta, entonces está convencido de que la firma del adaptador de Alice es válida:

$$s_A' \cdot G = N_A + H(N_A + T \paralelo P_A \paralelo m_A) \cdot P_A$$

&nbsp;


- Esta verificación proporciona a Bob garantías de Alice, para que pueda continuar el proceso de intercambio atómico con tranquilidad. A continuación, creará su propia transacción $m_B$ enviando 1 BTC a Alice y su propia firma adaptadora $s_B'$, que estará vinculada con el mismo secreto $t$ que sólo Alice conoce por ahora (Bob no conoce este valor $t$, sino sólo su punto correspondiente $T$ que Alice le ha proporcionado): $$s_B' = n_B + H(N_B + T \paralelo P_B \paralelo m_B) \cdot p_B$$

&nbsp;


- Bob envía a Alice su firma adaptadora $s_B'$, su transacción sin firma $m_B$, el punto correspondiente al secreto $T$, y el punto correspondiente al nonce $N_B$. Alice puede ahora combinar la firma adaptadora $s_B'$ de Bob con el secreto $t$, que sólo ella conoce, para calcular una firma válida $s_B$ para la transacción $m_B$ que le envía el BTC de Bob:

$$s_B = s_B' + t$$

&nbsp;

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \paralelo P_B \paralelo m_B) \cdot P_B$$

&nbsp;


- Alice difunde esta transacción firmada $m_B$ en la blockchain de Bitcoin para recuperar los BTC que Bob le prometió. Bob se entera de esta transacción en la blockchain. Así puede extraer la firma $s_B = s_B' + t$. A partir de esta información, Bob puede aislar el famoso secreto $t$ que necesitaba:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$

&nbsp;


- Sin embargo, este secreto $t$ era la única información que le faltaba a Bob para producir la firma válida $s_A$, a partir de la firma adaptadora $s_A'$ de Alice, que le permitirá validar la transacción $m_A$ enviando un BTC de Alice a Bob. Entonces calcula $s_A$ y transmite la transacción $m_A$ a su vez: $$s_A = s_A' + t$$

&nbsp;

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \paralelo P_A \paralelo m_A) \cdot P_A$$