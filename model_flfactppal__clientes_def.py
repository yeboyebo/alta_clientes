# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration alta_clientes #
from YBLEGACY.constantes import *
from YBUTILS import gesDoc


class alta_clientes(interna):

    def alta_clientes_initValidation(self, name, data=None):
        response = True
        return response

    def alta_clientes_iniciaValoresLabel(self, model=None, template=None, cursor=None):
        labels = {}
        return labels

    def alta_clientes_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def alta_clientes_getFilters(self, model, name, template=None):
        filters = []
        return filters

    def alta_clientes_getForeignFields(self, model, template=None):
        fields = []
        return fields

    def alta_clientes_getDesc(self):
        desc = "nombre"
        return desc

    def alta_clientes_subirDocSepa(self, model, oParam):
        response = True
        nombre = "Mandato SEPA"
        tipo = "SEPA"
        if not gesDoc.fileUpload("clientes", model.codcliente, oParam['FILES'], nombre=nombre, tipo=tipo):
            return False
        return response

    def __init__(self, context=None):
        super(alta_clientes, self).__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.alta_clientes_initValidation(name, data)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None):
        return self.ctx.alta_clientes_iniciaValoresLabel(model, template, cursor)

    def bChLabel(self, fN=None, cursor=None):
        return self.ctx.alta_clientes_bChLabel(fN, cursor)

    def getFilters(self, model, name, template=None):
        return self.ctx.alta_clientes_getFilters(model, name, template)

    def getForeignFields(self, model, template=None):
        return self.ctx.alta_clientes_getForeignFields(model, template)

    def getDesc(self):
        return self.ctx.alta_clientes_getDesc()

    def subirDocSepa(self, model, oParam):
        return self.ctx.alta_clientes_subirDocSepa(model, oParam)


# @class_declaration head #
class head(alta_clientes):

    def __init__(self, context=None):
        super(head, self).__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super(ifaceCtx, self).__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
