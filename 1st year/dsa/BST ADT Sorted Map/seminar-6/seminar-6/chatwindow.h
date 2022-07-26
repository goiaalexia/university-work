//
// Created by lexig on 02.06.2022.
//

#ifndef SEMINAR_6_CHATWINDOW_H
#define SEMINAR_6_CHATWINDOW_H

#include <QWidget>


QT_BEGIN_NAMESPACE
namespace Ui { class chatWindow; }
QT_END_NAMESPACE

class chatWindow : public QWidget {
Q_OBJECT

public:
    explicit chatWindow(QWidget *parent = nullptr);

    ~chatWindow() override;

private:
    Ui::chatWindow *ui;
};


#endif //SEMINAR_6_CHATWINDOW_H
