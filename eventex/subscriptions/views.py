from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core import mail
from django.template.loader import render_to_string

def new(request):
    if request.method == 'POST':
        return create(request)
        
    return empty_form(request)


def empty_form(request):
    return render(request,'subscriptions/subscription_form.html',{'form': SubscriptionForm() } )


def create(request):
        form = SubscriptionForm(request.POST)
        if not form.is_valid():
            return render(request,'subscriptions/subscription_form.html',{'form': form })

        subscription = form.save()
        
        _send_mail('Confirmação de Inscrição',settings.DEFAULT_FROM_EMAIL,subscription.email,'subscriptions/subscription_email.txt',{'subscription': subscription})
        messages.success(request,'Inscrição realizada com Sucesso!')

        return HttpResponseRedirect (r('subscriptions:detail',str(subscription.hash_id)))




def detail(request, hash_id):
    try: 
        subscription = Subscription.objects.get(hash_id=hash_id)
    except: 
        Subscription.DoesNotExist
        raise Http404
    
    return render(request,'subscriptions/subscription_detail.html',{'subscription':subscription})


def _send_mail(subject, from_,to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])