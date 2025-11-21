---
term: LNURL
---

Communication protocol that specifies a set of features designed to simplify interactions between Lightning nodes and clients, as well as third-party applications. This protocol is based on HTTP and enables links to be created for various operations, such as a payment request, a withdrawal request, or other functionalities that enhance the user experience. Each LNURL is a URL encoded in bech32 with the prefix `lnurl`, which, when scanned, triggers a series of automatic actions on the Lightning wallet.

For example, LNURL-withdraw (LUD-03) lets you withdraw funds from a service by scanning a QR code, without having to manually generate a Invoice. Or LNURL-auth (LUD-04) lets you connect to online services using a private key on your Lightning wallet instead of a password.