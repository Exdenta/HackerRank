#include <algorithm>
#include <iostream>
#include <vector>
#include <fstream>
#include <list>
#include <stack>

// Сгенерировать все возможные правильные последовательности длины N.
// Например, последовательности «(())()», «()» и «(()(()))» — правильные, 
// в то время как «)(», «(()» и «(()))(» — нет.

using namespace std;

class Sequence
{
public:
    std::string result_;

    // N - '(' left to add
    int n_;

    // M - ')' left to add
    int m_;

    Sequence(int n, int m) : result_(""), n_(n), m_(m) {}

    Sequence(std::string s, int n, int m) : result_(s), n_(n), m_(m) {}

    Sequence *copy()
    {
        return new Sequence(result_, n_, m_);
    }
};

void generateSequences(int num)
{
    std::vector<std::string> str_seq;

    std::stack<Sequence *> sequences;
    sequences.push(new Sequence(num, num));

    while (!sequences.empty())
    {
        Sequence *sequence = sequences.top(); 
        sequences.pop();

        // equal amount of 0 and 1
        if (sequence->n_ == sequence->m_)
        {
            if (sequence->n_ != 0)
            {
                sequence->result_.append("("); 
                sequence->n_--;
                sequences.push(sequence); 
            }
            else
            {
                str_seq.push_back(sequence->result_);
                delete sequence;
            }
        }
        else
        {
            if (sequence->n_ != 0)
            {
                sequences.push(new Sequence(sequence->result_ + "(",
                                            sequence->n_ - 1,
                                            sequence->m_));
            }

            sequence->result_.append(")");
            sequence->m_--;
            sequences.push(sequence);
        }
    }

    std::sort(str_seq.begin(), str_seq.end());  

    for(auto it = str_seq.begin(); it != str_seq.end(); it++){
        std::cout <<  *it << std::endl;
    }
}

int main()
{
    int len = 5;
    generateSequences(len);

    return 0;
}