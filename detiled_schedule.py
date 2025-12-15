from EncodingAndInit import *


def get_detailed_schedule(chromosome: List[int]) -> List[Dict]:

    detailed_schedule = []

    slot_map = {slot['SlotID']: slot for slot in ALL_SLOTS}

    for i in range(NUM_MATCHES):
        match_id = i
        home_team, away_team = ALL_MATCHES[i]
        slot_id = chromosome[i]
        slot_info = slot_map.get(slot_id)

        if slot_info is None:
            continue

        detailed_schedule.append({
            'MatchID': match_id,
            'Home': home_team,
            'Away': away_team,
            'DateTime': slot_info['DateTime'],
            'RoundIndex': slot_info['RoundIndex'],
            'VenueID': slot_info['VenueID']
        })

    return detailed_schedule