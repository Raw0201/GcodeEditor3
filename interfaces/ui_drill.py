# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drillVasxnl.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QToolButton,
    QWidget,
)
import resources_rc


class Ui_frm_drill(object):
    def setupUi(self, frm_drill):
        if not frm_drill.objectName():
            frm_drill.setObjectName("frm_drill")
        frm_drill.resize(210, 730)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frm_drill.sizePolicy().hasHeightForWidth())
        frm_drill.setSizePolicy(sizePolicy)
        frm_drill.setMinimumSize(QSize(210, 730))
        frm_drill.setMaximumSize(QSize(210, 730))
        icon = QIcon()
        icon.addFile(":/icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        frm_drill.setWindowIcon(icon)
        frm_drill.setStyleSheet(
            "/* ---------------------------------------------------------------------------\n"
            "\n"
            "    Created by the qtsass compiler v0.1.1\n"
            "    \n"
            "    https://github.com/sommerc/pyqt-stylesheets\n"
            "\n"
            '    The definitions are in the "qdarkstyle.qss._styles.scss" module\n'
            "\n"
            "    WARNING! All changes made in this file will be lost!\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "/* QDarkStyleSheet -----------------------------------------------------------\n"
            "\n"
            "This is the main style sheet, the palette has nine colors.\n"
            "\n"
            "It is based on three selecting colors, three greyish (background) colors\n"
            "plus three whitish (foreground) colors. Each set of widgets of the same\n"
            "type have a header like this:\n"
            "\n"
            "    ------------------\n"
            "    GroupName --------\n"
            "    ------------------\n"
            "\n"
            "And each widget is separated with a header like this:\n"
            "\n"
            "    QWidgetName ------\n"
            "\n"
            "This makes more easy to find and change some css field. The basic\n"
            ""
            "configuration is described bellow.\n"
            "\n"
            "    BACKGROUND -----------\n"
            "\n"
            "        Light   (unpressed)\n"
            "        Normal  (border, disabled, pressed, checked, toolbars, menus)\n"
            "        Dark    (background)\n"
            "\n"
            "    FOREGROUND -----------\n"
            "\n"
            "        Light   (texts/labels)\n"
            "        Normal  (not used yet)\n"
            "        Dark    (disabled texts)\n"
            "\n"
            "    SELECTION ------------\n"
            "\n"
            "        Light  (selection/hover/active)\n"
            "        Normal (selected)\n"
            "        Dark   (selected disabled)\n"
            "\n"
            "If a stranger configuration is required because of a bugfix or anything\n"
            "else, keep the comment on the line above so nobody changes it, including the\n"
            "issue number.\n"
            "\n"
            "*/\n"
            "/*\n"
            "\n"
            "See Qt documentation:\n"
            "\n"
            "  - https://doc.qt.io/qt-5/stylesheet.html\n"
            "  - https://doc.qt.io/qt-5/stylesheet-reference.html\n"
            "  - https://doc.qt.io/qt-5/stylesheet-examples.html\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "/* QWidget ----------"
            "------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QWidget {\n"
            "  background-color: #19232D;\n"
            "  border: 0px solid #32414B;\n"
            "  padding: 0px;\n"
            "  color: #F0F0F0;\n"
            "  selection-background-color: #1464A0;\n"
            "  selection-color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QWidget:disabled {\n"
            "  background-color: #19232D;\n"
            "  color: #787878;\n"
            "  selection-background-color: #14506E;\n"
            "  selection-color: #787878;\n"
            "}\n"
            "\n"
            "QWidget::item:selected {\n"
            "  background-color: #1464A0;\n"
            "}\n"
            "\n"
            "QWidget::item:hover {\n"
            "  background-color: #148CD2;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "/* QMainWindow ------------------------------------------------------------\n"
            "\n"
            "This adjusts the splitter in the dock widget, not qsplitter\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QMainWindow::separator {\n"
            ""
            "  background-color: #32414B;\n"
            "  border: 0px solid #19232D;\n"
            "  spacing: 0px;\n"
            "  padding: 2px;\n"
            "}\n"
            "\n"
            "QMainWindow::separator:hover {\n"
            "  background-color: #505F69;\n"
            "  border: 0px solid #148CD2;\n"
            "}\n"
            "\n"
            "QMainWindow::separator:horizontal {\n"
            "  width: 5px;\n"
            "  margin-top: 2px;\n"
            "  margin-bottom: 2px;\n"
            '  image: url(":/qss_icons/rc/toolbar_separator_vertical.png");\n'
            "}\n"
            "\n"
            "QMainWindow::separator:vertical {\n"
            "  height: 5px;\n"
            "  margin-left: 2px;\n"
            "  margin-right: 2px;\n"
            '  image: url(":/qss_icons/rc/toolbar_separator_horizontal.png");\n'
            "}\n"
            "\n"
            "/* QToolTip ---------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtooltip\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QToolTip {\n"
            "  background-color: #ffffff;\n"
            "  border: 1px solid #19232D;\n"
            "  color: #19232D;\n"
            "  /* Remove padding, for fix combo box tooltip */\n"
            "  padding: 0px;\n"
            ""
            "  /* Remove opacity, fix #174 - may need to use RGBA */\n"
            "}\n"
            "\n"
            "/* QStatusBar -------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qstatusbar\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QStatusBar {\n"
            "  border: 1px solid #32414B;\n"
            "  /* Fixes Spyder #9120, #9121 */\n"
            "  background: #32414B;\n"
            "  /* Fixes #205, white vertical borders separating items */\n"
            "}\n"
            "\n"
            "QStatusBar::item {\n"
            "  border: none;\n"
            "}\n"
            "\n"
            "QStatusBar QToolTip {\n"
            "  background-color: #148CD2;\n"
            "  border: 1px solid #19232D;\n"
            "  color: #19232D;\n"
            "  /* Remove padding, for fix combo box tooltip */\n"
            "  padding: 0px;\n"
            "  /* Reducing transparency to read better */\n"
            "  opacity: 230;\n"
            "}\n"
            "\n"
            "QStatusBar QLabel {\n"
            "  /* Fixes Spyder #9120, #9121 */\n"
            "  background: transparent;\n"
            "}\n"
            "\n"
            "/* QGroupBox --------------------------------------------------------------\n"
            "\n"
            "https"
            "://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QGroupBox {\n"
            "  font-weight: bold;\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "  padding: 4px;\n"
            "  margin-top: 16px;\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "  subcontrol-origin: margin;\n"
            "  subcontrol-position: top left;\n"
            "  left: 3px;\n"
            "  padding-left: 3px;\n"
            "  padding-right: 5px;\n"
            "  padding-top: 8px;\n"
            "  padding-bottom: 16px;\n"
            "}\n"
            "\n"
            "QGroupBox::indicator {\n"
            "  margin-left: 2px;\n"
            "  height: 16px;\n"
            "  width: 16px;\n"
            "}\n"
            "\n"
            "QGroupBox::indicator:unchecked {\n"
            "  border: none;\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked.png");\n'
            "}\n"
            "\n"
            "QGroupBox::indicator:unchecked:hover, QGroupBox::indicator:unchecked:focus, QGroupBox::indicator:unchecked:pressed {\n"
            "  border: none;\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked_focus.png");\n'
            "}\n"
            "\n"
            "QGroupBox::indicator:unchecked:disabled "
            "{\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked_disabled.png");\n'
            "}\n"
            "\n"
            "QGroupBox::indicator:checked {\n"
            "  border: none;\n"
            '  image: url(":/qss_icons/rc/checkbox_checked.png");\n'
            "}\n"
            "\n"
            "QGroupBox::indicator:checked:hover, QGroupBox::indicator:checked:focus, QGroupBox::indicator:checked:pressed {\n"
            "  border: none;\n"
            '  image: url(":/qss_icons/rc/checkbox_checked_focus.png");\n'
            "}\n"
            "\n"
            "QGroupBox::indicator:checked:disabled {\n"
            '  image: url(":/qss_icons/rc/checkbox_checked_disabled.png");\n'
            "}\n"
            "\n"
            "/* QRadioButton -----------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qradiobutton\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QRadioButton {\n"
            "  background-color: #19232D;\n"
            "  color: #F0F0F0;\n"
            "  spacing: 4px;\n"
            "  padding: 0px;\n"
            "  border: none;\n"
            "  outline: none;\n"
            "}\n"
            "\n"
            "QRadioButton:focus {\n"
            "  border: none;\n"
            "}\n"
            "\n"
            "QRadioB"
            "utton:disabled {\n"
            "  background-color: #19232D;\n"
            "  color: #787878;\n"
            "  border: none;\n"
            "  outline: none;\n"
            "}\n"
            "\n"
            "QRadioButton QWidget {\n"
            "  background-color: #19232D;\n"
            "  color: #F0F0F0;\n"
            "  spacing: 0px;\n"
            "  padding: 0px;\n"
            "  outline: none;\n"
            "  border: none;\n"
            "}\n"
            "\n"
            "QRadioButton::indicator {\n"
            "  border: none;\n"
            "  outline: none;\n"
            "  margin-left: 4px;\n"
            "  height: 16px;\n"
            "  width: 16px;\n"
            "}\n"
            "\n"
            "QRadioButton::indicator:unchecked {\n"
            '  image: url(":/qss_icons/rc/radio_unchecked.png");\n'
            "}\n"
            "\n"
            "QRadioButton::indicator:unchecked:hover, QRadioButton::indicator:unchecked:focus, QRadioButton::indicator:unchecked:pressed {\n"
            "  border: none;\n"
            "  outline: none;\n"
            '  image: url(":/qss_icons/rc/radio_unchecked_focus.png");\n'
            "}\n"
            "\n"
            "QRadioButton::indicator:unchecked:disabled {\n"
            '  image: url(":/qss_icons/rc/radio_unchecked_disabled.png");\n'
            "}\n"
            "\n"
            "QRadioButton::indicator:checked {\n"
            "  border: none;\n"
            "  outline: none;\n"
            '  image: url(":/'
            'qss_icons/rc/radio_checked.png");\n'
            "}\n"
            "\n"
            "QRadioButton::indicator:checked:hover, QRadioButton::indicator:checked:focus, QRadioButton::indicator:checked:pressed {\n"
            "  border: none;\n"
            "  outline: none;\n"
            '  image: url(":/qss_icons/rc/radio_checked_focus.png");\n'
            "}\n"
            "\n"
            "QRadioButton::indicator:checked:disabled {\n"
            "  outline: none;\n"
            '  image: url(":/qss_icons/rc/radio_checked_disabled.png");\n'
            "}\n"
            "\n"
            "/* QMenuBar ---------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QMenuBar {\n"
            "  background-color: #32414B;\n"
            "  padding: 2px;\n"
            "  border: 1px solid #19232D;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QMenuBar:focus {\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QMenuBar::item {\n"
            "  background: transparent;\n"
            "  padding: 4px;\n"
            "}\n"
            "\n"
            "QMenuBar::item:selected {\n"
            "  padding: 4px;\n"
            "  background: t"
            "ransparent;\n"
            "  border: 0px solid #32414B;\n"
            "}\n"
            "\n"
            "QMenuBar::item:pressed {\n"
            "  padding: 4px;\n"
            "  border: 0px solid #32414B;\n"
            "  background-color: #148CD2;\n"
            "  color: #F0F0F0;\n"
            "  margin-bottom: 0px;\n"
            "  padding-bottom: 0px;\n"
            "}\n"
            "\n"
            "/* QMenu ------------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QMenu {\n"
            "  border: 0px solid #32414B;\n"
            "  color: #F0F0F0;\n"
            "  margin: 0px;\n"
            "}\n"
            "\n"
            "QMenu::separator {\n"
            "  height: 1px;\n"
            "  background-color: #505F69;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QMenu::icon {\n"
            "  margin: 0px;\n"
            "  padding-left: 8px;\n"
            "}\n"
            "\n"
            "QMenu::item {\n"
            "  background-color: #32414B;\n"
            "  padding: 4px 24px 4px 24px;\n"
            "  /* Reserve space for selection border */\n"
            "  border: 1px transparent #32414B;\n"
            "}\n"
            "\n"
            "QMenu::item:selected {\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "Q"
            "Menu::indicator {\n"
            "  width: 12px;\n"
            "  height: 12px;\n"
            "  padding-left: 6px;\n"
            "  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
            "  /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
            "}\n"
            "\n"
            "QMenu::indicator:non-exclusive:unchecked {\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked.png");\n'
            "}\n"
            "\n"
            "QMenu::indicator:non-exclusive:unchecked:selected {\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked_disabled.png");\n'
            "}\n"
            "\n"
            "QMenu::indicator:non-exclusive:checked {\n"
            '  image: url(":/qss_icons/rc/checkbox_checked.png");\n'
            "}\n"
            "\n"
            "QMenu::indicator:non-exclusive:checked:selected {\n"
            '  image: url(":/qss_icons/rc/checkbox_checked_disabled.png");\n'
            "}\n"
            "\n"
            "QMenu::indicator:exclusive:unchecked {\n"
            '  image: url(":/qss_icons/rc/radio_unchecked.png");\n'
            "}\n"
            "\n"
            "QMenu::indicator:exclusive:unchecked:selected {\n"
            '  image: url(":/qss_icons/rc/radio_unchecked_disabled.png");\n'
            ""
            "}\n"
            "\n"
            "QMenu::indicator:exclusive:checked {\n"
            '  image: url(":/qss_icons/rc/radio_checked.png");\n'
            "}\n"
            "\n"
            "QMenu::indicator:exclusive:checked:selected {\n"
            '  image: url(":/qss_icons/rc/radio_checked_disabled.png");\n'
            "}\n"
            "\n"
            "QMenu::right-arrow {\n"
            "  margin: 5px;\n"
            '  image: url(":/qss_icons/rc/arrow_right.png");\n'
            "  height: 12px;\n"
            "  width: 12px;\n"
            "}\n"
            "\n"
            "/* QAbstractItemView ------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QAbstractItemView {\n"
            "  alternate-background-color: #19232D;\n"
            "  color: #F0F0F0;\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QAbstractItemView QLineEdit {\n"
            "  padding: 2px;\n"
            "}\n"
            "\n"
            "/* QAbstractScrollArea ----------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrolla"
            "rea\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QAbstractScrollArea {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "  padding: 2px;\n"
            "  /* fix #159 */\n"
            "  min-height: 1.25em;\n"
            "  /* fix #159 */\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QAbstractScrollArea:disabled {\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "/* QScrollArea ------------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QScrollArea QWidget QWidget:disabled {\n"
            "  background-color: #19232D;\n"
            "}\n"
            "\n"
            "/* QScrollBar -------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QScrollBar:horizontal {\n"
            "  height: 16px;\n"
            "  margin: 2px 16px 2px 16px;\n"
            "  border: 1px solid #32414B;\n"
            "  bor"
            "der-radius: 4px;\n"
            "  background-color: #19232D;\n"
            "}\n"
            "\n"
            "QScrollBar:vertical {\n"
            "  background-color: #19232D;\n"
            "  width: 16px;\n"
            "  margin: 16px 2px 16px 2px;\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal {\n"
            "  background-color: #787878;\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "  min-width: 8px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal:hover {\n"
            "  background-color: #148CD2;\n"
            "  border: 1px solid #148CD2;\n"
            "  border-radius: 4px;\n"
            "  min-width: 8px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal:focus {\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "  background-color: #787878;\n"
            "  border: 1px solid #32414B;\n"
            "  min-height: 8px;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical:hover {\n"
            "  background-color: #148CD2;\n"
            "  border: 1px solid #148CD2;\n"
            "  border-radius: 4px;\n"
            "  min-height: 8px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical:focus {\n"
            ""
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:horizontal {\n"
            "  margin: 0px 0px 0px 0px;\n"
            '  border-image: url(":/qss_icons/rc/arrow_right_disabled.png");\n'
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  subcontrol-position: right;\n"
            "  subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
            '  border-image: url(":/qss_icons/rc/arrow_right.png");\n'
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  subcontrol-position: right;\n"
            "  subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "  margin: 3px 0px 3px 0px;\n"
            '  border-image: url(":/qss_icons/rc/arrow_down_disabled.png");\n'
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  subcontrol-position: bottom;\n"
            "  subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
            '  border-image: url(":/qss_icons/rc/arrow_down.png");\n'
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  subcontrol-position: bottom;\n"
            "  s"
            "ubcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:horizontal {\n"
            "  margin: 0px 3px 0px 3px;\n"
            '  border-image: url(":/qss_icons/rc/arrow_left_disabled.png");\n'
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  subcontrol-position: left;\n"
            "  subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
            '  border-image: url(":/qss_icons/rc/arrow_left.png");\n'
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  subcontrol-position: left;\n"
            "  subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "  margin: 3px 0px 3px 0px;\n"
            '  border-image: url(":/qss_icons/rc/arrow_up_disabled.png");\n'
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  subcontrol-position: top;\n"
            "  subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
            '  border-image: url(":/qss_icons/rc/arrow_up.png");\n'
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  subcontrol-position: top;\n"
            "  subcontrol-origin:"
            " margin;\n"
            "}\n"
            "\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
            "  background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "  background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
            "  background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "  background: none;\n"
            "}\n"
            "\n"
            "/* QTextEdit --------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-specific-widgets\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QTextEdit {\n"
            "  background-color: #19232D;\n"
            "  color: #F0F0F0;\n"
            "  border-radius: 4px;\n"
            "  border: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "QTextEdit:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QTextEdit:focus {\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QTextEdit:selected {\n"
            "  backg"
            "round: #1464A0;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "/* QPlainTextEdit ---------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QPlainTextEdit {\n"
            "  background-color: #19232D;\n"
            "  color: #F0F0F0;\n"
            "  border-radius: 4px;\n"
            "  border: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "QPlainTextEdit:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QPlainTextEdit:focus {\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QPlainTextEdit:selected {\n"
            "  background: #1464A0;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "/* QSizeGrip --------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsizegrip\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QSizeGrip {\n"
            "  background: transparent;\n"
            "  width: 12px;\n"
            "  height: 12px;\n"
            '  image: url(":/qss_icons/rc/window_grip.png");\n'
            "}\n"
            "\n"
            "/* QSt"
            "ackedWidget ---------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QStackedWidget {\n"
            "  padding: 2px;\n"
            "  border: 1px solid #32414B;\n"
            "  border: 1px solid #19232D;\n"
            "}\n"
            "\n"
            "/* QToolBar ---------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QToolBar {\n"
            "  background-color: #32414B;\n"
            "  border-bottom: 1px solid #19232D;\n"
            "  padding: 2px;\n"
            "  font-weight: bold;\n"
            "  spacing: 2px;\n"
            "}\n"
            "\n"
            "QToolBar QToolButton {\n"
            "  background-color: #32414B;\n"
            "  border: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "QToolBar QToolButton:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QToolBar QToolButton:checked {\n"
            "  border: 1px solid #19232D;\n"
            "  background-color: #19232D;\n"
            "}\n"
            "\n"
            "QToolBar QToolButton:checked:hover {\n"
            " "
            " border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QToolBar::handle:horizontal {\n"
            "  width: 16px;\n"
            '  image: url(":/qss_icons/rc/toolbar_move_horizontal.png");\n'
            "}\n"
            "\n"
            "QToolBar::handle:vertical {\n"
            "  height: 16px;\n"
            '  image: url(":/qss_icons/rc/toolbar_move_vertical.png");\n'
            "}\n"
            "\n"
            "QToolBar::separator:horizontal {\n"
            "  width: 16px;\n"
            '  image: url(":/qss_icons/rc/toolbar_separator_horizontal.png");\n'
            "}\n"
            "\n"
            "QToolBar::separator:vertical {\n"
            "  height: 16px;\n"
            '  image: url(":/qss_icons/rc/toolbar_separator_vertical.png");\n'
            "}\n"
            "\n"
            "QToolButton#qt_toolbar_ext_button {\n"
            "  background: #32414B;\n"
            "  border: 0px;\n"
            "  color: #F0F0F0;\n"
            '  image: url(":/qss_icons/rc/arrow_right.png");\n'
            "}\n"
            "\n"
            "/* QAbstractSpinBox -------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QAbstractSpinBox {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #F0F0F0;\n"
            ""
            "  /* This fixes 103, 111 */\n"
            "  padding-top: 2px;\n"
            "  /* This fixes 103, 111 */\n"
            "  padding-bottom: 2px;\n"
            "  padding-left: 4px;\n"
            "  padding-right: 4px;\n"
            "  border-radius: 4px;\n"
            "  /* min-width: 5px; removed to fix 109 */\n"
            "}\n"
            "\n"
            "QAbstractSpinBox:up-button {\n"
            "  background-color: transparent #19232D;\n"
            "  subcontrol-origin: border;\n"
            "  subcontrol-position: top right;\n"
            "  border-left: 1px solid #32414B;\n"
            "  border-bottom: 1px solid #32414B;\n"
            "  border-top-left-radius: 0;\n"
            "  border-bottom-left-radius: 0;\n"
            "  margin: 1px;\n"
            "  width: 12px;\n"
            "  margin-bottom: -1px;\n"
            "}\n"
            "\n"
            "QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {\n"
            '  image: url(":/qss_icons/rc/arrow_up_disabled.png");\n'
            "  height: 8px;\n"
            "  width: 8px;\n"
            "}\n"
            "\n"
            "QAbstractSpinBox::up-arrow:hover {\n"
            '  image: url(":/qss_icons/rc/arrow_up.png");\n'
            "}\n"
            "\n"
            "QAbstractSpinBox:down-button {\n"
            "  background-color: transparent #19232D;\n"
            "  subcontrol"
            "-origin: border;\n"
            "  subcontrol-position: bottom right;\n"
            "  border-left: 1px solid #32414B;\n"
            "  border-top: 1px solid #32414B;\n"
            "  border-top-left-radius: 0;\n"
            "  border-bottom-left-radius: 0;\n"
            "  margin: 1px;\n"
            "  width: 12px;\n"
            "  margin-top: -1px;\n"
            "}\n"
            "\n"
            "QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {\n"
            '  image: url(":/qss_icons/rc/arrow_down_disabled.png");\n'
            "  height: 8px;\n"
            "  width: 8px;\n"
            "}\n"
            "\n"
            "QAbstractSpinBox::down-arrow:hover {\n"
            '  image: url(":/qss_icons/rc/arrow_down.png");\n'
            "}\n"
            "\n"
            "QAbstractSpinBox:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QAbstractSpinBox:focus {\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QAbstractSpinBox:selected {\n"
            "  background: #1464A0;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "/* ------------------------------------------------------------------------ */\n"
            "/* DISPLAYS --------------------------------------------------------------- */\n"
            ""
            "/* ------------------------------------------------------------------------ */\n"
            "/* QLabel -----------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QLabel {\n"
            "  background-color: #19232D;\n"
            "  border: 0px solid #32414B;\n"
            "  padding: 2px;\n"
            "  margin: 0px;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "  background-color: #19232D;\n"
            "  border: 0px solid #32414B;\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "/* QTextBrowser -----------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QTextBrowser {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #F0F0F0;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QTextBrowser:disabled {\n"
            ""
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #787878;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QTextBrowser:hover, QTextBrowser:!hover, QTextBrowser:selected, QTextBrowser:pressed {\n"
            "  border: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "/* QGraphicsView ----------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QGraphicsView {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #F0F0F0;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QGraphicsView:disabled {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #787878;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QGraphicsView:hover, QGraphicsView:!hover, QGraphicsView:selected, QGraphicsView:pressed {\n"
            "  border: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "/* QCalendarWidget --------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------"
            "- */\n"
            "QCalendarWidget {\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QCalendarWidget:disabled {\n"
            "  background-color: #19232D;\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "/* QLCDNumber -------------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QLCDNumber {\n"
            "  background-color: #19232D;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QLCDNumber:disabled {\n"
            "  background-color: #19232D;\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "/* QProgressBar -----------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qprogressbar\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QProgressBar {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #F0F0F0;\n"
            "  border-radius: 4px;\n"
            "  text-align: center;\n"
            "}\n"
            "\n"
            "QProgressBar:disabled {\n"
            "  background-color: #19232D;\n"
            "  b"
            "order: 1px solid #32414B;\n"
            "  color: #787878;\n"
            "  border-radius: 4px;\n"
            "  text-align: center;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk {\n"
            "  background-color: #1464A0;\n"
            "  color: #19232D;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk:disabled {\n"
            "  background-color: #14506E;\n"
            "  color: #787878;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "/* ------------------------------------------------------------------------ */\n"
            "/* BUTTONS ---------------------------------------------------------------- */\n"
            "/* ------------------------------------------------------------------------ */\n"
            "/* QPushButton ------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QPushButton {\n"
            "  background-color: #505F69;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #F0F0F0;\n"
            "  border-radius: 4px;\n"
            "  padding: 3px;\n"
            "  outline: none"
            ";\n"
            "  /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */\n"
            "  min-width: 80px;\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "  background-color: #32414B;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #787878;\n"
            "  border-radius: 4px;\n"
            "  padding: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "  background-color: #32414B;\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "  padding: 3px;\n"
            "  outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:checked:disabled {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #787878;\n"
            "  border-radius: 4px;\n"
            "  padding: 3px;\n"
            "  outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:checked:selected {\n"
            "  background: #1464A0;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "QPushButton::menu-indicator {\n"
            "  subcontrol-origin: padding;\n"
            "  subcontrol-position: bottom right;\n"
            "  bottom: 4px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #19232D;\n"
            "}\n"
            "\n"
            "QPushButton:pressed:ho"
            "ver {\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QPushButton:selected {\n"
            "  background: #1464A0;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "/* QToolButton ------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbutton\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QToolButton {\n"
            "  background-color: transparent;\n"
            "  border: 1px solid transparent;\n"
            "  border-radius: 4px;\n"
            "  margin: 0px;\n"
            "  padding: 2px;\n"
            "  /* The subcontrols below are used only in the DelayedPopup mode */\n"
            "  /* The subcontrols below are used only in the MenuButtonPopup mode */\n"
            "  /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode *"
            "/\n"
            "}\n"
            "\n"
            "QToolButton:checked {\n"
            "  background-color: transparent;\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QToolButton:checked:disabled {\n"
            "  border: 1px solid #14506E;\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "  margin: 1px;\n"
            "  background-color: transparent;\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QToolButton:disabled {\n"
            "  border: none;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            'QToolButton[popupMode="0"] {\n'
            "  /* Only for DelayedPopup */\n"
            "  padding-right: 2px;\n"
            "}\n"
            "\n"
            'QToolButton[popupMode="1"] {\n'
            "  /* Only for MenuButtonPopup */\n"
            "  padding-right: 20px;\n"
            "}\n"
            "\n"
            'QToolButton[popupMode="1"]::menu-button {\n'
            "  border: none;\n"
            "}\n"
            "\n"
            'QToolButton[popupMode="1"]::menu-button:hover {\n'
            "  border: none;\n"
            "  border-left: 1px solid #148CD2;\n"
            "  border-radius: 0;\n"
            "}\n"
            "\n"
            'QToolButton[popupMode="2"] {\n'
            "  /* Only for InstantPopup */\n"
            "  padding-right: 2px;\n"
            "}\n"
            "\n"
            "QToolButton::menu-butt"
            "on {\n"
            "  padding: 2px;\n"
            "  border-radius: 4px;\n"
            "  border: 1px solid #32414B;\n"
            "  width: 12px;\n"
            "  outline: none;\n"
            "}\n"
            "\n"
            "QToolButton::menu-button:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QToolButton::menu-button:checked:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QToolButton::menu-indicator {\n"
            '  image: url(":/qss_icons/rc/arrow_down.png");\n'
            "  height: 8px;\n"
            "  width: 8px;\n"
            "  top: 0;\n"
            "  /* Exclude a shift for better image */\n"
            "  left: -2px;\n"
            "  /* Shift it a bit */\n"
            "}\n"
            "\n"
            "QToolButton::menu-arrow {\n"
            '  image: url(":/qss_icons/rc/arrow_down.png");\n'
            "  height: 8px;\n"
            "  width: 8px;\n"
            "}\n"
            "\n"
            "QToolButton::menu-arrow:hover {\n"
            '  image: url(":/qss_icons/rc/arrow_down_focus.png");\n'
            "}\n"
            "\n"
            "/* QCommandLinkButton -----------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QCommandLinkButton {\n"
            "  background-color: transparent;\n"
            "  border: "
            "1px solid #32414B;\n"
            "  color: #F0F0F0;\n"
            "  border-radius: 4px;\n"
            "  padding: 0px;\n"
            "  margin: 0px;\n"
            "}\n"
            "\n"
            "QCommandLinkButton:disabled {\n"
            "  background-color: transparent;\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "/* ------------------------------------------------------------------------ */\n"
            "/* INPUTS - NO FIELDS ----------------------------------------------------- */\n"
            "/* ------------------------------------------------------------------------ */\n"
            "/* QComboBox --------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QComboBox {\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "  selection-background-color: #1464A0;\n"
            "  padding-left: 4px;\n"
            "  padding-right: 36px;\n"
            "  /* 4 + 16*2 See scrollbar size */\n"
            "  /* Fixes #103, #111 */\n"
            "  min-height: 1.5em;\n"
            "  /* padding-top: 2px;     removed to fi"
            "x #132 */\n"
            "  /* padding-bottom: 2px;  removed to fix #132 */\n"
            "  /* min-width: 75px;      removed to fix #109 */\n"
            "  /* Needed to remove indicator - fix #132 */\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 0;\n"
            "  background-color: #19232D;\n"
            "  selection-background-color: #1464A0;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView:hover {\n"
            "  background-color: #19232D;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView:selected {\n"
            "  background: #1464A0;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView:alternate {\n"
            "  background: #19232D;\n"
            "}\n"
            "\n"
            "QComboBox:disabled {\n"
            "  background-color: #19232D;\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "QComboBox:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QComboBox:focus {\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QComboBox:on {\n"
            "  selection-background-color: #1464A0;\n"
            "}\n"
            "\n"
            "QComboBox::indicator {\n"
            "  border: none;\n"
            "  border-radius: 0;\n"
            "  back"
            "ground-color: transparent;\n"
            "  selection-background-color: transparent;\n"
            "  color: transparent;\n"
            "  selection-color: transparent;\n"
            "  /* Needed to remove indicator - fix #132 */\n"
            "}\n"
            "\n"
            "QComboBox::indicator:alternate {\n"
            "  background: #19232D;\n"
            "}\n"
            "\n"
            "QComboBox::item:alternate {\n"
            "  background: #19232D;\n"
            "}\n"
            "\n"
            "QComboBox::item:checked {\n"
            "  font-weight: bold;\n"
            "}\n"
            "\n"
            "QComboBox::item:selected {\n"
            "  border: 0px solid transparent;\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "  subcontrol-origin: padding;\n"
            "  subcontrol-position: top right;\n"
            "  width: 12px;\n"
            "  border-left: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            '  image: url(":/qss_icons/rc/arrow_down_disabled.png");\n'
            "  height: 8px;\n"
            "  width: 8px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:on, QComboBox::down-arrow:hover, QComboBox::down-arrow:focus {\n"
            '  image: url(":/qss_icons/rc/arrow_down.png");\n'
            "}\n"
            "\n"
            "/* QSlider ----------------------------------------------------------------\n"
            ""
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QSlider:disabled {\n"
            "  background: #19232D;\n"
            "}\n"
            "\n"
            "QSlider:focus {\n"
            "  border: none;\n"
            "}\n"
            "\n"
            "QSlider::groove:horizontal {\n"
            "  background: #32414B;\n"
            "  border: 1px solid #32414B;\n"
            "  height: 4px;\n"
            "  margin: 0px;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::groove:vertical {\n"
            "  background: #32414B;\n"
            "  border: 1px solid #32414B;\n"
            "  width: 4px;\n"
            "  margin: 0px;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::add-page:vertical {\n"
            "  background: #1464A0;\n"
            "  border: 1px solid #32414B;\n"
            "  width: 4px;\n"
            "  margin: 0px;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::add-page:vertical :disabled {\n"
            "  background: #14506E;\n"
            "}\n"
            "\n"
            "QSlider::sub-page:horizontal {\n"
            "  background: #1464A0;\n"
            "  border: 1px solid #32414B;\n"
            "  height: 4px;\n"
            "  margin: 0px;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            ""
            "QSlider::sub-page:horizontal:disabled {\n"
            "  background: #14506E;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "  background: #787878;\n"
            "  border: 1px solid #32414B;\n"
            "  width: 8px;\n"
            "  height: 8px;\n"
            "  margin: -8px 0px;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:hover {\n"
            "  background: #148CD2;\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal:focus {\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QSlider::handle:vertical {\n"
            "  background: #787878;\n"
            "  border: 1px solid #32414B;\n"
            "  width: 8px;\n"
            "  height: 8px;\n"
            "  margin: 0 -8px;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QSlider::handle:vertical:hover {\n"
            "  background: #148CD2;\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QSlider::handle:vertical:focus {\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "/* QLineEdit --------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit\n"
            "\n"
            "-------------------"
            "-------------------------------------------------------- */\n"
            "QLineEdit {\n"
            "  background-color: #19232D;\n"
            "  padding-top: 2px;\n"
            "  /* This QLineEdit fix  103, 111 */\n"
            "  padding-bottom: 2px;\n"
            "  /* This QLineEdit fix  103, 111 */\n"
            "  padding-left: 4px;\n"
            "  padding-right: 4px;\n"
            "  border-style: solid;\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QLineEdit:disabled {\n"
            "  background-color: #19232D;\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "QLineEdit:selected {\n"
            "  background-color: #1464A0;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "/* QTabWiget --------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QTabWidget {\n"
            ""
            "  padding: 2px;\n"
            "  selection-background-color: #32414B;\n"
            "}\n"
            "\n"
            "QTabWidget QWidget {\n"
            "  /* Fixes #189 */\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QTabWidget::pane {\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "  margin: 0px;\n"
            "  /* Fixes double border inside pane with pyqt5 */\n"
            "  padding: 0px;\n"
            "}\n"
            "\n"
            "QTabWidget::pane:selected {\n"
            "  background-color: #32414B;\n"
            "  border: 1px solid #1464A0;\n"
            "}\n"
            "\n"
            "/* QTabBar ----------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QTabBar {\n"
            "  qproperty-drawBase: 0;\n"
            "  border-radius: 4px;\n"
            "  margin: 0px;\n"
            "  padding: 2px;\n"
            "  border: 0;\n"
            "  /* left: 5px; move to the right by 5px - removed for fix */\n"
            "}\n"
            "\n"
            "QTabBar::close-button {\n"
            "  border: 0;\n"
            "  margin: 2px;\n"
            "  padding: 2px;\n"
            '  image: url(":/qss_ico'
            'ns/rc/window_close.png");\n'
            "}\n"
            "\n"
            "QTabBar::close-button:hover {\n"
            '  image: url(":/qss_icons/rc/window_close_focus.png");\n'
            "}\n"
            "\n"
            "QTabBar::close-button:pressed {\n"
            '  image: url(":/qss_icons/rc/window_close_pressed.png");\n'
            "}\n"
            "\n"
            "/* QTabBar::tab - selected ------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QTabBar::tab {\n"
            "  /* !selected and disabled ----------------------------------------- */\n"
            "  /* selected ------------------------------------------------------- */\n"
            "}\n"
            "\n"
            "QTabBar::tab:top:selected:disabled {\n"
            "  border-bottom: 3px solid #14506E;\n"
            "  color: #787878;\n"
            "  background-color: #32414B;\n"
            "}\n"
            "\n"
            "QTabBar::tab:bottom:selected:disabled {\n"
            "  border-top: 3px solid #14506E;\n"
            "  color: #787878;\n"
            "  background-color: #32414B;\n"
            "}\n"
            "\n"
            "QTabBar::tab:left:selected:di"
            "sabled {\n"
            "  border-right: 3px solid #14506E;\n"
            "  color: #787878;\n"
            "  background-color: #32414B;\n"
            "}\n"
            "\n"
            "QTabBar::tab:right:selected:disabled {\n"
            "  border-left: 3px solid #14506E;\n"
            "  color: #787878;\n"
            "  background-color: #32414B;\n"
            "}\n"
            "\n"
            "QTabBar::tab:top:!selected:disabled {\n"
            "  border-bottom: 3px solid #19232D;\n"
            "  color: #787878;\n"
            "  background-color: #19232D;\n"
            "}\n"
            "\n"
            "QTabBar::tab:bottom:!selected:disabled {\n"
            "  border-top: 3px solid #19232D;\n"
            "  color: #787878;\n"
            "  background-color: #19232D;\n"
            "}\n"
            "\n"
            "QTabBar::tab:left:!selected:disabled {\n"
            "  border-right: 3px solid #19232D;\n"
            "  color: #787878;\n"
            "  background-color: #19232D;\n"
            "}\n"
            "\n"
            "QTabBar::tab:right:!selected:disabled {\n"
            "  border-left: 3px solid #19232D;\n"
            "  color: #787878;\n"
            "  background-color: #19232D;\n"
            "}\n"
            "\n"
            "QTabBar::tab:top:!selected {\n"
            "  border-bottom: 2px solid #19232D;\n"
            "  margin-top: 2px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:bottom:!selected {\n"
            "  border-top: 2px solid #"
            "19232D;\n"
            "  margin-bottom: 3px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:left:!selected {\n"
            "  border-left: 2px solid #19232D;\n"
            "  margin-right: 2px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:right:!selected {\n"
            "  border-right: 2px solid #19232D;\n"
            "  margin-left: 2px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:top {\n"
            "  background-color: #32414B;\n"
            "  color: #F0F0F0;\n"
            "  margin-left: 2px;\n"
            "  padding-left: 4px;\n"
            "  padding-right: 4px;\n"
            "  padding-top: 2px;\n"
            "  padding-bottom: 2px;\n"
            "  min-width: 5px;\n"
            "  border-bottom: 3px solid #32414B;\n"
            "  border-top-left-radius: 3px;\n"
            "  border-top-right-radius: 3px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:top:selected {\n"
            "  background-color: #505F69;\n"
            "  color: #F0F0F0;\n"
            "  border-bottom: 3px solid #1464A0;\n"
            "  border-top-left-radius: 3px;\n"
            "  border-top-right-radius: 3px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:top:!selected:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  border-bottom: 3px solid #148CD2;\n"
            "  /* Fixes spyder-ide/spyder#9766 */\n"
            "  padding-left: 4px;\n"
            "  padding-right: 4px;\n"
            ""
            "}\n"
            "\n"
            "QTabBar::tab:bottom {\n"
            "  color: #F0F0F0;\n"
            "  border-top: 3px solid #32414B;\n"
            "  background-color: #32414B;\n"
            "  margin-left: 2px;\n"
            "  padding-left: 4px;\n"
            "  padding-right: 4px;\n"
            "  padding-top: 2px;\n"
            "  padding-bottom: 2px;\n"
            "  border-bottom-left-radius: 3px;\n"
            "  border-bottom-right-radius: 3px;\n"
            "  min-width: 5px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:bottom:selected {\n"
            "  color: #F0F0F0;\n"
            "  background-color: #505F69;\n"
            "  border-top: 3px solid #1464A0;\n"
            "  border-bottom-left-radius: 3px;\n"
            "  border-bottom-right-radius: 3px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:bottom:!selected:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  border-top: 3px solid #148CD2;\n"
            "  /* Fixes spyder-ide/spyder#9766 */\n"
            "  padding-left: 4px;\n"
            "  padding-right: 4px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:left {\n"
            "  color: #F0F0F0;\n"
            "  background-color: #32414B;\n"
            "  margin-top: 2px;\n"
            "  padding-left: 2px;\n"
            "  padding-right: 2px;\n"
            "  padding-top: 4px;\n"
            "  padding-bottom: 4px;\n"
            "  border-top-left-radius: "
            "3px;\n"
            "  border-bottom-left-radius: 3px;\n"
            "  min-height: 5px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:left:selected {\n"
            "  color: #F0F0F0;\n"
            "  background-color: #505F69;\n"
            "  border-right: 3px solid #1464A0;\n"
            "}\n"
            "\n"
            "QTabBar::tab:left:!selected:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  border-right: 3px solid #148CD2;\n"
            "  padding: 0px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:right {\n"
            "  color: #F0F0F0;\n"
            "  background-color: #32414B;\n"
            "  margin-top: 2px;\n"
            "  padding-left: 2px;\n"
            "  padding-right: 2px;\n"
            "  padding-top: 4px;\n"
            "  padding-bottom: 4px;\n"
            "  border-top-right-radius: 3px;\n"
            "  border-bottom-right-radius: 3px;\n"
            "  min-height: 5px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:right:selected {\n"
            "  color: #F0F0F0;\n"
            "  background-color: #505F69;\n"
            "  border-left: 3px solid #1464A0;\n"
            "}\n"
            "\n"
            "QTabBar::tab:right:!selected:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  border-left: 3px solid #148CD2;\n"
            "  padding: 0px;\n"
            "}\n"
            "\n"
            "QTabBar QToolButton {\n"
            "  /* Fixes #136 */\n"
            "  background-color:"
            " #32414B;\n"
            "  height: 12px;\n"
            "  width: 12px;\n"
            "}\n"
            "\n"
            "QTabBar QToolButton:pressed {\n"
            "  background-color: #32414B;\n"
            "}\n"
            "\n"
            "QTabBar QToolButton:pressed:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QTabBar QToolButton::left-arrow:enabled {\n"
            '  image: url(":/qss_icons/rc/arrow_left.png");\n'
            "}\n"
            "\n"
            "QTabBar QToolButton::left-arrow:disabled {\n"
            '  image: url(":/qss_icons/rc/arrow_left_disabled.png");\n'
            "}\n"
            "\n"
            "QTabBar QToolButton::right-arrow:enabled {\n"
            '  image: url(":/qss_icons/rc/arrow_right.png");\n'
            "}\n"
            "\n"
            "QTabBar QToolButton::right-arrow:disabled {\n"
            '  image: url(":/qss_icons/rc/arrow_right_disabled.png");\n'
            "}\n"
            "\n"
            "/* QDockWiget -------------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QDockWidget {\n"
            "  outline: 1px solid #32414B;\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "  titlebar-close-icon: "
            'url(":/qss_icons/rc/window_close.png");\n'
            '  titlebar-normal-icon: url(":/qss_icons/rc/window_undock.png");\n'
            "}\n"
            "\n"
            "QDockWidget::title {\n"
            "  /* Better size for title bar */\n"
            "  padding: 6px;\n"
            "  spacing: 4px;\n"
            "  border: none;\n"
            "  background-color: #32414B;\n"
            "}\n"
            "\n"
            "QDockWidget::close-button {\n"
            "  background-color: #32414B;\n"
            "  border-radius: 4px;\n"
            "  border: none;\n"
            "}\n"
            "\n"
            "QDockWidget::close-button:hover {\n"
            '  image: url(":/qss_icons/rc/window_close_focus.png");\n'
            "}\n"
            "\n"
            "QDockWidget::close-button:pressed {\n"
            '  image: url(":/qss_icons/rc/window_close_pressed.png");\n'
            "}\n"
            "\n"
            "QDockWidget::float-button {\n"
            "  background-color: #32414B;\n"
            "  border-radius: 4px;\n"
            "  border: none;\n"
            "}\n"
            "\n"
            "QDockWidget::float-button:hover {\n"
            '  image: url(":/qss_icons/rc/window_undock_focus.png");\n'
            "}\n"
            "\n"
            "QDockWidget::float-button:pressed {\n"
            '  image: url(":/qss_icons/rc/window_undock_pressed.png");\n'
            "}\n"
            "\n"
            "/* QTreeView QListView QTableView --"
            "---------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QTreeView:branch:selected, QTreeView:branch:hover {\n"
            '  background: url(":/qss_icons/rc/transparent.png");\n'
            "}\n"
            "\n"
            "QTreeView:branch:has-siblings:!adjoins-item {\n"
            '  border-image: url(":/qss_icons/rc/branch_line.png") 0;\n'
            "}\n"
            "\n"
            "QTreeView:branch:has-siblings:adjoins-item {\n"
            '  border-image: url(":/qss_icons/rc/branch_more.png") 0;\n'
            "}\n"
            "\n"
            "QTreeView:branch:!has-children:!has-siblings:adjoins-item {\n"
            '  border-image: url(":/qss_icons/rc/branch_end.png") 0;\n'
            "}\n"
            "\n"
            "QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has-siblings {\n"
            "  border-image: none;\n"
            '  image: url(":/qss_'
            'icons/rc/branch_closed.png");\n'
            "}\n"
            "\n"
            "QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {\n"
            "  border-image: none;\n"
            '  image: url(":/qss_icons/rc/branch_open.png");\n'
            "}\n"
            "\n"
            "QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {\n"
            '  image: url(":/qss_icons/rc/branch_closed_focus.png");\n'
            "}\n"
            "\n"
            "QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {\n"
            '  image: url(":/qss_icons/rc/branch_open_focus.png");\n'
            "}\n"
            "\n"
            "QTreeView::indicator:checked,\n"
            "QListView::indicator:checked {\n"
            '  image: url(":/qss_icons/rc/checkbox_checked.png");\n'
            "}\n"
            "\n"
            "QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,\n"
            "QListView::indicator:checked:hover,\n"
            "QListView::indicator:checked:focus,\n"
            "QListView::indicator:checked:pressed {\n"
            '  image: url(":/qss_icons/r'
            'c/checkbox_checked_focus.png");\n'
            "}\n"
            "\n"
            "QTreeView::indicator:unchecked,\n"
            "QListView::indicator:unchecked {\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked.png");\n'
            "}\n"
            "\n"
            "QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,\n"
            "QListView::indicator:unchecked:hover,\n"
            "QListView::indicator:unchecked:focus,\n"
            "QListView::indicator:unchecked:pressed {\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked_focus.png");\n'
            "}\n"
            "\n"
            "QTreeView::indicator:indeterminate,\n"
            "QListView::indicator:indeterminate {\n"
            '  image: url(":/qss_icons/rc/checkbox_indeterminate.png");\n'
            "}\n"
            "\n"
            "QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,\n"
            "QListView::indicator:indeterminate:hover,\n"
            "QListView::indicator:indeterminate:focus,\n"
            "QListView::indicator:indeterminate:pressed {\n"
            '  image: url(":/qss_icons/rc/checkbox_indeterminate_focus.png");\n'
            "}\n"
            ""
            "\n"
            "QTreeView,\n"
            "QListView,\n"
            "QTableView,\n"
            "QColumnView {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #F0F0F0;\n"
            "  gridline-color: #32414B;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            "QTreeView:disabled,\n"
            "QListView:disabled,\n"
            "QTableView:disabled,\n"
            "QColumnView:disabled {\n"
            "  background-color: #19232D;\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "QTreeView:selected,\n"
            "QListView:selected,\n"
            "QTableView:selected,\n"
            "QColumnView:selected {\n"
            "  background-color: #1464A0;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "QTreeView:hover,\n"
            "QListView:hover,\n"
            "QTableView:hover,\n"
            "QColumnView:hover {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #148CD2;\n"
            "}\n"
            "\n"
            "QTreeView::item:pressed,\n"
            "QListView::item:pressed,\n"
            "QTableView::item:pressed,\n"
            "QColumnView::item:pressed {\n"
            "  background-color: #1464A0;\n"
            "}\n"
            "\n"
            "QTreeView::item:selected:hover,\n"
            "QListView::item:selected:hover,\n"
            "QTableView::item:selected:hover,\n"
            "QColumnView::item:selected:hov"
            "er {\n"
            "  background: #1464A0;\n"
            "  color: #19232D;\n"
            "}\n"
            "\n"
            "QTreeView::item:selected:active,\n"
            "QListView::item:selected:active,\n"
            "QTableView::item:selected:active,\n"
            "QColumnView::item:selected:active {\n"
            "  background-color: #1464A0;\n"
            "}\n"
            "\n"
            "QTreeView::item:!selected:hover,\n"
            "QListView::item:!selected:hover,\n"
            "QTableView::item:!selected:hover,\n"
            "QColumnView::item:!selected:hover {\n"
            "  outline: 0;\n"
            "  color: #148CD2;\n"
            "  background-color: #32414B;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "  background-color: #19232D;\n"
            "  border: 1px transparent #32414B;\n"
            "  border-radius: 0px;\n"
            "}\n"
            "\n"
            "/* QHeaderView ------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QHeaderView {\n"
            "  background-color: #32414B;\n"
            "  border: 0px transparent #32414B;\n"
            "  padding: 0px;\n"
            "  margin: 0px;\n"
            "  b"
            "order-radius: 0px;\n"
            "}\n"
            "\n"
            "QHeaderView:disabled {\n"
            "  background-color: #32414B;\n"
            "  border: 1px transparent #32414B;\n"
            "  padding: 2px;\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "  background-color: #32414B;\n"
            "  color: #F0F0F0;\n"
            "  padding: 2px;\n"
            "  border-radius: 0px;\n"
            "  text-align: left;\n"
            "}\n"
            "\n"
            "QHeaderView::section:checked {\n"
            "  color: #F0F0F0;\n"
            "  background-color: #1464A0;\n"
            "}\n"
            "\n"
            "QHeaderView::section:checked:disabled {\n"
            "  color: #787878;\n"
            "  background-color: #14506E;\n"
            "}\n"
            "\n"
            "QHeaderView::section::horizontal {\n"
            "  padding-left: 4px;\n"
            "  padding-right: 4px;\n"
            "  border-left: 1px solid #19232D;\n"
            "}\n"
            "\n"
            "QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one {\n"
            "  border-left: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "QHeaderView::section::horizontal:disabled {\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "QHeaderView::section::vertical {\n"
            "  padding-left: 4px;\n"
            "  padding-right: 4px;\n"
            "  border-top: 1px solid #19232D;\n"
            "}\n"
            ""
            "\n"
            "QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one {\n"
            "  border-top: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "QHeaderView::section::vertical:disabled {\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "QHeaderView::down-arrow {\n"
            "  /* Those settings (border/width/height/background-color) solve bug */\n"
            "  /* transparent arrow background and size */\n"
            "  background-color: #32414B;\n"
            "  border: none;\n"
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  padding-left: 2px;\n"
            "  padding-right: 2px;\n"
            '  image: url(":/qss_icons/rc/arrow_down.png");\n'
            "}\n"
            "\n"
            "QHeaderView::up-arrow {\n"
            "  background-color: #32414B;\n"
            "  border: none;\n"
            "  height: 12px;\n"
            "  width: 12px;\n"
            "  padding-left: 2px;\n"
            "  padding-right: 2px;\n"
            '  image: url(":/qss_icons/rc/arrow_up.png");\n'
            "}\n"
            "\n"
            "/* QToolBox --------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox\n"
            "\n"
            "-------------------------------------------------"
            "-------------------------- */\n"
            "QToolBox {\n"
            "  padding: 0px;\n"
            "  border: 0px;\n"
            "  border: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "QToolBox:selected {\n"
            "  padding: 0px;\n"
            "  border: 2px solid #1464A0;\n"
            "}\n"
            "\n"
            "QToolBox::tab {\n"
            "  background-color: #19232D;\n"
            "  border: 1px solid #32414B;\n"
            "  color: #F0F0F0;\n"
            "  border-top-left-radius: 4px;\n"
            "  border-top-right-radius: 4px;\n"
            "}\n"
            "\n"
            "QToolBox::tab:disabled {\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "QToolBox::tab:selected {\n"
            "  background-color: #505F69;\n"
            "  border-bottom: 2px solid #1464A0;\n"
            "}\n"
            "\n"
            "QToolBox::tab:selected:disabled {\n"
            "  background-color: #32414B;\n"
            "  border-bottom: 2px solid #14506E;\n"
            "}\n"
            "\n"
            "QToolBox::tab:!selected {\n"
            "  background-color: #32414B;\n"
            "  border-bottom: 2px solid #32414B;\n"
            "}\n"
            "\n"
            "QToolBox::tab:!selected:disabled {\n"
            "  background-color: #19232D;\n"
            "}\n"
            "\n"
            "QToolBox::tab:hover {\n"
            "  border-color: #148CD2;\n"
            "  border-bottom: 2px solid #148CD2;\n"
            "}\n"
            "\n"
            "QToolBox QScrol"
            "lArea QWidget QWidget {\n"
            "  padding: 0px;\n"
            "  border: 0px;\n"
            "  background-color: #19232D;\n"
            "}\n"
            "\n"
            "/* QFrame -----------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
            "https://doc.qt.io/qt-5/qframe.html#-prop\n"
            "https://doc.qt.io/qt-5/qframe.html#details\n"
            "https://stackoverflow.com/questions/14581498/qt-stylesheet-for-hline-vline-color\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "/* (dot) .QFrame  fix #141, #126, #123 */\n"
            ".QFrame {\n"
            "  border-radius: 4px;\n"
            "  border: 1px solid #32414B;\n"
            "  /* No frame */\n"
            "  /* HLine */\n"
            "  /* HLine */\n"
            "}\n"
            "\n"
            '.QFrame[frameShape="0"] {\n'
            "  border-radius: 4px;\n"
            "  border: 1px transparent #32414B;\n"
            "}\n"
            "\n"
            '.QFrame[frameShape="4"] {\n'
            "  max-height: 2px;\n"
            "  border: none;\n"
            "  background-color: #32414B;\n"
            "}\n"
            "\n"
            '.QFrame[frameShape="5"] {\n'
            "  max-width: 2px;\n"
            "  border: none;\n"
            "  bac"
            "kground-color: #32414B;\n"
            "}\n"
            "\n"
            "/* QSplitter --------------------------------------------------------------\n"
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QSplitter {\n"
            "  background-color: #32414B;\n"
            "  spacing: 0px;\n"
            "  padding: 0px;\n"
            "  margin: 0px;\n"
            "}\n"
            "\n"
            "QSplitter::handle {\n"
            "  background-color: #32414B;\n"
            "  border: 0px solid #19232D;\n"
            "  spacing: 0px;\n"
            "  padding: 1px;\n"
            "  margin: 0px;\n"
            "}\n"
            "\n"
            "QSplitter::handle:hover {\n"
            "  background-color: #787878;\n"
            "}\n"
            "\n"
            "QSplitter::handle:horizontal {\n"
            "  width: 5px;\n"
            '  image: url(":/qss_icons/rc/line_vertical.png");\n'
            "}\n"
            "\n"
            "QSplitter::handle:vertical {\n"
            "  height: 5px;\n"
            '  image: url(":/qss_icons/rc/line_horizontal.png");\n'
            "}\n"
            "\n"
            "/* QDateEdit, QDateTimeEdit -----------------------------------------------\n"
            "\n"
            "------------------------------------------------------------"
            "--------------- */\n"
            "QDateEdit, QDateTimeEdit {\n"
            "  selection-background-color: #1464A0;\n"
            "  border-style: solid;\n"
            "  border: 1px solid #32414B;\n"
            "  border-radius: 4px;\n"
            "  /* This fixes 103, 111 */\n"
            "  padding-top: 2px;\n"
            "  /* This fixes 103, 111 */\n"
            "  padding-bottom: 2px;\n"
            "  padding-left: 4px;\n"
            "  padding-right: 4px;\n"
            "  min-width: 10px;\n"
            "}\n"
            "\n"
            "QDateEdit:on, QDateTimeEdit:on {\n"
            "  selection-background-color: #1464A0;\n"
            "}\n"
            "\n"
            "QDateEdit::drop-down, QDateTimeEdit::drop-down {\n"
            "  subcontrol-origin: padding;\n"
            "  subcontrol-position: top right;\n"
            "  width: 12px;\n"
            "  border-left: 1px solid #32414B;\n"
            "}\n"
            "\n"
            "QDateEdit::down-arrow, QDateTimeEdit::down-arrow {\n"
            '  image: url(":/qss_icons/rc/arrow_down_disabled.png");\n'
            "  height: 8px;\n"
            "  width: 8px;\n"
            "}\n"
            "\n"
            "QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover, QDateEdit::down-arrow:focus, QDateTimeEdit::down-arrow:on, QDateTimeEdit::down-arrow:hover, QDateTimeEdit::down-arrow:focus {\n"
            "  image:"
            ' url(":/qss_icons/rc/arrow_down.png");\n'
            "}\n"
            "\n"
            "QDateEdit QAbstractItemView, QDateTimeEdit QAbstractItemView {\n"
            "  background-color: #19232D;\n"
            "  border-radius: 4px;\n"
            "  border: 1px solid #32414B;\n"
            "  selection-background-color: #1464A0;\n"
            "}\n"
            "\n"
            "/* QAbstractView ----------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QAbstractView:hover {\n"
            "  border: 1px solid #148CD2;\n"
            "  color: #F0F0F0;\n"
            "}\n"
            "\n"
            "QAbstractView:selected {\n"
            "  background: #1464A0;\n"
            "  color: #32414B;\n"
            "}\n"
            "\n"
            "/* PlotWidget -------------------------------------------------------------\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "PlotWidget {\n"
            "  /* Fix cut labels in plots #134 */\n"
            "  padding: 0px;\n"
            "}"
        )
        self.centralwidget = QWidget(frm_drill)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(10, 10, 190, 710))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(190, 710))
        self.frame.setMaximumSize(QSize(190, 710))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tbx_dpt = QLineEdit(self.frame)
        self.tbx_dpt.setObjectName("tbx_dpt")
        self.tbx_dpt.setGeometry(QRect(10, 30, 170, 26))
        self.tbx_dpt.setMinimumSize(QSize(170, 0))
        self.tbx_dpt.setMaximumSize(QSize(170, 16777215))
        self.tbx_dpt.setAlignment(Qt.AlignCenter)
        self.lbl_dpt = QLabel(self.frame)
        self.lbl_dpt.setObjectName("lbl_dpt")
        self.lbl_dpt.setEnabled(True)
        self.lbl_dpt.setGeometry(QRect(15, 10, 138, 26))
        self.tbx_cut = QLineEdit(self.frame)
        self.tbx_cut.setObjectName("tbx_cut")
        self.tbx_cut.setGeometry(QRect(10, 80, 170, 26))
        self.tbx_cut.setMinimumSize(QSize(170, 0))
        self.tbx_cut.setMaximumSize(QSize(170, 16777215))
        self.tbx_cut.setAlignment(Qt.AlignCenter)
        self.lbl_cut = QLabel(self.frame)
        self.lbl_cut.setObjectName("lbl_cut")
        self.lbl_cut.setEnabled(True)
        self.lbl_cut.setGeometry(QRect(15, 60, 101, 26))
        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setGeometry(QRect(10, 680, 171, 24))
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(88, 0))
        self.btn_save.setAutoDefault(True)
        self.lbl_fed = QLabel(self.frame)
        self.lbl_fed.setObjectName("lbl_fed")
        self.lbl_fed.setEnabled(True)
        self.lbl_fed.setGeometry(QRect(15, 160, 96, 26))
        self.tbx_fed = QLineEdit(self.frame)
        self.tbx_fed.setObjectName("tbx_fed")
        self.tbx_fed.setGeometry(QRect(10, 180, 170, 26))
        self.tbx_fed.setMinimumSize(QSize(170, 0))
        self.tbx_fed.setMaximumSize(QSize(170, 16777215))
        self.tbx_fed.setAlignment(Qt.AlignCenter)
        self.cbx_sde = QComboBox(self.frame)
        self.cbx_sde.setObjectName("cbx_sde")
        self.cbx_sde.setGeometry(QRect(10, 480, 170, 26))
        self.cbx_sde.setMinimumSize(QSize(170, 26))
        self.cbx_sde.setMaximumSize(QSize(170, 16777215))
        self.lbl_sde = QLabel(self.frame)
        self.lbl_sde.setObjectName("lbl_sde")
        self.lbl_sde.setEnabled(True)
        self.lbl_sde.setGeometry(QRect(15, 460, 104, 26))
        self.tbx_xin = QLineEdit(self.frame)
        self.tbx_xin.setObjectName("tbx_xin")
        self.tbx_xin.setGeometry(QRect(10, 280, 170, 26))
        self.tbx_xin.setMinimumSize(QSize(170, 0))
        self.tbx_xin.setMaximumSize(QSize(170, 16777215))
        self.tbx_xin.setAlignment(Qt.AlignCenter)
        self.lbl_xin = QLabel(self.frame)
        self.lbl_xin.setObjectName("lbl_xin")
        self.lbl_xin.setEnabled(True)
        self.lbl_xin.setGeometry(QRect(15, 260, 98, 26))
        self.lbl_yin = QLabel(self.frame)
        self.lbl_yin.setObjectName("lbl_yin")
        self.lbl_yin.setEnabled(True)
        self.lbl_yin.setGeometry(QRect(15, 310, 98, 26))
        self.tbx_yin = QLineEdit(self.frame)
        self.tbx_yin.setObjectName("tbx_yin")
        self.tbx_yin.setGeometry(QRect(10, 330, 170, 26))
        self.tbx_yin.setMinimumSize(QSize(170, 0))
        self.tbx_yin.setMaximumSize(QSize(170, 16777215))
        self.tbx_yin.setAlignment(Qt.AlignCenter)
        self.lbl_zin = QLabel(self.frame)
        self.lbl_zin.setObjectName("lbl_zin")
        self.lbl_zin.setEnabled(True)
        self.lbl_zin.setGeometry(QRect(15, 360, 98, 26))
        self.tbx_zin = QLineEdit(self.frame)
        self.tbx_zin.setObjectName("tbx_zin")
        self.tbx_zin.setGeometry(QRect(10, 380, 170, 26))
        self.tbx_zin.setMinimumSize(QSize(170, 0))
        self.tbx_zin.setMaximumSize(QSize(170, 16777215))
        self.tbx_zin.setAlignment(Qt.AlignCenter)
        self.cbx_sys = QComboBox(self.frame)
        self.cbx_sys.setObjectName("cbx_sys")
        self.cbx_sys.setGeometry(QRect(10, 530, 170, 26))
        self.cbx_sys.setMinimumSize(QSize(170, 26))
        self.cbx_sys.setMaximumSize(QSize(170, 16777215))
        self.lbl_sys = QLabel(self.frame)
        self.lbl_sys.setObjectName("lbl_sys")
        self.lbl_sys.setEnabled(True)
        self.lbl_sys.setGeometry(QRect(15, 510, 139, 26))
        self.lbl_znd = QLabel(self.frame)
        self.lbl_znd.setObjectName("lbl_znd")
        self.lbl_znd.setEnabled(True)
        self.lbl_znd.setGeometry(QRect(15, 560, 105, 26))
        self.cbx_znd = QComboBox(self.frame)
        self.cbx_znd.setObjectName("cbx_znd")
        self.cbx_znd.setGeometry(QRect(10, 580, 170, 26))
        self.cbx_znd.setMinimumSize(QSize(170, 26))
        self.cbx_znd.setMaximumSize(QSize(170, 16777215))
        self.tbx_rtr = QLineEdit(self.frame)
        self.tbx_rtr.setObjectName("tbx_rtr")
        self.tbx_rtr.setGeometry(QRect(10, 430, 170, 26))
        self.tbx_rtr.setMinimumSize(QSize(170, 0))
        self.tbx_rtr.setMaximumSize(QSize(170, 16777215))
        self.tbx_rtr.setAlignment(Qt.AlignCenter)
        self.lbl_rtr = QLabel(self.frame)
        self.lbl_rtr.setObjectName("lbl_rtr")
        self.lbl_rtr.setEnabled(True)
        self.lbl_rtr.setGeometry(QRect(15, 410, 115, 26))
        self.cbx_cyl = QComboBox(self.frame)
        self.cbx_cyl.setObjectName("cbx_cyl")
        self.cbx_cyl.setGeometry(QRect(10, 630, 170, 26))
        self.cbx_cyl.setMinimumSize(QSize(170, 26))
        self.cbx_cyl.setMaximumSize(QSize(170, 16777215))
        self.lbl_cyl = QLabel(self.frame)
        self.lbl_cyl.setObjectName("lbl_cyl")
        self.lbl_cyl.setEnabled(True)
        self.lbl_cyl.setGeometry(QRect(15, 610, 78, 26))
        self.tbx_ang = QLineEdit(self.frame)
        self.tbx_ang.setObjectName("tbx_ang")
        self.tbx_ang.setGeometry(QRect(10, 130, 170, 26))
        self.tbx_ang.setMinimumSize(QSize(170, 0))
        self.tbx_ang.setMaximumSize(QSize(170, 16777215))
        self.tbx_ang.setAlignment(Qt.AlignCenter)
        self.lbl_ang = QLabel(self.frame)
        self.lbl_ang.setObjectName("lbl_ang")
        self.lbl_ang.setEnabled(True)
        self.lbl_ang.setGeometry(QRect(15, 110, 111, 26))
        self.lbl_dwl = QLabel(self.frame)
        self.lbl_dwl.setObjectName("lbl_dwl")
        self.lbl_dwl.setEnabled(True)
        self.lbl_dwl.setGeometry(QRect(15, 210, 103, 26))
        self.tbx_dwl = QLineEdit(self.frame)
        self.tbx_dwl.setObjectName("tbx_dwl")
        self.tbx_dwl.setGeometry(QRect(10, 230, 170, 26))
        self.tbx_dwl.setMinimumSize(QSize(170, 0))
        self.tbx_dwl.setMaximumSize(QSize(170, 16777215))
        self.tbx_dwl.setAlignment(Qt.AlignCenter)
        self.tbx_dpt.raise_()
        self.lbl_dpt.raise_()
        self.tbx_cut.raise_()
        self.lbl_cut.raise_()
        self.btn_save.raise_()
        self.tbx_fed.raise_()
        self.lbl_fed.raise_()
        self.cbx_sde.raise_()
        self.lbl_sde.raise_()
        self.tbx_xin.raise_()
        self.lbl_xin.raise_()
        self.tbx_yin.raise_()
        self.tbx_zin.raise_()
        self.lbl_zin.raise_()
        self.lbl_yin.raise_()
        self.cbx_sys.raise_()
        self.lbl_sys.raise_()
        self.cbx_znd.raise_()
        self.tbx_rtr.raise_()
        self.lbl_rtr.raise_()
        self.lbl_znd.raise_()
        self.cbx_cyl.raise_()
        self.lbl_cyl.raise_()
        self.tbx_ang.raise_()
        self.lbl_ang.raise_()
        self.tbx_dwl.raise_()
        self.lbl_dwl.raise_()
        self.btn_help = QToolButton(self.centralwidget)
        self.btn_help.setObjectName("btn_help")
        self.btn_help.setGeometry(QRect(183, -2, 29, 29))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn_help.setFont(font)
        icon1 = QIcon()
        icon1.addFile(":/icons/question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon1)
        self.btn_help.setIconSize(QSize(20, 20))
        frm_drill.setCentralWidget(self.centralwidget)
        # if QT_CONFIG(shortcut)
        self.lbl_dpt.setBuddy(self.lbl_dpt)
        self.lbl_fed.setBuddy(self.lbl_fed)
        self.lbl_dwl.setBuddy(self.lbl_fed)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tbx_dpt, self.tbx_cut)
        QWidget.setTabOrder(self.tbx_cut, self.tbx_ang)
        QWidget.setTabOrder(self.tbx_ang, self.tbx_fed)
        QWidget.setTabOrder(self.tbx_fed, self.tbx_dwl)
        QWidget.setTabOrder(self.tbx_dwl, self.tbx_xin)
        QWidget.setTabOrder(self.tbx_xin, self.tbx_yin)
        QWidget.setTabOrder(self.tbx_yin, self.tbx_zin)
        QWidget.setTabOrder(self.tbx_zin, self.tbx_rtr)
        QWidget.setTabOrder(self.tbx_rtr, self.cbx_sde)
        QWidget.setTabOrder(self.cbx_sde, self.cbx_sys)
        QWidget.setTabOrder(self.cbx_sys, self.cbx_znd)
        QWidget.setTabOrder(self.cbx_znd, self.cbx_cyl)
        QWidget.setTabOrder(self.cbx_cyl, self.btn_save)
        QWidget.setTabOrder(self.btn_save, self.btn_help)

        self.retranslateUi(frm_drill)

        QMetaObject.connectSlotsByName(frm_drill)

    # setupUi

    def retranslateUi(self, frm_drill):
        frm_drill.setWindowTitle(
            QCoreApplication.translate("frm_drill", "GCode Editor", None)
        )
        # if QT_CONFIG(tooltip)
        self.tbx_dpt.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Digite la profundidad del agujero", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tbx_dpt.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tbx_dpt.setPlaceholderText("")
        self.lbl_dpt.setText(
            QCoreApplication.translate("frm_drill", "Profundidad del agujero", None)
        )
        # if QT_CONFIG(tooltip)
        self.tbx_cut.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Digite la profundidad de corte por pasada", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tbx_cut.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tbx_cut.setText(QCoreApplication.translate("frm_drill", "0.1", None))
        self.tbx_cut.setPlaceholderText("")
        self.lbl_cut.setText(
            QCoreApplication.translate("frm_drill", "Corte por pasada", None)
        )
        # if QT_CONFIG(tooltip)
        self.btn_save.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Agregar los datos al programa CNC", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn_save.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.btn_save.setText(QCoreApplication.translate("frm_drill", "Agregar", None))
        # if QT_CONFIG(shortcut)
        self.btn_save.setShortcut(
            QCoreApplication.translate("frm_drill", "Ctrl+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lbl_fed.setText(
            QCoreApplication.translate("frm_drill", "Avance de corte", None)
        )
        # if QT_CONFIG(tooltip)
        self.tbx_fed.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Digite la velocidad de avance de corte", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tbx_fed.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tbx_fed.setText(QCoreApplication.translate("frm_drill", ".005", None))
        self.tbx_fed.setPlaceholderText("")
        # if QT_CONFIG(tooltip)
        self.cbx_sde.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Seleccione el husillo de trabajo a utilizar", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lbl_sde.setText(
            QCoreApplication.translate("frm_drill", "Husillo de trabajo", None)
        )
        # if QT_CONFIG(tooltip)
        self.tbx_xin.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Digite la posici\u00f3n de inicio en el eje X", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tbx_xin.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tbx_xin.setText(QCoreApplication.translate("frm_drill", "0.0", None))
        self.tbx_xin.setPlaceholderText("")
        self.lbl_xin.setText(
            QCoreApplication.translate("frm_drill", "Posici\u00f3n inicio X", None)
        )
        self.lbl_yin.setText(
            QCoreApplication.translate("frm_drill", "Posici\u00f3n inicio Y", None)
        )
        # if QT_CONFIG(tooltip)
        self.tbx_yin.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Digite la posici\u00f3n de inicio en el eje Y", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tbx_yin.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tbx_yin.setText(QCoreApplication.translate("frm_drill", "0.0", None))
        self.tbx_yin.setPlaceholderText("")
        self.lbl_zin.setText(
            QCoreApplication.translate("frm_drill", "Posici\u00f3n inicio Z", None)
        )
        # if QT_CONFIG(tooltip)
        self.tbx_zin.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Digite la posici\u00f3n de inicio en el eje Z", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tbx_zin.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tbx_zin.setText(QCoreApplication.translate("frm_drill", "0.0", None))
        self.tbx_zin.setPlaceholderText("")
        # if QT_CONFIG(tooltip)
        self.cbx_sys.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Seleccione el sistema de coordenadas a utilizar", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lbl_sys.setText(
            QCoreApplication.translate("frm_drill", "Sistema de coordenadas", None)
        )
        self.lbl_znd.setText(
            QCoreApplication.translate("frm_drill", "Posici\u00f3n de salida", None)
        )
        # if QT_CONFIG(tooltip)
        self.cbx_znd.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Seleccione el punto de salida del perforado", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.tbx_rtr.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Digite la distancia de retracci\u00f3n", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tbx_rtr.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tbx_rtr.setText(QCoreApplication.translate("frm_drill", "0.0", None))
        self.tbx_rtr.setPlaceholderText("")
        self.lbl_rtr.setText(
            QCoreApplication.translate("frm_drill", "Punto de retracci\u00f3n", None)
        )
        # if QT_CONFIG(tooltip)
        self.cbx_cyl.setToolTip(
            QCoreApplication.translate(
                "frm_drill",
                "Seleccione si requiere un ciclo de perforado o cortes individuales",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lbl_cyl.setText(
            QCoreApplication.translate("frm_drill", "Codificaci\u00f3n", None)
        )
        # if QT_CONFIG(tooltip)
        self.tbx_ang.setToolTip(
            QCoreApplication.translate(
                "frm_drill", "Digite el \u00e1ngulo de la punta de la broca", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tbx_ang.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tbx_ang.setText(QCoreApplication.translate("frm_drill", "118", None))
        self.tbx_ang.setPlaceholderText("")
        self.lbl_ang.setText(
            QCoreApplication.translate("frm_drill", "\u00c1ngulo de la punta", None)
        )
        self.lbl_dwl.setText(
            QCoreApplication.translate("frm_drill", "Tiempo de espera", None)
        )
        # if QT_CONFIG(tooltip)
        self.tbx_dwl.setToolTip(
            QCoreApplication.translate(
                "frm_drill",
                "Digite el tiempo de espera en segundos para pulir el fondo del agujero",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tbx_dwl.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.tbx_dwl.setText(QCoreApplication.translate("frm_drill", "0.0", None))
        self.tbx_dwl.setPlaceholderText("")
        self.btn_help.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_help.setShortcut(QCoreApplication.translate("frm_drill", "F1", None))


# endif // QT_CONFIG(shortcut)
# retranslateUi
