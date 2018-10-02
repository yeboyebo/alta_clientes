# @class_declaration interna_ejercicios #
from YBUTILS.viewREST import helpers
from models.flfactppal import models as modelos
import importlib


class interna_ejercicios(modelos.mtd_ejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration alta_clientes_ejercicios #
class alta_clientes_ejercicios(interna_ejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def initValidation(name, data=None):
        return form.iface.initValidation(name, data)

    def iniciaValoresLabel(self, template=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, template, cursor)

    def bChLabel(fN=None, cursor=None):
        return form.iface.bChLabel(fN, cursor)

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getDesc():
        return form.iface.getDesc()


# @class_declaration ejercicios #
class ejercicios(alta_clientes_ejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.flfactppal.ejercicios_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
