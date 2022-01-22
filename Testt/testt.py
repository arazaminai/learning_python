from validate_email import validate_email
import requests as req

def authenticate():
    resp = req.get("https://rentry.co/pk2h5/raw")
    emails = resp.text.split("\n")
    emails = "kingminai@gmail.com"

    for i in emails:
        is_valid = validate_email(
            email_address=i,
            check_format=True,
            check_blacklist=True,
            check_dns=True,
            dns_timeout=10,
            check_smtp=True,
            smtp_timeout=10,
            smtp_helo_host='my.host.name',
            smtp_from_address='my@from.addr.ess',
            smtp_skip_tls=False,
            smtp_tls_context=None,
            smtp_debug=False
            )

        print(i)

        if is_valid:
            print("Yes\n")
        else:
            print("Invalid Details")

authenticate()