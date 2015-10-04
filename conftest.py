"""
Configuration file for py.test
"""

import django


def pytest_configure():
    from django.conf import settings
    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "test.sqlite3",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            # "django.contrib.sites",
            "taggit",
            "taggit_labels",
            "test_app",
        ],
        MIDDLEWARE_CLASSES=(),
        SITE_ID=1,
    )
    try:
        django.setup()
    except AttributeError:
        # Django 1.7 or lower
        pass
