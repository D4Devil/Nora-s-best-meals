class Config():
    #Flask config
    SECRET_KEY = 'This is insecure as hell, and should be a longer string'

    #flask_user config
    USER_APP_NAME = "Nora's best meals"
    USER_ENABLE_EMAIL = False
    USER_ENABLE_USERNAME = True
    USER_REQUIRE_RETYPE_PASSWORD = False
    USER_ENABLE_CONFIRM_EMAIL = False

    ##DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']

    #Mongo config
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost/noras-best-meals',
        'port': 27017,
        'connect': False
    }