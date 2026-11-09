---
name: trinh-ky
description: "Quy trình trọn gói: Rà soát một văn bản trước khi trình ký – kiểm tra thể thức tự động bằng công cụ + soát nội dung, báo lỗi 3 mức CHẶN/CẦN SỬA/GỢI Ý."
---

Thông tin cần có từ người dùng: [đường dẫn file .docx hoặc dán nội dung]. Thiếu thông tin quan trọng thì hỏi gọn một lần.


Kiểm tra trước trình ký: yêu cầu của người dùng

Dùng skill `kiem-tra-truoc-trinh-ky`. Chạy `kiem_tra_the_thuc` trên file (hoặc nội dung), soát nội dung theo checklist, rồi báo cáo đúng định dạng: kết luận 1 dòng → bảng lỗi → điểm không kiểm tra được → hỏi có cần bản sửa (tạo file mới, không ghi đè).
