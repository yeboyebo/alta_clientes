# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration alta_clientes #
from YBLEGACY.constantes import *


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
        desc = "descripcion"
        return desc

    def alta_clientes_cambiarDomFacturacion(self, model, oParam):
        return self.cambiarDom(u"domfacturacion", oParam)

    def alta_clientes_cambiarDomEnvio(self, model, oParam):
        return self.cambiarDom(u"domenvio", oParam)

    def alta_clientes_cambiarDom(self, tipo, oParam):
        aChecked = oParam['selecteds'].split(u",")
        response = {}
        response['status'] = 1
        if len(aChecked) > 1:
            response['msg'] = "Error: Selecciona solo un elemento"
            return response
        if not aChecked[0]:
            response['msg'] = "Error: Selecciona un elemento"
            return response
        cursor = qsatype.FLSqlCursor("dirclientes")
        cursor.select(ustr("id = '", aChecked[0], "'"))
        cursor.setModeAccess(cursor.Edit)
        cursor.refreshBuffer()
        if cursor.first():
            cursorBorrar = qsatype.FLSqlCursor(u"dirclientes")
            cursorBorrar.select(ustr(u"codcliente = '", cursor.valueBuffer(u"codcliente"), u"' AND ", tipo, u" = 'true'"))
            cursorBorrar.first()
            cursorBorrar.setModeAccess(cursorBorrar.Edit)
            cursorBorrar.refreshBuffer()
            cursorBorrar.setValueBuffer(tipo, u"false")
            cursorBorrar.commitBuffer()

            cursor.setValueBuffer(tipo, u"true")
            if not cursor.commitBuffer():
                return False
        return True

    def __init__(self, context=None):
        super(alta_clientes, self).__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.alta_clientes_initValidation(name, data=None)

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

    def cambiarDomFacturacion(self, model, oParam):
        return self.ctx.alta_clientes_cambiarDomFacturacion(model, oParam)

    def cambiarDomEnvio(self, model, oParam):
        return self.ctx.alta_clientes_cambiarDomEnvio(model, oParam)

    def cambiarDom(self, tipo, oParam):
        return self.ctx.alta_clientes_cambiarDom(tipo, oParam)


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
