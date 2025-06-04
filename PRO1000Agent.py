import streamlit as st
import plotly.graph_objects as go

# Initialize step and all session state keys only once
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.TCH = 3
    st.session_state.COM = 3
    st.session_state.RAD = 3
    st.session_state.CPL = 3
    st.session_state.SEC = 3
    st.session_state.COS = 3
    st.session_state.LSG = 3
    st.session_state.ORG = 3
    st.session_state.CPT = 3
    
# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0

# Go to next step
def next_step():
    st.session_state.step += 1

# Reset
def reset():
    st.session_state.step = 0

# Title
st.set_page_config(page_title="Đánh giá khả thi Blockchain", layout="centered")
st.title("🧠 Hệ thống đánh giá khả thi ứng dụng Blockchain trong GTVT & Logistics")

# Step 0: Landing page
if st.session_state.step == 0:
    st.header("1️⃣ Mô tả trường hợp và lĩnh vực áp dụng")
    domain = st.selectbox("Chọn lĩnh vực", ["Vận tải hàng hóa", "Quản lý đăng kiểm", "Logistics", "Quản lý dự án hạ tầng", "Khác"])
    case_desc = st.text_area("Mô tả ngắn gọn về trường hợp áp dụng", placeholder="Ví dụ: Ứng dụng Blockchain để minh bạch hóa lịch sử đăng kiểm...")
    org_name = st.text_input("Tên tổ chức hoặc doanh nghiệp liên quan")
    if st.button("Bắt đầu đánh giá", type="primary"):
        next_step()

# Step 1: Công nghệ và nhận thức
elif st.session_state.step == 1:
    st.header("2️⃣ Các yếu tố về công nghệ và nhận thức")
    st.slider("Sự sẵn sàng về công nghệ (TCH)", 1, 5, key="TCH")
    st.slider("Khả năng tương thích hệ thống (COM)", 1, 5, key="COM")
    st.slider("Nhận thức lợi ích và lợi thế cạnh tranh (RAD)", 1, 5, key="RAD")
    st.slider("Tính phức tạp kỹ thuật (CPL)", 1, 5, key="CPL")
    if st.button("Tiếp tục"):
        next_step()

# Step 2: Bảo mật, chi phí, pháp lý
elif st.session_state.step == 2:
    st.header("3️⃣ Các yếu tố pháp lý, chi phí và bảo mật")
    st.slider("Bảo mật và quyền riêng tư (SEC)", 1, 5, key="SEC")
    st.slider("Chi phí triển khai và vận hành (COS)", 1, 5, key="COS")
    st.slider("Pháp lý & chính sách hỗ trợ từ Chính phủ (LSG)", 1, 5, key="LSG")
    if st.button("Tiếp tục"):
        next_step()

# Step 3: Tổ chức và cạnh tranh
elif st.session_state.step == 3:
    st.header("4️⃣ Các yếu tố tổ chức và cạnh tranh")
    st.slider("Sự sẵn sàng của tổ chức (ORG)", 1, 5, key="ORG")
    st.slider("Áp lực cạnh tranh (CPT)", 1, 5, key="CPT")
    if st.button("Xem kết quả đánh giá", type="primary"):
        next_step()

# Step 4: Kết quả và khuyến nghị
elif st.session_state.step == 4:
    st.header("🧾 Kết quả đánh giá khả thi")

    # Simple scoring
    score = (
        st.session_state.TCH +
        st.session_state.COM +
        st.session_state.RAD +
        (6 - st.session_state.CPL) +  # lower complexity = higher score
        st.session_state.SEC +
        (6 - st.session_state.COS) +  # lower cost = higher score
        st.session_state.LSG +
        st.session_state.ORG +
        st.session_state.CPT
    )

    feasibility_level = ""
    if score >= 38:
        feasibility_level = "✅ Rất khả thi"
    elif score >= 30:
        feasibility_level = "🟡 Khả thi có điều kiện"
    else:
        feasibility_level = "🔴 Chưa khả thi"

    st.subheader("🔍 Tổng điểm: " + str(score) + " / 45")
    st.subheader("📊 Biểu đồ đánh giá theo tiêu chí")
    # Radar chart categories and values
    labels = [
        "Công nghệ (TCH)",
        "Tương thích (COM)",
        "Lợi ích cảm nhận (RAD)",
        "Độ phức tạp (CPL ↓)",
        "Bảo mật (SEC)",
        "Chi phí (COS ↓)",
        "Pháp lý (LSG)",
        "Tổ chức (ORG)",
        "Cạnh tranh (CPT)"
    ]
    
    # Invert CPL and COS to represent "less is better"
    values = [
        st.session_state.TCH,
        st.session_state.COM,
        st.session_state.RAD,
        6 - st.session_state.CPL,
        st.session_state.SEC,
        6 - st.session_state.COS,
        st.session_state.LSG,
        st.session_state.ORG,
        st.session_state.CPT
    ]
    
    fig = go.Figure(
        data=[
            go.Scatterpolar(
                r=values,
                theta=labels,
                fill='toself',
                name='Mức điểm đánh giá'
            )
        ],
        layout=go.Layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )
            ),
            showlegend=False
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.success(f"Đánh giá mức độ khả thi: **{feasibility_level}**")
    
    # Recommendations
    st.markdown("### 📌 Khuyến nghị:")
    if st.session_state.LSG < 3:
        st.warning("⚠️ Cần thúc đẩy khung pháp lý và chính sách hỗ trợ từ Chính phủ.")
    if st.session_state.ORG < 3:
        st.warning("⚠️ Tổ chức của bạn chưa đủ sẵn sàng về quy trình và nhân lực.")
    if st.session_state.SEC < 3:
        st.warning("⚠️ Cân nhắc đầu tư vào giải pháp bảo mật và đảm bảo quyền riêng tư.")
    if st.session_state.COS > 3:
        st.info("💡 Xem xét lựa chọn các mô hình blockchain mã nguồn mở để giảm chi phí.")

    st.divider()
    st.button("Thực hiện lại đánh giá", on_click=reset)
