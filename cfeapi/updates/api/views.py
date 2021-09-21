from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
from django.core.serializers import serialize

from .mixins import CSRFExemptMixin
import json
from cfeapi.mixins import HttpResponseMixin

class UpdateModelDetailAPIView(CSRFExemptMixin,View):
    is_json = True
    def get(self,request,id,*args,**kwrgs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self,request,*args,**kwrgs):
        json_data = {}
        return self.render_to_response(json_data)

    def put(self,request,*args,**kwrgs):
        json_data = {}
        return self.render_to_response(json_data)

    def delete(self,request,*args,**kwrgs):
        json_data = {}
        return self.render_to_response(json_data,status=403)

class UpdateModelListAPIView(CSRFExemptMixin,View):
    is_json = True
    def get(self,request,*args,**kwrgs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)
 
    def post(self,request,*args,**kwrgs):
        data = json.dumps({"message":"Unknown data"})
        return self.render_to_response(data,status=400)

    def delete(self,request,*args,**kwrgs):
        data = json.dumps({"message":"You can not delete list"})
        status_code = 403
        return HttpResponse(data,status=status_code)

