from urllib.parse import urlparse

import pytest

from django.urls import reverse

from tests.base.views import BaseViewTest


@pytest.mark.sso_mark
class GitHubIdentityTest(BaseViewTest):
    def test_wrong_provider_raises_404(self):
        auth_path = reverse('oauth:create_identity', kwargs={'provider': 'undefined'})
        resp = self.client.get(auth_path)
        assert resp.status_code == 404

    def test_get_redirects_to_login(self):
        auth_path = reverse('oauth:create_identity', kwargs={'provider': 'github'})
        resp = self.client.get(auth_path)
        redirect = urlparse(resp['Location'])
        assert resp.status_code == 302
        assert redirect.path == reverse('users:registration_complete')

    def test_flow(self):
        auth_path = reverse('oauth:create_identity', kwargs={'provider': 'github'})

        resp = self.client.post(auth_path)
        assert resp.status_code == 302
        redirect = urlparse(resp['Location'])
        assert redirect.scheme == 'https'
        assert redirect.netloc == 'github.com'
        assert redirect.path == '/login/oauth/authorize'
