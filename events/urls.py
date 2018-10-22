from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (Login, Logout, Signup,
 home, dashboard, create_event, event_detail,
 events_list, event_update, event_book)

urlpatterns = [
	path('', home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('event/list/', events_list, name='events-list'),
    path('event/detail/<int:event_id>/', event_detail, name='event-detail'),
    path('event/create', create_event, name='create-event'),
    path('event/update/<int:event_id>/', event_update, name='event-update'),
    path('event/book/<int:event_id>/', event_book, name='event-book'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)