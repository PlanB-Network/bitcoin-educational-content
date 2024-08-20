---
term: LABEL (PAGOS SILENCIOSOS)
---

Dentro del protocolo de Pagos Silenciosos, las etiquetas son enteros utilizados para modificar la dirección estática inicial con el fin de crear muchas otras direcciones estáticas. El uso de estas etiquetas permite la segregación de pagos enviados a través de Pagos Silenciosos, empleando diferentes direcciones estáticas para cada uso, sin aumentar excesivamente la carga operativa para detectar estos pagos (escaneo). Bob utiliza una dirección estática $B$, compuesta por dos claves públicas: $B_{\text{scan}}$ para escanear y $B_{\text{spend}}$ para gastar. El hash de $b_{\text{scan}}$ y un entero $m$, multiplicado escalarmente por el punto generador $G$, se suma a la clave pública de gasto $B_{\text{spend}}$ para crear una especie de nueva clave pública de gasto $B_m$:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Por ejemplo, la primera clave $B_1$ se obtiene de esta manera:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

La dirección estática publicada por Bob ahora estará compuesta por $B_{\text{scan}}$ y $B_m$. Por ejemplo, la primera dirección estática con la etiqueta $1$ será:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Solo comenzamos desde la etiqueta $1$, porque la etiqueta $0$ está reservada para el cambio. Alice, que desea enviar bitcoins a la dirección estática etiquetada proporcionada por Bob, derivará la dirección de pago única $P_0$ usando el nuevo $B_1$ en lugar de $B_{\text{spend}}$:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

En realidad, Alice puede ni siquiera saber que Bob tiene una dirección etiquetada, ya que simplemente usa la segunda parte de la dirección estática que él proporcionó, que en este caso es el valor $B_1$ en lugar de $B_{\text{spend}}$. Para escanear pagos, Bob siempre usará el valor de su dirección estática inicial con $B_{\text{spend}}$ de esta manera:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Luego, simplemente restará el valor que encuentra para $P_0$ de cada salida una por una. Luego verifica si uno de los resultados de estas restas coincide con el valor de una de las etiquetas que usa en su billetera. Si coincide, por ejemplo, para la salida #4 con la etiqueta $1$, esto significa que esta salida es un Pago Silencioso asociado con su dirección estática etiquetada $B_1$:
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Esto funciona porque:
$$  B_1 = B_{\text{gasto}} + \text{hash}(b_{\text{escaneo}} \text{ ‖ } 1) \cdot G  $$
Gracias a este método, Bob puede usar una multitud de direcciones estáticas (con $B_1$, $B_2$, $B_3$...), todas derivadas de su dirección estática base ($B = B_{\text{escaneo}} \text{ ‖ } B_{\text{gasto}}$), con el fin de separar adecuadamente los usos.

Sin embargo, esta separación de direcciones estáticas solo es válida desde una perspectiva de gestión de cartera personal, pero no permite la separación de identidades. Dado que todas tienen el mismo $B_{\text{escaneo}}$, es muy fácil asociar todas las direcciones estáticas juntas y deducir que pertenecen a una única entidad.