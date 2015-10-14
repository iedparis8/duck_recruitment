# -*- coding: utf8 -*-
from xadmin import views
import xadmin

from django.views.decorators.cache import never_cache
from xadmin.views import filter_hook

from duck_recruitment.models import Titulaire


class RecruitmentDashboard(views.Dashboard):
    base_template = "duck_recruitment/declare_agent.html"
    widget_customiz = False

    def get_context(self):
        context = super(RecruitmentDashboard, self).get_context()
        # context['personnes'] = Personnel.objects.root_nodes()
        return context

    @filter_hook
    def get_breadcrumb(self):
        return [{'url': self.get_admin_url('index'), 'title': 'Accueil'},]

    @never_cache
    def get(self, request, *args, **kwargs):
        self.widgets = self.get_widgets()
        return self.template_response(self.base_template, self.get_context())

xadmin.site.register_view(r'^recruitment/$', RecruitmentDashboard, 'recruitment_dashboard')

xadmin.site.register(Titulaire)

