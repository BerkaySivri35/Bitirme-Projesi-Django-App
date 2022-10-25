from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from uyelikSistemi.forms import SignUpForm
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Hesabı Etkinleştirme'
            message = render_to_string('registration/activate_mail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')

            send_mail(mail_subject, message, 'idu.iibf.ybs@outlook.com', [to_email])
            return HttpResponse('Kaydı tamamlamak için lütfen e-posta adresinizi onaylayın')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):
    UserModel = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('E-posta onayınız için teşekkür ederiz. Artık hesabınıza giriş yapabilirsiniz.')
    else:
        return HttpResponse('Aktivasyon bağlantısı geçersiz!')

# Create your views here.
