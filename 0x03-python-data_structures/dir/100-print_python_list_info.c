#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{

/*	PyTypeObject *type = Py_TYPE(p);
	to get each item type*/
	PyListObject *obj = (PyListObject *)p;
	
	printf("[*] Size of the Python List = %li\n", Py_SIZE(p));
	printf("[*] Allocated = %li\n", obj->allocated);
}
