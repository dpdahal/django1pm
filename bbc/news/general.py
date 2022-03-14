from .models import CompanySetting


def data_pass(request):
    data = {
        'companyData': CompanySetting.objects.first()
    }

    return data
