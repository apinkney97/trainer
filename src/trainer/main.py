from trainer.settings import settings

from nrewebservices.ldbws import Session


def main():

    session = Session(wsdl=settings.api_url, api_key=settings.api_key)
    board = session.get_station_board(
        crs="SDH",
        rows=50,
        include_departures=True,
        include_arrivals=False,
        to_filter_crs="MYB",
    )

    print(f"Departures from {board.location_name}:")

    for service in board.train_services:
        print(f"{service.std}   {service.destination:30s} {service.etd:10s} {service.operator}")
        # print(service.__dict__)
        # {'origins': [<nrewebservices.ldbws.responses.ServiceLocation object at 0x7f0bf037edb0>], 'destinations': [<nrewebservices.ldbws.responses.ServiceLocation object at 0x7f0bf15772f0>], 'current_origins': [], 'current_destinations': [], 'sta': None, 'eta': None, 'std': 22:31, 'etd': On time, 'platform': 5, 'operator': Elizabeth Line, 'operator_code': XR, 'circular_route': False, 'cancelled': False, 'filter_location_cancelled': False, 'service_type': train, 'length': None, 'detach_front': False, 'reverse_formation': False, 'cancel_reason': None, 'delay_reason': None, 'service_id': 3791720STFD____, 'adhoc_alerts': None, 'rsid': None, 'formation': None, 'origin': 'Shenfield', 'destination': 'London Paddington'}
        # {'origins': [<nrewebservices.ldbws.responses.ServiceLocation object at 0x7f0bf0127260>], 'destinations': [<nrewebservices.ldbws.responses.ServiceLocation object at 0x7f0bf0127560>], 'current_origins': [], 'current_destinations': [], 'sta': None, 'eta': None, 'std': 22:36, 'etd': On time, 'platform': 9, 'operator': Greater Anglia, 'operator_code': LE, 'circular_route': False, 'cancelled': False, 'filter_location_cancelled': False, 'service_type': train, 'length': 5, 'detach_front': False, 'reverse_formation': False, 'cancel_reason': None, 'delay_reason': None, 'service_id': 3794372STFD____, 'adhoc_alerts': None, 'rsid': None, 'formation': None, 'origin': 'Colchester Town', 'destination': 'London Liverpool Street'}
