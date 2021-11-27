
#ifndef __LIBMYPY_H__
#define __LIBMYPY_H__

#include <Python.h>
 extern "C" {
PyObject * _decrypt(PyObject *, PyObject *);
PyObject * _encrypt(PyObject *, PyObject *);
}
#endif