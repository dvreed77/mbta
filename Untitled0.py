import pandas as pd
import numpy as np
from mbta import *

# Get supporting info
trips = pd.read_csv('MBTA_GTFS/trips.txt')
stops = pd.read_csv('MBTA_GTFS/stops.txt')
routes = pd.read_csv('MBTA_GTFS/routes.txt')
stop_times = pd.read_csv('MBTA_GTFS/stop_times.txt')
shape = pd.read_csv('MBTA_GTFS/shapes.txt')

grp_rt = trips.groupby('route_id')

trips.trip_headsign = trips.trip_headsign.fillna("")
trips.block_id = trips.block_id.fillna("")
trips.shape_id = trips.shape_id.fillna("")

def shapes_tojson():
    for name, group in shape.groupby('shape_id'):
        
        STOP
# # Lets concentrate on route 01
# trips_rt01 = trips[trips.route_id == "01"].trip_id

# grouped = stop_times.groupby('trip_id')
# start_times = grouped.first().arrival_time

# # get all trip_ids currently active
# all_curr_trip_ids = [x.trip_id for x in dave()]
# curr_trips_ids_rt01 = intersect1d(all_curr_trip_ids, trips_rt01.apply(str))

# trips[trips.trip_id.isin(curr_trips_ids_rt01.astype(str))]

# buses_rt1 = filter(lambda x: len(x.trip_id) and (int(x.trip_id) in curr_trips_ids_rt01), out)
# buses_rt1



# bus_tmp = buses_rt1[2]
# print bus_tmp
# print datetime.datetime.fromtimestamp(bus_tmp.time)


# sid = stop_times[(stop_times.trip_id == 20251824) & (stop_times.stop_sequence == 8)].stop_id
# stops[stops.stop_id == str(sid.iloc[0])]

def find_trip(trip_string):
    mask = trips.trip_headsign.str.contains(trip_string)
    return trips[mask]

def plot_bus(bus_info):
    trip_id = bus_info.trip_id
#     print datetime.datetime.fromtimestamp(bus_tmp.time)
    sids = stop_times[stop_times.trip_id == int(trip_id)]
    sids1 = stops[stops.stop_id.isin(sids.stop_id.apply(str))]
    sid = sids[sids.stop_sequence == bus_info.curr_stop_seq]
#     print sids1
#     print sid.arrival_time
#     print bus_info.curr_stop_seq
#     print bus_info.curr_stop
    
    stmp = stops[stops.stop_id == str(sid.stop_id.iloc[0])]
#     print stmp
    plot(sids1.stop_lon, sids1.stop_lat, '.')
    plot(bus_info.lng, bus_info.lat, '.', ms=10, color='r')
    plot(stmp.stop_lon, stmp.stop_lat, '.', ms=10, color='g')


# In[115]:

def how_late(bus_info):
    trip_id = bus_info.trip_id
    bt = datetime.datetime.fromtimestamp(bus_tmp.time)
    # sids = stop_times[stop_times.trip_id == int(trip_id)]
    sids = stop_times.groupby('trip_id').groups[trip_id]
    sid = sids[sids.stop_sequence == bus_info.curr_stop_seq]
#     sids1 = stop_times[stop_times.stop_id.isin(sids.stop_id.apply(str))]
    
    at = sid.arrival_time.iloc[0]
    hour, minute, second = at.strip().split(':')
#     print at
    
    a = datetime.datetime(bt.year, bt.month, bt.day, int(hour), int(minute), int(second))
    
    print "The bus is late by: %s" % str(bt - a)
    return bt, a
    
#     print sids1
#     print sid.arrival_time
#     print bus_info.curr_stop_seq
#     print bus_info.curr_stop


# In[122]:

# how_late(buses_rt1[6])