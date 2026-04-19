import streamlit as st
import pandas as pd

# =========================================================
# 0) APP SETTINGS  Hier sind Informationen über die Startseite des Spiels
# =========================================================

# =========================================================
# 1) DESIGN (CSS)  Hier sind die Designs der App aufgeführt
# =========================================================
st.markdown("""
<style>
/* --- App Hintergrund --- */
.stApp {
    background-color: #FFB3D1;
}

/* --- Globale Textfarben --- */
h1, p, span, div {
    color: #4B0082 !important;
}

/* --- Standard Cards --- */
.cute-card {
    background-color: #FFE4F1;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 12px;
}
.result-card {
    background-color: #E6F7FF;
    padding: 15px;
    border-radius: 20px;
    margin-bottom: 10px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.06);
}
.hint-card {
    background-color: #F3E8FF;
    padding: 12px 14px;
    border-radius: 18px;
    margin-bottom: 10px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.06);
}

/* --- Standard Buttons --- */
div.stButton > button {
    background-color: #FFD6E8;
    color: #4B0082 !important;
    border-radius: 22px;
    border: none;
    padding: 0.6em 1.1em;
    font-weight: 700;
}
div.stButton > button:hover {
    background-color: #4B0082;
    color: white !important;
}

/* --- Sticky App Header --- */
.app-header {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(255, 179, 209, 0.95);
    backdrop-filter: blur(8px);
    padding: 10px 6px 12px 6px;
    border-bottom: 1px solid rgba(0,0,0,0.05);
    margin-bottom: 10px;
}
.header-row {
    display: flex;
    gap: 10px;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
}
.header-left {
    display: flex;
    gap: 10px;
    align-items: center;
    flex-wrap: wrap;
}
.header-pill {
    background-color: #F3E8FF;
    border-radius: 999px;
    padding: 6px 12px;
    display: inline-block;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08);
    font-weight: 800;
    color: #4B0082 !important;
}
.header-score {
    background-color: #E6F7FF;
    border-radius: 999px;
    padding: 6px 12px;
    display: inline-block;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08);
    font-weight: 800;
    color: #4B0082 !important;
}
.app-header div.stButton > button {
    background-color: #FFE4F1 !important;
    color: #4B0082 !important;
    border-radius: 999px !important;
    padding: 0.45em 1.0em !important;
    font-weight: 800 !important;
    border: none !important;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08) !important;
}
.app-header div.stButton > button:hover {
    background-color: #4B0082 !important;
    color: white !important;
}

/* --- Laborstationen im Lab-Screen --- */
.station-card {
    background: #FFE4F1;
    border-radius: 26px;
    padding: 20px 18px;
    box-shadow: 0px 8px 18px rgba(0,0,0,0.08);
    border: 1px solid rgba(75, 0, 130, 0.08);
    min-height: 260px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: left;
}
.station-icon {
    font-size: 34px;
    margin-bottom: 8px;
}
.station-title {
    font-weight: 900;
    font-size: 20px;
    line-height: 1.2;
    margin-bottom: 10px;
    color: #4B0082 !important;
}
.station-sub {
    font-size: 15px;
    line-height: 1.65;
    color: #6A3FA0 !important;
    margin-bottom: 14px;
}
.station-badge {
    display: inline-block;
    background: #E6F7FF;
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 800;
    color: #4B0082 !important;
    width: fit-content;
    margin-top: auto;
}
.station-wrap {
    margin-bottom: 14px;
}

/* --- Cute Agar + Mikroskop Screens --- */
.screen-box {
    background-color: #FFF0F7;
    border-radius: 28px;
    padding: 20px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}
.plate-card {
    background: #FFE4F1;
    border-radius: 999px;
    width: 180px;
    height: 180px;
    margin: 0 auto 12px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: inset 0 0 0 8px rgba(255,255,255,0.4),
                0px 8px 18px rgba(0,0,0,0.08);
    font-size: 56px;
}
.plate-label {
    text-align: center;
    font-weight: 800;
    font-size: 18px;
    margin-bottom: 8px;
    color: #4B0082 !important;
}
.microscope-box {
    background: #E6F7FF;
    border-radius: 28px;
    padding: 24px;
    text-align: center;
    box-shadow: 0px 8px 18px rgba(0,0,0,0.08);
    margin-bottom: 16px;
}
.gram-step-card {
    background: #F3E8FF;
    border-radius: 20px;
    padding: 16px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
    margin-bottom: 10px;
    min-height: 120px;
}
.gram-step-title {
    font-weight: 800;
    margin-bottom: 8px;
    color: #4B0082 !important;
}
.big-emoji {
    font-size: 44px;
    margin-bottom: 10px;
    display: block;
}
.path-card {
    background: #FFF7D6;
    border-radius: 18px;
    padding: 12px 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    margin-top: 10px;
    margin-bottom: 14px;
    color: #4B0082 !important;
}
            
/* --- Laborjournal --- */
.journal-card {
    background: #FFF8DC;
    border-radius: 22px;
    padding: 18px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.08);
    border: 2px dashed #E6CFA7;
    margin-bottom: 14px;
}
.journal-title {
    font-weight: 900;
    font-size: 20px;
    margin-bottom: 12px;
    color: #4B0082 !important;
}
.journal-section {
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 6px;
    color: #4B0082 !important;
}
.journal-entry {
    margin-left: 10px;
    margin-bottom: 4px;
    font-size: 14px;
    color: #5A2D82 !important;
}            
</style>
""", unsafe_allow_html=True)

# =========================================================
# 2) SESSION STATE
# =========================================================
if "screen" not in st.session_state:
    st.session_state.screen = "home"

