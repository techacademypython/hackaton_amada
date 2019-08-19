from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import JsonResponse

def cordinates(request):
    my_model = Device.objects.filter(id=1).last()
    temp = my_model.get_cordinates()

    temp = temp.split(",")
    newtemp = []
    for i in temp :
        newtemp.append(float(i))

    print(newtemp)
    return JsonResponse({
                  "coordinates": newtemp})

def notfication(request):
    my_notf = Notfication.objects.filter(device__id=1).last()


    return  JsonResponse({
        "status": True,
        "notication": my_notf.notfication()
    })

def index(request):
    context = {}
    # context["marker"] = Fuel_of_Device.objects.all()
    data = Device.objects.all()
    notfication = Notfication.objects.all().order_by("-id")[:5]
    # ''' device locakitino''''
    result = []
    col = []
    notf = []
    order = 0

    for item in data:
        order = order + 1

        try:
            if item.humudity < 25:
                color = "bg-success"
            elif item.humudity < 51:
                color = "yellow"
            elif item.humudity < 75:
                color = "orange"
            else:
                color = "bg-danger"

            print(data)
            # new_data = Fuel_of_Device.objects.get(
            #     device_imei__device_imei=item.device_imei)
            result.append({
                "device_id": item.imei,
                "coords": {"lat": item.device_lat, "lng": item.device_long},
                "device_icon": item.new_info(),
            })
            col.append({
                "text": "{} {} {} {} {} {}".format(order, item.imei or int(0), item.tempureture or int(0),
                                    item.humudity or int(0), float(item.pressure)/100 or int(0), item.time_s or int(0)).split(),
                "battery": color,

            })


        except Exception as err:
            print(err)
    for i in notfication:
        order = order + 1

        notf.append({
                "notfication": "{}  {} {}".format(i.id, i.device.imei or int(0), i.time_s or int(0)).split(),
                "not" : i.notification_type,
                "user": i.by_who
            })

    print(col)
    # print(result)
    print(notf)
    context["object_list"] = result
    context["info"] = col
    context["notf"] = notf
    # context["user"] =

    return render(request, "index.html", context)