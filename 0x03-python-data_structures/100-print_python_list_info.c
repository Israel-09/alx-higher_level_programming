#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints some basic information about python list
 * @p: pointer to an object
 */
void print_python_list_info(PyObject *p)
{
	long int i, len;
	PyListObject *obj = (PyListObject *)p;
	PyListObject *item;
	len = obj->ob_base.ob_size;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < len; i++)
	{
		item = (PyListObject *)obj->ob_item[i];
		printf("Element %li: %s\n", i, item->ob_base.ob_base.ob_type->tp_name);
	}
}
