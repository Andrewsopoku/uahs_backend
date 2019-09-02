from core.core_util import calc_dist
from core.models.ambulance import Ambulance
from core.models.ambulance_service import AmbulanceService
from core.models.base_model import BaseModel
from django.db import models



class AmbulanceLocation(BaseModel):
   ambulance = models.OneToOneField(Ambulance,on_delete=models.CASCADE, blank=True,null=True)
   status = models.CharField(max_length=255, null=True,default="Available")
   long = models.CharField(max_length=255, null=True)
   lat = models.CharField(max_length=255, null=True)


   @classmethod
   def create_or_edit(cls,ambulance,lat,long):
       location = cls.objects.filter(ambulance=ambulance)
       if location:
           location[0].lat =lat
           location[0].long = long
           location[0].save()
       else:
           loc = cls(ambulance=ambulance,lat=lat,long=long)
           loc.save()
       return True

   @classmethod
   def get_closest_ambulance(cls,lat_a,long_a):
       locs = cls.objects.filter(status="Available")
       print(locs)
       ambulance_location = None
       distance = 20000000000
       for loc in locs:
           point_distance = calc_dist(eval(lat_a), eval(long_a), eval(loc.lat), eval(loc.long))
           if point_distance < distance :
               ambulance_location = loc
               distance = point_distance

       print(ambulance_location)
       return ambulance_location

