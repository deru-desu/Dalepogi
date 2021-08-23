from django.db import models

# Create your models here.

class information(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'fullname', blank = True)

    studentID = models.CharField(max_length = 12, verbose_name = 'student ID', unique = True, blank = True)

    studentstatus = [
                    ('OP', 'Observation and Participation'),
                    ('PT', 'Practice Teacher'),
                    ('Done', 'Done')
    ]

    studentstatus = models.CharField(max_length = 50, choices = studentstatus, verbose_name = 'Student Status', default = '', blank = True)

    professor = models.CharField(max_length = 50, verbose_name = 'Professor in Charge', blank = True)

    school = models.CharField(max_length = 50, verbose_name = 'School', blank = True)

    schedule = models.CharField(max_length = 50, verbose_name = 'Schedule', blank = True)

    def __str__(self):
        return self.studentID

class UpdateInfo(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'fullname', blank = True)

    studentID = models.TextField(max_length = 12, verbose_name = 'student ID', unique = True, blank = True)

    studentstatus = [
                    ('OP', 'Observation and Participation'),
                    ('PT', 'Practice Teacher')
    ]

    studentstatus = models.CharField(max_length = 50, choices = studentstatus, verbose_name = 'Student Status', default = '')

    professor = models.TextField(max_length = 50, verbose_name = 'Professor in Charge', blank = True)

    school = models.TextField(max_length = 50, verbose_name = 'School', blank = True)