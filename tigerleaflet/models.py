from django.contrib.gis.db import models


class State(models.Model):
    fips_code = models.CharField('FIPS Code', max_length=2)
    usps_code = models.CharField('USPS state abbreviation', max_length=2, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    area_description_code = models.CharField(max_length=2)
    feature_class_code = models.CharField(max_length=5)
    functional_status = models.CharField(max_length=1)
    mpoly = models.MultiPolygonField()

    objects = models.GeoManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class County(models.Model):
    state = models.ForeignKey(State)
    # redundant field, but necessary until serializer overrides can be done
    usps_code = models.CharField('USPS state abbreviation', max_length=2)
    state_fips_code = models.CharField('State FIPS Code', max_length=2)
    fips_code = models.CharField('FIPS Code', max_length=3)
    county_identifier = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    name_and_description = models.CharField(max_length=100)
    legal_statistical_description = models.CharField(max_length=2)
    fips_55_class_code = models.CharField(max_length=2)
    feature_class_code = models.CharField(max_length=5)
    functional_status = models.CharField(max_length=1)
    mpoly = models.MultiPolygonField()

    objects = models.GeoManager()

    def save(self, *args, **kwargs):
        self.state = State.objects.get(fips_code=self.state_fips_code)
        self.usps_code = self.state.usps_code
        super(County, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Counties'

    def __str__(self):
        return self.name + ", " + self.usps_code
