---
term: BIP0072

definition: Mở rộng URI Bitcoin với một tham số cho các yêu cầu thanh toán bảo mật của BIP70. Chưa bao giờ được áp dụng rộng rãi.
---
Completes BIP70 and BIP71 by defining the extension of Bitcoin URI (BIP21) with an additional parameter `r`. This parameter allows including a link to a secure payment request signed by the merchant's SSL certificate. When a client clicks on this extended URI, their wallet contacts the merchant's server to request payment details. These details are automatically filled in the wallet's transaction interface, and the client can be informed that they are paying the domain owner corresponding to the signing certificate (for example, "pandul.fr"). Since this enhancement is bundled with BIP70, it has never been widely adopted.