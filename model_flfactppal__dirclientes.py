# @class_declaration interna_dirclientes #
from YBUTILS.viewREST import helpers
from models.flfactppal import models as modelos
import importlib


class interna_dirclientes(modelos.mtd_dirclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration alta_clientes_dirclientes #
class alta_clientes_dirclientes(interna_dirclientes, helpers.MixinConAcciones):
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

    @helpers.decoradores.accion(aqparam=["oParam"])
    def cambiarDomFacturacion(self, oParam):
        return form.iface.cambiarDomFacturacion(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def cambiarDomEnvio(self, oParam):
        return form.iface.cambiarDomEnvio(self, oParam)


# @class_declaration dirclientes #
class dirclientes(alta_clientes_dirclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.flfactppal.dirclientes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
