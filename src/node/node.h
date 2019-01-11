#ifndef NODE_H
#define NODE_H
#include <iostream>

using namespace std;

class Node {

    private:
        int i = 5;
    public:
        Node();
        ~Node();
        void printI(void);
};
#endif // NODE_H
