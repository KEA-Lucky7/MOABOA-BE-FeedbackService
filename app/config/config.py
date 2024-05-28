from decouple import config


class Config:
    APP_NAME = 'myapp'
    SECRET_KEY = config('SECRET_KEY')

    AWS_DEFAULT_REGION = 'ap-northeast-2'

    STATIC_PREFIX_PATH = 'static'
    ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'gif']
    MAX_IMAGE_SIZE = 5242880  # 5MB


class LocalConfig(Config):
    DEBUG = True
    TESTING = True

    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID_TEST')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY_TEST')
    AWS_S3_BUCKET_NAME = config('AWS_S3_BUCKET_NAME_TEST')
    DATABASE_URI = config('DATABASE_URI_TEST')


class DevelopmentConfig(Config):
    DEBUG = False

    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID_PROD')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY_PROD')
    AWS_S3_BUCKET_NAME = config('AWS_S3_BUCKET_NAME_PROD')
    DATABASE_URI = config('DATABASE_URI_PROD')
