
from qgate.uc.ucsetup import UCSetup
from qgate.uc.ucoutput import UCOutput
#from qgate.solution import Solution
from dotenv import dotenv_values
import mlrun
import mlrun.feature_store as fstore
from mlrun.features import Feature
from mlrun.data_types.data_types import spark_to_value_type
from mlrun.datastore import ParquetTarget
import json
import glob
import os
import pandas as pd
import shutil


class UCBase:
    """
    Base class for all use cases
    """

    def __init__(self, sln, output, name):
        self._sln=sln
        self._output=output
        self._name=name

    @property
    def sln(self):
        return self._sln

    @property
    def output(self):
        return self._output

    @property
    def desc(self):
        raise NotImplemented()

    @property
    def name(self):
        return self._name

    def exec(self):
        raise NotImplemented()

    def log(self, *args, **kwargs):
        self.output.log("", *args, **kwargs)

    def logh(self, *args, **kwargs):
        self.output.log(self.name + ": " + self.desc, *args, **kwargs)

    def logln(self, *args, **kwargs):
        self.output.logln("", *args, **kwargs)

    def loghln(self, *args, **kwargs):
        self.output.logln(self.name + ": " + self.desc, *args, **kwargs)

