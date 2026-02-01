import json


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

    original_data['version'] = patch_data['toVersion']
    original_data['parent'] = original_data


def rollback(ad_load):
    pass

if __name__ == '__main__':
    original_load = "JsonFiles/adload1.json"
    patch1 = "JsonFiles/patch1.json"
    modify_ad_load(original_load, patch1)