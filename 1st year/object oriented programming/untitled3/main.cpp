#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    QLabel label("Futu-te-n aripa");
    label.show();
    return QApplication::exec();
}
