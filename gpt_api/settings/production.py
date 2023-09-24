from .base import *

if not DEBUG:
    ADMINS = [
        ("Muzamil Ali", "muzmmila141@gmail.com"),
    ]

    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.

    ALLOWED_HOSTS.append("bookskai.com")
    RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
        ALLOWED_HOSTS.append("*")

    # Email setting
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = True

    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    SENDGRID_API_KEY = "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"
    EMAIL_HOST_USER = "mly88207@gmail.com"
    EMAIL_HOST_PASSWORD = "mwnieujlittzbzlz"
    RECIPIENT_ADDRESS = "muzmmila141@gmail.com"
    SERVER_EMAIL = EMAIL_HOST_USER
