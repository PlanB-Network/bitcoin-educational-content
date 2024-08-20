---
term: UTREEXO
---

UTREEXO là một giao thức được thiết kế bởi Tadge Dryja nhằm rút gọn bộ UTXO của các nút Bitcoin sử dụng một bộ tích lũy dựa trên cây Merkle. Khác với bộ UTXO truyền thống yêu cầu không gian lưu trữ đáng kể, Utreexo giảm đáng kể bộ nhớ cần thiết bằng cách chỉ lưu trữ các gốc cây Merkle. Điều này cho phép nút xác minh sự tồn tại của UTXOs được sử dụng trong các đầu vào giao dịch, mà không cần phải giữ toàn bộ bộ UTXOs. Bằng cách sử dụng Utreexo, mỗi nút chỉ giữ một dấu vân tay mật mã gọi là gốc Merkle. Khi một giao dịch được thực hiện, người dùng cung cấp các bằng chứng sở hữu của UTXOs và các đường dẫn Merkle tương ứng. Như vậy, nút có thể xác minh giao dịch mà không cần lưu trữ toàn bộ bộ UTXO. Hãy xem một ví dụ với sơ đồ để hiểu cơ chế này:

![](../../dictionnaire/assets/15.png)

Trong ví dụ này, tôi cố ý giảm bộ UTXO xuống còn 4 UTXOs để dễ hiểu hơn. Trên thực tế, quan trọng là phải tưởng tượng rằng có gần 140 triệu UTXOs trên Bitcoin vào thời điểm viết những dòng này. Trong sơ đồ này, nút Utreexo chỉ cần giữ gốc Merkle trong RAM. Nếu nó nhận được một giao dịch chi tiêu UTXO số 3 (màu đen), bằng chứng sẽ bao gồm các yếu tố sau:
* UTXO 3;
* HASH 4;
* HASH 1-2.

Với thông tin này được truyền bởi người gửi giao dịch, nút Utreexo thực hiện các xác minh sau:
* Nó tính toán dấu vân tay của UTXO 3, từ đó nó nhận được HASH 3;
* Nó nối HASH 3 với HASH 4;
* Nó tính toán dấu vân tay của chúng, từ đó nhận được HASH 3-4;
* Nó nối HASH 3-4 với HASH 1-2;
* Nó tính toán dấu vân tay của chúng, từ đó nhận được gốc Merkle.

Nếu gốc Merkle mà nó thu được qua quá trình này giống với gốc Merkle mà nó đã lưu trong RAM, thì nó tin rằng UTXO số 3 thực sự là một phần của bộ UTXO.
Phương pháp này giảm yêu cầu RAM cho các nhà vận hành nút đầy đủ. Tuy nhiên, Utreexo có những hạn chế, bao gồm sự tăng kích thước khối do các bằng chứng bổ sung và sự phụ thuộc tiềm năng của các nút Utreexo vào Bridge Nodes để lấy các bằng chứng còn thiếu. Bridge Nodes là các nút đầy đủ truyền thống cung cấp các bằng chứng cần thiết cho các nút Utreexo, do đó cho phép xác minh đầy đủ. Cách tiếp cận này cung cấp một sự cân bằng giữa hiệu quả và phân quyền, làm cho việc xác minh giao dịch trở nên dễ dàng hơn đối với người dùng có nguồn lực hạn chế.