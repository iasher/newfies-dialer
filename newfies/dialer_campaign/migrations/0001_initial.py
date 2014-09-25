# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dialer_campaign.models
import jsonfield.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sms', '__first__'),
        ('dnc', '0001_initial'),
        ('audiofield', '__first__'),
        ('dialer_contact', '0001_initial'),
        ('dialer_gateway', '__first__'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campaign_code', models.CharField(default=dialer_campaign.models.set_campaign_code, max_length=20, blank=True, help_text='this code is auto-generated by the platform, this is used to identify the campaign', unique=True, verbose_name='campaign code')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(help_text='campaign description', null=True, verbose_name='description', blank=True)),
                ('status', models.IntegerField(default=2, null=True, verbose_name='status', blank=True, choices=[(3, 'ABORT'), (4, 'END'), (2, 'PAUSE'), (1, 'START')])),
                ('callerid', models.CharField(help_text='outbound Caller ID', max_length=80, verbose_name='Caller ID Number', blank=True)),
                ('caller_name', models.CharField(help_text='outbound Caller Name', max_length=80, verbose_name='Caller Name', blank=True)),
                ('startingdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='start')),
                ('expirationdate', models.DateTimeField(default=dialer_campaign.models.set_expirationdate, verbose_name='finish')),
                ('daily_start_time', models.TimeField(default=b'00:00:00', verbose_name='daily start time')),
                ('daily_stop_time', models.TimeField(default=b'23:59:59', verbose_name='daily stop time')),
                ('monday', models.BooleanField(default=True, verbose_name='monday')),
                ('tuesday', models.BooleanField(default=True, verbose_name='tuesday')),
                ('wednesday', models.BooleanField(default=True, verbose_name='wednesday')),
                ('thursday', models.BooleanField(default=True, verbose_name='thursday')),
                ('friday', models.BooleanField(default=True, verbose_name='friday')),
                ('saturday', models.BooleanField(default=True, verbose_name='saturday')),
                ('sunday', models.BooleanField(default=True, verbose_name='sunday')),
                ('frequency', models.IntegerField(default=b'10', help_text='calls per minute', null=True, verbose_name='frequency', blank=True)),
                ('callmaxduration', models.IntegerField(default=b'1800', help_text='maximum call duration in seconds', null=True, verbose_name='max call duration', blank=True)),
                ('maxretry', models.IntegerField(default=b'0', help_text='maximum retries per contact', null=True, verbose_name='max retries', blank=True)),
                ('intervalretry', models.IntegerField(default=b'300', help_text='time delay in seconds before retrying contact', null=True, verbose_name='time between retries', blank=True)),
                ('completion_maxretry', models.IntegerField(default=b'0', help_text='number of retries until a contact completes survey', null=True, verbose_name='completion max retries', blank=True)),
                ('completion_intervalretry', models.IntegerField(default=b'900', help_text='time delay in seconds before retrying contact to complete survey', null=True, verbose_name='completion time between retries', blank=True)),
                ('calltimeout', models.IntegerField(default=b'45', help_text='connection timeout in seconds', null=True, verbose_name='timeout on call', blank=True)),
                ('object_id', models.PositiveIntegerField(verbose_name='application')),
                ('extra_data', models.CharField(help_text='additional application parameters.', max_length=120, verbose_name='extra parameters', blank=True)),
                ('imported_phonebook', models.CharField(default=b'', max_length=500, verbose_name='imported phonebook', blank=True)),
                ('totalcontact', models.IntegerField(default=0, help_text='total contact for this campaign', null=True, verbose_name='total contact', blank=True)),
                ('completed', models.IntegerField(default=0, help_text='total contact that completed call / survey', null=True, verbose_name='completed', blank=True)),
                ('has_been_started', models.BooleanField(default=False, verbose_name='has been started')),
                ('has_been_duplicated', models.BooleanField(default=False, verbose_name='has been duplicated')),
                ('voicemail', models.BooleanField(default=False, verbose_name='voicemail detection')),
                ('amd_behavior', models.IntegerField(default=1, null=True, verbose_name='detection behaviour', blank=True, choices=[(1, 'ALWAYS PLAY MESSAGE'), (2, 'PLAY MESSAGE TO HUMAN ONLY'), (3, 'LEAVE MESSAGE TO VOICEMAIL ONLY')])),
                ('agent_script', models.TextField(null=True, verbose_name='agent script', blank=True)),
                ('lead_disposition', models.TextField(null=True, verbose_name='lead disposition', blank=True)),
                ('external_link', jsonfield.fields.JSONField(help_text='enter the list of parameters in Json format, e.g. {"title": ["tab-1", "tab-2"], "url": ["https://duckduckgo.com/", "http://www.newfies-dialer.org/"]}', null=True, verbose_name='additional parameters (JSON)', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('aleg_gateway', models.ForeignKey(related_name=b'A-Leg Gateway', verbose_name='A-Leg gateway', to='dialer_gateway.Gateway', help_text='select outbound gateway')),
                ('content_type', models.ForeignKey(verbose_name='type', to='contenttypes.ContentType')),
                ('dnc', models.ForeignKey(related_name=b'DNC', blank=True, to='dnc.DNC', help_text='do not call list', null=True, verbose_name='DNC')),
                ('phonebook', models.ManyToManyField(to='dialer_contact.Phonebook', null=True, blank=True)),
                ('sms_gateway', models.ForeignKey(related_name=b'campaign_sms_gateway', blank=True, to='sms.Gateway', help_text='select SMS gateway', null=True, verbose_name='sms gateway')),
                ('user', models.ForeignKey(related_name=b'Campaign owner', to=settings.AUTH_USER_MODEL)),
                ('voicemail_audiofile', models.ForeignKey(verbose_name='voicemail audio file', blank=True, to='audiofield.AudioFile', null=True)),
            ],
            options={
                'db_table': 'dialer_campaign',
                'verbose_name': 'campaign',
                'verbose_name_plural': 'campaigns',
                'permissions': (('view_campaign', 'can see campaign'), ('view_dashboard', 'can see campaign dashboard')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_attempt', models.DateTimeField(null=True, verbose_name='last attempt', blank=True)),
                ('count_attempt', models.IntegerField(default=0, null=True, verbose_name='count attempts', blank=True)),
                ('completion_count_attempt', models.IntegerField(default=0, null=True, verbose_name='completion count attempts', blank=True)),
                ('duplicate_contact', models.CharField(max_length=90, verbose_name='contact')),
                ('status', models.IntegerField(default=1, null=True, verbose_name='status', blank=True, choices=[(3, 'ABORT'), (8, 'COMPLETED'), (4, 'FAIL'), (6, 'IN PROCESS'), (7, 'NOT AUTHORIZED'), (2, 'PAUSE'), (1, 'PENDING'), (5, 'SENT')])),
                ('disposition', models.IntegerField(null=True, verbose_name='disposition', blank=True)),
                ('collected_data', models.TextField(help_text='collect user call data', null=True, verbose_name='subscriber response', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('campaign', models.ForeignKey(blank=True, to='dialer_campaign.Campaign', help_text='select campaign', null=True)),
                ('contact', models.ForeignKey(blank=True, to='dialer_contact.Contact', help_text='select contact', null=True)),
            ],
            options={
                'db_table': 'dialer_subscriber',
                'verbose_name': 'subscriber',
                'verbose_name_plural': 'subscribers',
                'permissions': (('view_subscriber', 'can see subscriber'),),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='subscriber',
            unique_together=set([('contact', 'campaign')]),
        ),
    ]