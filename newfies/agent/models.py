#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from common.language_field import LanguageField
from django_countries import CountryField
from user_profile.models import Manager, Profile_abstract


class AgentProfile(Profile_abstract):
    """This defines extra features for the user

    **Attributes**:

        * ``accountcode`` - Account name.
        * ``address`` -
        * ``city`` -
        * ``state`` -
        * ``address`` -
        * ``country`` -
        * ``zip_code`` -
        * ``phone_no`` -
        * ``fax`` -
        * ``company_name`` -
        * ``company_website`` -
        * ``language`` -
        * ``note`` -

    **Relationships**:

        * ``user`` - Foreign key relationship to the User model.
        * ``userprofile_gateway`` - ManyToMany
        * ``userprofile_voipservergroup`` - ManyToMany
        * ``dialersetting`` - Foreign key relationship to the DialerSetting \
        model.

    **Name of DB table**: user_profile

    """
    is_agent = models.BooleanField(default=True,
        verbose_name=_('Designates whether the user is an agent.'))
    manager = models.ForeignKey(Manager, verbose_name=_("manager"), blank=True, null=True,
        help_text=_("select manager"), related_name="manager")

    class Meta:
        db_table = 'agent_profile'
        verbose_name = _("agent profile")
        verbose_name_plural = _("agent profiles")

    def __unicode__(self):
        return u"%s" % str(self.user)


class Agent(User):
    """Agent"""

    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = _('agent')
        verbose_name_plural = _('agents')

        permissions = (
            ("aegnt", _('can see agent interface')),
        )

    def save(self, **kwargs):
        if not self.pk:
            self.is_staff = 0
            self.is_superuser = 0
        super(Agent, self).save(**kwargs)