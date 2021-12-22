#include <math.h>

double cdist(const double *a, const double *b, int n) {
  double d = 0.0;
  for (int i = 0; i < n; ++i) {
    d += pow(a[i] - b[i], 2);
  }
  return sqrt(d);
}
