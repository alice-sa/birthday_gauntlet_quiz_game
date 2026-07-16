import streamlit as st
import time
import datetime

# Set up page styling
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# --- URL ROUTING & LOCK CONTROLLER ---
is_static = False
if "mode" in st.query_params and st.query_params["mode"] == "static":
    is_static = True

if "level" in st.query_params:
    try:
        requested_level = int(st.query_params["level"])
        if "level" not in st.session_state or st.session_state.get("last_url_level") != requested_level:
            st.session_state.level = requested_level
            st.session_state.last_url_level = requested_level
            st.session_state.wrong_answer = False
            if "completed_static" in st.session_state:
                del st.session_state.completed_static
    except ValueError:
        pass

# Fallback initializers
if "level" not in st.session_state:
    st.session_state.level = 1
if "wrong_answer" not in st.session_state:
    st.session_state.wrong_answer = False

# --- APP HEADER ---
st.title("🎁 The Birthday Gauntlet")
st.write("Complete the quest to unlock your final birthday surprise.")
st.divider()

# Helper function to handle correct answers
def handle_correct(next_level_num, message):
    st.balloons()
    time.sleep(0.5)
    st.balloons()
    time.sleep(0.5)
    st.balloons()
    
    if is_static:
        st.session_state.completed_static = True
        st.success(f"{message}\n\n🌟 LEVEL COMPLETED! 🌟")
    else:
        st.success(message)
        time.sleep(3.0)
        st.session_state.level = next_level_num
        st.rerun()

# ==============================================================================
# LEVEL 1: FIRST DATE (3X BALLOONS)
# ==============================================================================
if st.session_state.level == 1:
    st.header("Level 1: Where It All Began ☕")
    st.write("Where did we have our very first date?")
    
    # 1. This shows if the level is already completed (e.g. on page refresh)
    if st.session_state.get("completed_static"):
        st.success("🎉 YES! You actually remembered! Best first date ever.\n\n🌟 LEVEL COMPLETED! 🌟\n\nYour first surprise is with the flowers... 💐")
        
    elif not st.session_state.wrong_answer:
        answer_1 = st.text_input("Your answer:", key="q1").strip().lower()
        if st.button("Submit Answer", key="btn1"):
            if "malabar" in answer_1:
                # 2. We pass your custom flower surprise clue straight into the success function here:
                handle_correct(2, "🎉 YES! You actually remembered! Best first date ever.\n\nYour first surprise is with the flowers... 💐")
            else:
                st.session_state.wrong_answer = True
                st.rerun()
    else:
        st.error("❌ Wrong! You got this, just think back to the first time we met... 👀")
        if st.button("🔄 Try Again", key="retry1"):
            st.session_state.wrong_answer = False
            st.rerun()
# ==============================================================================
# LEVEL 2: HONEYMOON (3X BALLOONS + SNOW)
# ==============================================================================
elif st.session_state.level == 2:
    st.header("Level 2: Just Married ✈️")
    st.write("Where did we go on our honeymoon?")
    
    if st.session_state.get("completed_static"):
        st.snow()
        st.success("🎉 BRAVO! Italy was magical. Take me back to those pasta days! 🇮🇹\n\n🌟 LEVEL COMPLETED! 🌟 ")
    elif not st.session_state.wrong_answer:
        answer_2 = st.text_input("Your answer:", key="q2").strip().lower()
        if st.button("Submit Answer", key="btn2"):
            if "italy" in answer_2:
                st.snow()
                handle_correct(3, "🎉 BRAVO! Italy was magical. Take me back to those pasta days! 🇮🇹\n\n Your next surprise is where you mostly sit for work...")
            else:
                st.session_state.wrong_answer = True
                st.rerun()
    else:
        st.error("❌ Wrong! Hint: Think of wine, pizza, and romance... 🍷")
        if st.button("🔄 Try Again", key="retry2"):
            st.session_state.wrong_answer = False
            st.rerun()

