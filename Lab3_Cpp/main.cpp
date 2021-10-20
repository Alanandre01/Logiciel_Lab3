#include <new>
#include <windows.h>
#include <dshow.h>
#include <string>
#include <Python.h>
#include "playback.h"

#pragma comment(lib, "strmiids.lib")
using namespace std;

//Contr�le de la vid�o
DShowPlayer* g_pPlayer = NULL;

//Contr�le de la vid�o avec les touches du clavier
void OnChar(wchar_t c)
{
    switch (c)
    {
    case L'p':
    case L'P':
        if (g_pPlayer->State() == STATE_RUNNING)
        {
            g_pPlayer->Pause();
        }
        else
        {
            g_pPlayer->Play();
        }
        break;

    case L'r':
    case L'R':
        if (g_pPlayer->State() == STATE_RUNNING)
        {
            REFERENCE_TIME rtNow = 0;
            g_pPlayer->SetPositions(&rtNow);

        }
        break;

    case L's':
    case L'S':
        delete g_pPlayer;
        g_pPlayer = NULL;
        break;

    case L'q':
    case L'Q':
        delete g_pPlayer;
        g_pPlayer = NULL;
        exit(0);
        break;
    }
}

//Extension python pour initlialisation du player vid�o
static PyObject* initModule(PyObject* self, PyObject* args)
{
    delete g_pPlayer;
    g_pPlayer = new DShowPlayer(PyUnicode_AsUTF8(args));
    g_pPlayer->Play();

    PyObject* python_val = Py_BuildValue("");
    return python_val;
}

//Extension python pour l'ennvoie des touches de clavier
static PyObject* inputChar(PyObject* self, PyObject* args)
{
    OnChar(*PyUnicode_AsUTF8(args));
    
    PyObject* python_val = Py_BuildValue("");
    return python_val;
}

//Cr�ation de l'extension python
static PyMethodDef methods[] = {
    { "initModule", (PyCFunction)initModule, METH_O, "Initialise player" },
    { "inputChar", (PyCFunction)inputChar, METH_O, "Input des touches" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef videoplayer = {
    PyModuleDef_HEAD_INIT,
    "Lab3_Cpp",         /* name of module */
    nullptr,                   /* module documentation, may be NULL */
    -1,                      /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    methods
};

PyMODINIT_FUNC PyInit_Lab3_Cpp(void) {
    return PyModule_Create(&videoplayer);
}