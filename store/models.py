from django.db import models
from django.conf import settings

# Create your models here.

class Properties(models.Model):
    #what I put in the API
    externalid = models.TextField(db_column='externalId', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    arearaw = models.TextField(db_column='areaRaw', blank=True, null=True)  # Field name made lowercase.
    areasqm = models.IntegerField(db_column='areaSqm', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(blank=True, null=True)
    coverimageurl = models.TextField(db_column='coverImageUrl', blank=True, null=True)  # Field name made lowercase.
    furnish = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    postalcode = models.TextField(db_column='postalCode', blank=True, null=True)  # Field name made lowercase.
    postedago = models.TextField(db_column='postedAgo', blank=True, null=True)  # Field name made lowercase.
    propertytype = models.TextField(db_column='propertyType', blank=True, null=True)  # Field name made lowercase.
    rawavailability = models.TextField(db_column='rawAvailability', blank=True, null=True)  # Field name made lowercase.
    rent = models.IntegerField(blank=True, null=True)
    rentdetail = models.TextField(db_column='rentDetail', blank=True, null=True)  # Field name made lowercase.
    rentraw = models.TextField(db_column='rentRaw', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    additionalcosts = models.FloatField(db_column='additionalCosts', blank=True, null=True)  # Field name made lowercase.
    additionalcostsraw = models.TextField(db_column='additionalCostsRaw', blank=True, null=True)  # Field name made lowercase.
    deposit = models.FloatField(blank=True, null=True)
    depositraw = models.TextField(db_column='depositRaw', blank=True, null=True)  # Field name made lowercase.
    descriptionnontranslated = models.TextField(db_column='descriptionNonTranslated', blank=True, null=True)  # Field name made lowercase.
    descriptionnontranslatedraw = models.TextField(db_column='descriptionNonTranslatedRaw', blank=True, null=True)  # Field name made lowercase.
    descriptiontranslated = models.TextField(db_column='descriptionTranslated', blank=True, null=True)  # Field name made lowercase.
    descriptiontranslatedraw = models.TextField(db_column='descriptionTranslatedRaw', blank=True, null=True)  # Field name made lowercase.
    energylabel = models.TextField(db_column='energyLabel', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(blank=True, null=True)
    internet = models.TextField(blank=True, null=True)
    isroomactive = models.TextField(db_column='isRoomActive', blank=True, null=True)  # Field name made lowercase.
    kitchen = models.TextField(blank=True, null=True)
    living = models.TextField(blank=True, null=True)
    matchage = models.TextField(db_column='matchAge', blank=True, null=True)  # Field name made lowercase.
    matchagebackup = models.TextField(db_column='matchAgeBackup', blank=True, null=True)  # Field name made lowercase.
    matchcapacity = models.TextField(db_column='matchCapacity', blank=True, null=True)  # Field name made lowercase.
    matchgender = models.TextField(db_column='matchGender', blank=True, null=True)  # Field name made lowercase.
    matchgenderbackup = models.TextField(db_column='matchGenderBackup', blank=True, null=True)  # Field name made lowercase.
    matchlanguages = models.TextField(db_column='matchLanguages', blank=True, null=True)  # Field name made lowercase.
    matchstatus = models.TextField(db_column='matchStatus', blank=True, null=True)  # Field name made lowercase.
    matchstatusbackup = models.TextField(db_column='matchStatusBackup', blank=True, null=True)  # Field name made lowercase.
    pagedescription = models.TextField(db_column='pageDescription', blank=True, null=True)  # Field name made lowercase.
    pagetitle = models.TextField(db_column='pageTitle', blank=True, null=True)  # Field name made lowercase.
    pets = models.TextField(blank=True, null=True)
    registrationcost = models.TextField(db_column='registrationCost', blank=True, null=True)  # Field name made lowercase.
    registrationcostraw = models.TextField(db_column='registrationCostRaw', blank=True, null=True)  # Field name made lowercase.
    roommates = models.TextField(blank=True, null=True)
    shower = models.TextField(blank=True, null=True)
    smokinginside = models.TextField(db_column='smokingInside', blank=True, null=True)  # Field name made lowercase.
    toilet = models.TextField(blank=True, null=True)
    userdisplayname = models.TextField(db_column='userDisplayName', blank=True, null=True)  # Field name made lowercase.
    userid = models.TextField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    userlastloggedon = models.TextField(db_column='userLastLoggedOn', blank=True, null=True)  # Field name made lowercase.
    usermembersince = models.TextField(db_column='userMemberSince', blank=True, null=True)  # Field name made lowercase.
    userphotourl = models.TextField(db_column='userPhotoUrl', blank=True, null=True)  # Field name made lowercase.
    field_id_oid = models.TextField(db_column='_id.$oid', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    firstseenat_date = models.TextField(db_column='firstSeenAt.$date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lastseenat_date = models.TextField(db_column='lastSeenAt.$date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    additionalcostsdescription = models.TextField(db_column='additionalCostsDescription',blank=True,null=True)

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, primary_key=True)  # User as primary key
    properties = models.ManyToManyField(Properties,  related_name='wishlists')  # Many-to-Many relationship
