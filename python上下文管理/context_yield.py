#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
import contextlib

class Pipeline(object):
    def _publish(self):
        print "publish the data"

    def _flush(self):
        print "flush the mem"

    @contextlib.contextmanager
    def publisher(self):
        try:
            yield self._publish()
        finally:
            self._flush()

    def execute(self):
        print "exec code"

pipeline = Pipeline()
with pipeline.publisher() as publisher:
    pipeline.execute()