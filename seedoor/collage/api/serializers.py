from rest_framework import serializers
from collage.models import Student
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
#from books.models import Book
#from books.apibooks.serializers import BookSerializer

class StudentUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student
		fields = ('pk','reg_number', 'ein_1', 'ein_2', 'ein_3', 'nid', 'amount')

class StudentSerializer(serializers.ModelSerializer):
	#personalinfo = BookSerializer(many=True)
	class Meta:
		model = Student
		fields = ('pk','reg_number', 'ein_1', 'ein_2', 'ein_3', 'nid', 'amount')

class  StudentCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('reg_number', 'ein_1', 'ein_2', 'ein_3', 'nid', 'amount')

	def save(self):
		try:
			reg_number      = self.validated_data['reg_number']
			ein_1        	= self.validated_data['ein_1']
			ein_2           = self.validated_data['ein_2']
			ein_3           = self.validated_data['ein_3']
			nid             = self.validated_data['nid']
			amount          = self.validated_data['amount']
	
			collage = Student(
								reg_number=reg_number,
								ein_1=ein_1,
								ein_2=ein_2,
								ein_3=ein_3,
								nid=nid,
								amount=amount
								)
			collage.save()
			return collage
		except KeyError:
			raise serializers.ValidationError({"response": "this invalid somethings!!!!!"})