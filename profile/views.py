"""
-- whats cooking harman internal project
"""
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.views.generic import FormView

from forms import LoginForm, EMP_USER


class LoginView(FormView):
    """ login page """
    form_class = LoginForm
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        return super(LoginView, self).get(self, request, *args, **kwargs)

    def form_valid(self, form):
        """ save the user type in session and redirect to home page """
        user_type = form.cleaned_data.get('user_type')
        message = 'Invalid login'

        # if user employee type do ldap verification and login.
        if user_type == EMP_USER:
            # do ldap coding here !
            user = None
            message = "LDAP authenticate is not implemented yet!!"
        else:
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse('home'))
        form.errors.update({'username': message})
        return render_to_response(self.template_name, context_instance=RequestContext(self.request, {'form': form}))


def logout_view(request):
    """ logout page """
    logout(request)
    return HttpResponseRedirect(reverse('home'))