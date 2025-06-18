---
term: OFFER
---

Dans le cadre de BOLT12, les « *offers* » sont des QR codes statiques pour effectuer plusieurs paiements sur le Lightning Network. Contrairement aux invoices classiques, les *offers* peuvent être réutilisées. Elles permettent de générer plusieurs demandes d'invoices. Lorsqu'un utilisateur scanne un QR code contenant une *offer*, il envoie un message pour demander une nouvelle invoice au nœud Lightning associé. Le nœud répond avec une invoice que le payeur peut utiliser. Les *offers* permettent ainsi de disposer d'un identifiant unique pour recevoir de nombreux paiement de la part de plusieurs utilisateurs différents sur Lightning.
