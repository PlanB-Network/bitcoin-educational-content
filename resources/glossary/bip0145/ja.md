---
term: BIP0145
definition: SegWitサポートとトランザクション・ウェイト（重量）の計算を統合するためのJSON-RPC getblocktemplateコールの更新。
---
BIP141に従って、JSON-RPCコール`getblocktemplate`を更新し、SegWitのサポートを含める。この更新により、マイナーはSegWitによって導入されたトランザクションとブロックの新しい「重み」測定、およびsigops制限の計算などの他のパラメータを考慮してブロックを構築できるようになります。