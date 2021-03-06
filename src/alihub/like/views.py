
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType



from rest_framework import views
from rest_framework.permissions import IsAuthenticated



from post.models import Post
from .serializers import LikeSerializer
from .models import Like




class LikeAPIView(views.APIView):
	lookup_field      =  'id'
	
	permission_classes = (IsAuthenticated)


	def get(self, *args, **kwargs):
		user     	 = self.request.user
		obj      	 = get_object_or_404(Like)

		target   	 = ContentType.objects.get_for_model(Story)
		object_id 	 = target.id
		liked  		= obj.liked
		if user.is_authenticated():
			if liked  == True:
				obj.likes_count =+ 1
			else:
				obj.likes_count = -1
		data = LikeSerializer(many = True).data
		return Response(data)
	




		









