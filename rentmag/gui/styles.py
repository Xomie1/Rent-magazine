# -*- coding: utf-8 -*-
"""Design tokens and application stylesheet."""

# ── Palette ────────────────────────────────────────────────────────────────────
BG         = "#E9EBEE"
PANEL_BG   = "#F6F7F9"
PANEL_BDR  = "#E2E6EA"
CARD       = "#FFFFFF"
BORDER     = "#E2E6EA"
ACCENT     = "#1A56A0"
ACCENT2    = "#2F6FED"
SUCCESS    = "#3F8A4D"
WARN       = "#B45309"
ERROR      = "#B91C1C"
ERROR_BG   = "#FEF2F2"
WARN_BG    = "#FFFBEB"
CARD_BG    = "#FFFFFF"
TEXT1      = "#2C3A49"
TEXT2      = "#6B7787"
MUTED      = "#9AA6B3"

STEPS: list[str] = ["検出", "リネーム", "振り分け", "レタッチ", "ロゴ挿入", "JPG保存"]

# ── Stylesheet ─────────────────────────────────────────────────────────────────
QSS = f"""
* {{
    font-family: "Meiryo", "Meiryo UI", "Yu Gothic UI", "MS UI Gothic", sans-serif;
    color: {TEXT1};
}}
QMainWindow, QWidget {{ background: {BG}; }}
QDialog               {{ background: {BG}; }}

/* ── Header ─────────────────────────────────────────────────────────── */
#appHeader {{
    background: #27384A;
    border: none;
}}
#appHeader QLabel {{
    color: white;
    font-size: 18px;
    font-weight: 700;
    background: transparent;
}}

/* ── Sidebar ────────────────────────────────────────────────────────── */
#sidebar {{
    background: {PANEL_BG};
    border: 1px solid {PANEL_BDR};
    border-radius: 8px;
}}
QFrame#panel-sep {{
    background: {PANEL_BDR};
    border: none;
    max-height: 1px;
    min-height: 1px;
}}

/* ── Generic labels ─────────────────────────────────────────────────── */
QLabel {{ background: transparent; }}
QLabel#sectionTitle {{ color: #3A4757; font-size: 14px; font-weight: 700; }}
QLabel#fieldLabel   {{ color: #6B7787; font-size: 12px; }}
QLabel#stat-lbl     {{ color: {TEXT2}; font-size: 13px; }}
QLabel#stat-num     {{ font-size: 14px; font-weight: 700; }}
QLabel#pct-label    {{ color: {TEXT1}; font-size: 28px; font-weight: 800; }}
QLabel#conn-label   {{ font-size: 13px; background: transparent; }}

/* ── Right panel cards ──────────────────────────────────────────────── */
QFrame#right-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 8px;
}}
QFrame#log-frame {{
    border: 1px solid {BORDER};
    border-radius: 6px;
    background: {CARD};
}}

/* ── Buttons (generic default) ──────────────────────────────────────── */
QPushButton {{
    outline: none;
    font-size: 12px;
    padding: 6px 14px;
    border-radius: 5px;
    border: 1px solid #C7CED6;
    background: #EEF1F4;
    color: #33414F;
}}

/* run / start button */
QPushButton#runBtn {{
    background: #2563EB;
    color: #fff;
    font-size: 16px;
    font-weight: 700;
    border: none;
    border-radius: 8px;
    min-height: 44px;
}}
QPushButton#runBtn:hover    {{ background: #1D4ED8; }}
QPushButton#runBtn:disabled {{ background: #BDBDBD; color: white; border: none; }}

QPushButton#btn-pause {{
    background: #FFFFFF;
    color: #37475A;
    border: 2px solid #C2C9D2;
    border-radius: 7px;
    padding: 4px;
    font-size: 16px;
    font-weight: 700;
}}
QPushButton#btn-pause:hover    {{ background: #F1F4F8; border-color: #97A2AE; }}
QPushButton#btn-pause:disabled {{ background: {BG}; color: {MUTED}; border-color: #DDE1E7; }}

QPushButton#btn-stop {{
    background: #FFFFFF;
    color: {ERROR};
    border: 2px solid #E0B4B4;
    border-radius: 7px;
    padding: 4px;
    font-size: 14px;
    font-weight: 700;
}}
QPushButton#btn-stop:hover    {{ background: #FBEEEE; border-color: #CF8F8F; }}
QPushButton#btn-stop:disabled {{ background: {BG}; color: {MUTED}; border-color: #DDE1E7; }}

QPushButton#btn-secondary {{
    background: transparent;
    color: {TEXT1};
    border: 1px solid {BORDER};
    border-radius: 5px;
    padding: 5px 12px;
    font-size: 13px;
}}
QPushButton#btn-secondary:hover    {{ background: {CARD}; }}
QPushButton#btn-secondary:disabled {{ color: {MUTED}; border-color: {BORDER}; }}

QPushButton#btn-link {{
    background: transparent;
    color: {ACCENT2};
    border: none;
    padding: 4px 0;
    font-size: 13px;
    text-align: left;
}}
QPushButton#btn-link:hover {{ color: {ACCENT}; }}

QPushButton#btn-topbar {{
    background: rgba(255,255,255,0.12);
    color: white;
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 5px;
    padding: 5px 14px;
    font-size: 13px;
}}
QPushButton#btn-topbar:hover {{ background: rgba(255,255,255,0.22); }}

/* ── Progress bar ───────────────────────────────────────────────────── */
QProgressBar {{
    border: none;
    border-radius: 5px;
    background: #E7EBF0;
    height: 10px;
    color: transparent;
}}
QProgressBar::chunk {{
    border-radius: 5px;
    background: {ACCENT2};
}}

/* ── Table ──────────────────────────────────────────────────────────── */
QTableWidget {{
    border: none;
    background: {CARD};
    outline: none;
    gridline-color: {BORDER};
    font-size: 13px;
    selection-background-color: #DBEAFE;
    selection-color: {TEXT1};
}}
QTableWidget::item          {{ padding: 7px 12px; border-bottom: 1px solid {BORDER}; }}
QTableWidget::item:selected {{ background: #DBEAFE; color: {TEXT1}; }}
QHeaderView::section {{
    background: #F3F5F7;
    color: {TEXT2};
    border: none;
    border-right: 1px solid {BORDER};
    border-bottom: 1px solid {BORDER};
    padding: 7px 12px;
    font-size: 12px;
    font-weight: 600;
}}

/* ── Inputs ─────────────────────────────────────────────────────────── */
QComboBox {{
    border: 1px solid #D4DAE1;
    border-radius: 5px;
    padding: 5px 10px;
    background: {CARD};
    font-size: 13px;
    min-height: 28px;
}}
QComboBox:focus             {{ border-color: {ACCENT2}; }}
QComboBox::drop-down        {{ border: none; width: 14px; }}
QComboBox QAbstractItemView {{ background: {CARD}; border: 1px solid {BORDER}; font-size: 13px; }}

QLineEdit {{
    font-size: 13px;
    color: #2C3A49;
    background: #FFFFFF;
    border: 1px solid #D4DAE1;
    border-radius: 5px;
    padding: 6px 9px;
    min-height: 18px;
}}
QLineEdit:focus     {{ border-color: {ACCENT2}; }}
QLineEdit:read-only {{ background: #F9FAFB; color: {TEXT2}; }}

/* ── Scrollbars ─────────────────────────────────────────────────────── */
QScrollBar:vertical, QScrollBar:horizontal {{
    background: transparent;
}}
QScrollBar:vertical   {{ width: 6px; }}
QScrollBar:horizontal {{ height: 6px; }}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {{
    background: #BEC3CB;
    border-radius: 3px;
    min-height: 20px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    height: 0; width: 0;
}}

/* ── Dialogs ────────────────────────────────────────────────────────── */
QGroupBox {{
    border: 1px solid {BORDER};
    border-radius: 8px;
    margin-top: 12px;
    font-size: 14px;
    font-weight: 600;
    color: {ACCENT2};
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 8px;
    padding: 1px 5px;
    background: {BG};
    font-size: 14px;
    font-weight: 700;
    color: #3A4757;
}}
QRadioButton {{ spacing: 6px; background: transparent; color: {TEXT1}; font-size: 13px; }}
"""
