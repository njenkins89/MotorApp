# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Currents(models.Model):
    id = models.IntegerField(unique=True, primary_key = True)
    latticesize = models.BigIntegerField(db_column='LatticeSize', blank=True, null=True)  # Field name made lowercase.
    density = models.FloatField(db_column='Density', blank=True, null=True)  # Field name made lowercase.
    k12 = models.BigIntegerField(blank=True, null=True)
    k23 = models.BigIntegerField(blank=True, null=True)
    k3fa = models.FloatField(blank=True, null=True)
    k3fb = models.BigIntegerField(blank=True, null=True)
    k3fc = models.FloatField(blank=True, null=True)
    k3b = models.BigIntegerField(blank=True, null=True)
    fuelgrad = models.FloatField(db_column='fuelGrad', blank=True, null=True)  # Field name made lowercase.
    current = models.TextField(db_column='Current', blank=True, null=True)  # Field name made lowercase.
    time = models.BigIntegerField(db_column='SimTime', blank=True, null=True)  # Field name made lowercase.
    forceMean = models.FloatField(db_column='ForceMean', blank=True, null=True)  # Field name made lowercase.
    forceStd = models.TextField(db_column='ForceStdDev', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Currents'


class Data(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    latticesize = models.IntegerField(db_column='LatticeSize', blank=True, null=True)  # Field name made lowercase.
    density = models.FloatField(db_column='Density', blank=True, null=True)  # Field name made lowercase.
    k12 = models.FloatField(blank=True, null=True)
    k23 = models.FloatField(blank=True, null=True)
    k3fa = models.FloatField(blank=True, null=True)
    k3fb = models.FloatField(blank=True, null=True)
    k3fc = models.FloatField(blank=True, null=True)
    k3b = models.FloatField(blank=True, null=True)
    fuelgrad = models.FloatField(db_column='fuelGrad', blank=True, null=True)  # Field name made lowercase.
    event = models.CharField(db_column='Event', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dwell = models.FloatField(db_column='Dwell', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Data'


class Trap(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    latticesize = models.IntegerField(db_column='LatticeSize', blank=True, null=True)  # Field name made lowercase.
    stiffness = models.FloatField(db_column='Stiffness', blank=True, null=True)  # Field name made lowercase.
    k12 = models.FloatField(blank=True, null=True)
    k23 = models.FloatField(blank=True, null=True)
    k3fa = models.FloatField(blank=True, null=True)
    k3fb = models.FloatField(blank=True, null=True)
    k3fc = models.FloatField(blank=True, null=True)
    k3b = models.FloatField(blank=True, null=True)
    fuelgrad = models.FloatField(db_column='fuelGrad', blank=True, null=True)  # Field name made lowercase.
    event = models.CharField(db_column='Event', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dwell = models.FloatField(db_column='Dwell', blank=True, null=True)  # Field name made lowercase.
    force = models.FloatField(db_column='Force', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trap'


class Multiplemotor(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    latticesize = models.BigIntegerField(db_column='LatticeSize', blank=True, null=True)  # Field name made lowercase.
    density = models.FloatField(db_column='Density', blank=True, null=True)  # Field name made lowercase.
    k12 = models.BigIntegerField(blank=True, null=True)
    k23 = models.BigIntegerField(blank=True, null=True)
    k3fa = models.FloatField(blank=True, null=True)
    k3fb = models.BigIntegerField(blank=True, null=True)
    k3fc = models.FloatField(blank=True, null=True)
    k3b = models.BigIntegerField(blank=True, null=True)
    fuelgrad = models.FloatField(db_column='fuelGrad', blank=True, null=True)  # Field name made lowercase.
    event = models.TextField(db_column='Event', blank=True, null=True)  # Field name made lowercase.
    dwell = models.FloatField(db_column='Dwell', blank=True, null=True)  # Field name made lowercase.
    force = models.FloatField(db_column='Force', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'multipleMotor'
