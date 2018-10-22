#include <string>
#include <iostream>
#include <fstream>
#include "json.hpp"

using nlohmann::json;
using namespace std;

string readFile(string);
void parseJSON(string);

int main()
{
    string name;
    cout << "Enter File Name: ";
  //  cin >> name;
    string data = "hello";//readFile(name);
    // cout << data;
    parseJSON(data);
    return 0;
}

string readFile(string path)
{
    string line;
    string data;
    ifstream myfile(path);
    if (myfile.is_open())
    {
        while (getline(myfile, line))
        {
            data += line;
        }
        myfile.close();
    }
    else
    {
        return "Unable to open file";
    }
    return data;
}

void parseJSON(string data)
{
    //   cout << data << "\n";
   string jsonTest = "{ \"name\":\"John\", \"age\":30, \"car\":null }";
    cout << json::parse(jsonTest);
}