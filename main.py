import json
import copy


def modify_ad_load(ad_load, patch):
    with open(ad_load) as f:
        original_data = json.load(f)
    with open(patch) as f:
        patch_data = json.load(f)


    original_campaigns = original_data['data']
    patch_campaigns = patch_data['data']

    for p_campaign in patch_campaigns:
        for o_campaign in original_campaigns:
            if p_campaign['campaign_id'] == o_campaign['campaign_id']:
                o_campaign.update(p_campaign)

    #Create a snapshot of parent and set 'parent' equal to it
    parent_snapshot = copy.deepcopy(original_data)
    original_data['parent'] = parent_snapshot

    original_data['version'] = patch_data['toVersion']
    #Update original_data with new information
    with open(ad_load, "w") as f:
        json.dump(original_data, f, indent=2)


def rollback(ad_load):
    with open(ad_load) as f:
        current_data = json.load(f)
    current_data.update(current_data['parent'])
    print(current_data)

if __name__ == '__main__':
    original_load = "JsonFiles/adload1.json"
    patch1 = "JsonFiles/patch1.json"
    modify_ad_load(original_load, patch1)
    rollback(original_load)