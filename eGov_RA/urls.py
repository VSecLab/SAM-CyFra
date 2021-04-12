"""eGov_RA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from parsingbpmn.views import bpmn_process_management, system_management, \
    delete_process, delete_system, process_enrichment, threat_modeling, process_view_task_type, process_view_attribute, \
    task_type_enrichment, export_threat_modeling, threats_and_controls, bpmn_viewer, edit_process, context_management, \
    profile_management, fusion_perform, fusion_profile_perform, controls_missing, profile_roadmap, delete_profile, \
    delete_context, create_context, save_contextualization, create_profile, save_profile, profile_controls, save_profile_controls, \
    down_context_sample, read_context_file, generate_profile,profile_evaluation, profile_missing, export_context, export_profile, \
    export_roadmap, implemented_controls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', system_management, name='system_management'),
    path('bpmn_process_management/<int:pk>', bpmn_process_management, name='bpmn_process_management'),
    path('process_view_task_type/<int:pk>', process_view_task_type, name='process_view_task_type'),
    path('process_view_attribute/<int:pk>', process_view_attribute, name='process_view_attribute'),
    path('edit_process/<int:pk>', edit_process, name='edit_process'),
    path('delete_process/<int:pk>', delete_process, name='delete_process'),
    path('delete_system/<int:pk>', delete_system, name='delete_system'),
    path('process_enrichment/<int:pk>', process_enrichment, name='process_enrichment'),
    path('bpmn_viewer/<int:pk>', bpmn_viewer, name='bpmn_viewer'),
    path('task_type_enrichment/<int:pk>', task_type_enrichment, name='task_type_enrichment'),
    path('threats_and_controls/<int:pk>', threats_and_controls, name='threats_and_controls'),
    path('threat_modeling/<int:pk>', threat_modeling, name='threat_modeling'),
    path('export_threat_modeling/<int:pk>', export_threat_modeling, name='export_threat_modeling'),
    path('context_management', context_management, name = 'context_management'),
    path('profile_management/<int:pk>', profile_management, name='profile_management'),
    path('fusion_perform', fusion_perform, name='fusion_perform'),
    path('fusion_profile_perform', fusion_profile_perform, name='fusion_profile_perform'),
    path('controls_missing', controls_missing, name='controls_missing'),
    path('profile_roadmap/<int:pk>', profile_roadmap, name='profile_roadmap'),
    path('delete_profile/<int:pk>', delete_profile, name='delete_profile'),
    path('delete_context/<int:pk>', delete_context, name='delete_context'),
    path('create_context', create_context, name='create_context'),
    path('save_contextualization', save_contextualization, name='save_contextualization'),
    path('create_profile/<int:pk>', create_profile, name='create_profile'),
    path('save_profile/<int:pk>', save_profile, name='save_profile'),
    path('profile_controls/<int:pk>', profile_controls, name='profile_controls'),
    path('save_profile_controls/<int:pk>', save_profile_controls, name='save_profile_controls'),
    path('down_context_sample', down_context_sample, name='down_context_sample'),
    path('read_context_file', read_context_file, name='read_context_file'),
    path('generate_profile/<int:pk>', generate_profile, name='generate_profile'),
    path('profile_evaluation/<int:pk>', profile_evaluation, name='profile_evaluation'),
    path('profile_missing/<int:pk>', profile_missing, name='profile_missing'),
    path('export_context/<int:pk>', export_context, name='export_context'),
    path('export_profile/<int:pk>', export_profile, name='export_profile'),
    path('export_roadmap/<int:pk>', export_roadmap, name='export_roadmap'),
    path('implemented_controls', implemented_controls, name='implemented_controls'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)