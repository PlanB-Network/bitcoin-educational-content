---
term: Macaroon

definition: Cơ chế xác thực được sử dụng trên Lightning để bảo mật quyền truy cập vào các dịch vụ từ xa.
---
An authentication mechanism designed to secure access to services on distributed systems. Macaroons are notably used on Lightning to authenticate users when they access delegated services. For example, with a Lightning node, it is possible to generate a macaroon that authorizes the execution of transactions from your smartphone via your remote node. Unlike cookies, macaroons have the advantage of being cryptographically validated by the issuer or being delegated for verification.