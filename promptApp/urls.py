from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from promptApp.api.views.promptApiView import PromptView
from promptApp.api.views.userApiView import UserView

# para Swagger
from rest_framework.schemas import get_schema_view

# Routing
router = routers.DefaultRouter()
router.register(r'prompts', PromptView)
router.register(r'users', UserView)

swaggerUi_schema = get_schema_view(
    title='SwaggerUi ApiPrompts',
    description='Guide for the API Prompts',
    version='v1.0.0',
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # End Point para construir el schema de configuracion del Swagger
    path('schema/', swaggerUi_schema, name="schema-apiPrompts"),

    # End Point para visitar la Documentacion de la Api
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'schema-apiPrompts'}
    ), name='swagger-ui'),
]
