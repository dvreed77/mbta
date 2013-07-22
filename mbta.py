from gtfs_realtime_pb2 import *


def dave():
	fm = FeedMessage()
	fm.ParseFromString(open('Vehicles.pb', 'rb').read())
	for en in fm.entity:
		try:
			print int(en.vehicle.trip.trip_id)
		except:
			pass
