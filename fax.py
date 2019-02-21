from twilio.rest import Client


def fax_reps():

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    fax = client.fax.faxes \
        .create(
             from_='+15618011480',
             to='+18665192390',
             media_url='https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf'
         )

    print(fax.sid)
