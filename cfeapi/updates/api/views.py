from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
from django.core.serializers import serialize

from .mixins import CSRFExemptMixin
import json
from cfeapi.mixins import HttpResponseMixin
from updates.forms import UpdateModelForm

class UpdateModelDetailAPIView(HttpResponseMixin,CSRFExemptMixin,View):
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

class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    is_json = True
    
    def get(self,request,*args,**kwrgs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)
 
    def post(self,request,*args,**kwrgs):
        form = UpdateModelForm(request.POST)
        if(form.is_valid()):
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data,status=201)
        if(form.errors):
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)
        data = {"message":"Not Allowed"}
        return self.render_to_response(data,status=400)

    def delete(self,request,*args,**kwrgs):
        data = json.dumps({"message":"You can not delete list"})
        status_code = 403
        return self.render_to_response(data,status=status_code)

