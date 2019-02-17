from twilio.rest import Client


def fax_reps():

    account_sid = 'AC03acac4bff7bd871e3b64549e63232e0'
    auth_token = 'f7ec33e94f42b6168ce17f0266f5c44a'
    client = Client(account_sid, auth_token)

    fax = client.fax.faxes \
        .create(
             from_='+15618011480',
             to='+18665192390',
             media_url='https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf'
         )

    print(fax.sid)
