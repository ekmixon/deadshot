from deadshot.services.common.secrets_loader import get_secrets
import os
# Configuration settings for Github


class GithubConfig:
    def get_github_secrets(self):
        _github_secrets = get_secrets("SECRET_GITHUB_SECRET")
        webhook_secret = _github_secrets["webhook_secret"]
        integration_id = int(_github_secrets["github_app_integration_id"])
        app_pem = _github_secrets["github_app_pem_key"]
        return integration_id, app_pem

    def get_github_url(self):
        return os.environ.get("GITHUB_URL")

    def get_github_webhook_secret(self):
        _github_secrets = get_secrets("SECRET_GITHUB_SECRET")
        return _github_secrets["webhook_secret"]

    def get_github_api(self):
        return os.environ.get("GITHUB_API")

    def get_github_app_name(self):
        return os.environ.get("GITHUB_APP_NAME")
