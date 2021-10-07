from django.shortcuts import render, redirect, reverse
from .models import Lead
from .forms import *
from django.views.generic import *
from django.core.mail import send_mail

#crm12
#crm23

class LeadList(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


class LeadDetail(DetailView):
    queryset = Lead.objects.all()
    template_name="leads/lead_detail.html"
    context_object_name = "leads"

def lead_detail(request, pk):
    leads = Lead.objects.get(id=pk)
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_detail.html", context)


class LeadCreate(CreateView):
    form_class = LeadForm
    template_name="leads/create_lead.html"
    context_object_name = "form"

    def get_success_url(self):
        return reverse('lead_list')

    def form_valid(self, form):
        send_mail(subject="A new lead has been createet",message="Go to the site to see the new lead",
         from_email="test@test.com",recipient_list=["yair2321@gmail.com"] )
        return super(LeadCreate, self).form_valid(form)


def lead_create(request):
    create_leads = LeadForm()
    if request.method == 'POST':
        create_leads = LeadForm(request.POST)
        if create_leads.is_valid():
            create_leads.save()
        return redirect('../')
    context = {
        "form": create_leads
    }
    return render(request, "leads/create_lead.html", context)


class LeadUpdate(UpdateView):
    queryset = Lead.objects.all()
    form_class = LeadForm
    template_name="leads/lead_update.html"
    context_object_name = "lead"

    def get_success_url(self):
        return reverse('lead_list')


def update_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    update_lead = LeadForm(instance=lead)
    context = {
        "form": update_lead,
        "lead": lead }
    if request.method == 'POST':
        update_lead = LeadForm(request.POST, instance=lead)
        if update_lead.is_valid():
            update_lead.save()
            return redirect('../../')
    return render(request, "leads/lead_update.html", context)


class LeadDelete(DeleteView):
    queryset = Lead.objects.all()
    template_name="leads/delete_lead.html"
    context_object_name = "lead"

    def get_success_url(self):
        return reverse('lead_list')


def delete_lead(request, pk):
    leads = Lead.objects.get(id=pk)
    if request.method == 'POST':
        leads.delete()
        return redirect('../../')

    context = {"lead": leads }
    return render(request, "leads/delete_lead.html", context)
