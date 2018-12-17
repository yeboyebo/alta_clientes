
# @class_declaration alta_clientes_clientes #
class alta_clientes_clientes(flfactppal_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def subirDocSepa(self, oParam):
        return form.iface.subirDocSepa(self, oParam)

