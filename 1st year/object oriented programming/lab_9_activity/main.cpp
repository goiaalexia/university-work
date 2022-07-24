template <typename T>
class Comparator: {
public:
    Comparator();
    virtual bool compare(T t1, T t2) = 0;

};