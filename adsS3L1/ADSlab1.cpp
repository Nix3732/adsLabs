#include <iostream>
#include <string>
#include <locale.h>
#include <stack>


bool check(std::string str)
{   
    std::stack<int> stc;

    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] != ')' and str[i] != '}' and str[i] != ']' and str[i] != '(' and str[i] != '{' and str[i] != '[')
        {
            std::cout << "В строке присутствует лишний символ" << std::endl;
            return false;
        }
        if (str[i] == '(' || str[i] == '[' || str[i] == '{')
        {
            stc.push(str[i]);
        }
        else
        {
            if (str[i] == ')' and !stc.empty() and stc.top() == '(')
            {
                stc.pop();
            }
            else if (str[i] == '}' and !stc.empty() and stc.top() == '{') 
            {
                stc.pop();
            }
            else if (str[i] == ']' and !stc.empty() and stc.top() == '[') 
            {
                stc.pop();
            }
            else if ((str[i] == ')' || str[i] == '}' || str[i] == ']') and stc.empty()) 
            {
                std::cout << "Закрывающая скобка ничего не закрывает" << std::endl;
            }
        }
    }
    if (stc.empty()) 
    {
        std::cout << "Строка сущесвтует" << std::endl;
        return true;
    }
    else
    {   
        std::cout << "Сущесвтует не закрытая скобка" << std::endl;
        return false;
    }

}

int main()
{   
    setlocale(LC_ALL, "Russian");

    std::string str;
    std::cout << "Введите последовательность скобок" << std::endl;
    std::cin >> str;
    
    if (str.length() == 0)
    {
        std::cout << "Пустая строка" << std::endl;
        return 0;
    }
    check(str);
}
