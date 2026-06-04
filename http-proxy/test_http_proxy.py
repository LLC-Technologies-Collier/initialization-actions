import pkg_resources
from absl.testing import absltest
from absl.testing import parameterized

from integration_tests.dataproc_test_case import DataprocTestCase


class HttpProxyTestCase(DataprocTestCase):
  COMPONENT = 'http-proxy'
  INIT_ACTIONS = ['http-proxy/http-proxy.sh']

  @parameterized.parameters(
      ("SINGLE",),
  )
  def test_http_proxy_skip(self, configuration):
    # Test that it exits cleanly when no proxy metadata is provided
    self.createCluster(
        configuration,
        self.INIT_ACTIONS,
        timeout_in_minutes=10)


if __name__ == '__main__':
  absltest.main()
