from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
    


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.doctor.name
    
    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    