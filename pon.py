#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:35:59 2020
@author: ponaravind
"""
from datetime import datetime 
import requests
import numpy as np

class Patient:
    def __init__(self, name, gender, age, email, origin, time_for_patient):
        self.name = name
        self.gender = gender
        self.age = age
        self.email = email
        self.origin = origin
        self.time_for_patient = time_for_patient
            
    def description(self):
        return "\nPATIENT INFO""\nname: {} \ngender: {} \nage: {} \nemail: {} \naddress: {} \ntime_for_patient: {}".format(self.name, self.gender, self.age, self.email, self.origin, self.time_for_patient)
    
    def get_lat_lng_for_patient(apiKey, origin):
        url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
                .format(origin.replace(' ','+'), apiKey))
        response = requests.get(url)
        resp_json_payload = response.json()
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
        return lat, lng
        print('\n{} Coordinates:\nLatitude:  {}°\nLongitude: {}°'.format(origin,lat, lng))
        
# def schedule(self, patient_name, patient_slot):
#             doctors_slot = set(aravind_slot) & set(swapna_slot) 
#             if set(patient_slot) & set(doctors_slot) is True:
#                 if patient_name == harshitha:
#                    driving_time_harshitha = min(drive_time_harshitha[1], drive_time_harshitha[2])
#                    print("Appointment is fixed at {} with {}" .format(patient_slot, driving_time_harshitha))
#                 elif patient_name == adithya:
#                     driving_time_adithya = min(drive_time_adithya[1], drive_time_adithya[2])
#                     print("Appointment is fixed at {} with {}" .format(patient_slot, driving_time_adithya))
#                 elif patient_name == tarun:
#                     driving_time_tarun = min(drive_time_tarun[1], drive_time_tarun[2]) 
#                     print("Appointment is fixed at {} with {}" .format(patient_slot, driving_time_tarun))            
#             elif set(patient_slot) & set(aravind_slot) is True:
#                 print("Appointment is fixed at {} with Dr.Aravind" .format(patient_slot))
#             elif set(patient_slot) & set(swapna_slot) is True:
#                 print("Appointment is fixed at {} with Dr.Swapna" .format(patient_slot))
#             else:
#                 print("Choose another time slot")
    
class Doctor:
    def __init__(self, name, specialty, destination, time_for_doctor):
        self.name = name
        self.specialty = specialty
        self.destination = destination
        self.time_for_doctor = time_for_doctor
            
    def description(self):
        return "\nDOCTOR INFO""\nname: {} \nspeacialty: {} \naddress: {} \ntime_for_doctor: {}".format(self.name, self.specialty, self.destination, self.time_for_doctor)

    def get_lat_lng_for_doctor(apiKey, destination):
        url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
                .format(destination.replace(' ','+'), apiKey))
        response = requests.get(url)
        resp_json_payload = response.json()
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
        return lat, lng
        print('\n{} Coordinates:\nLatitude:  {}°\nLongitude: {}°'.format(destination,lat, lng))

def get_drive_time(apiKey, origin, destination):
    import requests
    url = ('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'
           .format(origin.replace(' ','+'), destination.replace(' ','+'),apiKey))
    response = requests.get(url)
    resp_json_payload = response.json()
    drive_time = resp_json_payload['rows'][0]['elements'][0]['duration']['value']/60
    return drive_time

apiKey = 'AIzaSyCWRUNhSuFeF9wTgTjTY3YYwSV2Umd7NP4'

SLOT_1  = [datetime(2020, 3, 1, 8, 00)]
SLOT_2  = [datetime(2020, 3, 1, 8, 30)]
SLOT_3  = [datetime(2020, 3, 1, 9, 0)]
SLOT_4  = [datetime(2020, 3, 1, 9, 30)]
SLOT_5  = [datetime(2020, 3, 1, 10, 00)]
SLOT_6  = [datetime(2020, 3, 1, 10, 30)]
SLOT_7  = [datetime(2020, 3, 1, 11, 0)]
SLOT_8  = [datetime(2020, 3, 1, 11, 30)]
SLOT_9  = [datetime(2020, 3, 1, 13, 0)]
SLOT_10 = [datetime(2020, 3, 1, 13, 30)]
SLOT_11 = [datetime(2020, 3, 1, 14, 0)]
SLOT_12 = [datetime(2020, 3, 1, 14, 30)]
SLOT_13 = [datetime(2020, 3, 1, 15, 0)]
SLOT_14 = [datetime(2020, 3, 1, 15, 30)]
SLOT_15 = [datetime(2020, 3, 1, 16, 0)]
SLOT_16 = [datetime(2020, 3, 1, 16, 30)]

# harshitha _slot = [SLOT_2, SLOT_3, SLOT_4, SLOT_7, SLOT_8, SLOT_5, SLOT_6, SLOT_7, SLOT_8, SLOT_11]
# adithya_slot    = [SLOT_4, SLOT_7, SLOT_8, SLOT_14, SLOT_15, SLOT_16]
# tarun_slot      = [SLOT_1, SLOT_3, SLOT_4, SLOT_14, SLOT_15, SLOT_16]

aravind_slot = np.array([SLOT_2, SLOT_3, SLOT_4, SLOT_7, SLOT_8, SLOT_9, SLOT_10, SLOT_14, SLOT_15, SLOT_16])
# aravind_slot = aravind_slot [0]
swapna_slot  = np.array([SLOT_1, SLOT_3, SLOT_4, SLOT_5, SLOT_6, SLOT_7, SLOT_8, SLOT_11, SLOT_12, SLOT_13])
# swapna_slot  = swapna_slot[0]

harshitha   = Patient("harshitha", "female", "24", "email", "Mason, Cincinnati", datetime(2020, 3, 1, 13))
adithya     = Patient("tarun", "male", "24", "email", "Loveland, Cincinnati", datetime(2020, 3, 2, 11))
tarun       = Patient("tarun", "male", "24", "email", "3305 Jefferson Avenue, Cincinnati", datetime(2020, 3, 1, 13))         
swapna      = Doctor("swapna", "psychologist", "Blue ash, Cincinnati", datetime(2020, 3, 1, 11))
aravind     = Doctor("aravind", "ent", "Bawarchi, Sharonville, Cincinnati", datetime(2020, 3, 1, 13))
patient_names = [harshitha, adithya, tarun]
# print(tarun.description(), "\nPatient id is", id(tarun))
# print(adithya.description(), "\nPatient id is", id(adithya))
# print(harshitha.description(), "\nPatient id is", id(harshitha))
# print(aravind.description(), "\nDoctor id is", id(aravind))
# print(swapna.description(), "\nDoctor id is", id(swapna))

origin_harshitha    = harshitha.origin
origin_adithya      = adithya.origin
origin_tarun        = tarun.origin
destination_swapna  = swapna.destination
destination_aravind = aravind.destination

origin              = [origin_harshitha, origin_adithya, origin_tarun]
destination         = [destination_swapna, destination_aravind] 

# current_origin      = origin[2]
# current_destination = destination[0] 
# drive_time          = get_drive_time(apiKey, current_origin , current_destination)
# print('\nOrigin:      {}\nDestination: {}\nDrive Time:  {} hr'.format(current_origin, current_destination, drive_time/60))

drive_time_harshitha_swapna    = get_drive_time(apiKey, origin[0] , destination[0])
drive_time_harshitha_aravind   = get_drive_time(apiKey, origin[0] , destination[1])
drive_time_adithya_swapna      = get_drive_time(apiKey, origin[1] , destination[0])
drive_time_adithya_aravind     = get_drive_time(apiKey, origin[1] , destination[1])
drive_time_tarun_swapna        = get_drive_time(apiKey, origin[2] , destination[0])
drive_time_tarun_aravind       = get_drive_time(apiKey, origin[2] , destination[1])

drive_time_harshitha = dict([
     (1, drive_time_harshitha_swapna),
     (2, drive_time_harshitha_aravind),
])

min(drive_time_harshitha[1], drive_time_harshitha[2])

drive_time_adithya = dict([
     (1, drive_time_adithya_swapna),
     (2, drive_time_adithya_aravind),
])

min(drive_time_adithya[1], drive_time_adithya[2])

drive_time_tarun = dict([
     (1, drive_time_tarun_swapna),
     (2, drive_time_tarun_aravind), 
 ])

min(drive_time_tarun[1], drive_time_tarun[2])        
    
class scheduler:
        def __init__(self, patient_name, patient_slot):
            self.patient_name = patient_name
            self.patient_slot = patient_slot 
            
        def schedule(self):
            doctors_slot = set(aravind_slot.flatten()) & set(swapna_slot.flatten())
            if set(self.patient_slot) & set(doctors_slot) is True:
                if self.patient_name == harshitha:
                   driving_time_harshitha = min(drive_time_harshitha[1], drive_time_harshitha[2])
                   print("Appointment is fixed at {} with {}" .format(self.patient_slot, driving_time_harshitha))
                if self.patient_name == adithya:
                    driving_time_adithya = min(drive_time_adithya[1], drive_time_adithya[2])
                    print("Appointment is fixed at {} with {}" .format(self.patient_slot, driving_time_adithya))
                if self.patient_name == tarun:
                    driving_time_tarun = min(drive_time_tarun[1], drive_time_tarun[2]) 
                    print("Appointment is fixed at {} with {}" .format(self.patient_slot, driving_time_tarun))            

            if len(set(self.patient_slot) & set(aravind_slot.flatten())) > 0:
                print("Appointment is fixed at {} with Dr.Aravind" .format(self.patient_slot))    
            if len(set(self.patient_slot) & set(swapna_slot.flatten())) > 0:
                print("Appointment is fixed at {} with Dr.Swapna" .format(self.patient_slot))
            
            else:
                pass

patient_apt = scheduler(tarun, SLOT_2)
patient_apt.schedule()      
# datetime.strptime('Mar 1 2020  8:00AM', '%b %d %Y %I:%M%p')