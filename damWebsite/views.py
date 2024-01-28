from django.shortcuts import render, redirect

#from .models import DassetsT
from .models import LocationLu
from .models import ActionLu, EmotionLu, ScenarioLu, LocationtagT, ActiontagT, EmotiontagT,ScenariotagT, TagsT, AssetTagsT, DassetsT

#C:\Users\punya\Documents\Project\ddamPro\DAM_Project\damWebsite\models.py

def home(request):
    return render(request, 'home.html', {})

def SearchAsset(request):
    #table1_values = Table1.objects.values_list('field_name', flat=True)
    Locations = LocationLu.objects.all().values_list('locationid', 'locationdescription')
    Actions = ActionLu.objects.all().values_list('actionid', 'actiondescription') 
    Emotions = EmotionLu.objects.all().values_list('emotionid', 'edescription') 
    Scenarios = ScenarioLu.objects.all().values_list('scenarioid', 'sdescription')   # Fetch data
        
    if request.method == 'GET':
        #print(Locations)
        
        return render(request, 'SearchAsset.html', {'Locations':Locations,
                                                'Actions' : Actions,
                                                'Emotions': Emotions,
                                                'Scenarios':Scenarios})
    if request.method == 'POST':
       Location_value = request.POST.get('Locations')
       Action_value = request.POST.get('Actions')
       Emotion_value = request.POST.get('Emotions')
       Scenario_value = request.POST.get('Scenarios')

       results = search_assets_logic(Location_value, Action_value, Emotion_value, Scenario_value)  # Assumed function for asset search
    return render(request, 'Assets.html', {'results' : results})


def search_assets_logic(param1, param2, param3, param4):
    # Perform actions based on parameters, e.g., query the asset table
    # ...
    try:
        print(param1)
        print(param2)
        print(param3)
        print(param4)

        Locations = LocationLu.objects.all().values_list('locationid', 'locationdescription')
        Actions = ActionLu.objects.all().values_list('actionid', 'actiondescription') 
        Emotions = EmotionLu.objects.all().values_list('emotionid', 'edescription') 
        Scenarios = ScenarioLu.objects.all().values_list('scenarioid', 'sdescription')

        location_match = Locations.filter(locationdescription=param1).first()
        #print(location_match)
        locationID = location_match[0]

        action_match = Actions.filter(actiondescription=param2).first()
        actionID = action_match[0]

        emotion_match = Emotions.filter(edescription=param3).first()
        emotionID = emotion_match[0]

        scenario_match = Scenarios.filter(sdescription=param4).first()
        scenarioID = scenario_match[0]

        Locationtag = LocationtagT.objects.all().values_list('tag', 'location')
        Actiontag = ActiontagT.objects.all().values_list('tag', 'action') 
        Emotiontag = EmotiontagT.objects.all().values_list('tag', 'emotion') 
        Scenariotag = ScenariotagT.objects.all().values_list('tag', 'scenario')

        locationtag_match = Locationtag.filter(location=locationID).first()
        locationtagID = locationtag_match[0]

        actiontag_match = Actiontag.filter(action=actionID).first()
        actiontagID = actiontag_match[0]

        emotiontag_match = Emotiontag.filter(emotion=emotionID).first()
        emotiontagID = emotiontag_match[0]

        scenariotag_match = Scenariotag.filter(scenario=scenarioID).first()
        scenariotagID = scenariotag_match[0]

        TagID = TagsT.objects.all().values_list('tagid', 'tagtype')
        tags_list = []

        tag_match = TagID.filter(tagid=locationtagID).first()
        tags_list.append(tag_match[0])

        tag_match = TagID.filter(tagid = actiontagID).first()
        tags_list.append(tag_match[0])

        tag_match = TagID.filter(tagid = emotiontagID).first()
        tags_list.append(tag_match[0])

        tag_match = TagID.filter(tagid = scenariotagID).first()
        tags_list.append(tag_match[0])

        #print(tags_list)

        DAssetID = DassetsT.objects.all().values_list('assetid','filename','link','updatedtime')
        #DAssets_dict = {}
        DAssets_list = []
        for i in tags_list:
            AssetID = AssetTagsT.objects.all().values_list('dassetid', 'tagsid')
            #print(DAssetID)
            Assettag_match = AssetID.filter(tagsid = i).first()
            print(Assettag_match)
            Assettag = Assettag_match[0]
            Asset_value = DAssetID.filter(assetid = Assettag).first()
            #DAssets_list.append(Asset_value)
            if(Asset_value not in DAssets_list):
                DAssets_list.append(Asset_value)
        print(DAssets_list)
        return DAssets_list
    except:
        return "No asset found"
    