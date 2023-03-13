#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
/*	Py_ssize_t len;

	len = PyList_Size(p);*/
	PyTypeObject *type = Py_TYPE(p);
	Py_buffer *buff;
	
	printf("Hello: %s\n", type->tp_name);
	printf("Hello: %li\n", Py_SIZE(p));
	printf("Hello: %li\n", buff->itemsize);
}
