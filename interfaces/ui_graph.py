# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphDdxLaU.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from pyqtgraph import PlotWidget

import resources_rc


class Ui_frm_graph(object):
    def setupUi(self, frm_graph):
        if not frm_graph.objectName():
            frm_graph.setObjectName("frm_graph")
        frm_graph.resize(1292, 1300)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frm_graph.sizePolicy().hasHeightForWidth())
        frm_graph.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(":/icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        frm_graph.setWindowIcon(icon)
        frm_graph.setStyleSheet(
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
            "  background-color: #19232D; /*#19232D*/\n"
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
            "QMainWindow::sep"
            "arator {\n"
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
            "  /* Remove padding, for fix combo box tooltip *"
            "/\n"
            "  padding: 0px;\n"
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
            "/* QCheckBox ---------------------------------------------------"
            "-----------\n"
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
            '  image: url(":/qss_icons/rc/checkbox_un'
            'checked_disabled.png");\n'
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
            ""
            "\n"
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
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
            "QGroupBox::indicator:unchecked"
            ":disabled {\n"
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
            ""
            "QRadioButton:disabled {\n"
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
            "  image: u"
            'rl(":/qss_icons/rc/radio_checked.png");\n'
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
            "  backgr"
            "ound: transparent;\n"
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
            ""
            "\n"
            "QMenu::indicator {\n"
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
            '  image: url(":/qss_icons/rc/radio_unchecked_disabled.png")'
            ";\n"
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
            "https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstracts"
            "crollarea\n"
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
            ""
            "  border-radius: 4px;\n"
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
            "QScrollBar::handle:vertical:focus "
            "{\n"
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
            ""
            "  subcontrol-origin: margin;\n"
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
            "  subcontrol-orig"
            "in: margin;\n"
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
            "  ba"
            "ckground: #1464A0;\n"
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
            "/* "
            "QStackedWidget ---------------------------------------------------------\n"
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
            ""
            "  border: 1px solid #148CD2;\n"
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
        self.actionNew = QAction(frm_graph)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QAction(frm_graph)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QAction(frm_graph)
        self.actionSave.setObjectName("actionSave")
        self.actionGuardar_como = QAction(frm_graph)
        self.actionGuardar_como.setObjectName("actionGuardar_como")
        self.actionDirectorio_base = QAction(frm_graph)
        self.actionDirectorio_base.setObjectName("actionDirectorio_base")
        self.actionClose = QAction(frm_graph)
        self.actionClose.setObjectName("actionClose")
        self.actionDuplicate = QAction(frm_graph)
        self.actionDuplicate.setObjectName("actionDuplicate")
        icon1 = QIcon()
        icon1.addFile(":/resources/cnc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDuplicate.setIcon(icon1)
        self.actionDelete = QAction(frm_graph)
        self.actionDelete.setObjectName("actionDelete")
        self.actionVersion = QAction(frm_graph)
        self.actionVersion.setObjectName("actionVersion")
        self.actionInvert_X = QAction(frm_graph)
        self.actionInvert_X.setObjectName("actionInvert_X")
        self.actionInvert_Y = QAction(frm_graph)
        self.actionInvert_Y.setObjectName("actionInvert_Y")
        self.actionInvert_Z = QAction(frm_graph)
        self.actionInvert_Z.setObjectName("actionInvert_Z")
        self.actionMove_up = QAction(frm_graph)
        self.actionMove_up.setObjectName("actionMove_up")
        self.actionMove_down = QAction(frm_graph)
        self.actionMove_down.setObjectName("actionMove_down")
        self.actionGo_to = QAction(frm_graph)
        self.actionGo_to.setObjectName("actionGo_to")
        self.actionReturn_to = QAction(frm_graph)
        self.actionReturn_to.setObjectName("actionReturn_to")
        self.actionShow_functions = QAction(frm_graph)
        self.actionShow_functions.setObjectName("actionShow_functions")
        self.actionShow_tape1_widget = QAction(frm_graph)
        self.actionShow_tape1_widget.setObjectName("actionShow_tape1_widget")
        self.actionShow_tape2_widget = QAction(frm_graph)
        self.actionShow_tape2_widget.setObjectName("actionShow_tape2_widget")
        self.actionHide_functions = QAction(frm_graph)
        self.actionHide_functions.setObjectName("actionHide_functions")
        self.actionHide_tape1_widget = QAction(frm_graph)
        self.actionHide_tape1_widget.setObjectName("actionHide_tape1_widget")
        self.actionHide_tape2_widget = QAction(frm_graph)
        self.actionHide_tape2_widget.setObjectName("actionHide_tape2_widget")
        self.actionSeleccionar_maquina = QAction(frm_graph)
        self.actionSeleccionar_maquina.setObjectName("actionSeleccionar_maquina")
        self.actionShow_config_widget = QAction(frm_graph)
        self.actionShow_config_widget.setObjectName("actionShow_config_widget")
        self.actionHide_config_widget = QAction(frm_graph)
        self.actionHide_config_widget.setObjectName("actionHide_config_widget")
        self.actionBlock = QAction(frm_graph)
        self.actionBlock.setObjectName("actionBlock")
        self.actionGraph = QAction(frm_graph)
        self.actionGraph.setObjectName("actionGraph")
        self.centralwidget = QWidget(frm_graph)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName("frame1")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graph1_widget = PlotWidget(self.frame1)
        self.graph1_widget.setObjectName("graph1_widget")
        self.graph1_widget.setStyleSheet(
            "QWidget {\n"
            "  background-color: #000000;\n"
            "  border: 0px solid #32414B;\n"
            "  padding: 0px;\n"
            "  color: #F0F0F0;\n"
            "  selection-background-color: #1464A0;\n"
            "  selection-color: #F0F0F0;\n"
            "}"
        )

        self.verticalLayout_4.addWidget(self.graph1_widget)

        self.verticalLayout.addWidget(self.frame1)

        self.frame2 = QFrame(self.centralwidget)
        self.frame2.setObjectName("frame2")
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graph2_widget = PlotWidget(self.frame2)
        self.graph2_widget.setObjectName("graph2_widget")
        self.graph2_widget.setStyleSheet(
            "QWidget {\n"
            "  background-color: #000000;\n"
            "  border: 0px solid #32414B;\n"
            "  padding: 0px;\n"
            "  color: #F0F0F0;\n"
            "  selection-background-color: #1464A0;\n"
            "  selection-color: #F0F0F0;\n"
            "}"
        )

        self.verticalLayout_3.addWidget(self.graph2_widget)

        self.verticalLayout.addWidget(self.frame2)

        frm_graph.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_graph)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1292, 31))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        frm_graph.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_graph)
        self.statusbar.setObjectName("statusbar")
        frm_graph.setStatusBar(self.statusbar)
        self.dock_functions = QDockWidget(frm_graph)
        self.dock_functions.setObjectName("dock_functions")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.dock_functions.sizePolicy().hasHeightForWidth()
        )
        self.dock_functions.setSizePolicy(sizePolicy1)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_program = QGroupBox(self.dockWidgetContents)
        self.groupBox_program.setObjectName("groupBox_program")
        self.gridLayout = QGridLayout(self.groupBox_program)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_free = QPushButton(self.groupBox_program)
        self.btn_free.setObjectName("btn_free")
        self.btn_free.setMinimumSize(QSize(28, 0))
        self.btn_free.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.btn_free, 4, 0, 1, 1)

        self.btn_end = QPushButton(self.groupBox_program)
        self.btn_end.setObjectName("btn_end")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_end.sizePolicy().hasHeightForWidth())
        self.btn_end.setSizePolicy(sizePolicy2)
        self.btn_end.setMinimumSize(QSize(28, 0))
        self.btn_end.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.btn_end, 6, 0, 1, 1)

        self.btn_comment = QPushButton(self.groupBox_program)
        self.btn_comment.setObjectName("btn_comment")
        sizePolicy2.setHeightForWidth(self.btn_comment.sizePolicy().hasHeightForWidth())
        self.btn_comment.setSizePolicy(sizePolicy2)
        self.btn_comment.setMinimumSize(QSize(28, 0))
        self.btn_comment.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.btn_comment, 3, 0, 1, 1)

        self.btn_header = QPushButton(self.groupBox_program)
        self.btn_header.setObjectName("btn_header")
        sizePolicy2.setHeightForWidth(self.btn_header.sizePolicy().hasHeightForWidth())
        self.btn_header.setSizePolicy(sizePolicy2)
        self.btn_header.setMinimumSize(QSize(28, 0))
        self.btn_header.setMaximumSize(QSize(120, 16777215))
        self.btn_header.setFlat(False)

        self.gridLayout.addWidget(self.btn_header, 0, 0, 1, 1)

        self.btn_subrutine = QPushButton(self.groupBox_program)
        self.btn_subrutine.setObjectName("btn_subrutine")

        self.gridLayout.addWidget(self.btn_subrutine, 5, 0, 1, 1)

        self.verticalLayout_5.addWidget(self.groupBox_program)

        self.verticalSpacer_5 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.dock_functions.setWidget(self.dockWidgetContents)
        frm_graph.addDockWidget(Qt.LeftDockWidgetArea, self.dock_functions)
        QWidget.setTabOrder(self.btn_header, self.btn_comment)
        QWidget.setTabOrder(self.btn_comment, self.btn_free)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)

        self.retranslateUi(frm_graph)
        self.actionShow_functions.triggered.connect(self.dock_functions.show)
        self.actionHide_functions.triggered.connect(self.dock_functions.hide)

        QMetaObject.connectSlotsByName(frm_graph)

    # setupUi

    def retranslateUi(self, frm_graph):
        frm_graph.setWindowTitle(
            QCoreApplication.translate("frm_graph", "CNC Editor - Gr\u00e1fico", None)
        )
        self.actionNew.setText(QCoreApplication.translate("frm_graph", "Nuevo", None))
        # if QT_CONFIG(statustip)
        self.actionNew.setStatusTip(
            QCoreApplication.translate("frm_graph", "Crear un nuevo programa CNC", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(
            QCoreApplication.translate("frm_graph", "Ctrl+N", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("frm_graph", "Abrir", None))
        # if QT_CONFIG(statustip)
        self.actionOpen.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Abrir un programa CNC existente", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(
            QCoreApplication.translate("frm_graph", "Ctrl+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSave.setText(
            QCoreApplication.translate("frm_graph", "Guardar", None)
        )
        # if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Guardar el programa CNC actual", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(
            QCoreApplication.translate("frm_graph", "Ctrl+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionGuardar_como.setText(
            QCoreApplication.translate("frm_graph", "Guardar como", None)
        )
        # if QT_CONFIG(statustip)
        self.actionGuardar_como.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Guardar el programa CNC actual con otro nombre", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionGuardar_como.setShortcut(
            QCoreApplication.translate("frm_graph", "Ctrl+A", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionDirectorio_base.setText(
            QCoreApplication.translate("frm_graph", "Directorio base", None)
        )
        # if QT_CONFIG(statustip)
        self.actionDirectorio_base.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Seleccionar el folder donde se va a trabajar", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionDirectorio_base.setShortcut(
            QCoreApplication.translate("frm_graph", "Ctrl+D", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionClose.setText(
            QCoreApplication.translate("frm_graph", "Cerrar", None)
        )
        # if QT_CONFIG(statustip)
        self.actionClose.setStatusTip(
            QCoreApplication.translate("frm_graph", "Cerrar la aplicaci\u00f3n", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(
            QCoreApplication.translate("frm_graph", "Ctrl+Q", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionDuplicate.setText(
            QCoreApplication.translate("frm_graph", "Duplicar l\u00edneas       ", None)
        )
        # if QT_CONFIG(statustip)
        self.actionDuplicate.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Duplicar las l\u00edneas seleccionadas", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionDuplicate.setShortcut(
            QCoreApplication.translate("frm_graph", "Alt+D", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(
            QCoreApplication.translate("frm_graph", "Borrar l\u00edneas", None)
        )
        # if QT_CONFIG(statustip)
        self.actionDelete.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Borrar las l\u00edneas seleccionadas", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(
            QCoreApplication.translate("frm_graph", "Del", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionVersion.setText(
            QCoreApplication.translate("frm_graph", "Versi\u00f3n", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionVersion.setShortcut(
            QCoreApplication.translate("frm_graph", "F1", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionInvert_X.setText(
            QCoreApplication.translate("frm_graph", "Invertir X", None)
        )
        # if QT_CONFIG(statustip)
        self.actionInvert_X.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Invertir el signo de los movimientos en el eje X", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionInvert_X.setShortcut(
            QCoreApplication.translate("frm_graph", "Alt+X", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionInvert_Y.setText(
            QCoreApplication.translate("frm_graph", "Invertir Y", None)
        )
        # if QT_CONFIG(statustip)
        self.actionInvert_Y.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Invertir el signo de los movimientos en el eje Y", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionInvert_Y.setShortcut(
            QCoreApplication.translate("frm_graph", "Alt+Y", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionInvert_Z.setText(
            QCoreApplication.translate("frm_graph", "Invertir Z", None)
        )
        # if QT_CONFIG(statustip)
        self.actionInvert_Z.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Invertir el signo de los movimientos en el eje Z", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionInvert_Z.setShortcut(
            QCoreApplication.translate("frm_graph", "Alt+Z", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionMove_up.setText(
            QCoreApplication.translate("frm_graph", "Mover arriba", None)
        )
        # if QT_CONFIG(statustip)
        self.actionMove_up.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Mover hacia arriba las l\u00edneas seleccionadas", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionMove_up.setShortcut(
            QCoreApplication.translate("frm_graph", "Alt+Up", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionMove_down.setText(
            QCoreApplication.translate("frm_graph", "Mover abajo", None)
        )
        # if QT_CONFIG(statustip)
        self.actionMove_down.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Mover hacia abajo las l\u00edneas seleccionadas", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionMove_down.setShortcut(
            QCoreApplication.translate("frm_graph", "Alt+Down", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionGo_to.setText(
            QCoreApplication.translate("frm_graph", "Ir a programa", None)
        )
        # if QT_CONFIG(statustip)
        self.actionGo_to.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Cambiar al programa CNC seleccionado", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionGo_to.setShortcut(
            QCoreApplication.translate("frm_graph", "Alt+Right", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionReturn_to.setText(
            QCoreApplication.translate("frm_graph", "Regresar a programa      ", None)
        )
        # if QT_CONFIG(statustip)
        self.actionReturn_to.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Regresar al programa CNC anterior", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionReturn_to.setShortcut(
            QCoreApplication.translate("frm_graph", "Alt+Left", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionShow_functions.setText(
            QCoreApplication.translate("frm_graph", "Barra de funciones", None)
        )
        # if QT_CONFIG(statustip)
        self.actionShow_functions.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Mostrar la barra de funciones", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionShow_functions.setShortcut(
            QCoreApplication.translate("frm_graph", "0", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionShow_tape1_widget.setText(
            QCoreApplication.translate("frm_graph", "Ventana programa 1", None)
        )
        # if QT_CONFIG(statustip)
        self.actionShow_tape1_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Mostrar la ventana del programa principal", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionShow_tape1_widget.setShortcut(
            QCoreApplication.translate("frm_graph", "1", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionShow_tape2_widget.setText(
            QCoreApplication.translate("frm_graph", "Ventana programa 2", None)
        )
        # if QT_CONFIG(statustip)
        self.actionShow_tape2_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Mostrar la ventana del programa secundario", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionShow_tape2_widget.setShortcut(
            QCoreApplication.translate("frm_graph", "2", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionHide_functions.setText(
            QCoreApplication.translate("frm_graph", "Barra de funciones", None)
        )
        # if QT_CONFIG(statustip)
        self.actionHide_functions.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Ocultar la barra de funciones", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionHide_functions.setShortcut(
            QCoreApplication.translate("frm_graph", "9", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionHide_tape1_widget.setText(
            QCoreApplication.translate("frm_graph", "Ventana programa 1", None)
        )
        # if QT_CONFIG(statustip)
        self.actionHide_tape1_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Ocultar la ventana del programa principal", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionHide_tape1_widget.setShortcut(
            QCoreApplication.translate("frm_graph", "4", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionHide_tape2_widget.setText(
            QCoreApplication.translate("frm_graph", "Ventana programa 2", None)
        )
        # if QT_CONFIG(statustip)
        self.actionHide_tape2_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Ocultar la ventana del programa secundario", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionHide_tape2_widget.setShortcut(
            QCoreApplication.translate("frm_graph", "5", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSeleccionar_maquina.setText(
            QCoreApplication.translate("frm_graph", "Seleccionar m\u00e1quina", None)
        )
        # if QT_CONFIG(statustip)
        self.actionSeleccionar_maquina.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Seleccionar el tipo de m\u00e1quina a programar", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionSeleccionar_maquina.setShortcut(
            QCoreApplication.translate("frm_graph", "Ctrl+M", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionShow_config_widget.setText(
            QCoreApplication.translate("frm_graph", "Esquema programa", None)
        )
        # if QT_CONFIG(statustip)
        self.actionShow_config_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Mostrar el esquema del programa", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionShow_config_widget.setShortcut(
            QCoreApplication.translate("frm_graph", "3", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionHide_config_widget.setText(
            QCoreApplication.translate("frm_graph", "Esquema programa", None)
        )
        # if QT_CONFIG(statustip)
        self.actionHide_config_widget.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Ocultar el esquema del programa", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionHide_config_widget.setShortcut(
            QCoreApplication.translate("frm_graph", "6", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionBlock.setText(
            QCoreApplication.translate("frm_graph", "Bloquear l\u00edneas", None)
        )
        # if QT_CONFIG(statustip)
        self.actionBlock.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Bloquear las l\u00edneas seleccionadas", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionBlock.setShortcut(QCoreApplication.translate("frm_graph", "/", None))
        # endif // QT_CONFIG(shortcut)
        self.actionGraph.setText(
            QCoreApplication.translate("frm_graph", "Graficar tape", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionGraph.setShortcut(
            QCoreApplication.translate("frm_graph", "Ctrl+G", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("frm_graph", "Archivo", None))
        self.dock_functions.setWindowTitle(
            QCoreApplication.translate("frm_graph", "Funciones", None)
        )
        self.groupBox_program.setTitle(
            QCoreApplication.translate("frm_graph", "Programa", None)
        )
        # if QT_CONFIG(tooltip)
        self.btn_free.setToolTip(
            QCoreApplication.translate(
                "frm_graph", "Agrega comandos personalizados por el usuario", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn_free.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Agrega comandos personalizados por el usuario", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.btn_free.setText(
            QCoreApplication.translate("frm_graph", "C\u00f3digo &Libre", None)
        )
        # if QT_CONFIG(tooltip)
        self.btn_end.setToolTip(
            QCoreApplication.translate(
                "frm_graph",
                "Agrega los comandos de finalizaci\u00f3n del programa",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn_end.setStatusTip(
            QCoreApplication.translate(
                "frm_graph",
                "Agrega los comandos de finalizaci\u00f3n del programa",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.btn_end.setText(
            QCoreApplication.translate("frm_graph", "&Finalizar programa", None)
        )
        # if QT_CONFIG(tooltip)
        self.btn_comment.setToolTip(
            QCoreApplication.translate(
                "frm_graph",
                "Agrega comentarios para facilitar la comprensi\u00f3n del programa",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn_comment.setStatusTip(
            QCoreApplication.translate(
                "frm_graph",
                "Agrega comentarios para facilitar la comprensi\u00f3n del programa",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.btn_comment.setText(
            QCoreApplication.translate("frm_graph", "&Comentario", None)
        )
        # if QT_CONFIG(tooltip)
        self.btn_header.setToolTip(
            QCoreApplication.translate(
                "frm_graph", "Agrega el encabezado del programa", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn_header.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Agrega el encabezado del programa", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.btn_header.setText(
            QCoreApplication.translate("frm_graph", "&Iniciar programa", None)
        )
        # if QT_CONFIG(tooltip)
        self.btn_subrutine.setToolTip(
            QCoreApplication.translate(
                "frm_graph", "Llama la subrutina dentro del programa principal", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn_subrutine.setStatusTip(
            QCoreApplication.translate(
                "frm_graph", "Llama la subrutina dentro del programa principal", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.btn_subrutine.setText(
            QCoreApplication.translate("frm_graph", "Llamar Subrutina", None)
        )

    # retranslateUi
