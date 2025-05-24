import streamlit as st
def set_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://i.pinimg.com/originals/70/f0/3b/70f03b53862c00f069f0e6a8f065584c.jpg");
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Initialize session states
if "scene" not in st.session_state:
    st.session_state.scene = "start"
if "intro_step" not in st.session_state:
    st.session_state.intro_step = 0

def start_scene():
    st.title("🤝 tomodachi - kanojo ❤️")

    if st.session_state.intro_step == 0:
        st.balloons()
        st.title("**Welcome SIM!**")
        st.image("https://media.tenor.com/hVRhFeDFW6oAAAAj/anime-wave.gif")
        
        if st.button("**SIM : HI!**"):
            st.session_state.intro_step = 1
            st.rerun()
        if st.button("**SIM : EH?**"):
            st.session_state.intro_step = 2
            st.rerun()
        return

    if st.session_state.intro_step == 1:
        st.markdown("*First question : Do u ❤️ me?*")
        st.image("https://media.tenor.com/IAUeLdWRZAcAAAAM/heart-anime.gif")
        if st.button("SIM: YES OFC ❤️"):
            st.session_state.scene = "yapping"
            st.rerun()
        if st.button("SIM : KHAI KUNI .. "):
            st.session_state.scene = "home"
            st.rerun()
        if st.button("🔙 Go back"):
            st.session_state.scene = "start"
            st.session_state.intro_step = 0
            st.rerun()
        return

    if st.session_state.intro_step == 2:
        st.title("**AK : REALLY?**")
        st.image("https://i.pinimg.com/originals/f9/0b/8c/f90b8c286d7235354668ac66b3194a0a.gif")
        if st.button("SIM: JK JK JK JK JK JK"):
            st.session_state.intro_step = 0
            st.rerun()
        return

def yapping_scene():
    st.title("AK : FERI , FERI ")
    st.image("https://media.tenor.com/DE327HSCNlMAAAAM/hanako-kun-anime.gif")
    #st.image("https://gifsec.com/wp-content/uploads/2022/11/love-anime-gif-11.gif")
    if st.button("SIM: I LOVE YOU"):
        st.session_state.scene = "acceptance"
        
        st.rerun()


# Scene functions for denials ---------------------------------------------------------------------------------------------------------------------------
def pleading_scene():
    st.title("**AK: REALLY**")
    st.image("https://media.tenor.com/RS_GviUBBkQAAAAM/sad-anime-boy-sad-eyes.gif")
    
    if st.button("SIM: JK I DO ❤️"):
        st.session_state.scene = "yapping"
        st.rerun()

    if st.button("SIM: I DONT KNOW"):
        st.session_state.scene = "pleading_2"
        st.rerun()
def pleading_scene2():
    st.title("**AK: PAKKA**")
    st.image("https://i.pinimg.com/originals/e2/6b/a5/e26ba56bb9d602304eeab73f4f0a6933.gif")
    if st.button("SIM: UFFF , I DO ❤️"):
        st.session_state.scene = "yapping"
        st.rerun()
    if st.button("SIM: I JUST DONT KNOW"):
        st.session_state.scene = "pleading3"
        st.rerun()
def pleading_scene3():
    st.title("**AK: PAKKA WALLA PAKKA**")
    st.image("https://i.pinimg.com/originals/12/97/ba/1297ba0b2945a2e7b5aad0c942ccfd71.gif")
    if st.button("SIM: UFFF , I DO ❤️"):
        st.session_state.scene = "force" 
        st.rerun()
def forcefully():
    st.title("FORCEFULLY VANAW HAI 🥺")
    st.title("LAST AND FINAL")
    st.image("https://media.tenor.com/uPXOZG2S4O0AAAAM/anime-love.gif")
    st.markdown("**AK: I LOVE YOU SIM ❤️**")
    st.markdown("**AK: DO U LOVE ME BACK**")

    if st.button("SIM: YES I DO HWWWWWWWWWWWW ❤️"):
        st.session_state.scene = "yapping"
        st.rerun() 
    if st.button("SIM: I DONT KNOW (will go back to start TOTORE 😒)"):
        st.session_state.scene = "start"
        st.session_state.intro_step = 0
        st.rerun()
def home_scene():
    st.title("**SACHII**")
    st.image("https://gifdb.com/images/high/anime-boy-mafuyu-sato-uoucoq3gpd5q24l5.gif")
    if st.button("SIM : JK I DO ❤️"):
        st.session_state.scene = "yapping"
    if st.button("SIM : SACHII I DONT KNOW"): 
        st.session_state.scene = "pleading"
        
        st.rerun()
#--------------------------------------------------------------------------------------
# Acceptance scenes
def acceptance():
    st.title("**AK: SAY IT AGAIN**")
    st.image("https://media.tenor.com/z3decH92y2gAAAAM/shy-embarrassed.gif")
    if st.button("SIM: YES I DO ❤️ U") :
        st.session_state.scene = "acceptance2"
        st.rerun()

