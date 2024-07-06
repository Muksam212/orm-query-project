from django.urls import path
from api.views import (
    CompanyList,
    CompanyDetails,
    LanguageList,
    LanguageDetails,
    ProgrammerList,
    ProgrammerDetails
)

urlpatterns = [
    path('api/company/list/', CompanyList.as_view(), name='api-company-list'),
    path('api/company/details/<int:id>/', CompanyDetails.as_view(), name='api-company-details'),

    path('api/language/list/', LanguageList.as_view(), name='api-language-list'),
    path('api/language/details/<int:id>/', LanguageDetails.as_view(), name='api-language-details'),

    path('api/programmer/list/', ProgrammerList.as_view(), name='api-programmer-list'),
    path('api/programmer/details/<int:id>/', ProgrammerDetails.as_view(), name='api-programmer-details')
]
