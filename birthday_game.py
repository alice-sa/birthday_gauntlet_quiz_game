import streamlit as st
import time
import datetime

# Set up page styling
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# --- INITIALIZE GAME STATE ---
if "level" not in st.session_state:
    st.session_state.level = 1
if "wrong_answer" not in st.session_state:
    st.session_state.wrong_answer = False

# --- APP HEADER ---
st.title("🎁 The Birthday Gauntlet")
st.write("Complete the quest to unlock your final birthday surprise.")
st.divider()

# ==============================================================================
# LEVEL 1: FIRST DATE (3X BALLOONS)
# ==============================================================================
if st.session_state.level == 1:
    st.header("Level 1: Where It All Began ☕")
    st.write("Where did we have our very first date?")
    
    if not st.session_state.wrong_answer:
        answer_1 = st.text_input("Your answer:", key="q1").strip().lower()
        
        if st.button("Submit Answer", key="btn1"):
            if "malabar" in answer_1:
                # --- TRIPLE CELEBRATION WAVE ---
                st.balloons()   
                time.sleep(0.5)
                st.balloons()   
                time.sleep(0.5)
                st.balloons()   
                
                st.success("🎉 YES! You actually remembered! Best first date ever.")
                time.sleep(3.0)  
                st.session_state.level = 2
                st.rerun()
            else:
                st.session_state.wrong_answer = True
                st.rerun()
    else:
        st.error("❌ Wrong! Oof, off to a rocky start. Think back to day one... 👀")
        if st.button("🔄 Try Again", key="retry1"):
            st.session_state.wrong_answer = False
            st.rerun()

# ==============================================================================
# LEVEL 2: HONEYMOON (3X BALLOONS)
# ==============================================================================
elif st.session_state.level == 2:
    st.header("Level 2: Just Married ✈️")
    st.write("Where did we go on our honeymoon?")
    
    if not st.session_state.wrong_answer:
        answer_2 = st.text_input("Your answer:", key="q2").strip().lower()
        
        if st.button("Submit Answer", key="btn2"):
            if "italy" in answer_2:
                # --- TRIPLE CELEBRATION WAVE + SNOW ---
                st.balloons() 
                time.sleep(0.5)
                st.balloons() 
                time.sleep(0.5)
                st.balloons() 
                
                st.success("🎉 BRAVO! Italy was magical. Take me back to those pasta days! 🇮🇹")
                time.sleep(3.0)
                st.session_state.level = 3
                st.rerun()
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
    
    if not st.session_state.wrong_answer:
        selected_date = st.date_input(
            "Select the date:",
            value=datetime.date(2026, 1, 1),
            key="q3"
        )
        
        if st.button("Submit Answer", key="btn3"):
            if selected_date == datetime.date(2026, 1, 6):
                # --- TRIPLE CELEBRATION WAVE ---
                st.balloons() 
                time.sleep(0.5)
                st.balloons() 
                time.sleep(0.5)
                st.balloons() 
                
                st.info("💙 AMAZING! January 6, 2026. A brand new chapter started that day!")
                time.sleep(3.5)
                st.session_state.level = 4
                st.rerun()
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
    
    if not st.session_state.wrong_answer:
        show_choice = st.radio(
            "Select the correct show:",
            ["Modern Family", "Young Sheldon"]
        )
        
        if st.button("Lock It In", key="btn4"):
            if "modern family" in show_choice.lower():
                # --- TRIPLE CELEBRATION WAVE ---
                st.balloons()
                time.sleep(0.5)
                st.balloons()
                time.sleep(0.5)
                st.balloons()
                
                st.success("🎉 Yes! Phil Dunphy would be proud. You're crushing this!")
                time.sleep(3.0)
                st.session_state.level = 5
                st.rerun()
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
    
    if not st.session_state.wrong_answer:
        answer_5 = st.text_input("Your answer:", key="q5").strip().lower()
        
        if st.button("Submit Final Answer", key="btn5"):
            if "iceland" in answer_5:
                # --- TRIPLE CELEBRATION WAVE + SNOW ---
                st.balloons() 
                st.snow()
                time.sleep(0.5)
                st.balloons() 
                time.sleep(0.5)
                st.balloons() 
                
                st.success("🎉 Spot on! Northern Lights, here we come!")
                time.sleep(3.0)
                st.session_state.level = 6
                st.rerun()
            else:
                st.session_state.wrong_answer = True
                st.rerun()
    else:
        st.error("❌ Nope! Think glaciers, waterfalls, and black sand beaches... 🧊")
        if st.button("🔄 Try Again", key="retry5"):
            st.session_state.wrong_answer = False
            st.rerun()

# ==============================================================================
# WIN SCREEN: THE GRAND PRIZE REVEAL (THE ULTIMATE BALLOON FLOOD)
# ==============================================================================
elif st.session_state.level == 6:
    # --- ULTIMATE FINALE WAVE ---
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
    
    st.info("🎁 YOUR REAL GIFT IS HIDDEN UNDER THE SOFA! GO GET IT! I LOVE YOU AND WISH YOU HAPPY BIRTHDAY ONCE AGAIN !!!")