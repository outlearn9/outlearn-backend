from django.conf.urls import url 
#from OutLearnApi import views 
from .views import specialisationViews
from .views import higherstudyViews
from .views  import userViews
 
urlpatterns = [ 
    url(r'^api/v1/specialisation$', specialisationViews.specialisation_list),
    url(r'^api/v1/category$',specialisationViews.category_list),
    url(r'^api/v1/getSpecialisation$',specialisationViews.get_specialisation),
    url(r'^api/v1/getHigherStudy$',higherstudyViews.higher_study_master),
    url(r'^api/v1/saveVisitorInfo$',userViews.save_visitor_info),
    url(r'^api/v1/user$',userViews.save_user),
    url(r'^api/v1/sendOtp$',userViews.send_otp),
    url(r'^api/v1/verifyOtp$',userViews.verify_otp),
    url(r'^api/v1*',specialisationViews.specialisation_list),
 
]