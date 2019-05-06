def collect_pin_codes(offset_count=0):
    try:
        import requests
        from data_source import IndianPinCode
        endpoint = "https://api.data.gov.in/resource/6176ee09-3d56-4a3b-8115-21841576b2f6?" \
                   "api-key=API_CODE&format=json&offset="+str(offset_count)+"&limit=1000"

        response = requests.get(endpoint)
        if response.status_code != 200:
            return {"status": "FAILED", "msg": "Bad status code from data.gov.in"}
        response = response.json()
        pin_code_list = response["records"]
        if len(pin_code_list) == 0:
            return {"status": "COMPLETED", "msg": "No more pin code data from data.gov.in"}

        insert_list = []

        for code in pin_code_list:
            insert_list.append(IndianPinCode(office_name=code["officename"], pin_code=code["pincode"],
                                             office_type=code["officetype"], delivery_status=code["deliverystatus"],
                                             division_name=code["divisionname"], region_name=code["regionname"],
                                             circle_name=code["circlename"], taluk=code["taluk"],
                                             district_name=code["districtname"], state_name=code["statename"]))
        return insert_list
    except Exception as err:
        print("collect_pin_codes Error--->", err)
        return {"status": "FAILED", "msg": "Error in collect_pin_codes"}


def insert_codes(list_of_codes):
    try:
        if 'status' not in list_of_codes:
            from data_source import Session
            session = Session()
            session.add_all(list_of_codes)
            session.commit()
            return {"status": "SUCCESS", "msg": "Completed writing a specific set of pin codes on database"}
        return list_of_codes
    except Exception as err:
        print("insert_codes Error--->", err)
        return {"status": "FAILED", "msg": "Error in insert_codes"}


count = 0
switch = True
while switch:
    start_collecting_data = insert_codes(collect_pin_codes(count))
    print(count,"Output --->", start_collecting_data)
    count += 1000
    if start_collecting_data["status"] == "COMPLETED":
        switch = False
