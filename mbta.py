from gtfs_realtime_pb2 import *
import numpy as np
import pandas as pd
from urllib2 import urlopen
import datetime
import os
import time
import glob

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

def get_veh_data():
	url = 'http://developer.mbta.com/lib/gtrtfs/Vehicles.pb'

	now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	fname = 'veh_%s.pb' % now
	with open(os.path.join('data', fname), 'wb') as fid:
		fid.write(urlopen(url).read())

def get_veh_data2():
	for ii in range(100):
		get_veh_data()
		time.sleep(20)

def parse_veh_pb(fname):
	fm = FeedMessage()
	with open(fname, 'rb') as fid:
		fm.ParseFromString(fid.read())

	trip_ids = []
	for en in fm.entity:
		out = AttrDict()

		veh = en.vehicle
		out.trip_id = veh.trip.trip_id
		out.lat = veh.position.latitude
		out.lng = veh.position.longitude
		out.curr_stop_seq = veh.current_stop_sequence
		out.curr_stop = veh.stop_id
		out.status = veh.current_status
		out.time = veh.timestamp
		trip_ids.append(out)

	return pd.DataFrame.from_records(trip_ids)

def parse_all():
	df = pd.DataFrame()
	for fname in glob.glob(os.path.join('data', '*.pb')):
		df = pd.concat([df, parse_veh_pb(fname)])
	
	return df

def dave():
	fm = FeedMessage()
	with open('Vehicles.pb', 'rb') as fid:
		fm.ParseFromString(fid.read())
	trip_ids = []
	for en in fm.entity:
		try:
			veh = en.vehicle

			out = AttrDict()
			
			out.trip_id = veh.trip.trip_id
			out.lat = veh.position.latitude
			out.lng = veh.position.longitude
			out.curr_stop_seq = veh.current_stop_sequence
			out.curr_stop = veh.stop_id
			out.status = veh.current_status
			out.time = veh.timestamp
			# STOP
			# trip_id = int(en.vehicle.trip.trip_id)
			# route_id = int(en.vehicle.trip.route_id)
			trip_ids.append(out)

			# print int(en.vehicle.trip.trip_id)
			# print en.vehicle.trip.route_id



		except:
			STOP
			pass

	# trip_ids = np.array(trip_ids)

	return pd.DataFrame.from_records(trip_ids)