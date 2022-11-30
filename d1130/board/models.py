from django.db import models

# Create your models here.
class Board(models.Model):
	title   = models.CharField(max_length=200)
	author  = models.CharField(max_length=30)
	article = models.TextField(null=True)
	date    = models.DateTimeField(auto_now_add=True)

	# class Meta:
	# 	managed = False
	# 	db_table = 'board_boardtest'
	
	def __str__(self):
		return self.title