def acceptance2():
    st.title("**AK: AGAIN**")
    st.image("https://media1.tenor.com/m/cDQNKjfsXGkAAAAC/vnc-vanitas.gif")
    if st.button("SIM: 🤍 U"):
        st.session_state.scene = "acceptance3"
        st.rerun()


def acceptance3():
    st.title("**AK: LAST TIME**")
    st.image("https://c.tenor.com/t7_iTN0iYekAAAAd/tenor.gif")
    if st.button("SIM: I LOVE YOU ❤️"):
        st.session_state.scene = "acceptance4"
        st.rerun()

def acceptance4():
    st.title("**AK: Ah , VAYO VAYO ,**")
    st.image("https://gifsec.com/wp-content/uploads/2022/11/love-anime-gif-11.gif")
    st.markdown("**AK: LOVE YOU  2 SIM**")
    if st.button("**SIM : OKAY**"):
        st.session_state.scene = "moving forward"
        st.rerun()

#Moving Forward ----------------------------------------------------------------------

def moving_forward():
    st.title("**AK:  MOVING FORWARD**")
    st.image("https://media.tenor.com/uXIogZmtfiYAAAAM/haru-yoshida-tonari-no-kaibutsu-kun.gif")
    st.markdown("**U Know its been a long time since we met**")
    st.markdown("**like its been 7 months , my god time just passed**")
    st.markdown("**I am so happy to have u in my life**")
    st.markdown("**I miss u so much**")
    if st.button("**SIM : OKAY**"):
        st.session_state.scene = "moving_forward2"
        st.rerun()
 
def moving_forward2():
    st.markdown("**SO I thought like since I cannot meet u in person**")
    st.markdown("**cant give u anything**")
    st.markdown("**(Am broke)**")
    st.image("https://media.tenor.com/jczQB19mnk0AAAAj/chibi-anime-boy.gif")
    st.markdown("**I thought I can give u something virtually**")
    st.markdown("**IF U LIKE IT , IF IT COUNTS , IDK**")
    if st.button("**SIM : OKAY**"):
        st.session_state.scene = "moving_forward3"
        st.rerun()
def moving_forward3():
    st.title("**So here is this**")
    st.image("https://art.pixilart.com/089afd91508f143.gif",width=200)
    st.markdown("**better keep it safe**")
    st.markdown("**LOL , SO CRINGE**")
    if st.button("**SIM : OKAY**"):
        st.session_state.scene = "moving_forward4"
        st.rerun()
def moving_forward4():
    st.image("https://media.tenor.com/sBCLip9eDcQAAAAM/hyouka.gif",width=200)
    st.markdown("**I made this game for u**")
    st.markdown("**I hope u like it**")
    st.markdown("**I hope u enjoy it**")
    st.markdown("**I hope u have fun playing it**")
    st.image("https://media.tenor.com/1b2c3g0d4e8AAAAd/anime-love.gif")
    st.markdown("**I love u so much , I miss u so much , I care for u so much**")
    if st.button("**SIM : OKAY , I LOVE U TOO ❤️**"):
        st.session_state.scene = "moving_forward5"
        st.rerun()

def moving_forward5():
    st.image("https://i.pinimg.com/originals/b2/1e/eb/b21eebc40e9fb6b52d08aaa60216bea3.gif")
    st.markdown("DAMN , I CANT BELIEVE U MADE IT THIS FAR")
    st.markdown            ("HANDLING ALL THIS CRINGE ")
    st.markdown           ("I AM SO PROUD OF U ❤️")
    st.markdown           ("HEHE SO THIS IS THE END OF THE GAME")
    st.markdown           ("I HOPE U ENJOYED IT")
    st.markdown           (" HOPE U HAD FUN")
    st.markdown           (" HOPE I DIDNT HURT U ( I HIGHLY DOUBT IT THO)")
    st.markdown           ("THE BELLOW BUTTON GOES TO THE START SCREEN")
    st.markdown           ("DAISKI ................. ")
    if st.button("**SIM : THANKS FOR MAKING THIS GAME ❤️**"):
        st.session_state.scene = "start"
        st.balloons()
        st.session_state.intro_step = 0
        st.rerun()
scene_map = {
    "start": start_scene,
    "yapping": yapping_scene,
    "home": home_scene,
    "pleading": pleading_scene,
    "pleading_2": pleading_scene2,
    "pleading3": pleading_scene3,
    "force" : forcefully,
    "acceptance": acceptance,
    "acceptance2": acceptance2,
    "acceptance3": acceptance3,
    "acceptance4": acceptance4,
    "moving forward": moving_forward,
    "moving_forward2": moving_forward2,
    "moving_forward3": moving_forward3,
    "moving_forward4": moving_forward4,
    "moving_forward5": moving_forward5,

}

# Render current scene
scene_map[st.session_state.scene]()
