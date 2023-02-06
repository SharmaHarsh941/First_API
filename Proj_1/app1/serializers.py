# import serializer from rest_framework
from rest_framework import serializers

# create a serializer
class SimpleSerializer(serializers.Serializer):
	# initialize fields

	name = serializers.CharField(max_length = 200)
	city = serializers.CharField(max_length = 200)
