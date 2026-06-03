import streamlit as st
import time

# 웹 페이지 제목 및 스타일 설정
st.set_page_config(page_title="톨만 온도 시뮬레이터", page_icon="🌌")
st.title("🌌 일반 상대성 이론: 톨만 온도 시뮬레이터")
st.markdown("---")

# 1. 사용자에게 아는지 모르는지 질문 (라디오 버튼)
st.subheader("자, 우리는 톨만 온도에 대해서 알아볼겁니다.")
answer = st.radio("혹시 톨만 온도에 대해서 아시나요?", ["선택하세요", "Yes", "No"], index=0)

st.markdown("---")

# 2. 조건문 처리
if answer == "No":
    st.markdown("### 📡 [시스템] 톨만 온도 데이터베이스를 로드합니다...")
    time.sleep(0.8)
    
    st.info("💡 **톨만 온도라는 것은, 중력이 존재 한다면 열평형이 되기 위해서 각 지점의 온도가 달라져야 한다는 것을 의미합니다.**")
    time.sleep(1.2)
    st.write("상대성 이론에 의하면, **중력이 강한 곳은 시간이 느리게 갑니다.**")
    time.sleep(1.2)
    st.write("시간이 느리다면 분자들의 움직임, 즉 에너지가 감소할것이고 그에 따라 그 곳의 국소 온도도 낮아질 것입니다.")
    time.sleep(1.5)
    st.write("따라서 열평형을 맞추기 위해 낮아진 국소 온도를 올려야겠죠. 이것이 톨만 온도입니다.")
    time.sleep(1.2)
    
    st.success("🔄 이제 개념을 이해하셨으니 위의 질문을 **'Yes'**로 바꾸고 계산을 해볼까요?")

elif answer == "Yes":
    st.subheader("🛰️ [블랙홀 탐사선 시스템 가동]")
    
    # 사건의 지평선 입력창
    rs = st.number_input("사건의 지평선 반지름은?(km) :", min_value=1, value=10, step=1)
    
    # 계산 실행 버튼
    if st.button("🚀 탐사 시작"):
        temper = []
        distance = []
        T = 2.73  # 우주 배경 복사 온도 (K)

        # 파이썬 코드의 로딩 바 효과를 스트림릿 프로그레스 바로 구현
        st.write("🔮 블랙홀 주변 시공간의 열평형 상태를 연산 중입니다...")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        st.success("] 100% 연산 완료!")
        time.sleep(0.5)

        # 데이터 계산 로직 (기존 내용 유지)
        for r in range(rs + 2, rs + 22):
            tem = T * (1 - (rs / r))**(-0.5)
            temper.append(tem)
            distance.append(r)
        
        st.markdown(f"### 📡 사건의 지평선({rs}km) 인근 {rs+2}km 부터 {rs+22}km 까지의 톨만 온도를 스캔합니다.")
        st.markdown("---")
        time.sleep(0.8)

        # 실시간 출력 연출용 컨테이너 생성
        status_area = st.container()
        
        with status_area:
            for i in range(20):
                # 온도의 강도에 따라 시각적인 위험도(게이지) 표시 (기존 내용 유지)
                if temper[i] > 6.0:
                    status = "⚠️ [초고온 위험 지대] 🔥🔥🔥"
                elif temper[i] > 4.0:
                    status = "🚨 [고온 경계 지대] 🔥"
                else:
                    status = "✨ [안정 구간]"

                # 스트림릿 화면에 한 줄씩 스르륵 출력
                st.write(f"📍 **{i+1:02d}번 지점** | 거리 : `{distance[i]:>2d}km`  | ➡️  온도 : `{temper[i]:.2f}K` {status}")
                time.sleep(0.1)  # 타이핑 효과 유지
        
        st.markdown("---")
        time.sleep(0.5)
        
        # 탐사 결론 출력 (기존 내용 유지)
        st.markdown("### 📝 [탐사 결론]")
        st.info(
            "이렇듯 톨만 온도는 블랙홀에 가장 가까운 지점에서 폭발적으로 높고, "
            "멀어질수록 우주 배경 복사 온도(2.73K)에 수렴하며 낮아진다는 사실을 확인할 수 있습니다."
        )