if "score" not in st.session_state:
    st.session_state.score = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = None

default_unlocked = {
    "Mikroskop": False,
    "Kultur & Tests": False,
    "Blutanalyse": False,
}

if "unlocked" not in st.session_state or set(st.session_state.unlocked.keys()) != set(default_unlocked.keys()):
    st.session_state.unlocked = default_unlocked.copy()

if "case" not in st.session_state:
    st.session_state.case = "Fall 1"

if "selected_plate" not in st.session_state:
    st.session_state.selected_plate = None

if "gram_steps" not in st.session_state:
    st.session_state.gram_steps = []

if "gram_result" not in st.session_state:
    st.session_state.gram_result = None

if "selected_blood_param" not in st.session_state:
    st.session_state.selected_blood_param = None
if "lab_journal" not in st.session_state:
    st.session_state.lab_journal = {
        "Mikroskop": [],
        "Kultur & Tests": [],
        "Blutanalyse": []
    }

if "show_help" not in st.session_state:
    st.session_state.show_help = False

if "gram_done" not in st.session_state:
    st.session_state.gram_done = False

if "selected_plate" not in st.session_state:
    st.session_state.selected_plate = None

# =========================================================
# 3) FALLDATEN Hier sind alle Falldaten aufgeführt (Patientanakten)
# =========================================================
cases = {
    "Fall 1": {"Name": "Britney McAdams", "Alter": 26, "Geschlecht": "weiblich", "Symptome": "Fieber, Schüttelfrost, Verwirrtheit"},
    "Fall 2": {"Name": "Lukas Meier", "Alter": 55, "Geschlecht": "männlich", "Symptome": "Brustschmerzen, Atemnot"},
    "Fall 3": {"Name": "Sara Keller", "Alter": 24, "Geschlecht": "weiblich", "Symptome": "Übelkeit, Bauchschmerzen"},
    "Fall 4": {"Name": "Tim Weber", "Alter": 33, "Geschlecht": "männlich", "Symptome": "Juckreiz, Bauchschmerzen nach Reise"},
    "Fall 5": {"Name": "Clara Huber", "Alter": 72, "Geschlecht": "weiblich", "Symptome": "Rötung um Katheterstelle"},
    "Fall 6": {"Name": "Kelly Keller", "Alter": 29, "Geschlecht": "weiblich", "Symptome": "Husten, Müdigkeit"},
}

# Mikroskopischer Test bei jedem Patient
lab_info = {
    "Fall 1": {"Mikroskop": "Diff-BB: Neutrophilie, Linksverschiebung möglich.",
               "Agarplatte": "Wachstum auf Kulturmedien erwartet.",
               "Blutprobe": "Entzündungszeichen passend zu bakterieller Infektion."},
    "Fall 2": {"Mikroskop": "Kettenbild passend zu grampositiven Kokken möglich.",
               "Agarplatte": "β-Hämolyse wäre ein wichtiger Hinweis.",
               "Blutprobe": "Entzündungszeichen passend zu Infektion."},
    "Fall 3": {"Mikroskop": "Stäbchen wären passend.",
               "Agarplatte": "MAC wäre besonders spannend.",
               "Blutprobe": "Leichte Entzündungszeichen möglich."},
    "Fall 4": {"Mikroskop": "Keine Bakterien zu sehen.",
               "Agarplatte": "Wachstum möglich, aber weniger aggressiv.",
               "Blutprobe": "Eosinophilie wäre ein zentraler Hinweis."},
    "Fall 5": {"Mikroskop": "Kokken sind sichtbar.",
               "Agarplatte": "Standardplatten wenig hilfreich.",
               "Blutprobe": "Erhöhte Entzündungszeichen."},
    "Fall 6": {"Mikroskop": "Sprosszellen oder Hyphen möglich.",
               "Agarplatte": "Pilzwachstum könnte sichtbar sein.",
               "Blutprobe": "Unspezifische Entzündungszeichen."},
}
# Agar-Ergebnisse pro Fall (COS / MAC / CNA)
micro_tests = {
    "Fall 1": {"Gram": "Gram-positiv, Kokken in Haufen", "Katalase": "positiv", "Koagulase": "positiv", "Hämolyse": "β-Hämolyse möglich"},
    "Fall 2": {"Gram": "Gram-positiv, Kokken in Ketten", "Katalase": "negativ", "Koagulase": "nicht sinnvoll", "Hämolyse": "β-Hämolyse"},
    "Fall 3": {"Gram": "Gram-negativ, Stäbchen", "Katalase": "nicht zentral", "Koagulase": "nicht sinnvoll", "Hämolyse": "nicht zentral"},
    "Fall 4": {"Gram": "Nicht sinnvoll", "Katalase": "nicht sinnvoll", "Koagulase": "nicht sinnvoll", "Hämolyse": "nicht sinnvoll"},
    "Fall 5": {"Gram": "Gram-positiv", "Katalase": "negativ", "Koagulase": "negativ", "Hämolyse": "leichte Hämolyse"},
    "Fall 6": {"Gram": "Nicht typisch / Pilzverdacht", "Katalase": "nicht primär", "Koagulase": "nicht primär", "Hämolyse": "nicht typisch"},
}
# beschreibt die Mikroskopischen Eindrücke pro Fall, die angezeigt werden, wenn die Spieler die Mikroskop-Station öffnen. Es enthält auch den Pfad zu einem Bild, das den mikroskopischen Eindruck visualisiert. Diese Bilder sollten in einem Ordner "images" im selben Verzeichnis wie die App liegen.
#Aufzeigen der Mikroskopischen Bildern
microscope_info = {
    "Fall 1": {
        "view": "Grampositive Kokken in Haufen. Das spricht eher für Staphylokokken.",
        "gram_type": "Gram-positiv",
        "image": "images/fall1_mikro.png",
        "sample": "Probe: Eiter aus einer Hautabszess-Läsion."
    },
    "Fall 2": {
        "view": "Grampositive Kokken in Ketten. Das spricht eher für Streptokokken.",
        "gram_type": "Gram-positiv",
        "image": "images/fall2_mikro.png",
        "sample": "Probe: Rachenabstrich."
    },
    "Fall 3": {
        "view": "Gramnegative Stäbchen sind sichtbar.",
        "gram_type": "Gram-negativ",
        "image": "images/fall3_mikro.png",
        "sample": "Probe: Mittelstrahlurin."
    },
    "Fall 4": {
        "view": "Auffälliges, strukturiertes Ei, passend zu einem Helminthen.",
        "gram_type": "Nicht sinnvoll",
        "image": "images/fall4_mikro.png",
        "sample": "Probe: Stuhlprobe."
    },
    "Fall 5": {
        "view": "Grampositive Kokken erkennbar.",
        "gram_type": "Gram-positiv, aber unspezifisch",
        "image": "images/fall5_mikro.png",
        "sample": "Probe: Liquor."
    },
    "Fall 6": {
        "view": "Sprosszellen und Hyphen, vereinbar mit einem Hefepilz.",
        "gram_type": "Nicht typisch / Pilzverdacht",
        "image": "images/fall6_mikro.png",
        "sample": "Probe: Vaginalabstrich."
    }
}

