
# @class_declaration alta_clientes #
from YBLEGACY.constantes import *
from YBUTILS import gesDoc


class alta_clientes(flfactppal):

    def alta_clientes_subirDocSepa(self, model, oParam):
        response = True
        nombre = "Mandato SEPA"
        tipo = "SEPA"
        if not gesDoc.fileUpload("clientes", model.codcliente, oParam['FILES'], nombre=nombre, tipo=tipo):
            return False
        return response

    def __init__(self, context=None):
        super().__init__(context)

    def subirDocSepa(self, model, oParam):
        return self.ctx.alta_clientes_subirDocSepa(model, oParam)

