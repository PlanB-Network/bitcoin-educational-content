---
term: PRUNED NODE
---

Một pruned node, trong tiếng Anh là "Pruned Node", là một full node thực hiện việc cắt tỉa blockchain. Điều này bao gồm việc loại bỏ dần các khối cũ nhất, sau khi đã kiểm tra chúng một cách đúng đắn, để chỉ giữ lại các khối gần đây nhất. Giới hạn lưu trữ được chỉ định trong tệp `bitcoin.conf` thông qua tham số `prune=n`, nơi `n` là kích thước tối đa mà các khối chiếm dụng tính bằng megabyte (MB). Nếu sau tham số này ghi là `0`, thì việc cắt tỉa được vô hiệu hóa, và node sẽ giữ lại blockchain một cách toàn vẹn.

Các pruned node đôi khi được coi là các loại node khác biệt so với full node. Việc sử dụng một pruned node có thể đặc biệt thú vị đối với những người dùng đối mặt với hạn chế về dung lượng lưu trữ. Hiện tại, một full node cần phải có gần 600 GB chỉ để lưu trữ blockchain. Một pruned node có thể giới hạn dung lượng lưu trữ cần thiết xuống còn tối đa 550 MB. Mặc dù sử dụng ít không gian đĩa hơn, một pruned node vẫn duy trì mức độ kiểm tra và xác thực tương tự như một full node. Do đó, pruned nodes cung cấp nhiều sự tin cậy hơn cho người dùng của họ so với các light node (SPV).