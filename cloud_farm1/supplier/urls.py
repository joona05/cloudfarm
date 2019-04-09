from django.conf.urls import url
from supplier import views 

urlpatterns = [
    # url(r'^start/',ld),
    url(r'^$',views.home),

    url(r'^regload/$',views.supplier_register),
    url(r'^logload/$',views.login),
    url(r'^add/$',views.add),
    url(r'^logout/$',views.logout),
    url(r'^product/$',views.product),
    # url(r'^addpho/$',views.addpho),
    url(r'^update/$',views.update),
    url(r'^edit/$',views.edit),
    url(r'^search/$',views.search),
    url(r'^Orderlist/$',views.Orderlist),
    url(r'^approve/$',views.approve),
    url(r'^Orderedlist/$',views.Orderedlist),


    




    ]