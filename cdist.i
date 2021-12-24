%module cdist

%{
    #define SWIG_FILE_WITH_INIT
    #include "cdist.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}


%apply (double* IN_ARRAY1, int DIM1) {(double* vec1, int len1), (double* vec2, int len2)}

%include "cdist.h"
%rename (dist) my_dist;

%inline %{
    double my_dist(double* vec1, int len1, double* vec2, int len2) {
    if (len1 != len2) {
        PyErr_Format(PyExc_ValueError, "Arrays of lengths (%d,%d) given", len1, len2);
        return 0.0;
    }
    return dist(vec1, vec2, len1);
}
%}