# Referenzwerte f¨r Blutprobe zur Interpretation
REF = {
    "CRP (mg/L)": (0, 5),
    "PCT (ng/mL)": (0, 0.05),
    "Leukos (G/L)": (4, 10),
    "Troponin (ng/L)": (0, 14),
    "Glukose (mmol/L)": (3.9, 5.6),
    "pH (BGA)": (7.35, 7.45),
    "Laktat (mmol/L)": (0.5, 2.0),
}
# Referenzwerte Differentialblutbild
REF_BLOOD_DIFF = {
    "Leukozyten (G/L)": (4, 10),
    "Neutrophile (%)": (40, 75),
    "Lymphozyten (%)": (20, 45),
    "Eosinophile (%)": (0, 6)
}
# Werte für die Blurprobenscreening
blood_values = {
    "Fall 1": {"CRP (mg/L)": 180, "PCT (ng/mL)": 8.5, "Leukos (G/L)": 18, "Laktat (mmol/L)": 4.2, "pH (BGA)": 7.28},
    "Fall 2": {"CRP (mg/L)": 95, "Leukos (G/L)": 14},
    "Fall 3": {"CRP (mg/L)": 35, "Leukos (G/L)": 12},
    "Fall 4": {"CRP (mg/L)": 8, "Leukos (G/L)": 8},
    "Fall 5": {"CRP (mg/L)": 4, "Leukos (G/L)": 9},
    "Fall 6": {"CRP (mg/L)": 20, "Leukos (G/L)": 10},
}
# Werte für das Weisse blutbild
blood_diff = {
    "Fall 1": {"Leukozyten (G/L)": 14, "Neutrophile (%)": 82, "Lymphozyten (%)": 12, "Eosinophile (%)": 1},
    "Fall 2": {"Leukozyten (G/L)": 13, "Neutrophile (%)": 78, "Lymphozyten (%)": 15, "Eosinophile (%)": 1},
    "Fall 3": {"Leukozyten (G/L)": 12, "Neutrophile (%)": 74, "Lymphozyten (%)": 18, "Eosinophile (%)": 1},
    "Fall 4": {"Leukozyten (G/L)": 8, "Neutrophile (%)": 60, "Lymphozyten (%)": 30, "Eosinophile (%)": 2},
    "Fall 5": {"Leukozyten (G/L)": 9, "Neutrophile (%)": 45, "Lymphozyten (%)": 25, "Eosinophile (%)": 18},
    "Fall 6": {"Leukozyten (G/L)": 10, "Neutrophile (%)": 55, "Lymphozyten (%)": 30, "Eosinophile (%)": 6},
}
# Erklärungstexte für Blutbild-Werte als Hilfestellung
blood_explanations = {
    "Leukozyten (G/L)": "Leukozyten sind weisse Blutkörperchen. Erhöhte Werte sprechen oft für eine Entzündung oder Infektion.",
    "Neutrophile (%)": "Neutrophile sind oft bei bakteriellen Infektionen erhöht.",
    "Lymphozyten (%)": "Lymphozyten sind häufig bei viralen Infektionen erhöht.",
    "Eosinophile (%)": "Eosinophile können bei Parasiten oder allergischen Reaktionen erhöht sein."
}

# Agar-Ergebnisse pro Fall (COS / MAC / CNA)
agar_results = {
    "Fall 1": {
        "COS": "Wachstum vorhanden, helle Kolonien, Hämolyse sichtbar.",
        "MAC": "Kein Wachstum.",
        "CNA": "Deutliches Wachstum mit Hämolyse."
    },
    "Fall 2": {
        "COS": "Deutliches Wachstum mit β-Hämolyse.",
        "MAC": "Kein Wachstum.",
        "CNA": "Wachstum vorhanden."
    },
    "Fall 3": {
        "COS": "Wachstum vorhanden.",
        "MAC": "Starkes Wachstum vorhanden.",
        "CNA": "Kein Wachstum."
    },
    "Fall 4": {
        "COS": "Kein Wachstum.",
        "MAC": "Kein Wachstum.",
        "CNA": "Wachstum vorhanden."
    },
    "Fall 5": {
        "COS": "leichtes Wachstum.",
        "MAC": "Kein Wachstum.",
        "CNA": "leichtes Wachstum."
    },
    "Fall 6": {
        "COS": "Mögliches atypisches Wachstum.",
        "MAC": "Kein Wachstum.",
        "CNA": "Kein Wachstum."
    }
}

