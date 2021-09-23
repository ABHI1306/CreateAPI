from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
from django.core.serializers import serialize

from .mixins import CSRFExemptMixin
import json
from cfeapi.mixins import HttpResponseMixin
from updates.forms import UpdateModelForm

from .utils import is_json

class UpdateModelDetailAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    is_json = True

    def get_object(self,id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self,request,id,*args,**kwrgs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self,request,*args,**kwrgs):
        json_data = json.dumps({"message":"Not allowed, please use the /api/updates/ endpoint."})
        return self.render_to_response(json_data,status=403)

    def put(self,request,id,*args,**kwrgs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"Invalid data sent, please send using JSON."})
            return self.render_to_response(error_data,status=400)       
        
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        new_data = {}
        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        for key,value in passed_data.items():
            data[key] = value
        form = UpdateModelForm(data, instance=obj)
        if(form.is_valid()):
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data,status=201)
        data = json.loads(request.body)
        if(form.errors):
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)
        
        json_data = json.dumps({"message":"Something..."})
        return self.render_to_response(json_data)

    def delete(self,request,id,*args,**kwrgs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message":"Update not found"})
            return self.render_to_response(error_data,status=404)
        deleted_, item_deleted = obj.delete()
        if deleted_ == 1:
            json_data = json.dumps({"message":"Successfully deleted..."})
            return self.render_to_response(json_data,status=200)
        error_data = json.dumps({"message":"Could not delete item. Please try again later."})
        return self.render_to_response(error_data,status=400)

class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):
    is_json = True
    
    def get(self,request,*args,**kwrgs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)
 
    def post(self,request,*args,**kwrgs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"Invalid data sent, please send using JSON."})
            return self.render_to_response(error_data,status=400)       
        data = json.loads(request.body)
        form = UpdateModelForm(data)
        if(form.is_valid()):
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data,status=201)
        data = json.loads(request.body)
        if(form.errors):
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)
        data = {"message":"Not Allowed"}
        return self.render_to_response(data,status=400)

    def delete(self,request,*args,**kwrgs):
        data = json.dumps({"message":"You cannot delete an entire list."})
        status_code = 403
        return self.render_to_response(data,status=status_code)

