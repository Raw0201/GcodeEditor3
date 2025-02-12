# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_windowKlRfbn.ui'
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
    QAction,
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
    QAbstractItemView,
    QApplication,
    QHBoxLayout,
    QHeaderView,
    QMainWindow,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)
import resources_rc


class Ui_frm_data_window(object):
    def setupUi(self, frm_data_window):
        if not frm_data_window.objectName():
            frm_data_window.setObjectName("frm_data_window")
        frm_data_window.resize(903, 582)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frm_data_window.sizePolicy().hasHeightForWidth())
        frm_data_window.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(":/icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        frm_data_window.setWindowIcon(icon)
        frm_data_window.setStyleSheet(
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
            "  background-color: #ffffff/*#148CD2*/;\n"
            "  border: 1px solid #19232D;\n"
            "  color: #19232D;\n"
            "  /* Remove padding, for fix combo box tooltip */\n"
            "  paddi"
            "ng: 0px;\n"
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
            "/* QCheckBox --------------------------------------------------------------\n"
            ""
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox\n"
            "\n"
            "--------------------------------------------------------------------------- */\n"
            "QCheckBox {\n"
            "  background-color: #19232D;\n"
            "  color: #F0F0F0;\n"
            "  spacing: 4px;\n"
            "  outline: none;\n"
            "  padding-top: 4px;\n"
            "  padding-bottom: 4px;\n"
            "}\n"
            "\n"
            "QCheckBox:focus {\n"
            "  border: none;\n"
            "}\n"
            "\n"
            "QCheckBox QWidget:disabled {\n"
            "  background-color: #19232D;\n"
            "  color: #787878;\n"
            "}\n"
            "\n"
            "QCheckBox::indicator {\n"
            "  margin-left: 4px;\n"
            "  height: 16px;\n"
            "  width: 16px;\n"
            "}\n"
            "\n"
            "QCheckBox::indicator:unchecked {\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked.png");\n'
            "}\n"
            "\n"
            "QCheckBox::indicator:unchecked:hover, QCheckBox::indicator:unchecked:focus, QCheckBox::indicator:unchecked:pressed {\n"
            "  border: none;\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked_focus.png");\n'
            "}\n"
            "\n"
            "QCheckBox::indicator:unchecked:disabled {\n"
            '  image: url(":/qss_icons/rc/checkbox_unchecked_disabled'
            '.png");\n'
            "}\n"
            "\n"
            "QCheckBox::indicator:checked {\n"
            '  image: url(":/qss_icons/rc/checkbox_checked.png");\n'
            "}\n"
            "\n"
            "QCheckBox::indicator:checked:hover, QCheckBox::indicator:checked:focus, QCheckBox::indicator:checked:pressed {\n"
            "  border: none;\n"
            '  image: url(":/qss_icons/rc/checkbox_checked_focus.png");\n'
            "}\n"
            "\n"
            "QCheckBox::indicator:checked:disabled {\n"
            '  image: url(":/qss_icons/rc/checkbox_checked_disabled.png");\n'
            "}\n"
            "\n"
            "QCheckBox::indicator:indeterminate {\n"
            '  image: url(":/qss_icons/rc/checkbox_indeterminate.png");\n'
            "}\n"
            "\n"
            "QCheckBox::indicator:indeterminate:disabled {\n"
            '  image: url(":/qss_icons/rc/checkbox_indeterminate_disabled.png");\n'
            "}\n"
            "\n"
            "QCheckBox::indicator:indeterminate:focus, QCheckBox::indicator:indeterminate:hover, QCheckBox::indicator:indeterminate:pressed {\n"
            '  image: url(":/qss_icons/rc/checkbox_indeterminate_focus.png");\n'
            "}\n"
            "\n"
            "/* QGroupBox --------------------------------------------------------------\n"
            "\n"
            "https://do"
            "c.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
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
            "QGroupBox::indicator:unchecked:disabled {\n"
            ""
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
            "QRadioButton:"
            "disabled {\n"
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
            '  image: url(":/qss_ic'
            'ons/rc/radio_checked.png");\n'
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
            "  background: transpa"
            "rent;\n"
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
            "QMenu::"
            "indicator {\n"
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
            "}\n"
            ""
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
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
            ""
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
            "  border-radi"
            "us: 4px;\n"
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
            "  borde"
            "r: 1px solid #1464A0;\n"
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
            "  subcontr"
            "ol-origin: margin;\n"
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
            "  subcontrol-origin: margin"
            ";\n"
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
            "  background: "
            "#1464A0;\n"
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
            "/* QStackedWi"
            "dget ---------------------------------------------------------\n"
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
            "  border"
            ": 1px solid #148CD2;\n"
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
            "  /* Th"
            "is fixes 103, 111 */\n"
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
            "  subcontrol-origin"
            ": border;\n"
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
            "/* -"
            "----------------------------------------------------------------------- */\n"
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
            " "
            " background-color: #19232D;\n"
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
            "---------------------------------------------------------------------------"
            " */\n"
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
            "  bo"
            "rder: 1px solid #32414B;\n"
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
            "  outline: none;"
            "\n"
            "  /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */\n"
            "  min-width: 20px;\n"
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
            "QPushButton:pressed:hov"
            "er {\n"
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
            "  /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */"
            "\n"
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
            "QToolButton::menu-butto"
            "n {\n"
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
            "  border: 1"
            "px solid #32414B;\n"
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
            "  /* padding-top: 2px;     removed to fix"
            " #132 */\n"
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
            "  backg"
            "round-color: transparent;\n"
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
        self.actionNew = QAction(frm_data_window)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QAction(frm_data_window)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QAction(frm_data_window)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QAction(frm_data_window)
        self.actionClose.setObjectName("actionClose")
        self.actionDelete = QAction(frm_data_window)
        self.actionDelete.setObjectName("actionDelete")
        self.actionVersion = QAction(frm_data_window)
        self.actionVersion.setObjectName("actionVersion")
        self.actionX_invert = QAction(frm_data_window)
        self.actionX_invert.setObjectName("actionX_invert")
        self.actionY_invert = QAction(frm_data_window)
        self.actionY_invert.setObjectName("actionY_invert")
        self.actionZ_invert = QAction(frm_data_window)
        self.actionZ_invert.setObjectName("actionZ_invert")
        self.actionMove_up = QAction(frm_data_window)
        self.actionMove_up.setObjectName("actionMove_up")
        self.actionMove_down = QAction(frm_data_window)
        self.actionMove_down.setObjectName("actionMove_down")
        self.actionGo_to = QAction(frm_data_window)
        self.actionGo_to.setObjectName("actionGo_to")
        self.actionReturn_to = QAction(frm_data_window)
        self.actionReturn_to.setObjectName("actionReturn_to")
        self.actionShow_functions = QAction(frm_data_window)
        self.actionShow_functions.setObjectName("actionShow_functions")
        self.actionShow_tape1_widget = QAction(frm_data_window)
        self.actionShow_tape1_widget.setObjectName("actionShow_tape1_widget")
        self.actionShow_tape2_widget = QAction(frm_data_window)
        self.actionShow_tape2_widget.setObjectName("actionShow_tape2_widget")
        self.actionHide_functions = QAction(frm_data_window)
        self.actionHide_functions.setObjectName("actionHide_functions")
        self.actionHide_tape1_widget = QAction(frm_data_window)
        self.actionHide_tape1_widget.setObjectName("actionHide_tape1_widget")
        self.actionHide_tape2_widget = QAction(frm_data_window)
        self.actionHide_tape2_widget.setObjectName("actionHide_tape2_widget")
        self.actionShow_config_widget = QAction(frm_data_window)
        self.actionShow_config_widget.setObjectName("actionShow_config_widget")
        self.actionHide_config_widget = QAction(frm_data_window)
        self.actionHide_config_widget.setObjectName("actionHide_config_widget")
        self.actionBlock = QAction(frm_data_window)
        self.actionBlock.setObjectName("actionBlock")
        self.actionGraph = QAction(frm_data_window)
        self.actionGraph.setObjectName("actionGraph")
        self.actionSubrut_up = QAction(frm_data_window)
        self.actionSubrut_up.setObjectName("actionSubrut_up")
        self.actionSubrut_down = QAction(frm_data_window)
        self.actionSubrut_down.setObjectName("actionSubrut_down")
        self.actionLoop_up = QAction(frm_data_window)
        self.actionLoop_up.setObjectName("actionLoop_up")
        self.actionLoop_down = QAction(frm_data_window)
        self.actionLoop_down.setObjectName("actionLoop_down")
        self.actionX_up = QAction(frm_data_window)
        self.actionX_up.setObjectName("actionX_up")
        self.actionX_down = QAction(frm_data_window)
        self.actionX_down.setObjectName("actionX_down")
        self.actionY_up = QAction(frm_data_window)
        self.actionY_up.setObjectName("actionY_up")
        self.actionY_down = QAction(frm_data_window)
        self.actionY_down.setObjectName("actionY_down")
        self.actionZ_up = QAction(frm_data_window)
        self.actionZ_up.setObjectName("actionZ_up")
        self.actionZ_down = QAction(frm_data_window)
        self.actionZ_down.setObjectName("actionZ_down")
        self.actionFeed_up = QAction(frm_data_window)
        self.actionFeed_up.setObjectName("actionFeed_up")
        self.actionFeed_down = QAction(frm_data_window)
        self.actionFeed_down.setObjectName("actionFeed_down")
        self.actionDuplicate = QAction(frm_data_window)
        self.actionDuplicate.setObjectName("actionDuplicate")
        self.actionSpeed_up = QAction(frm_data_window)
        self.actionSpeed_up.setObjectName("actionSpeed_up")
        self.actionSpeed_down = QAction(frm_data_window)
        self.actionSpeed_down.setObjectName("actionSpeed_down")
        self.actionS1_move = QAction(frm_data_window)
        self.actionS1_move.setObjectName("actionS1_move")
        self.actionS2_move = QAction(frm_data_window)
        self.actionS2_move.setObjectName("actionS2_move")
        self.actionS3_move = QAction(frm_data_window)
        self.actionS3_move.setObjectName("actionS3_move")
        self.actionI_invert = QAction(frm_data_window)
        self.actionI_invert.setObjectName("actionI_invert")
        self.actionJ_invert = QAction(frm_data_window)
        self.actionJ_invert.setObjectName("actionJ_invert")
        self.actionK_invert = QAction(frm_data_window)
        self.actionK_invert.setObjectName("actionK_invert")
        self.actionI_up = QAction(frm_data_window)
        self.actionI_up.setObjectName("actionI_up")
        self.actionJ_up = QAction(frm_data_window)
        self.actionJ_up.setObjectName("actionJ_up")
        self.actionK_up = QAction(frm_data_window)
        self.actionK_up.setObjectName("actionK_up")
        self.actionI_down = QAction(frm_data_window)
        self.actionI_down.setObjectName("actionI_down")
        self.actionJ_down = QAction(frm_data_window)
        self.actionJ_down.setObjectName("actionJ_down")
        self.actionK_down = QAction(frm_data_window)
        self.actionK_down.setObjectName("actionK_down")
        self.actionG_invert = QAction(frm_data_window)
        self.actionG_invert.setObjectName("actionG_invert")
        self.centralwidget = QWidget(frm_data_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.data_widget = QTableWidget(self.centralwidget)
        self.data_widget.setObjectName("data_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.data_widget.sizePolicy().hasHeightForWidth())
        self.data_widget.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(9)
        self.data_widget.setFont(font)
        self.data_widget.setStyleSheet(
            "QWidget {\n"
            "  background-color: #000000;\n"
            "  border: 0px solid #32414B;\n"
            "  padding: 0px;\n"
            "  color: #F0F0F0;\n"
            "  selection-background-color: #1464A0;\n"
            "  selection-color: #F0F0F0;\n"
            "}"
        )
        self.data_widget.setLineWidth(1)
        self.data_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.data_widget.setDragDropOverwriteMode(False)
        self.data_widget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.data_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.data_widget.setShowGrid(True)
        self.data_widget.setWordWrap(True)
        self.data_widget.setColumnCount(0)
        self.data_widget.horizontalHeader().setMinimumSectionSize(20)
        self.data_widget.horizontalHeader().setDefaultSectionSize(150)
        self.data_widget.horizontalHeader().setProperty("showSortIndicator", True)
        self.data_widget.horizontalHeader().setStretchLastSection(False)
        self.data_widget.verticalHeader().setVisible(True)
        self.data_widget.verticalHeader().setCascadingSectionResizes(False)
        self.data_widget.verticalHeader().setMinimumSectionSize(0)
        self.data_widget.verticalHeader().setDefaultSectionSize(50)
        self.data_widget.verticalHeader().setProperty("showSortIndicator", False)
        self.data_widget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.data_widget)

        frm_data_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(frm_data_window)
        self.actionShow_tape1_widget.triggered.connect(self.data_widget.show)

        QMetaObject.connectSlotsByName(frm_data_window)

    # setupUi

    def retranslateUi(self, frm_data_window):
        frm_data_window.setWindowTitle(
            QCoreApplication.translate("frm_data_window", "GCode Editor", None)
        )
        self.actionNew.setText(
            QCoreApplication.translate("frm_data_window", "Nuevo", None)
        )
        # if QT_CONFIG(statustip)
        self.actionNew.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Crear un nuevo programa CNC", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+N", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(
            QCoreApplication.translate("frm_data_window", "Abrir", None)
        )
        # if QT_CONFIG(statustip)
        self.actionOpen.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Abrir un programa CNC existente", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSave.setText(
            QCoreApplication.translate("frm_data_window", "Guardar", None)
        )
        # if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Guardar el programa CNC actual", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionClose.setText(
            QCoreApplication.translate("frm_data_window", "Cerrar", None)
        )
        # if QT_CONFIG(statustip)
        self.actionClose.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Cerrar la aplicaci\u00f3n", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Q", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(
            QCoreApplication.translate("frm_data_window", "Borrar", None)
        )
        # if QT_CONFIG(statustip)
        self.actionDelete.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Borrar las l\u00edneas seleccionadas", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(
            QCoreApplication.translate("frm_data_window", "Del", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionVersion.setText(
            QCoreApplication.translate("frm_data_window", "Versi\u00f3n", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionVersion.setShortcut(
            QCoreApplication.translate("frm_data_window", "F1", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionX_invert.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n X", None)
        )
        # if QT_CONFIG(statustip)
        self.actionX_invert.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invertir el signo de los movimientos en el eje X",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionX_invert.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+X", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionY_invert.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n Y", None)
        )
        # if QT_CONFIG(statustip)
        self.actionY_invert.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invertir el signo de los movimientos en el eje Y",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionY_invert.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+Y", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionZ_invert.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n Z", None)
        )
        # if QT_CONFIG(statustip)
        self.actionZ_invert.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invertir el signo de los movimientos en el eje Z",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionZ_invert.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+Z", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionMove_up.setText(
            QCoreApplication.translate("frm_data_window", "Mover arriba       ", None)
        )
        # if QT_CONFIG(statustip)
        self.actionMove_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Mover hacia arriba las l\u00edneas seleccionadas",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionMove_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+Up", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionMove_down.setText(
            QCoreApplication.translate("frm_data_window", "Mover abajo", None)
        )
        # if QT_CONFIG(statustip)
        self.actionMove_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Mover hacia abajo las l\u00edneas seleccionadas",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionMove_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+Down", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionGo_to.setText(
            QCoreApplication.translate("frm_data_window", "Ir a programa", None)
        )
        # if QT_CONFIG(statustip)
        self.actionGo_to.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Cambiar al programa CNC seleccionado", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionGo_to.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+Right", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionReturn_to.setText(
            QCoreApplication.translate(
                "frm_data_window", "Regresar a programa      ", None
            )
        )
        # if QT_CONFIG(statustip)
        self.actionReturn_to.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Regresar al programa CNC anterior", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionReturn_to.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+Left", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionShow_functions.setText(
            QCoreApplication.translate("frm_data_window", "Barra de funciones", None)
        )
        # if QT_CONFIG(statustip)
        self.actionShow_functions.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Mostrar la barra de funciones", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionShow_functions.setShortcut(
            QCoreApplication.translate("frm_data_window", "0", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionShow_tape1_widget.setText(
            QCoreApplication.translate("frm_data_window", "Ventana programa 1", None)
        )
        # if QT_CONFIG(statustip)
        self.actionShow_tape1_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Mostrar la ventana del programa principal", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionShow_tape1_widget.setShortcut(
            QCoreApplication.translate("frm_data_window", "1", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionShow_tape2_widget.setText(
            QCoreApplication.translate("frm_data_window", "Ventana programa 2", None)
        )
        # if QT_CONFIG(statustip)
        self.actionShow_tape2_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Mostrar la ventana del programa secundario", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionShow_tape2_widget.setShortcut(
            QCoreApplication.translate("frm_data_window", "2", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionHide_functions.setText(
            QCoreApplication.translate("frm_data_window", "Barra de funciones", None)
        )
        # if QT_CONFIG(statustip)
        self.actionHide_functions.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Ocultar la barra de funciones", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionHide_functions.setShortcut(
            QCoreApplication.translate("frm_data_window", "9", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionHide_tape1_widget.setText(
            QCoreApplication.translate("frm_data_window", "Ventana programa 1", None)
        )
        # if QT_CONFIG(statustip)
        self.actionHide_tape1_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Ocultar la ventana del programa principal", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionHide_tape1_widget.setShortcut(
            QCoreApplication.translate("frm_data_window", "4", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionHide_tape2_widget.setText(
            QCoreApplication.translate("frm_data_window", "Ventana programa 2", None)
        )
        # if QT_CONFIG(statustip)
        self.actionHide_tape2_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Ocultar la ventana del programa secundario", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionHide_tape2_widget.setShortcut(
            QCoreApplication.translate("frm_data_window", "5", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionShow_config_widget.setText(
            QCoreApplication.translate("frm_data_window", "Esquema programa", None)
        )
        # if QT_CONFIG(statustip)
        self.actionShow_config_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Mostrar el esquema del programa", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionShow_config_widget.setShortcut(
            QCoreApplication.translate("frm_data_window", "3", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionHide_config_widget.setText(
            QCoreApplication.translate("frm_data_window", "Esquema programa", None)
        )
        # if QT_CONFIG(statustip)
        self.actionHide_config_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Ocultar el esquema del programa", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionHide_config_widget.setShortcut(
            QCoreApplication.translate("frm_data_window", "6", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionBlock.setText(
            QCoreApplication.translate("frm_data_window", "Bloquear", None)
        )
        # if QT_CONFIG(statustip)
        self.actionBlock.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Bloquear las l\u00edneas seleccionadas", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionBlock.setShortcut(
            QCoreApplication.translate("frm_data_window", "/", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionGraph.setText(
            QCoreApplication.translate("frm_data_window", "Graficar tape", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionGraph.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+G", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSubrut_up.setText(
            QCoreApplication.translate("frm_data_window", "Subrutina", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionSubrut_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Incrementa el n\u00famero de subrutina en 1", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionSubrut_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Incrementa el n\u00famero de subrutina en 1", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionSubrut_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+P", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSubrut_down.setText(
            QCoreApplication.translate("frm_data_window", "Subrutina            ", None)
        )
        self.actionSubrut_down.setIconText(
            QCoreApplication.translate(
                "frm_data_window", "Decrementa el n\u00famero de subrutina en 1", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.actionSubrut_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Decrementa el n\u00famero de subrutina en 1", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actionSubrut_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+P", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionLoop_up.setText(
            QCoreApplication.translate("frm_data_window", "Repeticiones", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionLoop_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Incrementa el n\u00famero de repeticiones en 1",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionLoop_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Incrementa el n\u00famero de repeticiones en 1",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionLoop_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+L", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionLoop_down.setText(
            QCoreApplication.translate("frm_data_window", "Repeticiones     ", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionLoop_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Decrementa el n\u00famero de repeticiones en 1",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionLoop_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Decrementa el n\u00famero de repeticiones en 1",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionLoop_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+L", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionX_up.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n X", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionX_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de X en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionX_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de X en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionX_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+X", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionX_down.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n X", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionX_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de X en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionX_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de X en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionX_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+X", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionY_up.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n Y", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionY_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de Y en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionY_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de Y en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionY_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+Y", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionY_down.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n Y", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionY_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de Y en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionY_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de Y en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionY_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+Y", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionZ_up.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n Z", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionZ_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de Z en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionZ_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de Z en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionZ_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+Z", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionZ_down.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n Z", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionZ_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de Z en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionZ_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de Z en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionZ_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+Z", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionFeed_up.setText(
            QCoreApplication.translate("frm_data_window", "Avance de corte", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionFeed_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Incrementa el valor del avance en 1", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionFeed_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Incrementa el valor del avance en 1", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionFeed_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+F", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionFeed_down.setText(
            QCoreApplication.translate("frm_data_window", "Avance de corte", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionFeed_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Decrementa el valor del avance en 1", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionFeed_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Decrementa el valor del avance en 1", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionFeed_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+F", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionDuplicate.setText(
            QCoreApplication.translate("frm_data_window", "Duplicar", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionDuplicate.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Duplicar las l\u00edneas seleccionadas", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionDuplicate.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Duplicar las l\u00edneas seleccionadas", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionDuplicate.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+D", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSpeed_up.setText(
            QCoreApplication.translate("frm_data_window", "Velocidad de giro", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionSpeed_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Incrementa la velocidad de giro en 100", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionSpeed_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Incrementa la velocidad de giro en 100", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionSpeed_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSpeed_down.setText(
            QCoreApplication.translate("frm_data_window", "Velocidad de giro", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionSpeed_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Decrementa la velocidad de giro en 100", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionSpeed_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Decrementa la velocidad de giro en 100", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionSpeed_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionS1_move.setText(
            QCoreApplication.translate("frm_data_window", "Mover a $1", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionS1_move.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Mover las l\u00edneas seleccionadas a $1", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionS1_move.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Mover las l\u00edneas seleccionadas a $1", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionS1_move.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+1", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionS2_move.setText(
            QCoreApplication.translate("frm_data_window", "Mover a $2", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionS2_move.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Mover las l\u00edneas seleccionadas a $2", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionS2_move.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Mover las l\u00edneas seleccionadas a $2", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionS2_move.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+2", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionS3_move.setText(
            QCoreApplication.translate("frm_data_window", "Mover a $3", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionS3_move.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", "Mover las l\u00edneas seleccionadas a $3", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionS3_move.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", "Mover las l\u00edneas seleccionadas a $3", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionS3_move.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+3", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionI_invert.setText(
            QCoreApplication.translate("frm_data_window", "Dimension I", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionI_invert.setToolTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invertir el signo de la dimensi\u00f3n en el centro I (eje X)",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionI_invert.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invertir el signo de la dimensi\u00f3n en el centro I (eje X)",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionI_invert.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+I", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionJ_invert.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n J", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionJ_invert.setToolTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invertir el signo de la dimensi\u00f3n en el centro J (eje Y)",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionJ_invert.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invertir el signo de la dimensi\u00f3n en el centro J (eje Y)",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionJ_invert.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+J", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionK_invert.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n K", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionK_invert.setToolTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invertir el signo de la dimensi\u00f3n en el centro K (eje Z)",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionK_invert.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invertir el signo de la dimensi\u00f3n en el centro K (eje Z)",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionK_invert.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+K", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionI_up.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n I", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionI_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de I en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionI_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de I en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionI_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+I", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionJ_up.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n J", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionJ_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de J en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionJ_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de J en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionJ_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+J", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionK_up.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n K", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionK_up.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de K en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionK_up.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Incrementa el valor de K en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionK_up.setShortcut(
            QCoreApplication.translate("frm_data_window", "Shift+K", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionI_down.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n I", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionI_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de I en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionI_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de I en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionI_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+I", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionJ_down.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n J", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionJ_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de J en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionJ_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de J en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionJ_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+J", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionK_down.setText(
            QCoreApplication.translate("frm_data_window", "Dimensi\u00f3n K", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionK_down.setToolTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de K en .001"', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionK_down.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window", 'Decrementa el valor de K en .001"', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionK_down.setShortcut(
            QCoreApplication.translate("frm_data_window", "Ctrl+Shift+K", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionG_invert.setText(
            QCoreApplication.translate("frm_data_window", "C\u00f3digos G", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionG_invert.setToolTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invierte el c\u00f3digo G (lineal y radial) de las l\u00edneas seleccionadas",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionG_invert.setStatusTip(
            QCoreApplication.translate(
                "frm_data_window",
                "Invierte el c\u00f3digo G (lineal y radial) de las l\u00edneas seleccionadas",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionG_invert.setShortcut(
            QCoreApplication.translate("frm_data_window", "Alt+G", None)
        )


# endif // QT_CONFIG(shortcut)
# retranslateUi
