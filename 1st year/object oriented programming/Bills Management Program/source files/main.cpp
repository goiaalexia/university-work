#include "../header files/ui.h"

int main(){
    Repo r;
    Service s = Service(r);
    UI ui = UI(s);
    ui.start_ui();
    return 0;
}
