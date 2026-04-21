import streamlit as st

# -------------------------
# HOME SCREEN
# -------------------------

# Falls 'screen' noch nicht existiert, hier lokal initialisieren
if "screen" not in st.session_state:
    st.session_state.screen = "home"

if st.session_state.screen == "home":
    st.title("🔬 Der Labordetektiv")

    # Begrüßung mit Persona-Bezug
    st.markdown(f"""
    <div class="cute-card">
        <h3>Willkommen im Team! 🕵️‍♀️</h3>
        <p>In diesem Labor kombinieren wir Wissenschaft mit Spürsinn. Deine Aufgabe ist es, durch präzise Analysen die richtige Diagnose für unsere Patienten zu finden.</p>
    </div>
    """, unsafe_allow_html=True)

    # Spielablauf als schicke Spalten (User Experience)
    st.subheader("Dein Weg zur Diagnose")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="hint-card" style="min-height: 10px;">
        <b>1. Akte wählen</b><br>
        Such dir einen der 6 spannenden Fälle aus.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="hint-card" style="min-height: 10px;">
        <b>2. Laborbesuch</b><br>
        Nutze Mikroskop, Agarplatten oder das Blutbild.
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="hint-card" style="min-height: 10px;">
        <b>3. Rätsel lösen</b><br>
        Kombiniere die Befunde und stelle die Diagnose.
        </div>
        """, unsafe_allow_html=True)

    # Der zentrale Start-Button
    st.write("---")
    if st.button("Jetzt Ermittlung starten! 🚀", use_container_width=True):
        st.switch_page("views/Der Labordetektiv.py")

    # Autoren dezent im Footer
    st.write("---")
    with st.expander("👥 Das Team hinter dem Labordetektiv"):
        st.markdown("""
        * **Eronita Sahiti** (sahitero@students.zhaw.ch)
        * **Lilia Totila** (totillil@students.zhaw.ch)
        * **Lia Bütikofer** (buetilia@students.zhaw.ch)
        * **Vanessa Cakoncev** (cakonvan@students.zhaw.ch)
        """)