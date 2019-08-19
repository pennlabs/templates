import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from pennlabs.settings.base import *


DEBUG = False

# Fix MySQL Emoji support
DATABASES['default']['OPTIONS'] = {'charset': 'utf8mb4'}

# Honour the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow production host headers
ALLOWED_HOSTS = ['example.pennlabs.org']

SENTRY_URL = os.environ.get('SENTRY_URL', '')

sentry_sdk.init(
    dsn=SENTRY_URL,
    integrations=[DjangoIntegration()]
)

# Labs Accounts Settings

PLATFORM_ACCOUNTS = {
    'REDIRECT_URI': 'https://example.pennlabs.org/accounts/callback/',
    'ADMIN_PERMISSION': 'example_admin'
}
