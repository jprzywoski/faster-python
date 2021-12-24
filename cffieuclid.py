from cffi import FFI

ffi = FFI()
ffi.cdef("double dist(const double *a, const double *b, int n);")
lib = ffi.dlopen("./libdist.so")
fn = lib.dist


def dist(x, y):
    p = ffi.cast("const double *", ffi.from_buffer(x))
    q = ffi.cast("const double *", ffi.from_buffer(y))
    return fn(p, q, len(x))
