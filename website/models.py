from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    songs_no = models.IntegerField()
    album_logo = models.ImageField(upload_to='album_logo', blank=True, null=False)

    def __str__(self):
        return self.album_name

#
# class Song(models.Model):
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     song_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.song_name


class Contact(models.Model):
    name = models.CharField(max_length=100, )
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name
