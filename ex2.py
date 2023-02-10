from math import cos, sin, tan, atan2, pi, acos

path =[[137.788742,1632.470703],[137.732239,1633.003662],[137.67514,1633.465576],[137.604904,1633.99585],[137.539551,1634.467163],[137.467392,1634.971191],[137.393951,1635.471313],[137.320557,1635.960693],[137.243561,1636.4646],[137.166565,1636.959473],[137.088623,1637.453125],[137.008896,1637.950073],[136.92778,1638.447754],[136.845886,1638.943237],[136.763535,1639.433105],[136.677719,1639.935303],[136.5914,1640.430908],[136.506241,1640.909912],[136.41272,1641.423828],[136.321671,1641.909668],[136.224869,1642.407349],[136.12381,1642.900635],[136.01265,1643.400269],[135.899597,1643.830933],[135.75795,1644.28772],[135.604584,1644.76416],[135.446747,1645.246582],[135.286514,1645.730957],[135.13179,1646.195068],[134.966431,1646.687988],[134.808105,1647.157349],[134.648666,1647.627563],[134.484207,1648.11084],[134.321732,1648.58606],[134.159836,1649.057495],[133.99588,1649.532959],[133.830811,1650.009766],[133.665344,1650.485596],[133.500275,1650.957764],[133.336243,1651.424927],[133.164886,1651.909912],[132.996887,1652.382446],[132.833206,1652.839478],[132.655334,1653.332031],[132.483994,1653.80127],[132.31514,1654.257568],[132.128403,1654.752808],[131.962097,1655.18103],[131.755295,1655.684326],[131.584869,1656.042114]]
car_len = 2 #[2m]
car_position_x = 134  
car_position_y = 1649.057495
car_vel = 10     #[m/s]
heading = 60*180/pi   #[rad]
Lfd_min = 5
Lfd_max = 30

print("자동차의 전후방 차축 길이[m] : ",car_len)
print("차량의 현재 위치 x = {}, y = {}".format(car_position_x,car_position_y))
print("차량의 현재 속도[m/s] : ", car_vel)
print("차량의 현재 heading 각도[rad] : ",heading)
print("path에 속한 Waypoint 개수 : ",len(path))
print("Look-ahead-distance Max = {}, Min = {}".format(Lfd_max,Lfd_min))