from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from app_contact.forms import ContactForm
from app_contact.tasks import send_contact_email_task


class ContactFormView(FormView):
    """Представление формы контактов"""

    template_name = "app_contact/form.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        # Вызываем асинхронную задачу
        send_contact_email_task.delay(data=form.cleaned_data)
        return super().form_valid(form=form)


class ContactThanksView(TemplateView):
    """Представление успешной отправки формы"""

    template_name = "app_contact/thanks.html"
