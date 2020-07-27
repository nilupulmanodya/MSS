# -*- coding: utf-8 -*-
"""

    mslib.mscolab._tests.test_files_api
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    api integration tests for file based handlers

    This file is part of mss.

    :copyright: Copyright 2019 Shivashis Padhi
    :copyright: Copyright 2019-2020 by the mss team, see AUTHORS.
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import requests
import json
from werkzeug.urls import url_join
from mslib.mscolab.models import User, Change, Project
from mslib._tests.constants import MSCOLAB_URL_TEST
from mslib.mscolab.conf import mscolab_settings
from mslib.mscolab.server import db, APP, initialize_managers
from mslib.mscolab.utils import get_recent_pid


class Test_Files(object):
    def setup(self):
        self.sockets = []
        self.file_message_counter = [0] * 2
        self.undefined_p_id = 123
        self.no_perm_p_id = 2
        self.app = APP
        self.app.config['SQLALCHEMY_DATABASE_URI'] = mscolab_settings.SQLALCHEMY_DB_URI
        self.app.config['MSCOLAB_DATA_DIR'] = mscolab_settings.MSCOLAB_DATA_DIR
        self.app, _, cm, fm = initialize_managers(self.app)
        self.fm = fm
        self.cm = cm
        db.init_app(self.app)
        data = {
            'email': 'a',
            'password': 'a'
        }
        r = requests.post(MSCOLAB_URL_TEST + '/token', data=data)
        self.token = json.loads(r.text)['token']
        with self.app.app_context():
            self.user = User.query.filter_by(id=8).first()

    def test_create_project(self):
        data = {
            "token": self.token,
            "path": "dummy",
            "description": "test description"
        }
        r = requests.post(MSCOLAB_URL_TEST + '/create_project', data=data)
        assert r.text == "True"
        r = requests.post(MSCOLAB_URL_TEST + '/create_project', data=data)
        assert r.text == "False"

    def test_projects(self):
        data = {
            "token": self.token
        }
        r = requests.get(MSCOLAB_URL_TEST + '/projects', data=data)
        json_res = json.loads(r.text)
        assert len(json_res["projects"]) == 4
        data["token"] = "garbage text"
        r = requests.get(MSCOLAB_URL_TEST + '/projects', data=data)
        assert r.text == "False"

    def test_get_project(self):
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
            data = {
                "token": self.token,
                "p_id": p_id
            }
            r = requests.get(MSCOLAB_URL_TEST + '/get_project', data=data)
            assert json.loads(r.text)["content"] == self.fm.get_file(int(p_id), self.user)

    def test_authorized_users(self):
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
        data = {
            "token": self.token,
            "p_id": p_id
        }
        r = requests.get(MSCOLAB_URL_TEST + '/authorized_users', data=data)
        users = json.loads(r.text)["users"]
        assert len(users) == 1
        # for any other random process which doesn't exist it will return empty array
        data["p_id"] = 43
        r = requests.get(MSCOLAB_URL_TEST + '/authorized_users', data=data)
        users = json.loads(r.text)["users"]
        assert len(users) == 0

    def test_get_users_without_permission(self):
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
        data = {
            "token": self.token,
            "p_id": p_id
        }
        res = requests.get(url_join(MSCOLAB_URL_TEST, "users_without_permission"), data=data).json()
        assert res["success"] is True
        data["p_id"] = self.undefined_p_id
        res = requests.get(url_join(MSCOLAB_URL_TEST, "users_without_permission"), data=data).json()
        assert res["success"] is False
        data["p_id"] = self.no_perm_p_id
        res = requests.get(url_join(MSCOLAB_URL_TEST, "users_without_permission"), data=data).json()
        assert res["success"] is False

    def test_get_users_with_permission(self):
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
        data = {
            "token": self.token,
            "p_id": p_id
        }
        res = requests.get(url_join(MSCOLAB_URL_TEST, "users_with_permission"), data=data).json()
        assert res["success"] is True
        data["p_id"] = self.undefined_p_id
        res = requests.get(url_join(MSCOLAB_URL_TEST, "users_with_permission"), data=data).json()
        assert res["success"] is False
        data["p_id"] = self.no_perm_p_id
        res = requests.get(url_join(MSCOLAB_URL_TEST, "users_with_permission"), data=data).json()
        assert res["success"] is False

    def test_add_bulk_permissions(self):
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
        data = {
            "token": self.token,
            "p_id": p_id,
            "selected_userids": json.dumps([12, 13]),
            "selected_access_level": "collaborator"
        }
        res = requests.post(url_join(MSCOLAB_URL_TEST, 'add_bulk_permissions'), data=data).json()
        assert res["success"] is True
        data["p_id"] = self.undefined_p_id
        res = requests.post(url_join(MSCOLAB_URL_TEST, 'add_bulk_permissions'), data=data).json()
        assert res["success"] is False
        data["p_id"] = self.no_perm_p_id
        res = requests.post(url_join(MSCOLAB_URL_TEST, 'add_bulk_permissions'), data=data).json()
        assert res["success"] is False

    def test_modify_bulk_permissions(self):
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
        data = {
            "token": self.token,
            "p_id": p_id,
            "selected_userids": json.dumps([12, 13]),
            "selected_access_level": "viewer"
        }
        r = requests.post(url_join(MSCOLAB_URL_TEST, 'modify_bulk_permissions'), data=data).json()
        assert r["success"] is True
        data["p_id"] = self.undefined_p_id
        r = requests.post(url_join(MSCOLAB_URL_TEST, 'modify_bulk_permissions'), data=data).json()
        assert r["success"] is False
        data["p_id"] = self.no_perm_p_id
        r = requests.post(url_join(MSCOLAB_URL_TEST, 'modify_bulk_permissions'), data=data).json()
        assert r["success"] is False

    def test_delete_bulk_permissions(self):
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
        data = {
            "token": self.token,
            "p_id": p_id,
            "selected_userids": json.dumps([12, 13]),
        }
        r = requests.post(url_join(MSCOLAB_URL_TEST, 'delete_bulk_permissions'), data=data).json()
        assert r["success"] is True
        data["p_id"] = self.undefined_p_id
        r = requests.post(url_join(MSCOLAB_URL_TEST, 'delete_bulk_permissions'), data=data).json()
        assert r["success"] is False
        data["p_id"] = self.no_perm_p_id
        r = requests.post(url_join(MSCOLAB_URL_TEST, 'delete_bulk_permissions'), data=data).json()
        assert r["success"] is False

    def test_import_permissions(self):
        current_p_id = 4
        import_p_id = 1
        data = {
            "token": self.token,
            "current_p_id": current_p_id,
            "import_p_id": import_p_id
        }
        res = requests.post(url_join(MSCOLAB_URL_TEST, 'import_permissions'), data=data).json()
        assert res["success"] is True
        data["import_p_id"] = self.no_perm_p_id
        res = requests.post(url_join(MSCOLAB_URL_TEST, 'import_permissions'), data=data).json()
        assert res["success"] is False
        data["current_p_id"] = self.no_perm_p_id
        res = requests.post(url_join(MSCOLAB_URL_TEST, 'import_permissions'), data=data).json()
        assert res["success"] is False

    def test_update_project(self):
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
        # ToDo handle paths with blank characters here
        data = {
            "token": self.token,
            "p_id": p_id,
            "attribute": "path",
            "value": "a_diff_path"
        }
        r = requests.post(MSCOLAB_URL_TEST + '/update_project', data=data)
        assert r.text == "True"
        # to make sure that path has changed, which is indirectly known by this request
        # getting results properly
        r = requests.get(MSCOLAB_URL_TEST + '/get_project', data=data)
        assert r.text != "False"
        data = {
            "token": self.token,
            "p_id": p_id,
            "attribute": "description",
            "value": "a_diff description"
        }
        r = requests.post(MSCOLAB_URL_TEST + '/update_project', data=data)
        assert r.text == "True"
        with self.app.app_context():
            project = Project.query.filter_by(id=p_id).first()
            assert project.path == "a_diff_path"
            assert project.description == "a_diff description"

    def test_delete_project(self):
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
        data = {
            "token": self.token,
            "p_id": p_id
        }
        r = requests.post(MSCOLAB_URL_TEST + '/delete_project', data=data)
        assert r.text == "True"
        r = requests.post(MSCOLAB_URL_TEST + '/delete_project', data=data)
        assert r.text == "False"

    def test_change(self):
        """
        since file needs to be saved to inflict changes, changes during integration
        tests have to be manually inserted
        """
        with self.app.app_context():
            p_id = get_recent_pid(self.fm, self.user)
            ch = Change(int(p_id), 8, "", "Version1", "some comment")

            db.session.add(ch)
            db.session.commit()
        data = {
            "token": self.token,
            "p_id": p_id
        }
        # test 'get all changes' request
        r = requests.get(MSCOLAB_URL_TEST + '/get_all_changes', data=data)
        changes = json.loads(r.text)["changes"]
        assert len(changes) == 1
        assert changes[0]["comment"] == "some comment"

        data = {
            "token": self.token,
            "ch_id": changes[0]["id"]
        }
        # test 'get change content' request
        url = url_join(MSCOLAB_URL_TEST, 'get_change_content')
        r = requests.post(url, data=data)
        # TODO: FIX THIS TEST
        change_content = json.loads(r.text)["content"]
        assert ["content"] == "some content"

        data["p_id"] = 123
        data["ch_id"] = 123
        # test unauthorized requests
        r = requests.get(MSCOLAB_URL_TEST + '/get_changes', data=data)
        assert r.text == "False"
        r = requests.get(MSCOLAB_URL_TEST + '/get_change_id', data=data)
        assert r.text == "False"
        with self.app.app_context():
            Change.query.filter_by(content="some content").delete()
            db.session.commit()

    def teardown(self):
        for socket in self.sockets:
            socket.disconnect()
