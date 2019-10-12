# Imports the Google Cloud client library
from google.cloud import translate

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    content_type = request.headers['content-type']
    print('content_type: {}'.format(content_type))

    request_json = request.get_json(silent=True)
    print('request_json: {}'.format(request_json))
    
    #if request.args and 'message' in request.args:
    #    return request.args.get('message')
    #elif request_json and 'message' in request_json:
    #    return request_json['message']
    #else:
    #    return f'Hello World!'

    # Instantiates a client
    translate_client = translate.Client()
    # The text to translate
    text = u'Hello, world!'
    # The target language
    target = 'es'
    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)
    print(u'Text: {}'.format(text))
    return u'Translation: {}'.format(translation['translatedText'])
