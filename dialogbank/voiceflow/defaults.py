API_BASE_URL = 'https://general-runtime.voiceflow.com'
VERSION_ID = 'production'
DEFAULT_INTERACT_CONFIG = {
    'tts': False,
    'stripSSML': True,
    'stopAll': True,
    'stopTypes': [],
    'excludeTypes': [
        'block',
        'debug',
        'flow',
    ]
}
