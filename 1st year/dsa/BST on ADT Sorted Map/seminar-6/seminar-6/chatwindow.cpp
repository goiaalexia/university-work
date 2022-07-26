//
// Created by lexig on 02.06.2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_chatWindow.h" resolved

#include "chatwindow.h"
#include "ui_chatWindow.h"


chatWindow::chatWindow(QWidget *parent) :
        QWidget(parent), ui(new Ui::chatWindow) {
    ui->setupUi(this);
}

chatWindow::~chatWindow() {
    delete ui;
}

