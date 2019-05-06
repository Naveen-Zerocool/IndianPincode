from django.db import models


class IndianPincode(models.Model):
    office_name = models.TextField(verbose_name='Office Name', help_text='Office Name')
    pin_code = models.IntegerField(verbose_name='Pincode', help_text='Pincode')
    office_type = models.TextField(verbose_name='Office Type', help_text='Office Type')
    delivery_status = models.CharField(max_length=100, verbose_name='Delivery Status', help_text='Delivery Status')
    division_name = models.TextField(verbose_name='Division Name', help_text='Division')
    region_name = models.TextField(verbose_name='Region Name', help_text='Region')
    circle_name = models.TextField(verbose_name='Circle Name', help_text='Circle')
    taluk = models.TextField(verbose_name='Taluk Name', help_text='Taluk')
    district_name = models.TextField(verbose_name='District Name', help_text='District')
    state_name = models.TextField(verbose_name='State Name', help_text='State')

    def __str__(self):
        return str(self.pin_code) + " - " + str(self.office_name) + " - "\
               + str(self.district_name) + " - " + str(self.state_name)

    class Meta:
        db_table = 'indian_pincode'
