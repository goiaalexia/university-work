#include <string>
#include <utility>

class UserMessage {
private:
    std::string msg;
    std::string user;
public:
    UserMessage(std::string u, std::string msg) {
        this->user = std::move(u);
        this->msg = std::move(msg);
    }
};
