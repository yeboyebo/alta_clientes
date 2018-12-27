
# @class_declaration alta_clientes #
from YBLEGACY.constantes import *


class alta_clientes(flfactppal):

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
        super().__init__(context)

    def cambiarDomFacturacion(self, model, oParam):
        return self.ctx.alta_clientes_cambiarDomFacturacion(model, oParam)

    def cambiarDomEnvio(self, model, oParam):
        return self.ctx.alta_clientes_cambiarDomEnvio(model, oParam)

    def cambiarDom(self, tipo, oParam):
        return self.ctx.alta_clientes_cambiarDom(tipo, oParam)

