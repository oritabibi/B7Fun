from django.db import models
class community_centers(models.Model):
    Address =  models.CharField(max_length=255, verbose_name="Address")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    Name = models.CharField(max_length=255, verbose_name="Name")
    neighborhood = models.CharField(max_length=255, verbose_name="neighborhood")

    class Meta:
        db_table = 'community_centers'

    def __str__(self):
        return self.Name


class dog_gardens(models.Model):
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    Name = models.CharField(max_length=255, verbose_name="Name")
    SHAPE_Area = models.CharField(max_length=255, verbose_name="SHAPE_Area")
    SHAPE_Length = models.CharField(max_length=255, verbose_name="SHAPE_Length")

    class Meta:
        db_table = 'dog_gardens'

    def __str__(self):
        return self.Name

class elderly_social_club(models.Model):
    Address =  models.CharField(max_length=255, verbose_name="Address")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    Name = models.CharField(max_length=255, verbose_name="Name")
    Type = models.CharField(max_length=255, verbose_name="type")

    class Meta:
        db_table = 'elderly_social_club'

    def __str__(self):
        return self.Name


class playgrounds(models.Model):
    carrousel = models.IntegerField(verbose_name="carrousel")
    combined1 = models.IntegerField(verbose_name="combined1")
    combined2 = models.IntegerField(verbose_name="combined2")
    combined3 = models.IntegerField(verbose_name="combined3")
    omega = models.IntegerField(verbose_name="omega")
    roserose = models.IntegerField(verbose_name="roserose")
    slid = models.IntegerField(verbose_name="slid")
    SpecialCom = models.IntegerField(verbose_name="SpecialCom")
    spring = models.IntegerField(verbose_name="spring")
    Swing = models.IntegerField(verbose_name="Swing")
    other = models.CharField(max_length=255, verbose_name="other")
    shadowing = models.CharField(max_length=255, verbose_name="shadowing")
    surface = models.CharField(max_length=255, verbose_name="surface")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    Name = models.CharField(max_length=255, verbose_name="Name")

    class Meta:
        db_table = 'playgrounds'

    def __str__(self):
        return self.Name
    
class sport_facilities(models.Model):
    Type = models.CharField(max_length=255, verbose_name="shadowing")
    Name = models.CharField(max_length=255, verbose_name="Name")
    street = models.CharField(max_length=255, verbose_name="street")
    HouseNumber = models.CharField(max_length=255, verbose_name="HouseNumber")
    neighborhood = models.CharField(max_length=255, verbose_name="neighborhood")
    Operator = models.CharField(max_length=255, verbose_name="Operator")
    Seats = models.IntegerField(verbose_name="Seats")
    Activity = models.CharField(max_length=255, verbose_name="Activity")
    fencing = models.CharField(max_length=255, verbose_name="fencing")
    lighting = models.CharField(max_length=255, verbose_name="lighting")
    handicapped = models.CharField(max_length=255, verbose_name="handicapped")
    condition = models.CharField(max_length=255, verbose_name="condition")
    Owner = models.CharField(max_length=255, verbose_name="Owner")
    ForSchool = models.CharField(max_length=255, verbose_name="ForSchool")
    association = models.CharField(max_length=255, verbose_name="association")
    SportType = models.CharField(max_length=255, verbose_name="SportType")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    

    class Meta:
        db_table = 'sport_facilities'

    def __str__(self):
        return self.Name

class urban_nature(models.Model):
    MainFeature = models.CharField(max_length=255, verbose_name="MainFeature")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    
    class Meta:
        db_table = 'urban_nature'

    def __str__(self):
        return self.MainFeature
