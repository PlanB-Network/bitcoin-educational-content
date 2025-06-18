---
term: OFFER
---

In BOLT12, *offers* are static QR codes for making multiple payments on Lightning Network. Unlike conventional invoices, *offers* can be reused. They can be used to generate multiple invoice requests. When a user scans a QR code containing an *offer*, it sends a message requesting a new Invoice to the associated Lightning node. The node responds with a Invoice that the payer can use. The *offers* thus provide a unique identifier for receiving multiple payments from different users on Lightning.