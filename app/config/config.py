from decouple import config


class Config:
    APP_NAME = 'myapp'
    # SECRET_KEY = config('SECRET_KEY')

    STATIC_PREFIX_PATH = 'static'
    ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'gif']
    MAX_IMAGE_SIZE = 5242880  # 5MB


class LocalConfig(Config):
    DEBUG = True
    TESTING = True

    GCP_VM_ENDPOINT = None
    DATABASE_ENDPOINT = config('DATABASE_ENDPOINT_LOCAL')


class DevelopmentConfig(Config):
    DEBUG = False

    GCP_VM_ENDPOINT = config('GCP_VM_ENDPOINT_DEV')
    DATABASE_ENDPOINT = config('DATABASE_ENDPOINT_DEV')
