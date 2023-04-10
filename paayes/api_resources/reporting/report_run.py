from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import ListableAPIResource


class ReportRun(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "reporting.report_run"
