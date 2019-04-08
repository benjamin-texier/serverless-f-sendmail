import boto3

TO = ["{{ my-email }}"]
FROM = "{{ my-email }}"
SUBJECT = "[CONTACT] New message"

def send_mail(event, context):
    data = event['body']
    name = data ['name']
    source = data['email']
    message = data['message']

    _message = "Message from: " + name + "\nEmail: " + source + "\nMessage content: " + message    

    client = boto3.client('ses' )    
    client.send_email(
        Destination={
            'ToAddresses': TO
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': _message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': SUBJECT,
            },
        },
        Source=FROM,
    )
    return _message