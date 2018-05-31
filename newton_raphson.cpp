#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

template<class T>
T function_derivative(T x)
{
    return(8*x - 4);

}
template<class T>
T function(T x)
{
    return(4*x*x - 4*x + 1);
}

template<class T>
T newton_raphson(T x)
{
    float h =  function(x)/function_derivative(x);
    while(fabs(h) > 0.0001)
    {
        h = function(x)/function_derivative(x);
        x = x - h;
    }
    return x;

}

int main()
{
    float x = 12;

    cout<<"root is "<<newton_raphson(x)<<endl;
    return 0;
}
