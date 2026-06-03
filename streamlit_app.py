import streamlit as st

# 웹 페이지 제목 설정
st.title("🌌 일반 상대성 이론: 톨만 온도 시뮬레이터")
st.markdown("---")

# 1. 사용자에게 아는지 모르는지 질문 (라디오 버튼)
st.subheader("자, 우리는 톨만 온도에 대해서 알아볼겁니다.")
answer = st.radio("혹시 톨만 온도에 대해서 아시나요?", ["선택하세요", "Yes", "No"], index=0)

st.markdown("---")

# 2. 조건문 처리
if answer == "No":
    st.info("💡 **톨만 온도(Tolman temperature)란?**")
    st.write("중력이 존재한다면 열평형이 되기 위해서 각 지점의 온도가 달라져야 한다는 것을 의미합니다.")
    st.write("상대성 이론에 의하면, **중력이 강한 곳은 시간이 느리게 갑니다.**")
    st.write("시간이 느리다면 분자들의 움직임, 즉 에너지가 감소할 것이고 그에 따라 그 곳의 국소 온도도 낮아질 것입니다.")
    st.write("따라서 열평형을 맞추기 위해 낮아진 국소 온도를 올려야겠죠. 이것이 톨만 온도입니다.")
    st.success("이제 개념을 이해하셨다면 위의 질문을 **'Yes'**로 바꾸고 계산을 해볼까요?")

elif answer == "Yes":
    st.subheader("🧮 톨만 온도 계산기")
    
    # 숫자 입력창 (기본값 10km)
    rs = st.number_input("사건의 지평선 반지름은 몇 km인가요? (정수 입력)", min_value=1, value=10, step=1)
    
    # 계산 실행 버튼
    if st.button("온도 조사하기"):
        temper = []
        distance = []

        # 기존 로직대로 계산
        for r in range(rs + 2, rs + 22):
            tem = rs / r
            temper.append(tem)
            distance.append(r)
        
        st.write(f"🔍 **사건의 지평선 반지름이 {rs}km일 때, {rs+2}km부터 {rs+22}km까지의 톨만 온도 조사 결과입니다.**")
        st.write("")

        # 결과를 보기 좋게 출력 (2열 레이아웃이나 표로 만들어도 좋지만, 기존 코드 스타일을 살려 출력합니다)
        for i in range(20):
            st.write(f"📍 **{i+1}번 지점** | 거리: `{distance[i]}km` ➡️ 온도: `{temper[i]:.2f}°C` ")
        
        st.markdown("---")
        st.success("✨ 이렇듯 톨만 온도는 **가장 가까운 지점에서 제일 높고, 가장 먼 곳에서 제일 낮다**는 사실을 알 수 있습니다!")