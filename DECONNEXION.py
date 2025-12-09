import streamlit as st

# --- Configuration de la page
st.set_page_config(page_title="Login", page_icon="🔐", layout="wide")

# --- Initialisation session_state
if "auth" not in st.session_state:
    st.session_state.auth = False
if "username" not in st.session_state:
    st.session_state.username = ""

# --- CSS personnalisé
st.markdown("""
<style>
/* Fond de la page */
body {
    background-color: #f0f4f8;
}

.stApp {
     background: url('https://images.unsplash.com/photo-1557683316-973673baf926') !important;
    background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }

/* Titre */
.login-title {
    font-size: 32px;
    font-weight: 700;
    text-align: center;
    color: #2c3e50;
    margin-bottom: 10px;
}

/* Sous-titre */
.login-subtitle {
    text-align: center;
    color: #7f8c8d;
    margin-bottom: 30px;
}

/* Input stylé */
.stTextInput>div>div>input {
    border-radius: 10px;
    padding: 10px;
}

/* Bouton stylé */
.stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: #2c3e50;
    color: white;
    padding: 12px;
    font-size: 16px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #34495e;
}


/* Masquer la sidebar */
[data-testid="stSidebar"] {
    display: none !important;
}

/* Masquer le bloc de navigation multipages */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Masquer la flèche (collapse control) */
[data-testid="collapsedControl"] {
    display: none !important;
}

/* Masquer les buttons du header (hamburger, etc.) */
header [data-testid="stToolbar"] {
    display: none !important;
}

/* Masquer tout bouton d'icône */
button[title="Menu"] {
    display: none !important;
}

button[kind="icon"] {
    display: none !important;
}

/* Masquer le bouton du mode multipage */
[data-testid="stApp"] div:first-child div[role="button"] {
    display: none !important;
}
.input-container{
    width:100px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="login-card">', unsafe_allow_html=True)
st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="login-subtitle">Please enter your login details</div>', unsafe_allow_html=True)

with st.container():
# --- Inputs centrés dans un div à 50% ---
    col1, col2, col3 = st.columns([1, 2, 1])  # col2 = au centre
    with col2:
        st.markdown('<div class="input-container">', unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("password", type="password")
        left, middle, right = st.columns(3)
        login = st.button("Log in",use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

# --- Vérification login ---
if login:
    if username == "conde" and password == "621670812":
        st.session_state.auth = True
        st.session_state.username = username
        st.success("Login successful !")
        st.switch_page("pages/1_ACCUEIL.py")
    else:
        st.error("Incorrect login credentials")

st.markdown('</div>', unsafe_allow_html=True)