# Mikroskopischer Eindruck + Gram-Ziel pro Fall
gram_data = {
    "Fall 1": "Gram-positiv, Kokken in Haufen",
    "Fall 2": "Gram-negativ, Stäbchen",
    "Fall 3": "Gram-positiv, Ketten",
    "Fall 4": "Keine Bakterien, aber auffällige Strukturen",
    "Fall 5": "Gram-positiv, Kokken",
    "Fall 6": "Pilzstrukturen sichtbar"
}
# Die Lösungen alles Fälle
solutions = {
    "Fall 1": "Staphylococcus aureus",
    "Fall 2": "Streptococcus pyogenes",
    "Fall 3": "Escherichia coli",
    "Fall 4": "Helmintheninfektion",
    "Fall 5": "Staphylococcus epidermidis",
    "Fall 6": "Candida spp.",
}
# Hier sind die Diagnoseoptionen, die in der Auswahlbox angezeigt werden. Sie sollten alle möglichen Diagnosen enthalten, damit die Spieler eine Auswahl treffen können. Einige Fälle sind als Verwirrung hier
DIAG_CHOICES = [
    "Staphylococcus aureus",
    "Staphylococcus epidermidis",
    "Streptococcus pyogenes",
    "Escherichia coli",
    "Klebsiella pneumoniae",
    "Pseudomonas aeruginosa",
    "Candida spp.",
    "Virale Infektion (z.B. Influenza)",
    "EBV / Mononukleose",
    "Allergische Reaktion / Hypersensitivität",
    "Helmintheninfektion",
    "Giardiasis (Protozoen)",
    "Akutes Koronarsyndrom",
    "Pneumonie (bakteriell)",
    "Pneumonie (viral)",
    "Diabetische Ketoazidose",
    "Gastroenteritis (bakteriell)",
    "Gastroenteritis (viral)",
    "Unklar",
]

# =========================================================
# 4) HELPER FUNCTIONS, z.Bsp. für die Interpretation von Blutwerten oder Mikrotests
# =========================================================
def flag(value, low, high):
    if value < low:
        return "↓"
    if value > high:
        return "↑"
    return "✓"

def interpret_blood(diff: dict) -> list[str]:
    hints = []
    neut = float(diff.get("Neutrophile (%)", 0))
    lymph = float(diff.get("Lymphozyten (%)", 0))
    eos = float(diff.get("Eosinophile (%)", 0))

    if neut >= 70:
        hints.append("🧠 Neutrophile ↑ → spricht eher für **bakterielle** Ursache (akut).")
    if lymph >= 45:
        hints.append("🧠 Lymphozyten ↑ → spricht eher für **virale** Ursache.")
    if eos >= 6:
        hints.append("🧠 Eosinophile ↑ → spricht für **Parasiten** oder **Allergie/Überempfindlichkeit**.")
    if not hints:
        hints.append("🧠 Differentialblutbild: kein klarer Hinweis → Kontext/weitere Tests wichtig.")
    return hints

def interpret_micro(mt: dict) -> list[str]:
    hints = []
    gram = mt.get("Gram", "").lower()
    kat = mt.get("Katalase", "").lower()
    koa = mt.get("Koagulase", "").lower()

    if "gram-positiv" in gram and "kokken" in gram and "haufen" in gram and "positiv" in kat:
        hints.append("🧠 Gram+ Kokken in Haufen + Katalase+ → **Staphylokokken**.")
        if "positiv" in koa:
            hints.append("🧠 Koagulase+ → Hinweis auf **Staphylococcus aureus**.")
        elif "negativ" in koa:
            hints.append("🧠 Koagulase− → eher **Staphylococcus epidermidis**.")

    if "ketten" in gram and "negativ" in kat:
        hints.append("🧠 Gram+ Kokken in Ketten + Katalase− → Hinweis auf **Streptokokken**.")

    if not hints:
        hints.append("🧠 Mikrotests: kein eindeutiger Shortcut → Kultur/weitere Schritte beachten.")
    return hints

def reset_gram_game():
    st.session_state.gram_steps = []
    st.session_state.gram_result = None

# =========================================================
# 5) SCREENS  Hier wird definiert, was auf den verschiedenen Screens angezeigt wird (Home, Level-Auswahl, Labor, etc.)
# =========================================================

# -------------------------
# HOME SCREEN 
# -------------------------
if st.session_state.screen == "home":
    st.title("🧪 Lab Diagnose Game 🎀")
    st.write("Willkommen im biomedizinischen Labor!")

    st.markdown(f"""
    <div class="hint-card">
    🎯 <b>Score:</b> {st.session_state.score}
    </div>
    """, unsafe_allow_html=True)

    if st.button("Start", key="start_home"):
        st.session_state.screen = "level"
        st.session_state.selected_plate = None
        st.rerun()

