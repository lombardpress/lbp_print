import os

from lbp_print.core import RemoteResource, UrlResource


class TestUrlResource:

    url = "https://raw.githubusercontent.com/scta-texts/da-49/master/da-49-l1q1/da-49-l1q1.xml"
    res = UrlResource(url)

    def test_url_resource_identified(self):
        assert self.res.url == self.url

    def test_successfull_download_to_file(self):
        assert self.res.file is not None
        assert os.path.exists(self.res.file)

    def test_identified_schema_info(self):
        assert self.schema_info.version is not None


class TestRemoteResource:

    trans = RemoteResource("da-49-l1q1")

    def test_remote_transcription_object(self):
        assert (
            self.trans.transcription_object.to_s()
            == "http://scta.info/resource/da-49-l1q1/critical/transcription"
        )

    def test_remote_file_download(self):
        assert self.trans.file is not None
