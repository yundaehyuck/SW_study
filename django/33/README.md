#url은 필요없는것 같은데..
1. 
STATICFILES_DIRS=[
    BASE_DIR/'assets',
]

2.

MEDIA_ROOT = BASE_DIR/'uploaded_files'

MEDIA_URL = '/uploaded_files/'
