from .processbuilder import ProcessBuilder

class KubeBuilder(ProcessBuilder):
    # override server image by user option
    async def prespawn_server_options(self, dashboard, dashboard_user, ns):
        res = {}
        if dashboard.image:
            res['image'] = dashboard.image
        return res
