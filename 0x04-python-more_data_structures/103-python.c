#include <stdio.h>
#include "Python.h"


void print_python_bytes(PyObject *p);

/**
 * print_python_list_info - prints some basic information about python list
 * @p: pointer to an object
 */
void print_python_list(PyObject *p)
{
	long int i, len;
	PyListObject *obj = (PyListObject *)p;
	PyListObject *item;
	len = obj->ob_base.ob_size;

	printf("[.] Python list info\n");
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < len; i++)
	{
		item = (PyListObject *)obj->ob_item[i];
		printf("Element %li: %s\n", i, item->ob_base.ob_base.ob_type->tp_name);
		if (strcmp(item->ob_base.ob_base.ob_type->tp_name, "bytes") == 0)
			print_python_bytes((obj->ob_item[i]));
	}
}

/**
 * print_python_bytes - prints some basic info about python bytes objects
 * @p: pointer to an object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *obj = (PyBytesObject *)p;
	unsigned int i, size, temp;

	printf("[.] bytes object info\n");
	if (strcmp(obj->ob_base.ob_base.ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = obj->ob_base.ob_size;
	printf("  size: %u\n", size);
	printf("  trying string: %s\n", obj->ob_sval);

	printf("  first %u bytes: ", size > 10? 10: size + 1);

	for (i = 0; i < 10; i++)
	{
		
		if (i == size + 1)
		{
			printf("%02x\n", obj->ob_sval[i]);
			return;
		}
		temp = obj->ob_sval[i] & 0xFF;
		printf("%02x ", temp);
	}
	putchar('\n');

}
