
from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from .models import Productmodel,Calendarmodel
from .serializers import MyModelSerializer,ModelSerializer
from django.db.models import Sum
import datetime


class ProductViews(APIView):
    def get(self,request):
        product = Productmodel.objects.all()
        serializer = MyModelSerializer(product,many=True)
        return Response({"message":"Success","data":serializer.data})
    
    def post(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product created successfully", "data": serializer.data})
        return Response(serializer.errors, status=400)


class SalesProduct(APIView):
    def get(self, request):
        # Retrieve the data from the model
        queryset = Productmodel.objects.all()
        data_count = queryset.count()
        
        # Calculate the sum of the 'price' column
        price_sum = Productmodel.objects.aggregate(total_price=Sum('amountpaid'))['total_price']
        print(price_sum)
        
        return Response({'sum': price_sum,'count':data_count})

class SalesMonthProduct(APIView):
    def get(self, request):
       
        # Retrieve the data from the model
        
       current_month = datetime.datetime.now().month

        # Retrieve all objects from the model
       queryset = Productmodel.objects.all()

        # Filter the objects for the current month
       filtered_objects = [
            obj for obj in queryset if datetime.datetime.strptime(obj.date, '%d-%m-%Y').month == current_month
        ]

        # Calculate the sum of the 'amountpaid' field for the filtered objects
       price_sum = sum(float(obj.amountpaid) for obj in filtered_objects)
       return Response({'sum': price_sum,'month':current_month})



#artifice division  
class ShareDivision(APIView):
    def get(self,request):
        shipping = int(request.query_params.get('search'))
        print(shipping,type(shipping))
        
        current_month = datetime.datetime.now().month

        # Retrieve all objects from the model
        queryset = Productmodel.objects.all()

        # Filter the objects for the current month
        filtered_objects = [
            obj for obj in queryset if datetime.datetime.strptime(obj.date, '%d-%m-%Y').month == current_month
        ]

        # Calculate the sum of the 'amountpaid' field for the filtered objects
        price_sum = sum(float(obj.amountpaid) for obj in filtered_objects)
        if(shipping):
            net = price_sum-shipping
            kashish = net*0.4
            gautam = net*0.3
            artifice = net*0.3
        else:
            shipping = 0
            net = price_sum-shipping
            kashish = net*0.4
            gautam = net*0.3
            artifice = net*0.3
        return Response([{"id": "Kashish","label": kashish,"value": 40,"color": "hsl(104, 70%, 50%)"},{"id":"Gautam" ,"label": gautam,"value": 30,"color": "hsl(162, 70%, 50%)"},{"id": "Artifice","label":artifice,"value": 30,"color": "hsl(291, 70%, 50%)"}])


class CalendarData(APIView):
    def post(self,request):
        serializer = ModelSerializer(data=request.data)
        print(request.data,'pppppp')
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Event created successfully", "data": serializer.data})
        return Response(serializer.errors, status=400)
    
    def get(self,request):
        product = Calendarmodel.objects.all()
        serializer = ModelSerializer(product,many=True)
        return Response({"message":"Success","data":serializer.data})
    
    
    def delete(self,request):
        event_id = request.data.get('id')
        print(event)
        try:
            # Retrieve the event from the database
            event = Calendarmodel.objects.get(id=event_id)
        except Calendarmodel.DoesNotExist:
            return Response({"message": "Event not found"}, status=404)
        
        # Delete the event
        event.delete()
        
        return Response({"message": "Event deleted successfully"})
    

class DeleteOrder(APIView):
    def get_object(self, pk):
        try:
            return Calendarmodel.objects.get(pk=pk)
        except Calendarmodel.DoesNotExist:
            raise Response({"message":"error"})


    def delete(self,request,pk):
        try:
            obj = self.get_object(pk=pk)
            obj.delete()
            return Response({"message":"user deleted"})
        except:
            return Response({"message":"server error"})  


    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = ModelSerializer(obj, data=request.data)
        print(request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            print(title)
            obj.title = title  # Update the title of the event
            obj.save()  # Save the updated event object
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
