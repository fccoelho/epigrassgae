"""
Using redirect route instead of simple routes since it supports strict_slash
Simple route: http://webapp-improved.appspot.com/guide/routing.html#simple-routes
RedirectRoute: http://webapp-improved.appspot.com/api/webapp2_extras/routes.html#webapp2_extras.routes.RedirectRoute
"""

from webapp2_extras.routes import RedirectRoute
import handlers

secure_scheme = 'https'

_routes = [
    RedirectRoute('/taskqueue-send-email/', handlers.SendEmailHandler, name='taskqueue-send-email', strict_slash=True),
    RedirectRoute('/_ah/login_required', handlers.LoginRequiredHandler),
    RedirectRoute('/login/', handlers.LoginHandler, name='login', strict_slash=True),
    RedirectRoute('/logout/', handlers.LogoutHandler, name='logout', strict_slash=True),
    RedirectRoute('/social_login/<provider_name>', handlers.SocialLoginHandler, name='social-login', strict_slash=True),
    RedirectRoute('/social_login/<provider_name>/complete', handlers.CallbackSocialLoginHandler,
                  name='social-login-complete', strict_slash=True),
    RedirectRoute('/social_login/<provider_name>/delete', handlers.DeleteSocialProviderHandler,
                  name='delete-social-provider', strict_slash=True),
    RedirectRoute('/register/', handlers.RegisterHandler, name='register', strict_slash=True),
    RedirectRoute('/activation/<user_id>/<token>', handlers.AccountActivationHandler, name='account-activation',
                  strict_slash=True),
    RedirectRoute('/resend/<user_id>/<token>', handlers.ResendActivationEmailHandler, name='resend-account-activation',
                  strict_slash=True),
    RedirectRoute('/contact/', handlers.ContactHandler, name='contact', strict_slash=True),
    RedirectRoute('/simulations/', handlers.LibraryHandler, name='simulations', strict_slash=True),
    RedirectRoute('/simulations/delete/<simulation_id>/', handlers.SimulationDelete, name='sim-del', strict_slash=True),
    RedirectRoute('/simulations/view/<simulation_id>/', handlers.SimulationHandler, name='sim-view', strict_slash=True),
    RedirectRoute('/simulations/view/<simulation_id>/map/', handlers.SimulationMapHandler, name='sim-map',
                  strict_slash=True),
    RedirectRoute('/simulations/view/<simulation_id>/series/', handlers.SimulationSeriesHandler, name='sim-series',
                  strict_slash=True),
    RedirectRoute('/simulations/view/<simulation_id>/network/', handlers.SimulationNetHandler, name='sim-net',
                  strict_slash=True),
    RedirectRoute('/simulations/view/<simulation_id>/spread/', handlers.SimulationSpreadHandler, name='sim-spread',
                  strict_slash=True),
    RedirectRoute('/simulations/upload/', handlers.UploadHandler, name='carga', strict_slash=True),
    RedirectRoute('/settings/profile', handlers.EditProfileHandler, name='edit-profile', strict_slash=True),
    RedirectRoute('/settings/password', handlers.EditPasswordHandler, name='edit-password', strict_slash=True),
    RedirectRoute('/settings/email', handlers.EditEmailHandler, name='edit-email', strict_slash=True),
    RedirectRoute('/password-reset/', handlers.PasswordResetHandler, name='password-reset', strict_slash=True),
    RedirectRoute('/password-reset/<user_id>/<token>', handlers.PasswordResetCompleteHandler,
                  name='password-reset-check', strict_slash=True),
    RedirectRoute('/change-email/<user_id>/<encoded_email>/<token>', handlers.EmailChangedCompleteHandler,
                  name='email-changed-check', strict_slash=True),
    RedirectRoute('/', handlers.HomeRequestHandler, name='home', strict_slash=True)
]


def get_routes():
    return _routes


def add_routes(app):
    if app.debug:
        secure_scheme = 'http'
    for r in _routes:
        app.router.add(r)
