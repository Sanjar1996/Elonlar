from django.shortcuts import redirect
from django.contrib import messages

class LogoutRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'Siz tizimga kirgansiz!!')
            return redirect('articles:index')
        return super().dispatch(request, *args, **kwargs)