from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from users.models import CustomUser


class UserRegisterView(TemplateView):
    template_name = 'register.html'


class UserMakeRegisterView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST

        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            user = CustomUser.objects.create_user(
                email=email, password=password1,
                first_name=first_name, last_name=last_name,
            )
            return render(request, 'product-list.html')
        else:
           pass

