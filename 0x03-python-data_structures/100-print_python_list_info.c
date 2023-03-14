#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints some basic information about python list
 * @p: pointer to an object
 */
void print_python_list_info(PyObject *p)
{
	long int i, len;

	len = Py_SIZE(p);
	PyTypeObject *type;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < len; i++)
	{
		type = Py_TYPE(obj->ob_item[i]);
		printf("Element %li: %s\n", i, type->tp_name);
	}
}
