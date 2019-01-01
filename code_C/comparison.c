int main(void) {
// Par multiplications
  int base, pow;
  int res;
  base = 2;
  pow = 10;
  res = 1;
  for(int i=0; i<pow; i++)
      res *= base;
// Par décalage
  int res2 = 1;
  res2 = res2 << pow;
// Validation  
  if (res == res2)
     return 0;
  else 
     return -1;
}
