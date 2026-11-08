---
description: Quy trình trọn gói tuyển và nhận một nhân viên mới – JD, tin tuyển dụng, offer (lương net/gross), HĐLĐ/thử việc, checklist onboarding, báo tăng BHXH.
argument-hint: "[vị trí, mức lương, ngày dự kiến đi làm]"
---

Thực hiện quy trình nhận nhân viên mới cho: $ARGUMENTS

Làm lần lượt, mỗi bước xong thì tóm tắt và hỏi người dùng có tiếp không (không tự gửi gì ra ngoài):

1. Dùng skill `tuyen-dung`: làm rõ nhu cầu, viết JD và tin tuyển dụng (rà phân biệt đối xử). Nếu đã có ứng viên thì bỏ qua sang bước 2.
2. Dùng skill `tuyen-dung`: tính lương offer bằng công cụ `luong_net_gross` (đúng vùng, số người phụ thuộc, ngày bắt đầu), kiểm tra `kiem_tra_luong_toi_thieu`, `kiem_tra_thu_viec`; soạn thư mời nhận việc (dạng nháp).
3. Dùng skill `hop-dong-lao-dong`: soạn HĐ thử việc hoặc HĐLĐ có điều khoản thử việc; rà điều khoản trái luật.
4. Dùng skill `onboarding-offboarding`: checklist trước ngày đầu (người phụ trách, hạn), lịch tuần đầu, mục tiêu 30-60-90; tính ngày kết thúc thử việc bằng `cong_ngay_lich`.
5. Nhắc thủ tục: báo tăng BHXH trong tháng (skill `bhxh-che-do`), cập nhật sổ quản lý lao động, lưu hồ sơ (skill `luu-tru-ho-so`).

Cuối cùng: bảng tổng hợp việc – người phụ trách – hạn, và danh sách thông tin còn thiếu.
