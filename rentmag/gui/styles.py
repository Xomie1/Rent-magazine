# -*- coding: utf-8 -*-
"""Design tokens and application stylesheet."""

# ── Palette ────────────────────────────────────────────────────────────────────
BG         = "#E9EBEE"       # main background
PANEL_BG   = "#F6F7F9"       # left panel
PANEL_BDR  = "#E2E6EA"       # left panel right edge
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
    color: {TEXT2};
    font-size: 16px;
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
    font-size: 22px;
    font-weight: 700;
    background: transparent;
}}
QLabel#conn-label {{ font-size: 15px; background: transparent; }}

/* ── Generic labels ─────────────────────────────────────────────────── */
QLabel {{ background: transparent; }}
QLabel#section-title {{ color: {TEXT1}; font-size: 20px; font-weight: 700; }}
QLabel#field-label   {{ color: {TEXT2}; font-size: 14px; }}
QLabel#stat-lbl      {{ color: {TEXT2}; font-size: 16px; }}
QLabel#stat-num      {{ font-size: 20px; font-weight: 700; }}
QLabel#pct-label     {{ color: {TEXT1}; font-size: 39px; font-weight: 800; }}

/* ── Right panel cards ──────────────────────────────────────────────── */
QFrame#right-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 10px;
}}

/* ── Buttons ────────────────────────────────────────────────────────── */
QPushButton {{ outline: none; }}

QPushButton#btn-primary {{
    background: {ACCENT2};
    color: white;
    border: none;
    border-radius: 7px;
    padding: 9px 24px;
    font-size: 18px;
    font-weight: 600;
}}
QPushButton#btn-primary:hover    {{ background: {ACCENT}; }}
QPushButton#btn-primary:disabled {{ background: #BDBDBD; color: white; }}

QPushButton#btn-start {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3F8A4D, stop:1 #2F7A3E);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 9px 24px;
    font-size: 21px;
    font-weight: 700;
}}
QPushButton#btn-start:hover    {{ background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2F7A3E, stop:1 #265F32); }}
QPushButton#btn-start:disabled {{ background: #BDBDBD; color: white; }}

QPushButton#btn-pause {{
    background: #FFFFFF;
    color: #37475A;
    border: 2px solid #C2C9D2;
    border-radius: 10px;
    padding: 6px;
    font-size: 24px;
    font-weight: 700;
}}
QPushButton#btn-pause:hover    {{ background: #F1F4F8; border-color: #97A2AE; }}
QPushButton#btn-pause:disabled {{ background: {BG}; color: {MUTED}; border-color: #DDE1E7; }}

QPushButton#btn-stop {{
    background: #FFFFFF;
    color: {ERROR};
    border: 2px solid #E0B4B4;
    border-radius: 10px;
    padding: 6px;
    font-size: 22px;
    font-weight: 700;
}}
QPushButton#btn-stop:hover    {{ background: #FBEEEE; border-color: #CF8F8F; }}
QPushButton#btn-stop:disabled {{ background: {BG}; color: {MUTED}; border-color: #DDE1E7; }}

QPushButton#btn-secondary {{
    background: transparent;
    color: {TEXT1};
    border: 1px solid {BORDER};
    border-radius: 7px;
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
    font-size: 16px;
    text-align: left;
}}
QPushButton#btn-link:hover {{ color: {ACCENT}; }}

QPushButton#btn-topbar {{
    background: rgba(255,255,255,0.12);
    color: white;
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 7px;
    padding: 8px 18px;
    font-size: 18px;
}}
QPushButton#btn-topbar:hover {{ background: rgba(255,255,255,0.22); }}

/* ── Progress bar ───────────────────────────────────────────────────── */
QProgressBar {{
    border: none;
    border-radius: 6px;
    background: #E7EBF0;
    height: 12px;
    color: transparent;
}}
QProgressBar::chunk {{
    border-radius: 6px;
    background: {ACCENT2};
}}

/* ── Table ──────────────────────────────────────────────────────────── */
QTableWidget {{
    border: none;
    background: {CARD};
    outline: none;
    gridline-color: {BORDER};
    font-size: 16px;
    selection-background-color: #DBEAFE;
    selection-color: {TEXT1};
}}
QTableWidget::item          {{ padding: 12px 16px; border-bottom: 1px solid {BORDER}; }}
QTableWidget::item:selected {{ background: #DBEAFE; color: {TEXT1}; }}
QHeaderView::section {{
    background: #F3F5F7;
    color: {TEXT2};
    border: none;
    border-right: 1px solid {BORDER};
    border-bottom: 1px solid {BORDER};
    padding: 11px 16px;
    font-size: 15px;
    font-weight: 600;
}}
QFrame#log-frame {{
    border: 1px solid {BORDER};
    border-radius: 8px;
    background: {CARD};
}}

/* ── Inputs ─────────────────────────────────────────────────────────── */
QComboBox {{
    border: 1px solid #D4DAE1;
    border-radius: 7px;
    padding: 9px 12px;
    background: {CARD};
    font-size: 18px;
    min-height: 42px;
}}
QComboBox:focus             {{ border-color: {ACCENT2}; }}
QComboBox::drop-down        {{ border: none; width: 16px; }}
QComboBox QAbstractItemView {{ background: {CARD}; border: 1px solid {BORDER}; }}

QLineEdit {{
    border: 1px solid #D4DAE1;
    border-radius: 7px;
    padding: 9px 12px;
    background: {CARD};
    font-size: 18px;
    min-height: 42px;
}}
QLineEdit:focus     {{ border-color: {ACCENT2}; }}
QLineEdit:read-only {{ background: #F9FAFB; color: {TEXT2}; }}
QLineEdit#prop-field         {{ border: 1px solid #D4DAE1; border-radius: 7px;
                                padding: 4px 10px; background: {CARD}; font-size: 15px;
                                min-height: 30px; }}
QLineEdit#prop-field:focus   {{ border-color: {ACCENT2}; background: #FAFCFF; }}

/* ── Scrollbars ─────────────────────────────────────────────────────── */
QScrollBar:vertical, QScrollBar:horizontal {{
    background: transparent;
}}
QScrollBar:vertical   {{ width: 8px; }}
QScrollBar:horizontal {{ height: 8px; }}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {{
    background: #BEC3CB;
    border-radius: 4px;
    min-height: 24px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    height: 0; width: 0;
}}

/* ── Dialogs ────────────────────────────────────────────────────────── */
QGroupBox {{
    border: 1px solid {BORDER};
    border-radius: 10px;
    margin-top: 14px;
    font-size: 18px;
    font-weight: 600;
    color: {ACCENT2};
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
