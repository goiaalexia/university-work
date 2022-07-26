
#include <vector>
#include "observer.h"

class Subject {
private:
    std::vector<Observer*> observers;

public:
    void registerObserver(Observer* o) {
        this->observers.push_back(o);
    }

    void unregisterObserver(Observer* o) {
        for(int i = 0; i < this->observers.size(); i++) {
            if(this->observers[i] == o)
                this->observers.erase(this->observers.begin()+i);
        }
    }

    void notify() {
        for(auto &o : this->observers) {
            o->update();
        }
    }

};