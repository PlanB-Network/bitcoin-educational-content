---
term: MACAROON
---

一种旨在保护分布式系统上服务访问的认证机制。Macaroons 特别用于 Lightning 上，当用户访问委托服务时进行认证。例如，在 Lightning 节点上，可以生成一个 macaroon，授权从您的智能手机通过远程节点执行交易。与 cookies 不同，macaroons 的优势在于可以由发行者加密验证或委托进行验证。