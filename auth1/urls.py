from rest_framework.routers import DefaultRouter
from auth1 import views

router=DefaultRouter()
router.register(r'Account', views.AccountViewSet, basename='AccountViewSet')
#router.register(r'search-food', views.SearchFoodViewSet, base_name='SearchFoodViewSet')
#router.register(r'v2/search-food', views.NewSearchFoodViewSet, base_name='NewSearchFoodViewSet')
#router.register(r'get-food', views.SingleFoodViewSet, base_name='SingleFoodViewSet')
#router.register(r'contact-us', views.ContactUsViewSet, base_name='ContactUsViewSet')
#router.register(r'beta-test-form', views.BetaTestingUserViewSet, base_name='BetaTestingUserViewSet')

urlpatterns = router.urls