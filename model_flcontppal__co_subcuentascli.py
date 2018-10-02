# @class_declaration interna_co_subcuentascli #
from YBUTILS.viewREST import helpers
from models.flcontppal import models as modelos
import importlib


class interna_co_subcuentascli(modelos.mtd_co_subcuentascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration alta_clientes_co_subcuentascli #
class alta_clientes_co_subcuentascli(interna_co_subcuentascli, helpers.MixinConAcciones):
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


# @class_declaration co_subcuentascli #
class co_subcuentascli(alta_clientes_co_subcuentascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.flcontppal.co_subcuentascli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
