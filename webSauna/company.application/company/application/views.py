"""My Application views."""
from websauna.system.http import Request
from websauna.system.core.route import simple_route


# Configure a sample view provided by this addon
@simple_route("/test", route_name="home", renderer='company.application/home.html')
def home(request: Request):
    """Render site homepage."""
    return {"project": "My Application"}
