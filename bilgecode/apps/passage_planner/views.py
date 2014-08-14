from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, DetailView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import Passage

from datetime import date

import stathat

class PlannerHome(TemplateView):
    """
        The landing page for passage planner with a list of passages
        belonging to the authenticated user.
    """

    template_name = "passage_planner/home.html"

    def get_context_data(self, *args, **kwargs):
        _context = super(PlannerHome, self).get_context_data(*args, **kwargs)

        passage_list = []
        if self.request.user.is_authenticated():
            passage_list = Passage.objects.filter(user=self.request.user).order_by('date_created')
        _context['passage_list'] = passage_list

        return _context


class PassageNew(RedirectView):
    """
        Creates a passage and then redirects to that passage
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):

        # stathat statistic for new passage
        stathat.ez_count('ben@bilgecode.com', 'Passages Created', 1)

        p = Passage.objects.create(
            user=self.request.user,
            passage_data={
                "name": "New Passage",
                "departureDate": date.today().strftime("%Y-%m-%d"),
                "waypoints": [],
                "estimatedAvgSpeed": 5,
                "timeZone": "America/New_York"
            }
        )
        return p.get_absolute_url()


class PassageDemo(TemplateView):
    template_name = "passage_planner/demo.html"


class PassageDetail(DetailView):
    """
        Display a specific passage
    """
    template_name = "passage_planner/detail.html"
    slug_field = "hash_key"
    queryset = Passage.objects.all()


class PassageDelete(DeleteView):
    template_name = "passage_planner/delete.html"
    slug_field = "hash_key"
    queryset = Passage.objects.all()
    success_url = reverse_lazy('planner-home')
