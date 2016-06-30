#!/usr/bin/env python
# -*- cooding: utf-8 -*-



import unittest

from base import Test
from tests import test_cfg
from view import *

container_serial = None

class TestInstance(Test):


    def test_ins_1_create_success(self):
        req = dict(
            container_name=test_cfg.INSTANCE_NAME_TEST,
            image_id=test_cfg.INSTANCE_IMAGE_TEST,
            user_name=test_cfg.USER_NAME_TEST
        )
        response = self.app.post('/create_ins', data = json.dumps(req), follow_redirects=True)
        res_dict = json.loads(response.data)
        self.assertEquals(res_dict['code'], 'ok')

    # Container name occupied by others
    def test_ins_2_create_failed(self):
        req = dict(
            container_name=test_cfg.INSTANCE_NAME_TEST,
            image_id=test_cfg.INSTANCE_IMAGE_TEST,
            user_name=test_cfg.USER_NAME_TEST
        )
        response = self.app.post('/create_ins', data=json.dumps(req), follow_redirects=True)
        res_dict = json.loads(response.data)
        self.assertEquals(res_dict['message'], 'container name occupied.')

    def test_ins_3_stop_success(self):
        container_serial = self.get_container_serial_by_name(test_cfg.INSTANCE_NAME_TEST)
        req = dict(
            container_serial=container_serial,
            user_name=test_cfg.USER_NAME_TEST
        )
        response = self.app.post('/stop_ins', data=json.dumps(req), follow_redirects=True)
        res_dict = json.loads(response.data)
        self.assertEquals(res_dict['code'], 'ok')

    # Container is not exist
    def test_ins_4_stop_failed(self):
        container_serial = self.get_random_string()
        req = dict(
            container_serial=container_serial,
            user_name=test_cfg.USER_NAME_TEST
        )
        response = self.app.post('/stop_ins', data=json.dumps(req), follow_redirects=True)
        res_dict = json.loads(response.data)
        self.assertEquals(res_dict['message'], 'container not exist')

    def test_ins_5_restart_success(self):
        container_serial = self.get_container_serial_by_name(test_cfg.INSTANCE_NAME_TEST)
        req = dict(
            container_serial=container_serial,
            user_name=test_cfg.USER_NAME_TEST
        )
        response = self.app.post('/restart_ins', data=json.dumps(req), follow_redirects=True)
        res_dict = json.loads(response.data)
        self.assertEquals(res_dict['code'], 'ok')

    # Container is not exist
    def test_ins_6_restart_failed(self):
        container_serial = self.get_random_string()
        req = dict(
            container_serial=container_serial,
            user_name=test_cfg.USER_NAME_TEST
        )
        response = self.app.post('/restart_ins', data=json.dumps(req), follow_redirects=True)
        res_dict = json.loads(response.data)
        self.assertEquals(res_dict['message'], 'container not exist')

    def test_ins_7_remove_success(self):
        container_serial = self.get_container_serial_by_name(test_cfg.INSTANCE_NAME_TEST)
        req = dict(
            container_serial=container_serial,
            user_name=test_cfg.USER_NAME_TEST
        )
        response = self.app.post('/remove_ins', data=json.dumps(req), follow_redirects=True)
        res_dict = json.loads(response.data)
        self.assertEquals(res_dict['code'], 'ok')

    def test_ins_8_remove_failed(self):
        container_serial = self.get_random_string()
        req = dict(
            container_serial=container_serial,
            user_name=test_cfg.USER_NAME_TEST
        )
        response = self.app.post('/remove_ins', data=json.dumps(req), follow_redirects=True)
        res_dict = json.loads(response.data)
        self.assertEquals(res_dict['message'], 'container not exist')

    def test_ins_9_clear(self):
        self.clear_instances()
        self.clear_users()
        self.clear_log_file()


if __name__ == '__main__':
    unittest.main()
