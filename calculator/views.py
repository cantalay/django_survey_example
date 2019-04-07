
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import numpy as np
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

def index(request):
    s = np.random.normal(0.5, 0.1, 100)
    for x in s:
        return HttpResponse(x)

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        """Return 3 dataset to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()