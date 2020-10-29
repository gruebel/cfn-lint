"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import logging
import test.fixtures.schemas
from jsonschema import validate
from test.testlib.testcase import BaseTestCase
import cfnlint.helpers


LOGGER = logging.getLogger('cfnlint.maintenance')
LOGGER.addHandler(logging.NullHandler())


class TestRequiredBasedOnValueSpec(BaseTestCase):


    def validate_additional_specs_schema(self):
        spec = cfnlint.helpers.load_resource(cfnlint.data.AdditionalSpecs, 'RequiredBasedOnValue.json')
        schema = cfnlint.helpers.load_resource(test.fixtures.schemas, 'RequiredBasedOnValue.json')
        validate(spec, schema)
