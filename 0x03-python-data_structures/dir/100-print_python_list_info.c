#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
/*	Py_ssize_t len;

	len = PyList_Size(p);*/
	printf("Hello: %li\n", PyList_GET_SIZE(p));
	printf("Hello: %li\n", PyList_Size(p));
}
