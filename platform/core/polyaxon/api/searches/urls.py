from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import re_path

from api.searches import views
from constants.urls import ID_PATTERN, OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN

searches_urlpatterns = [
    re_path(r'^searches/{}/{}/groups/?$'.format(OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN),
            views.ExperimentGroupSearchListView.as_view()),
    re_path(r'^searches/{}/{}/experiments/?$'.format(OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN),
            views.ExperimentSearchListView.as_view()),
    re_path(r'^searches/{}/{}/builds/?$'.format(OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN),
            views.BuildSearchListView.as_view()),
    re_path(r'^searches/{}/{}/jobs/?$'.format(OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN),
            views.JobSearchListView.as_view()),
    re_path(r'^searches/{}/{}/notebooks/?$'.format(OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN),
            views.NotebookSearchListView.as_view()),
    re_path(r'^searches/{}/{}/tensorboards/?$'.format(OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN),
            views.TensorboardSearchListView.as_view()),

    re_path(r'^searches/{}/{}/groups/{}?$'.format(
        OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, ID_PATTERN),
        views.ExperimentGroupSearchDeleteView.as_view()),
    re_path(r'^searches/{}/{}/experiments/{}?$'.format(
        OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, ID_PATTERN),
        views.ExperimentSearchDeleteView.as_view()),
    re_path(r'^searches/{}/{}/builds/{}?$'.format(
        OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, ID_PATTERN),
        views.BuildSearchDeleteView.as_view()),
    re_path(r'^searches/{}/{}/jobs/{}?$'.format(
        OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, ID_PATTERN),
        views.JobSearchDeleteView.as_view()),
    re_path(r'^searches/{}/{}/notebooks/{}?$'.format(
        OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, ID_PATTERN),
        views.NotebookSearchDeleteView.as_view()),
    re_path(r'^searches/{}/{}/tensorboards/{}?$'.format(
        OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, ID_PATTERN),
        views.TensorboardSearchDeleteView.as_view()),
]

urlpatterns = format_suffix_patterns(searches_urlpatterns)
