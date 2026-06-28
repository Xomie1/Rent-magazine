"""Design tokens and application stylesheet."""

# ── Palette ────────────────────────────────────────────────────────────────────
BG         = "#EEF0F3"       # main background
PANEL_BG   = "#E6E9EE"       # left panel
PANEL_BDR  = "#CDD1D9"       # left panel right edge
CARD       = "#FFFFFF"
BORDER     = "#D6DAE1"
ACCENT     = "#1A56A0"
ACCENT2    = "#2261B8"
SUCCESS    = "#2E7D32"
WARN       = "#B45309"
ERROR      = "#B91C1C"
ERROR_BG   = "#FEF2F2"
WARN_BG    = "#FFFBEB"
CARD_BG    = "#FFFFFF"
TEXT1      = "#1C1F26"
TEXT2      = "#55606E"
MUTED      = "#8E96A2"

STEPS = ["検出", "リネーム", "振り分け", "レタッチ", "ロゴ挿入", "JPG保存"]

# ── Stylesheet ─────────────────────────────────────────────────────────────────
QSS = f"""
* {{
    font-family: "Meiryo", "Meiryo UI", "Yu Gothic UI", "MS UI Gothic", sans-serif;
    font-size: 17px;
    color: {TEXT1};
}}
QMainWindow, QWidget   {{ background: {BG}; }}
QDialog                {{ background: {BG}; }}

/* ── Left panel ────────────────────────────────────────────────────── */
QWidget#left-panel {{
    background: {PANEL_BG};
    border-right: 1px solid {PANEL_BDR};
}}
QFrame#panel-sep {{
    background: {PANEL_BDR};
    border: none;
    max-height: 1px;
    min-height: 1px;
}}
QLabel#panel-heading {{
    color: #5A6573;
    font-size: 15px;
    font-weight: 700;
    background: transparent;
}}

/* ── Top bar ────────────────────────────────────────────────────────── */
QFrame#topbar {{
    background: #27384A;
    border: none;
}}
QLabel#topbar-title {{
    color: white;
    font-size: 20px;
    font-weight: 700;
    background: transparent;
}}
QLabel#conn-label {{ font-size: 15px; background: transparent; }}

/* ── Generic labels ─────────────────────────────────────────────────── */
QLabel {{ background: transparent; }}
QLabel#section-title {{ color: #2C3A49; font-size: 19px; font-weight: 700; }}
QLabel#field-label   {{ color: {TEXT2}; font-size: 15px; }}
QLabel#stat-lbl      {{ color: {TEXT2}; font-size: 15px; }}
QLabel#stat-num      {{ font-size: 20px; font-weight: 700; }}
QLabel#pct-label     {{ color: {TEXT1}; font-size: 39px; font-weight: 800; }}

/* ── Right panel cards ──────────────────────────────────────────────── */
QFrame#right-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 5px;
}}

/* ── Buttons ────────────────────────────────────────────────────────── */
QPushButton {{ outline: none; }}

QPushButton#btn-primary {{
    background: {ACCENT2};
    color: white;
    border: none;
    border-radius: 3px;
    padding: 9px 24px;
    font-size: 18px;
    font-weight: 600;
}}
QPushButton#btn-primary:hover    {{ background: {ACCENT}; }}
QPushButton#btn-primary:disabled {{ background: #BDBDBD; color: white; }}

QPushButton#btn-start {{
    background: #1F9D52;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 20px;
    font-size: 21px;
    font-weight: 800;
}}
QPushButton#btn-start:hover    {{ background: #18843F; }}
QPushButton#btn-start:disabled {{ background: #BDBDBD; color: white; }}

QPushButton#btn-pause {{
    background: #FFFFFF;
    color: #37475A;
    border: 2px solid #C2C9D2;
    border-radius: 8px;
    padding: 6px;
    font-size: 24px;
    font-weight: 700;
}}
QPushButton#btn-pause:hover    {{ background: #F1F4F8; border-color: #97A2AE; }}
QPushButton#btn-pause:disabled {{ background: #EEF0F3; color: #B3BAC4; border-color: #DDE1E7; }}

QPushButton#btn-stop {{
    background: #FFFFFF;
    color: {ERROR};
    border: 2px solid #E0B4B4;
    border-radius: 8px;
    padding: 6px;
    font-size: 22px;
    font-weight: 700;
}}
QPushButton#btn-stop:hover    {{ background: #FBEEEE; border-color: #CF8F8F; }}
QPushButton#btn-stop:disabled {{ background: #EEF0F3; color: #B3BAC4; border-color: #DDE1E7; }}

QPushButton#btn-secondary {{
    background: transparent;
    color: {TEXT1};
    border: 1px solid {BORDER};
    border-radius: 3px;
    padding: 8px 15px;
    font-size: 17px;
}}
QPushButton#btn-secondary:hover    {{ background: {CARD}; }}
QPushButton#btn-secondary:disabled {{ color: {MUTED}; border-color: {BORDER}; }}

QPushButton#btn-link {{
    background: transparent;
    color: {ACCENT2};
    border: none;
    padding: 5px 0;
    font-size: 15px;
    text-align: left;
}}
QPushButton#btn-link:hover {{ color: {ACCENT}; }}

QPushButton#btn-topbar {{
    background: rgba(255,255,255,0.12);
    color: white;
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 3px;
    padding: 8px 18px;
    font-size: 17px;
}}
QPushButton#btn-topbar:hover {{ background: rgba(255,255,255,0.22); }}

/* ── Progress bar ───────────────────────────────────────────────────── */
QProgressBar {{
    border: none;
    border-radius: 3px;
    background: #D1D5DB;
    height: 12px;
    color: transparent;
}}
QProgressBar::chunk {{
    border-radius: 3px;
    background: {ACCENT2};
}}

/* ── Table ──────────────────────────────────────────────────────────── */
QTableWidget {{
    border: none;
    background: {CARD};
    outline: none;
    gridline-color: {BORDER};
    font-size: 15px;
    selection-background-color: #DBEAFE;
    selection-color: {TEXT1};
}}
QTableWidget::item          {{ padding: 5px 12px; border-bottom: 1px solid {BORDER}; }}
QTableWidget::item:selected {{ background: #DBEAFE; color: {TEXT1}; }}
QHeaderView::section {{
    background: #F3F5F7;
    color: {TEXT2};
    border: none;
    border-right: 1px solid {BORDER};
    border-bottom: 1px solid {BORDER};
    padding: 6px 12px;
    font-size: 15px;
    font-weight: 600;
}}
QFrame#log-frame {{
    border: 1px solid {BORDER};
    border-radius: 4px;
    background: {CARD};
}}

/* ── Inputs ─────────────────────────────────────────────────────────── */
QComboBox {{
    border: 1px solid {BORDER};
    border-radius: 3px;
    padding: 5px 9px;
    background: {CARD};
    font-size: 17px;
    min-height: 30px;
}}
QComboBox:focus             {{ border-color: {ACCENT2}; }}
QComboBox::drop-down        {{ border: none; width: 16px; }}
QComboBox QAbstractItemView {{ background: {CARD}; border: 1px solid {BORDER}; }}

QLineEdit {{
    border: 1px solid {BORDER};
    border-radius: 3px;
    padding: 5px 9px;
    background: {CARD};
    font-size: 17px;
    min-height: 30px;
}}
QLineEdit:focus     {{ border-color: {ACCENT2}; }}
QLineEdit:read-only {{ background: #F9FAFB; color: {TEXT2}; }}
QLineEdit#prop-field         {{ border: 1px solid {BORDER}; border-radius: 3px;
                                padding: 5px 9px; background: {CARD}; font-size: 17px; }}
QLineEdit#prop-field:focus   {{ border-color: {ACCENT2}; background: #FAFCFF; }}

/* ── Scrollbars ─────────────────────────────────────────────────────── */
QScrollBar:vertical, QScrollBar:horizontal {{
    background: transparent;
}}
QScrollBar:vertical   {{ width: 8px; }}
QScrollBar:horizontal {{ height: 8px; }}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {{
    background: #BEC3CB;
    border-radius: 3px;
    min-height: 24px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    height: 0; width: 0;
}}

/* ── Dialogs ────────────────────────────────────────────────────────── */
QGroupBox {{
    border: 1px solid {BORDER};
    border-radius: 4px;
    margin-top: 14px;
    font-size: 17px;
    font-weight: 600;
    color: {ACCENT};
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 8px;
    padding: 1px 5px;
    background: {BG};
}}
QRadioButton {{ spacing: 6px; background: transparent; color: {TEXT1}; font-size: 17px; }}
"""
