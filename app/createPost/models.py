from django.db import models
from django.utils import timezone
from app.models import AuthUser
import os
import uuid
from django.dispatch import receiver

class createdPost(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100,blank=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.SmallIntegerField()
    remarks = models.TextField()
    photo = models.FileField(upload_to='PROFILE/',default='PROFILE/nopicture1.jpg')
    services_type = models.CharField(max_length=255)

    @property
    def get_pict(self):
        data = upload_profile.objects.filter(created_id=self.id).all()
        for row in data:
            return row.profile_pict
        
    @property
    def get_location(self):
        data = createLocation.objects.filter(created_id=self.id).all()
        for row in data:
            return row.location

    class Meta:
        managed = False
        db_table = 'created_post'


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename_start = filename.replace('.'+ext,'')
    filename = "%s__%s.%s" % (uuid.uuid4(),filename_start, ext)
    return os.path.join('UPLOADED', filename)

class uploadfile(models.Model):
    title_post = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100)
    description_post = models.TextField()
    status = models.SmallIntegerField(default=1)
    file_upload = models.FileField(upload_to=get_file_path,verbose_name=(u'File'))
    title = models.ForeignKey('createdPost', models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)
    file_ext = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'created_postdata'


def get_profile_picture(instance, filename):
    ext = filename.split('.')[-1]
    filename_start = filename.replace('.'+ext,'')
    filename = "%s__%s.%s" % (uuid.uuid4(),filename_start, ext)
    return os.path.join('PROFILE', filename)

class upload_profile(models.Model):
    created = models.ForeignKey('createdPost', models.DO_NOTHING)
    profile_pict = models.FileField(upload_to=get_profile_picture,verbose_name=(u'File'))
    class Meta:
        managed = False
        db_table = 'created_postprofile'


@receiver(models.signals.post_delete, sender=upload_profile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.profile_pict:
        if os.path.isfile(instance.profile_pict.path):
            os.remove(instance.profile_pict.path)


def get_location_picture(instance, filename):
    ext = filename.split('.')[-1]
    filename_start = filename.replace('.'+ext,'')
    filename = "%s__%s.%s" % (uuid.uuid4(),filename_start, ext)
    return os.path.join('LOCATION', filename)

class location_picture(models.Model):
    created = models.ForeignKey('createdPost', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    photo = models.FileField(upload_to=get_location_picture, verbose_name=(u'File'))
    class Meta:
        managed = False
        db_table = 'created_picturelocation'

class createLocation(models.Model):
    created = models.ForeignKey('createdPost', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    location = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'created_location'

class createFeedback(models.Model):
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    mood = models.CharField(max_length=255)
    sex = models.SmallIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    class Meta:
        managed = False
        db_table = 'created_feedback'

#DIRECTORY LIST

class createDirectory(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    information = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'create_directorylist'

def get_Directory_Profile(instance, filename):
    ext = filename.split('.')[-1]
    filename_start = filename.replace('.'+ext,'')
    filename = "%s__%s.%s" % (uuid.uuid4(),filename_start, ext)
    return os.path.join('Directory_picture', filename)

class createDirectoryPicture(models.Model):
    directory = models.ForeignKey('createDirectory', models.DO_NOTHING)
    photo = models.FileField(upload_to=get_Directory_Profile, verbose_name=(u'File'))
    class Meta:
        managed = False
        db_table = 'create_directorypictures'

#SATELLITE OFFICES

class createDirectorySwad(models.Model):
    swad_team = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)
    contact_no = models.CharField(max_length=255)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)

    
    class Meta:
        managed = False
        db_table = 'create_directoryswad'