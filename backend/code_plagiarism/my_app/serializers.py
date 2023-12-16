# Serializers are used to convert complex data types, such as Django models, into native Python data types that can be easily rendered into JSON.
from rest_framework import serializers
from .my_app.models import CodeSubmission


class CodeSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSubmission
        fields = '__all__'