# ==============================================================================
# LEVEL 3: USA LANDING (3X BALLOONS + BLUE CARD)
# ==============================================================================
elif st.session_state.level == 3:
    st.header("Level 3: Landing in the US 🇺🇸")
    st.write("On what date did we officially land in the US together?")
    
    if st.session_state.get("completed_static"):
        st.info("💙 AMAZING! January 6, 2026. A brand new chapter started that day!\n\n🌟 LEVEL COMPLETED! 🌟")
    elif not st.session_state.wrong_answer:
        selected_date = st.date_input("Select the date:", value=datetime.date(2026, 1, 1), key="q3")
        if st.button("Submit Answer", key="btn3"):
            if selected_date == datetime.date(2026, 1, 6):
                handle_correct(4, "💙 AMAZING! January 6, 2026. A brand new chapter started that day!/n/nYour third surprise is where you would never look. Kiss your wife for hints. Kisses for each hint, hehe!")
            else:
                st.session_state.wrong_answer = True
                st.rerun()
    else:
        st.error("❌ Not quite! Think back to the very beginning of 2026... ✈️")
        if st.button("🔄 Try Again", key="retry3"):
            st.session_state.wrong_answer = False
            st.rerun()

# ==============================================================================
# LEVEL 4: BINGE SHOW (3X BALLOONS MEGA BURST)
# ==============================================================================
elif st.session_state.level == 4:
    st.header("Level 4: Couch Potato Protocol 📺")
    st.write("What is our absolute favorite show to binge together?")
    
    if st.session_state.get("completed_static"):
        st.success("🎉 Yes! Phil Dunphy would be proud. You're crushing this!\n\n🌟 LEVEL COMPLETED! 🌟 ")
    elif not st.session_state.wrong_answer:
        show_choice = st.radio("Select the correct show:", ["Modern Family", "Young Sheldon"])
        if st.button("Lock It In", key="btn4"):
            if "modern family" in show_choice.lower():
                handle_correct(5, "🎉 Yes! Phil Dunphy would be proud. You're crushing this! \n\n Tap your wife down for the next gift")
            else:
                st.session_state.wrong_answer = True
                st.rerun()
    else:
        st.error("❌ Wait, seriously?! You think that's our number one? Try again! 😂")
        if st.button("🔄 Try Again", key="retry4"):
            st.session_state.wrong_answer = False
            st.rerun()

# ==============================================================================
# LEVEL 5: DREAM DESTINATION (3X BALLOONS + ICELAND SNOW)
# ==============================================================================
elif st.session_state.level == 5:
    st.header("Level 5: Future Adventures 🌌")
    st.write("Last and final question: Which is our dream destination to visit in the future?")
    
    if st.session_state.get("completed_static"):
        st.snow()
        st.success("🎉 Spot on! Northern Lights, here we come!\n\n🌟 LEVEL COMPLETED! 🌟")
    elif not st.session_state.wrong_answer:
        answer_5 = st.text_input("Your answer:", key="q5").strip().lower()
        if st.button("Submit Final Answer", key="btn5"):
            if "iceland" in answer_5:
                st.snow()
                handle_correct(6, "🎉 Spot on! Northern Lights, here we come!")
            else:
                st.session_state.wrong_answer = True
                st.rerun()
    else:
        st.error("❌ Nope! Think glaciers, waterfalls, and black sand beaches... 🧊")
        if st.button("🔄 Try Again", key="retry5"):
            st.session_state.wrong_answer = False
            st.rerun()

# ==============================================================================
# WIN SCREEN: THE GRAND PRIZE REVEAL
# ==============================================================================
elif st.session_state.level == 6:
    st.balloons() 
    st.snow()
    time.sleep(0.5)
    st.balloons() 
    time.sleep(0.5)
    st.balloons() 
    
    st.header("🎉 YOU DID IT! 🎉")
    st.subheader("Happy Birthday to my amazing husband!")
    st.write("You have successfully conquered the gauntlet and proved your memory is top-tier.")
    st.write("Your birthday reward is waiting for you:")
    st.info("🎁 YOUR REAL GIFT IS HIDDEN UNDER THE SOFA! GO GET IT!")
