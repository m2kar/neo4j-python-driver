#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2002-2017 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from neo4j.bolt.exceptions import *


class CypherError(Exception):
    """ Raised when the Cypher engine returns an error to the client.
    """

    code = None
    message = None

    def __init__(self, data):
        super(CypherError, self).__init__(data.get("message"))
        for key, value in data.items():
            if not key.startswith("_"):
                setattr(self, key, value)


class SessionError(Exception):
    """ Raised when an error occurs while using a session.
    """


class TransactionError(Exception):
    """ Raised when an error occurs while using a transaction.
    """


class SessionExpired(SessionError):
    """ Raised when no a session is no longer able to fulfil
    its purpose.
    """

    def __init__(self, session, *args, **kwargs):
        self.session = session
        super(SessionExpired, self).__init__(*args, **kwargs)