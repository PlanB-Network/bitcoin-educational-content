---
term: REDEEMSCRIPT
---

REDEEMSCRIPT là một script định nghĩa các điều kiện cụ thể mà các input phải đáp ứng để mở khóa các quỹ liên kết với một đầu ra P2SH. Trong một UTXO P2SH, `scriptPubKey` chứa hash của `redeemScript`. Khi một giao dịch muốn chi tiêu UTXO này như một input, nó phải cung cấp `redeemScript` rõ ràng phù hợp với hash chứa trong `scriptPubKey`. Vì vậy, `redeemScript` được đưa vào trong `scriptSig` của input, cùng với các yếu tố khác cần thiết để thỏa mãn các điều kiện của script, như chữ ký hoặc khóa công khai. Cấu trúc được đóng gói này đảm bảo rằng các chi tiết của điều kiện chi tiêu được giấu kín cho đến khi bitcoin thực sự được chi tiêu. Nó đặc biệt được sử dụng cho ví đa chữ ký P2SH Legacy.