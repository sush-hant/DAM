from django.db import models

class ActionLu(models.Model):
    actionid = models.AutoField(db_column='ActionID', primary_key=True)  # Field name made lowercase.
    actiondescription = models.CharField(db_column='ActionDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'action_lu'


class ActiontagT(models.Model):
    tag = models.OneToOneField('TagsT', models.DO_NOTHING, db_column='Tag_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Tag_ID, Action_ID) found, that is not supported. The first column is selected.
    action = models.ForeignKey(ActionLu, models.DO_NOTHING, db_column='Action_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actiontag_t'
        unique_together = (('tag', 'action'),)


class AssetTagsT(models.Model):
    dassetid = models.OneToOneField('DassetsT', models.DO_NOTHING, db_column='DAssetID', primary_key=True)  # Field name made lowercase. The composite primary key (DAssetID, TagsID) found, that is not supported. The first column is selected.
    tagsid = models.ForeignKey('TagsT', models.DO_NOTHING, db_column='TagsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asset_tags_t'
        unique_together = (('dassetid', 'tagsid'),)


class DassetsT(models.Model):
    assetid = models.AutoField(db_column='AssetID', primary_key=True)  # Field name made lowercase.
    filename = models.CharField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=1000, blank=True, null=True)
    updatedtime = models.DateTimeField(db_column='UpdatedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dassets_t'


class EmotionLu(models.Model):
    emotionid = models.AutoField(db_column='EmotionID', primary_key=True)  # Field name made lowercase.
    edescription = models.CharField(db_column='EDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emotion_lu'


class EmotiontagT(models.Model):
    tag = models.OneToOneField('TagsT', models.DO_NOTHING, db_column='Tag_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Tag_ID, Emotion_ID) found, that is not supported. The first column is selected.
    emotion = models.ForeignKey(EmotionLu, models.DO_NOTHING, db_column='Emotion_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emotiontag_t'
        unique_together = (('tag', 'emotion'),)


class LocationLu(models.Model):
    locationid = models.AutoField(db_column='LocationID', primary_key=True)  # Field name made lowercase.
    locationdescription = models.CharField(db_column='LocationDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location_lu'

class LocationtagT(models.Model):
    tag = models.OneToOneField('TagsT', models.DO_NOTHING, db_column='Tag_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Tag_ID, Location_ID) found, that is not supported. The first column is selected.
    location = models.ForeignKey(LocationLu, models.DO_NOTHING, db_column='Location_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'locationtag_t'
        unique_together = (('tag', 'location'),)


class PassengertypeLu(models.Model):
    ptypeid = models.AutoField(db_column='PTypeID', primary_key=True)  # Field name made lowercase.
    pdescription = models.CharField(db_column='PDescription', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'passengertype_lu'


class ScenarioLu(models.Model):
    scenarioid = models.AutoField(db_column='ScenarioID', primary_key=True)  # Field name made lowercase.
    sdescription = models.CharField(db_column='SDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scenario_lu'


class ScenariotagT(models.Model):
    tag = models.OneToOneField('TagsT', models.DO_NOTHING, db_column='Tag_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Tag_ID, Scenario_ID) found, that is not supported. The first column is selected.
    scenario = models.ForeignKey(ScenarioLu, models.DO_NOTHING, db_column='Scenario_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scenariotag_t'
        unique_together = (('tag', 'scenario'),)


class TagsT(models.Model):
    tagid = models.AutoField(db_column='TagID', primary_key=True)  # Field name made lowercase.
    tagtype = models.CharField(db_column='TagType', max_length=200, blank=True, null=True)  # Field name made lowercase.       

    class Meta:
        managed = False
        db_table = 'tags_t'


class WorkertypeLu(models.Model):
    wtypeid = models.AutoField(db_column='WTypeID', primary_key=True)  # Field name made lowercase.
    wdescription = models.CharField(db_column='WDescription', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workertype_lu'



