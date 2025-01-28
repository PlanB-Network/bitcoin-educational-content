---
term: BIP72

---
Completa BIP70 y BIP71 definiendo la extensión de Bitcoin URI (BIP21) con un parámetro adicional `r`. Este parámetro permite incluir un enlace a una solicitud de pago seguro firmada por el certificado SSL del comerciante. Cuando un cliente hace clic en este URI extendido, su monedero contacta con el servidor del comerciante para solicitar los detalles del pago. Estos detalles se rellenan automáticamente en la interfaz de transacciones del monedero, y se puede informar al cliente de que está pagando al propietario del dominio correspondiente al certificado de firma (por ejemplo, "pandul.fr"). Como esta mejora está incluida en el BIP70, nunca se ha generalizado.