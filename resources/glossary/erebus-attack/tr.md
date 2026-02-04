---
term: Erebus saldırısı
definition: Kötü niyetli bir İnternet Servis Sağlayıcısının bir Bitcoin düğümünü ağdan izole etmesine olanak tanıyan saldırı.
---

A highly sophisticated form of attack against the Bitcoin network that allows a malicious Internet Service Provider to isolate specific Bitcoin nodes. Thus, it is a form of Eclipse attack. The Erebus attack exploits the structure of the Internet network, particularly the mandatory passage points (or "bottlenecks") in the routing between Autonomous Systems (AS). An attacker, by controlling an autonomous system, can manipulate network traffic to isolate a Bitcoin node from the rest of the network, thereby making it believe in a false state of the Blockchain (blocks or transactions not known by the node). This isolation can lead to double spending or censorship against the isolated node. This attack has been made much more difficult since the release of Bitcoin core version 0.20.0 and the introduction of Asmap.