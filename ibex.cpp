#include "ibex.h"
using namespace ibex;

#define __PREC__ 1e-11
#define __METH__ RK4
#define __DURATION__ 16.0

Interval p1(0.2,0.3);
const double p2 = 1.9255;
const double p3 = 0.1451;

int main() 
{
    //Dimention of IVP
    const int n = 2;
    
    //State Variables
    Variable y(n);
    
    //Initial Conditions
    IntervalVector yinit(n);
    yinit[0] = Interval(1,1);
    yinit[1] = Interval(0,0);
    
    //Function
    Function ydot = Function (y, Return ((-(p3+p1)*y[0]) + (p2*y[1]) , (p3*y[0]) - (p2*y[1])));
    
    //IVP with initial time = 0
    ivp_ode problem = ivp_ode (ydot, 0.0, yinit);
    
    //Simulation and Run
    Simulation simu = simulation (&problem, __DURATION__, __METH__, __PREC__);
    simu.run_simulation();
    simu.export_yn("ivp.txt")
  
    // For having the result in t=16, we can uncomment following lines
    /*
    std::cout<<"Verified Numerical Solution"<<std::endl;
    std::cout<<"Solution Enclosure at t= "<<__DURATION__<<std::endl;
    
    IntervalVector ylast(n);
    ylast = simu.get_last();
    for(int i=0; i<n; i++)
    {
        std::cout<<ylast[i]<<'\t';
    }
    std::cout<<std::endl;
    */
    return 0;
}
        
    
