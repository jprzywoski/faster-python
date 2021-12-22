from cffi import FFI

ffi = FFI()
ffi.cdef("double cdist(const double *a, const double *b, int n);")
fn = ffi.dlopen("./libdist.so").cdist


def dist(x, y):
    p = ffi.cast("const double *", ffi.from_buffer(x))
    q = ffi.cast("const double *", ffi.from_buffer(y))
    return fn(p, q, len(x))
