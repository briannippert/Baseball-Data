#include <string>

using namespace std;
class Game
{
    // Access specifier
  public:
    //def __init__(self, ball, strike, out, scoreDiff, outcome, first, second, third, inning, winningTeam=None, id=None):

    // Data Members
    string id;
    int outs;
    int scoreDiff;
    int inning;
    int ball;
    int strike;
    bool first;
    bool second;
    bool third;
    bool winner;
    char outcome;
}