from django.conf import settings
import requests


class PayStack:
    PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
    base_url = "https://api.paystack.co"

    def verify_payment(self, ref, *args, **kwargs):
        path = f'/transaction/verify/{ref}'

        headers = {
            'Authorization': r'Bearer {}'.format(self.PAYSTACK_SECRET_KEY),
            'Content-Type': 'application/json',
        }
        url = self.base_url + path
        response = requests.get(url=url, headers=headers)
        response_data = response.json()
        if response.status_code == 200:
            return response_data['status'], response_data['data']
        return response_data['status'], response_data['message']

