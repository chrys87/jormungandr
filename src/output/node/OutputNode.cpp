#include "OutputNode.h"
#include "../../node/node.h"
#include <boost/locale.hpp>
#include <iostream>

#include <ctime>
#include <string>

int main()
{
    using namespace boost::locale;
    using namespace std;
    Node n = Node();
    //Node n = Node("127.0.0.1", 22447);
    n.connect();
    string lineOut;
    string lineIn;    
    cin >> lineIn;
    n.sendLine(lineIn);
    n.getLine(lineOut);
    cout << "echo: " << lineOut << endl;
    
}
