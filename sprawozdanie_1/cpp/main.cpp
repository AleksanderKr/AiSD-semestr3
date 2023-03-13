#include <iostream>
#include <vector>

using namespace std;


float func_float(float y, float z){
    return 108 - (815 - 1500 / y) / z;
}

double func_double(double y, double z){
    return 108 - (815 - 1500 / y) / z;
}

long double func_l_d(long double y, long double z){
    return 108 - (815 - 1500 / y) / z;
}

__float128 func_float128(__float128 y, __float128 z){
    return 108 - (815 - 1500 / y) / z;
}

int precision_float(){
    std::vector<float> x = {4, 4.25};
    int i = 0;
    float tmp = 0;

    while(tmp < 5){
        tmp = func_float(x[i], x[i+1]);
        x.push_back(tmp);
        i += 1;
        cout << i << "   " << tmp << "\n";
    }
}

int precision_double(){
    std::vector<double> x = {4, 4.25};
    int i = 0;
    double tmp = 0;

    while(tmp < 5){
        tmp = func_double(x[i], x[i+1]);
        x.push_back(tmp);
        i += 1;
        cout << i << "   " << tmp << "\n";
    }
    return 0;
}
int precision_long_double(){
    std::vector<long double> x = {4, 4.25};
    int i = 0;
    long double tmp = 0;

    while(tmp < 5){
        tmp = func_l_d(x[i], x[i+1]);
        x.push_back(tmp);
        i += 1;
        cout << i << "   " << tmp << "\n";
    }
    return 0;
}

int precision_float128(){
    std::vector<__float128> x = {4, 4.25};
    int i = 0;
    __float128 tmp = 0;

    while(tmp < 5){
        tmp = func_float128(x[i], x[i+1]);
        x.push_back(tmp);
        i += 1;
        cout << i << "   " << static_cast<long double>(tmp) << "\n";
    }
    return 0;
}

int main(){

    //precision_float();                //5
    //precision_double();             //10
    //precision_long_double();        //13
    precision_float128();           //22
    return 0;
}
