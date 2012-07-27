#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from django.contrib.auth.models import User
from common.utils import BaseAuthenticatedClient
from survey.models import SurveyApp, SurveyQuestion,\
    SurveyResponse, SurveyCampaignResult
import nose.tools as nt


class SurveyAdminView(BaseAuthenticatedClient):
    """Test Function to check Survey, SurveyQuestion,
       SurveyResponse Admin pages
    """

    def test_admin_surveyapp_view_list(self):
        """Test Function to check admin surveyapp list"""
        response = self.client.get('/admin/survey/surveyapp/')
        self.failUnlessEqual(response.status_code, 200)

    def test_admin_surveyapp_view_add(self):
        """Test Function to check admin surveyapp add"""
        response = self.client.get('/admin/survey/surveyapp/add/')
        self.failUnlessEqual(response.status_code, 200)

    def test_admin_surveyquestion_view_list(self):
        """Test Function to check admin surveyquestion list"""
        response = self.client.get('/admin/survey/surveyquestion/')
        self.failUnlessEqual(response.status_code, 200)

    def test_admin_surveyquestion_view_add(self):
        """Test Function to check admin surveyquestion add"""
        response = self.client.get('/admin/survey/surveyquestion/add/')
        self.failUnlessEqual(response.status_code, 200)

    def test_admin_surveyresponse_view_list(self):
        """Test Function to check admin surveyresponse list"""
        response = self.client.get('/admin/survey/surveyresponse/')
        self.failUnlessEqual(response.status_code, 200)

    def test_admin_surveyresponse_view_add(self):
        """Test Function to check admin surveyresponse add"""
        response = self.client.get('/admin/survey/surveyresponse/add/')
        self.failUnlessEqual(response.status_code, 200)

    def test_admin_surveycampaignresult_view_list(self):
        """Test Function to check admin surveycampaignresult list"""
        response = self.client.get('/admin/survey/surveycampaignresult/')
        self.failUnlessEqual(response.status_code, 200)

    def test_admin_surveycampaignresult_view_add(self):
        """Test Function to check admin surveycampaignresult add"""
        response = self.client.get('/admin/survey/surveycampaignresult/add/')
        self.failUnlessEqual(response.status_code, 200)


class SurveyCustomerView(BaseAuthenticatedClient):
    """Test Function to check Survey, SurveyQuestion,
       SurveyResponse Customer pages
    """

    fixtures = ['survey.json', 'survey_question', 'survey_response']

    def test_survey_view(self):
        """Test Function survey view"""
        response = self.client.get('/survey/')
        self.assertEqual(response.status_code, 200)

    def test_survey_view_list(self):
        """Test Function survey view list"""
        response = self.client.get('/survey/')
        self.assertTemplateUsed(response, 'frontend/survey/survey_list.html')

    def test_survey_view_add(self):
        """Test Function survey view add"""
        response = self.client.get('/survey/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/survey/survey_change.html')

    def test_survey_view_get(self):
        """Test Function survey view get"""
        response = self.client.get('/survey/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/survey/survey_change.html')

    def test_survey_view_report(self):
        """Test Function survey view report"""
        response = self.client.get('/survey_report/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/survey/survey_report.html')


class SurveyModel(object):
    """Test Survey, SurveyQuestion, SurveyResponse Model"""

    def setup(self):
        self.user = User.objects.get(username='admin')

        # SurveyApp model
        self.survey = SurveyApp(
            name='test_survey',
            user=self.user,
        )
        self.survey.save()

        # SurveyQuestion model
        self.survey_question = SurveyQuestion(
            question='test_question',
            user=self.user,
            surveyapp=self.survey,
        )
        self.survey_question.save()

        # SurveyResponse model
        self.survey_response = SurveyResponse(
            key='5',
            keyvalue='egg',
            surveyquestion=self.survey_question,
        )
        self.survey_response.save()

        # SurveyCampaignResult model
        self.survey_result = SurveyCampaignResult(
            surveyapp=self.survey,
            question='test_question',
            response='5',
            callrequest_id=1,
        )
        self.survey_result.save()

    def test_name(self):
        nt.assert_equal(self.survey.name, "test_survey")
        nt.assert_equal(self.survey_question.question, "test_question")
        nt.assert_equal(self.survey_response.key, "5")
        nt.assert_equal(self.survey_result.surveyapp, self.survey)

    def teardown(self):
        self.survey.delete()
        self.survey_question.delete()
        self.survey_response.delete()
        self.survey_result.delete()
