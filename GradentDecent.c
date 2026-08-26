#include <stdio.h>

float f(float x){
  return (x*x)+(6*x)+6;
}

float df(float x){
  return (2*x)+6;
}

float GradentDecent(float minimum,float LearningRate,float iterations){
  float x = minimum;
  for (int i=0;i<=iterations;i++) {
    x = x-(LearningRate*df(x));
  }
  return x;
}

int main(){
  float Gradent = GradentDecent(0,0.1,70);
  printf("The Gradent is: ");
  printf("%f\n",Gradent);
}
