from django.conf.urls import url
from users import views 
urlpatterns = [
    # url(r'^start/',ld),
    url(r'^$',views.home),
    url(r'^regload/$',views.register),
    url(r'^logload/$',views.login),
    url(r'^order/$',views.order),
    url(r'^logout/$',views.logout),
    url(r'^mkorder/$',views.mkorder),
    url(r'^my_order/$',views.my_order),
    url(r'^finds/$',views.finds),
    url(r'^morder/$',views.morder),
    url(r'^search/$',views.search),
    url(r'^pending/$',views.pending),
    url(r'^total/$',views.total),
    url(r'^Ordered/$',views.Ordered),

    # url(r'^signup/(?P<num>[0-3]+)/$',views.signup),
    # url(r'^signin/$',views.signin),
    # url(r'^emp_home/$',views.emp_home),
    # url(r'^changepassword/$',views.changepassword),
    # url(r'^brwsjob/$',views.brwsjob), url(r'^mngjbs/$',views.mngjbs),url(r'^msgs/$',views.msgs),url(r'^dashboard/$',views.dashboard),
    # url(r'^logout/$',views.logout),
    # url(r'^addresumehead/$', views.addresumehead),url(r'^addfrfsum/$', views.addfrfsum),url(r'^addcareer/$', views.addcareer),
    # url(r'^addpersonaldetail/$', views.addpersonaldetail),url(r'^uploads/(?P<num>[0-3]+)/$', views.dbuploads),
    # url(r'^addemp/$', views.addemp),url(r'^sel/$', views.sel),url(r'^addskill/$', views.addskill),url(r'^addedu/$', views.addedu),
    # url(r'^addedu/$', views.addedu),url(r'^del_dtls/$', views.del_dtls)
]