
# @class_declaration alta_clientes_dirclientes #
class alta_clientes_dirclientes(flfactppal_dirclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def cambiarDomFacturacion(self, oParam):
        return form.iface.cambiarDomFacturacion(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def cambiarDomEnvio(self, oParam):
        return form.iface.cambiarDomEnvio(self, oParam)