# -------------------------
# LEVEL SCREEN, Hier sollte die Aufführung alles Fälle sein, damit die Spieler einen Fall auswählen können. Es sollte auch der aktuelle Score angezeigt werden.
# -------------------------
elif st.session_state.screen == "level":
    st.title("Fall auswählen")

    st.markdown(f"""
    <div class="hint-card">
    🎯 <b>Score:</b> {st.session_state.score}
    </div>
    """, unsafe_allow_html=True)

    order = ["Fall 1 - Schwerer Infekt mit Fieber", "Fall 2 - Akute Halsentzündung", "Fall 3 - Verdacht auf Harnwegsinfekt", "Fall 4 - Gastrointestinale Beschweerden", "Fall 5 - Infektion an Kathetherstelle", "Fall 6 - Verdacht auf Infektion"]
    cols = st.columns(3)

    for i, f in enumerate(order):
        with cols[i % 3]:
            if st.button(f, key=f"btn_{f}"):
                st.session_state.case = f
                st.session_state.screen = "lab"
                st.session_state.feedback = None
                st.session_state.selected_plate = None
                reset_gram_game()
                st.rerun()

    if st.button("🔙 Zurück", key="back_level"):
        st.session_state.screen = "home"
        st.rerun()

# -------------------------
# LAB SCREEN zur Fallbearbeitung, hier sollten die Patientendaten, die Auswahl der Laborstationen und die Diagnoseoptionen angezeigt werden. Je nachdem, welche Laborstationen freigeschaltet wurden, sollten die entsprechenden Ergebnisse/Hinweise angezeigt werden. Es sollte auch die Möglichkeit geben, zur Level-Auswahl zurückzukehren.
# -------------------------
elif st.session_state.screen == "lab":
    case = st.session_state.case
    data = cases[case]

    # reset unlocked + feedback bei Fallwechsel
    if "last_case" not in st.session_state or st.session_state.last_case != case:
        st.session_state.unlocked = {
            "Mikroskop": False,
            "Kultur & Tests": False,
            "Blutanalyse": False
        }
        st.session_state.lab_journal = {
            "Mikroskop": [],
            "Kultur & Tests": [],
            "Blutanalyse": []
        }
        st.session_state.gram_done = False
        st.session_state.last_case = case
        st.session_state.feedback = None
        st.session_state.selected_plate = None
        st.session_state.selected_blood_param = None
        reset_gram_game()

    # Sticky Header mit Fallname und Score + Zurück-Button
    st.markdown('<div class="app-header">', unsafe_allow_html=True)
    st.markdown('<div class="header-row"><div class="header-left">', unsafe_allow_html=True)

    if st.button("← Zurück", key=f"header_back_{case}"):
        st.session_state.screen = "level"
        st.rerun()

    st.markdown(f'<div class="header-pill">🧪 {case}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="header-score">🎯 Score: {st.session_state.score}</div>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

    left, right = st.columns([0.85, 1.7], gap="large")

    # ---------- LEFT ----------
    with left:
        st.markdown(f"""
        <div class="cute-card">
        <h4>📄 Patientenakte</h4>
        <b>Name:</b> {data["Name"]}<br>
        <b>Alter:</b> {data["Alter"]}<br>
        <b>Geschlecht:</b> {data["Geschlecht"]}<br>
        <b>Symptome:</b> {data["Symptome"]}
        </div>
        """, unsafe_allow_html=True)

        st.subheader("🧠 Diagnose (bitte wählen)")
        diag_options = ["— bitte wählen —"] + DIAG_CHOICES

        with st.form(key=f"diag_form_{case}", clear_on_submit=False):
            diagnosis = st.selectbox(
                "Was ist am wahrscheinlichsten?",
                diag_options,
                index=0,
                key=f"diag_{case}"
            )
            submitted = st.form_submit_button("✅ Diagnose abgeben")

        if submitted:
            if diagnosis == "— bitte wählen —":
                st.session_state.feedback = {
                    "type": "warning",
                    "msg": "Bitte zuerst eine Diagnose auswählen 🙂"
                }
            else:
                if diagnosis == solutions[case]:
                    st.session_state.score += 10
                    st.session_state.feedback = {
                        "type": "success",
                        "msg": "✅ Richtig! +10 Punkte"
                    }
                else:
                    st.session_state.score -= 5
                    st.session_state.feedback = {
                        "type": "error",
                        "msg": f"❌ Falsch. Richtige Lösung: {solutions[case]} (-5 Punkte)"
                    }
            st.rerun()

        fb = st.session_state.get("feedback")
        if fb:
            if fb["type"] == "success":
                st.success(fb["msg"])
            elif fb["type"] == "error":
                st.error(fb["msg"])
            else:
                st.warning(fb["msg"])

    # ---------- RIGHT ----------
        # ---------- RIGHT ----------
    with right:
        top1, top2 = st.columns([6, 1])

        with top1:
            st.subheader("🔬 Laborstationen")

        with top2:
            if st.button("❓", key="help_lab"):
                st.session_state.show_help = not st.session_state.show_help

        if st.session_state.show_help:
            st.markdown("""
            <div class="hint-card">
            <b>🧪 So funktioniert das Spiel:</b><br><br>
            1. Wähle einen Fall aus und lies die Patientenakte.<br>
            2. Öffne Laborstationen und sammle Befunde.<br>
            3. Übernimm wichtige Resultate ins Laborjournal.<br>
            4. Nutze das Journal, um die wahrscheinlichste Diagnose auszuwählen.<br><br>

            <b>🔬 Laborstationen:</b><br>
            • <b>Mikroskop</b>: Morphologie und Gram-Färbung<br>
            • <b>🧫 Kultur & Tests</b>: Agarplatten, Katalase, Koagulase, Hämolyse<br>
            • <b>🩸 Blutanalyse</b>: Blutwerte und Differentialblutbild<br><br>

            <b>🎯 Ziel:</b><br>
            Kombiniere die Befunde richtig und finde die passende Diagnose.
            </div>
            """, unsafe_allow_html=True)

        st.write("Tippe, um Stationen freizuschalten:")

        cols = st.columns(3, gap="medium")

        with cols[0]:
            st.markdown(f"""
            <div class="station-wrap">
                <div class="station-card">
                    <div>
                        <div class="station-icon">🔬</div>
                        <div class="station-title">Mikroskop</div>
                        <div class="station-sub">
                            Gram-Färbung<br>
                            Morphologie
                        </div>
                    </div>
                    <div class="station-badge">{'✅ freigeschaltet' if st.session_state.unlocked['Mikroskop'] else '🔒 noch zu öffnen'}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Mikroskop öffnen", key=f"open_mic_{case}", use_container_width=True):
                st.session_state.unlocked["Mikroskop"] = True
                st.session_state.screen = "mikroskop"
                reset_gram_game()
                st.rerun()

        with cols[1]:
            st.markdown(f"""
            <div class="station-wrap">
                <div class="station-card">
                    <div>
                        <div class="station-icon">🧫</div>
                        <div class="station-title">Kultur & Tests</div>
                        <div class="station-sub">
                            Agarplatten<br>
                            Katalase / Koagulase
                        </div>
                    </div>
                    <div class="station-badge">{'✅ freigeschaltet' if st.session_state.unlocked['Kultur & Tests'] else '🔒 noch zu öffnen'}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Kultur & Tests öffnen", key=f"open_kultur_{case}", use_container_width=True):
                st.session_state.unlocked["Kultur & Tests"] = True
                st.session_state.screen = "agar"
                st.session_state.selected_plate = None
                st.rerun()

        with cols[2]:
            st.markdown(f"""
            <div class="station-wrap">
                <div class="station-card">
                    <div>
                        <div class="station-icon">🩸</div>
                        <div class="station-title">Blutanalyse</div>
                        <div class="station-sub">
                            CRP / PCT / Leukos<br>
                            Diff-BB / Interpretation
                        </div>
                    </div>
                    <div class="station-badge">{'✅ freigeschaltet' if st.session_state.unlocked['Blutanalyse'] else '🔒 noch zu öffnen'}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Blutanalyse öffnen", key=f"open_blut_{case}", use_container_width=True):
                st.session_state.unlocked["Blutanalyse"] = True
                st.session_state.screen = "blutbild"
                st.session_state.selected_blood_param = None
                st.rerun()

        st.write("---")
        st.subheader("📓 Laborjournal")

        journal = st.session_state.lab_journal

        journal_html = """
        <div class="journal-card">
            <div class="journal-title">📓 Mein Laborheft</div>
        """

        if any(journal.values()):
            for section, entries in journal.items():
                if entries:
                    journal_html += f'<div class="journal-section">{section}</div>'
                    for entry in entries:
                        journal_html += f'<div class="journal-entry">• {entry}</div>'
        else:
            journal_html += '<div class="journal-entry">Noch keine Einträge vorhanden.</div>'

        journal_html += "</div>"

        st.markdown(journal_html, unsafe_allow_html=True)

        if not any(st.session_state.unlocked.values()):
            st.markdown("""
            <div class="hint-card">
            Noch keine Station gewählt. Tippe auf eine Station oben.
            </div>
            """, unsafe_allow_html=True)

# -------------------------
# AGAR SCREEN leitet die Agarplatte, hier können die Spieler zwischen den verschiedenen Platten wechseln (COS / MAC / CNA) und die Ergebnisse sehen, die ihnen bei der Diagnose helfen können. Es gibt auch einen Zurück-Button, um zurück zum Labor zu gelangen.
# -------------------------
elif st.session_state.screen == "agar":
    case = st.session_state.case

    st.markdown("""
    <div class="screen-box">
        <h1 style="text-align:center;">🧫 Kultur & Tests</h1>
        <p style="text-align:center;">Wähle eine Agarplatte aus und kombiniere das Wachstum mit den mikrobiologischen Schnelltests.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Zurück zum Labor", key=f"back_from_agar_{case}"):
        st.session_state.screen = "lab"
        st.rerun()

    st.markdown("""
    <div class="path-card">
    🧪 <b>Plattenübersicht:</b> COS = Kochblut, MAC = MacConkey, CNA = grampositive Selektion
    </div>
    """, unsafe_allow_html=True)

    st.subheader("1️⃣ Agarplatte auswählen")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="plate-card">🧫</div>
        <div class="plate-label">COS</div>
        """, unsafe_allow_html=True)
        if st.button("COS öffnen", key=f"plate_cos_{case}"):
            st.session_state.selected_plate = "COS"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="plate-card">🧫</div>
        <div class="plate-label">MAC</div>
        """, unsafe_allow_html=True)
        if st.button("MAC öffnen", key=f"plate_mac_{case}"):
            st.session_state.selected_plate = "MAC"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="plate-card">🧫</div>
        <div class="plate-label">CNA</div>
        """, unsafe_allow_html=True)
        if st.button("CNA öffnen", key=f"plate_cna_{case}"):
            st.session_state.selected_plate = "CNA"
            st.rerun()

    st.write("")

    # 🧠 aktuelle Auswahl holen
plate = st.session_state.get("selected_plate", None)
case = st.session_state.case

# 🖼️ Bilder
plate_images = {
    "Fall 1": {
        "COS": "images/fall1_cos.png",
        "MAC": "images/fallleer_mac.png",
        "CNA": "images/fall1_cna.png"
    },
    "Fall 2": {
        "COS": "images/fall2_cos.png",
        "MAC": "images/fallleer_mac.png",
        "CNA": "images/fall2_cna.png"
    },
    "Fall 3": {
        "COS": "images/fall3_cos.png",
        "MAC": "images/fall3_mac.png",
        "CNA": "images/fallleer_cna.png"
    },
    "Fall 4": {
        "COS": "images/fall4_cos.png",
        "MAC": "images/fallleer_mac.png",
        "CNA": "images/fall4_cna.png"
    },
    "Fall 5": {
        "COS": "images/fall5_cos.png",
        "MAC": "images/fallleer_mac.png",
        "CNA": "images/fall5_cna.png"
    },
    "Fall 6": {
        "COS": "images/fall6_cos.png",
        "MAC": "images/fallleer_mac.png",
        "CNA": "images/fallleer_cna.png"
    }
}

# 🧾 Befunde
plate_text = {
    "Fall 1": {
        "COS": "Goldene Kolonien mit β-Hämolyse",
        "MAC": "Kein Wachstum",
        "CNA": "Wachstum mit β-Hämolyse"
    },
    "Fall 2": {
        "COS": "Kleine Kolonien mit starker β-Hämolyse",
        "MAC": "Kein Wachstum",
        "CNA": "Wachstum mit β-Hämolyse"
    },
    "Fall 3": {
        "COS": "Graue Kolonien",
        "MAC": "Rosa Kolonien (Laktose+)",
        "CNA": "Kein Wachstum"
    },
    "Fall 4": {
        "COS": "Kein Wachstum",
        "MAC": "Kein Wachstum",
        "CNA": "Kein Wachstum"
    },
    "Fall 5": {
        "COS": "Weisse Kolonien ohne Hämolyse",
        "MAC": "Kein Wachstum",
        "CNA": "Wachstum ohne Hämolyse"
    },
    "Fall 6": {
        "COS": "Cremige, weissliche Kolonien",
        "MAC": "Kein Wachstum",
        "CNA": "Kaum oder kein Wachstum"
    }
}

# 🔬 ANZEIGE
if plate is not None:
    st.markdown("## 🧫 Wachstum auf der ausgewählten Platte")

    st.markdown(f"""
    <div class="result-box">
        <h3>🔎 Ausgewählte Platte: {plate}</h3>
    </div>
    """, unsafe_allow_html=True)

    image_path = plate_images[case][plate]
    text = plate_text[case][plate]

    st.image(image_path, use_container_width=True)
    st.info(text)

    if st.session_state.selected_plate:
        plate = st.session_state.selected_plate
        result = agar_results[case][plate]
        mt = micro_tests[case]

        st.subheader("2️⃣ Wachstum auf der ausgewählten Platte")
        st.markdown(f"""
        <div class="result-card">
        <h4>🔍 Ausgewählte Platte: {plate}</h4>
        {result}
        </div>
        """, unsafe_allow_html=True)

        st.subheader("3️⃣ Mikrobiologische Schnelltests")
        st.markdown(f"""
        <div class="result-card">
        <b>Gram:</b> {mt["Gram"]}<br>
        <b>Katalase:</b> {mt["Katalase"]}<br>
        <b>Koagulase:</b> {mt["Koagulase"]}<br>
        <b>Hämolyse:</b> {mt["Hämolyse"]}
        </div>
        """, unsafe_allow_html=True)

        st.subheader("4️⃣ Interpretation")
        for h in interpret_micro(mt):
            st.markdown(f"""<div class="hint-card">{h}</div>""", unsafe_allow_html=True)

        st.write("---")

        if st.button("📓 Befunde ins Laborjournal übernehmen", key=f"journal_agar_{case}"):
            mt = micro_tests[case]

            st.session_state.lab_journal["Kultur & Tests"] = []
            st.session_state.lab_journal["Kultur & Tests"].append(f"Gram: {mt['Gram']}")
            st.session_state.lab_journal["Kultur & Tests"].append(f"Katalase: {mt['Katalase']}")
            st.session_state.lab_journal["Kultur & Tests"].append(f"Koagulase: {mt['Koagulase']}")
            st.session_state.lab_journal["Kultur & Tests"].append(f"Hämolyse: {mt['Hämolyse']}")

            st.success("✅ Kultur & Tests wurden ins Journal übernommen!")

    else:
        st.markdown("""
        <div class="hint-card">
        Wähle zuerst eine Platte aus, damit Wachstum, Schnelltests und Interpretation angezeigt werden.
        </div>
        """, unsafe_allow_html=True)
# -------------------------
# MIKROSKOP SCREEN hier können die Spieler den mikroskopischen Eindruck der Probe sehen und danach die Gram-Färbung durchführen, indem sie die Schritte in der richtigen Reihenfolge auswählen. Es gibt auch einen Zurück-Button, um zurück zum Labor zu gelangen.
# -------------------------
elif st.session_state.screen == "mikroskop":
    case = st.session_state.case

    st.markdown("""
    <div class="screen-box">
        <h1 style="text-align:center;">🔬 Mikroskop</h1>
        <p style="text-align:center;">Beobachte die Probe und führe danach die Gram-Färbung durch.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Zurück zum Labor", key=f"back_from_mic_{case}"):
        st.session_state.screen = "lab"
        st.rerun()

    st.markdown(f"""
    <div class="microscope-box">
        <span class="big-emoji">🔬</span>
        <h3>Mikroskopischer Eindruck</h3>
        <p>{microscope_info[case]["view"]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎮 Gram-Färbung Mini-Spiel")
    st.write("Wähle die Schritte in der richtigen Reihenfolge:")

    c1, c2, c3, c4 = st.columns(4)

    with c3:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🟣</span>
            <div class="gram-step-title">Kristallviolett</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Wählen", key=f"cv_{case}"):
            st.session_state.gram_steps.append("Kristallviolett")
            st.rerun()

    with c1:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🧴</span>
            <div class="gram-step-title">Lugol</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Wählen", key=f"lugol_{case}"):
            st.session_state.gram_steps.append("Lugol")
            st.rerun()

    with c4:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">💧</span>
            <div class="gram-step-title">Alkohol</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Wählen", key=f"alk_{case}"):
            st.session_state.gram_steps.append("Alkohol")
            st.rerun()

    with c2:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🩷</span>
            <div class="gram-step-title">Safranin</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Wählen", key=f"saf_{case}"):
            st.session_state.gram_steps.append("Safranin")
            st.rerun()

    col_a, col_b = st.columns([3, 1])

    with col_a:
        st.markdown(f"""
        <div class="hint-card">
        <b>Deine Reihenfolge:</b> {" → ".join(st.session_state.gram_steps) if st.session_state.gram_steps else "Noch keine Schritte gewählt."}
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        if st.button("🔄 Reset", key=f"reset_gram_{case}"):
            reset_gram_game()
            st.session_state.gram_done = False
            st.rerun()

    if len(st.session_state.gram_steps) == 4 and st.session_state.gram_result is None:
        correct_order = ["Kristallviolett", "Lugol", "Alkohol", "Safranin"]

        if st.session_state.gram_steps == correct_order:
            st.session_state.gram_result = microscope_info[case]["gram_type"]
            st.session_state.gram_done = True
        else:
            st.session_state.gram_result = "Reihenfolge nicht korrekt"
            st.session_state.gram_done = False

    if st.session_state.gram_result:
        if st.session_state.gram_result == "Reihenfolge nicht korrekt":
            st.error("❌ Die Reihenfolge war nicht korrekt. Versuch es nochmals.")
        else:
            st.success(f"✅ Ergebnis der Gram-Färbung: {st.session_state.gram_result}")

    if st.session_state.gram_done:
        st.image(
            microscope_info[case]["image"],
            caption="Mikroskopischer Befund",
            use_container_width=True
        )

        st.markdown(f"""
        <div class="hint-card">
        <b>🧪 {microscope_info[case]["sample"]}</b>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="hint-card">
        🔬 Führe zuerst die Gram-Färbung korrekt durch, damit das Präparat sichtbar wird.
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    if st.button("📓 Mikroskop-Befund ins Laborjournal übernehmen", key=f"journal_micro_{case}"):
        st.session_state.lab_journal["Mikroskop"] = []

        if st.session_state.gram_result and st.session_state.gram_result != "Reihenfolge nicht korrekt":
            st.session_state.lab_journal["Mikroskop"].append(
                f"Mikroskopischer Eindruck: {microscope_info[case]['view']}"
            )
            st.session_state.lab_journal["Mikroskop"].append(
                f"Gram-Ergebnis: {st.session_state.gram_result}"
            )
            st.success("✅ Mikroskop-Befund wurde ins Journal übernommen!")
        else:
            st.warning("Bitte führe zuerst die Gram-Färbung korrekt durch.")
# -------------------------
# BLUTBILD SCREEN
# -------------------------
elif st.session_state.screen == "blutbild":
    case = st.session_state.case
    values = blood_values[case]
    diff = blood_diff[case]

    st.markdown("""
    <div class="screen-box">
        <h1 style="text-align:center;">🩸 Blutanalyse</h1>
        <p style="text-align:center;">Beurteile die Blutwerte und das Differentialblutbild und übernimm die wichtigsten Befunde ins Laborjournal.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Zurück zum Labor", key=f"back_from_blood_{case}"):
        st.session_state.screen = "lab"
        st.rerun()

    st.markdown("""
    <div class="path-card">
    🧪 <b>Hinweis:</b> Achte auf erhöhte Entzündungswerte und auf Veränderungen im Differentialblutbild.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🧪 Blutwerte")

    for param, val in values.items():
        if param in REF:
            low, high = REF[param]
            flag_symbol = flag(val, low, high)
            st.markdown(f"""
            <div class="result-card">
            {param}: <b>{val}</b> (Ref: {low}–{high}) <b>{flag_symbol}</b>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card">
            {param}: <b>{val}</b>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.subheader("🩸 Differentialblutbild")

    for param, val in diff.items():
        if param in REF_BLOOD_DIFF:
            low, high = REF_BLOOD_DIFF[param]
            flag_symbol = flag(val, low, high)
            st.markdown(f"""
            <div class="result-card">
            {param}: <b>{val}</b> (Ref: {low}–{high}) <b>{flag_symbol}</b>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card">
            {param}: <b>{val}</b>
            </div>
            """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("🧾 Interpretation")

    for h in interpret_blood(diff):
        st.markdown(f"""<div class="hint-card">{h}</div>""", unsafe_allow_html=True)

    st.write("---")

    if st.button("📓 Ins Laborjournal übernehmen", key=f"journal_blood_{case}"):
        st.session_state.lab_journal["Blutanalyse"] = []

        for param, val in values.items():
            st.session_state.lab_journal["Blutanalyse"].append(f"{param}: {val}")

        for param, val in diff.items():
            st.session_state.lab_journal["Blutanalyse"].append(f"{param}: {val}")

        st.success("✅ Blutanalyse wurde ins Laborjournal übernommen!")