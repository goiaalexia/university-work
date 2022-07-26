#include <string>
#include "subject.h"
#include "UserMessage.h"

class ChatSession : public Subject {
private:
    std::vector<UserMessage> messages;
public:

    void addMessage(std::string user, std::string msg) {
        auto m = UserMessage(user, msg);
        this->messages.push_back(m);
        this->notify();
    }
};