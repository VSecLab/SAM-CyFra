from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from enum import Enum

# Create your models here.
# To execute the database dump, in the terminal digit:
# mysqldump -u root -p egov_db > egov_db.sql


class System(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name="System"
        verbose_name_plural="Systems"

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        processes = Process.objects.filter(system=self)
        for process in processes:
            process.xml.delete()
        super().delete(*args, **kwargs)

class Process(models.Model):
    name = models.CharField(max_length=100)
    xml = models.FileField(upload_to='processes/xml/',
                           validators=[FileExtensionValidator(allowed_extensions=['xml','bpmn'])])
    system = models.ForeignKey(System, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Process"
        verbose_name_plural="Processes"

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.xml.delete()
        super().delete(*args, **kwargs)

class Asset_type(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name="Asset_type"
        verbose_name_plural="Assets_types"

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=100)
    bpmn_id= models.CharField(max_length=100,null=True)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    asset_type = models.ForeignKey(Asset_type,on_delete=models.CASCADE,null=True)
    position=models.CharField(max_length=100,null=True)

    class Meta:
        verbose_name="Asset"
        verbose_name_plural="Assets"

    def __str__(self):
        return self.name

class Attribute_value(models.Model):
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name="Attribute_value"
        verbose_name_plural="Attributes_values"

    def __str__(self):
        return self.value

class Threat(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name="Threat"
        verbose_name_plural="Threats"

    def __str__(self):
        return self.name

class Attribute(models.Model):
    attribute_name = models.CharField(max_length=100)
    asset_type = models.ForeignKey(Asset_type,on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(Attribute_value,on_delete=models.CASCADE)

    class Meta:
        verbose_name="Attribute"
        verbose_name_plural="Attributes"

    def __str__(self):
        return self.attribute_name

class control_framework(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.name

class Family(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    framework_id=models.ForeignKey(control_framework,on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "Family"
        verbose_name_plural = "Families"

    def __str__(self):
        return self.name

class Control(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    family= models.ForeignKey(Family, on_delete=models.CASCADE, default='1', null=True)
    maturity_level = models.CharField(max_length=100, default = "minimo")

    class Meta:
        verbose_name="Control"
        verbose_name_plural="Controls"

    def __str__(self):
        return self.name

class Asset_has_attribute(models.Model):
    asset = models.ForeignKey(Asset,on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute,on_delete=models.CASCADE)

class Threat_has_attribute(models.Model):
    threat = models.ForeignKey(Threat,on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute,on_delete=models.CASCADE)

class Threat_has_control(models.Model):
    threat = models.ForeignKey(Threat, on_delete=models.CASCADE)
    control = models.ForeignKey(Control, on_delete=models.CASCADE)

class Threat_has_family(models.Model):
    threat = models.ForeignKey(Threat, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

# AL MODELLO DEI DATI MANCA SOLO LA PARTE RELATIVA AI THREAT AGENTS

class Category(models.Model):

    class FunctionStatus(Enum):
        IDENTIFY = 'ID'
        PROTECT = 'PR'
        DETECT = 'DE'
        RESPOND = 'RS'
        RECOVER = 'RC'

        def __str__(self):
            return self.value

        @classmethod
        def choices(cls):
            return (
                (str(cls.IDENTIFY), _('Identify')),
                (str(cls.PROTECT), _('Protect')),
                (str(cls.DETECT), _('Detect')),
                (str(cls.RESPOND), _('Respond')),
                (str(cls.RECOVER), _('Recover')),
            )


    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    function = models.CharField(_('function'), default = FunctionStatus.IDENTIFY, choices= FunctionStatus.choices(), max_length= 250)
    source=models.CharField(max_length=500, default = 'Cybersecurity framework nazionale')


    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name= models.CharField(max_length=100)
    description= models.CharField(max_length=500)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name= "Subcategory"
        verbose_name_plural="Subcategories"

    def __str__(self):
        return self.name

class Context(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Context"
        verbose_name_plural = "Contexts"

    def __str__(self):
        return self.name

class Contextualization(models.Model):
   context=models.ForeignKey(Context, on_delete=models.CASCADE)
   subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE)
   priority= models.CharField(max_length=100)


class Profile(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, null=True, blank=True)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    framework=models.ForeignKey(control_framework, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.name


class Maturity_level(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    level=models.CharField(max_length=100)
    context=models.ForeignKey(Context,on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "Maturity_level"
        verbose_name_plural = "maturity_levels"

    def __str__(self):
        return self.name

class contextualization_has_maturity_levels(models.Model):
    subcategory_contextualization=models.ForeignKey(Contextualization, on_delete=models.CASCADE)
    maturity_level=models.ForeignKey(Maturity_level,on_delete=models.CASCADE)

class profile_has_subcategory(models.Model):
   profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
   subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE)
   priority= models.CharField(max_length=100)
   maturity_level = models.ForeignKey(Maturity_level, on_delete=models.CASCADE, default="3")


class profile_maturity_control(models.Model):
   profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
   subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE)
   control=models.ForeignKey(Control, on_delete=models.CASCADE)
   implementation=models.CharField(max_length=1000, null=True)

class is_a_requirement_for_mitigation(models.Model):
    threat=models.ForeignKey(Threat,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)

class Subcategory_is_implemented_through_control(models.Model):
    subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    control=models.ForeignKey(Control, on_delete=models.CASCADE)

class Threat_has_threatdetails(models.Model):
    threat=models.ForeignKey(Threat, related_name= 'threat_father', on_delete=models.CASCADE)
    threatdetails=models.ForeignKey(Threat,related_name='threat_child', on_delete=models.CASCADE)

class Control_has_subcontrol(models.Model):
    control=models.ForeignKey(Control, related_name='control_father', on_delete=models.CASCADE)
    subcontrol=models.ForeignKey(Control,  related_name='control_child', on_delete=models.CASCADE)

class Control_has_relatedcontrol(models.Model):
    control= models.ForeignKey(Control, related_name='control_relating', on_delete=models.CASCADE)
    relatedcontrol=models.ForeignKey(Control, related_name='control_related', on_delete= models.CASCADE)
    family= models.ForeignKey(Family, related_name='family_relating', on_delete=models.CASCADE)
    relatedfamily = models.ForeignKey(Family, related_name='family_related', on_delete=models.CASCADE)

class Fusioncontext_has_context(models.Model):
    fusion_context = models.ForeignKey(Context, related_name='context_father', on_delete=models.CASCADE)
    context= models.ForeignKey(Context, related_name= 'context_child', on_delete=models.CASCADE)



