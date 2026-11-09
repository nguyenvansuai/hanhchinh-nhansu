---
name: xu-ly-ky-luat
description: "Quy trình trọn gói: Kiểm tra điều kiện và lập đủ hồ sơ xử lý kỷ luật lao động đúng trình tự (thời hiệu, thông báo họp 5 ngày làm việc, biên bản họp, quyết định)."
---

Thông tin cần có từ người dùng: [hành vi vi phạm, ngày xảy ra, nhân viên, hình thức dự kiến]. Thiếu thông tin quan trọng thì hỏi gọn một lần.


Xử lý kỷ luật lao động cho vụ việc: yêu cầu của người dùng

Dùng skill `ky-luat-lao-dong`:
1. Chạy bảng sàng lọc Bước 0 – báo từng điều kiện Đạt/Không đạt/Chưa rõ. Có điều kiện "Không đạt" thì dừng và giải thích.
2. Gọi `thoi_hieu_ky_luat` (ngày vi phạm, có liên quan tài chính/tài sản/bí mật không, ngày họp dự kiến) → lịch các mốc.
3. Soạn: biên bản vi phạm (nếu chưa có), thông báo họp, biên bản họp (khung để điền tại cuộc họp), dự thảo quyết định.
4. Liệt kê chứng cứ cần có và hồ sơ cần lưu.

Không kết luận hình thức thay người dùng; với sa thải luôn khuyến nghị tham vấn luật sư/pháp chế.
